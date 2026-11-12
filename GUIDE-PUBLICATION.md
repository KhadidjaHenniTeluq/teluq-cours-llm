# Publier le cours sur GitHub Pages

Le dépôt `origin` est déjà configuré sur :
https://github.com/KhadidjaHenniTeluq/teluq-cours-llm

L’adresse Hugo correspond à :
https://khadidjahenniteluq.github.io/teluq-cours-llm/

## Vérifier en local

```bash
cd "/Users/khenni/Documents/Cours Teluq/LLM-course-teluq-main"
hugo server -D
```

Ouvrir l’adresse affichée dans le terminal. Arrêter le serveur avec Ctrl+C.
Les vidéos sont déjà rendues et stockées dans `static/videos/manim/`.
La publication ne nécessite pas Manim.

## Envoyer les modifications

Le dossier contient aussi des modifications personnelles antérieures (page d’accueil,
photo, configuration et pages de semaine 1). Les commandes suivantes les incluent :
consulter le diff avant le commit.

```bash
git status --short
git diff --stat
git add content layouts static animations hugo.toml .gitignore GUIDE-PUBLICATION.md .gitmodules themes/hugo-book
git diff --cached --stat
git commit -m "Réviser le cours, séparer les corrigés et préparer les narrations"
git push origin main
```

Le thème est déjà un dépôt Git imbriqué et `.gitmodules` est présent.
`git add themes/hugo-book` enregistre sa révision comme sous-module pour que le
workflow existant puisse le récupérer. Ne pas supprimer son dossier `.git`.
Les fichiers `.DS_Store` déjà suivis peuvent toujours apparaître dans `git status` :
ils ne sont pas nécessaires au site. Pour les exclure du commit après le `git add` :

```bash
git restore --staged -- ':(glob)**/.DS_Store'
```

Si GitHub refuse le push parce que des commits distants manquent, récupérer et
examiner les changements avec `git fetch origin` et `git log --oneline --left-right
HEAD...origin/main` avant d’intégrer les modifications. Ne pas forcer le push.

## Activer Pages

Dans le dépôt GitHub : **Settings → Pages → Build and deployment → Source → GitHub Actions**.
Le workflow `.github/workflows/deploy.yml` est déjà présent et se déclenche sur les
pushs vers `main`. Suivre son exécution dans **Actions**. Après une exécution réussie,
ouvrir l’adresse du site ci-dessus.

Documentation : https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Modifier ou régénérer les animations

Les vingt scènes sont dans `animations/scenes.py`. Le catalogue
`animations/catalogue.json` associe chaque vidéo à sa semaine et sa page.
Les 15 semaines possèdent au moins une animation. Chaque vidéo est accompagnée
d’une transcription dans la page du cours. Les animations sont silencieuses,
avec du texte explicatif intégré à l’image.

| Semaine | Animations |
| --- | --- |
| 1 | RNN et mémoire séquentielle |
| 2 | Du texte aux tokens, Embeddings et similarité cosinus |
| 3 | Comprendre les poids d’attention, Visualiser le masque causal |
| 4 | BERT et le token masqué |
| 5 | La génération autorégressive, Température et probabilités |
| 6 | Du document aux passages pertinents |
| 7 | BERTopic : des groupes aux sujets |
| 8 | Construire un prompt vérifiable |
| 9 | Les étapes d’un système RAG |
| 10 | CLIP et l’apprentissage contrastif, Du patch au token visuel |
| 11 | LoRA et les matrices de faible rang, Quantification et erreur d’arrondi |
| 12 | Apprendre avec des paires de préférences |
| 13 | Le cache KV pendant le décodage |
| 14 | La boucle d’un agent avec outils |
| 15 | minGPT : de la prédiction à la mise à jour |

Pour ne régénérer qu’une scène : `python animations/render.py temperature`.
Sans argument, le script régénère les vingt vidéos.

Installer les dépendances système Cairo, Pango, pkg-config et FFmpeg selon votre
système, puis créer un environnement Python compatible avec Manim 0.22 :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r animations/requirements.txt
python animations/render.py
python animations/verify.py
hugo --minify
```

Le rendu produit les MP4 H.264 en 720p et les affiches JPEG. Les fichiers
intermédiaires restent dans `animations/media/`, exclu de Git.
Documentation Manim : https://docs.manim.community/en/stable/installation.html

## Révision éditoriale et examen

Il n’est pas nécessaire de supprimer le dépôt GitHub ni son historique pour mettre
le site à jour. Le commit puis le push remplacent la version publiée après la
réussite du workflow Pages.

Les corrigés sont conservés localement dans `enseignant-prive/`, exclu de Git et
du site Hugo. Ne les copiez pas dans `content/` ou `static/` et ne forcez pas leur
ajout avec `git add -f`. Vérifiez l’exclusion avant de publier :

```bash
git check-ignore enseignant-prive/corrige-examen-final.md
git diff --cached --name-only
hugo --minify
```

Attention : les anciennes réponses figurent déjà dans un commit local. Si cette
version a été envoyée sur GitHub, elles peuvent rester consultables dans
l’historique. Retirer les réponses de la nouvelle page ne les rend pas secrètes
rétroactivement. Pour un examen confidentiel, préparez de nouvelles questions.

Les textes des vingt narrations sont dans `animations/NARRATIONS-COMPLETES.md`.
Consultez `animations/ENREGISTRER-AUDIO.md` pour les noms des fichiers audio et
la préparation du montage. Les vidéos publiées restent silencieuses tant que
les enregistrements n’ont pas été fournis et intégrés.

## Capsules longues, version de préparation

Le dossier `animations/capsules-longues/` contient quinze narrations développées
et les scripts Manim correspondants, avec des durées indicatives de 6 à 9 minutes.
Ces sources seront incluses par `git add animations`. Les fichiers audio personnels
et les rendus intermédiaires restent exclus de Git.

Les vidéos courtes actuellement intégrées au site restent disponibles. Les futures
capsules longues seront montées avec la voix de l’enseignante, vérifiées et reliées
aux pages des semaines après réception des enregistrements. La présence des scripts
ne signifie pas que ces nouvelles vidéos sont déjà publiées.
