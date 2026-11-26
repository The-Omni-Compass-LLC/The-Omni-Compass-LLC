(()=>{ /* ONE CONTROL PANEL IN EACH DEVICE (v239). The 16-pad beat machine and the MIDI keyboard each carry the whole transport
   in their own window, in one row: ⏮ REWIND · ▶ PLAY · ■ STOP · ● REC · ⏭ SKIP · ↶ UNDO · 🗑 CLEAR (and 🔒 LATCH on the keys).
   PLAY and STOP are two buttons, never one that changes its name; REC records that device in real time, as played; REWIND goes back
   to bar 1 and SKIP jumps a bar on. While the pad or keyboard window is open, the separate floating remote steps aside: the device
   is the remote. The Studio’s transport bar, the rail’s ▶ and the keyboard shortcuts all drive the same clock. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const playing=()=>{ try{ return !!(PS()&&PS().playing); }catch(_){ return false; } };
 const R=()=>{ try{ return KREMOTE.act; }catch(_){ return null; } };
 const DEV={pads:{bar:()=>$('mpcBar'),attr:'m',recOn:()=>{ const b=$('padRecLive'); return !!b&&(b.classList.contains('rec')||/on$/i.test(b.textContent.trim())); }},
  keys:{bar:()=>$('kbDash'),attr:'k',recOn:()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); }}};
 const css=document.createElement('style'); css.textContent=`
.kDevTx{display:grid;grid-template-columns:repeat(auto-fit,minmax(64px,1fr));gap:5px;margin:0 0 5px}
.kDevTx button{display:flex!important;flex-direction:column;align-items:center;justify-content:center;gap:1px;min-height:54px!important;padding:2px 3px!important;border-radius:12px!important;font:900 11px system-ui,sans-serif!important;letter-spacing:0;white-space:nowrap;overflow:hidden;color:#fff!important;border:2px solid rgba(255,255,255,.28)!important}
.kDevTx button span{font-size:20px;line-height:1}
.kDevTx [data-tx="rew"],.kDevTx [data-tx="skip"]{background:#3b2f7a!important}
.kDevTx [data-tx="play"]{background:#137a3f!important}.kDevTx [data-tx="play"].on{background:#22c55e!important;color:#04150b!important;box-shadow:0 0 0 3px #7cff8a}
.kDevTx [data-tx="stop"]{background:#b3172f!important}
.kDevTx [data-tx="rec"]{background:#5c0d1c!important}.kDevTx [data-tx="rec"].on{background:#ff2d4f!important;box-shadow:0 0 0 3px #ffb3c0;animation:kTxRec 1s ease-in-out infinite alternate}
.kDevTx [data-tx="undo"]{background:#2a4fa8!important}.kDevTx [data-tx="clear"]{background:#4a4f63!important}.kDevTx [data-tx="latch"]{background:#6b4a00!important}.kDevTx [data-tx="latch"].on{background:#ffe94a!important;color:#14163a!important}
@keyframes kTxRec{from{filter:brightness(1)}to{filter:brightness(1.4)}}
#mpcBar .mr.kTxOld,#kbDash .mr.kTxOld{display:none!important}
html body #mpcBar .kDevTx button,html body #kbDash .kDevTx button,html body #mpcBar [data-m="click"],html body #kbDash button{white-space:nowrap!important;word-break:keep-all!important;overflow-wrap:normal!important;hyphens:none!important}
body.kDevOpen #kRemote{display:none!important}
html body .kFloat.kFOn.kMin,html body #pad .pmain.kFloat.kFOn.kMin,html body #kbTop.kFloat.kFOn.kMin{max-height:50px!important;height:50px!important;min-height:0!important;overflow:hidden!important;resize:none!important}
html body .kSpd .clk{min-width:56px!important;white-space:nowrap!important;word-break:keep-all!important}html body .kSpd .clk span{font-size:11.5px!important;white-space:nowrap!important}
@media (max-width:420px){ .kDevTx{grid-template-columns:repeat(4,minmax(0,1fr))} .kDevTx button{min-height:50px!important;font-size:10.5px!important} }`; document.head.appendChild(css);
 const old=(dev,k)=>{ const b=DEV[dev].bar(); return b&&b.querySelector('.mr [data-'+DEV[dev].attr+'="'+k+'"]'); };
 function act(dev,k){ const r=R();
  if(k==='play'){ if(playing()) return say('▶ Already playing. ■ STOP ends it.'); const o=old(dev,'play'); if(o) o.click(); else if(r) r.play(); return; }
  if(k==='stop'){ const was=playing(); if(was){ const o=old(dev,'play'); if(o) o.click(); } try{ if(PS()&&PS().playing) PS().stop(); }catch(_){ } if(r) try{ r.stop(); }catch(_){ } else say('■ Stopped.'); return; }
  if(k==='rec'){ const o=old(dev,'rec'); if(o) o.click(); else if(r) r.rec(); return; }
  if(k==='rew'){ if(r) r.rew(); return; }
  if(k==='skip'){ /* one bar on in the loop; past the last bar it wraps to bar 1 */ try{ const P=window.PADS, ps=PS(); const spb=(ps&&ps.spbN)||16, bars=(ps&&ps.barsN)||1; if(P&&typeof P.step==='number'&&P.playing&&bars>1){ const nb=(Math.floor(Math.max(0,P.step)/spb)+1)%bars; P.step=nb*spb-1; return say('⏭ Bar '+(nb+1)+' of '+bars+'.'); } }catch(_){ } if(r) r.skip(); return; }
  if(k==='undo'||k==='clear'||k==='latch'){ const o=old(dev,k); if(o) o.click(); return; } }
 function build(dev){ const bar=DEV[dev].bar(); if(!bar) return null; let tx=bar.querySelector(':scope > .kDevTx'); if(tx) return tx; const mr=bar.querySelector(':scope > .mr'); if(!mr) return null;
  tx=document.createElement('div'); tx.className='kDevTx'; tx.setAttribute('role','toolbar'); tx.setAttribute('aria-label',(dev==='pads'?'Beat machine':'Keyboard')+' transport');
  const B=[['rew','⏮','REWIND'],['play','▶','PLAY'],['stop','■','STOP'],['rec','●','REC'],['skip','⏭','SKIP'],['undo','↶','UNDO'],['clear','🗑','CLEAR']].concat(dev==='keys'?[['latch','🔒','LATCH']]:[]);
  tx.innerHTML=B.map(([k,i,l])=>'<button type="button" data-tx="'+k+'"'+(k==='stop'?' data-m="stop"':'')+' title="'+l.charAt(0)+l.slice(1).toLowerCase()+'" aria-label="'+l.charAt(0)+l.slice(1).toLowerCase()+'" data-noul><span>'+i+'</span>'+l+'</button>').join('');
  tx.addEventListener('click',e=>{ const b=e.target.closest('[data-tx]'); if(!b) return; e.stopPropagation(); act(dev,b.dataset.tx); setTimeout(paint,60); setTimeout(paint,300); });
  mr.classList.add('kTxOld'); bar.insertBefore(tx,mr); return tx; }
 function paint(){ let any=false; for(const dev of Object.keys(DEV)){ const tx=build(dev); if(!tx) continue; const p=playing(), rc=DEV[dev].recOn();
   const pb=tx.querySelector('[data-tx="play"]'), rb=tx.querySelector('[data-tx="rec"]'); if(pb.classList.contains('on')!==p) pb.classList.toggle('on',p); if(rb.classList.contains('on')!==rc){ rb.classList.toggle('on',rc); rb.lastChild.textContent=rc?'REC ON':'REC'; }
   const lb=tx.querySelector('[data-tx="latch"]'); if(lb){ const o=old(dev,'latch'); const on=!!o&&(o.classList.contains('on')||/on/i.test(o.getAttribute('aria-pressed')||'')); if(lb.classList.contains('on')!==on) lb.classList.toggle('on',on); } }
  try{ const F=KRAIL.FLOAT; const pad=$('pad'); any=!!(pad&&pad.classList.contains('on')&&(F.isOpen('pads')||F.isOpen('keys'))); }catch(_){ any=false; }
  if(document.body.classList.contains('kDevOpen')!==any) document.body.classList.toggle('kDevOpen',any); }
 /* SCROLL TO REACH WHAT IS UNDER: when you scroll the Studio down into the sequencer or the mixing board, an open pad or keyboard
    window folds to its title bar so every knob, fader and step under it can be touched; scroll back up to where it opened and it
    opens again. A tap on its title bar (▁) opens it any time. */
 const base={}, auto={}, wasOpen={}; let told=false;
 const elOf=k=>k==='pads'?document.querySelector('#pad .pmain'):$('kbTop');
 function fold(){ const pad=$('pad'); if(!pad||!pad.classList.contains('on')) return; let F; try{ F=KRAIL.FLOAT; }catch(_){ return; } const y=pad.scrollTop;
  ['pads','keys'].forEach(k=>{ const el=elOf(k); const open=!!(el&&F.isOpen(k)); if(!open){ wasOpen[k]=false; auto[k]=false; return; }
   const min=el.classList.contains('kMin'); if(!wasOpen[k]||(!min&&!auto[k]&&base[k]==null)){ base[k]=y; } wasOpen[k]=true;
   if(!min&&!auto[k]&&base[k]!=null&&Math.abs(y-base[k])<40) base[k]=Math.min(base[k],y);
   if(!min&&y-base[k]>180){ el.classList.add('kMin'); auto[k]=true; if(!told){ told=true; say('🥁 The pad window folded so you can reach the knobs under it. Scroll back up, or tap its ▁, to open it.'); } }
   else if(min&&auto[k]&&y-base[k]<70){ el.classList.remove('kMin'); auto[k]=false; try{ KPADFLOAT.fit(k); }catch(_){ } }
   else if(!min&&auto[k]){ auto[k]=false; base[k]=y; } /* opened by hand while down there: it stays open here */ }); }
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('.kFHead [data-fh="min"]'); if(!b) return; setTimeout(()=>{ ['pads','keys'].forEach(k=>{ const el=elOf(k); if(el&&el.contains(b)){ auto[k]=false; const pad=$('pad'); base[k]=pad?pad.scrollTop:0; } }); },50); },true);
 setInterval(()=>{ paint(); fold(); },300);
 let rf=0; document.addEventListener('scroll',e=>{ if(rf) return; const t=e.target; if(t!==$('pad')&&t!==document&&t!==document.documentElement) return; rf=requestAnimationFrame(()=>{ rf=0; fold(); }); },true);
 window.KDEVTX={act,paint};
})();
