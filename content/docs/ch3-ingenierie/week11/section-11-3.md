---
title: "11.3 Quantification "
weight: 4
---

## Quantification

La quantification représente des valeurs avec une précision ou un nombre de niveaux plus faible. Elle peut réduire le stockage et certains coûts de calcul, mais introduit une erreur. Il faut distinguer le format de stockage des poids du format utilisé pour les calculs.

## Animation : Quantification et erreur d’arrondi

{{< conceptvideo name="quantification" title="Quantification et erreur d’arrondi" >}}
Sur une grille symétrique de pas s = 0,5, sans saturation, on calcule q = arrondi(w / s), puis le poids reconstruit s × q. Les poids −1,3, 0,2 et 1,7 deviennent respectivement −1,5, 0 et 1,5. Réduire le nombre de valeurs représentables peut économiser du stockage, au prix d’une erreur. Les méthodes réelles incluent des échelles par groupe, des métadonnées et parfois une grille non uniforme ; cette démonstration n’est pas une reproduction de NF4.
{{< /conceptvideo >}}

## Qu'est-ce que la quantification ? L'analogie de la peinture
La quantification est l'art de réduire la précision des nombres qui représentent les poids d'un réseau de neurones. Pour comprendre, imaginez que vous deviez peindre un tableau. 
*   **Haute précision (Float32)** : Vous avez une palette de 4 milliards de nuances de couleurs. C'est magnifique, mais cela prend énormément de place de stocker tous ces tubes de peinture. 
*   **Quantification (Int4)** : On vous force à ne peindre qu'avec 16 couleurs de base. 

> [!NOTE]
**Le but de la quantification** : Trouver la meilleure façon de choisir ces 16 couleurs pour que, de loin, le tableau ressemble encore exactement à l'original. En informatique, nous passons de nombres codés sur 32 ou 16 bits à des nombres codés sur seulement 4 bits.


---
## La mathématique des bits : Float32 vs Float16 
Regardons la **Figure 11-9 : Représentation de Pi en différentes précisions** . Cette figure est capitale pour comprendre ce que nous sacrifions.

{{< bookfig src="271.png" week="11" >}}


*   **Float32 (Précision complète)** : Un nombre occupe 32 bits (4 octets). Il se décompose en un bit de signe, 8 bits d'exposant et 23 bits de mantisse. C'est la précision utilisée pour la recherche scientifique de pointe.
*   **Float16 / BFloat16 (Demi-précision)** : Un nombre occupe 16 bits (2 octets). Comme le montre la figure, on commence à perdre des chiffres après la virgule. C'est le standard actuel pour l'entraînement des LLM car cela divise par deux la mémoire nécessaire sans impacter significativement l'intelligence du modèle.
*   **Int4 (Quantification extrême)** : On n'utilise plus que 4 bits. On n'a plus que 16 valeurs possibles (de 0 à 15, ou -8 à 7). 

> [!WARNING]
**Attention :** On ne peut pas simplement "couper" les chiffres après la virgule. Si vous faites cela, vous détruisez les relations subtiles entre les neurones et le modèle devient incohérent (hallucinations massives).

---
## Le problème de la quantification naïve 
Observez la **Figure 11-10 : Problème de l'arrondi uniforme** . Cette illustration nous montre ce qui se passe quand on essaie de faire rentrer des poids très différents dans des "bacs" (buckets) de même taille.

{{< bookfig src="272.png" week="11" >}}

*   **Analyse de la figure** : Si vous avez beaucoup de poids proches de zéro et quelques poids très élevés (des "outliers"), une règle de calcul simple va écraser tous les petits poids dans la même valeur zéro. Vous perdez toute la nuance qui fait la richesse du langage. 

> [!IMPORTANT]
**À retenir :** Le secret d'une bonne quantification n'est pas de réduire, mais de **distribuer** intelligemment les valeurs. 

---
## La solution QLoRA : NF4 et Quantification par blocs
En 2023, *Tim Dettmers* a publié l'article "QLoRA", qui a permis de fine-tuner des modèles de 65B paramètres sur un seul GPU. Cette prouesse repose sur deux innovations majeures détaillées ci-dessous:

### 1. Le type de données NF4 (Normalized Float 4-bit)
Regardez la **Figure 11-11 : Distribution des poids et blocs** . 

{{< bookfig src="274.png" week="11" >}}

Les chercheurs ont remarqué que les poids des réseaux de neurones suivent presque toujours une "Courbe de Gauss" (une cloche). La plupart des poids sont très proches de zéro.
> [!TIP]
>*   **L'astuce de la Figure 11-11** : Au lieu de créer des intervalles réguliers, on crée des intervalles plus "serrés" près de zéro et plus larges sur les côtés. On appelle cela le **Normal Float 4-bit (NF4)**. 

> [!NOTE]
> **Note technique** : NF4 construit ses niveaux à partir d’une distribution normale de référence. Les poids réels et leur normalisation ne correspondent pas nécessairement à cette distribution ; la reconstruction introduit une erreur.

> Cette représentation vise à adapter les niveaux de quantification à la distribution des poids.

