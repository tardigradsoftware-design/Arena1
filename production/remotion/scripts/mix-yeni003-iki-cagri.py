#!/usr/bin/env python3
"""Mix a closing-style test. Speech splice and captions are approximate, pending listening review."""
from pathlib import Path
import subprocess, sys
import imageio_ffmpeg

root = Path(__file__).resolve().parents[3]
d = root / 'production/yeni-senaryolar/VID-003'
if len(sys.argv) != 3:
    raise SystemExit('Usage: mix-yeni003-iki-cagri.py muted.mp4 output.mp4')
ff = imageio_ffmpeg.get_ffmpeg_exe()
duration = 476 / 30
filters = (
    '[1:a]atempo=1.55,atrim=0:14.35,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo[main];'
    '[2:a]atempo=1.55,atrim=0.18:1.68,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo[cta];'
    '[main][cta]concat=n=2:v=0:a=1[voice];'
    f'[3:a]atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-22dB,afade=t=out:st=15.45:d=0.4[music];'
    f'[voice][music]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.85,apad,atrim=duration={duration}[out]'
)
subprocess.run([ff, '-y', '-hide_banner', '-loglevel', 'error', '-i', sys.argv[1],
                '-i', str(d/'ozgun-anlatim.wav'), '-i', str(d/'cta-kaydet-gonder.wav'),
                '-stream_loop', '-1', '-i', str(root/'production/assets/peaceful_days.mp3'),
                '-filter_complex', filters, '-map', '0:v', '-map', '[out]', '-c:v', 'copy',
                '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', sys.argv[2]], check=True)
