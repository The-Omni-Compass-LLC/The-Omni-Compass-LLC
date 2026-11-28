(()=>{ /* 🥁 THE BEAT LINK AND THE PAGE TOOLS (v255). Every screen is wired into the beat machine and carries the same tools:
   • 🥁 BEAT LINK: the cannon and the games play the beat machine. Every 💥 cannon shot plays the kick, a hit or a point the snare, a win
     the crash, a miss the low tom and a tap in a game the hi-hat, from the pad bank on screen. "With the beat" (the factory setting)
     "On" (the factory setting) plays the pad at once while the beat is stopped, and while the beat plays holds each hit to the next
     sixteenth so it lands on the grid; with ● REC on it is recorded into the pattern like a pad played by hand. "Only with the beat"
     plays only while the beat runs; "Off" leaves the beat machine alone.
   • 🛠 TOOLS, BESIDE EVERY SCREEN'S UNDO AND CLOSE (v256; the floating remote is retired, its transport now lives in the pads, the
     keyboard, the sequencer and the karaoke themselves): the beat link, the tempo (− BPM +), the master volume, ⬆ Upload (any sound goes onto the selected
     pad and into your library; any other file into your library), ⬇ Save page (the screen's words and links as a file), 📚 Library,
     🎵 Sounds (every sound in the app), 🌐 Language (the whole app in another language) and ⌨ Shortcuts. The beat link also sits on the
     studio's transport bar.
   • 🏠 Home closes every platform page (Find, Services, Sports, News, Markets, Religion, Knowledge, your page, Legal) as well as the screens. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const PS=()=>window.PADSTUDIO; window.KREMOTE_RETIRED=true; /* v256: the floating remote is retired; its own repaint loop stands down */
 /* ---------- 🏠 Home closes every platform page ---------- */
 const OVL=['kFind','kServices','kSports','kNews','kMarket','kRelig','kKnow','kAcct','kLegal','kSndSheet','kReligX','kArr'];
 const closeAll=()=>OVL.forEach(id=>{ const x=$(id); if(x&&!x.hidden) x.hidden=true; });
 addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome')) closeAll(); },true);
 const wrapHome=()=>{ const g=window.GOHOME; if(typeof g!=='function'||g.__v255) return; const w=function(){ closeAll(); return g.apply(this,arguments); }; w.__v255=true; window.GOHOME=w; }; wrapHome(); setTimeout(wrapHome,2500);
 /* ---------- 🥁 the beat link ---------- */
 const MODES=[['on','On'],['grid','Only with the beat'],['off','Off']];
 const mode=()=>{ const m=getLS('kanin-beatlink2','on'); return MODES.some(x=>x[0]===m)?m:'on'; };
 const PADOF={cannon:0,score:2,hit:3,tap:4,miss:7,win:10};
 const bank=()=>{ const b=$('padBank'); return Math.max(0,Math.min(3,+(b&&b.value)||0))*16; };
 const Q=[]; let fired=0, lastTap=0, hooked=false;
 function hook(){ const P=PS(); if(hooked||!P||!P.STEPHOOKS) return; hooked=true;
  P.STEPHOOKS.push((c,dest,t,s,sd)=>{ if(!Q.length||c!==P.ac()) return; const take=[...new Set(Q.splice(0,4))]; const ms=Math.max(0,(t-c.currentTime)*1000); setTimeout(()=>take.forEach(i=>{ try{ P.hitPad(i); }catch(_){ } }),ms); }); }
 function trig(kind){ const m=mode(); if(m==='off') return false; const P=PS(); if(!P) return false; hook(); const i=bank()+(PADOF[kind]!=null?PADOF[kind]:4);
  if(P.playing){ if(Q.length<16) Q.push(i); } else if(m==='on'){ try{ P.hitPad(i); }catch(_){ return false; } } else return false;
  fired++; document.querySelectorAll('[data-bl="n"]').forEach(c=>c.textContent=String(fired)); return true; }
 const GAME=['gamesDock','kVG','tac','gsPick','kJump','omniDock'];
 const inGame=el=>{ if(el&&el.closest&&el.closest(GAME.map(x=>'#'+x).join(','))) return true; let c=''; try{ c=KRAIL.cur(); }catch(_){ } return GAME.includes(c); };
 /* the cannon, anywhere: the 💥 buttons, the floating cannon and the story's FIRE */
 addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('button,[role=button]'); if(!b||b.closest('#kToolsPop')) return; if(b.id==='kCannonBtn'||b.id==='fire'||/💥/.test(b.textContent||'')) trig('cannon'); },true);
 /* a tap in a game */
 addEventListener('pointerdown',e=>{ const t=e.target; if(!inGame(t)||t.closest('#kToolsPop,#kToolsBtn,#rDock')) return; const now=performance.now(); if(now-lastTap<120) return; lastTap=now; if(t.closest('button,canvas,[data-i],[data-c],.card,.cell')) trig('tap'); },true);
 /* what a game says: a win, a point, a miss */
 const wrapToast=()=>{ const t0=window.toast; if(typeof t0!=='function'||t0.__v255) return; const w=function(m){ try{ if(inGame()){ const s=String(m||''); if(/\b(you win|you won|winner|victory|checkmate|bingo|yahtzee|jackpot|level up|cleared|champion)\b/i.test(s)) trig('win'); else if(/\b(miss|missed|you lose|lost|wrong|bust|game over|try again)\b/i.test(s)) trig('miss'); else if(/\b(hit|score|scored|point|goal|nice|great|perfect|match|correct)\b|\+\d+/i.test(s)) trig('score'); } }catch(_){ } return t0.apply(this,arguments); }; w.__v255=true; window.toast=w; };
 wrapToast(); setTimeout(wrapToast,2500);
 /* ---------- 🎛 the remote's tools ---------- */
 const css=document.createElement('style'); css.textContent=`
#kToolsPop .rmTools{display:flex;flex-wrap:wrap;gap:4px;padding:0 6px 6px;max-width:min(560px,calc(100vw - 90px))}
#kRemote{display:none!important}
#kToolsBtn{position:fixed;z-index:9745;min-height:40px;padding:0 12px;border-radius:999px;font:900 14px system-ui,sans-serif;background:#2b1d6e!important;color:#fff!important;border:2px solid #ffe94a!important;box-shadow:0 4px 14px rgba(0,0,0,.45)}
#kToolsBtn.on{background:#ffe94a!important;color:#14163a!important}
#kToolsPop{position:fixed;z-index:9746;background:rgba(12,10,36,.97);border:2px solid #ffe94a;border-radius:6px 16px 6px 16px;box-shadow:0 10px 30px rgba(0,0,0,.6);padding:8px 2px 2px;max-width:min(540px,calc(100vw - 80px))}
#kToolsPop[hidden]{display:none!important}
#kToolsPop .rmTools button{min-height:40px!important;min-width:0!important;padding:0 8px!important;border-radius:10px!important;font:800 11.5px system-ui,sans-serif!important;display:inline-flex!important;align-items:center;gap:4px}
#kToolsPop .rmTools .bl{background:#2b5d1c!important;border-color:#7dffb0!important}
#kToolsPop .rmTools .bl.off{background:#3a2a2a!important;border-color:#a88!important}
#kToolsPop .rmTools .bpm{display:inline-flex;align-items:center;gap:2px;background:#1b1240;border:1.5px solid #cfc4ff;border-radius:10px;padding:0 2px}
#kToolsPop .rmTools .bpm b{min-width:46px;text-align:center;color:#ffe94a;font:900 12px ui-monospace,monospace}
#kToolsPop .rmTools .bpm button{min-height:34px!important;padding:0 7px!important}
#kToolsPop .rmTools label{display:inline-flex;align-items:center;gap:4px;color:#ffe94a;font:800 11.5px system-ui,sans-serif;background:#1b1240;border:1.5px solid #cfc4ff;border-radius:10px;padding:0 6px;min-height:40px}
#kToolsPop .rmTools input[type=range]{width:82px;accent-color:#ffe94a}
#kLangPop{position:fixed;z-index:9790;left:50%;top:30%;transform:translateX(-50%);background:#141833;border:2px solid #ffe94a;border-radius:6px 16px 6px 16px;padding:14px;color:#eef;font:15px system-ui,sans-serif;display:flex;flex-direction:column;gap:8px;width:min(360px,calc(100vw - 32px))}
#kLangPop[hidden]{display:none!important}
#kLangPop select{min-height:44px;font-size:16px}
#kLangPop .row{display:flex;gap:8px}#kLangPop button{min-height:44px;flex:1}`; document.head.appendChild(css);
 const modeLabel=()=>'🥁 Beat link: '+MODES.find(x=>x[0]===mode())[1];
 function pop(){ let p=$('kToolsPop'); if(!p){ p=document.createElement('div'); p.id='kToolsPop'; p.hidden=true; p.setAttribute('role','dialog'); p.setAttribute('aria-label','Tools'); document.body.appendChild(p);
   document.addEventListener('pointerdown',e=>{ if(!p.hidden&&!e.target.closest('#kToolsPop,#kToolsBtn,#kLangPop,#kKeysPop')){ p.hidden=true; const b=$('kToolsBtn'); if(b) b.classList.remove('on'); } },true); } return p; }
 /* 🛠 beside the screen's ↶ Undo and ✕ Close (or at the top right on the landing page) */
 function btn(){ let b=$('kToolsBtn'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kToolsBtn'; b.setAttribute('data-noul',''); b.title='Tools: beat link, tempo, volume, upload, save page, library, sounds, language, shortcuts (Alt+/ lists the shortcuts)'; b.textContent='🛠 Tools'; document.body.appendChild(b);
   b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); const p=pop(); p.hidden=!p.hidden; b.classList.toggle('on',!p.hidden); if(!p.hidden) place(); },true); }
  const vis=el=>el&&el.getClientRects().length&&el.getBoundingClientRect().width>0&&getComputedStyle(el).visibility!=='hidden'; const u=[$('kUndoAll'),$('kXAll')].find(vis); const ur=u?u.getBoundingClientRect():null; const ph=innerWidth<=760; const lab=ph?'🛠':'🛠 Tools'; if(b.textContent!==lab) b.textContent=lab; const rail=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58; const bw=b.offsetWidth||90;
  if(ur&&ur.width){ b.style.top=Math.round(ur.top+(ur.height-(b.offsetHeight||40))/2)+'px'; b.style.left=Math.max(6,Math.round(ur.left-bw-8))+'px'; b.style.right='auto'; } else { b.style.top='calc(10px + env(safe-area-inset-top,0px))'; b.style.left='auto'; b.style.right=(rail+12)+'px'; } return b; }
 function place(){ const b=$('kToolsBtn'), p=$('kToolsPop'); if(!b||!p||p.hidden) return; const r=b.getBoundingClientRect(); p.style.top=Math.round(r.bottom+8)+'px'; const w=p.offsetWidth||360; p.style.left=Math.max(6,Math.min(innerWidth-w-8,Math.round(r.right-w)))+'px'; }
 function tools(){ btn(); const R=pop(); let T=R.querySelector('.rmTools'); if(T){ place(); return refresh(T); }
  T=document.createElement('div'); T.className='rmTools'; T.setAttribute('role','toolbar'); T.setAttribute('aria-label','Beat link, tempo, volume and page tools');
  T.innerHTML='<button type="button" class="bl" data-t="bl" data-noul title="Games and the cannon play the beat machine">'+modeLabel()+' · <span data-bl="n">'+fired+'</span></button>'+
   '<span class="bpm"><button type="button" data-t="bpm-" data-noul title="Slower">−</button><b data-t="bpmv">90 BPM</b><button type="button" data-t="bpm+" data-noul title="Faster">+</button></span>'+
   '<label title="Master volume">🔊<input type="range" min="0" max="150" value="'+getLS('kanin-mvol',100)+'" data-t="vol" data-nodice data-die="1" aria-label="Master volume"></label>'+
   '<button type="button" data-t="up" data-noul title="Upload a sound onto the selected pad, or any file into your library">⬆ Upload</button>'+
   '<button type="button" data-t="save" data-noul title="Save this screen’s words and links as a file">⬇ Save page</button>'+
   '<button type="button" data-t="lib" data-noul title="Your library and projects">📚 Library</button>'+
   '<button type="button" data-t="snd" data-noul title="Every sound in the app">🎵 Sounds</button>'+
   '<button type="button" data-t="lang" data-noul title="The whole app in another language">🌐 Language</button>'+
   '<button type="button" data-t="keys" data-noul title="Every keyboard shortcut (Alt+/)">⌨ Shortcuts</button>';
  R.appendChild(T); T.addEventListener('click',onClick);
 T.addEventListener('input',e=>{ if(e.target.dataset.t==='vol') vol(+e.target.value); }); refresh(T); }
 function refresh(T){ const b=T.querySelector('[data-t="bl"]'); if(b){ b.classList.toggle('off',mode()==='off'); const want=modeLabel(); if(!b.textContent.startsWith(want)){ b.innerHTML=want+' · <span data-bl="n">'+fired+'</span>'; } } const v=T.querySelector('[data-t="bpmv"]'); const bp=$('padBpm'); if(v&&bp){ const t=(+bp.value||90)+' BPM'; if(v.textContent!==t) v.textContent=t; } }
 function vol(v){ putLS('kanin-mvol',v); const P=PS(); try{ const g=P&&P.out&&P.out(); if(g&&g.gain) g.gain.value=v/100; }catch(_){ } document.querySelectorAll('audio,video').forEach(m=>{ try{ m.volume=Math.min(1,v/100); }catch(_){ } }); }
 function bpm(d){ const b=$('padBpm'); if(!b) return say('Open the studio once to set the tempo.'); b.value=String(Math.max(40,Math.min(240,(+b.value||90)+d))); b.dispatchEvent(new Event('input',{bubbles:true})); b.dispatchEvent(new Event('change',{bubbles:true})); const T=document.querySelector('#kToolsPop .rmTools'); if(T) refresh(T); }
 const curName=()=>{ let c='home'; try{ c=KRAIL.cur(); }catch(_){ } const o=OVL.find(id=>{ const x=$(id); return x&&!x.hidden; }); return o||c||'home'; };
 function topScreen(){ const o=OVL.map($).find(x=>x&&!x.hidden); if(o) return o; let c=''; try{ c=KRAIL.cur(); }catch(_){ } return (c&&$(c))||document.querySelector('.wrap')||document.body; }
 async function upload(){ const inp=document.createElement('input'); inp.type='file'; inp.multiple=true; inp.accept='audio/*,video/*,image/*,.txt,.md,.json,.pdf,.csv';
  inp.onchange=async()=>{ const fs=[...inp.files]; let n=0; for(const f of fs){ try{ if(/^audio\//.test(f.type)||/\.(wav|mp3|ogg|m4a|aac|flac)$/i.test(f.name)){ const P=PS(); const c=P&&P.ac&&P.ac(); if(c){ const buf=await c.decodeAudioData(await f.arrayBuffer()); const s=document.querySelector('#padGrid .pd.sel'); const i=s?+s.dataset.i:bank(); P.setBuf(i,buf,f.name.replace(/\.[^.]+$/,'').slice(0,18),true); try{ P.refresh(); }catch(_){ } try{ await KLIB.saveAudio(buf,f.name,{from:'upload',screen:curName()}); }catch(_){ } say('⬆ '+f.name+' is on pad '+'ABCD'[Math.floor(i/16)]+(i%16+1)+' and in your library.'); n++; continue; } }
     await KLIB.save({kind:'file',name:f.name,blob:f,meta:{type:f.type,size:f.size,from:'upload',screen:curName()}}); n++; }catch(e){ say('That file could not be read: '+f.name); } }
   if(n) say('⬆ '+n+' file'+(n>1?'s':'')+' saved to your library.'); };
  inp.click(); }
 async function savePage(){ const el=topScreen(); const title=(el.querySelector('h1,h2,h3')||{}).textContent||curName(); const lines=['# '+title.trim(),''];
  const walk=n=>{ for(const k of n.childNodes){ if(k.nodeType===3){ const t=k.textContent.replace(/\s+/g,' ').trim(); if(t) lines.push(t); } else if(k.nodeType===1){ const st=getComputedStyle(k); if(st.display==='none'||k.matches('script,style,button,select,input,textarea,canvas,svg')) continue; if(k.tagName==='A'&&/^https:\/\//.test(k.href)){ lines.push('['+k.textContent.trim()+']('+k.href+')'); continue; } if(/^H[1-4]$/.test(k.tagName)){ lines.push('','## '+k.textContent.trim()); continue; } walk(k); } } };
  walk(el); const N='© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com';
  const txt=N+'\n\n'+lines.filter((l,i,a)=>l||a[i-1]).join('\n')+'\n\nFrom the Omni-Galaxy Multi-Media Studios Platform · www.omni-galaxy.com\n\n'+N+'\n';
  const name=(title.trim().replace(/[^\w\- ]+/g,'').replace(/\s+/g,'-').slice(0,60)||'page')+'.md'; const blob=new Blob([txt],{type:'text/markdown'});
  try{ const ok=await KLIB.download(blob,name); if(ok!==false) say('⬇ Saved '+name+'.'); }catch(_){ try{ const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=name; document.body.appendChild(a); a.click(); a.remove(); }catch(__){ say('Saving is not allowed here.'); } } }
 function lang(){ let p=$('kLangPop'); const src=$('appLang'); if(!src) return say('The language list is not ready yet.'); if(!p){ p=document.createElement('div'); p.id='kLangPop'; p.setAttribute('role','dialog'); p.setAttribute('aria-label','Language'); document.body.appendChild(p);
   p.addEventListener('click',e=>{ const b=e.target.closest('[data-lp]'); if(!b) return; e.stopPropagation(); if(b.dataset.lp==='go'){ const s=p.querySelector('select'); src.value=s.value; src.dispatchEvent(new Event('change',{bubbles:true})); const go=$('appLangGo'); if(go) go.click(); } p.hidden=true; }); }
  p.innerHTML='<b>🌐 The whole app in another language</b><select aria-label="Language">'+[...src.options].map(o=>'<option value="'+esc(o.value)+'"'+(o.value===src.value?' selected':'')+'>'+esc(o.textContent)+'</option>').join('')+'</select><div class="row"><button type="button" data-lp="go" data-noul>✅ Translate</button><button type="button" data-lp="x" data-noul>✕ Close</button></div>'; p.hidden=false; }
 function onClick(e){ const b=e.target.closest('[data-t]'); if(!b) return; e.stopPropagation(); e.preventDefault(); const t=b.dataset.t;
  if(t==='bl'){ const i=MODES.findIndex(x=>x[0]===mode()); putLS('kanin-beatlink2',MODES[(i+1)%MODES.length][0]); refresh(b.parentElement); say(modeLabel()+(mode()==='on'?': games and the cannon play the pads; while the beat plays each hit lands on the next sixteenth, and ● REC records it.':mode()==='grid'?': games play the pads only while the beat plays, always on the grid.':': games leave the beat machine alone.')); return; }
  if(t==='bpm-') return bpm(-5); if(t==='bpm+') return bpm(5);
  if(t==='up') return upload(); if(t==='save') return savePage();
  if(t==='lib'){ try{ KPROJ.open(); }catch(_){ say('Projects are not ready yet.'); } return; }
  if(t==='snd'){ try{ const s=document.querySelector('#padGrid .pd.sel'); const i=s?+s.dataset.i:bank(); KSNDPICK.open('pads',i,'for pad '+'ABCD'[Math.floor(i/16)]+(i%16+1)); }catch(_){ say('Open the studio once to load the sounds.'); } return; }
  if(t==='lang') return lang();
  if(t==='keys'){ try{ KKEYS.show(); }catch(_){ } return; } }
 function studioBar(){ const bb=$('bbBar'); if(!bb||bb.querySelector('[data-blk]')) return; const b=document.createElement('button'); b.type='button'; b.dataset.blk='1'; b.setAttribute('data-noul',''); b.title='Beat link: games and the cannon play the beat machine'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); const i=MODES.findIndex(x=>x[0]===mode()); putLS('kanin-beatlink2',MODES[(i+1)%MODES.length][0]); paintBar(); say(modeLabel()); },true); bb.appendChild(b); paintBar(); }
 function paintBar(){ const b=document.querySelector('#bbBar [data-blk]'); if(b){ const t='🥁 Link: '+MODES.find(x=>x[0]===mode())[1]; if(b.textContent!==t) b.textContent=t; } const T=document.querySelector('#kToolsPop .rmTools'); if(T) refresh(T); }
 setInterval(()=>{ tools(); hook(); studioBar(); paintBar(); },900); addEventListener('resize',()=>{ btn(); place(); });
 setTimeout(()=>{ const v=getLS('kanin-mvol',100); if(v!==100) vol(v); },3000);
 window.KBEAT={trig,mode,setMode:m=>{ if(MODES.some(x=>x[0]===m)) putLS('kanin-beatlink2',m); },get fired(){ return fired; },closeAll};
})();
