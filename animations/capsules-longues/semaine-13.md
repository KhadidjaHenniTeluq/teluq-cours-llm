# Semaine 13 : Accélérer la génération avec le cache KV et mesurer les compromis

## Préparation

**739 mots ; durée indicative 06:53 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:59 à 07:26.**

Fichier audio complet possible : `semaine-13.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Un calcul qui se répète

Repère provisoire : 00:00 à 00:57. Audio : `semaine-13-01.wav`.

### Narration

Lorsqu’un décodeur génère un texte, chaque nouveau token s’ajoute au contexte. Une implémentation naïve pourrait recalculer à chaque étape des informations déjà obtenues pour toutes les positions précédentes. Le cache KV évite une partie de ce travail en conservant certaines clés et valeurs calculées dans les couches d’attention. Nous allons suivre trois étapes de génération pour voir ce qui est réutilisé, ce qui reste à calculer et pourquoi cette optimisation consomme de la mémoire. Le but est de comprendre un compromis concret de déploiement. Accélérer une partie du calcul ne signifie pas rendre la génération gratuite ni supprimer les limites de contexte.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : contexte initial → token suivant → contexte agrandi → nouvelle étape.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : La phase de traitement initial

Repère provisoire : 00:57 à 01:55. Audio : `semaine-13-02.wav`.

### Narration

Au départ, le système traite le prompt. Cette phase est souvent appelée prefill. Les représentations des positions fournies permettent de calculer les clés et les valeurs nécessaires dans les différentes couches. Nous les conservons pour les étapes suivantes. Pendant ce traitement initial, plusieurs positions peuvent être calculées ensemble avec le masque approprié. Le coût dépend notamment de la longueur du prompt et de l’architecture. Il faut distinguer ce temps initial du temps nécessaire pour produire ensuite chaque token. Un système peut être rapide sur les tokens suivants tout en imposant une longue attente avant le premier token lorsque le document d’entrée est très volumineux.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : prompt complet → projections → clés et valeurs → cache initial.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Ajouter un token sans tout recommencer

Repère provisoire : 01:55 à 02:56. Audio : `semaine-13-03.wav`.

### Narration

Supposons que les clés et les valeurs des trois premières positions soient déjà conservées. Pour traiter la quatrième position, nous calculons les nouvelles informations nécessaires pour cette position et utilisons les clés et valeurs disponibles des positions autorisées. Nous ajoutons ensuite les nouvelles entrées au cache. Les anciennes valeurs ne sont pas recalculées simplement parce qu’un token a été ajouté, dans le fonctionnement causal standard considéré ici. Cette possibilité vient de la dépendance au passé : une représentation passée ne doit pas dépendre du futur token. Le cache contient des tenseurs intermédiaires précis ; il ne s’agit pas d’une mémoire générale où le modèle écrit des faits en langage naturel.

### Réalisation Manim

Visuel : `cache`. Apparition progressive : cache positions 1 à 3 → nouvelle position 4 → nouvelle clé et valeur → cache positions 1 à 4.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Ce qui reste à calculer

Repère provisoire : 02:56 à 03:54. Audio : `semaine-13-04.wav`.

### Narration

Le cache ne supprime pas la comparaison de la requête actuelle avec les clés pertinentes ni la combinaison des valeurs. Le nouveau token traverse aussi les autres composants du modèle. Plus le contexte conservé est long, plus la lecture et l’utilisation de ces données peuvent coûter cher. Le temps réellement observé dépend du matériel, des transferts de mémoire et de l’implémentation. C’est pourquoi un simple nombre théorique d’opérations ne décrit pas toute la latence. Lorsque vous mesurez un service, séparez le temps jusqu’au premier token, la vitesse de génération et le temps total de réponse. Ces mesures répondent à des expériences utilisateur différentes.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : requête actuelle → clés conservées → poids d’attention → sortie actuelle.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Estimer la mémoire du cache

Repère provisoire : 03:54 à 04:54. Audio : `semaine-13-05.wav`.

### Narration

Pour un exemple simplifié, supposons deux tenseurs, clés et valeurs, deux couches, cent tokens et une dimension totale des clés ou des valeurs de seize par couche. Avec deux octets par valeur et un seul élément dans le lot, le stockage vaut deux fois deux fois cent fois seize fois deux, soit douze mille huit cents octets. Ce calcul exclut les autres objets et les surcoûts du système. Dans une architecture réelle, il faut utiliser le nombre de têtes de clés et valeurs, leur dimension, le lot et la précision effective. Certaines architectures partagent des clés et valeurs entre têtes de requêtes, ce qui modifie le calcul.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : 2 tenseurs → couches × tokens → dimension KV → octets par valeur.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Servir plusieurs demandes

Repère provisoire : 04:54 à 05:53. Audio : `semaine-13-06.wav`.

### Narration

Lorsque plusieurs utilisateurs génèrent en même temps, chaque séquence peut demander son propre espace de cache. Les longueurs et les moments de fin varient. Un ordonnanceur peut regrouper ou réorganiser le travail pour mieux utiliser le matériel, mais il doit gérer les ressources et la séparation entre demandes. Les optimisations ne remplacent pas les règles de confidentialité et de conservation des données. Pour dimensionner un service, testez des longueurs représentatives et plusieurs demandes simultanées. Mesurez la mémoire maximale et les temps d’attente, pas seulement le meilleur débit obtenu sur un exemple court. Un réglage efficace pour une démonstration unique peut mal convenir à une classe entière.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : requête A → requête B → caches distincts → mémoire totale.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Identifier le bon compromis

Repère provisoire : 05:53 à 06:53. Audio : `semaine-13-07.wav`.

### Narration

Voici la question finale : si nous doublons le nombre de tokens conservés dans le cache, que devient son stockage dans notre estimation simplifiée, toutes choses égales par ailleurs ? Il double. Cela ne permet pas de déduire automatiquement que le temps total double, car plusieurs composantes interviennent. Pour votre exercice, préparez un tableau avec trois longueurs de prompt et relevez le temps initial, la vitesse de génération et la mémoire utilisée dans le même environnement. Interprétez les différences avant de choisir un réglage. Le cache KV est un exemple de compromis entre mémoire et recalcul, que l’on doit examiner avec des mesures adaptées à l’usage prévu.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : latence → débit → mémoire → qualité préservée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
