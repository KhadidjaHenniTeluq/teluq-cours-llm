---
title: "Chapitre 01 : Fondements des LLM"
weight: 1
bookCollapseSection: true
---

# Chapitre 1 : Fondements des modèles de langage

## Représentations et architectures (semaines 1 à 5)

Ce chapitre présente les notions et les méthodes décrites ci-dessous. Les activités permettent de les appliquer et d’en examiner les limites.

## Organisation du chapitre

* **Semaine 1 : Repères historiques** : méthodes de comptage, représentations distribuées et architectures séquentielles.
* **Semaine 2 : Tokenisation et embeddings** : segmentation du texte et représentation vectorielle des tokens.
* **Semaine 3 : Architecture Transformer** : attention, encodage positionnel et organisation des blocs.
* **Semaine 4 : Modèles de représentation** : BERT, classification et évaluation.
* **Semaine 5 : Modèles de génération** : GPT, décodage et limites des réponses générées.

## Progression des apprentissages

<div align="center">

```mermaid
graph TD
    W1[<b>Semaine 1 : Contexte</b><br/>Évolution des méthodes] --> W2[<b>Semaine 2 : Représentations</b><br/>Tokens & Embeddings]
    W2 --> W3[<b>Semaine 3 : Architecture</b><br/>Le Transformer & l'Attention]
    W3 --> W4[<b>Semaine 4 : Analyse</b><br/>L'Encodeur - BERT]
    W3 --> W5[<b>Semaine 5 : Génération</b><br/>Le Décodeur - GPT]
    
    style W3 fill:#f96,stroke:#333,stroke-width:4px
```

</div>

## Liens entre les notions

1. La tokenisation définit les unités d’entrée ; les embeddings leur associent des vecteurs.
2. L’attention combine ces vecteurs en tenant compte du contexte, tandis que l’encodage positionnel apporte l’information d’ordre.
3. Les architectures BERT et GPT illustrent des objectifs et des modes d’utilisation distincts du Transformer.

> [!IMPORTANT]
> Justifiez les choix techniques à partir des objectifs de la tâche et des résultats d’évaluation.
