(()=>{ /* 💥 THE CANNON, ONE TRIGGER EVERYWHERE (v245). The cannon is KAN-IN's own mechanism: it makes the thing for you. Every screen has its
   own shot (a beat in the Studio, a song in Karaoke, a joke in Laugh, a spin in LuvMyZodiac, a craft, a storybook, a canvas on the
   Omni-Compass, a random game, a dish, a lesson, a headline), and one 💥 CANNON button, the same on every screen, fires that screen's shot.
   Every shot, from this button or any 💥 button anywhere, is counted and kept in 💥 My Cannon on your page.
   And the devices float over every studio: 🎤 the Karaoke mic joins the pads, the keyboard, the DJ decks and the track sequencer as a
   movable panel over the mixing board, and the same devices come up over the 🎬 Video studio. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 const press=sel=>{ const b=document.querySelector(sel); if(b){ b.click(); return true; } return false; };
 const randomTile=sel=>{ const L=[...document.querySelectorAll(sel)].filter(x=>x.getClientRects().length&&!x.disabled); if(!L.length) return false; L[Math.floor(Math.random()*L.length)].click(); return true; };
 const NAME={pad:'Studio',home:'Story',kKara:'Karaoke',kHumor:'Laugh',zodDock:'LuvMyZodiac',omniDock:'Omni-Compass',swDock:'Songwriter',craftDock:'Craft',sbDock:'Storybook',langDock:'Language',musicDock:'Music',mutDock:'Mutate',gamesDock:'Games',kVG:'Games',kKnow:'Knowledge',kNews:'News',kRelig:'Cultures & Religion',kMarket:'Stock Market',kEasel:'The Easel',aivDock:'Video studio',voiceDock:'Voices',recipeDock:'Recipes',kAcct:'My page'};
 const SHOT={pad:()=>press('#bmFire')||press('#cFire'),home:()=>press('#kCanAll')||press('[data-to="all"]'),kKara:()=>press('#kKara [data-kk="cannon"]'),kHumor:()=>press('#kHumor [data-kh="cannon"]'),zodDock:()=>press('#z4SpinGo')||press('#zlFire'),omniDock:()=>press('#otBoom'),swDock:()=>press('#swFire'),craftDock:()=>press('#crFire'),sbDock:()=>press('#sbFireAll'),langDock:()=>press('[data-kl="cannon"]'),musicDock:()=>press('[data-m="cannon"]'),mutDock:()=>press('#mrFire'),
  gamesDock:()=>randomTile('#gamesDock .gsTile,#gamesDock [data-game]'),kVG:()=>randomTile('#kVG .vgList button,#kVG .ghGrid button'),kKnow:()=>{ const L=[...document.querySelectorAll('#knList > details')]; if(!L.length) return false; const d=L[Math.floor(Math.random()*L.length)]; d.open=true; d.scrollIntoView({block:'center',behavior:'smooth'}); return true; },
  kNews:()=>randomTile('#kNews .nwItem button,#kNews article button'),recipeDock:()=>{ const b=[...document.querySelectorAll('#recipeDock button')].find(x=>/Surprise/.test(x.textContent)&&x.getClientRects().length); if(b){ b.click(); return true; } return false; }};
 /* every 💥 anywhere is a shot, kept for My Cannon */
 let lastLog=0;
 function log(where,what){ const now=Date.now(); if(now-lastLog<600) return; lastLog=now; const L=getLS('kanin-shots',[])||[]; L.unshift({at:now,what:(where?where+': ':'')+String(what||'a surprise').replace(/^💥\s*/,'').slice(0,60)}); putLS('kanin-shots',L.slice(0,80)); putLS('kanin-shotn',(+getLS('kanin-shotn',0)||0)+1); }
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('button'); if(!b||b.id==='kCannonBtn') return; const t=(b.textContent||'').trim(); if(/^💥/.test(t)) log(NAME[cur()]||'',t); },true);
 function fire(){ const c=cur(); let ok=false; try{ ok=!!(SHOT[c]&&SHOT[c]()); }catch(_){ ok=false; }
  if(!ok){ try{ KJUMP.open(); setTimeout(()=>{ try{ KJUMP.jump(); }catch(_){ } },350); ok=true; log(NAME[c]||'Anywhere','the jump generator'); }catch(_){ say('The cannon is loading. Try again in a moment.'); return; } }
  else log(NAME[c]||c,'fired on '+(NAME[c]||'this screen'));
  boom(); }
 /* the button: the same on every screen */
 const css=document.createElement('style'); css.textContent=`
#kCannonBtn{position:fixed;z-index:9750;left:calc(12px + env(safe-area-inset-left,0px));bottom:calc(64px + env(safe-area-inset-bottom,0px));width:64px;height:64px;border-radius:50%;border:3px solid #ffe94a!important;background:radial-gradient(circle at 35% 30%,#ff9f43,#d4145a 70%)!important;color:#fff!important;font:900 26px/1 system-ui,sans-serif!important;box-shadow:0 8px 24px rgba(0,0,0,.55);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0!important;cursor:pointer}
#kCannonBtn small{font:900 9.5px system-ui,sans-serif;letter-spacing:.04em;margin-top:2px}
#kCannonBtn:active{transform:scale(.94)}
body.gated #kCannonBtn,#kCannonBtn[hidden]{display:none!important}
.kBoom{position:fixed;z-index:9751;pointer-events:none;width:10px;height:10px;border-radius:50%;background:#ffe94a;box-shadow:0 0 18px #ff9f43;animation:kBoom .7s ease-out forwards}
@keyframes kBoom{to{transform:translate(var(--dx),var(--dy)) scale(.3);opacity:0}}
#kKaraMini{display:none;color:#eef;font:14px/1.4 system-ui,sans-serif}
#kKaraMini.kFOn{display:flex!important;flex-direction:column;gap:6px}
#kKaraMini .kmRow{display:flex;flex-wrap:wrap;gap:6px}
#kKaraMini button{min-height:44px!important;padding:0 12px!important;border-radius:12px!important;font:800 13.5px system-ui,sans-serif!important}
#kKaraMini .kmRec{background:#ff2d55!important;color:#fff!important;flex:1 1 140px}
#kKaraMini .kmTake{display:flex;align-items:center;gap:6px;background:rgba(255,255,255,.06);border-radius:10px;padding:4px 8px}
#kKaraMini .kmTake span{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:700}
#kKaraMini .kmTake button{min-height:32px!important;padding:0 8px!important}`; document.head.appendChild(css);
 function btn(){ let b=$('kCannonBtn'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kCannonBtn'; b.setAttribute('data-noul',''); b.title='💥 Fire the cannon: it makes the thing for you, on this screen'; b.setAttribute('aria-label','Fire the cannon'); b.innerHTML='💥<small>CANNON</small>'; b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); fire(); }); document.body.appendChild(b); }
  const t=$('tourTab'); const menuOpen=!!(t&&t.getClientRects().length&&getComputedStyle(t).display!=='none'&&t.getBoundingClientRect().width>40); const hide=menuOpen||!!document.querySelector('#kDemo:not([hidden])'); if(b.hidden!==hide) b.hidden=hide; }
 function boom(){ const b=$('kCannonBtn'); if(!b) return; const r=b.getBoundingClientRect(); for(let i=0;i<14;i++){ const d=document.createElement('i'); d.className='kBoom'; d.style.left=(r.left+r.width/2)+'px'; d.style.top=(r.top+r.height/2)+'px'; const a=-Math.PI/2+(Math.random()-.2)*Math.PI*.9; const L=90+Math.random()*160; d.style.setProperty('--dx',Math.cos(a)*L+'px'); d.style.setProperty('--dy',Math.sin(a)*L+'px'); document.body.appendChild(d); setTimeout(()=>d.remove(),800); } }
 /* 🎤 the Karaoke mic, a floating panel over the mixing board */
 const kk=a=>{ if(!$('kKara')){ try{ KKARA.open(); KKARA.close(); }catch(_){ } } return press('#kKara [data-kk="'+a+'"]'); };
 function mini(){ const pad=$('pad'); if(!pad) return null; let m=$('kKaraMini'); if(m) return m; m=document.createElement('div'); m.id='kKaraMini'; pad.appendChild(m);
  m.addEventListener('click',e=>{ const b=e.target.closest('[data-km]'); if(!b) return; e.stopPropagation(); const a=b.dataset.km;
   if(a==='full'){ try{ KKARA.open(); }catch(_){ } return; } if(a==='mute'){ const o=document.querySelector('#kKara [data-kk="lmute"][data-i="'+b.dataset.i+'"]'); if(o) o.click(); else { const T=(KKARA.takes()||[])[+b.dataset.i]; if(T) T.mute=!T.mute; } setTimeout(paintMini,150); return; }
   kk(a); setTimeout(paintMini,300); });
  return m; }
 function paintMini(){ const m=$('kKaraMini'); if(!m||!m.classList.contains('kFOn')) return; let takes=[]; try{ takes=KKARA.takes()||[]; }catch(_){ } const recB=document.querySelector('#kKara [data-kk="rec"]'); const recOn=!!recB&&/Stop/.test(recB.textContent);
  const h='<div class="kmRow"><button type="button" class="kmRec" data-km="rec" data-noul>'+(recOn?'■ Stop the take':'● Record a take')+'</button><button type="button" data-km="lbeat" data-noul>▶ Takes + beat</button><button type="button" data-km="lstop" data-noul>■ Stop</button></div><div class="kmRow"><button type="button" data-km="cannon" data-noul>💥 Cannon song</button><button type="button" data-km="sing" data-noul>🎤 Lyrics full screen</button><button type="button" data-km="full" data-noul>⤢ Full Karaoke</button></div>'+(takes.length?takes.slice(-6).map((t,j)=>{ const i=takes.length-Math.min(6,takes.length)+j; return '<div class="kmTake"><span>🎙 '+String(t.name||'Take').replace(/[<>&]/g,'')+(t.buf?' · '+t.buf.duration.toFixed(1)+' s':'')+'</span><button type="button" data-km="mute" data-i="'+i+'" data-noul>'+(t.mute?'🔇':'🔊')+'</button></div>'; }).join(''):'<div style="opacity:.8">No takes yet. ● Record a take sings over the beat; each take lands on its own microphone strip of the mixing board.</div>');
  if(m.dataset.h!==h){ m.dataset.h=h; m.innerHTML=h; } }
 function register(){ let F; try{ F=KRAIL.FLOAT; }catch(_){ return; } if(!F||!F.add||!mini()) return; F.add('kara',{get:()=>$('kKaraMini'),t:'🎤 Karaoke mic',i:'🎤',l:'Mic'});
  if(!getLS('kanin-float-kara',null)){ const W=innerWidth-(innerWidth<=760?58:76); putLS('kanin-float-kara',innerWidth<=760?{x:4,y:60,w:W-8,h:300}:{x:Math.max(8,W-380),y:90,w:360,h:340}); }
  const bb=$('bbBar'); if(bb&&!bb.querySelector('[data-kmo]')){ const b=document.createElement('button'); b.type='button'; b.dataset.kmo='1'; b.setAttribute('data-noul',''); b.textContent='🎤 Mic'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); try{ F.toggle('kara'); }catch(_){ } setTimeout(paintMini,100); },true); bb.appendChild(b); } }
 setInterval(()=>{ btn(); register(); paintMini(); },700);
 window.KCANNON={fire,log,SHOT,NAME};
})();
