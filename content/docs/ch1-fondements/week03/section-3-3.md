---
title: "3.3 Blocs Transformer et optimisation"
weight: 4
---

{{< katex />}}

## Blocs Transformer et optimisation

Un bloc Transformer associe une couche d’attention et un réseau appliqué à chaque position. Des connexions résiduelles et des normalisations facilitent l’entraînement. Il est utile de comprendre ce trajet principal avant d’étudier les variantes qui réduisent le coût du calcul ou de la mémoire.

## 1. L'architecture du bloc original
Commençons par regarder les plans de la machine d'origine, telle qu'imaginée en 2017. Regardez la **Figure 3-10 : Un bloc Transformer de l'article original** .

<a id="fig-3-10"></a>

{{< bookfig src="82.png" week="03" >}}

** Explication** : Cette illustration nous présente une unité de traitement composée de 2 "étages" superposés.
1.  **L'étage inférieur (Communication)** : C'est la couche de Multi-Head Attention. C'est ici que les mots "se parlent".
2.  **L'étage supérieur (Réflexion)** : C'est la couche Feedforward (FFN). C'est ici que chaque mot "réfléchit" individuellement sur les informations qu'il vient de récolter.
3.  **Les flèches pointillées (Residual Connections)** : Notez ces lignes qui contournent les blocs. Elles sont le secret de la survie du signal.
4.  **Les boîtes "Add & Norm"** : Elles agissent comme des douanes qui régulent le flux pour éviter que les nombres ne deviennent trop grands ou trop petits.

> [!TIP]
**Interprétation:** Imaginez que le bloc Transformer soit une réunion de travail. 

> La Self-attention, c'est le moment du débat où tout le monde échange des idées. Le Feedforward, c'est le moment où chaque participant retourne à son bureau pour rédiger sa propre synthèse de la réunion. Sans le débat, personne n'apprend rien de neuf. Sans le travail individuel, on n'aboutit à aucune décision concrète.

---
## 2. Les connexions résiduelles : L'autoroute du gradient

> [!WARNING]
**Attention :** On pourrait croire que plus on empile de couches, plus le modèle est intelligent. 

> En réalité, sans les connexions résiduelles (les "Skip Connections"), un modèle de 12 couches serait incapable d'apprendre.

** Pourquoi sont-elles vitales ?**
Rappelez-vous le problème de la disparition du gradient (Semaine 1.2). À chaque fois que l'information traverse une couche complexe comme l'attention, le signal s'affaiblit. 

> [!NOTE]
**La solution mathématique** : Au lieu de calculer $y = f(x)$, on calcule $y = x + f(x)$. On ajoute l'entrée originale au résultat du calcul.
*   **L'effet autoroute** : Pendant l'entraînement, le signal d'erreur peut "sauter" par-dessus les couches complexes via ces connexions directes pour atteindre les premières couches du modèle. C'est ce qui permet d'entraîner des modèles de 100 couches ou plus (comme GPT-4) sans que le cerveau de l'IA ne devienne amnésique.

---
## 3. La Normalisation : Garder la raison dans les nombres
Dans un réseau de neurones, si les nombres deviennent trop grands, la machine "explose" (overflow). S'ils deviennent trop petits, elle "s'éteint" (underflow). 

La normalisation est le thermostat qui maintient tout à une température stable.

### LayerNorm vs RMSNorm
Historiquement, nous utilisions la **LayerNorm**. Elle recalcule la moyenne et la variance de toutes les activations pour les ramener vers une **distribution standard** (moyenne 0, écart-type 1).

<a id="fig-3-11"></a>

**L'évolution moderne** : Regardez la **Figure 3-11 : Bloc Transformer d'un modèle de l'ère 2024** . Vous remarquerez que l'on utilise désormais la **RMSNorm** (*Root Mean Square Layer Normalization*).

{{< bookfig src="83.png" week="03" >}}

*   **La différence** : La RMSNorm ne calcule pas la moyenne, seulement la racine carrée de la moyenne des carrés. 
*   **L'avantage** : Elle est environ 40 % plus rapide à calculer sur GPU et offre la même stabilité. C'est pour cela que **Llama 3** et **Phi-3** l'utilisent exclusivement.


### Pre-Normalization vs Post-Normalization
Observez bien la position de la boîte "Normalize" entre la Figure 3-10 et la 3-11.
*   **Original (Post-Norm)** : On normalise *après* l'addition. C'est instable au début de l'entraînement.
*   **Moderne (Pre-Norm)** : On normalise *avant* d'entrer dans l'attention ou le feedforward. 

