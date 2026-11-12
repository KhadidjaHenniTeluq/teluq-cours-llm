# Semaine 11 : Adapter un modèle avec LoRA et comprendre la quantification

## Préparation

**955 mots ; durée indicative 08:54 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 07:44 à 09:35.**

Fichier audio complet possible : `semaine-11.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Adapter un comportement

Repère provisoire : 00:00 à 00:57. Audio : `semaine-11-01.wav`.

### Narration

Nous disposons d’un modèle préentraîné, mais nous souhaitons améliorer son comportement sur une tâche précise, par exemple rédiger des résumés de cours selon un format donné. Un ajustement supervisé utilise des exemples d’entrées et de sorties attendues. Avant de choisir une méthode technique, il faut préciser le besoin : voulons-nous modifier un style de réponse, apprendre une tâche ou fournir des informations qui changent souvent ? Ces objectifs ne se traitent pas toujours de la même manière. Dans cette capsule, nous étudions LoRA pour réduire le nombre de paramètres entraînables, puis la quantification pour représenter certains nombres avec moins de bits.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : modèle préentraîné → exemples de tâche → adaptation → évaluation.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Le coût d’une matrice complète

Repère provisoire : 00:57 à 01:54. Audio : `semaine-11-02.wav`.

### Narration

Considérons une matrice de poids de mille lignes et mille colonnes. Elle contient un million de paramètres. Si nous ajustons tous ces paramètres, l’entraînement doit aussi gérer des gradients et, selon l’optimiseur, des états supplémentaires. La mémoire totale dépend également des activations, de la précision numérique et de la longueur des séquences. Compter seulement les poids est donc insuffisant pour estimer le besoin en mémoire. Le calcul de ce petit exemple nous donne néanmoins un point de comparaison. Notre question devient : peut-on représenter une modification utile de cette matrice avec moins de paramètres que ceux de la matrice complète ?

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : W : 1000 × 1000 → 1 000 000 poids → gradients → états optimiseur.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Décomposer la modification

Repère provisoire : 01:54 à 02:54. Audio : `semaine-11-03.wav`.

### Narration

LoRA conserve la matrice de base et apprend une mise à jour construite à partir de deux matrices plus petites. Avec un rang de huit, prenons une matrice A de huit lignes et mille colonnes, et une matrice B de mille lignes et huit colonnes. Leur produit possède bien mille lignes et mille colonnes, comme la matrice initiale. Au lieu d’apprendre un million de nombres pour cette mise à jour, nous apprenons huit mille nombres dans A et huit mille dans B, soit seize mille. La mise à jour est contrainte par ce faible rang. Elle ne peut pas représenter n’importe quelle modification possible avec la même liberté.

### Réalisation Manim

Visuel : `lora`. Apparition progressive : W gelée → A : 8 × 1000 → B : 1000 × 8 → ΔW = B × A.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Comprendre la réduction annoncée

Repère provisoire : 02:54 à 03:53. Audio : `semaine-11-04.wav`.

### Narration

Seize mille divisé par un million donne un virgule six pour cent. Pour cette matrice et ce rang, le nombre de paramètres entraînables de l’adaptation est donc réduit de quatre-vingt-dix-huit virgule quatre pour cent par rapport à un ajustement complet de cette matrice. Ce résultat ne signifie pas que toute la mémoire ou tout le temps de calcul baisse dans la même proportion. Le modèle de base reste utilisé, les activations existent toujours et d’autres modules peuvent être adaptés. Lorsque vous lisez un pourcentage de réduction, demandez toujours ce qui est compté : une matrice, les paramètres entraînables du modèle ou l’ensemble de la mémoire d’entraînement.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : 1 000 000 → 16 000 → rapport : 1,6 % → réduction : 98,4 %.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Choisir le rang et les modules

Repère provisoire : 03:53 à 04:54. Audio : `semaine-11-05.wav`.

### Narration

Augmenter le rang ajoute des paramètres et donne davantage de capacité à la mise à jour. Cela ne garantit pas une amélioration sur les exemples réservés. Le choix dépend de la tâche, des données, des modules ciblés et du budget. Les noms de modules varient entre les architectures : avant de demander une adaptation de q_proj et v_proj, vérifiez que ces modules existent dans le modèle concerné. La mise à l’échelle de l’adaptation est également un paramètre à documenter ; dans une formulation courante, elle dépend du rapport entre alpha et le rang. Comparez quelques réglages de manière contrôlée plutôt que de choisir automatiquement le plus grand rang possible.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : rang faible → rang plus élevé → modules ciblés → validation.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Quantifier avec un petit exemple

Repère provisoire : 04:54 à 05:54. Audio : `semaine-11-06.wav`.

### Narration

La quantification est une autre idée. Elle représente des valeurs à l’aide d’un ensemble plus limité de niveaux et de paramètres associés. Pour l’illustrer, prenons une grille fictive avec zéro, zéro virgule vingt-cinq et zéro virgule cinquante. La valeur zéro virgule trente-sept est plus proche de zéro virgule vingt-cinq que de zéro virgule cinquante. La remplacer par ce niveau produit une erreur absolue de zéro virgule douze. Les méthodes réelles utilisent des grilles, des échelles et des regroupements plus élaborés. L’objectif est de réduire le stockage ou certains coûts, tout en conservant une qualité acceptable. La quantification ne garantit pas une absence de perte sur toutes les tâches.

### Réalisation Manim

Visuel : `quantize`. Apparition progressive : valeur : 0,37 → grille : 0 ; 0,25 ; 0,50 → arrondi : 0,25 → erreur : 0,12.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Combiner les deux idées

Repère provisoire : 05:54 à 06:55. Audio : `semaine-11-07.wav`.

### Narration

Dans une approche comme QLoRA, le modèle de base est représenté sous une forme quantifiée et les adaptateurs sont entraînés. Il ne faut pas en déduire que tous les calculs et tous les objets en mémoire utilisent exactement quatre bits. Les opérations nécessitent des traitements adaptés et certaines données restent dans d’autres précisions. La distinction importante est entre la représentation stockée de la base, les paramètres entraînables et les calculs effectués. Cette combinaison peut rendre certaines adaptations plus accessibles, mais la faisabilité dépend encore de la taille du modèle, du lot, des séquences et de l’environnement logiciel. Une promesse générale de fonctionnement sur n’importe quel GPU serait donc trompeuse.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : base quantifiée → adaptateurs LoRA → calculs intermédiaires → entraînement.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 8 : Évaluer l’adaptation

Repère provisoire : 06:55 à 07:54. Audio : `semaine-11-08.wav`.

### Narration

Préparez un ensemble d’exemples qui ne servent pas à entraîner les adaptateurs. Comparez le modèle initial et le modèle adapté sur les mêmes consignes. Observez le respect du format, la fidélité aux sources et les erreurs de contenu. Un modèle qui reproduit mieux le style des exemples peut aussi mémoriser certaines formulations ou perdre en qualité sur d’autres demandes. Notez les ressources utilisées et les paramètres de génération pour rendre la comparaison interprétable. Si le but est d’ajouter des informations souvent mises à jour, examinez aussi si un système documentaire serait plus adapté. L’ajustement ne doit pas remplacer une analyse du besoin et des données.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : modèle initial → mêmes exemples de test → modèle adapté → comparaison.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 9 : Vérifier les dimensions

Repère provisoire : 07:54 à 08:54. Audio : `semaine-11-09.wav`.

### Narration

Voici votre calcul final. Pour une matrice de cinq cents lignes et deux cents colonnes avec un rang de quatre, combien de paramètres faut-il dans les deux facteurs ? A en contient huit cents et B deux mille, soit deux mille huit cents au total. La matrice complète en contient cent mille. Prenez le temps de vérifier que le produit B fois A possède bien la forme attendue. Ce contrôle de dimensions aide à comprendre LoRA plus sûrement qu’un pourcentage appris par cœur. Retenez enfin trois décisions distinctes : quels paramètres adapter, comment représenter les poids et comment mesurer la qualité du modèle obtenu sur la tâche visée.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : W : 500 × 200 → rang : 4 → A : 4 × 200 → B : 500 × 4.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Référence de préparation

[LoRA](https://arxiv.org/abs/2106.09685)
