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
// Caption timing is derived from Vosk/interpolation, not verified forced alignment.
function AnimatedLabel({from,to,children,top=260,left=45,right,accent='#ffe135',angle=-2}){
 const f=useCurrentFrame(),{fps}=useVideoConfig(); if(f<from||f>=to)return null;
 const local=f-from, p=spring({frame:local,fps,config:{damping:16,stiffness:240,mass:.62}});
 const opacity=interpolate(f,[from,from+3,to-6,to],[0,1,1,0],clamp);
 return <div style={{position:'absolute',top,left,right,opacity,transform:`translateY(${(1-p)*42}px) scale(${.78+.22*p}) rotate(${angle}deg)`,transformOrigin:right?'right center':'left center',display:'inline-block',background:accent,color:'#211d17',border:'4px solid #211d17',padding:'12px 20px',borderRadius:13,boxShadow:'6px 6px 0 #211d17, 0 12px 24px rgba(0,0,0,.28)',font:'900 34px Arial, sans-serif',whiteSpace:'nowrap'}}>{children}</div>;
}
function DrawnArc({from,to,kind='curve'}){
 const f=useCurrentFrame();if(f<from||f>=to)return null;
 const p=interpolate(f-from,[0,16],[0,1],clamp);
 const opacity=interpolate(f,[from,from+4,to-8,to],[0,1,1,0],clamp);
 const d=kind==='ring'?'M 185 430 A 205 205 0 1 1 183 432':'M 72 399 C 90 430 118 444 163 452 M 163 452 L 145 436 M 163 452 L 140 455';
 return <svg viewBox="0 0 720 1280" style={{position:'absolute',inset:0,width:'100%',height:'100%',opacity,filter:'drop-shadow(0 2px 2px #111)'}}><path d={d} fill="none" stroke="#ffe135" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-p}/></svg>;
}
function MotionGraphics(){
 const f=useCurrentFrame(),{fps}=useVideoConfig();
 const item = f>=220&&f<254 ? {from:220,to:254,type:'spoon',title:'KARBONAT',amount:'1 YEMEK KAŞIĞI'} : f>=256&&f<288 ? {from:256,to:288,type:'tablet',title:'BULAŞIK DETERJANI',amount:'1 TABLET'} : f>=296&&f<332 ? {from:296,to:332,type:'glass',title:'BEYAZ SİRKE',amount:'YARIM ÇAY BARDAĞI'} : null;
 const age=item?f-item.from:0;
 const pop=spring({frame:Math.max(age,0),fps,config:{damping:18,stiffness:230,mass:.6}});
 const alpha=item?interpolate(f,[item.from,item.from+3,item.to-4,item.to],[0,1,1,0],clamp):0;
 const float=Math.sin(age/16)*3;
 return <AbsoluteFill style={{pointerEvents:'none'}}>
   <AnimatedLabel from={75} to={158} top={220} accent="#fff9e9">SARARMIŞ KILIFLAR</AnimatedLabel>
   <DrawnArc from={87} to={164}/>
   {item&&<div style={{position:'absolute',top:205,left:55,right:55,height:194,opacity:alpha,transform:`translateY(${(1-pop)*-60}px)`,perspective:900}}>
    <div style={{position:'absolute',inset:'12px 0 0 18px',background:'rgba(19,18,16,.72)',border:'2px solid rgba(255,255,255,.35)',borderRadius:26,transform:'rotate(-1deg)',boxShadow:'0 12px 28px rgba(0,0,0,.3)'}}/>
    <div style={{position:'absolute',top:25,left:30,width:124,height:124,borderRadius:26,background:'#fff8e7',border:'4px solid #211d17',display:'grid',placeItems:'center',transform:`translateY(${float}px) rotate(${(1-pop)*-15}deg) scale(${.65+.35*pop})`,boxShadow:'5px 5px 0 #211d17'}}><Marker type={item.type}/></div>
    <div style={{position:'absolute',top:38,left:175,right:20,font:'900 23px Arial',color:'#fff',letterSpacing:1,opacity:Math.min(1,Math.max(0,(age-3)/5))}}>{item.amount}</div>
    <div style={{position:'absolute',top:78,left:175,right:14,font:'900 31px Arial',lineHeight:1.05,color:'#ffe135',transform:`translateX(${(1-pop)*45}px)`}}>{item.title}</div>
   </div>}
   <AnimatedLabel from={340} to={402} top={210} left={null} right={50} angle={3}>60° NORMAL PROGRAM</AnimatedLabel>
   <DrawnArc from={344} to={420} kind="ring"/>
   <AnimatedLabel from={465} to={513} top={210} accent="#fff9e9">BEYAZ YASTIK KILIFLARI</AnimatedLabel>
   {f>=468&&f<519&&[0,1,2].map(i=>{const t=f-468-i*5;const p=interpolate(t,[0,7,30,42],[0,1,1,0],clamp);return <svg key={i} viewBox="0 0 50 50" style={{position:'absolute',left:460+i*64,top:350+i%2*50,width:35,height:35,opacity:p,transform:`scale(${p})`}}><path d="M25 2 L29 20 L48 25 L29 29 L25 48 L21 29 L2 25 L21 20 Z" fill="#ffe135" stroke="#211d17" strokeWidth="2"/></svg>})}
   <AnimatedLabel from={544} to={585} top={245} left={null} right={70} accent="#ffe135" angle={2}>KAYDET</AnimatedLabel>
 </AbsoluteFill>;
}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111'}}>
  <Background/><Hook/><MotionGraphics/><Captions/>
  {(f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600)?<div style={{position:'absolute',bottom:210,width:'100%',textAlign:'center',font:'500 23px Arial',color:'rgba(255,255,255,.7)',textShadow:'0 2px 4px #000'}}>kadincayasam</div>:null}
  <Audio src={staticFile('VID-001-voice.wav')} volume={1}/>
  <Audio src={staticFile('peaceful_days.mp3')} volume={0.10}/>
  {[0,98,188,275,338,460,550].map((n,i)=><Sequence from={n} key={n}><Audio src={staticFile('whoosh.wav')} volume={i===0?.20:(i%2?.09:.14)}/></Sequence>)}
  <Sequence from={300}><Audio src={staticFile('drip.wav')} volume={.08}/></Sequence>
  {[221,255,297,468,536].map(n=><Sequence from={n} key={'fx'+n}><Audio src={staticFile('whoosh.wav')} volume={.045}/></Sequence>)}
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID001Hybrid" component={Video} durationInFrames={620} fps={30} width={720} height={1280}/>}
registerRoot(Root);
