(()=>{ /* 🟢 EASY FOLDS THE BIG SCREENS (v245). On the Easy level a screen shows what a first-timer needs and folds the rest away, one tap
   from coming back:
   • THE STUDIO shows its transport bar, 🟢 Easy Studio and the floating devices (pads, keyboard, track sequencer). The deep sections
     open from one row in Easy Studio: 🎛 Channel rack · 🎚 Mixing board · 🔁 Loops · 🎼 Composer · 🎤 Vocals · ⚙ The whole studio.
   • THE KNOWLEDGE LIBRARY and VIDEO GAMES open with every section folded shut: tap a section's title to open it.
   • LONG ROWS OF CHIPS (genres, avatars, crafts) show the first 10 and a ＋ N more chip.
   Everyday and Pro show everything, as before. Nothing is removed: every folded button still works when shown, and keys still work. */
 const $=id=>document.getElementById(id); const easy=()=>document.documentElement.classList.contains('lvl-easy');
 const GROUPS={seq:['#crSec','#kSeqTabs','#kTrans','#pad .pin > .prow'],mixer:['#mxBanks','#kStudioHead','#kGovBoard','#kFXRet','#padMixer','#kDjStrips','#kIO','#pad .pin > h4','#pad .pin > p.pnote'],loops:['#kLoops'],composer:['#cmpWrap','#kLockBeat'],vocals:['#vocSec']};
 const LABEL={seq:'🎛 Channel rack',mixer:'🎚 Mixing board',loops:'🔁 Loops',composer:'🎼 Composer',vocals:'🎤 Vocals'};
 let shown=new Set(), all=false;
 const css=document.createElement('style'); css.textContent=`
html.lvl-easy #pad [data-ezg]:not(.kEzShow){display:none!important}
html.lvl-easy :is(#knList,#kVG .vgIn) > details:not([open]) > :not(summary){display:none!important}
html.lvl-easy :is(#knList,#kVG .vgIn) > details > summary{cursor:pointer;min-height:44px;display:flex;align-items:center}
.kEzRow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:12px}
.kEzRow b{font:800 clamp(14px,1.2vw,22px) system-ui,sans-serif;color:#bfb8ff;margin-right:4px}
.kEzRow button{min-height:48px!important;padding:4px 16px!important;border-radius:999px!important;font:800 clamp(14px,1.15vw,22px) system-ui,sans-serif!important;background:#2a2470!important;color:#fff!important;border:2px solid rgba(255,255,255,.25)!important}
.kEzRow button.on{background:#ffe94a!important;color:#14163a!important}
html.lvl-easy [data-ezc] > [data-ezx]:not(.kEzKeep){display:none!important}
html.lvl-easy [data-ezc].kEzOpen > [data-ezx]{display:inline-flex!important}
.kEzMoreChip{display:none}
html.lvl-easy .kEzMoreChip{display:inline-flex;align-items:center;justify-content:center;min-height:36px;padding:0 14px;border-radius:999px;font:800 13px system-ui,sans-serif;background:#ffe94a!important;color:#14163a!important}`; document.head.appendChild(css);
 /* the studio */
 function tagStudio(){ Object.entries(GROUPS).forEach(([g,sels])=>sels.forEach(s=>document.querySelectorAll(s).forEach(el=>{ if(el.dataset.ezg!==g) el.dataset.ezg=g; el.classList.toggle('kEzShow',all||shown.has(g)); })));
  const ez=$('kEasyStudio'); if(!ez) return; let row=ez.querySelector(':scope > .kEzRow'); if(!row){ row=document.createElement('div'); row.className='kEzRow'; row.innerHTML='<b>More of the studio:</b>'+Object.keys(LABEL).map(g=>'<button type="button" data-ezs="'+g+'" data-noul>'+LABEL[g]+'</button>').join('')+'<button type="button" data-ezs="all" data-noul>⚙ The whole studio</button>';
   const more=ez.querySelector('.ezMore'); if(more) ez.insertBefore(row,more); else ez.appendChild(row);
   row.addEventListener('click',e=>{ const b=e.target.closest('[data-ezs]'); if(!b) return; e.preventDefault(); e.stopPropagation(); show(b.dataset.ezs,true); }); }
  row.querySelectorAll('[data-ezs]').forEach(b=>b.classList.toggle('on',b.dataset.ezs==='all'?all:shown.has(b.dataset.ezs))); }
 function show(g,toggle){ if(g==='all'){ all=toggle?!all:true; } else { if(toggle&&shown.has(g)) shown.delete(g); else shown.add(g); } tagStudio();
  if(g!=='all'&&shown.has(g)){ const first=document.querySelector('#pad [data-ezg="'+g+'"].kEzShow'); if(first) setTimeout(()=>first.scrollIntoView({block:'start',behavior:'smooth'}),60); } }
 /* other places that send you to the mixing board open it first */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('[data-sq="mix"],[data-kd="mix"],[data-io],#kStudioHead [data-bank]'); if(b) show('mixer'); },true);
 /* the knowledge library and video games: sections start folded */
 const FOLD=[['kKnow','#knList > details'],['kVG','.vgIn > details']]; const folded=new WeakSet();
 function foldDetails(){ if(!easy()) return; FOLD.forEach(([id,sel])=>{ const root=$(id); if(!root||root.hidden||!root.getClientRects().length) return; root.querySelectorAll(sel).forEach(d=>{ if(!folded.has(d)){ folded.add(d); d.open=false; } }); }); }
 /* long rows of chips: the first 10 and ＋ N more */
 const CHIPS='.soGrid,.soChips,.crChips,#mGenres,.mGenres';
 function chips(){ document.querySelectorAll(CHIPS).forEach(c=>{ const kids=[...c.children].filter(x=>x.tagName==='BUTTON'&&!x.classList.contains('kEzMoreChip')); if(kids.length<=14){ c.removeAttribute('data-ezc'); kids.forEach(x=>x.removeAttribute('data-ezx')); const m=c.querySelector(':scope > .kEzMoreChip'); if(m) m.remove(); return; }
   c.dataset.ezc='1'; kids.forEach((x,i)=>{ if(i>=10){ if(!x.hasAttribute('data-ezx')) x.setAttribute('data-ezx',''); x.classList.toggle('kEzKeep',x.classList.contains('on')||x.getAttribute('aria-pressed')==='true'); } else x.removeAttribute('data-ezx'); });
   let m=c.querySelector(':scope > .kEzMoreChip'); if(!m){ m=document.createElement('button'); m.type='button'; m.className='kEzMoreChip'; m.setAttribute('data-noul',''); m.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); c.classList.toggle('kEzOpen'); chips(); }); }
   if(m!==c.lastElementChild) c.appendChild(m); const t=c.classList.contains('kEzOpen')?'− Fewer':'＋ '+(kids.length-10)+' more'; if(m.textContent!==t) m.textContent=t; }); }
 setInterval(()=>{ tagStudio(); foldDetails(); chips(); },1200);
 window.KFOLD={show,get shown(){ return [...shown]; },get all(){ return all; }};
})();
