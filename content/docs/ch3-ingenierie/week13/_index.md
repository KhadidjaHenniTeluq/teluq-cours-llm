---
title: "Semaine 13 : Déploiement, optimisation et éthique"
weight: 3
bookCollapseSection : true
---


# Semaine 13 : Déploiement, optimisation et éthique

Identifier les contraintes de calcul, de confidentialité et de suivi.

## Description générale

Identifier les contraintes de calcul, de confidentialité et de suivi. Distinguer latence, débit et mémoire du cache KV. Repérer une injection indirecte et proposer des contrôles d’accès.

---
## Pré-requis importants
Pour réussir cette phase finale, vous devez maîtriser :
1.  **Mécanique des Transformers (Semaine 3)** : Essentiel pour comprendre pourquoi le KV cache est nécessaire.
2.  **Quantification (Semaine 11)** : Savoir faire la différence entre NF4 et les formats d'inférence (GGUF, AWQ).
3.  **Bases du Web & API** : Comprendre comment une requête circule entre un client et un serveur.

**Ressources pour réviser les pré-requis :**
*    **Hugging Face Blog** : [A Guide to Quantization](https://huggingface.co/docs/optimum/en/concept_guides/quantization) .
*    **Maarten Grootendorst** : [Visual Guide to Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization) .

*   **Caleb Curry (Youtube)** : [REST API Crash Course - Introduction + Full Python API Tutorial](https://www.youtube.com/watch?v=qbLc5a9jdXo)

---
## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Hugging Face Article** : [Ethics + Sustainability = Responsible AI](https://huggingface.co/blog/sasha/ethics-sustainability), Un manifeste sur les biais et la transparence.
*   **Llama.cpp GitHub** : [GGUF Format & Inference](https://github.com/ggerganov/llama.cpp), Le projet leader pour l'inférence locale optimisée.
*   **AI Act Official** : [EU Artificial Intelligence Act Info](https://artificialintelligenceact.eu/), Pour comprendre le cadre réglementaire européen.

### Vidéos recommandées
*    **Andrej Karpathy** : [Intro to LLMs (Security & Future)](https://www.youtube.com/watch?v=zjkBMFhNj_g), (À partir de 28:00 pour les attaques par injection et les enjeux de sécurité).
*    **NVIDIA** : [Mastering LLM Inference Optimization](https://www.youtube.com/watch?v=9tvJ_GYJA-o), Détails techniques sur le throughput et la latence.

### Frameworks de production
*   **vLLM Documentation** : [High-throughput serving](https://docs.vllm.ai/en/latest/), La bibliothèque de référence pour servir des LLM à grande échelle.
*   **Guardrails AI** : [Input/Output Validation](https://www.guardrailsai.com/docs), Pour sécuriser les interactions.

---

> [!TIP] 
**Conseil méthodologique** : En production, la vitesse est une forme de politesse. 

> [!WARNING]
**Attention :** un utilisateur n'attendra jamais 30 secondes pour une réponse. 

Apprenez à sacrifier un peu de précision pour beaucoup de réactivité. C'est là que l'ingénieur prend le pas sur le chercheur !

## Repères de lecture

**Prérequis à revoir :** Comprendre l’inférence et la recherche documentaire.

**À comprendre en premier :** Distinguer latence, débit et mémoire du cache KV. Repérer une injection indirecte et proposer des contrôles d’accès.

**À lire ensuite pour approfondir :** Moteurs d’inférence, licences et comparaison des cadres juridiques. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Pourquoi un filtre de recherche ne remplace-t-il pas à lui seul une autorisation d’accès ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Le cache KV pendant le décodage]({{< relref "/docs/ch3-ingenierie/week13/section-13-1.md" >}})
