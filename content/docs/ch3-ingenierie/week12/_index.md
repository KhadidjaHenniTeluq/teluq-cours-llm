---
title: "Semaine 12 : Alignement et réglage par préférences"
weight: 2
bookCollapseSection : true
---


# Semaine 12 : Alignement et réglage par préférences

Comprendre comment des comparaisons de réponses orientent un modèle.

## Description générale

Comprendre comment des comparaisons de réponses orientent un modèle. Expliquer une paire de réponses préférée et rejetée. Comparer les composants de RLHF et de DPO et discuter leurs limites.

---
## Pré-requis importants
Pour bien saisir ces concepts, assurez-vous d'avoir compris :
1.  **Le Fine-tuning supervisé (Semaine 11)** : L'alignement commence toujours après une phase SFT réussie.
2.  **Les Log-Probabilités (Semaine 5)** : Comprendre comment le modèle score ses propres jetons.
3.  **L'intuition des fonctions de perte (Loss functions)** : Savoir comment on "pousse" un modèle vers un comportement souhaité.

**Ressources pour réviser les pré-requis :**
*    **Hugging Face Course** : [Introduction to Fine-tuning](https://huggingface.co/learn/nlp-course/chapter3/1) .
*    **StatQuest (YouTube)** : [Probability Distributions Explained](https://www.youtube.com/watch?v=oI3hZJqXJuc) .

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Hugging Face Blog** : [Illustrating Reinforcement Learning from Human Feedback (RLHF)](https://huggingface.co/blog/rlhf), Le guide visuel de référence pour comprendre le cycle Feedback -> Reward -> Policy.
*   **Hugging Face Blog** : [Fine-tune Llama 2 with DPO](https://huggingface.co/blog/dpo-trl), Une explication technique de pourquoi DPO est plus simple et efficace que le RLHF classique.
*   **Dave Bergmann (IBM)** : [LLM Alignment Explained](https://www.ibm.com/think/topics/llm-alignment), Une article profond sur l'alignement des LLMs.


### Vidéos recommandées
*    **Andrej Karpathy** : [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), (Regardez à partir de 13:00 pour la section sur l'alignement et le RLHF).
*    **Stanford Online** : [Guest lecture on DPO](https://www.youtube.com/watch?v=Q7rl8ovBWwQ), Une présentation détaillée sur le DPO.

### Outils et Frameworks
*   **TRL Documentation** : [Direct Preference Optimization (DPO)](https://huggingface.co/docs/trl/main/en/dpo_trainer), Guide pratique pour utiliser le DPOTrainer .


---
> [!TIP]
**Conseil méthodologique** : Dans l'alignement, le plus dur n'est pas le code, c'est la donnée. 

> [!WARNING]
**Attention :** si vos paires de préférences sont mal choisies, vous allez "brider" l'intelligence de votre modèle. 

> Un bon assistant doit être utile (*helpful*) mais aussi inoffensif (*harmless*). C'est cet équilibre fragile que nous allons apprendre à coder !

## Repères de lecture

**Prérequis à revoir :** Distinguer préentraînement, SFT et évaluation.

**À comprendre en premier :** Expliquer une paire de réponses préférée et rejetée. Comparer les composants de RLHF et de DPO et discuter leurs limites.

**À lire ensuite pour approfondir :** Dérivation de la perte DPO et optimisation PPO. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Un modèle qui satisfait un évaluateur répond-il nécessairement correctement ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Apprendre avec des paires de préférences]({{< relref "/docs/ch3-ingenierie/week12/section-12-3.md" >}})
