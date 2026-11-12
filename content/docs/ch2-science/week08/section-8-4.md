---
title: "8.4 Vérification et contrôle"
weight: 5
---

## Vérification et contrôle

Une application doit vérifier les sorties qu’elle reçoit. Un schéma permet de contrôler la structure d’un objet JSON ; un décodage contraint peut limiter les formes générées. Ces outils ne vérifient pas automatiquement la pertinence ou la vérité des valeurs contenues dans la réponse.

## Pourquoi valider la sortie ? Les trois risques majeurs
Dans un environnement professionnel, on ne peut pas se contenter d'un "ça a l'air de marcher". Voici les trois piliers de vérification indispensables pour tout ingénieur en LLM :
1.  **La structure (Format)** : Si votre logiciel attend un format JSON pour mettre à jour une base de données et que l'IA répond "Voici votre JSON : { ... }", la phrase d'introduction fera échouer votre code.
2.  **La validité (Logic)** : Même si le format est bon, les valeurs doivent être cohérentes. Une IA qui génère un personnage de jeu avec une "force" de 1 000 000 alors que le maximum est 100 brise l'équilibre de votre application.
3.  **L'éthique et la sécurité** : C'est le point non-négociable. Nous devons nous assurer que la sortie ne contient pas de données personnelles (PII), de propos haineux ou de failles de sécurité (injections de code).


## Technique 1 : La boucle de vérification par les pairs (Self-Correction)
La méthode la plus simple consiste à utiliser un LLM pour en vérifier un autre, ou pour se vérifier lui-même. C'est ce qu'illustre la **Figure 8-12**.

{{< bookfig src="152.png" week="08" >}}

Décortiquons le contenu de cette figure :
*   **Le cycle itératif** : La figure montre un premier passage où l'IA génère une réponse (A). Cette réponse est ensuite passée à un "vérificateur" (qui peut être le même modèle avec un prompt différent).
*   **Les règles (Guardrails)** : Le vérificateur a une liste de critères (ex: "Le texte est-il en JSON ? Est-il courtois ?"). 
*   **La rétroaction** : Si une règle est enfreinte, le vérificateur renvoie une erreur à l'IA initiale ("Tu as oublié de fermer l'accolade, recommence").

> [!TIP]
**Interprétation:** C'est comme un auteur qui se relit ou qui demande à un éditeur de corriger son manuscrit. Cela améliore la qualité, mais attention : cela double votre consommation de tokens et votre temps de réponse !


## Technique 2 : L'échantillonnage contraint (Constrained Sampling)
La génération contrainte intervient sur les probabilités des tokens pour restreindre les sorties à une syntaxe autorisée, plutôt que de corriger uniquement les erreurs après la génération.

Regardons les **Figures 8-13 et 8-14** :
*   **Figure 8-13 : Génération de pièces manquantes** : On donne au modèle un "moule" (un template JSON avec des trous). On force le modèle à ne remplir que les trous. Le modèle n'a pas le choix, il ne peut pas ajouter de texte inutile autour.
{{< bookfig src="153.png" week="08" >}}

*   **Figure 8-14 : Constrained Sampling par masque de probabilité** : C'est la technique la plus avancée. Imaginez que le modèle doive choisir le prochain token. Normalement, il a 50 000 choix possibles. Si nous savons que l'étape suivante dans un JSON doit être un chiffre, nous appliquons un "masque" : nous mettons la probabilité de tous les mots du dictionnaire à zéro, sauf pour les chiffres de 0 à 9.
{{< bookfig src="154.png" week="08" >}}
 
> [!NOTE]
**À retenir :** Avec cette technique, le modèle ne peut mathématiquement PAS produire une erreur de format. Il devient un moteur de données déterministe au sein d'une architecture probabiliste.


## L'usage des Grammaires (GBNF)
Pour réaliser ce tour de force avec des modèles locaux (comme ceux que nous utilisons sur Colab), nous utilisons souvent le format **GBNF** (*Guidance/GGML BNF*). C'est une façon de définir une "recette" syntaxique que l'IA doit suivre.
*   *Analogie* : C'est comme un rail de chemin de fer. Le train (l'IA) peut aller vite et être puissant, mais il ne peut pas sortir des rails que vous avez posés.


