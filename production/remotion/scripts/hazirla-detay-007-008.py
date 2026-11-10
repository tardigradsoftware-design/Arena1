from pathlib import Path
import json, shutil

root = Path(__file__).resolve().parents[3]
rem = root / 'production/remotion'
configs = {
    '007': [(0, 'rev2-1.png'), (42, 'rev2-2-ayna.png'), (94, 'rev2-1.png'), (263, 'detay-1.png'), (360, 'detay-2.png'), (550, 'rev2-4.png')],
    '008': [(0, 'rev2-1.png'), (45, 'rev2-2.png'), (114, 'rev2-1.png'), (238, 'detay-1.png'), (367, 'detay-1.png'), (476, 'detay-2.png'), (540, 'rev2-4.png')],
}
for ident, shots in configs.items():
    source = root / f'production/sifirdan-yeni/VID-{ident}'
    config = json.loads((rem / f'bastan-{ident}.json').read_text())
    config['dir'] = 'detay' + ident
    config['shots'] = [{'from': frame, 'file': name, 'captionTop': 1480} for frame, name in shots]
    config['detailCards'] = []
    dest = rem / 'public' / config['dir']
    dest.mkdir(parents=True, exist_ok=True)
    for shot in config['shots']:
        shutil.copyfile(source / shot['file'], dest / shot['file'])
    (rem / f'detay-{ident}.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    (rem / f'detay-{ident}.jsx').write_text((rem / f'bastan-{ident}.jsx').read_text().replace(f'bastan-{ident}.json', f'detay-{ident}.json'))
