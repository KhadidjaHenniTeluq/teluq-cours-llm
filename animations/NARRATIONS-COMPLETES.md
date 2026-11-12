# Textes de narration des 20 animations

Version de préparation, à enregistrer avec votre voix. Les numéros de segment servent de repères et ne sont pas à lire. Les durées actuelles des vidéos ne sont pas des contraintes pour votre enregistrement.

## Semaine 1 : RNN et mémoire séquentielle

Audio : `recurrence.wav`

Un réseau récurrent lit une séquence étape par étape. Ici, il reçoit successivement les tokens « Le », « chat », « noir » et « dort ». À chaque étape, il met à jour un état caché.

Cet état dépend du token courant et de l’état précédent. Il transmet donc une partie de l’information déjà traitée. Pour calculer le deuxième état, il faut avoir calculé le premier.

Pendant l’entraînement, le gradient parcourt ces étapes dans le sens inverse. Sur de longues séquences, ce signal peut devenir très faible ou, au contraire, augmenter fortement.

Les LSTM utilisent des mécanismes de contrôle pour atténuer certaines de ces difficultés. Ils conservent toutefois une dépendance séquentielle entre leurs étapes.

## Semaine 2 : Du texte aux tokens

Audio : `tokenisation.wav`

Avant de traiter une phrase, le modèle reçoit une suite de tokens. Prenons « Les chats dorment ». Dans cet exemple, nous découpons la phrase en cinq unités, en comptant le point final.

Le mot « dorment » est séparé en deux morceaux. Cela montre qu’un token n’est pas forcément un mot entier. Certains tokens comprennent aussi un espace.

Chaque unité reçoit ensuite un identifiant. Les nombres affichés ici sont fictifs. Le découpage et les identifiants réels dépendent du tokeniseur choisi.

Enfin, chaque identifiant sert à sélectionner une ligne de la matrice d’embeddings. Deux identifiants proches ne désignent pas nécessairement deux mots de sens proche.

## Semaine 2 : Embeddings et similarité cosinus

Audio : `embeddings.wav`

Un embedding représente une entrée par un vecteur de nombres. Pour visualiser l’idée, nous utilisons ici un dessin à deux dimensions. Les coordonnées sont inventées pour la démonstration.

Les vecteurs de « chat » et de « félin » pointent dans des directions proches. Celui de « moteur » a une direction différente.

La similarité cosinus compare ces directions. On calcule le produit scalaire, puis on le divise par le produit des normes. Pour des vecteurs non nuls, leur longueur ne change donc pas cette mesure.

Dans les modèles réels, les embeddings ont beaucoup plus de dimensions. Cette carte aide à comprendre le calcul, mais elle ne représente pas une mesure tirée d’un modèle.

## Semaine 3 : Comprendre les poids d’attention

Audio : `attention.wav`

L’attention permet à une position de combiner des informations provenant d’autres positions. Le modèle construit pour cela des requêtes, des clés et des valeurs, appelées Q, K et V.

Une requête est comparée aux clés. Les produits scalaires sont divisés par la racine de la dimension des clés. Dans notre exemple, les scores obtenus sont zéro, un et deux.

Le softmax transforme ces scores en poids : environ neuf pour cent, vingt-quatre et demi pour cent, et soixante-six et demi pour cent. Leur somme vaut un.

La sortie est une somme des valeurs V pondérées par ces poids. Dans un décodeur causal, les positions futures sont masquées avant le softmax.

## Semaine 3 : Visualiser le masque causal

Audio : `masque-causal.wav`

Voici une matrice d’attention. Chaque ligne correspond à une requête et chaque colonne à une clé. Les numéros indiquent les positions dans la séquence.

Les cases vertes montrent les connexions autorisées. À la deuxième position, le modèle peut consulter les positions un et deux, mais pas les suivantes.

Pour bloquer une position future, on ajoute moins l’infini à son score avant le softmax. Son poids devient alors nul.

