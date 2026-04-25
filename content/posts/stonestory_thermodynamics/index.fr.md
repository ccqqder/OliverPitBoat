---
title: "Rêve du simulateur de chambre rouge : thermodynamique et choix artistique"
date: 2026-03-29T15:28:32.157Z
draft: false
categories:
  - L'Atelier
tags:
  - Thermodynamique
  - Rêve de la Chambre Rouge
  - LLM
  - Moteur de règles
  - Simulation littéraire
keywords:
  - thermodynamique
  - Rêve de la Chambre Rouge
  - 紅樓夢
  - Simulateur de la Chambre Rouge
  - LLM
  - grand modèle de langage
  - moteur de règles
  - Cao Xueqin
  - analyse structurée
  - prédiction littéraire
  - Douze beautés de Jinling
  - verset prophétique
  - choix artistique
  - moteur de simulation
description: "Ce qui a changé, c’est que la productivité est soudainement devenue beaucoup plus élevée. Ce que le rêve du simulateur de chambre rouge vise à faire, c'est, avec une telle productivité à portée de main, d'utiliser des méthodes structurées traditionnelles pour produire et accumuler rapidement des résultats avec un minimum d'effort humain."
author: "QQder"
---

URL de l'application : [LIEN](https://apps.apple.com/tw/app/%E7%B4%85%E6%A8%93%E5%A4%A2%E6%A8%A1%E6%93%AC%E5%99%A8/id6759855416)

## Préface

Le point clé du volet précédent

était de considérer le texte comme fondamentalement symbolique --

l'astronomie, l'hydrologie, les sciences humaines... tous les « wen » (文, modèle/texte) du ciel, de la terre et de l'humanité.

Le texte cartographie le monde et la pensée de manière rentable,

devenant notre principal outil pour comprendre et interagir avec la réalité objective.

Une fois que vous avez compris cela, vous réalisez que

bien que les LLM (Large Language Models) ne soient essentiellement que des prédicteurs de prochain jeton,

une fois que leur capacité atteint un certain niveau, ils deviennent des instruments de qualité nucléaire d’importance nationale.

Leur importance m'a donné envie de vérifier leurs capacités

et de le faire à plusieurs reprises à mesure qu’ils s’améliorent avec le temps.

Une référence presque parfaite pour cela est *Dream of the Red Chamber* (紅樓夢, *Hong Lou Meng*).

Supposons qu'il existe un LLM omniscient et omnipotent --

il pourrait prendre les 80 premiers chapitres originaux de Cao Xueqin du *Rêve de la Chambre Rouge* comme entrée et sortie des chapitres suivants.

Mais comme les données de formation LLM sont limitées,

c'est comme un puzzle de Sudoku avec trop peu de nombres donnés – la réponse ne peut pas être déterminée avec certitude.

Ce que les LLM actuels peuvent faire, c'est produire à très haut débit dans le cadre de ce qu'ils comprennent.

Ce que le *Dream of the Red Chamber Simulator* vise à faire, c'est, avec une telle productivité à portée de main,

utiliser des méthodes structurées traditionnelles pour produire et accumuler rapidement des résultats avec un minimum d’effort humain.

## Hypothèses

Nous avons besoin de quelques hypothèses, préjugés et théories pour rendre la tâche de prédire la fin suffisamment réalisable et mécanique.

Lorsqu’il s’agit de prédiction précise, mon intuition se tourne vers la physique classique, en particulier la thermodynamique.

Dans un système fermé, si l'on précise les conditions initiales et les lois régissant,

l'évolution d'un système thermodynamique est prévisible et déterministe.

Une autre hypothèse est que les capacités LLM continueront de s'améliorer,

mais dans un avenir prévisible, nous n'obtiendrons pas de données d'entraînement supplémentaires de la dynastie Qing ou de Cao Xueqin lui-même.

Par conséquent, nous pouvons établir un flux de travail structuré que les LLM actuels et futurs peuvent exécuter.

### Conditions initiales

Les conditions initiales sont principalement des données extraites du roman original.

Nous utilisons désormais les LLM pour effectuer ce qui était auparavant un travail à forte intensité de main-d'œuvre.

Dans le passé, les coûts du travail humain étaient trop élevés et impliquer davantage de personnes sur le problème ne pouvait pas réduire les délais.

