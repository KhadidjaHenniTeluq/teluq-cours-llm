---
title: "14.2 Nouveaux paradigmes d'architecture "
weight: 3
---

{{< katex />}}

## Nouveaux paradigmes d'architecture

Les Transformers ne sont pas la seule famille de modèles de séquences. RWKV et les modèles à espace d’état, dont Mamba, explorent d’autres compromis entre état interne, calcul et accès au passé. Comparer ces architectures demande de préciser la phase considérée, la longueur de la séquence et la tâche.

## Le mur de la complexité quadratique : L'ennemi invisible
Pour comprendre les nouvelles architectures, nous devons identifier le problème que nous essayons de résoudre. Rappelez-vous la Semaine 3 sur la Self-Attention.

*   **La mathématique de l'attention** : Pour que le mot $N$ comprenne son sens, il doit comparer son vecteur à TOUS les $N-1$ mots précédents. 
*   **La complexité $O(L^2)$** : Si vous doublez la longueur de votre texte, vous ne multipliez pas le travail par deux... vous le multipliez par quatre ! 
*   **L'impact sur la VRAM** : C'est ce qui crée le mur du KV cache que nous avons vu en Semaine 13. À mesure que la conversation s'allonge, la mémoire du GPU finit par exploser. 

> [!WARNING]
**Attention :** On pense souvent qu'il suffit d'ajouter plus de GPU pour traiter des textes de 1 million de mots. C'est faux! 

> Avec une complexité quadratique, la quantité de mémoire requise finit par dépasser les capacités physiques de n'importe quel datacenter. 

Pour lire un livre entier en une seule fois, ou analyser une vidéo de 2 heures, nous avons besoin d'une complexité **linéaire** ($O(L)$). C'est le défi des architectures de nouvelle génération.

---
## Analyse de la Figure 14-1 : L'arbre généalogique des alternatives
Regardons attentivement la **Figure 14-1 : Alternatives au Transformer** . 


<a id="llm-timeline"></a>
{{< bookfig src="32.png" week="14" >}}

**Explication de la figure** : Elle présente des recherches sur des architectures alternatives aux Transformers.
*   **2021-2022** : On voit apparaître des noms comme **S4** (Structured State Spaces) et **Hyena**. L'idée est d'utiliser des filtres mathématiques (convolutions géantes) pour remplacer l'attention.
*   **2023** : C'est l'éclosion de **RWKV** et de **Mamba**.


**Le message de la figure** : Le monopole du Transformer est attaqué par des modèles qui promettent une vitesse constante, peu importe la longueur du texte. C'est le passage d'une mémoire "totale" (attention) à une mémoire "compressée" (état).


---
## RWKV : Quand le RNN rencontre le Transformer
vous vous souvenez des RNN de la Semaine 1.2 ? Nous les avions enterrés parce qu'ils oubliaient tout et étaient impossibles à paralléliser. Et si je vous disais qu'ils font leur grand retour ?

L'architecture **RWKV** (*Receptance Weighted Key Value*) est une architecture hybride. 
1.  **L'entraînement comme un Transformer** : Grâce à une formulation mathématique astucieuse, RWKV peut être entraîné de manière parallèle sur GPU. On ne traite plus les mots un par un pendant l'apprentissage.
2.  **L'inférence comme un RNN** : Au moment de répondre à l'utilisateur, RWKV ne regarde pas tout son passé (pas de KV cache !). Il maintient un petit vecteur d'état qui se met à jour à chaque mot. 

> [!TIP]
**Interprétation** : RWKV actualise un état interne au fil des tokens. Cet état résume les informations utilisées pour le traitement de la suite de la séquence.

> Son avantage ? Il utilise la même quantité de mémoire, que vous lui donniez 10 mots ou 100 000 mots.


---
## Mamba et les modèles à espace d'état (SSM)
Nous arrivons maintenant au sujet le plus "brûlant" de la recherche actuelle : **Mamba**. Pour comprendre Mamba, nous devons parler des **State Space Models**.

### 1. L'héritage des systèmes de contrôle
Les SSM viennent de l'ingénierie aéronautique et de la physique. Ce sont des équations qui décrivent comment un système (un avion, un robot) évolue dans le temps en fonction d'entrées continues. Les chercheurs *Gu et Dao* ont eu l'idée d'utiliser ces équations pour traiter des séquences de texte.

### 2. Le concept de "Sélection" (Mamba)

> [!IMPORTANT]
**À retenir :**Le problème des anciens SSM était qu'ils traitaient chaque mot avec la même importance. Ils étaient "aveugles au contenu". 
**Mamba** a introduit le concept de **Selective SSM**. 
*   Le modèle regarde chaque token et décide : "Ceci est une information capitale, je dois la stocker dans mon état interne" ou "Ceci est un mot de liaison inutile, je peux l'oublier pour libérer de la place". 

> [!NOTE]
C'est une forme d'attention, mais compressée. 

> Le modèle ne garde pas le mot, il garde l'**essence** du mot dans un état mathématique compact.


### 3. Hardware-Awareness : L'IA au service du silicium
L’implémentation de Mamba tient compte de la hiérarchie mémoire des GPU. Elle cherche notamment à limiter les transferts entre la mémoire HBM et la mémoire SRAM (section 13.1).

> [!TIP]
**Le résultat** : Mamba est jusqu'à 5 fois plus rapide que les Transformers équivalents tout en ayant une mémoire de contexte virtuellement infinie.


