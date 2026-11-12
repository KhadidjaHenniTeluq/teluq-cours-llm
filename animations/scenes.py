"""Animations pédagogiques originales, sans LaTeX ni narration audio."""
from manim import *
import numpy as np

BG = '#101e30'
INK = '#eef3fa'
ACCENT = '#56d6c5'
BLUE = '#76aaff'


def label(text, size=27, color=INK):
    return Text(text, font='Arial', font_size=size, color=color)


def box(text, color=BLUE, width=2.5):
    shape = RoundedRectangle(width=width, height=.8, corner_radius=.12, color=color)
    words = label(text, 24)
    if words.width > width-.25:
        words.scale_to_fit_width(width-.25)
    return VGroup(shape, words)


class Lesson(Scene):
    def setup(self):
        self.camera.background_color = BG
        self.note = None

    def heading(self, title, subtitle):
        self.add(label(title, 38).to_edge(UP, buff=.45))
        self.add(label(subtitle, 21, BLUE).move_to([0,2.65,0]))

    def explain(self, text, hold=3):
        new = label(text, 24).to_edge(DOWN, buff=.48)
        if new.width > 12.8:
            new.scale_to_fit_width(12.8)
        if self.note is not None:
            self.play(FadeOut(self.note), run_time=.3)
        self.play(FadeIn(new), run_time=.5)
        self.note = new
        self.wait(hold)


class Tokenisation(Lesson):
    def construct(self):
        self.heading('Du texte aux tokens', 'Exemple illustratif : le découpage dépend du tokeniseur')
        phrase = label('Les chats dorment.', 36).move_to(UP*1.4)
        self.play(Write(phrase))
        self.explain('Le modèle reçoit des identifiants, pas directement une phrase.')
        tokens = VGroup(*[box(t, width=2.1) for t in ['Les',' chats',' dor','ment','.']]).arrange(RIGHT,buff=.25)
        self.play(LaggedStart(*[FadeIn(t,shift=DOWN*.3) for t in tokens],lag_ratio=.3))
        self.explain('Un token peut être un mot, un sous-mot ou une ponctuation.')
        ids = VGroup(*[label(t,29,ACCENT) for t in ['42','817','209','65','9']])
        for t,i in zip(tokens,ids):
            i.next_to(t,DOWN,buff=.8)
            self.play(GrowArrow(Arrow(t.get_bottom(),i.get_top(),buff=.15)),FadeIn(i),run_time=.6)
        self.explain('Ces identifiants fictifs servent à sélectionner des lignes de la matrice d’embeddings.',5)
        self.play(Indicate(tokens[2:4],color=ACCENT))
        self.explain('Ici, « dorment » occupe deux tokens. Un ID n’exprime pas une quantité.',5)


class Embeddings(Lesson):
    def construct(self):
        self.heading('Embeddings : comparer des directions', 'Projection en 2D inventée pour illustrer la similarité cosinus')
        axes = Axes(x_range=[-1,4,1],y_range=[-1,3,1],x_length=8,y_length=4, tips=False).shift(DOWN*.1)
        self.play(Create(axes))
        origin = axes.c2p(0,0)
        vectors = []
        for word,xy,col in [('chat',(3,1),ACCENT),('félin',(2.7,1.4),BLUE),('moteur',(.3,2.6),'#f4b86a')]:
            arrow = Arrow(origin, axes.c2p(*xy),buff=0,color=col)
            caption = label(word,25,col).next_to(arrow.get_end(),UP,buff=.15)
            self.play(GrowArrow(arrow),FadeIn(caption))
            vectors.append(arrow)
        self.explain('« chat » et « félin » pointent dans des directions proches.',4)
        self.play(Indicate(vectors[0]),Indicate(vectors[1]))
        self.explain('cos(u, v) = (u · v) / (||u|| × ||v||) : on compare l’angle.',5)
        self.play(Indicate(vectors[2]))
        self.explain('Une direction différente suggère ici un sens différent.',4)
        self.explain('Les vrais embeddings ont bien plus de dimensions ; cette carte est schématique.',5)


