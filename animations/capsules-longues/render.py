"""Rendu d'une capsule longue, avec narration par séquence en option."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

def audio_duration(path):
    result=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
      '-of','default=noprint_wrappers=1:nokey=1',str(path)],text=True)
    value=float(result.strip())
    if value<=0:raise ValueError(f'Audio de durée invalide : {path}')
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('week',type=int,choices=range(1,16))
    parser.add_argument('--section',type=int,help='Une seule séquence, pour vérifier un passage.')
    parser.add_argument('--audio-dir',type=Path,help='Dossier des WAV nommés semaine-XX-YY.wav.')
    parser.add_argument('--preview',action='store_true',help='Brouillon accéléré silencieux, 8 pour cent de la durée, 480p.')
    parser.add_argument('--output',type=Path,default=ROOT/'rendus',help='Dossier de rendu, sans publication automatique.')
    parser.add_argument('--plan',action='store_true',help='Afficher les durées sans lancer Manim.')
    args=parser.parse_args()
    lesson=next(x for x in json.loads((ROOT/'catalogue.json').read_text()) if x['week']==args.week)
    sections=[s for s in lesson['sections'] if not args.section or s['number']==args.section]
    if not sections:parser.error('Numéro de séquence absent de cette capsule.')
    if args.preview and args.audio_dir:parser.error('La prévisualisation accélérée doit rester silencieuse.')
    timings={}
    if args.audio_dir:
        for s in sections:
            path=args.audio_dir.resolve()/s['audio']
            if not path.is_file():parser.error(f'Audio manquant : {path}')
            timings[str(s['number'])]=audio_duration(path)
    duration=sum(timings.get(str(s['number']),s['speech_seconds'])+6 for s in sections)
    if args.preview:duration*=.08
    print(f"Semaine {args.week:02} : {duration:.1f} secondes, {len(sections)} séquences.",flush=True)
    if args.plan:return
    env=os.environ.copy()
    env.update(CAPSULE_WEEK=str(args.week),CAPSULE_SECTION=str(args.section or 0),
               CAPSULE_TIME_SCALE='.08' if args.preview else '1',CAPSULE_AUDIO_TIMING=json.dumps(timings))
    env.pop('CAPSULE_AUDIO_DIR',None)
    if args.audio_dir:env['CAPSULE_AUDIO_DIR']=str(args.audio_dir.resolve())
    name=f"semaine-{args.week:02}"+(f"-sequence-{args.section:02}" if args.section else '')
    name+= '-apercu' if args.preview else ('-avec-voix' if args.audio_dir else '-silencieuse')
    args.output.mkdir(parents=True,exist_ok=True)
    # Les sorties existantes ne sont jamais remplacées implicitement.
    if any(args.output.rglob(name+'.mp4')):parser.error('Ce rendu existe déjà ; choisissez un autre dossier de sortie.')
    subprocess.run([sys.executable,'-m','manim','-ql' if args.preview else '-qm','--fps','24',
       '--disable_caching','--media_dir',str(args.output.resolve()),'-o',name,str(ROOT/'scenes.py'),'CapsuleLongue'],
       check=True,env=env,cwd=ROOT)
    print('Rendu terminé dans',args.output.resolve())

if __name__=='__main__':main()
