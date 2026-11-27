(()=>{ /* ONE APP AT A TIME (v228). KAN-IN shows one app at a time: opening any app first closes the one that is open and stops its
   sound, the way a TV switches channels. Find and the Menu are not apps: they float over the open app and close when you pick one.
   The 16 pads, the keyboard and the DJ decks belong to the Studio: they stay while the Studio is open and close with it.
   Two layers keep the rule: every app's own open() is wrapped to close the others first, and a watcher closes any app left open
   underneath, keeping the newest. */
 const $=id=>document.getElementById(id);
 const OV={kAI:'KAI',kKara:'KKARA',kEasel:'KEASEL',kVG:'KVG',kRec:'KREC',kSocial:'KSOCIAL',kProj:'KPROJ',kProfile:'KPROFILE',kKnow:'KKNOW',kLock:'KLOCK',kJump:'KJUMP',kHumor:'KHUMOR',kOwner:'KOWNER',kNews:'KNEWS',kRelig:'KRELIG',kMarket:'KMARKET',kSports:'KSPORTS'};
 const DOCKS=['pad','swDock','zodDock','omniDock','gamesDock','libDock','fileDock','sbDock','musicDock','aivDock','voiceDock','langDock','layDock','craftDock','mutDock','mapDock','askDock'];
 const APPS=[...DOCKS,...Object.keys(OV)];
 const vis=id=>{ const e=$(id); if(!e||e.hidden) return false; if(id==='pad') return e.classList.contains('on'); const cs=getComputedStyle(e); if(cs.display==='none'||cs.visibility==='hidden') return false; const r=e.getBoundingClientRect(); return r.width>20&&r.height>20; };
 const openNow=()=>APPS.filter(vis);
 function stopSound(){ try{ if(window.KSTUDIO&&KSTUDIO.playing()){ const k=$('kStopBtn'); if(k) k.click(); } }catch(_){ } try{ KAUDIO.stopAll(); }catch(_){ } try{ speechSynthesis.cancel(); }catch(_){ } try{ PADSTUDIO.stop(); }catch(_){ }
  try{ ['A','B'].forEach(d=>{ if(DJBOOTH.D[d].playing) DJBOOTH.pause(d); }); }catch(_){ }
  document.querySelectorAll('audio,video').forEach(m=>{ try{ if(m.id==='mAudio'&&window.KMINI&&KMINI.bgOn) return; if(!m.paused) m.pause(); }catch(_){ } }); }
 const floatsShut=()=>{ try{ ['pads','keys','dj'].forEach(k=>{ if(KRAIL.FLOAT.isOpen&&KRAIL.FLOAT.isOpen(k)) KRAIL.FLOAT.close(k); }); }catch(_){ } };
 let busy=false;
 function closeApp(id){ if(!vis(id)) return; busy=true; try{
   const g=OV[id]; if(g&&window[g]&&typeof window[g].close==='function'){ try{ window[g].close(); }catch(_){ } }
   if(vis(id)){ const e=$(id); const x=e&&e.querySelector('.kBar [data-ka="close"],[data-kk="close"],[data-so="close"],[data-ko="close"],[data-vg="close"],[data-ea="close"],[data-ai="close"],[data-kh="close"],[data-kj="close"],.mClose');
    if(x&&x.getClientRects().length){ try{ x.click(); }catch(_){ } } }
   if(id==='pad'){ floatsShut(); if(vis('pad')){ try{ $('pad').classList.remove('on'); }catch(_){ } } }
   else if(vis(id)){ try{ $(id).hidden=true; }catch(_){ } }
  } finally { busy=false; } }
 function closeAllBut(keep){ openNow().forEach(id=>{ if(id!==keep) closeApp(id); }); try{ if(keep&&window.KFINDALL&&vis('kFind')) KFINDALL.close(); }catch(_){ } }
 /* layer 1: wrap every app's own open() so the others close first */
 function wrapOverlays(){ for(const [id,g] of Object.entries(OV)){ const o=window[g]; if(!o||typeof o.open!=='function'||o.open.__kone) continue; const f=o.open;
   const w=function(...a){ if(!vis(id)){ const others=openNow().filter(x=>x!==id); if(others.length){ stopSound(); others.forEach(closeApp); } } try{ if(vis('kFind')) KFINDALL.close(); }catch(_){ } return f.apply(this,a); };
   w.__kone=true; o.open=w; } }
 function wrapRail(){ const R=window.KRAIL; if(!R||typeof R.goTo!=='function'||R.goTo.__kone) return; const f=R.goTo;
  const w=function(id,...a){ const target=id; const ovs=openNow().filter(x=>OV[x]); const curDock=DOCKS.find(vis);
   if(target&&target!==curDock&&(ovs.length||curDock)){ if(curDock&&target!=='home'||ovs.length) stopSound(); ovs.forEach(closeApp); if(curDock==='pad'&&target!=='pad') floatsShut(); }
   try{ if(vis('kFind')) KFINDALL.close(); }catch(_){ } return f.call(this,id,...a); };
  w.__kone=true; R.goTo=w; }
 /* layer 2: the watcher keeps only the newest app open */
 const seen=new Map(); let tick=0;
 function watch(){ wrapOverlays(); wrapRail(); if(busy) return; tick++; const open=openNow(); open.forEach(id=>{ if(!seen.has(id)) seen.set(id,tick); }); [...seen.keys()].forEach(id=>{ if(!open.includes(id)) seen.delete(id); });
  if(open.length>1){ const keep=open.slice().sort((a,b)=>seen.get(b)-seen.get(a))[0]; open.forEach(id=>{ if(id!==keep) closeApp(id); }); }
  if(!vis('pad')&&!document.body.classList.contains('kDevOver')) floatsShut(); /* v242: the devices brought over Karaoke stay up */ }
 setInterval(watch,400); watch();
 window.KONE={open:openNow,closeAllBut,closeApp};
})();
