"""Contrôle du catalogue, de la couverture hebdomadaire et des médias livrés."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / 'animations/catalogue.json').read_text())
slugs = [item['slug'] for item in items]
assert len(slugs) == len(set(slugs)), 'Slugs de vidéos dupliqués'
weeks = {item['week'] for item in items}
assert weeks == set(range(1, 16)), f'Semaines manquantes : {set(range(1,16)) - weeks}'
references = {}
for page in (ROOT / 'content').rglob('*.md'):
    for slug in re.findall(r'{{< conceptvideo name="([^"]+)"', page.read_text()):
        references.setdefault(slug, []).append(page)
assert set(references) == set(slugs), 'Catalogue et intégrations de vidéos incohérents'
for item in items:
    page = ROOT / 'content' / item['page']
    assert page in references[item['slug']], f"Page incorrecte : {item['slug']}"
    assert f"week{item['week']:02}" in page.parts, f"Semaine incorrecte : {page}"
    text = page.read_text()
    match = re.search(r'{{< conceptvideo name="' + re.escape(item['slug']) + r'"[^>]*>}}(.*?){{< /conceptvideo >}}', text, re.S)
    assert match and len(match[1].strip()) > 100, f"Transcription manquante : {page}"
    media = ROOT / 'static/videos/manim' / item['slug']
    assert media.with_suffix('.jpg').stat().st_size > 1000, f'Affiche manquante : {media}'
    data = json.loads(subprocess.check_output(['ffprobe', '-v', 'quiet', '-show_streams', '-show_format', '-of', 'json', str(media.with_suffix('.mp4'))]))
    video = next(s for s in data['streams'] if s['codec_type'] == 'video')
    assert (video['codec_name'], video['width'], video['height']) == ('h264', 1280, 720), media
    assert float(data['format']['duration']) > 15, media
    print(f"S{item['week']:02} {item['slug']}: {float(data['format']['duration']):.1f} s")
print(f'{len(items)} animations valides ; 15 semaines couvertes ; transcriptions présentes.')
