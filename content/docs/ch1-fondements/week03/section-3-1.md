---
title: "3.1 Le mécanisme d'attention : Mathématiques détaillées"
weight: 2
---

{{< katex />}}

## Le mécanisme d'attention : Mathématiques détaillées

L’attention transforme une séquence de vecteurs en combinant les informations disponibles à chaque position. Les requêtes Q et les clés K servent à calculer des poids ; ces poids pondèrent les valeurs V. Dans un décodeur causal, les positions futures sont masquées. Nous détaillons le calcul sur de petits exemples avant de généraliser aux matrices.

{{< bookfig src="68.png" week="03" >}}

## Animation : Visualiser le masque causal

{{< conceptvideo name="masque-causal" title="Visualiser le masque causal" >}}
Dans la matrice d’attention, les lignes représentent les requêtes et les colonnes les clés. La ligne 2 peut utiliser les colonnes 1 et 2, mais pas les suivantes. Les scores des positions futures reçoivent −∞ avant softmax, ce qui annule leurs poids. Pendant l’entraînement, plusieurs positions sont traitées en parallèle, mais le masque empêche chacune de consulter les tokens futurs servant de cibles.
{{< /conceptvideo >}}

## Animation : Comprendre les poids d’attention

{{< conceptvideo name="attention" title="Comprendre les poids d’attention" >}}
Les projections Q, K et V sont apprises. Une requête est comparée à trois clés par les scores Q · K / √d. Dans l’exemple, les scores 0, 1 et 2 donnent, après softmax, des poids d’environ 0,090, 0,245 et 0,665. Leur somme vaut 1. La sortie est la somme des vecteurs V pondérés par ces poids. Pour un décodeur causal, les positions futures sont masquées avant softmax.
{{< /conceptvideo >}}

## Les projections : Query, Key et Value

> [!TIP]
Les projections Query, Key et Value constituent les trois éléments du calcul de l’attention présenté dans cette section.

Le Transformer ne compare pas les vecteurs de mots directement. Il projette chaque mot dans trois espaces fonctionnels différents.

Comme l'illustre la **Figure 3-2 : Matrices de projection**, le modèle possède trois matrices de poids apprises durant l'entraînement : $W_Q, W_K$ et $W_V$. Lorsqu'un mot entre dans la couche d'attention :

{{< bookfig src="71.png" week="03" >}}

1.  **Query (La Requête - Q)** : C'est ce que le mot cherche. Si le mot est "il", sa requête demande : "Où est mon sujet masculin dans cette phrase ?".
2.  **Key (La Clé - K)** : C'est l'étiquette du mot. Un mot comme "livre" possède une clé qui dit : "Je suis un objet inanimé masculin".
3.  **Value (La Valeur - V)** : C'est l'information sémantique pure que le mot contient.

> [!TIP]
**Analogie** : Imaginez que vous cherchiez un tutoriel de cuisine sur YouTube. 

> Votre barre de recherche est la **Query**. Le titre de la vidéo sur le serveur est la **Key**. Le contenu de la vidéo (ce que vous allez apprendre) est la **Value**. L'attention est l'algorithme qui fait correspondre votre recherche au titre le plus proche.

---
## Le calcul matriciel étape par étape
Nous décomposons cette chorégraphie mathématique avec une précision à évaluer.

### Étape 1 : Le calcul des scores de pertinence (Figure 3-3)

{{< bookfig src="72.png" week="03" >}}

** Explication** : Pour chaque mot, on multiplie sa **Query** par les **Keys** de tous les autres mots. Mathématiquement, c'est un produit scalaire (Dot Product). 
*   Si les vecteurs Q et K pointent dans la même direction, le score est élevé.
*   Si ils sont orthogonaux, le score est nul.
Cette opération crée une grille de scores indiquant à quel point chaque mot est "intéressé" par les autres.

### Étape 2 : Le "Scaling" et le Softmax (Figure 3-4)

> [!WARNING]
**Attention** : Des scores de grande amplitude peuvent saturer le softmax et réduire la sensibilité de ses gradients. La mise à l’échelle des scores contribue à limiter cet effet.

> [!TIP]
**La solution mathématique** : On divise les scores par la racine carrée de la dimension des clés ($\sqrt{d_k}$). C'est le **Scaled Dot-Product Attention**. 


{{< bookfig src="73.png" week="03" >}}

Ensuite, comme le montre la **Figure 3-4**, on applique une fonction **Softmax**. 
*   **L'effet visuel** : Les scores sont transformés en probabilités entre 0 et 1. La somme totale pour chaque mot est égale à 100 %. On voit alors apparaître une "carte d'attention" où certains liens s'allument (forte probabilité) et d'autres s'éteignent.


### Étape 3 : La pondération des valeurs (Figure 3-5)

{{< bookfig src="74.png" week="03" >}}

