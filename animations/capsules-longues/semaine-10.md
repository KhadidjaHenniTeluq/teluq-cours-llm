# Semaine 10 : Relier images et textes : patches, CLIP et limites

## Préparation

**730 mots ; durée indicative 06:49 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:55 à 07:21.**

Fichier audio complet possible : `semaine-10.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Deux formes de données

Repère provisoire : 00:00 à 00:57. Audio : `semaine-10-01.wav`.

### Narration

Une image et une phrase décrivent parfois le même objet, mais elles n’arrivent pas au modèle sous la même forme. L’image contient des valeurs de pixels organisées dans l’espace ; le texte est transformé en tokens. Pour faire correspondre ces informations, nous devons construire des représentations numériques adaptées. Nous allons distinguer deux idées : transformer une image en une séquence utilisable par un Transformer et apprendre à rapprocher des images de descriptions textuelles. Cette distinction évite de confondre un encodeur visuel, un modèle de comparaison image-texte et un système capable de produire une réponse en langage naturel à propos d’une image.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : image → pixels → texte → tokens.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Découper une image en patches

Repère provisoire : 00:57 à 01:53. Audio : `semaine-10-02.wav`.

### Narration

Prenons une image de deux cent vingt-quatre pixels de côté et découpons-la en carrés de seize pixels de côté, sans chevauchement. Nous obtenons quatorze patches par ligne et quatorze par colonne, soit cent quatre-vingt-seize patches. Si l’image possède trois canaux de couleur, chaque patch contient seize fois seize fois trois valeurs avant projection. Une transformation apprise produit ensuite un vecteur par patch. Le modèle doit aussi disposer d’une information de position pour distinguer les arrangements spatiaux. Ce calcul est un exemple de configuration, pas une règle universelle. D’autres modèles utilisent d’autres résolutions, tailles de patches ou traitements de l’image.

### Réalisation Manim

Visuel : `patches`. Apparition progressive : image 224 × 224 → patch 16 × 16 → 14 × 14 patches → 196 patches.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Combiner les parties de l’image

Repère provisoire : 01:53 à 02:52. Audio : `semaine-10-03.wav`.

### Narration

Une fois les patches représentés par des vecteurs, les couches d’attention peuvent combiner des informations provenant de différentes zones. Pour reconnaître un vélo, il peut être utile de relier des indices sur les roues, le cadre et le guidon. Cependant, un patch ne correspond pas automatiquement à un objet complet, et une tête d’attention ne possède pas nécessairement un rôle simple que nous pourrions nommer. La représentation finale dépend de l’entraînement. Lorsque l’image contient de petits caractères ou des détails fins, la résolution et le découpage peuvent limiter l’information disponible. Agrandir un affichage après l’encodage ne recrée pas les détails qui ont été perdus au départ.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : patch roue → patch cadre → patch guidon → représentation.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Apprendre des correspondances avec CLIP

Repère provisoire : 02:52 à 03:49. Audio : `semaine-10-04.wav`.

### Narration

Dans CLIP, un encodeur traite les images et un autre traite les textes. L’apprentissage cherche à rapprocher les représentations des paires associées et à distinguer les autres associations du lot. La formulation précise utilise des scores de similarité et un objectif contrastif. Intuitivement, une image de vélo devrait obtenir un score élevé avec sa description associée par rapport aux descriptions concurrentes. Cela n’exige pas que l’encodeur produise une phrase. Il apprend un espace de comparaison. Les données d’entraînement peuvent contenir des descriptions incomplètes ou des biais ; les associations apprises reflètent donc aussi les régularités et les limites de ces données.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : encodeur image → encodeur texte → vecteurs → similarités.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Comparer des descriptions candidates

Repère provisoire : 03:49 à 04:49. Audio : `semaine-10-05.wav`.

### Narration

À l’utilisation, nous pouvons encoder une image et plusieurs descriptions candidates : « un vélo », « une voiture » et « un arbre ». Nous calculons leurs similarités et obtenons un classement relatif à ces descriptions. Si vélo arrive en tête, cela ne prouve pas que l’image a été comprise dans tous ses détails. Le résultat dépend des candidats proposés. Si aucune description ne convient, un maximum existe quand même. Il faut également tester la sensibilité aux formulations. Une comparaison entre catégories est différente d’une réponse ouverte à une question comme « la roue arrière est-elle endommagée ? », qui demande d’autres capacités et un protocole spécifique.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : image de vélo → un vélo → une voiture → un arbre.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Passer à une réponse générée

Repère provisoire : 04:49 à 05:49. Audio : `semaine-10-06.wav`.

### Narration

Un système qui répond en phrases à propos d’une image doit relier les informations visuelles à un modèle génératif. Selon l’architecture, un module transforme ou sélectionne les représentations visuelles avant leur utilisation par le modèle de langage. Les détails varient entre les systèmes. Ce raccordement ne garantit pas que chaque phrase produite corresponde à un détail réellement visible. Un modèle peut compléter avec une association plausible et inventer un objet. Il faut donc comparer la réponse à l’image et distinguer observation et inférence. Pour les nombres, les tableaux ou les petites inscriptions, prévoyez des tests ciblés plutôt que de généraliser à partir d’une description de scène réussie.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : encodeur visuel → module de liaison → modèle de langage → réponse.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Deux questions pour vérifier

Repère provisoire : 05:49 à 06:49. Audio : `semaine-10-07.wav`.

### Narration

Revenons au calcul : combien de patches obtenons-nous avec quatorze lignes de quatorze patches ? Cent quatre-vingt-seize. Pourquoi ce nombre compte-t-il ? Parce qu’il contribue à la longueur de la séquence traitée et donc au coût du modèle. Deuxième question : si la meilleure description parmi trois est « un vélo », pouvons-nous conclure qu’un vélo est certainement présent ? Non, les trois candidats peuvent être inadéquats. Pour votre exercice, proposez une image ambiguë et plusieurs descriptions proches, puis examinez ce que le classement permet réellement d’affirmer. Retenez les trois niveaux distincts : encoder une image, comparer des représentations et générer une réponse vérifiable à partir d’informations visuelles.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : 196 patches → comparaison relative → objet absent → vérification visuelle.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
