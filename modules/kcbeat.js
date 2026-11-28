(()=>{ /* 🎯 CANNON BEAT (v255): a game that plays and writes the beat machine. The cannon lays a target groove across four lanes (kick, snare,
   hi-hat, clap, from the pad bank on screen) and the targets fall in time with the beat. Hit a lane's pad as its target reaches the line, by
   its key on the computer keyboard (the pads' own keys), by tapping the lane, or on any pad, and the cannon fires that hit into the beat
   machine's pattern on that exact step: Perfect, Good or Miss. A miss leaves the step empty, so the beat that plays back is the beat you hit.
   🎲 lays a new target groove; Easy, Normal and Hard set how busy it is; "Play along" scores against the pattern already in the beat
   machine and writes nothing. ↶ Undo puts back the pattern from before the game. It floats like the pads and keyboard, on every screen. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const LANES=[[0,'Kick','#ffe94a'],[2,'Snare','#ff7ad1'],[4,'Hi-hat','#6fe8ff'],[3,'Clap','#7dffb0']];
 const KEYS='1234qwerasdfzxcv';
 const bank=()=>{ const b=$('padBank'); return Math.max(0,Math.min(3,+(b&&b.value)||0))*16; };
 let st={run:false,mode:'build',level:'normal',T:null,hit:null,score:0,combo:0,best:0,perf:0,good:0,miss:0,fired:0,lastPass:-1,passes:0,clock:[],snap:null};
 const css=document.createElement('style'); css.textContent=`
#kCBeat{background:linear-gradient(170deg,#1c0f4a,#07041a);color:#eef;font:14px system-ui,sans-serif;display:none;flex-direction:column;gap:6px;padding:8px;box-sizing:border-box;border:2px solid #ffe94a;border-radius:6px 18px 6px 18px}
#kCBeat.kFOn:not(.kFOff){display:flex}
#kCBeat .cbBar{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
#kCBeat .cbBar button,#kCBeat .cbBar select{min-height:40px;padding:0 10px;border-radius:4px 12px 4px 12px;font:800 13px system-ui,sans-serif}
#kCBeat .cbBar select{width:auto!important;max-width:170px!important;flex:0 1 auto!important}
#kCBeat .cbBar .go{background:#137a3f!important;border-color:#7dffb0!important}
#kCBeat .cbBar .st{background:#b3172f!important}
#kCBeat .cbScore{display:flex;flex-wrap:wrap;gap:10px;font:800 13px ui-monospace,monospace;color:#ffe94a}
#kCBeat canvas{flex:1;min-height:220px;width:100%;border-radius:10px;background:#05030f;touch-action:none;cursor:pointer}
#kCBeat .cbNote{font-size:12px;opacity:.85;line-height:1.4}`; document.head.appendChild(css);
 function el(){ let d=$('kCBeat'); if(d) return d; d=document.createElement('div'); d.id='kCBeat'; d.setAttribute('role','application'); d.setAttribute('aria-label','Cannon Beat game');
  d.innerHTML='<div class="cbBar"><button type="button" class="go" data-cb="start" data-noul>▶ Start</button><button type="button" class="st" data-cb="stop" data-noul>■ Stop</button><button type="button" data-cb="new" data-noul>🎲 New targets</button>'+
   '<select data-cb="level" aria-label="How busy"><option value="easy">Easy</option><option value="normal" selected>Normal</option><option value="hard">Hard</option><option value="pro">Pro</option><option value="wild">Wild</option></select>'+
   '<select data-cb="mode" aria-label="What a hit does"><option value="build" selected>Build the beat</option><option value="play">Play along</option><option value="fill">Fill the gaps</option><option value="double">Double time</option><option value="half">Half time</option></select>'+
   '<button type="button" data-cb="undo" data-noul>↶ Undo</button></div>'+
   '<div class="cbScore"><span data-cs="score">Score 0</span><span data-cs="combo">Combo 0</span><span data-cs="acc">Perfect 0 · Good 0 · Miss 0</span><span data-cs="fired">Fired in 0</span></div>'+
   '<canvas width="640" height="360" aria-label="Lanes"></canvas>'+
   '<div class="cbNote" data-cs="note">Hit each lane’s pad when its target reaches the line: by its key, by tapping the lane, or on the pads. Every hit is fired into the beat machine on that step.</div>';
  document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-cb]'); if(!b||b.tagName==='SELECT') return; e.stopPropagation(); const k=b.dataset.cb; if(k==='start') start(); if(k==='stop') stop(true); if(k==='new'){ lay(); say('🎲 The cannon laid new targets.'); } if(k==='undo') undo(); });
  d.addEventListener('change',e=>{ const k=e.target.dataset.cb; if(k==='level'){ st.level=e.target.value; lay(); } if(k==='mode'){ st.mode=e.target.value; lay(); } });
  const cv=d.querySelector('canvas'); cv.addEventListener('pointerdown',e=>{ const r=cv.getBoundingClientRect(); const l=Math.floor((e.clientX-r.left)/r.width*LANES.length); const P=PS(); if(P&&l>=0&&l<LANES.length){ e.preventDefault(); try{ P.hitPad(bank()+LANES[l][0]); }catch(_){ } } });
  return d; }
 /* the beat machine's own clock: every scheduled step, with its audio time */
 let hooked=false; function hook(){ const P=PS(); if(hooked||!P||!P.STEPHOOKS) return; hooked=true; P.STEPHOOKS.push((c,dest,t,s,sd)=>{ if(c!==P.ac()) return; st.clock.push([t,s,sd]); if(st.clock.length>64) st.clock.splice(0,st.clock.length-64); }); }
 function now(){ const P=PS(); const c=P&&P.ac&&P.ac(); if(!c||!st.clock.length) return null; const t=c.currentTime; let e=null; for(let i=st.clock.length-1;i>=0;i--){ if(st.clock[i][0]<=t){ e=st.clock[i]; break; } } if(!e) return null; return {pos:e[1]+(t-e[0])/e[2],sd:e[2]}; }
 const total=()=>{ const P=PS(); return Math.max(16,(P&&P.total)||16); };
 /* the cannon lays the targets */
 const rnd=()=>Math.random();
 function lay(){ const P=PS(); if(!P) return; const N=total(), spb=P.spb||16, q=spb/4; const D={easy:.35,normal:.6,hard:.85,pro:1,wild:1.2}[st.level]||.6;
  if(st.mode==='play'){ st.T=LANES.map(([o])=>{ const p=P.pads[bank()+o]; return Array.from({length:N},(_,k)=>!!(p&&p.steps&&p.steps[k])); }); }
  else { st.T=LANES.map(([o],l)=>Array.from({length:N},(_,k)=>{ const inBar=k%spb, beat=inBar%q===0, off=inBar%(q/2)===0;
    if(st.mode==='half'&&k%2) return false;
    if(l===0) return beat&&(inBar===0||rnd()<.45*D)||(!beat&&off&&rnd()<.22*D)||(st.mode==='double'&&off&&rnd()<.5*D);
    if(l===1) return inBar===q||inBar===3*q||(st.level!=='easy'&&!beat&&rnd()<.08*D);
    if(l===2) return off&&rnd()<(.55+.4*D)||(st.level==='hard'||st.level==='pro'||st.level==='wild')&&!off&&rnd()<.3*D;
    return (inBar===q||inBar===3*q)&&rnd()<.5*D||(!beat&&rnd()<.06*D); }));
   if(st.mode==='fill'){ st.T=st.T.map((row,l)=>row.map((v,k)=>{ const p=P.pads[bank()+LANES[l][0]]; return v&&!(p&&p.steps&&p.steps[k]); })); } }
  st.hit=LANES.map(()=>Array(N).fill(0)); st.lastPass=-1; }
 function paintScore(){ const d=$('kCBeat'); if(!d) return; const set=(k,v)=>{ const x=d.querySelector('[data-cs="'+k+'"]'); if(x&&x.textContent!==v) x.textContent=v; };
  set('score','Score '+st.score); set('combo','Combo '+st.combo+(st.best?' (best '+st.best+')':'')); set('acc','Perfect '+st.perf+' · Good '+st.good+' · Miss '+st.miss); set('fired','Fired in '+st.fired); }
 /* a pad was hit (by key, tap, click or MIDI): judge it against the nearest target in its lane */
 let shots=[], flashes=[];
 function onPad(i){ if(!st.run||!st.T) return; const l=LANES.findIndex(x=>bank()+x[0]===i); if(l<0) return; const n=now(); if(!n) return; const N=total(); const pos=n.pos;
  let best=null; for(let d=-1;d<=1;d++){ const k=((Math.round(pos)+d)%N+N)%N; if(!st.T[l][k]||st.hit[l][k]) continue; let dk=pos-Math.round(pos)-d; if(Math.abs(dk)>.75) continue; if(!best||Math.abs(dk)<Math.abs(best.dk)) best={k,dk}; }
  if(!best){ st.combo=0; paintScore(); return; }
  const a=Math.abs(best.dk); const P=PS(); st.hit[l][best.k]=a<=.25?2:1; if(a<=.25){ st.perf++; st.score+=100+st.combo*5; } else { st.good++; st.score+=50+st.combo*2; } st.combo++; st.best=Math.max(st.best,st.combo);
  if(st.mode!=='play'&&P){ const p=P.pads[i]; if(p&&p.steps&&!p.steps[best.k]){ p.steps[best.k]=1; st.fired++; try{ P.refresh(); }catch(_){ } } }
  shots.push({l,t:performance.now(),q:a<=.25?'Perfect':'Good'}); paintScore(); }
 let mo=null; function watchPads(){ const g=$('padGrid'); if(!g||mo) return; mo=new MutationObserver(ms=>{ for(const m of ms){ const t=m.target; if(m.attributeName==='class'&&t.classList&&t.classList.contains('hit')&&!m.oldValue?.includes('hit')&&t.dataset.i!=null) onPad(+t.dataset.i); } }); mo.observe(g,{subtree:true,attributes:true,attributeFilter:['class'],attributeOldValue:true}); }
 function start(){ const P=PS(); if(!P) return say('The studio is still loading. Try again in a moment.'); hook(); watchPads();
  st.snap=P.pads.map(p=>p.steps?p.steps.slice():null); try{ KUNDO.push(()=>undo(true),'the beat before Cannon Beat'); }catch(_){ }
  if(!st.T) lay(); Object.assign(st,{run:true,score:0,combo:0,perf:0,good:0,miss:0,fired:0,passes:0}); st.hit=LANES.map(()=>Array(total()).fill(0));
  try{ const f=F(); if(f&&!f.isOpen('pads')) f.open('pads'); }catch(_){ }
  if(!P.playing){ try{ P.play(); }catch(_){ } } paintScore(); loop(); say('🎯 Cannon Beat: hit the targets as they reach the line. '+(st.mode==='play'?'Play along: nothing is written.':'Every hit is fired into the beat.')); }
 function stop(tell){ const P=PS(); st.run=false; try{ if(P&&P.playing) P.stop(); }catch(_){ } if(tell){ const tot=st.perf+st.good+st.miss; const pct=tot?Math.round((st.perf+st.good)/tot*100):0; const n=$('kCBeat')&&$('kCBeat').querySelector('[data-cs="note"]'); const m='🎯 '+st.score+' points, '+pct+'% on target, best combo '+st.best+'. '+(st.mode==='play'?'':st.fired+' hits fired into the beat machine: press ▶ to hear the beat you built, or ↶ Undo for the old one.'); if(n) n.textContent=m; say(m); } }
 function undo(quiet){ const P=PS(); if(!P||!st.snap) return; st.snap.forEach((s,i)=>{ if(s&&P.pads[i]) P.pads[i].steps=s.slice(); }); try{ P.refresh(); }catch(_){ } if(!quiet) say('↶ The beat is back to how it was before Cannon Beat.'); }
 /* drawing */
 function loop(){ const d=$('kCBeat'); if(!d||!st.run) return; const cv=d.querySelector('canvas'); const r=cv.getBoundingClientRect(); const W=Math.max(200,Math.round(r.width)), H=Math.max(160,Math.round(r.height)); if(cv.width!==W) cv.width=W; if(cv.height!==H) cv.height=H; const x=cv.getContext('2d');
  x.fillStyle='#05030f'; x.fillRect(0,0,W,H); const L=LANES.length, lw=W/L, line=H-46, ahead=16, px=(line-10)/ahead; const n=now(); const N=total();
  LANES.forEach(([o,name,col],l)=>{ x.fillStyle=l%2?'rgba(255,255,255,.035)':'rgba(255,255,255,.06)'; x.fillRect(l*lw,0,lw,H);
   x.fillStyle=col; x.font='800 12px system-ui,sans-serif'; x.textAlign='center'; const key=(KEYS[o]||'').toUpperCase(); x.fillText(name+' · '+key,l*lw+lw/2,H-8);
   /* the cannon at the foot of the lane */
   x.save(); x.translate(l*lw+lw/2,line+18); x.fillStyle='#ffe94a'; x.fillRect(-7,-14,14,18); x.beginPath(); x.arc(0,6,9,0,7); x.fillStyle='#6b4ff5'; x.fill(); x.restore(); });
  x.strokeStyle='#ffe94a'; x.lineWidth=3; x.beginPath(); x.moveTo(0,line); x.lineTo(W,line); x.stroke();
  if(n&&st.T){ const pos=n.pos; const pass=Math.floor(pos/N);
   for(let l=0;l<L;l++){ for(let a=-1;a<=ahead;a++){ const kk=Math.floor(pos)+a; const k=((kk%N)+N)%N; if(!st.T[l]||!st.T[l][k]) continue; const y=line-(kk-pos)*px; if(y<-20||y>line+30) continue; const h=st.hit[l][k];
     if(!h&&kk-pos<-.75){ st.hit[l][k]=-1; st.miss++; st.combo=0; paintScore(); }
     const hh=st.hit[l][k]; x.beginPath(); x.arc(l*lw+lw/2,y,Math.min(18,lw/4),0,7); x.fillStyle=hh>0?'rgba(125,255,176,.25)':hh<0?'rgba(255,90,110,.35)':LANES[l][2]; x.fill(); if(hh===0){ x.lineWidth=2; x.strokeStyle='#fff'; x.stroke(); } } }
   /* a new pass of the loop: clear the marks so the next pass can be played again */
   if(st.lastPass!==pass){ if(st.lastPass>=0){ st.passes++; st.hit=st.hit.map(row=>row.map(v=>v>0&&st.mode!=='play'?v:0)); } st.lastPass=pass; } }
  else { x.fillStyle='#fff'; x.textAlign='center'; x.font='700 15px system-ui,sans-serif'; x.fillText('Waiting for the beat… press ▶ Start',W/2,H/2); }
  const t=performance.now(); shots=shots.filter(s=>t-s.t<450); shots.forEach(s=>{ const k=(t-s.t)/450; const cx=s.l*lw+lw/2; x.globalAlpha=1-k; x.fillStyle='#fff'; x.beginPath(); x.arc(cx,line-k*(line-20),5+10*k,0,7); x.fill(); x.font='900 14px system-ui,sans-serif'; x.textAlign='center'; x.fillStyle=s.q==='Perfect'?'#7dffb0':'#ffe94a'; x.fillText(s.q,cx,line-24-k*20); x.globalAlpha=1; });
  requestAnimationFrame(loop); }
 /* a floating panel like the pads, opened from the studio bar, the Games screen and Find */
 function reg(){ const f=F(); if(!f||!f.add) return; if(!reg.done){ el(); f.add('cbeat',{get:()=>$('kCBeat'),t:'🎯 Cannon Beat · hit the targets, build the beat',i:'🎯',l:'Cannon Beat'}); reg.done=true;
   try{ if(!localStorage.getItem('kanin-float-cbeat')){ const ph=innerWidth<=760, W=innerWidth-(ph?58:76); localStorage.setItem('kanin-float-cbeat',JSON.stringify(ph?{x:4,y:56,w:W-8,h:Math.round(innerHeight*.7)}:{x:Math.round(W*.3),y:90,w:Math.min(680,Math.round(W*.5)),h:Math.round(innerHeight*.72)})); } }catch(_){ } }
  const bb=$('bbBar'); if(bb&&!bb.querySelector('[data-cbo]')){ const b=document.createElement('button'); b.type='button'; b.dataset.cbo='1'; b.setAttribute('data-noul',''); b.textContent='🎯 Cannon Beat'; b.title='A game that builds the beat: hit the targets on time'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); open(); },true); bb.appendChild(b); }
  const gd=$('gamesDock'); if(gd&&!gd.hidden&&!gd.querySelector('[data-cbg]')){ const b=document.createElement('button'); b.type='button'; b.dataset.cbg='1'; b.setAttribute('data-noul',''); b.textContent='🎯 Cannon Beat · the game that builds your beat'; b.style.cssText='display:block;margin:8px auto;min-height:52px;padding:0 20px;border-radius:4px 16px 4px 16px;background:#ffe94a;color:#14092e;font:900 16px system-ui,sans-serif'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); open(); },true); const host=gd.querySelector('.gsIn,.gdIn,[class*="In"]')||gd; host.insertBefore(b,host.firstChild); } }
 function idle(){ const d=$('kCBeat'); if(!d||st.run) return; const cv=d.querySelector('canvas'); const r=cv.getBoundingClientRect(); const W=Math.max(200,Math.round(r.width)), H=Math.max(160,Math.round(r.height)); cv.width=W; cv.height=H; const x=cv.getContext('2d'); x.fillStyle='#05030f'; x.fillRect(0,0,W,H); const lw=W/LANES.length; LANES.forEach(([o,n,c],l)=>{ x.fillStyle=l%2?'rgba(255,255,255,.035)':'rgba(255,255,255,.06)'; x.fillRect(l*lw,0,lw,H); x.fillStyle=c; x.font='800 12px system-ui,sans-serif'; x.textAlign='center'; x.fillText(n+' · '+(KEYS[o]||'').toUpperCase(),l*lw+lw/2,H-8); }); x.fillStyle='#ffe94a'; x.font='900 18px system-ui,sans-serif'; x.textAlign='center'; x.fillText('🎯 Press ▶ Start',W/2,H/2-8); x.fillStyle='#fff'; x.font='600 13px system-ui,sans-serif'; x.fillText('Hit each lane’s pad as its target reaches the line',W/2,H/2+16); }
 function open(){ const f=F(); if(!f) return; reg(); f.open('cbeat'); setTimeout(idle,200); try{ const R=$('kRemote'); if(R&&innerWidth<=760) R.classList.add('min'); }catch(_){ } try{ if(!st.T) lay(); }catch(_){ } }
 setInterval(reg,1000);
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Play','🎯','Cannon Beat: the game that builds your beat on the beat machine','Cannon Beat',()=>open()); }); }catch(_){ }
 try{ const hookCannon=()=>{ if(window.KCANNON&&KCANNON.SHOT&&!KCANNON.SHOT.kCBeat){ KCANNON.SHOT.kCBeat=()=>{ lay(); return true; }; KCANNON.NAME.kCBeat='Cannon Beat'; } }; hookCannon(); setTimeout(hookCannon,3000); }catch(_){ }
 window.KCBEAT={open,start,stop,lay,undo,get state(){ return st; },onPad};
})();
