---
title: "4.3 Applications pratiques"
weight: 4
---

{{< katex />}}

## Applications pratiques

La classification associe une étiquette à un texte. Nous construisons ici un classifieur à partir d’embeddings, puis nous évaluons ses erreurs. Une matrice de confusion, la précision, le rappel et le score F1 montrent des aspects complémentaires de la performance.

## Mise en œuvre : La recette du classifieur par embeddings
Comme nous l'avons vu en [**section 4.2**]({{< relref "section-4-2.md" >}}), nous allons utiliser la stratégie de l'extraction de caractéristiques. Nous n'allons pas modifier les "connaissances" de notre modèle de langage, mais nous allons lui demander de nous extraire la substantifique moelle de chaque critique de film sous forme de vecteurs.

Le processus se déroule en trois étapes :
1.  **L'encodage** : Nous passons chaque texte dans un modèle de type `sentence-transformers` (qui est une version optimisée de BERT pour les phrases). Chaque critique devient un point dans un espace à 768 dimensions.
2.  **L'entraînement** : Nous utilisons ces 768 nombres comme caractéristiques (features) pour un classifieur simple. Ici, nous choisissons la **Régression Logistique**. Pourquoi ? Parce qu'elle est extrêmement rapide, stable et très efficace sur de petits volumes de données.
3.  **L'inférence** : Nous testons notre classifieur sur des données qu'il n'a jamais vues pour vérifier s'il a vraiment "compris" la notion de sentiment ou s'il a simplement mémorisé les exemples.

## Laboratoire de code : Classification de sentiments (Colab T4)
Voici l'implémentation complète. Remarquez la vitesse d'exécution : une fois les embeddings extraits, l'entraînement du classifieur prend moins d'une seconde !

```python
# Installation des dépendances
# !pip install sentence-transformers datasets scikit-learn

from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# 1. Chargement du dataset
dataset = load_dataset("rotten_tomatoes")

# 2. Chargement du modèle de représentation (Frozen BERT-like)
model = SentenceTransformer("all-mpnet-base-v2", device="cuda")

# 3. Extraction des embeddings (On transforme le texte en nombres)
print("Extraction des caractéristiques en cours...")
X_train = model.encode(dataset["train"]["text"], show_progress_bar=True)
X_test = model.encode(dataset["test"]["text"], show_progress_bar=True)
y_train = dataset["train"]["label"]
y_test = dataset["test"]["label"]

# 4. Entraînement du classifieur léger (Scikit-Learn)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# 5. Évaluation (Inférence)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["Négatif", "Positif"]))

```

## Le juge de paix : La Matrice de Confusion
Une fois que le code a tourné, vous obtenez des chiffres. Mais comment les lire ? Regardez la **Figure 4-7 : Matrice de confusion**. C'est votre tableau de bord absolu.

{{< bookfig src="94.png" week="04" >}}


Elle croise la réalité (*Actual values*) et la prédiction du modèle (*Predicted values*). Elle définit quatre destins pour une donnée :
1.  **Vrais Positifs (TP)** : Le film est génial, et BERT l'a trouvé génial. Bravo !
2.  **Vrais Négatifs (TN)** : Le film est un navet, et BERT a confirmé que c'était un navet.
3.  **Faux Positifs (FP)** : C'est l'erreur "optimiste". Le film est mauvais, mais le modèle l'a classé comme bon.
4.  **Faux Négatifs (FN)** : C'est l'erreur "pessimiste". Le film est un chef-d'œuvre, mais le modèle l'a détesté.

**À retenir :** Ne regardez jamais uniquement le score global (l'Accuracy). Si vous travaillez sur la détection de fraude et que 99% des transactions sont honnêtes, un modèle qui dit "Toujours Honnête" aura 99% d'accuracy mais sera totalement inutile pour attraper le 1% de voleurs. C'est là qu'interviennent nos **trois piliers** .

## Précision, Rappel et Score F1 : Trois mesures complémentaires
Comme l'illustre la **Figure 4-8 : Rapport de classification**, nous devons jongler avec trois mesures.

{{< bookfig src="95.png" week="04" >}}


### 1. La Précision (Precision)
C'est la question de la **fiabilité**. "Quand mon modèle dit que c'est positif, quelle est la probabilité qu'il ait raison ?"
*   *Analogie* : C'est comme un témoin au tribunal. On veut qu'il ne dise que la vérité. S'il accuse quelqu'un à tort (Faux Positif), sa précision chute.

### 2. Le Rappel (Recall)
C'est la question de la **complétude**. "Sur tous les films positifs qui existent dans mon test, combien mon modèle a-t-il réussi à en attraper ?"
*   *Analogie* : C'est comme un filet de pêche. On veut qu'il attrape tous les poissons. Si des poissons s'échappent (Faux Négatifs), le rappel chute.

### 3. Le Score F1
> [!WARNING]
**Attention :** On ne fait pas une simple moyenne arithmétique entre Précision et Rappel. On utilise une **moyenne harmonique**. Pourquoi ? Parce que la moyenne harmonique punit sévèrement les déséquilibres. Si votre précision est de 1.0 (parfaite) mais votre rappel de 0.0 (vous n'avez rien trouvé), votre score F1 sera de 0, et non de 0.5. C'est l'indicateur de la robustesse globale de votre application.

## Au-delà du sentiment : La Reconnaissance d'Entités Nommées (NER)
La classification de texte n'est que la partie émergée de l'iceberg. Une autre application majeure des modèles *Encoder-only* est le **NER** (*Named Entity Recognition*).
Ici, nous ne classons pas toute la phrase, mais chaque mot individuellement. 
* **Exemple**: "Elon Musk habite au Texas."

    -> BERT va classer "Elon Musk" comme `PERSONNE` et "Texas" comme `LIEU`.

> [!NOTE]
**La distinction technique :** Pour le sentiment, nous utilisions le vecteur du token `[CLS]`. Pour le *NER*, nous utilisons les vecteurs de *chaque* mot à la sortie du Transformer pour décider de leur étiquette. C'est la différence entre une vision globale et une vision granulaire.

## Éthique et Responsabilité : Le danger du "Label Noise"

> [!WARNING]
soyez critiques envers vos données! 

>Dans notre application pratique, nous supposons que les labels "positif" et "négatif" sont la vérité absolue. Mais l'humain est complexe ! Une critique peut être sarcastique : "Quel chef-d'œuvre d'ennui !". Un labelleur humain fatigué pourrait classer cela en positif à cause du mot "chef-d'œuvre". 

> [!CAUTION]
**Conséquence éthique :** Si vos données de départ sont mal étiquetées (le *Label Noise*), votre modèle va apprendre à reproduire ces erreurs. Avant de lancer un modèle BERT en production, passez du temps à regarder les cas où votre modèle se trompe. Souvent, vous découvrirez que c'est l'étiquette humaine qui était erronée ou ambiguë. L'IA n'est que le reflet de notre propre clarté.

---