Ce masque permet de traiter plusieurs positions en parallèle pendant l’entraînement sans leur donner accès aux tokens futurs. Le modèle apprend ainsi à prédire la suite à partir du seul contexte autorisé.

## Semaine 4 : BERT et le token masqué

Audio : `bert.wav`

BERT construit des représentations en utilisant le contexte situé à gauche et à droite. Dans cette phrase, un token a été remplacé par le marqueur « masque ».

Le mot « miaule » fournit un indice pour retrouver « chat ». Les probabilités affichées sont fictives : elles servent seulement à illustrer la prédiction.

Pendant le préentraînement, la perte compare les prédictions aux cibles sur les positions sélectionnées. Le modèle ajuste ses paramètres pour améliorer cette reconstruction.

Il faut distinguer deux mécanismes. Remplacer un token d’entrée par un masque cache son contenu. Un masque causal interdit, lui, certaines connexions d’attention. Ce ne sont pas les mêmes opérations.

## Semaine 5 : La génération autorégressive

Audio : `generation.wav`

Un modèle génératif produit sa réponse un token à la fois. Le contexte de départ est ici « Le chat ». Le modèle calcule plusieurs suites possibles et leur attribue des probabilités.

Nous utilisons un décodage glouton : il choisit le token le plus probable. Dans cet exemple fictif, le modèle sélectionne « dort ». Ce token est ajouté au contexte.

Le calcul recommence sur le nouveau contexte. Le modèle choisit ensuite « sur », puis « le ». À chaque étape, la distribution est recalculée.

La boucle continue jusqu’à une condition d’arrêt, comme une limite de longueur ou un token de fin. Avec l’échantillonnage, le token choisi peut être différent du plus probable.

## Semaine 5 : Température et probabilités

Audio : `temperature.wav`

La température modifie une distribution avant l’échantillonnage. Nous gardons ici les mêmes scores : deux, un et zéro. On les divise par la température, puis on applique le softmax.

À zéro virgule cinq, la probabilité se concentre sur le premier candidat. Il reçoit environ quatre-vingt-sept pour cent de la masse totale.

À un, nous retrouvons la distribution initiale. À deux, les probabilités deviennent plus proches les unes des autres : les candidats moins probables ont davantage de chances d’être tirés.

Pour une température positive, le classement reste le même. Le décodage glouton choisit donc toujours le même maximum. Modifier la température ne garantit pas l’exactitude des réponses.

## Semaine 6 : Du document aux passages pertinents

Audio : `recherche.wav`

Pour chercher dans un document long, on peut d’abord le découper en passages. Ici, les trois passages concernent l’inscription, les frais et les examens.

Chaque passage reçoit un embedding. La question « combien coûte le cours ? » est encodée dans un espace compatible avec ces représentations.

On compare ensuite les vecteurs. Dans cet exemple fictif, le passage sur les frais obtient le score le plus élevé. Une recherche top-k conserve les meilleurs candidats.

Le découpage et le modèle d’embeddings influencent ces résultats. Un score élevé indique une proximité selon la mesure choisie. Il ne prouve pas que le passage contient une réponse correcte : il faut encore lire et vérifier son contenu.

## Semaine 7 : BERTopic : des groupes aux sujets

Audio : `bertopic.wav`

BERTopic organise la découverte de sujets en plusieurs étapes. Les embeddings représentent d’abord les documents. UMAP réduit ensuite le nombre de dimensions utilisé pour le regroupement.

HDBSCAN cherche des groupes de points denses. Dans notre dessin, deux groupes apparaissent et un point reste à l’extérieur. Tous les documents ne sont donc pas forcés dans un groupe.

La méthode appelée c-TF-IDF met ensuite en évidence les mots caractéristiques de chaque groupe. Ici, les descriptions évoquent les cours et les frais.

