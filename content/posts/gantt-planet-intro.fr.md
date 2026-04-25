---
title: "Gantt Planet : niche et considérations pour un développeur indépendant"
date: 2026-02-25T06:55:21.349Z
draft: false
categories:
  - L'Observatoire
tags:
  - Développeur indépendant
  - Magasin d'applications
  - Diagramme de Gantt
  - Développement de produits
  - Développement assisté par l'IA
  - projet parallèle
keywords:
  - développeur indépendant
  - Magasin d'applications
  - Diagramme de Gantt
  - Planète de Gantt
  - développement de produits
  - projet parallèle
  - Développement assisté par l'IA
  - Diagramme de Gantt de la vie
  - Visualisation 3D
  - Application iOS
description: "L'App Store comme page d'accueil personnelle d'une nouvelle ère, en utilisant Gantt Planet comme étude de cas"
author: "QQder"
---


![](/images/gantt-planet-cover.jpg)

# Préface

Dans cet article, je parlerai du marché, des ressources, de l'écosystème et du processus de développement du point de vue d'un développeur indépendant.
En guise de plug-in sans vergogne, j'utilise Gantt Planet comme exemple courant : [URL](https://apps.apple.com/us/app/%E7%94%98%E7%89%B9%E6%98%9F%E7%90%83/id6757654373).
J'admets d'emblée qu'il ne s'agit que de mes projets parallèles – la pression est très différente de celle de quelqu'un qui en vit – donc je ne parle ici que de l'approche de recherche.

## L'étincelle et le décrochage

L'idée derrière Gantt Planet était simple : les outils gratuits de diagramme de Gantt, qu'il s'agisse de logiciels de bureau, d'applications mobiles ou d'applications Web, sont tous assez difficiles à utiliser.
Ceux qui semblent en fait décents facturent tous de l'argent, alors j'ai pensé que je créerais simplement ma propre application de diagramme de Gantt.

Il ne m’a pas fallu longtemps avant de réaliser que les choses n’étaient pas si simples :

1. L'affichage d'un diagramme de Gantt de type feuille de calcul sur l'écran d'un téléphone est bien trop étroit
2. Un diagramme de Gantt approprié doit se connecter à une tonne de ressources : courrier électronique, contacts, salles de réunion, etc.

Résoudre l’un ou l’autre de ces problèmes coûte cher. Vous auriez besoin de passer énormément de temps à peaufiner l'interface utilisateur et à concevoir des flux d'utilisation idéaux, tout en acceptant que certains flux de travail ne peuvent tout simplement pas être intégrés et doivent être abandonnés.

En ce qui concerne l'intégration des ressources, vous devrez gérer les connexions pour toutes les principales plates-formes, gérer d'innombrables API et protocoles d'authentification, et tout maintenir à l'avenir.

À ce stade, je me heurte à un mur – et lorsque vous travaillez à une échelle qui ne bénéficie pas d’économies d’échelle, c’est quasiment inévitable.

## Pivot après pivot

Dans des moments comme celui-ci, j’aime prendre chaque facteur et l’étendre d’un pas ou deux vers l’extérieur, à la recherche d’une intersection viable où les choses pourraient réellement fonctionner.

En tant que développeur motivé par un intérêt personnel, « viable » signifie un coût extrêmement faible, ainsi qu'une proposition de valeur petite mais clairement définie.

L’IA m’a aidé à réaliser la première partie – à un coût extrêmement faible.

Quant à la partie valeur, elle est en grande partie auto-définie, bien que faire rebondir les idées sur l’IA puisse également aider à cristalliser les choses.

Pour moi, il s'agit principalement de construire quelque chose que je voudrais réellement utiliser – quelque chose que j'aimerais au moins regarder. Au-delà de cela, si personne d’autre ne l’a fait, il n’existe pas de version gratuite, ou il existe un différenciateur clair, qui compte également comme valeur.

À ce stade, j'ai commencé à me demander : existe-t-il quelque chose qui ressemble à un diagramme de Gantt, mais pas vraiment à un diagramme de Gantt ?

Et puis une image s’est formée dans mon esprit.

Je me suis souvenu que lorsque j'utilise des diagrammes de Gantt, j'ai tendance à placer les éléments les plus importants plus bas.

L’élément le plus bas est généralement la condition globale pour terminer l’ensemble du projet – ou il représente le projet lui-même.

Mais que se passerait-il s’il y avait des éléments même en dessous de cette rangée du bas – des éléments encore plus importants ? Quels seraient-ils ?

Eh bien, il y a beaucoup de choses plus importantes – elles n’ont tout simplement rien à voir avec le travail. Ils parlent de moi. À propos de la vie.

Et c'est ainsi que le déclic s'est produit : je n'allais pas créer un diagramme de Gantt professionnel classique. J'allais créer un **diagramme de Gantt de vie**.

![](/images/gantt-planet-chart-en.png)

## La prochaine étape

J'ai donc décidé de créer un diagramme de Gantt qui s'écarte du cas d'utilisation typique en entreprise.

Cela signifiait commodément que je n'avais plus besoin d'intégrer les services en ligne,

parce que désormais, tout dépendait de l’utilisateur – juste d’eux, et rien d’autre.

Avec cela, j'avais fait un pas de plus et j'avais maintenu le projet en vie pour le moment. Mais cela pourrait-il conduire à suffisamment de substance pour être complet ?

J'ai pensé à l'autogestion et aux choses importantes mais pas urgentes de la vie : elles ont toutes des rythmes et des fréquences.

La santé est importante, c'est pourquoi les entreprises effectuent des contrôles annuels. La famille compte, alors assurez-vous de voir vos proches avant que trop de temps ne passe.

En combinaison avec la nature des diagrammes de Gantt, dans une fenêtre de temps donnée, les éléments se chevauchent le jour en cours.

