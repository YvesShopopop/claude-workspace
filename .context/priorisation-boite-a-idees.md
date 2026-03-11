# Priorisation — Boîte à idées Destinataire

**Fichier de travail :** `claude_workspace/outputs/priorisation-destinataire-Q2-2026.xlsx`
**Source Notion :** https://www.notion.so/shopopop/Destinataires-bo-te-id-es-2ea2c5c7981680bdaf81cd44d9379014
**Dernière mise à jour :** 11 mars 2026

---

## Contexte

Exercice de priorisation des sujets potentiels pour le produit Destinataire, avant de lancer la discovery. L'objectif est d'identifier les sujets à investiguer en priorité pour compléter le T2 2026.

**Sujets déjà planifiés en T2 (exclus de la priorisation) :**
- RECI-299 — Compte destinataire : création de compte Shopopop
- RECI-295 — Préférences destinataire : choix de cotransporteurs favoris
- RECI-303 — Modération - Signalement

---

## Framework de scoring

**Formule : Score = Reach × Impact × Confiance** (sans effort — l'effort sera pris en compte dans un second temps)

| Critère | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Reach** | Cas très rare | Segment restreint (<20%) | Segment significatif (20-50%) | Majorité (>50%) | Tous les destinataires |
| **Impact** | Marginal | Faible | Modéré sur 1 KPI | Fort sur 1 KPI clé | Majeur sur plusieurs KPIs |
| **Confiance** | Aucun signal | Hypothèse peu validée | Signal modéré / logique forte | Signal fort (retours terrain) | Données / multi-sources confirmées |

**Légende couleurs dans le tableau :**
- 🟢 Score ≥ 50 → Priorité haute
- 🟠 Score 25–49 → Priorité moyenne
- 🔴 Score < 25 → Faible / parking lot
- ⏳ Fond jaune → Score provisoire (en attente de données)

---

## Scores actuels

| # | Sujet | Auteur | R | I | C | Score | Provisoire |
|---|---|---|---|---|---|---|---|
| 1 | Validation de la livraison par le destinataire | Pierre | 5 | 5 | 4 | **100** | Non |
| 2 | Recueillir les feedbacks des destinataires | Yves | 5 | 4 | 4 | **80** | Non |
| 3 | Infos parking (conditions de stationnement) | Eugénie | 4 | 4 | 3 | **48** | Non |
| 4 | Présentation réciproque CTP / Destinataire | Pierre | 4 | 4 | 3 | **48** | Non |
| 5 | Notifications temps réel (enrichissement) | Pierre | 3 | 3 | 4 | **36** | Non |
| 6 | FAQ contextualisée | Matthieu | 3 | 3 | 3 | **27** | ⏳ Oui |
| 7 | Chat Destinataire / CTP | Pierre | 3 | 3 | 3 | **27** | Non |
| 8 | Annulation de livraison par le destinataire | Sophie | 2 | 4 | 3 | **24** | ⏳ Oui |
| 9 | Consignes particulières (handicap, aide) | Matthieu | 2 | 5 | 2 | **20** | Non |
| 10 | Historique CTP / destinataire | Eugénie | 3 | 3 | 2 | **18** | Non |
| 11 | Pourboire supplémentaire (tip additionnel) | Matthieu / Eugénie | 2 | 3 | 2 | **12** | Non |
| 12 | Transmettre les commentaires positifs au CTP | Collectif | 3 | 2 | 2 | **12** | Non |
| 13 | Jeu pendant l'attente | Clément | 2 | 1 | 1 | **2** | Non |

---

## Scores provisoires — données attendues

### ⏳ FAQ contextualisée (score actuel : 27)
- **Données attendues :** volume et motifs de contact des destinataires au service client
- **Impact attendu sur le score :** Reach et Confiance pourraient augmenter si les questions récurrentes représentent un volume significatif

### ⏳ Annulation de livraison par le destinataire (score actuel : 24)
- **Données attendues :** volume mensuel de cas gérés par le SAV sur ce motif
- **Impact attendu sur le score :** Reach pourrait passer de 2 à 3 si le volume est significatif

---

## Sujets exclus

| Sujet | Raison |
|---|---|
| CTP favori / choisir un livreur de confiance | En roadmap Q2 — RECI-295 |
| Signaler un problème sur ma livraison | En roadmap Q2 — RECI-303 |
| Compte destinataire | En roadmap Q2 — RECI-299 |
| Recueillir le consentement (RGPD) | Inclus dans le scope RECI-299 |
| Consignes en cas d'absence | Couvert par RECI-241 (T1, en cours) |
| Client absent | Couvert par épics décalage (RECI-134, RECI-145, RECI-241) |
| Pickup return | Couvert par épics décalage (RECI-134, RECI-145) |
| Suivre livraison depuis le site web | Déjà livré — RECI-83 + RECI-113 |
| Ne pas proposer les créneaux difficiles | Hors scope Destinataire (algo / app CTP) |
| Enrichissement données CTP prisme qualité | Hors scope Destinataire (BI / BO) |

---

## Rationale des scores clés

**Validation de la livraison (100)** — Impacts multiples confirmés : suppression de l'échange de code, réduction du délai de pourboire (cas sans code), meilleure connaissance de l'heure réelle de livraison. Couvre 100% des livraisons.

**Recueillir les feedbacks (80)** — Manque structurel : peu de signal côté destinataire bloque la validation de nombreuses autres idées. Sujet transversal qui alimente la priorisation future.

**Notifications enrichies (36, baissé de 64)** — Les alertes critiques (décalage, annulation) existent déjà via mail/SMS. Ce qui manque = mises à jour temps réel ("en route", etc.) visibles uniquement sur la page de tracking. C'est un enrichissement, pas un gap critique.

**Présentation réciproque + Chat (48 et 27, montés)** — Ancrés dans l'axe stratégique "Model fit" : Shopopop est une plateforme de mise en relation, pas un service de livraison. Toute initiative qui différencie de la livraison professionnelle est stratégiquement importante.
