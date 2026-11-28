(()=>{ /* ⌨ KEYBOARD SHORTCUTS FOR EVERY SCREEN AND TAB (v256). Hold Alt (Option on a Mac) and press a letter to open any screen or platform,
   on any keyboard layout (the key's position is read, not the letter printed on it), and never in the way of the split keyboard, which
   plays the pads and the piano on plain keys: Alt+S the studio, Alt+G games, Alt+Z LuvMyZodiac, Alt+Y the live zodiac ring, Alt+K
   karaoke, and so on. Alt+[ and Alt+] step to the previous or next tab on the screen in front, Alt+1 to Alt+9 open that tab, Esc closes
   the page in front and Alt+/ shows this list. Alt+D, Alt+E and Alt+F are left to the browser, and Alt+arrows are not used, because
   browsers keep those for their own menus and for going back and forward. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const click=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const go=id=>{ try{ (window.KBEAT&&KBEAT.closeAll)&&KBEAT.closeAll(); }catch(_){ } try{ KRAIL.goTo(id); return true; }catch(_){ return false; } };
 const call=(o,f)=>()=>{ try{ (window.KBEAT&&KBEAT.closeAll)&&KBEAT.closeAll(); }catch(_){ } try{ const O=window[o]; if(O&&O[f]){ O[f](); return true; } }catch(_){ } return false; };
 /* [code, key shown, what it opens, action] */
 const MAP=[
  ['KeyH','H','🏠 Home',()=>click('kdHome')],['KeyM','M','☰ Menu',()=>click('lpMenu')],['KeyQ','Q','🔎 Find (ask or search)',()=>click('kdFind')],
  ['KeyS','S','🎛 Studio: beat machine, sequencer, mixer',()=>click('kdStudio')||go('pad')],['KeyG','G','🎮 Games',()=>click('kdGames')||go('gamesDock')],
  ['KeyB','B','🎯 Cannon Beat',call('KCBEAT','open')],['KeyK','K','🎤 Karaoke',()=>click('kdKara')||go('kKara')],
  ['KeyZ','Z','♈ LuvMyZodiac',()=>click('kdZod')||go('zodDock')],['KeyY','Y','♈ The Zodiac Ring, live sky',call('KZRING','page')],
  ['KeyC','C','🧭 Omni-Compass',()=>click('kdOmni')||go('omniDock')],['KeyA','A','🤖 AI',()=>click('kdAI')||go('kAI')],
  ['KeyP','P','📁 Projects',()=>click('kdProj')],['KeyO','O','👤 Your page and social',call('KACCT','open')],
  ['KeyL','L','📚 Knowledge Library',call('KKNOW','open')],['KeyR','R','✝️ Cultures & Religion',call('KRELIG','open')],
  ['KeyN','N','📰 Current News',call('KNEWS','open')],['KeyT','T','📈 Stock Market',call('KMARKET','open')],
  ['KeyX','X','🏟 Sports',call('KSPORTS','open')],['KeyV','V','🧾 Services',call('KSERVICES','open')],
  ['KeyI','I','⚖️ Legal & Safety',call('KLEGAL','open')],
  ['Digit0','0','🌐 The Doorway: every outside platform',call('KDOOR','open')],['Minus','-','💃 Dance Karaoke',call('KDANCE','open')],['Equal','=','🎼 Song Arranger',call('KARR','open')],
  ['KeyU','U','⬆ Upload a sound or file',()=>tool('up')],['KeyW','W','⬇ Save this page',()=>tool('save')],['KeyJ','J','🌐 Language',()=>tool('lang')]].filter(r=>r[2]);
 const tool=t=>{ const b=document.querySelector('#kToolsPop [data-t="'+t+'"]'); if(b){ b.click(); return true; } say('The tools are still loading.'); return false; };
 /* the page or screen in front, and its tabs */
 const OVL=['kArr','kReligX','kZRingPage','kSndSheet','kLegal','kAcct','kServices','kSports','kNews','kMarket','kRelig','kKnow','kFind'];
 function front(){ for(const id of OVL){ const x=$(id); if(x&&!x.hidden&&x.getClientRects().length) return x; } let c=''; try{ c=KRAIL.cur(); }catch(_){ } return (c&&c!=='home'&&$(c))||document.querySelector('.wrap')||document.body; }
 const TABSEL='[role=tab],.rxTabs button[data-rx="tab"],.svRow button[data-sv="cat"],.kTabs button,.vgTabs button,.mtabs button,.tabs button,[data-tab],.spRow button,.nwRow button,.mkRow button,.rgRow button,.kaTabs button,[data-ka-tab]';
 function tabs(){ const f=front(); return [...f.querySelectorAll(TABSEL)].filter(b=>b.getClientRects().length&&!b.disabled); }
 const isOn=b=>b.classList.contains('on')||b.getAttribute('aria-selected')==='true'||b.getAttribute('aria-pressed')==='true';
 function stepTab(d){ const T=tabs(); if(!T.length){ say('This screen has no tabs.'); return; } let i=T.findIndex(isOn); i=i<0?(d>0?0:T.length-1):(i+d+T.length)%T.length; T[i].click(); T[i].focus&&T[i].focus({preventScroll:false}); say('Tab '+(i+1)+' of '+T.length+': '+T[i].textContent.trim().slice(0,40)); }
 function nthTab(n){ const T=tabs(); if(!T[n]){ say('This screen has '+T.length+' tab'+(T.length===1?'':'s')+'.'); return; } T[n].click(); say('Tab '+(n+1)+': '+T[n].textContent.trim().slice(0,40)); }
 function closeFront(){ for(const id of ['kKeysPop','kLangPop','kToolsPop']){ const x=$(id); if(x&&!x.hidden){ x.hidden=true; const b=$('kToolsBtn'); if(id==='kToolsPop'&&b) b.classList.remove('on'); return true; } }
  for(const id of OVL){ const x=$(id); if(x&&!x.hidden&&x.getClientRects().length){ const b=x.querySelector('[data-ar="x"],[data-rx="x"],[data-zp="x"],[data-sv="x"],[data-lg="x"],[data-ss="x"],button[aria-label*="Close"],button[title*="Close"]'); if(b) b.click(); else x.hidden=true; return true; } } const pop=$('kToolsPop'); if(pop&&!pop.hidden){ pop.hidden=true; return true; } const kp=$('kKeysPop'); if(kp&&!kp.hidden){ kp.hidden=true; return true; } return false; }
 const typing=t=>t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable);
 addEventListener('keydown',e=>{
  if(e.key==='Escape'&&!e.altKey&&!e.ctrlKey&&!e.metaKey){ if(closeFront()){ e.preventDefault(); } return; }
  if(!e.altKey||e.ctrlKey||e.metaKey) return; if(typing(e.target)&&!/^(Slash|BracketLeft|BracketRight)$/.test(e.code)) return;
  const c=e.code||'';
  if(c==='Slash'){ e.preventDefault(); show(); return; }
  if(c==='BracketLeft'){ e.preventDefault(); stepTab(-1); return; } if(c==='BracketRight'){ e.preventDefault(); stepTab(1); return; }
  const dm=c.match(/^Digit([1-9])$/); if(dm){ e.preventDefault(); nthTab(+dm[1]-1); return; }
  const r=MAP.find(x=>x[0]===c); if(r){ e.preventDefault(); e.stopPropagation(); const ok=r[3](); if(ok===false) say(r[2]+' is not ready yet.'); }
 },true);
 /* the list of every shortcut */
 const css=document.createElement('style'); css.textContent=`
#kKeysPop{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9795;background:rgba(5,4,16,.88);display:flex;align-items:flex-start;justify-content:center;overflow-y:auto;padding:calc(16px + env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-left,0px)) 30px}
#kKeysPop[hidden]{display:none!important}
#kKeysPop .kkIn{max-width:980px;width:100%;background:#141833;border:2px solid #ffe94a;border-radius:6px 18px 6px 18px;padding:16px;color:#eef;font:15px/1.5 system-ui,sans-serif}
#kKeysPop h2{margin:0 0 6px;color:#ffe94a;font:900 22px system-ui,sans-serif}
#kKeysPop h3{margin:12px 0 4px;color:#ffd27a;font:900 16px system-ui,sans-serif}
#kKeysPop .kkGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:4px 14px}
#kKeysPop .kkRow{display:flex;gap:8px;align-items:center;min-height:30px}
#kKeysPop kbd{display:inline-block;min-width:22px;padding:2px 7px;border-radius:6px;background:#2b2470;border:1px solid #8f86ff;box-shadow:0 2px 0 #0a0820;font:800 13px ui-monospace,monospace;color:#fff;text-align:center}
#kKeysPop .kkTop{display:flex;justify-content:space-between;align-items:center;gap:8px}
#kKeysPop button{min-height:44px;padding:0 16px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif}`; document.head.appendChild(css);
 const mac=/Mac|iPhone|iPad/.test(navigator.platform||navigator.userAgent); const ALT=mac?'⌥ Option':'Alt';
 function show(){ let p=$('kKeysPop'); if(!p){ p=document.createElement('div'); p.id='kKeysPop'; p.setAttribute('role','dialog'); p.setAttribute('aria-label','Keyboard shortcuts'); document.body.appendChild(p); p.addEventListener('click',e=>{ if(e.target===p||e.target.closest('[data-kk="x"]')){ e.stopPropagation(); p.hidden=true; } }); }
  const k=s=>s.split('+').map(x=>'<kbd>'+esc(x)+'</kbd>').join('+');
  const row=(keys,what)=>'<div class="kkRow">'+k(keys)+'<span>'+esc(what)+'</span></div>';
  p.innerHTML='<div class="kkIn"><div class="kkTop"><h2>⌨ Keyboard shortcuts</h2><button type="button" data-kk="x" data-noul>✕ Close</button></div><p>Hold <kbd>'+ALT+'</kbd> and press a key. The keys are read by position, so they work on any keyboard layout.</p>'+
   '<h3>Open any screen</h3><div class="kkGrid">'+MAP.map(r=>row(ALT+'+'+r[1],r[2])).join('')+'</div>'+
   '<h3>Tabs and pages</h3><div class="kkGrid">'+row(ALT+'+[','Previous tab on this screen')+row(ALT+'+]','Next tab on this screen')+row(ALT+'+1…9','That tab on this screen')+row('Esc','Close the page in front')+row(ALT+'+/','This list')+row('Ctrl+Z','Undo the last move')+'</div>'+
   '<h3>The split keyboard (when the pads and keyboard are open)</h3><div class="kkGrid">'+row('1 2 3 4','Pads 1–4 (top row)')+row('Q W E R','Pads 5–8')+row('A S D F','Pads 9–12')+row('Z X C V','Pads 13–16')+row('Y U I O P [ ] \\','Piano white keys')+row('7 8 0 - =','Piano black keys')+row('H','Rewind')+row('J','Play')+row('K','Stop')+row('L','Record')+row(';','Undo')+row('N / M','Pad bank down / up')+row(', / .','Octave down / up')+row('\'','Pad sounds')+row('/','Keyboard sounds')+'</div>'+
   '<p style="opacity:.8;font-size:13px;margin-top:12px">Alt+D, Alt+E, Alt+F and Alt with the arrow keys are left to the browser.</p></div>'; p.hidden=false; }
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('You','⌨','Keyboard shortcuts for every screen and tab','Shortcuts',()=>show()); }); }catch(_){ }
 window.KKEYS={show,MAP:MAP.map(r=>[r[0],r[1],r[2]]),stepTab,nthTab,closeFront};
})();
