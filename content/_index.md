---
title: "Accueil"
layout: "page"
---

# SCI1040 : Les grands modèles de langage (LLM)

## Comprendre, utiliser et concevoir des systèmes fondés sur les LLM

Bonjour à toutes et à tous,

Le cours **SCI1040 : Les grands modèles de langage (LLM)** présente les fondements, les méthodes et les applications des modèles de langage, notamment la génération, le résumé et la traduction de textes.

Les LLM ne sont pas seulement des outils conversationnels. Ils reposent sur des concepts scientifiques, des architectures profondes, des méthodes d’entraînement avancées et des choix d’ingénierie qui transforment déjà plusieurs secteurs : l’éducation, la recherche, la programmation, la santé, les services numériques et les entreprises.

Dans ce cours, nous allons apprendre à comprendre ces modèles, à les utiliser de manière rigoureuse et à concevoir des applications concrètes fondées sur les technologies actuelles de l’IA générative.

---

## Pour commencer

Consultez les [rappels de Python, de calcul vectoriel et de probabilités]({{< relref "/docs/avant-de-commencer.md" >}}). Chaque semaine propose un ordre de lecture pour aborder les notions essentielles avant les détails avancés.

## La philosophie du cours : l’intuition d’abord

Dans ce cours, nous suivons une approche fondée sur **l’intuition avant la formalisation**. Le domaine des LLM évolue très rapidement, et il peut devenir difficile de tout mémoriser si l’on commence uniquement par les détails techniques.

L’objectif est donc de construire d’abord des images mentales solides. Nous allons comprendre les grandes idées avant d’entrer progressivement dans les équations, les architectures, le code et les choix d’implémentation.

**Notez que** : nous n’allons pas nous noyer dans les détails mathématiques dès le départ. Nous allons avancer étape par étape, en reliant chaque notion à une intuition simple, à un exemple concret et à une application pratique.

---

## La structure du cours : trois grands piliers

Le cours est structuré autour de trois grands piliers que nous explorerons pendant 15 semaines.

1. **Les fondements des LLM**

    Nous commencerons par les notions de base nécessaires pour comprendre les modèles de langage modernes : les tokens, les embeddings, les représentations vectorielles, les mécanismes d’attention et l’architecture Transformer.

2. **La science des LLM**

    Nous étudierons ensuite les méthodes qui permettent aux LLM d’interagir avec des données, des documents et des contextes complexes. Cette partie abordera notamment la recherche sémantique, le **RAG** (*Retrieval-Augmented Generation*), l’évaluation des modèles et la multimodalité.

3. **L’ingénierie des LLM**

    Enfin, nous verrons comment adapter, aligner et déployer des systèmes fondés sur les LLM. Cette partie couvrira le **fine-tuning**, les approches d’alignement, les agents, les garde-fous, ainsi que les enjeux liés au déploiement en production.

---

## Conseils pour réussir le cours

> [!TIP]
> Pour tirer le meilleur de ce cours, il est important d’adopter une attitude active et expérimentale.

1. **Ne vous limitez pas à copier le code**

    Les exemples et les laboratoires vous fourniront une base de départ. Mais la compréhension vient surtout lorsque vous modifiez un paramètre, testez une hypothèse, observez le comportement du modèle et analysez les résultats.

> [!IMPORTANT]
> Faire des erreurs fait partie de l’apprentissage. Modifier le code, provoquer des erreurs et les corriger vous aidera à mieux comprendre le fonctionnement réel des modèles.

2. **Apprenez à travailler avec des ressources limitées**

    Les laboratoires visent notamment Google Colab et une carte de type **NVIDIA T4 avec 16 Go de VRAM**. La disponibilité du GPU et la compatibilité des bibliothèques doivent être vérifiées avant chaque séance. L’objectif est de montrer qu’il est possible de construire des prototypes pertinents sans disposer d’un supercalculateur.

3. **Visualisez les concepts**

    Les diagrammes du cours doivent être utilisés comme des cartes de compréhension. Si vous êtes capables d’expliquer le trajet d’un token dans une couche d’attention, vous avez déjà franchi une étape importante.

4. **Gardez une réflexion éthique**

    À chaque étape, nous nous poserons des questions essentielles : quels sont les biais possibles du modèle ? Peut-il produire des réponses trompeuses ? Comment évaluer sa fiabilité ? Comment protéger les utilisateurs ?

5. **Partagez et collaborez**

    Le domaine des LLM repose fortement sur la recherche ouverte, les bibliothèques partagées et les communautés de développeurs. L’apprentissage sera plus riche si vous échangez vos idées, vos difficultés et vos solutions.

---

## Prérequis et matériel

* **Logiciels** : Python 3.11 ou 3.12, ainsi que les bibliothèques `transformers`, `datasets`, `peft`, `trl` et les outils de l’écosystème Hugging Face.
* **Matériel** : un navigateur web suffit pour accéder à Google Colab et exécuter les laboratoires du cours.
* **Compétences utiles** : des bases en programmation Python, en apprentissage automatique et en manipulation de données.
* **Attitude attendue** : curiosité, rigueur, patience et volonté d’expérimenter.

---

## Notre engagement éthique

> [!WARNING]
> Les LLM sont des outils puissants. Ils peuvent produire du texte, influencer des décisions, automatiser des tâches et modifier des pratiques professionnelles.

Tout au long du cours, nous rappellerons que l’IA doit rester un **outil au service de l’humain**. Nous aborderons les notions de transparence, de responsabilité, de biais, de sécurité, de confidentialité et de garde-fous dès les premières activités du cours.

---

## Prêts à commencer ?

Ce cours vous accompagnera progressivement dans la compréhension des grands modèles de langage, depuis leurs fondements jusqu’à leur utilisation dans des applications concrètes.

L’objectif n’est pas seulement de savoir utiliser des outils existants. L’objectif est de comprendre comment ils fonctionnent, comment les évaluer, comment les adapter et comment les intégrer de manière responsable dans des solutions réelles.

---

### Débuter le cours

***Professeure Khadidja Henni***