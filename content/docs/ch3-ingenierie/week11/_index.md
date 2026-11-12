---
title: "Semaine 11 : Fine-tuning supervisé de modèles génératifs"
weight: 1
bookCollapseSection : true
---

# Semaine 11 : Fine-tuning supervisé de modèles génératifs

Distinguer adaptation complète, LoRA et quantification.

## Description générale

Distinguer adaptation complète, LoRA et quantification. Calculer le nombre de paramètres de deux matrices LoRA. Distinguer format des poids, format de calcul et mémoire totale.

---
## Pré-requis importants
Pour maîtriser le fine-tuning supervisé, vous devez avoir révisé :
1.  **Le Fine-tuning de BERT (Semaine 4)** : Pour comprendre la logique de base de la mise à jour des poids.
2.  **Paramètres de génération (Semaine 5)** : Car un modèle mal réglé après fine-tuning reste imprévisible.
3.  **Bases du Gradient Descent** : L'intuition mathématique de la correction d'erreur.

**Ressources pour réviser les pré-requis :**
*    **Hugging Face Course** : [Fine-tuning a pretrained model](https://huggingface.co/learn/nlp-course/chapter3/1) .
*    **PyTorch Tutorials** : [What is torch.nn?](https://pytorch.org/tutorials/beginner/nn_tutorial.html), Pour l'intuition sur les couches et les paramètres.


---
## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Hugging Face Blog** : [PEFT: Parameter-Efficient Fine-Tuning](https://huggingface.co/blog/peft), Ce blog explique comment adapter de grands modèles avec des ressources limitées. Il présente notamment LoRA et les préfixes virtuels.
*   **ArXiv (Article LoRA)** : [LoRA: Low-Rank Adaptation of LLMs](https://arxiv.org/abs/2106.09685), L'article scientifique fondateur pour ceux qui veulent comprendre la décomposition matricielle mathématique.
*   **Hugging Face Blog** : [Making LLMs even more accessible (QLoRA)](https://huggingface.co/blog/4bit-transformers-bitsandbytes), Un guide technique sur la quantification 4-bit. Il montre comment charger des modèles massifs sur un seul GPU.
*   **Lightning AI** : [LoRA from scratch](https://lightning.ai/lightning-ai/studios/code-lora-from-scratch), Une implémentation pas à pas pour comprendre ce qui se passe réellement dans les couches de poids.

### Documentations et Outils
*   **TRL (Transformer Reinforcement Learning)** : [SFTTrainer Documentation](https://huggingface.co/docs/trl/sft_trainer), Le manuel d'utilisation de l'outil que nous utiliserons pour nos laboratoires.
*   **BitsAndBytes GitHub** : [Quantization Basics](https://github.com/bitsandbytes-foundation/bitsandbytes), Pour comprendre les types de données NF4 et l'optimisation GPU.

### Vidéos recommandées
*   **Krish Naik**: [Finetuning LLM](https://www.youtube.com/playlist?list=PLZoTAELRMXVN9VbAx5I2VvloTtYmlApe3) - Une playliste couvrant tous les concepts que vous allez voir cette semaine.
*   **Ai Engineer** : [RFT, DPO, SFT: Fine-tuning avec OpenAI, Ilan Bigio, OpenAI](https://www.youtube.com/watch?v=JfaLQqfXqPA) - Atelier complet couvrant toutes les formes de fine-tuning et de prompt engineering (SFT, DPO, RFT), l'optimisation de prompts et l'architecture d'agents.

---
> [!NOTE]
**Note** : Dans cette semaine, nous allons parler de "rang" et de "matrices". 

> [!WARNING]
**Attention :** ne vous perdez pas dans les équations. Retenez l'image : LoRA est comme un post-it intelligent que l'on colle sur un dictionnaire géant pour y ajouter de nouvelles définitions sans réécrire tout le livre !

## Repères de lecture

**Prérequis à revoir :** Revoir l’entraînement supervisé et les dimensions des matrices.

**À comprendre en premier :** Calculer le nombre de paramètres de deux matrices LoRA. Distinguer format des poids, format de calcul et mémoire totale.

**À lire ensuite pour approfondir :** NF4, paged optimizers et entraînement QLoRA complet. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Réduire les paramètres entraînables de moitié divise-t-il toute la mémoire par deux ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [LoRA et les matrices de faible rang]({{< relref "/docs/ch3-ingenierie/week11/section-11-2.md" >}})
- [Quantification et erreur d’arrondi]({{< relref "/docs/ch3-ingenierie/week11/section-11-3.md" >}})
