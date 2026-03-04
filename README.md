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

**En début de chaque session, lire obligatoirement les fichiers de contexte suivants avant toute chose :**
- `.context/shopopop.md` — vocabulaire, parties prenantes, règles terminologiques
- `.context/produit.md` — contexte produit
- `.context/equipe.md` — composition de l'équipe
- `.context/destinataire.md` — profil du destinataire

Ces fichiers font foi. En cas de doute sur un terme ou un concept, s'y référer.

## Usage

- **Contexte** : renseigner les fichiers `.context/` pour que Claude ait une base de connaissance sur Shopopop
- **Skills** : les skills dans `.skills/skills/` sont automatiquement détectés par Cowork
- **Scripts** : scripts Python versionnés et réutilisables
- **Outputs** : les fichiers générés (Word, Excel, PPT...) sont stockés ici mais exclus du versioning git

## Versioning

Ce repo est versionné sur GitHub. Les outputs et fichiers binaires générés sont exclus via `.gitignore`.
