from pathlib import Path
import json, shutil
r=Path(__file__).resolve().parents[3]; rem=r/'production/remotion'
config={'003':[(0,'rev2-1.png'),(45,'rev2-2.png'),(130,'rev2-1.png'),(205,'detay-1.png'),(355,'detay-2.png'),(500,'rev2-4.png')], '004':[(0,'rev2-1.png'),(45,'rev2-2.png'),(110,'rev2-1.png'),(190,'detay-1.png'),(290,'detay-2.png'),(440,'rev2-4.png')]}
for id,shots in config.items():
 d=r/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/f'bastan-{id}.json').read_text());c['dir']='detay'+id
 c['shots']=[{'from':a,'file':f,'captionTop':1480} for a,f in shots]
 c['detailCards']=([{'from':385,'to':450,'top':550,'left':55,'width':300,'lines':['Folyoyu','top yapıp','hafifçe sil']} ] if id=='003' else [{'from':210,'to':275,'top':500,'left':55,'width':420,'lines':['Macun + karbonat','+ birkaç damla','bulaşık deterjanı']},{'from':310,'to':400,'top':500,'left':55,'width':350,'lines':['Lastik kenarı','fırçala']}])
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'detay-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'detay-{id}.jsx').write_text((rem/f'bastan-{id}.jsx').read_text().replace(f'bastan-{id}.json',f'detay-{id}.json'))
