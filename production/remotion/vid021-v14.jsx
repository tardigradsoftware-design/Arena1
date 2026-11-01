import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {BatchV14} from './BatchV14';
import captions from './vid021-captions.json';
import config from './vid021-config.json';
function Video(){return <BatchV14 config={config} captions={captions}/>}
function Root(){return <Composition id="VID021" component={Video} durationInFrames={config.frames} fps={30} width={720} height={1280}/>}
registerRoot(Root);
