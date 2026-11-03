"""Mix VID-001 HD test soundtrack with FFmpeg, retaining rendered video without re-encoding.

Run from the repository root using production/.venv/bin/python. `imageio-ffmpeg`
provides the executable; all assets and their licenses are recorded in the report.
"""
from pathlib import Path
import subprocess
import sys
import imageio_ffmpeg

if len(sys.argv) != 3:
    raise SystemExit('Usage: mix-vid001-sinematik.py muted-video.mp4 final.mp4')
root = Path(__file__).resolve().parents[3]
public = root / 'production/remotion/public'
inputs = [Path(sys.argv[1]), public/'VID-001-voice.wav', public/'peaceful_days.mp3', public/'sfx-hook-merak.wav', public/'sfx-isin.wav', public/'sfx-result-chime.wav', public/'sfx-kaydet.wav', root/'production/assets/whoosh.wav']
for item in inputs:
    if not item.is_file():
        raise SystemExit(f'Missing input: {item}')
args = [imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-hide_banner', '-loglevel', 'error']
for item in inputs:
    args += ['-i', str(item)]
filters = [
    '[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1.0[voice]',
    '[2:a]atrim=duration=23.6667,asetpts=PTS-STARTPTS,volume=0.09,afade=t=in:st=0:d=0.4,afade=t=out:st=22.1:d=1.55[music]',
    '[3:a]volume=0.42[hook]',
    '[5:a]volume=0.30,adelay=15667:all=1[result]',
    '[6:a]volume=0.36,adelay=17867:all=1[save]',
    '[4:a]asplit=4[beam0][beam1][beam2][beam3]',
    '[beam0]volume=0.25,adelay=7367:all=1[b0]',
    '[beam1]volume=0.25,adelay=8500:all=1[b1]',
    '[beam2]volume=0.25,adelay=9900:all=1[b2]',
    '[beam3]volume=0.25,adelay=11533:all=1[b3]',
    '[7:a]asplit=2[wash0][wash1]',
    '[wash0]volume=0.12,adelay=6267:all=1[w0]',
    '[wash1]volume=0.12,adelay=15333:all=1[w1]',
    '[voice][music][hook][result][save][b0][b1][b2][b3][w0][w1]amix=inputs=11:duration=longest:normalize=0,alimiter=limit=0.89,atrim=duration=23.6667[aout]',
]
args += ['-filter_complex', ';'.join(filters), '-map', '0:v:0', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', sys.argv[2]]
subprocess.run(args, check=True)
