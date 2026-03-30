# Workspace Claude — Shopopop

Espace de travail partagé entre Yves et Claude (Cowork).

## Structure

```
workspace/
├── .context/       # Fichiers de contexte (Shopopop, produit, équipe)
├── .skills/        # Skills custom pour Claude
│   └── skills/
│       └── user-stories/
├── scripts/        # Scripts Python réutilisables
│   ├── analyse/
│   └── dataviz/
└── outputs/        # Livrables générés (non versionnés)
```

## Instructions pour Claude

**Fichiers temporaires** : utiliser `/tmp/` pour tout fichier intermédiaire (packages exportés, archives, fichiers de travail transitoires). Ne jamais écrire de fichiers temporaires dans ce workspace.

**Fichiers HTML générés** (reviews, rapports, visualisations) : les sauvegarder dans `outputs/html/`.

**En début de chaque session, lire obligatoirement les fichiers de contexte suivants avant toute chose :**
- `.context/shopopop.md` — vocabulaire, parties prenantes, règles terminologiques
- `.context/produit.md` — contexte produit
- `.context/equipe.md` — composition de l'équipe
- `.context/destinataire.md` — profil du destinataire
- `todo-jour.md` — tâches du jour (lire pour connaître les tâches en cours et l'état de la veille)
- `todo-plus-tard.md` — tâches à plus long terme (vérifier les échéances)

Ces fichiers font foi. En cas de doute sur un terme ou un concept, s'y référer.

## Usage

- **Contexte** : renseigner les fichiers `.context/` pour que Claude ait une base de connaissance sur Shopopop
- **Skills** : les skills dans `.skills/skills/` sont automatiquement détectés par Cowork
- **Scripts** : scripts Python versionnés et réutilisables
- **Outputs** : les fichiers générés (Word, Excel, PPT...) sont stockés ici mais exclus du versioning git

## Scripts

### Prérequis (à faire une seule fois)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

Pour les sessions suivantes, activer simplement le venv :
```bash
source .venv/bin/activate
```

### zendesk_export.py — Export des tickets destinataires

Copier `.env.example` en `.env` et renseigner les credentials + filtre.

```bash
# Identifier le filtre destinataire (tags, group_id, ticket_form_id)
python3 scripts/zendesk_export.py --discover

# Exporter les tickets sur une période (CSV dans data/)
python3 scripts/zendesk_export.py

# Vérifier pourquoi des tickets spécifiques seraient absents d'un export
python3 scripts/zendesk_export.py --check-ids 123456,789012

# Consulter l'historique des exports déjà réalisés
python3 scripts/zendesk_export.py --history
```

Les exports sont sauvegardés dans `data/` au format `zendesk_destinataires_YYYY-MM-DD_YYYY-MM-DD.csv`.
L'historique des périodes exportées est tracé dans `data/zendesk_fetch_history.json`.

## Versioning

Ce repo est versionné sur GitHub. Les outputs et fichiers binaires générés sont exclus via `.gitignore`.
