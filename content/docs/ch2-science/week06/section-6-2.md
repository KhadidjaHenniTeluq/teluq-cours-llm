---
title: "6.2 Mesures de similarité"
weight: 3
---

{{< katex />}}

## Mesures de similarité

Une mesure de similarité transforme la comparaison de deux vecteurs en un score. Le cosinus compare leurs directions, la distance euclidienne mesure leur écart et le produit scalaire dépend aussi de leur norme. Le choix de la mesure doit correspondre à la façon dont les embeddings ont été entraînés et normalisés.

<a id="cos-sin"></a>

## La Similarité Cosinus : Le standard de l'industrie

La mesure reine en NLP est la **Similarité Cosinus**. Pourquoi ne pas simplement utiliser une règle pour mesurer la distance entre deux points ? Parce que dans le langage, la "longueur" d'un vecteur (sa magnitude) peut être trompeuse.

Regardez attentivement la **Figure 6-5 : Similarité cosinus**. 

{{< bookfig src="101.png" week="06" >}}

Cette illustration est capitale. Imaginez deux flèches partant de l'origine (le point 0,0): 
*   La flèche A représente un document court : "J'aime les chats."
*   La flèche B représente un document long sur le même sujet : "Le bonheur de posséder un petit félin domestique est immense..."

Leurs vecteurs n'auront pas la même longueur, mais ils pointent exactement dans la même direction sémantique. La similarité cosinus ne mesure pas la distance entre les pointes des flèches, mais l'**angle** $\theta$ entre elles. 

> [!TIP]
**L'intuition mathématique :** 
> *   Si l'angle est de 0°, les deux phrases pointent dans la même direction : Similarité = 1 (même direction des vecteurs).
> *   Si l'angle est de 90°, leurs vecteurs sont orthogonaux : Similarité = 0.
> *   Si l'angle est de 180°, leurs vecteurs ont des directions opposées : Similarité = -1.

> [!WARNING]
**Attention :** Dans la plupart des bibliothèques de LLM, les scores de similarité oscillent entre 0 et 1 car les vecteurs sont normalisés. Un score de 0.9 est excellent, un score de 0.1 indique une absence totale de lien.


## Comparaison : Euclidienne vs. Cosinus
Pourquoi ne pas utiliser la distance Euclidienne (L2), celle que vous avez apprise à l'école ? 

1.  **Distance Euclidienne** : C'est la ligne droite entre deux points. 
    *   *Problème* : Si vous comparez un paragraphe de 10 lignes et un livre de 500 pages sur le même sujet, la distance Euclidienne sera énorme simplement parce que le second vecteur est "plus loin" de l'origine à cause de sa masse de mots.
2.  **Similarité Cosinus** : Elle normalise la longueur. 
    *   *Avantage* : Elle se concentre uniquement sur l'**orientation**. C'est pour cela qu'elle est le choix par défaut pour la recherche sémantique. 

> [!NOTE]
**Note technique :** Si vous "normalisez" vos vecteurs (c'est-à-dire que vous ramenez leur longueur à 1), alors la distance Euclidienne et la similarité cosinus deviennent mathématiquement équivalentes. C'est ce que font beaucoup de bases de données vectorielles pour gagner en vitesse.


## Le Produit Scalaire (Dot Product)
Le **Dot Product** est le calcul brut derrière la similarité. C'est une simple multiplication membre à membre des composants de deux vecteurs, suivie d'une somme.
*   Si vos vecteurs ne sont pas normalisés, le Dot Product peut donner des nombres énormes.
*   C'est la mesure préférée des GPU car elle est extrêmement rapide à calculer sous forme de matrices. 


## Adaptation des représentations à la recherche documentaire
Parfois, les modèles pré-entraînés ne suffisent pas. Un modèle généraliste peut penser que "pomme" est proche de "banane" (ce sont des fruits), mais si vous construisez un moteur de recherche pour une entreprise de technologie, vous voulez peut-être que "pomme" soit proche de "iPhone".

C'est ici qu'intervient le **fine-tuning pour le retrieval**, illustré par les **Figures 6-6 et 6-7**. 
*   **Figure 6-6** : Montre l'état initial. Les requêtes (queries) et les documents sont éparpillés. Le modèle ne sait pas encore quel document répond spécifiquement à quelle question.

<a id="fig-6-6"></a>
{{< bookfig src="183.png" week="06" >}}

*   **Figure 6-7** : Après l'entraînement sur des paires "Question/Réponse", le modèle a appris à "tirer" les bonnes réponses vers la question et à "pousser" les mauvaises au loin. 

<a id="fig-6-7"></a>
{{< bookfig src="184.png" week="06" >}}

> [!IMPORTANT]
**À retenir :** pour réussir ce réglage, vous avez besoin de "*Contrastive Pairs*" : une question, une réponse correcte (exemple positif) et une réponse erronée (exemple négatif). C'est ainsi que l'on transforme un modèle de langage en un expert en recherche. 


## Implémentation pratique : Similarité avec Scikit-learn
Voici comment calculer ces scores de proximité sur Google Colab.

```python
# Exemple prévu pour Colab T4
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. On charge notre modèle de référence
model = SentenceTransformer("all-mpnet-base-v2")

# 2. On définit une requête et des documents
query = "How to improve my health?"
docs = [
    "You should exercise daily and eat vegetables.", # Très pertinent
    "The stock market is fluctuating due to global news.", # Hors sujet
    "Maintaining a balanced diet is key to well-being." # Pertinent
]

# 3. Encodage en vecteurs
query_vec = model.encode([query])
docs_vec = model.encode(docs)

# 4. Calcul de la similarité cosinus
similarities = cosine_similarity(query_vec, docs_vec)

print(f"Requête : {query}\n")
for i, score in enumerate(similarities[0]):
    print(f"Document {i+1} : Score = {score:.4f} -> {docs[i]}")

# ATTENDU : Scores élevés (> 0.7) pour les docs 1 et 3, faible (< 0.2) pour le doc 2.
```
> [!NOTE]
Regardez les scores. Même le document 2 aura un score légèrement supérieur à 0 (peut-être 0.15). 

> [!IMPORTANT]
**C'est non-négociable :** en recherche vectorielle, tout est relié à tout à un certain degré. Votre rôle d'ingénieur est de fixer un **seuil (threshold)** en dessous duquel vous considérez que le résultat est du bruit.


## Éthique et Biais dans la similarité

> [!CAUTION]
la mathématique de la similarité peut être injuste. 

Les mesures de similarité ne sont que le reflet des corrélations apprises. 
1.  **Biais de neutralité** : Si vous cherchez "personne compétente", et que le modèle renvoie systématiquement des profils ayant un certain type de vocabulaire culturel, vous excluez des talents sans le savoir.
2.  **Fausse certitude** : Un score de 0.98 n'est pas une preuve de vérité, c'est une preuve de ressemblance statistique. 

> [!TIP]
**Conseil méthodologique** : Ne basez jamais une décision automatique grave (recrutement, justice, crédit) uniquement sur un score de similarité vectorielle sans un audit humain rigoureux.

---
La section suivante présente **l'indexation vectorielle**, qui utilise ces mesures de similarité pour rechercher des documents dans une collection.
