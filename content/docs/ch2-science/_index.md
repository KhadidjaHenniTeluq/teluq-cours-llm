---
title: "Chapitre 02 : Science des LLM"
weight: 2
bookCollapseSection: true
---

# Chapitre 2 : Applications des modèles de langage

## Recherche, génération et multimodalité (semaines 6 à 10)

Ce chapitre présente les notions et les méthodes décrites ci-dessous. Les activités permettent de les appliquer et d’en examiner les limites.

## Organisation du chapitre

* **Semaine 6 : Recherche sémantique** : représentations des documents, mesures de similarité et indexation.
* **Semaine 7 : Regroupement thématique** : réduction de dimension, clustering et BERTopic.
* **Semaine 8 : Formulation des consignes** : exemples, décomposition des tâches et contrôle des sorties.
* **Semaine 9 : RAG** : recherche documentaire, génération augmentée et évaluation.
* **Semaine 10 : Multimodalité** : représentations conjointes du texte et des images.

## Progression des apprentissages

<div align="center">

```mermaid
graph TD
    T1[<b>Exploration & Structure</b>]
    T2[<b>Interaction & Preuve</b>]

    subgraph " "
    W6[<b>Semaine 6 : Recherche</b><br/>Rechercher des documents] --> W7[<b>Semaine 7 : Clustering</b><br/>Grouper les thèmes]
    end
    
    subgraph " "
    W8[<b>Semaine 8 : Prompting</b><br/>Formulation des consignes] --> W9[<b>Semaine 9 : RAG</b><br/>Génération ancrée]
    end
    
    T1 --- W6
    T2 --- W9
    W7 --> W8
    W9 --> W10[<b>Semaine 10 : Multimodal</b><br/>Associer texte et image]
    
    style T1 fill:none,stroke:none
    style T2 fill:none,stroke:none
    style W9 fill:#f96,stroke:#333,stroke-width:4px
    linkStyle 2 stroke-width:0px
    linkStyle 3 stroke-width:0px
```
</div>

## Liens entre les notions

1. Les représentations vectorielles servent à la recherche documentaire et au regroupement thématique.
2. La formulation des consignes définit la tâche ; le RAG ajoute des informations récupérées dans les sources.
3. Les modèles multimodaux étendent l’analyse aux relations entre des données de types différents.

> [!IMPORTANT]
> Justifiez les choix techniques à partir des objectifs de la tâche et des résultats d’évaluation.
