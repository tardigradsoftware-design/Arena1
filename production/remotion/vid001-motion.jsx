import React from 'react';
import {AbsoluteFill, Audio, Composition, Img, Sequence, interpolate, registerRoot, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import captions from './vid001-captions.json';

const shots = [
 {from:0,file:'VID-001-a.png',focus:'50% 55%',scale:1.01},
 {from:98,file:'VID-001-a.png',focus:'50% 70%',scale:1.03},
 {from:188,file:'VID-001-b.png',focus:'50% 52%',scale:1.01},
 {from:275,file:'VID-001-b.png',focus:'50% 60%',scale:1.03},
 {from:338,file:'VID-001-c.png',focus:'50% 52%',scale:1.01},
 {from:460,file:'VID-001-d.png',focus:'50% 40%',scale:1.01},
 {from:550,file:'VID-001-d.png',focus:'50% 38%',scale:1.03},
];
const slideFrames=7;
const ease=(t)=>1-Math.pow(1-t,3);
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'};

function Background(){
 const f=useCurrentFrame();
 return <AbsoluteFill style={{backgroundColor:'#13110f',overflow:'hidden'}}>
  {shots.map((shot,i)=>{
    const next=shots[i+1]?.from??99999;
    if(f<shot.from || f>=next+slideFrames) return null;
    const p=interpolate(f-shot.from,[0,slideFrames],[0,1],clamp);
    const dir=i%2?1:-1;
    const x=i===0?0:dir*(1-ease(p))*720;
    const age=Math.max(f-shot.from,0); const zoom=shot.scale+0.045*ease(Math.min(age/100,1));
    return <AbsoluteFill key={i} style={{transform:`translateX(${x}px)`, overflow:'hidden'}}>
      <Img src={staticFile(shot.file)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:shot.focus,transform:`scale(${zoom})`}}/>
      <AbsoluteFill style={{background:'linear-gradient(180deg,rgba(11,9,9,.22) 0%,rgba(11,9,9,0) 38%,rgba(11,9,9,.15) 100%)'}}/>
    </AbsoluteFill>;
  })}
 </AbsoluteFill>;
}
function Hook(){
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 if(f>=60)return null;
 const entrance=spring({frame:f,fps,config:{damping:17,stiffness:230,mass:.7}});
 const opacity=interpolate(f,[0,2,48,59],[0.8,1,1,0],clamp);
 const scale=0.7+0.3*entrance;
 return <AbsoluteFill style={{opacity,pointerEvents:'none'}}>
    <div style={{position:'absolute',top:230,left:50,width:610,transform:`translateY(${(1-entrance)*-34}px) scale(${scale})`,transformOrigin:'center',fontFamily:'Arial, sans-serif',fontWeight:950,textAlign:'center',lineHeight:1.03,filter:'drop-shadow(0px 8px 6px rgba(0,0,0,.6))'}}>
     <div style={{display:'inline-block',fontSize:105,color:'#201510',background:'#ffe135',padding:'3px 32px 5px',transform:'rotate(-3deg)',borderRadius:8,letterSpacing:'-3px'}}>SAKIN!</div>
     <div style={{fontSize:42,color:'white',marginTop:14,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>SARARAN KILIFLARI</div>
     <div style={{fontSize:46,color:'white',marginTop:3,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>ÇÖPE ATMA<br/><span style={{color:'#ffe135'}}>YIPRATMA!</span></div>
    </div>
    <div style={{position:'absolute',left:75,top:240,width:31,height:10,background:'#fff',transform:`rotate(-25deg) scaleX(${entrance})`,borderRadius:8}}/>
    <div style={{position:'absolute',right:82,top:345,width:26,height:9,background:'#ffe135',transform:`rotate(30deg) scaleX(${entrance})`,borderRadius:8}}/>
 </AbsoluteFill>;
}
function Captions(){
 const f=useCurrentFrame(), t=f/30;
 const cap=captions.find(c=>t>=c.start && t<c.end);
 if(!cap || f<60)return null;
 return <div style={{position:'absolute',top:640,left:35,width:650,transform:'translateY(-50%)',textAlign:'center',fontFamily:'Arial, sans-serif',fontSize:45,fontWeight:900,letterSpacing:-.3,lineHeight:1.2,color:'white',textShadow:'0 2px 1px #000, 0 0 7px #000, 2px 2px 4px #000',WebkitTextStroke:'1px #111'}}>
  {cap.words.map((w,i)=><React.Fragment key={i}><span style={{color:i===cap.active?'#ffe230':'#fff'}}>{w}</span>{i<cap.words.length-1?' ':''}</React.Fragment>)}
 </div>;
}
// Word-linked timing is approximate (Vosk + interpolation), not verified alignment.
function Marker({type}) {
 if(type==='spoon') return <svg viewBox="0 0 100 100" width="72" height="72"><ellipse cx="36" cy="35" rx="19" ry="14" fill="#f3efe7" stroke="#25211b" strokeWidth="4"/><path d="M49 43 L81 78" stroke="#eee9df" strokeWidth="10" strokeLinecap="round"/><path d="M49 43 L81 78" stroke="#25211b" strokeWidth="3" strokeLinecap="round"/></svg>;
 if(type==='tablet') return <svg viewBox="0 0 100 100" width="72" height="72"><rect x="19" y="25" width="62" height="52" rx="13" fill="#eee8db" stroke="#25211b" strokeWidth="4"/><rect x="24" y="31" width="52" height="16" rx="5" fill="#5badb6"/><circle cx="50" cy="55" r="10" fill="#8bb9cb" stroke="#25211b" strokeWidth="3"/></svg>;
 if(type==='glass') return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M28 20 Q49 26 72 20 L66 42 Q62 54 70 75 Q50 81 30 75 Q38 54 34 42 Z" fill="#d9eef1" fillOpacity=".9" stroke="#25211b" strokeWidth="4"/><path d="M35 53 Q50 57 65 53 L70 75 Q50 81 30 75Z" fill="#b7d7d4" fillOpacity=".65"/></svg>;
 return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M26 14 H74 V86 L50 70 L26 86 Z" fill="#ffe135" stroke="#25211b" strokeWidth="5" strokeLinejoin="round"/></svg>;
}
function InfoMotion(){
 const f=useCurrentFrame(), {fps}=useVideoConfig();
 // Entry times follow the source's word estimates and must be checked against the voice.
 const scenes=[
  {from:228,to:253, label:'KARBONAT', icon:'spoon'},
  {from:260,to:284, label:'BULAŞIK DETERJANI', icon:'tablet'},
  {from:307,to:332, label:'BEYAZ SİRKE', icon:'glass'},
  {from:542,to:575, label:'KAYDET', icon:'save'}
 ];
 const item=scenes.find(x=>f>=x.from&&f<x.to); if(!item)return null;
 const t=f-item.from; const p=spring({frame:t,fps,config:{damping:18,stiffness:190,mass:.65}});
 const alpha=interpolate(f,[item.from,item.from+4,item.to-5,item.to],[0,1,1,0],clamp);
 const line=Math.min(1,Math.max(0,(t-3)/12));
 return <AbsoluteFill style={{pointerEvents:'none',opacity:alpha}}>
  <div style={{position:'absolute',top:210,left:64,display:'flex',alignItems:'center',gap:10,transform:`translateY(${(1-p)*-30}px) scale(${.85+.15*p})`,transformOrigin:'left center',filter:'drop-shadow(0px 7px 7px rgba(0,0,0,.42))'}}>
   <div style={{width:80,height:80,display:'grid',placeItems:'center',background:'#fff8e5',border:'3px solid #211d19',borderRadius:18}}><Marker type={item.icon}/></div>
   <div style={{font:'900 28px Arial',background:'#fff8e5',color:'#211d19',padding:'14px 18px',border:'3px solid #211d19',borderRadius:12,boxShadow:'4px 5px 0 #211d19',maxWidth:440}}>{item.label}</div>
  </div>
  <svg viewBox="0 0 720 1280" style={{position:'absolute',inset:0,width:'100%',height:'100%',filter:'drop-shadow(0 2px 2px #111)'}}><path d="M 95 326 C 115 365 145 375 195 390 M 195 390 L 179 374 M 195 390 L 174 393" fill="none" stroke="#ffe135" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-line}/></svg>
 </AbsoluteFill>;
}
function Progress(){
 const f=useCurrentFrame(); const total=620;
 const part=f<188?0:f<338?1:f<460?2:3;
 const labels=['BAŞLANGIÇ','HAZIRLIK','YIKAMA','SONUÇ'];
 if(f<60)return null;
 return <div style={{position:'absolute',top:95,left:62,right:62,display:'flex',alignItems:'center',gap:12,opacity:.93}}>
  <div style={{background:'#201d19',padding:'6px 12px',borderRadius:7,font:'bold 19px Arial',letterSpacing:1,color:'#fff'}}>{labels[part]}</div>
  <div style={{height:5,flex:1,background:'rgba(255,255,255,.55)',borderRadius:5,overflow:'hidden'}}><div style={{height:'100%',width:`${100*f/total}%`,background:'#ffe135'}}/></div>
 </div>;
}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111'}}>
  <Background/><Progress/><Hook/><InfoMotion/><Captions/>
  {(f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600)?<div style={{position:'absolute',bottom:210,width:'100%',textAlign:'center',font:'500 23px Arial',color:'rgba(255,255,255,.7)',textShadow:'0 2px 4px #000'}}>kadincayasam</div>:null}
  <Audio src={staticFile('VID-001-voice.wav')} volume={1}/>
  <Audio src={staticFile('peaceful_days.mp3')} volume={0.10}/>
  {[0,98,188,275,338,460,550].map((n,i)=><Sequence from={n} key={n}><Audio src={staticFile('whoosh.wav')} volume={i===0?.20:(i%2?.09:.14)}/></Sequence>)}
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID001Motion" component={Video} durationInFrames={620} fps={30} width={720} height={1280}/>}
registerRoot(Root);
