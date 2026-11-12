# Semaine 1 : RNN et mémoire séquentielle

Fichier audio attendu : `recurrence.wav` ou `recurrence.mp3`.

Script Manim : classe `Recurrence` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 38.5 secondes. Ce texte contient environ 116 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Un réseau récurrent lit une séquence étape par étape. Ici, il reçoit successivement les tokens « Le », « chat », « noir » et « dort ». À chaque étape, il met à jour un état caché.

## Segment 2

Cet état dépend du token courant et de l’état précédent. Il transmet donc une partie de l’information déjà traitée. Pour calculer le deuxième état, il faut avoir calculé le premier.

## Segment 3

Pendant l’entraînement, le gradient parcourt ces étapes dans le sens inverse. Sur de longues séquences, ce signal peut devenir très faible ou, au contraire, augmenter fortement.

## Segment 4

Les LSTM utilisent des mécanismes de contrôle pour atténuer certaines de ces difficultés. Ils conservent toutefois une dépendance séquentielle entre leurs étapes.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `recurrence-01.wav`, `recurrence-02.wav`, etc. Un fichier continu reste possible.
