---
title: "7.3 Représentation des sujets"
weight: 4
---

## Représentation des sujets

Après le regroupement, il faut choisir les mots qui décrivent chaque sujet. Les scores c-TF-IDF offrent un point de départ ; des méthodes de reclassement peuvent améliorer la pertinence ou limiter la redondance. L’objectif est de produire une description compréhensible et fidèle aux documents.

## Le socle : c-TF-IDF et ses limites "sac de mots"
Avant de passer aux techniques avancées, comprenons bien notre point de départ. Le **c-TF-IDF** agit comme un premier filtre. Il identifie les mots qui apparaissent plus fréquemment dans un cluster spécifique que dans le reste du corpus. C'est une approche dite "Bag-of-words" (sac de mots). 

Le problème ? Le c-TF-IDF ne "comprend" pas le sens des mots. Si un mot comme "données" apparaît très souvent dans un cluster sur l'IA et aussi dans un cluster sur la biologie, il risque d'avoir un score faible, alors qu'il est crucial pour les deux. De plus, il peut laisser passer des variantes grammaticales inutiles (ex: "chat", "chats", "chaton") qui encombrent votre liste de mots-clés. C'est pour corriger ces défauts que nous introduisons le **Reranking** (ré-ordonnancement).

## Le concept de Reranking
Regardons attentivement la **Figure 7-12 : Affiner les représentations de sujets**.

{{< bookfig src="128.png" week="07" >}}

*   **À gauche (Original topic)** : On voit une liste de mots générée par le c-TF-IDF pur. L'ordre est purement statistique. Certains mots en haut de liste peuvent être génériques.
*   **Le bloc central (Reranker)** : C'est le "cerveau" additionnel que nous ajoutons. Son rôle est de reprendre les candidats fournis par la statistique et de les passer au crible de la sémantique.
*   **À droite (Reranked topic)** : La liste est réorganisée. Les mots qui capturent le mieux l'essence sémantique du groupe montent en grade, tandis que le "bruit" statistique descend. 

> [!NOTE]
**À retenir :** On ne change pas le contenu du sac, on change simplement l'ordre dans lequel on sort les objets du sac pour présenter les plus beaux en premier.


## KeyBERTInspired : Quand les embeddings jugent les mots
La première technique de pointe que nous étudions est **KeyBERTInspired**. Cette méthode est une adaptation de l'algorithme KeyBERT au monde du topic modeling. 

Regardez la **Figure 7-13 : Le bloc de reranking**. Elle illustre comment ce bloc vient s'enficher par-dessus la couche de représentation.

{{< bookfig src="129.png" week="07" >}}