Si vous êtes arrivé à mi-chemin et que vous souhaitez modifier les règles d’extraction et recommencer, ce n’est tout simplement pas pratique.

Le temps et le coût ne sont plus des obstacles ; la qualité de l'extraction dépend désormais de la capacité du modèle.

Par exemple, j'ai extrait :

- Profils de personnages clés, dossiers de personnalité, généalogies familiales ;

- Des instantanés par chapitre de l'état économique, social, émotionnel, de santé et interpersonnel de chaque personnage dans les 120 chapitres ;

- Une carte spatiale de base du domaine Jia (賈) avec des métadonnées spatiales ;

- Tous les enregistrements de dialogues, corpus de poésie...

L’approche consistait à commencer par une extraction large, pas encore rigoureuse, qui permet au moins d’atteindre une couverture élevée – en garantissant que chaque morceau de texte est classé dans une catégorie.

### Lois applicables

Je divise les lois régissantes en deux types selon mon propre jugement : les règles mondiales fondamentales et la volonté artistique de l'auteur.

C'est certes arbitraire, mais sans un tel jugement, le travail ne peut pas avancer du tout.

Les règles mondiales incluent, sans s'y limiter :

- Société : hiérarchie de classes, dynamiques de pouvoir, relations maître-serviteur, mariage ;

- Économie : revenus et dépenses, dette, risque de confiscation des biens ;

- Culture : convenance confucéenne, fêtes, valeurs féodales ;

- Psychologie : émotions des personnages, comportement axé sur la personnalité, conflits internes ;

- Politique : faveur impériale, dynamique de cour, forces extérieures…

La volonté artistique est précisément ce qui fait du *Rêve de la Chambre Rouge* -- outre le fait qu'il lui manque une fin définitive -- une cible de prédiction idéale.

Cao Xueqin a intégré des indices sur le destin des personnages tout au long du roman, dès le début.

L'exemple le plus emblématique est le 判詞 (versets prophétiques/poèmes de jugement) des 十二金釵 (Douze beautés de Jinling), qui préfigurent explicitement le destin de la protagoniste féminine et deutéragoniste :

> 可嘆停機德，堪憐詠絮才。玉帶林中掛，金簪雪裡埋。

