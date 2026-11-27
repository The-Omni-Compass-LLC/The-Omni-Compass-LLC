(()=>{ /* 🎬 DEMO: MAKE A BEAT (v242). A guided tour that makes a real track, step by step, on the real controls: it opens each
   device, rings the button to press, says what it does, and on "▶ Do it for me" presses it itself (it really plays the pads and
   the keys in time, so the recording you hear is a real one). "⏩ Play the whole demo" runs every step on its own. ✕ stops at
   any point and leaves what was made, ↶ Undo works as usual. Steps: the beat machine, a kit, a 2-bar loop, recording drums in
   real time, the track sequencer, arming the bass track, recording a bassline over the drums, listening, mute and solo, the
   mixing board, saving. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const sl=ms=>new Promise(r=>setTimeout(r,ms));
 const PS=()=>window.PADSTUDIO; const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const q=s=>document.querySelector(s);
 const press=s=>{ const b=typeof s==='string'?q(s):s; if(b){ b.click(); return true; } return false; };
 const beatMs=()=>60000/((PS()&&PS().bpm&&PS().bpm())||90);
 async function playDrums(){ const P=PS(); if(!P) return; const b=beatMs(); const pat=[[0,0],[1,4],[0.5,8],[1.5,8],[2,0],[2.5,0],[3,4],[3.5,8]]; /* [beat, pad]: kick 0, snare 4? use the kit's own pads */
  const KICK=0, SNARE=2, HAT=4; const seq=[[0,KICK],[0,HAT],[.5,HAT],[1,SNARE],[1,HAT],[1.5,HAT],[2,KICK],[2.25,KICK],[2,HAT],[2.5,HAT],[3,SNARE],[3,HAT],[3.5,HAT]];
  const t0=performance.now(); for(const [beat,pad] of seq){ const wait=t0+beat*b-performance.now(); if(wait>0) await sl(wait); try{ P.hitPad(pad); }catch(_){ } flashPad(pad); if(!running) return; } }
 function flashPad(i){ const el=q('#padGrid .pd[data-i="'+i+'"]'); if(el){ el.classList.add('kbHit'); setTimeout(()=>el.classList.remove('kbHit'),140); } }
 async function playBass(){ if(!window.KEYS) return; const b=beatMs(); const line=[[0,0,.9],[1,0,.4],[1.5,3,.4],[2,5,.9],[3,7,.4],[3.5,5,.4]]; const t0=performance.now();
  for(const [beat,k,len] of line){ const wait=t0+beat*b-performance.now(); if(wait>0) await sl(wait); try{ KEYS.down(k); }catch(_){ } await sl(len*b); try{ KEYS.up(k); }catch(_){ } if(!running) return; } }
 const STEPS=[
  {t:'1 · The beat machine',d:'This is the 16-pad beat machine. Tap a pad to hear it. On a computer keyboard the pads are 1 2 3 4 · Q W E R · A S D F · Z X C V.',ring:'#pad .pmain',go:async()=>{ try{ if(KRAIL.cur()!=='pad') KRAIL.goTo('pad'); }catch(_){ } await sl(900); try{ F().open('pads'); }catch(_){ } await sl(500); }},
  {t:'2 · Pick a kit',d:'◀ KIT ▶ under the screen changes the whole drum kit. The screen shows its name (PGM).',ring:'#mpcBar .kScr [data-sf="kitn"]',go:async()=>{ const s=$('padKit'); if(s){ s.value='10'; s.dispatchEvent(new Event('input',{bubbles:true})); s.dispatchEvent(new Event('change',{bubbles:true})); } await sl(400); }},
  {t:'3 · A 2-bar loop',d:'🔄 LOOP sets how long the loop is: 1, 2, 4 or 8 bars. The screen shows LOOP 2 BARS.',ring:'#mpcBar .kScr [data-sf="loop"]',go:async()=>{ try{ PS().setBars(2); }catch(_){ } await sl(300); }},
  {t:'4 · Clear the pattern',d:'🗑 CLEAR empties the selected pad. For this demo the whole pattern starts empty, so you hear only what gets recorded.',ring:'#mpcBar .kDevTx [data-tx="clear"]',go:async()=>{ try{ PS().pads.forEach(p=>{ if(p.steps) p.steps.fill(0); p.xh=[]; }); PS().refresh(); }catch(_){ } await sl(300); }},
  {t:'5 · Record drums in real time',d:'● REC starts the loop and records every pad you hit onto the track the pads are on (Pads A), exactly when you hit it (🧲 Q off). Watch the demo play kick, snare and hi-hat.',ring:'#mpcBar .kDevTx [data-tx="rec"]',go:async()=>{ const P=PS(); try{ KSEQ.select('pA',true); }catch(_){ } press('#mpcBar .kDevTx [data-tx="rec"]'); await sl(250); if(P&&!P.playing){ press('#mpcBar .kDevTx [data-tx="play"]'); await sl(200); } await playDrums(); await playDrums(); press('#mpcBar .kDevTx [data-tx="rec"]'); await sl(200); }},
  {t:'6 · The track sequencer',d:'🎼 Tracks opens the sequencer: Pads A to D on top (the four pad banks, each its own sounds), keyboard tracks under them (each its own sound), the playhead riding the loop. Tap a track and the pads or the keyboard move to it.',ring:'#bbBar [data-sqo]',go:async()=>{ try{ KSEQ.open(); }catch(_){ } await sl(900); try{ F().open('keys'); }catch(_){ } await sl(600); }},
  {t:'7 · Arm the bass track',d:'Tap the bass track: the keyboard moves to it, with its bass sound on the keys, and records onto it.',ring:'#sqHeads [data-tr="k2"]',go:async()=>{ try{ KSEQ.arm('k2'); }catch(_){ } await sl(400); }},
  {t:'8 · Record a bassline',d:'● REC on the keyboard records the notes in real time over the drums. On a computer keyboard the piano is Z X C V B N M (and Q W E R T Y U I).',ring:'#kbDash .kDevTx [data-tx="rec"]',go:async()=>{ const P=PS(); if(P&&!P.playing){ press('#kbDash .kDevTx [data-tx="play"]'); await sl(300); } press('#kbDash .kDevTx [data-tx="rec"]'); await sl(200); await playBass(); await playBass(); press('#kbDash .kDevTx [data-tx="rec"]'); await sl(200); }},
  {t:'9 · Listen',d:'▶ PLAY loops the whole track: the drums and the bass you just recorded. ■ STOP stops it.',ring:'#kSeqWin [data-sq="play"]',go:async()=>{ const P=PS(); if(P&&!P.playing){ press('#kSeqWin [data-sq="play"]'); } await sl(beatMs()*8); }},
  {t:'10 · Mute and solo',d:'M mutes a track, S plays it alone. Here the bass plays alone for a moment, then everything comes back.',ring:'#sqHeads [data-tr="k2"] [data-tk="solo"]',go:async()=>{ press('#sqHeads [data-tr="k2"] [data-tk="solo"]'); await sl(beatMs()*4); press('#sqHeads [data-tr="k2"] [data-tk="solo"]'); await sl(300); }},
  {t:'11 · Fix a take',d:'↶ UNDO on the keyboard takes back the last take on the armed track; tap any note in the sequencer to delete it. Q snaps a track to the grid.',ring:'#sqHeads [data-tr="k2"] [data-tk="q"]',go:async()=>{ await sl(300); }},
  {t:'12 · The mixing board',d:'🎚 Mixer opens the console: a channel strip for every pad and track, with volume, pan, mute and solo.',ring:'#kSeqWin [data-sq="mix"]',go:async()=>{ await sl(300); }},
  {t:'13 · Save it',d:'💾 Save keeps the beat in your Projects on this device. That is a whole track: drums, bass, mixed and saved.',ring:'#bbBar',go:async()=>{ try{ KREMOTE.act.save(); }catch(_){ } await sl(400); press('#kSeqWin [data-sq="stop"]'); }}];
 let i=0, running=false, auto=false;
 const css=document.createElement('style'); css.textContent=`
#kDemo{position:fixed;z-index:9795;left:calc(10px + env(safe-area-inset-left,0px));bottom:calc(10px + env(safe-area-inset-bottom,0px));width:min(420px,calc(100vw - var(--kRailW,58px) - 24px));background:#14163a;color:#fff;border:3px solid #ffe94a;border-radius:16px;box-shadow:0 14px 40px rgba(0,0,0,.6);padding:12px 14px;font:15px/1.45 system-ui,sans-serif}
#kDemo[hidden]{display:none!important}
#kDemo h3{margin:0 0 4px;font:900 18px system-ui,sans-serif;color:#ffe94a}
#kDemo p{margin:0 0 10px}
#kDemo .dmRow{display:flex;flex-wrap:wrap;gap:6px}
#kDemo .dmRow button{flex:1 1 auto;min-height:42px!important;border-radius:10px!important;font:800 13.5px system-ui,sans-serif!important}
#kDemo .dmRow .go{background:#137a3f!important}#kDemo .dmRow .auto{background:#2a4fa8!important}#kDemo .dmRow .x{background:#7a0f22!important;flex:0 0 auto}
#kDemo .dmBar{height:5px;border-radius:3px;background:#2e3266;margin:0 0 8px;overflow:hidden}#kDemo .dmBar i{display:block;height:100%;background:#ffe94a}
#kDemoRing{position:fixed;z-index:9794;pointer-events:none;border:3px solid #ffe94a;border-radius:12px;box-shadow:0 0 0 4px rgba(255,233,74,.35),0 0 22px #ffe94a;transition:all .25s ease}
#kDemoRing[hidden]{display:none!important}`; document.head.appendChild(css);
 function card(){ let c=$('kDemo'); if(c) return c; c=document.createElement('div'); c.id='kDemo'; c.hidden=true; c.setAttribute('role','dialog'); c.setAttribute('aria-label','Demo: make a beat'); document.body.appendChild(c);
  c.addEventListener('click',async e=>{ const b=e.target.closest('[data-dm]'); if(!b) return; e.stopPropagation(); const k=b.dataset.dm;
   if(k==='x') return stop(); if(k==='back'){ i=Math.max(0,i-1); return paint(); } if(k==='next'){ i=Math.min(STEPS.length-1,i+1); return paint(); }
   if(k==='do'){ await doStep(); if(i<STEPS.length-1){ i++; paint(); } else finish(); }
   if(k==='auto'){ auto=true; paint(); while(running&&auto&&i<STEPS.length){ await doStep(); if(!running||!auto) break; if(i<STEPS.length-1){ i++; paint(); await sl(900); } else { finish(); break; } } } });
  let r=$('kDemoRing'); if(!r){ r=document.createElement('div'); r.id='kDemoRing'; r.hidden=true; document.body.appendChild(r); } return c; }
 let busy=false; async function doStep(){ if(busy) return; busy=true; const s=STEPS[i]; const c=card(); c.querySelectorAll('button').forEach(b=>b.disabled=b.dataset.dm!=='x'); try{ await s.go(); }catch(_){ } busy=false; c.querySelectorAll('button').forEach(b=>b.disabled=false); }
 function speak(t){ try{ if(!window.speechSynthesis) return; speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(t); try{ const v=window.KVOICE&&KVOICE('en'); if(v) u.voice=v; }catch(_){ } u.rate=1.02; speechSynthesis.speak(u); }catch(_){ } }
 function paint(){ const c=card(); const s=STEPS[i]; c.innerHTML='<div class="dmBar"><i style="width:'+Math.round((i+1)/STEPS.length*100)+'%"></i></div><h3>🎬 '+s.t+'</h3><p>'+s.d+'</p><div class="dmRow"><button type="button" data-dm="back" data-noul'+(i?'':' disabled')+'>◀ Back</button><button type="button" class="go" data-dm="do" data-noul>▶ Do it for me</button><button type="button" data-dm="next" data-noul>Next ▶</button><button type="button" class="auto" data-dm="auto" data-noul>'+(auto?'⏩ Playing the demo…':'⏩ Play the whole demo')+'</button><button type="button" class="x" data-dm="x" aria-label="End the demo" data-noul>✕</button></div>';
  ring(); if(!auto) speak(s.t.replace(/^\d+ · /,'')+'. '+s.d); }
 function ring(){ const r=$('kDemoRing'); if(!r||!running) return; const s=STEPS[i]; const el=s&&q(s.ring); if(!el||!el.getClientRects().length){ r.hidden=true; return; } const b=el.getBoundingClientRect(); r.hidden=false; r.style.left=(b.left-5)+'px'; r.style.top=(b.top-5)+'px'; r.style.width=(b.width+10)+'px'; r.style.height=(b.height+10)+'px'; }
 setInterval(ring,300);
 function start(){ document.body.classList.add('kDemoOn'); running=true; auto=false; i=0; card().hidden=false; paint(); STEPS[0].go(); }
 function stop(){ running=false; auto=false; const c=$('kDemo'); if(c) c.hidden=true; const r=$('kDemoRing'); if(r) r.hidden=true; try{ speechSynthesis.cancel(); }catch(_){ } }
 function finish(){ auto=false; const c=card(); c.innerHTML='<h3>🎬 Done: you made a track</h3><p>Drums recorded in real time, a bassline on its own track, mixed and saved. Now make your own: arm a track, press ● REC and play.</p><div class="dmRow"><button type="button" data-dm="x" class="go" data-noul>✓ Finish</button></div>'; const r=$('kDemoRing'); if(r) r.hidden=true; speak('Done. You made a track.'); }
 /* ways in: the Menu, Find, the Easy Studio panel */
 setInterval(()=>{ const ez=$('kEasyStudio'); if(ez&&!ez.querySelector('[data-kdemo]')){ const g=ez.querySelector('.ezGrid'); if(g){ const b=document.createElement('button'); b.type='button'; b.dataset.kdemo='1'; b.setAttribute('data-noul',''); b.className='go'; b.innerHTML='<i>🎬</i>Demo: make a beat'; b.addEventListener('click',e=>{ e.stopPropagation(); start(); }); g.insertBefore(b,g.firstChild); } } },1000);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Studio','🎬','Demo: make a beat, step by step','guided tour',()=>start()); });
 window.KDEMO={start,stop,steps:STEPS.length};
 /* v245: while the demo runs, every button it points at is shown */ setInterval(()=>document.body.classList.toggle('kDemoOn',!!running),500);
})();
