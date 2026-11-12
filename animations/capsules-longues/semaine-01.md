# Semaine 1 : Pourquoi les modèles de langage ont besoin du contexte

## Préparation

**707 mots ; durée indicative 06:38 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:45 à 07:08.**

Fichier audio complet possible : `semaine-01.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Une phrase à compléter

Repère provisoire : 00:00 à 00:59. Audio : `semaine-01-01.wav`.

### Narration

Commençons par une phrase simple : la souris mange du fromage. Si je vous demande de prévoir le mot qui suit « la souris mange du », vous pouvez proposer fromage. Vous utilisez à la fois la grammaire et les associations apprises en lisant. Un modèle de langage attribue lui aussi des probabilités à différentes continuations. Cela ne signifie pas qu’il possède notre expérience du monde. Dans cette capsule, nous allons suivre trois façons de représenter le contexte : une courte fenêtre de mots, un état récurrent, puis l’attention. Notre question sera toujours la même : quelles informations sont disponibles au moment de prédire ?

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : La souris → mange → du fromage.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Une fenêtre limitée

Repère provisoire : 00:59 à 01:55. Audio : `semaine-01-02.wav`.

### Narration

Un premier modèle peut estimer le prochain mot à partir d’un nombre limité de mots précédents. Avec deux mots de contexte, il consulte par exemple « dort sur » pour proposer « le ». Cette approche est utile pour comprendre la prédiction, mais elle rencontre rapidement une limite. La phrase « la souris que j’ai achetée hier ne fonctionne plus » parle probablement d’un appareil. Si nous regardons seulement les derniers mots, nous pouvons perdre cette indication. Augmenter la fenêtre multiplie les combinaisons à observer. Les séquences rares deviennent difficiles à estimer à partir des seules fréquences du corpus.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : Le chat → dort → sur le tapis.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Lire un élément après l’autre

Repère provisoire : 01:55 à 02:52. Audio : `semaine-01-03.wav`.

### Narration

Un réseau récurrent propose une autre organisation. Il reçoit un élément, met à jour un état interne, puis transmet cet état à l’étape suivante. Sur le schéma, le petit rectangle qui circule représente un vecteur de nombres, pas une copie du texte. L’état après le deuxième élément dépend du deuxième élément et de l’état précédent. Les mêmes paramètres de transition sont utilisés à chaque position. Cette répétition permet de traiter des séquences de longueurs différentes. Elle impose aussi une dépendance : pour calculer l’état suivant, il faut disposer de l’état précédent. Nous voyons ainsi le lien entre l’architecture et l’ordre du calcul.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : entrée x₁ → état h₁ → état h₂ → prédiction.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Ce que contient un état

Repère provisoire : 02:52 à 03:48. Audio : `semaine-01-04.wav`.

### Narration

Reprenons la souris près du clavier. Lorsque le réseau arrive à « fonctionne », son état doit encore porter une information utile sur la souris et le clavier. Il n’existe pas nécessairement une case réservée au mot souris. L’information est distribuée dans les composantes du vecteur. Imaginez un carnet de taille fixe où chaque nouvelle observation oblige à réorganiser les notes. Cette comparaison aide à comprendre la compression, mais le réseau apprend une transformation numérique, pas une prise de notes explicite. Dans certaines architectures encodeur-décodeur, résumer toute une entrée dans un seul vecteur crée un goulot d’étranglement particulièrement visible.

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : La souris → près du clavier → ne fonctionne → plus.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Apprendre sur une longue séquence

Repère provisoire : 03:48 à 04:44. Audio : `semaine-01-05.wav`.

### Narration

Pour apprendre, nous comparons la prédiction avec la cible attendue et nous calculons une perte. La rétropropagation indique comment modifier les paramètres pour diminuer cette perte. Dans un réseau récurrent, ce calcul remonte les étapes de la séquence. Les produits successifs peuvent rendre certains gradients très petits ou très grands. Un faible gradient ne signifie pas que le réseau a consciemment oublié le début de la phrase. Il signifie que le signal d’ajustement devient difficile à exploiter. Des architectures à portes, comme les LSTM, facilitent la conservation et la modification de l’état, sans supprimer toutes les difficultés des longues dépendances.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : erreur finale → gradient → étapes passées → paramètres.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Consulter plusieurs positions

Repère provisoire : 04:44 à 05:39. Audio : `semaine-01-06.wav`.

### Narration

L’attention permet de calculer une combinaison de représentations situées à plusieurs positions. Au lieu d’exiger que toute information utile passe uniquement par le dernier état récurrent, une position peut utiliser plusieurs représentations disponibles. Les poids déterminent leur contribution à la sortie calculée. Dans un modèle causal, les positions futures restent interdites. Nous détaillerons plus tard les requêtes, les clés et les valeurs. Pour le moment, retenez le changement de circulation de l’information. Un poids élevé dans une tête d’attention n’est pas, à lui seul, une explication complète du raisonnement du modèle ou une preuve de compréhension humaine.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : position actuelle → positions passées → poids → combinaison.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Vérifier sa compréhension

Repère provisoire : 05:39 à 06:38. Audio : `semaine-01-07.wav`.

### Narration

Prenez quelques secondes pour répondre : dans quelle approche l’information passe-t-elle par un état mis à jour à chaque étape ? Il s’agit du réseau récurrent. Quelle approche combine explicitement plusieurs représentations disponibles à l’aide de poids ? Il s’agit de l’attention. Enfin, pourquoi un modèle fondé sur une petite fenêtre peut-il manquer le sens de souris ? Parce que l’indice pertinent peut se trouver en dehors de cette fenêtre. Pour terminer, dessinez les trois schémas sans regarder la vidéo et indiquez où se trouve le contexte. Si vous pouvez expliquer les flèches avec vos propres mots, vous avez compris l’objectif de cette première capsule.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : fenêtre courte → état récurrent → attention → comparaison.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
