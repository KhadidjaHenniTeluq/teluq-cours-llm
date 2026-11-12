---
title: "Semaine 7 : Clustering et Modélisation de sujets"
weight: 2
bookCollapseSection : true
---

# Semaine 7 : Clustering et modélisation de sujets

Interpréter les étapes d’un pipeline de clustering et de BERTopic.

## Description générale

Interpréter les étapes d’un pipeline de clustering et de BERTopic. Distinguer regroupement de documents et description des groupes. Examiner les documents représentatifs et les points hors groupe.

## Pré-requis importants
Pour réussir cette semaine, assurez-vous de maîtriser :
1.  **Manipulation de vecteurs (Semaine 6)** : Savoir transformer du texte en embeddings.
2.  **Pandas & Dataframes** : Être capable de manipuler des colonnes de texte et de labels.
3.  **Statistiques de base** : Comprendre la notion de distribution de mots.

**Ressources pour réviser les pré-requis :**
*    **Documentation Pandas** : [Introduction to DataFrames](https://pandas.pydata.org/docs/user_guide/dsintro.html).
*    **Scikit-learn** : [Introduction aux k-means](https://scikit-learn.org/stable/modules/clustering.html#k-means) (Pour comprendre la différence avec HDBSCAN).
*    **TensorFlow Projector** : [Visualiser les embeddings en 3D](https://projector.tensorflow.org/) (Outil interactif pour explorer les représentations).

---

## Ressources utiles pour les concepts de la semaine

### Documentations et Articles de référence
*   **Documentation Officielle de BERTopic** : [maartengr.github.io/BERTopic/](https://maartengr.github.io/BERTopic/), La bible du sujet, créée par Maarten Grootendorst.
*   **Guide UMAP** : [How UMAP Works](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html), Pour comprendre comment on passe de 768 dimensions à 2 ou 5 dimensions.
*   **Guide HDBSCAN** : [Understanding HDBSCAN](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html), Pourquoi c'est le meilleur choix pour les données textuelles bruitées.

### Tutoriels pratiques
*   **SBERT Clustering** : [K-Means vs Agglomerative](https://www.sbert.net/examples/applications/clustering/README.html), Des exemples de code simples pour débuter.
*   **Hugging Face** : [Topic Modeling with BERTopic](https://huggingface.co/blog/bertopic), Un guide d'implémentation rapide sur le hub.

### Vidéos recommandées
*    **Maarten Grootendorst** : [BERTopic for Topic Modeling](https://www.youtube.com/watch?v=uZxQz87lb84), Présentation claire et concise de BERTopic.

---

> [!TIP]
**Conseil méthodologique** : Dans cette semaine, vous allez voir des formes colorées apparaître sur vos écrans. Ne vous contentez pas de l'esthétique ! 

> [!WARNING]
**Attention :** un bon clustering est un clustering que vous pouvez expliquer. Demandez-vous toujours : "Pourquoi ces deux documents sont-ils dans le même groupe ?".

## Repères de lecture

**Prérequis à revoir :** Comprendre la représentation vectorielle de documents.

**À comprendre en premier :** Distinguer regroupement de documents et description des groupes. Examiner les documents représentatifs et les points hors groupe.

**À lire ensuite pour approfondir :** Paramètres de réduction de dimension et reclassement MMR. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Un groupe produit par un algorithme correspond-il forcément à une catégorie utile ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [BERTopic : des groupes aux sujets]({{< relref "/docs/ch2-science/week07/section-7-2.md" >}})
