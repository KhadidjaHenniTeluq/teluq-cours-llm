# Semaine 7 : Découvrir des sujets dans un corpus avec BERTopic

## Préparation

**722 mots ; durée indicative 06:45 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:52 à 07:16.**

Fichier audio complet possible : `semaine-07.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Des messages sans catégories

Repère provisoire : 00:00 à 00:58. Audio : `semaine-07-01.wav`.

### Narration

Imaginons deux cents messages envoyés par des étudiants : certains parlent des échéances, d’autres des accès informatiques, d’autres encore des difficultés avec les exercices. Nous aimerions explorer leurs thèmes sans définir toutes les catégories à l’avance. La modélisation de sujets peut nous aider à résumer le corpus. Elle ne découvre pas automatiquement une vérité cachée ni les intentions exactes des auteurs. Dans cette capsule, nous suivons les étapes d’une configuration courante de BERTopic et nous apprenons à lire ses résultats avec prudence. Le but est de produire des groupes interprétables, de vérifier des exemples et de comprendre l’effet de nos choix de traitement.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : messages étudiants → aucune étiquette → groupes possibles → inspection.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Conserver le sens des documents

Repère provisoire : 00:58 à 01:57. Audio : `semaine-07-02.wav`.

### Narration

Commençons par les données. Nous supprimons les doublons exacts lorsque cela correspond à l’objectif, nous repérons les messages vides et nous conservons les informations nécessaires pour retrouver la source. Il faut éviter un nettoyage qui détruit des distinctions utiles : retirer une négation peut changer le sens d’une plainte. Les documents sont ensuite représentés par des embeddings. Ces vecteurs cherchent à rendre comparables les contenus selon le modèle choisi. La longueur et la langue des messages peuvent influencer le résultat. Si le corpus mélange plusieurs langues, vérifier la compatibilité du modèle est plus utile que supposer que tous les vecteurs seront spontanément alignés de manière satisfaisante.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : message original → nettoyage limité → métadonnées → embeddings.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Réduire la dimension

Repère provisoire : 01:57 à 02:53. Audio : `semaine-07-03.wav`.

### Narration

Une configuration courante utilise une réduction de dimension, souvent UMAP, avant le regroupement. L’objectif est de rendre certaines structures plus faciles à exploiter par l’étape suivante. Cette transformation n’est pas une photographie exacte de l’espace d’origine. Les distances et les formes peuvent changer. Un nuage projeté en deux dimensions est utile pour explorer, mais il faut éviter de lire chaque séparation visuelle comme une frontière naturelle incontestable. Les paramètres et l’aléatoire peuvent modifier la disposition. Notez la configuration utilisée et distinguez la dimension destinée au regroupement de la projection éventuellement choisie seulement pour afficher un graphique lisible à l’écran.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : vecteurs nombreux → réduction → voisinages → nouvel espace.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Former des groupes et garder les atypiques

Repère provisoire : 02:53 à 03:51. Audio : `semaine-07-04.wav`.

### Narration

Une méthode de regroupement fondée sur la densité, comme HDBSCAN dans une configuration fréquente, peut produire plusieurs groupes et laisser certains documents comme atypiques. Cela ne signifie pas que ces messages sont inutiles ou incorrects. Ils peuvent exprimer un sujet rare, mélanger plusieurs thèmes ou être mal représentés par le modèle. Leur examen fait partie de l’analyse. Un groupe contenant vingt messages ne garantit pas non plus que ses vingt membres parlent exactement de la même chose. Le regroupement dépend des représentations et des paramètres. Nous devons donc lire des documents proches du centre apparent, mais aussi ceux qui semblent moins représentatifs du groupe.

### Réalisation Manim

Visuel : `clusters`. Apparition progressive : groupe A → groupe B → groupe C → points atypiques.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Décrire un groupe avec des mots

Repère provisoire : 03:51 à 04:49. Audio : `semaine-07-05.wav`.

### Narration

Une fois les groupes obtenus, il faut les décrire. BERTopic peut utiliser une représentation fondée sur c-TF-IDF : les documents d’un groupe sont considérés ensemble pour identifier des termes qui le caractérisent par rapport aux autres groupes. Cette étape ne fonctionne pas de la même façon que les embeddings utilisés au départ. On retrouve ici des informations lexicales utiles pour nommer un sujet. Par exemple, les mots délai, remise et prolongation peuvent suggérer un thème sur les échéances. Pourtant, un mot fréquent peut être administratif et peu informatif. Les mots proposés constituent une aide à l’interprétation, à confirmer par la lecture des messages concernés.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : documents du groupe → comptage des termes → c-TF-IDF → mots descriptifs.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Un exemple de contrôle humain

Repère provisoire : 04:49 à 05:46. Audio : `semaine-07-06.wav`.

### Narration

Supposons qu’un groupe soit décrit par accès, mot de passe et date limite. Avant de l’appeler « problèmes informatiques », lisons plusieurs messages. Certains étudiants ont peut-être oublié leur mot de passe juste avant une remise, tandis que d’autres discutent seulement d’un délai. Deux thèmes peuvent avoir été mélangés. Nous pouvons comparer une autre configuration ou garder un intitulé plus précis. Le contrôle ne consiste pas à choisir uniquement les exemples qui confirment notre intuition. Il faut aussi chercher des contre-exemples. Documentez les cas ambigus et évitez de transformer les groupes exploratoires en décisions individuelles concernant les étudiants sans autre vérification.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : accès → mot de passe → date limite → groupe à vérifier.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Comparer deux solutions

Repère provisoire : 05:46 à 06:45. Audio : `semaine-07-07.wav`.

### Narration

Pour votre exercice, comparez deux configurations sur le même corpus. Notez le nombre de groupes, leur taille, la proportion de documents atypiques et la facilité à décrire chaque groupe avec des exemples. Une solution comportant davantage de groupes n’est pas automatiquement meilleure. Elle peut distinguer des thèmes utiles ou simplement fragmenter un sujet. Posez-vous cette question : si plusieurs messages semblables changent de groupe après une petite modification des paramètres, quelle confiance accordez-vous à l’étiquette proposée ? La réponse invite à examiner la stabilité. Retenez enfin les étapes : représenter, réduire éventuellement la dimension, regrouper, décrire et contrôler. Chacune peut influencer l’interprétation finale du corpus.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : configuration A → configuration B → exemples représentatifs → stabilité.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Référence de préparation

[BERTopic : algorithme](https://maartengr.github.io/BERTopic/algorithm/algorithm.html)
