# Semaine 4 : BERT : exploiter le contexte pour représenter et classer un texte

## Préparation

**724 mots ; durée indicative 06:46 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:53 à 07:17.**

Fichier audio complet possible : `semaine-04.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Représenter plutôt que poursuivre

Repère provisoire : 00:00 à 00:59. Audio : `semaine-04-01.wav`.

### Narration

Cette semaine, nous étudions un modèle qui construit des représentations à partir d’un texte disponible. Prenons un avis : « le film commence lentement, mais la fin est remarquable ». Pour décider si cet avis est positif, un mot isolé ne suffit pas. Nous devons tenir compte des relations entre les parties de la phrase. Un encodeur comme BERT permet à une position de consulter le contexte à gauche et à droite, sous réserve du masque des tokens de remplissage. Cela le distingue du masque causal utilisé pour prédire la suite d’un texte. Nous allons relier cette propriété au préentraînement puis à une tâche de classification.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : phrase complète → encodeur → représentations → tâche.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Apprendre avec un mot masqué

Repère provisoire : 00:59 à 01:56. Audio : `semaine-04-02.wav`.

### Narration

Imaginez que le verbe dans « le chat dort sur le tapis » soit caché. Le modèle doit attribuer des probabilités aux candidats possibles à partir du texte observé. Le contexte après le masque apporte une information utile. L’entraînement original de BERT comprend un objectif de prédiction de tokens sélectionnés, avec plusieurs façons de les traiter ; tous ne sont pas simplement remplacés par le symbole masque. Pour comprendre le principe, nous montrons seulement le cas masqué. La cible vient du texte d’origine. Il n’est donc pas nécessaire qu’une personne étiquette manuellement chaque verbe du corpus pour construire cet exercice d’apprentissage.

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : Le chat → [MASK] → sur le tapis → prédiction.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Un vecteur par position

Repère provisoire : 01:56 à 02:55. Audio : `semaine-04-03.wav`.

### Narration

Après les couches de l’encodeur, chaque position possède un vecteur contextualisé. Le token souris peut recevoir des représentations différentes dans une phrase sur un ordinateur et dans une phrase sur un animal. Le modèle ne remplace pas explicitement le mot par une définition de dictionnaire. Ses transformations apprises produisent des nombres utiles pour les objectifs rencontrés à l’entraînement. La représentation finale dépend donc du modèle, de la couche et du contexte choisi. Pour comparer deux exemples, il faut préciser ces éléments et utiliser un protocole cohérent. Une jolie projection en deux dimensions ne suffit pas à démontrer que toutes les distinctions de sens ont été apprises.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : souris → près du clavier → souris → dans le jardin.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Passer à la classification

Repère provisoire : 02:55 à 03:52. Audio : `semaine-04-04.wav`.

### Narration

Pour classer l’avis sur le film, nous avons besoin d’une sortie au niveau du texte. Une approche courante avec BERT utilise la représentation associée au token spécial de classification, puis une couche de sortie adaptée aux catégories. Cette représentation n’est pas automatiquement un résumé parfait de la phrase. Son utilité pour la tâche dépend de l’apprentissage. Pendant l’ajustement supervisé, nous présentons des avis accompagnés de leurs étiquettes, calculons une perte et adaptons les paramètres choisis. Nous devons conserver des exemples indépendants pour évaluer la généralisation. Tester sur les mêmes avis que ceux utilisés pour apprendre peut donner une impression de qualité trompeuse.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : avis → représentation globale → couche de sortie → positif ou négatif.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Lire une matrice de confusion

Repère provisoire : 03:52 à 04:50. Audio : `semaine-04-05.wav`.

### Narration

Supposons que notre système détecte des avis positifs. Sur vingt exemples, il trouve huit vrais positifs, produit deux faux positifs, manque quatre positifs et reconnaît six vrais négatifs. La précision vaut huit divisé par dix, soit quatre-vingts pour cent. Le rappel vaut huit divisé par douze, soit environ soixante-six virgule sept pour cent. Ces mesures répondent à deux questions différentes. Parmi les avis annoncés positifs, combien le sont réellement ? Parmi tous les avis réellement positifs, combien avons-nous retrouvés ? Un chiffre global ne remplace pas cette lecture, surtout lorsque les classes sont déséquilibrées ou que certaines erreurs ont des conséquences plus importantes.

### Réalisation Manim

Visuel : `confusion`. Apparition progressive : vrais positifs : 8 → faux positifs : 2 → faux négatifs : 4 → vrais négatifs : 6.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Deux limites pratiques

Repère provisoire : 04:50 à 05:47. Audio : `semaine-04-06.wav`.

### Narration

Deux limites méritent une attention particulière. D’abord, la longueur d’entrée est limitée par la configuration du modèle. Si nous tronquons un avis avant la phrase « mais la fin est remarquable », nous supprimons peut-être l’indice décisif. Ensuite, un modèle adapté à des critiques de cinéma peut mal fonctionner sur des commentaires médicaux ou des messages ironiques. Il faut examiner des erreurs concrètes, pas seulement ajouter des couches ou augmenter le nombre d’époques. Notez les cas où l’étiquette elle-même est discutable. Une évaluation utile distingue les erreurs du modèle, les ambiguïtés du texte et les problèmes dans les annotations de référence.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : texte long → troncature → données différentes → erreurs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Choisir une représentation selon la tâche

Repère provisoire : 05:47 à 06:46. Audio : `semaine-04-07.wav`.

### Narration

Pour conclure, BERT fournit des représentations contextualisées, mais leur utilisation doit correspondre à la tâche. Une représentation qui convient à une classification ajustée sur des avis n’est pas nécessairement la meilleure pour comparer directement deux phrases par cosinus. Des modèles sont spécialement entraînés pour cette comparaison. Voici votre question : pourquoi le mot situé après un masque peut-il aider BERT, alors qu’un modèle causal ne peut pas consulter un futur token à prédire ? Prenez quelques secondes. La différence vient du masque d’attention et de l’objectif d’apprentissage. Résumez enfin le parcours complet : texte disponible, représentations contextualisées, sortie adaptée, puis évaluation sur des données réservées.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : classification → similarité → recherche → évaluation.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Référence de préparation

[BERT](https://arxiv.org/abs/1810.04805)
