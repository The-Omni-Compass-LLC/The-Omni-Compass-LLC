(()=>{ /* 🔌 ONE CONTROLLER, EVERY STATION (v242). The 16 pads and the keyboard are one controller for the whole studio:
   • 🎧 DJ PAD MODE, the way a DJ controller's pads work: the top two rows (1 2 3 4 · Q W E R) are DECK A, the bottom two rows
     (A S D F · Z X C V) are DECK B, eight pads each, in four pages: HOT CUE (cues 1–4, play/pause, clear, nudge), ROLL (loop rolls
     1/8 to 4 beats, nudge), FX (echo, filter sweep, brake, spinback, stutter, play/pause, nudge) and SAMPLER (the DJ's eight hits
     on the top rows, the beat machine's first eight pads of the selected bank on the bottom rows). 🥁 BEAT puts the pads back on
     the beat machine. The ` key (top left) flips BEAT and DJ. The decks play through their own strips on the mixing board (29, 30).
   • 🎤 KARAOKE: the pads, the keyboard, the DJ decks and the track sequencer come up over the Karaoke page on the same beat (the
     song's beat is the beat machine's clock), so you can sing, hit pads, play keys and record onto the tracks at the same time;
     every take lands on its microphone strip and every track on its own strip of the same mixing board. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const PADK='1234qwerasdfzxcv', KMAP='zsxdcvgbhnjmq2w3er5t6y7ui';
 let mode=getLS('kanin-djpads','beat'); if(!['beat','cue','roll','fx','samp'].includes(mode)) mode='beat';
 const PAGES={cue:['CUE 1','CUE 2','CUE 3','CUE 4','▶ ⏸','CLEAR','◀ NUDGE','NUDGE ▶'],roll:['ROLL 1/8','ROLL 1/4','ROLL 1/2','ROLL 1','ROLL 2','ROLL 4','◀ NUDGE','NUDGE ▶'],fx:['ECHO','SWEEP','BRAKE','SPIN','STUTTER','▶ ⏸','◀ NUDGE','NUDGE ▶']};
 const ROLL=['0.125','0.25','0.5','1','2','4'], FX=['echo','sweep','brake','spin','stutter'];
 const sampNames=()=>[...document.querySelectorAll('#djSamp button')].map(b=>b.textContent.trim());
 const bank=()=>Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0));
 function label(k){ const d=k<8?'A':'B', h=k%8; if(mode==='samp'){ if(k<8) return '🎧 '+(sampNames()[h]||'HIT '+(h+1)); const P=PS(); const pd=P&&P.pads[bank()*16+h]; return '🥁 '+((pd&&pd.name)||'PAD '+(h+1)); } return (PAGES[mode]||[])[h]?d+' · '+PAGES[mode][h]:''; }
 const deck=d=>{ try{ return DJBOOTH.D[d]; }catch(_){ return null; } };
 const perf=(d,sel)=>document.querySelector('#djSec .djPerf[data-d="'+d+'"] '+sel);
 function act(k){ const d=k<8?'A':'B', h=k%8;
  if(mode==='samp'){ if(k<8){ const b=document.querySelectorAll('#djSamp button')[h]; if(b) b.click(); return; } try{ PS().hitPad(bank()*16+h); }catch(_){ } return; }
  const D=deck(d); if(!D||!D.buf){ say('🎧 Load a song on deck '+d+' first: the 🎧 DJ window, Load. The pads then play deck '+d+'.'); try{ F().open('dj'); }catch(_){ } return; }
  let b=null;
  if(mode==='cue'){ if(h<4) b=perf(d,'[data-cue="'+(h+1)+'"]'); else if(h===4) b=document.querySelector('#deck'+d+' [data-a="play"]'); else if(h===5) b=perf(d,'[data-cueclr]'); else b=perf(d,'[data-nudge="'+(h===6?-1:1)+'"]'); }
  if(mode==='roll'){ if(h<6) b=perf(d,'[data-roll="'+ROLL[h]+'"]'); else b=perf(d,'[data-nudge="'+(h===6?-1:1)+'"]'); }
  if(mode==='fx'){ if(h<5) b=perf(d,'[data-fx="'+FX[h]+'"]'); else if(h===5) b=document.querySelector('#deck'+d+' [data-a="play"]'); else b=perf(d,'[data-nudge="'+(h===6?-1:1)+'"]'); }
  if(b) b.click(); }
 function flash(k){ const el=document.querySelector('#padGrid .pd[data-i="'+(bank()*16+k)+'"]'); if(el){ el.classList.add('kbHit'); setTimeout(()=>el.classList.remove('kbHit'),140); } }
 const djOn=()=>mode!=='beat';
 /* touch and mouse: in DJ mode a pad is a DJ pad */
 document.addEventListener('pointerdown',e=>{ if(!djOn()) return; const pd=e.target.closest&&e.target.closest('#padGrid .pd'); if(!pd) return; e.preventDefault(); e.stopImmediatePropagation(); const k=(+pd.dataset.i)%16; act(k); flash(k); },true);
 document.addEventListener('click',e=>{ if(!djOn()) return; const pd=e.target.closest&&e.target.closest('#padGrid .pd'); if(pd){ e.preventDefault(); e.stopImmediatePropagation(); } },true);
 /* the keyboard: in DJ mode 1234 QWER ASDF ZXCV play the DJ pads; ` flips BEAT and DJ; over Karaoke the pads and the piano still play */
 const typing=t=>t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable);
 const over=()=>document.body.classList.contains('kDevOver');
 const padsLive=()=>{ const pad=$('pad'); return !!pad&&(pad.classList.contains('on')||over()); };
 const owner=()=>{ try{ return KKEYROUTE.owner; }catch(_){ return 'pads'; } };
 const isOpen=k=>{ try{ return F().isOpen(k); }catch(_){ return false; } };
 const held=new Map();
 addEventListener('keydown',e=>{ if(e.ctrlKey||e.metaKey||e.altKey||typing(e.target)) return; const key=(e.key||'').toLowerCase();
  if(key==='`'&&padsLive()&&isOpen('pads')){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat) setMode(djOn()?'beat':(getLS('kanin-djpads-last','cue'))); return; }
  if(e.shiftKey) return;
  if(djOn()&&padsLive()&&isOpen('pads')&&owner()!=='keys'){ const k=PADK.indexOf(key); if(k>=0&&/^(Digit|Key)/.test(e.code||'')){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat){ act(k); flash(k); } return; } }
  /* over Karaoke the studio is not the screen, so the pads and the piano are played from here */
  if(over()&&!$('pad').classList.contains('on')){ if(owner()==='keys'&&isOpen('keys')){ const k=KMAP.indexOf(key); if(k>=0&&/^(Digit|Key)/.test(e.code||'')){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat&&!held.has(key)){ held.set(key,k); try{ KEYS.down(k); }catch(_){ } } return; } }
   else if(isOpen('pads')&&!djOn()){ const k=PADK.indexOf(key); if(k>=0&&/^(Digit|Key)/.test(e.code||'')){ e.preventDefault(); e.stopImmediatePropagation(); if(!e.repeat){ try{ PS().hitPad(bank()*16+k); }catch(_){ } flash(k); } return; } } } },true);
 addEventListener('keyup',e=>{ const key=(e.key||'').toLowerCase(); if(held.has(key)){ const k=held.get(key); held.delete(key); try{ KEYS.up(k); }catch(_){ } e.preventDefault(); } },true);
 addEventListener('blur',()=>{ held.forEach(k=>{ try{ KEYS.up(k); }catch(_){ } }); held.clear(); });
 /* the mode strip on the beat machine */
 const css=document.createElement('style'); css.textContent=`
.kDjBar{display:flex;flex-wrap:wrap;gap:4px;align-items:center;margin:4px 0 2px}
.kDjBar b{font:900 11px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.06em;margin-right:2px}
.kDjBar button{position:relative;min-height:34px!important;padding:0 9px!important;border-radius:8px!important;font:900 11.5px system-ui,sans-serif!important;white-space:nowrap}
.kDjBar button.on{background:#ffe94a!important;color:#14163a!important}
.kDjBar button.dj.on{background:#2ad4ff!important;color:#07121f!important}
body.kDJpads #padGrid .pd{position:relative}
body.kDJpads #padGrid .pd::after{content:attr(data-dj);position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;padding:2px;border-radius:inherit;font:900 11px/1.15 system-ui,sans-serif;color:#fff;pointer-events:none;background:linear-gradient(180deg,rgba(0,140,190,.92),rgba(0,70,120,.92));white-space:normal;overflow:hidden}
body.kDJpads #padGrid .pd.kDjB::after{background:linear-gradient(180deg,rgba(200,40,170,.92),rgba(110,20,100,.92))}
body.kDJpads #padGrid .pd.kbHit::after{filter:brightness(1.6)}
/* 🎤 the devices over Karaoke: the studio stays alive under the song, only its floating devices show */
body.kDevOver #pad{display:block!important;position:fixed!important;inset:0!important;visibility:hidden!important;pointer-events:none!important;z-index:8600!important;background:transparent!important;overflow:visible!important}
body.kDevOver #pad .kFloat.kFOn:not(.kFOff){visibility:visible!important;pointer-events:auto!important}
#kKara .kkDev{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:8px 0;padding:8px 10px;border-radius:12px;background:rgba(42,212,255,.08);border:1px solid rgba(42,212,255,.35)}
#kKara .kkDev b{font:800 13px system-ui,sans-serif;color:#7ff;flex:1 1 100%}
#kKara .kkDev button{min-height:44px;border-radius:12px;padding:0 14px;font:800 14px system-ui,sans-serif}
#kKara .kkDev button.on{background:#2ad4ff!important;color:#07121f!important}`; document.head.appendChild(css);
 function bar(){ const host=$('mpcBar'); if(!host) return; let b=host.querySelector(':scope > .kDjBar'); if(!b){ b=document.createElement('div'); b.className='kDjBar'; b.setAttribute('role','toolbar'); b.setAttribute('aria-label','Pad mode');
   b.innerHTML='<b>PADS PLAY</b><button type="button" data-dm="beat" data-noul title="The pads play the beat machine">🥁 BEAT</button><button type="button" class="dj" data-dm="cue" data-noul title="Hot cues on both decks">🎧 DJ · CUE</button><button type="button" class="dj" data-dm="roll" data-noul title="Loop rolls on both decks">🎧 ROLL</button><button type="button" class="dj" data-dm="fx" data-noul title="FX pads on both decks">🎧 FX</button><button type="button" class="dj" data-dm="samp" data-noul title="The DJ sampler and the beat machine">🎧 SAMPLER</button><button type="button" data-dm="open" data-noul title="Open the DJ decks">🎧 Decks</button>';
   b.addEventListener('click',e=>{ const x=e.target.closest('[data-dm]'); if(!x) return; e.stopPropagation(); if(x.dataset.dm==='open'){ try{ F().open('dj'); }catch(_){ } return; } setMode(x.dataset.dm); });
   const tx=host.querySelector(':scope > .kDevTx'); if(tx&&tx.nextSibling) host.insertBefore(b,tx.nextSibling); else host.appendChild(b); }
  b.querySelectorAll('[data-dm]').forEach(x=>x.classList.toggle('on',x.dataset.dm===mode));
  const phys=document.body.classList.contains('kKBon'); let s=b.querySelector('[data-dm="'+(djOn()?'beat':'cue')+'"] .kKB'); b.querySelectorAll('.kKB').forEach(k=>{ if(k!==s) k.remove(); }); if(phys&&!s){ s=document.createElement('span'); s.className='kKB'; s.textContent='`'; b.querySelector('[data-dm="'+(djOn()?'beat':'cue')+'"]').appendChild(s); } }
 function setMode(m){ mode=m; putLS('kanin-djpads',m); if(m!=='beat') putLS('kanin-djpads-last',m); paint(); if(m==='beat') say('🥁 The pads play the beat machine again.'); else { const D=deck('A'), E=deck('B'); say('🎧 DJ '+({cue:'HOT CUE',roll:'ROLL',fx:'FX',samp:'SAMPLER'}[m])+': top two rows play deck A, bottom two rows deck B.'+((!D||!D.buf)&&(!E||!E.buf)&&m!=='samp'?' Load a song on a deck first (🎧 Decks).':'')); if(m!=='samp'&&(!D||!D.buf)) try{ F().open('dj'); }catch(_){ } } }
 function paint(){ bar(); document.body.classList.toggle('kDJpads',djOn()); if(!djOn()) return; const g=$('padGrid'); if(!g) return; g.querySelectorAll('.pd').forEach(el=>{ const k=(+el.dataset.i)%16; const t=label(k); if(el.dataset.dj!==t) el.dataset.dj=t; el.classList.toggle('kDjB',k>=8); }); }
 /* the Karaoke page: bring the devices up over the song */
 function karaBar(){ const K=$('kKara'); if(!K||K.hidden) return; const inn=K.querySelector('.kkIn'); if(!inn) return; let d=inn.querySelector('.kkDev'); if(!d){ d=document.createElement('div'); d.className='kkDev';
   d.innerHTML='<b>🎛 Play live over the song: the same beat, the same tracks, the same mixing board</b><button type="button" data-kd="pads" data-noul>🥁 Pads</button><button type="button" data-kd="keys" data-noul>🎹 Keys</button><button type="button" data-kd="dj" data-noul>🎧 DJ decks</button><button type="button" data-kd="seq" data-noul>🎼 Tracks</button><button type="button" data-kd="mix" data-noul>🎚 Mixing board</button>';
   d.addEventListener('click',e=>{ const x=e.target.closest('[data-kd]'); if(!x) return; e.stopPropagation(); const k=x.dataset.kd; const f=F(); if(!f) return;
    if(k==='mix'){ try{ KKARA.close(); }catch(_){ } try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ const m=$('padMixer'); if(m) m.scrollIntoView({block:'start',behavior:'smooth'}); },900); return; }
    const vis=over()&&f.isOpen(k); document.body.classList.add('kDevOver'); if(vis) f.close(k); else { f.open(k); if(k==='pads') try{ KKEYROUTE.owner='pads'; }catch(_){ } if(k==='keys') try{ KKEYROUTE.owner='keys'; }catch(_){ } }
    say(f.isOpen(k)?({pads:'🥁 The pads are over the song: hit them or 1 2 3 4 · Q W E R · A S D F · Z X C V. ● REC records them on the beat.',keys:'🎹 The keyboard is over the song: Z to M and Q to I play it. ● REC records it onto its track.',dj:'🎧 The DJ decks are over the song.',seq:'🎼 The track sequencer is over the song: the Karaoke takes are on it too.'}[k]):'Closed.'); paintKara(); });
   const rows=inn.querySelectorAll('.kkRow'); const at=rows[1]||rows[0]; if(at&&at.parentNode) at.parentNode.insertBefore(d,at.nextSibling); else inn.insertBefore(d,inn.firstChild); }
  paintKara(); }
 function paintKara(){ const d=document.querySelector('#kKara .kkDev'); if(!d) return; d.querySelectorAll('[data-kd]').forEach(x=>{ const k=x.dataset.kd; if(k!=='mix') x.classList.toggle('on',over()&&isOpen(k)); }); }
 /* Karaoke redraws its page often: the device bar goes back in at once */
 let mo=null; function watchKara(){ const K=$('kKara'); if(!K||mo) return; mo=new MutationObserver(()=>{ if(!K.hidden&&!K.querySelector('.kkDev')) karaBar(); }); mo.observe(K,{childList:true,subtree:false}); const inn=K.querySelector('.kkIn'); if(inn) mo.observe(inn,{childList:true}); }
 setInterval(()=>{ watchKara(); paint(); karaBar(); const K=$('kKara'); const karaUp=!!K&&!K.hidden; if(over()&&(!karaUp||$('pad').classList.contains('on'))) document.body.classList.remove('kDevOver'); },600);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Studio','🎧','DJ pads: the 16 pads play both DJ decks (hot cue, roll, FX, sampler)','Studio',()=>{ try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ try{ F().open('pads'); }catch(_){ } setMode('cue'); },900); }); });
 window.KWIRE={get mode(){ return mode; },setMode,act,label};
})();
