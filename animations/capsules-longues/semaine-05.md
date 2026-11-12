# Semaine 5 : Générer un texte : probabilités, température et arrêt

## Préparation

**731 mots ; durée indicative 06:50 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:56 à 07:21.**

Fichier audio complet possible : `semaine-05.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Une génération en plusieurs décisions

Repère provisoire : 00:00 à 00:57. Audio : `semaine-05-01.wav`.

### Narration

Lorsqu’un modèle produit un paragraphe, il ne choisit généralement pas tout le paragraphe en une seule opération. Il calcule une distribution pour le prochain token, sélectionne un candidat selon une règle de décodage, ajoute ce token au contexte et recommence. Cette boucle est appelée génération autorégressive. Nous allons suivre un exemple avec trois candidats et comparer plusieurs règles. L’objectif est de comprendre quels paramètres changent la sélection et quels paramètres ne garantissent pas la qualité du contenu. Gardez cette distinction en tête : le modèle calcule des scores ; le mécanisme de décodage décide comment les utiliser pour produire une suite particulière.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : début de phrase → distribution → token choisi → nouveau contexte.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Décaler les entrées et les cibles

Repère provisoire : 00:57 à 01:58. Audio : `semaine-05-02.wav`.

### Narration

Pendant l’entraînement causal, une séquence fournit plusieurs couples entre contexte et token suivant. Si l’entrée contient « le chat dort », les cibles correspondantes peuvent être « chat dort », puis un token de fin selon la construction de l’exemple. Le décalage d’une position est essentiel. Le modèle ne doit pas voir le token qu’il essaie de prédire à cette position. Le masque causal assure cette contrainte lorsque plusieurs positions sont calculées dans une même passe. La perte pénalise les probabilités trop faibles données aux cibles du corpus. Apprendre ainsi à prédire une continuation ne suffit pas, à lui seul, à garantir une réponse utile à chaque demande humaine.

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : Le chat dort → chat dort [fin] → prédictions → perte.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Choisir toujours le maximum

Repère provisoire : 01:58 à 02:55. Audio : `semaine-05-03.wav`.

### Narration

Pour un contexte donné, imaginons trois candidats : chat avec une probabilité de zéro virgule cinquante, chien avec zéro virgule trente et oiseau avec zéro virgule vingt. Le décodage glouton choisit chat. Il est simple et n’utilise pas un tirage aléatoire à cette étape. Pourtant, ce choix local ne garantit pas la meilleure séquence complète. Un candidat un peu moins probable peut mener ensuite à une continuation plus cohérente. De plus, une réponse reproductible dans un environnement donné peut être fausse. Il ne faut donc pas confondre la stabilité du choix, la qualité de rédaction et l’exactitude factuelle de la réponse.

### Réalisation Manim

Visuel : `sampling`. Apparition progressive : chat : 0,50 → chien : 0,30 → oiseau : 0,20 → choix : chat.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Modifier la température

Repère provisoire : 02:55 à 03:53. Audio : `semaine-05-04.wav`.

### Narration

La température agit sur les scores avant leur conversion par le softmax. Pour une température strictement positive, nous divisons les scores par cette valeur. Une température plus petite accentue les écarts et concentre généralement la distribution. Une température plus grande la rend plus diffuse. Avec les scores zéro, un et deux, diviser par deux donne zéro, zéro virgule cinq et un : les différences sont réduites. Diviser par zéro virgule cinq donne zéro, deux et quatre : elles sont amplifiées. La température ne fournit pas de nouvelles connaissances au modèle. Elle modifie la façon dont les candidats déjà proposés se partagent la probabilité.

### Réalisation Manim

Visuel : `temperature`. Apparition progressive : scores 0 ; 1 ; 2 → T = 0,5 → T = 1 → T = 2.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Restreindre les candidats

Repère provisoire : 03:53 à 04:50. Audio : `semaine-05-05.wav`.

### Narration

On peut également restreindre l’ensemble des candidats avant le tirage. Avec top-k, on conserve un nombre fixé de candidats parmi les mieux classés. Avec top-p, on conserve un ensemble dont la probabilité cumulée atteint un seuil, selon la convention de l’implémentation. Dans notre distribution cinquante, trente et vingt pour cent, un seuil de quatre-vingts pour cent peut retenir les deux premiers candidats. Leurs probabilités doivent ensuite être renormalisées pour tirer dans cet ensemble. Les paramètres peuvent interagir et leur ordre d’application mérite d’être vérifié dans l’outil utilisé. Ne changez pas cinq réglages à la fois si vous souhaitez comprendre l’effet de chacun.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : classement → top-k → seuil top-p → tirage.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Arrêter et vérifier la sortie

Repère provisoire : 04:50 à 05:49. Audio : `semaine-05-06.wav`.

### Narration

La boucle s’arrête lorsqu’une condition définie est atteinte : un token de fin, une limite de génération ou un autre critère. Une limite trop courte peut couper une phrase ou un objet JSON avant sa fermeture. Demander un format dans le prompt ne dispense pas de vérifier le résultat. Si l’application attend un titre et un résumé, elle doit contrôler la syntaxe, la présence des champs et leurs types. Il faut ensuite examiner si le contenu respecte la demande. Un JSON valide peut contenir une affirmation fausse. La validation de structure et la validation du contenu sont donc deux étapes complémentaires, avec des critères différents.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : token de fin → limite de longueur → texte tronqué → validation.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Comparer proprement deux réglages

Repère provisoire : 05:49 à 06:50. Audio : `semaine-05-07.wav`.

### Narration

Pour un petit exercice, gardez trois demandes identiques et comparez deux températures avec la même méthode d’échantillonnage. Effectuez plusieurs essais pour chaque configuration. Relevez les répétitions, les variations, les erreurs et les sorties incomplètes. Une seule réponse séduisante ne suffit pas à conclure qu’un réglage est meilleur. Avant de terminer, répondez à cette question : augmenter la température rend-il le modèle plus compétent ? Non, cela modifie la distribution utilisée pour sélectionner les tokens. La compétence et la fiabilité dépendent aussi du modèle, des données, du contexte et de la tâche. Vous pouvez maintenant lire les paramètres de génération comme des choix expérimentaux plutôt que comme une recette universelle.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : mêmes demandes → un paramètre changé → plusieurs essais → analyse.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
