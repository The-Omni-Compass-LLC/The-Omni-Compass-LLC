(()=>{ /* ONE BOTTOM BAR: Menu, Freeze, Stop, Pad, Ask, Remote and Online in one row along the bottom, on every screen and every size.
   Nothing floats over the page any more; the page and every screen end above the bar. On a phone every screen opens full-screen. */
 const $=id=>document.getElementById(id);
 const css=document.createElement('style'); css.id='kDockCss';
 css.textContent=`
:root{--kDockH:calc(60px + env(safe-area-inset-bottom,0px));--rdockH:60px}
html body #rDock#rDock{position:fixed!important;left:0!important;right:0!important;bottom:0!important;top:auto!important;width:auto!important;max-width:none!important;height:var(--kDockH)!important;margin:0!important;padding:5px max(6px,env(safe-area-inset-right,0px)) calc(5px + env(safe-area-inset-bottom,0px)) max(6px,env(safe-area-inset-left,0px))!important;box-sizing:border-box!important;display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;align-items:stretch!important;justify-content:center!important;gap:5px!important;background:rgba(9,11,38,.97)!important;border-top:1px solid rgba(255,233,74,.35)!important;box-shadow:0 -6px 20px rgba(0,0,0,.5)!important;pointer-events:auto!important;z-index:9050!important;transform:none!important;overflow:visible!important}
html body #rDock#rDock #inMode,html body #rDock#rDock #kStop{display:contents!important}
html body #rDock#rDock #kWhat{display:none!important}
html body #rDock#rDock button{flex:1 1 0!important;min-width:0!important;max-width:140px!important;width:auto!important;height:auto!important;min-height:0!important;max-height:none!important;margin:0!important;padding:2px 3px!important;border-radius:12px!important;position:static!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:2px!important;line-height:1.05!important;white-space:nowrap!important;overflow:hidden!important;transform:none!important;letter-spacing:0!important;font-size:11px!important;box-shadow:none!important}
html body #rDock#rDock button[hidden]{display:none!important}
html body #rDock#rDock #lpMenu[hidden]{display:flex!important}
html body #rDock#rDock :is(#lpMenu,#kFreeze,#kStopBtn,#imPad,#askBtn,#kdRemote,#kdNet){display:flex!important}
html body #rDock#rDock button[data-kd-i]{font-size:0!important;color:transparent!important}
html body #rDock#rDock button[data-kd-i]::before{content:attr(data-kd-i)!important;display:block!important;font-size:19px!important;line-height:1!important;color:#fff!important;width:auto!important;height:auto!important;position:static!important;background:none!important;margin:0!important}
html body #rDock#rDock button[data-kd-i]::after{content:attr(data-kd-l)!important;display:block!important;font:700 11px/1.1 system-ui,sans-serif!important;color:#e6ebff!important;max-width:100%;overflow:hidden;text-overflow:ellipsis;position:static!important;background:none!important;margin:0!important;width:auto!important;height:auto!important}
html body #rDock#rDock #lpMenu{order:1!important}html body #rDock#rDock #kFreeze{order:2!important}html body #rDock#rDock #kStopBtn{order:3!important}html body #rDock#rDock #imPad{order:4!important}html body #rDock#rDock #askBtn{order:5!important}html body #rDock#rDock #kdRemote{order:6!important}html body #rDock#rDock #kdNet{order:7!important}html body #rDock#rDock #imTog{order:8!important}html body #rDock#rDock button{order:9}
html body #rDock#rDock #lpMenu{background:#ffe94a!important;border:1px solid #ffe94a!important}html body #rDock#rDock #lpMenu::before,html body #rDock#rDock #lpMenu::after{color:#14163a!important}
html body #rDock#rDock #kStopBtn{background:#b3172f!important;border:1px solid #ff6b81!important}
html body #rDock#rDock #kdNet.off{background:#5a1020!important}
html body #rmtBtn#rmtBtn,html body #kNet#kNet{display:none!important}
html body{padding-bottom:var(--kDockH)!important}
html body #tourMini{bottom:calc(var(--kDockH) + 8px)!important}
html body #tourTab.lp{bottom:calc(var(--kDockH) + 10px)!important;max-height:calc(100vh - var(--kDockH) - 24px)!important}
@media (max-width:760px){
 html body #rDock#rDock #imTog,html body #rDock#rDock #inMode button:not(#imPad){display:none!important}
 html body #rDock#rDock{gap:4px!important;padding-left:max(4px,env(safe-area-inset-left,0px))!important;padding-right:max(4px,env(safe-area-inset-right,0px))!important}
 html body #rDock#rDock button{padding:2px 1px!important}
 html body :is(#sbDock,#musicDock,#aivDock,#voiceDock,#langDock,#layDock,#craftDock,#mutDock,#mapDock):not([hidden]){top:0!important;left:0!important;right:0!important;bottom:var(--kDockH)!important;width:auto!important;height:auto!important;max-height:none!important;max-width:none!important;margin:0!important;border-radius:0!important;transform:none!important;z-index:8550!important}
 html body #askDock:not([hidden]){top:0!important;left:0!important;right:0!important;bottom:var(--kDockH)!important;width:auto!important;height:auto!important;max-height:none!important;max-width:none!important;margin:0!important;border-radius:0!important;transform:none!important}
}
html body :is(#pad.on,#swDock,#zodDock,#omniDock,#opsHub,#gamesDock,#tac,#libDock,#fileDock):not([hidden]){bottom:var(--kDockH)!important;height:auto!important;max-height:none!important}
@media (min-width:761px){ html body :is(#sbDock,#musicDock,#aivDock,#voiceDock,#langDock,#layDock,#craftDock,#mutDock,#mapDock,#askDock):not([hidden]){bottom:calc(var(--kDockH) + 8px)!important;height:auto!important;max-height:calc(100vh - var(--kDockH) - 16px)!important} }
@media (min-width:761px){ html body #rDock#rDock button{max-width:150px!important} html body #rDock#rDock button[data-kd-i]::after{font-size:12px!important} }
`;
 document.head.appendChild(css);
 const LB={lpMenu:['☰','Menu'],imPad:['🥁','Pad'],askBtn:['🎙','Ask'],imTog:['⌨','Play by'],kdRemote:['📡','Remote']};
 let label=function(){ const d=$('rDock'); if(!d) return;
  Object.keys(LB).forEach(id=>{ if(id==='lpMenu') return; const b=$(id); if(b&&d.contains(b)&&b.dataset.kdI!==LB[id][0]){ b.dataset.kdI=LB[id][0]; b.dataset.kdL=LB[id][1]; if(!b.getAttribute('aria-label')) b.setAttribute('aria-label',LB[id][1]); } });
  const f=$('kFreeze'); if(f){ const fr=/▶|release|move again/i.test((f.textContent||'')+' '+(f.getAttribute('aria-label')||'')); const i=fr?'▶':'❚❚', l=fr?'Move':'Freeze'; if(f.dataset.kdI!==i){ f.dataset.kdI=i; f.dataset.kdL=l; } }
  /* the Remote and the online dot join the bar */
  const rb=$('rmtBtn'); let rp=$('kdRemote'); if(rb&&!rp){ rp=document.createElement('button'); rp.type='button'; rp.id='kdRemote'; rp.title='Remote: control KAN-IN from another phone or computer'; rp.setAttribute('aria-label','Remote'); rp.setAttribute('data-noul',''); rp.addEventListener('click',e=>{ e.stopPropagation(); try{ $('rmtBtn').click(); }catch(_){} }); d.appendChild(rp); rp.dataset.kdI='📡'; rp.dataset.kdL='Remote'; }
  if(rp&&!rb) rp.remove();
  const nb=$('kNet'); let np=$('kdNet'); if(nb&&!np){ np=document.createElement('button'); np.type='button'; np.id='kdNet'; np.setAttribute('data-noul',''); np.addEventListener('click',e=>{ e.stopPropagation(); try{ if(window.KNET&&KNET.open) KNET.open(); else $('kNet').click(); }catch(_){ try{ $('kNet').click(); }catch(__){} } }); d.appendChild(np); }
  if(np){ let on=navigator.onLine!==false; try{ if(window.KNET&&KNET.isOn) on=!!KNET.isOn(); }catch(_){} const i=on?'🟢':'🔴', l=on?'Online':'Offline'; if(np.dataset.kdI!==i){ np.dataset.kdI=i; np.dataset.kdL=l; np.title=on?'Online: everything works. Tap to see or change.':'Offline: the app still works; tap to see what is limited.'; np.setAttribute('aria-label',l); np.classList.toggle('off',!on); } }
 }
 /* the daily reading waits as a small notice above the bar; it never covers the page */
 const c2=document.createElement('style'); c2.textContent=`#kDayChip{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(var(--kDockH) + 10px);z-index:9040;display:flex;gap:6px;align-items:center;max-width:calc(100vw - 24px);background:#16195a;border:2px solid #ffe94a;border-radius:999px;padding:4px;box-shadow:0 8px 22px rgba(0,0,0,.5)}#kDayChip[hidden]{display:none}#kDayChip button{background:none;border:0;color:#fff;font:600 14px system-ui,sans-serif;padding:8px 12px;border-radius:999px;cursor:pointer;white-space:nowrap}#kDayChip .kdcOpen b{color:#ffe94a}#kDayChip .kdcX{background:#2a2f7a;min-width:36px}`; document.head.appendChild(c2);
 /* Menu is always on the bar: from any screen it brings up the main menu; pressed again it closes it */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#lpMenu'); if(!b) return; e.stopImmediatePropagation(); e.preventDefault();
  if(window.LAUNCH==='open'){ try{ LAUNCHPAD.fold(); }catch(_){} }
  else { let on=false; try{ on=window.KBAR&&KBAR.onScreen&&KBAR.onScreen(); }catch(_){} try{ ['kManual','kMe','kCan','kNetCard','kDay'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){} if(on){ try{ GOHOME(); }catch(_){} } setTimeout(()=>{ try{ LAUNCHPAD.unfold(); }catch(_){} },on?250:0); }
  setTimeout(label,300); },true);
 const lbl0=label; label=function(){ lbl0(); try{ const c=$('kDayChip'); if(c&&!c.hidden&&window.KBAR&&KBAR.onScreen&&KBAR.onScreen()) c.hidden=true; }catch(_){ } const m=$('lpMenu'); if(!m) return; if(m.hidden) m.hidden=false; const open=window.LAUNCH==='open'; const i=open?'✕':'☰', l=open?'Close':'Menu'; if(m.dataset.kdI!==i){ m.dataset.kdI=i; m.dataset.kdL=l; m.setAttribute('aria-label',open?'Close the menu':'Open the menu'); } };
 label(); setInterval(()=>label(),1500); window.addEventListener('online',label); window.addEventListener('offline',label);
 try{ new MutationObserver(()=>label()).observe(document.body,{childList:true}); }catch(_){}
 try{ const lm=$('lpMenu'); if(lm) new MutationObserver(()=>label()).observe(lm,{attributes:true,attributeFilter:['hidden']}); }catch(_){}
 window.KDOCK={label};
})();
