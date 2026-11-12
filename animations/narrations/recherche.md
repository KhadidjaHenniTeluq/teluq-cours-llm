# Semaine 6 : Du document aux passages pertinents

Fichier audio attendu : `recherche.wav` ou `recherche.mp3`.

Script Manim : classe `Recherche` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 28.6 secondes. Ce texte contient environ 113 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Pour chercher dans un document long, on peut d’abord le découper en passages. Ici, les trois passages concernent l’inscription, les frais et les examens.

## Segment 2

Chaque passage reçoit un embedding. La question « combien coûte le cours ? » est encodée dans un espace compatible avec ces représentations.

## Segment 3

On compare ensuite les vecteurs. Dans cet exemple fictif, le passage sur les frais obtient le score le plus élevé. Une recherche top-k conserve les meilleurs candidats.

## Segment 4

Le découpage et le modèle d’embeddings influencent ces résultats. Un score élevé indique une proximité selon la mesure choisie. Il ne prouve pas que le passage contient une réponse correcte : il faut encore lire et vérifier son contenu.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `recherche-01.wav`, `recherche-02.wav`, etc. Un fichier continu reste possible.
