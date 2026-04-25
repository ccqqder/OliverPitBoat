---
title: "Journal de développement de Kana Juku (partie 1) : des chatbots aux agents IA"
date: 2026-02-22T13:16:34.278Z
author: "QQder"
categories:
  - L'Atelier
tags:
  - Application iOS
  - IA sur l'appareil
  - Reconnaissance de l'écriture manuscrite
  - udemie
  - Claude
  - Code Claude
  - Gémeaux
  - Gémeaux cli
  - interface utilisateur rapide
  - KitUI
keywords:
  - Agent IA
  - Code Claude
  - Gémeaux cli
  - Développement iOS
  - développeur indépendant
  - Kana Juku
  - Apprentissage du japonais
  - interface utilisateur rapide
  - IA sur l'appareil
  - opus
  - chatbot
description: "Partager mon expérience de développement de ma première application, Kana Juku — un parcours qui retrace également mon passage des chatbots aux agents IA"
---


# Préface

Kana Juku est la première application que j'ai jamais créée et expédiée sur l'App Store.

Comme c'était mon premier, il y a un arc d'histoire complet à partager.

Cette série couvre le processus de développement, la façon dont j'ai utilisé l'assistance de l'IA et son évolution, le travail avec des ensembles de données publics et les considérations de droits d'auteur, et bien plus encore.

Si d'autres applications ont des histoires remarquables, je les publierai séparément.

Cet article se concentre sur la transition des chatbots vers les agents IA à partir du **4e trimestre 2025**.

Les choses bougent vite dans cet espace, j'ai donc carrément horodaté les moments clés.

## À propos de l'application

Si vous possédez un appareil Apple, n'hésitez pas à le télécharger et à l'essayer.

Plusieurs articles à venir utiliseront également cette application comme exemple d'exécution – des sujets tels que le nettoyage des [ensembles de données ETL](https://etlcdb.db.aist.go.jp/), [Apple Create ML](https://developer.apple.com/machine-learning/create-ml/), [PyTorch](https://pytorch.org/), [VOICEVOX](https://voicevox.hiroshiba.jp/), les grands modèles de langage sur l'appareil, et plus encore.

