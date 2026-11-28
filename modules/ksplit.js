(()=>{ /* ⌨ ONE KEYBOARD, SPLIT LEFT AND RIGHT (v245). Every laptop and desktop keyboard (the standard QWERTY layout) plays the pads and the
   piano at the same time, so both devices can be open, played and recorded together with no key shared between them:
     LEFT HAND · the 16 pads, 4 × 4 like the screen     1 2 3 4 · Q W E R · A S D F · Z X C V
     RIGHT HAND · one octave of piano                    white keys  Y U I O P [ ] \   (C D E F G A B C)
                                                         black keys  7 8 · 0 - =       (C♯ D♯ · F♯ G♯ A♯, above their white keys)
     RIGHT HAND · the controls                           H ⏮ rewind · J ▶ play · K ■ stop · L ● record (both) · ; ↶ undo · ' ⬇ load pads
                                                         N bank ◀ · M bank ▶ · , octave − · . octave + · / ⬇ load keys · Space play/stop
     🎧 DJ MODE · one deck per hand                     deck A: 1 2 3 4 · Q W E R      deck B: 7 8 9 0 · U I O P
   The keys work wherever the devices are up: the Music Studio, and over Karaoke and the Video studio. ` flips the pads between
   the beat machine and the DJ decks. */
 const $=id=>document.getElementById(id);
 const PADK='1234qwerasdfzxcv';
 /* v254: keys are read by their PHYSICAL position (KeyboardEvent.code), so the same left and right halves work on every layout:
    U.S. QWERTY, German QWERTZ, French AZERTY, Dvorak, laptop or desktop; the on-screen letters follow the keyboard in use. */
 const PADC=['Digit1','Digit2','Digit3','Digit4','KeyQ','KeyW','KeyE','KeyR','KeyA','KeyS','KeyD','KeyF','KeyZ','KeyX','KeyC','KeyV'];
 const PIANOC={KeyY:0,Digit7:1,KeyU:2,Digit8:3,KeyI:4,KeyO:5,Digit0:6,KeyP:7,Minus:8,BracketLeft:9,Equal:10,BracketRight:11,Backslash:12};
 const DJBC=['Digit7','Digit8','Digit9','Digit0','KeyU','KeyI','KeyO','KeyP'];
 const QUIET=['KeyZ','KeyS','KeyX','KeyD','KeyC','KeyV','KeyG','KeyB','KeyQ','KeyW','KeyE','KeyR','Digit2','Digit3','Digit5','Digit6','KeyT'];
 let LM=null; try{ if(navigator.keyboard&&navigator.keyboard.getLayoutMap) navigator.keyboard.getLayoutMap().then(m=>{ LM=m; }).catch(()=>{}); }catch(_){ }
 const lab=(code,def)=>{ const v=LM&&LM.get(code); return (v||def||'').toUpperCase(); };
 const PIANO={y:0,'7':1,u:2,'8':3,i:4,o:5,'0':6,p:7,'-':8,'[':9,'=':10,']':11,'\\':12};
 const DJB=['7','8','9','0','u','i','o','p'];
 const typing=t=>t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable);
 const isOpen=k=>{ try{ return KRAIL.FLOAT.isOpen(k); }catch(_){ return false; } };
 const live=()=>{ const pad=$('pad'); return !!pad&&(pad.classList.contains('on')||document.body.classList.contains('kDevOver')); };
 const bank=()=>Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0));
 const djMode=()=>{ try{ return KWIRE.mode!=='beat'; }catch(_){ return false; } };
 const flash=sel=>{ const el=document.querySelector(sel); if(el){ el.classList.add('kbHit'); setTimeout(()=>el.classList.remove('kbHit'),140); } };
 const held=new Map();
 addEventListener('keydown',e=>{ if(e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||typing(e.target)||!live()) return; const c=e.code||''; const physKey=/^(Digit|Key|Minus|Equal|BracketLeft|BracketRight|Backslash)/.test(c);
  if(!physKey) return;
  /* 🎧 DJ: deck A on the left hand, deck B on the right hand */
  if(djMode()&&isOpen('pads')){ const a=PADC.slice(0,8).indexOf(c), bi=DJBC.indexOf(c); if(a>=0||bi>=0){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat){ const pad=a>=0?a:8+bi; try{ KWIRE.act(pad); }catch(_){ } flash('#padGrid .pd[data-i="'+(bank()*16+pad)+'"]'); } return; } }
  /* left hand: the 16 pads */
  const p=PADC.indexOf(c); if(p>=0&&isOpen('pads')&&!djMode()){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat){ try{ PADSTUDIO.hitPad(bank()*16+p); }catch(_){ } flash('#padGrid .pd[data-i="'+(bank()*16+p)+'"]'); } return; }
  /* right hand: the piano */
  if(c in PIANOC&&isOpen('keys')){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat&&!held.has(c)){ held.set(c,PIANOC[c]); try{ KEYS.down(PIANOC[c]); }catch(_){ } } return; }
  /* the old one-device piano letters stay quiet, so a key never plays two different things */
  if(isOpen('keys')&&QUIET.includes(c)){ e.preventDefault(); e.stopImmediatePropagation(); } },true);
 addEventListener('keyup',e=>{ const k=e.code||''; if(held.has(k)){ const n=held.get(k); held.delete(k); try{ KEYS.up(n); }catch(_){ } e.preventDefault(); e.stopImmediatePropagation(); } },true);
 addEventListener('blur',()=>{ held.forEach(n=>{ try{ KEYS.up(n); }catch(_){ } }); held.clear(); });
 /* the strip on each device says which hand plays it */
 const css=document.createElement('style'); css.textContent=`
html body .kKeyOwn{display:none!important}
.kSplitStrip{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;margin:0 0 6px;padding:6px 10px;border-radius:12px;background:#ffe94a;color:#14163a;font:900 13.5px system-ui,sans-serif}
.kSplitStrip small{font:800 12px ui-monospace,monospace;opacity:.85}
body:not(.kKBon) .kSplitStrip{display:none}`; document.head.appendChild(css);
 function strips(){ [['mpcBar','⌨ Left hand plays the pads',PADC.map(c=>lab(c,c.slice(-1))).reduce((a,x,i)=>a+(i&&i%4===0?' · ':i?' ':'')+x,'')+(djMode()?'  ·  DJ: deck A 1234 QWER · deck B 7890 UIOP':'')],['kbDash','⌨ Right hand plays the piano','white '+['KeyY','KeyU','KeyI','KeyO','KeyP','BracketLeft','BracketRight','Backslash'].map(c=>lab(c,{BracketLeft:'[',BracketRight:']',Backslash:'\\'}[c]||c.slice(-1))).join(' ')+' · black '+['Digit7','Digit8'].map(c=>lab(c,c.slice(-1))).join(' ')+' · '+['Digit0','Minus','Equal'].map(c=>lab(c,{Minus:'-',Equal:'='}[c]||c.slice(-1))).join(' ')+' · controls H J K L ; \' · N M , . /']].forEach(([id,t,s])=>{ const bar=$(id); if(!bar) return; let el=bar.parentElement&&bar.parentElement.querySelector(':scope > .kSplitStrip'); if(!el){ el=document.createElement('div'); el.className='kSplitStrip'; bar.parentElement.insertBefore(el,bar); } const h='<b>'+t+'</b><small>'+s+'</small>'; if(el.dataset.h!==h){ el.dataset.h=h; el.innerHTML=h; } }); }
 /* the piano's letters follow the keyboard in use */
 function relabel(){ if(!LM) return; const kb=document.getElementById('kbKeys'); if(!kb) return; Object.entries(PIANOC).forEach(([code,n])=>{ const el=kb.querySelector('[data-n="'+n+'"] > .kKL'); if(el){ const t=lab(code,el.textContent); if(el.textContent!==t) el.textContent=t; } }); }
 setInterval(()=>{ strips(); relabel(); },800);
 window.KSPLIT={on:true,PIANO,PADK};
})();
