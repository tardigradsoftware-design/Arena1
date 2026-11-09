from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-001'; c=json.loads((rem/'yeniden-001.json').read_text()); boundary=32.40
with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c.update(dir='bastan001',frames=math.ceil((boundary/1.55+(dur-boundary)/1.62+.3)*30),captionEnd=boundary/1.55,ctaStart=round(boundary/1.55*30),tempoBoundary=boundary,ctaStackFrames=[round((boundary/1.55+(x-boundary)/1.62)*30) for x in [34.5,35.22,35.94,36.72]],shots=[{'from':0,'file':'rev2-1.png'},{'from':45,'file':'rev2-2.png'},{'from':210,'file':'rev2-3.png'},{'from':420,'file':'rev2-4.png'}],highlight={'file':'rev2-1.png','from':10,'to':42,'path':'M 190 570 C 230 500 320 490 385 490 C 480 490 550 530 580 600 C 610 680 590 770 540 825 C 490 880 405 892 330 880 C 250 870 195 830 180 760 C 165 700 165 625 190 570'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-001.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-001.jsx').write_text((rem/'yeniden-001.jsx').read_text().replace('yeniden-001.json','bastan-001.json'))
im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
for j,line in enumerate(['TIKALI GİDER','NASIL AÇILIR?']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',76),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-001-bastan-img-1.jpg',quality=92);print(c['frames'],c['ctaStackFrames'])
