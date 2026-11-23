from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-048';b=32.8
caption='Kahvaltıda ekmeğinize tereyağı sürmek istediğinizde dolaptan yeni çıkan tereyağı taş gibi sertse ve ekmeği parçalıyorsa sakın ocakta eritmeyin! Bir su bardağının içine kaynar su doldurup otuz saniye bekletin, ardından suyu döküp ısınan bardağı dikey olarak tereyağı kalıbının üzerine kapatın. Bardağın içindeki termal ısı tereyağını hiç eritmeden ve suyunu saldırmadan sadece bir dakikada oda sıcaklığına getirecek, pamuk gibi sürülebilir yapacaktır. Kahvaltı sofrası için bu tüyoyu hemen kaydet!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='048',dir='yeniliste-bastan048',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['TAŞ GİBİ TEREYAĞI','NASIL YUMUŞAR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(165,2),(270,2),(350,3),(485,3),(560,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(200,245,'30','SANİYE','clock','right'),(430,470,'1','DAKİKA','clock','left')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M450 920 C470 880 510 860 565 870 C610 880 640 910 650 950 C660 990 630 1030 580 1040 C520 1050 470 1020 450 985 C440 960 440 940 450 920'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-048.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-048.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-048.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['TAŞ GİBİ TEREYAĞI','NASIL YUMUŞAR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-048-img-1.jpg',quality=92)