### 2. La Quantification par blocs (Blockwise Quantization)
Regardez la **Figure 11-12 : Blocs de quantification** .

{{< bookfig src="273.png" week="11" >}}

La quantification peut être appliquée à des blocs de poids, par exemple des blocs de 64 valeurs.
*   **Pourquoi ?** Si un bloc contient un poids aberrant (très grand), il n'aura d'impact que sur ses 63 voisins, et non sur les millions d'autres poids de la matrice. Cela permet de garder une précision locale très élevée.

### 3. La Double Quantification (Double Quantization)
C'est le sommet de l'économie de mémoire. Pour quantifier par blocs, on a besoin de stocker des "constantes de quantification" (des multiplicateurs). Ces constantes prennent elles-mêmes de la place. La double quantification consiste à... quantifier ces constantes ! 

> [!TIP]
On gagne encore environ 0,5 bit par paramètre. À l'échelle de milliards de paramètres, c'est crucial.

---
## Le concept de "Compute Dtype" : Le secret de la vitesse

> [!WARNING]
Ne confondez pas stockage et calcul. 

C'est un point technique que beaucoup d'étudiants ratent. 
*   Les poids du modèle sont stockés sur le disque et en VRAM en **4-bit** (pour gagner de la place).
*   Mais au moment où le modèle doit faire un calcul (une multiplication matricielle), il décompresse temporairement les nombres en **Float16** ou **BFloat16**. 

> [!IMPORTANT]
>*    **À retenir :** Le calcul se fait toujours en haute précision. 

> La quantification n'est qu'un mode de stockage ultra-compressé qui se "déplie" uniquement quand on en a besoin.

---
## Laboratoire de code : Charger un modèle en 4-bit avec BitsAndBytes
Voici comment implémenter cette technologie sur Colab. Nous allons utiliser la bibliothèque `bitsandbytes` pour charger un modèle de la famille Llama ou Phi en mode QLoRA.

```python
# Exemple prévu pour Colab T4 16GB VRAM
# !pip install transformers accelerate bitsandbytes

from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

# 1. CONFIGURATION DE LA QUANTIFICATION (Garde-fous de mémoire)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,              # Activation du mode 4-bit
    bnb_4bit_quant_type="nf4",      # Utilisation du Normal Float (Section 11.3)
    bnb_4bit_compute_dtype=torch.float16, # Précision pour les calculs (Compute Dtype)
    bnb_4bit_use_double_quant=True, # Gain de mémoire supplémentaire
    bnb_4bit_quant_storage=torch.uint8 # Type de stockage
)

# 2. CHARGEMENT DU MODÈLE
# On utilise device_map="auto" pour que Transformers gère la répartition sur le GPU
model_id = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)

# 3. VÉRIFICATION DE LA MÉMOIRE
mem = torch.cuda.memory_allocated() / 1024**3
print(f"Mémoire occupée sur le GPU : {mem:.2f} Go")
# Résultat attendu : Environ 2.3 Go pour Phi-3 (au lieu de ~8 Go en Float16)
```

> [!TIP]
**Conseil méthodologique** : La mémoire disponible après le chargement doit également accueillir les activations, les gradients et les états de l’optimiseur. Vérifiez sa consommation pendant l’entraînement.

---
## Paged Optimizers : Le filet de sécurité
Parfois, pendant l'entraînement, il y a des "pics" (spikes) de mémoire qui font planter le système (le fameux `CUDA Out of Memory`). 

QLoRA introduit les **Paged Optimizers**. 
L'idée est empruntée aux systèmes d'exploitation : si la VRAM du GPU est pleine, on déplace temporairement une partie des calculs vers la mémoire vive (RAM) de l'ordinateur. C'est un peu plus lent, mais cela empêche le crash. 

>  **C'est le gage de robustesse de votre pipeline.**

---
## Éthique et Responsabilité : L'IA sobre et accessible
> [!IMPORTANT]
la quantification est un acte d'écologie numérique. 
1.  **Réduction de l'empreinte carbone** : Faire tourner un modèle en 4-bit consomme moins d'énergie qu'en 16-bit. Multiplié par des millions d'utilisateurs, l'impact est massif. 
2.  **Démocratisation** : Sans quantification, le fine-tuning resterait le privilège des *GAFAM* (Google, Apple, Facebook(Meta), Amazon and Microsoft).
> En permettant l'entraînement sur des GPU "grand public" (comme ceux des gamers), nous permettons à des hôpitaux, des universités et des petites entreprises de posséder leur propre IA sans dépendre du cloud. 
3.  **Le risque de dégradation** : 
> [!IMPORTANT]
**À retenir :** une quantification trop agressive (ex: 2-bit) dégrade la logique du modèle. 

> Vous devez toujours tester si le modèle quantifié répond aussi intelligemment que l'original. L'économie de moyens ne doit pas se faire au détriment de la qualité de service pour l'humain.

> [!TIP]
**Synthèse** : La quantification réduit la mémoire nécessaire au stockage des paramètres. Ses effets sur la qualité des réponses et la vitesse d'exécution doivent être mesurés.

---
La prochaine section associe LoRA et la quantification dans un entraînement par instructions avec **QLoRA**.
