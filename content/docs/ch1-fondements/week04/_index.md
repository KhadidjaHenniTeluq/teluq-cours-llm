---
title: "Semaine 4: Modèles de représentation (Encoder-only)"
weight: 4
bookCollapseSection: true
---


# Semaine 4 : Modèles de représentation (encoder-only)

Utiliser un encodeur pour représenter un texte et construire un classifieur.

## Description générale

Utiliser un encodeur pour représenter un texte et construire un classifieur. Expliquer le préentraînement par masquage de BERT. Interpréter une matrice de confusion, la précision et le rappel.

---
## Pré-requis importants
Pour maîtriser cette semaine, assurez-vous d'avoir bien intégré :
1.  **Le mécanisme d'Attention (Semaine 3)** : Comprendre comment les mots se donnent mutuellement du contexte.
2.  **La Tokenisation (Semaine 2)** : Savoir comment BERT découpe les mots complexes avec `##`.
3.  **Python & Scikit-learn** : Être à l'aise avec la notion de "classifieur" et de "matrice".

**Ressources pour réviser les pré-requis :**
*    **Hugging Face Course** : [The Transformer Hierarchy](https://huggingface.co/learn/nlp-course/chapter1/4) .
*    **Scikit-learn documentation** : [Supervised Learning Intro](https://scikit-learn.org/stable/supervised_learning.html) .

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Jay Alammar** : [A Visual Guide to Using BERT for the First Time](https://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/), Une merveille de pédagogie visuelle sur le passage du texte à la classification.
*   **Hugging Face Blog** : [BERT 101: State of the Art NLP](https://huggingface.co/blog/bert-101), Tout ce qu'il faut savoir sur l'architecture et les variantes.
*   **SBERT (Sentence-Transformers)** : [Documentation officielle](https://www.sbert.net/), L'outil standard pour transformer BERT en extracteur d'embeddings de phrases.

### Vidéos recommandées
*    **Stanford Online** : [BERT and Other Pre-trained Language Models](https://www.youtube.com/watch?v=knTc-NQSjKA) .
*    **CodeEmporium** : [BERT Explained](https://www.youtube.com/watch?v=xI0HHN5XKDo) .

---

> [!TIP]
**Conseil méthodologique** : BERT est un modèle de "représentation". ne lui demandez pas d'écrire une histoire, il n'est pas fait pour cela. 

> Utilisez-le pour transformer le chaos du langage en vecteurs organisés. C'est le socle de toute la recherche sémantique que nous verrons en Semaine 6 !

## Repères de lecture

**Prérequis à revoir :** Comprendre les embeddings et distinguer entraînement et test.

**À comprendre en premier :** Expliquer le préentraînement par masquage de BERT. Interpréter une matrice de confusion, la précision et le rappel.

**À lire ensuite pour approfondir :** Variantes de BERT et classification sans exemples étiquetés. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Pourquoi un bon score global peut-il masquer de mauvaises prédictions sur une classe rare ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [BERT et le token masqué]({{< relref "/docs/ch1-fondements/week04/section-4-1.md" >}})
