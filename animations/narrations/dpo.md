# Semaine 12 : Apprendre avec des paires de préférences

Fichier audio attendu : `dpo.wav` ou `dpo.mp3`.

Script Manim : classe `DPO` dans `animations/scenes.py`.

Vidéo silencieuse actuelle : 29.0 secondes. Ce texte contient environ 114 mots ; lisez à votre rythme. La durée visuelle sera adaptée à votre audio.

## Segment 1

DPO adapte un modèle à partir de préférences. Pour une même question, le jeu de données fournit une réponse préférée et une réponse rejetée.

## Segment 2

La méthode compare leurs log-probabilités dans le modèle à entraîner et dans un modèle de référence gelé. La marge affichée mesure cette différence relative.

## Segment 3

La perte encourage une marge plus grande pour la réponse préférée. Le paramètre bêta intervient dans cette fonction de perte. L’objectif porte sur une comparaison relative, pas sur une garantie que chaque probabilité évolue isolément dans le sens attendu.

## Segment 4

La qualité des préférences reste essentielle. Satisfaire les comparaisons d’un jeu de données ne garantit pas qu’une réponse sera vraie, utile ou sûre dans toutes les situations.

## Pour l’enregistrement

Lire uniquement les paragraphes. Laisser une courte pause entre les segments. Si vous enregistrez chaque segment séparément, nommer les fichiers `dpo-01.wav`, `dpo-02.wav`, etc. Un fichier continu reste possible.
