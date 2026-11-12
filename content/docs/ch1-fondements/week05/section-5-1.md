---
title: "5.1 La famille GPT"
weight: 2
---

## La famille GPT

Un modèle de type GPT prédit le prochain token à partir du contexte disponible. Son décodeur utilise une attention causale pour ne pas consulter les positions futures. À la génération, chaque token choisi est ajouté au contexte, puis le processus recommence jusqu’à une condition d’arrêt.

{{< bookfig src="28.png" week="05" >}}

## Animation : La génération autorégressive

{{< conceptvideo name="generation" title="La génération autorégressive" >}}
Le contexte initial est « Le chat ». Le modèle attribue des probabilités fictives à plusieurs tokens candidats. Le décodage glouton choisit « dort » (60 %), puis « sur » (70 %), puis « le » (80 %). À chaque étape, le token choisi est ajouté au contexte et une nouvelle distribution est calculée. La boucle continue jusqu’au critère d’arrêt, par exemple un token de fin ou une limite de longueur. L’échantillonnage peut choisir un autre token que le plus probable.
{{< /conceptvideo >}}

## Le moteur autorégressif : La boucle infinie du langage
Le concept fondamental à graver dans votre esprit est la nature **autorégressive** de ces modèles. 
1.  Le modèle reçoit un texte en entrée (le *prompt*).
2.  Il calcule les probabilités pour tous les mots de son dictionnaire et en choisit un.
3.  Ce nouveau mot est ajouté à l'entrée originale.
4.  Le modèle recommence le processus avec cette nouvelle séquence plus longue.

Regardez la [**Figure 1-11**]({{< relref "section-1-2.md" >}}#fig-1-11) que nous avions vue en semaine 1 : c'est ce processus itératif qui permet de construire des paragraphes entiers, mot après mot, brique après brique. 

> [!WARNING]
**Attention :** Le modèle ne "planifie" pas sa phrase à l'avance. Il navigue dans un océan de probabilités statistiques, choisissant à chaque étape le chemin le plus probable (ou le plus créatif selon vos réglages).

## L'épopée GPT : Une montée en puissance phénoménale
L'histoire de la famille GPT est celle d'un changement d'échelle (le *scaling*) qui a révélé des capacités émergentes inattendues. Cette évolution est détaillée à travers les **Figures 5-1 à 5-4** .

### 1. GPT-1 (2018) : La preuve par l'exemple
Avec ses **117 millions de paramètres**, GPT-1 a prouvé que le pré-entraînement sur de grandes quantités de texte brut permettait au modèle d'apprendre la structure du langage sans supervision humaine directe. C'était la naissance du *Foundation Model*.

### 2. GPT-2 (2019) : L'éveil de la généralisation
GPT-2 compte jusqu’à **1,5 milliard de paramètres**. Son évaluation comprend des tâches de traduction et de résumé sans adaptation supervisée propre à ces tâches.

### 3. GPT-3 (2020) : Le géant et le prompting
GPT-3 atteint **175 milliards de paramètres**. Il est évalué notamment en *few-shot prompting*, où quelques exemples sont fournis dans le contexte sans mise à jour des paramètres. La **Figure 5-2** illustre l’augmentation de la taille de ces modèles.

{{< bookfig src="29.png" week="05" >}}

### 4. GPT-4 (2023) : Les entrées multimodales
Bien que ses chiffres exacts soient gardés secrets, GPT-4 marque l'ère des modèles capables de raisonner sur des textes et des images (multimodalité) avec une logique qui frôle parfois celle de l'humain. 

## Tableau récapitulatif de l'évolution GPT

| Modèle | Paramètres | Date | Innovation Majeure |
| :--- | :--- | :--- | :--- |
| **GPT-1** | 117M | 2018 | Premier succès du pré-entraînement génératif |
| **GPT-2** | 1,5B | 2019 | Capacité de généralisation "Zero-shot" |
| **GPT-3** | 175B | 2020 | In-context learning (apprendre via le prompt) |
| **GPT-4** | Inconnu (T) | 2023 | Raisonnement complexe et multimodalité |

> [!NOTE]
En tant que systèmes séquence-vers-séquence, les modèles génératifs essaient fondamentalement de compléter le texte d'entrée.

>Bien que cette capacité d'autocomplétion soit utile, leur plein potentiel s'est révélé lorsqu'ils ont été entraînés pour le **dialogue**. Plutôt que de simplement terminer une phrase, ces modèles peuvent être affinés (via un fine-tuning) pour répondre à des questions et obéir à des instructions. Comme le montre la **Figure 5-3**, le système résultant accepte le prompt de l'utilisateur et génère la réponse la plus probable. Par conséquent, les modèles génératifs sont fréquemment appelés modèles de complétion.

<a id="fig-5-3"></a>
{{< bookfig src="30.png" week="05" >}}

> [!NOTE]
La fenêtre de contexte est une fonctionnalité essentielle définissant le nombre maximum de tokens qu'un modèle peut traiter (**Figure 5-4**). Une fenêtre plus large permet d'analyser des documents entiers. Comme ces modèles sont autorégressifs, la longueur du contexte augmente naturellement à mesure que de nouveaux tokens sont générés.

{{< bookfig src="31.png" week="05" >}}


## Du modèle de fondation à l'assistant : Le tournant de l'Instruction Tuning

> [!IMPORTANT]
**La distinction est capitale :** Un modèle "Base" (comme GPT-3 original) est un compléteur de texte.

Si vous lui demandez "Quelle est la capitale de la France ?", il pourrait répondre par une autre question comme "Et quelle est la capitale de l'Italie ?" car statistiquement, les questionnaires listent souvent des questions à la suite.

Pour transformer ce compléteur en un assistant utile, on utilise le **Supervised Fine-Tuning (SFT)** ou **Instruction Tuning**, illustré en [**Figure 5-3**](#fig-5-3). On montre au modèle des milliers d'exemples de "Question -> Réponse attendue". C'est ce qui crée les modèles **Instruct** ou **Chat** que nous utilisons tous les jours.

## Exemple de génération autorégressive (Intuition technique)

```python
# Exemple conceptuel de génération token par token
# Exemple prévu pour Colab T4 avec un modèle léger (GPT-2)
from transformers import pipeline, set_seed

# Utilisation d'un modèle génératif standard
generator = pipeline('text-generation', model='gpt2', device=0)
set_seed(42)

prompt = "The future of AI is"

# Le modèle va prédire un token, l'ajouter, et recommencer
output = generator(prompt, max_length=15, num_return_sequences=1)

print(f"Sortie du modèle : {output[0]['generated_text']}")
```

## Éthique et Transparence : La séduction du faux

> [!WARNING]
ne vous laissez pas berner par la fluidité. 

>Parce que GPT est un décodeur de probabilités, il ne possède pas de base de données de "vérité". S'il prédit qu'un mot est statistiquement probable, il l'écrira, même si c'est une erreur factuelle totale. C'est l'**hallucination**. 

> [!IMPORTANT]
**À retenir :** Plus le modèle est "large", plus il semble convaincant, ce qui rend ses erreurs d'autant plus dangereuses. Une IA qui parle bien n'est pas forcément une IA qui sait. En tant qu'experts, votre rôle est de concevoir des systèmes de vérification (comme le RAG que nous verrons en Semaine 9) pour ancrer cette imagination débordante dans la réalité.

---
