---
title: "Semaine 3 : Architecture Transformer approfondie"
weight: 3
bookCollapseSection: true
---


# Semaine 3 : Architecture Transformer approfondie

Suivre le trajet des vecteurs dans une couche d’attention et un bloc Transformer.

## Description générale

Suivre le trajet des vecteurs dans une couche d’attention et un bloc Transformer. Calculer un petit softmax et expliquer le masque causal. Décrire le rôle de Q, K, V, des positions et des connexions résiduelles.

---
## Pré-requis importants
Pour maîtriser cette semaine complexe, vous devez avoir consolidé :
1.  **Algèbre Matricielle de base** : Comprendre qu'une multiplication de matrices est un moyen de projeter des données d'un espace à un autre.
2.  **Intuition des Embeddings (Semaine 2)** : Savoir que chaque mot est déjà représenté par un vecteur de nombres.
3.  **Softmax** : Comprendre que cette fonction transforme des scores bruts en probabilités (la somme de ces probabilités est égale à 1).

**Ressources pour réviser les pré-requis :**
*    **3Blue1Brown (YouTube)** : [Le calcul matriciel visuel](https://www.youtube.com/watch?v=fNk_zzaMoSs) .
*    **Hugging Face Course** : [The Transformer Architecture](https://huggingface.co/learn/nlp-course/chapter1/4) (Une introduction à l’architecture Transformer).

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Jay Alammar** : [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), L'explication visuelle la plus célèbre au monde pour comprendre les matrices Q, K, V.
*   **Lilian Weng (OpenAI)** : [Transformer Improvements](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/), Une excellente synthèse sur RoPE, SwiGLU et RMSNorm.
*   **Hugging Face Blog** : [FlashAttention, GQA, and more](https://huggingface.co/blog/optimize-llm), Pour comprendre comment on rend l'attention plus rapide sur GPU.


### Vidéos recommandées
*    **StatQuest** : [Transformer Neural Networks, Clearly Explained!!!](https://www.youtube.com/watch?v=zxQyTK8quyY), Une décomposition étape par étape, idéale pour ceux qui craignent les mathématiques complexes.
*    **CodeEmporium** : [Transformers Explained](https://www.youtube.com/watch?v=TQQlZhbC5ps), Une vision plus conceptuelle et historique de l'architecture.

---

> [!TIP]
**Conseil méthodologique** : Ne vous laissez pas intimider par les termes "Query" ou "Key". 

voyez cela comme une conversation dans une bibliothèque. Le Transformer pose des questions (Query), regarde les étiquettes des livres (Key) et extrait le savoir (Value). Si vous gardez cette image en tête, les équations deviendront vos amies !

## Repères de lecture

**Prérequis à revoir :** Calculer un produit scalaire et lire les dimensions d’une matrice.

**À comprendre en premier :** Calculer un petit softmax et expliquer le masque causal. Décrire le rôle de Q, K, V, des positions et des connexions résiduelles.

**À lire ensuite pour approfondir :** RoPE, GQA, FlashAttention et détails d’optimisation. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Après softmax, des scores de 1 et 0 donnent-ils des poids de 100 % et 0 % ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Comprendre les poids d’attention]({{< relref "/docs/ch1-fondements/week03/section-3-1.md" >}})
- [Visualiser le masque causal]({{< relref "/docs/ch1-fondements/week03/section-3-1.md" >}})
