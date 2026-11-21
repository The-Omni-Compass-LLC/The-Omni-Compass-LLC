(()=>{ /* 🔁 THE LOOP LIBRARY (v232): 48 genres × 200 loops = 9,600 loops, each one written straight into the Studio's own sequencer:
   drums on the 16 drum pads, the bass line on the bass pads, the chords on the chord pads and a lead on the lead pads, in your key
   and mode. Every loop is made the same way every time from its genre and its number (a seeded generator), so loop 37 of Trap is
   always loop 37 of Trap. Play it as a full loop, drums only, drums and bass, percussion only, or as an instrumental with no drums.
   Then tweak it: half time, double time, shift, reverse, thin out, add ghost notes, add a fill, mutate, reroll the drums, the bass or
   the chords, change the swing and the length, mute any layer. ↶ Undo puts back whatever was in the sequencer before. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } }; const P=()=>window.PADSTUDIO;
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 /* pads: 0 kick, 1 kick 2, 2 snare, 3 clap, 4 closed hat, 5 open hat, 6 rim, 7-9 toms, 10 crash, 11 ride, 12 shaker, 13 cowbell, 14 snap, 15 808;
    16-31 bass notes, 32-38 chords I to vii, 39 I up, 40-47 lead notes */
 const PADK={k:0,k2:1,s:2,cl:3,h:4,o:5,r:6,tl:7,tm:8,th:9,cr:10,rd:11,sh:12,cb:13,sn:14,b8:15};
 const PERC=new Set([6,7,8,9,12,13,14]);
 const F4='x...x...x...x...', BB='....x.......x...', H8='x.x.x.x.x.x.x.x.', H16='xxxxxxxxxxxxxxxx', OFF='..x...x...x...x.';
 /* [name, bpm low, bpm high, swing 0-4, kit, [drum patterns], [bass styles], [chord styles], lead chance] */
 const G=[
  ['Boom bap',84,96,2,10,[{k:'x.....x...x.....',s:BB,h:H8},{k:'x..x......x..x..',s:BB,h:H8,o:'..............x.'}],['root','sync'],['stab','whole'],.3],
  ['Trap',130,150,0,1,[{k:'x......x..x.....',cl:'........x.......',h:H16,b8:'x......x..x.....'},{k:'x.....x.x......x',cl:'........x.......',h:'x.x.x.x.x.x.xxxx',b8:'x.....x.x......x'}],['808'],['whole','half'],.5],
  ['Drill',138,146,0,11,[{k:'x.....x...x.....',s:'......x.......x.',h:'x..x..x.x..x..x.',b8:'x.....x...x....x'},{k:'x......x..x.....',s:'....x.....x..x..',h:'x.x..x.xx.x..x.x',b8:'x......x..x..x..'}],['808'],['whole'],.4],
  ['Lo-fi',70,86,3,4,[{k:'x.....x...x.....',s:BB,h:'x...x.x.x...x.x.'},{k:'x..x....x.......',s:BB,h:H8,sh:'..x...x...x...x.'}],['root','walk'],['whole','half'],.5],
  ['House',120,126,1,12,[{k:F4,cl:BB,o:OFF,h:H16},{k:F4,cl:BB,o:OFF,sh:H8}],['offbeat','octave'],['house','stab'],.4],
  ['Deep house',118,124,1,12,[{k:F4,r:'....x.......x..x',o:OFF,sh:H16},{k:F4,cl:BB,o:OFF,h:H8}],['offbeat','sync'],['whole','house'],.4],
  ['Techno',126,136,0,3,[{k:F4,cl:BB,h:H8,o:OFF},{k:F4,h:H16,rd:OFF,r:'.......x.......x'}],['offbeat','roots8'],['stab','none'],.3],
  ['Tech house',124,128,1,12,[{k:F4,cl:BB,h:H16,o:OFF,sh:'x.xxx.xxx.xxx.xx'},{k:F4,cl:BB,o:OFF,cb:'...x......x.....'}],['sync','offbeat'],['stab','none'],.3],
  ['Trance',136,142,0,3,[{k:F4,cl:BB,o:OFF,h:H16},{k:F4,o:OFF,cr:'x...............'}],['offbeat','roots8'],['pump','whole'],.6],
  ['Drum and bass',170,176,0,15,[{k:'x.........x.....',s:BB,h:H8},{k:'x.x.......x.....',s:'....x..x.x..x..x',h:H8}],['roots8','sync'],['whole','stab'],.4],
  ['Jungle',160,170,0,15,[{k:'x.x.......xx....',s:'....x..x.x..x..x',h:H16},{k:'x.........x..x..',s:'....x.x..x..x.x.',rd:H8}],['root','sync'],['whole'],.3],
  ['Dubstep',138,142,0,3,[{k:'x.........x.....',s:'........x.......',h:H8},{k:'x......x.x......',s:'........x.......',h:'x.x.x.x.x.xxx.x.'}],['808','root'],['whole','none'],.3],
  ['UK garage',130,136,3,12,[{k:'x.....x..x......',s:BB,h:'..x...x...x..xx.'},{k:'x..x....x.......',s:BB,h:H8,sh:H16}],['sync','offbeat'],['stab','house'],.4],
  ['Afrobeats',100,112,1,13,[{k:'x...x..x..x.....',r:'...x..x....x..x.',sh:'x.xxx.xxx.xxx.xx'},{k:'x..x..x...x.....',r:'...x..x....x..x.',h:H8,cb:'x.....x.....x...'}],['sync','root'],['stab','skank'],.5],
  ['Amapiano',110,115,1,13,[{k:F4,r:'....x.......x...',sh:H16,b8:'...x..x....x.x..'},{k:F4,cl:BB,sh:H16,b8:'..x...x..x...x..'}],['808','sync'],['whole','stab'],.5],
  ['Dancehall',96,104,0,6,[{k:'x..x..x...x..x..',s:'...x..x....x..x.',h:H8},{k:F4,r:'...x..x....x..x.',h:H8}],['sync','root'],['skank','stab'],.4],
  ['Reggaeton',88,98,0,5,[{k:F4,s:'...x..x....x..x.',h:H8},{k:F4,r:'...x..x....x..x.',sh:H16}],['root','808'],['stab','whole'],.4],
  ['Reggae',70,82,2,6,[{k:'........x.......',r:'........x.......',h:H8},{k:'x.......x.......',r:'........x.......',h:H8}],['root','sync'],['skank'],.3],
  ['Dembow',112,124,0,5,[{k:F4,s:'...x..x....x..x.',h:H16},{k:'x..x..x.x..x..x.',s:'...x..x....x..x.',h:H8}],['808'],['stab'],.3],
  ['Funk',96,112,1,2,[{k:'x.x...x...x..x..',s:'....x..x.x..x...',h:H16},{k:'x..x..x...x.x...',s:'....x....x..x..x',h:H16,o:'.......x........'}],['sync','octave'],['stab','pump'],.4],
  ['Disco',116,124,1,3,[{k:F4,s:BB,o:OFF,h:H16},{k:F4,cl:BB,o:OFF,sh:H16}],['octave'],['pump','stab'],.5],
  ['Soul',88,104,2,10,[{k:'x.....x...x.....',s:BB,h:H8},{k:'x..x......x.....',s:BB,h:H8,sh:BB}],['root','walk'],['whole','half'],.4],
  ['R&B',80,100,2,0,[{k:'x......x.x......',s:BB,h:'x.xxx.x.x.xxx.x.'},{k:'x.....x...x..x..',sn:BB,h:H8}],['sync','root'],['whole','half'],.5],
  ['Pop',100,124,0,3,[{k:'x.......x.......',s:BB,h:H8},{k:F4,cl:BB,h:H8}],['roots8','root'],['pump','whole'],.6],
  ['Rock',110,140,0,2,[{k:'x.......x.x.....',s:BB,h:H8},{k:'x...x...x.x.x...',s:BB,h:H8,cr:'x...............'}],['roots8'],['pump','whole'],.4],
  ['Punk',160,190,0,2,[{k:H8,s:BB,h:H8},{k:'x.x.x.x.x.x.x.x.',s:'..x...x...x...x.',h:H8}],['roots8'],['pump'],.2],
  ['Metal',100,140,0,2,[{k:H16,s:BB,rd:H8},{k:'xxx.xxx.xxx.xxx.',s:BB,cr:'x.......x.......'}],['roots8'],['pump','stab'],.2],
  ['Jazz swing',110,180,4,14,[{rd:'x...x.x.x...x.x.',h:BB,k:'x.......x.......'},{rd:'x...x.x.x...x.x.',h:BB,s:'.......x.......x'}],['walk'],['half','stab'],.5],
  ['Bossa nova',120,140,0,14,[{k:'x..x....x..x....',r:'..x..x...x..x...',h:H8},{k:'x..x....x..x....',r:'x..x..x...x..x..',sh:H16}],['root','walk'],['stab','half'],.5],
  ['Samba',96,104,0,5,[{k:'x..xx..xx..xx..x',sh:H16,r:'..x..x.x..x..x.x'},{k:'x...x...x...x...',sh:H16,tm:'..x...x...x...x.',cb:'x.x..x.x..x.x..x'}],['root','sync'],['stab'],.4],
  ['Salsa',180,200,0,5,[{cb:'x.x.x.xxx.x.x.xx',r:'x..x..x.....x.x.',tl:'......xx......xx'},{cb:'x.x.x.x.x.x.x.x.',r:'..x.x...x..x..x.',tm:'...x..x....x..x.'}],['sync'],['stab'],.4],
  ['Cumbia',90,100,0,5,[{k:'x.......x.......',sh:'x.xxx.xxx.xxx.xx',s:BB},{k:'x.......x.......',sh:H16,r:'..x...x...x...x.'}],['root','sync'],['skank','stab'],.4],
  ['Latin trap',130,150,0,1,[{k:'x......x..x.....',s:'...x..x....x..x.',h:H16,b8:'x......x..x.....'},{k:F4,cl:'........x.......',h:'x.x.x.x.x.x.xxxx',b8:'x...x...x...x...'}],['808'],['whole'],.4],
  ['Synthwave',96,118,0,3,[{k:'x.......x.......',s:BB,h:H8},{k:F4,s:BB,h:H16}],['roots8','octave'],['whole','pump'],.6],
  ['Breakbeat',126,136,1,0,[{k:'x.........x..x..',s:BB,h:H8},{k:'x.x.......x.....',s:'....x..x....x...',h:H8}],['sync','root'],['stab','none'],.3],
  ['Trip hop',76,92,3,4,[{k:'x.....x...x.....',s:'....x.......x...',h:'x...x...x...x...'},{k:'x..x......x.....',s:BB,rd:H8}],['root','sync'],['whole'],.4],
  ['Phonk',130,145,0,1,[{k:'x......x..x.....',cl:'........x.......',cb:'x..x..x...x..x..',h:H8},{k:'x.....x.x.......',cl:'........x.......',cb:'x.x..x.x..x.x..x',b8:'x.....x.x.......'}],['808'],['none','whole'],.5],
  ['Jersey club',138,145,0,1,[{k:'x..x..x.x..x..x.',cl:BB,h:H8},{k:'x.x..x.x..x.x...',cl:'....x.......x...',sn:'..x.......x.....'}],['808','sync'],['stab'],.3],
  ['Baile funk',126,132,0,5,[{k:'x..x..x...x..x..',s:'...x..x...x..x.x',h:H8},{k:'x..x..x...x..x..',cl:'...x..x...x..x..',cb:'x.....x.....x...'}],['808'],['stab','none'],.3],
  ['Footwork',156,162,0,1,[{k:'x..x..x..x..x..x',cl:'........x.......',h:H16},{k:'x..x..x...x..x..',s:'....x.......x..x',h:'x.x.x.xxx.x.x.xx'}],['808'],['stab','none'],.3],
  ['Electro',124,132,0,3,[{k:'x......x..x.....',cl:BB,h:H8},{k:'x.....x.x.......',cl:BB,h:H16,cb:'...x.......x....'}],['sync','roots8'],['stab'],.4],
  ['Hyperpop',150,170,0,8,[{k:'x......x..x.....',cl:'....x.......x...',h:H16},{k:'x.x...x.x.x.....',cl:BB,h:'xxxx.x.xxxxx.x.x'}],['808','octave'],['pump','stab'],.6],
  ['Country',100,120,0,14,[{k:F4,r:'..x...x...x...x.',h:H16},{k:'x.......x.......',s:BB,h:H8}],['root','walk'],['whole','pump'],.4],
  ['Gospel',70,90,3,0,[{k:'x..x..x.x.......',s:BB,h:H8},{k:'x.....x...x.....',s:'....x..x....x...',h:H8}],['walk','root'],['whole','half'],.5],
  ['Motown',104,120,1,2,[{k:'x.x.x.x.x.x.x.x.',s:BB,sh:BB,h:H8},{k:'x...x...x...x...',s:BB,sh:'....x.......x...'}],['walk','roots8'],['pump','stab'],.4],
  ['Gqom',122,128,0,13,[{k:'x..x..x...x.....',r:'....x..x....x...',sh:H16},{k:'x...x..x..x.....',tl:'..x.....x..x....',sh:H8}],['808'],['none','stab'],.2],
  ['Ambient',60,80,0,9,[{sh:'x.......x.......',rd:'....x.......x...'},{tl:'x...............',sh:'..x.......x.....'}],['root'],['whole'],.7],
  ['Chiptune',140,160,0,8,[{k:'x.......x.......',s:BB,h:H8},{k:'x...x...x.x.x...',s:BB,h:H16}],['octave','roots8'],['pump','stab'],.8]];
 const PROGS=[[0,4,5,3],[5,3,0,4],[0,5,3,4],[1,4,0,0],[0,3,4,3],[5,4,3,4],[0,3,5,4],[0,6,5,4],[3,4,0,5],[5,3,4,0],[0,2,3,4],[0,4,3,3]];
 const RN=['I','ii','iii','IV','V','vi','vii°'];
 const TYPES=[['full','Full loop: drums, bass, chords, lead'],['drums','Drums only'],['db','Drums and bass'],['perc','Percussion only'],['inst','Instrumental: no drums']];
 const SW=['0','.08','.16','.24','.33'];
 const PER=200;
 const rngOf=seed=>{ let a=seed>>>0; return ()=>{ a|=0; a=a+0x6D2B79F5|0; let t=Math.imul(a^a>>>15,1|a); t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }; };
 const pick=(r,a)=>a[Math.floor(r()*a.length)];
 /* one loop: {name, bpm, swing, kit, bars, lanes:{pad:[16*bars steps]}} */
 function make(gi,v){ const g=G[gi], r=rngOf(gi*100003+v*7919+17); const base=g[5][v%g[5].length]; const dens=pick(r,['sparse','normal','normal','busy']); const bars=pick(r,[2,2,2,4,1]);
  const prog=PROGS[Math.floor(r()*PROGS.length)], bassSt=pick(r,g[6]), chordSt=pick(r,g[7]), lead=r()<g[8];
  const L={}; const lane=p=>L[p]||(L[p]=new Array(bars*16).fill(0));
  for(let b=0;b<bars;b++){ for(const [key,pat] of Object.entries(base)){ const p=PADK[key]; for(let i=0;i<16;i++){ if(pat[i]!=='x') continue; let on=1; if(dens==='sparse'&&(p===4||p===12||p===11)&&i%4!==0&&r()<.35) on=0; lane(p)[b*16+i]=on; } }
   if(dens==='busy'){ for(let i=0;i<16;i++){ if(!lane(2)[b*16+i]&&!lane(3)[b*16+i]&&i%2===1&&r()<.12) lane(base.s?2:3)[b*16+i]=1; if(i%4===2&&r()<.08) lane(0)[b*16+i]=1; } }
   if(g[0]==='Trap'||g[0]==='Latin trap'||g[0]==='Phonk'||g[0]==='Drill'){ if(r()<.5){ const s0=8+Math.floor(r()*6); for(let i=s0;i<Math.min(16,s0+3);i++) lane(4)[b*16+i]=1; } }
   if(b===bars-1&&bars>1&&r()<.45){ [12,13,14,15].forEach((i,k)=>{ lane([9,8,7,7][k])[b*16+i]=1; }); }
   if(b>0&&r()<.3){ const i=6+2*Math.floor(r()*4); if(lane(0)) lane(0)[b*16+i]=1; } }
  const span=bars*16/prog.length;
  prog.forEach((d,ci)=>{ const st=Math.round(ci*span), en=Math.round((ci+1)*span);
   const cp=32+d, bp=16+d;
   if(chordSt==='whole') lane(cp)[st]=1;
   else if(chordSt==='half'){ lane(cp)[st]=1; if(st+Math.round(span/2)<en) lane(cp)[st+Math.round(span/2)]=1; }
   else if(chordSt==='stab'){ [0,3,6,10].forEach(o=>{ if(st+o<en&&r()<.75) lane(cp)[st+o]=1; }); lane(cp)[st]=1; }
   else if(chordSt==='skank'||chordSt==='house'){ for(let i=st;i<en;i++) if(i%4===2) lane(cp)[i]=1; }
   else if(chordSt==='pump'){ for(let i=st;i<en;i+=2) lane(cp)[i]=1; }
   if(bassSt==='root') lane(bp)[st]=1;
   else if(bassSt==='roots8'){ for(let i=st;i<en;i+=2) lane(bp)[i]=1; }
   else if(bassSt==='offbeat'){ for(let i=st;i<en;i++) if(i%4===2) lane(bp)[i]=1; }
   else if(bassSt==='octave'){ for(let i=st;i<en;i+=2) lane((i/2)%2?Math.min(31,bp+7):bp)[i]=1; }
   else if(bassSt==='walk'){ for(let i=st,k=0;i<en;i+=4,k++) lane(16+((d+[0,2,4,5][k%4])%14))[i]=1; }
   else if(bassSt==='sync'){ [0,3,6,10,11].forEach(o=>{ if(st+o<en&&(o===0||r()<.6)) lane(bp)[st+o]=1; }); }
   else if(bassSt==='808'){ const kk=L[0]||[]; let any=false; for(let i=st;i<en;i++) if(kk[i]){ lane(bp)[i]=1; any=true; } if(!any) lane(bp)[st]=1; } });
  if(lead){ const pent=[0,1,2,4,5,7], ph=[]; for(let i=0;i<16;i++) if(r()<(i%2?.18:.4)) ph.push(i); let deg=Math.floor(r()*4); for(let b=0;b<bars;b++) ph.forEach(i=>{ deg=Math.max(0,Math.min(5,deg+pick(r,[-1,0,1,1,-2,2]))); lane(40+pent[deg])[b*16+i]=1; }); }
  const bpm=Math.round(g[1]+r()*(g[2]-g[1]));
  const name=g[0]+' '+(v+1)+' · '+dens+' · '+prog.map(d=>RN[d]).join(' ')+' · '+bpm+' BPM';
  return {gi,v,name,bpm,swing:g[3],kit:g[4],bars,lanes:L,dens,bassSt,chordSt,lead}; }
 /* ---------------- state, undo and writing to the sequencer ---------------- */
 let cur=null, type=getLS('kanin-loop-type','full'), gi=getLS('kanin-loop-genre',0), vi=getLS('kanin-loop-n',0), mute={drums:false,bass:false,chords:false,lead:false}, snaps=[];
 const layerOf=p=>p<16?(PERC.has(p)?'perc':'drums'):p<32?'bass':p<40?'chords':'lead';
 function allowed(p){ const l=layerOf(p); if(l==='perc') return type==='full'||type==='drums'||type==='db'||type==='perc'?!mute.drums:false;
  if(l==='drums') return (type==='full'||type==='drums'||type==='db')&&!mute.drums; if(l==='bass') return (type==='full'||type==='db'||type==='inst')&&!mute.bass;
  if(l==='chords') return (type==='full'||type==='inst')&&!mute.chords; return (type==='full'||type==='inst')&&!mute.lead; }
 function snap(){ const ps=P(); if(!ps) return; snaps.push({steps:ps.pads.map(p=>p.steps.slice()),bars:ps.barsN,bpm:ps.bpm(),kit:ps.kitI,sw:($('padSwing')||{}).value}); if(snaps.length>30) snaps.shift(); }
 function undo(){ const s=snaps.pop(), ps=P(); if(!s||!ps) return say('↶ Nothing from the Loop Library to undo.'); try{ ps.setBars(s.bars); }catch(_){ } s.steps.forEach((st,i)=>{ if(ps.pads[i]) ps.pads[i].steps=st; }); try{ ps.setKit(s.kit); }catch(_){ } try{ KSPEED.setBpm(s.bpm); }catch(_){ } setSw(s.sw); try{ ps.refresh(); }catch(_){ } say('↶ The sequencer is back the way it was.'); paint(); }
 function setSw(v){ const s=$('padSwing'); if(s&&v!=null&&s.value!==String(v)){ s.value=String(v); s.dispatchEvent(new Event('change',{bubbles:true})); } }
 async function write(lp,{keepSnap}={}){ const ps=P(); if(!ps) return say('Open 🎛 Studio first.'); if(!keepSnap) snap();
  if(ps.spbN!==16){ const sp=$('padSpb'); if(sp){ sp.value='16'; sp.dispatchEvent(new Event('change',{bubbles:true})); await new Promise(r=>setTimeout(r,120)); } }
  try{ ps.setBars(lp.bars); }catch(_){ } await new Promise(r=>setTimeout(r,60));
  const n=ps.pads[0].steps.length;
  for(let p=0;p<48;p++){ const pd=ps.pads[p]; if(!pd) continue; const st=new Array(pd.steps.length||n).fill(0); const src=lp.lanes[p]; if(src&&allowed(p)) for(let i=0;i<src.length&&i<st.length;i++) st[i]=src[i]?1:0; pd.steps=st; }
  try{ ps.setKit(lp.kit); }catch(_){ } try{ KSPEED.setBpm(lp.bpm); }catch(_){ } setSw(SW[lp.swing]); try{ ps.refresh(); }catch(_){ } }
 async function load(g,v,{play}={}){ gi=g; vi=v; putLS('kanin-loop-genre',gi); putLS('kanin-loop-n',vi); cur=make(gi,vi); await write(cur); paint(); if(play){ try{ if(!ps().playing) ps().play(); }catch(_){ } } say('🔁 '+cur.name+' is in the sequencer.'); }
 const ps=()=>P()||{};
 /* ---------------- tweaks: each rewrites the loop in the sequencer ---------------- */
 const drumPads=()=>Object.keys(cur.lanes).map(Number).filter(p=>p<16);
 const T={
  half(){ const B=Math.min(4,cur.bars*2); drumPads().forEach(p=>{ const a=cur.lanes[p], o=new Array(B*16).fill(0); a.forEach((x,i)=>{ if(x&&i*2<o.length) o[i*2]=1; }); cur.lanes[p]=o; }); Object.keys(cur.lanes).map(Number).filter(p=>p>=16).forEach(p=>{ const a=cur.lanes[p], o=new Array(B*16).fill(0); a.forEach((x,i)=>{ if(x&&i*2<o.length) o[i*2]=1; }); cur.lanes[p]=o; }); cur.bars=B; return 'Half time: everything stretched to '+B+' bars.'; },
  dbl(){ const B=Math.max(1,cur.bars); drumPads().forEach(p=>{ const a=cur.lanes[p], o=new Array(B*16).fill(0); for(let i=0;i<o.length;i++) o[i]=a[(i*2)%a.length]?1:0; cur.lanes[p]=o; }); return 'Double time: the drums play twice as fast.'; },
  left(){ drumPads().forEach(p=>{ const a=cur.lanes[p]; a.push(a.shift()); }); return 'Drums shifted one step earlier.'; },
  right(){ drumPads().forEach(p=>{ const a=cur.lanes[p]; a.unshift(a.pop()); }); return 'Drums shifted one step later.'; },
  rev(){ drumPads().forEach(p=>{ const a=cur.lanes[p]; for(let b=0;b<cur.bars;b++){ const s=a.slice(b*16,b*16+16).reverse(); s.forEach((x,i)=>a[b*16+i]=x); } }); return 'Drums reversed inside every bar.'; },
  thin(){ let n=0; drumPads().forEach(p=>{ const a=cur.lanes[p]; a.forEach((x,i)=>{ if(x&&i%4!==0&&Math.random()<.3){ a[i]=0; n++; } }); }); return 'Thinned out: '+n+' hits taken away.'; },
  ghost(){ const sp=cur.lanes[2]?2:3; const a=cur.lanes[sp]||(cur.lanes[sp]=new Array(cur.bars*16).fill(0)); let n=0; a.forEach((x,i)=>{ if(!x&&i%2===1&&Math.random()<.18){ a[i]=1; n++; } }); return n+' ghost notes added.'; },
  fill(){ const b=cur.bars-1; [12,13,14,15].forEach((i,k)=>{ const p=[9,8,7,7][k]; (cur.lanes[p]||(cur.lanes[p]=new Array(cur.bars*16).fill(0)))[b*16+i]=1; }); const cr=cur.lanes[10]||(cur.lanes[10]=new Array(cur.bars*16).fill(0)); cr[0]=1; return 'A tom fill at the end and a crash at the top.'; },
  mutate(){ let n=0; drumPads().forEach(p=>{ const a=cur.lanes[p]; a.forEach((x,i)=>{ if(i%16===0&&p===0) return; if(Math.random()<.06){ a[i]=x?0:1; n++; } }); }); return 'Mutated: '+n+' drum steps flipped.'; },
  newdrums(){ const m=make(cur.gi,Math.floor(Math.random()*PER)); for(let p=0;p<16;p++) delete cur.lanes[p]; Object.keys(m.lanes).map(Number).filter(p=>p<16).forEach(p=>{ cur.lanes[p]=fit(m.lanes[p]); }); return 'New drums; your bass and chords stay.'; },
  newbass(){ const m=make(cur.gi,Math.floor(Math.random()*PER)); for(let p=16;p<32;p++) delete cur.lanes[p]; Object.keys(m.lanes).map(Number).filter(p=>p>=16&&p<32).forEach(p=>{ cur.lanes[p]=fit(m.lanes[p]); }); return 'A new bass line.'; },
  newchords(){ const m=make(cur.gi,Math.floor(Math.random()*PER)); for(let p=32;p<48;p++) delete cur.lanes[p]; Object.keys(m.lanes).map(Number).filter(p=>p>=32).forEach(p=>{ cur.lanes[p]=fit(m.lanes[p]); }); return 'New chords and lead.'; }};
 const fit=a=>{ const o=new Array(cur.bars*16).fill(0); for(let i=0;i<o.length;i++) o[i]=a[i%a.length]; return o; };
 async function tweak(k){ if(!cur) await load(gi,vi); const msg=T[k](); cur.name=cur.name.replace(/ · tweaked$/,'')+' · tweaked'; await write(cur); paint(); say('🎛 '+msg); }
 /* ---------------- the panel inside the Studio ---------------- */
 const css=document.createElement('style'); css.textContent=`
#kLoops{margin:10px 0;padding:12px;border-radius:14px;background:linear-gradient(180deg,#1b1f2b,#11141c);border:2px solid #3a4152;color:#eef;font:14px/1.4 system-ui,sans-serif}
#kLoops h4{margin:0 0 6px;font:900 17px system-ui,sans-serif;color:#ffe94a}#kLoops .kln{font-size:12.5px;color:#9aa3b8}
#kLoops .klr{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;align-items:center}
#kLoops select{min-height:40px;border-radius:10px;max-width:100%;flex:1 1 180px}
#kLoops button{min-height:40px;border-radius:10px;padding:0 10px;font:800 13px system-ui,sans-serif}
#kLoops button.go{background:#2bd673!important;color:#08210f!important}#kLoops button.on{background:#ff4f6d!important;color:#fff!important}
#kLoops .klNow{font:800 14px system-ui,sans-serif;color:#7ff;margin-top:4px;overflow-wrap:anywhere}`; document.head.appendChild(css);
 function panel(){ const pad=$('pad'); if(!pad) return null; let d=$('kLoops'); if(d) return d; const host=pad.querySelector('.pin')||pad; d=document.createElement('section'); d.id='kLoops'; d.setAttribute('aria-label','Loop Library');
  const head=$('kStudioHead'); if(head&&head.parentNode===host) host.insertBefore(d,head); else host.insertBefore(d,host.firstChild);
  d.addEventListener('change',e=>{ const t=e.target; if(t.id==='klGenre'){ load(+t.value,0); } if(t.id==='klN'){ load(gi,+t.value); } if(t.id==='klType'){ type=t.value; putLS('kanin-loop-type',type); if(cur) write(cur).then(paint); } if(t.id==='klSwing'){ if(cur){ cur.swing=+t.value; setSw(SW[cur.swing]); } } if(t.id==='klBars'){ if(cur){ const nb=+t.value; Object.keys(cur.lanes).forEach(p=>{ const a=cur.lanes[p], o=new Array(nb*16).fill(0); for(let i=0;i<o.length;i++) o[i]=a[i%a.length]; cur.lanes[p]=o; }); cur.bars=nb; write(cur).then(paint); say('🔁 The loop is '+nb+' bar'+(nb>1?'s':'')+' long.'); } } });
  d.addEventListener('click',async e=>{ const b=e.target.closest('[data-kl]'); if(!b) return; e.stopPropagation(); const k=b.dataset.kl;
   if(k==='play'){ if(!cur) await load(gi,vi); try{ if(!ps().playing) ps().play(); }catch(_){ } return; }
   if(k==='stop'){ try{ ps().stop(); }catch(_){ } return; }
   if(k==='prev') return load(gi,(vi+PER-1)%PER,{play:ps().playing}); if(k==='next') return load(gi,(vi+1)%PER,{play:ps().playing});
   if(k==='rand') return load(gi,Math.floor(Math.random()*PER),{play:ps().playing});
   if(k==='any') return load(Math.floor(Math.random()*G.length),Math.floor(Math.random()*PER),{play:ps().playing});
   if(k==='cannon'){ let a=Math.random(), c=Math.random(); try{ const r=UNILAW.fire('games',{quiet:true}); if(r&&r.land){ a=(r.land[0]/24+(r.first||0))%1; c=(r.land[1]/24+(r.first||0))%1; } }catch(_){ } return load(Math.floor(a*G.length),Math.floor(c*PER),{play:ps().playing}); }
   if(k==='undo') return undo();
   if(k==='save'){ const sb=$('padSave'); if(sb){ sb.click(); say('💾 Saved with your beats in 📁 Projects.'); } else say('💾 Your loop is in the sequencer; save it from the Studio.'); return; }
   if(k.startsWith('m-')){ const l=k.slice(2); mute[l]=!mute[l]; b.classList.toggle('on',mute[l]); if(cur){ await write(cur,{keepSnap:true}); } return say((mute[l]?'🔇 ':'🔊 ')+l[0].toUpperCase()+l.slice(1)+(mute[l]?' muted.':' back on.')); }
   if(T[k]) return tweak(k); });
  return d; }
 function paint(){ const d=panel(); if(!d) return; const opt=(v,t,sel)=>'<option value="'+v+'"'+(sel?' selected':'')+'>'+t+'</option>';
  const names=[]; for(let v=0;v<PER;v++) names.push(v);
  d.innerHTML='<h4>🔁 Loop Library · '+(G.length*PER).toLocaleString()+' loops</h4><div class="kln">'+G.length+' genres × '+PER+' loops each, written into the pads below: drums, bass, chords and a lead, in your key. Each loop is always the same loop.</div>'+
   '<div class="klr"><select id="klGenre" aria-label="Loop genre">'+G.map((g,i)=>opt(i,g[0]+' · '+g[1]+'–'+g[2]+' BPM',i===gi)).join('')+'</select><select id="klN" aria-label="Loop number">'+names.map(v=>opt(v,'Loop '+(v+1),v===vi)).join('')+'</select><select id="klType" aria-label="What plays">'+TYPES.map(([v,t])=>opt(v,t,v===type)).join('')+'</select></div>'+
   '<div class="klr"><button type="button" class="go" data-kl="play" data-noul>▶ Play</button><button type="button" data-kl="stop" data-noul>■ Stop</button><button type="button" data-kl="prev" data-noul>⏮ Previous</button><button type="button" data-kl="next" data-noul>⏭ Next</button><button type="button" data-kl="rand" data-noul>🎲 In this genre</button><button type="button" data-kl="any" data-noul>🎲 Any genre</button><button type="button" data-kl="cannon" data-noul>💥 Cannon</button><button type="button" data-kl="undo" data-noul>↶ Undo</button><button type="button" data-kl="save" data-noul>💾 Save</button></div>'+
   '<div class="klr"><button type="button" data-kl="half" data-noul>½ Half time</button><button type="button" data-kl="dbl" data-noul>2× Double time</button><button type="button" data-kl="left" data-noul>⇠ Shift</button><button type="button" data-kl="right" data-noul>Shift ⇢</button><button type="button" data-kl="rev" data-noul>⇄ Reverse</button><button type="button" data-kl="thin" data-noul>✂ Thin out</button><button type="button" data-kl="ghost" data-noul>👻 Ghost notes</button><button type="button" data-kl="fill" data-noul>🥁 Fill</button><button type="button" data-kl="mutate" data-noul>🧬 Mutate</button></div>'+
   '<div class="klr"><button type="button" data-kl="newdrums" data-noul>🎲 New drums</button><button type="button" data-kl="newbass" data-noul>🎲 New bass</button><button type="button" data-kl="newchords" data-noul>🎲 New chords</button>'+['drums','bass','chords','lead'].map(l=>'<button type="button" data-kl="m-'+l+'" class="'+(mute[l]?'on':'')+'" data-noul>🔇 '+l[0].toUpperCase()+l.slice(1)+'</button>').join('')+
   '<select id="klSwing" aria-label="Swing" style="flex:0 1 150px">'+['Straight','Light swing','Medium swing','Heavy swing','Shuffle'].map((t,i)=>opt(i,t,cur&&cur.swing===i)).join('')+'</select><select id="klBars" aria-label="Loop length" style="flex:0 1 120px">'+[1,2,4].map(n=>opt(n,n+' bar'+(n>1?'s':''),cur&&cur.bars===n)).join('')+'</select></div>'+
   '<div class="klNow">'+(cur?'Now: '+cur.name+' · bass '+cur.bassSt+' · chords '+cur.chordSt+(cur.lead?' · lead':''):'Pick a genre and a loop, or press 🎲 or 💥.')+'</div>'; }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')&&!$('kLoops')) paint(); },700);
 /* the cannon can land on a loop genre too */
 setTimeout(function addRealm(){ try{ if(window.KJUMP&&KJUMP.realms&&!KJUMP.realms.some(r=>r.id==='loopgenre')) KJUMP.realms.push({id:'loopgenre',i:'🔁',n:'Loop genre',o:()=>G.map((g,i)=>({v:String(i),t:g[0]+' loops'}))}); }catch(_){ } },3000);
 window.KLOOPS={genres:G.map(g=>g[0]),count:G.length*PER,make,load,tweak,undo,get current(){ return cur; },types:TYPES.map(t=>t[0]),setType(t){ type=t; }};
})();
