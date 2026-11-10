from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion'
data={'010':dict(b=26.55,oldb=27.95,shots=[(0,1),(45,4),(105,1),(160,5),(298,4),(386,6),(500,4)],cover=['KAVANOZ KAPAĞI','NASIL AÇILIR?'],highlight=(5,165,210,'M 285 478 C 315 450 365 439 405 450 C 435 458 440 482 421 499 C 395 513 346 514 315 503 C 297 497 285 490 285 478')),'011':dict(b=29.05,oldb=27.85,shots=[(0,1),(45,2),(100,1),(140,2),(340,3),(435,4)],cover=['BAYAT EKMEK','NASIL YUMUŞAR?'],highlight=(4,445,490,'M 192 801 C 195 765 230 742 271 745 C 315 746 349 768 358 801 C 366 832 342 859 308 866 C 265 876 221 858 201 838 C 192 829 190 815 192 801'))}
for id,v in data.items():
 d=root/'production/sifirdan-yeni'/f'VID-{id}';c=json.loads((rem/f'yeniden-{id}.json').read_text());b=v['b']
 with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 cta=round(b/1.55*30);ratio=cta/c['ctaStart']
 for e in c['events']:e['from']=round(e['from']*ratio);e['to']=min(cta,round(e['to']*ratio))
 ix,start,end,path=v['highlight']
 c.update(dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=cta,tempoBoundary=b,ctaStackFrames=[round((b/1.55+x/1.62)*30) for x in [2,2.7,3.4,4.25]],shots=[{'from':round(a*ratio),'file':f'rev2-{n}.png'} for a,n in v['shots']],highlight={'file':f'rev2-{ix}.png','from':round(start*ratio),'to':round(end*ratio),'path':path})
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/f'yeniden-{id}.jsx').read_text().replace(f'yeniden-{id}.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',68),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-bastan-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
