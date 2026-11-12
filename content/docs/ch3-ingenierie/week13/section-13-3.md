---
title: "13.3 Considérations légales"
weight: 4
---

## Identifier les règles applicables

Un projet de LLM utilise des données, des logiciels et des modèles soumis à des conditions différentes. Avant un déploiement, il faut identifier le territoire concerné, le rôle de l’organisation, les personnes touchées et l’usage prévu. Un même outil peut être soumis à des obligations différentes selon le contexte.

Cette section donne des repères de lecture. Les textes applicables et leurs dates d’entrée en application doivent être vérifiés pour chaque projet.

## Renseignements personnels au Québec

Les organisations doivent examiner comment les renseignements sont collectés, utilisés, communiqués, conservés et détruits. Cette analyse concerne les données d’entraînement, mais aussi les prompts, les documents d’un RAG et les journaux d’utilisation. Il faut distinguer le cadre des organismes publics de celui des entreprises privées. La [Commission d’accès à l’information du Québec](https://www.cai.gouv.qc.ca/protection-renseignements-personnels/information-entreprises-privees) fournit les ressources de référence et des liens vers les obligations applicables.

Pour les exercices, employez des données fictives ou explicitement autorisées. Un embedding ou une pseudonymisation ne doit pas être considéré automatiquement comme une anonymisation.

## Un exemple international : l’AI Act européen

L’AI Act distingue notamment des pratiques interdites, des systèmes présentant des risques élevés, des obligations de transparence et des obligations visant certains modèles d’IA à usage général. Les obligations dépendent du rôle de l’acteur et des conditions prévues par le règlement. La présence d’un LLM dans une application ne suffit pas à déterminer sa catégorie.

Pour un projet lié au marché européen, consultez la [présentation officielle de la Commission européenne](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) et le texte auquel elle renvoie. Vérifiez le calendrier applicable plutôt que de supposer que toutes les dispositions s’appliquent au même moment. D’autres règles, dont celles sur les données personnelles, peuvent aussi s’appliquer.

## Licences et droits d’utilisation

Vérifiez séparément les conditions du code, des poids du modèle, du jeu de données et du service utilisé. Un téléchargement libre ne signifie pas que tous les usages sont autorisés. La possibilité d’exploiter une sortie et les risques de reproduction d’un contenu protégé doivent aussi être examinés selon le contexte juridique.

## Questions à documenter avant un déploiement

- Quelles données entrent dans le système et qui peut y accéder ?
- Où sont-elles envoyées et pendant combien de temps sont-elles conservées ?
- Quelles licences et conditions contractuelles s’appliquent ?
- Quelles erreurs pourraient toucher les personnes concernées ?
- Qui traite les demandes, les incidents et les contestations ?

La section suivante traite du suivi technique du système. Cette documentation permet de relier les choix d’architecture aux responsabilités de l’organisation.
