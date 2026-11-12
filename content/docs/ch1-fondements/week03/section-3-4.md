---
title: "3.4 Forward pass complet et accélération par cache KV"
weight: 5
---

## Forward pass complet et accélération par cache KV

Le passage avant, ou forward pass, transforme les tokens d’entrée en scores sur le vocabulaire. Les embeddings traversent plusieurs blocs Transformer avant la projection finale. Une stratégie de décodage choisit ensuite le token suivant. Le cache KV réutilise une partie des calculs lors de la génération causale.

## 1. L'architecture du flux

<a id="fig-3-20"></a>

Commençons par regarder la carte du trajet. La **Figure 3-20 : Les composants de la passe avant** est notre plan de vol. 

{{< bookfig src="57.png" week="03" >}}

** Explication** : Cette illustration nous montre que la passe avant n'est pas un bloc monolithique, mais une succession de trois grandes gares :
1.  **Le Tokeniseur** : Il transforme le texte en IDs.
2.  **La Pile de blocs Transformer** : C'est le cœur du traitement (la "boîte noire").
3.  **La Tête de modélisation du langage (LM Head)** : C'est là que la décision finale est prise.

> [!TIP]
**À retenir :** l'information ne circule que dans un seul sens, du haut vers le bas (ou de l'entrée vers la sortie). 

> Contrairement à l'entraînement (Backpropagation), ici on ne revient jamais en arrière. On calcule, on avance.

---
## 2. Phase 1 : La porte d'entrée
Tout commence par un texte brut. Supposons que l'utilisateur tape : "Say something smart".
Regardez la **Figure 3-21 : Le vocabulaire et les embeddings** .

{{< bookfig src="58.png" week="03" >}}

** Explication** : 
*   **Mise en correspondance** : Le mot "smart" est identifié dans le dictionnaire du tokeniseur. Supposons que son ID soit `50000`.
*   **L'extraction du vecteur** : Le modèle va chercher la 50 000ème ligne de sa matrice d'embeddings. Comme le montre la figure, il en ressort un vecteur de nombres (ex: 768 ou 3072 dimensions). 
*   **L'injection de position** : À ce vecteur, on ajoute immédiatement l'encodage positionnel (vu en 3.2). Sans cela, le modèle saurait que l'on parle de "smart", mais il ne saurait pas que c'est le troisième mot de la phrase. 

