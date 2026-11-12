# Semaine 12 : Apprendre à partir de préférences : RLHF et DPO

## Préparation

**935 mots ; durée indicative 08:43 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 07:35 à 09:24.**

Fichier audio complet possible : `semaine-12.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Deux réponses pour une demande

Repère provisoire : 00:00 à 00:56. Audio : `semaine-12-01.wav`.

### Narration

Une réponse peut être grammaticalement correcte et pourtant peu utile. Pour une même question, nous pouvons préférer une réponse précise, honnête sur ses limites et adaptée au niveau de l’étudiant. L’apprentissage à partir de préférences exploite des comparaisons entre réponses. Prenons une question sur un exercice de matrices. La réponse A explique les dimensions avant le calcul ; la réponse B donne un résultat sans justification. Une personne peut préférer A selon une grille pédagogique. Ce jugement dépend du contexte et des critères. Dans cette capsule, nous distinguons les données de préférence, une démarche RLHF avec PPO et l’approche DPO.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : même question → réponse A → réponse B → préférence annotée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Définir les critères de comparaison

Repère provisoire : 00:56 à 01:55. Audio : `semaine-12-02.wav`.

### Narration

Avant d’entraîner quoi que ce soit, il faut définir ce que signifie préférer une réponse. Si un annotateur privilégie la brièveté et un autre la démonstration détaillée, leur désaccord peut refléter des critères différents plutôt qu’une erreur. Une grille explicite permet de discuter l’exactitude, la pertinence, la clarté et le respect des consignes. Certaines paires restent ambiguës ; on peut les signaler ou prévoir une procédure de résolution. Des préférences humaines ne constituent pas une mesure parfaite de vérité. Une réponse convaincante mais fausse peut être choisie si l’annotation ne vérifie pas les faits. La qualité des comparaisons influence donc directement ce que le modèle apprend.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : exactitude → clarté → pertinence → désaccord possible.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Commencer par un modèle supervisé

Repère provisoire : 01:55 à 02:54. Audio : `semaine-12-03.wav`.

### Narration

Une démarche courante commence par un modèle ajusté sur des démonstrations de réponses attendues. Cette étape supervisée lui donne un comportement de départ pour suivre des consignes. Les préférences ajoutent ensuite une autre information : parmi deux réponses possibles à une même demande, laquelle est jugée meilleure ? Il ne faut pas confondre ces deux types de données. Une démonstration fournit une sortie cible ; une comparaison fournit un ordre relatif. La quantité nécessaire et les détails de l’entraînement dépendent du projet. Notre objectif ici est de comprendre le rôle de chaque composant, pas de proposer une recette de réglages valable pour tous les modèles.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : modèle initial → démonstrations → ajustement supervisé → politique de départ.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Une démarche RLHF avec PPO

Repère provisoire : 02:54 à 03:52. Audio : `semaine-12-04.wav`.

### Narration

Dans une démarche RLHF utilisant PPO, un modèle de récompense peut être appris à partir des comparaisons. Il attribue ensuite un score à des réponses produites par la politique, c’est-à-dire le modèle que nous cherchons à ajuster. Une optimisation par renforcement utilise ce signal tout en limitant certains changements par rapport à un modèle de référence. Ce résumé simplifie un entraînement qui comporte plusieurs choix techniques. Le modèle de récompense et le modèle de référence jouent des rôles différents : l’un estime une préférence, l’autre fournit un point de comparaison pour contrôler l’évolution du comportement. Ils ne doivent pas être confondus dans le schéma.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : comparaisons → modèle de récompense → politique → optimisation PPO.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Le risque d’un mauvais indicateur

Repère provisoire : 03:52 à 04:50. Audio : `semaine-12-05.wav`.

### Narration

Si le modèle de récompense favorise involontairement les réponses longues, l’optimisation peut produire davantage de longueur sans améliorer l’utilité. C’est un exemple de la différence entre optimiser un indicateur et atteindre l’objectif réel. Une récompense apprise reste une approximation des jugements disponibles. Il faut surveiller les réponses générées et rechercher les comportements inattendus. Le modèle de référence aide à encadrer certains changements, mais ne garantit pas l’absence de dérive. Dans une application pédagogique, nous devons vérifier des explications, des calculs et des cas où la bonne réponse consiste à reconnaître une information insuffisante. La moyenne d’un score ne montre pas tous ces aspects.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : récompense élevée → réponse longue → information fausse → contrôle humain.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Le principe de DPO

Repère provisoire : 04:50 à 05:47. Audio : `semaine-12-06.wav`.

### Narration

DPO utilise directement des paires préférées et écartées dans un objectif d’optimisation. Dans sa formulation standard, il n’est pas nécessaire d’entraîner séparément un modèle de récompense puis d’exécuter la même boucle PPO. Le modèle entraîné est comparé à une référence figée. L’objectif porte sur la différence entre les log-probabilités des deux réponses, relativement à cette référence. Pour une première lecture, retenez le mouvement recherché : favoriser davantage la réponse préférée par rapport à l’autre, en tenant compte du point de départ. Cette description ne signifie pas que la réponse préférée devient automatiquement certaine ni que toutes les réponses possibles ont été comparées.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : réponse préférée → réponse écartée → modèle entraîné → référence figée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Lire une différence relative

Repère provisoire : 05:47 à 06:46. Audio : `semaine-12-07.wav`.

### Narration

Prenons un exemple purement illustratif. Pour une paire donnée, la différence de log-probabilités entre la réponse préférée et l’autre vaut plus un dans le modèle entraîné, et zéro dans la référence. La différence relative vaut donc plus un avant l’application des autres éléments de l’objectif. Si la référence favorisait déjà fortement la réponse préférée, il faudrait en tenir compte. Cette comparaison évite de lire une probabilité isolée comme toute l’information utile. Les log-probabilités concernent des séquences de tokens, et l’implémentation de la perte doit être étudiée avec soin. Nous ne cherchons pas ici à convertir la marge affichée en pourcentage de vérité ou de satisfaction humaine.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : modèle : différence +1 → référence : différence 0 → marge : +1 → préférence favorisée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 8 : Évaluer sans réutiliser les mêmes paires

Repère provisoire : 06:46 à 07:43. Audio : `semaine-12-08.wav`.

### Narration

Après l’entraînement, évaluons des demandes réservées. Nous pouvons comparer les réponses du modèle initial et du modèle ajusté en masquant leur origine aux évaluateurs. La grille doit rester cohérente avec l’objectif pédagogique. Mesurons également l’exactitude et les cas difficiles, car une préférence globale peut cacher une dégradation sur les calculs ou les réponses courtes. Des jeux de test trop proches des paires d’entraînement risquent de surestimer la généralisation. Conservez aussi des exemples de désaccord entre annotateurs. Ils indiquent parfois une ambiguïté de la tâche qui ne peut pas être résolue simplement par davantage d’entraînement ou par un réglage plus fort de l’objectif.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : paires d’entraînement → demandes réservées → comparaison aveugle → erreurs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 9 : Distinguer trois rôles

Repère provisoire : 07:43 à 08:43. Audio : `semaine-12-09.wav`.

### Narration

Pour terminer, expliquez les trois distinctions suivantes. Une démonstration fournit une réponse attendue ; une préférence compare des réponses. Un modèle de récompense estime un score de préférence ; un modèle de référence fournit un point de comparaison. Enfin, DPO et une démarche RLHF avec PPO n’organisent pas l’optimisation de la même façon. Prenez quelques secondes pour refaire les deux schémas. La question centrale reste commune : quels comportements les données et l’objectif encouragent-ils réellement ? Si vous pouvez répondre à cette question avec des exemples de réussite et d’échec, vous avez dépassé la simple mémorisation des sigles et vous pouvez analyser les limites d’une procédure d’alignement.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : démonstration → récompense apprise → modèle de référence → comparaison directe.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Référence de préparation

[DPO](https://arxiv.org/abs/2305.18290)
