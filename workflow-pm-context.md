# Workflow PM — Spec Driven Development adapté

## Objectif
Construire un workflow complet couvrant les tâches PM de Yves, inspiré du Spec Driven Development, avec un skill Claude pour chaque étape.

## Périmètre
- De l'émergence d'une idée jusqu'à la User Story (upstream dev)
- Review fonctionnelle de ce qui a été implémenté
- Documentation des features
- Communication des évolutions

---

## Étapes du workflow

### Étape 1 — Capture d'opportunité ✅ COMPLÈTE
**Input :** idée brute (de Yves, d'un autre service, ou des utilisateurs)
**Output :** entrée dans la BDD Notion "Opportunités"
**Skill :** `capture-opportunite` ✅ créé, testé et installé

**BDD Notion :** https://www.notion.so/25aa587de95f453392690c4751ae3f1b
**Page parente :** https://www.notion.so/shopopop/Opportunit-s-3282c5c7981680e99131e5b48ad6acad

**Champs de la BDD :**
- Titre (TITLE)
- Problème décrit (RICH_TEXT)
- Source (RICH_TEXT — texte libre, pas de liste)
- Impact estimé (SELECT : Faible / Moyen / Fort / Très fort)
- Effort estimé (SELECT : Faible / Moyen / Fort / Très fort)
- Statut (SELECT : À évaluer / À creuser / Initiative / Abandonné)
- Date de création (auto)
- Notes (RICH_TEXT)
- Score priorité (FORMULA : Impact / Effort, valeurs 0.25 à 4)
- Epic Jira (URL : lien vers l'epic Jira associée, renseigné lors du passage en Initiative)

**Logique de décision :**
- Critères pour passer "À creuser" : impact estimé + effort estimé (en lien avec axes stratégiques produit)
- Passage opportunité → Initiative : décision de Yves (peut consulter d'autres personnes)

---

### Étape 2 — Cadrage / Epic Jira
**Input :** opportunité passée en statut "Initiative" dans Notion
**Output :** Epic Jira structurée (projet RECI)
**Skill :** `epic-creator` ✅ existant

**Règles :**
- Toute epic hors statut "Parking lot" doit avoir un trimestre renseigné (champ `Trimestre`, format `26Q1`, `26Q2`…)
- Les epics en "Parking lot" peuvent ne pas avoir de trimestre

---

### Étape 3 — Spécification
**Input :** Epic Jira
**Output :** User Stories Jira
**Skill :** `user-stories` ✅ existant

---

### Étape 4 — Review fonctionnelle
**Input :** US Jira livrées
**Output :** commentaire Jira avec liste des points testés (conformité fonctionnelle uniquement)
**Skill :** à créer

---

### Étape 5 — Documentation
**Input :** US validées
**Output :** page Notion de doc feature
**Skill :** à créer

---

### Étape 6 — Communication
**Input :** Epic / US / doc feature
**Output :** message Slack product-news
**Skill :** `product-news` ✅ existant

---

## Avancement

| Étape | BDD / Structure | Skill |
|-------|----------------|-------|
| 1 — Capture d'opportunité | ✅ BDD Notion créée | ✅ capture-opportunite |
| 2 — Epic Jira | — | ✅ epic-creator |
| 3 — Spécification | — | ✅ user-stories |
| 4 — Review fonctionnelle | — | ⏳ à créer |
| 5 — Documentation | — | ⏳ à créer |
| 6 — Communication | — | ✅ product-news |

## Prochaines étapes suggérées

### Workflow PM — Skills manquants
Créer les skills pour les étapes 4 et 5 (review fonctionnelle et documentation).
Yves a indiqué vouloir commencer par l'une ou l'autre — à confirmer en début de session.

### Gestion du planning des epics (à traiter)
La timeline Jira se base sur des champs date (start date / due date). Ces champs devraient être synchronisés avec les infos de planification de l'epic :
- Si l'epic est planifiée sur un **trimestre** → dériver les dates de début/fin du trimestre correspondant
- Si l'epic est planifiée sur un ou plusieurs **sprints** → dériver les dates depuis les dates du/des sprints

Objectif : garder la timeline Jira cohérente sans avoir à saisir les dates manuellement.

## Notes de session
- Le skill `capture-opportunite` a été testé sur un cas réel : "Transmettre les commentaires du destinataire au CTP quand il a laissé une bonne note" → entrée créée dans Notion avec succès.
- Le skill est packagé dans le workspace : `capture-opportunite.skill`

## Session 2026-03-24
- BDD Opportunités passée en mode **inline** dans la page Notion parente
- Ajout d'un champ **Score priorité** (formula Impact/Effort) dans la BDD
- Ajout d'un champ **Epic Jira** (URL) dans la BDD
- Import de 14 opportunités depuis la boîte à idées Destinataire
- Cadrage de l'opportunité "Ajouter étage et ascenseur dans le tracking" → epic **RECI-363** créée (26Q3, Discovery)
- Opportunité "Permettre au destinataire de valider la livraison" liée à l'epic existante **RECI-335**
- Règle ajoutée dans epic-creator : toute epic hors Parking lot doit avoir un trimestre ; après création, mettre à jour l'opportunité Notion (statut + lien Epic Jira)
- Fichier `destinataire.md` allégé : suppression de la roadmap inline, remplacée par des liens vers Jira et le HTML généré
