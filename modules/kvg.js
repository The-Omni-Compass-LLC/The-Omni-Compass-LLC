(()=>{ /* 🕹 VIDEO GAMES: one lobby for every game, an on-screen controller (a game pad you can touch), real game controllers
   (USB or Bluetooth), and the controls monitor: a live keyboard that lights every key you press and shows what each key does. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const NEW=[['vg_tower','Storm Tower','Girder climb','Climb the tower, jump the thunderballs, reach the compass.'],['vg_bake','Bakery Drop','Shelf-stacking chase','Walk the cake layers down to the plates; dodge the runaway dough.'],['vg_orbit','Orbit Guard','Planet defender with radar','Fly over the planet and save the colonists from the drones.'],['vg_vortex','Vortex Rim','Tube shooter','Ride the rim of a neon tube and blast everything climbing up.'],['vg_arena','Neon Arena','Twin-stick arena','Move with one hand, shoot with the other, save the Pips.'],['vg_road','Night Highway','Road racer','Race the neon highway at night and beat the clock.']];
 /* what every key does, game by game: the controls monitor */
 const GEN=[['ArrowLeft','Move left'],['ArrowRight','Move right'],['ArrowUp','Up'],['ArrowDown','Down'],[' ','Action / fire / start'],['Enter','Start / special'],['p','Pause'],['Escape','Close the game']];
 const CTRL={vg_tower:[['ArrowLeft','Walk left'],['ArrowRight','Walk right'],['ArrowUp','Climb up a ladder'],['ArrowDown','Climb down a ladder'],[' ','Jump'],['p','Pause'],['Escape','Close']],
  vg_bake:[['ArrowLeft','Walk left'],['ArrowRight','Walk right'],['ArrowUp','Climb up'],['ArrowDown','Climb down'],[' ','Throw a flour puff'],['p','Pause'],['Escape','Close']],
  vg_orbit:[['ArrowLeft','Fly left'],['ArrowRight','Fly right'],['ArrowUp','Climb'],['ArrowDown','Dive'],[' ','Fire'],['Enter','Nova bomb'],['p','Pause'],['Escape','Close']],
  vg_vortex:[['ArrowLeft','Move around the rim'],['ArrowRight','Move around the rim'],[' ','Fire'],['Enter','Vortex zapper'],['p','Pause'],['Escape','Close']],
  vg_arena:[['w','Move up'],['a','Move left'],['s','Move down'],['d','Move right'],['ArrowUp','Shoot up'],['ArrowDown','Shoot down'],['ArrowLeft','Shoot left'],['ArrowRight','Shoot right'],['p','Pause'],['Escape','Close']],
  vg_road:[['ArrowUp','Gas'],[' ','Gas'],['ArrowDown','Brake'],['ArrowLeft','Steer left'],['ArrowRight','Steer right'],['p','Pause'],['Escape','Close']]};
 /* how the on-screen controller is wired for each game */
 const PADC={vg_arena:{L:'wasd',R:'stick',Ln:'MOVE',Rn:'SHOOT'},vg_tower:{A:[' ','JUMP']},vg_bake:{A:[' ','FLOUR']},vg_orbit:{A:[' ','FIRE'],B:['Enter','NOVA']},vg_vortex:{A:[' ','FIRE'],B:['Enter','ZAP']},vg_road:{A:['ArrowUp','GAS'],B:['ArrowDown','BRAKE']}};
 const DIRS={arrows:['ArrowUp','ArrowDown','ArrowLeft','ArrowRight'],wasd:['w','s','a','d']};
 let padMode=getLS('kanin-pad','auto'), padSize=getLS('kanin-pad-size','m');
 const touchy=()=>{ try{ return matchMedia('(pointer:coarse)').matches; }catch(_){ return false; } };
 const padOn=()=>padMode==='on'||(padMode==='auto'&&touchy());
 const cur=()=>{ const s=document.querySelectorAll('#gamesDock .gmTop select'); return s[1]&&s[1].value||''; };
 const CODE={' ':'Space','Enter':'Enter','ArrowUp':'ArrowUp','ArrowDown':'ArrowDown','ArrowLeft':'ArrowLeft','ArrowRight':'ArrowRight','p':'KeyP','Escape':'Escape'};
 function send(key,down){ try{ document.dispatchEvent(new KeyboardEvent(down?'keydown':'keyup',{key,code:CODE[key]||('Key'+key.toUpperCase()),bubbles:true,cancelable:true})); }catch(_){ } }
 const held=new Set(); const press=(k,on)=>{ if(on&&!held.has(k)){ held.add(k); send(k,true); } else if(!on&&held.has(k)){ held.delete(k); send(k,false); } };
 function releaseAll(){ [...held].forEach(k=>press(k,false)); }
 const css=document.createElement('style'); css.textContent=`
#kVG{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 44px 14px;background:radial-gradient(circle at 50% 0,#14204a,#04040f 70%);color:#eef;font:15px/1.5 system-ui,sans-serif}
#kVG[hidden]{display:none!important}
#kVG .vgIn{max-width:1060px;margin:0 auto}
#kVG .vgBrand{font:700 12px ui-monospace,monospace;letter-spacing:.12em;color:#7ff;text-transform:uppercase}
#kVG h2{font:900 28px/1.15 system-ui,sans-serif;margin:6px 0 2px;color:#ffe94a}
#kVG h3{font:800 18px/1.2 system-ui,sans-serif;margin:22px 0 8px;color:#fff;border-top:1px solid rgba(255,255,255,.15);padding-top:12px}
#kVG .vgN{font-size:14px;opacity:.88}
#kVG .vgCards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
#kVG .vgCard{border:1px solid rgba(111,232,255,.35);border-radius:14px;padding:12px;background:rgba(0,0,0,.35);display:flex;flex-direction:column;gap:6px;min-width:0}
#kVG .vgCard b{font:900 18px system-ui,sans-serif;color:#fff}
#kVG .vgCard i{font:700 12px ui-monospace,monospace;letter-spacing:.06em;color:#ff7ad9;font-style:normal;text-transform:uppercase}
#kVG .vgCard button,#kVG .vgRow button{min-height:44px;border-radius:12px;font:800 15px system-ui,sans-serif;padding:0 14px}
#kVG details{margin:8px 0;border:1px solid rgba(255,255,255,.16);border-radius:12px;background:rgba(255,255,255,.04)}
#kVG summary{cursor:pointer;min-height:46px;display:flex;align-items:center;padding:0 12px;font:800 15px system-ui,sans-serif;color:#ffe94a}
#kVG details>.vgList{display:flex;flex-wrap:wrap;gap:6px;padding:0 10px 12px}
#kVG .vgList button{min-height:40px;border-radius:10px;padding:0 12px;font:600 14px system-ui,sans-serif}
#kVG .vgRow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0}
#kVG .vgRow select{min-height:42px;border-radius:10px;max-width:100%}
#kVG .vgLinks a{color:#7ff;display:inline-block;margin:4px 12px 4px 0}
.kKeyMon{border:1px solid rgba(111,232,255,.35);border-radius:12px;background:rgba(0,0,0,.4);padding:8px;margin:8px 0;color:#eef;font:13px/1.4 system-ui,sans-serif}
.kKeyMon summary{cursor:pointer;font:800 14px system-ui,sans-serif;color:#7ff;min-height:36px;display:flex;align-items:center}
.kKeyMon .kmKb{display:grid;gap:4px;margin:6px 0;overflow-x:auto}
.kKeyMon .kmR{display:flex;gap:4px}
.kKeyMon .kmK{flex:0 0 auto;min-width:30px;height:30px;border-radius:6px;border:1px solid #3a4470;background:#141a33;color:#cfd6ff;display:flex;align-items:center;justify-content:center;font:700 12px ui-monospace,monospace;padding:0 6px;transition:background .05s}
.kKeyMon .kmK.use{border-color:#ffe94a;color:#ffe94a}
.kKeyMon .kmK.on{background:#ffe94a!important;color:#14163a!important;box-shadow:0 0 12px #ffe94a}
.kKeyMon .kmK.wide{min-width:58px}.kKeyMon .kmK.space{min-width:150px}
.kKeyMon .kmMap{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:4px 12px;margin-top:6px}
.kKeyMon .kmMap span b{color:#ffe94a;font-family:ui-monospace,monospace}
.kKeyMon .kmPad{font-size:12.5px;opacity:.85;margin-top:4px}
#kPadV{--ps:120px;display:flex;justify-content:space-between;align-items:center;gap:10px;margin:10px auto 4px;max-width:720px;user-select:none;-webkit-user-select:none;touch-action:none}
#kPadV.s{--ps:96px}#kPadV.l{--ps:150px}
#kPadV .kpStick{width:var(--ps);height:var(--ps);border-radius:50%;background:radial-gradient(circle,#26305c,#0c1024);border:2px solid #6fe8ff;position:relative;touch-action:none;flex:0 0 auto}
#kPadV .kpStick .kpNub{position:absolute;left:50%;top:50%;width:40%;height:40%;margin:-20% 0 0 -20%;border-radius:50%;background:#6fe8ff;opacity:.85;pointer-events:none}
#kPadV .kpStick small{position:absolute;bottom:-18px;left:0;right:0;text-align:center;font:800 10px ui-monospace,monospace;color:#7ff;letter-spacing:.1em}
#kPadV .kpMid{display:flex;flex-direction:column;gap:6px;align-items:center}
#kPadV .kpMid button{min-height:34px;min-width:60px;border-radius:17px;font:800 12px system-ui,sans-serif}
#kPadV .kpBtns{display:grid;grid-template-columns:1fr 1fr;gap:8px;flex:0 0 auto}
#kPadV .kpB{width:calc(var(--ps)*.5);height:calc(var(--ps)*.5);border-radius:50%;font:900 13px system-ui,sans-serif;border:2px solid #ffe94a;background:#3a2a08;color:#ffe94a;touch-action:none;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.05;padding:2px}
#kPadV .kpB.b{border-color:#ff4f6d;background:#3a0a14;color:#ff9aa9;margin-top:calc(var(--ps)*.25)}
#kPadV .kpB.on,#kPadV .kpStick.on{filter:brightness(1.6)}
html body #rDock#rDock #kdVG{order:4!important;display:flex!important}html body #rDock#rDock #kdVG[hidden]{display:none!important}
#gamesDock .vgBack{background:#ffe94a!important;color:#14163a!important;font-weight:800}
#tourTab #ttVG{grid-column:1/-1;min-height:52px;font:800 16px/1.2 system-ui,sans-serif!important}
@media (min-width:1100px){#gamesDock{grid-template-rows:auto auto auto auto auto!important;grid-template-areas:"top title side" "top area side" "top area side" "lib lib lib" "foot foot foot"!important}#gamesDock>.ocLib,#gamesDock>[id^="lib-"]{grid-area:lib!important;max-width:980px;margin:12px auto 0}#gamesDock>.ocFoot{grid-area:foot!important}}`; document.head.appendChild(css);
 /* the live keyboard */
 const ROWS=[[['Escape','Esc','wide'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['0']],[['q'],['w'],['e'],['r'],['t'],['y'],['u'],['i'],['o'],['p']],[['a'],['s'],['d'],['f'],['g'],['h'],['j'],['k'],['l'],['Enter','Enter','wide']],[['Shift','Shift','wide'],['z'],['x'],['c'],['v'],['b'],['n'],['m'],['ArrowUp','↑']],[[' ','Space','space'],['ArrowLeft','←'],['ArrowDown','↓'],['ArrowRight','→']]];
 const kName=k=>k===' '?'Space':k==='ArrowUp'?'↑':k==='ArrowDown'?'↓':k==='ArrowLeft'?'←':k==='ArrowRight'?'→':k==='Escape'?'Esc':k.length===1?k.toUpperCase():k;
 function monitor(id,open){ const map=CTRL[id]||GEN; const use=new Map(); map.forEach(([k,a])=>use.set(k,(use.get(k)?use.get(k)+' · ':'')+a));
  return '<details class="kKeyMon"'+(open?' open':'')+' data-g="'+esc(id||'')+'"><summary>⌨ Controls monitor'+(id?' · '+esc(nameOf(id)):'')+'</summary><div class="kmKb">'+ROWS.map(r=>'<div class="kmR">'+r.map(([k,l,c])=>'<span class="kmK '+(c||'')+(use.has(k)?' use':'')+'" data-k="'+esc(k)+'" title="'+esc(use.get(k)||'')+'">'+esc(l||kName(k))+'</span>').join('')+'</div>').join('')+'</div>'+
   '<div class="kmMap">'+map.map(([k,a])=>'<span><b>'+esc(kName(k))+'</b> · '+esc(a)+'</span>').join('')+'</div><div class="kmPad">Keys light up as you press them, on the keyboard, the 🎮 on-screen controller or a real game controller. Gold keys are the ones this game uses.</div></details>'; }
 function nameOf(id){ try{ const g=GAMES.list.find(x=>x.id===id); return g?g.name:id; }catch(_){ return id; } }
 function lightKey(k,on){ k=k&&k.length===1?k.toLowerCase():k; document.querySelectorAll('.kKeyMon .kmK').forEach(el=>{ if(el.dataset.k===k) el.classList.toggle('on',on); }); }
 window.addEventListener('keydown',e=>lightKey(e.key,true),true); window.addEventListener('keyup',e=>lightKey(e.key,false),true); window.addEventListener('blur',()=>document.querySelectorAll('.kKeyMon .kmK.on').forEach(el=>el.classList.remove('on')));
 /* the on-screen controller */
 function stick(el,keys){ let pid=null; const nub=el.querySelector('.kpNub');
  const set=(e)=>{ const r=el.getBoundingClientRect(), cx=r.left+r.width/2, cy=r.top+r.height/2; let dx=e.clientX-cx, dy=e.clientY-cy; const m=Math.hypot(dx,dy), R=r.width/2; if(m>R){ dx=dx/m*R; dy=dy/m*R; } nub.style.transform='translate('+dx*0.6+'px,'+dy*0.6+'px)'; const dead=R*0.25, on=m>dead; const a=Math.atan2(dy,dx);
   const up=on&&Math.sin(a)<-0.38, dn=on&&Math.sin(a)>0.38, lf=on&&Math.cos(a)<-0.38, rt=on&&Math.cos(a)>0.38; press(keys[0],up); press(keys[1],dn); press(keys[2],lf); press(keys[3],rt); };
  const end=()=>{ pid=null; nub.style.transform=''; el.classList.remove('on'); keys.forEach(k=>press(k,false)); };
  el.addEventListener('pointerdown',e=>{ e.preventDefault(); pid=e.pointerId; try{ el.setPointerCapture(pid); }catch(_){ } el.classList.add('on'); set(e); });
  el.addEventListener('pointermove',e=>{ if(e.pointerId===pid) set(e); }); el.addEventListener('pointerup',end); el.addEventListener('pointercancel',end); el.addEventListener('lostpointercapture',end); }
 function button(el,key){ const dn=e=>{ e.preventDefault(); try{ el.setPointerCapture(e.pointerId); }catch(_){ } el.classList.add('on'); press(key,true); }, up=()=>{ el.classList.remove('on'); press(key,false); };
  el.addEventListener('pointerdown',dn); el.addEventListener('pointerup',up); el.addEventListener('pointercancel',up); el.addEventListener('lostpointercapture',up); }
 function padEl(id){ const c=Object.assign({L:'arrows',R:'buttons',A:[' ','A'],B:['Enter','B'],Ln:'MOVE',Rn:'AIM'},PADC[id]||{}); const d=document.createElement('div'); d.id='kPadV'; d.className=padSize; d.dataset.g=id;
  d.innerHTML='<div class="kpStick" data-s="L"><div class="kpNub"></div><small>'+c.Ln+'</small></div><div class="kpMid"><button type="button" data-pk="p" data-noul>⏸ Pause</button><button type="button" data-pk="Enter" data-noul>▶ Start</button></div>'+(c.R==='stick'?'<div class="kpStick" data-s="R" style="border-color:#ff7ad9"><div class="kpNub" style="background:#ff7ad9"></div><small>'+c.Rn+'</small></div>':'<div class="kpBtns"><button type="button" class="kpB b" data-noul>'+esc(c.B[1])+'</button><button type="button" class="kpB a" data-noul>'+esc(c.A[1])+'</button></div>');
  stick(d.querySelector('[data-s="L"]'),DIRS[c.L]); if(c.R==='stick') stick(d.querySelector('[data-s="R"]'),DIRS.arrows); else { button(d.querySelector('.kpB.a'),c.A[0]); button(d.querySelector('.kpB.b'),c.B[0]); }
  d.querySelectorAll('[data-pk]').forEach(b=>button(b,b.dataset.pk)); return d; }
 function dress(){ const dock=$('gamesDock'), area=$('gmArea'); if(!dock||dock.hidden||!area) return; const id=cur(); if(!id) return; const has=area.querySelector('canvas');
  const p=area.querySelector('#kPadV'); if(p&&(p.dataset.g!==id||!padOn()||!has)){ releaseAll(); p.remove(); }
  if(has&&padOn()&&!area.querySelector('#kPadV')) area.appendChild(padEl(id));
  const m=area.querySelector('.kKeyMon'); if(m&&m.dataset.g!==id) m.remove(); if(!area.querySelector('.kKeyMon')){ const w=document.createElement('div'); w.innerHTML=monitor(id,innerWidth>=900&&!touchy()); area.appendChild(w.firstChild); }
  const top=dock.querySelector('.gmTop .gbar'); if(top&&!top.querySelector('.vgBack')){ const b=document.createElement('button'); b.type='button'; b.className='vgBack'; b.textContent='🕹 All video games'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); top.insertBefore(b,top.firstChild); } }
 setInterval(dress,600);
 /* real game controllers (USB or Bluetooth) */
 let gpOn=false, gpPrev={}, gpName='';
 window.addEventListener('gamepadconnected',e=>{ gpName=e.gamepad.id; say('🎮 Controller connected: '+gpName.slice(0,40)); paintGp(); });
 window.addEventListener('gamepaddisconnected',()=>{ gpName=''; releaseAll(); paintGp(); });
 function pollGp(){ requestAnimationFrame(pollGp); const dock=$('gamesDock'); if(!dock||dock.hidden) return; let gp=null; try{ gp=[...(navigator.getGamepads?navigator.getGamepads():[])].find(Boolean); }catch(_){ return; } if(!gp) return;
  const c=Object.assign({L:'arrows',R:'buttons',A:[' ','A'],B:['Enter','B']},PADC[cur()]||{}); const ax=i=>gp.axes[i]||0, bt=i=>!!(gp.buttons[i]&&gp.buttons[i].pressed);
  const st={}; const L=DIRS[c.L]; st[L[0]]=ax(1)<-0.4||bt(12); st[L[1]]=ax(1)>0.4||bt(13); st[L[2]]=ax(0)<-0.4||bt(14); st[L[3]]=ax(0)>0.4||bt(15);
  if(c.R==='stick'){ const A=DIRS.arrows; st[A[0]]=ax(3)<-0.4; st[A[1]]=ax(3)>0.4; st[A[2]]=ax(2)<-0.4; st[A[3]]=ax(2)>0.4; } else { st[c.A[0]]=(st[c.A[0]]||false)||bt(0); st[c.B[0]]=(st[c.B[0]]||false)||bt(1); }
  st.p=bt(9); Object.keys(st).forEach(k=>{ if(!!st[k]!==!!gpPrev[k]) press(k,!!st[k]); }); gpPrev=st; }
 try{ requestAnimationFrame(pollGp); }catch(_){ }
 function paintGp(){ const s=$('vgGp'); if(s) s.textContent=gpName?'🎮 Connected: '+gpName.slice(0,60):'No controller found yet. Plug one in (USB) or pair it (Bluetooth), then press any button on it.'; }
 /* the lobby */
 const SRC=[['OpenGameArt.org · free game art and sounds','https://opengameart.org/'],['Kenney · free game assets (CC0)','https://kenney.nl/assets'],['Freesound · free sound effects','https://freesound.org/'],['itch.io · open-source games','https://itch.io/games/tag-open-source'],['GitHub · HTML5 games','https://github.com/topics/html5-game'],['Phaser · open-source game framework','https://phaser.io/'],['MDN · using game controllers on the web','https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API'],['Classic arcade history · The Strong National Museum of Play','https://www.museumofplay.org/']];
 const ORDER=['Video games','Arcade','Mobile hits','Puzzle','Word','Board','Cards','Dice','Casino'];
 const ICON={'Video games':'🕹','Arcade':'👾','Mobile hits':'📱','Puzzle':'🧩','Word':'📝','Board':'♟','Cards':'🃏','Dice':'🎲','Casino':'🎰'};
 function draw(){ const d=box(); let L=[]; try{ L=GAMES.list; }catch(_){ } const by={}; L.forEach(g=>(by[g.cat]=by[g.cat]||[]).push(g)); const cats=ORDER.filter(c=>by[c]).concat(Object.keys(by).filter(c=>!ORDER.includes(c)));
  d.innerHTML='<div class="kBar" data-sc="kVG"><button type="button" data-ka="close" data-vg="close">✕</button></div><div class="vgIn"><div class="vgBrand">The Omni-Compass LLC · DD Universe Multi-Media Studios’ KAN-IN™ · Video games</div><h2>🕹 Video games</h2><div class="vgN">'+L.length+' games, all our own code. Play with the keyboard, a mouse, touch, the 🎮 on-screen controller or a real game controller. Play chips only: no money, no prizes.</div>'+
   '<div class="vgRow"><button type="button" data-vg="surprise" data-noul>🎲 Surprise me</button><button type="button" data-vg="close" data-noul>✕ Close</button></div>'+
   '<h3>⭐ New: our own arcade classics</h3><div class="vgCards">'+NEW.map(([id,n,st,t])=>'<div class="vgCard"><i>'+esc(st)+'</i><b>'+esc(n)+'</b><span class="vgN">'+esc(t)+'</span><button type="button" data-vg="play" data-id="'+id+'" data-noul>▶ Play '+esc(n)+'</button></div>').join('')+'</div>'+
   '<h3>🗂 Every game, by kind</h3>'+cats.map(c=>'<details><summary>'+(ICON[c]||'🎮')+' '+esc(c)+' · '+by[c].length+' games</summary><div class="vgList">'+by[c].map(g=>'<button type="button" data-vg="play" data-id="'+esc(g.id)+'" data-noul>▶ '+esc(g.name)+'</button>').join('')+'</div></details>').join('')+
   '<h3>⌨ Controls monitor</h3><div class="vgRow"><label>Show the controls for <select id="vgCtl">'+L.map(g=>'<option value="'+esc(g.id)+'"'+(g.id==='vg_arena'?' selected':'')+'>'+esc(g.name)+'</option>').join('')+'</select></label></div><div id="vgMon">'+monitor('vg_arena',true)+'</div>'+
   '<h3>🎮 Controller</h3><div class="vgRow"><label>On-screen controller <select id="vgPad"><option value="auto"'+(padMode==='auto'?' selected':'')+'>Automatic (on phones and tablets)</option><option value="on"'+(padMode==='on'?' selected':'')+'>Always show</option><option value="off"'+(padMode==='off'?' selected':'')+'>Hide</option></select></label><label>Size <select id="vgPadS"><option value="s"'+(padSize==='s'?' selected':'')+'>Small</option><option value="m"'+(padSize==='m'?' selected':'')+'>Medium</option><option value="l"'+(padSize==='l'?' selected':'')+'>Large</option></select></label></div><div class="vgN" id="vgGp"></div>'+
   '<details><summary>📚 Libraries, kits and sources</summary><div class="vgList vgLinks">'+SRC.map(([t,u])=>'<a href="'+u+'" target="_blank" rel="noopener">'+esc(t)+' ↗</a>').join('')+'</div></details>'+
   '<p class="vgN" style="margin-top:22px">© 2026 The Omni-Compass LLC and DD Universe Multi-Media Studios. All rights reserved. Every game here is original code with its own names, characters and levels; the classic board, card and dice games are public domain.</p></div>'; paintGp(); }
 function box(){ let d=$('kVG'); if(!d){ d=document.createElement('div'); d.id='kVG'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Video games'); document.body.appendChild(d);
   d.addEventListener('click',e=>{ const b=e.target.closest('[data-vg]'); if(!b) return; e.stopPropagation(); const k=b.dataset.vg; if(k==='close') return close(); if(k==='play') return play(b.dataset.id); if(k==='surprise'){ try{ const L=GAMES.list; play(L[Math.floor(Math.random()*L.length)].id); }catch(_){ } } });
   d.addEventListener('change',e=>{ const t=e.target; if(t.id==='vgCtl'){ $('vgMon').innerHTML=monitor(t.value,true); } if(t.id==='vgPad'){ padMode=t.value; putLS('kanin-pad',padMode); say('🎮 On-screen controller: '+t.options[t.selectedIndex].text); } if(t.id==='vgPadS'){ padSize=t.value; putLS('kanin-pad-size',padSize); const p=$('kPadV'); if(p) p.className=padSize; } }); } return d; }
 function play(id){ close(); try{ GAMES.open(id); }catch(_){ } setTimeout(dress,300); }
 function open(){ try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ const g=$('gamesDock'); if(g&&!g.hidden) GAMES.close(); }catch(_){ } draw(); const d=box(); d.hidden=false; d.scrollTop=0; }
 function close(){ const d=$('kVG'); if(d) d.hidden=true; }
 try{ const gh=window.GOHOME; if(gh&&!gh.__kvg){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kvg=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')) close(); },true);
 /* the Menu and the rail */
 function menu(){ const t=$('tourTab'); if(!t||$('ttVG')) return; const ref=[...t.querySelectorAll('button')].find(b=>/^(🎲|🎮).*Games/i.test(b.textContent.trim())||/Games/.test(b.textContent)&&/ttGames|ttPlay/.test(b.id)); const b=document.createElement('button'); b.type='button'; b.id='ttVG'; b.className='ttMusic'; b.textContent='🕹 Video games: '+(()=>{ try{ return GAMES.list.length; }catch(_){ return ''; } })()+' games'; b.style.order=ref&&ref.style.order?ref.style.order:'4'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); if(ref) ref.insertAdjacentElement('afterend',b); else t.appendChild(b); }
 function rail(){ const d=$('rDock'); if(!d) return; let b=$('kdVG'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kdVG'; b.setAttribute('data-noul',''); b.dataset.kdI='🎮'; b.dataset.kdL='Pad'; b.title='Show or hide the on-screen game controller'; b.setAttribute('aria-label','Game controller'); b.addEventListener('click',e=>{ e.stopPropagation(); padMode=padOn()?'off':'on'; putLS('kanin-pad',padMode); say(padOn()?'🎮 On-screen controller on.':'🎮 On-screen controller hidden.'); dress(); }); d.appendChild(b); } const g=$('gamesDock'); b.hidden=!(g&&!g.hidden); b.classList.toggle('on',padOn()); }
 setInterval(()=>{ menu(); rail(); },800);
 window.KVG={open,close,play,monitor,pad:()=>padMode};
})();
