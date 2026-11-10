from pathlib import Path
import json, shutil
root = Path(__file__).resolve().parents[3]
rem = root / 'production/remotion'
source = root / 'production/sifirdan-yeni/VID-014'
c = json.loads((rem / 'rev2-014.json').read_text())
c['dir'] = 'detay014'
c['shots'] = [{'from': f, 'file': name, 'captionTop': 1480} for f, name in [(0,'rev2-1.png'),(45,'sahne-1.png'),(155,'detay-1.png'),(245,'detay-1.png'),(355,'detay-2.png'),(520,'sahne-3.png'),(580,'rev2-4.png')]]
dest = rem / 'public' / c['dir']
dest.mkdir(parents=True, exist_ok=True)
for shot in c['shots']:
    shutil.copyfile(source / shot['file'], dest / shot['file'])
(rem / 'detay-014.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
(rem / 'detay-014.jsx').write_text((rem / 'rev2-014.jsx').read_text().replace('rev2-014.json', 'detay-014.json'))
