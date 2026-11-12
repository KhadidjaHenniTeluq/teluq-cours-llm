---
title: "6.1 Embeddings de phrases "
weight: 2
---

## Embeddings de phrases

La recherche sémantique compare souvent des phrases ou des passages entiers. Il faut donc produire un vecteur pour chaque unité de texte. Les méthodes de pooling et les modèles entraînés pour la similarité de phrases répondent à ce besoin, avec des performances qui dépendent du domaine et de la langue.

{{< bookfig src="46.png" week="06" >}}

## La naissance de Sentence-BERT (SBERT)
Un *Cross-Encoder* traite conjointement chaque paire de phrases. Comparer un grand nombre de paires exige donc de nombreux passages dans le modèle, ce qui augmente le coût de calcul.

**SBERT** (Reimers et Gurevych, 2019) propose une approche adaptée à la comparaison de représentations de phrases.
> [!IMPORTANT]
**À retenir :**SBERT utilise une architecture dite "Siamese" (Siamoise).

> On utilise deux réseaux BERT identiques qui partagent les mêmes poids. Chaque phrase passe par un réseau, et on optimise le modèle pour que les phrases ayant un sens proche finissent avec des vecteurs proches. 

C'est ce que montre la **Figure 6-2 : Recherche sémantique dense**. Dans cette illustration, vous pouvez voir que dans l'espace mathématique du modèle, la phrase "Le ciel est bleu" (text 1) se retrouve physiquement proche de "Il fait beau aujourd'hui" (text 2), alors qu'elle est très éloignée de "Le moteur de ma voiture est cassé" (text 3). 

{{< bookfig src="175.png" week="06" >}}

> [!NOTE]
**À retenir :** La recherche sémantique transforme le langage en une carte géographique où la proximité physique égale la proximité de sens.


## L'art du Pooling : Comment résumer une séquence ?
Un Transformer produit un vecteur pour *chaque* token de la phrase. Si votre phrase fait 10 tokens, vous avez 10 vecteurs. Comment n'en obtenir qu'un seul pour représenter la phrase entière ? C'est ce qu'on appelle le **Pooling**.

Il existe trois stratégies principales :
1.  **CLS Pooling** : On utilise uniquement le vecteur du premier token spécial `[CLS]`. C'est la méthode historique de BERT.
2.  **Mean Pooling (Moyenne)** : On calcule la moyenne mathématique de tous les vecteurs de la phrase. 
> [!TIP]
**C'est la méthode recommandée par SBERT :** Elle capture mieux l'essence globale de la séquence que le simple token `[CLS]`.
3.  **Max Pooling** : On prend la valeur maximale de chaque dimension à travers tous les tokens.

> [!WARNING]
**Attention :** N'essayez pas de faire du pooling manuellement si vous utilisez la bibliothèque `sentence-transformers`. Elle gère cela automatiquement selon le modèle choisi.


## Choisir son modèle : Modèles de fondation vs Modèles spécialisés

> [!IMPORTANT]
Ne prenez pas le premier modèle venu sur Hugging Face !

Pour la recherche sémantique, la taille ne fait pas tout: 

*   **all-mpnet-base-v2** : C'est le "couteau suisse (swiss army knife)". Avec ses 768 dimensions, il offre le meilleur équilibre entre précision et vitesse pour l'anglais.
*   **paraphrase-multilingual-MiniLM-L12-v2** : Indispensable si vous travaillez en français ou dans plusieurs langues simultanément. Il est très léger et rapide.
*   **gte-small / bge-micro** : Des modèles très récents (2023-2024) qui battent des records sur les benchmarks tout en étant minuscules.

> [!TIP]
**Repère d’évaluation : MTEB**. Le *Massive Text Embedding Benchmark* permet de comparer des modèles sur plusieurs tâches. Les résultats de recherche documentaire (*Retrieval*) doivent être complétés par une évaluation sur les données de l’application.


## Projection spatiale et intuition de recherche

Regardez la **Figure 6-3 : Projection de la requête**. Lorsqu'un utilisateur pose une question, le système transforme cette question en un vecteur (une étoile dans la galaxie). Le moteur de recherche n'a plus qu'à regarder quelles sont les "étoiles" (les documents) les plus proches de la question.

{{< bookfig src="176.png" week="06" >}}


C'est ce qui est détaillé en **Figure 6-4 : Workflow de la base de connaissance** : 
1.  On transforme tous nos documents en vecteurs à l'avance (Indexation).
2.  On les stocke dans une "base de données vectorielle".
3.  À la requête, on compare et on affiche les résultats.

{{< bookfig src="177.png" week="06" >}}


## Laboratoire de code : Créer ses premiers embeddings (Colab T4)
Voici comment implémenter cela très simplement. Nous allons utiliser la bibliothèque `sentence-transformers`, qui est le standard de l'industrie.

```python
# Installation : !pip install sentence-transformers
from sentence_transformers import SentenceTransformer
import torch

# 1. Chargement du modèle de pointe
model = SentenceTransformer("all-mpnet-base-v2", device="cuda")

# 2. Nos phrases à comparer
sentences = [
    "The cat is relaxing on the sofa.",
    "A feline is resting on the couch.", # Très proche sémantiquement
    "The stock market experienced a significant drop today." # Très éloigné
]

# 3. Encodage : Transformation en vecteurs (Embeddings)
embeddings = model.encode(sentences)

print(f"Forme de la matrice d'embeddings : {embeddings.shape}")
# Attendu : (3, 768) -> 3 phrases de 768 dimensions chacune.

# 4. Vérification de la dimension
print(f"Dimension du vecteur pour une phrase : {len(embeddings[0])}")
# Attendu : 768

# 5. Comparaison des embeddings
from sklearn.metrics.pairwise import cosine_similarity

print(f"Similarité entre phrase 1 et 2 : {cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]}")
print(f"Similarité entre phrase 1 et 3 : {cosine_similarity([embeddings[0]], [embeddings[2]])[0][0]}")

```

> [!NOTE]
Comparez les représentations obtenues pour les deux phrases. Bien que les mots diffèrent (« cat » et « feline », « sofa » et « couch »), les embeddings peuvent refléter leur proximité sémantique.

## Éthique et Transparence : Les dimensions cachées du sens

> [!WARNING]
un vecteur est une réduction de la réalité. 
Quand vous compressez une pensée humaine complexe dans 768 nombres, vous perdez forcément des nuances. 
1.  **Biais de distance** : Si votre modèle a été entraîné sur des textes majoritairement occidentaux, il pourrait considérer que "mariage" est plus proche de "fête" que de "contrat", ce qui n'est pas universel.
2.  **Sensibilité aux détails** : Les embeddings de phrases sont parfois "trop globaux". Ils peuvent rater une petite négation ("ne... pas") qui change tout le sens de la phrase. 

> [!IMPORTANT]
**À retenir :** La recherche sémantique est un outil de découverte, pas un juge de vérité. Toujours prévoir une étape de vérification humaine ou un modèle de reranking (que nous verrons en [**section 6.3**]({{< relref "section-6-3.md" >}})) pour affiner les résultats.

---
