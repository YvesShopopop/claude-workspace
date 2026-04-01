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
├── .gitignore
└── README.md
```

## Règles de création de fichiers

- **Tout livrable final** (HTML, Markdown, Excel, Word, PDF, PowerPoint) → `outputs/`
- **Fichiers HTML** (roadmaps, dashboards, KPIs, visualisations) → `outputs/html/`
- **Brouillons / WIP** (documents en cours, epics non finalisées) → `wip/`
- **Données brutes** (CSV, exports Jira/Metabase) → `data/`
- **Skills** → `.skills/skills/` uniquement (ne jamais créer de fichiers `.skill` à la racine)
- **Ne rien créer à la racine** en dehors des fichiers de configuration (`.gitignore`, `README.md`)

## Modification des skills — procédure obligatoire

Les fichiers de skills installés (dans `.claude/skills/`) sont en **lecture seule**. Toute tentative de modification directe échouera. Il faut toujours passer par cette procédure :

1. Copier le skill dans `/tmp/` : `cp -r /path/to/skill /tmp/skill-name`
2. Rendre le fichier modifiable : `chmod u+w /tmp/skill-name/SKILL.md`
3. Éditer `/tmp/skill-name/SKILL.md`
4. Copier le skill-creator dans `/tmp/` (lui aussi en lecture seule) : `cp -r /path/to/skill-creator /tmp/skill-creator && chmod -R u+w /tmp/skill-creator`
5. Packager depuis `/tmp/skill-creator` : `cd /tmp/skill-creator && python -m scripts.package_skill /tmp/skill-name`
6. Déplacer le `.skill` généré dans `claude_workspace/` pour que l'utilisateur puisse l'installer

> ⚠️ Ne jamais essayer d'éditer directement un fichier dans `.claude/skills/` — c'est en lecture seule et ça échouera systématiquement.

## Ce qu'il ne faut pas faire

- Ne pas créer de fichiers `.skill` à la racine (format obsolète)
- Ne pas laisser de fichiers lock (`.~lock.*`)
- Ne pas créer de dossiers `scripts/` sans contenu prévu
- Ne jamais affirmer qu'une action est impossible via une API sans avoir essayé : tester d'abord avec l'outil disponible. Exemple : modifier une formule Notion est possible via `notion-update-data-source`, contrairement à ce qui avait été affirmé à tort.
- Ne pas créer de nouveaux fichiers de contexte sans avoir d'abord vérifié que `.context/` n'en contient pas déjà un approprié (`find /sessions/.../mnt -name "*.md"`).
