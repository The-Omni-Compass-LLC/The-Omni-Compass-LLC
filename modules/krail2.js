(()=>{ /* 📐 v224: THE RIGHT-HAND RAIL, READABLE. No empty gap: every button grows into the whole column; ▶ Play sits at the bottom,
   right on top of ☰ Menu; the names are big enough to read (about 12px on a phone, up to 15px on a desktop) and the rail is a
   little wider on phones so no name is cut. */
 const css=document.createElement('style'); css.textContent=`
@media (max-width:760px){ :root{--kRailW:64px!important} }
html body #rDock#rDock#rDock{gap:2px!important;justify-content:stretch!important}
html body #rDock#rDock#rDock .kdSpace{flex:0 0 0px!important;min-height:0!important;height:0!important;margin:0!important;padding:0!important}
html body #rDock#rDock#rDock>button,html body #rDock#rDock#rDock #kStopBtn{flex:1 1 0px!important;min-height:0!important;max-height:96px!important;padding:1px 1px!important;gap:0!important;justify-content:center!important;overflow:hidden!important}
html body #rDock#rDock#rDock #kStopBtn{order:8!important;flex:1.25 1 0px!important}
html body #rDock#rDock#rDock #lpMenu{order:9!important;flex:1.25 1 0px!important;min-height:0!important}
html body #rDock#rDock#rDock>button::before,html body #rDock#rDock#rDock #kStopBtn::before{font-size:var(--rIco,clamp(14px,2.7vh,22px))!important;line-height:1.05!important}
html body #rDock#rDock#rDock>button::after,html body #rDock#rDock#rDock #kStopBtn::after{font-size:var(--rLab,clamp(10px,1.8vh,12.5px))!important;line-height:1.08!important;font-weight:800!important;letter-spacing:-.015em!important;white-space:nowrap!important;max-width:100%!important;overflow:hidden!important;text-overflow:clip!important}
`; document.head.appendChild(css);
 /* the fitter: from the rail's own height and the number of buttons it carries now, the biggest icon and name that fit whole */
 const cv=document.createElement('canvas').getContext('2d'); let last='';
 function fit(){ const d=document.getElementById('rDock'); if(!d) return; const bs=[...d.querySelectorAll(':scope > button, :scope #kStopBtn')].filter(b=>!b.hidden&&getComputedStyle(b).display!=='none');
  const n=bs.length; if(!n) return; const cs=getComputedStyle(d); const H=d.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom)-2*(n-1); const W=d.clientWidth-6;
  const per=H/(n+0.5); const big=innerWidth>=1700?1.35:innerWidth>=761?1.15:1;
  let lab=Math.min(15*big,Math.max(9,per*0.34)), ico=Math.min(28*big,Math.max(11,per*0.5));
  const b0=bs.find(b=>b.dataset.kdL)||bs[0], ac=getComputedStyle(b0,'::after'), bc=getComputedStyle(b0); const inner=b0.clientWidth-parseFloat(bc.paddingLeft)-parseFloat(bc.paddingRight)-4; cv.font=(ac.fontWeight||'800')+' 100px '+(ac.fontFamily||'system-ui,sans-serif'); const ls=parseFloat(ac.letterSpacing)||0; const longest=Math.max(...bs.map(b=>{ const t=b.dataset.kdL||''; return cv.measureText(t).width/100+(t.length*(ls/ (parseFloat(ac.fontSize)||12))); })); if(longest>0) lab=Math.min(lab,Math.max(8,inner)/longest);
  if(ico*1.05+lab*1.1+3>per){ lab=Math.max(8.5,Math.min(lab,(per-3)*0.4)); ico=Math.max(10,(per-3-lab*1.1)/1.05); }
  const key=n+'|'+Math.round(per*10)+'|'+W; if(key===last) return; last=key; d.style.setProperty('--rLab',lab.toFixed(2)+'px'); d.style.setProperty('--rIco',ico.toFixed(2)+'px'); }
 addEventListener('resize',()=>{ last=''; setTimeout(fit,60); }); setInterval(fit,700); setTimeout(fit,300);
 window.KRAILFIT=fit;
})();
