(()=>{ /* FIXES FROM THE WHOLE-APP INSPECTION (v191):
   1 · a guide that is running closes when you leave its screen from the rail or the Menu (on a phone it covered everything);
   2 · the builder's error note steps aside: small, at the bottom, and it hides itself after ten seconds;
   3 · every field, drop-down and 🎲 is big enough for a finger on a phone;
   4 · nothing scrolls sideways on a phone (the 🎮 controller, the karaoke labels). */
 const $=id=>document.getElementById(id);
 const guideOn=()=>{ const c=$('gtCard'); return c&&!c.hidden; };
 document.addEventListener('click',e=>{ const t=e.target; if(!t||!t.closest) return; if(!guideOn()) return; if(t.closest('#gtCard')) return;
  if(t.closest('#rDock button,#tourTab button,#lpMenu,#kPanel [data-kp="x"]')){ try{ GUIDE.end(); }catch(_){ } } },true);
 /* the full-screen prompter closes when you go somewhere else from the rail or the Menu */
 document.addEventListener('click',e=>{ const t=e.target; if(!t||!t.closest||!t.closest('#rDock button,#tourTab button,#lpMenu')) return; const f=$('tpFull'); if(!f||f.hidden||!f.getClientRects().length) return; const x=f.querySelector('[data-a="close"],.tpClose,#tpFullX,button[aria-label*="lose"]'); if(x) x.click(); else f.hidden=true; },true);
 /* the builder's note */
 const tidy=()=>{ const d=$('kaninDiagBox'); if(!d||d.dataset.tidy) return; d.dataset.tidy='1'; d.style.cssText+=';top:auto;bottom:calc(10px + env(safe-area-inset-bottom,0px));right:auto;max-width:min(440px,calc(100vw - 90px));font-size:12px;opacity:.95'; setTimeout(()=>{ try{ d.remove(); }catch(_){ } },10000); };
 try{ new MutationObserver(tidy).observe(document.body,{childList:true}); }catch(_){ }
 const css=document.createElement('style'); css.textContent=`
@media (pointer:coarse){
 html body select,html body input:not([type=checkbox]):not([type=radio]):not([type=range]):not([type=color]):not([type=hidden]){min-height:40px}
 html body button.dieBtn.dieBtn.dieBtn{min-width:36px!important;min-height:36px!important}
 html body button[aria-label^="Spin "][aria-label^="Spin "]{min-height:36px!important;min-width:36px!important}
 html body #toc2 button{min-height:40px!important}
 html body #sbDock .acts button.x,html body #sbDock .acts button{min-height:36px!important;min-width:36px!important}
 html body #zodDock input{min-height:40px!important}
 html body .themeChips button{min-height:36px!important;font-size:13.5px!important;padding:0 12px!important}
}
#kPadV{box-sizing:border-box;width:100%;max-width:min(720px,100%);--ps:min(120px,29vw)!important}
#kPadV.s{--ps:min(96px,25vw)!important}#kPadV.l{--ps:min(150px,31vw)!important}
#kKara .kkN{max-width:100%;box-sizing:border-box;flex-wrap:wrap;white-space:normal}
#kKara .kkN select,#kKara .kkN input{max-width:100%}
.kKeyMon{max-width:100%;box-sizing:border-box}`; document.head.appendChild(css);
})();
