---
title: "Semaine 8 : Ingénierie des prompts"
weight: 3
bookCollapseSection : true
---

# Semaine 8 : Ingénierie des prompts

Construire une demande précise et vérifier la sortie obtenue.

## Description générale

Construire une demande précise et vérifier la sortie obtenue. Séparer consigne, données, exemples et format attendu. Distinguer validation de structure et vérification du contenu.

## Pré-requis importants
Pour cette semaine, vous devez avoir bien assimilé :
1.  **Intuition des modèles génératifs (Semaine 5)** : Comprendre comment le modèle prédit le prochain token.
2.  **Paramètres de génération (Semaine 5)** : Savoir ce que sont la température et le Top-P.
3.  **Bases du Python** : Pour manipuler des chaînes de caractères et faire des appels aux modèles via `transformers` ou `llama-cpp-python`.

**Ressources pour réviser les pré-requis :**
*    **Tutoriel Hugging Face** : [Pipeline de génération de texte](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextGenerationPipeline) .
*    **Documentation Python** : [F-strings et manipulation de chaînes](https://docs.python.org/3/tutorial/inputoutput.html) .

---

## Ressources utiles pour les concepts de la semaine

### Documentations et Guides de référence
*   **PromptingGuide.ai** : [The Prompt Engineering Guide](https://www.promptingguide.ai/fr), La ressource la plus complète et multilingue sur le sujet .
*   **Hugging Face Blog** : [LLM Prompting Guide](https://huggingface.co/docs/transformers/v4.49.0/tasks/prompting), Un excellent point de départ technique .
*   **Documentation OpenAI** : [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering), Des conseils applicables à tous les modèles, pas seulement GPT .

### Vidéos recommandées
*    **DeepLearning.AI (Andrew Ng)** : [ChatGPT Prompt Engineering for Developers](https://www.youtube.com/watch?v=H4YK_7MAckk), Un cours fondamental sur la structuration des instructions .
*    **Elvis Saravia** : [Advanced Prompting Techniques](https://www.youtube.com/watch?v=dOxUroR57xs), Focus sur le raisonnement et les agents .

### Outils de contrôle
*   **llama-cpp-python** : [Guide sur les grammaires GBNF](https://github.com/abetlen/llama-cpp-python#json-schema-and-grammar-based-sampling), Pour forcer les modèles locaux à sortir du JSON .

---

> [!TIP]
Dans cette semaine, vous allez devenir des "sculpteurs de contexte". 

> [!WARNING]
**Attention :** un prompt trop long peut perdre le modèle au milieu du texte. C'est ce qu'on appelle le phénomène du "Lost in the Middle". Apprenez à être précis, concis et structuré !

## Repères de lecture

**Prérequis à revoir :** Comprendre la génération et ses limites.

**À comprendre en premier :** Séparer consigne, données, exemples et format attendu. Distinguer validation de structure et vérification du contenu.

**À lire ensuite pour approfondir :** Tree-of-Thought et grammaires de décodage. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Un JSON valide contient-il nécessairement des informations exactes ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [Construire un prompt vérifiable]({{< relref "/docs/ch2-science/week08/section-8-1.md" >}})
