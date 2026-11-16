(()=>{ /* VIDEO GAMES: six of our own games in the classic arcade styles. Our own names, heroes, worlds and levels; nothing copied.
   Storm Tower (girder climb), Bakery Drop (shelf-stacking chase), Orbit Guard (side-scrolling planet defender with radar),
   Vortex Rim (tube shooter), Neon Arena (twin-stick arena) and Night Highway (road racer). Same frame as Mobile hits. */
 const CAT='Video games';
/*@FRAME@*/
 const KEYS=new Set(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown',' ','Enter','w','a','s','d','x','z','Shift']);
 const KS=(F,e,down)=>{ const k=e.key&&e.key.length===1?e.key.toLowerCase():e.key; if(!KEYS.has(k)) return false; F.keys[k]=down; return true; };
 const L=F=>F.keys.ArrowLeft||F.keys.a, R=F=>F.keys.ArrowRight||F.keys.d, U=F=>F.keys.ArrowUp||F.keys.w, D=F=>F.keys.ArrowDown||F.keys.s;
 const edge=(F,k)=>{ F.pv=F.pv||{}; const on=!!F.keys[k], was=!!F.pv[k]; F.pv[k]=on; return on&&!was; };
 const lerp=(a,b,t)=>a+(b-a)*t;
 function boom(g,x,y,t,c){ g.save(); g.globalAlpha=Math.max(0,1-t); g.strokeStyle=c||'#ffe94a'; g.lineWidth=2; for(let k=0;k<8;k++){ const a=k*Math.PI/4, r=6+t*26; g.beginPath(); g.moveTo(x+Math.cos(a)*r*0.4,y+Math.sin(a)*r*0.4); g.lineTo(x+Math.cos(a)*r,y+Math.sin(a)*r); g.stroke(); } g.restore(); }

 /* 1 · STORM TOWER: climb the girders, jump the thunderballs the storm cloud rolls down, reach the compass at the top */
 reg('vg_tower','Storm Tower','Climb the tower to the golden compass at the top. Nimbus the storm cloud rolls thunderballs down the sloped girders: jump over them (100 each) or grab the spark wrench to smash them (300). Climb ladders with Up and Down. Keys: ← → move, ↑ ↓ climb, Space jumps. Touch: hold left or right of the robot to walk, hold above or below at a ladder to climb, tap quickly to jump.',ctx=>{
  const N=6; let G=[], LD=[], P, balls=[], fx=[], lv=1, lives=3, spawnT=0, wrench=0, wr, bonus=3000, tap=0, jumpReq=false;
  const F=frame(ctx,'vg_tower',{ratio:0.95,maxW:640,title:'Storm Tower',go:'Climb! Jump the thunderballs.',hint:'Press ▶ Start. ← → walk, ↑ ↓ ladders, Space jumps.',
   reset:F=>{ lv=1; lives=3; build(F); }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS,
   pointer:(F,t,x,y)=>{ if(t==='down') tap=F.t; if(t==='up'&&F.t-tap<0.2) jumpReq=true; },
   buttons:F=>[['⤴ Jump',()=>{ jumpReq=true; }]], hud:F=>'Score '+F.score+' · lives '+lives+' · level '+lv+' · bonus '+Math.max(0,Math.round(bonus))});
  function gy(i,x){ const s=G[i]; return s.yl+(s.yr-s.yl)*(cl(x,s.xa,s.xb)-s.xa)/(s.xb-s.xa); }
  function build(F){ const W=F.W,H=F.H, yB=H-20, top=64, sp=(yB-top)/(N-1); G=[]; LD=[];
   for(let i=0;i<N;i++){ const y=yB-i*sp; if(i===0) G.push({xa:6,xb:W-6,yl:y,yr:y}); else if(i%2) G.push({xa:6,xb:W-46,yl:y-9,yr:y+9}); else G.push({xa:46,xb:W-6,yl:y+9,yr:y-9}); }
   for(let i=0;i<N-1;i++){ const xs=i%2?[0.38,0.72]:[0.2,0.6]; xs.forEach((f,k)=>LD.push({x:Math.round(W*(f+((lv+i+k)%3)*0.03)),lo:i,hi:i+1})); }
   wr={x:W*0.5,i:2,taken:false}; P={x:24,y:gy(0,24),i:0,vy:0,air:false,climb:null,face:1,step:0}; balls=[]; fx=[]; spawnT=1.2; wrench=0; bonus=3000; }
  function hurt(F){ lives--; F.snd(120,.3); fx.push({x:P.x,y:P.y-10,t:0,c:'#6fe8ff'}); if(lives<=0) return F.end('The storm got you.'); F.msg('Ouch! '+lives+' left. Up you go again.'); const s=F.score; build(F); F.score=s; }
  function step(F,dt){ const W=F.W, sp=W*0.3, j=edge(F,' ')||jumpReq; jumpReq=false; bonus=Math.max(0,bonus-40*dt); wrench=Math.max(0,wrench-dt);
   let mx=(R(F)?1:0)-(L(F)?1:0), up=U(F), dn=D(F);
   if(F.down&&!P.climb){ const dx=F.px-P.x, dy=F.py-(P.y-10); const near=LD.find(l=>Math.abs(l.x-P.x)<16&&((dy<-30&&l.lo===P.i)||(dy>30&&l.hi===P.i))); if(near){ up=dy<0; dn=dy>0; } else if(Math.abs(dx)>8) mx=Math.sign(dx); }
   if(F.down&&P.climb){ const dy=F.py-(P.y-10); up=dy<-6; dn=dy>6; }
   if(P.climb){ const l=P.climb, yT=gy(l.hi,l.x), yBt=gy(l.lo,l.x); if(up) P.y-=W*0.2*dt; if(dn) P.y+=W*0.2*dt; P.step+=(up||dn)?dt*8:0;
    if(P.y<=yT){ P.y=yT; P.i=l.hi; P.climb=null; } else if(P.y>=yBt){ P.y=yBt; P.i=l.lo; P.climb=null; } }
   else if(!P.air){ if(mx){ P.face=mx; P.x=cl(P.x+mx*sp*dt,G[P.i].xa+6,G[P.i].xb-6); P.step+=dt*10; } P.y=gy(P.i,P.x);
    if(up){ const l=LD.find(l=>l.lo===P.i&&Math.abs(l.x-P.x)<9); if(l){ P.climb=l; P.x=l.x; } }
    if(dn&&!P.climb){ const l=LD.find(l=>l.hi===P.i&&Math.abs(l.x-P.x)<9); if(l){ P.climb=l; P.x=l.x; P.y+=2; } }
    if(j&&!P.climb){ P.air=true; P.vy=-Math.sqrt(2*760*F.H*0.085); P.vx=mx*sp; F.snd(620,.04); } }
   else { P.x=cl(P.x+P.vx*dt,G[P.i].xa+6,G[P.i].xb-6); P.vy+=760*dt; P.y+=P.vy*dt; const g0=gy(P.i,P.x); if(P.vy>0&&P.y>=g0){ P.y=g0; P.air=false; } }
   if(!wr.taken&&P.i===wr.i&&!P.climb&&Math.abs(P.x-wr.x)<12){ wr.taken=true; wrench=7; F.add(200); F.msg('⚡ Spark wrench! Smash thunderballs for 7 seconds.'); F.snd(880,.12); }
   spawnT-=dt; if(spawnT<=0){ spawnT=Math.max(0.85,2.7-lv*0.28)*rr(0.75,1.25); const t=N-1; balls.push({x:G[t].xa+30,y:0,i:t,dir:1,st:'roll',vy:0,r:Math.max(6,W*0.02),done:new Set(),jumped:false,a:0}); }
   const bs=W*0.3*(1+0.09*(lv-1));
   balls.forEach(b=>{ b.a+=dt*b.dir*8;
    if(b.st==='roll'){ b.x+=b.dir*bs*dt; const s=G[b.i]; b.y=gy(b.i,b.x)-b.r;
     const l=LD.find(l=>l.hi===b.i&&Math.abs(l.x-b.x)<3&&!b.done.has(l)); if(l){ b.done.add(l); if(Math.random()<0.28+0.03*lv){ b.st='lad'; b.x=l.x; b.l=l; } }
     if(b.st==='roll'&&((b.dir>0&&b.x>s.xb)||(b.dir<0&&b.x<s.xa))){ if(b.i===0) b.gone=true; else { b.st='fall'; b.vy=0; } } }
    else if(b.st==='fall'){ b.vy+=760*dt; b.y+=b.vy*dt; b.x+=b.dir*bs*0.25*dt; const n=b.i-1; if(b.y+b.r>=gy(n,b.x)){ b.i=n; b.st='roll'; b.dir=n===0?-1:(n%2?1:-1); } }
    else { b.y+=bs*0.75*dt; const n=b.l.lo; if(b.y+b.r>=gy(n,b.x)){ b.i=n; b.st='roll'; b.dir=n===0?-1:(n%2?1:-1); } }
    const cx=P.x, cy=P.y-11; if(Math.hypot(b.x-cx,b.y-cy)<b.r+9){ if(wrench>0){ b.gone=true; F.add(300); fx.push({x:b.x,y:b.y,t:0}); F.snd(300,.08); } else { b.hit=true; } }
    if(P.air&&!b.jumped&&Math.abs(b.x-P.x)<12&&b.y>P.y&&b.i===P.i){ b.jumped=true; F.add(100); F.snd(760,.05); } });
   if(balls.some(b=>b.hit)) return hurt(F);
   balls=balls.filter(b=>!b.gone&&b.x>-30&&b.x<W+30);
   fx.forEach(e=>e.t+=dt*2); fx=fx.filter(e=>e.t<1);
   if(P.i===N-1&&!P.climb&&Math.abs(P.x-F.W*0.62)<14){ const s=F.score+1000+Math.round(bonus); lv++; F.snd(990,.2); build(F); F.score=s; F.msg('🧭 You reached the compass! Level '+lv+': the storm rolls faster.'); } }
  function paint(F){ const g=F.g,W=F.W,H=F.H; const bg=g.createLinearGradient(0,0,0,H); bg.addColorStop(0,'#0b0b2e'); bg.addColorStop(1,'#1a0f3a'); g.fillStyle=bg; g.fillRect(0,0,W,H);
   for(let k=0;k<30;k++){ g.fillStyle='rgba(255,255,255,'+(0.2+0.3*((k*7)%5)/5)+')'; g.fillRect((k*97)%W,(k*53)%(H*0.5)+26,1.5,1.5); }
   LD.forEach(l=>{ const y1=gy(l.hi,l.x), y2=gy(l.lo,l.x); g.strokeStyle='#6fe8ff'; g.lineWidth=2; g.beginPath(); g.moveTo(l.x-6,y1); g.lineTo(l.x-6,y2); g.moveTo(l.x+6,y1); g.lineTo(l.x+6,y2); for(let y=y1+5;y<y2;y+=7){ g.moveTo(l.x-6,y); g.lineTo(l.x+6,y); } g.stroke(); });
   G.forEach(s=>{ g.strokeStyle='#ff4f6d'; g.lineWidth=7; g.beginPath(); g.moveTo(s.xa,s.yl+3); g.lineTo(s.xb,s.yr+3); g.stroke(); g.strokeStyle='#7a1830'; g.lineWidth=1.5; for(let x=s.xa+6;x<s.xb;x+=12){ const y=s.yl+(s.yr-s.yl)*(x-s.xa)/(s.xb-s.xa); g.beginPath(); g.moveTo(x,y); g.lineTo(x+6,y+6); g.stroke(); } });
   const t=G[N-1], cx=t.xa+16, cy=t.yl-26; g.fillStyle='#9aa3c7'; [[0,0,14],[14,-5,12],[26,2,11],[-12,4,10]].forEach(([a,b,r])=>{ g.beginPath(); g.arc(cx+a,cy+b,r,0,7); g.fill(); }); g.fillStyle='#ffe94a'; g.fillRect(cx+2,cy-2,4,3); g.fillRect(cx+12,cy-2,4,3); if(Math.sin(F.t*6)>0.6){ g.strokeStyle='#ffe94a'; g.lineWidth=2; g.beginPath(); g.moveTo(cx+6,cy+12); g.lineTo(cx+2,cy+20); g.lineTo(cx+8,cy+20); g.lineTo(cx+4,cy+30); g.stroke(); }
   const gx=W*0.62, gyy=gy(N-1,gx)-16; g.fillStyle='#ffe94a'; g.beginPath(); g.arc(gx,gyy,9,0,7); g.fill(); g.fillStyle='#14163a'; g.beginPath(); g.moveTo(gx,gyy-7); g.lineTo(gx+3,gyy); g.lineTo(gx-3,gyy); g.fill(); g.fillStyle='#ff4f6d'; g.beginPath(); g.moveTo(gx,gyy+7); g.lineTo(gx+3,gyy); g.lineTo(gx-3,gyy); g.fill();
   if(!wr.taken){ const y=gy(wr.i,wr.x)-10; g.save(); g.translate(wr.x,y); g.rotate(Math.sin(F.t*3)*0.4); g.fillStyle='#7cff8a'; g.fillRect(-2,-8,4,14); g.beginPath(); g.arc(0,-9,5,0,7); g.fill(); g.restore(); }
   balls.forEach(b=>{ const gr=g.createRadialGradient(b.x,b.y,1,b.x,b.y,b.r); gr.addColorStop(0,'#fff'); gr.addColorStop(1,'#3d7bff'); g.fillStyle=gr; g.beginPath(); g.arc(b.x,b.y,b.r,0,7); g.fill(); g.strokeStyle='#ffe94a'; g.lineWidth=1.5; g.beginPath(); const a=b.a; g.moveTo(b.x+Math.cos(a)*b.r*0.8,b.y+Math.sin(a)*b.r*0.8); g.lineTo(b.x,b.y); g.lineTo(b.x-Math.cos(a+1)*b.r*0.8,b.y-Math.sin(a+1)*b.r*0.8); g.stroke(); });
   const x=P.x,y=P.y, leg=Math.sin(P.step)*3; g.fillStyle=wrench>0&&Math.sin(F.t*20)>0?'#7cff8a':'#ffe94a'; g.fillRect(x-6,y-18,12,11); g.fillStyle='#ffd23f'; g.fillRect(x-5,y-25,10,7); g.fillStyle='#14163a'; g.fillRect(x+(P.face>0?0:-4),y-23,4,3); g.fillStyle='#c9a400'; g.fillRect(x-5,y-7,3,7+leg*0.3); g.fillRect(x+2,y-7,3,7-leg*0.3); if(wrench>0){ g.fillStyle='#7cff8a'; g.fillRect(x+P.face*7,y-22,3,12); }
   fx.forEach(e=>boom(g,e.x,e.y,e.t,e.c)); }
  return {state:()=>({score:F.score,lives,level:lv,girder:P.i})}; });

 /* 2 · BAKERY DROP: walk across every cake layer to drop it down a shelf; stack every cake on its plate; runaway dough chases you */
 reg('vg_bake','Bakery Drop','You are Pip the baker. Walk across all four parts of a cake layer and it drops one shelf down, knocking the layer below it down too. Get every layer of every cake onto its plate at the bottom to clear the level. Runaway dough blobs chase you: a layer dropped on a blob squashes it (500); Space throws a flour puff that freezes the blobs in front of you (three a level). Keys: ← → walk, ↑ ↓ ladders, Space flour. Touch: hold where you want to go.',ctx=>{
  const FN=5, C=4; let lay=[], LD=[], P, en=[], fx=[], lv=1, lives=3, puffs=3, plates=[0,0,0,0], cloud=null;
  const TY=[['#ff4f6d','#fff3f7'],['#ff9ad5','#ffd6ef'],['#fff5d6','#e8dcb2'],['#e8b04a','#b57a22']];
  const F=frame(ctx,'vg_bake',{ratio:0.92,maxW:640,title:'Bakery Drop',go:'Bake! Walk over the layers.',hint:'Press ▶ Start. ← → walk, ↑ ↓ ladders, Space throws flour.',
   reset:F=>{ lv=1; lives=3; build(F); }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS, buttons:F=>[['☁ Flour',()=>{ F.keys[' ']=true; setTimeout(()=>{ F.keys[' ']=false; },60); }]],
   hud:F=>'Score '+F.score+' · lives '+lives+' · flour '+puffs+' · level '+lv});
  function floorY(f){ return 52+f*((F.H-58-46)/(FN-1)); }
  function colX(c){ return F.W*(c+0.5)/C; } function lw(){ return F.W/C*0.72; }
  function build(Fr){ const W=Fr.W; lay=[]; LD=[]; plates=[0,0,0,0]; puffs=3; cloud=null;
   for(let c=0;c<C;c++){ const fl=[0,1,2,3]; if((c+lv)%3===0) fl.splice(1,1,1); fl.forEach((f,k)=>lay.push({c,f,type:k,seg:[0,0,0,0],fall:null,py:0})); }
   for(let f=0;f<FN-1;f++){ const gaps=f%2?[1,3]:[0,2,4]; gaps.forEach(j=>LD.push({x:j===0?W*0.035:j===C?W*0.965:W*j/C,lo:f+1,hi:f})); }
   P={f:FN-1,x:W/2,climb:null,face:1,step:0}; en=[]; const n=Math.min(5,1+lv); for(let k=0;k<n;k++) en.push({f:0,x:k%2?W*0.08:W*0.92,climb:null,frz:0,dead:k*2.5,sp:W*(0.13+0.015*lv)*(0.85+0.1*k),plan:null}); fx=[]; }
  function drop(L,Fr){ if(L.fall) return; L.fall={y:floorY(L.f),vy:0,to:L.f+1}; Fr.add(50); Fr.snd(420,.05); }
  function step(Fr,dt){ const W=Fr.W, sp=W*0.28; let mx=(R(Fr)?1:0)-(L(Fr)?1:0), up=U(Fr), dn=D(Fr);
   if(Fr.down){ const dy=Fr.py-floorY(P.f), dx=Fr.px-P.x; const want=Math.abs(dy)>24; const l=LD.find(l=>Math.abs(l.x-P.x)<14&&((dy<0&&l.lo===P.f)||(dy>0&&l.hi===P.f))); if(P.climb){ up=dy<-4; dn=dy>4; mx=0; } else if(want&&l){ up=dy<0; dn=dy>0; } else if(want){ const t=LD.filter(l=>dy<0?l.lo===P.f:l.hi===P.f).sort((a,b)=>Math.abs(a.x-P.x)-Math.abs(b.x-P.x))[0]; if(t) mx=Math.sign(t.x-P.x); } else if(Math.abs(dx)>6) mx=Math.sign(dx); }
   if(P.climb){ const l=P.climb; const yT=floorY(l.hi), yB=floorY(l.lo); if(up) P.cy-=W*0.22*dt; if(dn) P.cy+=W*0.22*dt; P.step+=(up||dn)?dt*8:0; if(P.cy<=yT){ P.f=l.hi; P.climb=null; } else if(P.cy>=yB){ P.f=l.lo; P.climb=null; } }
   else { if(mx){ P.face=mx; P.x=cl(P.x+mx*sp*dt,8,W-8); P.step+=dt*10; }
    if(up){ const l=LD.find(l=>l.lo===P.f&&Math.abs(l.x-P.x)<10); if(l){ P.climb=l; P.x=l.x; P.cy=floorY(P.f); } }
    if(dn&&!P.climb){ const l=LD.find(l=>l.hi===P.f&&Math.abs(l.x-P.x)<10); if(l){ P.climb=l; P.x=l.x; P.cy=floorY(P.f); } }
    lay.forEach(Lr=>{ if(Lr.fall||Lr.f!==P.f) return; const x0=colX(Lr.c)-lw()/2; const k=Math.floor((P.x-x0)/(lw()/4)); if(k>=0&&k<4&&!Lr.seg[k]){ Lr.seg[k]=1; Fr.snd(300+k*60,.03); if(Lr.seg.every(Boolean)) drop(Lr,Fr); } }); }
   if(edge(Fr,' ')&&puffs>0&&!P.climb){ puffs--; cloud={f:P.f,x:P.x+P.face*40,t:0}; en.forEach(e=>{ if(!e.climb&&e.f===P.f&&Math.sign(e.x-P.x)===P.face&&Math.abs(e.x-P.x)<W*0.32) e.frz=3; }); Fr.snd(200,.12); }
   if(cloud){ cloud.t+=dt; if(cloud.t>0.8) cloud=null; }
   lay.forEach(Lr=>{ if(!Lr.fall) return; const fl=Lr.fall; fl.vy+=900*dt; fl.y+=fl.vy*dt; const tgtY=fl.to>=FN?Fr.H-10-plates[Lr.c]*7:floorY(fl.to);
    if(fl.y>=tgtY){ en.forEach(e=>{ if(e.dead<=0&&!e.climb&&e.f===fl.to&&Math.abs(e.x-colX(Lr.c))<lw()/2+6){ e.dead=4; Fr.add(500); fx.push({x:e.x,y:floorY(e.f)-8,t:0,c:'#fff3f7'}); Fr.snd(180,.15); } });
     if(fl.to>=FN){ Lr.f='plate'; Lr.py=plates[Lr.c]++; Lr.fall=null; Fr.add(100); }
     else { const below=lay.find(o=>o!==Lr&&!o.fall&&o.c===Lr.c&&o.f===fl.to); Lr.f=fl.to; Lr.fall=null; Lr.seg=[0,0,0,0]; if(below) drop(below,Fr); } } });
   if(lay.every(Lr=>Lr.f==='plate')){ const s=Fr.score+1500+puffs*300; lv++; build(Fr); Fr.score=s; Fr.snd(990,.25); Fr.msg('🎂 Every cake is plated! Level '+lv+': more dough is rising.'); return; }
   en.forEach(e=>{ if(e.dead>0){ e.dead-=dt; if(e.dead<=0){ e.f=0; e.x=Math.random()<0.5?W*0.08:W*0.92; e.climb=null; } return; } if(e.frz>0){ e.frz-=dt; return; }
    if(e.climb){ const l=e.climb; const yT=floorY(l.hi), yB=floorY(l.lo); e.cy+=e.cdir*e.sp*0.8*dt; if(e.cy<=yT){ e.f=l.hi; e.climb=null; } else if(e.cy>=yB){ e.f=l.lo; e.climb=null; } return; }
    let tx=P.x; if(e.f!==P.f||P.climb){ const tf=P.climb?(P.cy<floorY(e.f)?e.f-1:e.f+1):P.f; const goUp=tf<e.f; const cands=LD.filter(l=>goUp?l.lo===e.f:l.hi===e.f); if(cands.length){ if(!e.plan||!cands.includes(e.plan)||Math.random()<0.004) e.plan=Math.random()<0.2?pick(cands):cands.sort((a,b)=>Math.abs(a.x-e.x)-Math.abs(b.x-e.x))[0]; tx=e.plan.x; if(Math.abs(e.x-tx)<3){ e.climb=e.plan; e.x=tx; e.cy=floorY(e.f); e.cdir=goUp?-1:1; e.plan=null; return; } } }
    e.x+=Math.sign(tx-e.x)*Math.min(Math.abs(tx-e.x),e.sp*dt);
    const py=P.climb?P.cy:floorY(P.f); if(!e.climb&&Math.abs(e.x-P.x)<12&&Math.abs(floorY(e.f)-py)<14){ e.hit=true; } });
   if(en.some(e=>e.hit)){ en.forEach(e=>e.hit=false); lives--; Fr.snd(120,.3); if(lives<=0) return Fr.end('The dough got you.'); Fr.msg('The dough caught Pip! '+lives+' left.'); P={f:FN-1,x:W/2,climb:null,face:1,step:0}; en.forEach((e,k)=>{ e.f=0; e.x=k%2?W*0.08:W*0.92; e.climb=null; e.dead=1+k; }); }
   fx.forEach(e=>e.t+=dt*2); fx=fx.filter(e=>e.t<1); }
  function cake(g,x,y,w,type,seg){ const [c1,c2]=TY[type], h=7; for(let k=0;k<4;k++){ const dy=seg&&seg[k]?3:0; g.fillStyle=c1; g.fillRect(x-w/2+k*w/4+0.5,y-h+dy,w/4-1,h); g.fillStyle=c2; g.fillRect(x-w/2+k*w/4+0.5,y-h+dy,w/4-1,2); } if(type===0){ g.fillStyle='#ff1744'; g.beginPath(); g.arc(x,y-h-3,3,0,7); g.fill(); } }
  function paint(Fr){ const g=Fr.g,W=Fr.W,H=Fr.H; g.fillStyle='#2b1810'; g.fillRect(0,0,W,H); g.fillStyle='rgba(255,220,170,.05)'; for(let x=0;x<W;x+=24) g.fillRect(x,0,12,H);
   LD.forEach(l=>{ const y1=floorY(l.hi), y2=floorY(l.lo); g.strokeStyle='#e8c48a'; g.lineWidth=2; g.beginPath(); g.moveTo(l.x-5,y1); g.lineTo(l.x-5,y2); g.moveTo(l.x+5,y1); g.lineTo(l.x+5,y2); for(let y=y1+5;y<y2;y+=7){ g.moveTo(l.x-5,y); g.lineTo(l.x+5,y); } g.stroke(); });
   for(let f=0;f<FN;f++){ const y=floorY(f); g.fillStyle='#8a5a2b'; g.fillRect(0,y,W,5); g.fillStyle='#5c3a1a'; g.fillRect(0,y+5,W,2); }
   for(let c=0;c<C;c++){ g.fillStyle='#c9cbd6'; g.beginPath(); g.ellipse(colX(c),H-8,lw()/2+6,5,0,0,7); g.fill(); }
   lay.forEach(Lr=>{ const x=colX(Lr.c); if(Lr.f==='plate') cake(g,x,H-10-Lr.py*7,lw(),Lr.type); else if(Lr.fall) cake(g,x,Lr.fall.y,lw(),Lr.type); else cake(g,x,floorY(Lr.f),lw(),Lr.type,Lr.seg); });
   en.forEach(e=>{ if(e.dead>0) return; const y=e.climb?e.cy:floorY(e.f); const wob=Math.sin(Fr.t*8+e.x)*1.5; g.fillStyle=e.frz>0?'#e9f6ff':'#f2d7a6'; g.beginPath(); g.ellipse(e.x,y-8,9+wob,8-wob*0.5,0,0,7); g.fill(); g.fillStyle='#3a2410'; g.fillRect(e.x-4,y-11,2,3); g.fillRect(e.x+2,y-11,2,3); });
   const y=P.climb?P.cy:floorY(P.f), x=P.x, leg=Math.sin(P.step)*3; g.fillStyle='#fff'; g.fillRect(x-6,y-19,12,11); g.fillStyle='#ffd9b0'; g.fillRect(x-5,y-25,10,7); g.fillStyle='#fff'; g.fillRect(x-6,y-31,12,6); g.beginPath(); g.arc(x,y-31,6,Math.PI,0); g.fill(); g.fillStyle='#14163a'; g.fillRect(x+(P.face>0?1:-4),y-23,3,2); g.fillStyle='#3a6fd8'; g.fillRect(x-5,y-8,3,8+leg*0.3); g.fillRect(x+2,y-8,3,8-leg*0.3);
   if(cloud){ g.fillStyle='rgba(255,255,255,'+(0.8-cloud.t)+')'; [[0,0,12],[12,-4,9],[-10,-3,9]].forEach(([a,b,r])=>{ g.beginPath(); g.arc(cloud.x+a,floorY(cloud.f)-12+b,r+cloud.t*10,0,7); g.fill(); }); }
   fx.forEach(e=>boom(g,e.x,e.y,e.t,e.c)); }
  return {state:()=>({score:F.score,lives,level:lv,plated:lay.filter(l=>l.f==='plate').length,total:lay.length})}; });

 /* 3 · ORBIT GUARD: fly over the planet, shoot the abductor drones before they carry the colonists away; the radar shows the whole world */
 reg('vg_orbit','Orbit Guard','Guard the planet Kestra. Abductor drones drop from orbit to carry your colonists away; shoot them first (150). Shoot a drone that is carrying someone and catch the colonist before they fall (500), then fly low to set them down. A colonist carried to the top turns the drone into a hunter. The radar strip shows the whole planet. Keys: ← → fly and turn, ↑ ↓ climb and dive, Space fires, Enter sets off a nova bomb (clears the screen, three a game). Touch: hold where you want to fly; the guns fire on their own.',ctx=>{
  let S, cam=0, B=[], EB=[], E=[], Cn=[], fx=[], wave=1, lives=3, bombs=3, toSpawn=0, spT=0, fireT=0, WW=0, hills=[], stars=[]; const top=56;
  const F=frame(ctx,'vg_orbit',{ratio:0.62,maxW:880,title:'Orbit Guard',go:'Guard the colonists!',hint:'Press ▶ Start. ← → fly, ↑ ↓ height, Space fire, Enter nova bomb.',
   reset:F=>{ wave=1; lives=3; bombs=3; world(F); newWave(F); }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS, buttons:F=>[['💥 Nova bomb',()=>{ nova(F); }]],
   hud:F=>'Score '+F.score+' · ships '+lives+' · novas '+bombs+' · wave '+wave});
  const gnd=()=>F.H-20;
  const wrap=dx=>{ dx=((dx%WW)+WW)%WW; return dx>WW/2?dx-WW:dx; };
  const sx=x=>F.W/2+wrap(x-cam);
  function world(Fr){ WW=Fr.W*5; hills=[]; for(let x=0;x<=WW;x+=40) hills.push(Fr.H-22-Math.abs(Math.sin(x*0.004)*22+Math.sin(x*0.013)*10)); stars=[]; for(let k=0;k<60;k++) stars.push([Math.random()*WW,top+Math.random()*(Fr.H-top-60)]); S={x:Fr.W*0.5,y:Fr.H*0.45,vx:0,face:1,inv:2}; cam=S.x; Cn=[]; for(let k=0;k<8;k++) Cn.push({x:k*WW/8+rr(0,WW/16),y:Fr.H-20,st:'walk',vy:0,dir:Math.random()<0.5?1:-1,y0:0}); }
  function newWave(Fr){ toSpawn=5+wave*2; spT=1; E=[]; EB=[]; B=[]; if(!Cn.some(c=>c.st!=='gone')) Cn.forEach(c=>{ c.st='walk'; c.y=Fr.H-20; }); }
  function nova(Fr){ if(!Fr.running||Fr.over||bombs<=0) return; bombs--; let n=0; E.forEach(e=>{ if(Math.abs(wrap(e.x-cam))<Fr.W/2+20){ e.dead=true; n++; fx.push({x:e.x,y:e.y,t:0}); if(e.carry){ e.carry.st='fall'; e.carry.y0=e.carry.y; } } }); EB=[]; Fr.add(n*150); Fr.snd(90,.4); fx.push({x:cam,y:Fr.H/2,t:0,c:'#fff',big:1}); }
  function lose(Fr){ lives--; Fr.snd(110,.4); fx.push({x:S.x,y:S.y,t:0,c:'#ff4f6d'}); if(lives<=0) return Fr.end('Kestra has fallen.'); Fr.msg('Ship lost! '+lives+' left.'); S.inv=2.5; EB=[]; if(S.carry){ S.carry.st='fall'; S.carry.y0=S.y; S.carry=null; } }
  function step(Fr,dt){ const W=Fr.W,H=Fr.H; S.inv=Math.max(0,S.inv-dt);
   let lr=(R(Fr)?1:0)-(L(Fr)?1:0), ud=(D(Fr)?1:0)-(U(Fr)?1:0), fire=Fr.keys[' '];
   if(Fr.down){ const dx=Fr.px-sx(S.x), dy=Fr.py-S.y; lr=Math.abs(dx)>20?Math.sign(dx):0; ud=Math.abs(dy)>10?Math.sign(dy):0; fire=true; }
   if(lr) S.face=lr; S.vx+=lr*W*2.2*dt; S.vx*=Math.pow(0.35,dt); S.vx=cl(S.vx,-W*1.1,W*1.1); S.x=(S.x+S.vx*dt+WW)%WW; S.y=cl(S.y+ud*H*0.75*dt,top+8,gnd()-14);
   const tc=S.x+S.face*W*0.22+S.vx*0.15; cam=(cam+wrap(tc-cam)*Math.min(1,dt*3)+WW)%WW;
   fireT-=dt; if(fire&&fireT<=0){ fireT=0.16; B.push({x:S.x+S.face*14,y:S.y+1,d:S.face,l:0.5}); Fr.snd(880,.02); }
   if(edge(Fr,'Enter')) nova(Fr);
   B.forEach(b=>{ b.x=(b.x+b.d*W*2.4*dt+WW)%WW; b.l-=dt; }); B=B.filter(b=>b.l>0);
   spT-=dt; if(toSpawn>0&&spT<=0&&E.length<7){ spT=rr(1.2,2.6); toSpawn--; let x; do{ x=Math.random()*WW; }while(Math.abs(wrap(x-S.x))<W*0.6); E.push({x,y:top+6,st:'seek',t:Math.random()*9,tgt:null,sp:W*(0.1+0.01*wave)}); }
   const live=Cn.filter(c=>c.st==='walk');
   E.forEach(e=>{ e.t+=dt;
    if(e.st==='seek'){ if(!e.tgt||e.tgt.st!=='walk') e.tgt=live.length?live.sort((a,b)=>Math.abs(wrap(a.x-e.x))-Math.abs(wrap(b.x-e.x)))[0]:null; if(e.tgt){ const dx=wrap(e.tgt.x-e.x); e.x=(e.x+Math.sign(dx)*Math.min(Math.abs(dx),e.sp*dt)+WW)%WW; const ty=Math.abs(dx)<60?gnd()-26:H*0.4+Math.sin(e.t)*20; e.y+=Math.sign(ty-e.y)*Math.min(Math.abs(ty-e.y),H*0.2*dt); if(Math.abs(dx)<6&&e.y>=gnd()-30){ e.st='rise'; e.carry=e.tgt; e.tgt.st='carried'; } } else { e.st='hunt'; } }
    else if(e.st==='rise'){ e.y-=H*0.11*dt; e.carry.x=e.x; e.carry.y=e.y+14; if(e.y<=top+4){ e.carry.st='gone'; e.carry=null; e.st='hunt'; e.sp*=2.4; Fr.msg('A colonist was taken. A hunter is loose!'); Fr.snd(220,.2); } }
    else { const dx=wrap(S.x-e.x), dy=S.y-e.y; e.x=(e.x+Math.sign(dx)*Math.min(Math.abs(dx),e.sp*dt)+WW)%WW; e.y+=Math.sign(dy+Math.sin(e.t*5)*30)*H*0.3*dt; e.y=cl(e.y,top,gnd()-10); }
    const on=Math.abs(wrap(e.x-cam))<W/2; if(on&&Math.random()<dt*(0.35+0.05*wave)){ const dx=wrap(S.x-e.x), dy=S.y-e.y, m=Math.hypot(dx,dy)||1; EB.push({x:e.x,y:e.y,vx:dx/m*W*0.32,vy:dy/m*W*0.32,l:3}); }
    B.forEach(b=>{ if(!b.dead&&Math.abs(wrap(b.x-e.x))<11&&Math.abs(b.y-e.y)<10){ b.dead=true; e.dead=true; Fr.add(150); fx.push({x:e.x,y:e.y,t:0}); Fr.snd(260,.06); if(e.carry){ e.carry.st='fall'; e.carry.y0=e.carry.y; e.carry.vy=0; e.carry=null; } } });
    if(!e.dead&&S.inv<=0&&Math.abs(wrap(e.x-S.x))<14&&Math.abs(e.y-S.y)<11){ e.dead=true; lose(Fr); } });
   B=B.filter(b=>!b.dead); E=E.filter(e=>!e.dead);
   EB.forEach(b=>{ b.x=(b.x+b.vx*dt+WW)%WW; b.y+=b.vy*dt; b.l-=dt; if(S.inv<=0&&Math.abs(wrap(b.x-S.x))<9&&Math.abs(b.y-S.y)<7){ b.l=0; lose(Fr); } }); EB=EB.filter(b=>b.l>0&&b.y>top&&b.y<H);
   Cn.forEach(c=>{ if(c.st==='walk'){ c.x=(c.x+c.dir*8*dt+WW)%WW; if(Math.random()<dt*0.2) c.dir*=-1; }
    else if(c.st==='fall'){ c.vy=(c.vy||0)+260*dt; c.y+=c.vy*dt; if(Math.abs(wrap(c.x-S.x))<14&&Math.abs(c.y-S.y)<16&&!S.carry){ c.st='saved'; S.carry=c; Fr.add(500); Fr.snd(990,.08); Fr.msg('Caught! Fly low to set them down.'); }
     else if(c.y>=gnd()){ c.y=gnd(); if(c.y-c.y0>H*0.45){ c.st='gone'; Fr.msg('A colonist fell too far.'); } else { c.st='walk'; Fr.add(250); } } }
    else if(c.st==='saved'){ c.x=S.x; c.y=S.y+12; if(S.y>gnd()-30){ c.st='walk'; c.y=gnd(); S.carry=null; Fr.add(500); Fr.snd(990,.12); } } });
   fx.forEach(e=>e.t+=dt*1.6); fx=fx.filter(e=>e.t<1);
   if(toSpawn<=0&&!E.length){ const alive=Cn.filter(c=>c.st!=='gone').length; Fr.add(alive*100); wave++; bombs=Math.min(5,bombs+1); Fr.msg('Wave cleared! '+alive+' colonists safe. Wave '+wave+' is coming.'); Fr.snd(990,.25); newWave(Fr); } }
  function paint(Fr){ const g=Fr.g,W=Fr.W,H=Fr.H; g.fillStyle='#03030f'; g.fillRect(0,0,W,H);
   g.fillStyle='rgba(111,232,255,.07)'; g.fillRect(0,25,W,28); g.strokeStyle='#6fe8ff'; g.lineWidth=1; g.strokeRect(6.5,26.5,W-13,25);
   const rx=x=>8+((x%WW+WW)%WW)/WW*(W-16), ry=y=>27+(y-top)/(H-top)*23;
   g.strokeStyle='#ffe94a'; g.strokeRect(rx(cam-W/2),27,W/WW*(W-16),23);
   Cn.forEach(c=>{ if(c.st==='gone') return; g.fillStyle='#7cff8a'; g.fillRect(rx(c.x),ry(c.y)-1,2,2); }); E.forEach(e=>{ g.fillStyle=e.st==='hunt'?'#ff7ad9':'#ff4f6d'; g.fillRect(rx(e.x)-1,ry(e.y)-1,3,3); }); g.fillStyle='#fff'; g.fillRect(rx(S.x)-1.5,ry(S.y)-1.5,4,3);
   g.save(); g.beginPath(); g.rect(0,top,W,H-top); g.clip();
   stars.forEach(([x,y])=>{ const X=W/2+wrap(x-cam*0.5); if(X>0&&X<W){ g.fillStyle='rgba(255,255,255,.5)'; g.fillRect(X,y,1.5,1.5); } });
   g.strokeStyle='#c38bff'; g.lineWidth=2; g.beginPath(); for(let X=-40;X<=W+40;X+=8){ const wx=((cam-W/2+X)%WW+WW)%WW; const i=Math.floor(wx/40), f=(wx%40)/40; const y=lerp(hills[i],hills[(i+1)%hills.length],f); X===-40?g.moveTo(X,y):g.lineTo(X,y); } g.stroke();
   Cn.forEach(c=>{ if(c.st==='gone') return; const X=sx(c.x); if(X<-10||X>W+10) return; g.fillStyle='#7cff8a'; g.fillRect(X-2,c.y-8,4,8); g.beginPath(); g.arc(X,c.y-10,2.5,0,7); g.fill(); });
   E.forEach(e=>{ const X=sx(e.x); if(X<-20||X>W+20) return; if(e.st==='hunt'){ g.fillStyle='#ff7ad9'; g.beginPath(); g.moveTo(X,e.y-8); g.lineTo(X+9,e.y); g.lineTo(X,e.y+8); g.lineTo(X-9,e.y); g.fill(); } else { g.fillStyle='#ff4f6d'; g.beginPath(); g.ellipse(X,e.y,10,6,0,0,7); g.fill(); g.fillStyle='#ffe94a'; g.fillRect(X-6,e.y-1,3,2); g.fillRect(X+3,e.y-1,3,2); g.strokeStyle='#ff4f6d'; g.beginPath(); g.moveTo(X-6,e.y+5); g.lineTo(X-9,e.y+11); g.moveTo(X+6,e.y+5); g.lineTo(X+9,e.y+11); g.stroke(); } });
   B.forEach(b=>{ const X=sx(b.x); g.strokeStyle='#ffe94a'; g.lineWidth=2; g.beginPath(); g.moveTo(X,b.y); g.lineTo(X-b.d*18,b.y); g.stroke(); });
   EB.forEach(b=>{ g.fillStyle='#ff9a3c'; g.beginPath(); g.arc(sx(b.x),b.y,2.5,0,7); g.fill(); });
   if(!(S.inv>0&&Math.sin(Fr.t*30)>0)){ const X=sx(S.x), y=S.y, f=S.face; g.fillStyle='#e9f1ff'; g.beginPath(); g.moveTo(X+f*15,y); g.lineTo(X-f*11,y-6); g.lineTo(X-f*7,y); g.lineTo(X-f*11,y+6); g.closePath(); g.fill(); g.fillStyle='#6fe8ff'; g.fillRect(X-f*2-2,y-3,5,3); if(Math.abs(S.vx)>20){ g.fillStyle='#ff9a3c'; g.beginPath(); g.moveTo(X-f*9,y-3); g.lineTo(X-f*(16+Math.random()*6),y); g.lineTo(X-f*9,y+3); g.fill(); } }
   fx.forEach(e=>{ if(e.big){ g.fillStyle='rgba(255,255,255,'+Math.max(0,0.6-e.t)+')'; g.fillRect(0,top,W,H); } else boom(g,sx(e.x),e.y,e.t,e.c); });
   g.restore(); }
  return {state:()=>({score:F.score,lives,wave,colonists:Cn.filter(c=>c.st!=='gone').length,enemies:E.length})}; });

 /* 4 · VORTEX RIM: ride the rim of a neon tube and blast everything climbing up the lanes */
 reg('vg_vortex','Vortex Rim','You ride the rim of a neon tube. Shapes climb up the lanes toward you: blast them before they reach the rim. Flippers (red bow ties) hop lanes and hunt along the rim; crawlers (green) climb straight; both shoot. Clear each tube to warp to a new shape. Enter fires the vortex zapper (clears the tube, once a tube). Keys: ← → move around the rim, Space fires. Touch: tap anywhere around the tube to jump to that lane and fire; hold to keep firing.',ctx=>{
  const NL=16; let V=[], v=[], pl=0, B=[], EB=[], E=[], fx=[], lv=1, lives=3, kills=0, need=0, zap=1, warp=0, spT=0, mvT=0, fireT=0, cx=0, cy=0;
  const SH=[t=>1,t=>1/Math.max(Math.abs(Math.cos(t)),Math.abs(Math.sin(t)))*0.82,t=>1+0.18*Math.cos(4*t),t=>1+0.22*Math.cos(3*t),t=>0.9+0.12*Math.cos(6*t),t=>1+0.3*Math.cos(2*t)];
  const COLS=['#3d7bff','#c38bff','#7cff8a','#ff9a3c','#6fe8ff','#ff7ad9'];
  const F=frame(ctx,'vg_vortex',{ratio:0.92,maxW:640,title:'Vortex Rim',go:'Hold the rim!',hint:'Press ▶ Start. ← → move, Space fire, Enter zapper.',
   reset:F=>{ lv=1; lives=3; tube(F); }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS, buttons:F=>[['⚡ Zapper',()=>{ zapIt(F); }]],
   pointer:(F,t,x,y)=>{ if(t==='down'||t==='move'){ const a=Math.atan2(y-cy,x-cx); let best=0,bd=9; for(let i=0;i<NL;i++){ const m=mid(i,1); const d=Math.abs(Math.atan2(m[1]-cy,m[0]-cx)-a); const dd=Math.min(d,Math.PI*2-d); if(dd<bd){ bd=dd; best=i; } } pl=best; } },
   hud:F=>'Score '+F.score+' · lives '+lives+' · tube '+lv+' · zapper '+(zap?'ready':'used')});
  function tube(Fr){ cx=Fr.W/2; cy=Fr.H*0.55; const Rr=Math.min(Fr.W*0.46,Fr.H*0.44), sh=SH[(lv-1)%SH.length]; V=[]; v=[]; for(let k=0;k<NL;k++){ const t=-Math.PI/2+2*Math.PI*k/NL, r=sh(t)*Rr; V.push([cx+Math.cos(t)*r,cy+Math.sin(t)*r]); v.push([cx+Math.cos(t)*r*0.13,cy+Math.sin(t)*r*0.13-Fr.H*0.03]); } B=[]; EB=[]; E=[]; kills=0; need=10+lv*4; zap=1; spT=1.2; }
  const f=d=>d*d;
  function pt(i,d,t){ const a=i%NL, b=(i+1)%NL, A=[lerp(v[a][0],V[a][0],f(d)),lerp(v[a][1],V[a][1],f(d))], Bq=[lerp(v[b][0],V[b][0],f(d)),lerp(v[b][1],V[b][1],f(d))]; return [lerp(A[0],Bq[0],t),lerp(A[1],Bq[1],t)]; }
  const mid=(i,d)=>pt(i,d,0.5);
  function zapIt(Fr){ if(!Fr.running||Fr.over||!zap) return; zap=0; E.forEach(e=>{ fx.push({p:mid(e.l,e.d),t:0}); kills++; }); Fr.add(E.length*100); E=[]; EB=[]; Fr.snd(80,.4); fx.push({flash:1,t:0}); }
  function die(Fr){ lives--; Fr.snd(100,.4); fx.push({p:mid(pl,1),t:0,c:'#ffe94a'}); if(lives<=0) return Fr.end('The vortex took you.'); Fr.msg('Hit! '+lives+' left.'); E=E.filter(e=>e.d<0.6); EB=[]; }
  function step(Fr,dt){ if(warp>0){ warp-=dt; if(warp<=0){ lv++; tube(Fr); Fr.msg('Tube '+lv+'. Hold the rim.'); } return; }
   mvT-=dt; const lr=(R(Fr)?1:0)-(L(Fr)?1:0); if(lr&&mvT<=0){ pl=(pl+lr+NL)%NL; mvT=0.085; } if(!lr) mvT=0;
   fireT-=dt; if((Fr.keys[' ']||Fr.down)&&fireT<=0&&B.length<8){ fireT=0.12; B.push({l:pl,d:1}); Fr.snd(900,.02); }
   if(edge(Fr,'Enter')) zapIt(Fr);
   B.forEach(b=>b.d-=2.4*dt); B=B.filter(b=>b.d>0);
   spT-=dt; if(spT<=0&&kills+E.length<need){ spT=Math.max(0.45,1.6-lv*0.1)*rr(0.7,1.3); E.push({l:Math.floor(Math.random()*NL),d:0.02,ty:Math.random()<0.55?'flip':'crawl',sp:rr(0.09,0.14)*(1+lv*0.08),fT:rr(1,2),mT:0}); }
   E.forEach(e=>{ if(e.d<1){ e.d=Math.min(1,e.d+e.sp*dt); if(e.ty==='flip'){ e.fT-=dt; if(e.fT<=0){ e.fT=rr(0.9,1.8); e.l=(e.l+(Math.random()<0.5?1:-1)+NL)%NL; } } if(Math.random()<dt*0.18*(1+lv*0.1)) EB.push({l:e.l,d:e.d}); }
    else { e.mT-=dt; if(e.mT<=0){ e.mT=e.ty==='flip'?0.45:0.8; const dif=((pl-e.l)+NL)%NL; if(dif) e.l=(e.l+(dif<=NL/2?1:-1)+NL)%NL; } }
    B.forEach(b=>{ if(!b.dead&&!e.dead&&b.l===e.l&&Math.abs(b.d-e.d)<0.07){ b.dead=e.dead=true; kills++; Fr.add(e.ty==='flip'?150:100); fx.push({p:mid(e.l,e.d),t:0}); Fr.snd(300,.05); } });
    if(!e.dead&&e.d>=1&&e.l===pl){ e.dead=true; e.hitP=true; } });
   if(E.some(e=>e.hitP)){ E=E.filter(e=>!e.hitP); die(Fr); if(Fr.over) return; }
   E=E.filter(e=>!e.dead); B=B.filter(b=>!b.dead);
   EB.forEach(b=>{ b.d+=0.5*dt; B.forEach(x=>{ if(!x.dead&&x.l===b.l&&Math.abs(x.d-b.d)<0.06){ x.dead=b.dead=true; Fr.add(20); } }); if(b.d>=1){ b.dead=true; if(b.l===pl) b.hit=true; } });
   if(EB.some(b=>b.hit)){ EB=[]; die(Fr); if(Fr.over) return; } EB=EB.filter(b=>!b.dead); B=B.filter(b=>!b.dead);
   fx.forEach(e=>e.t+=dt*1.8); fx=fx.filter(e=>e.t<1);
   if(kills>=need&&!E.length){ Fr.add(1000+lives*200); warp=1.2; Fr.snd(990,.3); Fr.msg('Tube clear! Warping…'); } }
  function paint(Fr){ const g=Fr.g,W=Fr.W,H=Fr.H; g.fillStyle='#000'; g.fillRect(0,0,W,H); const col=COLS[(lv-1)%COLS.length];
   const z=warp>0?1+(1.2-warp)*1.5:1; g.save(); if(warp>0){ g.translate(cx,cy); g.scale(z,z); g.translate(-cx,-cy); g.globalAlpha=Math.max(0.1,warp/1.2); }
   g.strokeStyle=col; g.lineWidth=1.3; g.beginPath(); for(let k=0;k<NL;k++){ g.moveTo(v[k][0],v[k][1]); g.lineTo(V[k][0],V[k][1]); } g.moveTo(V[0][0],V[0][1]); V.forEach(p=>g.lineTo(p[0],p[1])); g.lineTo(V[0][0],V[0][1]); g.moveTo(v[0][0],v[0][1]); v.forEach(p=>g.lineTo(p[0],p[1])); g.lineTo(v[0][0],v[0][1]); g.stroke();
   const a=pt(pl,1,0), b=pt(pl,1,1); g.strokeStyle='#ffe94a'; g.lineWidth=2.5; g.beginPath(); g.moveTo(a[0],a[1]); g.lineTo(V[(pl+1)%NL][0]*0+(a[0]+b[0])/2+(cx-(a[0]+b[0])/2)*-0.08,(a[1]+b[1])/2+(cy-(a[1]+b[1])/2)*-0.08); g.lineTo(b[0],b[1]); g.stroke(); const pa=pt(pl,1,0), pb=pt(pl,1,1); g.strokeStyle='rgba(255,233,74,.35)'; g.lineWidth=4; g.beginPath(); g.moveTo(pa[0],pa[1]); g.lineTo(pb[0],pb[1]); g.stroke();
   E.forEach(e=>{ const p0=pt(e.l,e.d,0.15), p1=pt(e.l,e.d,0.85), m=mid(e.l,e.d), s=0.4+e.d; if(e.ty==='flip'){ g.strokeStyle='#ff4f6d'; g.lineWidth=2; g.beginPath(); g.moveTo(p0[0],p0[1]-5*s); g.lineTo(p1[0],p1[1]+5*s); g.lineTo(p1[0],p1[1]-5*s); g.lineTo(p0[0],p0[1]+5*s); g.closePath(); g.stroke(); } else { g.strokeStyle='#7cff8a'; g.lineWidth=2; g.beginPath(); g.moveTo(m[0],m[1]-6*s); g.lineTo(m[0]+6*s,m[1]); g.lineTo(m[0],m[1]+6*s); g.lineTo(m[0]-6*s,m[1]); g.closePath(); g.stroke(); } });
   B.forEach(b=>{ const p=mid(b.l,b.d); g.fillStyle='#ffe94a'; g.beginPath(); g.arc(p[0],p[1],1.5+2*b.d,0,7); g.fill(); });
   EB.forEach(b=>{ const p=mid(b.l,b.d); g.fillStyle='#ff9a3c'; g.fillRect(p[0]-2,p[1]-2,4,4); });
   fx.forEach(e=>{ if(e.flash){ g.fillStyle='rgba(255,255,255,'+Math.max(0,0.5-e.t)+')'; g.fillRect(0,0,W,H); } else boom(g,e.p[0],e.p[1],e.t,e.c||'#ff7ad9'); });
   g.restore(); }
  return {state:()=>({score:F.score,lives,tube:lv,kills,need,lane:pl})}; });

 /* 5 · NEON ARENA: move with one hand, shoot with the other; save the Pips from the robot horde */
 reg('vg_arena','Neon Arena','Twin-stick action in a neon arena. Move with W A S D, shoot in eight directions with the arrow keys (hold two arrows for diagonals). Save the Pips (pink) by touching them: 1,000, then 2,000, up to 5,000. Grunts chase you, Sparks shoot, and Bulwarks (big green) cannot be destroyed: your shots only push them back. Clear every Grunt and Spark to win the wave. Touch or mouse: hold where you want to go; the guns aim at the nearest robot on their own. On a phone the 🎮 controller gives you two sticks.',ctx=>{
  let P, B=[], EB=[], E=[], fr=[], fx=[], wave=1, lives=3, save=0, fireT=0;
  const F=frame(ctx,'vg_arena',{ratio:0.8,maxW:720,title:'Neon Arena',go:'Save the Pips!',hint:'Press ▶ Start. W A S D move, arrows shoot.',
   reset:F=>{ wave=1; lives=3; newWave(F); }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS, hud:F=>'Score '+F.score+' · lives '+lives+' · wave '+wave});
  function spot(Fr,minD){ let x,y,n=0; do{ x=rr(16,Fr.W-16); y=rr(36,Fr.H-16); }while(Math.hypot(x-Fr.W/2,y-Fr.H/2)<minD&&++n<50); return [x,y]; }
  function newWave(Fr){ P={x:Fr.W/2,y:Fr.H/2,inv:1.5,fx:1,fy:0}; B=[]; EB=[]; E=[]; fr=[]; save=0; const s=Math.min(Fr.W,Fr.H);
   for(let k=0;k<8+wave*3;k++){ const [x,y]=spot(Fr,s*0.3); E.push({ty:'grunt',x,y,sp:s*(0.08+0.012*wave)*rr(0.8,1.2),hp:1}); }
   for(let k=0;k<Math.floor(wave/2);k++){ const [x,y]=spot(Fr,s*0.35); E.push({ty:'bulk',x,y,sp:s*0.05,hp:1e9,vx:0,vy:0}); }
   for(let k=0;k<(wave>=2?1+Math.floor(wave/3):0);k++){ const [x,y]=spot(Fr,s*0.35); E.push({ty:'spark',x,y,sp:s*0.12,hp:1,a:Math.random()*7}); }
   for(let k=0;k<4;k++){ const [x,y]=spot(Fr,s*0.15); fr.push({x,y,a:Math.random()*7}); } }
  function hurt(Fr){ lives--; Fr.snd(110,.4); fx.push({x:P.x,y:P.y,t:0,c:'#6fe8ff'}); if(lives<=0) return Fr.end('The horde took the arena.'); Fr.msg('Hit! '+lives+' left.'); P.inv=2; EB=[]; E.forEach(e=>{ if(Math.hypot(e.x-P.x,e.y-P.y)<Fr.W*0.25&&e.ty!=='bulk'){ const a=Math.atan2(e.y-P.y,e.x-P.x); e.x=cl(P.x+Math.cos(a)*Fr.W*0.3,10,Fr.W-10); e.y=cl(P.y+Math.sin(a)*Fr.W*0.3,30,Fr.H-10); } }); }
  function step(Fr,dt){ const W=Fr.W,H=Fr.H, s=Math.min(W,H); P.inv=Math.max(0,P.inv-dt);
   let mx=(Fr.keys.d?1:0)-(Fr.keys.a?1:0), my=(Fr.keys.s?1:0)-(Fr.keys.w?1:0), fx_=(Fr.keys.ArrowRight?1:0)-(Fr.keys.ArrowLeft?1:0), fy=(Fr.keys.ArrowDown?1:0)-(Fr.keys.ArrowUp?1:0);
   if(Fr.down){ const dx=Fr.px-P.x, dy=Fr.py-P.y, m=Math.hypot(dx,dy); if(m>8){ mx=dx/m; my=dy/m; } const t=E.filter(e=>e.ty!=='bulk').sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0]; if(t){ const a=Math.atan2(t.y-P.y,t.x-P.x); fx_=Math.cos(a); fy=Math.sin(a); } }
   const mm=Math.hypot(mx,my); if(mm){ P.x=cl(P.x+mx/mm*s*0.32*dt,10,W-10); P.y=cl(P.y+my/mm*s*0.32*dt,32,H-10); }
   fireT-=dt; const fm=Math.hypot(fx_,fy); if(fm&&fireT<=0){ fireT=0.11; P.fx=fx_/fm; P.fy=fy/fm; B.push({x:P.x,y:P.y,vx:P.fx*s*1.3,vy:P.fy*s*1.3}); Fr.snd(1000,.015); }
   B.forEach(b=>{ b.x+=b.vx*dt; b.y+=b.vy*dt; }); B=B.filter(b=>b.x>0&&b.x<W&&b.y>26&&b.y<H);
   E.forEach(e=>{ const dx=P.x-e.x, dy=P.y-e.y, m=Math.hypot(dx,dy)||1;
    if(e.ty==='grunt'){ e.x+=dx/m*e.sp*dt; e.y+=dy/m*e.sp*dt; }
    else if(e.ty==='spark'){ e.a+=rr(-3,3)*dt; e.x=cl(e.x+Math.cos(e.a)*e.sp*dt,10,W-10); e.y=cl(e.y+Math.sin(e.a)*e.sp*dt,30,H-10); if(e.x<=10||e.x>=W-10||e.y<=30||e.y>=H-10) e.a+=Math.PI; if(Math.random()<dt*0.8) EB.push({x:e.x,y:e.y,vx:dx/m*s*0.45,vy:dy/m*s*0.45,l:3}); }
    else { const tgt=fr[0]||P; const ex=tgt.x-e.x, ey=tgt.y-e.y, em=Math.hypot(ex,ey)||1; e.vx=(e.vx||0)*Math.pow(0.1,dt); e.vy=(e.vy||0)*Math.pow(0.1,dt); e.x=cl(e.x+(ex/em*e.sp+e.vx)*dt,14,W-14); e.y=cl(e.y+(ey/em*e.sp+e.vy)*dt,34,H-14); fr.forEach(f=>{ if(Math.hypot(f.x-e.x,f.y-e.y)<16){ f.gone=true; fx.push({x:f.x,y:f.y,t:0,c:'#ff7ad9'}); } }); }
    B.forEach(b=>{ if(!b.dead&&Math.hypot(b.x-e.x,b.y-e.y)<(e.ty==='bulk'?14:10)){ b.dead=true; if(e.ty==='bulk'){ e.vx+=b.vx*0.25; e.vy+=b.vy*0.25; } else { e.dead=true; Fr.add(e.ty==='spark'?250:100); fx.push({x:e.x,y:e.y,t:0,c:e.ty==='spark'?'#ffe94a':'#ff4f6d'}); Fr.snd(240,.04); } } });
    if(!e.dead&&P.inv<=0&&Math.hypot(e.x-P.x,e.y-P.y)<(e.ty==='bulk'?16:11)) e.hitP=true; });
   if(E.some(e=>e.hitP)){ E.forEach(e=>e.hitP=false); hurt(Fr); if(Fr.over) return; }
   E=E.filter(e=>!e.dead); B=B.filter(b=>!b.dead); fr=fr.filter(f=>!f.gone);
   EB.forEach(b=>{ b.x+=b.vx*dt; b.y+=b.vy*dt; b.l-=dt; if(P.inv<=0&&Math.hypot(b.x-P.x,b.y-P.y)<7){ b.l=0; b.hit=true; } }); if(EB.some(b=>b.hit)){ hurt(Fr); if(Fr.over) return; } EB=EB.filter(b=>b.l>0&&!b.hit);
   fr.forEach(f=>{ f.a+=rr(-2,2)*dt; f.x=cl(f.x+Math.cos(f.a)*s*0.05*dt,12,W-12); f.y=cl(f.y+Math.sin(f.a)*s*0.05*dt,32,H-12); if(Math.hypot(f.x-P.x,f.y-P.y)<14){ f.gone=true; save=Math.min(5,save+1); Fr.add(save*1000); Fr.snd(990,.1); Fr.msg('Pip saved! +'+(save*1000)); } }); fr=fr.filter(f=>!f.gone);
   fx.forEach(e=>e.t+=dt*2); fx=fx.filter(e=>e.t<1);
   if(!E.some(e=>e.ty!=='bulk')){ wave++; Fr.add(500); Fr.snd(990,.25); Fr.msg('Wave clear! Wave '+wave+'.'); newWave(Fr); } }
  function paint(Fr){ const g=Fr.g,W=Fr.W,H=Fr.H; g.fillStyle='#07071a'; g.fillRect(0,0,W,H); g.strokeStyle='rgba(195,139,255,.12)'; g.lineWidth=1; for(let x=0;x<W;x+=24){ g.beginPath(); g.moveTo(x,26); g.lineTo(x,H); g.stroke(); } for(let y=26;y<H;y+=24){ g.beginPath(); g.moveTo(0,y); g.lineTo(W,y); g.stroke(); } g.strokeStyle='#c38bff'; g.lineWidth=2; g.strokeRect(2,27,W-4,H-29);
   fr.forEach(f=>{ g.fillStyle='#ff7ad9'; g.beginPath(); g.arc(f.x,f.y-3,4,0,7); g.fill(); g.fillRect(f.x-3,f.y,6,6); });
   E.forEach(e=>{ if(e.ty==='grunt'){ g.fillStyle='#ff4f6d'; g.fillRect(e.x-6,e.y-6,12,12); g.fillStyle='#ffe94a'; g.fillRect(e.x-4,e.y-3,3,3); g.fillRect(e.x+1,e.y-3,3,3); } else if(e.ty==='bulk'){ g.fillStyle='#2fbf5a'; g.fillRect(e.x-11,e.y-11,22,22); g.fillStyle='#14163a'; g.fillRect(e.x-7,e.y-5,14,3); } else { g.strokeStyle='#ffe94a'; g.lineWidth=2; g.beginPath(); for(let k=0;k<4;k++){ const a=e.a+k*Math.PI/4*2; g.moveTo(e.x-Math.cos(a)*8,e.y-Math.sin(a)*8); g.lineTo(e.x+Math.cos(a)*8,e.y+Math.sin(a)*8); } g.stroke(); } });
   B.forEach(b=>{ g.strokeStyle='#6fe8ff'; g.lineWidth=2; g.beginPath(); g.moveTo(b.x,b.y); g.lineTo(b.x-b.vx*0.012,b.y-b.vy*0.012); g.stroke(); });
   EB.forEach(b=>{ g.fillStyle='#ff9a3c'; g.beginPath(); g.arc(b.x,b.y,2.5,0,7); g.fill(); });
   if(!(P.inv>0&&Math.sin(Fr.t*30)>0)){ g.fillStyle='#e9f1ff'; g.beginPath(); g.arc(P.x,P.y,7,0,7); g.fill(); g.strokeStyle='#6fe8ff'; g.lineWidth=2; g.beginPath(); g.moveTo(P.x,P.y); g.lineTo(P.x+P.fx*11,P.y+P.fy*11); g.stroke(); }
   fx.forEach(e=>boom(g,e.x,e.y,e.t,e.c)); }
  return {state:()=>({score:F.score,lives,wave,robots:E.length,pips:fr.length})}; });

 /* 6 · NIGHT HIGHWAY: a neon road race through the night; pass the traffic, beat the clock, reach the checkpoints */
 reg('vg_road','Night Highway','Race down a neon highway at night. Hold ↑ (or Space) for gas, ↓ to brake, ← → to steer. Stay on the road: the grass slows you down. Pass cars (50 each) without hitting them, and reach each checkpoint before the clock runs out to win more time. Touch: hold the screen for gas and steer by holding left or right of the middle.',ctx=>{
  const SEG=200, RW=2000, DD=110, LANES=3, CAMH=1000, DEPTH=1/Math.tan(50*Math.PI/180); let segs=[], LEN=0, pos=0, px=0, spd=0, time=60, cars=[], dist=0, cp=0, passed=0, sky=0, MAX=SEG*60;
  const F=frame(ctx,'vg_road',{ratio:0.62,maxW:880,title:'Night Highway',go:'Floor it!',hint:'Press ▶ Start. ↑ or Space gas, ↓ brake, ← → steer.',
   reset:F=>{ build(); pos=0; px=0; spd=0; time=60; dist=0; cp=1; passed=0; }, update:(F,dt)=>step(F,dt), draw:F=>paint(F), key:KS,
   hud:F=>'Score '+F.score+' · '+Math.round(spd/MAX*240)+' km/h · time '+Math.ceil(time)+' s'});
  function add(n,curve,hill){ const y0=segs.length?segs[segs.length-1].p2.y:0; for(let k=0;k<n;k++){ const i=segs.length, e=(1-Math.cos(Math.PI*k/n))/2, e2=(1-Math.cos(Math.PI*(k+1)/n))/2; segs.push({i,curve:curve*Math.sin(Math.PI*(k+0.5)/n),p1:{y:y0+hill*e,z:i*SEG},p2:{y:y0+hill*e2,z:(i+1)*SEG},cars:[]}); } }
  function build(){ segs=[]; add(40,0,0); add(80,3,0); add(60,0,1500); add(80,-4,0); add(60,0,-1500); add(100,2,800); add(60,-2,-800); add(80,5,0); add(50,0,0); add(90,-3,1200); add(90,0,-1200); add(70,4,0); add(60,-5,0); add(60,0,0);
   const last=segs[segs.length-1].p2.y; if(Math.abs(last)>1) add(60,0,-last); LEN=segs.length*SEG; cars=[]; const cols=['#ff4f6d','#6fe8ff','#7cff8a','#ffe94a','#c38bff','#ff9a3c','#e9f1ff'];
   for(let k=0;k<26;k++){ cars.push({off:pick([-0.66,0,0.66])+rr(-0.1,0.1),z:rr(3000,LEN-1000),sp:MAX*rr(0.18,0.45),col:pick(cols),passed:false}); } }
  const seg=z=>segs[Math.floor(((z%LEN)+LEN)%LEN/SEG)%segs.length];
  function proj(p,cx,cy,cz,W,H){ const z=p.z-cz; const s=DEPTH/z; return {x:Math.round(W/2+s*(-cx)*W/2),y:Math.round(H/2-s*(p.y-cy)*H/2),w:Math.round(s*RW*W/2),s,z}; }
  function step(Fr,dt){ const W=Fr.W; let gas=Fr.keys.ArrowUp||Fr.keys.w||Fr.keys[' '], brk=Fr.keys.ArrowDown||Fr.keys.s, st=(R(Fr)?1:0)-(L(Fr)?1:0);
   if(Fr.down){ gas=true; const d=Fr.px-W/2; st=Math.abs(d)>W*0.08?Math.sign(d):0; }
   const ps=seg(pos+CAMH*DEPTH*0+400), pct=spd/MAX; px+=st*dt*2*pct; px-=dt*2*pct*ps.curve*0.32; sky-=ps.curve*pct*dt*20;
   if(gas) spd+=MAX/5*dt; else if(brk) spd-=MAX*dt; else spd-=MAX/5*dt;
   if((px<-1||px>1)&&spd>MAX/4) spd-=MAX/2*dt;
   px=cl(px,-2.2,2.2); spd=cl(spd,0,MAX);
   const pz=pos+400; cars.forEach(c=>{ c.z=(c.z+c.sp*dt)%LEN; const rel=((c.z-pz)%LEN+LEN)%LEN; if(rel<SEG*0.9&&Math.abs(c.off-px)<0.36&&spd>c.sp){ spd=c.sp*0.6; Fr.snd(120,.15); Fr.msg('Bump! Watch the traffic.'); }
    if(rel>LEN-SEG*2&&rel<LEN-10&&!c.passed){ c.passed=true; passed++; Fr.add(50); } if(rel>SEG*5&&rel<LEN/2) c.passed=false; });
   const ov=pos+spd*dt; if(ov>=LEN){ Fr.add(500); Fr.msg('Lap complete! +500'); } pos=((ov%LEN)+LEN)%LEN; dist+=spd*dt; Fr.score=Math.floor(dist/1000)+passed*50+(Fr.lapB||0);
   if(dist>=cp*LEN*0.5){ cp++; time+=25; Fr.snd(990,.2); Fr.msg('✔ Checkpoint! +25 seconds.'); }
   time-=dt; if(time<=0){ time=0; Fr.end('Time is up. You drove '+(dist/100000).toFixed(1)+' km.'); } }
  function paint(Fr){ const g=Fr.g,W=Fr.W,H=Fr.H; const sk=g.createLinearGradient(0,0,0,H*0.6); sk.addColorStop(0,'#05031a'); sk.addColorStop(1,'#2a0f4a'); g.fillStyle=sk; g.fillRect(0,0,W,H);
   for(let k=0;k<40;k++){ g.fillStyle='rgba(255,255,255,.6)'; g.fillRect(((k*137+sky*0.3)%W+W)%W,(k*61)%(H*0.4)+24,1.5,1.5); }
   g.fillStyle='#fff6cc'; g.beginPath(); g.arc(((W*0.8+sky*0.2)%W+W)%W,H*0.18,12,0,7); g.fill();
   g.fillStyle='#120826'; for(let k=0;k<26;k++){ const bw=W/14, x=((k*bw*0.9+sky)%(W+bw)+W+bw)%(W+bw)-bw, bh=H*(0.08+((k*29)%7)/40); g.fillRect(x,H*0.5-bh,bw*0.8,bh+2); g.fillStyle='rgba(255,233,74,.5)'; for(let wy=H*0.5-bh+4;wy<H*0.5-2;wy+=6) if((k+wy)%3<1.5) g.fillRect(x+3,wy,2,2); g.fillStyle='#120826'; }
   const base=seg(pos), bp=(pos%SEG)/SEG, cz=pos, cyy=CAMH+lerp(base.p1.y,base.p2.y,bp); let x=0, dx=-(base.curve*bp); const list=[];
   for(let n=0;n<DD;n++){ const s=segs[(base.i+n)%segs.length], loop=s.i<base.i?LEN:0; const p1={y:s.p1.y,z:s.p1.z+loop}, p2={y:s.p2.y,z:s.p2.z+loop};
    const a=proj(p1,px*RW-x,cyy,cz,W,H), b=proj(p2,px*RW-x-dx,cyy,cz,W,H); x+=dx; dx+=s.curve; if(a.z<=DEPTH||b.y>=a.y) { list.push(null); continue; } list.push({s,a,b,n}); }
   for(let k=list.length-1;k>=0;k--){ const it=list[k]; if(!it) continue; const {s,a,b}=it, alt=Math.floor(s.i/3)%2;
    g.fillStyle=alt?'#0b2a1a':'#0e3320'; g.fillRect(0,b.y,W,a.y-b.y+1);
    const quad=(x1,y1,w1,x2,y2,w2,c)=>{ g.fillStyle=c; g.beginPath(); g.moveTo(x1-w1,y1); g.lineTo(x2-w2,y2); g.lineTo(x2+w2,y2); g.lineTo(x1+w1,y1); g.closePath(); g.fill(); };
    const r1=a.w/6, r2=b.w/6; quad(a.x,a.y,a.w+r1,b.x,b.y,b.w+r2,alt?'#ff2bd6':'#00e5ff'); quad(a.x,a.y,a.w,b.x,b.y,b.w,alt?'#2a2a3a':'#30303f');
    if(alt){ for(let ln=1;ln<LANES;ln++){ const t=-1+2*ln/LANES; quad(a.x+a.w*t,a.y,a.w/60,b.x+b.w*t,b.y,b.w/60,'#e9f1ff'); } }
    if(s.i%Math.round(LEN/SEG/2)===0){ quad(a.x,a.y,a.w,b.x,b.y,b.w,'rgba(255,233,74,.6)'); }
    cars.forEach(c=>{ if(seg(c.z)!==s) return; const sc=a.s, cw=sc*RW*W/2*0.32, ch=cw*0.6, X=a.x+a.w*c.off, Y=a.y; if(cw<1.5) return; g.fillStyle=c.col; g.fillRect(X-cw/2,Y-ch,cw,ch); g.fillStyle='#14163a'; g.fillRect(X-cw*0.38,Y-ch*0.92,cw*0.76,ch*0.32); g.fillStyle='#ff1744'; g.fillRect(X-cw/2,Y-ch*0.42,cw*0.18,ch*0.16); g.fillRect(X+cw*0.32,Y-ch*0.42,cw*0.18,ch*0.16); }); }
   const cw=W*0.17, ch=cw*0.5, X=W/2+(px<-1||px>1?Math.sin(Fr.t*40)*1.5:0), Y=H-10, tilt=((R(Fr)?1:0)-(L(Fr)?1:0))*3; g.save(); g.translate(X,Y); g.rotate(tilt*Math.PI/180); g.fillStyle='#ff4f6d'; g.fillRect(-cw/2,-ch,cw,ch); g.fillStyle='#a3122e'; g.fillRect(-cw/2,-ch*0.35,cw,ch*0.35); g.fillStyle='#14163a'; g.fillRect(-cw*0.36,-ch*0.95,cw*0.72,ch*0.34); g.fillStyle=(Fr.keys.ArrowDown||Fr.keys.s)?'#ff8a8a':'#ff1744'; g.fillRect(-cw/2+3,-ch*0.55,cw*0.2,ch*0.15); g.fillRect(cw*0.3-3,-ch*0.55,cw*0.2,ch*0.15); g.fillStyle='#111'; g.fillRect(-cw/2-3,-ch*0.3,8,ch*0.3); g.fillRect(cw/2-5,-ch*0.3,8,ch*0.3); g.restore();
   g.fillStyle='rgba(0,0,0,.5)'; g.fillRect(W-112,28,104,40); g.fillStyle='#ffe94a'; g.font='bold 16px system-ui,sans-serif'; g.textAlign='right'; g.fillText(Math.round(spd/MAX*240)+' km/h',W-14,46); g.fillStyle=time<10?'#ff4f6d':'#7cff8a'; g.fillText('⏱ '+Math.ceil(time)+' s',W-14,64); g.textAlign='left'; }
  return {state:()=>({score:F.score,speed:Math.round(spd/MAX*240),time:Math.ceil(time),dist:Math.round(dist)})}; });
})();
