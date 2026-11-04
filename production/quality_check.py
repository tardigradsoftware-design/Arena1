"""Build a scene contact sheet for manual visual review, not automatic approval."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('video', type=int)
args = parser.parse_args()
root = Path(__file__).resolve().parent
paths = [root / 'images' / f'VID-{args.video:03d}-{i}.png' for i in range(1, 5)]
for path in paths:
    if not path.is_file():
        parser.error(f'Missing image: {path}')
sheet = Image.new('RGB', (1200, 570), 'white')
draw = ImageDraw.Draw(sheet)
for i, path in enumerate(paths):
    with Image.open(path) as image:
        image.thumbnail((290, 520))
        sheet.paste(image.convert('RGB'), (i * 300 + (300-image.width)//2, 35))
        draw.text((i * 300 + 8, 8), path.name, fill='black')
out = root / f'check-VID-{args.video:03d}.jpg'
sheet.save(out, quality=92)
print(out)
