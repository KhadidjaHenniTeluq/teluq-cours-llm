# Semaine 5 : La génération autorégressive

Fichier audio attendu : `generation.wav` ou `generation.mp3`.

Script Manim : classe `Generation` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 34.7 secondes. Ce texte contient environ 114 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Un modèle génératif produit sa réponse un token à la fois. Le contexte de départ est ici « Le chat ». Le modèle calcule plusieurs suites possibles et leur attribue des probabilités.

## Segment 2

Nous utilisons un décodage glouton : il choisit le token le plus probable. Dans cet exemple fictif, le modèle sélectionne « dort ». Ce token est ajouté au contexte.

## Segment 3

Le calcul recommence sur le nouveau contexte. Le modèle choisit ensuite « sur », puis « le ». À chaque étape, la distribution est recalculée.

## Segment 4

La boucle continue jusqu’à une condition d’arrêt, comme une limite de longueur ou un token de fin. Avec l’échantillonnage, le token choisi peut être différent du plus probable.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `generation-01.wav`, `generation-02.wav`, etc. Un fichier continu reste possible.
