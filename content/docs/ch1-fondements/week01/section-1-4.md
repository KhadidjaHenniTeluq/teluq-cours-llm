---
title: "1.4 Définition et applications des LLM"
weight: 5
---

## Définition et applications des LLM

Un grand modèle de langage (LLM) est un réseau entraîné sur de grandes quantités de données textuelles. Il apprend des régularités qui lui permettent notamment de prédire des tokens, de générer du texte ou de produire des représentations. Ses capacités dépendent des données, de l’architecture et de l’entraînement, et ne garantissent pas l’exactitude de ses réponses.

## Une définition mouvante : Qu'est-ce que "Large" ?
Il n’existe pas de seuil universel définissant un grand modèle de langage. BERT-base comporte 110 millions de paramètres ; Llama 3 existe notamment dans une version à 70 milliards. La taille exacte et les détails d’architecture de certains modèles propriétaires ne sont pas publiés : une estimation ne doit pas être présentée comme une donnée établie.

> [!NOTE]
**La distinction fondamentale :** La "largesse" ne se mesure pas qu'au nombre de neurones artificiels. Elle se définit par trois piliers :
1.  **Le volume de données** : Les corpus peuvent représenter des téraoctets de textes provenant de sources variées, notamment des pages web, des livres et du code.
2.  **La puissance de calcul** : Des milliers de GPU tournant pendant des mois.
3.  **L’émergence** : Certaines capacités deviennent observables lorsque la taille du modèle et les ressources d’entraînement augmentent. Leur mesure dépend des tâches et des critères d’évaluation retenus.

---
## La saga GPT : De la curiosité au séisme mondial
Pour comprendre où nous en sommes, nous devons suivre l'évolution de la lignée la plus célèbre, détaillée ci-dessous.

### 1. L'aube : GPT-1 et l'intuition du décodeur (Figure 1-20)

{{< bookfig src="28.png" week="01" >}}

**Explication** : GPT-1, sorti en 2018, ne possédait que 117 millions de paramètres. La figure montre une architecture "Decoder-only" simple. L'innovation ? C'était la preuve que l'on pouvait entraîner un modèle sans étiquettes humaines, simplement en lui demandant de prédire le mot suivant sur 7000 livres. C'était le passage de "l'IA de laboratoire" à "l'IA apprenante". 

### 2. La rupture : GPT-2 et le danger de la fluidité (Figure 1-21)

{{< bookfig src="29.png" week="01" >}}

**Explication** : En 2019, OpenAI passe à 1,5 milliard de paramètres. La figure illustre un saut d'échelle massif.

> [!NOTE]
**À retenir :** GPT-2 a été le premier modèle capable d'écrire des articles de presse si convaincants qu'OpenAI a d'abord refusé de le publier, craignant une vague massive de "Fake News". 

C'est là que la société a réalisé que l'IA pouvait désormais mimer la prose humaine à la perfection.

### 3. L'ère des géants : GPT-3 et le Zero-shot (Figure 1-21 suite)
Toujours sur la **Figure 1-21**, on voit l'explosion vers **175 milliards de paramètres** en 2020. 

> [!WARNING]
**Attention :** On pense souvent que GPT-3 est juste "plus fort". En réalité, il a introduit le **In-context learning**. 

On n'a plus besoin de ré-entraîner le modèle pour lui apprendre une tâche ; il suffit de lui donner deux ou trois exemples dans le prompt (Few-shot) ou même aucun (Zero-shot) pour qu'il comprenne.

### 4. La diffusion des assistants conversationnels : ChatGPT et GPT-4

{{< bookfig src="30.png" week="01" >}}

**Explication de la Figure 1-22** : Cette figure montre l'introduction de l' **Instruction Tuning**. On ne se contente plus de prédire le web ; on apprend au modèle à être un "assistant". 

{{< bookfig src="198.png" week="01" >}}

**Explication de la Figure 1-23** : On arrive à GPT-4, qui devient multimodal (il voit des images). C'est la fin du modèle purement textuel.

---
## Le paradigme de l'entraînement : La naissance d'un esprit numérique
voici le secret de fabrication que vous devez graver dans votre mémoire. Un LLM ne naît pas "intelligent", il le devient en deux étapes non-négociables.

### Étape 1 : Le Pré-entraînement (Pretraining) - L'éducation sauvage
C'est la phase "biblique" de l'IA. Le modèle lit tout ce qui est numérisé.
*   **Objectif** : Apprendre la structure du monde et du langage. 
*   **État final** : Le **Base Model** (ou Foundation Model). 

