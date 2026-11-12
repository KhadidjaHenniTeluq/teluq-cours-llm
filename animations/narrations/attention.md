# Semaine 3 : Comprendre les poids d’attention

Fichier audio attendu : `attention.wav` ou `attention.mp3`.

Script Manim : classe `Attention` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 29.5 secondes. Ce texte contient environ 110 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

L’attention permet à une position de combiner des informations provenant d’autres positions. Le modèle construit pour cela des requêtes, des clés et des valeurs, appelées Q, K et V.

## Segment 2

Une requête est comparée aux clés. Les produits scalaires sont divisés par la racine de la dimension des clés. Dans notre exemple, les scores obtenus sont zéro, un et deux.

## Segment 3

Le softmax transforme ces scores en poids : environ neuf pour cent, vingt-quatre et demi pour cent, et soixante-six et demi pour cent. Leur somme vaut un.

## Segment 4

La sortie est une somme des valeurs V pondérées par ces poids. Dans un décodeur causal, les positions futures sont masquées avant le softmax.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `attention-01.wav`, `attention-02.wav`, etc. Un fichier continu reste possible.
