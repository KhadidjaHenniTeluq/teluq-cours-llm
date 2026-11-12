# Semaine 6 : Construire et évaluer une recherche sémantique

## Préparation

**738 mots ; durée indicative 06:53 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:59 à 07:25.**

Fichier audio complet possible : `semaine-06.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Chercher au-delà des mots identiques

Repère provisoire : 00:00 à 01:00. Audio : `semaine-06-01.wav`.

### Narration

Une étudiante demande : « comment reporter la date de remise ? » Le document pertinent utilise peut-être les mots « prolongation du délai ». Une recherche fondée uniquement sur la présence des mêmes termes peut manquer ce passage. La recherche sémantique représente la question et les documents dans un espace où l’on peut comparer leurs vecteurs. Notre objectif est de construire le parcours complet, depuis les documents jusqu’aux résultats évalués. Nous verrons aussi pourquoi cette méthode n’est pas toujours suffisante : les identifiants exacts, les nombres et les noms de produits peuvent demander une recherche lexicale complémentaire. Le choix dépend du corpus et des questions réelles.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : question → documents → sens proche → résultats.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Préparer les passages

Repère provisoire : 01:00 à 02:00. Audio : `semaine-06-02.wav`.

### Narration

Un document entier peut contenir plusieurs sujets. Nous le découpons en passages pour que chaque unité indexée conserve une information assez ciblée. Un passage trop court perd son contexte ; un passage trop long mélange des informations et occupe davantage de place lors d’une utilisation ultérieure. Le chevauchement entre deux passages peut éviter de couper une explication, mais augmente la redondance. Conservez le titre, la source, la date et un identifiant. Ces métadonnées servent à comprendre les résultats et à appliquer les règles prévues par l’application. Il n’existe pas de longueur de découpage optimale pour tous les cours : comparez plusieurs choix sur un petit jeu de questions.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : document → découpage → passages → métadonnées.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Encoder dans un espace commun

Repère provisoire : 02:00 à 02:58. Audio : `semaine-06-03.wav`.

### Narration

Nous calculons ensuite un vecteur pour chaque passage à l’aide d’un modèle prévu pour la recherche ou la similarité. À l’arrivée d’une question, nous appliquons le traitement compatible avec ce modèle. Certains modèles demandent des préfixes différents pour les questions et les passages ; il faut respecter leurs consignes. Ne mélangez pas un index construit avec un modèle et des questions encodées par un autre sous prétexte que la dimension est identique. Les coordonnées n’ont pas nécessairement la même signification. Si le modèle ou le prétraitement change, il peut être nécessaire de reconstruire les vecteurs et de réévaluer toute la chaîne de recherche.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : passage A → encodeur → vecteur A → index.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Un classement calculable

Repère provisoire : 02:58 à 03:59. Audio : `semaine-06-04.wav`.

### Narration

Utilisons trois vecteurs de norme un. La question vaut un, zéro. Le passage A a le même vecteur ; le passage B vaut zéro virgule huit, zéro virgule six ; le passage C vaut zéro, un. Comme les normes valent un, le produit scalaire donne directement la similarité cosinus. Les scores sont un pour A, zéro virgule huit pour B et zéro pour C. Le classement est donc A, B, C. Dans cet exemple inventé, nous connaissons tous les nombres. Dans un système réel, les scores dépendent du modèle et ne représentent pas automatiquement des probabilités de pertinence. Un seuil doit être choisi et validé pour le contexte d’utilisation.

### Réalisation Manim

Visuel : `retrieval`. Apparition progressive : q = (1, 0) → A = (1, 0) → B = (0,8 ; 0,6) → C = (0, 1).

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Rechercher exactement ou approximativement

Repère provisoire : 03:59 à 04:57. Audio : `semaine-06-05.wav`.

### Narration

Pour un petit corpus, comparer la question à tous les passages peut être tout à fait raisonnable. Lorsque le corpus grandit, des index approchés permettent de réduire certains coûts de recherche, au prix d’un compromis sur les voisins effectivement retrouvés. Il faut distinguer la qualité du modèle d’embedding et celle de l’index. Si un passage pertinent n’est pas retourné, le problème peut venir de la représentation, du découpage, du filtre ou de l’approximation. Mesurez aussi le temps et la mémoire. Ajouter un index complexe à un corpus minuscule peut rendre le système plus difficile à comprendre sans apporter de bénéfice utile pour les étudiants.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : vecteurs → comparaison exhaustive → index approché → compromis.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Mesurer ce qui a été retrouvé

Repère provisoire : 04:57 à 05:55. Audio : `semaine-06-06.wav`.

### Narration

Supposons maintenant que, selon une annotation humaine, les passages pertinents soient A et C. Notre système retourne A et B dans ses deux premiers résultats. La précision à deux vaut un demi, puisqu’un seul des deux résultats est pertinent. Le rappel à deux vaut également un demi, puisque nous avons retrouvé un des deux passages pertinents connus. Ce résultat montre qu’un classement cohérent avec les vecteurs n’est pas forcément satisfaisant pour l’utilisateur. Il faut disposer de jugements de pertinence et discuter leurs limites. Si plusieurs passages peuvent répondre partiellement à la question, une simple étiquette binaire peut être insuffisante pour décrire leur utilité.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : pertinents : A et C → top 2 : A et B → précision : 1/2 → rappel : 1/2.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Diagnostiquer avant de modifier

Repère provisoire : 05:55 à 06:53. Audio : `semaine-06-07.wav`.

### Narration

Voici l’exercice final. Une question contient un numéro exact de formulaire et la recherche sémantique retourne des formulaires ressemblants, mais pas le bon. Quelle piste testeriez-vous ? Une recherche lexicale ou hybride peut mieux exploiter cet identifiant. Vérifiez d’abord que le passage attendu existe et que son texte n’a pas été perdu pendant l’extraction. Comparez ensuite les résultats sur plusieurs questions, pas sur ce seul exemple. Le parcours à retenir est : préparer les passages, produire des vecteurs compatibles, choisir une recherche, puis évaluer les documents retrouvés. Une amélioration utile doit pouvoir être reliée à un problème observé et confirmée sur des exemples réservés.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : question difficile → passage attendu → étape en défaut → nouvel essai.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
