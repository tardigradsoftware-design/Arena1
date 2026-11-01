import React from 'react';
import {AbsoluteFill, Audio, Composition, Img, Sequence, interpolate, registerRoot, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import captions from './captions.json';

const shots = [
  {from:0, file:'VID-035-1.png', focus:'50% 45%', scale:1.01},
  {from:98, file:'VID-035-1.png', focus:'50% 90%', scale:1.28},
  {from:235, file:'VID-035-2.png', focus:'50% 50%', scale:1.02},
  {from:333, file:'VID-035-3.png', focus:'50% 50%', scale:1.02},
  {from:424, file:'VID-035-4.png', focus:'50% 50%', scale:1.02},
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
 if(f>=89)return null;
 const entrance=spring({frame:f,fps,config:{damping:17,stiffness:230,mass:.7}});
 const opacity=interpolate(f,[0,4,74,88],[0,1,1,0],clamp);
 const scale=0.7+0.3*entrance;
 return <AbsoluteFill style={{opacity,pointerEvents:'none'}}>
    <div style={{position:'absolute',top:230,left:50,width:610,transform:`translateY(${(1-entrance)*-34}px) scale(${scale})`,transformOrigin:'center',fontFamily:'Arial, sans-serif',fontWeight:950,textAlign:'center',lineHeight:1.03,filter:'drop-shadow(0px 8px 6px rgba(0,0,0,.6))'}}>
     <div style={{display:'inline-block',fontSize:105,color:'#201510',background:'#ffe135',padding:'3px 32px 5px',transform:'rotate(-3deg)',borderRadius:8,letterSpacing:'-3px'}}>SAKIN!</div>
     <div style={{fontSize:42,color:'white',marginTop:14,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>SOĞAN DOĞRARKEN</div>
     <div style={{fontSize:46,color:'white',marginTop:3,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>GÖZYAŞLARINA<br/><span style={{color:'#ffe135'}}>BOĞULUP...</span></div>
    </div>
    <div style={{position:'absolute',left:75,top:240,width:31,height:10,background:'#fff',transform:`rotate(-25deg) scaleX(${entrance})`,borderRadius:8}}/>
    <div style={{position:'absolute',right:82,top:345,width:26,height:9,background:'#ffe135',transform:`rotate(30deg) scaleX(${entrance})`,borderRadius:8}}/>
 </AbsoluteFill>;
}
function Captions(){
 const f=useCurrentFrame(), t=f/30;
 const cap=captions.find(c=>t>=c.start && t<c.end);
 if(!cap)return null;
 return <div style={{position:'absolute',top:640,left:35,width:650,transform:'translateY(-50%)',textAlign:'center',fontFamily:'Arial, sans-serif',fontSize:45,fontWeight:900,letterSpacing:-.3,lineHeight:1.2,color:'white',textShadow:'0 2px 1px #000, 0 0 7px #000, 2px 2px 4px #000',WebkitTextStroke:'1px #111'}}>
  {cap.words.map((w,i)=><React.Fragment key={i}><span style={{color:i===cap.active?'#ffe230':'#fff'}}>{w}</span>{i<cap.words.length-1?' ':''}</React.Fragment>)}
 </div>;
}
function Sketch(){
 const f=useCurrentFrame(); const shot= f>=252&&f<322 ? 'glass': f>=349&&f<413?'knife':null;
 if(!shot)return null;
 const local=f-(shot==='glass'?252:349);const p=interpolate(local,[0,14],[0,1],clamp);const opacity=interpolate(local,[0,4,52,62],[0,1,1,0],clamp);
 const path=shot==='glass'?'M 385 610 C 415 628 449 660 489 722 M 470 713 L 489 722 L 490 703':'M 565 650 C 543 678 512 706 455 765 M 458 744 L 455 765 L 478 757';
 return <svg width="720" height="1280" viewBox="0 0 720 1280" style={{position:'absolute',inset:0,opacity,filter:'drop-shadow(0px 2px 2px #111)'}}><path d={path} fill="none" stroke="white" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-p}/></svg>;
}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111'}}>
  <Background/><Hook/><Sketch/><Captions/>
  {(f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600)?<div style={{position:'absolute',bottom:210,width:'100%',textAlign:'center',font:'500 23px Arial',color:'rgba(255,255,255,.7)',textShadow:'0 2px 4px #000'}}>kadincayasam</div>:null}
  <Audio src={staticFile('voice.wav')} volume={1}/>
  <Audio src={staticFile('peaceful_days.mp3')} volume={0.10}/>
  {[0,98,235,333,424].map((n,i)=><Sequence from={n} key={n}><Audio src={staticFile('whoosh.wav')} volume={i===0?.20:.16}/></Sequence>)}
  <Sequence from={350}><Audio src={staticFile('drip.wav')} volume={.12}/></Sequence>
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID035" component={Video} durationInFrames={629} fps={30} width={720} height={1280}/>}
registerRoot(Root);
