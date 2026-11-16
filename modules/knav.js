(()=>{ /* CLOSE AND DO-IT-FOR-ME: Escape closes whatever is on top, one layer at a time (card, menu, then the screen);
   and a button that needs a missing step first offers "Do it for me", does that step, then finishes what was tapped. */
 const $=id=>document.getElementById(id);
 const shown=e=>!!(e&&!e.hidden&&getComputedStyle(e).display!=='none'&&getComputedStyle(e).visibility!=='hidden'&&e.getBoundingClientRect().height>0);
 const CARDS=['kFix','kDayChip','kManual','kMe','kCan','kNetCard','kDay','rmtPanel','libDock','fileDock','playMode','tpFull','kmDia','smDia','qpDone','kbusCard'];
 function closeBtnIn(el){ const c=[...el.querySelectorAll('button,[role=button]')].filter(b=>b.offsetParent!==null||getComputedStyle(b).position==='fixed'); return c.find(b=>b.dataset.ka==='close')||c.find(b=>/(Close|X)$/.test(b.id||''))||c.find(b=>/^(✕|×|✖)/.test((b.textContent||'').trim())&&(b.textContent||'').trim().length<24)||c.find(b=>/^(close|done|hide|not now)$/i.test((b.getAttribute('aria-label')||b.textContent||'').trim())); }
 function topThing(){ const cards=CARDS.map($).filter(shown); if(cards.length){ cards.sort((a,b)=>(+getComputedStyle(b).zIndex||0)-(+getComputedStyle(a).zIndex||0)); return {kind:'card',el:cards[0]}; }
  const tt=$('tourTab'); if(window.LAUNCH==='open'&&shown(tt)) return {kind:'menu',el:tt};
  const docks=[...document.querySelectorAll('.kHas,#gamesDock,#opsHub,#tac,#sbp')].filter(d=>shown(d)&&getComputedStyle(d).position==='fixed'&&(d.id!=='pad'||d.classList.contains('on')));
  if(docks.length){ docks.sort((a,b)=>(+getComputedStyle(b).zIndex||0)-(+getComputedStyle(a).zIndex||0)); return {kind:'screen',el:docks[0]}; }
  return null; }
 function closeThing(t){ if(!t) return; if(t.kind==='menu'){ try{ LAUNCHPAD.fold(); }catch(_){ } return; }
  if(t.kind==='screen'){ const b=t.el.querySelector('.kBar [data-ka="close"]')||closeBtnIn(t.el); if(b){ b.click(); return; } try{ GOHOME(); }catch(_){ t.el.hidden=true; } return; }
  const b=closeBtnIn(t.el); if(b) b.click(); if(shown(t.el)) t.el.hidden=true; }
 document.addEventListener('keydown',e=>{ if(e.key!=='Escape'||e.shiftKey) return; const a=document.activeElement; if(a&&((a.tagName==='INPUT'&&/^(text|search|email|url|tel|number|password)$/i.test(a.type||'text'))||a.tagName==='TEXTAREA'||a.isContentEditable)&&a.value){ a.blur(); return; } const t=topThing(); if(!t) return; setTimeout(()=>{ if(t.kind==='menu'?window.LAUNCH==='open':shown(t.el)) closeThing(t); },80); },true);
 /* the phone's Back button walks back the same way: when the address goes back, the top layer closes */
 window.addEventListener('popstate',()=>{ const t=topThing(); if(t&&t.kind==='card') setTimeout(()=>{ if(shown(t.el)) closeThing(t); },80); });

 /* DO IT FOR ME */
 let last=null, lastAt=0; document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('button,[role=button]'); if(!b||b.closest('#kFix')) return; last=b; lastAt=Date.now(); },true);
 const click=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const quickPick=()=>{ if(!click('qpBtn')) return false; setTimeout(()=>{ const d=$('qpDone'); if(d) d.hidden=true; },3400); return true; };
 const landNext=()=>{ try{ const i=nextOpen(); setLanding(i,randomK(i),'cannon'); try{ refreshAll(); }catch(_){ } try{ save(); }catch(_){ } return true; }catch(_){ return false; } };
 const RULES=[
  [/Quick Pick|Spin at least one canvas|Land some canvases|Spin a canvas first|Land at least three chapters|no story to rewrite|Finish this book first|Spin it first|Fire this canvas first|made from the story/i,()=>'⚡ Build my story now',quickPick,3700],
  [/Canvas (\d+) is locked\. Land canvas (\d+) first/i,m=>'⚡ Land canvas '+m[2]+' now',landNext,900],
  [/Auto-create|Make some music first/i,()=>'⚡ Make the music now',()=>click('cAuto'),1800],
  [/Score the board first/i,()=>'⚡ Score the board now',()=>click('sbScore'),1500]];
 const css=document.createElement('style'); css.textContent=`#kFix{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(var(--kDockH,60px) + 12px);z-index:9045;display:flex;flex-wrap:wrap;justify-content:center;gap:6px;align-items:center;width:max-content;max-width:calc(100vw - 20px);box-sizing:border-box;background:#16195a;border:2px solid #ffe94a;border-radius:16px;padding:8px 10px;box-shadow:0 10px 26px rgba(0,0,0,.55);color:#fff;font:600 14px/1.3 system-ui,sans-serif}#kFix[hidden]{display:none}#kFix .kfM{flex:1 1 220px;min-width:0}#kFix button{border:0;border-radius:999px;padding:9px 14px;font:700 14px system-ui,sans-serif;cursor:pointer}#kFix#kFix .kfGo{background:#ffe94a!important;color:#14163a!important;border:0!important}#kFix#kFix .kfX{background:#2a2f7a!important;color:#fff!important;min-width:38px}`; document.head.appendChild(css);
 let fixT=0, busy=false;
 function offer(msg){ if(busy) return; const r=RULES.find(x=>x[0].test(msg)); if(!r) return; const m=msg.match(r[0]); const target=Date.now()-lastAt<2500?last:null;
  let f=$('kFix'); if(!f){ f=document.createElement('div'); f.id='kFix'; f.setAttribute('role','alert'); document.body.appendChild(f); }
  f.innerHTML='<span class="kfM"></span><button type="button" class="kfGo" data-noul></button><button type="button" class="kfX" aria-label="Not now" data-noul>✕</button>';
  f.querySelector('.kfM').textContent=msg; f.querySelector('.kfGo').textContent=r[1](m); f.hidden=false; clearTimeout(fixT); fixT=setTimeout(()=>{ f.hidden=true; },10000);
  f.querySelector('.kfX').onclick=()=>{ f.hidden=true; };
  f.querySelector('.kfGo').onclick=()=>{ f.hidden=true; busy=true; const ok=r[2](m); setTimeout(()=>{ busy=false; if(ok&&target&&document.contains(target)) target.click(); },ok?r[3]:0); }; }
 function wrap(){ const T0=window.toast; if(typeof T0!=='function'||T0.__kfix) return !!(T0&&T0.__kfix); const w=function(m){ const out=T0.apply(this,arguments); try{ offer(String(m||'')); }catch(_){ } return out; }; w.__kfix=1; try{ window.toast=w; }catch(_){ } return window.toast===w; }
 if(!wrap()){ let n=0; const t=setInterval(()=>{ if(wrap()||++n>20) clearInterval(t); },500); }
 window.KNAV={top:topThing,close:()=>closeThing(topThing()),offer};
})();
