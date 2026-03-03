# Skill : Rédaction de User Stories

## Description
Rédige des User Stories claires, bien structurées et prêtes pour le backlog, en suivant les standards de Shopopop.

## Format standard

### Structure d'une US
```
En tant que [persona],
Je veux [action/fonctionnalité],
Afin de [bénéfice/valeur].
```

### Critères d'acceptance
- Format Given / When / Then (Gherkin) ou liste de conditions vérifiables
- Chaque critère doit être testable
- Couvrir les cas nominaux ET les cas d'erreur

### Informations complémentaires à inclure
- **Titre** : court et descriptif
- **Epic / Feature** : rattachement dans la roadmap
- **Priorité** : MoSCoW (Must / Should / Could / Won't)
- **Story points** : estimation si demandée
- **Dépendances** : autres US liées
- **Notes techniques** : contraintes ou précisions pour les devs

## Instructions pour Claude

1. Lire le fichier `.context/produit.md` pour le contexte produit si disponible
2. Si le besoin est flou, poser des questions avant de rédiger
3. Proposer systématiquement plusieurs critères d'acceptance
4. Signaler si l'US semble trop large (candidat au découpage)
5. Adapter le vocabulaire au glossaire Shopopop

## Exemple

**Titre** : Notification de disponibilité d'un créneau

En tant que shopper,
Je veux recevoir une notification quand un créneau de livraison se libère dans ma zone,
Afin de ne pas rater des opportunités de mission.

**Critères d'acceptance :**
- Given je suis inscrit aux notifications pour la zone X
- When un créneau se libère dans cette zone
- Then je reçois une notification push dans les 5 minutes
- And la notification contient le créneau, la zone et la rémunération estimée
- Given je n'ai pas activé les notifications
- Then je ne reçois aucune notification