Kana Juku : [URL](https://apps.apple.com/us/app/%E5%81%87%E5%90%8D%E7%A7%81%E5%A1%BE/id6756785942)

![](/images/IMG_2433.JPG)

***

# Chronologie du développement

### Motivation

Ma famille et moi sommes tous deux intéressés à apprendre le japonais et je souhaitais depuis longtemps une application d'apprentissage du japonais qui réponde parfaitement à nos besoins.

Le problème de ma famille est qu'ils ne lisent pas l'anglais, donc le romaji dans la plupart des manuels et applications n'a aucun sens pour eux.

Pour moi, je voulais vraiment que les kana soient affichés à côté de leurs origines kanji (par exemple, "あ" dérive de "安").

Autre désagrément : j'ai installé le clavier japonais pour une utilisation occasionnelle, mais changer de méthode de saisie chaque jour signifiait un appui supplémentaire pour passer le clavier japonais – une petite friction qui s'additionnait.

### Préparation précoce

**[T4 2024]**

J'étais entre deux emplois à l'époque, j'avais donc la bande passante nécessaire pour suivre les cours [Udemy](https://www.udemy.com/). Depuis que j'ai une certaine expérience avec JavaScript, j'ai commencé avec [React](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih6Kzo2O-SAxUl3zQHHZoSL-kQFnoECDYQAQ&url=https%3A%2F%2Fzh-hant.legacy.reactjs.org%2F&usg=AOvVaw3Q6fqYyboB_gQOnPVX_tbN&opi=89978449) & [Expo](https://expo.dev/).

À ce stade, je suivais le contenu du cours : de simples pages de style Web, ainsi que des extras tels que le GPS, le contrôle de la caméra et la récupération de données à distance.

Mais comme il ne s’agissait pas de l’écosystème natif d’Apple, il y avait de nombreux outils supplémentaires à gérer.

**[T1 2025]**

Après avoir longtemps hésité, j'ai acheté un Mac Mini et je suis entièrement passé au SwiftUI d'Apple. Encore une fois, j'ai appris des cours Udemy.

La plupart de mon temps a été consacré à me familiariser avec les composants et les mises en page de base de l'interface utilisateur, ainsi qu'avec toutes les fonctionnalités fondamentales (persistance des données, récupération de données, intégration de cartes) et leurs équivalents SwiftUI.

SwiftUI est plus moderne et n'est pas aussi étroitement couplé à Xcode qu'UIKit, mais il est également plus difficile de prédire à quoi ressemblera réellement une mise en page SwiftUI. Au début, je m’en souciais trop et j’ai passé beaucoup de temps à expérimenter.

**[T3 2025]**

Comme j'avais un travail de jour et que je ne pouvais coder que le soir – et pas tous les soirs – les progrès étaient lents. En gros, je construisais le squelette de base et je connectais les données en langue japonaise.

Avec une première application, il est difficile de prévoir la forme finale, alors j'ai continué à réviser. Parfois, je revenais pour revoir les vidéos de cours sur les fonctionnalités dont je savais maintenant avoir besoin. Essentiellement, je payais les frais de scolarité.

Jusqu'à présent, à partir du **T1 2024**, les chatbots simples comme ChatGPT étaient déjà d'une grande aide pour le codage.

Mais le cycle copier-coller et devoir expliquer des montagnes de contexte prenaient énormément de temps. Le résultat manquait souvent la cible du premier essai ou dérivait, me renvoyant directement à la boucle copier-coller. Il n’a jamais atteint un cycle de rétroaction positive – il n’a été utile que comme référence d’apprentissage.

À l'époque, l'outil le plus populaire était en fait l'éditeur de curseur avec sa saisie semi-automatique par tabulation, mais il nécessitait un abonnement pour une utilisation significative, donc je **ne l'ai pas essayé**.

Pendant ce temps, Claude gagnait déjà en popularité en tant que meilleur modèle de codage, et Anthropic avait publié Claude Code, un agent IA qui s'exécute sur votre machine locale. Mais encore une fois, cela nécessitait un abonnement, donc je ne l'ai pas essayé.

***

### Passer aux agents IA

**[T4 2025]**

À ce stade, je m'attendais à ne m'abonner qu'à un seul chatbot à la fois, et je venais de passer de ChatGPT à Google Gemini.

Le développement piloté par les spécifications (SDD) était à la mode et Google avait lancé Gemini CLI – leur réponse à Claude Code – alors j'ai finalement **essayé**.

J'ai découvert que les agents éliminaient complètement l'étape de copier-coller, augmentant ainsi considérablement l'efficacité. L’étape consistant à recoller le code et à rechercher les lignes à modifier a également disparu.

J’étais alors convaincu : pour le codage, il faut utiliser un agent, pas un chatbot. Je me suis donc abonné à Claude pour utiliser Claude Code (CC à partir de maintenant).

Le modèle sous-jacent de CC était clairement plus solide. Sa compréhension des conversations et sa capacité à exécuter comme prévu étaient déjà remarquablement fiables.

#### Contrôler l'ordinateur et Opus 4.5

Une fois, le disque de mon Mac Mini était complètement plein et la machine était inutilisable. Je viens de demander à CC quoi faire – de la même manière que je poserais une question sur la page Web d'un chatbot.

CC est revenu avec un plan concret : quels répertoires pourraient être effacés, qu'est-ce qui pourrait être déplacé vers un disque externe, etc.

J'avais peur que cela puisse bloquer mon ordinateur, alors j'ai approuvé chaque étape une à la fois. Finalement, tout s'est bien passé.

Je n'étais pas très familier avec macOS ou l'environnement de build Xcode. C'est à ce moment-là que j'ai réalisé que l'IA comprenait au moins 80 % de *tout* – y compris des choses que je ne connais pas – et qu'être capable d'écrire du code équivaut à peu près à être capable de faire fonctionner un ordinateur.

Parce que CC pouvait contrôler directement la machine, elle se déplaçait librement entre les répertoires, écrivait du code, voyait ses propres erreurs et les corrigeait – une boucle de rétroaction positive entièrement autonome.

La vitesse de développement avec un agent était d'un tout autre niveau, et le fait d'avoir attendu trois mois supplémentaires avant de passer à CC m'a fait me sentir assez idiot.

Le temps perdu était stupéfiant, tant subjectivement qu'objectivement.

Subjectivement : si j'avais adopté les derniers outils plus tôt, les trois mois de travail précédents auraient pu être réalisés en deux à trois semaines.

Objectivement : d'autres personnes utilisant les derniers outils étaient plus productives que moi et expédiaient leurs produits plus tôt.

Mon refus antérieur d’essayer – économisant peut-être une demi-heure de temps d’installation et quelques centaines de dollars de frais d’abonnement – ​​a fini par me faire perdre de vastes périodes de ma vie.

Cela pourrait également expliquer pourquoi tant de gens sont obsédés par la recherche des dernières nouveautés en matière de produits d’IA.

Du moins, c'est comme ça pour moi : je ne peux pas me permettre de ne pas rester au courant des dernières versions. Il s'agit d'une forme de couverture des risques liés à la gestion du temps.

**[24 novembre 2025]**

L'opus 4.5 est sorti. Opus est le modèle phare de Claude, et la version 4.5 venait de sortir.

Au-delà des améliorations significatives des performances dans tous les domaines par rapport à son prédécesseur, la plus grande différence était sa compréhension de l'intention.

L'ancienne version faisait essentiellement exactement ce que vous avez indiqué (ce qui était déjà assez bon, honnêtement). À partir de la version 4.5, après réception de votre demande, elle résumera et planifiera dans une certaine mesure. Sur le plan humain : c'est devenu plus pointu, plus expérimenté.

Vous n’avez plus besoin de préciser quel fichier modifier et comment. Vous pourriez décrire l'objectif final comme celui d'un manager ou d'un cadre, et il le décomposerait et planifierait lui-même les deux prochaines étapes.

Cette capacité de planification a encore amélioré l’efficacité. Comme je l’ai mentionné, l’IA connaît déjà au moins 80 % de tout – elle exécute désormais de manière proactive les prochaines étapes du travail et les fait correctement.

Combiné à cela, j’ai pu opérer à un niveau d’abstraction beaucoup plus élevé. De plus en plus de choses ont été déléguées à CC. Peu à peu, j’ai cessé d’avoir besoin de lire ou de modifier du code moi-même.

Après la sortie de l'Opus 4.5, le débat sur les réseaux sociaux sur la capacité de l'IA à écrire du code a pratiquement pris fin.

Pour les ingénieurs logiciels à temps plein et les professionnels chevronnés, je ne peux pas parler de leur expérience.

Mais par rapport à moi-même : des choses qui m'auraient pris un à deux ans pourraient désormais être réalisées en deux ou trois mois.

Le résultat s’est établi juste au-delà des limites de mes propres connaissances – j’étais en fait le plus gros goulot d’étranglement.

*Fin de la partie 1*
