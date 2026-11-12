---
title: "7.4 Amélioration par les LLM"
weight: 5
---


## Amélioration par les LLM

Un LLM peut proposer un intitulé à partir de mots-clés et de documents représentatifs. Cela facilite la lecture des résultats, mais le modèle peut aussi ajouter une interprétation absente du corpus. Nous comparons les intitulés générés au contenu des documents et aux descriptions obtenues sans LLM.

## L'intuition technique : Le LLM comme agrégateur de contexte
Comment un modèle peut-il "nommer" un groupe de 5 000 documents sans les lire un par un ? La réponse réside dans la sélection intelligente d'échantillons. BERTopic ne demande pas au LLM de traiter l'intégralité du cluster (ce qui serait ruineux en termes de jetons/tokens et de temps). 

Regardez attentivement la **Figure 7-15 : Utilisation des LLM pour la génération de labels**. Cette illustration détaille un processus en trois temps :

{{< bookfig src="132.png" week="07" >}}

1.  **La sélection des délégués** : Pour chaque cluster, BERTopic identifie les documents les plus représentatifs (souvent les 3 ou 4 documents les plus proches du centre sémantique, le "centroïde"). 
2.  **La signature statistique** : On y ajoute les mots-clés c-TF-IDF que nous avons calculés en [**section 7.2**]({{< relref "section-7-2.md" >}}#c-tf-idf) .
3.  **Le Prompt de synthèse** : On envoie cet ensemble au LLM avec une consigne précise.

> [!TIP]
**Astuce de performance :** En ne fournissant que les "délégués" du sujet, on permet au LLM de saisir le contexte profond sans saturer sa fenêtre de contexte. C'est une forme de compression sémantique ultra-efficace. 


## L'art du Prompting pour la modélisation de sujets

> [!WARNING]
**Attention :** Si vous demandez simplement au LLM : "Donne un titre à ces mots", vous obtiendrez des résultats banals. Pour obtenir une étiquette de haute qualité, votre prompt doit être une architecture à part entière.

Un prompt de modélisation de sujets efficace doit contenir :
*   **Le rôle (Persona)** : "Vous êtes un expert en analyse documentaire et en taxonomie."
*   **Le contexte des données** : "Ces documents sont des résumés d'articles scientifiques provenant d'ArXiv."
*   **Les preuves (Documents représentatifs)** : "Voici trois exemples de textes appartenant à ce groupe..."
*   **Les indices (Mots-clés)** : "Les mots statistiquement dominants sont : [KEYWORDS]."
*   **La contrainte de sortie** : "Fournissez un titre court (moins de 7 mots) et une description d'une phrase."

> [!IMPORTANT]
**À retenir :** plus vous donnez de structure à votre demande, moins le modèle aura tendance à "halluciner" un titre qui n'a rien à voir avec vos données.


## Modèles propriétaires (API) vs Modèles Open-source
Dans le cadre de BERTopic, vous avez deux grandes options pour cette étape finale.

### 1. Les API de haut niveau (OpenAI, Anthropic, Cohere)
*   **Avantages** : Qualité de résumé exceptionnelle, gestion de l'ironie et des nuances complexes.
*   **Inconvénients** : Coût (facturation au token) et confidentialité (vos documents "délégués" sortent de votre infrastructure).
*   **Usage idéal** : Rapports stratégiques, analyse de presse internationale.

### 2. Les modèles locaux (Flan-T5, Mistral, Llama, Phi-3)
Le traitement porte sur quelques phrases par sujet, ce qui permet d’utiliser un modèle de taille limitée comme **Flan-T5-base**.
*   **Flan-T5** : Un modèle de type Encodeur-Décodeur, excellent pour le résumé pur et simple.
*   **Phi-3 / Llama-3-8B** : Plus créatifs, ils permettent de générer des labels plus "humains" et moins robotiques.


## Laboratoire de code : Intégration LLM dans BERTopic
Voici comment configurer BERTopic pour utiliser un LLM comme "moteur d'étiquetage". Nous allons simuler l'usage d'un modèle local pour rester dans une approche respectueuse de vos ressources GPU.

```python
# Installation requise : !pip install bertopic transformers accelerate bitsandbytes
from bertopic import BERTopic
from bertopic.representation import TextGeneration
from transformers import pipeline

# 1. Préparation du "Cerveau" de synthèse (Modèle local Phi-3-mini)
generator = pipeline(
    "text-generation", 
    model="microsoft/Phi-3-mini-4k-instruct", 
    device_map="auto",
    model_kwargs={"torch_dtype": "auto", "trust_remote_code": True}
)

# 2. Construction du Prompt Template spécialisé
prompt = """
I have a topic described by the following keywords: [KEYWORDS]
Based on the following example documents from this topic:
[DOCUMENTS]

Extract a concise, professional label for this topic.
Topic Label:"""

# 3. Création du bloc de représentation LLM
representation_model = TextGeneration(generator, prompt=prompt)

# 4. Intégration dans BERTopic (Supposons que topic_model est déjà créé)
# Nous utilisons update_topics pour ne pas perdre les calculs précédents
topic_model.update_topics(
    docs, 
    representation_model=representation_model
)

# 5. Résultat : Vos sujets ont maintenant un label généré par l'IA !
print(topic_model.get_topic_info()[["Topic", "CustomName", "Representation"]].head())
```

## Évaluation des labels générés : Comment savoir si l'IA ment ?

> [!WARNING]
Ne tombez pas dans le piège de la beauté.

> Un titre magnifique généré par GPT-4 peut être une hallucination complète si le modèle a mal interprété les documents délégués.

Comment vérifier ?
1.  **Cohérence intra-cluster** : Le titre correspond-il vraiment aux 10 premiers mots-clés du c-TF-IDF ?
2.  **Test de spécificité** : Si l'IA donne le même titre ("Informatique générale") à trois clusters différents, votre prompt n'est pas assez précis. 
3.  **L'audit humain** : 
> [!IMPORTANT]
**C'est non-négociable :** vous devez lire les documents délégués et juger si le titre résume honnêtement leur contenu.


## Éthique et Responsabilité : La tentation du "Rebranding"

> [!IMPORTANT]
nommer, c'est exercer un pouvoir.

Lorsque vous demandez à une IA de nommer un cluster de données sensibles (ex: des plaintes de citoyens ou des effets secondaires de médicaments) :
1.  **L'euphémisation** : L'IA, entraînée à être "polie" (RLHF), pourrait transformer un cluster de "Plaintes pour racisme" en "Défis de communication interculturelle". C'est un biais de neutralité dangereux qui masque la réalité sociale des données.
2.  **La stigmatisation** : À l'inverse, un prompt mal cadré pourrait pousser le modèle à utiliser des termes chargés d'émotion ou de préjugés pour décrire un groupe de population identifié par le clustering. 

> [!TIP]
**Conseil méthodologique** : Considérez toujours le label généré par le LLM comme une **suggestion**, et non comme une vérité définitive. Dans un pipeline de production, prévoyez toujours une étape de validation humaine pour les noms de sujets avant qu'ils ne soient diffusés. L'IA est une excellente assistante de rédaction, mais elle ne doit jamais être la seule juge de la signification de vos données.

---
