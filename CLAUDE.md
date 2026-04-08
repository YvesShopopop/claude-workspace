# Instructions de démarrage — Session Claude / Yves @ Shopopop

## À lire obligatoirement en début de chaque session

Avant toute chose, lire ces fichiers dans cet ordre :

1. `claude_workspace/.context/shopopop.md` — vocabulaire, parties prenantes, règles terminologiques
2. `claude_workspace/.context/produit.md` — contexte produit Destinataire
3. `claude_workspace/.context/equipe.md` — composition de l'équipe
4. `claude_workspace/.context/destinataire.md` — profil du destinataire
5. `claude_workspace/.context/workspace-structure.md` — règles d'organisation des fichiers et procédures - A lire avant de travailler sur les skills
6. `claude_workspace/todo-jour.md` — tâches du jour
7. `claude_workspace/todo-plus-tard.md` — tâches à plus long terme

Ces fichiers font foi. En cas de doute sur un terme, un concept ou une procédure, s'y référer.

## Règle importante

Ne jamais démarrer une tâche sans avoir chargé ce contexte. Si un fichier est manquant ou illisible, le signaler à Yves.

## Règle sur les skills — à retenir impérativement

Les fichiers de skills installés par Cowork (dans `.claude/skills/`) sont **en lecture seule**. Toute tentative d'édition directe échouera systématiquement.

**Procédure obligatoire pour modifier un skill :**
1. `cp -r /path/to/skill /tmp/skill-name` — copier dans `/tmp/`
2. `chmod u+w /tmp/skill-name/SKILL.md` — rendre modifiable
3. Éditer `/tmp/skill-name/SKILL.md`
4. `cp -r /path/to/skill-creator /tmp/skill-creator && chmod -R u+w /tmp/skill-creator`
5. `cd /tmp/skill-creator && python -m scripts.package_skill /tmp/skill-name` — packager
6. Copier le `.skill` généré dans `claude_workspace/` pour que Yves puisse le réinstaller via Cowork

Ne jamais essayer d'éditer directement un fichier dans `.claude/skills/` — cela échouera et fait perdre du temps à Yves.
