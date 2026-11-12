# Semaine 8 : Construire un prompt vérifiable

Fichier audio attendu : `prompt.wav` ou `prompt.mp3`.

Script Manim : classe `Prompt` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 30.8 secondes. Ce texte contient environ 109 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Un prompt devient plus facile à utiliser quand il précise la tâche, les données et le format attendu. Dans cet exemple, nous demandons d’extraire une date de remise.

## Segment 2

Nous fournissons ensuite le texte à analyser : « Le devoir est dû le douze novembre ». La donnée est clairement séparée de la consigne.

## Segment 3

Enfin, nous demandons un objet JSON contenant la date, ou une valeur nulle si elle est absente. La réponse illustrée reprend ici le douze novembre.

## Segment 4

L’application doit encore vérifier le format et la correspondance avec le texte source. Des délimiteurs améliorent la clarté, mais ils ne garantissent ni l’exactitude ni une protection complète contre les injections.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `prompt-01.wav`, `prompt-02.wav`, etc. Un fichier continu reste possible.
