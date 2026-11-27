(()=>{ /* ⌨ YOUR COMPUTER KEYS, STRAIGHT AND TRUE (v240). Any standard laptop or desktop keyboard, nothing special:
   🥁 The 16 pads are the 4 × 4 block on the left of the keyboard, laid out on screen exactly as the keys sit:
        1 2 3 4  /  Q W E R  /  A S D F  /  Z X C V      (the pads are always 4 across, so each pad is where its key is).
   🎹 The piano is the two letter rows, the way music programs use a typing keyboard:
        lower octave: Z X C V B N M are the white keys, S D G H J the black keys;
        upper octave: Q W E R T Y U I are the white keys, 2 3 5 6 7 the black keys.   Every piano key shows its letter.
   Your keys play ONE device at a time: the one you touched last (or the only one open). Each window says so in big words, and one
   tap switches. Space plays and stops. The extra controls of each device fold behind ⚙ More, so each window shows only the essentials. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PADK='1234qwerasdfzxcv', KMAP='y7u8io0p-[=]\\'; /* v245 split keyboard: the piano is on the right hand */
 let owner=getLS('kanin-keyowner','pads'); const was={pads:false,keys:false}; let more=getLS('kanin-devmore',{pads:false,keys:false}); if(!more||typeof more!=='object') more={pads:false,keys:false};
 const physical=()=>{ try{ return matchMedia('(hover:hover) and (pointer:fine)').matches||window.INPUTMODE==='keys'||window.INPUTMODE==='both'&&!matchMedia('(pointer:coarse)').matches; }catch(_){ return true; } };
 const css=document.createElement('style'); css.textContent=`
html body #padGrid{grid-template-columns:repeat(4,minmax(0,1fr))!important}
.kKeyOwn{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 6px;padding:6px 10px;border-radius:12px;font:900 14px system-ui,sans-serif;background:#2a2d38;color:#c9cede;border:2px dashed #555b6e;cursor:pointer}
.kKeyOwn b{font-size:15px;color:#fff}
.kKeyOwn small{font:700 12px system-ui,sans-serif;color:#aab}
.kKeyOwn.on{background:#ffe94a;color:#14163a;border:2px solid #fff;cursor:default}
.kKeyOwn.on b{color:#14163a}.kKeyOwn.on small{color:#3b3500}
.kKeyOwn button{margin-left:auto;min-height:34px!important;border-radius:10px!important;padding:0 10px!important;font:800 12.5px system-ui,sans-serif!important}
.kKeyOwn[hidden]{display:none!important}
#kbKeys .kKL{position:absolute;left:50%;transform:translateX(-50%);bottom:22px;font:900 12px ui-monospace,monospace;pointer-events:none;padding:1px 4px;border-radius:5px;background:#ffe94a;color:#14163a;line-height:1.2}
#kbKeys .kKL.blk{bottom:8px;background:#ff9de2}
#kbKeys:not(.kKLon) .kKL{display:none}
.kLess .kMoreOnly{display:none!important}
.kMoreBtn{min-height:36px!important;border-radius:10px!important;padding:0 10px!important;font:800 12.5px system-ui,sans-serif!important;background:#33384a!important}
.kMoreBtn.on{background:#ffe94a!important;color:#14163a!important}`; document.head.appendChild(css);
 const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const isOpen=k=>{ const f=F(); try{ return !!(f&&f.isOpen(k)); }catch(_){ return false; } };
 function setOwner(k,quiet){ if(k!=='pads'&&k!=='keys') return; const ch=owner!==k; owner=k; putLS('kanin-keyowner',k); apply(); if(ch&&!quiet&&physical()) say(k==='keys'?'🎹 Your keys now play the PIANO: Z X C V B N M and Q W E R T Y U I, black keys on S D G H J and 2 3 5 6 7.':'🥁 Your keys now play the PADS: 1 2 3 4 · Q W E R · A S D F · Z X C V.'); }
 function apply(){ const sel=$('kbKeyMode'); const want=window.KSPLIT?'pads':(owner==='keys'?'keys':'pads'); /* v245: with the split keyboard the old one-device piano mode stays off */ if(sel&&sel.value!==want){ sel.value=want; sel.dispatchEvent(new Event('change',{bubbles:true})); } paint(); }
 /* the device you touch takes your keys */
 document./* v245: the hand-off happens when the tap ends, so the strip changing size never moves a button out from under the finger */ addEventListener('pointerup',e=>{ const t=e.target; if(!t||!t.closest) return; if(t.closest('#kbTop')) setTimeout(()=>setOwner('keys'),0); else if(t.closest('#pad .pmain.kFloat')) setTimeout(()=>setOwner('pads'),0); },true);
 function strip(dev){ const bar=dev==='pads'?$('mpcBar'):$('kbDash'); if(!bar) return null; let s=bar.querySelector(':scope > .kKeyOwn'); if(s) return s; s=document.createElement('div'); s.className='kKeyOwn'; s.setAttribute('role','button'); s.tabIndex=0;
  s.addEventListener('click',e=>{ e.stopPropagation(); if(e.target.closest('[data-ko="map"]')){ try{ KKBD.open(dev==='pads'?'pads':'piano'); }catch(_){ } return; } setOwner(dev); });
  bar.insertBefore(s,bar.firstChild); return s; }
 function letters(){ const kb=$('kbKeys'); if(!kb) return; const on=physical(); kb.classList.toggle('kKLon',on); if(!on) return;
  for(let k=0;k<KMAP.length;k++){ const el=kb.querySelector('[data-n="'+k+'"]'); if(!el) continue; let l=el.querySelector(':scope > .kKL'); const blk=/(^|\s)(bk|black|b)(\s|$)/.test(el.className)||[1,3,6,8,10].includes(k%12); if(!l){ l=document.createElement('span'); l.className='kKL'+(blk?' blk':''); l.textContent=KMAP[k].toUpperCase(); if(getComputedStyle(el).position==='static') el.style.position='relative'; el.appendChild(l); } } }
 function fold(dev){ const bar=dev==='pads'?$('mpcBar'):$('kbDash'); if(!bar) return; const row=bar.querySelector(':scope > .mr2'); if(!row) return;
  const extra=dev==='pads'?[...row.querySelectorAll(':scope > [data-m="click"], :scope > [data-m="q"], .kPadInst, .kPadMode, .kBank')]
   :[...row.querySelectorAll(':scope > button.sm:not([data-k]), :scope > [data-k="bars"], :scope > [data-k="bpm"], #kbDashBpm, .kBank')].concat([...row.querySelectorAll(':scope > span.lbl')].filter(x=>/bars/i.test(x.textContent)));
  extra.forEach(x=>{ if(!x.classList.contains('kMoreBtn')&&!x.classList.contains('kMoreOnly')) x.classList.add('kMoreOnly'); });
  let b=row.querySelector(':scope > .kMoreBtn'); if(!b){ b=document.createElement('button'); b.type='button'; b.className='kMoreBtn'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); more[dev]=!more[dev]; putLS('kanin-devmore',more); paint(); try{ KPADFLOAT.fit(dev); }catch(_){ } }); row.appendChild(b); } else if(row.lastElementChild!==b) row.appendChild(b);
  const on=!!more[dev]; const t=on?'⚙ Less':'⚙ More'; if(b.textContent!==t) b.textContent=t; b.classList.toggle('on',on); b.title=on?'Hide the extra controls':'Sound banks, instruments, pad modes, latch to grid, bars and more'; bar.classList.toggle('kLess',!on); }
 function paint(){ const show=physical();
  ['pads','keys'].forEach(dev=>{ fold(dev); const s=strip(dev); if(!s) return; if(s.hidden!==!show) s.hidden=!show; if(!show) return; const on=owner===dev;
   const html=dev==='pads'?(on?'⌨ <b>Your keys play the PADS</b><small>1 2 3 4 · Q W E R · A S D F · Z X C V</small>':'⌨ <b>Tap here to play the pads with your keys</b><small>1 2 3 4 · Q W E R · A S D F · Z X C V</small>')
    :(on?'⌨ <b>Your keys play the PIANO</b><small>Z X C V B N M · Q W E R T Y U I</small>':'⌨ <b>Tap here to play the piano with your keys</b><small>Z X C V B N M · Q W E R T Y U I</small>');
   const full=html+'<button type="button" data-ko="map" data-noul>🗺 Key map</button>'; if(s.dataset.h!==full){ s.dataset.h=full; s.innerHTML=full; } s.classList.toggle('on',on); });
  letters(); }
 setInterval(()=>{ const po=isOpen('pads'), ko=isOpen('keys');
  if(ko&&!was.keys) setOwner('keys',true); else if(po&&!was.pads&&!ko) setOwner('pads',true);
  if(!ko&&owner!=='pads') setOwner('pads',true); if(ko&&!po&&owner!=='keys') setOwner('keys',true);
  was.pads=po; was.keys=ko; apply(); },400);
 /* while the piano has your keys, the pad-only keys (1 and 4) stay quiet instead of firing a pad behind your back */
 addEventListener('keydown',e=>{ if(window.KSPLIT||owner!=='keys'||e.ctrlKey||e.metaKey||e.altKey||e.shiftKey) return; const t=e.target; if(t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable)) return; const k=(e.key||'').toLowerCase(); if(PADK.includes(k)&&!KMAP.includes(k)&&$('pad')&&$('pad').classList.contains('on')){ e.stopImmediatePropagation(); } },true);
 /* "/" is 👆 TAP TEMPO in the controls block while a device is open (kdevkeys); Ctrl+K opens Find */
 /* the keyboard window never lands on top of the pad window on a laptop: it sits beside it, or below it when there is no room */
 function apart(){ if(innerWidth<=760||!isOpen('pads')||!isOpen('keys')) return; const pe=document.querySelector('#pad .pmain'), ke=$('kbTop'); if(!pe||!ke||ke.dataset.kApart==='1') return; const a=pe.getBoundingClientRect(), b=ke.getBoundingClientRect();
  const over=!(b.right<=a.left||b.left>=a.right||b.bottom<=a.top||b.top>=a.bottom); if(!over) { ke.dataset.kApart='1'; return; }
  if(a.left-24>=380){ ke.style.setProperty('--fx','8px'); ke.style.setProperty('--fw',Math.round(a.left-20)+'px'); } else if(innerHeight-a.bottom>=260){ ke.style.setProperty('--fy',Math.round(a.bottom+8)+'px'); } ke.dataset.kApart='1'; }
 setInterval(()=>{ const ke=$('kbTop'); if(ke&&!isOpen('keys')) delete ke.dataset.kApart; apart(); },500);
 const css2=document.createElement('style'); css2.textContent='#kbTop label:has(#kbKeyMode),#kbPlayHint{display:none!important}html body #kbKeys [data-kbd]::before,html body #kbKeys [data-kbd]::after{content:none!important;display:none!important}'; document.head.appendChild(css2);
 window.KKEYROUTE={get owner(){ return owner; },set owner(v){ setOwner(v,true); },PADK,KMAP};
})();
