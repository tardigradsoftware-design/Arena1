from pathlib import Path
import json, shutil
root = Path(__file__).resolve().parents[3]
rem = root / 'production/remotion'
source = root / 'production/sifirdan-yeni/VID-013'
c = json.loads((rem / 'rev2-013.json').read_text())
c['dir'] = 'detay013'
# The two water steps are shown separately; their combined arrangement is not verified.
c['shots'] = [{'from': f, 'file': name, 'captionTop': 1480} for f, name in [(0,'rev2-1.png'),(45,'sahne-1.png'),(125,'rev2-2.png'),(235,'rev2-1.png'),(315,'detay-5.png'),(405,'detay-4.png'),(575,'rev2-4.png')]]
c.pop('highlight', None)
dest = rem / 'public' / c['dir']
dest.mkdir(parents=True, exist_ok=True)
for shot in c['shots']:
    shutil.copyfile(source / shot['file'], dest / shot['file'])
(rem / 'detay-013.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
(rem / 'detay-013.jsx').write_text((rem / 'rev2-013.jsx').read_text().replace('rev2-013.json', 'detay-013.json'))
