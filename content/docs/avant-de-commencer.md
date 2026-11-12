---
title: "Avant de commencer"
weight: 0
---

# Avant de commencer

Ce cours aborde les LLM avec des exemples, des animations et du code. Il suppose des bases en Python et en apprentissage automatique. Si ces notions sont nouvelles, commencez par les rappels ci-dessous et les ressources de la semaine 1.

## Quatre outils à revoir

**Python.** Savoir lire une fonction, une boucle et une liste ; importer une bibliothèque ; exécuter un notebook dans l’ordre. Vous devez pouvoir expliquer ce que représente la sortie d’une cellule, même si la bibliothèque effectue le calcul.

**Vecteurs et matrices.** Un vecteur est une liste de nombres. Une matrice est un tableau de nombres. Si X contient 3 lignes et 4 colonnes et W contient 4 lignes et 2 colonnes, XW contient 3 lignes et 2 colonnes. Les dimensions communes, ici 4, doivent correspondre.

**Produit scalaire.** Pour u = [1, 2] et v = [3, 4], le produit scalaire vaut 1 × 3 + 2 × 4 = 11. Ce calcul intervient dans l’attention et dans certaines mesures de similarité.

**Probabilités et softmax.** Des scores ne sont pas encore des probabilités. Softmax([1, 0]) donne environ [0,731, 0,269] : les valeurs sont positives et leur somme vaut 1. Un score nul n’entraîne donc pas forcément une probabilité nulle.

## Apprendre et évaluer sont deux étapes différentes

Les données d’entraînement servent à modifier les paramètres. Un ensemble de validation aide à choisir les réglages. Le test sert à mesurer les résultats après ces choix. Si l’on règle le modèle sur les exemples de test, la mesure ne représente plus correctement sa capacité à traiter de nouvelles données.

## Quelques mots du cours

| Terme | Sens dans ce cours |
| --- | --- |
| Token | Unité de texte traitée par le modèle ; ce n’est pas toujours un mot entier. |
| Embedding | Vecteur qui représente un token, une phrase ou une autre entrée. |
| Paramètre ou poids | Valeur apprise pendant l’entraînement. |
| Activation | Valeur calculée pour une entrée donnée pendant le passage dans le réseau. |
| Logit | Score avant la transformation en probabilités. |
| Perte | Quantité utilisée pour mesurer l’erreur d’entraînement. |
| Gradient | Indication sur la variation de la perte par rapport aux paramètres. |
| Inférence | Utilisation d’un modèle pour calculer une sortie. |
| Fine-tuning | Adaptation d’un modèle préentraîné avec de nouveaux exemples. |
| Contexte | Informations fournies au modèle lors d’un appel. |

## Un ordre de travail conseillé

1. Lire l’introduction et les repères de la semaine.
2. Regarder l’animation, puis expliquer le schéma avec ses propres mots.
3. Lire les sections et refaire les petits calculs.
4. Exécuter le laboratoire, puis modifier un paramètre et comparer les résultats.
5. Faire le quiz et revenir aux notions qui posent problème.

Les repères « à comprendre en premier » et « pour approfondir » indiquent un ordre de lecture. Ils ne modifient pas les consignes ni le barème des évaluations.

## Ressources informatiques

Les exemples visent souvent Google Colab avec un GPU T4. La disponibilité du matériel, les quotas et la compatibilité des bibliothèques peuvent varier. Certains exercices utilisent un service externe nécessitant une clé et pouvant entraîner des coûts : vérifiez les consignes avant de les exécuter. Utilisez des données fictives ou autorisées.

Les exemples de code sont des supports d’apprentissage. Leur environnement doit être vérifié avant la séance, notamment les versions des bibliothèques, les téléchargements de modèles et les besoins en mémoire.
