---
title: "1.3 Le paradigme de l'attention"
weight: 4
---


## Le paradigme de l'attention

L’attention calcule une combinaison pondérée de représentations. Elle permet à une position de la séquence d’utiliser des informations provenant d’autres positions. Le Transformer, présenté dans « Attention Is All You Need » en 2017, place ce mécanisme au centre de son architecture. Les modèles antérieurs et les architectures alternatives restent utiles selon les tâches.

## L'intuition humaine : Pourquoi l'attention est-elle naturelle ?
Avant de parler de matrices et de vecteurs, regardons comment fonctionne votre propre cerveau. Quand je vous dis : « Le professeure Khadidja Henni, passionnée par les modèles de langage à grande échelle, a posé son **livre** sur la table parce qu'il était trop lourd », à quoi se rapporte le mot « il » ?

Votre cerveau ne lit pas chaque mot avec la même intensité. Pour comprendre « il », vous portez une **attention** immédiate et massive au mot « livre ». Vous ignorez « table » (une table n'est pas "lourde" dans ce contexte d'action) et vous ignorez le nom du professeur. C'est cette capacité à filtrer le bruit pour se concentrer sur les signaux pertinents que nous avons voulu donner aux machines. 

Dans les RNN (section 1.2), la machine essayait de se souvenir de tout. Dans les Transformers, la machine apprend à **choisir** ce qu'elle regarde.

---
## L'évolution : De l'attention "béquille" à l'attention "moteur"
L'attention n'est pas apparue d'un coup. Elle a d'abord été une solution de secours pour les RNN fatigués.

### L'Attention dans le décodeur RNN
Regardons la **Figure 1-13 : Attention dans le décodeur RNN** . 

{{< bookfig src="19.png" week="01" >}}

**Explication de la Figure 1-13** : Dans cette architecture hybride, on garde le RNN (l'encodeur et le décodeur), mais on ajoute un "câblage direct".
*   **Le problème initial** : Le décodeur ne recevait que le dernier mot de l'encodeur (le goulot d'étranglement).
*   **La solution de la figure** : On permet au décodeur, à chaque étape de génération, d'aller "piocher" des informations dans *tous* les états cachés de l'encodeur. 
*   **L'effet visuel** : On voit des flèches qui relient le décodeur à chaque mot de la phrase source. Si le modèle traduit le mot "lama's", il va activer la flèche qui pointe vers "llamas" dans la phrase d'origine. 

> [!NOTE]
**Note** : L'attention améliore l'accès aux états précédents, mais le RNN sous-jacent conserve un traitement séquentiel.


### La Self-Attention : Le dialogue interne
La **Figure 1-14 : Mécanisme d’attention** présente ce mécanisme.

{{< bookfig src="18.png" week="01" >}}

**Explication de la Figure 1-14** : On passe de l'attention entre deux modèles à la **Self-Attention** (Auto-attention) au sein d'un même texte.
*   Chaque mot de la phrase est comparé à tous les autres mots de la *même* phrase.
*   La figure montre une matrice de liens. Par exemple, le mot "animal" est fortement lié au mot "rue" et au mot "fatigué".

> [!TIP]
**L'intuition technique** : Chaque mot "s'enrichit" du sens de ses voisins. 

L'embedding statique de la Semaine 2 devient un **embedding contextuel**. Le mot "bank" ne sera plus un vecteur flou ; il absorbera le vecteur "rivière" s'il est à côté, ou le vecteur "argent" s'il est dans un autre contexte.

---
## La mathématique de l'Attention : Query, Key, Value
voici le moment où nous devons être rigoureux. Ne craignez pas les noms anglais, ils cachent une logique de bibliothèque très simple. 

Pour calculer l'attention, chaque mot (token) est transformé en trois vecteurs distincts :
1.  **Query (La Requête - Q)** : « Voici ce que je cherche. » (ex: le mot "elle" cherche son sujet).
2.  **Key (La Clé - K)** : « Voici ce que je contiens. » (ex: le mot "souris" dit "Je suis un nom féminin capable d'avoir faim").
3.  **Value (La Valeur - V)** : « Voici l'information que je donne si vous me choisissez. »

