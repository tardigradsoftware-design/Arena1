from pathlib import Path
import json, shutil
r=Path(__file__).resolve().parents[3]; rem=r/'production/remotion'; d=r/'production/sifirdan-yeni/VID-002'
c=json.loads((rem/'bastan-002.json').read_text()); c['dir']='detay002'
c['shots']=[{'from':a,'file':f,**({'captionTop':1480} if f.startswith('detay-') else {})} for a,f in [(0,'rev2-1.png'),(45,'rev2-2.png'),(210,'rev2-2.png'),(300,'detay-3.png'),(375,'detay-1.png'),(490,'detay-4.png')]]
c['detailCards']=[{'from':325,'to':405,'top':510,'left':60,'width':425,'lines':['Kuru kauçuk kenarı','halıya bastır;','kendine doğru çek.']}]
dest=rem/'public'/c['dir']; dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'detay-002.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/'detay-002.jsx').write_text((rem/'bastan-002.jsx').read_text().replace('bastan-002.json','detay-002.json'))
