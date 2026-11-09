from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';base=root/'production/sifirdan-yeni'
config={'002':{'b':31.85,'words':[34.2,34.95,35.67,36.48],'shots':[(0,1),(45,2),(210,2),(330,3),(470,4)],'cover':['HALIDAKİ TÜYLER','NASIL ÇIKAR?'],'path':'M 145 665 C 215 615 300 615 385 650 C 480 690 560 750 560 820 C 550 880 460 900 370 885 C 280 870 190 830 150 780 C 130 750 130 700 145 665'},'003':{'b':29.32,'words':[31.41,32.07,32.73,33.54],'shots':[(0,1),(45,2),(130,1),(205,2),(355,3),(500,4)],'cover':['YANMIŞ TENCERE','NASIL TEMİZLENİR?'],'path':'M 205 550 C 240 500 320 480 390 490 C 465 500 525 540 550 600 C 570 670 530 745 480 770 C 405 800 300 780 245 740 C 200 700 180 610 205 550'}}
for id,v in config.items():
 d=base/f'VID-{id}';c=json.loads((rem/f'yeniden-{id}.json').read_text());b=v['b']
 with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],shots=[{'from':a,'file':f'rev2-{n}.png'} for a,n in v['shots']],highlight={'file':'rev2-1.png','from':10,'to':42,'path':v['path']})
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for n in range(1,5):shutil.copyfile(d/f'rev2-{n}.png',dest/f'rev2-{n}.png')
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/f'yeniden-{id}.jsx').read_text().replace(f'yeniden-{id}.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',70 if len(line)<17 else 58),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-bastan-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
