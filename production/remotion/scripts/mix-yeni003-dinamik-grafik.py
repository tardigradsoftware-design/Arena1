#!/usr/bin/env python3
"""Single-take speech, 1.55x throughout, with a quiet synthesized hook and contextual label cues."""
from pathlib import Path
import math, random, struct, subprocess, sys, tempfile, wave
import imageio_ffmpeg

root = Path(__file__).resolve().parents[3]
d = root / 'production/yeni-senaryolar/VID-003'
if len(sys.argv) != 3:
    raise SystemExit('Usage: mix-yeni003-tek-parca-ornek.py muted.mp4 output.mp4')
ff = imageio_ffmpeg.get_ffmpeg_exe()
duration = 481 / 30
with tempfile.TemporaryDirectory() as tmp:
    cue = Path(tmp) / 'intro.wav'
    rate, length = 48000, duration
    rng = random.Random(3003)
    prev = 0.0
    samples = []
    events = [72 / 30, 130 / 30, 197 / 30, 278 / 30]
    for i in range(round(rate * length)):
        t = i / rate
        value = 0.0
        if t < .55:
            prev = 0.96 * prev + 0.04 * rng.uniform(-1, 1)
            env = math.sin(math.pi * t / .55) ** 2
            value += env * (0.05 * prev + 0.035 * math.sin(2 * math.pi * (350 * t + 260 * t * t)))
        for event in events:
            local = t - event
            if 0 <= local < .22:
                value += .045 * (1 - math.exp(-local * 90)) * math.exp(-local * 18) * math.sin(2 * math.pi * (720 * local - 65 * local * local))
        samples.append(struct.pack('<h', int(max(-1, min(1, value)) * 32767)))
    with wave.open(str(cue), 'wb') as w:
        w.setparams((1, 2, rate, len(samples), 'NONE', 'not compressed'))
        w.writeframes(b''.join(samples))
    filters = (
        '[1:a]atempo=1.55,aresample=48000,aformat=channel_layouts=stereo[voice];'
        f'[2:a]atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-22dB,afade=t=out:st=15.6:d=0.4[music];'
        '[3:a]aresample=48000,aformat=channel_layouts=stereo[sfx];'
        f'[voice][music][sfx]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]'
    )
    subprocess.run([ff, '-y', '-hide_banner', '-loglevel', 'error', '-i', sys.argv[1],
                    '-i', str(d/'tek-parca-ornek-anlatim.wav'), '-stream_loop', '-1',
                    '-i', str(root/'production/assets/peaceful_days.mp3'), '-i', str(cue),
                    '-filter_complex', filters, '-map', '0:v', '-map', '[out]',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', sys.argv[2]], check=True)
