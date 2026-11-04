#!/usr/bin/env python3
"""Mix a single narration take, unique hook and VID-038-based contextual SFX."""
from pathlib import Path
import json, math, random, struct, subprocess, sys, tempfile, wave
import imageio_ffmpeg
root = Path(__file__).resolve().parents[3]
if len(sys.argv)!=4: raise SystemExit('Usage: mix-yeni-seri-tek-parca.py ID muted.mp4 final.mp4')
id, muted, output = sys.argv[1:]
c = json.loads((root/'production/remotion'/f'yeni-seri-{id}.json').read_text())
public = root/'production/remotion/public'; rate=48000; duration=c['frames']/30; n=round(duration*rate); samples=[0.0]*n

def add(filename, frame, gain):
 with wave.open(str(public/filename),'rb') as w:
  assert w.getframerate()==rate and w.getnchannels()==1 and w.getsampwidth()==2
  data=w.readframes(w.getnframes())
 values=struct.unpack('<%dh'%(len(data)//2),data);start=round(frame/30*rate)
 for i,v in enumerate(values[:n-start]): samples[start+i]+=gain*v/32768

# Distinct low, smooth opening for each episode.
rng=random.Random(int(id)*1357); prev=0.0
for i in range(round(.62*rate)):
 t=i/rate;prev=.96*prev+.04*rng.uniform(-1,1);env=math.sin(math.pi*t/.62)**2
 freq=310+int(id)*65
 samples[i]+=env*(.055*prev+.065*math.sin(2*math.pi*(freq*t+250*t*t)))
for event in c['events']: add('sfx-isin.wav',event['from'],.38)
for frame in (c['ctaStart'], c['ctaStart']+4): add('sfx-kaydet.wav',frame,.22)
with tempfile.TemporaryDirectory() as tmp:
 wav=Path(tmp)/'effects.wav'
 with wave.open(str(wav),'wb') as w:
  w.setparams((1,2,rate,n,'NONE','not compressed'));w.writeframes(b''.join(struct.pack('<h',round(max(-1,min(1,x))*32767)) for x in samples))
 filt=(f'[1:a]atempo=1.55,aresample=48000,aformat=channel_layouts=stereo[voice];'
       f'[2:a]atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-22dB,afade=t=out:st={duration-.4}:d=0.4[music];'
       f'[3:a]aresample=48000,aformat=channel_layouts=stereo[sfx];'
       f'[voice][music][sfx]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.85,atrim=duration={duration}[out]')
 subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-y','-hide_banner','-loglevel','error','-i',muted,'-i',str(root/'production/yeni-senaryolar'/f'VID-{id}'/'seri-yeni-anlatim.wav'),'-stream_loop','-1','-i',str(root/'production/assets/peaceful_days.mp3'),'-i',str(wav),'-filter_complex',filt,'-map','0:v','-map','[out]','-c:v','copy','-c:a','aac','-b:a','128k','-movflags','+faststart',output],check=True)
