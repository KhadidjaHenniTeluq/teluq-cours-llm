# Semaine 11 : Quantification et erreur d’arrondi

Fichier audio attendu : `quantification.wav` ou `quantification.mp3`.

Script Manim : classe `Quantification` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 30.0 secondes. Ce texte contient environ 109 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

La quantification remplace des valeurs par des niveaux représentables avec moins de précision. Nous utilisons ici une grille simple dont le pas vaut zéro virgule cinq.

## Segment 2

Pour obtenir le niveau quantifié, on divise le poids par le pas et on arrondit. Pour reconstruire une approximation, on multiplie ce niveau par le pas.

## Segment 3

Ainsi, moins un virgule trois devient moins un virgule cinq. Zéro virgule deux devient zéro, et un virgule sept devient un virgule cinq.

## Segment 4

Ce procédé peut économiser du stockage, mais il introduit une erreur. Les formats réels utilisent aussi des échelles, des groupes de valeurs et parfois des grilles non uniformes. Notre exemple illustre seulement le principe.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `quantification-01.wav`, `quantification-02.wav`, etc. Un fichier continu reste possible.
