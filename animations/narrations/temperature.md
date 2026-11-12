# Semaine 5 : Température et probabilités

Fichier audio attendu : `temperature.wav` ou `temperature.mp3`.

Script Manim : classe `Temperature` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 28.0 secondes. Ce texte contient environ 107 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

La température modifie une distribution avant l’échantillonnage. Nous gardons ici les mêmes scores : deux, un et zéro. On les divise par la température, puis on applique le softmax.

## Segment 2

À zéro virgule cinq, la probabilité se concentre sur le premier candidat. Il reçoit environ quatre-vingt-sept pour cent de la masse totale.

## Segment 3

À un, nous retrouvons la distribution initiale. À deux, les probabilités deviennent plus proches les unes des autres : les candidats moins probables ont davantage de chances d’être tirés.

## Segment 4

Pour une température positive, le classement reste le même. Le décodage glouton choisit donc toujours le même maximum. Modifier la température ne garantit pas l’exactitude des réponses.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `temperature-01.wav`, `temperature-02.wav`, etc. Un fichier continu reste possible.
