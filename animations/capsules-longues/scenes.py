"""Scènes longues du cours. Réglages transmis par render.py ; aucun LaTeX requis."""
from pathlib import Path
import json
import os
import textwrap

import numpy as np
from manim import (
    Scene, Text, Group, VGroup, RoundedRectangle, Rectangle, Square, Dot, Arrow,
    Line, Circle, Axes, FadeIn, FadeOut, Create, GrowArrow, Indicate,
    UP, DOWN, LEFT, RIGHT, WHITE, config,
)

ROOT = Path(__file__).resolve().parent
BG, INK, ACCENT, BLUE, ORANGE = '#101e30', '#eef3fa', '#56d6c5', '#76aaff', '#f4b86a'


def text(value, size=27, width=12):
    result = Text(value, font='Arial', font_size=size, color=INK, line_spacing=1.15)
    if result.width > width:
        result.scale_to_fit_width(width)
    return result


def card(value, width=2.8, height=1.15):
    words = text(textwrap.fill(value, width=23), 25, width-.3)
    if words.height > height-.2:
        words.scale_to_fit_height(height-.2)
    return VGroup(RoundedRectangle(width=width, height=height, corner_radius=.12,
                                   color=BLUE, fill_color=BG, fill_opacity=1), words)


def diagram(section):
    """Retourne un fond et les étapes révélées au fil de la narration."""
    kind, nodes = section['visual'], section['nodes']
    base, steps = VGroup(), []
    if kind in {'flow', 'tokens', 'comparison'}:
        if kind == 'comparison':
            positions = [(-3.3, .8), (3.3, .8), (-3.3, -1.0), (3.3, -1.0)]
            for label, (x,y) in zip(nodes, positions):
                steps.append(card(label,5.3,1.25).move_to([x,y,0]))
        else:
            boxes = VGroup(*[card(n,2.7) for n in nodes]).arrange(RIGHT,buff=.5)
            boxes.move_to([0,0,0])
            for i,box in enumerate(boxes):
                if i and kind=='flow':
                    steps.append(VGroup(Arrow(boxes[i-1].get_right(),box.get_left(),buff=.08,color=ACCENT),box))
                else:steps.append(box)
    elif kind in {'softmax','sampling','temperature','loss','retrieval'}:
        entries = {
            'softmax': [('score 0',.09),('score 1',.245),('score 2',.665)],
            'sampling': [('chat',.5),('chien',.3),('oiseau',.2)],
            'temperature': [('T = 0,5',.867),('T = 1',.665),('T = 2',.506)],
            'loss': [('p = 0,50',.693),('p = 0,25',1.386)],
            'retrieval': [('A',1),('B',.8),('C',0)],
        }[kind]
        top = max(1,max(v for _,v in entries))
        axis = Line([-5,-1.5,0],[5,-1.5,0],color=BLUE);base.add(axis)
        for i,(name,value) in enumerate(entries):
            x=(i-(len(entries)-1)/2)*3
            h=max(.025,value/top*2.9)
            bar=Rectangle(width=1.65,height=h,color=ACCENT,fill_color=ACCENT,fill_opacity=.65).move_to([x,-1.5+h/2,0])
            val = f'{value:.3f}'.replace('.',',') if kind=='loss' else f'{value*100:.1f} %'.replace('.',',')
            if kind=='retrieval':val=f'{value:.1f}'.replace('.',',')
            steps.append(VGroup(bar,text(name,24,2.7).move_to([x,-1.9,0]),text(val,25,2.7).next_to(bar,UP,buff=.15)))
        if kind=='temperature':base.add(text('Probabilité du score maximal, pour les scores 0, 1 et 2',23).move_to([0,1.95,0]))
        if kind=='loss':base.add(text('Perte = −ln(probabilité de la cible)',25).move_to([0,2.15,0]))
    elif kind in {'vectors','weighted'}:
        if kind=='vectors':
            axes=Axes(x_range=[0,3,1],y_range=[0,2,1],x_length=7,y_length=3.2,tips=False).move_to([0,0,0]);base.add(axes)
            for label,point,color in [('u',(1,0),ACCENT),('v',(2,0),BLUE),('w',(0,1),ORANGE)]:
                arrow=Arrow(axes.c2p(0,0),axes.c2p(*point),buff=0,color=color)
                steps.append(VGroup(arrow,text(label,27).next_to(arrow.get_end(),UP,buff=.2)))
            steps.append(text('cos(u,v) = 1     cos(u,w) = 0',28).move_to([0,-2.2,0]))
        else:
            for i,line in enumerate(['0,090 × (1 ; 0) = (0,090 ; 0)', '0,245 × (0 ; 2) = (0 ; 0,490)',
                                     '0,665 × (2 ; 1) = (1,330 ; 0,665)', 'Somme ≈ (1,420 ; 1,155)']):
                steps.append(text(line,30).move_to([0,1.35-i*.9,0]))
    elif kind in {'causal','patches','confusion'}:
        if kind=='causal':
            base.add(text('Lignes : requêtes ; colonnes : positions consultées',23).move_to([0,2.0,0]))
            for i in range(3):
                row=VGroup()
                for j in range(3):
                    allowed=j<=i
                    sq=Square(side_length=.8,color=BLUE,fill_color=ACCENT if allowed else BG,fill_opacity=.6).move_to([(j-1)*.95,(1-i)*.95,0])
                    row.add(sq,text('oui' if allowed else 'non',20).move_to(sq))
                steps.append(row)
            steps.append(text('Position 2 : poids recalculés ≈ 0,269 ; 0,731 ; 0',23).move_to([0,-2,0]))
        elif kind=='patches':
            base.add(text('224 pixels ÷ 16 = 14 patches par côté',26).move_to([0,2.15,0]))
            for group in range(4):
                squares=VGroup()
                for i in range(14):
                    for j in range(14):
                        if (i*14+j)*4//196 != group:continue
                        squares.add(Square(side_length=.215,color=BLUE,stroke_width=1,fill_color=ACCENT,fill_opacity=.3).move_to([(j-6.5)*.235,(6.5-i)*.235,0]))
                steps.append(squares)
            steps.append(text('14 × 14 = 196 patches',29).move_to([0,-2.2,0]))
        else:
            for i,line in enumerate(['Vrais positifs : 8     Faux positifs : 2', 'Faux négatifs : 4     Vrais négatifs : 6',
                                     'Précision = 8 / 10 = 80 %', 'Rappel = 8 / 12 ≈ 66,7 %']):
                steps.append(text(line,29).move_to([0,1.25-i*.85,0]))
    elif kind=='clusters':
        rng=np.random.default_rng(7)
        for center,color in [((-3,0),ACCENT),((0,1),BLUE),((3,-.2),ORANGE)]:
            dots=VGroup(*[Dot([center[0]+rng.normal(0,.4),center[1]+rng.normal(0,.35),0],radius=.07,color=color) for _ in range(18)])
            steps.append(dots)
        steps.append(VGroup(Dot([-1,-1.35,0],color=WHITE),text('Document atypique : à examiner',24).move_to([1,-2.2,0])))
    elif kind=='lora':
        steps=[card('W gelée\n1000 × 1000',3.2,2).move_to([-4,0,0]),
               card('B\n1000 × 8',2.2,2).move_to([-.8,0,0]),
               card('A\n8 × 1000',3,.8).move_to([3,0,0]),
               text('ΔW = B × A     8 000 + 8 000 = 16 000 paramètres',26).move_to([0,-2,0])]
        base.add(text('+',40).move_to([-2.2,0,0]),text('×',40).move_to([.7,0,0]))
    elif kind=='quantize':
        base.add(Line([-4,0,0],[4,0,0],color=BLUE))
        for x,label in [(-4,'0'),(0,'0,25'),(4,'0,50')]:base.add(Dot([x,0,0],color=BLUE),text(label,25).move_to([x,-.45,0]))
        steps=[VGroup(Dot([1.92,0,0],color=ORANGE),text('0,37',25).move_to([1.92,.6,0])),
               Arrow([1.92,.2,0],[0,.2,0],buff=.05,color=ACCENT),text('Erreur absolue : |0,37 − 0,25| = 0,12',28).move_to([0,-1.6,0])]
    elif kind=='cache':
        for i in range(4):
            box=card(f'Position {i+1}\nK et V',2.6).move_to([(i-1.5)*3.05,0,0])
            if i==3:box[0].set_color(ACCENT)
            steps.append(box)
        base.add(text('Positions 1 à 3 conservées ; ajout de la position 4',26).move_to([0,-1.8,0]))
    else:
        raise ValueError(f'Visuel inconnu : {kind}')
    return base, steps


