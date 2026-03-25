# Epic WIP — Validation de la livraison

> **Statut :** Interview en cours — à reprendre à Q4 (KPIs chiffrés)

---

## 🧩 Contexte

La problématique est connue depuis longtemps, mais le sujet est opportun maintenant car :
- La page de suivi destinataire est en mesure d'évoluer techniquement
- L'axe stratégique "model fit" vise à donner plus de possibilités au destinataire

---

## 🔍 Problème observé

**Fonctionnement actuel de la validation de livraison :**

La validation est aujourd'hui effectuée par le **cotransporteur (CTP)**, selon deux modalités :

- **Validation avec code** : au début de la livraison, un code est transmis au destinataire. Lorsqu'il reçoit sa commande, il donne ce code au CTP qui l'utilise pour valider.
- **Validation sans code** : si le CTP a oublié de demander le code ou que le destinataire n'était pas en mesure de le donner, le CTP peut valider sans code — mais doit alors attendre 48h pour recevoir son pourboire (délai de sécurité pour Shopopop).
- Le **Service Client Shopopop** peut forcer la validation si nécessaire.

**Problèmes identifiés :**
1. L'échange de code peut être source d'erreur
2. Le CTP valide parfois la livraison très tard → donne l'impression d'une livraison en retard alors que la commande a été livrée dans les temps → **score qualité faussé (taux de retard surestimé)**

**Donnée disponible :** 19 minutes d'écart en moyenne entre l'événement "Arrivé chez le client" et la validation par le CTP.

---

## 🎯 Objectifs & KPIs

- **KPI 1 — Nb de validations effectuées par le destinataire** : baseline 0 → cible > 0 (premier jalon : prouver que le canal fonctionne)
- **KPI 2 — Taux de retard** : baseline 7,3% → cible < 7%
  - Mécanisme : en validant côté destinataire dès réception, on réduit l'écart entre "Arrivé chez le client" et validation effective (19 min en moyenne aujourd'hui)

---

## 🎨 Solution envisagée

Depuis la **page de tracking**, le destinataire peut valider sa livraison une fois qu'il l'a reçue.

**Principes :**
- La validation destinataire est proposée uniquement après que la livraison a été **retirée au point de retrait** (pré-condition)
- Le CTP conserve la possibilité de valider (avec ou sans code) — le mécanisme actuel avec code est maintenu dans un premier temps (pourrait être supprimé à terme)
- La **première validation reçue** (CTP ou destinataire) constitue la date de validation de la livraison

**Hors scope :** la gestion d'une validation par erreur (et le maintien de l'accès aux infos de livraison pour le CTP après validation) est hors périmètre RECI → à traiter par l'équipe Mobile.

---

## 🚀 Stratégie de déploiement

Déploiement progressif via **A/B test** : la fonctionnalité de validation destinataire est activée pour une partie aléatoire des destinataires. Cela permet de mesurer l'effet réel sur les KPIs (taux de retard, nb de validations) en comparant les deux groupes avant généralisation.

---

## 🔗 Liens & dépendances

- **Page de tracking** : pas de blocage, suffisamment avancée techniquement
- **Équipe Mobile** : gestion de la validation par erreur destinataire (accès du CTP aux infos de livraison après validation) — hors scope RECI, à aligner en parallèle
- **Équipe Communications** : à impliquer (notifications liées à la validation ?)
- **Équipe Data** : à embarquer pour le suivi de l'A/B test et la mesure des KPIs