class Attention(Lesson):
    def construct(self):
        self.heading('Attention : une somme pondérée', 'Une requête Q compare ses scores avec trois clés K')
        words = VGroup(*[box(t) for t in ['Le','chat','dort']]).arrange(RIGHT,buff=.8).move_to(UP*1.5)
        self.play(FadeIn(words))
        scores = label('Scores Q · K / √d :     0.0        1.0        2.0',28).move_to(UP*.3)
        self.play(Write(scores))
        self.explain('Les projections Q, K et V sont apprises pendant l’entraînement.',4)
        probs=np.exp([0.,1.,2.]); probs/=probs.sum()
        bars=VGroup()
        for i,p in enumerate(probs):
            b=Rectangle(width=1.3,height=float(p)*1.8,color=ACCENT,fill_opacity=.8)
            b.move_to([words[i].get_x(),-1.5+float(p)*.9,0])
            bars.add(VGroup(b,label(f'{p:.3f}',24).next_to(b,DOWN,buff=.12)))
        self.play(LaggedStart(*[FadeIn(b) for b in bars],lag_ratio=.25))
        self.explain('Softmax transforme les scores en poids positifs dont la somme vaut 1.',5)
        self.play(FadeOut(scores))
        equation=label('Sortie = 0.090 V₁ + 0.245 V₂ + 0.665 V₃',28,ACCENT).move_to(UP*.3)
        self.play(Write(equation))
        self.explain('Chaque valeur V contribue à la nouvelle représentation selon son poids.',5)
        self.explain('Dans un décodeur causal, les positions futures sont masquées avant softmax.',5)


class Generation(Lesson):
    def construct(self):
        self.heading('Générer un token à la fois', 'Exemple fictif de décodage glouton : choisir la probabilité maximale')
        phrase=label('Le chat',36).move_to(UP*1.4)
        self.play(Write(phrase))
        self.explain('Le contexte initial est fourni au modèle.',3)
        for sentence,candidates in [('Le chat dort',[('dort',.6),('mange',.3),('joue',.1)]),('Le chat dort sur',[('sur',.7),('ici',.2),('.',.1)]),('Le chat dort sur le',[('le',.8),('un',.15),('ce',.05)])]:
            rows=VGroup(*[label(f'{w}   {p:.0%}',29,ACCENT if i==0 else INK) for i,(w,p) in enumerate(candidates)]).arrange(DOWN,buff=.3)
            self.play(FadeIn(rows))
            self.explain('Le modèle recalcule une distribution à partir de tout le contexte disponible.',3)
            new=label(sentence,36).move_to(UP*1.4)
            self.play(Transform(phrase,new),FadeOut(rows))
            self.wait(1)
        self.explain('Le token choisi rejoint le contexte ; la boucle continue jusqu’au critère d’arrêt.',4)
        self.explain('Avec l’échantillonnage, on peut sélectionner un token autre que le plus probable.',4)


class RAG(Lesson):
    def construct(self):
        self.heading('RAG : retrouver, puis générer', 'Les documents enrichissent le contexte sans réentraîner le modèle')
        docs=box('Documents',width=2.6).move_to([-4.5,1.4,0])
        index=box('Index vectoriel',width=3).move_to([0,1.4,0])
        self.play(FadeIn(docs))
        self.play(GrowArrow(Arrow(docs.get_right(),index.get_left(),buff=.1)),FadeIn(index))
        self.explain('En amont : découper les documents, calculer leurs embeddings, les indexer.',4)
        q=box('Question',width=2.6).move_to([-4.5,-.3,0])
        chunks=box('Passages retrouvés',ACCENT,width=3).move_to([0,-.3,0])
        model=box('LLM',width=2.6).move_to([4.5,-.3,0])
        self.play(FadeIn(q))
        self.play(GrowArrow(Arrow(q.get_top(),index.get_left(),buff=.15)))
        self.explain('Encoder la question permet de rechercher les passages les plus proches.',4)
        self.play(GrowArrow(Arrow(index.get_bottom(),chunks.get_top(),buff=.1)),FadeIn(chunks))
        self.play(GrowArrow(Arrow(chunks.get_right(),model.get_left(),buff=.1)),FadeIn(model))
        question_path=Arrow(q.get_bottom(),model.get_bottom(),path_arc=1.0,buff=.15,color=BLUE)
        self.play(Create(question_path))
        self.explain('Le prompt contient la question ET les passages récupérés.',4)
        self.explain('Le LLM rédige une réponse ; les sources doivent permettre de la vérifier.',5)
        self.explain('Une récupération imparfaite peut encore produire une réponse erronée.',4)


