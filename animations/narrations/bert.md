# Semaine 4 : BERT et le token masqué

Fichier audio attendu : `bert.wav` ou `bert.mp3`.

Script Manim : classe `BERT` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 28.1 secondes. Ce texte contient environ 107 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

BERT construit des représentations en utilisant le contexte situé à gauche et à droite. Dans cette phrase, un token a été remplacé par le marqueur « masque ».

## Segment 2

Le mot « miaule » fournit un indice pour retrouver « chat ». Les probabilités affichées sont fictives : elles servent seulement à illustrer la prédiction.

## Segment 3

Pendant le préentraînement, la perte compare les prédictions aux cibles sur les positions sélectionnées. Le modèle ajuste ses paramètres pour améliorer cette reconstruction.

## Segment 4

Il faut distinguer deux mécanismes. Remplacer un token d’entrée par un masque cache son contenu. Un masque causal interdit, lui, certaines connexions d’attention. Ce ne sont pas les mêmes opérations.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `bert-01.wav`, `bert-02.wav`, etc. Un fichier continu reste possible.
