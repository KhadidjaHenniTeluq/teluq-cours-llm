---
title: "Conclusion"
weight: 6
---

# Conclusion du cours

Le cours a présenté les fondements des modèles de langage, leurs applications et les méthodes utilisées pour les adapter et les déployer. L’analyse d’un système doit relier son architecture, ses données, ses objectifs d’entraînement et ses conditions d’utilisation.

## Synthèse des apprentissages

Les premières semaines ont établi les notions de tokenisation, de représentation vectorielle et d’attention. Les applications ont ensuite mobilisé ces notions pour la recherche documentaire, le RAG et le traitement multimodal. Le dernier chapitre a porté sur l’adaptation, l’alignement et le déploiement.

Pour chaque méthode, il convient de préciser le problème traité, les hypothèses retenues et les limites observées. Une explication du fonctionnement doit être accompagnée d’une évaluation adaptée à la tâche.

## Préparation à l’examen final

Les consignes de l’examen restent la référence pour les modalités d’évaluation. Les questions suivantes permettent d’organiser la révision.

### 1. Justifier les compromis techniques

* Dans quelles conditions choisir un Bi-Encoder ou un Cross-Encoder ? Comparez la qualité des résultats et le coût de calcul (évaluation 2).
* Comment le rang de LoRA influence-t-il le nombre de paramètres entraînables et les ressources nécessaires (semaine 11) ?
* Quels effets la température et les méthodes d’échantillonnage ont-elles sur les réponses ? Pourquoi ne garantissent-elles pas leur exactitude (semaine 5) ?

### 2. Expliquer le traitement des données

Représentez les étapes et les échanges entre les composants des systèmes suivants :

* Le cycle **ReAct** : raisonnement, action et observation.
* L’architecture **FTI** : préparation des données (*Feature*), entraînement (*Training*) et inférence (*Inference*).
* Les blocs Transformer avec normalisation **Pre-Norm** ou **Post-Norm**.

### 3. Choisir et interpréter les mesures

* Que mesure le **MAP** dans un système de recherche ?
* Que permettent d’évaluer la **fidélité aux sources** (*Faithfulness*) et le score BLEU ? Quelles sont leurs limites respectives ?
* Comment une optimisation centrée sur un seul indicateur peut-elle dégrader d’autres propriétés du système ? Reliez votre réponse à la loi de Goodhart.

## Poursuivre les apprentissages

1. Reliez les bibliothèques aux opérations qu’elles réalisent : tokenisation, calcul des représentations, optimisation et génération.
2. Utilisez des implémentations comme **minGPT** pour examiner le code et vérifier votre compréhension des architectures.
3. Mesurez les effets des optimisations, notamment la quantification et les méthodes PEFT, sur la qualité, la mémoire et le temps d’exécution.

## Éthique et responsabilité

Les choix de données et de conception influencent les erreurs et les biais d’un système. Leur analyse doit tenir compte des personnes concernées et du contexte d’utilisation.

* Documentez les usages prévus, les résultats d’évaluation et les limites dans une fiche de modèle (*Model Card*).
* Examinez les risques associés aux réponses, aux données traitées et aux outils accessibles au système.
* Prévoyez un suivi après le déploiement et des mesures de correction adaptées aux erreurs observées.

Lorsque les mesures de protection sont insuffisantes, les risques identifiés peuvent justifier le report du déploiement.

## Pour conclure

Les deux projets de la semaine 15 permettent d’intégrer les notions étudiées. Appuyez vos choix sur des évaluations documentées et adaptez les méthodes aux contraintes de chaque application.

**Khadidja Henni**
