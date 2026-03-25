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

## Ce qu'il ne faut pas faire

- Ne pas créer de fichiers `.skill` à la racine (format obsolète)
- Ne pas laisser de fichiers lock (`.~lock.*`)
- Ne pas créer de dossiers `scripts/` sans contenu prévu
