from pathlib import Path
import json, shutil

root = Path(__file__).resolve().parents[3]
rem = root / 'production/remotion'
configs = {
    '011': [(0, 'rev2-1.png'), (47, 'detay-1.png'), (104, 'rev2-1.png'), (146, 'detay-1.png'), (355, 'detay-2.png'), (454, 'rev2-4.png')],
    '012': [(0, 'rev2-5.png'), (41, 'rev2-2.png'), (92, 'rev2-5.png'), (175, 'rev2-2.png'), (258, 'detay-1.png'), (432, 'detay-2.png'), (506, 'rev2-5.png')],
}
for ident, shots in configs.items():
    source = root / f'production/sifirdan-yeni/VID-{ident}'
    config = json.loads((rem / f'bastan-{ident}.json').read_text())
    config['dir'] = 'detay' + ident
    config['shots'] = [{'from': frame, 'file': name, 'captionTop': 1480} for frame, name in shots]
    dest = rem / 'public' / config['dir']
    dest.mkdir(parents=True, exist_ok=True)
    for shot in config['shots']:
        shutil.copyfile(source / shot['file'], dest / shot['file'])
    (rem / f'detay-{ident}.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    (rem / f'detay-{ident}.jsx').write_text((rem / f'bastan-{ident}.jsx').read_text().replace(f'bastan-{ident}.json', f'detay-{ident}.json'))
