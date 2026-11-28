(()=>{ /* ⌨ THE CONTROLS ON YOUR KEYBOARD (v245, the split keyboard). The left hand plays the 16 pads (1234 · QWER · ASDF · ZXCV), the
   right hand plays one octave of piano (white Y U I O P [ ] \, black 7 8 · 0 - =) and runs the controls on its home and bottom rows:
     H ⏮ REWIND · J ▶ PLAY · K ■ STOP · L ● REC (records both devices) · ; ↶ UNDO · ' ⬇ LOAD the pads
     N ◀ BANK · M BANK ▶ · , OCT − · . OCT + · / ⬇ LOAD the keys          (Space still plays and stops)
   Every on-screen button shows its key and lights when its key is pressed. Touch, mouse and keys all do the same thing. */
 const $=id=>document.getElementById(id);
 /* v245 split keyboard: the controls sit on the right hand's home and bottom rows, clear of the pads (left) and the piano (Y U I O P [ ] \ and 7 8 0 - =) */
 const COMMON={h:'rew',j:'play',k:'stop',l:'rec',';':'undo'};
 const PADS=Object.assign({"'":'snd',n:'bankp',m:'bankn'},COMMON);
 const KEYS=Object.assign({'/':'snd',',':'octd','.':'octu'},COMMON);
 const OWNER={"'":'pads',n:'pads',m:'pads','/':'keys',',':'keys','.':'keys'};
 const TX=new Set(['rew','play','stop','rec','skip','undo','clear']);
 const isOpen=k=>{ try{ return KRAIL.FLOAT.isOpen(k); }catch(_){ return false; } };
 const physical=()=>{ try{ return matchMedia('(hover:hover) and (pointer:fine)').matches||window.INPUTMODE==='keys'; }catch(_){ return true; } };
 const dev=()=>{ const po=isOpen('pads'), ko=isOpen('keys'); let o='pads'; try{ o=KKEYROUTE.owner; }catch(_){ } if(o==='keys'&&ko) return 'keys'; if(po) return 'pads'; if(ko) return 'keys'; return null; };
 const barOf=d=>d==='pads'?$('mpcBar'):$('kbDash');
 function btnFor(d,act){ const bar=barOf(d); if(!bar) return null; if(TX.has(act)||(act==='latch'&&d==='keys'&&false)) return bar.querySelector('.kDevTx [data-tx="'+act+'"]'); return bar.querySelector('.kScr [data-sf="'+act+'"]'); }
 function run(d,act){ const bar=barOf(d); if(!bar) return false;
  if(act==='bankp'||act==='bankn'){ const s=$('padBank'); const cur=s?+s.value:0; const nx=(cur+(act==='bankn'?1:3))%4; const b=bar.querySelector('.kScr [data-sf="bank'+nx+'"]'); if(b){ b.click(); flash(b); return true; } return false; }
  const b=btnFor(d,act); if(b){ b.click(); flash(b); return true; } return false; }
 function flash(b){ b.classList.add('kKeyHit'); setTimeout(()=>b.classList.remove('kKeyHit'),160); }
 /* UNIVERSAL: the same transport keys work wherever there is something to play or record, through the remote (on the screen it
    shows the same keys): the Studio with no device open, Karaoke, Music, Voices and the Video studio. */
 const UNIV=new Set(['pad','kKara','musicDock','voiceDock','aivDock','langDock']);
 const RKEY={h:'rew',j:'play',k:'stop',l:'rec',';':'undo'};
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 addEventListener('keydown',e=>{ if(e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||e.repeat) return; const t=e.target; if(t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable)) return;
  const pad=$('pad'); const d0=pad&&(pad.classList.contains('on')||document.body.classList.contains('kDevOver'))?dev():null;
  if(!d0){ const c=cur(); const a=RKEY[({KeyH:'h',KeyJ:'j',KeyK:'k',KeyL:'l',Semicolon:';',Quote:"'",KeyN:'n',KeyM:'m',Comma:',',Period:'.',Slash:'/'})[e.code]||(e.key||'').toLowerCase()]; if(a&&UNIV.has(c)){ let R=null; try{ R=KREMOTE.act; }catch(_){ } if(R&&R[a]){ e.preventDefault(); e.stopImmediatePropagation(); R[a](); const b=document.querySelector('#kRemote [data-r="'+a+'"]'); if(b) flash(b); } } return; }
  const k=({KeyH:'h',KeyJ:'j',KeyK:'k',KeyL:'l',Semicolon:';',Quote:"'",KeyN:'n',KeyM:'m',Comma:',',Period:'.',Slash:'/'})[e.code]||(e.key||'').toLowerCase(); const want=OWNER[k]; const d=want&&isOpen(want)?want:d0; const act=(d==='pads'?PADS:KEYS)[k]; if(!act) return;
  e.preventDefault(); e.stopImmediatePropagation(); run(d,act); if(act==='stop') setTimeout(()=>{ try{ if(PADSTUDIO.playing) PADSTUDIO.stop(); }catch(_){ } },180); },true);
 /* the key on every button */
 const css=document.createElement('style'); css.textContent=`
.kKB{position:absolute;top:2px;right:3px;font:900 9.5px/1 ui-monospace,monospace;padding:1px 3px;border-radius:4px;background:#ffe94a;color:#14163a;pointer-events:none}
.kDevTx button,.kSoft button{position:relative}
body:not(.kKBon) .kKB{display:none}
.kKeyHit{outline:3px solid #ffe94a!important;outline-offset:1px;filter:brightness(1.3)}`; document.head.appendChild(css);
 const LABEL={"'":"'",'\\':'\\'};
 function badges(){ document.body.classList.toggle('kKBon',physical()); if(!physical()) return;
  [['pads',PADS],['keys',KEYS]].forEach(([d,M])=>{ const bar=barOf(d); if(!bar) return; Object.entries(M).forEach(([key,act])=>{ const b=act==='bankp'||act==='bankn'?null:btnFor(d,act); if(!b) return; let s=b.querySelector(':scope > .kKB'); const txt=(LABEL[key]||key).toUpperCase(); if(!s){ s=document.createElement('span'); s.className='kKB'; b.appendChild(s); } if(s.textContent!==txt) s.textContent=txt; });
   /* the bank keys: - and = step the bank; the bank buttons show which way */
   if(d==='pads'){ const b0=bar.querySelector('.kScr [data-sf="bank0"]'), b3=bar.querySelector('.kScr [data-sf="bank3"]'); [[b0,'N'],[b3,'M']].forEach(([b,t])=>{ if(!b) return; let s=b.querySelector(':scope > .kKB'); if(!s){ s=document.createElement('span'); s.className='kKB'; b.appendChild(s); } if(s.textContent!==t) s.textContent=t; }); } }); }
 function remoteBadges(){ const on=physical()&&UNIV.has(cur()); Object.entries(RKEY).forEach(([key,a])=>{ const b=document.querySelector('#kRemote [data-r="'+a+'"]'); if(!b) return; let s=b.querySelector(':scope > .kKB'); if(!on){ if(s) s.remove(); return; } if(getComputedStyle(b).position==='static') b.style.position='relative'; if(!s){ s=document.createElement('span'); s.className='kKB'; b.appendChild(s); } const txt=key==='\\'?'\\':key.toUpperCase(); if(s.textContent!==txt) s.textContent=txt; }); }
 setInterval(()=>{ badges(); remoteBadges(); },1200);
 window.KDEVKEYS={PADS,KEYS,run};
})();
