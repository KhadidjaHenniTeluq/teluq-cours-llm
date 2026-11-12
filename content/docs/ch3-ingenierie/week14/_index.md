---
title: "Semaine 14 : Synthèse et frontières de la recherche"
weight: 4
bookCollapseSection : true
---


# Semaine 14 : Synthèse et frontières de la recherche

Relier les notions du cours à un choix d’architecture argumenté.

## Description générale

Relier les notions du cours à un choix d’architecture argumenté. Décrire la boucle décision, outil, observation et arrêt d’un agent. Comparer un cache croissant à un état interne de taille fixe.

---
## Pré-requis importants
Pour cette synthèse, vous devez mobiliser l'ensemble des connaissances du semestre :
1.  **Mécanique de l'Attention (Semaine 3)** : Pour comprendre pourquoi les nouvelles architectures (Mamba) tentent de s'en passer.
2.  **RAG & Tool Use (Semaine 9)** : Fondamental pour comprendre comment un agent utilise une mémoire externe et des logiciels.
3.  **Prompt Engineering (Semaine 8)** : Pour maîtriser les techniques de planification (Chain-of-Thought).

**Ressources pour réviser les piliers :**
*    **Jay Alammar** : [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) .
*    **Hugging Face** : [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) (Pour voir l'état de l'art actuel).

---

## Ressources utiles pour les concepts du futur

### Articles et Blogs de recherche
*   **Lilian Weng (OpenAI)** : [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/), L'article de référence mondial sur la structure des agents .
*   **The Gradient** : [Mamba Explained](https://thegradient.pub/mamba-explained/), Une explication visuelle des State Space Models et pourquoi ils pourraient remplacer les Transformers .
*   **ReAct Project** : [Synergizing Reasoning and Acting](https://react-lm.github.io/), Site officiel de la technique de raisonnement par action .

### Vidéos recommandées 
*    **Maarten Grootendorst** : [Intuition behind Mamba and State Space Models](https://www.youtube.com/watch?v=BDTVVlUU1Ck), Une explication limpide sur le futur des architectures .
*    **DeepLearning.AI** : [LangChain for LLM Application Development](https://www.youtube.com/playlist?list=PL8r5Fx7qq8LQxJm0RtE4Zf4Qw5zxQvDOq), Cours gratuit sur la création d'IA qui utilisent des outils .

### Frameworks d'Avenir
*   **AutoGPT / BabyAGI** : [Autonomous Agents Overview](https://github.com/Significant-Gravitas/AutoGPT), Pour voir jusqu'où peut aller l'autonomie .

---

> [!TIP]
**Conseil méthodologique** : Dans ce domaine, la demi-vie d'une connaissance technique est de six mois. 

> [!WARNING]
**Point d'attention** : Reliez l'utilisation des bibliothèques aux principes mathématiques et aux hypothèses des modèles.

> La compréhension des représentations vectorielles et de l'attention facilite l'analyse des nouvelles architectures.

## Repères de lecture

**Prérequis à revoir :** Revoir attention, cache KV, RAG et évaluation.

**À comprendre en premier :** Décrire la boucle décision, outil, observation et arrêt d’un agent. Comparer un cache croissant à un état interne de taille fixe.

**À lire ensuite pour approfondir :** Mamba, RWKV, MoE et recherches sur les contextes longs. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Comment empêcher un agent de répéter indéfiniment une action qui échoue ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [La boucle d’un agent avec outils]({{< relref "/docs/ch3-ingenierie/week14/section-14-3.md" >}})
