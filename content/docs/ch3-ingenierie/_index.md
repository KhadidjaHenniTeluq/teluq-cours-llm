---
title: "Chapitre 03 : Ingénierie des LLM"
weight: 3
bookCollapseSection: true
---

# Chapitre 3 : Ingénierie des modèles de langage

## Adaptation, déploiement et évaluation (semaines 11 à 14)

Ce chapitre présente les notions et les méthodes décrites ci-dessous. Les activités permettent de les appliquer et d’en examiner les limites.

## Organisation du chapitre

* **Semaine 11 : Adaptation** : fine-tuning supervisé, LoRA et quantification.
* **Semaine 12 : Alignement** : données de préférence, RLHF, DPO et évaluation.
* **Semaine 13 : Déploiement** : optimisation de l’inférence, sécurité et surveillance.
* **Semaine 14 : Synthèse et perspectives** : agents et architectures alternatives.

## Progression des apprentissages

<div align="center">

```mermaid
graph TD
    W11[<b>Semaine 11 : Expertise</b><br/>Spécialiser via LoRA] --> W12[<b>Semaine 12 : Alignement</b><br/>Aligner via DPO]
    W12 --> W13[<b>Semaine 13 : Déploiement</b><br/>Inférence & Sécurité]
    W13 --> W14[<b>Semaine 14 : Autonomie</b><br/>Agents & Architectures futures]
    
    style W13 fill:#f96,stroke:#333,stroke-width:4px
```
</div>

## Liens entre les notions

1. L’adaptation supervisée et l’apprentissage par préférences répondent à des objectifs complémentaires.
2. Le déploiement exige de mesurer la qualité, les ressources nécessaires et les risques du système.
3. Les agents associent un modèle à des outils et à une procédure d’exécution dont les limites doivent être définies.

> [!IMPORTANT]
> Justifiez les choix techniques à partir des objectifs de la tâche et des résultats d’évaluation.
