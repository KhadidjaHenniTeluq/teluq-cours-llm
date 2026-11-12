# Semaine 3 : Calculer une attention et comprendre le masque causal

## Préparation

**700 mots ; durée indicative 06:33 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:42 à 07:04.**

Fichier audio complet possible : `semaine-03.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Le problème à résoudre

Repère provisoire : 00:00 à 00:55. Audio : `semaine-03-01.wav`.

### Narration

Nous allons calculer une petite attention du début à la fin. L’objectif n’est pas de mémoriser une formule isolée, mais de comprendre ce que chaque opération apporte. Une position doit combiner des informations provenant d’autres positions. Pour cela, le modèle produit des requêtes, des clés et des valeurs à partir des représentations d’entrée. Ces transformations sont apprises. Dans notre exemple, nous fixerons les nombres pour pouvoir suivre le calcul à la main. Les petites dimensions et les scores affichés servent uniquement à l’explication. Ils ne proviennent pas d’un modèle entraîné et ne décrivent pas une interprétation linguistique universelle.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : trois positions → une requête → trois clés → trois valeurs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Requêtes, clés et valeurs

Repère provisoire : 00:55 à 01:51. Audio : `semaine-03-02.wav`.

### Narration

La requête d’une position est comparée aux clés des positions disponibles. Les valeurs constituent les informations qui seront combinées après le calcul des poids. Une analogie possible est celle d’une recherche : la requête décrit une comparaison, les clés rendent cette comparaison possible, puis les valeurs fournissent le contenu retenu. Mais les objets réels sont des vecteurs appris, pas des fiches lisibles. Si la matrice d’entrée possède trois lignes, une par token, multiplier cette matrice par les matrices de projection donne trois requêtes, trois clés et trois valeurs. Les matrices de projection sont partagées entre les positions d’une même tête.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : Q : ce que je compare → K : ce que je présente → V : ce que je transmets.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Des produits scalaires aux scores

Repère provisoire : 01:51 à 02:46. Audio : `semaine-03-03.wav`.

### Narration

Le produit scalaire d’une requête avec chaque clé produit une liste de scores. On divise ces scores par la racine carrée de la dimension des clés. Cette mise à l’échelle limite l’augmentation de leur amplitude associée à la dimension sous des hypothèses usuelles. Elle ne transforme pas les scores en probabilités. Pour notre calcul, supposons qu’après cette division les trois scores soient zéro, un et deux. Ils peuvent être négatifs dans un autre exemple. Ce qui compte maintenant est leur comparaison relative. Une même constante ajoutée à tous ces scores ne changera pas les poids du softmax.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : Q × Kᵀ → division par √dₖ → 0 ; 1 ; 2 → scores.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Calculer le softmax

Repère provisoire : 02:46 à 03:42. Audio : `semaine-03-04.wav`.

### Narration

Le softmax exponentie chaque score et divise chaque résultat par la somme des exponentielles. Pour zéro, un et deux, nous obtenons environ un, deux virgule sept cent dix-huit et sept virgule trois cent quatre-vingt-neuf. Leur somme vaut environ onze virgule cent sept. Les poids sont donc approximativement neuf pour cent, vingt-quatre virgule cinq pour cent et soixante-six virgule cinq pour cent. Ils sont positifs et leur somme vaut un, aux arrondis près. Le dernier score domine, mais les autres positions contribuent encore. Une attention ne revient donc pas nécessairement à choisir une seule position et à ignorer toutes les autres.

### Réalisation Manim

Visuel : `softmax`. Apparition progressive : exp(0) = 1 → exp(1) ≈ 2,718 → exp(2) ≈ 7,389 → somme ≈ 11,107.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Combiner les valeurs

Repère provisoire : 03:42 à 04:37. Audio : `semaine-03-05.wav`.

### Narration

Choisissons maintenant trois valeurs : un, zéro ; zéro, deux ; puis deux, un. Nous multiplions chaque vecteur par son poids et additionnons les résultats. La première coordonnée vaut environ zéro virgule zéro neuf plus zéro plus un virgule trente-trois, soit un virgule quarante-deux. La deuxième vaut zéro plus zéro virgule quarante-neuf plus zéro virgule soixante-six cinq, soit environ un virgule quinze. La sortie est un nouveau vecteur. Elle n’est ni le score le plus élevé ni la liste des poids. Cette différence entre poids d’attention et sortie de l’attention est essentielle pour suivre le reste du Transformer.

### Réalisation Manim

Visuel : `weighted`. Apparition progressive : V₁ = (1, 0) → V₂ = (0, 2) → V₃ = (2, 1) → sortie ≈ (1,42 ; 1,15).

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Interdire les positions futures

Repère provisoire : 04:37 à 05:35. Audio : `semaine-03-06.wav`.

### Narration

Dans un décodeur causal, la position deux ne doit pas consulter la position trois. Le masque intervient avant le softmax : les positions interdites reçoivent une valeur qui conduit à un poids nul, idéalement moins l’infini. Les poids sont alors normalisés uniquement sur les positions autorisées. Si notre troisième score est masqué, il ne faut pas simplement conserver neuf et vingt-quatre virgule cinq pour cent. On recalcule la normalisation de zéro et un, ce qui donne environ vingt-six virgule neuf et soixante-treize virgule un pour cent. Pendant l’entraînement, ce masque permet de traiter plusieurs positions en parallèle sans leur révéler leurs cibles futures.

### Réalisation Manim

Visuel : `causal`. Apparition progressive : position 1 → positions 1 à 2 → positions 1 à 3 → masque triangulaire.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Plusieurs têtes et une vérification

Repère provisoire : 05:35 à 06:33. Audio : `semaine-03-07.wav`.

### Narration

Plusieurs têtes utilisent différentes projections apprises et peuvent construire différentes combinaisons. Leurs sorties sont réunies puis projetées pour poursuivre le calcul. Il serait trompeur d’attribuer à chaque tête un rôle fixe, comme la grammaire ou les émotions, sans observation du modèle. Pour terminer, refaites le calcul avec deux scores égaux et deux valeurs différentes. Quels poids obtenez-vous ? Un demi pour chaque valeur. La sortie est leur moyenne. Expliquez ensuite à voix haute pourquoi masquer une position change aussi les autres poids. Si vous distinguez scores, poids et valeurs, vous disposez des repères nécessaires pour lire la formule de l’attention sans la réciter mécaniquement.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : tête A → tête B → concaténation → projection.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
