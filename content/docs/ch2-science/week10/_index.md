---
title: "Semaine 10 : LLM multimodaux"
weight: 5
bookCollapseSection : true
---

# Semaine 10 : LLM Multimodaux

Distinguer représentation d’image, alignement et génération multimodale.

## Description générale

Distinguer représentation d’image, alignement et génération multimodale. Expliquer le découpage d’une image en patches. Distinguer CLIP d’un modèle qui génère une réponse à partir d’une image.

## Pré-requis importants
Pour cette immersion, vous devez avoir révisé :
1.  **L'Attention Spatiale** : Comprendre que la self-attention (Semaine 3) peut s'appliquer aux pixels comme aux mots.
2.  **L'Espace Vectoriel Commun** : L'idée que le vecteur du mot "Chien" et le vecteur d'une photo de chien doivent être proches mathématiquement.

**Ressources pour réviser les pré-requis :**
*    **Computerphile** : [Vision Transformer (ViT) - How it works](https://www.youtube.com/watch?v=Hnsrm1ezI3g) (Excellente introduction au *Vision Transformer*).
*    **Hugging Face Documentation** : [Concepts de Computer Vision](https://huggingface.co/docs/transformers/tasks/image_classification) (Pour comprendre le prétraitement des images).

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Lilian Weng (OpenAI)** : [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/), Un blog technique détaillé et précis sur les modèles de langage visuels.
*   **OpenAI Index** : [CLIP: Connecting Text and Images](https://openai.com/index/clip/), L'article original expliquant l'apprentissage contrastif.
*   **Google Research Blog** : [Transformers for Image Recognition at Scale](https://blog.research.google/2020/12/transformers-for-image-recognition-at.html), L'introduction officielle du Vision Transformer (ViT).
*   **Hugging Face Blog** : [Zero-shot image-to-text generation with BLIP-2](https://huggingface.co/blog/blip-2), Analyse technique de l'architecture Q-Former et son intégration.
*   **Jay Alammar** : [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/), (Voir la section sur le "Text Encoder" pour comprendre comment CLIP aligne le sens).

### Tutoriels et Outils
*   **Hugging Face Documentation** : [Using CLIP for Zero-Shot Image Classification](https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification), Guide pratique pour classer des images sans entraînement.
*   **OpenCLIP GitHub** : [Models and Usage](https://github.com/mlfoundations/open_clip), La bibliothèque de référence pour les modèles CLIP open-source.

---

> [!TIP]
**Conseil méthodologique** : Dans les sections à venir, gardez en tête l'analogie du "Traducteur" : le Q-Former de BLIP-2 est comme un interprète assis entre un photographe (ViT) et un écrivain (LLM). Son rôle est de transformer des signaux visuels en concepts que l'écrivain peut comprendre. 

> [!WARNING]
**Attention :** un mauvais alignement conduit à des hallucinations visuelles !

## Repères de lecture

**Prérequis à revoir :** Comprendre les embeddings et l’attention.

**À comprendre en premier :** Expliquer le découpage d’une image en patches. Distinguer CLIP d’un modèle qui génère une réponse à partir d’une image.

**À lire ensuite pour approfondir :** Détails du Q-Former et entraînement de BLIP-2. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Pourquoi un bon score image-texte ne garantit-il pas que tous les détails ont été reconnus ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [CLIP et l’apprentissage contrastif]({{< relref "/docs/ch2-science/week10/section-10-1.md" >}})
- [Du patch au token visuel]({{< relref "/docs/ch2-science/week10/section-10-2.md" >}})
