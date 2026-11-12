# Semaine 2 : Du texte aux tokens

Fichier audio attendu : `tokenisation.wav` ou `tokenisation.mp3`.

Script Manim : classe `Tokenisation` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 27.3 secondes. Ce texte contient environ 105 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

Avant de traiter une phrase, le modèle reçoit une suite de tokens. Prenons « Les chats dorment ». Dans cet exemple, nous découpons la phrase en cinq unités, en comptant le point final.

## Segment 2

Le mot « dorment » est séparé en deux morceaux. Cela montre qu’un token n’est pas forcément un mot entier. Certains tokens comprennent aussi un espace.

## Segment 3

Chaque unité reçoit ensuite un identifiant. Les nombres affichés ici sont fictifs. Le découpage et les identifiants réels dépendent du tokeniseur choisi.

## Segment 4

Enfin, chaque identifiant sert à sélectionner une ligne de la matrice d’embeddings. Deux identifiants proches ne désignent pas nécessairement deux mots de sens proche.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `tokenisation-01.wav`, `tokenisation-02.wav`, etc. Un fichier continu reste possible.
