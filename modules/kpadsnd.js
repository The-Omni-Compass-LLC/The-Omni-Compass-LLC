(()=>{ /* 🗂 EVERY SOUND FROM EVERY SOUND LIST (v254). No sound list in the studio stops at kick, snare, hat and cowbell:
   • 🥁 THE PAD'S "Sound" LIST opens with "🗂 Every sound…" and carries all 138 Studio sounds by group (kicks, snares, claps, hats,
     cymbals, percussion, world percussion, 808s and bass, tones and stabs, synth leads and keys, FX, foley) beside the built-in kit.
   • 🗂 EVERY SOUND opens one picker over the studio: category → group or instrument → sound, ▶ to hear, → Pad to load. It reaches
     every sound in KAN-IN: the Studio groups, 7,417 recorded instruments (VCSL and VSCO, free to use) and 18 built-in instruments.
   • 🎹 THE KEYBOARD'S instrument list opens the same picker for the keys (any sound played across the keys, in tune).
   • 🎛 THE STEP SEQUENCER'S "Add a sound" list adds a row with any sound, and "🗂 Row sound" changes the sound of the row selected.
   Whatever is loaded goes through the same channel, mixing board, record, stop and undo as every other sound. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const PS=()=>window.PADSTUDIO; const KB=()=>window.KBROWSE;
 const lab=i=>'ABCD'[Math.floor(i/16)]+(i%16+1);
 const ALL='__all';
 const css=document.createElement('style'); css.textContent=`
#kSndSheet{position:fixed;z-index:9760;left:50%;top:calc(60px + env(safe-area-inset-top,0px));transform:translateX(-50%);width:min(720px,calc(100vw - var(--kRailW,58px) - 20px));max-height:calc(100vh - 90px);display:flex;flex-direction:column;background:linear-gradient(160deg,#151a33,#0a0d1c);border:1px solid rgba(127,255,255,.45);border-radius:6px 18px 6px 18px;box-shadow:0 18px 50px rgba(0,0,0,.6);color:#eef;font:14px/1.4 system-ui,sans-serif;overflow:hidden}
#kSndSheet[hidden]{display:none!important}
#kSndSheet .ssTop{display:flex;align-items:center;gap:8px;padding:8px 10px;background:rgba(127,255,255,.08);border-bottom:1px solid rgba(127,255,255,.25)}
#kSndSheet .ssTop b{flex:1;min-width:0;font:900 15px system-ui,sans-serif;color:#7ff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#kSndSheet .ssTop button{min-height:40px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 13px system-ui,sans-serif}
#kSndSheet .ssBody{overflow:auto;padding:8px 10px 12px}
#kSndSheet .ssBody .kBrowse .bwGrid{max-height:none}
#kSndSheet .ssBody .kBrowse .bwList{max-height:46vh}
#kSndSheet .ssNote{font-size:12px;opacity:.8;padding:0 10px 10px}
.kSndEvery{min-height:36px;padding:0 10px;border-radius:3px 10px 3px 10px;font:800 12.5px system-ui,sans-serif;background:#1f6f8b!important;color:#fff!important;margin-left:4px}`; document.head.appendChild(css);
 /* the one picker */
 let mode='pads', after=null;
 function sheet(){ let d=$('kSndSheet'); if(d) return d; d=document.createElement('div'); d.id='kSndSheet'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Every sound');
  d.innerHTML='<div class="ssTop"><b>🗂 Every sound</b><button type="button" data-ss="x" data-noul>✕ Close</button></div><div class="ssBody"><div data-ssb="pads"></div><div data-ssb="keys" hidden></div></div><div class="ssNote">Category → group or instrument → sound. ▶ hears it, → Pad loads it, 🎹 Keys plays it across the keyboard. Your own sounds: ⬆ UPLOAD or ● record on the pad.</div>';
  document.body.appendChild(d); d.addEventListener('click',e=>{ if(e.target.closest('[data-ss="x"]')){ e.stopPropagation(); close(); } });
  try{ KB().mount(d.querySelector('[data-ssb="pads"]'),'pads'); KB().mount(d.querySelector('[data-ssb="keys"]'),'keys'); }catch(_){ } return d; }
 function open(m,target,title,cb){ const d=sheet(); mode=m; after=cb||null; try{ KB().target=(m==='pads'&&target!=null)?target:null; }catch(_){ }
  d.querySelector('[data-ssb="pads"]').hidden=m!=='pads'; d.querySelector('[data-ssb="keys"]').hidden=m!=='keys';
  d.querySelector('.ssTop b').textContent='🗂 Every sound · '+(title||(m==='keys'?'for the keyboard':'for the pad')); d.hidden=false; }
 function close(){ const d=$('kSndSheet'); if(d) d.hidden=true; after=null; try{ KB().target=null; }catch(_){ } }
 const hook=()=>{ try{ if(KB()&&!KB().__ss){ KB().__ss=1; KB().onPad=(i,it)=>{ const f=after; if(f){ after=null; try{ f(i,it); }catch(_){ } } }; } }catch(_){ } };
 const selPad=()=>{ const s=document.querySelector('#padGrid .pd.sel'); if(s) return +s.dataset.i; const b=$('padBank'); return (Math.max(0,Math.min(3,+(b&&b.value)||0)))*16; };
 /* 🥁 the pad's Sound list: every Studio sound, grouped, and the whole picker */
 function fillPad(){ const s=$('padSound'); if(!s||s.querySelector('option[value="'+ALL+'"]')) return; let L=[]; try{ L=SNDLIB.items||[]; }catch(_){ }
  const cur=s.value; const built=[...s.options].filter(o=>o.value!=='u'); const up=[...s.options].find(o=>o.value==='u');
  const top=document.createElement('option'); top.value=ALL; top.textContent='🗂 Every sound: 10 categories, 7,500+ sounds…';
  const g0=document.createElement('optgroup'); g0.label='🥁 Built-in kit and instruments'; built.forEach(o=>g0.appendChild(o));
  s.innerHTML=''; s.appendChild(top); s.appendChild(g0);
  const cats=[...new Set(L.map(x=>x.cat))]; cats.forEach(c=>{ const g=document.createElement('optgroup'); g.label='🎛 '+c; L.forEach((x,k)=>{ if(x.cat!==c) return; const o=document.createElement('option'); o.value='lib:'+k; o.textContent=x.name; g.appendChild(o); }); s.appendChild(g); });
  const gu=document.createElement('optgroup'); gu.label='📁 Your own'; if(up) gu.appendChild(up); s.appendChild(gu);
  const bot=document.createElement('option'); bot.value=ALL; bot.textContent='🗂 More: every recorded instrument…'; gu.appendChild(bot);
  try{ s.value=cur; }catch(_){ } s.title='Pick any sound for the selected pad: the kit, 138 Studio sounds by group, your own, or 🗂 every sound';
  const lb=s.closest('label'); if(lb&&!lb.parentElement.querySelector('.kSndEvery')){ const b=document.createElement('button'); b.type='button'; b.className='kSndEvery'; b.setAttribute('data-noul',''); b.textContent='🗂 Every sound'; b.title='Browse every sound for the selected pad'; b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); const i=selPad(); open('pads',i,'for pad '+lab(i)); },true); lb.insertAdjacentElement('afterend',b); } }
 async function libToPad(k){ const P=PS(); let it=null; try{ it=SNDLIB.items[k]; }catch(_){ } if(!P||!it) return; const i=selPad(); const pd=P.pads[i]; if(!pd) return;
  const old={buf:pd.buf,rbuf:pd.rbuf,snd:pd.snd,name:pd.name,trim:pd.trim,cut:pd.cut,kLibV:pd.kLibV}; let buf=null; try{ buf=await SNDLIB.render(it); }catch(_){ } if(!buf) return say('That sound did not load. Try another.');
  P.setBuf(i,buf,String(it.name).slice(0,18),true); pd.kLibV='lib:'+k; try{ P.refresh(); }catch(_){ } try{ P.hitPad(i); }catch(_){ } say('🥁 Pad '+lab(i)+' now plays '+it.name+' ('+it.cat+').');
  try{ KUNDO.push(()=>{ Object.assign(P.pads[i],old); try{ P.refresh(); }catch(_){ } },'the pad sound'); }catch(_){ } }
 /* 🎹 the keyboard's instrument list */
 function fillKeys(){ const s=$('kbPre'); if(!s||s.querySelector('option[value="'+ALL+'"]')) return; if(!s.dataset.prev) s.dataset.prev=s.value; const o=document.createElement('option'); o.value=ALL; o.textContent='🗂 Every sound on the keys: 7,500+…'; s.insertBefore(o,s.firstChild); try{ if(s.value===ALL) s.selectedIndex=1; }catch(_){ } }
 /* 🎛 the step sequencer's Add a sound list, and the selected row's sound */
 function fillRack(){ const s=$('crAdd'); if(s&&!s.querySelector('option[value="'+ALL+'"]')){ const o=document.createElement('option'); o.value=ALL; o.textContent='🗂 Add a row with any sound (7,500+)…'; s.insertBefore(o,s.options[1]||null); }
  const bar=s&&s.closest('.crBar'); if(bar&&!bar.querySelector('[data-ssrow]')){ const b=document.createElement('button'); b.type='button'; b.dataset.ssrow='1'; b.className='kSndEvery'; b.setAttribute('data-noul',''); b.textContent='🗂 Row sound'; b.title='Change the sound of the selected row to any sound';
   b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); const m=(($('crVelL')||{}).textContent||'').match(/([ABCD])(\d{1,2})\b/); const i=m?'ABCD'.indexOf(m[1])*16+(+m[2]-1):selPad(); open('pads',i,'for row '+lab(i)); },true); s.insertAdjacentElement('afterend',b); } }
 function freePad(){ const s=$('crAdd'); const v=s?[...s.options].map(o=>o.value).filter(x=>/^\d+$/.test(x)).map(Number):[]; return v.length?v[v.length-1]:63; }
 /* one listener for all three, ahead of each list's own */
 document.addEventListener('change',e=>{ const t=e.target; if(!t||!t.id) return; const v=t.value;
  if(t.id==='padSound'&&(v===ALL||v.startsWith('lib:'))){ e.stopImmediatePropagation(); const P=PS(), i=selPad(), pd=P&&P.pads[i]; try{ t.value=pd?(pd.snd==='u'?(pd.kLibV||'u'):pd.snd):''; }catch(_){ } if(v===ALL) open('pads',i,'for pad '+lab(i)); else libToPad(+v.slice(4)); return; }
  if(t.id==='padSound'){ const P=PS(), pd=P&&P.pads[selPad()]; if(pd) pd.kLibV=null; }
  if(t.id==='kbPre'&&v===ALL){ e.stopImmediatePropagation(); try{ const pv=t.dataset.prev; t.value=(pv&&[...t.options].some(o=>o.value===pv))?pv:t.options[1].value; }catch(_){ } open('keys',null,'for the keyboard'); return; }
  if(t.id==='kbPre') t.dataset.prev=v;
  if(t.id==='crAdd'&&v===ALL){ e.stopImmediatePropagation(); t.value=''; const i=freePad(); open('pads',i,'a new row on pad '+lab(i),(j)=>{ const s=$('crAdd'); if(s&&[...s.options].some(o=>o.value===String(j))){ s.value=String(j); s.dispatchEvent(new Event('change',{bubbles:true})); } say('🎛 A new row plays it: '+lab(j)+'.'); }); return; } },true);
 /* the pad's list shows the Studio sound it plays */
 function showCur(){ const s=$('padSound'); if(!s||document.activeElement===s) return; const P=PS(); const pd=P&&P.pads[selPad()]; if(pd&&pd.snd==='u'&&pd.kLibV&&s.value!==pd.kLibV) try{ s.value=pd.kLibV; }catch(_){ } }
 setInterval(()=>{ hook(); fillPad(); fillKeys(); fillRack(); showCur(); },700);
 window.KSNDPICK={open,close,fill:()=>{ fillPad(); fillKeys(); fillRack(); }};
})();
