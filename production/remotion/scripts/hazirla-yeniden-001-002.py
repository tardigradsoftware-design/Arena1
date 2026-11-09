#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, math, shutil, wave
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; prod=root/'production/sifirdan-yeni'; font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
config={
 '001':{'boundary':33.6,'words':[35.55,36.24,36.90,37.59], 'title':'Tıkanan Banyo Giderindeki Saçları Tesisatçısız 5 Saniyede Çıkaran "Cırt Kelepçe" Hilesi', 'cover':['TIKALI GİDER','NASIL AÇILIR?']},
 '002':{'boundary':31.55,'words':[33.66,34.50,35.22,36.00], 'title':'Elektrik Süpürgesinin Çekemediği Halıdaki Saçları Söken "Cam Çekpası" Hilesi','cover':['HALIDAKİ TÜYLER','NASIL ÇIKAR?']}}
for id,v in config.items():
 d=prod/f'VID-{id}';c=json.loads((rem/f'sifirdan-tam-{id}.json').read_text()); boundary=v['boundary']; c['dir']='yeniden'+id
 with wave.open(str(d/'anlatim.wav')) as f: dur=f.getnframes()/f.getframerate()
 c.update(frames=math.ceil((boundary/1.55+(dur-boundary)/1.62+.3)*30),captionEnd=boundary/1.55,ctaStart=round(boundary/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((boundary/1.55+(t-boundary)/1.62)*30) for t in v['words']],tempoBoundary=boundary)
 # Diagram for the mechanism is an original schematic, with no in-video meta text.
 im=Image.new('RGB',(768,1376),'#f2f1e9');g=ImageDraw.Draw(im)
 if id=='001':
  g.rounded_rectangle((325,260,445,1100),radius=12,fill='#d8dedb',outline='#344b43',width=5)
  for y in range(430,1020,100):
   g.polygon([(320,y),(350,y-28),(320,y+14)],fill='#f2f1e9');g.polygon([(450,y),(420,y-28),(450,y+14)],fill='#f2f1e9')
  g.rounded_rectangle((300,200,470,320),radius=18,fill='#cbd5ce',outline='#344b43',width=5)
 else:
  g.rectangle((0,720,768,1376),fill='#ccb999');g.rounded_rectangle((160,600,605,675),radius=15,fill='#354842');g.rectangle((185,675,580,730),fill='#222');g.line((385,600,385,300),fill='#354842',width=40)
  for x in (220,280,340,400,460,520):g.arc((x-25,735,x+50,830),0,190,fill='#745d4b',width=5)
 im.save(d/'sahne-4.png')
 # Four distinct shots: issue, implement, schematic, outcome.
 c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':205,'file':'sahne-4.png'},{'from':420,'file':'sahne-3.png'}]
 c['representativeFiles']=[]
 c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path': ('M 115 670 C 160 565 260 540 380 550 C 495 554 600 625 625 720 C 650 815 560 905 438 920 C 300 940 160 900 120 810 C 100 770 100 710 115 670' if id=='001' else 'M 145 700 C 200 650 270 640 350 660 C 445 680 530 730 555 790 C 575 845 520 890 430 900 C 300 915 205 875 160 820 C 140 795 130 740 145 700')} 
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for p in d.glob('sahne-*.png'):shutil.copy(p,dest/p.name)
 (rem/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (rem/f'yeniden-{id}.jsx').write_text((rem/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));draw=ImageDraw.Draw(bg);draw.rounded_rectangle((60,180,1020,560),radius=32,fill='#101b19',outline='#ffffff',width=6)
 for j,line in enumerate(v['cover']):draw.text((540,245+j*130),line,font=ImageFont.truetype(font,82 if j==0 else 68),fill='#ffe135' if j==0 else 'white',anchor='mm',stroke_width=1)
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92)
 print(id,v['title'],c['frames'],c['ctaStackFrames'])