Ces mots facilitent l’interprétation, mais ne suffisent pas à valider un sujet. Il faut consulter les documents représentatifs. Les différents modules du pipeline peuvent aussi être remplacés.

## Semaine 8 : Construire un prompt vérifiable

Audio : `prompt.wav`

Un prompt devient plus facile à utiliser quand il précise la tâche, les données et le format attendu. Dans cet exemple, nous demandons d’extraire une date de remise.

Nous fournissons ensuite le texte à analyser : « Le devoir est dû le douze novembre ». La donnée est clairement séparée de la consigne.

Enfin, nous demandons un objet JSON contenant la date, ou une valeur nulle si elle est absente. La réponse illustrée reprend ici le douze novembre.

L’application doit encore vérifier le format et la correspondance avec le texte source. Des délimiteurs améliorent la clarté, mais ils ne garantissent ni l’exactitude ni une protection complète contre les injections.

## Semaine 9 : Les étapes d’un système RAG

Audio : `rag.wav`

Le RAG associe une recherche documentaire à un modèle génératif. Avant les questions des utilisateurs, les documents sont découpés en passages, transformés en embeddings et placés dans un index.

Quand une question arrive, le système l’encode pour rechercher des passages pertinents. Ces passages sont récupérés dans la base documentaire.

Le modèle reçoit alors un prompt qui contient la question et les passages sélectionnés. Il peut s’appuyer sur ce contexte pour formuler une réponse. Les poids du modèle ne sont pas réentraînés pendant cette recherche.

Les sources permettent de vérifier la réponse. Le RAG ne supprime toutefois pas toutes les erreurs : la récupération et l’interprétation des documents peuvent échouer.

## Semaine 10 : CLIP et l’apprentissage contrastif

Audio : `clip.wav`

CLIP apprend à comparer des images et des textes. Un encodeur traite les images et un autre traite les descriptions. Leurs vecteurs sont comparés dans un espace partagé.

La matrice montre trois images et trois textes. Les associations correctes sont sur la diagonale : le chat avec le chat, le vélo avec le vélo et l’arbre avec l’arbre.

La perte contrastive favorise ces associations par rapport aux autres paires du lot. La comparaison est effectuée dans les deux directions, de l’image vers le texte et du texte vers l’image.

Les valeurs présentées sont fictives. CLIP mesure une compatibilité entre entrées ; il ne génère pas lui-même une légende.

## Semaine 10 : Du patch au token visuel

Audio : `vision.wav`

Un Vision Transformer traite une image comme une séquence de représentations. On commence par la découper en patches. Notre dessin utilise une petite grille de quatre lignes et quatre colonnes.

Chaque patch est aplati, puis projeté en un vecteur. Les vecteurs obtenus ont la même dimension et forment une séquence.

On leur ajoute des informations de position pour conserver la localisation des patches dans l’image.

Pour une image de deux cent vingt-quatre pixels de côté et des patches de seize pixels, on obtient quatorze fois quatorze, soit cent quatre-vingt-seize patches. Dans un ViT qui ajoute un token de classification, la séquence compte donc cent quatre-vingt-dix-sept tokens.

## Semaine 11 : LoRA et les matrices de faible rang

Audio : `lora.wav`

LoRA adapte une matrice en conservant ses poids de base et en apprenant une petite correction. Ici, la matrice de base a quatre mille quatre-vingt-seize lignes et autant de colonnes.

La correction utilise deux matrices, A et B, avec un rang de huit. Ensemble, elles contiennent soixante-cinq mille cinq cent trente-six paramètres entraînables.

La sortie additionne le résultat de la matrice de base et celui de cette branche de faible rang. Le facteur alpha divisé par le rang règle l’échelle de la correction.

Pour cet exemple, il y a deux cent cinquante-six fois moins de paramètres entraînables. Mais les poids de base restent en mémoire : ce rapport ne mesure pas l’économie totale de mémoire GPU.

