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
// High-impact test hook: no changes to the recorded scenario.
function Hook(){
 const f=useCurrentFrame(); const {fps}=useVideoConfig(); if(f>=66)return null;
 const p=spring({frame:f,fps,config:{damping:20,stiffness:190,mass:.7}});
 const opacity=interpolate(f,[0,2,55,66],[1,1,1,0],clamp);
 const sweep=interpolate(f,[0,32],[-450,950],clamp);
 return <AbsoluteFill style={{opacity,pointerEvents:'none',overflow:'hidden'}}>
  <div style={{position:'absolute',inset:0,background:'linear-gradient(180deg,rgba(28,12,12,.70),rgba(20,12,8,.06) 54%,rgba(0,0,0,.12))'}}/>
  <div style={{position:'absolute',top:0,bottom:0,left:sweep,width:110,transform:'skewX(-18deg)',background:'linear-gradient(90deg,transparent,rgba(255,239,161,.17),transparent)'}}/>
  <svg viewBox="0 0 720 1280" width="720" height="1280" style={{position:'absolute',inset:0,filter:'drop-shadow(0 3px 4px #000)'}}>
   <path d="M46 390 L46 159 L138 159 M674 390 L674 159 L582 159" fill="none" stroke="#ffe135" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" opacity=".9"/>
   <path d="M485 515 C530 535 550 570 560 610 M560 610 L545 594 M560 610 L573 592" fill="none" stroke="#ffe135" strokeWidth="7" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-interpolate(f,[8,25],[0,1],clamp)}/>
  </svg>
  <div style={{position:'absolute',top:170,left:64,right:64,textAlign:'center',fontFamily:'Arial,sans-serif',fontWeight:950,filter:'drop-shadow(0 8px 6px rgba(0,0,0,.8))',transform:`translateY(${(1-p)*-22}px)`}}>
   <div style={{fontSize:43,letterSpacing:1,color:'#fff',lineHeight:1.1,textShadow:'0 3px 2px #000'}}>SARARMIŞ<br/>YASTIK KILIFLARI</div>
   <div style={{display:'inline-block',marginTop:14,background:'#ffe135',color:'#17120d',fontSize:83,lineHeight:1,fontWeight:950,borderRadius:9,padding:'8px 22px',transform:'rotate(-2deg)',boxShadow:'6px 7px 0 #17120d'}}>SAKIN ATMA!</div>
  </div>
  {[0,1,2].map(i=><div key={i} style={{position:'absolute',top:460+i*20,left:45+i*14,width:8,height:8,borderRadius:'50%',background:i===1?'white':'#ffe135',opacity:interpolate(f,[i*3,i*3+8],[0,1],clamp)}}/>)}
 </AbsoluteFill>;
}
const C={ink:'#111111',paper:'#F8F9FA',dot:'#E2E5E9',red:'#E63946',green:'#10B981',yellow:'#F59E0B',blue:'#2563EB'};

