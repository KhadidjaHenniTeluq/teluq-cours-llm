# Semaine 10 : Du patch au token visuel

Fichier audio attendu : `vision.wav` ou `vision.mp3`.

Script Manim : classe `Vision` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 29.0 secondes. Ce texte contient environ 106 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Un Vision Transformer traite une image comme une séquence de représentations. On commence par la découper en patches. Notre dessin utilise une petite grille de quatre lignes et quatre colonnes.

## Segment 2

Chaque patch est aplati, puis projeté en un vecteur. Les vecteurs obtenus ont la même dimension et forment une séquence.

## Segment 3

On leur ajoute des informations de position pour conserver la localisation des patches dans l’image.

## Segment 4

Pour une image de deux cent vingt-quatre pixels de côté et des patches de seize pixels, on obtient quatorze fois quatorze, soit cent quatre-vingt-seize patches. Dans un ViT qui ajoute un token de classification, la séquence compte donc cent quatre-vingt-dix-sept tokens.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `vision-01.wav`, `vision-02.wav`, etc. Un fichier continu reste possible.
