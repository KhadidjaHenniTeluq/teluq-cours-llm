---
title: "Projet 1 : Karpathy/minGPT "
weight: 1
bookCollapseSection: true
---

# Projet minGPT : lire une implémentation de GPT

Ce projet examine une implémentation compacte de GPT. Reliez le code du modèle, la boucle d’entraînement et la génération aux concepts du cours.

Dépôt étudié : [minGPT](https://github.com/karpathy/minGPT).

## Pourquoi avoir choisi minGPT ?

Dans notre parcours, nous avons souvent utilisé des bibliothèques de haut niveau comme `transformers` de Hugging Face. C'est excellent pour la production, mais ces outils cachent souvent la mécanique sous des milliers de lignes de code de gestion d'erreurs. 

**minGPT** est l'exact opposé : c'est une implémentation "nue". Andrej Karpathy  l'a écrit avec un seul objectif : **la clarté pédagogique**. 
*   **Minimalisme** : Tout est contenu dans un petit dossier `mingpt/`.
*   **Fidélité** : Il propose une implémentation pédagogique de la famille GPT étudiée en **Semaine 5**.
*   **Transparence** : Chaque ligne de code correspond à une équation que nous avons vue en **Semaine 3**.

## Structure du Projet : La Carte du Labyrinthe

Le dépôt est organisé de manière à ce qu'un étudiant puisse le parcourir en moins d'une heure. Voici comment les fichiers s'alignent avec les piliers de notre cours :

```mermaid
graph TD

    Project[<b>minGPT Repository</b>] --> Core[mingpt/ folder]

    Project --> Examples[root folder]

  

    Core --> M["<b>model.py</b><br/>Architecture & Attention<br/><i>(Semaines 2 & 3)</i>"]

    Core --> T["<b>trainer.py</b><br/>Boucle d'apprentissage<br/><i>(Semaines 11 & 13)</i>"]

    Core --> U[<b>utils.py</b><br/>Fonctions d'aide]

  

    Examples --> S["<b>play_shakespeare.ipynb</b><br/>Application créative<br/><i>(Semaine 5 & 8)</i>"]
```

1.  **`model.py`** : C'est le cœur du système. C'est ici que l'on trouve la définition des neurones, de la self-attention et de la structure du Transformer.
2.  **`trainer.py`** : C'est le moteur. Il gère l'optimisation, le calcul de la perte (loss) et la mise à jour des poids sur votre GPU T4.
3.  **Les scripts d'exemples** : Ils montrent comment "nourrir" ce cerveau avec du texte (Shakespeare, mathématiques) pour qu'il commence à générer du sens.


## L'Alignement avec notre cours
Tout au long de cette présentation, nous allons voir comment minGPT "donne vie" aux chapitres de notre livre de référence :
*   **La Géométrie (Fondements)** : Comment le code gère physiquement les matrices d'embeddings de la Section 2.4.
*   **La Dynamique (Science)** : Comment le mécanisme d'attention de la Section 3.1 est codé par une simple opération de multiplication matricielle (`@` en Python).
*   **La Rigueur (Ingénierie)** : Comment les techniques de régularisation et de normalisation de la Section 3.3 assurent que le modèle ne "devient pas fou" pendant l'entraînement.

> [!TIP]
**Présentation de la suite** : La **section 1** examine le fichier `model.py`, la conversion des tokens en vecteurs et le calcul de l'attention.

---

**Êtes-vous prêts à entrer dans le code source du miniGPT ?**