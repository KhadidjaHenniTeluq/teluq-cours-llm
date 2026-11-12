---
title: "Semaine 6 : Recherche Sémantique et Embeddings Textuels"
weight: 1
bookCollapseSection : true
---

# Semaine 6 : Recherche Sémantique et Embeddings Textuels

Construire un petit moteur de recherche sémantique.

## Description générale

Construire un petit moteur de recherche sémantique. Découper des documents et encoder leurs passages. Évaluer les résultats obtenus sur quelques requêtes.

## Pré-requis importants
Pour profiter pleinement de cette semaine, vous devez être à l'aise avec :
1.  **Algèbre linéaire de base** : Comprendre ce qu'est un vecteur et un produit scalaire.
2.  **Manipulation de données en Python** : Savoir utiliser `NumPy` pour des opérations sur des tableaux de nombres.
3.  **Intuition des Embeddings (Semaine 2)** : Vous devez avoir compris que les mots sont des points dans un espace multidimensionnel.

**Ressources pour réviser les pré-requis :**
*    **Vidéo (3Blue1Brown)** : [L'essence de l'algèbre linéaire](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (Surtout les épisodes sur les vecteurs et le produit scalaire).
*    **Tutoriel (Khan Academy)** : [Introduction aux vecteurs](https://fr.khanacademy.org/math/linear-algebra/vectors-and-spaces).
*    **Documentation NumPy** : [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html).

---

## Ressources utiles pour les concepts de la semaine

### Blogs et Articles de référence
*   **Jay Alammar** : [Illustrating Word2Vec](https://jalammar.github.io/illustrated-word2vec/) (Indispensable pour l'intuition de la distance entre vecteurs).
*   **Hugging Face Blog** : [Introduction to Semantic Search](https://huggingface.co/blog/semantic-search), Un guide pratique complet.
*   **Pinecone Learning Center** : [Vector Similarity Explained](https://www.pinecone.io/learn/vector-similarity/), une comparaison visuelle de la similarité cosinus et de la distance euclidienne.

### Tutoriels et Bibliothèques
*   **SBERT (Sentence-Transformers)** : [Documentation officielle](https://www.sbert.net/), C'est l'outil que nous utiliserons pour créer nos embeddings de phrases.
*   **FAISS (Facebook AI Similarity Search)** : [Tutoriel GitHub](https://github.com/facebookresearch/faiss/wiki/Getting-started), Pour apprendre à indexer des millions de vecteurs.
*   **LangChain** : [Guide sur le Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/), Pour maîtriser l'art du *chunking*.

### Vidéos recommandées
*    **Nils Reimers (Créateur de SBERT)** : [Introduction to Embeddings and Retrieval](https://www.youtube.com/watch?v=Skj-d78j4YM), Une conférence technique de haut niveau sur la recherche sémantique dense et les embeddings.
*    **Shaw Talebi (AI Builder Academy)** : [How to improve LLMs with RAG](https://youtu.be/Ylz779Op9Pw?si=kiNWa7MfvgVrto-s) et [Text Embeddings, Classification, and Semantic Search (w/ Python Code)](https://youtu.be/sNa_uiqSlJo?si=PnBkKocMaa8poOzQ) expliquent une grande partie des concepts que nous allons voir cette semaine.
*    **CodeEmporium** : [Sentence Transformers - EXPLAINED](https://www.youtube.com/watch?v=O3xbVmpdJwU) Une explication très claire et concise des *sentence transformers*.
---

> [!TIP]
**Conseil méthodologique** : Ne vous laissez pas impressionner par les formules mathématiques de similarité. Concentrez-vous sur l'image mentale : deux phrases qui disent la même chose sont comme deux étoiles proches dans une galaxie. Notre travail est de trouver la règle pour mesurer leur proximité.

## Repères de lecture

**Prérequis à revoir :** Comprendre les embeddings et la similarité cosinus.

**À comprendre en premier :** Découper des documents et encoder leurs passages. Évaluer les résultats obtenus sur quelques requêtes.

**À lire ensuite pour approfondir :** Index approximatifs et adaptation d’un modèle d’embeddings. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Quelle information peut-on perdre en représentant un long document par un seul vecteur ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Du document aux passages pertinents]({{< relref "/docs/ch2-science/week06/section-6-3.md" >}})
