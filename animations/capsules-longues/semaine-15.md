# Semaine 15 : Lire une boucle d’entraînement GPT et vérifier ce qu’elle apprend

## Préparation

**742 mots ; durée indicative 06:55 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 06:00 à 07:27.**

Fichier audio complet possible : `semaine-15.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Relier les notions dans un petit projet

Repère provisoire : 00:00 à 00:56. Audio : `semaine-15-01.wav`.

### Narration

Pour cette dernière capsule, nous suivons une boucle d’entraînement de type GPT dans un petit projet pédagogique inspiré de minGPT. Nous ne prétendons pas entraîner un grand assistant en quelques minutes. L’objectif est de relier les notions du cours : tokens, prédiction causale, perte, gradients et génération. Un code compact permet d’observer ces étapes, à condition de distinguer le schéma pédagogique d’une version précise d’un dépôt. Nous allons utiliser une séquence courte et vérifier les formes des données. À la fin, vous pourrez identifier ce qui relève de l’apprentissage, ce qui relève de l’évaluation et ce qui relève du décodage.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : tokens → Transformer causal → perte → mise à jour.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Préparer entrées et cibles

Repère provisoire : 00:56 à 01:57. Audio : `semaine-15-02.wav`.

### Narration

Prenons une séquence composée des tokens A, B, C et D. Nous construisons l’entrée A, B, C et les cibles B, C, D. Le modèle doit prédire B après A, C après A et B, puis D après A, B et C. Cette description explique le décalage des tableaux. Pour un lot de deux séquences de longueur trois, les identifiants d’entrée forment un tableau de deux lignes et trois colonnes. Le masque causal interdit à chaque position d’utiliser ses tokens futurs. Avant de lancer un entraînement, affichez quelques couples entrée-cible : une erreur de décalage peut rendre les résultats difficiles à interpréter malgré un programme qui s’exécute sans exception.

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : séquence : A B C D → entrée : A B C → cible : B C D → décalage.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Effectuer la passe avant

Repère provisoire : 01:57 à 02:54. Audio : `semaine-15-03.wav`.

### Narration

La passe avant transforme les identifiants en embeddings, ajoute ou intègre les informations de position selon l’architecture, puis applique les blocs du modèle. La couche de sortie produit des scores sur le vocabulaire à chaque position. Si le vocabulaire contient dix unités, notre lot de deux séquences de trois positions produit une sortie de forme deux, trois, dix. Ces scores ne sont pas encore des identifiants choisis. Pendant l’apprentissage, nous les utilisons pour calculer la perte par rapport aux cibles. Il n’est pas nécessaire de générer un paragraphe complet à chaque étape pour savoir si les cibles reçoivent une probabilité suffisante.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : identifiants → embeddings → blocs causaux → scores vocabulaire.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Comprendre une perte élémentaire

Repère provisoire : 02:54 à 03:55. Audio : `semaine-15-04.wav`.

### Narration

Pour une cible donnée, une perte de type entropie croisée pénalise une faible probabilité attribuée au token correct. Si cette probabilité vaut un demi, le logarithme négatif naturel vaut environ zéro virgule soixante-neuf. Si elle vaut un quart, la perte vaut environ un virgule trente-neuf. Le second cas est donc davantage pénalisé. Sur un lot, les pertes sont agrégées selon les positions retenues. Il faut gérer correctement les positions de remplissage ou les autres exclusions prévues. Une baisse de la perte sur les exemples d’apprentissage indique une amélioration sur cet objectif et ces données ; elle ne démontre pas à elle seule une meilleure qualité sur toutes les demandes.

### Réalisation Manim

Visuel : `loss`. Apparition progressive : cible correcte → probabilité 0,50 → probabilité 0,25 → perte plus élevée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Mettre à jour les paramètres

Repère provisoire : 03:55 à 04:55. Audio : `semaine-15-05.wav`.

### Narration

Une étape habituelle remet les gradients à zéro, calcule la perte, effectue la rétropropagation et demande à l’optimiseur de mettre à jour les paramètres entraînables. Sans remise à zéro, les gradients peuvent s’accumuler ; cette accumulation peut être volontaire dans certaines procédures, mais doit alors être conçue explicitement. Le taux d’apprentissage détermine une partie de l’amplitude des ajustements. Une valeur trop élevée peut rendre l’entraînement instable ; une valeur trop faible peut ralentir le progrès. Pour comprendre le code, repérez l’ordre de ces opérations et les paramètres réellement entraînés. Une variable appelée loss ne déclenche aucune mise à jour tant que les opérations correspondantes ne sont pas exécutées.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : remettre gradients à zéro → rétropropagation → optimiseur → nouveaux paramètres.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Évaluer sur des données réservées

Repère provisoire : 04:55 à 05:54. Audio : `semaine-15-06.wav`.

### Narration

Conservons une partie des données pour la validation et évitons de calculer des gradients lors de cette évaluation. Le mode d’évaluation modifie aussi le comportement de certains composants, comme le dropout. Si la perte d’entraînement baisse tandis que celle de validation augmente, nous devons examiner un possible surapprentissage et la qualité du découpage des données. Deux extraits presque identiques répartis entre entraînement et validation peuvent fausser l’analyse. Documentez donc la façon dont les exemples sont séparés. Les courbes fournissent des indices, mais il faut aussi lire quelques sorties et tester des cas représentatifs. Aucun indicateur unique ne remplace l’examen de ce que le modèle produit réellement.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : entraînement → validation → courbes séparées → surapprentissage possible.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Générer et conclure le projet

Repère provisoire : 05:54 à 06:55. Audio : `semaine-15-07.wav`.

### Narration

Après l’apprentissage, nous pouvons fournir un début de texte et générer une continuation. Cette étape utilise une règle de décodage, comme le choix glouton ou l’échantillonnage, qui doit être documentée. Une sortie amusante ou grammaticalement correcte ne constitue pas une évaluation complète. Pour votre compte rendu, montrez les formes des tenseurs, une évolution de perte, un exemple de génération et une limite observée. Expliquez enfin pourquoi changer la température après l’entraînement ne modifie pas les poids appris. Vous reliez ainsi les trois phases du projet : apprendre des paramètres, évaluer sur des données réservées et sélectionner des tokens pour produire une sortie. Ce sont des opérations liées, mais distinctes.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : début fourni → décodage → texte obtenu → analyse des limites.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
