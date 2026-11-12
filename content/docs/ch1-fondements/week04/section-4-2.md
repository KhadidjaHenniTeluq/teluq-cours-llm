---
title: "4.2 Stratégies d'utilisation"
weight: 3
---

{{< katex />}}

## Stratégies d'utilisation

Un modèle préentraîné peut servir d’extracteur de caractéristiques ou être adapté à une tâche. Dans le premier cas, on conserve ses poids et on entraîne éventuellement un classifieur sur ses représentations. Dans le second, on ajuste une partie ou l’ensemble de ses paramètres avec des données étiquetées.

{{< bookfig src="89.png" week="04" >}}

## Stratégie 1 : Le Fine-tuning complet (Unfreezing)
C'est la méthode la plus puissante, mais aussi la plus gourmande. Imaginez que vous engagiez un chercheur brillant et que vous lui permettiez de remettre en question tout ce qu'il sait pour s'adapter à votre entreprise.
*   **Le principe** : On prend BERT, on ajoute une petite couche de classification à la fin, et on ré-entraîne *l'intégralité* des paramètres sur nos données.
*   **Quand l'utiliser ?** : Lorsque vous avez beaucoup de données étiquetées (plusieurs milliers) et que votre domaine est très différent du langage courant (par exemple, de la physique nucléaire ou du droit ancien).
*   **Inconvénient** : C'est lent et cela nécessite une carte graphique robuste (comme la T4 de notre Colab). 
> [!WARNING]
**Attention :** Si vous ré-entraînez trop fort sur un petit jeu de données, vous risquez le "*Catastrophic Forgetting*" : le modèle devient un génie pour votre tâche mais oublie tout le reste du langage.

## Stratégie 2 : L'extraction de caractéristiques (Frozen Layers)
La **Figure 4-6 : Classification directe vs. indirecte** présente l’utilisation de BERT comme extracteur de représentations, sans modification de ses paramètres.
*   **Le principe** : On "gèle" (freeze) les 12 couches de BERT. On lui donne une phrase, il nous rend un vecteur (l'embedding du token `[CLS]`), et nous entraînons un classifieur très simple (comme une régression logistique avec Scikit-Learn) par-dessus.
*   **Analogie** : C'est comme si vous utilisiez un expert pour traduire un texte complexe, puis que vous preniez sa traduction pour décider si le sujet est intéressant. Vous ne changez pas la façon dont l'expert travaille ; vous utilisez simplement son résultat. 
*   **Avantage** : Les représentations peuvent être calculées sans mise à jour des paramètres de BERT. La durée du traitement dépend du volume de documents et des ressources disponibles.

{{< bookfig src="90.png" week="04" >}}


## Modèle de sélection : Comment choisir son champion ?
ne vous perdez pas dans les 60 000 modèles de Hugging Face ! Pour réussir votre projet, votre sélection doit suivre trois critères non-négociables :
1.  **La langue** : N'utilisez pas un BERT entraîné uniquement sur l'anglais pour analyser du français. Cherchez des modèles comme `CamemBERT` (français) ou des modèles multilingues comme `mBERT` ou `XLM-RoBERTa`.
2.  **La taille** : Si vous déployez sur un téléphone, `DistilBERT` est votre meilleur ami. Si vous cherchez la précision absolue, `DeBERTa-v3` est le roi actuel.
3.  **Le domaine** : Il existe des versions spécialisées comme `SciBERT` (articles scientifiques) ou `BioBERT` (médecine). Utiliser un modèle déjà pré-adapté à votre domaine vous fera gagner des semaines de travail.

## Le baromètre mondial : MTEB Leaderboard

> [!TIP]
Si vous voulez savoir quel modèle produit les meilleurs embeddings au monde aujourd'hui, vous devez consulter le **MTEB (Massive Text Embedding Benchmark) Leaderboard**. C'est le "*Billboard Hot 100*" de l'IA de représentation. Il classe les modèles sur des dizaines de tâches différentes. 

> [!WARNING]
Un modèle qui est numéro 1 pour la recherche de documents ne sera pas forcément le meilleur pour la classification de sentiments. Regardez les colonnes spécifiques à votre tâche !

## Implémentation pratique : La puissance de `pipeline`
Hugging Face a créé une abstraction magnifique pour nous simplifier la vie. Voici comment implémenter un classifieur de pointe en 3 lignes de code.

```python
# Installation : pip install transformers
from transformers import pipeline

# Choix d'un modèle RoBERTa optimisé pour le sentiment
model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Création de la pipeline
# device=0 utilise le GPU T4 de Colab (indispensable pour la vitesse)
pipe = pipeline("sentiment-analysis", model=model_path, device=0)

# Test sur une critique de film
result = pipe("This film is a masterpiece of modern representation models!")

print(f"Résultat : {result}")
# Sortie attendue : [{'label': 'positive', 'score': ~ 0.98}]
```
> [!NOTE]
**Note technique** : Le pipeline télécharge le tokeniseur et les poids du modèle, prépare les entrées et renvoie une étiquette de classification. Cette interface facilite le prototypage.

## Éthique et Responsabilité : Le coût de l'expertise

> [!CAUTION]
**Éthique ancrée** : Mesurez l'impact environnemental de vos choix. 
Le fine-tuning complet (Stratégie 1) consomme beaucoup d'énergie car vous recalculez les gradients pour des centaines de millions de paramètres à chaque itération. 

> [!TIP]
**Conseil méthodologique** : Commencez TOUJOURS par la Stratégie 2 (modèle gelé). Si les performances ne sont pas suffisantes, passez alors au fine-tuning. Une IA responsable est aussi une IA sobre qui n'utilise pas un marteau-pilon pour écraser une mouche.

---
La section suivante présente l'évaluation des modèles de classification à l'aide des **matrices de confusion** et du **score F1**.
