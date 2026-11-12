# Semaine 2 : Du texte aux vecteurs : tokens, identifiants et embeddings

## Préparation

**713 mots ; durée indicative 06:41 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:48 à 07:11.**

Fichier audio complet possible : `semaine-02.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Trois objets différents

Repère provisoire : 00:00 à 00:56. Audio : `semaine-02-01.wav`.

### Narration

Aujourd’hui, nous allons suivre une phrase depuis sa forme lisible jusqu’aux nombres utilisés par le modèle. Trois objets doivent rester distincts : le token, son identifiant et son vecteur. Un token est une unité produite par un découpage. L’identifiant sert à retrouver cette unité dans un vocabulaire. Le vecteur est une représentation numérique apprise. Cette distinction évite une confusion fréquente : un identifiant plus grand n’indique pas un sens plus important. À la fin, vous pourrez expliquer pourquoi deux tokeniseurs découpent une même phrase différemment et pourquoi deux vecteurs peuvent être comparés même si leurs identifiants sont très éloignés.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : texte → tokens → identifiants → vecteurs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Un découpage illustratif

Repère provisoire : 00:56 à 01:55. Audio : `semaine-02-02.wav`.

### Narration

Prenons « Les chats dorment ». Pour notre exemple pédagogique, imaginons les unités « Les », « chats », « dor » et « ment », puis la ponctuation. Ce découpage est inventé : un vrai résultat dépend du tokeniseur, des espaces, de la casse et du vocabulaire appris. Un token ne correspond donc pas toujours à un mot. Il peut représenter un morceau de mot ou plusieurs caractères. Cela explique pourquoi une limite de mille tokens ne correspond pas à mille mots. Pour mesurer la taille d’un document, utilisez le tokeniseur du modèle concerné plutôt qu’une conversion universelle fondée sur le nombre de mots.

### Réalisation Manim

Visuel : `tokens`. Apparition progressive : Les → chats → dor + ment → ..

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Apprendre des unités fréquentes

Repère provisoire : 01:55 à 02:52. Audio : `semaine-02-03.wav`.

### Narration

L’idée de méthodes fondées sur des fusions est de construire des unités utiles à partir d’éléments plus petits. Dans une version simplifiée de BPE, on compte des paires voisines et on fusionne une paire fréquente, puis on recommence. Le vocabulaire obtenu dépend du corpus d’apprentissage. Une séquence fréquente peut devenir une unité, tandis qu’un mot rare reste fragmenté. Certaines variantes partent d’octets, d’autres d’unités différentes. Il faut éviter de confondre le principe général et une implémentation précise. La fragmentation observée sur une langue peut augmenter le coût de traitement, sans suffire à mesurer toute la qualité du modèle dans cette langue.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : caractères ou octets → paires fréquentes → fusions → vocabulaire.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Les identifiants sont des adresses

Repère provisoire : 02:52 à 03:47. Audio : `semaine-02-04.wav`.

### Narration

Attribuons maintenant l’identifiant sept au token chat et l’identifiant quarante-deux au token moteur. Ces valeurs sont fictives. Nous ne devons pas conclure que moteur représente six fois chat. Les nombres servent ici d’adresses. Une table d’embeddings possède une ligne par entrée du vocabulaire. Pour le token d’identifiant sept, le programme sélectionne la ligne sept. Si le vocabulaire contient mille unités et que chaque vecteur comporte seize composantes, la table contient mille fois seize paramètres, soit seize mille nombres. Observez les dimensions : une séquence de cinq tokens donne cinq vecteurs de seize composantes avant l’ajout d’autres traitements.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : chat : ID 7 → table E → ligne 7 → vecteur.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Comparer les directions

Repère provisoire : 03:47 à 04:45. Audio : `semaine-02-05.wav`.

### Narration

Utilisons de petits vecteurs pour effectuer un calcul complet. Le vecteur u vaut un, zéro. Le vecteur v vaut deux, zéro. Leur produit scalaire vaut deux ; leurs normes valent un et deux. La similarité cosinus vaut donc deux divisé par deux, soit un. Le vecteur w, zéro, un, est orthogonal à u : leur produit scalaire vaut zéro et leur similarité aussi. La longueur différente de u et v n’empêche pas leur direction d’être identique. Attention cependant : dans un modèle réel, un cosinus élevé signale une proximité dans l’espace appris. Il ne démontre pas que deux phrases ont exactement le même sens.

### Réalisation Manim

Visuel : `vectors`. Apparition progressive : u = (1, 0) → v = (2, 0) → w = (0, 1) → cosinus.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Le contexte transforme les représentations

Repère provisoire : 04:45 à 05:41. Audio : `semaine-02-06.wav`.

### Narration

Un même token commence généralement par la même ligne de la table d’entrée. Pourtant, souris dans une phrase informatique ne doit pas être traité exactement comme souris dans une phrase sur les animaux. Les couches du modèle combinent la représentation initiale avec le contexte et produisent des représentations contextualisées. Il faut donc préciser ce que l’on compare : les vecteurs de la table d’entrée, ceux d’une couche intermédiaire ou un vecteur représentant toute une phrase. Comparer des sorties provenant de modèles différents sans alignement préalable n’a généralement pas de sens, même si les vecteurs ont le même nombre de composantes.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : souris : entrée → phrase informatique → phrase animale → sorties.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Exercice de lecture du pipeline

Repère provisoire : 05:41 à 06:41. Audio : `semaine-02-07.wav`.

### Narration

Voici un exercice. Un texte produit six tokens et le modèle utilise des embeddings de dimension huit. Quelle est la forme de la représentation obtenue pour cette séquence, en laissant de côté la dimension de lot ? Prenez un moment : six lignes et huit colonnes, donc quarante-huit valeurs. Les six identifiants d’entrée ne sont pas ces quarante-huit valeurs ; ils permettent de les sélectionner. Pour vérifier votre compréhension, expliquez ensuite pourquoi changer de tokeniseur peut changer la longueur de la séquence. Enfin, retenez les trois étapes : découper le texte, retrouver des identifiants dans un vocabulaire, puis sélectionner des vecteurs qui seront transformés par le contexte.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : 6 tokens → dimension 8 → 6 × 8 → 48 valeurs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
