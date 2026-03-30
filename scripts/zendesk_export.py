#!/usr/bin/env python3
"""
Zendesk Export — Tickets destinataires Shopopop
================================================
Usage:
  python zendesk_export.py                         Export interactif sur période donnée (CSV)
  python zendesk_export.py --discover              Analyse des tickets exemples pour identifier le filtre
  python zendesk_export.py --check-ids 123,456     Vérifie si ces tickets sont destinataires et explique pourquoi ils seraient absents
  python zendesk_export.py --history               Affiche les périodes déjà exportées

Note : les tickets destinataires sont identifiables à partir du 18/03/2026.
Stratégie d'export : incremental cursor export (plus fiable que search/export pour les gros volumes).
"""

import os
import sys
import csv
import json
import time
import argparse
import requests
from datetime import datetime, date
from pathlib import Path

# ---------------------------------------------------------------------------
# Chargement des variables d'environnement (.env)
# ---------------------------------------------------------------------------
def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if not env_path.exists():
        print(f"⚠️  Fichier .env introuvable : {env_path}")
        print("   Copie .env.example en .env et renseigne tes credentials.")
        sys.exit(1)
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

load_env()

SUBDOMAIN    = os.environ.get("ZENDESK_SUBDOMAIN", "")
EMAIL        = os.environ.get("ZENDESK_EMAIL", "")
API_TOKEN    = os.environ.get("ZENDESK_API_TOKEN", "")
EXAMPLE_IDS  = [i.strip() for i in os.environ.get("ZENDESK_EXAMPLE_IDS", "").split(",") if i.strip()]
DEST_FILTER  = os.environ.get("ZENDESK_DESTINATAIRE_FILTER", "").strip()  # ex: tags:destinataire

if not all([SUBDOMAIN, EMAIL, API_TOKEN]):
    print("❌  Credentials manquants dans .env (ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, ZENDESK_API_TOKEN)")
    sys.exit(1)

BASE_URL      = f"https://{SUBDOMAIN}.zendesk.com/api/v2"
AUTH          = (f"{EMAIL}/token", API_TOKEN)
EARLIEST_DATE = date(2026, 3, 18)
DATA_DIR      = Path(__file__).parent.parent / "data"
HISTORY_FILE  = DATA_DIR / "zendesk_fetch_history.json"

# Extraction du tag cible depuis ZENDESK_DESTINATAIRE_FILTER (ex: "tags:destinataire" → "destinataire")
def get_target_tag():
    if ":" in DEST_FILTER:
        return DEST_FILTER.split(":", 1)[1].strip()
    return DEST_FILTER.strip()

# ---------------------------------------------------------------------------
# Utilitaire HTTP avec gestion du rate limit (429)
# ---------------------------------------------------------------------------
def api_get(url, params=None, max_retries=5):
    for attempt in range(max_retries):
        resp = requests.get(url, auth=AUTH, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 10))
            print(f"   ⏳ Rate limit — attente {retry_after}s (tentative {attempt+1}/{max_retries})")
            time.sleep(retry_after)
        elif resp.status_code == 404:
            return None
        else:
            print(f"   ❌ Erreur {resp.status_code} : {resp.text[:300]}")
            resp.raise_for_status()
    raise RuntimeError(f"Rate limit persistant après {max_retries} tentatives")

