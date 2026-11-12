# Semaine 3 : Visualiser le masque causal

Fichier audio attendu : `masque-causal.wav` ou `masque-causal.mp3`.

Script Manim : classe `MasqueCausal` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 27.8 secondes. Ce texte contient environ 100 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Voici une matrice d’attention. Chaque ligne correspond à une requête et chaque colonne à une clé. Les numéros indiquent les positions dans la séquence.

## Segment 2

Les cases vertes montrent les connexions autorisées. À la deuxième position, le modèle peut consulter les positions un et deux, mais pas les suivantes.

## Segment 3

Pour bloquer une position future, on ajoute moins l’infini à son score avant le softmax. Son poids devient alors nul.

## Segment 4

Ce masque permet de traiter plusieurs positions en parallèle pendant l’entraînement sans leur donner accès aux tokens futurs. Le modèle apprend ainsi à prédire la suite à partir du seul contexte autorisé.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `masque-causal-01.wav`, `masque-causal-02.wav`, etc. Un fichier continu reste possible.
