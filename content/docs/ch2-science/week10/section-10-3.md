---
title: "10.3 Architecture avancée : BLIP-2"
weight: 4
---


## Architecture avancée : BLIP-2

BLIP-2 relie un encodeur d’images à un modèle de langage à l’aide d’un module appelé Q-Former. Celui-ci extrait un ensemble de représentations visuelles adaptées à l’interface du modèle de langage. Cette section permet de suivre le passage de l’image à une réponse textuelle sans supposer que le système décrit toujours correctement ce qu’il reçoit.

{{< bookfig src="213.png" week="10" >}}

## L'ingénierie du Q-Former : Interroger le visuel

> [!IMPORTANT]
**C'est le concept le plus sophistiqué de ce chapitre :** Le Q-Former (*Querying Transformer*) n'est pas un simple adaptateur linéaire. C'est un Transformer à part entière qui joue le rôle d'un "enquêteur". 

Regardez attentivement la **Figure 10-13 : Processus d'entraînement en deux étapes** . Pour comprendre le Q-Former, imaginez qu'il possède une petite collection de "Jetons de questions" (Learnable Queries), généralement 32 tokens. Ces jetons ne correspondent à aucun mot humain au départ. Leur mission est d'aller "frapper à la porte" du Vision Transformer pour lui demander : "Qu'y a-t-il d'intéressant dans cette image pour un modèle de langage ?". 
*   **Self-Attention** : Les 32 jetons discutent entre eux pour ne pas poser la même question.
*   **Cross-Attention** : Les jetons vont piocher des informations dans les patches du ViT (vus en 10.2).
*   **Résultat** : Ces représentations condensent l’information visuelle transmise au modèle de langage.

{{< bookfig src="214.png" week="10" >}}