# ---------------------------------------------------------------------------
# Historique des exports
# ---------------------------------------------------------------------------
def load_history():
    if not HISTORY_FILE.exists():
        return []
    with open(HISTORY_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_history(start: date, end: date, filename: str, count: int):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    history = load_history()
    history.append({
        "start": str(start), "end": str(end),
        "file": filename, "tickets": count,
        "fetched_at": str(date.today()),
    })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def find_overlaps(start: date, end: date, history: list):
    return [e for e in history
            if date.fromisoformat(e["start"]) <= end and date.fromisoformat(e["end"]) >= start]

def print_history(history):
    if not history:
        print("  (aucun export enregistré)")
        return
    print(f"  {'Période':<25} {'Tickets':>8}  {'Fichier':<50}  Exporté le")
    print("  " + "-" * 100)
    for e in history:
        print(f"  {e['start']} → {e['end']:<14} {e['tickets']:>8}  {e['file']:<50}  {e['fetched_at']}")

# ---------------------------------------------------------------------------
# MODE DISCOVER — analyser des tickets exemples
# ---------------------------------------------------------------------------
def discover():
    if not EXAMPLE_IDS:
        print("❌  Aucun ID exemple dans .env (ZENDESK_EXAMPLE_IDS=id1,id2,...)")
        sys.exit(1)
    print(f"\n🔍 Analyse de {len(EXAMPLE_IDS)} ticket(s) exemple(s)...\n")
    all_tags, all_groups, all_forms, all_channels = {}, {}, {}, {}
    for ticket_id in EXAMPLE_IDS:
        data = api_get(f"{BASE_URL}/tickets/{ticket_id}.json")
        if not data:
            print(f"   ⚠️  Ticket {ticket_id} introuvable")
            continue
        t = data["ticket"]
        print(f"  Ticket #{ticket_id} — {t.get('subject', '(sans sujet)')}")
        print(f"    Statut : {t.get('status')}  |  Canal : {t.get('channel')}  |  Groupe : {t.get('group_id')}  |  Form : {t.get('ticket_form_id')}")
        print(f"    Tags   : {', '.join(t.get('tags', []))}\n")
        for tag in t.get("tags", []):
            all_tags[tag] = all_tags.get(tag, 0) + 1
        for k, d in [(t.get("group_id"), all_groups), (t.get("ticket_form_id"), all_forms), (t.get("channel"), all_channels)]:
            if k: d[k] = d.get(k, 0) + 1
    n = len(EXAMPLE_IDS)
    print("=" * 60)
    print("📊 SYNTHÈSE\nTags (fréquence) :")
    for tag, count in sorted(all_tags.items(), key=lambda x: -x[1]):
        print(f"  {'█' * count} ({count}/{n})  {tag}")
    print(f"\nGroupes : {dict(all_groups)} | Formulaires : {dict(all_forms)} | Canaux : {dict(all_channels)}")
    print("\n👉 Renseigne ZENDESK_DESTINATAIRE_FILTER dans .env (ex: ZENDESK_DESTINATAIRE_FILTER=tags:destinataire)")

# ---------------------------------------------------------------------------
# MODE CHECK-IDS — diagnostiquer des tickets potentiellement manquants
# ---------------------------------------------------------------------------
def check_ids(ids: list):
    target_tag = get_target_tag()
    print(f"\n🔎 Vérification de {len(ids)} ticket(s) — tag cible : '{target_tag}'\n")
    for ticket_id in ids:
        data = api_get(f"{BASE_URL}/tickets/{ticket_id}.json")
        if not data:
            print(f"  ❌ #{ticket_id} — INTROUVABLE (supprimé ou inaccessible)")
            continue
        t = data["ticket"]
        tags       = t.get("tags", [])
        created    = t.get("created_at", "")[:10]
        has_tag    = target_tag in tags
        in_range   = created >= str(EARLIEST_DATE)
        status_tag = "✅" if has_tag else "❌"
        status_date = "✅" if in_range else f"❌ (avant {EARLIEST_DATE})"
        reasons = []
        if not has_tag:
            reasons.append(f"tag '{target_tag}' absent (tags présents : {', '.join(tags) or 'aucun'})")
        if not in_range:
            reasons.append(f"créé le {created}, avant la date minimale {EARLIEST_DATE}")
        if has_tag and in_range:
            print(f"  ✅ #{ticket_id} — devrait être dans l'export (créé {created}, tag ok)")
        else:
            print(f"  ⚠️  #{ticket_id} — absent car : {' | '.join(reasons)}")

# ---------------------------------------------------------------------------
# MODE EXPORT — incremental cursor export + filtre local par tag
# ---------------------------------------------------------------------------
def fetch_search_export(start_date: date, end_date: date):
    """
    Utilise l'API Search Export (cursor-based) — accessible sans droits admin.
    Filtre directement par tag et période via la query Zendesk.
    """
    if not DEST_FILTER:
        print("❌  ZENDESK_DESTINATAIRE_FILTER non renseigné dans .env")
        print("   Lance d'abord : python zendesk_export.py --discover")
        sys.exit(1)

    # Validation du format du filtre (chaque token doit avoir un préfixe connu)
    valid_prefixes = ("tags:", "tag:", "group_id:", "ticket_form_id:")
    tokens = DEST_FILTER.split()
    invalid = [t for t in tokens if not any(t.startswith(p) for p in valid_prefixes)]
    if invalid:
        print(f"❌  Token(s) non reconnu(s) dans ZENDESK_DESTINATAIRE_FILTER : {', '.join(invalid)}")
        print("   Préfixes valides : tags:  tag:  group_id:  ticket_form_id:")
        print("   Exemple multi-critères : group_id:12345 ticket_form_id:67890")
        sys.exit(1)

    query = f"type:ticket created>={start_date} created<={end_date} {DEST_FILTER}"
    print(f"\n🔎 Requête : {query}\n")

    tickets  = []
    url      = f"{BASE_URL}/search/export.json"
    params   = {"query": query, "filter[type]": "ticket", "page[size]": 100}
    page_num = 1

    while url:
        print(f"   Page {page_num} ({len(tickets)} tickets collectés)...", end="\r")
        data = api_get(url, params=params if page_num == 1 else None)
        if data is None:
            break
        tickets.extend(data.get("results", []))
        meta   = data.get("meta", {})
        links  = data.get("links", {})
        url    = links.get("next") if meta.get("has_more") else None
        params = None
        page_num += 1

    print(f"   {len(tickets)} tickets trouvés ({start_date} → {end_date}).          ")
    return tickets

def flatten_ticket(t):
    return {
        "id":           t.get("id"),
        "created_at":   t.get("created_at", "")[:10],
        "updated_at":   t.get("updated_at", "")[:10],
        "status":       t.get("status"),
        "subject":      t.get("subject", ""),
        "channel":      t.get("via", {}).get("channel", ""),
        "tags":         "|".join(t.get("tags", [])),
        "group_id":     t.get("group_id"),
        "form_id":      t.get("ticket_form_id"),
        "requester_id": t.get("requester_id"),
    }

def ask_date(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return datetime.strptime(val, "%Y-%m-%d").date()
        except ValueError:
            print("   Format attendu : YYYY-MM-DD")

def export(start_date: date, end_date: date):
    if start_date < EARLIEST_DATE:
        print(f"⚠️  Date de début ajustée à {EARLIEST_DATE} (première date disponible).")
        start_date = EARLIEST_DATE

    history  = load_history()
    overlaps = find_overlaps(start_date, end_date, history)
    if overlaps:
        print("\n⚠️  Chevauchement avec des exports déjà réalisés :")
        print_history(overlaps)
        if input("\nContinuer quand même ? [o/N] : ").strip().lower() != "o":
            print("Export annulé.")
            return

    tickets = fetch_search_export(start_date, end_date)
    if not tickets:
        print("ℹ️  Aucun ticket trouvé pour cette période.")
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    filename    = f"zendesk_destinataires_{start_date}_{end_date}.csv"
    output_path = DATA_DIR / filename
    rows        = [flatten_ticket(t) for t in tickets]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    save_history(start_date, end_date, filename, len(rows))
    print(f"\n✅ Export terminé : {output_path}")
    print(f"   {len(rows)} tickets exportés ({start_date} → {end_date})")

# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Zendesk Export — tickets destinataires")
    parser.add_argument("--discover",   action="store_true", help="Analyser les tickets exemples")
    parser.add_argument("--history",    action="store_true", help="Afficher les exports déjà réalisés")
    parser.add_argument("--check-ids",  type=str, metavar="ID1,ID2,...",
                        help="Vérifier pourquoi des tickets seraient absents de l'export")
    args = parser.parse_args()

    if args.discover:
        discover(); return

    if args.history:
        print("\n📋 Historique des exports Zendesk :\n")
        print_history(load_history()); print(); return

    if args.check_ids:
        ids = [i.strip() for i in args.check_ids.split(",") if i.strip()]
        check_ids(ids); return

    print("=== Zendesk Export — Tickets destinataires ===")
    history = load_history()
    if history:
        print(f"\n📋 {len(history)} export(s) déjà réalisé(s) :")
        print_history(history)
    print()

    start = ask_date("Période de début (YYYY-MM-DD) : ")
    end   = ask_date("Période de fin   (YYYY-MM-DD) : ")
    if end < start:
        print("❌  La date de fin doit être après la date de début.")
        sys.exit(1)
    export(start, end)

if __name__ == "__main__":
    main()
