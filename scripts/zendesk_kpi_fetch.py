#!/usr/bin/env python3
"""
Zendesk KPI Fetch — Volumes mensuels tickets destinataires Shopopop
====================================================================
Usage:
  python zendesk_kpi_fetch.py                  Fetch incrémental + cache → JSON stdout
  python zendesk_kpi_fetch.py --explore [N]    Explore les N derniers jours pour identifier les channels (défaut: 30)
  python zendesk_kpi_fetch.py --json-file PATH Sauvegarde le JSON dans un fichier plutôt que stdout
  python zendesk_kpi_fetch.py --cache-status   Affiche l'état du cache (mois couverts, date de fetch)
  python zendesk_kpi_fetch.py --force-month MM Reforce le fetch d'un mois spécifique (ex: 2026-03)

Stratégie cache :
  - Résultats stockés dans data/zendesk_kpi_cache.json
  - Les mois PASSÉS (terminés) ne sont fetchés qu'une seule fois
  - Le mois EN COURS est toujours re-fetché (données partielles)
  - Seuls les mois manquants entre le dernier mois caché et aujourd'hui sont requêtés

Sorties JSON :
  {
    "generated_at": "2026-04-23",
    "months": ["2026-03", "2026-04"],
    "inbound": [123, 45],
    "outbound": [67, 12],
    "total": [190, 57]
  }

Règle de classification :
  - OUTBOUND : via.channel contient "outbound" (ex: outbound_call, outbound_email)
  - INBOUND  : tout le reste (email, web, api, voice, chat, mobile_sdk…)
"""

import os
import sys
import json
import time
import argparse
import requests
from datetime import datetime, date, timedelta
from calendar import monthrange
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Chargement .env
# ---------------------------------------------------------------------------
def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if not env_path.exists():
        print(f"⚠️  Fichier .env introuvable : {env_path}", file=sys.stderr)
        sys.exit(1)
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

load_env()

SUBDOMAIN   = os.environ.get("ZENDESK_SUBDOMAIN", "")
EMAIL       = os.environ.get("ZENDESK_EMAIL", "")
API_TOKEN   = os.environ.get("ZENDESK_API_TOKEN", "")
DEST_FILTER = os.environ.get("ZENDESK_DESTINATAIRE_FILTER", "").strip()

if not all([SUBDOMAIN, EMAIL, API_TOKEN]):
    print("❌  Credentials manquants dans .env", file=sys.stderr)
    sys.exit(1)

BASE_URL      = f"https://{SUBDOMAIN}.zendesk.com/api/v2"
AUTH          = (f"{EMAIL}/token", API_TOKEN)
EARLIEST_DATE = date(2026, 3, 18)  # Première date avec tickets destinataires identifiables
DATA_DIR      = Path(__file__).parent.parent / "data"
CACHE_FILE    = DATA_DIR / "zendesk_kpi_cache.json"

# ---------------------------------------------------------------------------
# HTTP helper
# ---------------------------------------------------------------------------
def api_get(url, params=None, max_retries=5):
    for attempt in range(max_retries):
        resp = requests.get(url, auth=AUTH, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 10))
            print(f"   ⏳ Rate limit — attente {retry_after}s", file=sys.stderr)
            time.sleep(retry_after)
        elif resp.status_code == 404:
            return None
        else:
            print(f"   ❌ Erreur {resp.status_code} : {resp.text[:300]}", file=sys.stderr)
            resp.raise_for_status()
    raise RuntimeError(f"Rate limit persistant après {max_retries} tentatives")

