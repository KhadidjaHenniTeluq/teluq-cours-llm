---
title: "Semaine 2 : Tokens, tokeniseurs et embeddings"
weight: 2
bookCollapseSection: true
---


# Semaine 2 : Tokens, tokeniseurs et embeddings

Suivre le passage du texte aux tokens, puis aux embeddings.

## Description générale

Suivre le passage du texte aux tokens, puis aux embeddings. Comparer le découpage de deux tokeniseurs. Distinguer identifiant, embedding statique et représentation contextuelle.

## Pré-requis importants
Pour maîtriser cette semaine, vous devez être à l'aise avec :
1.  **Manipulation de chaînes en Python** : Utilisation des méthodes `.split()`, `.replace()` et des expressions régulières.
2.  **Intuition géométrique** : Comprendre qu'un point dans un espace peut être défini par plusieurs coordonnées.
3.  **Bases de l'Apprentissage Automatique** : La notion de "poids" (weights) que l'on ajuste pour minimiser une erreur.

**Ressources pour réviser les pré-requis :**
*    **Documentation Python** : [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) .
*    **Khan Academy** : [Points dans l'espace 3D](https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/visualizing-scalar-valued-functions/v/representing-points-in-3d) - Pour l'intuition des dimensions .

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Hugging Face Documentation** : [Summary of the Tokenizers](https://huggingface.co/docs/transformers/tokenizer_summary), Le guide ultime pour comparer BPE, WordPiece et SentencePiece.
*   **Jay Alammar** : [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/), Une explication visuelle sur la création des vecteurs de sens.
*   **Hugging Face Course (Chapter 2)** : [Tokenizers](https://huggingface.co/learn/nlp-course/chapter2/4), Exercices interactifs sur le fonctionnement des bibliothèques modernes.

### Vidéos recommandées
*    **Computerphile** : [Word Embeddings & Word2Vec](https://www.youtube.com/watch?v=gQddtTdmG_8), Une introduction claire à la raison pour laquelle nous utilisons des vecteurs.
*    **DataMListic** : [What is a Tokenizer?](https://www.youtube.com/watch?v=hL4ZnAWSyuU), Vidéo courte et pédagogique sur la tokenisation.

### Outils interactifs
*   **OpenAI Tokenizer Tool** : [Tokenizer Playground](https://platform.openai.com/tokenizer), Visualisez en temps réel comment GPT découpe vos phrases.


---
> [!TIP]
**Conseil méthodologique** : Ne négligez pas la tokenisation en vous disant que c'est du "nettoyage". 

> [!WARNING]
**Attention** : Le choix du tokeniseur influence la représentation des langues et des nombres. Vérifiez son comportement sur les données du domaine étudié.

## Repères de lecture

**Prérequis à revoir :** Manipuler des chaînes et des listes en Python.

**À comprendre en premier :** Comparer le découpage de deux tokeniseurs. Distinguer identifiant, embedding statique et représentation contextuelle.

**À lire ensuite pour approfondir :** Comparaison exhaustive des vocabulaires et analyse géométrique. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Pourquoi deux identifiants proches ne désignent-ils pas nécessairement des tokens de sens proche ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Du texte aux tokens]({{< relref "/docs/ch1-fondements/week02/section-2-1.md" >}})
- [Embeddings et similarité cosinus]({{< relref "/docs/ch1-fondements/week02/section-2-4.md" >}})
