(()=>{ /* ✏️ SEQUENCER EDIT TOOLS (v209): the channel rack edits like a production program. Tools: ✏️ Draw (tap or drag to draw hits),
   🧽 Erase (tap or drag to rub them out), 🔲 Select (drag a block of steps across rows), 🎚 Velocity (tap a hit to make it softer),
   📌 Paste (tap where the copied block starts). On the block (or the whole bar when nothing is picked): ✂ Cut, 📋 Copy, ⧉ Duplicate,
   🗑 Delete, ◀ ▶ Nudge, ⇄ Reverse, ▦ Select all. Every edit can be taken back with ↶ Undo, one move at a time, back to the last save.
   Keys: Ctrl/⌘ + C, X, V, D, and Delete. MIDI keyboards and pads play into it through 🎚 Inputs. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const spb=()=>PS().spbN, total=()=>PS().spbN*PS().barsN; const pg=()=>{ try{ return CRACK.state.page||0; }catch(_){ return 0; } };
 let open=false, tool='draw', sel=null, clip=null, drag=null, eatClick=false;
 const TOOLS=[['draw','✏️','Draw','Tap or drag across the steps to draw hits.'],['erase','🧽','Erase','Tap or drag across the steps to rub hits out.'],['select','🔲','Select','Drag from one step to another to pick a block, across as many rows as you like.'],['vel','🎚','Velocity','Tap a hit to make it softer: full, ¾, ½, ¼, then full again.'],['paste','📌','Paste','Tap the step where the copied block should start.']];
 const ACTS=[['cut','✂','Cut'],['copy','📋','Copy'],['dup','⧉','Duplicate'],['del','🗑','Delete'],['left','◀','Nudge'],['right','▶','Nudge'],['rev','⇄','Reverse'],['all','▦','Select all'],['none','⬚','Unselect'],['undo','↶','Undo'],['how','❓','How']];
 const css=document.createElement('style'); css.textContent=`
#kSeqTools{margin:6px 0;padding:6px 8px;border:1px dashed rgba(255,233,74,.65);border-radius:12px;background:rgba(22,18,64,.75);color:#fff}
#kSeqTools .stHead{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
#kSeqTools .stHead>b{font:800 clamp(12px,1vw,18px) system-ui,sans-serif;color:#ffe94a;letter-spacing:.04em}
#kSeqTools button{min-height:40px;border-radius:10px;padding:4px 10px!important;font:700 clamp(12.5px,.95vw,19px)/1.2 system-ui,sans-serif;white-space:normal;max-width:100%}
#kSeqTools button.on{background:#ffe94a!important;color:#14163a!important}
#kSeqTools .stRow{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
#kSeqTools .stInfo{font:600 clamp(12.5px,.95vw,18px)/1.45 system-ui,sans-serif;color:#d6d0ff;margin-top:6px;overflow-wrap:anywhere}
#kSeqTools:not(.open) .stRow,#kSeqTools:not(.open) .stInfo{display:none}
#crSec.kTools .crSteps{touch-action:none}
#crSec.kTools[data-tool="erase"] .crS,#crSec.kTools[data-tool="paste"] .crS{cursor:crosshair}
#crSec.kTools[data-tool="select"] .crS{cursor:cell}
#crRows .crS.kSel{outline:2px solid #ffe94a;outline-offset:-2px;box-shadow:inset 0 0 0 99px rgba(255,233,74,.28)}`; document.head.appendChild(css);
 const rowsShown=()=>[...document.querySelectorAll('#crRows .crRow')].map(r=>+r.dataset.i);
 const at=(x,y)=>{ const e=document.elementFromPoint(x,y); const b=e&&e.closest&&e.closest('#crRows .crS'); if(!b) return null; const r=b.closest('.crRow'); return {b,i:+r.dataset.i,s:pg()*spb()+ +b.dataset.s}; };
 const snap=()=>PS().pads.map(p=>Array.from(p.steps));
 function remember(name){ const S=snap(); try{ KUNDO.push(()=>{ PS().pads.forEach((p,i)=>{ if(S[i]) p.steps=S[i].slice(); }); redraw(); },name); }catch(_){ } }
 function redraw(){ try{ CRACK.render(); }catch(_){ } try{ PS().refresh(); }catch(_){ } mark(); info(); }
 const block=()=>{ if(sel) return sel; const n=spb(), o=pg()*n; return {rows:rowsShown(),a:o,b:o+n-1,whole:true}; };
 function grow(to){ let g=0; while(to>total()&&PS().barsN<16&&g<5){ try{ PS().setBars(PS().barsN*2); }catch(_){ break; } g++; } }
 const ACT={
  copy:(q)=>{ const B=block(); clip={len:B.b-B.a+1,rows:B.rows.map(i=>({i,v:Array.from(PS().pads[i].steps.slice(B.a,B.b+1))}))}; if(!q) say('📋 Copied '+clip.len+' steps on '+clip.rows.length+' rows. Pick 📌 Paste and tap where it goes.'); },
  cut:()=>{ ACT.copy(true); remember('Cut'); const B=block(); B.rows.forEach(i=>{ for(let s=B.a;s<=B.b;s++) PS().pads[i].steps[s]=0; }); redraw(); say('✂ Cut. Pick 📌 Paste and tap where it goes.'); },
  del:()=>{ remember('Delete'); const B=block(); B.rows.forEach(i=>{ for(let s=B.a;s<=B.b;s++) PS().pads[i].steps[s]=0; }); redraw(); say('🗑 Deleted.'); },
  dup:()=>{ const B=block(); const len=B.b-B.a+1; remember('Duplicate'); grow(B.b+1+len); B.rows.forEach(i=>{ const st=PS().pads[i].steps; for(let k=0;k<len;k++){ const t=B.b+1+k; if(t<total()) st[t]=st[B.a+k]; } }); if(sel) sel={rows:B.rows,a:B.b+1,b:Math.min(total()-1,B.b+len)}; redraw(); say('⧉ Duplicated right after itself.'+(B.b+1>=pg()*spb()+spb()?' Turn the page to see it.':'')); },
  left:()=>rot(-1), right:()=>rot(1),
  rev:()=>{ const B=block(); remember('Reverse'); B.rows.forEach(i=>{ const st=PS().pads[i].steps; const seg=Array.from(st.slice(B.a,B.b+1)).reverse(); seg.forEach((v,k)=>st[B.a+k]=v); }); redraw(); say('⇄ Reversed.'); },
  all:()=>{ sel={rows:rowsShown(),a:0,b:total()-1}; mark(); info(); say('▦ Everything is picked.'); },
  none:()=>{ sel=null; mark(); info(); },
  undo:()=>{ try{ KUNDO.any(); }catch(_){ } },
  how:()=>say('Pick a tool, then use it on the steps. 🔲 Select a block, then ✂ Cut, 📋 Copy, ⧉ Duplicate, 🗑 Delete, ◀ ▶ Nudge or ⇄ Reverse it. 📌 Paste puts the copy where you tap. ↶ Undo takes back the last move.')};
 function rot(d){ const B=block(); remember(d<0?'Nudge left':'Nudge right'); B.rows.forEach(i=>{ const st=PS().pads[i].steps; const seg=Array.from(st.slice(B.a,B.b+1)); const n=seg.length; seg.forEach((v,k)=>st[B.a+((k+d)%n+n)%n]=v); }); redraw(); }
 function paste(i0,s0){ if(!clip) return say('Copy or cut a block first.'); remember('Paste'); grow(s0+clip.len); clip.rows.forEach(r=>{ const st=PS().pads[r.i].steps; r.v.forEach((v,k)=>{ const t=s0+k; if(t<total()) st[t]=v; }); }); sel={rows:clip.rows.map(r=>r.i),a:s0,b:Math.min(total()-1,s0+clip.len-1)}; redraw(); say('📌 Pasted.'); }
 function mark(){ document.querySelectorAll('#crRows .crS').forEach(b=>{ let on=false; if(sel){ const r=b.closest('.crRow'); const i=+r.dataset.i, s=pg()*spb()+ +b.dataset.s; on=sel.rows.includes(i)&&s>=sel.a&&s<=sel.b; } if(b.classList.contains('kSel')!==on) b.classList.toggle('kSel',on); }); }
 function info(){ const e=document.querySelector('#kSeqTools .stInfo'); if(!e) return; const T=TOOLS.find(t=>t[0]===tool); e.textContent='Tool: '+T[1]+' '+T[2]+' · '+T[3]+' · Picked: '+(sel?(sel.b-sel.a+1)+' steps on '+sel.rows.length+' rows':'nothing (actions use this bar)')+' · Copied: '+(clip?clip.len+' steps':'nothing'); }
 function paint(){ const box=$('kSeqTools'); if(!box) return; box.classList.toggle('open',open); const sec=$('crSec'); if(sec){ sec.classList.toggle('kTools',open); sec.dataset.tool=tool; }
  box.querySelectorAll('[data-st]').forEach(b=>b.classList.toggle('on',b.dataset.st===tool)); const h=box.querySelector('[data-sx="open"]'); if(h){ h.classList.toggle('on',open); h.setAttribute('aria-expanded',open); } info(); }
 /* the floating 16 pads shrink to their title bar while editing, so every step can be reached; 🥁 Pads brings them back */
 function clearView(){ try{ if(KRAIL.FLOAT.isOpen('pads')){ const f=document.querySelector('.pmain.kFOn:not(.kMin) > .kFHead [data-fh="min"]'); if(f){ f.click(); say('🥁 The pads shrank so you can reach every step. Tap 🥁 Pads to bring them back.'); } } }catch(_){ } }
 function build(){ const rows=$('crRows'); if(!rows||$('kSeqTools')) return; const box=document.createElement('div'); box.id='kSeqTools';
  box.innerHTML='<div class="stHead"><button type="button" data-sx="open" data-noul aria-expanded="false" title="Open the editing tools">✏️ Edit tools</button><b>Draw · Erase · Select · Cut · Copy · Paste · Undo</b></div>'
   +'<div class="stRow" role="radiogroup" aria-label="Editing tool">'+TOOLS.map(t=>'<button type="button" data-st="'+t[0]+'" title="'+t[3]+'" data-noul>'+t[1]+' '+t[2]+'</button>').join('')+'</div>'
   +'<div class="stRow">'+ACTS.map(a=>'<button type="button" data-sa="'+a[0]+'" title="'+a[2]+'" data-noul>'+a[1]+' '+a[2]+'</button>').join('')+'</div><div class="stInfo" aria-live="polite"></div>';
  rows.insertAdjacentElement('beforebegin',box);
  box.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); if(b.dataset.sx==='open'){ open=!open; if(!open){ tool='draw'; } else clearView(); paint(); return; } if(b.dataset.st){ tool=b.dataset.st; if(!open) clearView(); open=true; paint(); say(TOOLS.find(t=>t[0]===tool).slice(1).join(' ')); return; } const f=ACT[b.dataset.sa]; if(f) f(); });
  paint(); }
 /* the gestures on the steps */
 document.addEventListener('pointerdown',e=>{ const h=e.target.closest&&e.target.closest('#crRows .crS'); if(!h||!open) return; const p=at(e.clientX,e.clientY); if(!p) return;
  if(tool==='draw'||tool==='erase'){ e.preventDefault(); const st=PS().pads[p.i].steps; const val=tool==='erase'?0:(st[p.s]?0:1); drag={kind:'paint',val,before:snap(),hit:false}; st[p.s]=val; drag.hit=true; if(val&&!PS().playing) try{ PS().hitPad(p.i); }catch(_){ } p.b.classList.toggle('on',!!val); eatClick=true; }
  else if(tool==='select'){ e.preventDefault(); drag={kind:'sel',a:p}; sel={rows:[p.i],a:p.s,b:p.s}; mark(); eatClick=true; } },true);
 document.addEventListener('pointermove',e=>{ if(!drag) return; const p=at(e.clientX,e.clientY); if(!p) return;
  if(drag.kind==='paint'){ const st=PS().pads[p.i].steps; if((st[p.s]?1:0)!==drag.val){ st[p.s]=drag.val; p.b.classList.toggle('on',!!drag.val); } }
  else { const R=rowsShown(); const ia=R.indexOf(drag.a.i), ib=R.indexOf(p.i); const r0=Math.min(ia,ib), r1=Math.max(ia,ib); sel={rows:R.slice(r0,r1+1),a:Math.min(drag.a.s,p.s),b:Math.max(drag.a.s,p.s)}; mark(); } },true);
 const up=()=>{ if(!drag) return; const d=drag; drag=null; setTimeout(()=>{ eatClick=false; },0); if(d.kind==='paint'){ const S=d.before; try{ KUNDO.push(()=>{ PS().pads.forEach((p,i)=>{ if(S[i]) p.steps=S[i].slice(); }); redraw(); },tool==='erase'?'Erase':'Draw'); }catch(_){ } redraw(); } else { info(); } };
 document.addEventListener('pointerup',up,true); document.addEventListener('pointercancel',up,true);
 document.addEventListener('click',e=>{ const h=e.target.closest&&e.target.closest('#crRows .crS'); if(!h) return;
  if(eatClick){ eatClick=false; e.stopPropagation(); e.preventDefault(); return; }
  if(!open||tool==='draw'){ remember('Step'); return; } /* the rack's own tap toggles the step; it can be undone */
  e.stopPropagation(); e.preventDefault(); const p=at(e.clientX,e.clientY)||(()=>{ const r=h.closest('.crRow'); return {i:+r.dataset.i,s:pg()*spb()+ +h.dataset.s}; })();
  if(tool==='erase'){ remember('Erase'); PS().pads[p.i].steps[p.s]=0; redraw(); }
  else if(tool==='vel'){ remember('Velocity'); const st=PS().pads[p.i].steps; const v=st[p.s]||0; const n=!v?1:v>.8?.75:v>.6?.5:v>.3?.25:1; st[p.s]=n; redraw(); say('🎚 '+Math.round(n*100)+'%'); }
  else if(tool==='paste') paste(p.i,p.s); },true);
 document.addEventListener('keydown',e=>{ if(!$('kSeqTools')) return; let id='home'; try{ id=KRAIL.cur(); }catch(_){ } if(id!=='pad') return; const t=e.target; if(t&&(t.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
  const k=(e.key||'').toLowerCase(); const mod=e.ctrlKey||e.metaKey; let f=null;
  if(mod&&k==='c') f=()=>ACT.copy(); else if(mod&&k==='x') f=ACT.cut; else if(mod&&k==='d') f=ACT.dup; else if(mod&&k==='v') f=()=>paste(0,sel?sel.a:pg()*spb()); else if(!mod&&(k==='delete'||k==='backspace')&&sel) f=ACT.del;
  if(f){ e.preventDefault(); e.stopPropagation(); f(); } },true);
 setInterval(()=>{ build(); if(sel||document.querySelector('#crRows .crS.kSel')) mark(); },300);
 window.KSEQTOOLS={act:ACT,get tool(){ return tool; },setTool:t=>{ tool=t; open=true; paint(); },open:()=>{ open=true; paint(); },get sel(){ return sel; },get clip(){ return clip; }};
})();
