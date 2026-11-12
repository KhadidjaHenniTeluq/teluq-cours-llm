# Semaine 9 : Les étapes d’un système RAG

Fichier audio attendu : `rag.wav` ou `rag.mp3`.

Script Manim : classe `RAG` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 31.8 secondes. Ce texte contient environ 109 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Le RAG associe une recherche documentaire à un modèle génératif. Avant les questions des utilisateurs, les documents sont découpés en passages, transformés en embeddings et placés dans un index.

## Segment 2

Quand une question arrive, le système l’encode pour rechercher des passages pertinents. Ces passages sont récupérés dans la base documentaire.

## Segment 3

Le modèle reçoit alors un prompt qui contient la question et les passages sélectionnés. Il peut s’appuyer sur ce contexte pour formuler une réponse. Les poids du modèle ne sont pas réentraînés pendant cette recherche.

## Segment 4

Les sources permettent de vérifier la réponse. Le RAG ne supprime toutefois pas toutes les erreurs : la récupération et l’interprétation des documents peuvent échouer.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `rag-01.wav`, `rag-02.wav`, etc. Un fichier continu reste possible.
