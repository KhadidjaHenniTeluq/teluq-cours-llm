---
title: "3.2 Encodage positionnel"
weight: 3
---

{{< katex />}}

## Encodage positionnel

Le mécanisme d’attention a besoin d’informations sur l’ordre des tokens pour distinguer des phrases contenant les mêmes mots dans un ordre différent. Les représentations de position apportent cette information. Nous comparons une construction sinusoïdale à RoPE, une méthode qui agit sur les requêtes et les clés.

## L'intuition : Les coordonnées GPS du langage
Imaginez que vous receviez les pièces d'un puzzle, mais que toutes les pièces soient parfaitement carrées et lisses. Vous savez ce qu'il y a sur chaque pièce (l'embedding sémantique), mais vous n'avez aucune idée de l'endroit où elles s'emboîtent. 

**L'encodage positionnel**, c'est l'étiquette que l'on colle au dos de chaque pièce pour dire : "Je suis la pièce n°1, tout en haut à gauche". 

Dans les RNN (Section 1.2), l'ordre était implicite : le mot 2 arrivait forcément après le mot 1. Dans le Transformer, nous devons injecter cette information artificiellement. 

> [!WARNING]
**Attention :** On ne donne pas simplement un numéro (1, 2, 3...) au modèle. Pourquoi ? Parce que si la phrase est très longue, le nombre "1000" écraserait par sa valeur mathématique les autres informations du vecteur. Nous avons besoin d'une méthode plus subtile.


---
## La méthode classique : Les ondes sinusoïdales
Dans l'article original de 2017, les chercheurs ont utilisé des fonctions sinus et cosinus. 
*   **L'idée** : Chaque position est représentée par des sinus et cosinus ; les fréquences diffèrent selon les dimensions du vecteur. 
*   **Le bénéfice** : Cela permet au modèle de comprendre la distance relative. Si le modèle sait comment oscille l'onde entre la position 2 et la position 5, il peut généraliser cette "distance de 3" à n'importe quel endroit du texte.

L'encodage absolu ajoute une information de position aux représentations initiales. L'**encodage rotatif** adopte une autre approche, présentée ci-dessous.


---
## RoPE (Rotary Positional Embeddings)
Si vous regardez les spécifications de modèles comme **Llama-3**, **Mistral** ou **Phi-3**, vous verrez toujours mentionné "**RoPE**". Ces familles de modèles utilisent un encodage rotatif. 

Regardons attentivement la **Figure 3-7 : Application des Rotary Embeddings** .

{{< bookfig src="85.png" week="03" >}}

** Explication** : Cette illustration est fondamentale pour comprendre la différence de philosophie. 
*   **Ancien monde** : On ajoutait la position une seule fois, tout au début, sur les embeddings d'entrée (les boîtes bleues en haut).
*   **Monde RoPE** : Comme le montre la figure, l'encodage positionnel est injecté **à chaque couche**, directement à l'intérieur des blocs d'attention (les ronds violets). 

> [!NOTE]
**À retenir :** RoPE n'est pas une addition, c'est une **multiplication**. On ne "colle" pas une étiquette, on fait "pivoter" le vecteur.


### La mathématique de la rotation
Passons à la géométrie avec la **Figure 3-8 : La rotation des vecteurs** . 

{{< bookfig src="86.png" week="03" >}}

** Explication** : Imaginez que chaque paire de dimensions dans votre vecteur (votre Query ou votre Key) soit une aiguille sur une horloge. 
*   Pour le mot n°1, on tourne l'aiguille de 10 degrés.
*   Pour le mot n°2, on la tourne de 20 degrés.
*   **Le produit scalaire après rotation** dépend du contenu des requêtes et des clés ainsi que de leur **position relative**. 
*   La proximité ne garantit pas un score élevé : le contenu des vecteurs intervient aussi. Voir [RoFormer](https://arxiv.org/abs/2104.09864).


> [!TIP]
**Interprétation:** RoPE permet au modèle de "sentir" la distance entre les mots sans avoir besoin de connaître leur position absolue. 

> C'est comme si, dans une file d'attente, vous ne saviez pas que vous étiez le 50ème, mais que vous sentiez exactement que la personne devant vous est à 50 cm et celle de derrière à 50 cm. C'est l'**Attention Relative**.


---
## Pourquoi RoPE a-t-il gagné ?
1.  **Extrapolabilité** : RoPE exprime une dépendance à la position relative. L’utilisation de séquences plus longues que celles de l’entraînement exige toutefois une validation et souvent une adaptation.
2.  **Stabilité** : Les rotations préservent la norme (la "longueur") des vecteurs, sans garantir à elles seules la stabilité de l’entraînement.
3.  **Richesse sémantique** : En faisant varier la vitesse de rotation selon les dimensions, le modèle peut dévouer certaines parties de son cerveau aux relations à court terme (mots voisins) et d'autres aux relations à long terme (début et fin de paragraphe).


---
## Optimisation de l'entraînement : Le Packing
*l'informatique n'est pas qu'une affaire de mathématiques, c'est aussi une affaire d'économie.* 

Entraîner un LLM coûte des millions d'euros en électricité. Chaque seconde où votre GPU ne calcule rien est un gaspillage. 

Regardons la **Figure 3-9 : Packing des documents** .

{{< bookfig src="84.png" week="03" >}}

** Explication** : Elle compare deux méthodes d'organisation des données.
*   **Approche naïve (Haut)** : Si vous avez une phrase de 10 mots et une fenêtre de contexte de 2048, vous remplissez le reste avec du "Padding" (des zéros). Le GPU passe son temps à multiplier des zéros. C'est un désastre d'efficacité.
*   **Approche par Packing (Bas)** : On "compacte" plusieurs documents différents à la suite dans le même bloc de 2048 tokens, séparés par un token spécial. 

> [!NOTE]
**Le défi technique** : Le pipeline doit choisir explicitement comment séparer les documents, gérer leurs positions et masquer éventuellement l’attention entre documents. L’encodage positionnel ne déduit pas ces frontières à lui seul.

---
## Limites et Frontières : La fenêtre de contexte
> [!WARNING]
Ne croyez pas que la mémoire de l'IA soit infinie. 

Même avec RoPE, chaque modèle possède une "Context Window" (Fenêtre de contexte) maximale.
*   **La limite physique** : La fenêtre utilisable dépend de la configuration du modèle, de son entraînement et de la mémoire disponible. Dépasser les longueurs validées peut dégrader ses réponses.
*   **Le coût quadratique** : Rappelez-vous la section 3.1. Même si l'encodage positionnel est parfait, le calcul de l'attention demande toujours $N \times N$ opérations. Doubler la longueur multiplie par quatre la taille de la matrice d’attention explicite ; la mémoire totale dépend aussi de l’implémentation, notamment de FlashAttention.

---
## Laboratoire de réflexion : Le temps est-il une dimension ?

> [!CAUTION]
réfléchissez à l'impact de ce découpage.

Pour un Transformer, le temps n'existe pas. Il n'y a que des positions dans une grille. 
1.  **L'absence de causalité réelle** : Le modèle ne comprend pas que la cause précède l'effet parce que c'est une loi physique ; il le comprend parce que statistiquement, le token "Cause" a une position inférieure au token "Effet" dans ses données d'entraînement. 
2. **Le biais de position** : Certains modèles exploitent moins bien une information placée au milieu d’un long contexte. Ce comportement dépend du modèle, de son entraînement et de la tâche ; il ne s’explique pas uniquement par l’encodage positionnel.


> [!TIP]
**Conseil méthodologique** : Lorsque vous construisez un système de RAG (Semaine 9), assurez-vous que l'information cruciale ne se trouve pas perdue au milieu d'un énorme bloc de texte, car l'encodage positionnel sémantique y est souvent moins "vif".


---
## Synthèse
Cette section a présenté la manière dont le Transformer prend en compte la position des tokens.
*   **L'encodage absolu** (sinus) a posé les bases.
*   **L'encodage rotatif (RoPE)** a apporté la flexibilité et la notion de distance relative, permettant l'explosion des fenêtres de contexte que nous connaissons aujourd'hui.
* **Le packing** réduit le calcul consacré au padding. Le gain dépend des longueurs de séquences et de l’implémentation ; il ne garantit pas une utilisation maximale du GPU.

> [!TIP]
**Synthèse** : L'encodage positionnel permet au modèle de prendre en compte l'ordre et la position des tokens.

> En apprenant à faire pivoter des vecteurs dans l'espace complexe, les chercheurs ont réussi l'impossible : garder la puissance du calcul parallèle tout en respectant la mélodie séquentielle du langage humain. C'est un triomphe de l'ingénierie mathématique.

---
La section suivante présente les **blocs Transformer** et les choix d’architecture qui influencent leur stabilité et leur coût de calcul.
