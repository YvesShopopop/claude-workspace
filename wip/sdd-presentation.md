# SDD — Spec Driven Development
## Présentation à l'équipe produit

---

## Slide : Le Vibe Coding

**Gauche — C'est quoi**
- Décrire ce qu'on veut en langage naturel → l'IA génère le code
- Très peu de structure, très peu de friction
- Idéal pour prototyper et explorer rapidement

**Droite — Les limites**
- Pas de source de vérité partagée (PM / dev / QA)
- L'IA perd le contexte entre les sessions
- Difficile à auditer et à faire évoluer
- Ne passe pas à l'échelle sur des features complexes

> 🎤 Le Vibe Coding c'est l'approche naturelle qu'on adopte quand on commence à utiliser l'IA pour coder. Ça marche vraiment — sur des périmètres limités. Le problème apparaît dès qu'on sort du prototype : sans spec commune, chacun a sa version de ce qu'on construit, l'IA repart de zéro à chaque session, et la dette technique s'accumule silencieusement.

---

## Slide : Le Spec Driven Development — L'idée centrale

**Gauche — Idée centrale**
- Garder la puissance de l'IA, encadrer avec de la structure
- La spec devient l'artefact central — pas le code
- Chaque étape produit un document lisible, reviewable, versionnable

**Droite — Memory bank vs Spec**
- **Memory bank** : contexte permanent du projet (product, archi, stack)
- **Spec** : règles de l'incrément en cours, propre à chaque feature
- La memory bank s'enrichit au fil des incréments

> 🎤 Le SDD est la suite logique du Vibe Coding. On garde l'IA au cœur du process, mais on s'impose une discipline : avant de coder, on spécifie. La distinction memory bank / spec est la clé : la memory bank c'est la mémoire long terme du projet, la spec c'est ce qu'on demande à l'IA de faire maintenant.

---

## Slide : Le Spec Driven Development — Les 5 étapes

**Gauche — Les étapes**
- **Specify** → `requirements.md` — ce que le logiciel doit faire, critères d'acceptation
- **Design** → `design.md` — architecture, séquences, choix techniques
- **Tasks** → `tasks.md` — plan d'implémentation découpé et séquencé
- **Implement** → Code — tâche par tâche, guidé par la spec
- **Document** → Mise à jour de la memory bank

**Droite**
- *[Visuel : flow linéaire avec artefacts]*

> 🎤 Ce qui change par rapport au Vibe Coding : on ne passe pas à l'étape suivante sans avoir validé l'artefact de l'étape précédente. C'est ça qui crée la traçabilité et permet de travailler à plusieurs — humains et IA — sur le même périmètre.

---

## Slide : Retour d'expérience — Cas simple (RECI-341 — Modification des seuils de tailles de commandes)

**Gauche — Contexte**
- Feature estimée XS, discovery déjà réalisée
- Objectif de l'atelier : tester le SDD autant que livrer la feature
- 1h avec le Team Lead et un dev
- Un seul écran partagé

**Droite — Comment ça s'est passé**
- Toutes les étapes SDD traversées (requirements → design → tasks → implement → document)
- Team Lead : pilote l'IA
- Yves : répond aux questions métier
- Dev : répond aux questions techniques
- Livrables de l'atelier : les artefacts SDD (requirements.md, design.md, tasks.md) + du code prêt à review
- Suite : review devs → tests QA → mise en prod

> 🎤 Sur ce premier cas, on a délibérément décidé de passer par toutes les étapes, même pour une feature simple, pour expérimenter le process dans son intégralité. Ce qui est frappant : en 1h à trois, on est sorti avec du code — et avec tous les artefacts de la spec. Pas juste un plan, pas juste une idée : une spec complète et du code. Chaque participant avait un rôle clair : le Team Lead pilotait l'IA, je répondais aux questions métier, le dev aux questions techniques. L'IA orchestrait, les humains validaient.

---

## Slide : Retour d'expérience — Cas complexe (RECI-295 — Choix de cotransporteurs favoris)

**Gauche — Contexte**
- Epic estimée à 1-2 sprints en développement classique
- Discovery, maquettes UX et conception technique déjà réalisées en amont
- 5 ateliers en binôme (Yves + dev) : 2×1h et 3×2h
- Dev : pilote l'IA et répond aux questions techniques
- Yves : répond aux questions métier
- Difficultés concentrées sur Specify et Design : beaucoup de questions liées à la complexité du périmètre

**Droite**
- *[Visuel : sdd-flow-reci295.html — flow des 5 étapes avec durées]*

> 🎤 Sur ce cas, tout était prêt en amont — discovery, maquettes, conception technique. Mais la complexité s'est quand même fait sentir : les étapes Specify et Design ont généré beaucoup d'allers-retours. C'est là que le SDD joue son rôle : il force à clarifier les ambiguïtés avant de coder, plutôt que de les découvrir en cours d'implémentation. Le résultat : une epic d'1-2 sprints adressée en une poignée d'ateliers.

---

## Slide : Réflexions — Ce qui fonctionne bien / les limites

**Gauche — Ce qui fonctionne**
- Aligne PM, dev et QA sur un seul artefact avant de coder
- Force à clarifier les ambiguïtés tôt — quand elles coûtent peu
- Rôles clairs dans l'atelier : métier / technique / pilote IA
- La spec devient une documentation vivante du projet
- Applicable même sur des features simples (le process reste léger)

**Droite — Les limites**
- Effort concentré sur Specify et Design : ça demande de la disponibilité
- Nécessite une discovery complète en amont — le SDD ne la remplace pas
- L'IA manque parfois de contexte implicite : la revue humaine reste indispensable
- Risque de glisser vers du Waterfall si on sur-spécifie avant d'avoir assez d'information

> 🎤 Ce qui ressort de ces deux expériences : le SDD ne réduit pas l'effort de réflexion — il le déplace. On pense plus tôt, on code mieux. La vraie valeur c'est l'alignement : tout le monde sait ce qu'on construit, pourquoi, et comment.
