#!/usr/bin/env python3
"""Photo-based new series: FFmpeg only. Timing overlays are approximate, not aligned."""
from pathlib import Path
import imageio_ffmpeg, math, struct, subprocess, sys, wave
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
FF=imageio_ffmpeg.get_ffmpeg_exe(); vid='001'; d=HERE/('VID-'+vid)
# Trim leading detected silence (0.31 s); 9.9 source seconds at 1.65x = 6 output seconds.
split=10.21
filters=(f"[0:a]asplit=2[a][b];[a]atrim=start=0.31:end={split},asetpts=PTS-STARTPTS,atempo=1.65[a1];"
 f"[b]atrim=start={split},asetpts=PTS-STARTPTS,atempo=1.50[b1];[a1][b1]concat=n=2:v=0:a=1,aresample=48000[out]")
subprocess.run([FF,'-y','-hide_banner','-loglevel','error','-i',str(d/'ozgun-anlatim.wav'),'-filter_complex',filters,'-map','[out]',str(d/'yuzsuz-islenmis.wav')],check=True)
with wave.open(str(d/'yuzsuz-islenmis.wav')) as w: secs=w.getnframes()/w.getframerate()
frames=math.ceil((secs+.5)*30); duration=frames/30
# 0.5s bass impact, synthesised original, moderate level.
rate=48000; ns=rate; b=[]
for i in range(ns):
 t=i/rate-.5; x=0 if t<0 else .23*math.sin(2*math.pi*(85*t-105*t*t))*math.exp(-10*t)
 b.append(struct.pack('<h',int(max(-1,min(1,x))*32767)))
with wave.open(str(d/'thud.wav'),'wb') as w: w.setparams((1,2,rate,ns,'NONE','not compressed')); w.writeframes(b''.join(b))
# Three visuals presented in two alternating reframings, photo animation not actual action.
counts=[round(frames*.18),round(frames*.16),round(frames*.18),round(frames*.16),round(frames*.16)]
counts.append(frames-sum(counts)); shots=['parmak','parmak','yuzsuz-1','yuzsuz-1','yuzsuz-2','yuzsuz-2']
a=[FF,'-y','-hide_banner','-loglevel','error']
for p in shots: a+=['-loop','1','-framerate','30','-i',str(d/({'parmak':'test-parmak.png','yuzsuz-1':'yuzsuz-1.png','yuzsuz-2':'yuzsuz-2.png'}[p]))]
a+=['-i',str(d/'yuzsuz-islenmis.wav'),'-stream_loop','-1','-i',str(ROOT/'production/assets/peaceful_days.mp3'),'-i',str(d/'thud.wav')]
f=[]
for i,n in enumerate(counts):
 # Quick push at the 0.5-second cue and slow movement otherwise.
 z="if(lt(on,15),1.02+0.001*on,if(lt(on,19),1.035+(on-15)*0.016,1.10+0.0003*(on-19)))" if i==0 else ("1.05+0.0006*on" if i%2==0 else "1.12-0.0005*on")
 f.append(f"[{i}:v]scale=1120:1992:force_original_aspect_ratio=increase,crop=1120:1992,zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s=1080x1920:fps=30,trim=end_frame={n},setsar=1,setpts=PTS-STARTPTS[v{i}]")
f.append(''.join(f'[v{i}]' for i in range(6))+'concat=n=6:v=1:a=0[base]')
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# V14-inspired opening hook and small lower-middle active-word subtitles.
fx=[]
fx.append("drawbox=x=70:y=230:w=940:h=245:color=black@0.73:t=fill:enable='lt(t,2.1)'")
fx.append(f"drawtext=fontfile={font}:text='AYNAYA':fontcolor=white:fontsize=84:borderw=4:bordercolor=black:x=(w-text_w)/2:y=245:enable='lt(t,2.1)'")
fx.append(f"drawtext=fontfile={font}:text='DİKKAT!':fontcolor=black:fontsize=100:box=1:boxcolor=0xFFE135:boxborderw=14:x=(w-text_w)/2:y=350:enable='lt(t,2.1)'")
# Approximate character-weighted timestamps, not forced alignment.
import re
text="Girdiğiniz soyunma kabinindeki aynaya tırnağınızı dayadığınızda parmağınızla yansımanız arasında boşluk yoksa hemen oradan çıkın! Gerçek aynalarda cam kalınlığından dolayı milimetrik bir boşluk kalır; boşluk olmaması arkadan izlenen çift taraflı bir cam olduğunu gösterir. Peki sen kabine girdiğinde ilk neyi kontrol edersin? Yorumlara yaz ki herkes öğrensin ve bu videoyu kız arkadaşlarına göndermeyi unutma."
words=text.split(); weights=[max(2,len(re.sub(r'[^\w]','',w))) for w in words]; total=sum(weights)
acc=0; times=[]
for w,weight in zip(words,weights):
 start=secs*acc/total; acc+=weight; end=secs*acc/total; times.append((w,start,end))
def stamp(t):
 cs=round(t*100); return f"{cs//360000}:{(cs//6000)%60:02d}:{(cs//100)%60:02d}.{cs%100:02d}"
ass=HERE/'VID-001'/'yuzsuz-altyazi.ass'
lines=['[Script Info]','ScriptType: v4.00+','PlayResX: 1080','PlayResY: 1920','WrapStyle: 2','[V4+ Styles]','Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding','Style: Default,DejaVu Sans,62,&H00000000,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,3,5,1,2,60,60,520,1','[Events]','Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
# Each word is shown with V14-style black/yellow high-contrast tile.
for idx,(w,start,end) in enumerate(times):
 if end<=2.1: continue
 start=max(start,2.1)
 # Two-word phrases: active word yellow, neighbour white. Timestamps are estimated.
 pair=idx-(idx%2); components=[]
 for k in range(pair,min(pair+2,len(times))):
  clean=times[k][0].replace('{','').replace('}','')
  color='35E1FF' if k==idx else 'FFFFFF'
  components.append('{' + '\\1c&H000000&\\3c&H'+color+'&' + '}' + clean)
 lines.append(f"Dialogue: 0,{stamp(start)},{stamp(end)},Default,,0,0,0,,"+' '.join(components))
ass.write_text('\n'.join(lines)+'\n',encoding='utf8')
fx.append(f"ass=filename={ass}")
fx.append(f"drawtext=fontfile={font}:text='kadincayasamax':fontcolor=white:fontsize=28:borderw=2:bordercolor=black:x=65:y=1500:enable='between(t,3,6)+between(t,10,13)+between(t,17,20)'")
f.append('[base]'+','.join(fx)+',format=yuv420p[vout]')
# Gain settings, not measured output dBFS. Limiter prevents additive clipping.
f += [f'[6:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1[voice]',f'[7:a]atrim=duration={duration},asetpts=PTS-STARTPTS,volume=-22dB,afade=t=out:st={max(0,duration-1):.2f}:d=1[music]','[8:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-8dB[thud]',f'[voice][music][thud]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]']
a+=['-filter_complex',';'.join(f),'-map','[vout]','-map','[out]','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','24','-c:a','aac','-b:a','128k','-movflags','+faststart',str(d/'VID-001-yuzsuz-v14-test.mp4')]
subprocess.run(a,check=True)
print(f'VID-{vid}: {duration:.2f}s ({frames} frames); voice {secs:.2f}s')
