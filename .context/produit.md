# Produit

## Vision produit

> Orchestrer intelligemment une logistique du dernier kilomètre basée sur l'existant, en connectant la demande de livraison des enseignes avec la capacité réelle des citoyens à livrer, au bon moment et au bon endroit.

Le portefeuille de produits Shopopop est au service d'un système cohérent, structuré autour de **4 missions** :

1. **Créer la confiance** — pour les enseignes qui externalisent un maillon critique de leur promesse client, pour les destinataires qui attendent une livraison fiable et solidaire, pour les cotransporteurs qui s'engagent sur un service d'entraide.
2. **Orchestrer la complexité** — arbitrer en temps réel entre demande, capacité, contraintes terrain et qualité de service ; absorber les aléas du réel sans dégrader l'expérience.
3. **Transformer la donnée en avantage compétitif** — capitaliser sur 10+ ans de données propriétaires, apprendre en continu pour améliorer le matching, la fiabilité, la marge et l'impact social.
4. **Rendre le modèle scalable** — sans multiplier les coûts fixes, sans industrialiser à outrance, en restant fidèle à un modèle de plateforme responsable.

**Boussole produit :** chaque produit, chaque initiative, chaque investissement doit répondre à :
> Est-ce que cela nous rapproche d'une plateforme de cotransportage plus fiable, plus efficace et plus responsable, à grande échelle ?

## Axes stratégiques

Trois axes structurants guident la roadmap produit. Ils répondent à la stratégie globale de l'entreprise (cf. Shopopoint juillet 2025). Les initiatives multi-axes sont valorisées et priorisées.

| Axe | Description | Contribution entreprise |
|---|---|---|
| 🚀 **Scale with UX** | Expérience utilisateur simple et personnalisée pour stimuler adoption, rétention et marge | Maximiser la performance économique |
| 📊 **Data monetization** | Exploiter la data propriétaire (10+ ans) pour créer de la valeur business | Accélérer la croissance par diversification des revenus |
| 🧩 **Model fit** | Aligner les produits avec le standard du cotransportage, rendre visible notre différence | Refonte opérationnelle garante de conformité |

## Principes d'alignement entre produits

| Principe | Description |
|---|---|
| 🧠 **Vision commune** | Chaque produit est un maillon d'un écosystème, pas un silo autonome. |
| 🌐 **Contribution transverse** | Une initiative locale doit créer de la valeur globale. |
| 🧮 **Priorité au modèle** | Ce qui renforce le cotransportage est prioritaire, même si cela demande un effort cross-team. |
| 🎯 **Alignement stratégique** | Chaque initiative doit répondre à au moins un des trois axes stratégiques, idéalement plusieurs. |

## Enablers

Initiatives à faible impact business direct mais nécessaires (réglementaire, UX, contractuel, organisationnel). Ils sont rendus visibles dans la roadmap, time-boxés, et justifiés par le "risque de ne pas faire".

## Fonctionnalités principales

Les fonctionnalités sont organisées par produit :

### Application mobile (cotransporteurs)
<!-- TODO : fonctionnalités clés de l'app mobile -->

### Back-office pro (enseignes)
<!-- TODO : fonctionnalités clés du BO pro -->

### Back-office interne (équipes Shopopop)
<!-- TODO : fonctionnalités clés du BO interne -->

### API partenaire

Responsable produit : **Yves**

API exposée par Shopopop permettant aux partenaires de connecter leurs outils internes pour transmettre des demandes de livraison. Documentation : https://developers.shopopop.com/partners/documentation/v2/

**5 endpoints disponibles :**

| Endpoint | Description |
|---|---|
| Éligibilité | Vérifier si une demande de livraison est éligible |
| Création | Créer une livraison |
| Annulation | Annuler une livraison |
| Modification de créneau | Modifier le créneau d'une livraison |
| Récupération | Récupérer les informations d'une livraison |

**Webhooks :** renvoi vers le partenaire des événements du cycle de vie de la livraison (principalement des changements de statut).

### Produit Destinataire

Responsable produit : **Yves**

Interface web à destination des destinataires. Produit récent malgré la place centrale du destinataire dans le modèle Shopopop.

**Fonctionnalités actuelles :**

- **Suivi de livraison** : page affichant le statut de la livraison en cours, avec possibilité de modifier le créneau dans certains cas
- **Évaluation** : formulaire de notation d'une livraison terminée

**Évolutions prévues :**

- Création de compte Shopopop pour les destinataires, donnant accès à des fonctionnalités enrichies

## Roadmap

La roadmap est structurée en trois niveaux :

- **Initiative** (projet SHOP dans Jira Product Discovery) : projet structurant, porté sur plusieurs trimestres, impliquant plusieurs équipes. Pilotée par un Product Lead (JM ou Matthieu), un référent UX, un Principal Engineer (Aymeric) et un Chef de projet transverse (Pierre).
- **Lot** (Initiative Lot SHOP) : déclinaison trimestrielle d'une initiative. Validée par JM ou Matthieu.
- **Epic** (projets BO / API / APP / DATA dans Jira) : périmètre d'un Product Manager.

Les initiatives peuvent couvrir plusieurs axes stratégiques — les initiatives multi-axes sont priorisées.

## Glossaire produit

| Terme | Définition |
|---|---|
| **Cotransporteur** | Particulier qui effectue la livraison sur son trajet (terme officiel — ne plus utiliser "Shopper") |
| **Destinataire** | Client final qui se fait livrer |
| **Enseigne** | Retailer / magasin, client direct de Shopopop |
| **Partenaire API** | Intégrateur technique entre Shopopop et une enseigne |
| **Initiative** | Projet structurant transverse, piloté sur plusieurs trimestres |
| **Enabler** | Initiative à faible impact business immédiat mais nécessaire (conformité, UX, contractuel, organisationnel) |
| **Lot** | Déclinaison trimestrielle d'une initiative |
| **Epic** | Unité de travail au niveau d'un Product Manager |

## Stack technique

| Couche | Technologie | Note |
|---|---|---|
| Back-end | Node.js | |
| Front-end | Node.js | |
| Mobile | iOS + Android | Application native |
| Base de données | MySQL | Base principale |

<!-- TODO : à compléter avec les développeurs (frameworks, infra, cloud, autres BDD...) -->
