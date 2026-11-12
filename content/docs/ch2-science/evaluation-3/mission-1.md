---
title: "Mission 1. Secure Ingestion"
weight: 1
---


# Évaluation 3 : Le Gardien de la Vérité
## Mission 1 : Secure Ingestion, Permissions et filtrage des résultats

Construisez la base documentaire du système RAG et filtrez ses résultats selon les métadonnées de permission. Distinguez ce filtre d’un contrôle d’accès complet.

## Objectif de la Mission
L'étudiant doit mettre en place la brique d'ingestion d'un système RAG pour une entreprise de Cloud Computing. Le défi majeur est d'implémenter un **filtrage par métadonnées**. Contrairement à une recherche classique, le `Retriever` doit être capable d'exclure dynamiquement des documents confidentiels si l'utilisateur actuel n'a qu'un profil "Guest" ou "Public".

---

## Le Concept technique : Metadata Filtering
Dans un pipeline RAG standard, le modèle cherche partout. Mais en production, nous utilisons les métadonnées pour réduire le "bruit" et augmenter la sécurité.

* **Filtrage des résultats** : Dans l’intégration FAISS de LangChain utilisée ici, la recherche récupère des candidats, puis le filtre examine leurs métadonnées. Ce comportement ne constitue pas un contrôle d’accès avant la recherche. Un système réel doit faire appliquer les permissions par l’application et, si nécessaire, isoler les index selon les droits.
*   **Intégrité sémantique** : En filtrant par "Catégorie", on évite que l'IA ne confonde une procédure de "Sécurité Incendie" avec une procédure de "Cybersécurité" simplement parce que les deux partagent le mot "Sécurité".

---

## 1. Configuration de l'environnement (Setup)
*Préparez votre session Colab sur **GPU T4**. Nous utilisons `langchain` pour orchestrer les documents et `sentence-transformers` pour la précision sémantique.*

```python
# Installation des dépendances (Environnement visé : Colab T4)
# !pip install -q langchain langchain-community langchain-classic sentence-transformers faiss-cpu ragas datasets langchain-openai openai

import torch
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.docstore.document import Document

# Hardware Check
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Audit matériel : Moteur d'embedding prêt sur {device}")
```

---

## 2. The English Knowledge Base (KB)
*Voici les données stratégiques de l'entreprise. Notez bien les différents niveaux de `access_level`.*


<!-- TODO - Add colab link -->
Le code et les données nécessaires sont présentés ci-dessous. Le lien vers un notebook dédié sera ajouté lorsqu’il sera disponible.


```python
raw_cloud_data = [
    {
        "title": "Public Cloud Pricing",
        "content": "Our basic cloud instance costs $0.05 per hour. Billing is calculated monthly based on actual usage. Free tier includes 5GB of storage.",
        "access_level": "public",
        "topic": "billing"
    },
    {
        "title": "Internal Server Maintenance",
        "content": "Maintenance windows are scheduled every Sunday at 02:00 UTC. Admins must verify the backup integrity before initiating the reboot sequence.",
        "access_level": "internal",
        "topic": "ops"
    },
    {
        "title": "Confidential Security Keys",
        "content": "The master encryption keys for the S3-equivalent buckets are stored in the hardware security module (HSM) located in the Phoenix datacenter. ACCESS RESTRICTED TO CTO ONLY.",
        "access_level": "confidential",
        "topic": "security"
    },
    {
        "title": "Employee Handbook - Remote Work",
        "content": "Employees are allowed to work remotely 3 days a week. High-speed internet is required for accessing internal VPN resources.",
        "access_level": "internal",
        "topic": "hr"
    }
]
```

---

## 3. Vos Tâches de Mission

### Tâche 1 : Ingestion avec Tags de Sécurité
Vous devez transformer `raw_cloud_data` en une liste d'objets `Document`. 

> [!IMPORTANT]
**À retenir :** Chaque document doit porter dans ses métadonnées les clés `access_level` et `topic`. 

> [!WARNING]
**Attention :** Si vous oubliez le tag d'accès, votre filtrage en Mission 2 sera inopérant.

### Tâche 2 : Indexation Vectorielle (Dense Index)
1.  Initialisez un modèle d'embedding performant (ex: `all-MiniLM-L6-v2`).
2.  Créez une base FAISS à partir de vos documents.
3.  Vérifiez la taille de votre index : vous devez avoir exactement 4 vecteurs à ce stade.

### Tâche 3 : Simulation du Profil Utilisateur
Créez une variable `current_user_clearance = "public"`. 
Votre code doit être prêt à passer ce filtre au `Retriever` LangChain pour que les documents "internal" et "confidential" ne soient pas transmis au générateur après la prochaine mission.

---


## Mes avertissements

> [!WARNING]
>*   **Erreur fréquente :** Tenter de filtrer les résultats *après* la recherche (Post-filtering). Si votre recherche ramène 5 documents et qu'ils sont tous confidentiels, après filtrage, il ne vous restera plus rien à donner au LLM ! Le filtrage doit se faire **avant** ou **pendant** la recherche vectorielle.
>*   **Confidentialité :** En production, les métadonnées sont souvent stockées en clair. Ne mettez jamais de secrets (mots de passe) dans les métadonnées elles-mêmes, utilisez-les uniquement pour le routage de l'information.


> [!TIP]
**Conseil méthodologique:** Regardez comment LangChain gère les dictionnaires de filtres. C'est une syntaxe proche de MongoDB qui permet de faire des recherches très puissantes (ex: 'Access' est 'Public' ET 'Topic' est 'Billing').

---

**Une fois que vos documents sont indexés et sécurisés, nous passerons à la Mission 2 : La Réécriture de Requête et l'Expansion Sémantique pour améliorer le rappel.**

Référence technique : [implémentation FAISS de LangChain](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/vectorstores/faiss.py). Vérifiez le comportement de la version utilisée dans le laboratoire.
