#!/usr/bin/env python3
"""Photo-based new series: FFmpeg only. Timing overlays are approximate, not aligned."""
from pathlib import Path
import imageio_ffmpeg, math, struct, subprocess, sys, wave
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
FF=imageio_ffmpeg.get_ffmpeg_exe(); vid='001'; d=HERE/('VID-'+vid)
# The split is in a detected pause, not exactly the third output second.
split=4.54
filters=(f"[0:a]asplit=2[a][b];[a]atrim=start=0:end={split},asetpts=PTS-STARTPTS,atempo=1.22[a1];"
 f"[b]atrim=start={split},asetpts=PTS-STARTPTS,atempo=1.12[b1];[a1][b1]concat=n=2:v=0:a=1,"
 "silenceremove=start_periods=1:start_duration=0.04:start_threshold=-38dB:stop_periods=-1:stop_duration=0.15:stop_threshold=-38dB:stop_silence=0.08,aresample=48000[out]")
subprocess.run([FF,'-y','-hide_banner','-loglevel','error','-i',str(d/'ozgun-anlatim.wav'),'-filter_complex',filters,'-map','[out]',str(d/'ozgun-islenmis.wav')],check=True)
with wave.open(str(d/'ozgun-islenmis.wav')) as w: secs=w.getnframes()/w.getframerate()
frames=math.ceil((secs+.5)*30); duration=frames/30
# 0.5s bass impact, synthesised original, moderate level.
rate=48000; ns=rate; b=[]
for i in range(ns):
 t=i/rate-.5; x=0 if t<0 else .23*math.sin(2*math.pi*(85*t-105*t*t))*math.exp(-10*t)
 b.append(struct.pack('<h',int(max(-1,min(1,x))*32767)))
with wave.open(str(d/'thud.wav'),'wb') as w: w.setparams((1,2,rate,ns,'NONE','not compressed')); w.writeframes(b''.join(b))
# Three visuals presented in two alternating reframings, photo animation not actual action.
counts=[round(frames*.18),round(frames*.16),round(frames*.18),round(frames*.16),round(frames*.16)]
counts.append(frames-sum(counts)); shots=[1,'parmak',2,3,3,4]
a=[FF,'-y','-hide_banner','-loglevel','error']
for p in shots: a+=['-loop','1','-framerate','30','-i',str(d/f'test-{p}.png')]
a+=['-i',str(d/'ozgun-islenmis.wav'),'-stream_loop','-1','-i',str(ROOT/'production/assets/peaceful_days.mp3'),'-i',str(d/'thud.wav')]
f=[]
for i,n in enumerate(counts):
 # Quick push at the 0.5-second cue and slow movement otherwise.
 z="if(lt(on,15),1.02+0.001*on,if(lt(on,19),1.035+(on-15)*0.016,1.10+0.0003*(on-19)))" if i==0 else ("1.05+0.0006*on" if i%2==0 else "1.12-0.0005*on")
 f.append(f"[{i}:v]scale=1120:1992:force_original_aspect_ratio=increase,crop=1120:1992,zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s=1080x1920:fps=30,trim=end_frame={n},setsar=1,setpts=PTS-STARTPTS[v{i}]")
f.append(''.join(f'[v{i}]' for i in range(6))+'concat=n=6:v=1:a=0[base]')
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
texts=[['SOYUNMA KABİNİNDE','AYNAYA DİKKAT!'],['TIRNAK VE','YANSIMA ARASI'],['AYNADAKİ BOŞLUK','KONUSU'],['SEN NEYİ','KONTROL EDERSİN?']]
ends=[3.0,duration*.48,duration*.76,duration]; starts=[0]+ends[:-1]
fx=[]
for j,((top,bottom),start,end) in enumerate(zip(texts,starts,ends)):
 fx.append(f"drawbox=x=55:y=240:w=970:h=230:color=black@0.67:t=fill:enable='between(t,{start:.2f},{end:.2f})'")
 for text,y,size,color in [(top,265,66,'white'),(bottom,355,56,'0xFFE135')]:
  fx.append(f"drawtext=fontfile={font}:text='{text}':fontcolor={color}:fontsize={size}:borderw=3:bordercolor=black:x='(w-text_w)/2+max(0,100-400*(t-{start:.2f}))':y={y}:enable='between(t,{start:.2f},{end:.2f})'")
fx.append(f"drawtext=fontfile={font}:text='@kadincayasamax':fontcolor=white:fontsize=30:borderw=3:bordercolor=black:x=(w-text_w)/2:y=1550")
f.append('[base]'+','.join(fx)+',format=yuv420p[vout]')
# Gain settings, not measured output dBFS. Limiter prevents additive clipping.
f += [f'[6:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1[voice]',f'[7:a]atrim=duration={duration},asetpts=PTS-STARTPTS,volume=-22dB,afade=t=out:st={max(0,duration-1):.2f}:d=1[music]','[8:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-8dB[thud]',f'[voice][music][thud]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]']
a+=['-filter_complex',';'.join(f),'-map','[vout]','-map','[out]','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','24','-c:a','aac','-b:a','128k','-movflags','+faststart',str(d/'VID-001-ozgun-test.mp4')]
subprocess.run(a,check=True)
print(f'VID-{vid}: {duration:.2f}s ({frames} frames); voice {secs:.2f}s')
