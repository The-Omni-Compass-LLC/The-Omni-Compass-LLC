(()=>{ /* 🥁 v223: the beat machine floats ON TOP of the sequencer and the mixing board, whole and in sight.
   · 🥁 Pads (rail, transport bar or Studio bar) brings it to the front and into view; a press while it is already in front puts it away;
   · it always fits the clear band between the transport bar and the Studio bar (it scrolls inside, never off the screen);
   · on a phone the 16 pads sit four across, so all 16 show at once; the section's notice moves to the end of the window. */
 const $=id=>document.getElementById(id);
 const css=document.createElement('style'); css.textContent=`
html body .kFloat.kFOn{max-height:var(--fmh,calc(100vh - 16px))!important}
html body #pad .pmain.kFloat.kFOn > div:not(.kFHead){display:flex!important;flex-direction:column}
html body #pad .pmain.kFloat.kFOn > div:not(.kFHead) > *{flex-shrink:0}
html body #pad .pmain.kFloat.kFOn .ocSec{order:99}
html body #pad .pmain.kFloat.kFOn #padGrid{order:-1}
@media (max-width:760px){
 html body #pad .pmain.kFloat.kFOn #padGrid{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:5px!important;width:100%!important}
 html body #pad .pmain.kFloat.kFOn #padGrid > .pd{width:auto!important;height:auto!important;min-height:0!important;aspect-ratio:1/0.82;padding:3px!important;font-size:12px!important}
 html body #pad .pmain.kFloat.kFOn #padGrid > .pd span{font-size:11px!important;line-height:1.1!important}
}
html body #pad .pmain.kFloat.kFOn #padGrid > .pd{height:var(--pdH,auto)!important}
html body #pad .pmain.kFloat.kFOn[style*="--pdH"] #padGrid > .pd{aspect-ratio:auto!important;min-height:0!important}
html body .kFloat.kFlash{box-shadow:0 0 0 4px #ffe94a,0 18px 44px rgba(0,0,0,.65)!important}`; document.head.appendChild(css);
 const vis=e=>!!e&&!e.hidden&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().height>0;
 function band(el){ let top=6, bottom=innerHeight-6; const bb=$('bbBar'), pad=$('pad');
  if(innerWidth<=760){ const xa=$('kXAll'); if(vis(xa)){ const r=xa.getBoundingClientRect(); if(r.bottom<innerHeight*0.25) top=Math.max(top,Math.round(r.bottom)+4); } } /* a phone: just under the app's Undo and Close, so the window's own buttons show */
  /* v264: the window is no longer held under the studio's transport bar: it goes anywhere, kept inside the screen */
  const rm=$('kRemote'); if(vis(rm)){ const r=rm.getBoundingClientRect(), e=el?el.getBoundingClientRect():null; const overlapX=!e||(r.left<e.right&&r.right>e.left); if(overlapX&&r.top>innerHeight*0.35) bottom=Math.min(bottom,Math.round(r.top)-6); }
  /* the track sequencer docks at the bottom of a wide screen: the pad and keyboard windows live in the space above it */
  const sq=$('kSeqWin'); if(innerWidth>760&&el&&el!==sq&&sq&&sq.classList.contains('kFOn')&&!sq.classList.contains('kFOff')&&!sq.classList.contains('kMin')){ const r=sq.getBoundingClientRect(); if(r.top>innerHeight*0.3&&r.height>60) bottom=Math.min(bottom,Math.round(r.top)-6); }
  if(bottom-top<160) bottom=Math.min(innerHeight-6,top+160); return {top,bottom}; }
 function fit(el,toTop){ if(!el||!el.classList.contains('kFOn')||el.classList.contains('kFOff')) return; const b=band(el); const avail=b.bottom-b.top; el.style.setProperty('--fmh',avail+'px');
  const g=el.querySelector('#padGrid')||el.querySelector('#kbKeys'); if(g&&!el.classList.contains('kMin')){
   if(g.id==='padGrid'){ /* a short band: the pads shrink so all sixteen still show */ el.style.removeProperty('--pdH'); const n0=Math.ceil(g.getBoundingClientRect().bottom-el.getBoundingClientRect().top+el.scrollTop+10); if(n0>avail){ const gh=g.getBoundingClientRect().height, rest=n0-gh, rowH=Math.max(32,Math.floor((avail-rest-15)/4)); el.style.setProperty('--pdH',rowH+'px'); } }
   const need=Math.ceil(g.getBoundingClientRect().bottom-el.getBoundingClientRect().top+el.scrollTop+10), fh=parseFloat(el.style.getPropertyValue('--fh'))||0; if(toTop==='size'||(fh&&fh<need)) el.style.setProperty('--fh',Math.min(avail,need)+'px'); }
  /* sideways too: never off the left edge, never under the rail, never a sliver */ { const W=innerWidth-(innerWidth<=760?58:76), q=el.getBoundingClientRect(), mw=Math.min(220,W-8); let w=q.width, x=q.left; if(w<mw||w>W-4){ w=Math.max(mw,Math.min(w,W-8)); el.style.setProperty('--fw',Math.round(w)+'px'); } if(x<0||x+w>W){ x=Math.max(0,Math.min(x,W-w)); el.style.setProperty('--fx',Math.round(x)+'px'); } }
  const r=el.getBoundingClientRect(); let y=toTop?b.top:r.top; const h=Math.min(el.scrollHeight+4,avail); if(y<b.top) y=b.top; if(y+h>b.bottom) y=Math.max(b.top,b.bottom-h); if(Math.abs(y-r.top)>1) el.style.setProperty('--fy',Math.round(y)+'px'); }
 const getEl=key=>{ try{ const F=KRAIL.FLOAT; return key==='pads'?document.querySelector('#pad .pmain'):key==='keys'?$('kbTop'):key==='dj'?$('djSec'):null; }catch(_){ return null; } };
 function inFront(el){ const r=el.getBoundingClientRect(); const pts=[]; for(const fx of [.12,.5,.88]) for(const fy of [.1,.5,.9]) pts.push([r.left+r.width*fx,r.top+r.height*fy]); return pts.every(([x,y])=>{ const t=document.elementFromPoint(Math.max(0,Math.min(innerWidth-1,x)),Math.max(0,Math.min(innerHeight-1,y))); return t&&el.contains(t); }); }
 function inView(el){ const r=el.getBoundingClientRect(), b=band(el); return r.top>=b.top-2&&r.bottom<=b.bottom+2&&r.left>=0&&r.right<=innerWidth; }
 /* a short screen: the Studio bar folds to its slim strip (its buttons repeat the transport bar's) so all 16 pads fit */
 function roomy(el){ const rm=$('kRemote'); if(!vis(rm)||rm.classList.contains('min')) return; el.__roomy=1; const g=el.querySelector('#padGrid')||el.querySelector('#kbKeys'); const b=band(el); const need=g?Math.ceil(g.getBoundingClientRect().bottom-el.getBoundingClientRect().top+el.scrollTop+10):310; if(b.bottom-b.top>=need) return; const m=rm.querySelector('[data-rm="min"]'); if(m){ m.click(); } }
 function flash(el){ el.classList.add('kFlash'); setTimeout(()=>el.classList.remove('kFlash'),700); }
 function wire(){ let F; try{ F=KRAIL.FLOAT; }catch(_){ return false; } if(!F||F.__padfit) return !!F; F.__padfit=1;
  const open0=F.open.bind(F);
  F.open=function(key){ open0(key); const el=getEl(key); if(!el) return; if(key==='pads'){ el.scrollTop=0; } requestAnimationFrame(()=>{ if(key==='pads'||key==='keys'){ el.scrollTop=0; el.__roomy=0; roomy(el); fit(el,'size'); if(innerWidth<=760) fit(el,true); } else fit(el); flash(el); }); setTimeout(()=>{ if(key==='pads') el.scrollTop=0; fit(el); },450); };
  F.toggle=function(key){ const el=getEl(key); if(F.isOpen(key)&&el&&inFront(el)&&inView(el)) F.close(key); else F.open(key); };
  return true; }
 if(!wire()){ const t=setInterval(()=>{ if(wire()) clearInterval(t); },500); }
 /* keep every open instrument inside the clear band when the screen turns, the Studio bar moves or the page scrolls */
 const refit=()=>{ ['pads','keys','dj'].forEach(k=>{ const el=getEl(k); if(el&&el.classList.contains('kFOn')&&!el.classList.contains('kFOff')){ if(!el.__roomy&&(k==='pads'||k==='keys')) roomy(el); fit(el); } }); };
 addEventListener('resize',()=>setTimeout(refit,120)); setInterval(()=>{ const p=$('pad'); if(p&&p.classList.contains('on')) refit(); },1000);
 document.addEventListener('scroll',()=>{ clearTimeout(refit.t); refit.t=setTimeout(refit,150); },true);
 window.KPADFLOAT={fit:k=>fit(getEl(k||'pads')),band:()=>band(getEl('pads')),inFront:k=>inFront(getEl(k||'pads')),inView:k=>inView(getEl(k||'pads'))};
})();
