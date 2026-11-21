 // world percussion (v232)
 [['Djembe bass',75,.35],['Djembe slap',0,.12],['Tabla na',0,.35],['Tabla ge',95,.6],['Cajon bass',70,.3],['Cajon slap',0,.1],['Taiko',55,.9],['Udu',180,.5],['Agogo high',0,.3],['Agogo low',0,.3],['Guiro',0,.35],['Cabasa',0,.15],['Steel drum',0,1]].forEach(([n,f,dec])=>add('World percussion',n,dec+.1,(c,o)=>{
  if(n==='Djembe slap'){ noise(c,o,'bandpass',2200,.7,dec,.001,1.5); tone(c,o,'sine',380,300,.4,dec*.6); }
  else if(n==='Tabla na'){ tone(c,o,'sine',1050,1040,.4,dec); tone(c,o,'sine',2100,2080,.15,dec*.6); }
  else if(n==='Cajon slap') noise(c,o,'bandpass',3000,.8,dec,.001,1);
  else if(n==='Agogo high'||n==='Agogo low'){ const b=n==='Agogo high'?930:620; tone(c,o,'square',b,b,.18,dec,.001,['bandpass',b*1.2,2]); tone(c,o,'sine',b*2.6,b*2.6,.08,dec*.7); }
  else if(n==='Guiro'){ for(let i=0;i<9;i++){ const s=c.createBufferSource(); s.buffer=noiseB(c); const fl=c.createBiquadFilter(), g=c.createGain(); fl.type='bandpass'; fl.frequency.value=3500; fl.Q.value=2; s.connect(fl); fl.connect(g); g.connect(o); env(c,g,i*.035,.001,.5,.025); s.start(i*.035); s.stop(i*.035+.06); } }
  else if(n==='Cabasa') noise(c,o,'highpass',5000,.5,dec,.01);
  else if(n==='Steel drum'){ const f0=523; [1,2,3.01].forEach((m,k)=>tone(c,o,'sine',f0*m,f0*m,[.4,.18,.08][k],dec,.004)); }
  else if(n==='Udu') tone(c,o,'sine',f*1.6,f,.8,dec,.01);
  else { tone(c,o,'sine',f*1.4,f,.9,dec); noise(c,o,'lowpass',900,.25,dec*.3); } }));
 // foley and textures (v232)
 [['Footsteps',1.4],['Door knock',1],['Heartbeat',1.6],['Clock tick',2],['Camera shutter',.4],['Coin',.8],['Rain',2.5],['Wind',3],['Thunder',3],['Bubbles',1.5],['Typewriter',1.2],['Applause',2.5]].forEach(([n,d])=>add('Foley and textures',n,d,(c,o)=>{
  const hit=(t,type,f,peak,dec,q)=>{ const s=c.createBufferSource(); s.buffer=noiseB(c); const fl=c.createBiquadFilter(), g=c.createGain(); fl.type=type; fl.frequency.value=f; if(q) fl.Q.value=q; s.connect(fl); fl.connect(g); g.connect(o); env(c,g,t,.002,peak,dec); s.start(t); s.stop(t+dec+.05); };
  const ping=(t,type,f1,f2,peak,dec)=>{ const x=c.createOscillator(), g=c.createGain(); x.type=type; x.frequency.setValueAtTime(f1,t); if(f2) x.frequency.exponentialRampToValueAtTime(Math.max(20,f2),t+dec*.8); x.connect(g); g.connect(o); env(c,g,t,.002,peak,dec); x.start(t); x.stop(t+dec+.05); };
  if(n==='Footsteps') [0,.35,.7,1.05].forEach(t=>{ hit(t,'lowpass',600,.7,.12); hit(t+.02,'bandpass',2500,.15,.06,1); });
  else if(n==='Door knock') [0,.18,.36].forEach(t=>{ ping(t,'sine',180,120,.8,.12); hit(t,'bandpass',900,.4,.05,2); });
  else if(n==='Heartbeat') [0,.22,.8,1.02].forEach((t,i)=>ping(t,'sine',i%2?55:65,40,i%2?.6:.9,.18));
  else if(n==='Clock tick') [0,.5,1,1.5].forEach((t,i)=>ping(t,'square',i%2?2600:3000,null,.12,.02));
  else if(n==='Camera shutter'){ hit(0,'highpass',3000,.6,.03); hit(.09,'bandpass',1800,.5,.05,2); }
  else if(n==='Coin'){ ping(0,'square',988,null,.15,.08); ping(.08,'square',1319,null,.15,.6); }
  else if(n==='Rain'){ hit(0,'highpass',4000,.25,d-.1); for(let i=0;i<40;i++) hit(Math.random()*(d-.2),'bandpass',2000+Math.random()*3000,.12,.02,3); }
  else if(n==='Wind'){ const fl=noise(c,o,'bandpass',500,.5,d-.2,.8,2); fl.frequency.setValueAtTime(400,0); fl.frequency.linearRampToValueAtTime(900,d*.5); fl.frequency.linearRampToValueAtTime(350,d-.1); }
  else if(n==='Thunder'){ hit(0,'lowpass',800,.9,.3); hit(.15,'lowpass',300,.8,d-.4); }
  else if(n==='Bubbles'){ for(let i=0;i<8;i++) ping(i*.17,'sine',400+Math.random()*300,900+Math.random()*500,.25,.08); }
  else if(n==='Typewriter'){ for(let i=0;i<8;i++){ const t=i*.13+(i%3)*.02; hit(t,'bandpass',3000,.6,.03,2); if(i===7) ping(t+.1,'sine',2000,null,.2,.4); } }
  else if(n==='Applause'){ for(let i=0;i<120;i++) hit(Math.random()*(d-.3),'bandpass',1500+Math.random()*1500,.08,.03,1.5); } }));
 // synth leads and keys (v232)
 [['Square lead'],['Saw lead'],['Supersaw stab'],['Sine bell'],['Retro arp'],['Hoover'],['Acid squelch'],['Chiptune blip'],['Pad swell'],['Pluck arp']].forEach(([n])=>add('Synth leads and keys',n,1.5,(c,o)=>{ const C=261.6;
  const v=(t,type,f,peak,dec,dt,a)=>{ const x=c.createOscillator(), g=c.createGain(); x.type=type; x.frequency.value=f; if(dt) x.detune.value=dt; x.connect(g); g.connect(o); env(c,g,t,a||.002,peak,dec); x.start(t); x.stop(t+(a||.002)+dec+.05); return x; };
  if(n==='Square lead') tone(c,o,'square',C*2,C*2,.25,1,.01,['lowpass',3000]);
  else if(n==='Saw lead') tone(c,o,'sawtooth',C*2,C*2,.25,1,.01,['lowpass',4000]);
  else if(n==='Supersaw stab') [-14,-7,0,7,14].forEach(dt=>v(0,'sawtooth',C,.08,.5,dt,.005));
  else if(n==='Sine bell'){ tone(c,o,'sine',C*4,null,.35,1.3); tone(c,o,'sine',C*4*2.76,null,.1,.6); }
  else if(n==='Retro arp') [0,4,7,12,7,4].forEach((s,i)=>v(i*.12,'square',C*Math.pow(2,s/12),.15,.1));
  else if(n==='Hoover') [-20,0,20].forEach(dt=>{ const x=v(0,'sawtooth',C*.75,.12,1.1,dt,.03); x.frequency.setValueAtTime(C*.75,0); x.frequency.exponentialRampToValueAtTime(C,.25); });
  else if(n==='Acid squelch'){ const lp=c.createBiquadFilter(); lp.type='lowpass'; lp.Q.value=14; lp.frequency.setValueAtTime(300,0); lp.frequency.exponentialRampToValueAtTime(3000,.12); lp.frequency.exponentialRampToValueAtTime(250,.5); lp.connect(o); tone(c,lp,'sawtooth',C/2,C/2,.4,.6,.005); }
  else if(n==='Chiptune blip') tone(c,o,'square',C*4,C*8,.18,.12);
  else if(n==='Pad swell') [0,4,7].forEach(s=>tone(c,o,'triangle',C*Math.pow(2,s/12),null,.12,1.2,.6));
  else if(n==='Pluck arp') [0,7,12,16].forEach((s,i)=>{ const t=i*.15, x=c.createOscillator(), g=c.createGain(), lp=c.createBiquadFilter(); lp.type='lowpass'; lp.frequency.setValueAtTime(5000,t); lp.frequency.exponentialRampToValueAtTime(600,t+.2); x.type='sawtooth'; x.frequency.value=C*Math.pow(2,s/12); x.connect(lp); lp.connect(g); g.connect(o); env(c,g,t,.002,.2,.25); x.start(t); x.stop(t+.35); }); }));
