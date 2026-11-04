"""Create a labeled review sheet for comparing consecutive source images.

This is a visual aid, not a detector or approval. Review originals as well.
"""
import argparse
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('images', nargs='+', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--columns', type=int, default=4)
    args = parser.parse_args()
    if not 1 <= args.columns <= 8:
        parser.error('columns must be between 1 and 8')
    thumb_w, thumb_h, label_h = 270, 480, 42
    cols = min(args.columns, len(args.images))
    rows = math.ceil(len(args.images) / cols)
    sheet = Image.new('RGB', (cols * thumb_w, rows * (thumb_h + label_h)), '#191919')
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, path in enumerate(args.images):
        with Image.open(path) as image:
            thumb = ImageOps.contain(ImageOps.exif_transpose(image).convert('RGB'), (thumb_w, thumb_h))
        x, y = (i % cols) * thumb_w, (i // cols) * (thumb_h + label_h)
        sheet.paste(thumb, (x + (thumb_w - thumb.width)//2, y + (thumb_h - thumb.height)//2))
        draw.text((x + 5, y + thumb_h + 8), path.name[:38], fill='white', font=font)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output)
    print(args.output)


if __name__ == '__main__':
    main()
