---
title: "2.2 Comparaison des tokeniseurs modernes"
weight: 3
---

## Comparaison des tokeniseurs modernes

Deux tokeniseurs peuvent découper la même phrase différemment. Comparer leurs sorties permet de comprendre l’effet du vocabulaire, de la normalisation et des données d’apprentissage. Dans les exemples suivants, on examine aussi les conséquences du découpage sur la longueur des séquences et le traitement du code.

## 1. BERT : La rigueur du pionnier (WordPiece)
BERT (2018) est notre point de référence historique. Il utilise l'algorithme **WordPiece** avec un vocabulaire relativement modeste de 30 000 tokens. 

**La distinction Cased vs. Uncased :**
Voici une différence fondamentale que vous rencontrerez souvent :
*   **BERT-uncased** : Tout est converti en minuscules. "New York" devient "new", "york". 

> [!WARNING]
**Attention** : La suppression de la casse peut convenir à certaines tâches, mais elle élimine un indice utile à la reconnaissance des entités nommées (NER).

*   **BERT-cased** : Préserve la casse. Par exemple, le mot "CAPITALIZATION" est découpé en huit tokens (`CA`, `##PI`, `##TA`, `##L`, `##I`, `##Z`, `##AT`, `##ION`). C'est beaucoup ! Cela montre que BERT-cased est plus précis mais "consomme" plus de jetons pour les mots en majuscules.

> [!NOTE]
** Discussion technique** : BERT utilise le symbole `##` pour marquer les sous-mots. Cela permet au modèle de savoir que `##tion` n'est pas un mot seul, mais la fin d'un mot précédent.

---
## 2. La lignée GPT : Tokenisation par BPE
OpenAI a popularisé le **Byte-level BPE**. Leur innovation ? Ne plus jamais voir de mots "inconnus" en travaillant au niveau des octets.

