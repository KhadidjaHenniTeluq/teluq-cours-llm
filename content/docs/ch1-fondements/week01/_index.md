---
title: "Semaine 1 : Introduction aux LLM et historique du NLP"
weight: 1
bookCollapseSection: true
---


# Semaine 1 : Introduction aux LLM et historique du NLP

Comparer un sac de mots, un embedding et un modèle de séquence.

## Description générale

Comparer un sac de mots, un embedding et un modèle de séquence. Identifier ce qu’un modèle apprend à partir de données. Distinguer représentation, entraînement et génération.

---
## Pré-requis importants
Pour bien démarrer ce cours, vous devriez être familiers avec :
1.  **Python intermédiaire** : Savoir manipuler des listes, des dictionnaires et des fonctions.
2.  **Bases de l'Apprentissage Automatique** : Comprendre ce qu'est un modèle, des données d'entraînement et une prédiction.
3.  **Calcul matriciel élémentaire** : Comprendre qu'un texte peut être représenté par une grille de chiffres.

**Ressources pour réviser les pré-requis :**
*    **Tutoriel Python** : [NLP Tutorial Python](https://www.youtube.com/playlist?list=PLeo1K3hjS3uuvuAXhYjV2lMEShq2UYSwX) .
*    **Cours Machine Learning (Google)** : [Introduction au ML](https://developers.google.com/machine-learning/crash-course/ml-intro?hl=fr) .

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Jay Alammar** : [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), L'explication visuelle la plus célèbre au monde pour comprendre l'attention.
*   **Jay Alammar** : [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/), Pour comprendre le passage du mot au vecteur dense.
*   **Hugging Face Course** : [Introduction to NLP and LLMs](https://huggingface.co/learn/nlp-course/chapter1/1), Une excellente mise en contexte des tâches de l'IA de langage.

### Vidéos recommandées
*    **Andrej Karpathy** : [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), Une conférence sur ce qu'est un LLM "sous le capot".
*    **StatQuest** : [Transformer Architecture Explained](https://www.youtube.com/watch?v=zxQyTK8quyY), Une décomposition pas à pas du mécanisme.

---

> [!TIP]
 **Conseil méthodologique** : Ne vous laissez pas intimider par la complexité mathématique des Transformers dès le premier jour. Concentrez-vous sur l'**intuition** : pourquoi le modèle a-t-il besoin de "regarder" plusieurs mots à la fois ? 

> [!WARNING]
 **Attention :** si vous comprenez le problème du goulot d'étranglement des RNN, vous avez déjà fait 50% du chemin !

## Repères de lecture

**Prérequis à revoir :** Lire une liste Python et reconnaître un vecteur.

**À comprendre en premier :** Identifier ce qu’un modèle apprend à partir de données. Distinguer représentation, entraînement et génération.

**À lire ensuite pour approfondir :** Équations des RNN et détails historiques. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Pourquoi un sac de mots ne distingue-t-il pas deux phrases dont les mots sont réordonnés ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [RNN et mémoire séquentielle]({{< relref "/docs/ch1-fondements/week01/section-1-2.md" >}})