class LoRA(Lesson):
    def construct(self):
        self.heading('LoRA : apprendre une petite correction', 'W reste gelée ; seules les matrices A et B sont entraînées')
        base=box('W : 4096 × 4096',BLUE,width=4).move_to([-3,1,0])
        a=box('A : 8 × 4096',ACCENT,width=3).move_to([2.5,1.5,0])
        b=box('B : 4096 × 8',ACCENT,width=3).move_to([2.5,0,0])
        self.play(FadeIn(base))
        self.explain('Une matrice dense contient 4096 × 4096 = 16 777 216 paramètres.',4)
        self.play(FadeIn(a),FadeIn(b),GrowArrow(Arrow(a.get_bottom(),b.get_top(),buff=.1)))
        self.explain('Avec un rang de 8, A et B totalisent seulement 65 536 paramètres entraînables.',5)
        equation=label('y = W x + (α / r) B A x',36,ACCENT).move_to(DOWN*1.5)
        self.play(Write(equation))
        self.explain('La branche de faible rang ajoute une correction à la sortie de W.',5)
        self.play(Indicate(a),Indicate(b))
        self.explain('Ici, 256 fois moins de paramètres entraînables pour cette matrice.',4)
        self.explain('Les poids de base restent en mémoire ; ce ratio ne décrit pas toute la mémoire GPU.',5)


class Recurrence(Lesson):
    def construct(self):
        self.heading('RNN : faire circuler un état caché', 'Une dépendance séquentielle entre les étapes de calcul')
        states=VGroup(*[box(f'h{i}',width=1.8) for i in range(1,5)]).arrange(RIGHT,buff=1).shift(UP*.3)
        for i,word in enumerate(['Le','chat','noir','dort']):
            token=label(word,27).next_to(states[i],DOWN,buff=.8)
            self.play(FadeIn(token),GrowArrow(Arrow(token.get_top(),states[i].get_bottom(),buff=.1)))
            if i: self.play(GrowArrow(Arrow(states[i-1].get_right(),states[i].get_left(),buff=.1)))
            self.play(FadeIn(states[i]),run_time=.6)
            self.wait(.5)
        self.explain('Chaque état dépend du token courant et de l’état précédent.',5)
        self.play(Write(label('h(t) = f(Wx x(t) + Wh h(t−1) + b)',32,ACCENT).move_to(UP*1.8)))
        self.explain('Il faut calculer h₁ avant h₂, puis h₃ : la séquence ne se parallélise pas directement.',5)
        for state in reversed(states): self.play(Indicate(state,color=ACCENT),run_time=.5)
        self.explain('À l’entraînement, le gradient traverse ces étapes en sens inverse.',5)
        self.explain('Sur de longues séquences, il peut diminuer ou exploser ; les LSTM atténuent ce problème.',5)


class BERT(Lesson):
    def construct(self):
        self.heading('BERT : reconstruire un token masqué', 'Le contexte à gauche ET à droite aide la prédiction')
        tokens=VGroup(*[box(t,width=2.3) for t in ['Le','[MASK]','miaule','.']]).arrange(RIGHT,buff=.4).shift(UP*.9)
        self.play(FadeIn(tokens))
        for i in [0,2,3]:
            self.play(Create(CurvedArrow(tokens[i].get_bottom(),tokens[1].get_bottom(),angle=.6 if i==0 else -.6,color=ACCENT)),run_time=.7)
        self.explain('Le token à reconstruire peut utiliser les informations des deux côtés.',5)
        choices=VGroup(*[label(t,28) for t in ['chat : 80 %','chien : 15 %','reste : 5 %']]).arrange(DOWN,buff=.3).move_to(DOWN*1)
        self.play(FadeIn(choices))
        self.explain('Distribution fictive : « miaule » apporte un indice pour retrouver « chat ».',5)
        self.play(Transform(tokens[1],box('chat',ACCENT,width=2.3).move_to(tokens[1])),FadeOut(choices))
        self.explain('La perte compare la prédiction à la vraie cible sur les positions sélectionnées.',5)
        self.explain('Le masquage d’un token est différent du masque causal qui bloque des liens d’attention.',5)


