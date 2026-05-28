# Scénarios de tests — Compte destinataire (RECI-299)

> **Epic** : [RECI-299 — Compte destinataire : donner au destinataire la possibilité de créer un compte Shopopop](https://shopopop.atlassian.net/browse/RECI-299)
> **Statut epic** : Dev ongoing — **Échéance** : 22/05/2026
> **Périmètre** : recette fonctionnelle (happy path + erreurs principales) avant mise en prod.

---

## Périmètre couvert

| Bloc | Story / Tâche Jira | Statut |
|---|---|---|
| Affichage page tracking selon état de connexion | [RECI-368](https://shopopop.atlassian.net/browse/RECI-368) | En cours |
| Affichage page rating selon état de connexion | [RECI-369](https://shopopop.atlassian.net/browse/RECI-369) | Fermée |
| Création de compte depuis la page de tracking | [RECI-301](https://shopopop.atlassian.net/browse/RECI-301) | En cours |
| Création de compte depuis la page de rating | [RECI-367](https://shopopop.atlassian.net/browse/RECI-367) | À faire |
| Compte déjà existant (gestion 403) | [RECI-477](https://shopopop.atlassian.net/browse/RECI-477) | Qualification |
| Réinitialisation du mot de passe | [RECI-371](https://shopopop.atlassian.net/browse/RECI-371) | Ouvert |
| Compte non lié à la livraison suivie | [RECI-402](https://shopopop.atlassian.net/browse/RECI-402) | Ouvert |
| Déconnexion depuis l'accueil du compte | [RECI-370](https://shopopop.atlassian.net/browse/RECI-370) | Ouvert |

---

## Prérequis & données de test à préparer

Avant de lancer la recette, prévoir un jeu de comptes / livraisons de test couvrant les cas suivants :

- **Destinataire A** — livraison en cours, téléphone unique sur 1 seule adresse email *(éligible à la création de compte)*
- **Destinataire B** — livraison en cours, téléphone associé à plusieurs adresses email *(non éligible)*
- **Destinataire C** — livraison en cours, email de type `*@shopopopmail.*` *(non éligible)*
- **Destinataire D** — compte Shopopop déjà existant
- **Destinataire E** — compte Shopopop existant mais lié à un autre numéro que celui de la livraison suivie (pour RECI-402)
- **Livraison F** — livraison terminée pour tester la page de rating
- **Téléphone de test** capable de recevoir un SMS OTP (réel ou via solution de mock SMS)

Environnements : **staging**. Navigateurs cibles : Chrome desktop + Safari iOS (à minima).

---

## F1 — Page de tracking selon l'état de connexion (RECI-368)

### F1.1 — Affichage non connecté (happy path)
**Préconditions** : destinataire non connecté, livraison valide.
**Étapes** :
1. Ouvrir le lien de tracking d'une livraison en cours.
**Résultat attendu** :
- La page de tracking s'affiche normalement.
- Un bloc d'invitation propose deux actions : *« Créer mon compte »* et *« J'ai déjà un compte »*.

### F1.2 — Clic sur « Créer mon compte » (non connecté)
**Étapes** : depuis F1.1, cliquer sur *« Créer mon compte »*.
**Résultat attendu** : le flux d'inscription se déclenche (cf. F3).

### F1.3 — Clic sur « J'ai déjà un compte » (non connecté)
**Étapes** : depuis F1.1, cliquer sur *« J'ai déjà un compte »*.
**Résultat attendu** : redirection vers la page de connexion Keycloak (champ email + mot de passe).

### F1.4 — Affichage connecté
**Préconditions** : destinataire connecté à son compte.
**Étapes** : ouvrir le lien de tracking.
**Résultat attendu** :
- Le bloc d'invitation n'apparaît plus.
- Le prénom du destinataire est affiché à la place.

### F1.5 — Clic sur le prénom
**Étapes** : depuis F1.4, cliquer sur le prénom.
**Résultat attendu** : redirection vers la page d'accueil du compte destinataire.

---

## F2 — Page de rating selon l'état de connexion (RECI-369)

### F2.1 — Affichage non connecté
**Préconditions** : livraison terminée, destinataire non connecté.
**Étapes** : ouvrir le lien de rating.
**Résultat attendu** : page de rating affichée + bloc *« Créer mon compte »* / *« J'ai déjà un compte »*.

### F2.2 — Clic « Créer mon compte » depuis rating
**Résultat attendu** : flux d'inscription déclenché (cf. F4).

### F2.3 — Clic « J'ai déjà un compte » depuis rating
**Résultat attendu** : redirection vers la page de connexion Keycloak.

### F2.4 — Affichage connecté
**Préconditions** : destinataire connecté.
**Résultat attendu** : prénom affiché à la place du bloc d'invitation ; clic redirige vers la page d'accueil du compte.

---

## F3 — Création de compte depuis la page de tracking (RECI-301)

### F3.1 — Inscription complète (happy path) — Destinataire A
**Étapes** :
1. Depuis la page de tracking, cliquer sur *« Créer mon compte »*.
2. Vérifier que le **téléphone** et **l'email** sont pré-remplis avec les données de la livraison.
3. Modifier l'email (optionnel) → vérifier que c'est possible.
4. Saisir un mot de passe respectant les contraintes : 8+ caractères, 1 maj, 1 min, 1 chiffre, 1 spécial.
5. Cocher les consentements RGPD (CGU + politique de confidentialité).
6. Valider → réception d'un OTP par SMS sur le numéro pré-rempli.
7. Saisir l'OTP correct.

**Résultat attendu** :
- Le compte est créé dans Keycloak.
- Le destinataire est redirigé vers la page de connexion Keycloak (pas d'autologin).

### F3.2 — Téléphone non modifiable
**Résultat attendu** : le champ téléphone est en lecture seule (pré-rempli, non modifiable).

### F3.3 — Mot de passe non conforme
**Étapes** : saisir successivement un mot de passe trop court, sans majuscule, sans chiffre, sans caractère spécial.
**Résultat attendu** : un message d'erreur clair indique la règle non respectée, le formulaire n'est pas soumis.

### F3.4 — Consentement RGPD non donné
**Étapes** : ne pas cocher les CGU et/ou la politique de confidentialité.
**Résultat attendu** : la création de compte est bloquée tant que les deux cases ne sont pas cochées. Liens CGU + politique de confidentialité fonctionnels.

### F3.5 — Échec OTP — code erroné
**Étapes** : saisir un OTP invalide.
**Résultat attendu** : message d'erreur, possibilité de retenter.

### F3.6 — Échec OTP — renvoi du SMS
**Étapes** : déclencher un renvoi de SMS.
**Résultat attendu** : un nouveau SMS est reçu ; vérifier la limite de retry (cf. RECI-464).

### F3.7 — Email modifié → format invalide
**Étapes** : remplacer l'email pré-rempli par une chaîne sans `@` ou avec un domaine invalide.
**Résultat attendu** : message d'erreur de format, soumission bloquée.

### F3.8 — Destinataire non éligible (téléphone multi-emails)
**Préconditions** : Destinataire B.
**Résultat attendu** : la création de compte n'est pas proposée OU le flux est bloqué avec message clair *(à confirmer côté front selon implémentation)*.

### F3.9 — Destinataire non éligible (shopopopmail)
**Préconditions** : Destinataire C.
**Résultat attendu** : idem F3.8.

---

## F4 — Création de compte depuis la page de rating (RECI-367)

Le flux est identique à F3 mais déclenché depuis la page de rating.
Rejouer au minimum :

### F4.1 — Inscription complète depuis rating (happy path)
Mêmes étapes que F3.1 mais point d'entrée = page de rating.
**Résultat attendu** : compte créé + redirection vers la page de connexion Keycloak.

### F4.2 — Cohérence des règles de validation
Rejouer F3.3 (mot de passe) et F3.4 (RGPD) depuis le rating pour vérifier la cohérence des règles.

---

## F5 — Compte déjà existant (RECI-477)

### F5.1 — Tentative d'inscription avec un email/téléphone déjà associé à un compte
**Préconditions** : Destinataire D (compte existant).
**Étapes** : déclencher le flux d'inscription, aller jusqu'à la soumission.
**Résultat attendu** :
- Le backend renvoie une 403.
- Le front affiche une page dédiée *« Vous avez déjà un compte »*.
- Un lien *« Se connecter »* est présent et redirige vers Keycloak.
- Un lien *« Mot de passe oublié »* est présent et redirige vers le flux Keycloak correspondant.

---

## F6 — Connexion au compte (Keycloak)

### F6.1 — Connexion réussie
**Étapes** : depuis la page Keycloak, saisir email + mot de passe valides.
**Résultat attendu** : redirection vers la page d'accueil du compte destinataire.

### F6.2 — Mot de passe erroné
**Résultat attendu** : message d'erreur Keycloak, pas d'accès au compte.

### F6.3 — Email inconnu
**Résultat attendu** : message d'erreur Keycloak.

---

## F7 — Réinitialisation du mot de passe (RECI-371)

> Flux entièrement délégué à Keycloak. Tester surtout le déclenchement et le retour vers Shopopop.

### F7.1 — Flux complet (happy path)
**Étapes** :
1. Sur la page de connexion Keycloak, cliquer sur *« Mot de passe oublié »*.
2. Saisir un email de compte existant.
3. Ouvrir l'email reçu, suivre le lien.
4. Définir un nouveau mot de passe respectant les contraintes.
5. Se connecter avec le nouveau mot de passe.

**Résultat attendu** : connexion réussie avec le nouveau mot de passe.

### F7.2 — Email inconnu
**Résultat attendu** : comportement Keycloak standard (pas de fuite d'information sur l'existence du compte — à vérifier).

---

## F8 — Compte non lié à la livraison suivie (RECI-402)

### F8.1 — Connexion depuis tracking avec compte sur autre téléphone
**Préconditions** : Destinataire E (compte existant lié à un téléphone ≠ téléphone de la livraison suivie).
**Étapes** :
1. Ouvrir le lien de tracking de la livraison.
2. Cliquer sur *« J'ai déjà un compte »*.
3. Se connecter avec les identifiants du compte E.

**Résultat attendu** : *à valider avec le ticket — comportement cible à confirmer* (afficher la livraison suivie comme livraison externe ? message d'avertissement ? redirection ?).

### F8.2 — Déjà connecté à l'ouverture du lien de tracking
**Préconditions** : destinataire déjà connecté, sur un compte non lié à la livraison du lien.
**Étapes** : ouvrir le lien de tracking.
**Résultat attendu** : *idem F8.1 — comportement à confirmer*.

> ⚠️ Cette story est encore en statut *Ouvert* — les critères d'acceptation ne sont pas finalisés. À aligner avec Pierre/Robert avant la recette.

---

## F9 — Déconnexion depuis l'accueil du compte (RECI-370)

### F9.1 — Déconnexion depuis l'accès via tracking
**Préconditions** : destinataire connecté, arrivé sur la page d'accueil du compte via la page de tracking.
**Étapes** : cliquer sur l'action de déconnexion.
**Résultat attendu** : redirection vers la **page de tracking** d'origine, en état **non connecté** (bloc d'invitation à la création de compte visible).

### F9.2 — Déconnexion depuis l'accès via rating
**Préconditions** : idem mais via la page de rating.
**Résultat attendu** : redirection vers la **page de rating** d'origine, en état non connecté.

---

## À clarifier avant recette

- **F3.8 / F3.9** : confirmer le comportement exact pour les destinataires non éligibles (bloc d'invitation masqué ? flux bloqué avec message ?).
- **F8** : critères d'acceptation à finaliser sur RECI-402 (encore *Ouvert*).
- **F3.6** : limite de retry SMS — voir [RECI-464](https://shopopop.atlassian.net/browse/RECI-464) en cours de revue.
- **Templates Keycloak** (login, registration, forgotten password) : vérifier le branding Shopopop ([RECI-415](https://shopopop.atlassian.net/browse/RECI-415), [RECI-416](https://shopopop.atlassian.net/browse/RECI-416)).
