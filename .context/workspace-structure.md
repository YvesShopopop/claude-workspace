# Structure du claude_workspace

## Arborescence cible

```
claude_workspace/
├── .context/          # Fichiers de contexte produit (ne pas modifier sans raison)
├── .skills/           # Skills (géré automatiquement, ne pas toucher)
├── outputs/           # Tous les livrables finaux
│   ├── html/          # Visualisations et dashboards HTML
│   └── (autres fichiers : .md, .xlsx, .pptx, .docx, .pdf…)
├── wip/               # Travaux en cours / brouillons non finalisés
├── data/              # Données brutes (CSV, exports…)
├── tmp/               # Fichiers temporaires : .skill en attente d'installation, scripts intermédiaires
│   └── cleanup-skills.sh  # Script de nettoyage automatique des .skill obsolètes
├── .gitignore
└── README.md
```

## Règles de création de fichiers

- **Tout livrable final** (HTML, Markdown, Excel, Word, PDF, PowerPoint) → `outputs/`
- **Fichiers HTML** (roadmaps, dashboards, KPIs, visualisations) → `outputs/html/`
- **Brouillons / WIP** (documents en cours, epics non finalisées) → `wip/`
- **Données brutes** (CSV, exports Jira/Metabase) → `data/`
- **Fichiers `.skill` temporaires** → `tmp/` uniquement (jamais à la racine ni ailleurs)
- **Ne rien créer à la racine** en dehors des fichiers de configuration (`.gitignore`, `README.md`)

## Modification des skills — procédure obligatoire

Les fichiers de skills installés (dans `.claude/skills/`) sont en **lecture seule**. Toute tentative de modification directe échouera. Il faut toujours passer par cette procédure :

**Avant de commencer**, exécuter le script de nettoyage :
```bash
bash claude_workspace/tmp/cleanup-skills.sh
```
Cela supprime les `.skill` temporaires déjà installés (skill installé plus récent que le fichier `.skill`).

1. Copier le skill dans `/tmp/` : `cp -r /path/to/skill /tmp/skill-name`
2. Rendre le fichier modifiable : `chmod u+w /tmp/skill-name/SKILL.md`
3. Éditer `/tmp/skill-name/SKILL.md`
4. Copier le skill-creator dans `/tmp/` (lui aussi en lecture seule) : `cp -r /path/to/skill-creator /tmp/skill-creator && chmod -R u+w /tmp/skill-creator`
5. Packager depuis `/tmp/skill-creator` : `cd /tmp/skill-creator && python -m scripts.package_skill /tmp/skill-name`
6. Déplacer le `.skill` généré dans **`claude_workspace/tmp/`** (pas à la racine) pour que l'utilisateur puisse l'installer

> ⚠️ Ne jamais essayer d'éditer directement un fichier dans `.claude/skills/` — c'est en lecture seule et ça échouera systématiquement.

## Règles comportementales pour les skills (overrides permanents)

Ces règles s'appliquent **en priorité** sur les instructions des skills, dès le démarrage de chaque session.

### Skill `daily-todo` — commande `!todo`

Avant toute chose quand `!todo` est invoqué :
1. Lire `todo-jour.md` et extraire la date du titre (ex. `# 🎯 Objectifs du jour — Jeudi 2 avril 2026`)
2. Comparer avec la date du jour (via bash `date`)
3. **Si la date n'est pas aujourd'hui** → lancer directement la routine matinale pour créer la todo du jour, SANS afficher l'état de la veille ni proposer de cocher des items
4. **Si la date est bien aujourd'hui** → afficher normalement l'état actuel

---

## Ce qu'il ne faut pas faire

- Ne pas créer de fichiers `.skill` à la racine (format obsolète)
- Ne pas laisser de fichiers lock (`.~lock.*`)
- Ne pas créer de dossiers `scripts/` sans contenu prévu
- Ne jamais affirmer qu'une action est impossible via une API sans avoir essayé : tester d'abord avec l'outil disponible. Exemple : modifier une formule Notion est possible via `notion-update-data-source`, contrairement à ce qui avait été affirmé à tort.
- Ne pas créer de nouveaux fichiers de contexte sans avoir d'abord vérifié que `.context/` n'en contient pas déjà un approprié (`find /sessions/.../mnt -name "*.md"`).
