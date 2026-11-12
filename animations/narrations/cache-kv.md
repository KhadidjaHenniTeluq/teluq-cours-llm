# Semaine 13 : Le cache KV pendant le décodage

Fichier audio attendu : `cache-kv.wav` ou `cache-kv.mp3`.

Script Manim : classe `CacheKV` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 31.8 secondes. Ce texte contient environ 110 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Pendant la génération causale, le cache KV conserve les clés et les valeurs déjà calculées. Le préremplissage commence par traiter les tokens du prompt, à chaque couche du modèle.

## Segment 2

Pour le token suivant, on calcule ses nouvelles projections. Ses clés et ses valeurs rejoignent le cache.

## Segment 3

La nouvelle requête consulte alors les clés et les valeurs des positions passées et de la position courante. Il faut donc toujours calculer l’attention au passé.

## Segment 4

Le gain vient de la réutilisation des projections précédentes. En échange, le cache occupe de la mémoire, et cette mémoire augmente avec la longueur du contexte. Il faut donc choisir un compromis entre vitesse et capacité de traitement.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `cache-kv-01.wav`, `cache-kv-02.wav`, etc. Un fichier continu reste possible.
