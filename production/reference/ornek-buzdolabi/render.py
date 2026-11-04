#!/usr/bin/env python3
"""Generate the photo-based example with FFmpeg; run using imageio-ffmpeg."""
from pathlib import Path
import math, random, struct, subprocess, wave
import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
DUR = 16.5
RATE = 48000
# Original synth music: unobtrusive plucked melody + soft pulse (no third-party recording).
rng = random.Random(103)
n = int(DUR * RATE)
buf = [0.0] * n
notes = [261.63,329.63,392.00,329.63,293.66,349.23,440.00,349.23]
for step in range(int(DUR / .4) + 1):
    start = round(step * .4 * RATE)
    for j in range(min(int(.23 * RATE), n - start)):
        t = j / RATE
        env = math.exp(-t * 14)
        note = notes[step % len(notes)]
        pluck = .085 * env * (math.sin(2*math.pi*note*t) + .25*math.sin(4*math.pi*note*t))
        kick = .07*math.exp(-t*35)*math.sin(2*math.pi*(92*t-190*t*t)) if step % 2 == 0 else 0
        tick = .012*math.exp(-t*65)*(rng.random()*2-1)
        buf[start+j] += pluck + kick + tick
with wave.open(str(HERE/'synth-muzik.wav'), 'wb') as w:
    w.setparams((1, 2, RATE, n, 'NONE', 'not compressed'))
    w.writeframes(b''.join(struct.pack('<h', int(max(-1,min(1,v))*32767)) for v in buf))

# Each item is one clip, numbered in the final cut; no fabricated movement/tracking.
shots = [(1,84),(4,72),(1,75),(4,45),(3,75),(3,63),(4,81)]
assert sum(x[1] for x in shots) == 495
args = [FF,'-y','-hide_banner','-loglevel','warning']
for num,_ in shots:
    args += ['-loop','1','-framerate','30','-i',str(HERE/f'gorsel-{num}.png')]
args += ['-i',str(HERE/'anlatim.mp3'),'-i',str(HERE/'synth-muzik.wav')]
filters=[]
for i,(_,frames) in enumerate(shots):
    # Alternating slow push and pull, slight horizontal drift; not physical motion tracking.
    zoom = "min(zoom+0.0009,1.07)" if i%2==0 else "if(eq(on,1),1.065,max(1.01,zoom-0.0007))"
    x = "iw/2-(iw/zoom/2)" if i%2==0 else "iw/2-(iw/zoom/2)+12*sin(on/28)"
    filters.append(f"[{i}:v]scale=1120:1992:force_original_aspect_ratio=increase,crop=1120:1992,zoompan=z='{zoom}':x='{x}':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps=30,trim=end_frame={frames},setsar=1,setpts=PTS-STARTPTS[v{i}]")
filters.append(''.join(f'[v{i}]' for i in range(len(shots)))+'concat=n=7:v=1:a=0[base]')
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# Labels deliberately summarize narration; timing is estimated rather than word-aligned.
def title(text, start, end, y, color='white', size=72):
    return (f"drawtext=fontfile={font}:text='{text}':fontsize={size}:fontcolor={color}:"
            f"borderw=4:bordercolor=black:shadowcolor=black@0.65:shadowx=4:shadowy=5:"
            f"x='(w-text_w)/2+max(0,80-320*(t-{start}))':y={y}:enable='between(t,{start},{end})'")
fx=[]
# Top bar gives strong contrast but does not cover the refrigerator thermometer.
fx.append("drawbox=x=65:y=270:w=950:h=240:color=black@0.60:t=fill:enable='between(t,0,3.5)'")
fx.append(title('BUZDOLABI',0,3.5,300,size=68))
fx.append(title('4°C VE ALTI',0,3.5,390,color='0xFFE23B',size=92))
fx.append("drawbox=x=100:y=295:w=880:h=185:color=black@0.64:t=fill:enable='between(t,3.5,8.6)'")
fx.append(title('TERMOMETREYİ',3.5,8.6,314,size=67))
fx.append(title('ORTA RAFA KOY',3.5,8.6,398,color='0xFFE23B',size=70))
fx.append("drawbox=x=100:y=270:w=880:h=200:color=black@0.67:t=fill:enable='between(t,8.6,13.4)'")
fx.append(title('ÇİĞ ETİ AYRI',8.6,13.4,294,size=72))
fx.append(title('KAPALI KAPTA SAKLA',8.6,13.4,382,color='0xFFE23B',size=54))
fx.append("drawbox=x=100:y=270:w=880:h=200:color=black@0.66:t=fill:enable='between(t,13.4,16.5)'")
fx.append(title('SENİN DOLABIN',13.4,16.5,290,size=68))
fx.append(title('KAÇ DERECE?',13.4,16.5,382,color='0xFFE23B',size=78))
fx.append(title('@kadincayasamax',0,16.5,1540,size=28))
filters.append('[base]'+','.join(fx)+',format=yuv420p[vout]')
filters += ["[7:a]atempo=1.08,aresample=48000,aformat=channel_layouts=stereo,volume=1.0[voice]", "[8:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=.33,afade=t=in:st=0:d=0.25,afade=t=out:st=15.3:d=1.2[music]", "[voice][music]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration=16.5[aout]"]
args += ['-filter_complex',';'.join(filters),'-map','[vout]','-map','[aout]','-t','16.5','-r','30','-c:v','libx264','-preset','veryfast','-crf','24','-c:a','aac','-b:a','128k','-movflags','+faststart',str(HERE/'ornek-buzdolabi.mp4')]
subprocess.run(args,check=True)
