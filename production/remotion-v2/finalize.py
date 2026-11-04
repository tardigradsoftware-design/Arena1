"""Size-budgeted two-pass H.264 master with AAC audio and loudness limit."""
import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path
import imageio_ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('output')
parser.add_argument('--seconds', type=float, required=True)
parser.add_argument('--max-mb', type=float, default=10)
a = parser.parse_args()
if a.seconds <= 0 or a.max_mb <= 0:
    parser.error('seconds and max-mb must be positive')
# Keep 6% overhead margin; never inflate the master above a sensible 1.7 Mbps.
video_kbps = min(1700, int((a.max_mb * 1_000_000 * 8 * .94 / a.seconds - 128_000) / 1000))
if video_kbps < 200:
    parser.error('size budget too small for video')
ff = imageio_ffmpeg.get_ffmpeg_exe()
with tempfile.TemporaryDirectory() as temp:
    log = os.path.join(temp, 'pass')
    common = ['-c:v','libx264','-preset','medium','-b:v',f'{video_kbps}k','-pix_fmt','yuv420p','-r','30']
    subprocess.run([ff,'-y','-loglevel','error','-i',a.source,*common,'-pass','1','-passlogfile',log,'-an','-f','null',os.devnull],check=True)
    subprocess.run([ff,'-y','-loglevel','error','-i',a.source,*common,'-pass','2','-passlogfile',log,'-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:a','aac','-b:a','128k','-ar','48000','-movflags','+faststart',a.output],check=True)
size = Path(a.output).stat().st_size
if size > a.max_mb*1_000_000:
    raise SystemExit(f'Output exceeds size budget: {size} bytes')
print(json.dumps({'duration_seconds':a.seconds,'video_kbps':video_kbps,'audio_kbps':128,'size_bytes':size}))
