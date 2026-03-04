# Produit

## Vision produit

> Orchestrer intelligemment une logistique du dernier kilomètre basée sur l'existant, en connectant la demande de livraison des enseignes avec la capacité réelle des citoyens à livrer, au bon moment et au bon endroit.

La plateforme Shopopop existe pour réconcilier trois réalités :
- Le dernier kilomètre est coûteux, source de frustrations opérationnelles et d'insatisfaction client
- Des millions de trajets sont effectués chaque jour sans être exploités
- Un modèle de cotransportage peut créer de la valeur économique et sociale à partir de ces trajets existants

**Boussole produit :** chaque produit, chaque initiative, chaque investissement doit répondre à :
> Est-ce que cela nous rapproche d'une plateforme de cotransportage plus fiable, plus efficace et plus responsable, à grande échelle ?

## Axes stratégiques

Trois axes structurants guident la roadmap produit :

| Axe | Description | Contribution entreprise |
|---|---|---|
| 🚀 **Scale with UX** | Expérience utilisateur simple et personnalisée pour stimuler adoption, rétention et marge | Maximiser la performance économique |
| 📊 **Data monetization** | Exploiter la data propriétaire (10+ ans) pour créer de la valeur business | Accélérer la croissance par diversification des revenus |
| 🧩 **Model fit** | Aligner les produits avec le standard du cotransportage, rendre visible notre différence | Refonte opérationnelle garante de conformité |

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
