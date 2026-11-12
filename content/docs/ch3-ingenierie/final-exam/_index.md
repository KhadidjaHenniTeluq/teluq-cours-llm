---
title: "Examen final"
weight: 7
---

# Examen final, SCI1040

Répondez aux questions en justifiant vos choix. Pour les exercices, remettez le code demandé, les résultats observés et une discussion de leurs limites. Les modalités de remise et les ressources autorisées sont celles communiquées par la professeure.

## Partie 1 : Questions de compréhension et de conception

### Question 1 : Architecture Transformer

Expliquez le rôle du facteur 1/√d_k dans le calcul des scores d’attention. Que peut-il se passer quand les scores deviennent très grands ?

### Question 2 : Inférence et Optimisation

Expliquez le compromis entre calcul et mémoire introduit par le cache KV pendant la génération causale.

### Question 3 : Fine-tuning (PEFT)

Dans la méthode LoRA, quel est l'impact d'un choix de rang (r) trop élevé par rapport à un rang faible ?

### Question 4 : Recherche Sémantique

Pourquoi utilise-t-on souvent un bi-encodeur pour la recherche initiale et un cross-encodeur pour reclasser une sélection de passages ?

### Question 5 : Alignement (DPO)

Comparez le rôle du modèle de référence dans une approche RLHF utilisant PPO et dans DPO. Distinguez-le du modèle de récompense.

### Question 6 : Tokenisation

Quelles sont les conséquences techniques d'un 'Fragmentation Ratio' élevé pour une langue spécifique ?

### Question 7 : Multimodalité

Dans l'architecture BLIP-2, quel est le rôle précis du Q-Former ?

### Question 8 : Ingénierie des Prompts

Décrivez le phénomène « Lost in the Middle ». Comment testeriez-vous son effet dans un système RAG ?

### Question 9 : RAG (Evaluation)

Un système obtient une fidélité au contexte de 1,0 et une pertinence de réponse de 0,1 selon son évaluateur. Que suggère ce résultat et quelles vérifications complémentaires faut-il faire ?

### Question 10 : Quantification

Pourquoi NF4 utilise-t-il une grille fondée sur une distribution normale de référence ? Quelles limites faut-il garder à l’esprit ?

### Question 11 : Agents et Autonomie

Décrivez le rôle des étapes de décision, d’action et d’observation dans une boucle ReAct. Pourquoi prévoir une condition d’arrêt ?

### Question 12 : Éthique et Biais

Comment la similarité cosinus peut-elle involontairement amplifier des biais lors d'une recherche de CV par embeddings ?

### Question 13 : Sécurité

Décrivez le mécanisme d'une 'Indirect Prompt Injection'.

### Question 14 : Architecture (Normalisation)

Quel est l'avantage de la 'Pre-Normalization' par rapport à la 'Post-Normalization' dans l'entraînement de modèles profonds ?

### Question 15 : Futur des LLM

Comparez la mémoire utilisée pour le passé par un Transformer causal avec cache KV et par un modèle à espace d’état récurrent. Précisez la phase de calcul considérée.

## Partie 2 : Exercices de programmation et d’analyse

### Exercice 1 : Étudier la géométrie des représentations

Avec GPT-2, construisez un échantillon de tokens et documentez leur contexte. Extrayez les représentations de deux couches, puis calculez la moyenne des similarités cosinus hors diagonale et visualisez leur distribution. Fixez une graine pour l’échantillonnage.

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModel, AutoTokenizer

model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id, output_hidden_states=True)
model.eval()

# À compléter : préparation des entrées et extraction des couches.

def moyenne_hors_diagonale(vecteurs):
    # À compléter : calcul, masque de la diagonale, moyenne.
    pass
```

Expliquez les limites de votre échantillon et ce qui permettrait de mieux étayer une conclusion sur l’anisotropie. Aucun intervalle numérique de similarité n’est imposé.

### Exercice 2 : Recherche et autorisations d’accès

Créez deux documents fictifs : un document public sur la météo et un document privé contenant une information confidentielle. À partir de leurs métadonnées, construisez une recherche destinée à un utilisateur public.

```python
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

# À compléter : documents fictifs, embeddings et recherche.
# Vérifier les documents effectivement transmis au générateur.
```

Testez une requête qui vise l’information privée. Montrez les documents retournés et justifiez le contrôle appliqué. Précisez où intervient le filtrage dans la version utilisée et quelles mesures supplémentaires seraient nécessaires pour une application réelle.

### Exercice 3 : Configurer LoRA

Construisez une configuration LoRA avec un rang de 8, un facteur alpha de 16 et les modules cibles `q_proj` et `v_proj`. Vérifiez que ces noms existent dans le modèle choisi.

```python
from peft import LoraConfig

# À compléter : configuration et vérification des modules ciblés.
```

Calculez le nombre de paramètres entraînables pour une matrice dont vous précisez les dimensions. Discutez la différence entre paramètres entraînables et mémoire totale.

### Exercice 4 : Génération et validation d’un format

Configurez une génération gloutonne, sans échantillonnage, limitée à 50 nouveaux tokens. Demandez une réponse JSON avec les champs `titre` et `resume`.

```python
import json

# À compléter : model.generate(...), décodage, json.loads(...).
# Vérifier les champs attendus et leur type.
# Prévoir le traitement d’une sortie invalide ou tronquée.
```

Présentez un exemple valide et expliquez comment détecter une réponse invalide. Distinguez le choix du mode de décodage, le respect de la structure et l’exactitude du contenu.

## Grille de notation des exercices

- Code fonctionnel : 50 % de la note de l’exercice.
- Justification théorique : 30 %.
- Discussion des limites : 20 %.

Relisez les dimensions, les hypothèses et les unités avant de remettre votre travail.