## Laboratoire de code : Contraindre le format JSON (Colab T4)
Nous allons utiliser la bibliothèque `llama-cpp-python` qui permet de charger des modèles compressés (GGUF) et de leur imposer une structure JSON stricte. 
> [!WARNING]
**Attention !** Assurez-vous d'avoir redémarré votre session Colab pour libérer la VRAM.

```python
# Installation des outils de contrôle
# !pip install llama-cpp-python 

from llama_cpp import Llama
import json

# 1. Chargement d'un modèle compact (TinyLlama ou Phi-3 GGUF)
llm = Llama(
    model_path="path_to_your_model.gguf", # Remplacez par votre lien de téléchargement
    n_gpu_layers=-1, # On utilise tout le GPU T4 !
    n_ctx=2048
)

# 2. Définition de la tâche
prompt = "Create a health report for a patient named Sarah. Include age, heart_rate, and status."

# 3. GÉNÉRATION CONTRAINTE (L'arme secrète)
# On demande explicitement un 'json_object' au moteur d'inférence
response = llm.create_chat_completion(
    messages=[{"role": "user", "content": prompt}],
    response_format={
        "type": "json_object",
        "schema": { # On définit le schéma attendu
            "type": "object",
            "properties": {
                "age": {"type": "number"},
                "heart_rate": {"type": "number"},
                "status": {"type": "string"}
            },
            "required": ["age", "heart_rate", "status"]
        }
    },
    temperature=0.7 # On peut garder de la créativité sur le contenu !
)

# 4. Extraction et validation
json_output = json.loads(response["choices"][0]["message"]["content"])
print(f"Sortie validée : {json_output}")
```

> [!NOTE]
**Note** : La température reste fixée à 0.7. La génération respecte la structure JSON prévue, mais les valeurs produites doivent être validées indépendamment.


## Frameworks de contrôle : Guardrails, Guidance et Outlines
Dans le monde professionnel, vous n'allez pas tout coder à la main. Il existe des bibliothèques dédiées à la sécurité et au contrôle des LLM :
*   **Guardrails AI** : Permet de définir des "Rails" en XML pour vérifier les sorties (ex: "Vérifie qu'il n'y a pas d'insultes").
*   **Guidance (Microsoft)** : Un langage de programmation qui entrelace le texte humain et le contrôle de l'IA.
* **Outlines** : Une bibliothèque de génération structurée. Les contraintes prises en charge peuvent assurer une structure conforme, sous les conditions de l’outil, mais ne valident pas les faits contenus dans la réponse.


## Éthique et Responsabilité : L'illusion du contrôle total

> [!CAUTION]
Ne vous laissez pas bercer par un sentiment de sécurité trompeur.

Un JSON syntaxiquement valide peut contenir des informations inexactes.
1.  **Hallucinations structurées** : L'IA peut vous donner un JSON très propre contenant des faits totalement inventés (ex: un faux diagnostic médical). 
> [!TIP]
**Règle d'or :** La structure n'est pas la vérité.
2.  **Biais de formatage** : Parfois, forcer un format (ex: n'accepter que "Oui" ou "Non") empêche l'IA d'exprimer une nuance importante ou une incertitude nécessaire. C'est une forme de censure technique qui peut mener à des décisions erronées. 
3.  **Sur-confiance** : Un développeur qui voit une sortie JSON a tendance à lui faire plus confiance qu'à un texte libre. C'est un piège psychologique. Gardez toujours un esprit critique.


**Synthèse** : Le contrôle du format facilite l'intégration des réponses dans une application. Il doit être complété par une validation de leur contenu.

> En maîtrisant ces techniques, vous ne construisez plus seulement des gadgets, vous construisez des systèmes fiables. Mais n'oubliez jamais : vous êtes le chef d'orchestre, et la machine n'est que l'instrument. La responsabilité finale de la décision appartient toujours à l'humain.

---
