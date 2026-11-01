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
    const zoom=shot.scale+Math.min(Math.max(f-shot.from,0),120)*0.00015;
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
 const opacity=interpolate(f,[0,4,48,59],[0,1,1,0],clamp);
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
function SceneDetails(){
 const f=useCurrentFrame(); const {fps}=useVideoConfig();
 const items=[{from:205,to:260,label:'BİR YEMEK KAŞIĞI KARBONAT'}, {from:267,to:330,label:'BİR TABLET BULAŞIK DETERJANI'}, {from:351,to:401,label:'ALTMIŞ DERECEDE'}, {from:500,to:550,label:'KAYDET'}];
 const item=items.find(x=>f>=x.from&&f<x.to); if(!item)return null;
 const local=f-item.from, pop=spring({frame:local,fps,config:{damping:18,stiffness:220,mass:.7}});
 return <AbsoluteFill style={{pointerEvents:'none'}}><div style={{position:'absolute',left:55,top:900,transform:`translateY(${(1-pop)*20}px)`,background:'#fff6d1',border:'3px solid #27231b',borderRadius:14,padding:'10px 18px',boxShadow:'0 5px 0 #222',fontFamily:'Arial',fontWeight:900,fontSize:26,color:'#221e17'}}>{item.label}</div><svg width="720" height="1280" style={{position:'absolute',inset:0}}><path d="M 650 840 Q 620 805 575 790 M 575 790 L 592 789 M 575 790 L 581 806" fill="none" stroke="#ffe135" strokeWidth="5" strokeLinecap="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-Math.min(1,local/13)}/></svg></AbsoluteFill>
}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111'}}>
  <Background/><Hook/><SceneDetails/><Captions/>
  {(f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600)?<div style={{position:'absolute',bottom:210,width:'100%',textAlign:'center',font:'500 23px Arial',color:'rgba(255,255,255,.7)',textShadow:'0 2px 4px #000'}}>kadincayasam</div>:null}
  <Audio src={staticFile('VID-001-voice.wav')} volume={1}/>
  <Audio src={staticFile('peaceful_days.mp3')} volume={0.10}/>
  {[0,98,188,275,338,460,550].map((n,i)=><Sequence from={n} key={n}><Audio src={staticFile('whoosh.wav')} volume={i===0?.20:(i%2?.09:.14)}/></Sequence>)}
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID001" component={Video} durationInFrames={620} fps={30} width={720} height={1280}/>}
registerRoot(Root);
