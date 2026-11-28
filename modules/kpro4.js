(()=>{ /* 🚀 PRO ARCADE (v266), part 4: STRIKE OPS 3D, a first-person tactical shooter of our own (our own compound, robots, weapons and
   missions; nothing copied from any game). A real-time 3D view drawn by ray casting: each screen column casts a ray through the map
   (a digital differential analyser steps it cell by cell), the wall it meets is drawn at a height of screen height ÷ perpendicular
   distance with a texture made on the device, darkened with distance (fog) and on the north–south faces; robots, drones and pick-ups are
   billboards depth-tested against the walls. The enemies are machines (security robots, drones and turrets): they patrol, spot you
   along a clear line of sight, close in or strafe, and fire bursts whose accuracy falls with distance and when you move.
   THE MISSION: hack the three data terminals (stand beside one for three seconds), then reach the extraction pad. Each mission adds
   more and tougher machines. Rifle (automatic), shotgun (eight pellets) and pulse launcher (blast radius). W A S D move and strafe,
   ← → or the mouse turn (click the screen to steer with the mouse, Esc to let go), Space or the mouse fire, R reload, 1 2 3 weapons,
   Shift sprint. 💥 Cannon on: a full charge calls an orbital strike where you aim. */
 const wait=fn=>{ if(window.KPRO&&window.GAMES&&GAMES.reg&&GAMES.lib) return fn(); let n=0; const t=setInterval(()=>{ if(window.KPRO&&window.GAMES&&GAMES.reg&&GAMES.lib){ clearInterval(t); fn(); } else if(++n>80) clearInterval(t); },400); };
 wait(()=>{ const {frame,rrect,reg,rnd,rr,cl}=KPRO;
 const MAP0=[
  '########################',
  '#S.....#........#......#',
  '#......#..CC....#..T...#',
  '#..MM..#........#......#',
  '#..MM......E....D......#',
  '#......#........#......#',
  '####D###...CC...###D####',
  '#......#........#......#',
  '#..T...#..####..#...E..#',
  '#......D..#..#..D......#',
  '#......#..#..#..#..CC..#',
  '#..E...#..#..#..#......#',
  '####D######D#####..#####',
  '#.........C.........M..#',
  '#..CC..........E....M..#',
  '#..........##..........#',
  '#...MM.....##.....CC...#',
  '#...MM.................#',
  '###D####....E....####D##',
  '#......#.........#.....#',
  '#..E...#...CC....#..T..#',
  '#......D.........D.....#',
  '#..X...#....E....#.....#',
  '########################'];
 const TS=64;
 function tex(kind){ const c=document.createElement('canvas'); c.width=c.height=TS; const g=c.getContext('2d'); const n=(x,y,s)=>{ const v=Math.sin(x*12.9898+y*78.233+s*37.7)*43758.5453; return v-Math.floor(v); };
  if(kind===0){ g.fillStyle='#7a7f8a'; g.fillRect(0,0,TS,TS); for(let y=0;y<TS;y++) for(let x=0;x<TS;x++){ const v=n(x,y,1); if(v>.72){ g.fillStyle='rgba(0,0,0,'+(v-.72)+')'; g.fillRect(x,y,1,1); } else if(v<.08){ g.fillStyle='rgba(255,255,255,.12)'; g.fillRect(x,y,1,1); } } g.fillStyle='rgba(0,0,0,.35)'; g.fillRect(0,31,TS,2); g.fillRect(31,0,2,31); g.fillRect(15,33,2,31); g.fillRect(47,33,2,31); }
  if(kind===1){ const gr=g.createLinearGradient(0,0,TS,0); gr.addColorStop(0,'#3a4658'); gr.addColorStop(.5,'#5d6d85'); gr.addColorStop(1,'#3a4658'); g.fillStyle=gr; g.fillRect(0,0,TS,TS); g.fillStyle='#ffcc33'; for(let i=-TS;i<TS*2;i+=16){ g.beginPath(); g.moveTo(i,54); g.lineTo(i+8,54); g.lineTo(i+16,64); g.lineTo(i+8,64); g.closePath(); g.fill(); } g.fillStyle='#222'; g.fillRect(0,52,TS,2); [[6,6],[58,6],[6,46],[58,46]].forEach(([x,y])=>{ g.fillStyle='#9aa8bf'; g.beginPath(); g.arc(x,y,2.5,0,7); g.fill(); }); g.fillStyle='rgba(111,232,255,.8)'; g.fillRect(20,20,24,4); }
  if(kind===2){ g.fillStyle='#8a5a2a'; g.fillRect(0,0,TS,TS); g.strokeStyle='#5a3610'; g.lineWidth=4; g.strokeRect(2,2,TS-4,TS-4); g.beginPath(); g.moveTo(4,4); g.lineTo(TS-4,TS-4); g.moveTo(TS-4,4); g.lineTo(4,TS-4); g.stroke(); for(let y=0;y<TS;y+=8){ g.fillStyle='rgba(0,0,0,.12)'; g.fillRect(0,y,TS,1); } }
  if(kind===3){ g.fillStyle='#2a3548'; g.fillRect(0,0,TS,TS); g.fillStyle='#16202e'; g.fillRect(8,0,48,TS); g.fillStyle='#6fe8ff'; for(let y=6;y<TS;y+=10) g.fillRect(12,y,40,2); g.fillStyle='#ff4f6d'; g.fillRect(28,28,8,8); }
  return c; }
 /* billboard sprites drawn on the device */
 function spr(kind,flash){ const c=document.createElement('canvas'); c.width=c.height=64; const g=c.getContext('2d');
  if(kind==='trooper'){ g.fillStyle='#4a5468'; rrect(g,20,18,24,30,6); g.fill(); g.fillStyle='#2e3444'; g.fillRect(22,48,8,14); g.fillRect(34,48,8,14); g.fillStyle='#5d6880'; rrect(g,22,4,20,16,6); g.fill(); g.fillStyle=flash?'#ffffff':'#ff3b3b'; g.shadowColor='#ff3b3b'; g.shadowBlur=8; g.fillRect(25,10,14,4); g.shadowBlur=0; g.fillStyle='#2e3444'; g.fillRect(40,26,16,5); g.fillRect(12,22,8,18); if(flash){ g.fillStyle='#ffe94a'; g.beginPath(); g.arc(58,28,6,0,7); g.fill(); } }
  if(kind==='drone'){ g.fillStyle='#6a7488'; g.beginPath(); g.arc(32,30,14,0,7); g.fill(); g.fillStyle=flash?'#fff':'#6fe8ff'; g.shadowColor='#6fe8ff'; g.shadowBlur=10; g.beginPath(); g.arc(32,30,5,0,7); g.fill(); g.shadowBlur=0; g.fillStyle='#3a4050'; g.fillRect(6,14,52,3); g.fillStyle='rgba(200,220,255,.5)'; g.fillRect(2,11,16,2); g.fillRect(46,11,16,2); if(flash){ g.fillStyle='#ffe94a'; g.beginPath(); g.arc(32,48,5,0,7); g.fill(); } }
  if(kind==='sentry'){ g.fillStyle='#3a4050'; g.fillRect(24,40,16,22); g.fillStyle='#55607a'; rrect(g,14,22,36,20,6); g.fill(); g.fillStyle='#2a2e3a'; g.fillRect(30,28,30,6); g.fillStyle=flash?'#fff':'#ff9a3c'; g.shadowColor='#ff9a3c'; g.shadowBlur=8; g.beginPath(); g.arc(24,32,4,0,7); g.fill(); g.shadowBlur=0; if(flash){ g.fillStyle='#ffe94a'; g.beginPath(); g.arc(60,31,6,0,7); g.fill(); } }
  if(kind==='med'){ g.fillStyle='#f2f2f2'; rrect(g,18,34,28,22,4); g.fill(); g.fillStyle='#ff3b3b'; g.fillRect(29,38,6,14); g.fillRect(25,42,14,6); }
  if(kind==='ammo'){ g.fillStyle='#4a6a2a'; rrect(g,16,38,32,20,3); g.fill(); g.fillStyle='#ffe94a'; g.font='bold 10px sans-serif'; g.fillText('AMMO',19,51); }
  if(kind==='term'){ g.fillStyle='#2a3548'; g.fillRect(20,18,24,44); g.fillStyle='#6fe8ff'; g.shadowColor='#6fe8ff'; g.shadowBlur=12; g.fillRect(23,22,18,12); g.shadowBlur=0; }
  if(kind==='termdone'){ g.fillStyle='#2a3548'; g.fillRect(20,18,24,44); g.fillStyle='#7cff8a'; g.shadowColor='#7cff8a'; g.shadowBlur=12; g.fillRect(23,22,18,12); g.shadowBlur=0; }
  if(kind==='pad'){ g.strokeStyle='#7cff8a'; g.lineWidth=3; g.beginPath(); g.ellipse(32,56,24,6,0,0,7); g.stroke(); g.fillStyle='rgba(124,255,138,.25)'; g.fillRect(10,10,44,46); }
  return c; }
 const WEAP=[{n:'Rifle',mag:30,res:180,rate:.1,dmg:16,spread:.02,pel:1,rel:1.4,auto:true},{n:'Shotgun',mag:8,res:40,rate:.75,dmg:11,spread:.09,pel:8,rel:1.8,auto:false},{n:'Pulse launcher',mag:3,res:6,rate:1.1,dmg:90,spread:0,pel:1,rel:2.2,auto:false,blast:2.2}];
 const ETYPE={trooper:{hp:60,sp:1.5,acc:.55,dmg:[6,10],cool:[.9,1.5],pts:150},drone:{hp:30,sp:2.6,acc:.4,dmg:[4,7],cool:[.6,1.1],pts:120},sentry:{hp:140,sp:0,acc:.7,dmg:[8,13],cool:[1.2,1.8],pts:300}};
 reg('pro_strike','Strike Ops 3D','🚀 Pro Arcade · first-person tactical shooter in real-time 3D. Your mission: hack the three data terminals (stand beside one for three seconds), then reach the green extraction pad, while security robots, drones and turrets hunt you. W A S D move and strafe, ← → or the mouse turn (click the screen to steer with the mouse; Esc lets go), Space or the mouse button fire, R reload, 1 2 3 switch between rifle, shotgun and pulse launcher, Shift sprint. Pick up medkits and ammo the machines drop. On a phone, the pad under the screen. 💥 Cannon on: a full charge calls an orbital strike where you aim.',ctx=>{
  let M, P, foes=[], items=[], terms=[], ext=null, spawns=[], zbuf=[], TX=null, SP={}, scr=null, sg=null, RW=0, RH=0, wi=0, ammo=[], fireT=0, relT=0, recoil=0, flashT=0, hitT=0, dmgDir=null, dmgT=0, feed=[], level=1, hack=0, wave=0, spawnT=0, strike=null, look=0, held=false;
  const wall=(x,y)=>{ const r=M[y|0]; if(!r) return 1; const c=r[x|0]; return c==='#'||c==='M'||c==='C'||c==='D'; };
  const wtype=c=>c==='M'?1:c==='C'?2:c==='D'?3:0;
  function load(F){ M=MAP0.map(r=>r.split('')); foes=[]; items=[]; terms=[]; spawns=[]; ext=null; hack=0; for(let y=0;y<M.length;y++) for(let x=0;x<M[y].length;x++){ const c=M[y][x]; if(c==='S'){ P={x:x+.5,y:y+.5,a:0.0,hp:100,ar:50,bob:0,sprint:false}; M[y][x]='.'; } if(c==='T'){ terms.push({x:x+.5,y:y+.5,done:false,p:0}); M[y][x]='.'; } if(c==='X'){ ext={x:x+.5,y:y+.5}; M[y][x]='.'; } if(c==='E'){ spawns.push({x:x+.5,y:y+.5}); M[y][x]='.'; } }
   ammo=WEAP.map(w=>({mag:w.mag,res:w.res})); wave=0; spawnT=1; for(let i=0;i<4+level;i++) spawnFoe(true); }
  function spawnFoe(init){ const sp=spawns.filter(s=>Math.hypot(s.x-P.x,s.y-P.y)>7); const s=(sp.length?sp:spawns)[rnd((sp.length?sp:spawns).length)]; const r=Math.random(); const type=r<.2+level*.03?'sentry':r<.55?'drone':'trooper'; const T=ETYPE[type]; foes.push({x:s.x+rr(-.3,.3),y:s.y+rr(-.3,.3),type,hp:Math.round(T.hp*(1+(level-1)*.15)),max:Math.round(T.hp*(1+(level-1)*.15)),alert:false,cool:rr(.5,2),flash:0,hurt:0,str:Math.random()<.5?1:-1,strT:0}); }
  function los(ax,ay,bx,by){ const d=Math.hypot(bx-ax,by-ay); const n=Math.ceil(d*6); for(let i=1;i<n;i++){ const t=i/n; if(wall(ax+(bx-ax)*t,ay+(by-ay)*t)) return false; } return true; }
  function move(o,dx,dy,r){ if(!wall(o.x+dx+Math.sign(dx)*r,o.y)&&!wall(o.x+dx+Math.sign(dx)*r,o.y+r*.7)&&!wall(o.x+dx+Math.sign(dx)*r,o.y-r*.7)) o.x+=dx; if(!wall(o.x,o.y+dy+Math.sign(dy)*r)&&!wall(o.x+r*.7,o.y+dy+Math.sign(dy)*r)&&!wall(o.x-r*.7,o.y+dy+Math.sign(dy)*r)) o.y+=dy; }
  function setup(F){ RW=Math.min(480,Math.round(F.W*.5)); RH=Math.round(RW*F.H/F.W); scr=document.createElement('canvas'); scr.width=RW; scr.height=RH; sg=scr.getContext('2d'); zbuf=new Float32Array(RW); if(!TX){ TX=[0,1,2,3].map(tex); ['trooper','drone','sentry'].forEach(k=>{ SP[k]=spr(k,false); SP[k+'F']=spr(k,true); }); ['med','ammo','term','termdone','pad'].forEach(k=>SP[k]=spr(k)); } }
  /* aim test: the nearest machine whose billboard covers the given ray, in front of the wall the ray meets */
  function aimRay(ang){ const dx=Math.cos(ang), dy=Math.sin(ang); let t=0, wallD=30; for(;t<30;t+=.05){ if(wall(P.x+dx*t,P.y+dy*t)){ wallD=t; break; } } let best=null, bd=1e9; foes.forEach(f=>{ const vx=f.x-P.x, vy=f.y-P.y; const along=vx*dx+vy*dy; if(along<=0||along>wallD) return; const across=Math.abs(-vx*dy+vy*dx); const half=f.type==='drone'?.24:.3; if(across<half&&along<bd){ bd=along; best=f; } }); return {f:best,d:best?bd:wallD,wx:P.x+dx*Math.min(wallD,best?bd:wallD),wy:P.y+dy*Math.min(wallD,best?bd:wallD)}; }
  function damageFoe(F,f,d){ f.hp-=d; f.hurt=.15; f.alert=true; hitT=.18; if(f.hp<=0){ foes.splice(foes.indexOf(f),1); const pts=ETYPE[f.type].pts*level; F.add(pts); F.feed(.07); feed.unshift({t:'✖ '+({trooper:'Security robot',drone:'Drone',sentry:'Turret'})[f.type]+' down  +'+pts,a:0}); if(feed.length>4) feed.pop(); F.snd(180,.08); if(Math.random()<.4) items.push({x:f.x,y:f.y,k:Math.random()<.5?'med':'ammo'}); } }
  function shoot(F){ const w=WEAP[wi], A=ammo[wi]; if(relT>0||fireT>0) return; if(A.mag<=0){ if(A.res>0) reload(F); else { F.snd(120,.03); F.msg('Out of ammunition for the '+w.n+'. Switch weapons (1 2 3) or find ammo.'); } return; }
   A.mag--; fireT=w.rate; recoil=1; flashT=.06; F.snd(wi===2?140:wi===1?110:260,wi===1?.09:.04);
   if(w.blast){ const r=aimRay(P.a); const bx=r.wx, by=r.wy; strikeAt(F,bx,by,w.blast,w.dmg,false); return; }
   for(let k=0;k<w.pel;k++){ const r=aimRay(P.a+rr(-w.spread,w.spread)*(P.sprint?1.6:1)); if(r.f) damageFoe(F,r.f,w.dmg); } }
  function strikeAt(F,x,y,rad,dmg,orbital){ foes.slice().forEach(f=>{ const d=Math.hypot(f.x-x,f.y-y); if(d<rad) damageFoe(F,f,Math.round(dmg*(1-d/rad*.5))); }); const dp=Math.hypot(P.x-x,P.y-y); if(!orbital&&dp<rad*.8){ hurtP(F,Math.round(30*(1-dp/rad)),x,y); } F.shake=orbital?16:8; F.flash=orbital?.8:.3; F.snd(70,.3); }
  function reload(F){ const w=WEAP[wi], A=ammo[wi]; if(relT>0||A.mag>=w.mag||A.res<=0) return; relT=w.rel; F.snd(400,.05); setTimeout(()=>{ const need=w.mag-A.mag, take=Math.min(need,A.res); A.mag+=take; A.res-=take; },w.rel*1000); }
  function hurtP(F,d,fx,fy){ const a=d*(P.ar>0?.45:1); P.ar=Math.max(0,P.ar-d*.55); P.hp-=Math.round(a); dmgT=.6; dmgDir=Math.atan2(fy-P.y,fx-P.x)-P.a; F.shake=Math.max(F.shake,4); F.snd(90,.05); if(P.hp<=0){ P.hp=0; F.end('Your operator went down on mission '+level+'.'); } }
  let F; const keys={};
  F=frame(ctx,'pro_strike',{title:'Strike Ops 3D',ratio:.6,maxW:960,hFrac:.66,charge:.0005,tapStarts:false,cannonHelp:'A full charge calls an orbital strike where you aim.',hint:'Hack the three terminals, then reach the green pad. Click the screen to steer with the mouse. Press ▶ Start.',go:'W A S D move, mouse or ← → turn, Space or click fire, R reload, 1 2 3 weapons.',
   pad:[['⟲','ArrowLeft'],['▲','w'],['▼','s'],['⟳','ArrowRight'],['🔫',' '],['↻','r'],['🔄','q']],
   reset(F){ level=1; load(F); setup(F); feed=[]; wi=0; },
   hud:F=>'Mission '+level+' · '+F.score.toLocaleString(),
   cannon(F){ const r=aimRay(P.a); strike={x:r.wx,y:r.wy,t:0}; feed.unshift({t:'💥 Orbital strike called in',a:0}); },
   key(F,e,down){ const k=e.key&&e.key.length===1?e.key.toLowerCase():e.key; if(['w','a','s','d','ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Shift',' '].includes(k)){ keys[k]=down; if(k===' ') held=down; return true; }
    if(!down) return false; if(k==='r'){ reload(F); return true; } if(k==='1'||k==='2'||k==='3'){ wi=+k-1; relT=0; F.snd(600,.03); return true; } if(k==='q'){ wi=(wi+1)%3; relT=0; return true; } return false; },
   pointer(F,t,x,y){ if(t==='down'){ if(matchMedia('(pointer:fine)').matches&&F.cv.requestPointerLock&&document.pointerLockElement!==F.cv){ try{ F.cv.requestPointerLock(); }catch(_){ } } held=true; F.lastX=x; } else if(t==='move'&&F.down&&document.pointerLockElement!==F.cv){ P.a+=(x-(F.lastX||x))*.008; F.lastX=x; } else if(t==='up') held=false; },
   update(F,dt){ if(!scr||scr.width!==Math.min(480,Math.round(F.W*.5))) setup(F);
    const sp=(keys.Shift?4.6:3)*dt; P.sprint=!!keys.Shift; const fx=Math.cos(P.a), fy=Math.sin(P.a); let mx=0,my=0; if(keys.w||keys.ArrowUp){ mx+=fx; my+=fy; } if(keys.s||keys.ArrowDown){ mx-=fx; my-=fy; } if(keys.a){ mx+=fy; my-=fx; } if(keys.d){ mx-=fy; my+=fx; }
    const ml=Math.hypot(mx,my); if(ml){ move(P,mx/ml*sp,my/ml*sp,.22); P.bob+=dt*(P.sprint?13:9); } if(keys.ArrowLeft) P.a-=2.4*dt; if(keys.ArrowRight) P.a+=2.4*dt; P.a+=look; look=0;
    fireT-=dt; if(relT>0) relT-=dt; recoil=Math.max(0,recoil-dt*6); flashT-=dt; hitT-=dt; dmgT-=dt; feed.forEach(f=>f.a+=dt); feed=feed.filter(f=>f.a<4);
    if(held&&(WEAP[wi].auto||fireT<=-.05)){ shoot(F); if(!WEAP[wi].auto) held=false; }
    /* the machines */ foes.forEach(f=>{ const T=ETYPE[f.type]; f.flash-=dt; f.hurt-=dt; const d=Math.hypot(P.x-f.x,P.y-f.y); const see=d<14&&los(f.x,f.y,P.x,P.y); if(see) f.alert=true;
     if(f.alert&&T.sp>0){ const ax=(P.x-f.x)/d, ay=(P.y-f.y)/d; f.strT-=dt; if(f.strT<=0){ f.str=Math.random()<.5?1:-1; f.strT=rr(.8,2); } let vx=0,vy=0; if(d>5||!see){ vx=ax; vy=ay; } else if(d<2.5){ vx=-ax; vy=-ay; } vx+=-ay*f.str*.8; vy+=ax*f.str*.8; const l=Math.hypot(vx,vy)||1; move(f,vx/l*T.sp*dt,vy/l*T.sp*dt,.25); }
     f.cool-=dt; if(see&&f.cool<=0&&d<16){ f.cool=rr(T.cool[0],T.cool[1])/(1+level*.05); f.flash=.1; F.snd(330,.02); const acc=T.acc*(1-d/18)*(ml?.7:1)*(1+level*.04); if(Math.random()<acc) hurtP(F,T.dmg[0]+rnd(T.dmg[1]-T.dmg[0]+1),f.x,f.y); } });
    for(let i=items.length-1;i>=0;i--){ const it=items[i]; if(Math.hypot(it.x-P.x,it.y-P.y)<.6){ if(it.k==='med'){ P.hp=Math.min(100,P.hp+35); P.ar=Math.min(100,P.ar+15); feed.unshift({t:'✚ Medkit +35',a:0}); } else { ammo.forEach((A,j)=>A.res+=[60,12,2][j]); feed.unshift({t:'▮ Ammunition',a:0}); } items.splice(i,1); F.snd(760,.05); } }
    /* the objectives */ terms.forEach(t=>{ if(t.done) return; if(Math.hypot(t.x-P.x,t.y-P.y)<1.3){ t.p+=dt/3; if(t.p>=1){ t.done=true; hack++; F.add(1000*level); F.feed(.2); feed.unshift({t:'⌁ Terminal hacked '+hack+'/3',a:0}); F.snd(990,.15); if(hack===3) feed.unshift({t:'➜ Extraction pad open',a:0}); } } else t.p=Math.max(0,t.p-dt*.3); });
    if(hack===3&&ext&&Math.hypot(ext.x-P.x,ext.y-P.y)<.9){ F.add(5000*level+P.hp*20); level++; feed.unshift({t:'✔ Mission complete · mission '+level,a:0}); F.text(F.W/2,F.H*.35,'MISSION COMPLETE','#7cff8a',30); F.snd(880,.3); load(F); return; }
    spawnT-=dt; if(spawnT<=0){ spawnT=Math.max(3,9-level); if(foes.length<5+level*2) spawnFoe(false); }
    if(strike){ strike.t+=dt; if(strike.t>=.8){ strikeAt(F,strike.x,strike.y,3.6,220,true); feed.unshift({t:'💥 Orbital strike',a:0}); strike=null; } } },
   draw(F){ const g=F.g, W=F.W, H=F.H; if(!scr) setup(F); const sgc=sg;
    const sky=sgc.createLinearGradient(0,0,0,RH/2); sky.addColorStop(0,'#0a1230'); sky.addColorStop(1,'#3a2a5a'); sgc.fillStyle=sky; sgc.fillRect(0,0,RW,RH/2); const fl=sgc.createLinearGradient(0,RH/2,0,RH); fl.addColorStop(0,'#1a1a22'); fl.addColorStop(1,'#4a4a52'); sgc.fillStyle=fl; sgc.fillRect(0,RH/2,RW,RH/2);
    const dx=Math.cos(P.a), dy=Math.sin(P.a), px=-dy*.66, py=dx*.66; const bobY=Math.sin(P.bob)*RH*.008;
    for(let x=0;x<RW;x++){ const cx=2*x/RW-1; const rx=dx+px*cx, ry=dy+py*cx; let mx=P.x|0, my=P.y|0; const ddx=Math.abs(1/rx), ddy=Math.abs(1/ry); let sx,sy,sdx,sdy; if(rx<0){ sx=-1; sdx=(P.x-mx)*ddx; } else { sx=1; sdx=(mx+1-P.x)*ddx; } if(ry<0){ sy=-1; sdy=(P.y-my)*ddy; } else { sy=1; sdy=(my+1-P.y)*ddy; }
     let side=0, hitc='#', n=0; while(n++<64){ if(sdx<sdy){ sdx+=ddx; mx+=sx; side=0; } else { sdy+=ddy; my+=sy; side=1; } const c=M[my]&&M[my][mx]; if(c===undefined){ hitc='#'; break; } if(c==='#'||c==='M'||c==='C'||c==='D'){ hitc=c; break; } }
     const pd=side===0?(sdx-ddx):(sdy-ddy); zbuf[x]=pd; const lh=RH/Math.max(.01,pd); const y0=RH/2-lh/2+bobY; let wx=side===0?P.y+pd*ry:P.x+pd*rx; wx-=Math.floor(wx); let tx=Math.floor(wx*TS); if(side===0&&rx>0) tx=TS-tx-1; if(side===1&&ry<0) tx=TS-tx-1;
     sgc.drawImage(TX[wtype(hitc)],tx,0,1,TS,x,y0,1,lh); const fog=Math.min(.88,pd/14)+(side?.18:0); if(fog>0.02){ sgc.fillStyle='rgba(6,6,16,'+fog+')'; sgc.fillRect(x,y0,1,lh); } }
    /* billboards, far to near */ const bills=[]; foes.forEach(f=>bills.push({x:f.x,y:f.y,img:f.flash>0?SP[f.type+'F']:SP[f.type],s:f.type==='drone'?.7:1,lift:f.type==='drone'?-.25:0,hurt:f.hurt>0,f})); items.forEach(it=>bills.push({x:it.x,y:it.y,img:SP[it.k],s:.6,lift:.2})); terms.forEach(t=>bills.push({x:t.x,y:t.y,img:t.done?SP.termdone:SP.term,s:.9,lift:0})); if(ext) bills.push({x:ext.x,y:ext.y,img:SP.pad,s:1,lift:0,glow:hack===3});
    bills.forEach(b=>b.d=(b.x-P.x)**2+(b.y-P.y)**2); bills.sort((a,b)=>b.d-a.d); const inv=1/(px*dy-dx*py);
    bills.forEach(b=>{ const rx=b.x-P.x, ry=b.y-P.y; const tX=inv*(dy*rx-dx*ry), tY=inv*(-py*rx+px*ry); if(tY<=.15) return; const scx=Math.round(RW/2*(1+tX/tY)); const sh=Math.abs(RH/tY)*b.s; const sw=sh; const y0=RH/2-sh/2+RH/tY*b.lift*.5+(RH/tY)*(1-b.s)*.5+bobY; const x0=scx-sw/2; const fog=Math.min(.85,Math.sqrt(b.d)/14);
     for(let sx=Math.max(0,Math.floor(x0));sx<Math.min(RW,x0+sw);sx++){ if(tY>=zbuf[sx]) continue; const u=Math.floor((sx-x0)/sw*64); sgc.drawImage(b.img,u,0,1,64,sx,y0,1,sh); }
     if(fog>.05||b.hurt){ sgc.save(); sgc.beginPath(); let any=false; for(let sx=Math.max(0,Math.floor(x0));sx<Math.min(RW,x0+sw);sx++){ if(tY<zbuf[sx]){ sgc.rect(sx,y0,1,sh); any=true; } } if(any){ sgc.clip(); sgc.globalCompositeOperation='source-atop'; } sgc.restore(); }
     if(b.f&&b.f.hp<b.f.max&&tY<zbuf[Math.max(0,Math.min(RW-1,scx))]){ sgc.fillStyle='rgba(0,0,0,.6)'; sgc.fillRect(scx-sw*.3,y0-4,sw*.6,3); sgc.fillStyle='#ff4f6d'; sgc.fillRect(scx-sw*.3,y0-4,sw*.6*b.f.hp/b.f.max,3); } });
    g.imageSmoothingEnabled=false; g.drawImage(scr,0,0,W,H); g.imageSmoothingEnabled=true;
    if(strike){ const a=Math.sin(strike.t*30)>0; g.strokeStyle=a?'#ff3b3b':'#ffe94a'; g.lineWidth=3; g.beginPath(); g.arc(W/2,H/2,30+strike.t*40,0,7); g.stroke(); }
    /* the weapon in hand */ const bx=W*.62+Math.cos(P.bob)*6, by=H-H*.04+Math.abs(Math.sin(P.bob))*6+recoil*18; g.save(); g.translate(bx,by); g.fillStyle='#1d222c'; g.beginPath(); g.moveTo(-40,0); g.lineTo(-10,-H*.2); g.lineTo(30,-H*.2); g.lineTo(60,0); g.closePath(); g.fill(); g.fillStyle=['#3a4658','#5a3a1a','#2a5058'][wi]; rrect(g,-14,-H*.26,40,H*.1,6); g.fill(); g.fillStyle='#0c0f16'; g.fillRect(-2,-H*.32,16,H*.08);
     if(flashT>0){ g.globalCompositeOperation='lighter'; const mg=g.createRadialGradient(6,-H*.33,0,6,-H*.33,40); mg.addColorStop(0,'rgba(255,240,180,1)'); mg.addColorStop(1,'rgba(255,140,40,0)'); g.fillStyle=mg; g.beginPath(); g.arc(6,-H*.33,40,0,7); g.fill(); g.globalCompositeOperation='source-over'; } g.restore();
    /* crosshair, hit marker, damage direction */ const gap=6+recoil*10+(P.sprint?6:0); g.strokeStyle='rgba(255,255,255,.9)'; g.lineWidth=2; [[1,0],[-1,0],[0,1],[0,-1]].forEach(([a,b])=>{ g.beginPath(); g.moveTo(W/2+a*gap,H/2+b*gap); g.lineTo(W/2+a*(gap+8),H/2+b*(gap+8)); g.stroke(); });
    if(hitT>0){ g.strokeStyle='#ffe94a'; g.lineWidth=3; [[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([a,b])=>{ g.beginPath(); g.moveTo(W/2+a*6,H/2+b*6); g.lineTo(W/2+a*13,H/2+b*13); g.stroke(); }); }
    if(dmgT>0&&dmgDir!=null){ g.save(); g.translate(W/2,H/2); g.rotate(dmgDir); g.strokeStyle='rgba(255,40,60,'+dmgT+')'; g.lineWidth=8; g.beginPath(); g.arc(0,0,Math.min(W,H)*.3,-.35,.35); g.stroke(); g.restore(); g.fillStyle='rgba(255,0,30,'+(dmgT*.18)+')'; g.fillRect(0,0,W,H); }
    /* HUD: health, armour, weapon, ammo, objective, minimap, compass, feed */ g.fillStyle='rgba(0,0,0,.5)'; rrect(g,10,H-52,190,42,10); g.fill(); g.fillStyle='#ff4f6d'; g.fillRect(18,H-44,170*P.hp/100,10); g.fillStyle='#6fe8ff'; g.fillRect(18,H-28,170*P.ar/100,6); g.fillStyle='#fff'; g.font='800 11px system-ui,sans-serif'; g.textAlign='left'; g.fillText('HEALTH '+P.hp+'  ·  ARMOUR '+Math.round(P.ar),18,H-14);
    const A=ammo[wi]; g.fillStyle='rgba(0,0,0,.5)'; rrect(g,W-180,H-52,170,42,10); g.fill(); g.fillStyle='#fff'; g.font='900 20px ui-monospace,monospace'; g.textAlign='right'; g.fillText((relT>0?'RELOAD':A.mag+' / '+A.res),W-20,H-24); g.font='800 11px system-ui,sans-serif'; g.fillStyle='#ffe94a'; g.fillText((wi+1)+' · '+WEAP[wi].n.toUpperCase(),W-20,H-12);
    g.textAlign='center'; g.fillStyle='rgba(0,0,0,.5)'; rrect(g,W/2-170,30,340,24,8); g.fill(); g.fillStyle=hack===3?'#7cff8a':'#ffe94a'; g.font='800 13px system-ui,sans-serif'; const near=terms.find(t=>!t.done&&t.p>0); g.fillText(hack<3?(near?'HACKING… '+Math.round(near.p*100)+'%':'Hack the data terminals · '+hack+' / 3'):'Reach the green extraction pad',W/2,47);
    const hd=((P.a*180/Math.PI)%360+360)%360; g.fillStyle='rgba(255,255,255,.65)'; g.font='700 10px ui-monospace,monospace'; [['N',270],['E',0],['S',90],['W',180]].forEach(([l,deg])=>{ let off=((deg-hd+540)%360)-180; if(Math.abs(off)<60) g.fillText(l,W/2+off*2.6,66); });
    const ms=Math.min(120,W*.16), cs=ms/24, mxp=W-ms-12, myp=34; g.fillStyle='rgba(0,0,0,.55)'; g.fillRect(mxp-3,myp-3,ms+6,ms+6); for(let y=0;y<24;y++) for(let x=0;x<24;x++){ const c=M[y][x]; if(c!=='.'){ g.fillStyle=c==='C'?'#8a5a2a':c==='D'?'#2a5068':'#5a6070'; g.fillRect(mxp+x*cs,myp+y*cs,cs,cs); } }
    terms.forEach(t=>{ g.fillStyle=t.done?'#7cff8a':'#6fe8ff'; g.fillRect(mxp+t.x*cs-2,myp+t.y*cs-2,4,4); }); if(ext&&hack===3){ g.fillStyle='#7cff8a'; g.beginPath(); g.arc(mxp+ext.x*cs,myp+ext.y*cs,4,0,7); g.fill(); } foes.forEach(f=>{ if(f.alert){ g.fillStyle='#ff4f6d'; g.fillRect(mxp+f.x*cs-1.5,myp+f.y*cs-1.5,3,3); } });
    g.fillStyle='#fff'; g.beginPath(); g.arc(mxp+P.x*cs,myp+P.y*cs,2.6,0,7); g.fill(); g.strokeStyle='#fff'; g.beginPath(); g.moveTo(mxp+P.x*cs,myp+P.y*cs); g.lineTo(mxp+(P.x+Math.cos(P.a)*2)*cs,myp+(P.y+Math.sin(P.a)*2)*cs); g.stroke();
    g.textAlign='left'; feed.forEach((f,i)=>{ g.globalAlpha=Math.max(0,1-f.a/4); g.fillStyle='#fff'; g.font='800 12px system-ui,sans-serif'; g.fillText(f.t,12,48+i*16); }); g.globalAlpha=1; } });
  /* the mouse steers while the screen holds the pointer */
  const mm=e=>{ if(document.pointerLockElement===F.cv&&F.running&&!F.paused) look+=e.movementX*.0026; };
  const md=e=>{ if(document.pointerLockElement===F.cv&&F.running&&!F.paused){ held=true; } }; const mu=()=>{ if(document.pointerLockElement===F.cv) held=false; };
  document.addEventListener('mousemove',mm); document.addEventListener('mousedown',md); document.addEventListener('mouseup',mu);
  const stop=()=>{ document.removeEventListener('mousemove',mm); document.removeEventListener('mousedown',md); document.removeEventListener('mouseup',mu); try{ if(document.pointerLockElement===F.cv) document.exitPointerLock(); }catch(_){ } };
  return {stop,state:()=>({level,hp:P.hp,hack,foes:foes.length,x:P.x,y:P.y,a:P.a,wi,ammo:ammo.map(a=>a.mag+'/'+a.res),score:F.score}),F,keys,face:a=>{ P.a=a; },tp:(x,y)=>{ P.x=x; P.y=y; }};
 });
 });
})();