# ---------------------------------------------------------------------------
# Gestion du cache
# ---------------------------------------------------------------------------
def load_cache() -> dict:
    """
    Structure du cache :
    {
      "months": {
        "2026-03": {
          "inbound": 123, "outbound": 67,
          "fetched_at": "2026-04-01", "complete": true
        },
        "2026-04": { ... "complete": false }   ← mois en cours, à re-fetcher
      }
    }
    """
    if not CACHE_FILE.exists():
        return {"months": {}}
    with open(CACHE_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_cache(cache: dict):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def month_is_complete(month_str: str) -> bool:
    """Un mois est 'complet' s'il est entièrement passé (le 1er du mois suivant est ≤ aujourd'hui)."""
    year, month = int(month_str[:4]), int(month_str[5:7])
    if month == 12:
        first_of_next = date(year + 1, 1, 1)
    else:
        first_of_next = date(year, month + 1, 1)
    return first_of_next <= date.today()

def month_date_range(month_str: str) -> tuple:
    """Retourne (start_date, end_date) pour un mois donné au format YYYY-MM."""
    year, month = int(month_str[:4]), int(month_str[5:7])
    start = date(year, month, 1)
    # Clamp au EARLIEST_DATE si le mois commence avant
    if start < EARLIEST_DATE:
        start = EARLIEST_DATE
    end = date(year, month, monthrange(year, month)[1])
    # Ne pas aller au-delà d'aujourd'hui
    end = min(end, date.today())
    return start, end

def months_to_fetch(cache: dict) -> list:
    """
    Retourne la liste des mois YYYY-MM à requêter :
    - Mois manquants entre EARLIEST_DATE et aujourd'hui
    - Mois présents en cache mais marqués 'complete: false' (mois en cours)
    """
    today = date.today()
    current_month = today.strftime("%Y-%m")
    start_month   = EARLIEST_DATE.strftime("%Y-%m")

    # Générer tous les mois entre start_month et current_month
    all_months = []
    y, m = int(start_month[:4]), int(start_month[5:7])
    while True:
        s = f"{y:04d}-{m:02d}"
        all_months.append(s)
        if s == current_month:
            break
        m += 1
        if m > 12:
            m = 1
            y += 1

    to_fetch = []
    cached   = cache.get("months", {})
    for month in all_months:
        if month not in cached:
            to_fetch.append(month)
        elif not cached[month].get("complete", False):
            # Mois en cours ou marqué incomplet → re-fetcher
            to_fetch.append(month)

    return to_fetch

def print_cache_status(cache: dict):
    cached = cache.get("months", {})
    if not cached:
        print("  (cache vide — aucun mois enregistré)", file=sys.stderr)
        return
    print(f"  {'Mois':<10}  {'Entrants':>9}  {'Sortants':>9}  {'Total':>7}  {'Complet':>8}  Fetché le",
          file=sys.stderr)
    print("  " + "-" * 70, file=sys.stderr)
    for month in sorted(cached.keys()):
        d = cached[month]
        total    = d.get("inbound", 0) + d.get("outbound", 0)
        complete = "✅" if d.get("complete") else "🔄 en cours"
        print(f"  {month:<10}  {d.get('inbound',0):>9}  {d.get('outbound',0):>9}  "
              f"{total:>7}  {complete:>8}  {d.get('fetched_at','?')}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Fetch tickets via Search Export (cursor-based)
# ---------------------------------------------------------------------------
def fetch_tickets(start_date: date, end_date: date, verbose=True) -> list:
    if not DEST_FILTER:
        print("❌  ZENDESK_DESTINATAIRE_FILTER non renseigné dans .env", file=sys.stderr)
        sys.exit(1)

    query    = f"type:ticket created>={start_date} created<={end_date} {DEST_FILTER}"
    if verbose:
        print(f"🔎 Requête : {query}", file=sys.stderr)

    tickets  = []
    url      = f"{BASE_URL}/search/export.json"
    params   = {"query": query, "filter[type]": "ticket", "page[size]": 100}
    page_num = 1

    while url:
        if verbose:
            print(f"   Page {page_num} ({len(tickets)} tickets)...", end="\r", file=sys.stderr)
        data = api_get(url, params=params if page_num == 1 else None)
        if data is None:
            break
        tickets.extend(data.get("results", []))
        meta   = data.get("meta", {})
        links  = data.get("links", {})
        url    = links.get("next") if meta.get("has_more") else None
        params = None
        page_num += 1

    if verbose:
        print(f"   {len(tickets)} tickets ({start_date} → {end_date}).          ", file=sys.stderr)
    return tickets

# ---------------------------------------------------------------------------
# Classification inbound / outbound
# ---------------------------------------------------------------------------
def classify_channel(ticket) -> str:
    """Retourne 'outbound' si le canal contient 'outbound', sinon 'inbound'."""
    channel = ticket.get("via", {}).get("channel", "") or ""
    if "outbound" in channel.lower():
        return "outbound"
    return "inbound"

# ---------------------------------------------------------------------------
# MODE EXPLORE — distribution des channels sur les N derniers jours
# ---------------------------------------------------------------------------
def explore(days: int):
    end_date   = date.today()
    start_date = max(end_date - timedelta(days=days), EARLIEST_DATE)
    print(f"\n🔍 Exploration des channels ({start_date} → {end_date})…\n", file=sys.stderr)

    tickets = fetch_tickets(start_date, end_date, verbose=True)
    if not tickets:
        print("ℹ️  Aucun ticket trouvé pour cette période.", file=sys.stderr)
        return

    channel_counts = defaultdict(int)
    for t in tickets:
        channel = t.get("via", {}).get("channel", "(vide)") or "(vide)"
        channel_counts[channel] += 1

    total = len(tickets)
    print(f"\n📊 Distribution des channels ({total} tickets) :\n", file=sys.stderr)
    print(f"  {'Channel':<30}  {'Nb':>6}  {'%':>6}  Classifié", file=sys.stderr)
    print("  " + "-" * 65, file=sys.stderr)
    for channel, count in sorted(channel_counts.items(), key=lambda x: -x[1]):
        classification = "outbound" if "outbound" in channel.lower() else "inbound"
        pct = count / total * 100
        print(f"  {channel:<30}  {count:>6}  {pct:>5.1f}%  → {classification}", file=sys.stderr)

    print(f"\n👉 Si la classification est incorrecte, modifie classify_channel() dans ce script.",
          file=sys.stderr)
    print(f"   Note : ces données NE sont PAS mises en cache (mode exploration).", file=sys.stderr)

    result = {
        "mode": "explore",
        "period": f"{start_date} → {end_date}",
        "total": total,
        "channels_raw": dict(channel_counts),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

# ---------------------------------------------------------------------------
# MODE PRINCIPAL — fetch incrémental avec cache
# ---------------------------------------------------------------------------
def fetch_kpis(json_file: str = None, force_month: str = None):
    cache = load_cache()

    # Si --force-month, invalider ce mois dans le cache
    if force_month:
        if force_month in cache.get("months", {}):
            del cache["months"][force_month]
            print(f"🔄 Mois {force_month} invalidé dans le cache.", file=sys.stderr)

    to_fetch = months_to_fetch(cache)

    if to_fetch:
        print(f"📥 Mois à fetcher : {', '.join(to_fetch)}", file=sys.stderr)
        for month in to_fetch:
            start, end = month_date_range(month)
            if start > end:
                print(f"   ⏭  {month} — aucune date valide (avant EARLIEST_DATE ou dans le futur)",
                      file=sys.stderr)
                continue
            tickets = fetch_tickets(start, end, verbose=True)

            # Agréger
            counts = {"inbound": 0, "outbound": 0}
            for t in tickets:
                counts[classify_channel(t)] += 1

            cache.setdefault("months", {})[month] = {
                "inbound":    counts["inbound"],
                "outbound":   counts["outbound"],
                "fetched_at": str(date.today()),
                "complete":   month_is_complete(month),
            }
            status = "✅ complet" if month_is_complete(month) else "🔄 partiel (mois en cours)"
            print(f"   {month} — entrants: {counts['inbound']}, sortants: {counts['outbound']} [{status}]",
                  file=sys.stderr)

        save_cache(cache)
        print(f"💾 Cache mis à jour : {CACHE_FILE}", file=sys.stderr)
    else:
        print("✅ Cache à jour — aucun fetch nécessaire.", file=sys.stderr)

    # Construire le résultat depuis le cache complet
    months_cached = sorted(cache.get("months", {}).keys())
    result = {
        "generated_at": str(date.today()),
        "earliest_date": str(EARLIEST_DATE),
        "months":   months_cached,
        "inbound":  [cache["months"][m]["inbound"]  for m in months_cached],
        "outbound": [cache["months"][m]["outbound"] for m in months_cached],
        "total":    [cache["months"][m]["inbound"] + cache["months"][m]["outbound"]
                     for m in months_cached],
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)

    if json_file:
        Path(json_file).write_text(output, encoding="utf-8")
        print(f"✅ KPIs Zendesk sauvegardés : {json_file}", file=sys.stderr)
    else:
        print(output)

    return result

# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Zendesk KPI Fetch — volumes SC destinataires")
    parser.add_argument("--explore",     nargs="?", const=30, type=int, metavar="DAYS",
                        help="Explorer les channels sur les N derniers jours (défaut: 30, sans cache)")
    parser.add_argument("--json-file",   type=str, metavar="PATH",
                        help="Sauvegarder le JSON dans un fichier")
    parser.add_argument("--cache-status", action="store_true",
                        help="Afficher l'état du cache sans faire de requête")
    parser.add_argument("--force-month", type=str, metavar="YYYY-MM",
                        help="Forcer le re-fetch d'un mois spécifique (ex: 2026-03)")
    args = parser.parse_args()

    if args.cache_status:
        cache = load_cache()
        print(f"\n📋 État du cache ({CACHE_FILE}) :\n", file=sys.stderr)
        print_cache_status(cache)
        to_fetch = months_to_fetch(cache)
        if to_fetch:
            print(f"\n⚠️  Mois non encore en cache : {', '.join(to_fetch)}", file=sys.stderr)
        else:
            print(f"\n✅ Tous les mois sont en cache.", file=sys.stderr)
        print()
        return

    if args.explore is not None:
        explore(args.explore)
    else:
        fetch_kpis(json_file=args.json_file, force_month=args.force_month)

if __name__ == "__main__":
    main()