class MasqueCausal(Lesson):
    def construct(self):
        self.heading('Masque causal : bloquer le futur', 'Ligne = requête ; colonne = clé ; ordre des tokens de 1 à 4')
        cells=VGroup()
        for i in range(4):
            self.add(label(str(i+1),24).move_to([-2.4,1.4-i*.75,0]))
            self.add(label(str(i+1),24).move_to([-1.4+i*.75,2.05,0]))
            for j in range(4):
                c=Square(side_length=.65,color=BLUE,fill_opacity=.25).move_to([-1.4+j*.75,1.4-i*.75,0]);cells.add(c)
        self.play(Create(cells))
        self.explain('Pendant l’entraînement, toutes les positions sont présentes dans le même lot.',5)
        for i in range(4):
            self.play(*[cells[i*4+j].animate.set_fill(ACCENT if j<=i else '#26303f',opacity=.9) for j in range(4)],run_time=.7)
        self.add(label('Vert : autorisé',25,ACCENT).move_to([3,1,0]),label('Gris : futur bloqué',25).move_to([3,.2,0]))
        self.explain('À la position 2, seules les positions 1 et 2 sont accessibles.',5)
        self.play(Indicate(VGroup(*cells[4:8])))
        self.explain('On ajoute −∞ aux scores interdits avant softmax : leurs poids deviennent nuls.',5)
        self.explain('Le modèle prédit le token suivant sans lire sa réponse dans les positions futures.',5)


class Recherche(Lesson):
    def construct(self):
        self.heading('Recherche sémantique : retrouver des passages', 'Exemple fictif : comparer la question aux embeddings des passages')
        doc=box('Document long',width=3.8).move_to(UP*1.6)
        self.play(FadeIn(doc))
        chunks=VGroup(*[box(t,width=3) for t in ['P1 : inscription','P2 : frais','P3 : examens']]).arrange(RIGHT,buff=.55)
        self.play(LaggedStart(*[FadeIn(c,shift=DOWN*.3) for c in chunks],lag_ratio=.3))
        self.explain('Découper le document conserve des unités de recherche plus ciblées.',5)
        question=label('Question : combien coûte le cours ?',29,ACCENT).move_to(DOWN*1.3)
        self.play(Write(question))
        self.explain('La question et les passages sont encodés dans un espace vectoriel compatible.',5)
        scores=VGroup()
        for c,v in zip(chunks,['0,35','0,91','0,18']): scores.add(label(v,28).next_to(c,UP,buff=.2))
        self.play(FadeIn(scores),Circumscribe(chunks[1],color=ACCENT))
        self.explain('La similarité classe ici P2 en tête ; top-k sélectionne les meilleurs candidats.',5)
        self.explain('Un score élevé ne prouve pas que le passage répond correctement : il faut vérifier.',5)


class BERTopic(Lesson):
    def construct(self):
        self.heading('BERTopic : des documents aux sujets', 'Exemple schématique ; les modules du pipeline sont interchangeables')
        stages=VGroup(*[box(t,width=2.6) for t in ['Embeddings','UMAP','HDBSCAN','c-TF-IDF']]).arrange(RIGHT,buff=.55).move_to(UP*1.6)
        for i,s in enumerate(stages):
            self.play(FadeIn(s),run_time=.5)
            if i:self.play(GrowArrow(Arrow(stages[i-1].get_right(),s.get_left(),buff=.05)),run_time=.4)
        self.explain('Les embeddings représentent les documents ; UMAP réduit leur dimension.',5)
        pts=VGroup(*[Dot([x,y,0],radius=.08,color=BLUE) for x,y in [(-3,.1),(-2.7,.4),(-3.3,-.2),(2,.1),(2.3,-.3),(1.7,.4),(0,-1.2)]])
        self.play(FadeIn(pts))
        self.play(*[p.animate.set_color(ACCENT if i<3 else '#f4b86a' if i<6 else INK) for i,p in enumerate(pts)])
        self.explain('HDBSCAN repère des groupes denses ; un document peut rester hors groupe.',5)
        tags=VGroup(label('cours, examen, note',24,ACCENT).move_to([-3,-.9,0]),label('prix, facture, frais',24,'#f4b86a').move_to([2,-.9,0]))
        self.play(FadeIn(tags))
        self.explain('c-TF-IDF met en évidence les mots caractéristiques de chaque groupe.',5)
        self.explain('Les mots décrivent le sujet ; les documents représentatifs permettent de le valider.',5)