> [!TIP]
**Interprétation:** Le Q-Former est comme un journaliste qui regarde une scène de crime (l'image) et qui n'en rapporte que les 32 indices les plus importants pour que le rédacteur en chef (le LLM) puisse écrire son article. Il élimine le bruit (les pixels inutiles) pour ne garder que la sémantique.

---
## Étape 1 : Apprendre à comprendre (Representation Learning)
L'entraînement de ce "pont" se fait en deux phases cruciales. Comme l'illustre la **Figure 10-14 : Étape 1 de l'entraînement de BLIP-2**, nous commençons par apprendre au Q-Former à aligner le visuel et le textuel *sans le LLM*.

{{< bookfig src="215.png" week="10" >}}

Le modèle s'exerce sur trois tâches simultanées pour devenir un expert en sémantique :
1.  **Image-Text Contrastive Learning** : Comme pour CLIP (section 10.1), on force le résumé du Q-Former à être mathématiquement proche de la légende de l'image.
2.  **Image-Text Matching** : On demande au modèle : "Est-ce que cette légende décrit vraiment cette photo ?". C'est un test de vérification binaire (Oui/Non).
3.  **Image-grounded Text Generation** : On force le Q-Former à prédire les mots de la légende à partir de ses jetons visuels. 

> [!WARNING]
**Attention :** On ne cherche pas encore à "discuter" avec l'image. On cherche simplement à ce que les 32 jetons du Q-Former capturent l'essence de ce qui est écrit dans la légende. 

---
## Étape 2 : Apprendre à parler (Generative Learning)
Une fois que le Q-Former a compris comment extraire le sens, il faut le connecter à la "bouche" du système : le LLM. C'est ce que montre la **Figure 10-15 : Connexion au LLM** .

{{< bookfig src="216.png" week="10" >}}

> [!NOTE]
**La prouesse technique :** On ajoute une simple **couche de projection linéaire** à la sortie du Q-Former. Son rôle est de transformer les 32 vecteurs visuels pour qu'ils fassent la même taille que les vecteurs de mots du LLM. 
*   Le LLM reçoit alors ces 32 jetons comme s'il s'agissait du début d'une phrase. 
*   Pour le LLM, c'est comme si nous lui chuchotions : "Voici le contexte visuel que tu dois utiliser pour ta réponse".
*   La couche de projection est entraînée afin de fournir au LLM des représentations utiles à la génération de réponses sur l’image.

Regardez la **Figure 10-16 : Architecture BLIP-2 complète** . Elle résume le parcours des données : l'image entre dans le ViT, le Q-Former l'interroge, le résultat est projeté vers le LLM, et le LLM répond. Tout cela en ne modifiant que le "traducteur" central.

{{< bookfig src="217.png" week="10" >}}

---
## Cas d'usage : Visual Question Answering (VQA)
Le **VQA** (réponse à des questions sur une image) est une application de BLIP-2. Il permet de répondre à une question précise, contrairement au légendage général de l’image.

Comme le montre l'exemple de la **Figure 10-17**, vous pouvez demander : "De quelle couleur est la voiture ?" ou "Pourquoi cette image est-elle drôle ?". Le modèle utilise ses jetons visuels pour aller chercher l'information spécifique demandée dans la question. 

> [!TIP]
**C'est le début de l'IA capable de raisonnement visuel.** 

{{< bookfig src="212.png" week="10" >}}

---
## Laboratoire de code : Discussion avec une image (VQA)
Voyons comment mettre en œuvre BLIP-2 sur votre GPU T4. Nous allons utiliser la version "mini" basée sur OPT-2.7B pour qu'elle tienne confortablement dans votre mémoire VRAM.

```python
# Exemple prévu pour Colab T4 16GB VRAM
# !pip install transformers accelerate bitsandbytes pillow requests

from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import requests
import torch

# 1. CHARGEMENT DU TRADUCTEUR ET DU GÉNÉRATEUR
# On utilise la version OPT-2.7B qui est un bon équilibre pour le T4
model_id = "Salesforce/blip2-opt-2.7b"
processor = Blip2Processor.from_pretrained(model_id)
# Utilisation de la demi-précision (float16) pour économiser la mémoire
model = Blip2ForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

# 2. PRÉPARATION DE L'IMAGE
url = "./images/car.png"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# 3. LE PROMPT MULTIMODAL
# On prépare une question sur l'image
question = "Question: What is unique about the car in this photo? Answer:"

# 4. LE PONT Q-FORMER EN ACTION
# Le processeur prépare l'image pour le ViT et le texte pour le Q-Former
inputs = processor(images=image, text=question, return_tensors="pt").to("cuda", torch.float16)

# 5. GÉNÉRATION
with torch.no_grad():
    generated_ids = model.generate(**inputs, max_new_tokens=50)
    # Décodage pour obtenir la réponse humaine
    answer = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

print(f"Image chargée : {url}")
print(f"IA : {answer}")

```

> [!IMPORTANT]
Si vous recevez une erreur de type `OutOfMemory`, c'est que vous avez oublié le `torch_dtype=torch.float16`. 
> [!IMPORTANT]
**À retenir :** en multimodal, la mémoire est votre ressource la plus précieuse. Le chargement en 16-bit divise par deux le poids du modèle sur votre carte graphique.

---
## Éthique et Responsabilité : Les hallucinations visuelles

> [!CAUTION]
l'IA peut parfois "voir" ce qu'elle a envie de voir.

Parce que BLIP-2 s'appuie sur un LLM puissant pour générer du texte, il souffre du même problème que nous avons vu en Semaine 5 : l'imagination statistique.
1.  **Le biais de confirmation** : Si vous demandez "Est-ce qu'il y a un chat dans cette cuisine ?" sur une photo vide, le modèle, influencé par la probabilité statistique que les chats soient dans les cuisines, pourrait répondre "Oui" avec assurance. 
2.  **L'illusion de la description** : la **Figure 10-18 : Test de Rorschach avec BLIP-2** montre que si l'image est ambiguë, le modèle plaque ses propres schémas mentaux appris durant son entraînement. Il ne "voit" pas l'image, il essaie de lui donner un sens qui ressemble aux millions d'autres images qu'il a déjà analysées. 

{{< bookfig src="218.png" week="10" >}}


> [!TIP]
**Synthèse** : La qualité d'un système multimodal dépend de l'encodeur visuel, du module de liaison et du modèle de langage.

> Si le ViT rate un détail, le Q-Former ne pourra pas le traduire, et le LLM inventera la suite. Ne prenez jamais la réponse d'un modèle comme BLIP-2 pour une preuve légale ou médicale sans une double vérification humaine. L'IA est une aide à la perception, pas un substitut à l'observation.

---
La dernière section de cette semaine examine les limites des modèles multimodaux et leurs applications.