from pathlib import Path
import json,shutil
r=Path(__file__).resolve().parents[3];rem=r/'production/remotion'
configs={'005':[(0,'rev2-1.png'),(41,'rev2-5.png'),(119,'rev2-1.png'),(179,'detay-1.png'),(275,'detay-2.png'),(431,'rev2-4.png')],'006':[(0,'rev2-1.png'),(42,'rev2-2.png'),(112,'rev2-1.png'),(183,'detay-1.png'),(272,'detay-2.png'),(436,'rev2-4.png')]}
for id,shots in configs.items():
 d=r/f'production/sifirdan-yeni/VID-{id}'; c=json.loads((rem/f'bastan-{id}.json').read_text());c['dir']='detay'+id;c['shots']=[{'from':a,'file':f,'captionTop':1480} for a,f in shots]
 c['detailCards']=([{'from':300,'to':380,'top':510,'left':55,'width':360,'lines':['Yayı kablo ucuna','döndürerek sar']}] if id=='005' else [{'from':200,'to':260,'top':480,'left':55,'width':350,'lines':['Eldiven giy','tabletin ucunu','ılık suya batır']},{'from':300,'to':390,'top':500,'left':55,'width':380,'lines':['Islak camdaki','lekenin üzerinde','tableti gezdir']}])
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'detay-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/f'detay-{id}.jsx').write_text((rem/f'bastan-{id}.jsx').read_text().replace(f'bastan-{id}.json',f'detay-{id}.json'))
