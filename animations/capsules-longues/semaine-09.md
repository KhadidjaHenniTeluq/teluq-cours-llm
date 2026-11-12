# Semaine 9 : Construire un RAG et repérer l’origine de ses erreurs

## Préparation

**735 mots ; durée indicative 06:51 à 120 mots/minute, pauses comprises. Plage à 110–140 mots/minute : 05:57 à 07:23.**

Fichier audio complet possible : `semaine-09.wav`. Pour le rendu synchronisé par séquence, fournir les fichiers numérotés indiqués ci-dessous. Ne pas lire les titres ni les indications de réalisation.

## Séquence 1 : Répondre à partir de documents

Repère provisoire : 00:00 à 01:01. Audio : `semaine-09-01.wav`.

### Narration

Supposons qu’un étudiant demande si un travail peut être remis en retard. Le modèle possède des connaissances générales, mais il ne connaît pas nécessairement le règlement actuel de ce cours. Un système RAG recherche des passages dans une base documentaire, les ajoute au contexte de génération et produit une réponse à partir de ces éléments. Nous allons suivre ce parcours et distinguer deux grandes familles d’erreurs : ne pas retrouver l’information utile et mal répondre malgré une information disponible. Cette distinction est essentielle. Modifier le prompt de génération ne corrigera pas un document absent de l’index, et améliorer la recherche ne garantit pas que la réponse citera correctement ses sources.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : question étudiant → règlement du cours → passages → réponse citée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 2 : Préparer une base fiable

Repère provisoire : 01:01 à 01:59. Audio : `semaine-09-02.wav`.

### Narration

Avant de générer une réponse, il faut préparer la base. Conservons le règlement officiel, sa date et sa version. Un ancien règlement encore présent peut créer une contradiction. Nous découpons ensuite le texte en passages qui gardent suffisamment de contexte, puis calculons leurs vecteurs. Les métadonnées doivent permettre de retrouver le document original et, lorsque c’est nécessaire, de gérer les permissions. Un identifiant de source stable aide à contrôler les citations. Le pipeline d’indexation mérite d’être testé : une mauvaise extraction peut perdre un tableau ou une négation. Une réponse erronée peut donc commencer par un problème de données bien avant l’appel au modèle.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : document officiel → version et date → passages → index.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 3 : Retrouver et éventuellement reclasser

Repère provisoire : 01:59 à 02:57. Audio : `semaine-09-03.wav`.

### Narration

À l’arrivée de la question, le système recherche des passages candidats. Il peut combiner recherche sémantique et recherche lexicale pour tenir compte du sens et des termes exacts. Un reclassement peut ensuite examiner plus finement quelques couples question-passage. Cette étape ajoute du calcul, et son intérêt doit être mesuré. Si nous récupérons vingt passages mais n’en transmettons que trois, il faut vérifier lesquels sont conservés. Le passage contenant l’exception aux retards peut être moins visible que la règle générale. Ajouter toujours plus de documents n’est pas une solution automatique : cela augmente le contexte, le coût et parfois les contradictions présentées au générateur.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : question → recherche initiale → candidats → reclassement.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 4 : Construire le contexte de réponse

Repère provisoire : 02:57 à 03:56. Audio : `semaine-09-04.wav`.

### Narration

Nous présentons maintenant au modèle la question et les passages sélectionnés avec leurs identifiants. La consigne lui demande de répondre à partir de ces éléments et de signaler une information insuffisante. Les passages restent des données, même s’ils contiennent une phrase ressemblant à une instruction. La réponse doit distinguer ce qui est explicitement écrit de ce qui n’est pas établi. Si le règlement indique seulement qu’une demande de prolongation doit être faite avant l’échéance, le modèle ne doit pas inventer une prolongation automatique de trois jours. La fluidité de la phrase finale ne compense pas cette différence entre une demande possible et une autorisation accordée.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : consigne → passage A → passage B → question.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 5 : Suivre un exemple contradictoire

Repère provisoire : 03:56 à 04:54. Audio : `semaine-09-05.wav`.

### Narration

Prenons un cas plus difficile. Un ancien document mentionne un délai de quarante-huit heures, tandis que la version actuelle demande une autorisation préalable sans délai automatique. Si les deux passages arrivent dans le contexte, le système doit pouvoir identifier leur provenance et appliquer la règle prévue pour les versions. Il ne doit pas choisir le nombre le plus commode. Si la priorité des sources n’est pas établie, il peut signaler la contradiction plutôt que trancher sans justification. Cette situation montre pourquoi les dates et les règles documentaires font partie de la conception. Le RAG n’efface pas les contradictions déjà présentes dans les données.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : ancien : 48 heures → nouveau : demande préalable → date de version → réponse prudente.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 6 : Évaluer deux étapes séparément

Repère provisoire : 04:54 à 05:52. Audio : `semaine-09-06.wav`.

### Narration

Évaluons d’abord la recherche : le passage nécessaire apparaît-il parmi les résultats transmis ? Évaluons ensuite la réponse : répond-elle à la question, ses affirmations sont-elles soutenues par les passages et les citations sont-elles exactes ? Une réponse peut être fidèle au contexte tout en évitant la question. Elle peut aussi citer un texte qui ne justifie pas la conclusion. Des évaluateurs automatiques facilitent le suivi, mais leurs scores dépendent du protocole et peuvent contenir des erreurs. Gardons un ensemble d’exemples vérifiés manuellement. Un score de fidélité parfait sur quelques tests ne démontre pas que toutes les réponses futures seront vraies ou suffisamment complètes.

### Réalisation Manim

Visuel : `comparison`. Apparition progressive : passage retrouvé ? → affirmations étayées ? → réponse pertinente ? → citations correctes ?.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.

## Séquence 7 : Diagnostiquer un échec

Repère provisoire : 05:52 à 06:51. Audio : `semaine-09-07.wav`.

### Narration

Pour l’exercice final, imaginez que le modèle annonce une prolongation automatique qui n’existe pas. Examinez successivement la base, les passages récupérés, le contexte envoyé et la réponse. Si la bonne version n’est pas indexée, corrigez les données. Si elle existe mais n’est pas retrouvée, examinez le découpage et la recherche. Si elle est fournie mais mal interprétée, étudiez la génération et les tests. Cette démarche évite de modifier tout le système à l’aveugle. Retenez enfin qu’un RAG relie des documents à une génération ; il réduit certains manques de contexte, mais demande une évaluation de bout en bout pour établir sa qualité sur les usages prévus.

### Réalisation Manim

Visuel : `flow`. Apparition progressive : source absente → mauvais passage → mauvaise génération → action ciblée.

Faire apparaître les éléments au fil de l’explication ; prévoir six secondes de lecture ou de réflexion à la fin. Les repères de phrases seront ajustés à l’enregistrement réel.
