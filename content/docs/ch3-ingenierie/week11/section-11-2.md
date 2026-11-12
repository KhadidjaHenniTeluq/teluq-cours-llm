---
title: "11.2 La méthode LoRA"
weight: 3
---

{{< katex />}}

## La méthode LoRA

LoRA conserve une matrice de poids et apprend une correction exprimée comme le produit de deux matrices de faible rang. Cette correction réduit le nombre de paramètres entraînables. Il faut distinguer cette économie de paramètres de la mémoire totale nécessaire au modèle, aux activations et à l’optimiseur.

## Animation : LoRA et les matrices de faible rang

{{< conceptvideo name="lora" title="LoRA et les matrices de faible rang" >}}
La matrice W de taille 4096 × 4096 reste gelée : elle contient 16 777 216 paramètres. Avec un rang r = 8, la matrice A a la taille 8 × 4096 et B la taille 4096 × 8. Ensemble, A et B contiennent 65 536 paramètres entraînables. La sortie est y = W x + (α / r) B A x. Cette branche ajoute une correction de faible rang. Pour cette matrice, il y a 256 fois moins de paramètres entraînables, mais les poids de base restent en mémoire : ce ratio n’est pas celui de la mémoire GPU totale.
{{< /conceptvideo >}}

## L'intuition : Le calque sur le dictionnaire
Pour comprendre LoRA, utilisons une analogie visuelle. Imaginez un dictionnaire géant de 10 000 pages (votre modèle de base). Vous voulez qu'il apprenne à parler comme un médecin. 
*   **Le Full Fine-Tuning** consisterait à réécrire chaque page du dictionnaire pour y insérer des termes médicaux. 
*   **LoRA**, comme l'illustre la **Figure 11-5 : LoRA comme sous-ensemble séparé**, consiste à laisser le dictionnaire original intact (il est **gelé**) et à poser par-dessus des calques transparents. Sur ces calques, vous n'écrivez que les *changements* nécessaires. À la fin, quand vous lisez le dictionnaire à travers les calques, vous obtenez le langage médical souhaité. 

{{< bookfig src="267.png" week="11" >}}

La **Figure 11-5** est cruciale car elle montre que les poids de l'adaptateur sont stockés séparément. 

> [!NOTE]
**C'est le secret de la portabilité :** vous pouvez échanger vos "calques" (adaptateurs) en quelques millisecondes sans jamais toucher au dictionnaire original (le Base Model).


---
## Le problème mathématique : La taille des matrices
Un Transformer comprend de nombreuses matrices de poids. La **Figure 11-6 : Le goulot d’étranglement des matrices de poids** en présente un exemple.

{{< bookfig src="268.png" week="11" >}}

