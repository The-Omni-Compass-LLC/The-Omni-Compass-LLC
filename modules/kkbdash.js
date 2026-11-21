(()=>{ /* 🎹 THE KEYBOARD'S OWN DASHBOARD (v225): the floating MIDI keyboard carries its controls inside its own box, like the pads:
   ● REC · ▶ PLAY / ■ STOP · ↶ UNDO · 🗑 CLEAR, then Octave − / +, the Sound, 1 · 2 · 4 BARS and the tempo; the keys sit right under it,
   the wheels and every other setting below. It drives the studio's own loop: what you play while REC is lit lands in the loop. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } }; const PS=()=>window.PADSTUDIO; const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const recOn=()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); };
 const css=document.createElement('style'); css.textContent=`
html body #kbTop.kFloat.kFOn{display:flex!important;flex-direction:column!important}
html body #kbTop.kFloat.kFOn > *{flex-shrink:0!important}
html body #kbTop.kFloat.kFOn > .kFHead{order:-10}html body #kbTop.kFloat.kFOn > #kbDash{order:-9}html body #kbTop.kFloat.kFOn > #kbKeys{order:-8}
html body #kbTop.kFloat.kFOn > h4{order:-7}html body #kbTop.kFloat.kFOn > #kbWheels{order:1}html body #kbTop.kFloat.kFOn > #mouseHint{order:3}html body #kbTop.kFloat.kFOn > .kgrid{order:2}html body #kbTop.kFloat.kFOn > #trBar{order:4}html body #kbTop.kFloat.kFOn > .ocSec{order:99}
#kbDash{display:flex;flex-direction:column;gap:5px;margin:2px 0 8px;padding:6px;border-radius:12px;background:linear-gradient(180deg,#22252e,#15171d);border:1px solid #3a3f4d}
#kbDash .mr{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:5px}
#kbDash .mr2{display:flex;gap:5px;align-items:center;overflow-x:auto;scrollbar-width:thin;padding-bottom:2px}
#kbDash button{min-height:44px!important;border-radius:10px!important;font:900 14px/1 system-ui,sans-serif!important;padding:0 6px!important;border:2px solid #444a5a!important;background:#2c303b!important;color:#f2f2f2!important;flex:none}
#kbDash button.rec{background:#5a0f18!important;border-color:#ff3b4f!important;color:#ffd0d6!important}#kbDash button.rec.on{background:#e0102e!important;color:#fff!important;animation:mpcBlink 1s steps(2) infinite}
#kbDash button.play{background:#123d22!important;border-color:#2ecc71!important}#kbDash button.play.on{background:#1f9d55!important}
#kbDash button.sm{min-height:40px!important;min-width:40px;font-size:13px!important}#kbDash button.sm.on{background:#ffe94a!important;color:#14163a!important;border-color:#ffe94a!important}
#kbDash select{min-height:40px;border-radius:10px;background:#2c303b;color:#fff;border:2px solid #444a5a;font:800 13px system-ui,sans-serif;max-width:150px;flex:none}
#kbDash .selw{display:inline-flex;align-items:center;gap:4px;flex:none;position:relative}#kbDash .selw > *{position:static!important;flex:none}
#kbDash .lbl{font:800 11px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.06em;text-transform:uppercase;flex:none}
#kbDash .oct{font:900 15px ui-monospace,monospace;color:#7cff8a;min-width:28px;text-align:center;flex:none}
@keyframes mpcBlink{50%{opacity:.55}}`; document.head.appendChild(css);
 function build(){ const top=$('kbTop'), keys=$('kbKeys'); if(!top||!keys||!PS()) return null; let d=$('kbDash'); if(d) return d; d=document.createElement('div'); d.id='kbDash'; d.setAttribute('role','toolbar'); d.setAttribute('aria-label','Keyboard controls'); d.addEventListener('click',onClick); d.addEventListener('change',onChange);
  const pre=$('kbPre'); const opts=pre?[...pre.options].map(o=>'<option value="'+o.value+'">'+o.textContent+'</option>').join(''):'';
  d.innerHTML='<div class="mr"><button type="button" class="rec" data-k="rec" data-noul>● REC</button><button type="button" class="play" data-k="play" data-noul>▶ PLAY</button><button type="button" data-k="undo" data-noul>↶ UNDO</button><button type="button" data-k="clear" data-noul>🗑 CLEAR</button></div>'
   +'<div class="mr2"><span class="lbl">Octave</span><button type="button" class="sm" data-k="octdn" aria-label="Octave down" data-noul>−</button><span class="oct" id="kbDashOct">C3</span><button type="button" class="sm" data-k="octup" aria-label="Octave up" data-noul>+</button>'
   +(opts?'<span class="selw"><select id="kbDashPre" aria-label="Sound" data-nodice="1">'+opts+'</select></span>':'')
   +'<span class="lbl">Bars</span><button type="button" class="sm" data-k="bars" data-v="1" data-noul>1</button><button type="button" class="sm" data-k="bars" data-v="2" data-noul>2</button><button type="button" class="sm" data-k="bars" data-v="4" data-noul>4</button>'
   +'<button type="button" class="sm" data-k="bpm" data-v="-5" aria-label="Slower" data-noul>−</button><span class="oct" id="kbDashBpm">90</span><button type="button" class="sm" data-k="bpm" data-v="5" aria-label="Faster" data-noul>+</button></div>';
  top.insertBefore(d,keys); return d; }
 function paint(){ const d=build(); if(!d) return; const ps=PS(); const r=d.querySelector('[data-k="rec"]'), p=d.querySelector('[data-k="play"]');
  r.classList.toggle('on',recOn()); const rt=recOn()?'● REC ON':'● REC'; if(r.textContent!==rt) r.textContent=rt; p.classList.toggle('on',!!ps.playing); const pt=ps.playing?'■ STOP':'▶ PLAY'; if(p.textContent!==pt) p.textContent=pt;
  d.querySelectorAll('[data-k="bars"]').forEach(b=>b.classList.toggle('on',+b.dataset.v===ps.barsN));
  const oc=$('kbOct'), od=$('kbDashOct'); if(oc&&od){ const t='C'+oc.value; if(od.textContent!==t) od.textContent=t; }
  const pre=$('kbPre'), dp=$('kbDashPre'); if(pre&&dp&&dp.value!==pre.value&&document.activeElement!==dp) dp.value=pre.value;
  const bp=$('padBpm'), bv=$('kbDashBpm'); if(bp&&bv&&bv.textContent!==bp.value) bv.textContent=bp.value; }
 const fire=(el,v)=>{ if(!el) return; el.value=String(v); el.dispatchEvent(new Event('input',{bubbles:true})); el.dispatchEvent(new Event('change',{bubbles:true})); };
 function onChange(e){ if(e.target.id==='kbDashPre') fire($('kbPre'),e.target.value); }
 function onClick(e){ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); const ps=PS(); const a=b.dataset.k;
  if(a==='rec'){ press('kbRec'); if(recOn()&&!ps.playing) ps.play(); say(recOn()?'● Recording the keys: play, every note lands in the loop.':'● Recording off: the loop keeps playing.'); }
  else if(a==='play'){ if(ps.playing){ ps.stop(); if(recOn()) press('kbRec'); } else ps.play(); }
  else if(a==='undo'){ press('kbUndo'); }
  else if(a==='clear'){ press('kbClear'); }
  else if(a==='octdn'||a==='octup'){ const oc=$('kbOct'); if(oc){ const v=Math.max(1,Math.min(6,(+oc.value||3)+(a==='octup'?1:-1))); if([...oc.options].some(o=>+o.value===v)) fire(oc,v); } }
  else if(a==='bars'){ ps.setBars(+b.dataset.v); }
  else if(a==='bpm'){ const bp=$('padBpm'); if(bp) fire(bp,Math.max(40,Math.min(240,(+bp.value||90)+(+b.dataset.v)))); }
  paint(); }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')) paint(); },250);
 window.KKBDASH={paint};
})();
