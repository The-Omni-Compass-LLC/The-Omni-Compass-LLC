(()=>{ /* 🚀 PRO ARCADE (v264), part 2. Our own games in well-known genres; our own names, characters, art and rules.
   3 · PULSE FIGHTERS (one-on-one fighting): four fighters of our own (Volt, Granite, Aria, Kestrel), each with its own speed, power,
   jump and pulse special. Punch, kick, low sweep, block, jump, a three-hit combo, a super meter, rounds against the clock, best of three,
   against a computer fighter that reads distance and reacts. 💥 Cannon on: a full charge fires a cannon beam across the arena.
   4 · MIND LAB (brain training): Memory Matrix (remember the lit tiles), Speed Match (is it the same as the one before?), Pattern Logic
   (what comes next?) and Quick Math, each a one-minute round that gets harder as you get it right. 💥 Cannon on: a full charge answers
   the question in front of you (in Memory Matrix it shows the pattern again). */
 const wait=fn=>{ if(window.KPRO&&window.GAMES&&GAMES.reg&&GAMES.lib) return fn(); let n=0; const t=setInterval(()=>{ if(window.KPRO&&window.GAMES&&GAMES.reg&&GAMES.lib){ clearInterval(t); fn(); } else if(++n>80) clearInterval(t); },400); };
 wait(()=>{ const {frame,rrect,reg,rnd,rr,cl,getLS,putLS}=KPRO;

 /* ================= 3 · PULSE FIGHTERS ================= */
 const CHR=[{n:'VOLT',c:'#4fe3ff',c2:'#1a6cff',sp:1.15,pw:.9,jp:1,proj:'orb'},{n:'GRANITE',c:'#ff9a3c',c2:'#a33a00',sp:.85,pw:1.25,jp:.9,proj:'rock'},{n:'ARIA',c:'#ff6fd8',c2:'#8a1e7a',sp:1,pw:1,jp:1,proj:'ring'},{n:'KESTREL',c:'#7cff8a',c2:'#1d7a36',sp:1.05,pw:.95,jp:1.22,proj:'feather'}];
 reg('pro_fight','Pulse Fighters','🚀 Pro Arcade · one-on-one fighting. Pick one of four fighters of our own (Volt fast, Granite strong, Aria balanced, Kestrel high-flying) and beat the computer fighter two rounds out of three before the clock runs out. ← → walk, ↑ jump, ↓ crouch, Z punch, X kick (↓ + X sweeps the legs), A block (hold), S pulse special (uses one bar of the meter). Punch, punch, kick quickly is a three-hit combo. On a phone, the pad under the screen. 💥 Cannon on: a full charge fires a cannon beam across the arena.',ctx=>{
  let P, E, me=0, foe=1, round=1, wins=[0,0], clock=60, banner='', bannerT=0, slow=0, proj=[], diff=1, hist=[], roundOver=0, sky=[];
  const GY=F=>F.H*.84, HT=F=>F.H*.34;
  function mkF(F,ci,x,face){ const c=CHR[ci]; return {c,x,y:GY(F),vx:0,vy:0,face,hp:100,dhp:100,meter:0,st:'idle',t:0,atk:null,air:false,crouch:false,block:false,stun:0,combo:0,lastHit:0}; }
  function startRound(F){ P=mkF(F,me,F.W*.28,1); E=mkF(F,foe,F.W*.72,-1); proj=[]; clock=60; banner='ROUND '+round; bannerT=1.6; roundOver=0; slow=0; F.snd(440,.1); setTimeout(()=>F.snd(660,.12),200); }
  const ATK={punch:{d:5,reach:.42,a0:.06,a1:.15,len:.26,h:'mid'},kick:{d:8,reach:.6,a0:.12,a1:.22,len:.42,h:'mid'},jab:{d:4,reach:.4,a0:.05,a1:.13,len:.24,h:'low'},sweep:{d:7,reach:.62,a0:.12,a1:.24,len:.5,h:'low',kd:1},finisher:{d:12,reach:.66,a0:.1,a1:.22,len:.46,h:'mid',kd:1},special:{d:0,reach:0,a0:.18,a1:.19,len:.5,h:'mid'}};
  function act(F,f,o,kind){ if(f.st==='ko'||f.st==='win'||f.stun>0||f.atk) return; if(kind==='special'){ if(f.meter<1) return; f.meter-=1; }
   if(kind==='kick'&&f.crouch) kind='sweep'; if(kind==='punch'&&f.crouch) kind='jab';
   const now=F.t; if(f===P){ hist.push([kind,now]); hist=hist.filter(h=>now-h[1]<.9); const k=hist.map(h=>h[0]).join(','); if(/punch,punch,kick$/.test(k)){ kind='finisher'; hist=[]; } }
   f.atk={k:kind,...ATK[kind],t:0,hit:false}; f.st=kind; F.snd(kind==='special'?300:kind==='kick'||kind==='sweep'||kind==='finisher'?220:330,.04); }
  function hurt(F,att,def,dmg,kd,low,isProj){ const blocking=def.block&&!(low&&!def.crouch)&&def.st!=='ko'; const hx=def.x, hy=def.y-HT(F)*(def.crouch?.35:.6);
   if(blocking){ dmg=Math.max(1,Math.round(dmg*.15)); def.hp=Math.max(0,def.hp-dmg); def.stun=.14; def.vx=110*-def.face; F.burst(hx,hy,'#cfe8ff',8,120,.3); F.snd(700,.03); }
   else { def.hp=Math.max(0,def.hp-dmg); def.stun=kd?.7:.32; def.vx=(kd?320:220)*att.face; if(kd){ def.vy=-320; def.air=true; } def.st='hit'; def.atk=null; att.meter=Math.min(3,att.meter+.14); def.meter=Math.min(3,def.meter+.07); att.combo++; att.lastHit=F.t;
    F.burst(hx,hy,att.c.c,18,240,.45); F.ring(hx,hy,att.c.c,60); F.shake=Math.max(F.shake,kd?9:5); F.snd(kd?120:180,.07); if(att===P){ F.add(dmg*25+(att.combo>1?att.combo*40:0)); F.feed(dmg*.012); if(att.combo>1) F.text(hx,hy-40,att.combo+' HIT COMBO',att.c.c,20); } }
   if(def.hp<=0&&!roundOver) ko(F,att,def); }
  function ko(F,w,l){ roundOver=2.6; slow=1.2; l.st='ko'; l.atk=null; l.vy=-260; l.air=true; w.st='win'; const wi=w===P?0:1; wins[wi]++; banner=w===P?'K.O. · YOU WIN THE ROUND':'K.O.'; bannerT=2.4; F.snd(90,.5); if(w===P) F.add(2000+Math.round(clock)*30); }
  function timeUp(F){ if(roundOver) return; const w=P.hp>=E.hp?P:E, l=w===P?E:P; roundOver=2.6; w.st='win'; wins[w===P?0:1]++; banner='TIME · '+(w===P?'YOU WIN THE ROUND':w.c.n+' WINS'); bannerT=2.4; if(w===P) F.add(1000); }
  function phys(F,f,o,dt){ const g=GY(F); f.t+=dt; if(f.stun>0){ f.stun-=dt; if(f.stun<=0&&f.st==='hit') f.st='idle'; }
   if(f.atk){ f.atk.t+=dt; const A=f.atk; if(A.k==='special'&&!A.hit&&A.t>=A.a0){ A.hit=true; proj.push({x:f.x+f.face*HT(F)*.35,y:f.y-HT(F)*.62,vx:f.face*(420+f.c.sp*60),o:f,t:0,kind:f.c.proj}); }
    else if(!A.hit&&A.t>=A.a0&&A.t<=A.a1){ const dist=Math.abs(o.x-f.x), inFront=Math.sign(o.x-f.x)===f.face||dist<10; const vy=Math.abs((o.y-(o.crouch?HT(F)*.2:0))-f.y)<HT(F)*.75; if(inFront&&dist<A.reach*HT(F)+HT(F)*.18&&vy&&o.st!=='ko'){ A.hit=true; hurt(F,f,o,Math.round(A.d*f.c.pw),A.kd,A.h==='low'); } }
    if(A.t>=A.len){ f.atk=null; if(f.st!=='hit'&&f.st!=='ko'&&f.st!=='win') f.st='idle'; } }
   f.x+=f.vx*dt; if(f.air){ f.vy+=1500*dt; f.y+=f.vy*dt; if(f.y>=g){ f.y=g; f.vy=0; f.air=false; if(f.st==='jump') f.st='idle'; } } else if(!f.atk||f.st==='hit') f.vx*=Math.pow(.0005,dt);
   const m=HT(F)*.25; f.x=cl(f.x,m,F.W-m); const gap=HT(F)*.36; if(Math.abs(f.x-o.x)<gap&&!f.air&&!o.air){ const push=(gap-Math.abs(f.x-o.x))/2*Math.sign(f.x-o.x||1); f.x+=push; o.x-=push; }
   if(f.st!=='ko'&&f.st!=='win'&&!f.atk&&f.stun<=0) f.face=o.x>f.x?1:-1; }
  function control(F,f,o,inp,dt){ if(f.st==='ko'||f.st==='win'||f.stun>0||roundOver) return; const sp=230*f.c.sp; f.block=!!inp.block&&!f.air; f.crouch=!!inp.down&&!f.air&&!f.atk;
   if(f.atk){ if(!f.air) f.vx*=.8; return; }
   if(inp.up&&!f.air&&!f.block){ f.vy=-640*f.c.jp; f.air=true; f.st='jump'; f.vx=(inp.left?-1:inp.right?1:0)*sp*.95; F.snd(520,.03); return; }
   if(f.air) return; if(f.block){ f.vx=0; f.st='block'; return; } if(f.crouch){ f.vx=0; f.st='crouch'; return; }
   const dir=(inp.right?1:0)-(inp.left?1:0); f.vx=dir*sp*(dir===f.face?1:.75); f.st=dir?'walk':'idle'; }
  /* the computer fighter: reads the distance, reacts to attacks, keeps its distance or closes in */
  let aiT=0, aiIn={};
  function ai(F,dt){ aiT-=dt; const d=Math.abs(P.x-E.x)/HT(F); const react=[.32,.2,.11][diff]; const pAtk=P.atk&&P.atk.t<P.atk.a1;
   if(pAtk&&d<1.1&&Math.random()<[.25,.5,.75][diff]*dt*12){ aiIn={block:true,down:P.atk&&P.atk.h==='low'}; aiT=.25; return aiIn; }
   if(aiT>0) return aiIn; aiT=react+Math.random()*.2; const toward=P.x>E.x?'right':'left', away=toward==='right'?'left':'right'; aiIn={};
   if(proj.some(q=>q.o===P&&Math.abs(q.x-E.x)<HT(F)*1.6)){ if(Math.random()<.5) aiIn.up=true; else aiIn.block=true; return aiIn; }
   /* in reach: a punch reaches about 0.6 of a fighter's height, a kick about 0.78 */
   if(d>2.2){ if(E.meter>=1&&Math.random()<.35) act(F,E,P,'special'); else aiIn[toward]=true; }
   else if(d>.62&&d<=.8){ const r=Math.random(); if(r<.45) act(F,E,P,'kick'); else if(r<.6){ aiIn.down=true; setTimeout(()=>act(F,E,P,'kick'),40); } else aiIn[toward]=true; }
   else if(d>.8){ const r=Math.random(); if(r<.5) aiIn[toward]=true; else if(r<.62) aiIn.up=true,aiIn[toward]=true; else if(r<.72&&E.meter>=1) act(F,E,P,'special'); }
   else { const r=Math.random(); if(r<.38) act(F,E,P,'punch'); else if(r<.62) act(F,E,P,'kick'); else if(r<.74){ aiIn.down=true; setTimeout(()=>act(F,E,P,'kick'),40); } else if(r<.86) aiIn[away]=true; else aiIn.block=true; }
   return aiIn; }
  function pose(f,F){ /* joint angles of the stick-figure athlete, by state */ const t=f.t, b=Math.sin(t*6)*.05; const A=f.atk, ph=A?cl(A.t/A.a1,0,1):0;
   let p={lean:.08+b,sh1:.9,el1:-1.9,sh2:.5,el2:-2.1,hp1:.25,kn1:.35,hp2:-.18,kn2:.3,crouch:0,rot:0};
   if(f.st==='walk'){ const w=Math.sin(t*11)*.45; p.hp1=.2+w; p.kn1=.35+Math.max(0,-w); p.hp2=-.15-w; p.kn2=.35+Math.max(0,w); }
   if(f.st==='crouch'||f.crouch){ p.crouch=.32; p.hp1=1.2; p.kn1=2.1; p.hp2=.9; p.kn2=2.2; p.lean=.35; }
   if(f.st==='block'){ p.sh1=.2; p.el1=-2.6; p.sh2=.05; p.el2=-2.7; p.lean=-.05; }
   if(f.st==='jump'||f.air&&f.st!=='hit'&&f.st!=='ko'){ p.hp1=1.1; p.kn1=1.9; p.hp2=.6; p.kn2=1.6; }
   if(A){ const k=A.k; if(k==='punch'||k==='jab'){ p.sh1=1.57*ph+.9*(1-ph); p.el1=-1.9*(1-ph); p.lean=.2; }
    if(k==='kick'||k==='finisher'){ p.hp1=1.57*ph+.25*(1-ph); p.kn1=.35*(1-ph); p.lean=-.25; } if(k==='sweep'){ p.crouch=.4; p.hp2=1; p.kn2=2.2; p.hp1=1.5*ph+.3; p.kn1=.2; p.lean=.4; }
    if(k==='special'){ p.sh1=1.57; p.el1=0; p.sh2=1.4; p.el2=-.2; p.lean=.15; } }
   if(f.st==='hit'){ p.lean=-.45; p.sh1=-.4; p.sh2=-.6; } if(f.st==='ko'){ p.rot=f.air?-.8:-1.57; p.lean=-.2; }
   if(f.st==='win'){ p.sh1=2.8; p.el1=-.3; p.sh2=2.5; p.el2=-.4; } return p; }
  function drawFighter(F,f){ const g=F.g, H=HT(F), p=pose(f,F), s=f.face; const L={thigh:H*.25,shin:H*.25,torso:H*.3,up:H*.16,fore:H*.16,head:H*.075};
   g.save(); g.translate(f.x,f.y); if(p.rot){ g.translate(0,-H*.15); g.rotate(p.rot*s); g.translate(0,H*.15); } g.scale(s,1);
   const hipY=-(L.thigh+L.shin)*(1-p.crouch*.55); const seg=(x,y,a,len)=>[x+Math.sin(a)*len,y+Math.cos(a)*len];
   const limb=(pts,w,col)=>{ g.strokeStyle=col; g.lineWidth=w; g.lineCap='round'; g.lineJoin='round'; g.beginPath(); g.moveTo(pts[0][0],pts[0][1]); for(let i=1;i<pts.length;i++) g.lineTo(pts[i][0],pts[i][1]); g.stroke(); };
   const hip=[0,hipY]; const sh=[Math.sin(p.lean)*L.torso,hipY-Math.cos(p.lean)*L.torso];
   const k2=seg(hip[0],hip[1],p.hp2,L.thigh), f2=seg(k2[0],k2[1],p.hp2-p.kn2,L.shin); const k1=seg(hip[0],hip[1],p.hp1,L.thigh), f1=seg(k1[0],k1[1],p.hp1-p.kn1,L.shin);
   const e2=seg(sh[0],sh[1],p.sh2,L.up), h2=seg(e2[0],e2[1],p.sh2+p.el2,L.fore); const e1=seg(sh[0],sh[1],p.sh1,L.up), h1=seg(e1[0],e1[1],p.sh1+p.el1,L.fore);
   g.shadowColor=f.c.c; g.shadowBlur=14; limb([hip,k2,f2],H*.075,f.c.c2); limb([sh,e2,h2],H*.06,f.c.c2);
   limb([hip,sh],H*.12,f.c.c); limb([hip,k1,f1],H*.08,f.c.c); limb([sh,e1,h1],H*.065,f.c.c);
   g.fillStyle=f.c.c; g.beginPath(); g.arc(sh[0]+Math.sin(p.lean)*L.head*1.3,sh[1]-L.head*1.6,L.head,0,7); g.fill(); g.shadowBlur=0;
   g.fillStyle='#0a0620'; g.fillRect(sh[0]+Math.sin(p.lean)*L.head*1.3+L.head*.1,sh[1]-L.head*1.8,L.head*.8,L.head*.28);
   [h1,h2].forEach(hh=>{ g.fillStyle='#fff'; g.beginPath(); g.arc(hh[0],hh[1],H*.035,0,7); g.fill(); });
   if(f.block){ g.strokeStyle='rgba(180,230,255,.75)'; g.lineWidth=3; g.beginPath(); g.arc(H*.18,hipY-L.torso*.6,H*.28,-1,1); g.stroke(); }
   g.restore(); g.fillStyle='rgba(0,0,0,.4)'; g.beginPath(); g.ellipse(f.x,GY(F)+4,H*.22,H*.04,0,0,7); g.fill(); }
  function cannon(F){ const y=P.y-HT(F)*.6; F.beam={t:0,y,dir:P.face,x:P.x}; const inLine=Math.sign(E.x-P.x)===P.face&&Math.abs(E.y-P.y)<HT(F); if(inLine) hurt(F,P,E,E.block?10:30,true,false,true); F.text(F.W/2,F.H*.3,'💥 CANNON BEAM','#ffe94a',30); }
  const inp={}; let F;
  F=frame(ctx,'pro_fight',{title:'Pulse Fighters',ratio:.56,maxW:960,hFrac:.62,charge:.0004,cannonHelp:'A full charge fires a cannon beam across the arena.',hint:'Pick a fighter with 👤, then ▶ Start. ← → ↑ ↓ move, Z punch, X kick, A block, S special.',go:'Fight! Z punch, X kick, A block, S special; punch, punch, kick is a combo.',
   pad:[['◀','ArrowLeft'],['▲','ArrowUp'],['▼','ArrowDown'],['▶','ArrowRight'],['👊','z'],['🦵','x'],['🛡','a'],['✨','s']],
   reset(F){ round=1; wins=[0,0]; foe=(me+1+rnd(3))%4; sky=Array.from({length:26},(_,i)=>({x:i/26,w:.02+Math.random()*.05,h:.15+Math.random()*.35,l:Math.random()})); startRound(F); },
   hud:F=>'Round '+round+' · '+wins[0]+'–'+wins[1]+' · '+F.score.toLocaleString(),
   cannon:F=>cannon(F),
   buttons:F=>[['👤 Fighter',()=>{ me=(me+1)%4; foe=(me+1+rnd(3))%4; startRound(F); ctx.status('👤 You fight as '+CHR[me].n+' against '+CHR[foe].n+'. Press ▶ Start.'); },true],['🤖 Level',()=>{ diff=(diff+1)%3; ctx.status('🤖 Computer fighter: '+['Easy','Normal','Hard'][diff]+'.'); },true]],
   key(F,e,down){ const k=e.key&&e.key.length===1?e.key.toLowerCase():e.key; const m={ArrowLeft:'left',ArrowRight:'right',ArrowUp:'up',ArrowDown:'down',a:'block'}[k]; if(m){ inp[m]=down; return true; }
    if(down&&!e.repeat){ if(k==='z'){ act(F,P,E,'punch'); return true; } if(k==='x'){ act(F,P,E,'kick'); return true; } if(k==='s'){ act(F,P,E,'special'); return true; } } return ['z','x','s'].includes(k); },
   update(F,dt){ if(bannerT>0) bannerT-=dt; const sdt=slow>0?dt*.35:dt; if(slow>0) slow-=dt;
    if(roundOver){ roundOver-=dt; phys(F,P,E,sdt); phys(F,E,P,sdt); if(roundOver<=0){ if(wins[0]>=2){ F.add(5000); F.end('You won the match as '+P.c.n+'!'); return; } if(wins[1]>=2){ F.end(E.c.n+' won the match.'); return; } round++; startRound(F); } return; }
    if(bannerT<=0&&!banner.startsWith('FIGHT')&&banner.startsWith('ROUND')){ banner='FIGHT!'; bannerT=.8; F.snd(880,.12); }
    if(!(banner.startsWith('ROUND')&&bannerT>0)) clock-=dt; if(clock<=0){ clock=0; timeUp(F); }
    if(!(banner.startsWith('ROUND')&&bannerT>0)){ control(F,P,E,inp,sdt); control(F,E,P,ai(F,sdt),sdt); } phys(F,P,E,sdt); phys(F,E,P,sdt);
    if(P.combo&&F.t-P.lastHit>1) P.combo=0; if(E.combo&&F.t-E.lastHit>1) E.combo=0;
    for(let i=proj.length-1;i>=0;i--){ const q=proj[i]; q.t+=sdt; q.x+=q.vx*sdt; const o=q.o===P?E:P; if(Math.abs(q.x-o.x)<HT(F)*.2&&Math.abs(q.y-(o.y-HT(F)*.55))<HT(F)*.5&&o.st!=='ko'){ hurt(F,q.o,o,Math.round(12*q.o.c.pw),false,false,true); proj.splice(i,1); continue; }
     const other=proj.find(z=>z!==q&&z.o!==q.o&&Math.abs(z.x-q.x)<20); if(other){ F.burst(q.x,q.y,'#fff',20,200,.4); proj.splice(proj.indexOf(other),1); proj.splice(proj.indexOf(q),1); continue; } if(q.x<-50||q.x>F.W+50) proj.splice(i,1); }
    P.dhp+=(P.hp-P.dhp)*Math.min(1,dt*2); E.dhp+=(E.hp-E.dhp)*Math.min(1,dt*2); if(F.beam){ F.beam.t+=dt; if(F.beam.t>.6) F.beam=null; } },
   draw(F,dt){ const g=F.g, W=F.W, H=F.H, gy=GY(F); const sk=g.createLinearGradient(0,0,0,gy); sk.addColorStop(0,'#1a0b44'); sk.addColorStop(.6,'#5a1460'); sk.addColorStop(1,'#ff6a3d'); g.fillStyle=sk; g.fillRect(0,0,W,gy);
    const cam=((P?P.x+E.x:W)/2-W/2)*.15; g.fillStyle='rgba(255,220,120,.85)'; g.beginPath(); g.arc(W*.7-cam*.3,gy*.55,H*.12,0,7); g.fill();
    sky.forEach(b=>{ const x=b.x*W*1.1-cam*.6-W*.05, bw=b.w*W, bh=b.h*gy; g.fillStyle='#120826'; g.fillRect(x,gy-bh,bw,bh); g.fillStyle='rgba(255,230,140,.55)'; for(let wy=gy-bh+8;wy<gy-6;wy+=10) for(let wx=x+4;wx<x+bw-4;wx+=8) if(((wx*7+wy*3+Math.floor(b.l*9))|0)%5===0) g.fillRect(wx,wy,3,4); });
    const fl=g.createLinearGradient(0,gy,0,H); fl.addColorStop(0,'#2a0d4a'); fl.addColorStop(1,'#07020f'); g.fillStyle=fl; g.fillRect(0,gy,W,H-gy);
    g.strokeStyle='rgba(255,79,216,.35)'; g.lineWidth=1; for(let i=-10;i<=10;i++){ g.beginPath(); g.moveTo(W/2+i*40-cam,gy); g.lineTo(W/2+i*160-cam*2,H); g.stroke(); } for(let k=1;k<6;k++){ const yy=gy+(H-gy)*(k/6)**1.6; g.beginPath(); g.moveTo(0,yy); g.lineTo(W,yy); g.stroke(); }
    if(!P) return; [E,P].forEach(f=>drawFighter(F,f));
    g.globalCompositeOperation='lighter'; proj.forEach(q=>{ const col=q.o.c.c; const r=HT(F)*.09; const gr=g.createRadialGradient(q.x,q.y,0,q.x,q.y,r*2.2); gr.addColorStop(0,'#fff'); gr.addColorStop(.4,col); gr.addColorStop(1,'rgba(0,0,0,0)'); g.fillStyle=gr; g.beginPath(); g.arc(q.x,q.y,r*2.2,0,7); g.fill(); if(q.kind==='ring'){ g.strokeStyle=col; g.lineWidth=3; g.beginPath(); g.arc(q.x,q.y,r*1.4+Math.sin(q.t*20)*3,0,7); g.stroke(); } });
    if(F.beam){ const b=F.beam, a=1-b.t/.6; const x0=b.x, x1=b.dir>0?W:0; const gr=g.createLinearGradient(0,b.y-40,0,b.y+40); gr.addColorStop(0,'rgba(255,233,74,0)'); gr.addColorStop(.5,'rgba(255,255,255,'+a+')'); gr.addColorStop(1,'rgba(255,233,74,0)'); g.fillStyle=gr; g.fillRect(Math.min(x0,x1),b.y-40*a-6,Math.abs(x1-x0),80*a+12); }
    g.globalCompositeOperation='source-over';
    /* health bars, meters, clock and names */ const bw=W*.38, by=34; [[P,12,1],[E,W-12-bw,-1]].forEach(([f,x,s])=>{ g.fillStyle='rgba(0,0,0,.55)'; rrect(g,x-2,by-2,bw+4,18,6); g.fill(); g.fillStyle='rgba(255,255,255,.85)'; const fd=bw*f.dhp/100, fh=bw*f.hp/100; g.fillRect(s>0?x+bw-fd:x,by,fd,14); const gr=g.createLinearGradient(x,0,x+bw,0); gr.addColorStop(0,f.hp>30?'#7cff8a':'#ff4f6d'); gr.addColorStop(1,f.hp>30?'#ffe94a':'#ff9a3c'); g.fillStyle=gr; g.fillRect(s>0?x+bw-fh:x,by,fh,14);
     g.fillStyle=f.c.c; g.font='900 13px system-ui,sans-serif'; g.textAlign=s>0?'left':'right'; g.fillText(f.c.n+(f===P?' · YOU':''),s>0?x:x+bw,by+30); for(let m=0;m<3;m++){ g.fillStyle=f.meter>m+1-1e-6?f.c.c:f.meter>m?'rgba(255,255,255,.4)':'rgba(255,255,255,.12)'; const mx=s>0?x+m*22:x+bw-20-m*22; rrect(g,mx,by+36,18,7,3); g.fill(); } });
    g.fillStyle='#fff'; g.font='900 24px ui-monospace,monospace'; g.textAlign='center'; g.fillText(String(Math.ceil(clock)),W/2,by+15); g.font='700 11px system-ui,sans-serif'; g.fillStyle='#ffe94a'; g.fillText('●'.repeat(wins[0])+'○'.repeat(2-wins[0])+'   '+'○'.repeat(2-wins[1])+'●'.repeat(wins[1]),W/2,by+32);
    if(bannerT>0&&banner){ const a=Math.min(1,bannerT*2); g.globalAlpha=a; g.font='900 '+Math.min(48,W/14)+'px system-ui,sans-serif'; g.textAlign='center'; g.lineWidth=6; g.strokeStyle='rgba(0,0,0,.7)'; g.strokeText(banner,W/2,H*.42); const tg=g.createLinearGradient(W/2-200,0,W/2+200,0); tg.addColorStop(0,'#ffe94a'); tg.addColorStop(1,'#ff4f6d'); g.fillStyle=tg; g.fillText(banner,W/2,H*.42); g.globalAlpha=1; } } });
  return {state:()=>({round,wins,php:P.hp,ehp:E.hp,clock,score:F.score}),F,act:k=>act(F,P,E,k)};
 });

 /* ================= 4 · MIND LAB ================= */
 const MODES=[['mem','🧩 Memory Matrix'],['speed','⚡ Speed Match'],['logic','🔢 Pattern Logic'],['math','➗ Quick Math']];
 const SHAPES=['●','▲','■','◆','★','⬢'], SCOL=['#ff4f6d','#ffe94a','#6fe8ff','#7cff8a','#c38bff','#ff9a3c'];
 reg('pro_mind','Mind Lab','🚀 Pro Arcade · brain training, four one-minute games. 🧩 Memory Matrix: remember the tiles that light, then tap them. ⚡ Speed Match: does this card match the one before? (← no, → yes). 🔢 Pattern Logic: pick what comes next. ➗ Quick Math: pick the answer. Each gets harder as you get it right; a mistake steps it back. Change the game with 🧠 Game. Keys 1 to 4 pick an answer. 💥 Cannon on: a full charge answers the question in front of you.',ctx=>{
  let mode=0, Q=null, left=60, streak=0, lvl=1, memN=3, memG=4, phase='show', phT=0, picked=new Set(), prevCard=null, card=null, shake=0, rightN=0, wrongN=0, opts=[];
  const ans=(F,ok,x,y)=>{ if(ok){ streak++; rightN++; const pts=Math.round((MODES[mode][0]==='mem'?memN*120:100)*(1+Math.min(streak,10)*.1)*(1+lvl*.1)); F.add(pts); F.feed(.05+streak*.004); F.burst(x||F.W/2,y||F.H/2,'#7cff8a',22,220,.6); F.text(x||F.W/2,(y||F.H/2)-30,'+'+pts,'#7cff8a',22); F.snd(880+streak*30,.06); lvl=Math.min(20,lvl+.5); }
   else { streak=0; wrongN++; shake=.4; F.burst(x||F.W/2,y||F.H/2,'#ff4f6d',14,180,.5); F.snd(150,.12); lvl=Math.max(1,lvl-1); } next(F); };
  function next(F){ const m=MODES[mode][0]; opts=[];
   if(m==='mem'){ if(Q&&Q.ok!=null){ memN=Q.ok?memN+1:Math.max(3,memN-1); } memG=memN>=10?6:memN>=7?5:4; const cells=new Set(); while(cells.size<memN) cells.add(rnd(memG*memG)); Q={cells,ok:null}; picked=new Set(); phase='show'; phT=Math.max(.9,1.6-memN*.05); }
   else if(m==='speed'){ prevCard=card; card={s:rnd(Math.min(6,2+Math.floor(lvl/3))),c:rnd(Math.min(6,2+Math.floor(lvl/4)))}; if(prevCard&&Math.random()<.45) card={...prevCard}; Q={match:prevCard?(prevCard.s===card.s&&prevCard.c===card.c):null}; }
   else if(m==='logic'){ const L=Math.floor(lvl); const kind=rnd(L<4?2:L<8?4:5); let seq=[], nxt;
    if(kind===0){ const a=rnd(9)+1, d=rnd(6)+2; seq=[0,1,2,3].map(i=>a+i*d); nxt=a+4*d; } else if(kind===1){ const a=rnd(4)+1, r=rnd(2)+2; seq=[0,1,2,3].map(i=>a*Math.pow(r,i)); nxt=a*Math.pow(r,4); }
    else if(kind===2){ const a=rnd(9)+2, d1=rnd(5)+1, d2=rnd(5)+2; seq=[a,a+d1,a+d1-d2,a+2*d1-d2]; nxt=a+2*d1-2*d2; } else if(kind===3){ let x=rnd(4)+1, y=rnd(4)+2; seq=[x,y]; while(seq.length<4) seq.push(seq[seq.length-1]+seq[seq.length-2]); nxt=seq[2]+seq[3]; } else { const a=rnd(5)+1; seq=[1,2,3,4].map(i=>(a+i)*(a+i)); nxt=(a+5)*(a+5); }
    Q={seq,ans:nxt}; const S=new Set([nxt]); while(S.size<4){ const v=nxt+(rnd(2)?1:-1)*(rnd(Math.max(3,Math.abs(nxt)/4|0))+1); if(v!==nxt) S.add(v); } opts=[...S].sort(()=>Math.random()-.5); }
   else { const L=Math.floor(lvl); const op=rnd(L<3?2:4); let a,b,r; if(op===0){ a=rnd(10*L)+2; b=rnd(10*L)+2; r=a+b; } else if(op===1){ a=rnd(10*L)+10; b=rnd(a-1)+1; r=a-b; } else if(op===2){ a=rnd(Math.min(12,2+L))+2; b=rnd(Math.min(12,2+L))+2; r=a*b; } else { b=rnd(Math.min(12,2+L))+2; r=rnd(Math.min(12,2+L))+2; a=b*r; }
    Q={txt:a+' '+['+','−','×','÷'][op]+' '+b,ans:r}; const S=new Set([r]); while(S.size<4){ const v=r+(rnd(2)?1:-1)*(rnd(Math.max(4,r/5|0))+1); if(v>=0&&v!==r) S.add(v); } opts=[...S].sort(()=>Math.random()-.5); } }
  const box=(F,i)=>{ const n=opts.length||2, w=Math.min(170,(F.W-40)/n-10), x=F.W/2-(n*(w+10)-10)/2+i*(w+10), y=F.H*.66; return {x,y,w,h:64}; };
  function pick(F,i){ const m=MODES[mode][0]; if(m==='logic'||m==='math'){ const b=box(F,i); if(opts[i]==null) return; ans(F,opts[i]===Q.ans,b.x+b.w/2,b.y); } }
  function speed(F,yes){ if(MODES[mode][0]!=='speed') return; if(Q.match===null){ next(F); return; } ans(F,yes===Q.match,F.W/2+(yes?120:-120),F.H*.7); }
  function grid(F){ const S=Math.min(F.W*.7,F.H-90), cs=S/memG; return {x:F.W/2-S/2,y:44,cs,S}; }
  let F; F=frame(ctx,'pro_mind',{title:'Mind Lab',ratio:.72,maxW:760,hFrac:.66,charge:.0004,cannonHelp:'A full charge answers the question in front of you.',hint:'Choose the game with 🧠 Game, then ▶ Start: one minute each.',
   reset(F){ left=60; streak=0; lvl=1; memN=3; rightN=0; wrongN=0; Q=null; card=null; prevCard=null; next(F); },
   hud:F=>MODES[mode][1]+' · '+Math.ceil(left)+' s · '+F.score.toLocaleString()+(streak>1?' · streak '+streak:''),
   buttons:F=>[['🧠 Game',()=>{ mode=(mode+1)%4; F.reset(); F.running=false; F.over=false; F.paint(); ctx.status(MODES[mode][1]+': press ▶ Start for a one-minute round.'); },true],['✖ No (←)',()=>speed(F,false)],['✔ Yes (→)',()=>speed(F,true)]],
   cannon(F){ const m=MODES[mode][0]; if(m==='mem'){ phase='show'; phT=1.2; F.text(F.W/2,40,'💥 The cannon shows it again','#ffe94a',20); } else if(m==='speed'){ speed(F,Q.match===null?true:Q.match); } else { const i=opts.indexOf(Q.ans); pick(F,i); } },
   key(F,e,down){ if(!down) return false; const k=e.key; if(/^[1-4]$/.test(k)){ pick(F,+k-1); return true; } if(k==='ArrowLeft'){ speed(F,false); return true; } if(k==='ArrowRight'){ speed(F,true); return true; } return false; },
   pointer(F,t,x,y){ if(t!=='down') return; const m=MODES[mode][0];
    if(m==='mem'&&phase==='pick'){ const G=grid(F); const c=Math.floor((x-G.x)/G.cs), r=Math.floor((y-G.y)/G.cs); if(r<0||c<0||r>=memG||c>=memG) return; const i=r*memG+c; if(picked.has(i)) return; picked.add(i);
     if(!Q.cells.has(i)){ Q.ok=false; ans(F,false,x,y); } else { F.snd(660+picked.size*40,.04); if([...Q.cells].every(z=>picked.has(z))){ Q.ok=true; ans(F,true,x,y); } } return; }
    if(m==='speed'){ speed(F,x>F.W/2); return; } for(let i=0;i<opts.length;i++){ const b=box(F,i); if(x>=b.x&&x<=b.x+b.w&&y>=b.y&&y<=b.y+b.h){ pick(F,i); return; } } },
   update(F,dt){ left-=dt; if(shake>0) shake-=dt; if(phase==='show'&&MODES[mode][0]==='mem'){ phT-=dt; if(phT<=0) phase='pick'; } if(left<=0){ left=0; const acc=rightN+wrongN?Math.round(rightN*100/(rightN+wrongN)):0; F.end(MODES[mode][1]+': '+rightN+' right, '+wrongN+' wrong ('+acc+'% accuracy).'); } },
   draw(F){ const g=F.g, W=F.W, H=F.H; const bg=g.createLinearGradient(0,0,W,H); bg.addColorStop(0,'#071a3a'); bg.addColorStop(1,'#1a0838'); g.fillStyle=bg; g.fillRect(0,0,W,H);
    for(let i=0;i<14;i++){ g.strokeStyle='rgba(111,232,255,'+(.04+.03*Math.sin(F.t+i))+')'; g.beginPath(); g.arc(W/2,H/2,40+i*36+(F.t*20)%36,0,7); g.stroke(); }
    g.save(); if(shake>0) g.translate(Math.sin(shake*80)*6,0); const m=MODES[mode][0]; g.textAlign='center';
    if(m==='mem'){ const G=grid(F); for(let r=0;r<memG;r++) for(let c=0;c<memG;c++){ const i=r*memG+c; const lit=(phase==='show'&&Q.cells.has(i))||(phase==='pick'&&picked.has(i)&&Q.cells.has(i)); const bad=phase==='pick'&&picked.has(i)&&!Q.cells.has(i);
      g.fillStyle=lit?'#6fe8ff':bad?'#ff4f6d':'rgba(255,255,255,.08)'; if(lit){ g.shadowColor='#6fe8ff'; g.shadowBlur=18; } rrect(g,G.x+c*G.cs+4,G.y+r*G.cs+4,G.cs-8,G.cs-8,10); g.fill(); g.shadowBlur=0; }
     g.fillStyle='#ffe94a'; g.font='800 15px system-ui,sans-serif'; g.fillText(phase==='show'?'Remember the '+memN+' lit tiles…':'Tap the '+memN+' tiles that were lit',W/2,H-14); }
    else if(m==='speed'){ const draw=(cd,x,a)=>{ if(!cd) return; g.globalAlpha=a; g.fillStyle='rgba(255,255,255,.1)'; rrect(g,x-70,H*.2,140,170,16); g.fill(); g.strokeStyle='rgba(255,255,255,.35)'; g.stroke(); g.fillStyle=SCOL[cd.c]; g.font='900 92px system-ui,sans-serif'; g.fillText(SHAPES[cd.s],x,H*.2+118); g.globalAlpha=1; };
     draw(prevCard,W/2-150,.35); draw(card,W/2+30,1); g.fillStyle='#fff'; g.font='800 16px system-ui,sans-serif'; g.fillText(Q.match===null?'Remember this card · press either side to begin':'Same as the card before?   ← No      Yes →',W/2,H*.82); }
    else { g.fillStyle='#fff'; g.font='900 '+Math.min(54,W/12)+'px system-ui,sans-serif'; g.fillText(m==='logic'?Q.seq.join('   ·   ')+'   ·   ?':Q.txt+' = ?',W/2,H*.38);
     opts.forEach((v,i)=>{ const b=box(F,i); const gr=g.createLinearGradient(0,b.y,0,b.y+b.h); gr.addColorStop(0,'#2a3480'); gr.addColorStop(1,'#141a48'); g.fillStyle=gr; rrect(g,b.x,b.y,b.w,b.h,14); g.fill(); g.strokeStyle='rgba(111,232,255,.6)'; g.lineWidth=2; g.stroke(); g.fillStyle='#fff'; g.font='900 28px system-ui,sans-serif'; g.fillText(String(v),b.x+b.w/2,b.y+42); g.fillStyle='rgba(255,233,74,.8)'; g.font='700 11px system-ui,sans-serif'; g.fillText(String(i+1),b.x+12,b.y+16); }); }
    g.restore(); const tw=W-40; g.fillStyle='rgba(255,255,255,.1)'; g.fillRect(20,H-6,tw,3); g.fillStyle=left<10?'#ff4f6d':'#7cff8a'; g.fillRect(20,H-6,tw*left/60,3); } });
  return {state:()=>({mode:MODES[mode][0],left,streak,lvl,memN,score:F.score,Q,opts}),F,pick:i=>pick(F,i),speed:y=>speed(F,y),setMode:i=>{ mode=i; F.reset(); }};
 });
 });
})();
