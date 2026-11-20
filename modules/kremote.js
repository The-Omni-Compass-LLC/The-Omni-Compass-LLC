(()=>{ /* THE REMOTE: one small control panel floating over every screen's canvas. Drag it anywhere (phone or desktop), shrink it to a
   bubble, open it again. ▶ Play · ■ Stop · ⏺ Record · ↶ Undo · 🔁 Loop · ✕ Close, plus the buttons that screen needs. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 const press=sel=>{ const b=document.querySelector(sel); if(b&&b.getClientRects().length){ b.click(); return true; } if(b){ b.click(); return true; } return false; };
 const NAME={pad:'Studio',kKara:'Karaoke',kEasel:'Easel',kAI:'AI',kSocial:'Social',kHumor:'Humor',kVG:'Video games',gamesDock:'Game',musicDock:'Music',aivDock:'Video',voiceDock:'Voices',langDock:'Language',zodDock:'LuvMyZodiac',swDock:'Songwriter',sbDock:'Storybook',sbp:'Storybook',craftDock:'Craft',mutDock:'Mutate',omniDock:'Compass',kJump:'Cannon',kOwner:'Owner’s word',kProj:'Projects',kKnow:'Knowledge library',kLock:'Lock & shuffle',kProfile:'Profile',libDock:'Library',fileDock:'Files',layDock:'Layers',mapDock:'Sections',askDock:'Ask',tac:'TAC-OPS',home:'Home'};
 const stopAll=()=>{ try{ if(window.KSTUDIO&&KSTUDIO.playing()){ press('#kStopBtn'); } }catch(_){ } try{ KAUDIO.stopAll(); }catch(_){ } try{ speechSynthesis.cancel(); }catch(_){ } try{ PADSTUDIO.stop(); }catch(_){ } try{ ['A','B'].forEach(d=>{ if(DJBOOTH.D[d].playing) DJBOOTH.pause(d); }); }catch(_){ } document.querySelectorAll('audio,video').forEach(m=>{ try{ if(!m.paused&&!m.muted) m.pause(); }catch(_){ } }); };
 /* 🎮 THE CONTROL PAD: ◀ ▲ ▼ ▶ move a big yellow light to the nearest button in that direction on whatever screen is open
    (scrolling the page when the next one is out of sight); OK presses the lit button. Nothing to aim, nothing small to hit. */
 const PADNAV=(()=>{ let curEl=null; const st=document.createElement('style'); st.textContent=`.kPadFocus{outline:4px solid #ffe94a!important;outline-offset:2px!important;box-shadow:0 0 0 8px rgba(255,233,74,.35)!important}
#kRemote .rmPad{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px;padding:6px 6px 0}
#kRemote .rmPad button{min-height:48px!important;min-width:0!important;padding:0!important;font:900 20px/1 system-ui,sans-serif!important;border-radius:12px!important}
#kRemote .rmPad .ok{background:#ffe94a!important;color:#14163a!important;font-size:16px!important}
#kRemote .rmHead button.on{background:#ffe94a!important;color:#14163a!important}
#kRemote .rmBtns button.more{background:#3b2f7a!important;border-color:#ffe94a!important}`; document.head.appendChild(st);
  const ok=e=>{ if(!e||!document.contains(e)||e.closest('#kRemote,#rDock,#kXAll')||e.disabled) return false; const r=e.getBoundingClientRect(); if(r.width<4||r.height<4||r.bottom<0||r.top>innerHeight||r.right<0||r.left>innerWidth) return false; const cs=getComputedStyle(e); if(cs.visibility==='hidden'||cs.pointerEvents==='none') return false;
   const t=document.elementFromPoint(Math.min(innerWidth-1,Math.max(0,r.left+r.width/2)),Math.min(innerHeight-1,Math.max(0,r.top+r.height/2))); return !!t&&(e===t||e.contains(t)||t.contains(e)); };
  const all=()=>[...document.querySelectorAll('button,a[href],input:not([type=hidden]),select,textarea,summary,[role=button],[tabindex]:not([tabindex="-1"])')].filter(ok);
  const mid=e=>{ const r=e.getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2}; };
  function clear(){ if(curEl) curEl.classList.remove('kPadFocus'); curEl=null; }
  function set(e){ clear(); curEl=e; e.classList.add('kPadFocus'); try{ e.focus({preventScroll:true}); }catch(_){ } try{ e.scrollIntoView({block:'nearest',inline:'nearest'}); }catch(_){ } }
  function scroller(e){ let p=e&&e.parentElement; while(p&&p!==document.body){ const cs=getComputedStyle(p); if(/(auto|scroll)/.test(cs.overflowY)&&p.scrollHeight>p.clientHeight+4) return p; p=p.parentElement; } return document.scrollingElement; }
  function pickFrom(L,dir){ const a=mid(curEl); let best=null,bv=1e9; L.forEach(e=>{ if(e===curEl||e.contains(curEl)||curEl.contains(e)) return; const b=mid(e); const dx=b.x-a.x, dy=b.y-a.y; let along,across; if(dir==='right'){ along=dx; across=dy; } else if(dir==='left'){ along=-dx; across=dy; } else if(dir==='down'){ along=dy; across=dx; } else { along=-dy; across=dx; } if(along<=3) return; const v=along+Math.abs(across)*2.2; if(v<bv){ bv=v; best=e; } }); return best; }
  function go(dir,retry){ if(dir==='ok'){ if(curEl&&document.contains(curEl)){ const e=curEl; e.click(); setTimeout(()=>{ if(!ok(e)) clear(); },350); } else say('🎮 Press an arrow to light a button, then OK.'); return; }
   const L=all(); if(!L.length) return say('🎮 No buttons on this screen.');
   if(!curEl||!ok(curEl)){ L.sort((a,b)=>{ const A=a.getBoundingClientRect(),B=b.getBoundingClientRect(); return (Math.round(A.top/20)-Math.round(B.top/20))||(A.left-B.left); }); return set(L[0]); }
   const best=pickFrom(L,dir); if(best) return set(best);
   if(!retry&&(dir==='down'||dir==='up')){ const sc=scroller(curEl); const before=sc.scrollTop; sc.scrollBy({top:(dir==='down'?1:-1)*innerHeight*0.55}); setTimeout(()=>{ if(sc.scrollTop!==before) go(dir,true); else say('🎮 That is the '+(dir==='down'?'bottom':'top')+'.'); },160); return; }
   say('🎮 Nothing further that way.'); }
  return {go,clear,lit:()=>curEl}; })();
 /* the screens that open over the page: the remote knows them too */
 const OVL={kRec:['Recipes',()=>{ try{ KREC.close(); }catch(_){ } }],kFind:['Find',()=>{ try{ KFINDALL.close(); }catch(_){ } }]};
 const ovl=()=>{ for(const id of Object.keys(OVL)){ const e=$(id); if(e&&!e.hidden&&getComputedStyle(e).display!=='none') return id; } return null; };
 const here=()=>ovl()||cur(); NAME.kRec='Recipes'; NAME.kFind='Find'; let lastHere='';
 const ACT={
  play:()=>{ try{ KSTUDIO.play(); }catch(_){ } },
  stop:()=>{ stopAll(); say('■ Stopped.'); },
  rec:()=>{ const id=cur(); if(id==='pad') return press('#bbRec')||say('Open the Studio first.'); if(id==='kKara') return press('#kKara [data-kk="rec"]'); try{ KKARA.open(); setTimeout(()=>press('#kKara [data-kk="rec"]'),500); }catch(_){ } },
  undo:()=>{ if(window.KUNDO) return KUNDO.any(); ACT.undoScreen(); },
  rew:()=>{ const id=cur(); if(id==='pad'&&press('#ktRew')) return say('⏮ Back to bar 1.'); const s=id==='home'?null:$(id); let n=0; (s?s.querySelectorAll('audio,video'):[]).forEach(m=>{ try{ m.currentTime=0; n++; }catch(_){ } }); say(n?'⏮ Back to the start.':'⏮ Nothing playing here to rewind.'); },
  save:()=>{ const id=cur(); const m={pad:'#padSave',kKara:'#kKara [data-kk="save"]'}; if(id==='kEasel'&&window.KEASEL){ KEASEL.save(); } else if(!(m[id]&&press(m[id]))){ const s=$(id); const b=s&&[...s.querySelectorAll('button')].find(b=>b.getClientRects().length&&(/save/i.test(b.id)||/^💾/.test(b.textContent.trim()))); if(b) b.click(); else { try{ KPROJ.open(); }catch(_){ } say('💾 Your work saves on this device as you go. Your projects are here.'); } } try{ KUNDO.saved(); }catch(_){ } },
  new:()=>{ const id=cur(); if(id==='kAI'&&window.KAI&&KAI.clear) return KAI.clear(); try{ KPROJ.open(); }catch(_){ } say('🆕 Pick what to start new: a story, a beat, a song, a drawing.'); },
  open:()=>{ try{ KPROJ.open(); }catch(_){ } say('📂 Your projects: tap one to open it.'); },
  undoScreen:()=>{ const id=cur(); const m={pad:'#padUndo',kKara:'#kKara [data-kk="undo"]',gamesDock:'#gmUndo',musicDock:'#mUndo'}; if(id==='kEasel'&&window.KEASEL) return KEASEL.undo(); if(m[id]&&press(m[id])) return; if(id==='pad'&&press('#kbUndo')) return; say('Nothing to undo here yet.'); },
  loop:()=>{ const id=cur(); if(id==='pad'||id==='kKara'){ if(press('#ktLoop')) return say('🔁 Loop switched.'); } if(id==='musicDock'&&press('#mShuf')) return; say('🔁 Loop works in the Studio and Karaoke.'); },
  close:()=>{ const o=ovl(); if(o){ OVL[o][1](); setTimeout(()=>paint(true),120); return; } const id=cur(); if(id==='home') return say('You are on the home page.'); const s=id==='pad'?$('pad'):$(id); const x=s&&s.querySelector('.kBar [data-ka="close"],[data-kk="close"],[data-so="close"],[data-ko="close"],[data-vg="close"],[data-ea="close"],[data-ai="close"]'); stopAll(); if(x) x.click(); else { try{ GOHOME(); }catch(_){ } } setTimeout(paint,300); }};
 /* the buttons each screen adds */
 const EXTRA={pad:[['🥁','Pads',()=>{ try{ KRAIL.FLOAT.toggle('pads'); }catch(_){ press('#kdIPads'); } }],['🎹','Keys',()=>{ try{ KRAIL.FLOAT.toggle('keys'); }catch(_){ press('#kdIKeys'); } }],['🎧','DJ',()=>{ try{ KRAIL.FLOAT.toggle('dj'); }catch(_){ press('#kdIDJ'); } }],['🎤','Sing',()=>{ try{ KKARA.open(); }catch(_){ } }],['×2','Double loop',()=>{ try{ KLOCK.double(); }catch(_){ } }],['🔒','Lock & shuffle',()=>{ try{ KLOCK.open('beat'); }catch(_){ } }]],
  kKara:[['📱','Phone rec',()=>press('#kkCap')],['🎚','Layers',()=>{ const l=$('kkLayers'); if(l) l.scrollIntoView({block:'start'}); else say('Record a take first.'); }],['🏗','Build song',()=>press('#kKara [data-kk="build"]')]],
  kEasel:[['🧹','Clear',()=>KEASEL&&KEASEL.clear()],['💾','Save',()=>KEASEL&&KEASEL.save()],['🌐','Post',()=>KEASEL&&KEASEL.post()]],
  kAI:[['🧹','New chat',()=>window.KAI&&KAI.clear()]],
  kLock:[['🔀','Partial',()=>press('#kLock [data-lk="part"]')],['🎲','Complete',()=>press('#kLock [data-lk="full"]')]],
  kKnow:[['🔎','Search',()=>{ const q=$('knQ'); if(q) q.focus(); }]],
  kProfile:[['✏️','Edit',()=>press('#kProfile [data-pf="edit"]')],['➕','Post',()=>press('#kProfile [data-pf="post"]')],['🎶','Song',()=>press('#kProfile [data-pf="songplay"]')]],
  kHumor:[['🔊','Read',()=>press('#kHumor [data-kh="daysay"]')],['🎲','Joke',()=>press('#kHumor [data-kh="rnd"]')]],
  kRec:[['🔎','Search',()=>{ const q=$('rcQ'); if(q){ q.focus(); q.select&&q.select(); } }],['🌍','Cultures',()=>press('#kRec [data-tab="cul"]')],['🎓','School',()=>{ try{ KREC.school(); }catch(_){ } }],['⭐','Favorites',()=>press('#kRec [data-tab="fav"]')],['🛒','List',()=>press('#kRec [data-tab="list"]')]],
  kFind:[['🔎','Type',()=>{ const q=$('fdQ'); if(q) q.focus(); }],['🤖','Ask AI',()=>press('#kFind [data-fd="ai"]')]],
  gamesDock:[['🕹','All games',()=>{ try{ KVG.open(); }catch(_){ } }]],
  home:[['🎛','Studio',()=>{ try{ KRAIL.goTo('pad'); }catch(_){ } }],['🎤','Karaoke',()=>{ try{ KKARA.open(); }catch(_){ } }],['🎨','Easel',()=>{ try{ KEASEL.open(); }catch(_){ } }],['🤖','AI',()=>{ try{ KAI.open(); }catch(_){ } }]]};
 const css=document.createElement('style'); css.textContent=`
#kRemote{position:fixed;z-index:9750;left:var(--rx,10px);top:var(--ry,auto);bottom:var(--rb,calc(12px + env(safe-area-inset-bottom,0px)));background:rgba(12,10,36,.94);border:2px solid #ffe94a;border-radius:16px;box-shadow:0 8px 28px rgba(0,0,0,.55);color:#fff;font:700 12px system-ui,sans-serif;max-width:calc(100vw - var(--kRailW,58px) - 16px);touch-action:none;user-select:none;-webkit-user-select:none}
#kRemote .rmHead{display:flex;align-items:center;gap:6px;padding:4px 6px 0 8px;cursor:grab}
#kRemote .rmHead b{flex:1;color:#ffe94a;font:900 11.5px ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#kRemote .rmHead button{min-height:26px!important;min-width:28px!important;padding:0 6px!important;border-radius:8px;font:900 13px system-ui,sans-serif}
#kRemote .rmBtns{display:flex;flex-wrap:wrap;gap:4px;padding:6px}
#kRemote .rmBtns button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;min-width:48px;min-height:48px!important;padding:2px 4px!important;border-radius:12px;font:800 10.5px system-ui,sans-serif}
#kRemote .rmBtns button span{font-size:19px;line-height:1}
#kRemote .rmBtns button[data-r="stop"]{background:#b3172f!important}
#kRemote .rmBtns button[data-r="play"]{background:#137a3f!important}
#kRemote .rmBtns button[data-r="rec"]{background:#7a0f22!important}
#kRemote.min .rmBtns{display:none}
#kRemote.min .rmHead b{display:none}
#kRemote[hidden]{display:none!important}
#kRemote.easy .rmBtns button{min-width:clamp(64px,6vw,128px);min-height:clamp(64px,6vw,128px)!important;font-size:clamp(12px,1vw,20px)}
#kRemote.easy .rmBtns button span{font-size:clamp(24px,2.2vw,46px)}
@media (max-width:600px){ #kRemote:not(.easy) .rmBtns button{min-width:44px;min-height:44px!important;font-size:9.5px} #kRemote:not(.easy) .rmBtns button span{font-size:17px} }
@media (min-width:1700px){ #kRemote:not(.easy) .rmBtns button{min-width:66px;min-height:66px!important;font-size:13.5px} #kRemote:not(.easy) .rmBtns button span{font-size:25px} #kRemote .rmHead b{font-size:15px} }
@media (min-width:2500px){ #kRemote:not(.easy) .rmBtns button{min-width:88px;min-height:88px!important;font-size:17px} #kRemote:not(.easy) .rmBtns button span{font-size:34px} #kRemote .rmHead b{font-size:19px} }`; document.head.appendChild(css);
 let min=getLS('kanin-remote-min',false), shownFor='', gameOpen=false; const GAMESCR=new Set(['gamesDock','kVG']); const isMin=id=>GAMESCR.has(id)?!gameOpen:id==='home'?!homeOpen:min; let homeOpen=false, moreOpen=false, padOn=getLS('kanin-remote-pad',false); /* on a game screen the remote starts as its bubble so it never covers the play area */
 function box(){ let r=$('kRemote'); if(r) return r; r=document.createElement('div'); r.id='kRemote'; r.setAttribute('role','toolbar'); r.setAttribute('aria-label','Remote control'); document.body.appendChild(r);
  const g=getLS('kanin-remote-pos',null); if(g){ r.style.setProperty('--rx',g.x+'px'); r.style.setProperty('--ry',g.y+'px'); r.style.setProperty('--rb','auto'); }
  r.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); if(b.dataset.rm==='min'){ if(GAMESCR.has(here())){ gameOpen=!gameOpen; return paint(true); } if(here()==='home'){ homeOpen=!homeOpen; return paint(true); } min=!min; putLS('kanin-remote-min',min); return paint(true); } if(b.dataset.rm==='hide'){ putLS('kanin-remote-off',true); r.hidden=true; return say('🎛 Remote hidden. Turn it back on in the ⚙ Panel or the Menu.'); } if(b.dataset.rm==='pad'){ padOn=!padOn; putLS('kanin-remote-pad',padOn); if(!padOn) PADNAV.clear(); return paint(true); } if(b.dataset.rm==='more'){ moreOpen=!moreOpen; return paint(true); } if(b.dataset.nav){ return PADNAV.go(b.dataset.nav); } const k=b.dataset.r; if(k&&ACT[k]) return ACT[k](); const x=b.dataset.x; if(x!=null){ const L=EXTRA[here()]||[]; const f=L[+x]; if(f) f[2](); } });
  let drag=null; r.addEventListener('pointerdown',e=>{ if(!e.target.closest('.rmHead')||e.target.closest('button')) return; const rc=r.getBoundingClientRect(); drag={dx:e.clientX-rc.left,dy:e.clientY-rc.top}; try{ r.setPointerCapture(e.pointerId); }catch(_){ } });
  r.addEventListener('pointermove',e=>{ if(!drag) return; const W=innerWidth-(parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58), x=Math.max(0,Math.min(W-80,e.clientX-drag.dx)), y=Math.max(0,Math.min(innerHeight-40,e.clientY-drag.dy)); r.style.setProperty('--rx',x+'px'); r.style.setProperty('--ry',y+'px'); r.style.setProperty('--rb','auto'); });
  const up=()=>{ if(!drag) return; drag=null; const rc=r.getBoundingClientRect(); putLS('kanin-remote-pos',{x:Math.round(rc.left),y:Math.round(rc.top)}); }; r.addEventListener('pointerup',up); r.addEventListener('pointercancel',up);
  return r; }
 function paint(force){ const r=box(); const id=here(); if(id!==lastHere){ lastHere=id; moreOpen=false; } const menuOpen=(()=>{ const t=$('tourTab'); return t&&t.getClientRects().length&&getComputedStyle(t).display!=='none'&&!t.hidden&&t.getBoundingClientRect().width>40; })();
  r.hidden=getLS('kanin-remote-off',false)||menuOpen||(innerWidth<700&&(id==='kAI'||(document.activeElement&&/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)&&!/^(range|checkbox|radio|button|file|color)$/.test(document.activeElement.type||''))))||(id==='pad'&&(()=>{ try{ return KLEVEL.get()==='easy'; }catch(_){ return false; } })()); if(r.hidden) return; const LVL=(()=>{ try{ return KLEVEL.get(); }catch(_){ return 'avg'; } })(); if(!GAMESCR.has(id)) gameOpen=false; const mn=isMin(id); const key=id+'|'+mn+'|'+LVL+'|'+moreOpen+'|'+padOn+'|'+(innerWidth<700); if(!force&&key===shownFor) return; shownFor=key; r.classList.toggle('min',mn);
  const base=LVL==='easy'?[['play','▶','Play'],['stop','■','Stop'],['rec','⏺','Record'],['undo','↶','Undo'],['save','💾','Save'],['close','✕','Close']]:[['rew','⏮','Rewind'],['play','▶','Play'],['stop','■','Stop'],['rec','⏺','Record'],['undo','↶','Undo'],['loop','🔁','Loop'],['save','💾','Save'],['new','🆕','New'],['open','📂','Open'],['close','✕','Close']];
  const all=EXTRA[id]||[]; const small=LVL==='easy'||innerWidth<700; const ex=small&&!moreOpen?[]:all; /* on a phone (and in Easy) the screen's own buttons wait behind ➕ More */ r.classList.toggle('easy',LVL==='easy');
  r.innerHTML='<div class="rmHead" title="Drag me anywhere"><b>⠿ 🎛 '+(NAME[id]||'Remote')+'</b>'+(mn?'':'<button type="button" data-rm="pad" class="'+(padOn?'on':'')+'" title="Control pad: arrows move between the buttons on the screen, OK presses one" data-noul>🎮</button>')+'<button type="button" data-rm="min" title="'+(mn?'Open the remote':'Shrink the remote')+'" data-noul>'+(mn?'🎛':'▁')+'</button>'+(mn?'':'<button type="button" data-rm="hide" title="Hide the remote" data-noul>✕</button>')+'</div>'+(padOn&&!mn?'<div class="rmPad"><button type="button" data-nav="left" aria-label="Left" data-noul>◀</button><button type="button" data-nav="up" aria-label="Up" data-noul>▲</button><button type="button" data-nav="ok" class="ok" aria-label="Press the lit button" data-noul>OK</button><button type="button" data-nav="down" aria-label="Down" data-noul>▼</button><button type="button" data-nav="right" aria-label="Right" data-noul>▶</button></div>':'')+'<div class="rmBtns">'+base.filter(b=>!(id==='home'&&(b[0]==='close'||b[0]==='undo'||b[0]==='loop'))).map(([k,i,l])=>'<button type="button" data-r="'+k+'" title="'+l+'" data-noul><span>'+i+'</span>'+l+'</button>').join('')+ex.map(([i,l],n)=>'<button type="button" data-x="'+n+'" title="'+l+'" data-noul><span>'+i+'</span>'+l+'</button>').join('')+(small&&all.length?'<button type="button" data-rm="more" class="more" title="'+(moreOpen?'Fewer buttons':'This screen’s own buttons')+'" data-noul><span>'+(moreOpen?'➖':'➕')+'</span>'+(moreOpen?'Less':'More')+'</button>':'')+'</div>'; }
 setInterval(()=>paint(false),400);
 /* the landing page never shows the remote: hide it the moment home is reached, not on the next tick */
 const homeNow=()=>{ const r=$('kRemote'); if(r) r.hidden=true; shownFor=''; [60,300].forEach(t=>setTimeout(()=>paint(true),t)); };
 try{ const gh=window.GOHOME; if(gh&&!gh.__krm){ const w=function(){ const r=gh.apply(this,arguments); homeNow(); return r; }; w.__krm=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu,[data-ka="close"],[data-kk="close"],[data-kn="close"],[data-lkx]')) homeNow(); },true);
 window.addEventListener('kanin',e=>{ if(e.detail==='gate-open') homeNow(); });
 window.KREMOTE={undoScreen:()=>ACT.undoScreen(),show:()=>{ putLS('kanin-remote-off',false); paint(true); },hide:()=>{ putLS('kanin-remote-off',true); paint(true); },act:ACT};
 /* ✕ CLOSE, ALWAYS IN REACH: on every screen but home a close button stays pinned at the top right, however far the page is
    scrolled and even with the remote hidden. It stops every sound and every reading voice and goes home. Escape does the same. */
 const xcss=document.createElement('style'); xcss.textContent='#kXAll{position:fixed;z-index:9760;top:calc(8px + env(safe-area-inset-top,0px));right:calc(var(--kRailW,58px) + 10px);min-height:44px!important;min-width:44px;padding:4px 12px!important;border-radius:999px!important;background:#b3172f!important;color:#fff!important;font:900 15px system-ui,sans-serif!important;border:2px solid #fff!important;box-shadow:0 4px 16px rgba(0,0,0,.5)}#kXAll[hidden]{display:none!important}body.gated #kXAll{display:none!important}'; document.head.appendChild(xcss);
 function closeAll(){ stopAll(); const id=cur(); if(id!=='home'){ try{ ACT.close(); }catch(_){ } setTimeout(()=>{ if(cur()!=='home'){ try{ GOHOME(); }catch(_){ } } try{ speechSynthesis.cancel(); }catch(_){ } },250); } }
 function paintX(){ let b=$('kXAll'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kXAll'; b.setAttribute('data-noul',''); b.setAttribute('aria-label','Close and go home'); b.textContent='✕ Close'; b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); closeAll(); }); document.body.appendChild(b); }
  const id=cur(); const menuOpen=(()=>{ const t=$('tourTab'); return t&&t.getClientRects().length&&getComputedStyle(t).display!=='none'&&t.getBoundingClientRect().width>40; })(); const hide=id==='home'||menuOpen; if(b.hidden!==hide) b.hidden=hide; }
 setInterval(paintX,400);
 document.addEventListener('keydown',e=>{ if(e.key!=='Escape') return; const t=e.target; if(t&&/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return; if(cur()!=='home') closeAll(); });
 window.KREMOTE.closeAll=closeAll;
})();
