#!/usr/bin/env python3
"""Mix the single-take narration with the original VID-038 synthetic card/clock effects.

Generate the public WAVs first using make-beam-sfx.py, make-fast-tick.py and
make-hook-save-sfx.py. Timings are tied to yeni-vid003-cagri-altyazisiz.jsx.
"""
from pathlib import Path
import math, random, struct, subprocess, sys, tempfile, wave
import imageio_ffmpeg

root = Path(__file__).resolve().parents[3]
public = root / 'production/remotion/public'
d = root / 'production/yeni-senaryolar/VID-003'
if len(sys.argv) != 3:
    raise SystemExit('Usage: mix-yeni003-vid038-referans.py muted.mp4 output.mp4')
ff = imageio_ffmpeg.get_ffmpeg_exe()
rate = 48000
duration = 481 / 30
length = round(rate * duration)
audio = [0.0] * length

def cue(filename, frame, gain):
    with wave.open(str(public / filename), 'rb') as w:
        assert w.getframerate() == rate and w.getnchannels() == 1 and w.getsampwidth() == 2
        data = w.readframes(w.getnframes())
    values = struct.unpack('<%dh' % (len(data) // 2), data)
    start = round(frame / 30 * rate)
    for i, value in enumerate(values[:max(0, length - start)]):
        audio[start + i] += gain * value / 32768

# Keep this video's unique synthesized opening rather than reusing VID-038's hook.
rng = random.Random(3003)
prev = 0.0
for i in range(round(rate * .55)):
    t = i / rate
    prev = .96 * prev + .04 * rng.uniform(-1, 1)
    env = math.sin(math.pi * t / .55) ** 2
    audio[i] += env * (.05 * prev + .035 * math.sin(2 * math.pi * (350 * t + 260 * t * t)))

# VID-038 source: contextual beam effect gain .38; repeated fast tick gain .14.
for frame in (72, 130, 197, 278):
    cue('sfx-isin.wav', frame, .38)
for frame in range(278, 336, 4):
    cue('sfx-fast-tick.wav', frame, .14)
# Match the two CTA entrances with the source's save cue, at a reduced gain.
for frame in (433, 436):
    cue('sfx-kaydet.wav', frame, .22)

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / 'effects.wav'
    with wave.open(str(path), 'wb') as w:
        w.setparams((1, 2, rate, length, 'NONE', 'not compressed'))
        w.writeframes(b''.join(struct.pack('<h', round(max(-1, min(1, x)) * 32767)) for x in audio))
    filters = (
        '[1:a]atempo=1.55,aresample=48000,aformat=channel_layouts=stereo[voice];'
        f'[2:a]atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-22dB,afade=t=out:st=15.6:d=0.4[music];'
        '[3:a]aresample=48000,aformat=channel_layouts=stereo[sfx];'
        f'[voice][music][sfx]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]'
    )
    subprocess.run([ff, '-y', '-hide_banner', '-loglevel', 'error', '-i', sys.argv[1],
                    '-i', str(d/'tek-parca-ornek-anlatim.wav'), '-stream_loop', '-1',
                    '-i', str(root/'production/assets/peaceful_days.mp3'), '-i', str(path),
                    '-filter_complex', filters, '-map', '0:v', '-map', '[out]',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', sys.argv[2]], check=True)
