---
name: epic-creator
description: >
  Crée des epics Jira bien structurées pour le projet Destinataire (RECI) chez Shopopop.
  Utilise ce skill dès que l'utilisateur mentionne vouloir créer une epic, cadrer un sujet
  produit, structurer une idée de feature ou d'amélioration en epic Jira — même s'il ne
  dit pas explicitement "epic". Utilise-le aussi quand l'utilisateur décrit un problème
  ou une opportunité produit qui mérite d'être formalisée. Le skill conduit une interview
  guidée pour s'assurer que l'epic est centrée sur la problématique et les KPIs avant de
  parler solution, puis crée l'epic directement dans Jira.
---

# Skill : Création d'Epic Jira — Shopopop

## Objectif

Ce skill guide Yves dans la création d'epics Jira pour le projet Destinataire (RECI).
Il s'assure que chaque epic est **centrée sur le problème** (problem-centric) plutôt que
sur la solution, et que des **KPIs mesurables** sont définis avant de parler features.

## Contexte à lire en priorité

Avant de commencer l'interview, lis :
- `.context/shopopop.md` — vocabulaire Shopopop (cotransporteur, destinataire, enseigne)
- `.context/destinataire.md` — contexte du produit Destinataire

## Processus

### Étape 1 — Interview guidée

Conduis une interview **une question à la fois**. Attends la réponse avant de passer à la
suivante. Adapte ton ton : conversationnel, pas bureaucratique.

**Ordre des questions :**

**Q1 — Titre**
Demande un titre court et factuel pour l'epic.
> Ex: "Modération - Signalement", "Amélioration du tunnel de commande"

**Q2 — Contexte**
Qu'est-ce qui a déclenché ce sujet maintenant ? Quelle est la situation actuelle ?
- Cherche à comprendre le "pourquoi maintenant"
- Un contexte produit, business, ou feedback terrain peut être la source

**Q3 — Problème observé** ⚠️ Section critique
Quel problème concret est observé ? Y a-t-il des données ou signaux qui le confirment ?
- Pousse pour avoir des chiffres si possible (ex: taux d'abandon, volume de retours SAV, note NPS)
- Qu'est-ce qui se passe pour le destinataire aujourd'hui sans cette epic ?
- Quel est l'impact si on ne résout pas ce problème ?

**Si la réponse décrit une solution plutôt qu'un problème** (ex: "je veux développer X"),
recentre doucement :
> "Et quel problème est-ce que ça résout ? Qu'est-ce que le destinataire vit aujourd'hui
> qui est frustrant ou bloquant ?"

**Q4 — Objectifs & KPIs**
Comment saurons-nous que cette epic a réussi ?
- Vise 2 à 3 KPIs mesurables et chiffrés
- Si l'utilisateur est bloqué, propose des KPIs adaptés au contexte :
  - Taux de conversion / complétion d'étape
  - NPS ou satisfaction (CSAT)
  - Volume de contacts SAV liés au sujet
  - Délai moyen (commande → livraison, attente, etc.)
  - Taux d'erreur ou d'échec
  - Taux d'adoption d'une feature
- "Améliorer l'expérience" n'est PAS un KPI. Aide l'utilisateur à le chiffrer.

**Q5 — Solution envisagée**
C'est ici seulement qu'on parle de solution.
Quelles features ou fonctionnalités sont envisagées ? Qu'est-ce qu'on sait déjà vouloir
construire ?

**Q6 — Stratégie de déploiement** *(optionnel)*
Y a-t-il des contraintes ou une stratégie de déploiement à anticiper ?
- Feature flag, déploiement progressif, rollback plan, bêta...
- Si rien à dire, cette section sera omise.

**Q7 — Liens & dépendances**
Y a-t-il des liens avec d'autres epics, équipes, systèmes ou API tiers ?
- Références Jira (ex: RECI-XXX), dépendances inter-équipes, APIs...
- Si rien à dire, cette section sera omise.

**Q8 — Trimestre**
Dans quel trimestre cette epic est-elle prévue ? (ex: 26Q1, 26Q2, 26Q3, 26Q4)
- Obligatoire sauf si l'epic est mise en statut "Parking lot"

---

### Étape 2 — Génération du draft

Une fois toutes les infos collectées, génère le draft complet dans le chat **avant**
de créer dans Jira. Utilise ce format exact :

```
**Titre :** [titre]

---

## 🧩 Contexte

[Description du contexte : pourquoi maintenant, quelle situation actuelle]

---

## 🔍 Problème observé

[Description factuelle du problème, avec données chiffrées si disponibles.
Impact si non résolu.]

---

## 🎯 Objectifs & KPIs

[Description de l'objectif stratégique]

- **KPI 1 :** [Métrique] → cible : [valeur]
- **KPI 2 :** [Métrique] → cible : [valeur]
- **KPI 3 :** [Métrique] → cible : [valeur] *(si pertinent)*

---

## 🎨 Solution envisagée

[Description des features / fonctionnalités prévues]

---

## 🚀 Stratégie de déploiement *(optionnel)*

[Si renseigné, sinon section absente]

---

## 🔗 Liens & dépendances

[Si renseigné, sinon section absente]
```

Demande ensuite : **"Ce draft te convient ? Je peux le créer dans Jira, ou tu veux modifier quelque chose ?"**

---

### Étape 3 — Création dans Jira

Une fois le draft validé, crée l'epic avec le tool `createJiraIssue` :

- **cloudId** : `93674ed8-babf-4447-b125-e6d2ac26406b`
- **projectKey** : `RECI`
- **issueTypeName** : `Epic`
- **summary** : titre de l'epic
- **description** : contenu complet en Markdown (sections 🧩🔍🎯🎨🚀🔗)
- **additional_fields** : `{"components": [{"id": "10496"}], "customfield_10700": {"id": "<id_trimestre>"}}`
  - IDs des trimestres : `26Q1` → `10573`, `26Q2` → `10574`, `26Q3` → `10575`
  - Composant par défaut : `Recipient UI` (id `10496`). Adapter si le sujet concerne une autre couche (ex: `Recipient API` → `10298`, `Partner API` → `10497`).

Après création, partage le lien Jira : `https://shopopop.atlassian.net/browse/[clé]`

Si l'epic a été créée à partir d'une opportunité Notion, mettre à jour l'opportunité avec `notion-update-page` :
- **Statut** → `Initiative`
- **Epic Jira** → URL de l'epic (ex: `https://shopopop.atlassian.net/browse/RECI-XXX`)

---

## Règles essentielles

- **Problème avant solution** : les sections Problème et KPIs viennent avant la Solution.
  Si l'utilisateur saute à la solution, remonte au problème.
- **KPIs chiffrés** : un objectif sans chiffre n'est pas un KPI.
- **Vocabulaire** : utiliser "destinataire" (pas "utilisateur"), "cotransporteur" (pas "shopper").
- **Ton** : conversationnel et bienveillant, pas robotique.
- **Une question à la fois** : ne bombarde pas l'utilisateur avec toutes les questions d'un coup.
