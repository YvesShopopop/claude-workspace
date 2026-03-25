---
name: product-news
description: >
  Rédige les communications "product-news" Shopopop envoyées dans Slack lors d'une mise en
  production. Utilise ce skill dès que l'utilisateur mentionne vouloir communiquer une évolution
  produit, écrire un message de release, annoncer une feature à l'équipe, rédiger un "product-news"
  ou un "product news" — même s'il ne nomme pas explicitement le skill. Utilise-le aussi quand
  l'utilisateur dit "je dois comm'" ou "je veux annoncer" une mise en prod. Le skill peut s'appuyer
  sur des pages Notion de discovery, des tickets Jira, ou simplement les inputs directs de l'utilisateur.
---

# Product News Writer

Ce skill génère des communications produit au format Shopopop, prêtes à être copiées-collées dans Slack.

## Contexte

Quand une évolution est mise en production, le PM communique à l'ensemble de Shopopop le contenu
de la release via un message Slack dans le channel `#product-news` (ou équivalent). Ce message
doit être clair pour toute l'équipe — y compris les personnes hors équipe produit (ops, support, sales).

## Structure du message Slack

Baser systématiquement sur ce format — c'est le meilleur compromis entre lisibilité et impact :

```
🇫🇷 [AUDIENCE] Titre court et descriptif

Phrase d'intro optionnelle si plusieurs features non liées.

EMOJI **Titre de la feature**
**Problème :** description courte du problème vécu par l'utilisateur ou l'équipe — en langage métier, pas technique.
**Solution :** ce qui a été livré et ce que ça change concrètement.

[Répéter le bloc EMOJI / Problème / Solution pour chaque feature]

**Disponibilité**
[Depuis ce matin ✅ / Disponible dès aujourd'hui ✅ / Déployé le [date] ✅]
```

**Audiences possibles :** `[Destinataire]`, `[App mobile]`, `[BO Pro]`, `[BO Interne]`, `[API Partenaires]`, `[Data]`

Le tag désigne le **produit ou l'équipe à l'origine de l'évolution**, pas nécessairement l'utilisateur final. Par exemple, une feature livrée dans le back-office prend `[BO Pro]` ou `[BO Interne]`, même si elle bénéficie indirectement aux destinataires.

Si la release couvre plusieurs produits distincts, produire un message par produit.

## Version anglaise

Après le message FR, produire la version anglaise dans ce format :

```
🇬🇧 [EN] [même titre]

[traduction fidèle du message FR, même structure Problème/Solution]
```

Préciser à l'utilisateur : *"Poste la version 🇬🇧 en commentaire du message Slack 🇫🇷."*

## Ton et style

- **Concis** : une à deux phrases par Problème, une à deux phrases par Solution
- **Centré sur l'impact** : parler de l'utilisateur final ou de l'équipe, pas de l'implémentation
- **Accessible** : éviter le jargon technique (ex : "les statuts sont mieux gérés" → "le livreur passe d'une étape à l'autre plus facilement")
- **Pas de "PS"** ni d'informations en vrac en fin de message — si quelque chose arrive bientôt, l'intégrer naturellement ("La fonctionnalité X arrivera prochainement.")
- Choisir un emoji thématique par feature pour aider à la lecture

## Récupération des informations

Le skill peut s'appuyer sur trois types de sources — utilise les outils disponibles :

1. **Page Notion** (discovery, spec, brief) : utiliser `notion-fetch` pour récupérer le contenu
2. **Ticket ou epic Jira** : utiliser `getJiraIssue` ou `searchJiraIssuesUsingJql` pour récupérer les détails
3. **Input direct de l'utilisateur** : si les sources Notion/Jira ne sont pas fournies ou insuffisantes

Si les informations sont partielles, poser les questions minimales nécessaires avant de rédiger :
- À quelle audience est destinée cette com' ?
- Quel problème concret cette évolution résout-elle pour l'utilisateur ?
- Quelle est la solution livrée et son impact visible ?

## Livrable

Produire **deux blocs distincts** clairement séparés, directement dans la conversation (pas de fichier) :

---
**📋 Message Slack 🇫🇷 — à poster**
```
[message FR prêt à copier-coller]
```

---
**💬 Commentaire Slack 🇬🇧 — à poster en commentaire**
```
[message EN prêt à copier-coller]
```
---