> [!IMPORTANT]
Un Base Model est un savant fou. 

> Si vous lui demandez "Quelle est la capitale de la France ?", il pourrait vous répondre "Et quelle est la capitale de l'Espagne ?" car il a appris que les listes de questions se suivent souvent. Il ne sait pas encore qu'il doit vous servir.

### Étape 2 : Le Réglage Fin (Fine-tuning) - L'école de la courtoisie
L’adaptation supervisée utilise un jeu de données plus restreint, composé d’exemples de dialogues ou de paires de consignes et de réponses de référence.
*   **SFT (Supervised Fine-Tuning)** : On lui montre des paires "Question -> Réponse idéale".
*   **RLHF (Reinforcement Learning from Human Feedback)** : On demande à des humains de noter ses réponses. L'IA apprend ce que nous préférons : la clarté, la politesse et la vérité.

---
## L'explosion de 2023 : La libération des modèles

{{< bookfig src="32.png" week="01" >}}

**Explication de la Figure 1-24** : Cette figure est sans doute la plus importante pour votre future carrière. Elle montre qu'en 2023, le monopole d'OpenAI s'est effondré. 
*   On voit l'arrivée de **Llama** (Meta), **Mistral**, **Falcon**.

> [!TIP]
**Le message de la figure** : Nous sommes passés de modèles fermés (Proprietary) à des modèles ouverts (Open Models) que vous pouvez faire tourner sur votre propre ordinateur. **C'est la démocratisation de la puissance de calcul**!

---
## Applications pratiques : Le couteau suisse universel
Pourquoi les entreprises s'arrachent-elles ces modèles ? Parce qu'un seul modèle peut remplacer dix logiciels différents.

**Tableau 1-2 : Panorama des applications industrielles des LLM**

| Domaine | Application Concrète | Ce que le LLM apporte |
| :--- | :--- | :--- |
| **Programmation** | Copilot, génération de fonctions | Gain de productivité de 40% pour les développeurs. |
| **Relation Client** | Chatbots de support niveau 1 | Réponse instantanée 24h/24 sans frustration. |
| **Droit & Finance** | Résumé de contrats de 200 pages | Extraction instantanée des clauses de risque. |
| **Médecine** | Aide au diagnostic, synthèse de dossiers | Analyse croisée de milliers de publications. |
| **Marketing** | Copywriting, création de slogans | Génération de 50 variantes en 3 secondes. |

---
## Éthique et Responsabilité : Les ombres du géant

> [!CAUTION]
Je ne serais pas une bonne enseignante si je ne vous montrais que le côté brillant de la médaille. Ces modèles sont des miroirs déformants de notre humanité.

Nous devons faire face à quatre défis éthiques majeurs :

1.  **Hallucinations** : Le modèle privilégie la fluidité sur la vérité. S'il ne connaît pas la réponse, sa nature statistique le pousse à inventer une réponse crédible. 
> [!IMPORTANT]
> **À retenir :** Ne faites jamais confiance à un LLM pour un fait médical ou juridique sans une source vérifiable (RAG, que nous verrons en Semaine 9).

2.  **Biais et Équité** : Si le web est sexiste ou raciste, le LLM le sera. Aligner un modèle est un combat permanent contre les préjugés enfouis dans les données.

3.  **Transparence** : Comment le modèle a-t-il pris sa décision ? Personne ne sait lire dans les 175 milliards de paramètres de GPT-3. C'est le problème de la "boîte noire".

4.  **Propriété Intellectuelle** : À qui appartiennent les données d'entraînement ? Les procès actuels entre artistes et entreprises d'IA vont redéfinir le droit d'auteur pour le siècle à venir.

---
## Limited Resources are All You Need : L'IA pour tous
Une note d'espoir pour conclure : *On n'a pas besoin d'être milliardaire pour utiliser ces technologies.*

> [!TIP]
**L'astuce de l'expert** : Grâce à la **Quantification** (réduire la précision des nombres) et au **PEFT** (modifier seulement 0,1% du modèle), vous pouvez adapter un modèle surpuissant sur une simple carte graphique T4 comme celle de notre laboratoire. L'intelligence est désormais un bien commun.

---
## Synthèse finale
> [!IMPORTANT]
Cette semaine relie les architectures récurrentes, le mécanisme d’attention et les étapes d’entraînement des modèles de langage.

L'analyse d'un modèle de langage doit tenir compte de son architecture, de ses données d'entraînement et des conditions de son utilisation. La qualité des réponses nécessite une évaluation adaptée à la tâche.

---