### GPT-2 (2019) : L'invention du caractère spécial Ġ
Dans le tokeniseur de GPT-2, le caractère `Ġ` (Unicode `\u0120`) représente un espace précédant un mot.
*   **Intuition** : GPT-2 traite l'espace *avant* un mot comme faisant partie du mot lui-même. 
*   **Pourquoi ?** Cela permet au modèle de distinguer "chat" (en début de phrase) et " chat" (au milieu d'une phrase). Pour l'IA, ce sont deux concepts statistiques légèrement différents. 

> [!NOTE]
**Notez bien :** Avec son vocabulaire de 50 000 tokens, GPT-2 est bien plus efficace que BERT pour représenter des mots complexes.

> [!NOTE]
**Note technique : L'importance cruciale des espaces** 
Pourquoi devrions-nous nous soucier autant des simples espaces blancs (espaces, tabulations) ? Ils sont en fait fondamentaux pour qu'un modèle puisse comprendre ou générer du code informatique de manière fiable.

> Prenons l'exemple de Python. Si un tokeniseur est optimisé pour utiliser un seul et unique token représentant "quatre espaces consécutifs", le modèle sera redoutablement efficace pour indenter du code. À l'inverse, si l'IA est forcée d'utiliser quatre tokens distincts pour coder ces mêmes sytaxes, l'exercice devient périlleux : le modèle doit constamment "garder en mémoire" le compte exact des espaces pour maintenir le niveau d'indentation, ce qui fait chuter ses performances globales. 
C'est la preuve formelle qu'un choix de conception en apparence mineur lors de la tokenisation peut transformer radicalement les capacités d'apprentissage du modèle sur une tâche spécifique !


### GPT-4 (2023) : Le saut vers les 100 000 tokens

> [!IMPORTANT]
**À retenir :**Entre GPT-2 et GPT-4, OpenAI a doublé la taille du dictionnaire. 
*   **L'avantage** : Un dictionnaire plus grand signifie que des mots longs et fréquents (ex: "anthropologie") deviennent un seul token au lieu de trois. 
*   ** Conséquence pour l'ingénieur** : Comme le modèle utilise moins de tokens pour dire la même chose, vous pouvez faire tenir des documents beaucoup plus longs dans la fenêtre de contexte. C'est un gain de productivité direct.

---
## 3. Flan-T5 et SentencePiece : L'approche agnostique
Flan-T5 utilise **SentencePiece**, un outil qui traite l'espace comme un caractère normal (souvent noté `_`). 

> [!WARNING]
**Avertissement** : Regardez la note ci-dessus. Flan-T5 a une faiblesse : il a été entraîné sans tokens pour les retours à la ligne (`\n`) ou les tabulations.

*   **Limite** : Lorsque la normalisation supprime les sauts de ligne, le modèle perd des informations de mise en page qui peuvent être utiles à l’analyse de fichiers de configuration ou de poèmes.

---
## 4. StarCoder2 : Le traducteur de code source
*si vous voulez que votre IA programme à votre place, elle doit comprendre la structure d'un code (Python par exemple).* 

> [!TIP]
StarCoder2 est une merveille d'ingénierie spécialisée.

**Les deux secrets de StarCoder2** :
1.  **L'indentation comme token** : Contrairement aux modèles de texte, StarCoder2 possède des tokens dédiés pour "un espace", "deux espaces", "quatre espaces". Pourquoi ? Parce qu'en Python, l'espace définit la logique. Si vous fusionnez les espaces n'importe comment, le code ne compilera jamais.
2.  **La tokenisation des chiffres** : 

> [!IMPORTANT]
>  **C'est un concept non-négociable :** StarCoder2 découpe les nombres chiffre par chiffre (`123` devient `1`, `2`, `3`). 

> *   *Pourquoi ?* Pour que le modèle apprenne l'arithmétique. Si "123" est un token unique, le modèle doit mémoriser son nom. S'il voit "1", "2" et "3", il peut apprendre les règles de retenue et de calcul comme un enfant à l'école.

---
## 5. Galactica : Un modèle pour les textes scientifiques
*Galactica* a été entraîné sur la science. Son tokeniseur est unique car il gère :
*   **Les citations** : Des tokens spéciaux comme `[START_REF]` et `[END_REF]` permettent au modèle de savoir quand il s'appuie sur une source.
*   **La chimie et l'ADN** : Il ne découpe pas les formules chimiques (`H2O`) de manière aléatoire, ce qui permet de préserver la sémantique des molécules. 
*   **Le raisonnement** : Il utilise le token `<work>` pour délimiter ses brouillons de calculs internes.

---
## 6. Phi-3 et Llama 2 : La standardisation moderne
Ces modèles utilisent des tokeniseurs BPE très optimisés pour le dialogue. Ils intègrent des balises de rôle comme `<|user|>` ou `<|assistant|>`. 

> [!NOTE]
**À retenir :** Ces tokens ne sont pas du texte, ce sont des "commandes de vol" pour le modèle. Ils indiquent à l'IA quand elle doit écouter et quand elle doit répondre.

---
## Tableau récapitulatif : Comparaison des vocabulaires

| Modèle | Méthode | Taille Vocab | Spécificité |
| :--- | :--- | :--- | :--- |
| **BERT** | WordPiece | 30 000 | Bidirectionnel, `##` pour sous-mots. |
| **GPT-2** | BPE | 50 257 | Byte-level, utilise le `Ġ` pour l'espace. |
| **GPT-4** | BPE | 100 256+ | Très efficace pour les fenêtres de contexte. |
| **Flan-T5** | Unigram | 32 100 | SentencePiece, gère mal les retours ligne. |
| **StarCoder2**| BPE | 49 152 | Chiffres isolés, tokens d'indentation. |
| **Galactica** | BPE | 50 000 | Citations et formules scientifiques. |


---
## Laboratoire de code : Comparaison pratique sur Colab
**Ne me croyez pas sur parole, testez-le !** 

Voici comment comparer l'efficacité de deux tokeniseurs sur une même phrase technique.

```python
# Exemple prévu pour Google Colab T4 16GB VRAM
from transformers import AutoTokenizer

# On compare BERT (texte) et StarCoder (code)
model_names = {
    "BERT (Général)": "bert-base-uncased",
    "StarCoder (Code)": "bigcode/starcoder2-7b" 
}

# Un texte avec du code et des chiffres
text = "for i in range(123): print(i)"

for name, path in model_names.items():
    try:
        tokenizer = AutoTokenizer.from_pretrained(path)
        tokens = tokenizer.tokenize(text)
        print(f"--- {name} ---")
        print(f"Nombre de tokens : {len(tokens)}")
        print(f"Découpage : {tokens}\n")
    except Exception:
        print(f"Note : {name} nécessite un accès spécifique sur HuggingFace.")
```

> [!IMPORTANT]
Observez le découpage du nombre `123`. Vous verrez que StarCoder le traite différemment pour préserver la logique mathématique. 

**C'est une distinction capitale pour vos futurs projets de data science.**

---
## Éthique et Économie : Le coût caché du token

> [!CAUTION]
la tokenisation est un enjeu de justice. 

Comme nous l'avons évoqué, la tokenisation n'est pas neutre économiquement.
1.  **Le coût de la langue** : Puisque la plupart des tokeniseurs sont entraînés sur des corpus anglo-centrés, un locuteur français ou arabe "consomme" plus de tokens pour la même phrase. Si vous utilisez une API payante (OpenAI, Anthropic), **votre facture sera plus élevée simplement à cause de votre langue maternelle.** 

2.  **La barrière à l'entrée** : Les modèles avec de petits dictionnaires (comme BERT) sont plus "bêtes" face aux langues rares car ils hachent les mots en trop de morceaux, perdant le fil sémantique. 

3.  **L'illusion de l'universalité** : 
> [!NOTE]
**À retenir :** Un tokeniseur "multilingue" est souvent un tokeniseur anglais qui a appris quelques mots d'ailleurs. Toujours tester la fragmentation de votre langue cible avant de choisir un modèle.

---
## Synthèse
Nous avons parcouru la jungle des tokeniseurs modernes. Nous avons vu que BERT privilégie la structure des mots (`##`), que GPT cherche l'efficacité massive (100k+ tokens), et que les modèles spécialisés (StarCoder, Galactica) réinventent le découpage pour servir la logique ou la science.

> [!IMPORTANT]
**Synthèse** : Avant d'adapter un modèle, examinez la segmentation des termes propres au domaine. La tokenisation influence la longueur des séquences et la représentation des données.

---
La section suivante examine les **propriétés techniques** des tokeniseurs et les paramètres de leur configuration.