#!/usr/bin/env python3
"""Process original narration and mix music + synthesized cues to a muted Remotion render."""
from pathlib import Path
import math, struct, subprocess, sys, tempfile, wave
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[3]; D=ROOT/'production/yeni-senaryolar/VID-001'; FF=imageio_ffmpeg.get_ffmpeg_exe(); duration=607/30
if len(sys.argv)!=3: raise SystemExit('Usage: mix-yeni001-cta.py MUTED.mp4 FINAL.mp4')
with tempfile.TemporaryDirectory(prefix='yenivid001-') as td:
 p=Path(td); voice=p/'voice.wav'; cues=p/'cues.wav'
 # 0.31 sec initial silence removed. 9.9s at 1.65x produces ~6 output sec.
 af='[0:a]atrim=start=0.31:end=22.78,asetpts=PTS-STARTPTS,atempo=1.55,aresample=48000[out]'
 subprocess.run([FF,'-y','-hide_banner','-loglevel','error','-i',str(D/'ozgun-anlatim.wav'),'-filter_complex',af,'-map','[out]',str(voice)],check=True)
 r=48000;n=round(duration*r); audio=[0.0]*n
 def add(time,length,func):
  start=round(time*r)
  for j in range(min(round(length*r),n-start)):
   t=j/r;audio[start+j]+=func(t)
 # Moderate low thud at 0.5 and short synthesized UI chimes at CTA arrival.
 add(.5,.45,lambda t:.22*math.sin(2*math.pi*(85*t-105*t*t))*math.exp(-10*t))
 for when,freq in [(2.33,540),(3.73,570),(7.63,590),(9.6,620),(11.97,540),(14.17,720),(15.97,660),(16.37,740),(16.77,810),(17.17,880),(17.63,960)]:
  add(when,.22,lambda t,freq=freq:.075*math.sin(2*math.pi*freq*t)*math.exp(-22*t))
 with wave.open(str(cues),'wb') as w:
  w.setparams((1,2,r,n,'NONE','not compressed')); w.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,x))*32767)) for x in audio))
 args=[FF,'-y','-hide_banner','-loglevel','error','-i',sys.argv[1],'-i',str(voice),'-stream_loop','-1','-i',str(ROOT/'production/assets/peaceful_days.mp3'),'-i',str(cues),'-i',str(ROOT/'production/assets/whoosh.wav')]
 f=[f'[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1[v]',f'[2:a]atrim=duration={duration},asetpts=PTS-STARTPTS,volume=-22dB,afade=t=out:st=19.0:d=1.2[m]','[3:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-8dB[c]','[4:a]asplit=2[w0][w1]','[w0]volume=0.08,adelay=700:all=1[s0]','[w1]volume=0.08,adelay=5667:all=1[s1]',f'[v][m][c][s0][s1]amix=inputs=5:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]']
 args+=['-filter_complex',';'.join(f),'-map','0:v:0','-map','[out]','-c:v','copy','-c:a','aac','-b:a','128k','-movflags','+faststart',sys.argv[2]]
 subprocess.run(args,check=True)
