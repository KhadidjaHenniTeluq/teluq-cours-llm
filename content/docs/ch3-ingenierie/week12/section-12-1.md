---
title: "12.1 Le besoin d'alignement"
weight: 2
---

{{< katex />}}

## Le besoin d'alignement

Suivre une instruction ne suffit pas pour produire une réponse utile, exacte et adaptée au contexte. Les méthodes d’alignement utilisent des exemples ou des préférences pour orienter le comportement du modèle. Les critères choisis et la population qui les définit influencent le résultat.

## Analyse du processus d'évaluation
Pour résoudre ces problèmes, nous devons introduire un mécanisme de jugement. Regardons ensemble la **Figure 12-1 : Utilisation d'un évaluateur de préférences** . 

{{< bookfig src="278.png" week="12" >}}

**Explication de la Figure 12-1** : Cette illustration nous montre une interaction fondamentale. Le modèle génère une réponse (A) à un prompt. Un évaluateur (qu'il soit humain ou une autre IA plus puissante) attribue un score de qualité, par exemple 4 sur une échelle de 1 à 6.

> [!NOTE]
**À retenir** : Le SFT utilise des réponses de référence. L’apprentissage par préférences compare des réponses selon des critères d’évaluation définis.

La suite logique est présentée dans la **Figure 12-2 : Mise à jour basée sur le score** .

{{< bookfig src="279.png" week="12" >}}

*   **Si le score est élevé** : On envoie un signal au modèle pour lui dire "Fais plus de choses comme ça". Mathématiquement, on augmente la probabilité des tokens qui ont mené à cette réponse.
*   **Si le score est bas** : On lui dit "Évite ce comportement". On réduit la probabilité de cette séquence dans le futur.

> [!WARNING]
**Attention :** Beaucoup pensent que cette étape change les connaissances du modèle. Non, elle change son **comportement**. Elle ajuste le "curseur" entre l'arrogance, l'humilité, la concision et la verbosité.

---
## La genèse de l'alignement : L'histoire de ChatGPT
Pour comprendre l'impact massif de l'alignement, nous devons regarder comment OpenAI a créé ChatGPT.

{{< bookfig src="108.png" week="12" >}}

**Explication de la Figure 12-3** : La première phase utilise des réponses de référence pour l'adaptation supervisée (SFT). L'apprentissage à partir de préférences complète ensuite cette étape.
<a id="fig-12-4"></a>

{{< bookfig src="109.png" week="12" >}}

**Explication de la Figure 12-4** : C'est le tournant historique. Au lieu de demander aux humains d'écrire, on leur demande de **classer**. On présente à un annotateur humain trois réponses générées par l'IA (A, B et C) et on lui demande de les ranger par ordre de préférence (ex: $C > B > A$). 

> [!IMPORTANT]
**À retenir :**Les humains sont très mauvais pour donner une note absolue (est-ce un 7.2 ou un 7.3/10 ?), mais ils sont excellents pour comparer deux choses ("Je préfère B à A").

> Cette comparaison est la donnée la plus pure et la plus fiable que nous puissions extraire du cerveau humain pour guider une IA.

---
## Le triptyque HHH : Helpful, Honest, Harmless
L'alignement vise à équilibrer trois objectifs souvent contradictoires, connus sous le nom de cadre "HHH" :

1.  **Helpful (Utile)** : Le modèle doit répondre à la question et fournir l'aide demandée. Un modèle trop aligné sur la sécurité pourrait refuser de répondre à tout par peur, devenant inutile.
2.  **Honest (Honnête)** : Le modèle doit admettre ses limites. S'il ne sait pas, il doit le dire plutôt que d'halluciner. Il doit être fidèle aux faits présents dans son contexte.
3.  **Harmless (Inoffensif)** : Le modèle ne doit pas aider à fabriquer des armes, ne doit pas tenir de propos haineux et ne doit pas encourager l'automutilation. 

> [!IMPORTANT]
l'équilibre est précaire.  

> Si vous poussez trop le curseur "Harmless", vous obtenez un modèle "lobotomisé" qui s'excuse pour tout. Si vous poussez trop le curseur "Helpful", vous obtenez un modèle qui vous explique comment pirater le Wi-Fi de votre voisin simplement parce que vous le lui avez demandé gentiment. L'alignement est l'art de trouver le "point de rosée" entre ces exigences.

---
## Éthique et Responsabilité : Qui définit la "Préférence" ?

> [!IMPORTANT]
**Éthique ancrée** : Posez-vous toujours la question : qui est l'humain derrière le feedback ?

L'alignement n'est pas une vérité mathématique universelle ; c'est un choix sociétal. 
1.  **Le biais des annotateurs** : Si les personnes qui classent les réponses (Figure 12-4) sont toutes issues de la même culture, du même milieu social ou de la même mouvance politique, le modèle va "hériter" de leur vision du monde. Il considérera comme "préférable" ce que ce groupe précis considère comme bon.
2.  **L'érosion de la diversité** : En forçant un modèle à toujours répondre d'une certaine façon "polie" ou "standard", nous risquons de perdre la richesse des dialectes, des styles et des perspectives minoritaires.
3.  **La manipulation** : Un gouvernement ou une entreprise pourrait utiliser l'alignement pour faire en sorte que l'IA ne critique jamais ses actions, transformant un outil d'information en outil de propagande. 

> [!TIP]
**Synthèse** : Explicitez les objectifs de l'alignement et les critères utilisés pour constituer les données de préférence.

---
## Vers l'automatisation : Le passage au Reward Model
Le problème de l'alignement par les humains est son coût. On ne peut pas demander à des milliers de personnes de classer des millions de réponses indéfiniment. 
C'est pourquoi nous utilisons la phase d'alignement pour entraîner un **Reward Model** (Modèle de récompense). 
*   On utilise les classements humains ($C > B > A$) pour entraîner un petit modèle BERT (Semaine 4) à prédire le score qu'un humain donnerait. 
*   Une fois ce "juge artificiel" entraîné, il peut noter des milliards de réponses à la place des humains. 

---
C'est cette transition entre le jugement humain et le calcul de récompense automatique qui nous mène au *RLHF*, que nous étudierons dans la prochaine section . Vous voyez ? Tout ce que nous avons appris depuis la Semaine 1 s'assemble enfin comme les pièces d'un puzzle géant.