// Word-linked timing is approximate (Vosk + interpolation), not verified alignment.
function Marker({type}) {
 if(type==='spoon') return <svg viewBox="0 0 100 100" width="72" height="72"><ellipse cx="36" cy="35" rx="19" ry="14" fill="#f3efe7" stroke="#25211b" strokeWidth="4"/><path d="M49 43 L81 78" stroke="#eee9df" strokeWidth="10" strokeLinecap="round"/><path d="M49 43 L81 78" stroke="#25211b" strokeWidth="3" strokeLinecap="round"/></svg>;
 if(type==='tablet') return <svg viewBox="0 0 100 100" width="72" height="72"><rect x="19" y="25" width="62" height="52" rx="13" fill="#eee8db" stroke="#25211b" strokeWidth="4"/><rect x="24" y="31" width="52" height="16" rx="5" fill="#5badb6"/><circle cx="50" cy="55" r="10" fill="#8bb9cb" stroke="#25211b" strokeWidth="3"/></svg>;
 if(type==='glass') return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M28 20 Q49 26 72 20 L66 42 Q62 54 70 75 Q50 81 30 75 Q38 54 34 42 Z" fill="#d9eef1" fillOpacity=".9" stroke="#25211b" strokeWidth="4"/><path d="M35 53 Q50 57 65 53 L70 75 Q50 81 30 75Z" fill="#b7d7d4" fillOpacity=".65"/></svg>;
 return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M26 14 H74 V86 L50 70 L26 86 Z" fill="#ffe135" stroke="#25211b" strokeWidth="5" strokeLinejoin="round"/></svg>;
}
// Timings derive from approximate word timestamps and still need listening review.
function MotionGraphics(){
 const f=useCurrentFrame(),{fps}=useVideoConfig();
 const events=[
  {from:75,to:175,label:'SARARMIŞ', sub:'YASTIK KILIFLARI', kind:'fabric', side:'left'},
  {from:221,to:254,label:'1 YEMEK KAŞIĞI', sub:'KARBONAT',kind:'spoon',side:'left'},
  {from:255,to:286,label:'1 TABLET', sub:'BULAŞIK DETERJANI',kind:'tablet',side:'right'},
  {from:297,to:331,label:'YARIM ÇAY BARDAĞI', sub:'BEYAZ SİRKE',kind:'glass',side:'left'},
  {from:338,to:390,label:'60°',sub:'NORMAL PROGRAM',kind:'temp',side:'right'},
  {from:468,to:515,label:'BEYAZ',sub:'YASTIK KILIFLARI',kind:'fabric',side:'left'},
  {from:536,to:578,label:'KAYDET',sub:'LAZIM OLDUĞUNDA',kind:'save',side:'right'},
 ];
 const item=events.find(e=>f>=e.from&&f<e.to); if(!item)return null;
 const age=f-item.from;const p=spring({frame:age,fps,config:{damping:16,stiffness:230,mass:.65}});
 const fade=interpolate(f,[item.from,item.from+3,item.to-5,item.to],[0,1,1,0],clamp);
 const dir=item.side==='left'?-1:1; const rotation=dir*interpolate(p,[0,1],[7,2]);
 const line=interpolate(age,[3,14],[0,1],clamp); const scale=.75+.25*p;
 return <AbsoluteFill style={{opacity:fade,pointerEvents:'none'}}>
  <div style={{position:'absolute',left:item.side==='left'?46:undefined,right:item.side==='right'?46:undefined,top:225,display:'flex',gap:12,alignItems:'center',transform:`translateX(${dir*(1-p)*260}px) rotate(${rotation}deg) scale(${scale})`,transformOrigin:item.side==='left'?'left center':'right center',filter:'drop-shadow(0px 8px 9px rgba(0,0,0,.4))'}}>
   <div style={{width:94,height:94,flexShrink:0,display:'grid',placeItems:'center',background:'#fff9ea',border:'4px solid #211d19',borderRadius:22,boxShadow:'5px 5px 0 #211d19'}}>
    {item.kind==='temp'?<div style={{font:'900 39px Arial',color:'#211d19'}}>60°</div>:item.kind==='fabric'?<svg viewBox="0 0 100 100" width="68" height="68"><path d="M16 30 Q49 18 84 30 L80 72 Q50 79 20 72 Z" fill="#f9f5e9" stroke="#211d19" strokeWidth="5"/><path d="M25 38 Q50 32 75 38 M26 62 Q50 67 74 62" fill="none" stroke="#c8bdaa" strokeWidth="3"/></svg>:<Marker type={item.kind}/>}
   </div>
   <div style={{fontFamily:'Arial, sans-serif',fontWeight:900,color:'#211d19',lineHeight:1.05}}>
    <div style={{display:'table',background:'#ffe135',border:'3px solid #211d19',borderRadius:9,padding:'7px 12px',fontSize:item.kind==='temp'?36:25,boxShadow:'4px 4px 0 #211d19'}}>{item.label}</div>
    <div style={{display:'table',marginTop:7,background:'#fff9ea',border:'3px solid #211d19',borderRadius:9,padding:'7px 12px',fontSize:23,boxShadow:'4px 4px 0 #211d19'}}>{item.sub}</div>
   </div>
  </div>
  <svg viewBox="0 0 720 1280" style={{position:'absolute',inset:0,width:'100%',height:'100%',filter:'drop-shadow(0 2px 2px #111)'}}><path d={item.side==='left'?'M 110 370 C 115 403 145 418 185 430 M 185 430 L 169 412 M 185 430 L 163 434':'M 610 370 C 605 403 575 418 535 430 M 535 430 L 551 412 M 535 430 L 557 434'} fill="none" stroke="#ffe135" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-line}/></svg>
  {[0,1,2].map(i=><div key={i} style={{position:'absolute',top:380+i*20,left:item.side==='left'?55+i*13:undefined,right:item.side==='right'?55+i*13:undefined,width:8+i*2,height:8+i*2,borderRadius:'50%',background:i===1?'#fff':'#ffe135',transform:`scale(${Math.max(0,Math.min(1,(age-i*3)/8))})`}}/>)}
 </AbsoluteFill>;
}
// Hand-drawn focus marks in gaps only; no duplicated icon cards.
function FocusMarks(){
 const f=useCurrentFrame();
 const segments=[
  {from:198,to:220,path:'M 97 380 C 150 383 187 420 215 475 M 215 475 L 191 461 M 215 475 L 213 447'},
  {from:400,to:454,path:'M 180 550 C 174 448 241 373 345 365 C 448 358 526 420 535 505'},
  {from:581,to:615,path:'M 570 480 C 557 420 535 380 484 348 M 484 348 L 508 350 M 484 348 L 497 370'}
 ];
 const item=segments.find(e=>f>=e.from&&f<e.to); if(!item)return null;
 const progress=interpolate(f,[item.from,item.from+18],[0,1],clamp);
 const opacity=interpolate(f,[item.from,item.from+4,item.to-8,item.to],[0,1,1,0],clamp);
 return <AbsoluteFill style={{opacity,pointerEvents:'none'}}><svg viewBox="0 0 720 1280" width="720" height="1280" style={{filter:'drop-shadow(0 2px 2px #111)'}}><path d={item.path} fill="none" stroke="#ffe135" strokeWidth="7" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-progress}/></svg></AbsoluteFill>;
}
// Result accent stays on the folded linens, not over the caption or product claims.
function ResultAccent(){
 const f=useCurrentFrame(); if(f<470||f>=526)return null;
 const fade=interpolate(f,[470,475,515,526],[0,1,1,0],clamp);
 const draw=interpolate(f,[470,492],[0,1],clamp);
 return <AbsoluteFill style={{opacity:fade,pointerEvents:'none'}}>
  <svg width="720" height="1280" viewBox="0 0 720 1280" style={{filter:'drop-shadow(0 2px 2px rgba(0,0,0,.65))'}}>
   <path d="M 490 328 C 540 320 580 333 610 360" fill="none" stroke="#ffe135" strokeWidth="5" strokeLinecap="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-draw}/>
   {[[578,280,17],[635,334,11],[485,384,10]].map(([x,y,r],i)=>{const p=interpolate(f,[474+i*4,482+i*4],[0,1],clamp);return <g key={i} transform={`translate(${x} ${y}) scale(${p})`}><path d={`M 0 ${-r} Q 2 -2 ${r} 0 Q 2 2 0 ${r} Q -2 2 ${-r} 0 Q -2 -2 0 ${-r}`} fill={i===0?'#ffe135':'#fff'} stroke="#231f19" strokeWidth="2"/></g>})}
  </svg>
 </AbsoluteFill>;
}
function Caption(){const f=useCurrentFrame(),t=f/30;const cap=captions.find(c=>t>=c.start&&t<c.end);if(!cap||f<60)return null;const k=interpolate(f/30,[cap.start,cap.start+.08,cap.end],[.94,1.05,1],clamp);return <div style={{position:'absolute',top:795,left:42,right:42,display:'flex',justifyContent:'center',alignItems:'center',gap:9,font:'900 37px Arial',textAlign:'center'}}>{cap.words.map((w,i)=><span key={i} style={{background:i===cap.active?'#ffe135':'white',color:C.ink,border:'3px solid #111',boxShadow:'3px 3px 0 #111',borderRadius:8,padding:'7px 10px',transform:i===cap.active?`scale(${k}) rotate(-2deg)`:'none'}}>{w}</span>)}</div>}
// Quiet design accents, kept outside the lower-caption safe zone.
function LiveAccents(){
 const f=useCurrentFrame(); if(f<66 || f>=620)return null;
 const glow=.13+.055*Math.sin(f/18);
 return <AbsoluteFill style={{pointerEvents:'none'}}>
  <div style={{position:'absolute',inset:0,boxShadow:`inset 0 0 110px rgba(255,198,90,${glow})`}}/>
  <svg width="720" height="1280" viewBox="0 0 720 1280" style={{position:'absolute',inset:0}}>
   <path d="M38 100 L38 60 L80 60 M682 100 L682 60 L640 60" stroke="#fff3ca" opacity=".65" strokeWidth="3" fill="none" strokeLinecap="round"/>
  </svg>
 </AbsoluteFill>;
}
function CallToAction(){
 const f=useCurrentFrame(),{fps}=useVideoConfig(); if(f<620)return null;
 const age=f-620; const p=spring({frame:age,fps,config:{damping:18,stiffness:170}});
 const controls=[['♡','BEĞEN'],['+','TAKİP ET'],['↗','PAYLAŞ']];
 return <AbsoluteFill style={{pointerEvents:'none',background:'linear-gradient(180deg,rgba(26,17,16,.55),rgba(26,17,16,.18) 48%,rgba(26,17,16,.65))'}}>
  <div style={{position:'absolute',top:240,left:50,right:50,textAlign:'center',color:'#fff',font:'900 39px Arial',textShadow:'0 4px 8px #000',transform:`translateY(${(1-p)*18}px)`,opacity:Math.min(1,p)}}>DAHA FAZLA PRATİK FİKİR İÇİN</div>
  <div style={{position:'absolute',top:360,left:52,right:52,display:'flex',gap:12,justifyContent:'center'}}>{controls.map(([icon,label],i)=>{const a=spring({frame:Math.max(0,age-i*6),fps,config:{damping:18,stiffness:190}});return <div key={label} style={{width:194,background:i===1?'#ffe135':'#fff',border:'3px solid #16130f',borderRadius:19,boxShadow:'5px 6px 0 #16130f',padding:'14px 5px',textAlign:'center',color:'#16130f',transform:`translateY(${(1-a)*35}px)`,opacity:Math.min(1,a)}}><div style={{font:'900 48px Arial',lineHeight:1}}>{icon}</div><div style={{font:'900 22px Arial',marginTop:8}}>{label}</div></div>})}</div>
  <div style={{position:'absolute',top:566,left:70,right:70,textAlign:'center',color:'#fff',font:'bold 30px Arial',textShadow:'0 3px 7px #000'}}>@kadincayasamax</div>
 </AbsoluteFill>;
}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111',overflow:'hidden'}}>
  <Background/><LiveAccents/><Hook/><MotionGraphics/><FocusMarks/><ResultAccent/><Caption/><CallToAction/>
  {((f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600))&&<div style={{position:'absolute',bottom:210,left:50,font:'bold 22px Arial',color:'white',textShadow:'0 2px 4px #000'}}>kadincayasamax</div>}
  <Audio src={staticFile('VID-001-voice.wav')} volume={1}/><Audio src={staticFile('peaceful_days.mp3')} volume={.10}/>
  {/* Hook, information graphics, outcome and save each have their own cue.
      Scene changes deliberately have no transition effect. */}
  <Sequence from={0}><Audio src={staticFile('sfx-hook-merak.wav')} volume={.48}/></Sequence>
  {[75,198,221,255,297,346,400,581].map(n=><Sequence from={n} key={'info'+n}><Audio src={staticFile('sfx-isin.wav')} volume={.38}/></Sequence>)}
  <Sequence from={470}><Audio src={staticFile('sfx-result-chime.wav')} volume={.36}/></Sequence>
  <Sequence from={536}><Audio src={staticFile('sfx-kaydet.wav')} volume={.48}/></Sequence>
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID001CanliTest" component={Video} durationInFrames={710} fps={30} width={720} height={1280}/>}
registerRoot(Root);
