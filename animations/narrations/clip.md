# Semaine 10 : CLIP et l’apprentissage contrastif

Fichier audio attendu : `clip.wav` ou `clip.mp3`.

Script Manim : classe `CLIP` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 30.8 secondes. Ce texte contient environ 108 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

CLIP apprend à comparer des images et des textes. Un encodeur traite les images et un autre traite les descriptions. Leurs vecteurs sont comparés dans un espace partagé.

## Segment 2

La matrice montre trois images et trois textes. Les associations correctes sont sur la diagonale : le chat avec le chat, le vélo avec le vélo et l’arbre avec l’arbre.

## Segment 3

La perte contrastive favorise ces associations par rapport aux autres paires du lot. La comparaison est effectuée dans les deux directions, de l’image vers le texte et du texte vers l’image.

## Segment 4

Les valeurs présentées sont fictives. CLIP mesure une compatibilité entre entrées ; il ne génère pas lui-même une légende.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `clip-01.wav`, `clip-02.wav`, etc. Un fichier continu reste possible.
