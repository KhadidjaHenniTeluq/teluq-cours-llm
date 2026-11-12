# Semaine 7 : BERTopic : des groupes aux sujets

Fichier audio attendu : `bertopic.wav` ou `bertopic.mp3`.

Script Manim : classe `BERTopic` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 29.2 secondes. Ce texte contient environ 106 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

BERTopic organise la découverte de sujets en plusieurs étapes. Les embeddings représentent d’abord les documents. UMAP réduit ensuite le nombre de dimensions utilisé pour le regroupement.

## Segment 2

HDBSCAN cherche des groupes de points denses. Dans notre dessin, deux groupes apparaissent et un point reste à l’extérieur. Tous les documents ne sont donc pas forcés dans un groupe.

## Segment 3

La méthode appelée c-TF-IDF met ensuite en évidence les mots caractéristiques de chaque groupe. Ici, les descriptions évoquent les cours et les frais.

## Segment 4

Ces mots facilitent l’interprétation, mais ne suffisent pas à valider un sujet. Il faut consulter les documents représentatifs. Les différents modules du pipeline peuvent aussi être remplacés.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `bertopic-01.wav`, `bertopic-02.wav`, etc. Un fichier continu reste possible.