*   **Analyse de la figure** : Pour un modèle comme GPT-3 ou Llama-3, une seule matrice de projection (comme celle de l'attention) peut faire 4096 x 4096, soit plus de 16 millions de paramètres. Et il y a des centaines de matrices de ce type ! 
*   **Le constat** : Modifier tous ces nombres à chaque étape de l'entraînement consomme une énergie et une mémoire VRAM colossales. 

> [!TIP]
C'est là que les chercheurs Edward Hu et ses collègues ont fait une découverte fondamentale : les modèles de langage ont une **dimension intrinsèque basse**. Cela signifie que même si la matrice a 16 millions de "boutons", seule une infime fraction de ces boutons a réellement besoin de bouger pour apprendre une nouvelle tâche.


---
## La solution : La décomposition à bas rang (Low-Rank)
La **Figure 11-7 : Décomposition d'une grande matrice en deux petites** présente le principe de cette factorisation.

{{< bookfig src="269.png" week="11" >}}


**Principe mathématique** : La mise à jour $\Delta W$, de dimension $d \times k$, est représentée par le produit de deux matrices de faible rang, **A** et **B**.
*   Si la matrice originale fait $100 \times 100$ (10 000 paramètres): Nous créons une matrice **A** de $100 \times r$ et une matrice **B** de $r \times 100$.
*   **r** est ce qu'on appelle le **Rang** (Rank). C'est un petit nombre, souvent égal à 4, 8 ou 16.
* **Calcul des paramètres** : Pour deux dimensions de 100 et un rang de 8, A et B comptent chacune 800 paramètres. Cela donne 1 600 paramètres entraînables contre 10 000 pour la matrice complète, soit 84 % de moins. Ce pourcentage ne mesure pas directement le gain de temps ni la mémoire totale.


---
## Le flux d'information
La **Figure 11-8 : Comparaison entre le Fine-tuning complet et LoRA** nous montre comment l'information circule pendant l'entraînement.

{{< bookfig src="270.png" week="11" >}}

1.  **Le chemin de gauche (Frozen)** : L'entrée (Input) passe par la matrice originale. Les poids sont gelés, aucune erreur ne remonte ici. 
2.  **Le chemin de droite (Trainable)** : L'entrée passe en parallèle par nos deux petites matrices A et B. C'est ici que le modèle "apprend". 
3.  **La fusion** : Les sorties des deux chemins sont additionnées. 

> [!WARNING]
**Attention :** Beaucoup croient que LoRA ralentit l'inférence. C'est faux. Une fois l'entraînement fini, on peut mathématiquement multiplier A et B pour obtenir une matrice de la même taille que l'originale, et l'additionner aux poids de base. On appelle cela le **Merge**. Le modèle redevient un Transformer standard, sans aucun délai supplémentaire.


---
## Les Hyperparamètres de LoRA : Régler son adaptateur

> [!IMPORTANT]
**À retenir :**### 1. Le Rang ($r$)
C'est la largeur de vos petites matrices. 
*   **Petit $r$ (4 ou 8)** : Très peu de paramètres, très rapide, mais peut manquer de "capacité de mémorisation" pour des tâches complexes.
*   **Grand $r$ (64 ou 128)** : Plus puissant, mais consomme plus de VRAM.
> [!TIP] 
**Conseil méthodologique** : Commencez toujours par $r=8$. C'est souvent suffisant pour l'instruction tuning.

### 2. Alpha ($\alpha$)
C'est un facteur d'échelle (scaling). Il détermine à quel point les "calques" (adaptateurs) doivent écraser ou non les connaissances du dictionnaire original. 

> [!TIP]
Une règle d'or empirique est de fixer $\alpha = 2 \times r$. Si $r=16$, alors $\alpha=32$.

### 3. Target Modules (Où coller les calques ?)
On n'applique pas LoRA partout. Dans un bloc Transformer (Semaine 3), on cible généralement les matrices de projection de l'attention :
*   `q_proj` (Query)
*   `v_proj` (Value)

> [!NOTE]
**Notez bien :** des recherches récentes montrent que cibler également les couches `k_proj` (Key) et les couches du MLP (Feedforward) augmente significativement la qualité du modèle au prix d'une légère augmentation de la mémoire.


---
## Mise en œuvre pratique : La bibliothèque PEFT
Hugging Face a créé la bibliothèque **PEFT** (*Parameter-Efficient Fine-Tuning*) pour automatiser tout cela. Voici à quoi ressemble la configuration d'un modèle Llama-3 ou Phi-3 pour LoRA sur votre GPU T4.

```python
# Exemple prévu pour Colab T4 16GB VRAM
# !pip install peft transformers

from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

# 1. Chargement du modèle de base (gelé)
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# 2. Configuration de l'adaptateur LoRA
peft_config = LoraConfig(
    r=16,                # Le rang (rank)
    lora_alpha=32,       # Facteur d'échelle (Alpha)
    target_modules=["q_proj", "v_proj", "k_proj"], # Les couches ciblées
    lora_dropout=0.05,   # Pour éviter le sur-apprentissage
    bias="none",
    task_type="CAUSAL_LM"
)

# 3. Création du modèle avec adaptateur
model = get_peft_model(model, peft_config)

# 4. Vérification des paramètres
model.print_trainable_parameters()
# Résultat attendu : "trainable params: 0.12% of total params"
```

> [!IMPORTANT]
Regardez bien le résultat de `print_trainable_parameters()`. 

> Vous verrez que vous n'entraînez que **0.1%** du modèle ! C'est ce chiffre minuscule qui permet à un étudiant avec une seule carte graphique de rivaliser avec des laboratoires de recherche.


---
## Avantages et limites de LoRA
Il existait d'autres méthodes comme les "Adapters" (insérer des couches *entre* les couches existantes). Mais LoRA a gagné car :
1.  **Pas de latence** : Grâce au "Merge", le modèle final est aussi rapide que l'original. 
2.  **Stabilité** : L'entraînement est beaucoup plus stable que le "Prompt Tuning" qui est très sensible à l'initialisation.
3.  **Modularité** : On peut entraîner un adaptateur LoRA pour le français, un pour le code, un pour le droit, et les charger à la volée sur le même modèle de base.


---
## Éthique et Responsabilité : La démocratisation du pouvoir

> [!NOTE]    
LoRA est un outil de libération.

L'adaptation de tous les paramètres d'un LLM peut exiger des ressources importantes. LoRA réduit les ressources nécessaires en limitant le nombre de paramètres entraînables.
1.  **Inclusion** : Grâce à LoRA, des communautés linguistiques minoritaires peuvent fine-tuner des modèles sur leurs propres langues sans budget massif. 
2.  **Souveraineté des données** : Comme LoRA permet d'entraîner sur des GPU modestes, vous n'avez plus besoin d'envoyer vos données sensibles (santé, vie privée) sur les serveurs d'OpenAI pour faire du fine-tuning. Vous pouvez le faire **localement**, en restant maître de vos données. 


**C'est un pilier de l'IA responsable :** la protection de la vie privée par la technique.

> [!TIP]
**Synthèse** : LoRA adapte le modèle à l'aide de matrices de faible rang. Le nombre de paramètres entraînables dépend notamment du rang choisi et des couches ciblées.


---
LoRA réduit le nombre de paramètres entraînables, mais le modèle de base doit toujours être chargé en mémoire. La section suivante présente la **quantification**, qui réduit la précision utilisée pour représenter les paramètres.