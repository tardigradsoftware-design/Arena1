from pathlib import Path
from PIL import Image, ImageDraw, ImageFont,ImageOps
import wave,json,math,shutil
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-004';c=json.loads((rem/'yeniden-004.json').read_text());b=25.2
with wave.open(str(d/'rev2-anlatim.wav')) as f:dur=f.getnframes()/f.getframerate()
c.update(dir='bastan004',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [27.27,28.05,28.8,29.7]],shots=[{'from':0,'file':'rev2-1.png'},{'from':45,'file':'rev2-2.png'},{'from':110,'file':'rev2-1.png'},{'from':190,'file':'rev2-2.png'},{'from':290,'file':'rev2-3.png'},{'from':440,'file':'rev2-4.png'}],highlight={'file':'rev2-1.png','from':115,'to':160,'path':'M 65 750 C 170 760 290 770 390 780 C 505 780 600 760 700 710 C 725 700 730 735 700 760 C 610 820 490 845 365 845 C 245 840 140 825 70 800 C 50 790 50 760 65 750'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for i in range(1,5):shutil.copyfile(d/f'rev2-{i}.png',dest/f'rev2-{i}.png')
(rem/'bastan-004.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-004.jsx').write_text((rem/'yeniden-004.jsx').read_text().replace('yeniden-004.json','bastan-004.json'))
im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
for i,line in enumerate(['SARARAN TABAN','NASIL BEYAZLAR?']):g.text((540,250+i*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',68),fill='#ffe135' if i==0 else 'white',anchor='mm')
im.save(d/'VID-004-bastan-img-1.jpg',quality=92);print(c['frames'],c['ctaStackFrames'])