class CapsuleLongue(Scene):
    def construct(self):
        self.camera.background_color=BG
        lessons=json.loads((ROOT/'catalogue.json').read_text())
        week=int(os.environ.get('CAPSULE_WEEK','1'))
        lesson=next(x for x in lessons if x['week']==week)
        selection=int(os.environ.get('CAPSULE_SECTION','0'))
        speed=float(os.environ.get('CAPSULE_TIME_SCALE','1'))
        timing=json.loads(os.environ.get('CAPSULE_AUDIO_TIMING','{}'))
        audio_dir=os.environ.get('CAPSULE_AUDIO_DIR')
        for section in lesson['sections']:
            if selection and section['number']!=selection:continue
            header=text(f"Semaine {week} · {section['number']}/{len(lesson['sections'])}",21).move_to([0,3.5,0])
            title=text(section['title'],34).move_to([0,2.85,0])
            footer=text('Capsule pédagogique · Khadidja Henni',19).move_to([0,-3.4,0])
            self.add(header,title,footer)
            base,steps=diagram(section);self.add(base)
            seconds=float(timing.get(str(section['number']),section['speech_seconds']))
            if audio_dir:self.add_sound(str(Path(audio_dir)/section['audio']))
            # Quatre à cinq révélations espacées. Les repères précis seront affinés avec la voix.
            slot=seconds/len(steps)*speed
            transition=min(.7*speed,slot/3)
            for part in steps:
                self.play(FadeIn(part,shift=UP*.08),run_time=transition)
                self.wait(max(0,slot-transition))
            self.wait(5*speed)
            self.play(FadeOut(Group(*self.mobjects)),run_time=1*speed)
