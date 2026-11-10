from pathlib import Path
import json, shutil
root = Path(__file__).resolve().parents[3]
rem = root / 'production/remotion'
source = root / 'production/sifirdan-tam/VID-015'
new = root / 'production/sifirdan-yeni/VID-015'
c = json.loads((rem / 'cta-ornek-015.json').read_text())
c['dir'] = 'detay015'
c['shots'] = [{'from': f, 'file': name} for f, name in [(0,'sahne-2.png'), (45,'sahne-1.png'), (155,'sahne-3.png'), (300,'detay-1.png'), (345,'sahne-1.png'), (460,'sahne-2.png')]]
c['representativeFiles'] = list(dict.fromkeys(s['file'] for s in c['shots']))
c.pop('highlight', None)
dest = rem / 'public' / c['dir']; dest.mkdir(parents=True, exist_ok=True)
for name in c['representativeFiles']:
    shutil.copyfile((new if name.startswith('detay-') else source) / name, dest / name)
(rem / 'detay-015.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
(rem / 'detay-015.jsx').write_text((rem / 'cta-ornek-015.jsx').read_text().replace('cta-ornek-015.json', 'detay-015.json'))
