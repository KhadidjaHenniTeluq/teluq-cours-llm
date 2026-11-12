# Capsules longues du cours

Ce dossier contient les scripts développés pour **une capsule par semaine**.
Chaque capsule comprend une narration complète, un exemple, des limites à retenir
et une question de compréhension. Les semaines 11 et 12 comportent neuf séquences ;
les autres en comportent sept. Au total : 15 capsules et 109 séquences.

Les durées prévues vont de **6 min 33 à 8 min 54**, à 120 mots par minute avec
six secondes de lecture ou de réflexion après chaque séquence. À un débit compris
entre 110 et 140 mots par minute, toutes les capsules restent entre 5 et 15 minutes.
Les nombres de mots traitent les nombres et expressions comme des mots écrits ;
la durée effective doit donc être mesurée après enregistrement.

## Quels fichiers lire ?

- `PLAN-DES-CAPSULES.md` : sujets, volumes et durées estimées.
- `NARRATIONS-COMPLETES.md` : les quinze narrations réunies.
- `semaine-01.txt` à `semaine-15.txt` : uniquement les textes à prononcer.
- `semaine-01.md` à `semaine-15.md` : narration et découpage visuel détaillé.
- `textes-par-sequence/` : les mêmes textes séparés pour enregistrer par séquence.
- `catalogue.json` : données structurées utilisées par les scènes.
- `scenes.py` : code Manim, schémas progressifs et exemples numériques.
- `render.py` : rendu de la capsule choisie, silencieux ou avec les WAV par séquence.

Les 20 animations courtes existantes restent dans le cours comme illustrations.
Ces nouvelles capsules ne sont pas encore des vidéos finales avec voix. Aucun
fichier du site n’est remplacé par le script de rendu.

## Enregistrer sa voix

Vous pouvez fournir **un audio par semaine**, par exemple `semaine-01.wav`, en WAV,
MP3 ou M4A. Lire naturellement ; marquer une courte pause entre les paragraphes.
Ne pas lire les titres ni les indications de réalisation.

Pour faciliter le montage, vous pouvez aussi enregistrer séparément les séquences :
`semaine-01-01.wav`, `semaine-01-02.wav`, jusqu’à `semaine-01-07.wav`.
Les semaines 11 et 12 vont jusqu’à `-09.wav`. Les textes correspondants figurent
dans `textes-par-sequence/`.

Un audio complet devra être repéré et découpé pour synchroniser les séquences.
Le rendu automatique ci-dessous attend des **WAV déjà séparés**. Il conserve la
vitesse de la voix et adapte la durée de chaque séquence à son fichier. Les
apparitions des objets sont encore réparties régulièrement dans la séquence ;
leur alignement avec les phrases sera affiné après écoute de vos enregistrements.
Il ne faut donc pas considérer cette première synchronisation comme un montage
pédagogique définitif.

## Préparer Manim

Depuis la racine du cours, utiliser l’environnement Manim déjà préparé ou installer
les dépendances décrites dans `GUIDE-PUBLICATION.md` et `animations/requirements.txt`.
FFmpeg et ffprobe doivent être disponibles. Les scènes ne nécessitent pas LaTeX.

```bash
python animations/capsules-longues/render.py 3 --plan
python animations/capsules-longues/render.py 3 --preview
python animations/capsules-longues/render.py 3
python animations/capsules-longues/render.py 3 --audio-dir animations/audio
```

La prévisualisation est volontairement accélérée et silencieuse. Elle sert à
vérifier les compositions, pas à estimer le temps d’apprentissage.
Sans `--preview`, le rendu est en 720p à 24 images par seconde. Sans audio, la durée
repose sur l’estimation de lecture. Avec les WAV, elle repose sur leur durée réelle,
à laquelle s’ajoutent les pauses entre les séquences.

Pour vérifier une seule séquence :

```bash
python animations/capsules-longues/render.py 11 --section 3 --preview
```

Les sorties sont enregistrées sous `rendus/`, exclu de Git. Un fichier existant
n’est pas écrasé : choisir un autre dossier avec `--output` pour un nouvel essai.
Après le montage, vérifier la voix, les calculs affichés, les transitions et les
transcriptions avant de remplacer les vidéos sur le site.

## Repères scientifiques consultés

- [BERT](https://arxiv.org/abs/1810.04805) : contexte bidirectionnel et adaptation.
- [BERTopic, algorithme](https://maartengr.github.io/BERTopic/algorithm/algorithm.html) : représentations, regroupement et description des sujets.
- [LoRA](https://arxiv.org/abs/2106.09685) : adaptation avec des facteurs de faible rang.
- [DPO](https://arxiv.org/abs/2305.18290) : objectif d’apprentissage direct sur les préférences.

Les exemples numériques sont construits pour l’enseignement. Les scripts ne
constituent pas des mesures de performance de modèles réels.
