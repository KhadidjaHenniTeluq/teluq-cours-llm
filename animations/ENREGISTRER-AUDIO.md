# Enregistrer les capsules longues

La version à enregistrer maintenant est celle des **15 capsules hebdomadaires
longues**, préparées pour environ 6 à 9 minutes chacune.

- Textes à lire : `capsules-longues/semaine-01.txt` à `semaine-15.txt`.
- Tous les textes réunis : `capsules-longues/NARRATIONS-COMPLETES.md`.
- Durées et sujets : `capsules-longues/PLAN-DES-CAPSULES.md`.
- Consignes de montage : `capsules-longues/README.md`.

Vous pouvez fournir un audio complet par semaine (`semaine-01.wav`, `.mp3` ou
`.m4a`) ou un WAV par séquence (`semaine-01-01.wav`, etc.). Les textes courts
ci-dessous restent disponibles comme archives pour les illustrations existantes.

---

# Enregistrer les narrations courtes (archives de préparation)

Les fichiers `narrations/*.txt` contiennent seulement le texte à lire. Les fichiers
Markdown correspondants ajoutent les repères de segments et le nom de la scène
Manim. `NARRATIONS-COMPLETES.md` réunit les vingt textes dans un document.

Vous pouvez adapter une formulation à votre façon de parler. Ne lisez pas les
numéros de segments, les titres de fichiers ni les indications techniques.

## Fichiers à fournir

Un fichier WAV, MP3 ou M4A par vidéo, portant le même nom que le texte :
`tokenisation.wav`, `attention.wav`, `rag.wav`, etc. Conservez une qualité de voix
constante et évitez une musique de fond. Une courte pause entre les paragraphes
facilitera le montage.

Pour une synchronisation plus précise, vous pouvez enregistrer les paragraphes
séparément : `attention-01.wav`, `attention-02.wav`, etc. Ce n’est pas obligatoire.

Les vidéos actuelles durent environ trente secondes. Ne cherchez pas à parler
vite pour tenir dans cette durée. Le montage ou le rendu Manim devra être adapté
à votre débit et aux passages que vous souhaitez commenter.

## Après réception des audios

Pour chaque vidéo : vérifier le son, repérer les phrases, ajuster les temps de
lecture des schémas, monter l’audio, puis vérifier le résultat en entier. Les
transcriptions doivent correspondre aux paroles effectivement enregistrées.

Le script `assemble_audio.py` produit seulement une prévisualisation en ajustant
globalement la durée visuelle. Il ne synchronise pas automatiquement chaque
phrase avec une étape du schéma. La synchronisation détaillée restera à effectuer
à partir de vos enregistrements.

```bash
python3 animations/assemble_audio.py attention /chemin/attention.wav
```

Les résultats sont écrits dans `animations/sorties-audio/`. Les vidéos du site ne
sont pas remplacées automatiquement. Aucun audio personnel n’a encore été reçu.
