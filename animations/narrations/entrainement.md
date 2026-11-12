# Semaine 15 : minGPT : de la prédiction à la mise à jour

Fichier audio attendu : `entrainement.wav` ou `entrainement.mp3`.

Script Manim : classe `Entrainement` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 38.1 secondes. Ce texte contient environ 112 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Pour entraîner minGPT, les cibles sont décalées d’un token par rapport aux entrées. Avec « Le », « chat » et « dort » en entrée, les cibles sont « chat », « dort » et le point.

## Segment 2

Le passage avant calcule des scores sur le vocabulaire. La perte d’entropie croisée compare ces scores aux cibles attendues.

## Segment 3

La rétropropagation calcule ensuite les gradients. L’optimiseur utilise ces informations pour mettre à jour les paramètres.

## Segment 4

Entre deux pas, on réinitialise les gradients, sauf si l’on veut volontairement les accumuler. Enfin, on mesure les résultats sur des données de validation séparées. Une baisse de la perte d’entraînement ne suffit pas à démontrer une meilleure généralisation.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `entrainement-01.wav`, `entrainement-02.wav`, etc. Un fichier continu reste possible.
