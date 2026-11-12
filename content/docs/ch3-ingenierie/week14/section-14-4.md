---
title: "14.4 Frontières de la recherche"
weight: 5
---

## Frontières de la recherche

Plusieurs directions de recherche cherchent à améliorer le coût, le traitement du contexte et l’évaluation des modèles. Nous présentons les mélanges d’experts, les calculs supplémentaires à l’inférence et la multimodalité comme des pistes à comparer. Leurs avantages dépendent du protocole d’évaluation ; ils ne constituent pas des garanties générales.

## L'évolution vers la parcimonie : Mixture of Experts (MoE)
L'une des tendances les plus lourdes de la recherche actuelle est le passage des modèles "denses" aux modèles "épars" (sparse). Jusqu'ici, nous avons étudié des modèles où chaque token passe par chaque paramètre (GPT-3, Llama-2). C'est inefficace.

### Le concept de Mixtral et GPT-4

> [!NOTE]
**L'intuition technique :** Imaginez une entreprise de 1000 experts. Si vous avez une question sur la plomberie, allez-vous réunir les 1000 employés dans une salle pour qu'ils vous répondent en chœur ? Non. Vous allez faire appel aux deux meilleurs plombiers. 

C'est le principe du **Mixture of Experts (MoE)**.
*   **Le Router (L'Aiguilleur)** : À chaque couche du Transformer, un petit réseau décide quel "expert" (un sous-ensemble de paramètres) est le plus qualifié pour traiter le token actuel.
*   **L'efficacité** : Un modèle comme Mixtral 8x7B possède 47 milliards de paramètres, mais n'en utilise que 12 milliards pour générer chaque mot. 
*   **Le résultat** : On obtient l'intelligence d'un géant avec la vitesse d'un modèle moyen. 


> [!WARNING]
**Attention :** On croit souvent que MoE réduit la mémoire VRAM nécessaire. C'est faux. 

> Vous devez toujours charger les 47 milliards de paramètres en VRAM, mais le calcul est beaucoup plus rapide car on ne réveille qu'une fraction des neurones.

---
## La conquête du contexte infini : Du "Needle in a Haystack" au million de tokens
En Semaine 5, nous avons parlé du mur de la fenêtre de contexte. Aujourd'hui, des modèles comme Gemini 1.5 Pro ou Claude 3.5 affichent des fenêtres de 200 000 à 2 millions de tokens. 

### Le défi technique : Le "Lost in the Middle"

> [!NOTE]
**À retenir :**Avoir une grande mémoire est inutile si l'IA est incapable d'y retrouver une information précise. 

Les chercheurs utilisent le test "Needle in a Haystack" (Une aiguille dans une botte de foin).
*   On cache un fait absurde (ex: "Le mot de passe de la machine à café est 'Girafe'") au milieu d'un texte de 500 pages. 
*   On demande au modèle : "Quel est le mot de passe ?".
* **Piste de recherche** : Les travaux sur les contextes longs cherchent à améliorer l’exploitation d’informations éloignées. Une grande fenêtre de contexte ne garantit pas que le modèle utilisera correctement chaque information.

---
## Le passage au Raisonnement de Système 2 (Inference-time Scaling)
L'allocation de calcul supplémentaire à l'inférence vise à améliorer la résolution de tâches complexes. Son intérêt doit être évalué en tenant compte de la qualité obtenue, du coût et de la latence.

### Le concept de "Recherche de raisonnement" (Search-based Reasoning)
La recherche s'oriente vers des modèles qui, face à un problème mathématique ou de code, "s'arrêtent pour réfléchir" avant d'émettre le premier token.
*   **Process Reward Models (PRM)** : Au lieu de récompenser le modèle seulement pour la bonne réponse finale (Semaine 12.2), on le récompense pour chaque étape de son raisonnement.
*   **Auto-Correction à l'inférence** : Le modèle génère une idée, la vérifie, remarque une erreur, et recommence son brouillon interne. 

> [!NOTE]
**Analogie:** On passe d'un candidat qui répond du tac au tac à un candidat qui prend une feuille de brouillon et vérifie ses calculs avant de rendre sa copie. 

Cela s'appelle le *Scaling de l'inférence* : on dépense plus d'énergie au moment de la réponse pour obtenir une qualité supérieure.

---
## La Convergence Multimodale Totale : L'IA qui vit dans notre monde
En Semaine 10, nous avons vu des modèles qui "voient" des images. La frontière actuelle est l'IA **Omni-modale**.
*   **Entrée/Sortie Native** : Des modèles comme GPT-4o ne passent plus par des traducteurs (comme le Q-Former de BLIP-2). Ils sont entraînés dès le premier jour sur du texte, de l'audio et de la vidéo simultanément.
*   **La perception du temps** : Un modèle multimodal de nouvelle génération ne voit pas une vidéo comme une suite d'images, mais comme un flux continu. Il peut comprendre l'ironie dans une intonation de voix ou la tension dans un mouvement corporel. 
*   **L'IA incarnée (Embodied AI)** : C'est le lien entre les LLM et la robotique. On utilise le LLM comme le "système de planification" d'un robot (Semaine 14.3) pour qu'il puisse exécuter des ordres vagues comme "Nettoie la cuisine" en comprenant ce qu'est une éponge et où se trouve la saleté.

---
## L'IA pour la Science (AI4Science) : Le nouveau microscope

> [!IMPORTANT]
l'IA ne sert pas qu'à écrire des poèmes ou du code. Elle est en train de résoudre des problèmes que l'humanité traîne depuis des siècles.

1.  **Génomique et Protéines** : En traitant l'ADN comme un langage, des modèles (ex: AlphaFold) prédisent la forme des protéines.  **L'impact** : On gagne des décennies dans la recherche de remèdes contre le cancer ou Alzheimer.
2.  **Science des matériaux** : Utiliser les LLM pour suggérer de nouvelles structures moléculaires pour des batteries plus performantes ou des matériaux captant le CO2.
3.  **Météorologie** : Des modèles de type Transformer (GraphCast) prédisent désormais le climat avec une précision supérieure aux supercalculateurs classiques, pour une fraction du coût énergétique.

---
## Les Défis Éthiques de la Frontière : Vers l'AGI et l'Alignement Super-humain
Nous arrivons à la partie la plus délicate de notre réflexion. Si les LLM deviennent plus intelligents que les humains dans certains domaines, comment les aligner ?

### 1. Le problème de la Super-alignement

> [!IMPORTANT]
**À retenir :**Si un modèle est plus savant que son professeur humain, comment le professeur peut-il savoir si l'élève triche ou s'il est réellement "bon" ? 
*   La recherche travaille sur le **Scalable Oversight** : utiliser des IA pour aider les humains à surveiller des IA encore plus puissantes. 
*    **Risque éthique** : Le risque de perte de contrôle si les deux IA s'allient ou si le système de surveillance devient lui-même biaisé.


### 2. La conscience de soi et l'anthropomorphisme

> [!CAUTION]
Un LLM peut écrire 'Je souffre' ou 'Je suis conscient', mais n'oubliez jamais la Semaine 3. 

Ce ne sont que des probabilités basées sur des textes de science-fiction et de philosophie humaine. 

> [!TIP]
**Conseil méthodologique** : Évaluez les performances observables de l’algorithme et évitez de lui attribuer des intentions ou des émotions.

Cependant, la façon dont nous traitons ces machines change notre propre psychologie. L'IA est un miroir qui nous oblige à redéfinir ce qui nous rend humains.


### 3. L'économie post-travail
Si une IA peut coder, analyser, rédiger et planifier mieux qu'un junior, quel est l'avenir de votre métier ? 
*   **La mutation** : Vous ne serez plus des "producteurs de texte", mais des "curateurs de systèmes". 
*   **La responsabilité** : Documentez les limites du système et les mesures prises pour assurer le suivi de ses résultats.


---
## Conclusion de la semaine

> [!IMPORTANT]
**Synthèse** : Cette semaine a présenté les agents et plusieurs pistes de recherche sur les architectures et l'inférence.


N'oubliez jamais les trois piliers : 
1.  **Les Fondements** pour ne jamais être dupes du marketing. 
2.  **La Science** pour savoir transformer la donnée en connaissance. 
3.  **L'Ingénierie** pour agir de manière responsable et efficace. 


---
**Et pour la suite ?** 
La **semaine 15** propose **deux projets complets** pour mettre en application les notions étudiées dans le cours.
