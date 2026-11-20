(()=>{ /* 🎵 BACKGROUND MUSIC (v211): one switch on the Music screen, 🎵 Background ON or OFF. With it ON, the song keeps playing
   when you close Music and work anywhere in the app; to turn it off, go back into Music. A small ♪ tag shows what is playing; tap it
   to go back into Music. When another sound starts (a beat, a video, the karaoke) the music pauses for it and comes back by itself
   when that sound ends, so one sound plays at a time. With the switch OFF, closing Music stops the music, as before. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 let bgOn=getLS('kanin-music-bg',true), explicitUntil=0, pausedFor=null, quietSince=0, under=getLS('kanin-mini-under',false), small=getLS('kanin-mini-min',false), last=null;
 const au=()=>$('mAudio');
 const scoreOn=()=>!!(window.MUSIC&&MUSIC.playing);
 const songOn=()=>{ const a=au(); return !!(a&&!a.paused&&!a.ended); };
 const bg=()=>scoreOn()||songOn();
 const explicit=(ms)=>{ explicitUntil=performance.now()+(ms||400); };
 const guarded=()=>bgOn&&bg()&&performance.now()>=explicitUntil;
 function otherPlaying(){ try{ if(window.PADSTUDIO&&PADSTUDIO.playing) return true; }catch(_){ } try{ const D=DJBOOTH.D; if(D.A.playing||D.B.playing) return true; }catch(_){ } try{ if(speechSynthesis.speaking) return true; }catch(_){ }
  for(const m of document.querySelectorAll('audio,video')){ if(m.id==='mAudio') continue; if(!m.paused&&!m.ended&&m.currentTime>0&&!m.muted&&m.volume>0) return true; } return false; }
 /* the guard on every way the app stops the music */
 function wrap(){ if(window.musicStop&&!window.musicStop.__kmini){ const real=window.musicStop; const w=function(keep){ if(guarded()){ const k=window.__kclaim; if(k&&k!=='score'){ if(under) return; const M=window.MUSIC||{}; pausedFor={kind:'score',mood:M.mood,ver:M.ver}; quietSince=0; return real.apply(this,arguments); } return; } return real.apply(this,arguments); }; w.__kmini=1; w.real=real; window.musicStop=w; }
  const a=au(); if(a&&!a.__kmini){ const rp=a.pause.bind(a); a.__kmini=1; a.realPause=rp; a.pause=function(){ if(guarded()&&songOn()){ const k=window.__kclaim; if(k&&k!=='media'){ if(under) return; pausedFor={kind:'song'}; quietSince=0; return rp(); } return; } return rp(); }; } }
 const realStop=()=>{ explicit(600); pausedFor=null; try{ (window.musicStop&&window.musicStop.real||window.musicStop)(); }catch(_){ } const a=au(); if(a){ try{ (a.realPause||a.pause).call(a); }catch(_){ } } };
 function resume(){ const p=pausedFor; pausedFor=null; if(!p) return; if(p.kind==='score'){ try{ musicStyle(p.mood,p.ver); }catch(_){ } } else { const a=au(); if(a) a.play().catch(()=>{}); } }
 /* the music screen's own buttons, the mini player and a stop with nothing else playing are real stops */
 document.addEventListener('click',e=>{ const t=e.target; if(!t.closest) return; if(t.closest('#musicDock')&&!t.closest('.kBar,[data-ka],#mBgTog')&&t.closest('button,li,select,input')) explicit(500);
  },true);
 
 /* the small player */
 const css=document.createElement('style'); css.textContent=`
#kMini{position:fixed;z-index:9740;left:calc(10px + env(safe-area-inset-left,0px));top:calc(8px + env(safe-area-inset-top,0px));display:flex;align-items:center;gap:4px;max-width:min(560px,calc(100vw - var(--kRailW,58px) - 150px));padding:4px 6px 4px 10px;border-radius:999px;background:linear-gradient(180deg,#2a1450,#150a2c);border:2px solid #b48cff;box-shadow:0 6px 20px rgba(0,0,0,.55);color:#fff;font:700 13px system-ui,sans-serif}
#kMini[hidden]{display:none!important} body.gated #kMini{display:none!important}
#kMini .mt{min-width:0;flex:1 1 auto;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
#kMini{cursor:pointer;min-height:40px} #kMini .go{flex:none;color:#ffe94a;font-weight:900;margin-left:4px}
#mBgTog.on{background:#7a3fd0!important;color:#fff!important;border-color:#ffe94a!important}
#kMini .mt small{color:#cdb8ff;font-weight:600}
#kMini button{min-width:40px;min-height:40px!important;padding:0 6px!important;border-radius:999px!important;font:900 16px system-ui,sans-serif!important;flex:none}
#kMini button.on{background:#ffe94a!important;color:#14163a!important}
#kMini button[data-mm="stop"]{background:#b3172f!important;color:#fff!important}
#kMini.min{padding:4px} #kMini.min .mt,#kMini.min button:not([data-mm="min"]){display:none}
#kMini .eq{display:inline-flex;gap:2px;align-items:flex-end;height:14px;margin-right:4px;vertical-align:middle}
#kMini .eq i{width:3px;background:#7dff8a;border-radius:1px;animation:kmEq 1s ease-in-out infinite}
#kMini .eq i:nth-child(2){animation-delay:.2s}#kMini .eq i:nth-child(3){animation-delay:.4s}
#kMini.paused .eq i{animation:none;height:3px;background:#888}
@keyframes kmEq{0%,100%{height:3px}50%{height:14px}}
@media (prefers-reduced-motion:reduce){ #kMini .eq i{animation:none;height:8px} }
@media (max-width:600px){ #kMini{max-width:calc(100vw - var(--kRailW,58px) - 120px);font-size:12px} #kMini button{min-width:36px;min-height:36px!important;font-size:14px!important} #kMini [data-mm="under"],#kMini [data-mm="open"]{display:none} }
@media (min-width:1700px){ #kMini{font-size:16px} #kMini button{min-width:50px;min-height:50px!important;font-size:20px!important} }`; document.head.appendChild(css);
 function title(){ if(songOn()||(pausedFor&&pausedFor.kind==='song')){ const q=window.MUSICQ; return '♪ '+((q&&q.title)||'Your song'); } const M=window.MUSIC||{}; const mood=(pausedFor&&pausedFor.mood)||M.mood||''; const v=(pausedFor&&pausedFor.ver!=null?pausedFor.ver:M.ver); return '♪ KAN-IN '+mood+' beat'+(v!=null?' · version '+(v+1):''); }
 function box(){ let b=$('kMini'); if(b) return b; b=document.createElement('button'); b.type='button'; b.id='kMini'; b.setAttribute('data-noul',''); b.hidden=true; document.body.appendChild(b);
  b.addEventListener('click',e=>{ e.stopPropagation(); try{ KRAIL.goTo('musicDock'); }catch(_){ } }); return b; }
 let sig='';
 function toggle(){ const st=$('mStop'); if(!st) return; let t=$('mBgTog'); if(!t){ t=document.createElement('button'); t.type='button'; t.id='mBgTog'; t.setAttribute('data-noul',''); st.insertAdjacentElement('afterend',t);
   t.addEventListener('click',e=>{ e.stopPropagation(); bgOn=!bgOn; putLS('kanin-music-bg',bgOn); toggle(); say(bgOn?'🎵 Background ON: the music keeps playing when you close Music. Come back here to turn it off.':'🎵 Background OFF: closing Music stops the music.'); }); }
  const tx=bgOn?'🎵 Background: ON':'🎵 Background: OFF'; if(t.textContent!==tx) t.textContent=tx; t.classList.toggle('on',bgOn); t.setAttribute('aria-pressed',String(bgOn)); t.title=bgOn?'ON: the music keeps playing when you close Music. Tap to turn it OFF.':'OFF: closing Music stops the music. Tap to turn it ON.'; }
 function paint(force){ wrap(); toggle(); const b=box(); const playingNow=bg(); const show=bgOn&&(playingNow||pausedFor)&&cur()!=='musicDock';
  if(b.hidden!==!show) b.hidden=!show; if(!show) return; const s=[playingNow,!!pausedFor,title()].join('|'); if(!force&&s===sig) return; sig=s;
  b.classList.toggle('paused',!playingNow); b.title='Playing in the background. Tap to go back into Music, where you turn it off.'; b.setAttribute('aria-label','Music playing in the background: '+title()+'. Tap to open Music.');
  b.innerHTML='<span class="eq" aria-hidden="true"><i></i><i></i><i></i></span><span class="mt">'+title()+(pausedFor?' · paused while another sound plays':' · in the background')+'</span><b class="go">↗ Music</b>'; }
 setInterval(()=>{ wrap(); if(pausedFor){ if(otherPlaying()){ quietSince=0; } else { if(!quietSince) quietSince=performance.now(); else if(performance.now()-quietSince>1200){ quietSince=0; resume(); } } } paint(false); },400);
 window.KMINI={get bgOn(){ return bgOn; },keeping:guarded,stop:realStop,get under(){ return under; },get pausedFor(){ return pausedFor; },paint:()=>paint(true)};
})();
