---
title: "4.1 La famille BERT"
weight: 2
---

{{< katex />}}

## La famille BERT

BERT est un modèle encodeur qui construit des représentations contextuelles en utilisant les positions à gauche et à droite. Son préentraînement comprend la reconstruction de tokens sélectionnés. Pour une tâche comme la classification, on ajoute ou adapte une couche de sortie. L’absence de masque causal ne signifie pas l’absence de tout masque, notamment pour le padding.

{{< bookfig src="25.png" week="04" >}}

## Animation : BERT et le token masqué

{{< conceptvideo name="bert" title="BERT et le token masqué" >}}
L’exemple « Le [MASK] miaule. » illustre l’utilisation du contexte à gauche et à droite. Une distribution fictive attribue 80 % à « chat », 15 % à « chien » et 5 % aux autres candidats. La perte est calculée sur les positions sélectionnées pour la reconstruction. Masquer un token d’entrée est différent du masque causal, qui interdit certaines connexions d’attention. Cette illustration simplifie la procédure de corruption utilisée pendant le préentraînement de BERT.
{{< /conceptvideo >}}

## Le token [CLS] : Le porte-parole de la phrase
Dans un modèle de représentation, nous ne voulons pas générer la suite du texte, nous voulons un "résumé mathématique" de ce que le texte raconte. Pour cela, BERT introduit une convention : le token **[CLS]** (pour *Classification*).

> [!CAUTION]
> **Attention** : Le token `[CLS]` est un token spécial placé au début de l'entrée. Dans BERT, l'attention bidirectionnelle permet à sa représentation d'intégrer des informations provenant des autres positions.

> [!NOTE]
**La règle d'or :** À la sortie de la 12ème couche, le vecteur correspondant au token `[CLS]` est utilisé comme la représentation compressée de toute la séquence. C'est ce vecteur que nous brancherons sur un classifieur pour décider si une critique est positive ou négative.

## Apprendre par les trous : Le Masked Language Modeling (MLM)
Comment entraîne-t-on un modèle à "comprendre" sans lui donner de labels ? On utilise un jeu d'enfant : le texte à trous. C'est le **Masked Language Modeling**, illustré dans les **Figures 4-2 et 4-3**.

{{< bookfig src="26.png" week="04" >}}
{{< bookfig src="27.png" week="04" >}}


Le processus se déroule ainsi :
1.  On prend une phrase normale (ex: "Le chat boit du lait").
2.  On cache aléatoirement 15% des mots avec un token spécial **[MASK]**.
3.  On demande au modèle de deviner ce qu'il y avait sous le masque.

Pour réussir, BERT est forcé d'apprendre la grammaire ("Le" suggère un nom masculin), la syntaxe, et surtout la sémantique ("boit" et "lait" sont fortement liés au mot caché "chat").

## L'évolution de la lignée : De RoBERTa à DeBERTa
Depuis la sortie de BERT par Google en 2018, la famille s'est agrandie. Regardez la **Figure 4-4 : Timeline des modèles BERT-like**. Chaque nouveau-venu a apporté une innovation majeure.

{{< bookfig src="91.png" week="04" >}}

### 1. RoBERTa (Facebook AI)
RoBERTa est la preuve que "plus c'est long, meilleur c'est". Les chercheurs ont repris l'architecture de BERT mais l'ont entraînée sur beaucoup plus de données, pendant plus longtemps, et en supprimant une tâche d'entraînement secondaire jugée inutile (la *Next Sentence Prediction*). 
> [!NOTE]
**Notez bien :** RoBERTa est souvent le choix par excellence pour la classification aujourd'hui car ses représentations sont plus robustes.

### 2. DistilBERT (Hugging Face)
« Tout le monde n'a pas un supercalculateur dans son garage ! » DistilBERT utilise une technique appelée "distillation de connaissances". On prend un gros BERT (le professeur) et on entraîne un petit BERT (l'élève) à imiter ses réponses. 
*   **Résultat** : 40% plus petit, 60% plus rapide, tout en conservant 97% des performances. C'est le modèle idéal pour les applications mobiles ou les serveurs à faibles ressources.

### 3. ALBERT et DeBERTa
*   **ALBERT** : Utilise des astuces mathématiques pour réduire le nombre de paramètres sans perdre en puissance.
*   **DeBERTa** : Introduit l'attention "désentrelacée" (*disentangled attention*). Il sépare le contenu du mot de sa position relative. C'est actuellement l'un des modèles les plus performants sur les benchmarks de compréhension de lecture.

## Tableau comparatif de la famille BERT

| Modèle | Innovation Clé | Cas d'usage idéal |
| :--- | :--- | :--- |
| **BERT** | Premier modèle bidirectionnel massif | Baseline historique, recherche générale |
| **RoBERTa** | Entraînement optimisé, plus de données | Classification haute performance |
| **DistilBERT** | Distillation (plus léger/rapide) | Inférence en temps réel, Edge computing |
| **DeBERTa** | Attention désentrelacée | Tâches de raisonnement complexe |


## Éthique et Transparence : Le miroir bidirectionnel
> [!WARNING]
**soyez vigilants!** 
Parce que BERT regarde la phrase dans les deux sens, il est extrêmement sensible au contexte. Mais ce contexte contient nos biais. Si BERT voit 100 000 fois "L'infirmière est entrée dans la pièce" et "Le médecin est entré dans la pièce", l'embedding du mot `[MASK]` dans "Le [MASK] est entré..." sera statistiquement biaisé vers le genre masculin ou féminin selon la profession.

> [!IMPORTANT]
**À retenir :** Ces modèles de représentation ne sont pas des arbitres de vérité. Ce sont des miroirs statistiques de nos écrits. Lorsque vous utilisez BERT pour filtrer des CV ou analyser des sentiments, vous devez auditer les biais que le modèle pourrait avoir "appris" durant son *MLM*. 

---
