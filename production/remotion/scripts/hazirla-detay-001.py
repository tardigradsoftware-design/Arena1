from pathlib import Path
import json, shutil
r=Path(__file__).resolve().parents[3]; rem=r/'production/remotion'; d=r/'production/sifirdan-yeni/VID-001'
c=json.loads((rem/'bastan-001.json').read_text()); c['dir']='detay001'
c['shots']=[{'from':a,'file':f,'captionTop':1480} for a,f in [(0,'rev2-1.png'),(45,'rev2-2.png'),(210,'detay-5.png'),(405,'detay-8.png'),(515,'detay-4.png')]]
c['detailCards']=[{'from':290,'to':380,'top':510,'left':60,'width':340,'lines':['İki kenara','küçük çapraz','çentikler']},{'from':425,'to':500,'top':1030,'left':60,'width':370,'lines':['Giderden içeri','yerleştir ve çevir']}]
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'detay-001.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/'detay-001.jsx').write_text((rem/'bastan-001.jsx').read_text().replace('bastan-001.json','detay-001.json'))