1.  **Le Centroïde du sujet** : Pour chaque cluster, nous calculons la moyenne de tous les embeddings des documents qui le composent. C'est le "poids lourd" sémantique du sujet, sa position GPS idéale.
2.  **La comparaison** : Nous prenons les mots-clés candidats (générés par c-TF-IDF) et nous les transformons eux aussi en vecteurs.
3.  **Le calcul de similarité** : Nous calculons la similarité cosinus (vue en [**6.2**]({{< relref "section-6-2.md" >}}#cos-sin)) entre le vecteur du mot et le centroïde du sujet.
4.  **Le verdict** : Si un mot a une fréquence élevée (statistique) ET qu'il est sémantiquement très proche du cœur du sujet (neuronal), il devient le candidat numéro 1. 

> [!NOTE]
**À retenir :** KeyBERTInspired permet d'éliminer les mots qui sont là par "accident statistique" mais qui n'ont rien à voir avec le thème central. C'est un filtre de cohérence.


## Vaincre la redondance : Maximal Marginal Relevance (MMR)

> [!WARNING]
**Attention** : Les mots les plus proches d’un sujet peuvent être redondants. Par exemple, « espace », « galaxie », « cosmos » et « univers » apportent des informations partiellement similaires. La diversité des termes contribue à la description du sujet.

Pour résoudre cela, nous utilisons la **Maximal Marginal Relevance (MMR)**. Comme l'illustre la **Figure 7-14 : Empiler plusieurs blocs**, MMR est souvent la dernière brique du mur.

{{< bookfig src="130.png" week="07" >}}

*   **Le principe** : MMR essaie de maximiser deux choses contradictoires : la **pertinence** par rapport au sujet et la **diversité** par rapport aux mots déjà choisis. 
*   **Le fonctionnement** : 
    1. On choisit le mot le plus pertinent. 
    2. Pour le deuxième mot, on cherche celui qui est pertinent MAIS qui est le plus "différent" (vecteur éloigné) du premier mot choisi. 
    3. On continue ainsi pour couvrir toutes les facettes du sujet.

> [!TIP]
**Interprétation:** MMR, c'est comme constituer une équipe de projet. Vous ne voulez pas 10 clones identiques du meilleur ingénieur ; vous voulez un ingénieur, un designer, un commercial et un juriste. Ils sont tous pertinents pour le projet, mais ils apportent des perspectives différentes.


## Mise à jour dynamique des représentations
BERTopic permet de modifier la représentation des sujets *sans recalculer l'ensemble du traitement*.

Supposons que le calcul des embeddings et des groupes de 100 000 documents ait pris deux heures, mais que les intitulés obtenus manquent de précision.
> [!WARNING]
Ne relancez pas tout ! Utilisez la méthode `.update_topics()`. Elle ne touche pas à la structure des groupes (les points ne bougent pas), elle change seulement l'algorithme qui "étiquette" ces groupes. C'est quasi instantané.


## Laboratoire de code : Affiner les thématiques
Voici comment implémenter ce pipeline de précision sur Google Colab. Nous allons stacker (empiler) KeyBERT et MMR pour obtenir des résultats professionnels.

```python
# Installation requise : !pip install bertopic
from bertopic.representation import KeyBERTInspired, MaximalMarginalRelevance
from bertopic import BERTopic

# 1. On définit nos modèles de sculpture sémantique
keybert_model = KeyBERTInspired()
mmr_model = MaximalMarginalRelevance(diversity=0.3) # 0.3 est un bon équilibre

# 2. On crée une liste de modèles de représentation
# BERTopic va les appliquer l'un après l'autre
representation_model = {
    "Main": [keybert_model, mmr_model]
}

# 3. Supposons que topic_model est déjà entraîné (vu en 7.2)
# On met à jour les représentations sans toucher aux clusters
topic_model.update_topics(
    docs, 
    representation_model=representation_model
)

# 4. Comparaison
# Regardez la différence entre les mots-clés avant et après !
print(topic_model.get_topic_info()[["Topic", "Count", "Name", "Representation"]].head())
```

> [!NOTE]
**Note technique sur le paramètre `diversity`** : Si vous le réglez à 0, MMR ne fait rien (on prend juste les plus proches). Si vous le réglez à 1, le modèle choisira des mots qui n'ont parfois aucun rapport entre eux juste pour être "différent". Une plage à essayer se situe souvent entre 0.2 et 0.5.


## Cas d'usage : Domaines techniques vs Domaines créatifs
Pourquoi ces réglages sont-ils vitaux ? 
*   **En Médecine** : c-TF-IDF pourrait vous donner "Patient", "Hôpital", "Soin". KeyBERTInspired va forcer le modèle à regarder les termes cliniques précis comme "Cardiopathie" ou "Insuffisance". MMR va s'assurer que vous n'avez pas juste 10 synonymes du mot "douleur".
*   **En Analyse de Presse** : MMR est indispensable. Un sujet sur une élection pourrait être saturé par le nom du gagnant. MMR va forcer le modèle à inclure "vote", "partis", "campagne" et "sondages" pour donner une image complète de l'événement.


## Éthique et Responsabilité : Le pouvoir du cadrage (Framing)

> [!WARNING]
les mots que vous choisissez de montrer à vos clients ou à vos décideurs créent une réalité.

Lorsque vous utilisez MMR ou KeyBERT pour "nettoyer" vos sujets, vous faites un choix éditorial. 
1.  **La réduction du complexe** : En voulant des mots-clés "propres" et "uniques", vous risquez d'effacer les contradictions internes d'un sujet. Un groupe de documents peut être très divisé sur une question, mais MMR va lisser cela pour donner une image de diversité harmonieuse.
2.  **Biais de centroïde** : KeyBERTInspired se base sur la "moyenne" du cluster. Cela signifie que les opinions extrêmes ou les cas particuliers au sein d'un thème seront systématiquement écartés de la description. C'est une forme de "tyrannie de la majorité sémantique". 

> [!TIP]
**Conseil méthodologique** : Utilisez ces techniques pour rendre vos résultats lisibles, mais gardez toujours la liste c-TF-IDF originale sous le coude. Elle est moins "jolie", mais elle est plus fidèle à la distribution brute des données. Ne sacrifiez jamais la vérité à l'esthétique !

---