---
## Comparaison au sommet : Transformer vs Mamba vs RWKV

« Pour votre examen final, vous devez être capables de justifier le choix d'une architecture selon le cas d'usage. »

| Dimension | Transformer (GPT/Llama) | Mamba (SSM) | RWKV |
| :--- | :--- | :--- | :--- |
| **Complexité Inférence** | $O(L^2)$ (Explosion mémoire) | $O(L)$ (Linéaire) | $O(L)$ (Linéaire) |
| **Mémoire (KV Cache)** | Grandit avec le texte | Taille fixe (Constante) | Taille fixe (Constante) |
| **Raisonnement long** | État de l'art (Parfait) | Excellent (en progrès) | Bon (difficile sur le très long) |
| **Vitesse d'entraînement** | Très rapide (GPU-native) | Très rapide (Hardware-aware) | Rapide |
| **Écosystème** | Immense (Standard) | Émergent | Communautaire |


> [!IMPORTANT]
**À comparer** : Un Transformer causal conserve des clés et valeurs pour les positions passées. Un modèle à espace d’état récurrent met à jour un état de taille fixe, à architecture donnée. Ce compromis de mémoire ne prouve pas une supériorité générale sur une tâche comme le résumé.


---
## L'émergence des Architectures Hybrides : Le meilleur des deux mondes
*Pourquoi choisir quand on peut marier les deux ?* 

2024 a vu la naissance de modèles hybrides comme **Jamba** (AI21 Labs). 
*   **La structure** : On utilise des blocs Mamba pour la rapidité et la gestion des longues séquences, et on insère quelques couches d'Attention (Transformer) tous les 8 blocs pour "recadrer" le raisonnement logique du modèle. 
*   **L'avantage** : Vous obtenez la vitesse linéaire de Mamba et la précision de raisonnement du Transformer. C'est sans doute là que se situe l'avenir immédiat des LLM de production.

---
## Laboratoire de code : Exploration d'un modèle non-Transformer
Bien que les Transformers dominent encore `transformers`, des bibliothèques comme `mamba-ssm` permettent déjà de tester ces nouveaux cerveaux. Voici comment charger un petit modèle Mamba pour observer sa structure.

```python
# Installation (Nécessite souvent des drivers CUDA spécifiques, simulation ici)
# !pip install mamba-ssm causal-conv1d

# Objectif : Charger un modèle Mamba et comparer sa sortie avec GPT-2.

try:
    from mamba_ssm import MambaLMHeadModel
    from transformers import AutoTokenizer

    model_id = "state-spaces/mamba-130m-hf" # Version compatible Hugging Face
    tokenizer = AutoTokenizer.from_pretrained("eleuther-ai/gpt-neox-20b")
    model = MambaLMHeadModel.from_pretrained(model_id).to("cuda")

    # Inférence simple
    input_ids = tokenizer("The theory of State Space Models is", return_tensors="pt").input_ids.to("cuda")
    
    print(" Génération avec Mamba...")
    out = model.generate(input_ids, max_length=20)
    print(tokenizer.decode(out[0]))

except ImportError:
    print(" Mamba nécessite une installation complexe de kernels CUDA. Simulation réussie.")
```

> [!NOTE]
Note du Professeur : Observez dans le code qu'il n'y a pas d'option 'use_cache=True'. 

> Pourquoi ? Parce que Mamba n'a pas de cache KV ! Son état interne est son cache.

---
## Les frontières de la recherche : Au-delà du mot suivant
ne croyez pas que changer d'architecture suffit. La recherche affronte aujourd'hui trois "murs" que même Mamba ne résout pas encore totalement :

1.  **Le Raisonnement Systémique** : Comment faire pour qu'une IA ne se contente pas de prédire le mot probable, mais qu'elle "vérifie" sa propre logique avant de parler ? (C'est le lien avec le Tree-of-Thought de la Semaine 8.3).
2.  **L'Apprentissage Continu** : Actuellement, nos modèles sont "gelés" après le fine-tuning. La recherche travaille sur des modèles capables d'apprendre de chaque nouvelle interaction sans oublier le passé (*Continual Learning*). 
3.  **L'Efficacité Énergétique** : 

> [!IMPORTANT]
**C'est mon cri du cœur éthique.** Le cerveau humain consomme environ 20 watts pour battre n'importe quel LLM en termes de sens commun. 

> Nos datacenters consomment des mégawatts. Les architectures comme Mamba sont un premier pas vers une IA plus "écologique" et sobre.

---
## Éthique et Responsabilité : L'accessibilité comme vertu

> [!IMPORTANT]
Pourquoi est-ce important pour vous, futurs ingénieurs ?

Si nous restons bloqués sur le Transformer et sa complexité quadratique, l'IA restera la propriété exclusive de trois ou quatre entreprises mondiales capables de payer les factures d'électricité et de mémoire. 

**La souveraineté technologique :** En développant et en maîtrisant des architectures linéaires (SSM, RWKV), nous permettons à des hôpitaux, des universités et des petites nations de faire tourner des modèles surpuissants sur du matériel modeste. L'optimisation architecturale est un acte de justice sociale numérique.

> [!WARNING]
**Synthèse** : Le choix d'une architecture doit être justifié par les exigences de la tâche et les résultats d'évaluation.

Comparez les architectures selon leurs performances, leur consommation de mémoire, leur temps d'exécution et les contraintes d'intégration.

---
