(()=>{ /* 🧭 ♈ v222: the side rail carries Omni-Compass and LuvMyZodiac; Recipes lives in the Menu, in Find and in the AI */
 const $=id=>document.getElementById(id);
 const go=dock=>{ try{ const r=$('kRec'); if(r) r.hidden=true; }catch(_){ } try{ KRAIL.goTo(dock); }catch(_){ try{ KBAR.go(dock); }catch(__){ } } };
 const B=[['kdZod','♈','Zodiac','LuvMyZodiac: your sign, birth chart, moons, Chinese zodiac and matches','zodDock'],['kdOmni','🧭','Compass','Omni-Compass: the live engine, its monitors and controls','omniDock']];
 const css=document.createElement('style'); css.textContent='html body #rDock#rDock #kdZod,html body #rDock#rDock #kdOmni{order:5!important;display:flex!important}html body #rDock#rDock #kdZod.on,html body #rDock#rDock #kdOmni.on{background:#ffe94a!important}'; document.head.appendChild(css);
 function rail(){ const d=$('rDock'); if(!d) return; let cur=''; try{ cur=KRAIL.cur(); }catch(_){ }
  B.forEach(([id,i,l,t,dock])=>{ let b=$(id); if(!b){ b=document.createElement('button'); b.type='button'; b.id=id; b.setAttribute('data-noul',''); b.dataset.kdI=i; b.dataset.kdL=l; b.title=t; b.setAttribute('aria-label',t); b.addEventListener('click',e=>{ e.stopPropagation(); go(dock); });
    const after=id==='kdOmni'?$('kdZod'):($('kdKara')||$('kdStudio')); if(after&&after.parentNode===d&&after.nextSibling) d.insertBefore(b,after.nextSibling); else d.appendChild(b); }
   const on=cur===dock; if(b.classList.contains('on')!==on) b.classList.toggle('on',on); }); }
 setInterval(rail,800); rail();
 window.KDOCKS={rail,go};
})();
