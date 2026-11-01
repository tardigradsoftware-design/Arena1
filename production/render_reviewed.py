"""Remotion gate. Pass every actual static image used by the composition."""
import argparse
from pathlib import Path
import subprocess
import sys
from image_quality import validate, QualityError

p=argparse.ArgumentParser(description='Review-gated Remotion runner')
p.add_argument('--review', type=Path, required=True)
p.add_argument('--image', type=Path, action='append', required=True)
p.add_argument('--cwd', type=Path, required=True)
p.add_argument('command', nargs=argparse.REMAINDER)
a=p.parse_args()
if not a.command or a.command[0] != '--' or len(a.command) < 2:
    p.error('supply the render command after --')
try:
    validate(a.review, a.image)
except QualityError as e:
    print(f'Görsel kalite denetiminden geçmedi: {e}', file=sys.stderr)
    raise SystemExit(2)
subprocess.run(a.command[1:], cwd=a.cwd, check=True)
