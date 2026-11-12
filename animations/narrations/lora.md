# Semaine 11 : LoRA et les matrices de faible rang

Fichier audio attendu : `lora.wav` ou `lora.mp3`.

Script Manim : classe `LoRA` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 30.8 secondes. Ce texte contient environ 116 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

LoRA adapte une matrice en conservant ses poids de base et en apprenant une petite correction. Ici, la matrice de base a quatre mille quatre-vingt-seize lignes et autant de colonnes.

## Segment 2

La correction utilise deux matrices, A et B, avec un rang de huit. Ensemble, elles contiennent soixante-cinq mille cinq cent trente-six paramètres entraînables.

## Segment 3

La sortie additionne le résultat de la matrice de base et celui de cette branche de faible rang. Le facteur alpha divisé par le rang règle l’échelle de la correction.

## Segment 4

Pour cet exemple, il y a deux cent cinquante-six fois moins de paramètres entraînables. Mais les poids de base restent en mémoire : ce rapport ne mesure pas l’économie totale de mémoire GPU.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `lora-01.wav`, `lora-02.wav`, etc. Un fichier continu reste possible.