## Semaine 11 : Quantification et erreur d’arrondi

Audio : `quantification.wav`

La quantification remplace des valeurs par des niveaux représentables avec moins de précision. Nous utilisons ici une grille simple dont le pas vaut zéro virgule cinq.

Pour obtenir le niveau quantifié, on divise le poids par le pas et on arrondit. Pour reconstruire une approximation, on multiplie ce niveau par le pas.

Ainsi, moins un virgule trois devient moins un virgule cinq. Zéro virgule deux devient zéro, et un virgule sept devient un virgule cinq.

Ce procédé peut économiser du stockage, mais il introduit une erreur. Les formats réels utilisent aussi des échelles, des groupes de valeurs et parfois des grilles non uniformes. Notre exemple illustre seulement le principe.

## Semaine 12 : Apprendre avec des paires de préférences

Audio : `dpo.wav`

DPO adapte un modèle à partir de préférences. Pour une même question, le jeu de données fournit une réponse préférée et une réponse rejetée.

La méthode compare leurs log-probabilités dans le modèle à entraîner et dans un modèle de référence gelé. La marge affichée mesure cette différence relative.

La perte encourage une marge plus grande pour la réponse préférée. Le paramètre bêta intervient dans cette fonction de perte. L’objectif porte sur une comparaison relative, pas sur une garantie que chaque probabilité évolue isolément dans le sens attendu.

La qualité des préférences reste essentielle. Satisfaire les comparaisons d’un jeu de données ne garantit pas qu’une réponse sera vraie, utile ou sûre dans toutes les situations.

## Semaine 13 : Le cache KV pendant le décodage

Audio : `cache-kv.wav`

Pendant la génération causale, le cache KV conserve les clés et les valeurs déjà calculées. Le préremplissage commence par traiter les tokens du prompt, à chaque couche du modèle.

Pour le token suivant, on calcule ses nouvelles projections. Ses clés et ses valeurs rejoignent le cache.

La nouvelle requête consulte alors les clés et les valeurs des positions passées et de la position courante. Il faut donc toujours calculer l’attention au passé.

Le gain vient de la réutilisation des projections précédentes. En échange, le cache occupe de la mémoire, et cette mémoire augmente avec la longueur du contexte. Il faut donc choisir un compromis entre vitesse et capacité de traitement.

## Semaine 14 : La boucle d’un agent avec outils

Audio : `agent.wav`

Un agent relie un modèle à des outils dans une boucle de contrôle. Prenons une question qui nécessite une recherche documentaire.

Le système décide d’appeler un outil. L’application vérifie que cet outil et ses paramètres sont autorisés, puis exécute la recherche.

Le résultat revient comme une donnée à examiner. Le système vérifie si les informations obtenues suffisent pour répondre et citer les sources. Sinon, une nouvelle recherche peut être proposée.

Cette boucle doit avoir des limites. Elle s’arrête quand l’objectif est atteint, quand le nombre maximal d’étapes est dépassé, en cas d’erreur ou lorsqu’une intervention humaine est nécessaire. Le résultat d’un outil n’est pas automatiquement une consigne à suivre.

## Semaine 15 : minGPT : de la prédiction à la mise à jour

Audio : `entrainement.wav`

Pour entraîner minGPT, les cibles sont décalées d’un token par rapport aux entrées. Avec « Le », « chat » et « dort » en entrée, les cibles sont « chat », « dort » et le point.

Le passage avant calcule des scores sur le vocabulaire. La perte d’entropie croisée compare ces scores aux cibles attendues.

La rétropropagation calcule ensuite les gradients. L’optimiseur utilise ces informations pour mettre à jour les paramètres.

Entre deux pas, on réinitialise les gradients, sauf si l’on veut volontairement les accumuler. Enfin, on mesure les résultats sur des données de validation séparées. Une baisse de la perte d’entraînement ne suffit pas à démontrer une meilleure généralisation.