** Explication** : Enfin, on multiplie ces probabilités par les **Values**. 
*   Si le mot "il" a 90 % d'attention sur "livre", alors 90 % du vecteur final de "il" sera composé de l'information sémantique de "livre". 
*   Le résultat est un nouveau vecteur, le **Contextual Embedding**, qui a "aspiré" le sens de son environnement.


---
## Multi-Head Attention : Les cerveaux parallèles
*Pourquoi se contenter d'un seul regard sur une phrase ?* 

Un mot peut avoir plusieurs rôles : il a un rôle grammatical, un rôle sémantique et un rôle émotionnel. 

C'est ce qu'illustre la **Figure 3-6 : Intuition des têtes d'attention**. 

{{< bookfig src="70.png" week="03" >}}

Au lieu d'avoir un seul trio Q, K, V, nous en créons plusieurs en parallèle (généralement **8**, **12** ou même **96** têtes). 
*   Une tête peut se spécialiser dans la détection des verbes.
*   Une autre dans la résolution des pronoms (coréférence).
*   Une autre dans l'analyse du ton (ironie).

> [!IMPORTANT]
**À retenir :** La Multi-Head Attention est ce qui donne au Transformer sa nuance. 

À la fin, on fusionne (concatène) les résultats de toutes les têtes pour obtenir une vision riche et multidimensionnelle de la phrase.

---
## Exemple numérique : Le bac à sable des matrices
Pour bien fixer l'idée, imaginons une séquence de deux tokens : "Chat" et "Dort".
Supposons que nos vecteurs de Query et Key soient simplifiés à 2 dimensions.

1.  **Matrices Q et K** :
    *   $Q_{chat} = [1, 0]$, $K_{chat} = [1, 0]$
    *   $Q_{dort} = [0, 1]$, $K_{dort} = [0, 1]$
2.  **Calcul du score** (Produit scalaire $Q \cdot K^T$) :
    *   Score "Chat" vers "Chat" : $1\times1 + 0\times0 = 1$
    *   Score "Chat" vers "Dort" : $1\times0 + 0\times1 = 0$
3.  **Softmax** :
    *   Sans mise à l’échelle, softmax([1, 0]) donne environ [0,731, 0,269], et non [1, 0].
    *   Avec la mise à l’échelle par la racine de 2, les scores [0,707, 0] donnent environ [0,670, 0,330]. Les deux valeurs contribuent donc à la sortie, sauf si un masque interdit une position.

> [!NOTE]
**Note** : La dimension du modèle et celle des requêtes et clés par tête sont différentes. Par exemple, un modèle de dimension 768 avec 12 têtes peut utiliser des clés de dimension 64 par tête.

> La complexité est telle que seule la puissance des GPU (section 1.2) permet de résoudre ces milliards de multiplications par seconde.

---
## L'attention comme moteur de la parallélisation
*Pourquoi avons-nous abandonné les RNN ?* 

Parce que dans le calcul $Q \cdot K^T$, nous pouvons calculer TOUS les scores de TOUS les mots en une seule opération matricielle géante.

> [!NOTE]
**Calcul parallèle** : Les produits matriciels traitent plusieurs positions simultanément à l’entraînement. Le gain de temps dépend de la taille du modèle, du matériel et de l’implémentation ; la génération autorégressive reste séquentielle.

---
## Éthique et Transparence : Le biais de l'attention

> [!CAUTION]
l'attention n'est pas neutre.

Les matrices $W_Q, W_K, W_V$ sont apprises sur des données humaines. 
1.  **Le renforcement des stéréotypes** : Si, dans les données d'entraînement, le mot "Infirmière" porte systématiquement son attention sur des pronoms féminins, le modèle va figer cette association. L'attention devient alors un mécanisme de reproduction des préjugés. 
2.  **L'opacité du raisonnement** : Visualiser l'attention (Exercice 1 du laboratoire) nous donne une illusion de compréhension. Mais attention : une tête d'attention qui regarde une virgule peut le faire pour des raisons de syntaxe pure, et non pour le sens. 

**Ne prêtez pas d'intentions humaines à une multiplication matricielle!**

---
## Synthèse
Pour maîtriser cette section, vous devez être capables de réciter la formule de l'attention de *Vaswani et al. (Attention is all you need!)* :

$$Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
*   $QK^T$ : Qui regarde qui ? (Scores)
*   $\sqrt{d_k}$ : On calme les nombres (Scaling).
*   $softmax$ : On transforme en pourcentages (Normalisation).
*   $V$ : On extrait le sens (Information).

> [!TIP]
**Synthèse** : L'attention combine les représentations des tokens en fonction de leurs relations dans le contexte.

> Sans elle, les mots sont des îles. Avec elle, ils forment un continent de pensée. C'est la brique la plus puissante jamais inventée en informatique linguistique.

---
