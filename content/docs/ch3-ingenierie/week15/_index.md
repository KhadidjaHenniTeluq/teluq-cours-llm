---
title: "Semaine 15 : Projets et consolidation"
weight: 5
bookCollapseSection : true
---

# Semaine 15 : Consolidation et préparation à l’examen

## Projets et consolidation

Cette semaine relie les notions du cours à deux projets : minGPT et un assistant documentaire. Commencez par identifier les entrées, les traitements et les sorties. La lecture détaillée de toutes les classes constitue un approfondissement.

## 15.1 La revue des Trois Piliers
si vous devez retenir une seule structure pour votre examen, c'est celle-ci. Pour devenir un architecte de l'intelligence, vous devez naviguer avec aisance entre ces trois mondes que nous avons explorés.

### Pilier 1 : Les Fondements (Semaines 1 à 5)
C'est la mécanique du cerveau. 

*   **La naissance du sens** : De la tokenisation (Semaine 2) au vecteur de sens (Embedding). 

> [!NOTE]
**Note** : Rappelez-vous que le Transformer est aveugle à l'ordre sans l'encodage positionnel (Semaine 3.2). 

*   **Le moteur d'Attention** : Le trio Q, K, V. Vous devez être capables d'expliquer comment l'attention contextuelle résout la polysémie (ex: l'exemple "avocat" de votre Évaluation 1). 

*   **Les deux branches** : Pourquoi utiliser BERT pour classer et GPT pour écrire ? (Semaines 4 et 5).


### Pilier 2 : La Science (Semaines 6 à 10)
C'est l'IA face à l'information. 
*   **La navigation** : La similarité cosinus (Semaine 6.2) et la recherche vectorielle (FAISS). 
*   **L'organisation** : Le clustering sémantique et la découverte automatique de thèmes avec BERTopic (Semaine 7). 
*   **L'ancrage (RAG)** : Comment injecter des preuves documentaires pour réduire certaines hallucinations et faciliter leur vérification (Semaine 9). 

> [!WARNING]
**Avertissement** : Un bon RAG ne se mesure pas seulement à sa réponse, mais à la fidélité de ses citations.


### Pilier 3 : L'Ingénierie (Semaines 11 à 14)
C'est l'IA face au monde réel.
*   **L'adaptation** : LoRA et QLoRA. Comment modifier un géant avec 0,1% de ses poids (Semaine 11). 
*   **L’alignement** : Le DPO adapte le modèle à partir de préférences documentées (semaine 12).
*   **La production** : L'optimisation de l'inférence (KV Cache) et la sécurité contre les injections de prompts (Semaine 13). 

> [!IMPORTANT]
**À retenir :** une IA de production doit être "Honnête, Utile et Inoffensive" (HHH).

---

## 15.2 Astuces et stratégies pour l'Examen Final

L'examen ne testera pas uniquement votre capacité à mémoriser des définitions, mais également votre aptitude à prendre des décisions techniques. 

1.  **Lisez bien les contraintes matérielles** : Si une question mentionne un "petit GPU", ne proposez pas un fine-tuning complet. Pensez à LoRA et à la quantification (Semaine 11).
2.  **Justifiez par les métriques** : Ne dites pas "le modèle est bon". Dites "le score de Faithfulness est de 0.9, ce qui indique une bonne fidélité selon ce protocole, à confirmer par une inspection des réponses" (Semaine 9.3).
3.  **Identifiez les biais** : Gardez toujours un œil sur l'éthique. Si vous concevez un système de recrutement, mentionnez comment vous allez auditer les biais des embeddings (Semaine 2.4).
4.  **Représentez le traitement** : Pour les questions d'architecture, décrivez le parcours des tokens, de l'entrée utilisateur jusqu'à la LM Head (section 3.4).

> [!TIP]
**Conseil de révision** : Vérifiez que vous pouvez expliquer les méthodes, justifier les choix techniques et identifier les limites des systèmes étudiés.

---

**Mots-clés de la semaine** : Synthèse, Consolidation, Piliers LLM, Audit final, Stratégies d'examen, Rétrospective.

## Repères de lecture

**Prérequis à revoir :** Pouvoir suivre une fonction Python et expliquer un pipeline RAG.

**À comprendre en premier :** Repérer entrées, cibles, perte et mise à jour dans une boucle d’entraînement. Décrire le trajet d’une question dans un assistant documentaire.

**À lire ensuite pour approfondir :** Lecture détaillée de toutes les classes et orchestration distribuée. Ces repères indiquent un ordre de lecture ; les consignes des évaluations restent la référence pour le travail à remettre.

**Question de vérification :** Où vérifieriez-vous les données et les résultats dans chacun des deux projets ?

## Animations de la semaine

Ces vidéos expliquent les concepts pas à pas, avec une transcription dans chaque section.

- [minGPT : de la prédiction à la mise à jour]({{< relref "/docs/ch3-ingenierie/week15/mingpt/section-2.md" >}})