> [!NOTE]
**Analogie:** C'est comme un voyageur qui arrive à l'aéroport. On lui donne un badge (l'embedding) et un numéro de siège (la position). Sans ces deux éléments, il ne peut pas embarquer dans l'avion Transformer.

---
## 3. Phase 2 : La traversée des blocs (Le traitement profond)
Une fois le passager "textuel" équipé, il entre dans la pile de blocs.
> [!WARNING] 
**Attention :** On imagine souvent que l'information reste la même tout au long de la pile. En réalité, le vecteur change de nature à chaque étage.

*   **Dans le bloc 1** : Le token "smart" regarde ses voisins ("say", "something"). Il comprend qu'il est l'adjectif d'une requête impérative.
*   **Dans le bloc 12** : Après douze couches d'attention et de réseaux FFN, la représentation de « smart » intègre des informations issues du contexte.

> [!IMPORTANT]
**À retenir :**Lors de la génération de texte, le modèle produit un vecteur de sortie pour *chaque* mot de l'entrée. 

> Mais pour prédire le mot suivant, nous n'utilisons que le vecteur correspondant à la **dernière position**. 
Pourquoi ? Parce que grâce à l'attention, ce dernier vecteur a déjà "absorbé" toute la connaissance des mots qui le précèdent.

---
## 4. Phase 3 : La décision finale
La représentation issue du dernier bloc est transmise à la **LM Head**, présentée dans la **Figure 3-23 : Prédiction de probabilité**.

{{< bookfig src="59.png" week="03" >}}

** Explication** : 
*   **La projection** : Le vecteur final (ex. : 768 dimensions) est projeté dans un espace dont la dimension correspond à la taille du vocabulaire (ex. : 50 000).
*   **Le score brut (Logits)** : Chaque mot du dictionnaire reçoit une note. Le mot "Think" pourrait recevoir 15.2, le mot "The" 8.1, et le mot "Banana" -4.5.
*   **Le Softmax** : On transforme ces notes en pourcentages. "Think" devient 40% probable, "The" devient 10%, etc. 

**C'est le moment de la parole :** Le modèle ne "sait" pas quel est le bon mot. Il sait simplement lequel est statistiquement le plus cohérent après "Say something smart".

---
## 5. Optimisation : Le KV Cache
Recalculer les représentations des tokens précédents à chaque étape de génération augmente le coût de l'inférence. Le cache KV permet de réutiliser certains résultats.

Regardez la **Figure 3-24 : KV cache pour accélération** .

{{< bookfig src="63.png" week="03" >}}

** Explication** : 
*   **Le gaspillage** : Pour générer le mot n°2, le modèle a besoin de re-calculer l'attention sur le mot n°1. 
*   **La solution** : On stocke les Keys (K) et les Values (V) du mot n°1 dans une mémoire vive ultra-rapide sur le GPU. 
*   **Le gain** : À l'étape suivante, le modèle calcule les représentations du nouveau token et réutilise les clés et valeurs conservées dans le cache.

> [!NOTE]
**À retenir :** Le KV Cache est ce qui permet à ChatGPT de vous répondre en "streaming" (mot à mot) en temps réel. Sans cette optimisation, l'IA de production n'existerait pas.

---
## 6. Sampling et Décodage : Choisir dans le nuage
Une fois que nous avons nos probabilités (Figure 3-23), comment choisir le mot final ?
1.  **Greedy Decoding** : On prend toujours le n°1 (40% "Think"). C'est sûr mais ennuyeux.
2.  **Sampling (Échantillonnage)** : On tire au sort selon les poids. "Think" a 4 chances sur 10 de sortir. C'est ce qui donne du "style" à l'IA.

> [!WARNING]
Ne confondez pas le calcul (Forward Pass) et le choix (Decoding). 

> Le Forward Pass est une mathématique déterministe. Le décodage est l'endroit où nous injectons le hasard (la Température) pour rendre l'IA humaine.

---
## Laboratoire de code : Analyse de la structure
Pour conclure cette semaine, je veux que vous sachiez comment lire le "plan de vol" de n'importe quel modèle.

```python
# Exemple prévu pour Colab T4 16GB VRAM
from transformers import AutoModelForCausalLM

# 1. CHARGEMENT D'UN MODÈLE COMPACT
model = AutoModelForCausalLM.from_pretrained("gpt2")

# 2. INSPECTION DU FORWARD PASS
# Cette commande imprime l'ordre exact des couches que le token va traverser
print("--- ARCHITECTURE DU MODÈLE (PASSE AVANT) ---")
print(model)

# --- EXPLICATION DES RÉSULTATS ---
# Vous verrez :
# - 'wte' (Word Token Embeddings) : Gare de départ
# - 'wpe' (Word Position Embeddings) : La boussole
# - 'h' (Blocks) : Les 12 étages de la matière grise
# - 'ln_f' (Final LayerNorm) : La stabilisation finale
# - 'lm_head' : La bouche du modèle (Dernière étape)
```
> [!NOTE]
**Note** : Regardez bien la couche `lm_head`. Vous verrez `Linear(in_features=768, out_features=50257)`. **C'est la preuve mathématique :** on transforme un résumé interne de 768 nombres en un choix parmi 50 257 mots possibles.

---
## Éthique et Responsabilité : La boîte noire et le déterminisme

> [!CAUTION]
la passe avant est une mécanique d'une précision effrayante, mais elle est opaque.

1.  **L'impossibilité de l'arrêt** : Une fois que le Forward Pass est lancé, on ne peut pas l'arrêter à mi-chemin pour dire au modèle : "Hé, tu es en train de prendre une mauvaise direction logique !". Le modèle calcule jusqu'au bout.
2.  **Le biais sémantique** : Si, à la couche 5, une tête d'attention a fait une erreur d'interprétation, cette erreur va se propager et s'amplifier dans les 27 couches suivantes. C'est *l'effet papillon* du neurone. 
3.  **La consommation invisible** : Chaque Forward Pass, même pour dire "Bonjour", consomme une quantité d'électricité précise sur le serveur. 

> [!IMPORTANT]
**La responsabilité de l'ingénieur** est de savoir quand utiliser un gros modèle ou un petit (Semaine 13) pour économiser ces ressources.

> [!TIP]
**Synthèse** : Cette section a décrit le parcours des représentations, de l'entrée du modèle jusqu'à la prédiction du token suivant.

> L’analyse du Transformer relie sa structure, l’encodage des positions et les transformations successives des représentations.

La semaine suivante porte sur les modèles **Encoder-only**, dont BERT.

---