Et si l’on considère la durée d’une vie entière, chaque élément est potentiellement pertinent aujourd’hui. Cela signifiait que je pouvais tout réduire sur la ligne centrale de l'interface utilisateur.

Cela a résolu le problème de l'interface utilisateur exiguë tout en exprimant un ensemble de valeurs que je trouvais véritablement significatives.

![Vue principale de la chronologie](/images/screenshots/gantt-planet/timeline-en.png)
*La vue chronologique réelle : tous les éléments de la vie convergent vers la ligne centrale du calendrier – voyez tout ce qui compte aujourd'hui en un coup d'œil*

## exhaustivité

L'une des directives d'évaluation de l'App Store est que votre application ne peut pas simplement reproduire ce qu'une page Web en texte brut pourrait faire.

Par exemple, une simple liste de choses à faire peut ne pas réussir. Je devais donc m'assurer que cette application était plus qu'une simple feuille de calcul, sinon Google Sheets pourrait faire la même chose.

Le flux visuel de haut en bas de la feuille de calcul m'a rappelé de creuser vers le bas - comme si chaque jour vous n'effectuiez que le strict minimum de tâches au niveau de la surface. Il existe un idiome chinois, « les gens flottant au-dessus de leur travail », qui reflète parfaitement cet état.

La métaphore d’éléments plus importants situés à des couches plus profondes m’a donné envie de la rendre plus visuelle, plus tangible. L’association immédiate était l’excavation – creuser dans des strates géologiques, l’exploitation minière.

Vint ensuite la question de la mise en œuvre. Dois-je courber légèrement chaque ligne de la feuille de calcul ? Ajouter une distorsion de perspective ?

J'ai réfléchi au contexte de ce diagramme de Gantt de vie – solitaire et introspectif.

L'image qui m'est venue à l'esprit était la suivante : à la surface de la croûte d'une planète, une personne creusant seule. Et puis ça m'a frappé : n'est-ce pas le garçon aux cheveux d'or qui arrose sa rose et apprivoise un renard ?

J'ai donc construit une version 3D du diagramme de Gantt, en utilisant un puits de mine et des pierres précieuses comme représentation visuelle des tâches à accomplir.

Une approche encore plus radicale aurait été de conserver uniquement la version planète, mais compte tenu de la facilité d'utilisation, de la difficulté de révision et du caractère intuitif de la compréhension, j'ai décidé de conserver les deux points de vue.

![](/images/gantt-planet-3d-en.png)

![Vue de la planète 3D](/images/screenshots/gantt-planet/geo-view-en.png)
*Le diagramme de Gantt de la planète 3D — puits de mine et pierres précieuses comme représentations visuelles des objectifs de vie*

## Il manque toujours un bureau

À l'époque où j'étais encore à l'école, je passais beaucoup de temps assis à mon bureau, seul, à étudier ou à écrire.

Utiliser et réfléchir à ce diagramme de Gantt de vie me donnait l'impression que cela me ramenait à ce bureau – celui qui avait longtemps été jeté.

Si j'ai terminé quelque chose que je ne fais qu'une fois tous les trois mois ou une fois par an - ou même un objectif à long terme -

Je pense que j'aimerais vraiment écrire dans un journal, ou peut-être écrire une lettre à un ami proche.

J'ai réalisé qu'il manquait encore à ce diagramme de Gantt un dernier exutoire émotionnel. Mais si j’ajoutais le partage sur les réseaux sociaux, les utilisateurs ne pourraient pas être totalement honnêtes.

Une autre option était la messagerie intégrée à l'application entre les utilisateurs, mais il n'y aurait jamais - maintenant ou dans le futur - suffisamment d'installations pour prendre en charge cela, ou au moins une version Android devrait également être disponible. Quoi qu’il en soit, ce n’était pas nécessaire pour la première version.

La solution la plus cohérente sur laquelle j’ai atterri était la plus polyvalente : un chatbot.

Nourrissez le chatbot avec un tas de classiques littéraires et laissez-le jouer le rôle d'un « arbre creux » – un confident – ​​offrant aux utilisateurs des commentaires réfléchis.

## Pensées finales

Voilà donc le développement du produit et la prise de décision derrière cette application.

On pourrait croire que j'ai continué à changer de direction jusqu'à ce que ce soit terminé, mais en réalité, il y a eu des tonnes d'idées abandonnées et de fonctionnalités rejetées que je n'ai même pas mentionnées.

Au-delà de donner aux amis curieux une fenêtre sur les types de considérations qui entrent en jeu dans le développement de produits,

la dernière chose que je veux souligner - et la réponse au titre - est que le créneau et la considération du développeur indépendant sont les suivants : **faire tout ce qui vous rend heureux !**

Je suis sûr que beaucoup de gens penseront que c'est trop spécialisé ou que cela ne correspond pas à leurs goûts ou à leurs valeurs.

Mais même ainsi, avec un peu de temps et l’aide de l’IA, vous pouvez créer ce que vous voulez et qui n’existe pas encore.

Vous devenez le patron, en décidant de ce qui a de la valeur et de ce qui mérite d'être construit.

Vous devenez le concepteur en choisissant vos mises en page, couleurs, polices et images préférées.

Vous devenez le PM – en décidant comment l’écrire et dans quelle mesure les fonctionnalités doivent être complètes.

L’IA n’en sera que plus forte. Même s'il ne peut pas tout faire aujourd'hui, dans un avenir proche, vous pourrez également profiter de tout cela.

L'App Store est désormais la page d'accueil personnelle d'une nouvelle ère : chacun peut publier sa propre histoire.

Si vous êtes intéressé, suivez ce blog. Je continuerai à partager de vraies expériences et réflexions issues de la publication sur l'App Store.
