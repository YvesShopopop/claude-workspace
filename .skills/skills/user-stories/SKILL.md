# Skill : Rédaction de User Stories

## Description
Rédige des User Stories claires et bien structurées, en suivant le template et les standards de Shopopop.

## Instructions pour Claude

**Avant toute rédaction**, lire obligatoirement :
- `.context/shopopop.md` — vocabulaire et parties prenantes (⚠️ "cotransporteur", pas "shopper")
- `.context/produit.md` — contexte produit
- `.context/destinataire.md` — profil du destinataire

## Template

```
**Titre :** [Titre court et descriptif]
**Epic :** [Lien vers l'epic Jira]

**Contexte**
[Description brève du contexte]

**Besoin**
[Phrase décrivant le besoin général.]

🎨 [Lien Figma] _(si des maquettes existent)_

---

[Règle métier 1]
- [Sous-règle ou option, si nécessaire]
- [Sous-règle ou option]

---

[Règle métier 2]

---

[Règle métier 3]
_(Élément hors scope — préciser l'équipe responsable.)_
```

## Règles

1. Le titre doit être court et descriptif
2. Le lien vers l'epic est obligatoire
3. Le contexte est bref — il pose le cadre, pas plus
4. Le besoin contient les règles métier claires, rédigées en langage naturel
5. Chaque règle métier est un bloc distinct, séparé par `---` pour aérer la lecture
6. Quand des maquettes existent, ajouter le lien Figma (🎨) dans Besoin, juste après la phrase du besoin général, avant les règles
7. Les listes d'options (ex : catégories d'un formulaire) sont en sous-bullet points imbriqués sous la règle concernée
8. Pas de critères d'acceptance dans l'US — ils doivent découler naturellement des règles métier
9. Les dépendances entre tickets ("is blocked by", "blocks"...) sont gérées via les liens Jira, pas dans le corps de l'US
10. Si le besoin est flou, poser des questions avant de rédiger
11. Respecter strictement le vocabulaire de `shopopop.md`

## Exemple

**Titre :** Notification de disponibilité d'un créneau
**Epic :** [RECI-XXX](https://shopopop.atlassian.net/browse/RECI-XXX)

**Contexte**
Les cotransporteurs ratent parfois des opportunités de mission faute de visibilité sur les créneaux qui se libèrent dans leur zone.

**Besoin**
Lorsqu'un créneau de livraison se libère dans une zone surveillée par un cotransporteur, celui-ci doit être notifié rapidement pour pouvoir s'en saisir.

🎨 [Lien Figma](https://www.figma.com/...)

---

Un cotransporteur ne reçoit des notifications que s'il s'est inscrit pour la zone concernée.

---

La notification doit être envoyée dans les 5 minutes suivant la libération du créneau.

---

Elle doit contenir les informations essentielles :
- Créneau
- Zone
- Rémunération estimée

---

Un cotransporteur qui n'a pas activé les notifications ne reçoit rien.