> [!IMPORTANT]
**À retenir :** La Pre-Norm est ce qui permet de lancer des entraînements massifs sans que le modèle ne diverge de manière catastrophique dans les premières heures. C'est le standard industriel actuel.

---
## 4. Le réseau Feedforward (FFN) : La digestion sémantique
Après que l'attention a mélangé les informations des mots, chaque token passe par un réseau de neurones dense identique.

> [!NOTE]
**Note technique** : Ce réseau augmente généralement la dimensionnalité (ex: de 768 à 3072) pour permettre au modèle de projeter le texte dans un espace beaucoup plus vaste, avant de le re-compresser. 

C'est ici que le modèle stocke ses "faits" (ex: "La capitale de la France est Paris"). Si l'attention est le système de communication, le FFN est la base de données de connaissances mémorisées (Figure 3-12).

{{< bookfig src="66.png" week="03" >}}


---
## 5. Optimiser l'attention : La course vers la vitesse
nous arrivons au défi majeur de l'ingénieur système : la gestion de la mémoire vive (VRAM). Vous avez compris que l'Attention est le cœur du Transformer, mais c'est aussi son "talon d'Achille". 

Mathématiquement, l'attention est gourmande : si vous multipliez par deux la longueur de votre texte, vous multipliez par quatre le besoin en calcul et en mémoire. 

Pour que l'IA ne devienne pas un gouffre énergétique réservé aux supercalculateurs, nous avons inventé des stratégies de "compression de regard". Décortiquons ensemble ces optimisations à travers les sections suivantes .

### 5.1 L'Attention Locale et Éparse
L'idée est simple : un mot a-t-il vraiment besoin de regarder TOUS les autres mots d'un livre pour comprendre son sens immédiat ? Probablement pas.

Regardons la **Figure 3-13 : L'attention locale** .

{{< bookfig src="75.png" week="03" >}}

*   **Analyse** : On y voit une fenêtre coulissante. Au lieu de laisser le modèle regarder toute la séquence (Global Attention), on le force à ne regarder que ses voisins immédiats (Local Attention). 

> [!TIP]
**Interprétation** : C'est comme lire avec un cache qui ne laisse voir que les 5 mots avant et les 5 mots après. 

> C'est foudroyant de rapidité, mais on perd la vision d'ensemble. C'est pour cela que des modèles comme GPT-3 alternent entre des couches "locales" et des couches "globales".


La **Figure 3-14 : Comparaison des motifs d'attention** va plus loin en montrant trois grilles :

{{< bookfig src="76.png" week="03" >}}

1.  **Transformer classique** : Une grille pleine (chaque token voit tout).
2.  **Sparse Transformer (Strided)** : Le modèle regarde par "sauts" (un mot sur deux ou trois).
3.  **Sparse Transformer (Fixed)** : Le modèle regarde des blocs fixes.

> [!NOTE]
**Notez bien la Figure 3-15 : Légende de la matrice** : Elle nous explique le code couleur de ces schémas. 

{{< bookfig src="77.png" week="03" >}}

Le carré bleu foncé est le token que la machine est en train de "prononcer", et les carrés bleu clair sont les souvenirs qu'elle a le droit de consulter. Plus il y a de bleu clair, plus la mémoire est riche, mais plus le GPU chauffe !


### 5.2 Optimiser la mémoire des têtes
> [!TIP]
Cette optimisation réduit les transferts de données. 

Dans l’attention multi-tête (MHA), chaque tête possède ses propres projections Query, Key et Value. Le stockage des clés et des valeurs dans le cache KV peut représenter une part importante de la mémoire utilisée.

La **Figure 3-16 : Comparaison MHA, MQA et GQA** est le panorama de cette évolution.

{{< bookfig src="78.png" week="03" >}}

*   **MHA (Multi-Head Attention)**, détaillée en **Figure 3-17** : C'est le luxe total. Chaque tête de Query a sa propre paire Key/Value. C'est très précis mais cela sature la VRAM.

{{< bookfig src="79.png" week="03" >}}

*   **MQA (Multi-Query Attention)**, illustrée en **Figure 3-18** : C'est la solution radicale. Toutes les têtes de Query se partagent une SEULE paire Key/Value.
> [!WARNING]
**Avertissement** : C'est ultra-léger, mais le modèle devient un peu "étourdi" car il mélange toutes les informations dans le même entonnoir.

{{< bookfig src="80.png" week="03" >}}


**Le compromis GQA (Grouped-Query Attention)**.
Regardez la **Figure 3-19 : Grouped-Query Attention** . C'est l'architecture utilisée par **Llama 3**.

{{< bookfig src="81.png" week="03" >}}

