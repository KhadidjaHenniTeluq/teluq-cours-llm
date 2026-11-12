---
title: "Mission 2. Analyse de l'Anisotropie"
weight: 2
---
{{< katex />}}

# Évaluation 1, Mission 2 : Analyse de l'Anisotropie (Le Phénomène du Cône)
## Audit de la distribution géométrique des vecteurs de la couche finale de GPT-2

Dans cette mission, nous analysons l'**anisotropie** des représentations (ou effet de « cône »).

> [!IMPORTANT]
**Note technique :** 
L’anisotropie décrit une distribution dont les propriétés dépendent de la direction. Pour des embeddings, une forte similarité moyenne entre représentations non apparentées peut signaler des directions communes. Cette observation demande un échantillon et un protocole ; elle ne constitue pas une maladie du modèle.

---

## 1. Préparation de l'environnement
*Temps estimé : 2 minutes. Assurez-vous d'être en mode "GPU T4" (Exécution > Modifier le type d'exécution).*

```python
# Installation des dépendances
# !pip install -q transformers torch numpy scipy matplotlib seaborn scikit-learn

import torch
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import AutoModelForCausalLM, AutoTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Hardware setup
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, output_hidden_states=True).to(device)
model.eval()
```

---

## 2. Implémentation technique
Nous allons extraire des vecteurs pour 500 tokens aléatoires à la couche 0 et à la couche 12, puis comparer leurs distributions de similarité.

```python
# Sélection de 500 tokens aléatoires (excluant les tokens de contrôle)
vocab_size = tokenizer.vocab_size
random_token_ids = random.sample(range(100, vocab_size - 100), 500)

def get_embeddings_at_layer(token_ids, layer_idx):
    """
    Extrait les vecteurs pour une liste d'IDs à une couche spécifique.
    """
    ids_tensor = torch.tensor([token_ids]).to(device) 
    with torch.no_grad():
        outputs = model(ids_tensor)
    
    selected_layer = outputs.hidden_states[layer_idx] 
    return selected_layer[0].cpu().numpy()

# --- CONFIGURATION DE LA MISSION (QUESTION CODE) ---
# TÂCHE : Extraire les embeddings aux couches 0 et 12, puis calculer la similarité cosinus moyenne.

# 1. Récupérez les embeddings pour embeddings_layer_0 et embeddings_layer_12
# ...

def compute_avg_cosine_sim(embeddings):
    # 2. Implémentez le calcul de la similarité cosinus moyenne en ignorant la diagonale
    # ...
    pass

# 3. Affichez et comparez les résultats !
```

---

## 3. Analyse et Justifications (À remettre par l'étudiant)

**Résultats attendus :**
Mesurez la moyenne hors diagonale et la distribution des similarités pour chaque couche. Ne cherchez pas à reproduire un intervalle imposé : les valeurs dépendent des tokens, de leur contexte, de la couche et du modèle. Ici, les tokens aléatoires sont concaténés dans une même séquence ; signalez que ce contexte artificiel limite l’interprétation.

> [!NOTE]
> * La solution complète avec le code matplotlib/seaborn pour générer les graphiques de densité KDE et l'analyse approfondie est incluse dans le notebook Colab qui sera partagé avec le prof.

---

## Question Critique de Mission
**Question** : Quelle est la cause structurelle de cette dégénérescence des représentations à la couche 12 de GPT-2, et quel est son impact concret sur la recherche sémantique ?

**Piste d’analyse** : Distinguez l’observation géométrique de son interprétation. Comparez les couches et discutez l’effet du contexte artificiel. On ne peut pas attribuer une cause unique à la similarité mesurée sans expériences complémentaires.

---

> [!WARNING]
**Limite de l’analyse** : Une mesure d’anisotropie ne suffit pas à démontrer un biais envers un groupe social. Une telle conclusion nécessite des données adaptées et une évaluation distincte.


Pour approfondir : [Ethayarajh, 2019, géométrie des représentations contextuelles](https://arxiv.org/abs/1909.00512).
