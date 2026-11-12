"""Prévisualisation voix + vidéo. Ajustement global, sans alignement par phrase."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def duration(path):
    value = float(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], text=True).strip())
    if value <= 0:
        raise ValueError(f'Durée invalide : {path}')
    return value

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug', choices=[x['slug'] for x in json.loads((ROOT/'animations/catalogue.json').read_text())])
    parser.add_argument('audio', type=Path)
    args = parser.parse_args()
    audio = args.audio.resolve()
    if not audio.is_file():
        parser.error(f'Audio introuvable : {audio}')
    video = ROOT/'static/videos/manim'/f'{args.slug}.mp4'
    output_dir = ROOT/'animations/sorties-audio'
    output_dir.mkdir(exist_ok=True)
    output = output_dir/f'{args.slug}-avec-voix.mp4'
    if output.exists():
        parser.error(f'Le fichier existe déjà : {output}. Déplacez-le avant de recommencer.')
    audio_seconds, video_seconds = duration(audio), duration(video)
    subprocess.run([
        'ffmpeg', '-n', '-loglevel', 'error', '-i', str(video), '-i', str(audio),
        '-filter_complex', f'[0:v]setpts={(audio_seconds/video_seconds):.12f}*(PTS-STARTPTS),fps=24[v];[1:a]asetpts=PTS-STARTPTS,apad[a]',
        '-map', '[v]', '-map', '[a]', '-t', f'{audio_seconds:.6f}',
        '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', str(output)
    ], check=True)
    print(output)
    print('Prévisualisation créée. Vérifier ensuite la synchronisation de chaque explication.')

if __name__ == '__main__':
    main()
