(()=>{ /* 🥁 THE MPC ROW (v225): the floating beat machine works like an Akai MPC. Right above the 16 pads:
   ● REC · ▶ PLAY / ■ STOP · ↶ UNDO · 🗑 CLEAR, then 1 · 2 · 4 BARS, the tempo (− 90 +), 🔔 CLICK and the timing grid.
   A 2-bar loop in two seconds: tap 2 BARS, tap ● REC (the loop starts with the click), play the pads: every hit lands in the
   loop on the beat and plays back on the next pass; keep playing to layer more, ↶ UNDO takes back the last hit or clear,
   ● REC again stops recording and the loop keeps going; ■ STOP ends it. All of it drives the studio's own sequencer. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const recOn=()=>{ const b=$('padRecLive'); return !!b&&(b.classList.contains('rec')||/on$/i.test(b.textContent.trim())); };
 const clickOn=()=>{ const c=$('padClick'); const t=c?c.textContent:''; return /on/i.test(t)&&!/off/i.test(t); };
 const QS=[['step','1/16'],['8','1/8'],['4','1/4'],['32','1/32'],['live','Live']];
 const css=document.createElement('style'); css.textContent=`
#mpcBar{order:-2;display:flex;flex-direction:column;gap:5px;margin:2px 0 8px;padding:6px;border-radius:12px;background:linear-gradient(180deg,#22252e,#15171d);border:1px solid #3a3f4d}
#mpcBar .mr{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:5px}
#mpcBar .mr2{display:flex;flex-wrap:nowrap;gap:5px;align-items:center;overflow-x:auto;scrollbar-width:thin;padding-bottom:2px}
#mpcBar .mr2 > *{flex:none}
#mpcBar button{min-height:46px!important;border-radius:10px!important;font:900 14px/1 system-ui,sans-serif!important;padding:0 6px!important;border:2px solid #444a5a!important;background:#2c303b!important;color:#f2f2f2!important;letter-spacing:.02em}
#mpcBar button.rec{background:#5a0f18!important;border-color:#ff3b4f!important;color:#ffd0d6!important}
#mpcBar button.rec.on{background:#e0102e!important;color:#fff!important;animation:mpcBlink 1s steps(2) infinite}
#mpcBar button.play{background:#123d22!important;border-color:#2ecc71!important}#mpcBar button.play.on{background:#1f9d55!important}
#mpcBar button.sm{min-height:40px!important;min-width:40px;font-size:13px!important}
#mpcBar button.sm.on{background:#ffe94a!important;color:#14163a!important;border-color:#ffe94a!important}
#mpcBar .grp{display:flex;gap:4px;align-items:center}
#mpcBar .lbl{font:800 11px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.06em;text-transform:uppercase}
#mpcBar .lcd{font:900 15px ui-monospace,monospace;color:#7cff8a;background:#0b1a10;border:1px solid #1f5a2c;border-radius:8px;padding:6px 8px;min-width:84px;text-align:center}
#mpcBar .bpm{font:900 16px ui-monospace,monospace;color:#ffe94a;min-width:34px;text-align:center}
@keyframes mpcBlink{50%{opacity:.55}}
@media (max-height:620px){ #mpcBar{padding:4px;gap:4px;margin-bottom:5px} #mpcBar button{min-height:38px!important} #mpcBar button.sm{min-height:34px!important;min-width:34px} #mpcBar .lcd{padding:4px 6px} }
@media (max-width:760px){ #mpcBar button{font-size:13px!important} #mpcBar .lcd{min-width:70px;font-size:13px} }`; document.head.appendChild(css);
 let clearedBackup=null; let lastAct='';
 function build(){ const g=$('padGrid'); if(!g||!PS()) return null; let m=$('mpcBar'); if(m&&m.nextElementSibling===g) return m; if(!m){ m=document.createElement('div'); m.id='mpcBar'; m.setAttribute('role','toolbar'); m.setAttribute('aria-label','MPC controls'); m.addEventListener('click',onClick);
   m.innerHTML='<div class="mr"><button type="button" class="rec" data-m="rec" data-noul>● REC</button><button type="button" class="play" data-m="play" data-noul>▶ PLAY</button><button type="button" data-m="undo" data-noul>↶ UNDO</button><button type="button" data-m="clear" data-noul>🗑 CLEAR</button></div>'
    +'<div class="mr2"><div class="grp"><span class="lbl">Bars</span><button type="button" class="sm" data-m="bars" data-v="1" data-noul>1</button><button type="button" class="sm" data-m="bars" data-v="2" data-noul>2</button><button type="button" class="sm" data-m="bars" data-v="4" data-noul>4</button></div>'
    +'<div class="grp"><button type="button" class="sm" data-m="bpm" data-v="-5" aria-label="Slower" data-noul>−</button><span class="bpm" id="mpcBpm">90</span><button type="button" class="sm" data-m="bpm" data-v="5" aria-label="Faster" data-noul>+</button></div>'
    +'<button type="button" class="sm" data-m="click" title="Metronome click" data-noul>🔔 Click</button><button type="button" class="sm" data-m="q" title="Timing grid: where your hits land" data-noul>Q 1/16</button><span class="lcd" id="mpcPos">1 · 1</span></div>'; }
  g.parentElement.insertBefore(m,g); return m; }
 function paint(){ const m=build(); if(!m) return; const ps=PS(); const r=m.querySelector('[data-m="rec"]'), p=m.querySelector('[data-m="play"]');
  r.classList.toggle('on',recOn()); r.textContent=recOn()?'● REC ON':'● REC'; p.classList.toggle('on',!!ps.playing); p.textContent=ps.playing?'■ STOP':'▶ PLAY';
  const nb=ps.barsN; m.querySelectorAll('[data-m="bars"]').forEach(b=>b.classList.toggle('on',+b.dataset.v===nb));
  const bp=$('padBpm'); const bv=$('mpcBpm'); if(bp&&bv&&bv.textContent!==bp.value) bv.textContent=bp.value;
  const ck=m.querySelector('[data-m="click"]'); ck.classList.toggle('on',clickOn());
  const md=window.PADRECMODE||'step'; const q=m.querySelector('[data-m="q"]'); const ql='Q '+(QS.find(x=>x[0]===md)||QS[0])[1]; if(q.textContent!==ql) q.textContent=ql;
  const P=window.PADS||{}; const pos=$('mpcPos'); const spb=ps.spbN||16; const txt=P.playing&&P.step>=0?('Bar '+(Math.floor(P.step/spb)+1)+' · '+((Math.floor((P.step%spb)/(spb/4)))+1)):(nb+' bar'+(nb>1?'s':'')+' · '+(ps.bpm?ps.bpm():90)); if(pos.textContent!==txt) pos.textContent=txt; }
 function clearAll(){ const ps=PS(); clearedBackup=ps.pads.map(P=>({steps:P.steps.slice(),offs:P.offs?{...P.offs}:null})); ps.pads.forEach(P=>{ P.steps=P.steps.map(()=>0); if(P.offs) P.offs={}; }); try{ ps.refresh(); }catch(_){ } lastAct='clear'; say('🗑 Loop cleared: an empty '+ps.barsN+'-bar loop. ↶ UNDO brings it back.'); }
 function undo(){ const ps=PS(); if(lastAct==='clear'&&clearedBackup){ ps.pads.forEach((P,i)=>{ const b=clearedBackup[i]; if(b){ P.steps=b.steps; if(b.offs) P.offs=b.offs; } }); clearedBackup=null; lastAct=''; try{ ps.refresh(); }catch(_){ } return say('↶ The loop is back.'); } press('padUndo'); }
 function onClick(e){ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); const ps=PS(); const a=b.dataset.m;
  if(a==='rec'){ if(!recOn()){ if(!clickOn()) press('padClick'); lastAct='rec'; press('padRecLive'); if(!ps.playing) ps.play(); say('● Recording: play the pads, every hit lands in the loop.'); } else { press('padRecLive'); say('● Recording off: the loop keeps playing.'); } }
  else if(a==='play'){ if(ps.playing){ ps.stop(); if(recOn()) press('padRecLive'); } else ps.play(); }
  else if(a==='undo') undo();
  else if(a==='clear') clearAll();
  else if(a==='bars'){ ps.setBars(+b.dataset.v); say('🔁 '+b.dataset.v+'-bar loop.'); }
  else if(a==='bpm'){ const bp=$('padBpm'); if(bp){ bp.value=String(Math.max(40,Math.min(240,(+bp.value||90)+(+b.dataset.v)))); bp.dispatchEvent(new Event('input',{bubbles:true})); bp.dispatchEvent(new Event('change',{bubbles:true})); } }
  else if(a==='click') press('padClick');
  else if(a==='q'){ const md=window.PADRECMODE||'step'; const i=QS.findIndex(x=>x[0]===md); const nx=QS[(i+1)%QS.length][0]; window.PADRECMODE=nx; try{ localStorage.setItem('kanin-recmode',JSON.stringify(nx)); }catch(_){ } say('Timing grid: '+QS.find(x=>x[0]===nx)[1]+(nx==='live'?' (hits stay exactly where you played them)':'')); }
  paint(); }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')) paint(); },200);
 window.KMPC={paint,clearAll};
})();