**Le processus de calcul (Le Dot-Product Attention)** :
*   On multiplie la **Query** du mot actuel par les **Keys** de tous les autres mots.
*   Cela donne un score (une note de compatibilité).
*   On passe ces scores dans une fonction **Softmax** pour obtenir des probabilités qui somment à 1 (ex: 90% d'attention sur "souris", 10% sur "chat").
*   Enfin, on multiplie ces probabilités par les **Values**. 


> [!TIP]
**Analogie** : Imaginez que vous cherchiez une vidéo sur YouTube. 

> Votre barre de recherche est la **Query**. Les titres des vidéos sur le serveur sont les **Keys**. Le contenu de la vidéo que vous allez finalement regarder est la **Value**. 

L'algorithme d'attention est le moteur de recherche qui fait correspondre votre demande aux titres disponibles.

---
## L'Architecture Transformer complète
Nous allons maintenant faire le tour du propriétaire de ce qu'on appelle "**La cathédrale de calcul**".

### 1. L'empilement global (Figure 1-15)
{{< bookfig src="20.png" week="01" >}}

**Explication** : Elle montre le Transformer comme un assemblage de deux tours : la tour en haut est l'**Encodeur**, celle en bas est le **Décodeur**. 

> [!NOTE]
**À retenir :** Dans l'article original, on utilise 6 blocs identiques pour chaque tour. Aujourd'hui, on peut en utiliser 100 ! L'information monte de couche en couche, devenant de plus en plus abstraite.


### 2. L'intérieur d'un bloc Encodeur (Figure 1-16)

{{< bookfig src="21.png" week="01" >}}

**Explication** : Chaque bloc se compose de deux sous-couches :
*   **Self-Attention** : Le dialogue entre les mots que nous venons de voir.
*   **Feedforward Neural Network** : Un réseau classique qui traite chaque mot indépendamment après qu'il a reçu ses informations de contexte.

> [!IMPORTANT]
Notez bien que l'attention permet la communication, tandis que le Feedforward permet la réflexion individuelle.

### 3. La simultanéité (Figure 1-17)

{{< bookfig src="22.png" week="01" >}}

**Explication** : C'est la figure de la libération ! Elle montre que contrairement aux RNN qui sont "coincés" dans le temps, le Transformer traite tous les mots **en parallèle**. 

> [!NOTE]
**Conséquence pour l'ingénieur** : C'est ce qui permet d'utiliser toute la puissance des GPU (comme notre T4 sur Colab). On peut entraîner sur des milliards de mots parce qu'on ne fait plus la queue mot par mot.

### 4. Le Décodeur et le masquage (Figure 1-18 et 1-19)

{{< bookfig src="23.png" week="01" >}}

**Explication** : Le décodeur (celui qui génère le texte) a une contrainte éthique et mathématique : il ne doit pas lire le futur.
*   On utilise une **Masked Self-Attention**. On "cache" les mots qui n'ont pas encore été générés. 

<a id="fig-1-19"></a>

{{< bookfig src="24.png" week="01" >}}
*   La **Figure 1-19** montre cette matrice triangulaire où les mots ne peuvent regarder que vers le passé. Cela peut favoriser que l'IA apprend vraiment à inventer la suite, et non à simplement copier ce qu'elle a déjà vu.

---
## Analyse de l'efficacité du Transformer
*il y a un "avant" et un "après" 2017.* 

Les avantages du Transformer sont triples :
1.  **L'évanouissement du signal est vaincu** : Dans un RNN, un mot en position 1 avait du mal à parler au mot en position 100. Dans un Transformer, la distance est toujours de **1**. Tous les mots sont connectés par un lien direct. Le "Vanishing Gradient" n'est plus un obstacle majeur.
2.  **La parallélisation massive** : Nous pouvons enfin "nourrir" les modèles avec l'intégralité de Wikipédia, du Web et des bibliothèques mondiales en des temps raisonnables. 
3.  **L'apprentissage de structures complexes** : L'attention permet de capturer la syntaxe, la grammaire et les faits du monde en même temps.

> [!IMPORTANT]
**À retenir :** Le Transformer est l'algorithme le plus efficace jamais créé pour traiter des données séquentielles.

---
## Exemple concret détaillé : La résolution de coréférence
Reprenons notre phrase : « Le chat poursuivait la souris parce qu'**elle** avait faim. »

Dans un Transformer, le mot « elle » va passer par plusieurs couches d'attention :
*   **Couche 1** : « elle » identifie qu'il s'agit d'un pronom féminin.
*   **Couche 2** : « elle » cherche des noms féminins dans la phrase : « chat » (masculin) est écarté, « souris » (féminin) est retenu.
*   **Couche 3** : L'attention se porte sur « faim ». Le modèle "sait" par ses statistiques d'entraînement que celui qui poursuit a souvent faim, mais la grammaire lie « elle » à « souris ». 

**Le résultat** : Le vecteur final de « elle » contiendra 90% d'information provenant de « souris ».

> [!TIP]
Vous voyez ? C'est une intelligence qui émerge de la statistique pure, guidée par une architecture qui favorise les liens logiques.

---
## Le rôle crucial de l'encodage positionnel (Positional Encoding)

> [!WARNING]
**Attention :** Si vous traitez tous les mots en même temps (parallélisme), vous perdez l'ordre des mots. Pour le modèle, « Le chat mange la souris » et « La souris mange le chat » redeviennent identiques !

Pour corriger cela, nous ajoutons aux vecteurs de mots un **signal de position**.
*   Ce n'est pas un simple numéro (1, 2, 3).
*   C'est une fonction sinusoïdale (des ondes) qui permet au modèle de comprendre la distance relative entre les mots.

> [!NOTE]
**Note technique** : Grâce à ces ondes, le modèle sait que le mot 1 est à côté du mot 2, mais loin du mot 50. C'est ainsi que l'on garde le bénéfice du parallèle sans perdre la structure de la séquence.

---
## Éthique et Responsabilité : L'opacité de l'attention

> [!CAUTION]
Nous arrivons au volet éthique. Cette puissance a un prix : l'**interprétabilité**.

Dans une sac de mots (section 1.1), on comprenait pourquoi le modèle décidait. Dans un Transformer de 175 milliards de paramètres, nous sommes face à une "boîte noire".
1.  **Le mirage de l'explication** : On peut visualiser les "cartes d'attention" (voir quels mots le modèle regarde). Mais attention ! Regarder n'est pas comprendre. Parfois, le modèle porte son attention sur une virgule ou un point pour des raisons purement techniques qui n'ont rien à voir avec le sens.
2.  **Les biais amplifiés** : Si le mécanisme d'attention remarque que dans 99% des cas, le mot « infirmière » est lié à « elle », il va renforcer ce lien sémantique de manière automatique. L'attention peut devenir un moteur de stéréotypes ultra-performant.
3.  **La consommation énergétique** : 
> [!IMPORTANT]
> **À retenir :** Le calcul de l'attention est gourmand. Entraîner ces modèles nécessite des milliers de GPU tournant pendant des mois. Votre responsabilité d'expert est aussi d'évaluer le coût écologique de la performance.

---
## Synthèse
Pour réussir votre évaluation, vous devez être capables de dessiner mentalement ce flux :
*   **Input** -> **Embeddings** + **Positional Encoding**.
*   **Encodeur** : Self-Attention + Feedforward (Comprendre le contexte).
*   **Décodeur** : Masked Attention + Cross-Attention (Générer en respectant le contexte).
*   **Output** : Probabilités sur le dictionnaire.

> [!TIP]
**Synthèse** : L'attention pondère les contributions des différentes positions pour construire une représentation contextualisée.

> Comprendre ce mécanisme permet d'analyser le fonctionnement des Transformers et les limites de l'interprétation de leurs poids d'attention.

---