*   **Analyse** : On divise les têtes en groupes (ex: des groupes de 4). Au sein d'un groupe, les 4 Queries partagent la même paire Key/Value. 
*   **Le bénéfice** : On garde la finesse du regard (plusieurs groupes) tout en divisant par 4 ou 8 la taille de la mémoire nécessaire pour le cache. C'est ce qui permet d'avoir des conversations de 32 000 mots sur un seul GPU.


### 5.3 FlashAttention : L'IA au service du matériel
Enfin, nous ne pouvons pas parler de vitesse sans citer **FlashAttention**. 
> [!IMPORTANT]
**À retenir :** ce n'est pas un changement mathématique, c'est un changement logistique.

*   **Le problème** : Le GPU perd un temps fou à déplacer les données entre sa mémoire lente (HBM) et son cerveau rapide (SRAM).
*   **La solution** : FlashAttention réécrit l'algorithme d'attention pour que tout le calcul d'un bloc se fasse "d'une traite" dans la mémoire rapide. 
*   **L'impact** : On multiplie par 3 la vitesse sans changer l'intelligence du modèle. C'est l'optimisation la plus élégante de ces trois dernières années.


---
## Tableau 3-1 : Comparaison des architectures d'attention

| Méthode | Mémoire (KV Cache) | Performance Sémantique | Utilisé par... |
| :--- | :--- | :--- | :--- |
| **Multi-Head Attention** | Maximale (Lourd) | Étalon-or | GPT-3, BERT |
| **Multi-Query Attention** | Minimale (Léger) | Moyenne | PaLM |
| **Grouped-Query (GQA)** | **Optimisée** | **Excellente** | **Llama 3, Mistral** |

---
## Laboratoire de code : Inspecter la structure d'un bloc Transformer
***Ne me croyez pas sur parole, ouvrez la machine !*** 

Voici comment explorer les entrailles d'un modèle moderne comme Phi-3 pour y retrouver nos composants.

```python
# Exemple prévu pour Colab T4 16GB VRAM
# !pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoConfig

# 1. Chargement de la configuration d'un modèle moderne
model_id = "microsoft/Phi-3-mini-4k-instruct"
config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)

# 2. ANALYSE DES HYPERPARAMÈTRES DU BLOC
print(f"--- STRUCTURE DU BLOC {model_id} ---")
print(f"Nombre de couches (Blocs) : {config.num_hidden_layers}")
print(f"Dimension du modèle (d_model) : {config.hidden_size}")
print(f"Nombre de têtes d'attention : {config.num_attention_heads}")
print(f"Type de fonction d'activation : {config.hidden_act}") # Souvent 'silu' pour SwiGLU

# 3. VÉRIFICATION DU GQA
# Si num_key_value_heads < num_attention_heads, c'est du GQA !
if hasattr(config, "num_key_value_heads"):
    print(f"Têtes Key/Value (GQA) : {config.num_key_value_heads}")
    ratio = config.num_attention_heads // config.num_key_value_heads
    print(f"Facteur de compression GQA : {ratio}:1")

```

> [!IMPORTANT]
Observez le "Facteur de compression GQA". 

> Si vous voyez un ratio de 4:1, cela signifie que vous économisez 75 % de la mémoire nécessaire pour stocker le contexte par rapport à un Transformer classique. C'est la différence entre pouvoir discuter 10 minutes avec l'IA ou seulement 2 minutes. 

> ** C'est une distinction non-négociable pour vos futurs déploiements.**

---
## Éthique et Responsabilité : L'IA énergivore

> [!CAUTION]
l'optimisation n'est pas qu'une question de vitesse, c'est une question d'éthique.

Chaque bloc Transformer que nous empilons demande des milliards d'opérations. 
1.  **L'impact environnemental** : La course au "plus gros modèle" a un coût carbone colossal. En maîtrisant FlashAttention ou GQA, vous apprenez à être des ingénieurs sobres : obtenir la même intelligence avec moins de kilowatts. 
2.  **L'accessibilité** : Si nous ne développions pas ces optimisations, l'IA resterait le privilège exclusif de trois ou quatre entreprises milliardaires. Un modèle optimisé est un modèle qui peut tourner dans un hôpital de campagne ou sur le smartphone d'un étudiant. 

> ** L'ingénierie est un acte de démocratisation.**

> [!TIP]
**Synthèse** : Un bloc Transformer combine plusieurs opérations complémentaires.

> Les connexions résiduelles facilitent la propagation de l'information, la normalisation stabilise les calculs, l'attention combine les représentations et le réseau FFN applique une transformation à chaque position.

---
