---
title: "Semaine 5 : Modèles génératifs (decoder-only)"
weight: 5
bookCollapseSection : true
---


# Semaine 5 : Modèles génératifs (decoder-only)

Comprendre la boucle autorégressive et comparer des stratégies de décodage.

## Description générale

Comprendre la boucle autorégressive et comparer des stratégies de décodage. Distinguer modèle de base et modèle adapté aux instructions. Comparer génération gloutonne et échantillonnage avec température.

---
## Pré-requis importants
Pour maîtriser cette semaine, vous devez avoir solidement acquis :
1.  **L'architecture Transformer (Semaine 3)** : Particulièrement le concept de "Self-Attention" (que nous utiliserons ici en mode masqué).
2.  **La Tokenisation (Semaine 2)** : Comprendre que le modèle ne prédit pas des lettres, mais des index de dictionnaire.
3.  **Probabilités de base** : Comprendre ce qu'est une distribution (quel mot a le plus de chances de sortir).

**Ressources pour réviser les pré-requis :**
*    **CodeEmporium (YouTube)** : [Transformers Explained](https://www.youtube.com/watch?v=TQQlZhbC5ps) .
*    **Hugging Face Course** : [How do Transformers work?](https://huggingface.co/learn/nlp-course/chapter1/1) .

---

## Ressources utiles pour les concepts de la semaine

### Articles et Blogs de référence
*   **Jay Alammar** : [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/), Le guide visuel indispensable pour comprendre comment le décodeur génère du texte.
*   **Hugging Face Blog** : [How to generate text: using different decoding methods](https://huggingface.co/blog/how-to-generate), une présentation de la température, du Top-K et du Top-P.
*   **PromptingGuide.ai** : [Introduction au Prompt Engineering](https://www.promptingguide.ai/fr), Pour comprendre comment parler aux modèles Instruct.

### Vidéos recommandées
*    **Andrej Karpathy** : [Let's build GPT: from scratch, in code.](https://www.youtube.com/watch?v=kCc8FmEb1nY), Une vidéo légendaire pour comprendre le "Next Token Prediction".

### Outils pratiques
*   **Hugging Face Documentation** : [Text Generation Strategies](https://huggingface.co/docs/transformers/v4.39.0/en/main_classes/text_generation), La référence pour coder vos paramètres.

---

> [!NOTE]
**Conseil méthodologique** : Un modèle génératif est comme un miroir de ses données. 

>  il est capable de simuler la logique, mais il peut aussi "halluciner" des faits avec une assurance totale. Ne confondez jamais la fluidité du style avec la véracité de l'information. En tant qu'experts, votre rôle est de rester les gardiens de la réalité !

## Repères de lecture

**Prérequis à revoir :** Lire une distribution de probabilités.

**À comprendre en premier :** Distinguer modèle de base et modèle adapté aux instructions. Comparer génération gloutonne et échantillonnage avec température.

**À lire ensuite pour approfondir :** Beam search et comparaison historique des modèles. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Une température basse suffit-elle pour obtenir une réponse factuellement exacte ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [La génération autorégressive]({{< relref "/docs/ch1-fondements/week05/section-5-1.md" >}})
- [Température et probabilités]({{< relref "/docs/ch1-fondements/week05/section-5-3.md" >}})
