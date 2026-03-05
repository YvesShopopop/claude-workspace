# Contexte : US Signalement destinataire (RECI-303)

_Dernière mise à jour : 2026-03-05_

## Statut

✅ **Terminé** — L'US et le ticket Jira sont finalisés et validés.

## Liens clés

- **Epic Jira :** [RECI-303 — Modération - Signalement](https://shopopop.atlassian.net/browse/RECI-303)
- **Ticket Jira :** [RECI-330](https://shopopop.atlassian.net/browse/RECI-330)
- **Maquettes Figma :** https://www.figma.com/design/5teEwiLxZ1RLJfH2zq8V37/Tracking---Rating?node-id=1903-32934
- **Fichier US :** `outputs/US-signalement.md`

## Ce qui a été fait

1. Rédaction de l'US `outputs/US-signalement.md` au format court Shopopop (sans critères d'acceptance)
2. Création du ticket Jira RECI-330 dans le projet Recipient, lié à l'epic RECI-303
3. Itérations sur le format du ticket (règles en blocs `---`, Figma dans Besoin, sous-listes imbriquées)
4. Mise à jour du skill `user-stories/SKILL.md` pour intégrer ces améliorations de format
5. Commit des changements (`3110ebf`)

## Décisions métier clés

- **Déclencheur d'accès au signalement :** dès qu'au moins un CTP a reçu les coordonnées du destinataire, c'est-à-dire quand la livraison est réservée à moins d'1h du début du créneau. L'accès est maintenu même si la livraison revient à un statut inférieur.
- **Multi-CTP :** si plusieurs CTPs ont eu accès aux coordonnées, le destinataire choisit lequel signaler.
- **Formulaire :** 3 champs obligatoires — catégorie (liste fixe), commentaire libre, numéro de téléphone (prérempli + indicatif international).
- **Un seul signalement par livraison.**

## Hors scope (cette US)

- Désactivation automatique du compte CTP → équipe BO
- Alerte et traitement par le Service Client → équipe BO
- Communication envoyée au destinataire suite au signalement → US dédiée, en coordination avec l'équipe marketing

## Prochaines étapes éventuelles

- Rédiger l'US pour la communication post-signalement (coordination équipe marketing)
- Rédiger les US côté BO pour la gestion des signalements par le SC
