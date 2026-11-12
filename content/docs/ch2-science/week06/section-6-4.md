---
title: "6.4 Fine-tuning pour retrieval "
weight: 5
---

## Fine-tuning pour retrieval

Un modèle d’embeddings généraliste peut mal distinguer des expressions propres à un domaine. Des paires ou des triplets d’exemples permettent de l’adapter. L’évaluation sur des requêtes séparées de l’entraînement est nécessaire pour vérifier que cette adaptation améliore réellement la recherche.

## La géométrie du changement : Analyser les Figures 6-6 et 6-7
Pour bien comprendre ce qui se passe dans "le cerveau" du modèle pendant cet entraînement, regardons les schémas de l'espace vectoriel suivants:

*   [**Figure 6-6 : État avant le fine-tuning**]({{< relref "section-6-2.md" >}}#fig-6-6) : Imaginez une carte du ciel. Vous avez une question (une requête) au centre. Autour d'elle, à des distances presque égales, gravitent plusieurs documents. Certains sont les bonnes réponses (exemples positifs), d'autres sont des hors-sujets qui partagent juste quelques mots en commun (exemples négatifs). Le modèle est confus : il ne "sent" pas la différence de pertinence. Tout se ressemble à ses yeux car il n'a pas appris votre contexte spécifique.
*   [**Figure 6-7 : État après le fine-tuning**]({{< relref "section-6-2.md" >}}#fig-6-7) : L’entraînement vise à augmenter la similarité entre les requêtes et les documents pertinents, tout en la réduisant pour les documents non pertinents.

> [!NOTE]
**À retenir :** le fine-tuning est un processus de tension géométrique. On rapproche les alliés et on éloigne les intrus.


## La préparation des données : Triplets et paires contrastives
Comment dire au modèle qui rapprocher et qui repousser ?

On ne lui donne pas des notes, on lui donne des **exemples de comparaison**. La méthode la plus robuste utilise des **triplets** (Ancre, Positif, Négatif) :
1.  **L'Ancre (Anchor)** : C'est la requête type de l'utilisateur (ex: "Comment réinitialiser le mot de passe ?").
2.  **Le Positif (Positive)** : C'est le paragraphe qui contient la vraie solution.
3.  **Le Négatif (Negative)** : C'est un document qui ressemble à la question mais ne contient pas la réponse.

> [!TIP]
**Le concept avancé : Les "Hard Negatives" (Négatifs difficiles)**. 

> C'est le secret des meilleurs moteurs de recherche. Si vous donnez au modèle un négatif totalement absurde (ex: une recette de cuisine pour une question sur l'informatique), il n'apprendra rien. C'est trop facile. Pour qu'il devienne un expert, vous devez lui donner des documents qui parlent du même sujet mais qui sont techniquement incorrects pour cette question précise. C'est en échouant sur ces nuances qu'il affine sa compréhension.


## Les fonctions de perte : Multiple Negatives Ranking (MNR) Loss
Mathématiquement, pour réaliser ce "rapprochement/éloignement", nous utilisons souvent la **MNR Loss**. 
L'idée est brillante : dans un lot (*batch*) de données, on suppose que pour chaque question, il n'y a qu'une seule bonne réponse parmi toutes celles présentes dans le lot. Le modèle essaie de maximiser la similarité de la paire correcte tout en minimisant celle de toutes les autres combinaisons possibles. C'est une forme d'apprentissage par élimination extrêmement efficace sur GPU.


## Laboratoire de code : Fine-tuning rapide avec Sentence-Transformers
Voici comment transformer un modèle généraliste en un expert sur un petit jeu de données de support technique.

```python
# Exemple prévu pour Google Colab T4 16GB VRAM
# !pip install sentence-transformers datasets

from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

# 1. Chargement d'un modèle de base performant
model = SentenceTransformer('all-mpnet-base-v2')

# 2. Préparation de nos données métier (Triplets ou Paires)
train_examples = [
    InputExample(texts=['My internet is slow', 'Check your router settings and cables.'], label=0.9),
    InputExample(texts=['Blue screen error', 'This usually indicates a kernel panic or hardware failure.'], label=0.9),
    InputExample(texts=['How to pay my bill?', 'You can access the payment portal in your account settings.'], label=0.9),
    # On pourrait ajouter des exemples négatifs avec un label de 0.1
]

# 3. Création du DataLoader (gestion des lots pour le GPU)
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

# 4. Définition de la fonction de perte (Loss)
# La CosineSimilarityLoss est parfaite pour débuter avec des scores de 0 à 1
train_loss = losses.CosineSimilarityLoss(model)

# 5. L'entraînement (Le Fine-tuning)
print("Début de l'entraînement métier...")
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=10)

# 6. Test après entraînement
# Le modèle est maintenant plus sensible à vos termes spécifiques
print("Modèle prêt pour votre domaine !")
```


## Évaluation : Comment savoir si on a progressé ?

> [!WARNING]
Ne vous contentez pas de regarder la perte descendre pendant l'entraînement. C'est un mirage. 

> Pour valider un système de recherche, vous devez utiliser des métriques spécifiques au domaine du *Information Retrieval* :
> 1.  **Hit Rate @ K** : "Dans mon top K résultats (ex: top 5), est-ce que la bonne réponse est présente au moins une fois ?"
> 2.  **MRR (Mean Reciprocal Rank)** : Cette métrique est plus sévère. Elle vous donne plus de points si la bonne réponse est en 1ère position qu'en 5ème. 

> [!TIP]
>  **À retenir :** en recherche sémantique, l'utilisateur regarde rarement au-delà des trois premiers résultats. Le MRR est votre juge de paix.


## Éthique et Responsabilité : Le danger du sur-apprentissage (Overfitting)

> [!CAUTION]
un modèle trop spécialisé devient un modèle aveugle.

Si vous entraînez trop fort votre modèle sur vos données internes, il risque de perdre ses connaissances générales. 
> 1.  **Le biais de domaine** : Si vous lui apprenez que "virus" désigne uniquement un logiciel malveillant, il pourrait devenir incapable de trouver des documents sur la biologie, ce qui peut être problématique si votre entreprise est dans la santé.
> 2.  **Confidentialité des données d'entraînement** :
>  **Point crucial !** Si vos questions-réponses d'entraînement contiennent des secrets industriels ou des noms de clients, ces informations peuvent être "mémorisées" par le modèle dans ses poids. Un attaquant pourrait potentiellement extraire des fragments de ces données en interrogeant finement le modèle. 

> [!TIP]
**Synthèse** : L'adaptation au domaine doit être évaluée sur des données distinctes de celles de l'entraînement, afin de mesurer ses bénéfices et de détecter un éventuel surapprentissage.


---
