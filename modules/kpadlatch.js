(()=>{ /* PAD MODES: LATCHED AND UNLATCHED (v234). The pad machine's "Pad mode" list sets what a pad does when you hit it:
   Tap: one hit. Hold (unlatched): the pad repeats at the rate you pick for as long as your finger stays on it. Latch: one tap starts
   it repeating, the next tap on the same pad stops it, and any number of pads can run at once. Latch one: a new pad takes over from
   the one running. Latch one bar: the pad runs to the end of the bar and stops by itself. Every repeat is a real hit, so while ● REC
   is on each one records, in real time. Recording now keeps every hit exactly where you played it (the factory setting, unlatched); 🧲 Latch to grid
   snaps hits to the grid (its size on the Q button); this setting is turned on once for everyone with this version. ■ Stop, the remote and closing the Studio release
   every latched pad. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } }; const P=()=>window.PADSTUDIO;
 const MODES=[['hit','Tap: one hit'],['hold','Hold: repeats while held (unlatched)'],['latch','Latch: tap on, tap off'],['latch1','Latch one pad at a time'],['latchbar','Latch for one bar']];
 const RATES=[['2','1/8'],['3','1/8 triplet'],['4','1/16'],['6','1/16 triplet'],['8','1/32']];
 let mode='hit', rate='4'; try{ mode=JSON.parse(localStorage.getItem('kanin-padmode')||'"hit"'); rate=JSON.parse(localStorage.getItem('kanin-padrate')||'"4"'); }catch(_){ }
 if(!MODES.some(m=>m[0]===mode)) mode='hit'; if(!RATES.some(r=>r[0]===rate)) rate='4';
 /* real time recording, turned on once for this version (the grid is still one tap away on Q) */
 try{ if(!localStorage.getItem('kanin-recmode-v234')){ window.PADRECMODE='live'; localStorage.setItem('kanin-recmode','"live"'); localStorage.setItem('kanin-recmode-v234','1'); } }catch(_){ window.PADRECMODE='live'; }
 const runs=new Map();
 const padEl=i=>{ const g=$('padGrid'); return g&&g.querySelector('[data-i="'+i+'"]'); };
 function tick(i){ const r=runs.get(i); if(!r) return; const ps=P(); if(!ps) return stop(i); try{ ps.hitPad(i); }catch(_){ } const bpm=Math.max(40,Math.min(240,(ps.bpm&&ps.bpm())||90)); r.t=setTimeout(()=>tick(i),60000/bpm/(+rate)); }
 function start(i){ if(runs.has(i)) return; const r={t:0,end:0}; runs.set(i,r); tick(i);
  if(mode==='latchbar'){ const ps=P(); const bpm=Math.max(40,Math.min(240,(ps&&ps.bpm&&ps.bpm())||90)); r.end=setTimeout(()=>stop(i),240000/bpm); } paint(); }
 function stop(i){ const r=runs.get(i); if(!r) return; clearTimeout(r.t); clearTimeout(r.end); runs.delete(i); paint(); }
 function stopAll(){ [...runs.keys()].forEach(stop); }
 function snapPaint(){ document.querySelectorAll('.kPadMode [data-pl="snap"]').forEach(b=>{ const on=(window.PADRECMODE||'live')!=='live'; const t='🧲 Latch to grid: '+(on?'on':'off'); if(b.textContent!==t) b.textContent=t; b.classList.toggle('on',on); b.style.background=on?'#ffe94a':''; b.style.color=on?'#14163a':''; }); }
 function paint(){ snapPaint(); const g=$('padGrid'); if(!g) return; g.querySelectorAll('.pd').forEach(el=>{ const on=runs.has(+el.dataset.i); if(el.classList.contains('kLatched')!==on) el.classList.toggle('kLatched',on); }); }
 /* the pad grid: hold and tap use the Studio's own note repeat; the latch modes are handled here */
 document.addEventListener('pointerdown',e=>{ const b=e.target.closest&&e.target.closest('#padGrid .pd'); if(!b) return; const rp=$('padRepeat');
  if(mode==='hit'){ if(rp&&rp.value!=='0') rp.value='0'; return; }
  if(mode==='hold'){ if(rp){ const v=[...rp.options].some(o=>o.value===rate)?rate:'4'; if(rp.value!==v) rp.value=v; } return; }
  e.preventDefault(); e.stopImmediatePropagation(); if(rp&&rp.value!=='0') rp.value='0'; const i=+b.dataset.i;
  if(runs.has(i)){ stop(i); return; } if(mode==='latch1') stopAll(); start(i); },true);
 /* release every latch on Stop, the remote's Stop or leaving the Studio */
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kRemote [data-r="stop"],#kStopBtn.kStop,[data-m="stop"],#padStop')) stopAll(); },true);
 setInterval(()=>{ const pad=$('pad'); if(runs.size&&!(pad&&pad.classList.contains('on'))) stopAll(); else paint(); ensure(); },400);
 const css=document.createElement('style'); css.textContent=`
#padGrid .pd.kLatched{box-shadow:0 0 0 3px #ffe94a,0 0 16px #ffe94a!important;animation:kLatchPulse .5s ease-in-out infinite alternate}
@keyframes kLatchPulse{from{filter:brightness(1)}to{filter:brightness(1.35)}}
.kPadMode{display:flex;align-items:center;gap:6px;flex:none}.kPadMode select{min-height:36px;max-width:190px;border-radius:8px;font:700 12.5px system-ui,sans-serif}
.kPadMode .lbl{font:800 10px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.08em;text-transform:uppercase}
.kPadMode button{min-height:36px;border-radius:8px;font:800 12px system-ui,sans-serif;padding:0 8px}`; document.head.appendChild(css);
 function ensure(){ const rp=$('padRepeat'); if(rp&&![...rp.options].some(o=>o.value==='3')){ const op=document.createElement('option'); op.value='3'; op.textContent='1/8 triplet'; const after=[...rp.options].find(o=>o.value==='4'); rp.insertBefore(op,after||null); }
  const bar=$('mpcBar'); if(!bar) return; const row=bar.querySelector('.mr2')||bar; let d=row.querySelector('.kPadMode'); if(d) return; d=document.createElement('div'); d.className='kPadMode';
  d.innerHTML='<span class="lbl">Pad mode</span><select data-pl="mode" aria-label="Pad mode" data-nodice>'+MODES.map(([v,t])=>'<option value="'+v+'"'+(v===mode?' selected':'')+'>'+t+'</option>').join('')+'</select><select data-pl="rate" aria-label="Repeat rate" data-nodice>'+RATES.map(([v,t])=>'<option value="'+v+'"'+(v===rate?' selected':'')+'>Repeat '+t+'</option>').join('')+'</select><button type="button" data-pl="off" data-noul>⏹ Release all</button><button type="button" data-pl="snap" data-noul>🧲 Latch to grid: off</button>';
  d.addEventListener('change',e=>{ const k=e.target.dataset.pl; if(!k) return; e.stopPropagation(); if(k==='mode'){ mode=e.target.value; stopAll(); try{ localStorage.setItem('kanin-padmode',JSON.stringify(mode)); }catch(_){ } say({hit:'🥁 Tap: each hit plays once.',hold:'🥁 Hold: a pad repeats while your finger is on it.',latch:'🔒 Latch: tap a pad to start it, tap it again to stop. Several can run.',latch1:'🔒 Latch one: a new pad takes over from the one running.',latchbar:'🔒 Latch one bar: a pad runs to the end of the bar.'}[mode]); }
   if(k==='rate'){ rate=e.target.value; try{ localStorage.setItem('kanin-padrate',JSON.stringify(rate)); }catch(_){ } } });
  d.addEventListener('click',e=>{ if(e.target.closest('[data-pl="snap"]')){ e.stopPropagation(); const live=(window.PADRECMODE||'live')==='live'; let g='step'; try{ g=JSON.parse(localStorage.getItem('kanin-recgrid')||'"step"'); }catch(_){ } const nx=live?(g==='live'?'step':g):'live'; if(!live){ try{ localStorage.setItem('kanin-recgrid',JSON.stringify(window.PADRECMODE)); }catch(_){ } } window.PADRECMODE=nx; try{ localStorage.setItem('kanin-recmode',JSON.stringify(nx)); }catch(_){ } snapPaint(); say(nx==='live'?'🧲 Latch to grid off: every hit records exactly where you play it.':'🧲 Latch to grid on: hits snap to '+({step:'1/16','8':'1/8','4':'1/4','32':'1/32'}[nx]||nx)+'. Change the grid with Q.'); return; }
   if(e.target.closest('[data-pl="off"]')){ e.stopPropagation(); const n=runs.size; stopAll(); say(n?'⏹ Every latched pad released.':'⏹ No pad is latched.'); } });
  row.appendChild(d); }
 window.KPADLATCH={modes:MODES.map(m=>m[0]),get mode(){ return mode; },set mode(v){ if(MODES.some(m=>m[0]===v)){ mode=v; stopAll(); } },set rate(v){ if(RATES.some(r=>r[0]===String(v))) rate=String(v); },running:()=>[...runs.keys()],stopAll,start,stop};
})();