*(Comme c'est lamentable, sa vertu d'arrêter le métier à tisser ; comme c'est pitoyable, son talent à chanter les chatons de saule. Une ceinture de jade pend dans la forêt ; une épingle à cheveux dorée est enfouie dans la neige.)*

### Moteur de règles

Compte tenu des conditions initiales et des lois applicables, comment les appliquer ?

L’approche la plus idéale serait de créer un moteur physique 3D similaire à un moteur de jeu, dans lequel chaque personnage possède uniquement les informations qu’il connaît, et de laisser un chatbot IA jouer le rôle de chaque personnage comme un acteur jouant un rôle.

Mais d’abord, le coût serait trop élevé et ne ferait qu’augmenter le spectacle : nous n’introduireions pas de nouvelles informations et le moteur 3D ne produirait pas de nouveaux résultats.

Deuxièmement, nous n’exécutons pas de simulation de dynamique des fluides en soufflerie ; nous essayons de deviner ce que Cao Xueqin avait en tête. S’en tenir au niveau textuel est suffisant pour l’instant.

Sur la base des données extraites précédemment, nous dérivons un ensemble de sujets et de règles informatiques.

En pratique, il s'agit du processus traditionnel d'évaluation des preuves, de la confiance et des ajustements additifs/soustractifs pour déterminer si un événement se produit --

rendu systématique, reproductible, modifiable et exhaustif par force brute.

Les étapes de simulation pour chaque tour sont :

1. Traiter les effets retardés -- vérifier les effets en attente ; appliquez ceux qui ont atteint leur chapitre dû.

2. Évaluez toutes les lois - vérifiez les prémisses de chaque loi pour voir si toutes sont satisfaites (ignorez celles avec confiance \ < 0,3).

3. Résolution des conflits : les lois déclenchées simultanément peuvent se contredire ; décider lequel gagne.

4. Appliquer des effets : ceux qui ont un retard vont dans la file d'attente ; ceux sans modifier directement l’état.

5. Instantané - compresse l'état actuel dans un vecteur numérique.

6. chapitre += 1

Un exemple complet – la mort de Lin Daiyu (林黛玉) au chapitre 98 – est annexé à la fin de cet article.

### Résumé du flux de travail

Parmi les nombreux composants du flux de travail ci-dessus,

si les **données extraites** sont académiquement rigoureuses, si les **règles** sont raisonnables et applicables, si les **étapes de simulation** sont solides --

rien de tout cela n’est d’une importance cruciale, car chaque pièce peut être améliorée et régénérée indépendamment.

D'un point de vue génie logiciel, mon objectif est de faire en sorte que ce moteur fonctionne bien au niveau de l'interface,

et affiner continuellement les résultats de prévision à mesure que davantage d’informations sont incorporées et que la méthodologie s’améliore.

### Résultats actuels : comparaison parallèle objective et subjective

Ici, je dois introduire une autre méthodologie que je m'impose pour permettre une comparaison structurée :

divisant les couches du moteur d'inférence en deux parties principales : les conditions objectives et le choix artistique.

![](</images/Simulator Screenshot - iPhone 17 - 2026-03-30 at 22.45.27.png>)![](</images/Simulator Screenshot - iPhone 17 - 2026-03-30 at 22.45.20.png>)

#### Conditions objectives

Le contexte historique de l’époque à laquelle le roman a été écrit – ses personnages, ses décors, son système féodal, son économie, etc. – constitue la première couche de conditions objectives. Cela peut délimiter toute la portée de ce que l’histoire est capable de contenir. Nous avons déjà extrait quelques lois objectives basées sur le contexte historique et la littérature académique adaptés à la période.

À l’inverse, tout ce qui existait réellement à cette époque pourrait, en théorie, apparaître et influencer l’histoire.

Par exemple, le roman présente déjà certains objets modernes occidentaux tels que des horloges à sonnerie automatique et des montres de poche. Et si les armes à feu occidentales apparaissaient et devenaient un moteur important du complot ?

L’exploration exhaustive de ces possibilités objectives de premier niveau constitue une direction pour les travaux futurs et pourrait produire un effet « raisonnable mais au-delà des attentes ».

#### Choix artistique

La deuxième couche est la culture de ce monde fictif par l'auteur Cao Xueqin (曹雪芹).

De nombreux personnages et la trajectoire globale de la famille portent une lourde coloration fataliste.

Les innombrables poèmes et métaphores du roman – ainsi que les annotations marginales d’un ami qui aurait lu la fin – le suggèrent.

Par conséquent, nous pouvons utiliser le parcours et les expériences de vie de l'auteur

pour déduire quel sort il a choisi pour ses personnages,

et révéler ainsi les valeurs qu'il souhaitait réellement exprimer.

#### Comparaison croisée

À partir de là, nous pouvons considérer la suite de Gao E (高鶚) comme l'œuvre du « joueur » le plus avancé à ce jour.

Ce qu'il a fait est essentiellement la même chose que je fais maintenant :

basé sur les personnages et le décor du roman, essayant de deviner au plus près les choix artistiques de Cao Xueqin.

De plus, Gao E a complété la fin existante, ce qui a considérablement augmenté la diffusion du roman, et sa version a été largement acceptée – nous plaçons donc sa version dans une position parallèle à des fins de comparaison.

#### Simulation réaliste

Et si on supprimait tout traitement artistique et ne conservait que des lois objectives, laissant l'histoire évoluer naturellement ?

Le résultat est que la plupart des événements de l’intrigue ne se produiraient pas en l’espace de 120 chapitres. Le récit serait moins dramatique et contiendrait moins de tragédies.

## Méthodes pour améliorer la qualité des prévisions

- Réextraire le texte lorsque les capacités LLM s'améliorent

- Plus d'intervention humaine pour affiner et expérimenter différentes invites

- Faites appel à des spécialistes de la redologie (紅學, l'étude académique du *Rêve de la Chambre Rouge*) ou à des historiens pour vous aider à nettoyer les données et à ajuster la logique du moteur.

- Incorporer du matériel nouvellement découvert ou non numérisé (le cas échéant) dans la formation

- Expérimenter des méthodologies alternatives

- Établissez un flux de travail fixe et laissez les agents IA affiner et produire en permanence de nombreuses versions ; puisqu'il n'y a pas de critère de terminaison clair, la qualité ne peut être jugée que manuellement

## Conclusion

En raison des contraintes des données existantes et pré-entraînées, et de la forte cohérence interne de *Dream of the Red Chamber* en tant qu'œuvre d'art,

Il est peu probable que les prédictions de Deus Ex Machina se réalisent. Ce que nous voyons à la place, ce sont des différences comparatives internes :

par exemple, la confiscation et le déclin de la famille Jia sont voués à se produire de toute façon ; la différence réside uniquement dans le timing.

### Une réflexion finale

Ce type de travail aurait initialement nécessité au moins un à deux ans et au moins une personne à temps plein.

Je peux désormais utiliser mes heures après le travail pour jouer un rôle professionnel différent – ​​ce qui satisfait également un regret du moment où la pression financière m'a obligé à changer de domaine il y a des années.

J'espère que partager le processus de réflexion derrière la construction du *Dream of the Red Chamber Simulator* vous sera utile,

et j’espère que les sciences sociales – et pas seulement l’informatique et les sciences naturelles – bénéficieront des progrès rapides de l’IA.

***

### Annexe : Exemple de processus de simulation complet

Chapitres 97-98, « La mort de Lin Daiyu » (黛玉之死) – une présentation complète des six étapes (le contenu suivant a été généré par l'IA) :

---

Exemple : Chapitre 97 -- Le complot Switcheroo (掉包計) -> Brûler des manuscrits et rompre les liens (焚稿斷情) -> La mort de Daiyu

État de fond (entrée dans le chapitre 97)

Après plus d'une douzaine de chapitres de déclin cumulé, l'état de Lin Daiyu est le suivant :

agent.林黛玉 : santé=0,12, humeur=0,08, isolement=0,72, tragédie\_risque=0,95, vivant=Vrai

agent.賈寶玉 : moine\_tendency=0,35, humeur=0,20

économie : dette\_ratio=0,65

politique : famille\_decides\_marriage=True

relation.賈寶玉::林黛玉: mariage\_probabilité=0,15

relation.賈寶玉::薛寶釵: mariage\_probabilité=0,72

Pourquoi la santé de Daiyu est-elle passée d'un niveau initial de 0,35 à 0,12 ? Parce que cette loi a déclenché silencieusement chaque chapitre :

▎ PSY\_E1\_DAIYU\_DECAY "La santé de Daiyu se dégrade lentement"

▎ Prémisse : santé > 0,0 ET isolement > 0,3 ET vivant = Vrai -> Effet : santé inférieure à 0,017

▎ À -0,017 par chapitre, sur une douzaine de chapitres, cela équivaut à une fuite chronique mortelle.

---

① Effets retardés du processus

Vérifiez la file d'attente en attente\_effects. Supposons que ce qui suit ait été déclenché au chapitre 13 :

▎ FATE\_010 "Le rêve sur le lit de mort de Qin Keqing : le pic prédit la chute" delay\_chapitres : 20

Son effet, economy.sending\_pression add 0.1, est déjà arrivé à échéance et a été exécuté au chapitre 33. La file d'attente est maintenant vide. Sauter.

---

② Évaluez les 369 lois

Le moteur analyse chaque loi dans l'ordre. Les lois clés qui déclenchent ce chapitre :

Loi A -- VAR\_MARRIAGE\_SWAP "Le Switcheroo : épouser secrètement Baochai à la place" conf=0.95

Vérification des locaux :

```
agent.林黛玉.health \< 0,15 -> 0,12 \< 0,15 ✅

agent.林黛玉.alive == Vrai -> Vrai ✅

Politics.family\_decides\_marriage -> Vrai ✅

relation.寶玉::黛玉.marriage\_probability \< 0,5 -> 0,15 \< 0,5 ✅

Tout est passé -> 🔥 Déclenché !
```

Loi B -- PSY\_E1\_DAIYU\_DECAY "Dégradation de la santé de Daiyu" conf=0.9

```
santé > 0,0 -> 0,12 > 0 ✅

isolement > 0,3 -> 0,72 > 0,3 ✅

vivant == Vrai ✅

-> 🔥 Déclenché !
```

Loi C -- VAR\_MARRIAGE\_DAIYU "Le lien de pierre et de bois : Baoyu et Daiyu se marient" conf=0.9

```
relation.寶玉::黛玉.marriage\_probability > 0.7 -> 0.15 > 0.7 ❌

-> Non déclenché (probabilité de mariage Baoyu-Daiyu trop faible)
```

Ce chapitre déclenche également simultanément plus d’une douzaine d’autres lois (déclin économique, risque politique, etc.), mais celles ci-dessus sont celles qui concernent directement Daiyu.

---

③ Résolution des conflits

VAR\_MARRIAGE\_SWAP, VAR\_MARRIAGE\_NORMAL\_BAOCHAI et VAR\_MARRIAGE\_DAIYU appartiennent au même groupe de variantes\_(les résultats du mariage s'excluent mutuellement).

Seul VAR\_MARRIAGE\_SWAP a réussi la vérification des prémisses, il n'y a donc pas de conflit réel. Cependant, si Daiyu était déjà mort (alive=False), alors VAR\_MARRIAGE\_NORMAL\_BAOCHAI se déclencherait à la place de la version switcheroo --

ce serait un chemin évolutif différent.

L'effet de PSY\_E1\_DAIYU\_DECAY est additif (sub), il n'entre donc pas en conflit avec d'autres lois. Tous les effets sont conservés.

---

④ Appliquer des effets

Les effets de la loi A s'exécutent immédiatement (délai=0) :

déclencheur de mariage\_event BAOYU\_MARRIED\_BAOCHAI -> fate\_flags\["BAOYU\_MARRIED\_BAOCHAI"] = True

relation.寶玉::寶釵.marriage\_probability set 1.0 -> 1.0

agent.賈寶玉.mood sub 0,5 -> 0,20 -> 0,00 (pince)

agent.賈寶玉.monk\_tendency ajouter 0,3 -> 0,35 -> 0,65

agent.林黛玉.health sub 0.1 -> 0.12 -> 0.02

Effets de la loi B :

agent.林黛玉.health sub 0,017 -> 0,02 -> 0,003

À ce stade, la santé de Daiyu = 0,003, proche de zéro.

---

⑤ Instantané

Compressez l'état actuel du monde en un vecteur numérique :

instantané = {

```
économie\_vecteur : \[0,42, 0,82, 0,65, 0,55, 0,80, 0,35],

agent\_vecteurs : {

"林黛玉": \[0,003, 0,08, 0,10, 0,00, 0,30, 0,00, 0,72, 0,95],

"賈寶玉": \[0,80, 0,00, 0,30, 0,72, 0,80, 0,65, 0,42, 0,92],

...

},

politique\_vecteur : \[0.0, 0.60, 0.75]
```

}

Ce vecteur sera ensuite comparé via la distance euclidienne au vecteur réel du chapitre 97 dans actual\_checkpoints.json.

---

⑥ chapitre = 98

Entrez dans le chapitre suivant. À ce stade, la santé de Daiyu = 0,003 et BAOYU\_MARRIED\_BAOCHAI = True.

Lorsque le chapitre 98 exécute à nouveau l'étape ②, deux lois mortelles se déclenchent simultanément :

▎ VAR\_DAIYU\_HEARTBREAK "Brûler des manuscrits, couper les liens : Daiyu meurt de chagrin" conf=0.95

▎ santé ≤ 0,05 -> 0,003 ≤ 0,05 ✅

▎ BAOYU\_MARRIED\_BAOCHAI -> Vrai ✅

▎ -> déclencheur de mort\_event FATE\_DAIYU\_DEATH

▎ -> moine\_tendency ajouter 0,4 -> Baoyu 0,65 -> 1,0 (pince)

▎ -> ensemble vivant Faux

Ensuite, SYS\_E19\_ZERO\_DAIYU se déclenche (checkpoint.FATE\_DAIYU\_DEATH = True), mettant à zéro tous les attributs de Daiyu.

Quelques chapitres plus tard, la tendance moine\_de Baoyu a atteint 1,0 et son humeur ≤ 0,15, déclenchant VAR\_MONK\_DESPAIR "Tous les espoirs éteints : Baoyu renonce au monde" (萬念俱灰：寶玉出家).