class Prompt(Lesson):
    def construct(self):
        self.heading('Construire un prompt vérifiable', 'Séparer la tâche, les données et le format attendu')
        rows=VGroup(*[box(t,width=11) for t in ['Tâche : extraire la date de remise','Données : « Le devoir est dû le 12 novembre. »','Format : {"date": "..."} ; sinon null']]).arrange(DOWN,buff=.3).shift(UP*.3)
        for row,note in zip(rows,['Une instruction précise définit ce que le modèle doit produire.','Les données à analyser sont délimitées et identifiées comme données.','Un format explicite rend la sortie plus facile à contrôler.']):
            self.play(FadeIn(row));self.explain(note,4)
        result=label('{"date": "12 novembre"}',29,ACCENT).move_to(DOWN*1.65)
        self.play(Write(result))
        self.explain('Vérifier ensuite la structure ET la présence de la date dans le texte source.',5)
        self.explain('Les délimiteurs seuls ne garantissent ni l’exactitude ni la résistance aux injections.',5)


class Vision(Lesson):
    def construct(self):
        self.heading('Vision Transformer : de l’image aux tokens', 'Grille 4 × 4 illustrative ; chaque carré devient un vecteur')
        patches=VGroup(*[Square(side_length=.65,stroke_color=INK,fill_color=interpolate_color(ManimColor(BLUE),ManimColor(ACCENT),(i+j)/6),fill_opacity=.8).move_to([-4+j*.7,1.4-i*.7,0]) for i in range(4) for j in range(4)])
        self.play(FadeIn(patches))
        self.explain('L’image est découpée en patches de taille fixe.',4)
        targets=VGroup(*[Rectangle(width=.38,height=.65,color=BLUE,fill_opacity=.5).move_to([-.2+(k%8)*.65,1.1-(k//8)*1.2,0]) for k in range(16)])
        self.play(LaggedStart(*[Transform(p,t) for p,t in zip(patches,targets)],lag_ratio=.06),run_time=3)
        self.explain('Chaque patch est aplati puis projeté en un embedding de même dimension.',5)
        pos=label('+ embeddings de position',28,ACCENT).move_to([1.9,-1.1,0])
        self.play(Write(pos));self.explain('La position indique où se trouvait chaque patch dans l’image.',4)
        count=label('224 / 16 = 14 ; 14 × 14 = 196 patches',28).move_to(DOWN*2)
        self.play(Write(count));self.explain('Dans le ViT avec [CLS], 196 patches donnent 197 tokens au total.',5)


class DPO(Lesson):
    def construct(self):
        self.heading('DPO : apprendre à partir de préférences', 'Une même question, une réponse préférée et une réponse rejetée')
        q=box('Question x',width=4).move_to(UP*1.7)
        chosen=box('Réponse préférée y+',ACCENT,width=4.5).move_to([-3,.3,0])
        rejected=box('Réponse rejetée y−',BLUE,width=4.5).move_to([3,.3,0])
        self.play(FadeIn(q),FadeIn(chosen),FadeIn(rejected))
        self.explain('Le jeu de données contient des paires comparées pour une même question.',5)
        eq=label('m = log π(y+|x)/πref(y+|x) − log π(y−|x)/πref(y−|x)',25,ACCENT).move_to(DOWN*.9)
        self.play(Write(eq))
        self.explain('DPO compare les log-probabilités relatives à un modèle de référence gelé.',5)
        loss=label('Perte = −log sigmoid(β m)',30).move_to(DOWN*1.8)
        self.play(Write(loss))
        self.explain('Réduire cette perte favorise une marge relative plus grande pour la réponse préférée.',5)
        self.play(Indicate(chosen))
        self.explain('La qualité des préférences compte : DPO ne garantit pas une réponse vraie ou sûre.',5)


class CacheKV(Lesson):
    def construct(self):
        self.heading('Cache KV : réutiliser le passé', 'Décodage causal ; les clés et valeurs passées restent disponibles')
        old=VGroup(*[box(t,width=2.1) for t in ['K₁, V₁','K₂, V₂','K₃, V₃']]).arrange(RIGHT,buff=.4).move_to([-1.5,.9,0])
        self.play(FadeIn(old))
        self.explain('Le préremplissage traite le prompt et conserve les K et V de chaque couche.',5)
        new=box('K₄, V₄',ACCENT,width=2.1).next_to(old,RIGHT,buff=.4)
        q=box('Q₄',ACCENT,width=2).move_to(DOWN*1.2)
        self.play(FadeIn(new),FadeIn(q))
        self.explain('Pour le nouveau token, on calcule ses projections et on ajoute ses K et V au cache.',5)
        arrows=VGroup(*[Arrow(q.get_top(),b.get_bottom(),buff=.15,color=ACCENT) for b in [*old,new]])
        self.play(Create(arrows))
        self.explain('La nouvelle requête consulte les clés et valeurs du passé et du token courant.',5)
        self.explain('On évite de recalculer les anciennes projections ; l’attention au passé reste nécessaire.',5)
        self.explain('Le cache accélère le décodage mais sa mémoire augmente avec la longueur du contexte.',5)


class Agent(Lesson):
    def construct(self):
        self.heading('Agent : décider, agir, observer', 'Un exemple de recherche documentaire avec une limite d’itérations')
        nodes=VGroup(box('Décider',width=3).move_to([-3,1,0]),box('Appeler un outil',width=3).move_to([3,1,0]),box('Observer le résultat',width=3).move_to([3,-1,0]),box('Vérifier / terminer',width=3).move_to([-3,-1,0]))
        notes=['La question exige une information : choisir une recherche documentaire.','L’application exécute l’outil autorisé avec des paramètres contrôlés.','Le résultat de recherche revient comme donnée à examiner.','Vérifier la réponse et les sources avant de terminer ou de rechercher à nouveau.']
        for i,n in enumerate(nodes):
            self.play(FadeIn(n))
            if i:
                start, end = [(nodes[0].get_right(), nodes[1].get_left()),
                              (nodes[1].get_bottom(), nodes[2].get_top()),
                              (nodes[2].get_left(), nodes[3].get_right())][i-1]
                self.play(GrowArrow(Arrow(start, end, buff=.12, color=ACCENT)))
            self.explain(notes[i],4)
        self.play(GrowArrow(Arrow(nodes[3].get_top(),nodes[0].get_bottom(),buff=.15,color=ACCENT)))
        self.explain('Prévoir un arrêt : objectif atteint, limite d’étapes, erreur ou intervention humaine.',5)


class Entrainement(Lesson):
    def construct(self):
        self.heading('minGPT : une étape d’entraînement', 'Les cibles sont décalées d’un token par rapport aux entrées')
        inputs=label('Entrées :   Le     chat     dort',30).move_to(UP*1.5)
        targets=label('Cibles :    chat   dort     .',30,ACCENT).move_to(UP*.8)
        self.play(Write(inputs),Write(targets))
        self.explain('À chaque position, le modèle doit prédire le token suivant.',5)
        stages=VGroup(*[box(t,width=2.6) for t in ['Forward','Perte','Backward','Mise à jour']]).arrange(RIGHT,buff=.5).move_to(DOWN*.5)
        for i,s in enumerate(stages):
            self.play(FadeIn(s))
            if i:self.play(GrowArrow(Arrow(stages[i-1].get_right(),s.get_left(),buff=.05)),run_time=.4)
        self.explain('Le forward calcule les logits ; l’entropie croisée les compare aux cibles.',5)
        self.play(Indicate(stages[2],color=ACCENT))
        self.explain('Backward calcule les gradients ; l’optimiseur ajuste les poids.',5)
        self.play(Indicate(stages[3],color=ACCENT))
        self.explain('Réinitialiser les gradients entre les pas, sauf si l’on accumule volontairement.',5)
        self.explain('Mesurer la perte sur une validation séparée pour surveiller la généralisation.',5)


class Temperature(Lesson):
    def construct(self):
        self.heading('Température : modifier la distribution', 'Même vecteur de logits [2, 1, 0] ; probabilités = softmax(logits / T)')
        bars=None;caption=None
        for temp in [.5,1.,2.]:
            p=np.exp(np.array([2.,1.,0.])/temp);p/=p.sum()
            group=VGroup()
            for i,v in enumerate(p):
                bar=Rectangle(width=1.5,height=float(v)*2.6,fill_color=ACCENT,fill_opacity=.8,stroke_color=ACCENT).move_to([-3+i*3,-1.3+float(v)*1.3,0])
                group.add(VGroup(bar,label(f'{v:.1%}',27).next_to(bar,UP,buff=.15),label(['A','B','C'][i],25).move_to([-3+i*3,-1.7,0])))
            cap=label(f'T = {temp:g}',32,BLUE).move_to(UP*1.9)
            if bars is None:self.play(FadeIn(group),FadeIn(cap))
            else:self.play(ReplacementTransform(bars,group),ReplacementTransform(caption,cap),run_time=2)
            bars,caption=group,cap
            self.explain({.5:'Une température basse concentre la probabilité sur le token favori.',1.:'À T = 1, on conserve la distribution définie par les logits.',2.:'Une température élevée aplatit la distribution et diversifie les tirages.'}[temp],5)
        self.explain('Le classement reste identique pour T > 0 ; le décodage glouton garde le même maximum.',5)


class Quantification(Lesson):
    def construct(self):
        self.heading('Quantification : arrondir sur une grille', 'Exemple scalaire symétrique : pas s = 0,5 ; sans saturation')
        line=NumberLine(x_range=[-2,2,.5],length=10,include_numbers=False).shift(DOWN*.1)
        self.play(Create(line))
        for v in [-2,-1,0,1,2]:self.add(label(str(v),24).next_to(line.n2p(v),DOWN,buff=.25))
        values=[-1.3,.2,1.7];dots=VGroup(*[Dot(line.n2p(v)+UP*.55,color=BLUE,radius=.1) for v in values])
        labels=VGroup(*[label(str(v),25,BLUE).next_to(d,UP,buff=.15) for v,d in zip(values,dots)])
        self.play(FadeIn(dots),FadeIn(labels));self.explain('Les poids réels sont rapprochés de niveaux représentables.',5)
        for v,d in zip(values,dots):self.play(d.animate.move_to(line.n2p(round(v/.5)*.5)),run_time=1)
        self.explain('q = arrondi(w / s), puis poids reconstruit = s × q.',5)
        result=label('−1,3 → −1,5       0,2 → 0       1,7 → 1,5',29,ACCENT).move_to(DOWN*1.5)
        self.play(Write(result));self.explain('Le stockage peut diminuer, mais l’arrondi introduit une erreur.',5)
        self.explain('Les formats réels utilisent des échelles, des groupes et parfois des grilles non uniformes.',5)


class CLIP(Lesson):
    def construct(self):
        self.heading('CLIP : aligner images et textes', 'Matrice de similarité fictive pour trois paires correctes')
        self.add(label('Textes :     chat      vélo      arbre',25).move_to([.4,2,0]))
        vals=[[.8,.1,.2],[.1,.9,.2],[.2,.1,.85]];cells=VGroup()
        for i,name in enumerate(['Image chat','Image vélo','Image arbre']):
            self.add(label(name,23).move_to([-3.8,1.1-i*1.1,0]))
            for j,val in enumerate(vals[i]):
                cell=Square(side_length=.9,color=BLUE,fill_opacity=val,fill_color=BLUE).move_to([-1+j*1.5,1.1-i*1.1,0]);cells.add(VGroup(cell,label(str(val),23).move_to(cell)))
        self.play(FadeIn(cells))
        self.explain('Un encodeur image et un encodeur texte produisent des vecteurs dans un espace partagé.',5)
        self.play(*[Circumscribe(cells[i*3+i],color=ACCENT) for i in range(3)])
        self.explain('Les paires associées se trouvent sur la diagonale de cette matrice.',5)
        self.explain('La perte contrastive favorise ces paires par rapport aux autres éléments du lot.',5)
        self.explain('La comparaison se fait dans les deux sens : image vers texte et texte vers image.',5)
        self.explain('CLIP mesure une compatibilité ; il ne génère pas lui-même une légende.',5)
