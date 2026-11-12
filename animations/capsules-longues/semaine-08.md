# Semaine 8 : Écrire un prompt que l’on peut tester

## Préparation

**725 mots ; durée indicative 06:46 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:53 à 07:18.**

Fichier audio complet possible : `semaine-08.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Partir d’une demande observable

Repère provisoire : 00:00 à 00:58. Audio : `semaine-08-01.wav`.

### Narration

Un prompt utile commence par une tâche suffisamment claire pour que nous puissions évaluer le résultat. « Fais un bon résumé » laisse plusieurs questions ouvertes : bon pour qui, de quelle longueur et avec quelles informations ? Nous allons transformer cette demande en une consigne testable. L’exemple porte sur un résumé de règlement de cours destiné à un étudiant qui cherche les modalités de remise. Nous préciserons le texte fourni, les éléments attendus et les limites. L’objectif n’est pas de trouver une formule magique. Il est de réduire l’ambiguïté, puis de vérifier sur des exemples si les réponses répondent réellement au besoin.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : résume ce texte → pour qui ? → quel contenu ? → quel résultat ?.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Définir la tâche et le destinataire

Repère provisoire : 00:58 à 01:58. Audio : `semaine-08-02.wav`.

### Narration

Nous pouvons commencer ainsi : « À partir du passage fourni, résume les modalités de remise pour un étudiant du cours. » Cette phrase identifie la source, l’action et le public. Nous ajoutons ensuite les éléments importants : date limite, format du fichier, lieu de dépôt et procédure en cas de difficulté. Si l’un de ces éléments n’apparaît pas dans le passage, le modèle doit l’indiquer plutôt que le compléter de mémoire. Cette consigne ne garantit pas qu’il obéira, mais elle donne un critère de contrôle. La longueur demandée doit aussi être compatible avec les informations à transmettre ; trois mots ne suffisent pas pour quatre modalités détaillées.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : tâche : résumer → public : étudiants → but : remise → longueur indicative.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Séparer données et instructions

Repère provisoire : 01:58 à 02:56. Audio : `semaine-08-03.wav`.

### Narration

Le prompt peut contenir une consigne, un document à analyser et des exemples. Il faut rendre ces rôles lisibles. Des délimiteurs permettent de repérer le début et la fin du texte source. Précisons que ce texte constitue une donnée à résumer, pas une nouvelle instruction à suivre. Si le document contient « ignore les consignes précédentes », nous voulons que l’application traite cette phrase comme un contenu. Cette séparation textuelle peut aider, mais ne constitue pas une barrière de sécurité suffisante contre les injections. Dans une application qui dispose d’outils ou de données privées, les permissions doivent aussi être contrôlées en dehors du modèle.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : consigne → délimiteur → document cité → fin du document.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Utiliser un exemple utile

Repère provisoire : 02:56 à 03:55. Audio : `semaine-08-04.wav`.

### Narration

Un exemple peut montrer la forme attendue. Imaginons un règlement qui mentionne la date et le format, mais pas le lieu de dépôt. La réponse d’exemple présente les deux informations connues et écrit « non indiqué dans le passage » pour la troisième. Cet exemple enseigne une conduite observable face à une information absente. Évitez de multiplier des exemples presque identiques qui ne couvrent qu’un cas facile. Un ensemble réduit, mais varié, peut mieux illustrer les limites de la tâche. Vérifiez aussi que les exemples sont cohérents entre eux : si l’un invente une donnée manquante, il contredit la consigne de s’en tenir au document.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : entrée d’exemple → réponse attendue → règle illustrée → nouvelle entrée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Définir une sortie vérifiable

Repère provisoire : 03:55 à 04:51. Audio : `semaine-08-05.wav`.

### Narration

Choisissons une sortie avec quatre champs clairement nommés. Le programme peut vérifier leur présence et le type de leurs valeurs. Cette validation de structure rend les erreurs plus faciles à détecter. Elle ne prouve pas que les dates ou les modalités sont exactes. Nous devons comparer chaque affirmation au passage source. Dans un usage pédagogique, on peut demander une courte citation justificative pour chaque modalité, puis vérifier que cette citation existe et qu’elle soutient vraiment l’affirmation. Une citation inventée ou mal interprétée reste une erreur. L’évaluation gagne donc à distinguer format valide, information fidèle et réponse utile au destinataire.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : date → format → dépôt → information absente.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Construire un petit jeu de tests

Repère provisoire : 04:51 à 05:47. Audio : `semaine-08-06.wav`.

### Narration

Préparons quatre cas. Le premier contient toutes les informations. Le deuxième omet le format du fichier. Le troisième présente deux dates, dont une ancienne explicitement remplacée. Le quatrième contient une instruction parasite dans le document. Pour chaque cas, écrivons ce que devrait faire une réponse acceptable. Testons ensuite plusieurs formulations du prompt en gardant les mêmes exemples. Nous évitons ainsi de conclure sur une seule sortie réussie. Lorsque le modèle échoue, cherchons la cause : consigne ambiguë, source insuffisante, sortie tronquée ou difficulté persistante du modèle. Le prompt ne peut pas résoudre à lui seul tous les problèmes du système.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : cas complet → champ absent → contradiction → instruction parasite.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Une révision guidée par les erreurs

Repère provisoire : 05:47 à 06:46. Audio : `semaine-08-07.wav`.

### Narration

Votre exercice consiste à écrire une première consigne, à noter deux erreurs observées, puis à proposer une modification ciblée. Expliquez pourquoi cette modification devrait agir sur ces erreurs. Retestez ensuite tous les cas, car corriger un problème peut en faire apparaître un autre. Une réponse plus longue n’est pas forcément plus fidèle, et un ton assuré n’est pas un indicateur de qualité. La question à retenir est : comment saurons-nous que la consigne fonctionne ? Si vous pouvez préciser la tâche, les données disponibles, les critères de réussite et les cas difficiles, vous disposez d’une méthode de travail réutilisable au-delà d’un modèle ou d’une formulation particulière.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : observer → modifier une consigne → retester → consigner.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
