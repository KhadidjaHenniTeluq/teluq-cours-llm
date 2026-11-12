"""Depuis la racine : python animations/render.py (Manim et FFmpeg requis)."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
import argparse
import json

catalogue = json.loads((ROOT / 'animations/catalogue.json').read_text())
parser = argparse.ArgumentParser(description='Rendre les animations du cours en 720p.')
parser.add_argument('scenes', nargs='*', help='Noms de scènes ou slugs ; vide = toutes.')
args = parser.parse_args()
known = {v for item in catalogue for v in (item['scene'], item['slug'])}
if set(args.scenes) - known:
    parser.error('Scènes inconnues : ' + ', '.join(sorted(set(args.scenes) - known)))
SCENES = {item['scene']: item['slug'] for item in catalogue
          if not args.scenes or item['scene'] in args.scenes or item['slug'] in args.scenes}
media = ROOT / 'animations' / 'media'
out = ROOT / 'static' / 'videos' / 'manim'
out.mkdir(parents=True, exist_ok=True)
for scene, slug in SCENES.items():
    subprocess.run([sys.executable, '-m', 'manim', '-qm', '--fps', '24',
                    '--media_dir', str(media), str(ROOT/'animations/scenes.py'), scene], check=True, cwd=ROOT)
    source = media / 'videos' / 'scenes' / '720p24' / f'{scene}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(source),
                    '-c:v', 'libx264', '-crf', '23', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                    '-an', str(out/f'{slug}.mp4')], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-sseof', '-4', '-i', str(out/f'{slug}.mp4'),
                    '-frames:v', '1', '-update', '1', str(out/f'{slug}.jpg')], check=True)
