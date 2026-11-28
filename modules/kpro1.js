(()=>{ /* 🚀 PRO ARCADE (v264), part 1: the upgraded frame every new game shares, and the first two games.
   Our own games in well-known genres: our own names, characters, art, rules and levels; nothing is copied from any game.
   THE FRAME: a sharp canvas on every screen (drawn at the screen's own pixel density), particles, glow, light and screen shake;
   ▶ Start / ⏸ Pause, ↺ Restart, 🔊 Sound, and the 💥 CANNON switch. With the cannon OFF a game plays on its own rules. With the
   cannon ON a charge meter fills as you play; when it is full, 💥 Fire (or C on the keyboard) fires the cannon into the game, each game
   its own way, and the shot goes through the app's own cannon (the Games limb), so a game is linked to the cannon or not, by choice.
   1 · PRISM CRUSH (match three): swap two gems side by side to line up three or more of a colour. Four in a row makes a line gem
   (it clears its row or column), an L or a T makes a nova (it clears a 3 × 3 square), five in a row makes a prism (it clears every gem
   of one colour). Cascades multiply the score. Reach the target in the moves you have to clear the level.
   2 · NEON LABYRINTH (maze chase): steer the comet through the maze and collect every spark. Four sentinels hunt you, each its own way
   (the Hunter goes for you, the Flanker for where you are going, the Warden guards its corner until you come near, the Drifter turns at
   random). A power core glitches them for a few seconds: touch one then to send it home. Clear the maze to go to the next level. */
 const CAT='Video games';
 const rnd=n=>Math.floor(Math.random()*n), rr=(a,b)=>a+Math.random()*(b-a), cl=(v,a,b)=>Math.max(a,Math.min(b,v));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const h=(t,a,c)=>GAMES.lib.h(t,a,c);
 function rrect(g,x,y,w,hh,r){ r=Math.min(r,w/2,hh/2); g.beginPath(); g.moveTo(x+r,y); g.arcTo(x+w,y,x+w,y+hh,r); g.arcTo(x+w,y+hh,x,y+hh,r); g.arcTo(x,y+hh,x,y,r); g.arcTo(x,y,x+w,y,r); g.closePath(); }
 function reg(id,name,how,init){ const go=()=>{ if(!window.GAMES||!GAMES.reg||!GAMES.lib) return false; GAMES.reg(id,name,CAT,how,init); return true; }; if(!go()){ let n=0; const t=setInterval(()=>{ if(go()||++n>60) clearInterval(t); },500); } }

 /* ================= THE FRAME ================= */
 function frame(ctx,id,o){ const L=GAMES.lib; const W=Math.round(Math.min(ctx.W(),o.maxW||900)); const ratio=W<520?Math.max(o.ratio||.62,.82):(o.ratio||.62); /* a narrow phone screen: a taller game screen */ const H=Math.round(Math.min(W*ratio,Math.max(320,innerHeight*(o.hFrac||0.64))));
  const B=L.mkCanvas(ctx,W,H); const g=B.g; B.cv.style.touchAction='none'; B.cv.style.borderRadius='12px'; B.cv.style.boxShadow='0 0 0 1px rgba(120,200,255,.35),0 10px 40px rgba(0,0,0,.55)';
  const F={W,H,g,cv:B.cv,ctx,id,score:0,best:getLS('kanin-best-'+id,0),running:false,paused:false,over:false,t:0,keys:{},muted:getLS('kanin-gmute',false),cannon:!!getLS('kanin-gcan-'+id,false),charge:0,P:[],T:[],R:[],shake:0,flash:0};
  F.snd=(f,d)=>{ if(F.muted) return; try{ ctx.beep(f,d||.05); }catch(_){ } };
  F.add=n=>{ F.score+=n; if(F.cannon&&!F.over) F.charge=Math.min(1,F.charge+n*(o.charge||0.0012)); };
  F.feed=x=>{ if(F.cannon&&!F.over) F.charge=Math.min(1,F.charge+x); };
  F.msg=t=>ctx.status(t);
  F.burst=(x,y,col,n,spd,life)=>{ for(let i=0;i<(n||16)&&F.P.length<420;i++){ const a=Math.random()*Math.PI*2, v=(spd||140)*(.3+Math.random()); F.P.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:0,L:(life||.7)*(.6+Math.random()*.8),c:col||'#ffe94a',r:1.5+Math.random()*2.5}); } };
  F.text=(x,y,s,col,size)=>{ F.T.push({x,y,s:String(s),c:col||'#fff',l:0,z:size||18}); };
  F.ring=(x,y,col,max)=>{ F.R.push({x,y,c:col||'#6fe8ff',l:0,m:max||120}); };
  F.end=m=>{ if(F.over) return; F.over=true; F.running=false; if(F.score>F.best){ F.best=F.score; putLS('kanin-best-'+id,F.best); m+=' A new best!'; } ctx.status(m+' Score '+F.score.toLocaleString()+' · best '+F.best.toLocaleString()+'. Press ↺ Restart or tap the screen to play again.'); F.snd(160,.3); paint(); };
  F.fire=()=>{ if(!F.cannon){ ctx.status('💥 The cannon is off for this game. Turn it on with 💥 Cannon: off.'); return; } if(!F.running||F.paused||F.over){ ctx.status('Start the game first, then fire the cannon.'); return; } if(F.charge<1){ ctx.status('💥 The cannon is charging: '+Math.round(F.charge*100)+'%. Keep playing to fill it.'); return; }
   F.charge=0; let pw=1; try{ const r=UNILAW.fire('games'); if(r&&typeof r.e==='number') pw=1+Math.min(.5,Math.abs(r.e)/10); }catch(_){ } window.CANNONHIT=(window.CANNONHIT||0)+1; F.shake=14; F.flash=1; F.snd(70,.35); setTimeout(()=>F.snd(220,.2),90); o.cannon&&o.cannon(F,pw); };
  const reset=()=>{ F.score=0; F.over=false; F.t=0; F.paused=false; F.charge=0; F.P.length=0; F.T.length=0; F.R.length=0; o.reset(F); };
  const start=()=>{ if(F.over) reset(); F.running=true; F.paused=false; paint(); ctx.status(o.go||'Go!'); };
  F.start=start; F.reset=reset;
  const bar=h('div',{className:'gbar kProBar'}); const mk=(t,fn,lab)=>{ const b=h('button',{type:'button','aria-label':lab||t},t); b.addEventListener('click',fn); bar.appendChild(b); return b; };
  const bStart=mk('▶ Start',()=>{ if(!F.running||F.over) start(); else { F.paused=!F.paused; paint(); ctx.status(F.paused?'Paused. Press ▶ Resume.':'Playing.'); } });
  mk('↺ Restart',()=>{ reset(); start(); });
  const bS=mk(F.muted?'🔇 Sound off':'🔊 Sound on',()=>{ F.muted=!F.muted; putLS('kanin-gmute',F.muted); bS.textContent=F.muted?'🔇 Sound off':'🔊 Sound on'; },'Sound on or off');
  const bC=mk('',()=>{ F.cannon=!F.cannon; putLS('kanin-gcan-'+id,F.cannon); F.charge=0; paint(); ctx.status(F.cannon?'💥 The cannon is ON: play to charge it, then 💥 Fire (C). '+(o.cannonHelp||''):'The cannon is OFF: the game plays on its own rules.'); },'Cannon on or off');
  const bF=mk('💥 Fire (C)',()=>F.fire(),'Fire the cannon');
  (o.buttons?o.buttons(F):[]).forEach(b=>{ mk(b[0],()=>{ if(!F.running&&!F.over&&!b[2]) start(); b[1](); },b[0]); });
  ctx.area.appendChild(bar);
  /* a touch pad under the screen for phones: each button holds its key down while pressed */
  if(o.pad){ const pad=h('div',{className:'kProPad'}); o.pad.forEach(([lab,key])=>{ const b=h('button',{type:'button','aria-label':lab},lab); const dn=e=>{ e.preventDefault(); if(!F.running&&!F.over){ start(); } F.keys[key]=true; o.key&&o.key(F,{key,code:key,repeat:false},true); }; const up=e=>{ e.preventDefault(); F.keys[key]=false; o.key&&o.key(F,{key,code:key,repeat:false},false); }; b.addEventListener('pointerdown',dn); b.addEventListener('pointerup',up); b.addEventListener('pointerleave',up); b.addEventListener('pointercancel',up); pad.appendChild(b); }); ctx.area.appendChild(pad); }
  function paint(){ bStart.textContent=!F.running||F.over?(F.over?'▶ Play again':'▶ Start'):(F.paused?'▶ Resume':'⏸ Pause'); bC.textContent=F.cannon?'💥 Cannon: on':'💥 Cannon: off'; bC.classList.toggle('on',F.cannon); bF.hidden=!F.cannon; }
  F.paint=paint;
  const pos=e=>{ const r=B.cv.getBoundingClientRect(); return [(e.clientX-r.left)*W/(r.width||1),(e.clientY-r.top)*H/(r.height||1)]; };
  B.cv.addEventListener('pointerdown',e=>{ if(e.button>0) return; e.preventDefault(); const [x,y]=pos(e); F.down=true; try{ B.cv.setPointerCapture(e.pointerId); }catch(_){ } if(F.over){ reset(); start(); return; } if(!F.running){ start(); if(o.tapStarts===false) return; } if(F.paused) return; o.pointer&&o.pointer(F,'down',x,y); });
  B.cv.addEventListener('pointermove',e=>{ const [x,y]=pos(e); if(F.running&&!F.paused) o.pointer&&o.pointer(F,'move',x,y); });
  const up=e=>{ const [x,y]=pos(e); const was=F.down; F.down=false; if(was&&F.running&&!F.paused) o.pointer&&o.pointer(F,'up',x,y); }; B.cv.addEventListener('pointerup',up); B.cv.addEventListener('pointercancel',up);
  ctx.key((e,down)=>{ const k=e.key; if(down&&(k==='p'||k==='P')&&F.running){ F.paused=!F.paused; paint(); return true; } if(down&&(k==='c'||k==='C')){ F.fire(); return true; }
   if(down&&!F.running&&(k===' '||k==='Enter')){ start(); return true; }
   if(F.running&&!F.paused&&o.key){ const r=o.key(F,e,down); if(r) return true; }
   if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown',' '].includes(k)){ F.keys[k]=down; return true; } return false; });
  reset(); paint();
  ctx.raf(dt=>{ if(F.running&&!F.paused&&!F.over){ F.t+=dt; o.update&&o.update(F,dt); }
   /* particles, rings and floating words */ for(let i=F.P.length-1;i>=0;i--){ const p=F.P[i]; p.l+=dt; if(p.l>p.L){ F.P.splice(i,1); continue; } p.x+=p.vx*dt; p.y+=p.vy*dt; p.vx*=.96; p.vy=p.vy*.96+60*dt; }
   for(let i=F.T.length-1;i>=0;i--){ const q=F.T[i]; q.l+=dt; q.y-=30*dt; if(q.l>1.1) F.T.splice(i,1); } for(let i=F.R.length-1;i>=0;i--){ const q=F.R[i]; q.l+=dt*1.6; if(q.l>1) F.R.splice(i,1); }
   g.save(); if(F.shake>0){ g.translate(rr(-F.shake,F.shake),rr(-F.shake,F.shake)); F.shake=Math.max(0,F.shake-dt*40); }
   o.draw(F,dt);
   g.globalCompositeOperation='lighter'; F.P.forEach(p=>{ const a=1-p.l/p.L; g.globalAlpha=a; g.fillStyle=p.c; g.beginPath(); g.arc(p.x,p.y,p.r*(1+a),0,7); g.fill(); });
   F.R.forEach(q=>{ g.globalAlpha=1-q.l; g.strokeStyle=q.c; g.lineWidth=4*(1-q.l)+1; g.beginPath(); g.arc(q.x,q.y,q.m*q.l,0,7); g.stroke(); });
   g.globalAlpha=1; g.globalCompositeOperation='source-over';
   F.T.forEach(q=>{ g.globalAlpha=Math.max(0,1-q.l/1.1); g.font='900 '+q.z+'px system-ui,sans-serif'; g.textAlign='center'; g.lineWidth=4; g.strokeStyle='rgba(0,0,0,.6)'; g.strokeText(q.s,q.x,q.y); g.fillStyle=q.c; g.fillText(q.s,q.x,q.y); }); g.globalAlpha=1;
   g.restore();
   if(F.flash>0){ g.fillStyle='rgba(255,240,200,'+(F.flash*.55)+')'; g.fillRect(0,0,W,H); F.flash=Math.max(0,F.flash-dt*2.5); }
   /* the HUD strip and the cannon meter */
   g.fillStyle='rgba(2,4,16,.62)'; g.fillRect(0,0,W,26); g.fillStyle='#ffe94a'; g.font='800 14px system-ui,sans-serif'; g.textAlign='left'; g.textBaseline='alphabetic'; g.fillText((o.hud?o.hud(F):'Score '+F.score.toLocaleString())+'  ·  best '+F.best.toLocaleString(),10,18);
   if(F.cannon){ const mw=Math.min(150,W*.22), mx=W-mw-12, full=F.charge>=1; g.fillStyle='rgba(255,255,255,.12)'; rrect(g,mx,7,mw,12,6); g.fill(); const gr=g.createLinearGradient(mx,0,mx+mw,0); gr.addColorStop(0,'#ff4f6d'); gr.addColorStop(1,'#ffe94a'); g.fillStyle=gr; rrect(g,mx,7,Math.max(12,mw*F.charge),12,6); g.fill(); g.fillStyle=full?(Math.sin(F.t*10)>0?'#fff':'#ffe94a'):'#fff'; g.font='900 11px system-ui,sans-serif'; g.textAlign='right'; g.fillText(full?'💥 FIRE · C':'💥 '+Math.round(F.charge*100)+'%',mx-6,18); }
   if(!F.running||F.paused||F.over){ g.fillStyle='rgba(4,3,20,.74)'; g.fillRect(0,H/2-58,W,116); const tg=g.createLinearGradient(W/2-200,0,W/2+200,0); tg.addColorStop(0,'#6fe8ff'); tg.addColorStop(.5,'#ff7ad9'); tg.addColorStop(1,'#ffe94a'); g.fillStyle=tg; g.textAlign='center'; g.font='900 '+Math.min(34,W/16)+'px system-ui,sans-serif'; g.fillText(F.over?'GAME OVER · '+F.score.toLocaleString():F.paused?'PAUSED':o.title.toUpperCase(),W/2,H/2-8); g.font='600 15px system-ui,sans-serif'; g.fillStyle='#ffe94a'; g.fillText(F.over?'Tap here or ↺ Restart to play again':F.paused?'Press ▶ Resume or P':(o.sub||'Tap here or press ▶ Start'),W/2,H/2+24); }
  });
  ctx.status(o.hint||'Press ▶ Start.');
  return F; }
 /* the frame's buttons and touch pad, one look for every Pro Arcade game */
 const css=document.createElement('style'); css.textContent=`
.kProBar button.on{background:#ffe94a!important;color:#14163a!important}
.kProPad{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0 0;user-select:none;-webkit-user-select:none}
.kProPad button{min-width:58px;min-height:52px;border-radius:14px;font:900 15px system-ui,sans-serif;touch-action:none;background:linear-gradient(180deg,#1d2458,#0c1030);color:#fff;border:1px solid #4a56a8}
.kProPad button:active{background:#ffe94a;color:#14163a}`; document.head.appendChild(css);
 window.KPRO={frame,rrect,reg,rnd,rr,cl,getLS,putLS};

 /* ================= 1 · PRISM CRUSH ================= */
 const GEMC=[['#ff3b6b','#ff9fb5'],['#ffb020','#ffe08a'],['#3dff8b','#b6ffd2'],['#2fa8ff','#a9dcff'],['#b45bff','#e0b8ff'],['#ffe94a','#fff7b8']];
 function gemSprite(t,s){ const d=Math.min(window.devicePixelRatio||1,2); const c=document.createElement('canvas'); c.width=c.height=Math.ceil(s*d); const g=c.getContext('2d'); g.scale(d,d); const m=s/2, r=s*.4;
  const [a,b]=GEMC[t]; g.shadowColor=a; g.shadowBlur=s*.18; const gr=g.createRadialGradient(m-r*.35,m-r*.4,r*.1,m,m,r*1.1); gr.addColorStop(0,b); gr.addColorStop(.45,a); gr.addColorStop(1,'#1a0830'); g.fillStyle=gr; g.beginPath();
  const poly=(n,rot,rad)=>{ for(let i=0;i<n;i++){ const an=rot+i*Math.PI*2/n; const x=m+Math.cos(an)*rad, y=m+Math.sin(an)*rad; i?g.lineTo(x,y):g.moveTo(x,y); } g.closePath(); };
  if(t===0) poly(6,Math.PI/6,r); else if(t===1) poly(4,0,r*1.08); else if(t===2) g.arc(m,m,r*.95,0,7); else if(t===3) poly(3,-Math.PI/2,r*1.12); else if(t===4) rrect(g,m-r*.85,m-r*.85,r*1.7,r*1.7,r*.35); else { for(let i=0;i<10;i++){ const an=-Math.PI/2+i*Math.PI/5, rad=i%2?r*.48:r*1.05; const x=m+Math.cos(an)*rad, y=m+Math.sin(an)*rad; i?g.lineTo(x,y):g.moveTo(x,y); } g.closePath(); }
  g.fill(); g.shadowBlur=0; g.strokeStyle='rgba(255,255,255,.55)'; g.lineWidth=1.4; g.stroke();
  g.globalCompositeOperation='lighter'; const hl=g.createRadialGradient(m-r*.35,m-r*.45,0,m-r*.35,m-r*.45,r*.6); hl.addColorStop(0,'rgba(255,255,255,.85)'); hl.addColorStop(1,'rgba(255,255,255,0)'); g.fillStyle=hl; g.beginPath(); g.arc(m-r*.3,m-r*.4,r*.55,0,7); g.fill();
  g.strokeStyle='rgba(255,255,255,.22)'; g.lineWidth=1; g.beginPath(); g.moveTo(m-r*.6,m+r*.1); g.lineTo(m,m-r*.6); g.lineTo(m+r*.6,m+r*.1); g.stroke(); return c; }
 reg('pro_prism','Prism Crush','🚀 Pro Arcade · match three. Swap two gems side by side to line up three or more of one colour. Four in a row makes a line gem (clears its row or column), an L or T makes a nova (clears a 3 × 3 square), five in a row makes a prism (swap it with a gem to clear every gem of that colour). Cascades multiply the score. Reach the target score in the moves you have to clear the level. Drag or tap two gems; keys: arrows move, Space picks. 💥 Cannon on: a full charge fires a cross blast through the busiest spot on the board.',ctx=>{
  const N=8; let B=[], cs=40, ox=0, oy=30, sprites=null, spSize=0, state='idle', anim=0, sel=null, cur={r:3,c:3}, swapA=null, swapB=null, chain=1, level=1, moves=20, target=3000, drag=null, uid=1, hintT=0, hint=null, toClear=new Set(), make=[];
  const cell=(r,c)=>(r>=0&&r<N&&c>=0&&c<N)?B[r][c]:null;
  const newGem=t=>({t:t==null?rnd(6):t,s:0,y:0,k:uid++,pop:0});
  function layout(F){ cs=Math.floor(Math.min((F.W-24)/N,(F.H-44)/N)); ox=Math.round((F.W-cs*N)/2); oy=Math.round(30+(F.H-30-cs*N)/2); if(spSize!==cs){ spSize=cs; sprites=GEMC.map((_,t)=>gemSprite(t,cs)); } }
  function fill(){ B=[]; for(let r=0;r<N;r++){ B.push([]); for(let c=0;c<N;c++){ let t; do{ t=rnd(6); }while((c>=2&&B[r][c-1].t===t&&B[r][c-2].t===t)||(r>=2&&B[r-1][c].t===t&&B[r-2][c].t===t)); B[r].push(newGem(t)); } } if(!anyMove()) fill(); }
  function runs(){ const R=[]; for(let r=0;r<N;r++){ let c=0; while(c<N){ const t=B[r][c].t; let e=c; while(e+1<N&&B[r][e+1].t===t&&t>=0) e++; if(e-c>=2&&t>=0) R.push({d:'h',r,c,len:e-c+1}); c=e+1; } }
   for(let c=0;c<N;c++){ let r=0; while(r<N){ const t=B[r][c].t; let e=r; while(e+1<N&&B[e+1][c].t===t&&t>=0) e++; if(e-r>=2&&t>=0) R.push({d:'v',r,c,len:e-r+1}); r=e+1; } } return R; }
  function anyMove(){ for(let r=0;r<N;r++) for(let c=0;c<N;c++){ for(const [dr,dc] of [[0,1],[1,0]]){ const r2=r+dr,c2=c+dc; if(r2>=N||c2>=N) continue; if(B[r][c].s==='p'||B[r2][c2].s==='p') return [[r,c],[r2,c2]]; swp(r,c,r2,c2); const ok=runs().length>0; swp(r,c,r2,c2); if(ok) return [[r,c],[r2,c2]]; } } return null; }
  function swp(r,c,r2,c2){ const t=B[r][c]; B[r][c]=B[r2][c2]; B[r2][c2]=t; }
  const key=(r,c)=>r*N+c;
  /* what a cleared special takes with it */
  function blast(F,r,c,seen){ const gm=B[r][c]; if(!gm||seen.has(key(r,c))) return; seen.add(key(r,c)); toClear.add(key(r,c));
   if(gm.s==='h'){ for(let x=0;x<N;x++) blast(F,r,x,seen); F.ring(ox+c*cs+cs/2,oy+r*cs+cs/2,'#ffe94a',cs*N); F.snd(880,.08); }
   else if(gm.s==='v'){ for(let y=0;y<N;y++) blast(F,y,c,seen); F.ring(ox+c*cs+cs/2,oy+r*cs+cs/2,'#6fe8ff',cs*N); F.snd(880,.08); }
   else if(gm.s==='b'){ for(let y=r-1;y<=r+1;y++) for(let x=c-1;x<=c+1;x++) if(cell(y,x)) blast(F,y,x,seen); F.ring(ox+c*cs+cs/2,oy+r*cs+cs/2,'#ff7ad9',cs*2.5); F.shake=6; F.snd(140,.18); }
   else if(gm.s==='p'){ const col=rnd(6); for(let y=0;y<N;y++) for(let x=0;x<N;x++) if(B[y][x].t===col) blast(F,y,x,seen); F.ring(ox+c*cs+cs/2,oy+r*cs+cs/2,'#ffffff',cs*N); F.flash=.4; F.snd(1200,.2); } }
  function resolve(F,swapCells){ const R=runs(); if(!R.length) return false; toClear=new Set(); make=[]; const inH=new Map(), inV=new Map();
   R.forEach(run=>{ for(let i=0;i<run.len;i++){ const r=run.d==='h'?run.r:run.r+i, c=run.d==='h'?run.c+i:run.c; (run.d==='h'?inH:inV).set(key(r,c),run); } });
   const seen=new Set(); R.forEach(run=>{ const cells=[]; for(let i=0;i<run.len;i++) cells.push(run.d==='h'?[run.r,run.c+i]:[run.r+i,run.c]);
    let at=cells[Math.floor(cells.length/2)]; if(swapCells) for(const sc of swapCells) if(cells.some(x=>x[0]===sc[0]&&x[1]===sc[1])) at=sc;
    if(run.len>=5) make.push({r:at[0],c:at[1],s:'p',t:-1}); else if(run.len===4) make.push({r:at[0],c:at[1],s:run.d==='h'?'v':'h',t:B[at[0]][at[1]].t});
    cells.forEach(([r,c])=>blast(F,r,c,seen)); });
   inH.forEach((run,k)=>{ if(inV.has(k)&&run.len<5&&inV.get(k).len<5){ const r=Math.floor(k/N), c=k%N; if(!make.some(m=>m.r===r&&m.c===c)) make.push({r,c,s:'b',t:B[r][c].t}); } });
   const pts=toClear.size*60*chain+make.length*200; F.add(pts); F.feed(toClear.size*.012);
   toClear.forEach(k=>{ const r=Math.floor(k/N), c=k%N; const gm=B[r][c]; if(gm){ gm.pop=0.0001; F.burst(ox+c*cs+cs/2,oy+r*cs+cs/2,GEMC[Math.max(0,gm.t)][0],7,160,.5); } });
   const cx=[...toClear].reduce((a,k)=>a+(k%N),0)/toClear.size, cy=[...toClear].reduce((a,k)=>a+Math.floor(k/N),0)/toClear.size;
   F.text(ox+cx*cs+cs/2,oy+cy*cs+cs/2,'+'+pts+(chain>1?'  ×'+chain:''),chain>1?'#ffe94a':'#fff',chain>1?22:18); F.snd(520+chain*90,.06);
   state='clear'; anim=0; return true; }
  function collapse(){ make.forEach(m=>{ toClear.delete(key(m.r,m.c)); const gm=B[m.r][m.c]; gm.s=m.s; gm.pop=0; if(m.s==='p') gm.t=-1; else gm.t=m.t; });
   for(let c=0;c<N;c++){ const keep=[]; for(let r=N-1;r>=0;r--) if(!toClear.has(key(r,c))) keep.push({gm:B[r][c],from:r}); let r=N-1; keep.forEach(({gm,from})=>{ gm.y+=(r-from)*cs; B[r][c]=gm; r--; }); const cnt=r+1; while(r>=0){ const gm=newGem(); gm.y=cnt*cs; B[r][c]=gm; r--; } }
   for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const gm=B[r][c]; if(gm.y<0) gm.y=0; }
   toClear=new Set(); make=[]; state='fall'; }
  function trySwap(F,a,b){ if(state!=='idle'||!a||!b) return; if(Math.abs(a.r-b.r)+Math.abs(a.c-b.c)!==1) return; sel=null; hint=null; hintT=0;
   const A=B[a.r][a.c], Bb=B[b.r][b.c];
   if(A.s==='p'||Bb.s==='p'){ /* a prism swapped with a gem clears that whole colour */ moves--; const pr=A.s==='p'?a:b, ot=A.s==='p'?b:a; const col=B[ot.r][ot.c].t; toClear=new Set(); make=[]; const seen=new Set(); seen.add(key(pr.r,pr.c)); toClear.add(key(pr.r,pr.c));
    for(let y=0;y<N;y++) for(let x=0;x<N;x++) if(B[y][x].t===col||(col<0)) blast(F,y,x,seen); toClear.forEach(k=>{ const gm=B[Math.floor(k/N)][k%N]; gm.pop=.0001; F.burst(ox+(k%N)*cs+cs/2,oy+Math.floor(k/N)*cs+cs/2,GEMC[Math.max(0,gm.t)][0],6,180,.5); });
    F.add(toClear.size*90); F.feed(.15); F.flash=.5; F.ring(ox+pr.c*cs+cs/2,oy+pr.r*cs+cs/2,'#fff',cs*N); F.snd(1300,.25); state='clear'; anim=0; chain=1; return; }
   swapA=a; swapB=b; state='swap'; anim=0; }
  function hitCell(x,y){ const c=Math.floor((x-ox)/cs), r=Math.floor((y-oy)/cs); return (r>=0&&r<N&&c>=0&&c<N)?{r,c}:null; }
  function cannon(F){ /* a cross blast through the busiest spot: the row and column with the most gems of one colour */ let best=null; for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const t=B[r][c].t; let n=0; for(let x=0;x<N;x++) if(B[r][x].t===t) n++; for(let y=0;y<N;y++) if(B[y][c].t===t) n++; if(!best||n>best.n) best={r,c,n}; }
   if(state!=='idle'||!best) return; toClear=new Set(); make=[]; const seen=new Set(); for(let x=0;x<N;x++) blast(F,best.r,x,seen); for(let y=0;y<N;y++) blast(F,y,best.c,seen);
   toClear.forEach(k=>{ const gm=B[Math.floor(k/N)][k%N]; gm.pop=.0001; F.burst(ox+(k%N)*cs+cs/2,oy+Math.floor(k/N)*cs+cs/2,'#ffe94a',8,240,.6); }); F.add(toClear.size*80); F.ring(ox+best.c*cs+cs/2,oy+best.r*cs+cs/2,'#ffe94a',cs*N*1.2); F.text(F.W/2,oy+cs,'💥 CANNON CROSS','#ffe94a',26); chain=1; state='clear'; anim=0; }
  let F; F=KPRO.frame(ctx,'pro_prism',{title:'Prism Crush',ratio:.92,maxW:640,hFrac:.72,charge:.0002,cannonHelp:'A full charge fires a cross blast through the busiest spot.',hint:'Swap two gems side by side to line up three. Press ▶ Start.',go:'Swap two gems side by side to line up three or more.',
   reset(F){ level=1; moves=20; target=3000; chain=1; state='idle'; sel=null; layout(F); fill(); },
   hud:F=>'Level '+level+' · '+F.score.toLocaleString()+' / '+target.toLocaleString()+' · moves '+moves,
   cannon:F=>cannon(F),
   buttons:F=>[['🔀 Shuffle',()=>{ if(state!=='idle') return; fill(); F.text(F.W/2,F.H/2,'Shuffled','#6fe8ff',24); }],['💡 Hint',()=>{ hint=anyMove(); hintT=0; }]],
   pointer(F,t,x,y){ const hc=hitCell(x,y); if(t==='down'){ if(!hc) return; if(sel&&Math.abs(sel.r-hc.r)+Math.abs(sel.c-hc.c)===1){ trySwap(F,sel,hc); sel=null; return; } sel=hc; drag={x,y,from:hc}; F.snd(660,.03); }
    else if(t==='move'&&drag&&F.down){ const dx=x-drag.x, dy=y-drag.y; if(Math.max(Math.abs(dx),Math.abs(dy))>cs*.45){ const to=Math.abs(dx)>Math.abs(dy)?{r:drag.from.r,c:drag.from.c+Math.sign(dx)}:{r:drag.from.r+Math.sign(dy),c:drag.from.c}; if(cell(to.r,to.c)) trySwap(F,drag.from,to); drag=null; } }
    else if(t==='up') drag=null; },
   key(F,e,down){ if(!down) return false; const k=e.key; const mv={ArrowLeft:[0,-1],ArrowRight:[0,1],ArrowUp:[-1,0],ArrowDown:[1,0]}[k]; if(mv){ cur={r:cl(cur.r+mv[0],0,N-1),c:cl(cur.c+mv[1],0,N-1)}; return true; } if(k===' '||k==='Enter'){ if(sel&&Math.abs(sel.r-cur.r)+Math.abs(sel.c-cur.c)===1){ trySwap(F,sel,{...cur}); sel=null; } else sel={...cur}; return true; } return false; },
   update(F,dt){ layout(F); hintT+=dt; if(hintT>8&&state==='idle'&&!hint) hint=anyMove();
    if(state==='swap'||state==='back'){ anim+=dt*6; if(anim>=1){ swp(swapA.r,swapA.c,swapB.r,swapB.c); if(state==='swap'){ chain=1; if(resolve(F,[[swapA.r,swapA.c],[swapB.r,swapB.c]])){ moves--; } else { state='back'; anim=0; F.snd(200,.06); return; } } else state='idle'; } }
    else if(state==='clear'){ anim+=dt*5; B.forEach(row=>row.forEach(gm=>{ if(gm.pop) gm.pop=Math.min(1,anim); })); if(anim>=1) collapse(); }
    else if(state==='fall'){ let moving=false; B.forEach(row=>row.forEach(gm=>{ if(gm.y>0){ gm.y=Math.max(0,gm.y-dt*cs*14); moving=true; } })); if(!moving){ chain++; if(!resolve(F,null)){ chain=1; state='idle'; if(F.score>=target){ level++; F.text(F.W/2,F.H/2,'LEVEL '+level,'#7cff8a',34); F.add(moves*150); F.snd(990,.2); moves=20+Math.min(10,level); target=Math.round(F.score+2500+level*1500); }
       else if(moves<=0) F.end('Out of moves on level '+level+'.'); else if(!anyMove()){ fill(); F.text(F.W/2,F.H/2,'No moves left · new board','#6fe8ff',20); } } } } },
   draw(F,dt){ const g=F.g; layout(F); const bg=g.createLinearGradient(0,0,0,F.H); bg.addColorStop(0,'#160a3a'); bg.addColorStop(1,'#03010d'); g.fillStyle=bg; g.fillRect(0,0,F.W,F.H);
    for(let i=0;i<40;i++){ const x=(i*97.3+F.t*8*(1+i%3))%F.W, y=(i*61.7)%F.H; g.fillStyle='rgba(180,200,255,'+(.15+(i%5)*.08)+')'; g.fillRect(x,y,1.6,1.6); }
    g.save(); rrect(g,ox-8,oy-8,cs*N+16,cs*N+16,16); g.fillStyle='rgba(20,16,60,.75)'; g.fill(); g.strokeStyle='rgba(140,170,255,.45)'; g.lineWidth=2; g.stroke(); g.restore();
    for(let r=0;r<N;r++) for(let c=0;c<N;c++){ g.fillStyle=(r+c)%2?'rgba(255,255,255,.035)':'rgba(255,255,255,.07)'; g.fillRect(ox+c*cs+1,oy+r*cs+1,cs-2,cs-2); }
    const sw=(state==='swap'||state==='back')?Math.sin(Math.min(1,anim)*Math.PI/2):0;
    for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const gm=B[r][c]; if(!gm) continue; let x=ox+c*cs, y=oy+r*cs-gm.y;
     if(sw&&swapA&&swapB){ const isA=r===swapA.r&&c===swapA.c, isB=r===swapB.r&&c===swapB.c; const f=state==='swap'?sw:1-sw; if(isA){ x+=(swapB.c-swapA.c)*cs*f; y+=(swapB.r-swapA.r)*cs*f; } if(isB){ x+=(swapA.c-swapB.c)*cs*f; y+=(swapA.r-swapB.r)*cs*f; } }
     if(y<oy-cs) continue; const sc=gm.pop?1-gm.pop:1+(sel&&sel.r===r&&sel.c===c?Math.sin(F.t*10)*.06+.04:0); if(sc<=0) continue;
     g.save(); g.translate(x+cs/2,y+cs/2); g.scale(sc,sc); if(gm.s==='p'){ const hue=(F.t*120)%360; const pg=g.createRadialGradient(0,0,2,0,0,cs*.42); pg.addColorStop(0,'#fff'); pg.addColorStop(.5,'hsl('+hue+',100%,65%)'); pg.addColorStop(1,'hsl('+((hue+180)%360)+',100%,40%)'); g.fillStyle=pg; g.beginPath(); g.arc(0,0,cs*.4,0,7); g.fill(); g.strokeStyle='#fff'; g.lineWidth=2; g.stroke(); }
     else g.drawImage(sprites[gm.t],-cs/2,-cs/2,cs,cs);
     if(gm.s==='h'||gm.s==='v'){ g.strokeStyle='rgba(255,255,255,.9)'; g.lineWidth=2.5; for(let k=-1;k<=1;k++){ g.beginPath(); if(gm.s==='h'){ g.moveTo(-cs*.3,k*cs*.13); g.lineTo(cs*.3,k*cs*.13); } else { g.moveTo(k*cs*.13,-cs*.3); g.lineTo(k*cs*.13,cs*.3); } g.stroke(); } }
     if(gm.s==='b'){ g.strokeStyle='#fff'; g.lineWidth=2.5; g.beginPath(); g.arc(0,0,cs*.32+Math.sin(F.t*8)*2,0,7); g.stroke(); g.fillStyle='#fff'; g.beginPath(); g.arc(0,0,cs*.08,0,7); g.fill(); }
     g.restore(); }
    if(hint&&state==='idle'){ const a=.5+.5*Math.sin(F.t*6); g.strokeStyle='rgba(255,233,74,'+a+')'; g.lineWidth=3; hint.forEach(([r,c])=>{ rrect(g,ox+c*cs+3,oy+r*cs+3,cs-6,cs-6,8); g.stroke(); }); }
    g.strokeStyle='rgba(111,232,255,.9)'; g.lineWidth=2; rrect(g,ox+cur.c*cs+2,oy+cur.r*cs+2,cs-4,cs-4,8); g.stroke();
    if(sel){ g.strokeStyle='#fff'; g.lineWidth=3; rrect(g,ox+sel.c*cs+1,oy+sel.r*cs+1,cs-2,cs-2,9); g.stroke(); } } });
  return {state:()=>({level,moves,target,score:F.score,state,charge:F.charge}),F};
 });

 /* ================= 2 · NEON LABYRINTH ================= */
 const MAZE=[
  '#####################',
  '#.........#.........#',
  '#o###.###.#.###.###o#',
  '#...................#',
  '#.###.#.#####.#.###.#',
  '#.....#...#...#.....#',
  '#####.###.#.###.#####',
  '    #.#.......#.#    ',
  '#####.#.##-##.#.#####',
  'T.......#HHH#.......T',
  '#####.#.#####.#.#####',
  '    #.#.......#.#    ',
  '#####.#.#####.#.#####',
  '#.........#.........#',
  '#.###.###.#.###.###.#',
  '#o..#.....P.....#..o#',
  '###.#.#.#####.#.#.###',
  '#.....#...#...#.....#',
  '#.#######.#.#######.#',
  '#...................#',
  '#####################'];
 reg('pro_maze','Neon Labyrinth','🚀 Pro Arcade · maze chase. Steer the comet through the maze and collect every spark. Four sentinels hunt you, each its own way: the Hunter goes straight for you, the Flanker for where you are heading, the Warden guards its corner until you come near, the Drifter turns at random. A power core glitches them for a few seconds: touch one then to send it home for points. Clear the maze for the next level; three lives. Arrows or W A S D, or swipe. 💥 Cannon on: a full charge fires an EMP that freezes every sentinel and sweeps up the sparks around you.',ctx=>{
  const Rw=MAZE.length, Cw=MAZE[0].length; let G=[], dots=0, cs=20, ox=0, oy=30, P={}, S=[], lives=3, level=1, fright=0, frightMax=7, mode='scatter', modeT=0, wall=null, wallSize=0, eaten=0, deathT=0, trail=[];
  const open=(r,c)=>{ if(c<0||c>=Cw) return r===9; const ch=G[r]&&G[r][c]; return ch!=='#'&&ch!==' '&&ch!=='-'; };
  const openS=(r,c,s)=>{ if(c<0||c>=Cw) return r===9; const ch=G[r]&&G[r][c]; if(ch==='-') return s.st==='exit'||s.st==='home'||s.st==='eyes'; return ch!=='#'&&ch!==' '; };
  const DIRS=[[0,-1,'ArrowLeft'],[0,1,'ArrowRight'],[-1,0,'ArrowUp'],[1,0,'ArrowDown']];
  const NAMES=[['Hunter','#ff3b6b'],['Flanker','#ff9a3c'],['Warden','#6fe8ff'],['Drifter','#c38bff']];
  function load(){ G=MAZE.map(r=>r.split('')); dots=0; for(let r=0;r<Rw;r++) for(let c=0;c<Cw;c++){ if(G[r][c]==='.'||G[r][c]==='o') dots++; if(G[r][c]==='P'){ G[r][c]=' '; G[r][c]='_'; } if(G[r][c]==='H') G[r][c]='h'; if(G[r][c]==='T') G[r][c]='_'; } wall=null; }
  function spawn(){ P={r:15,c:10,x:10,y:15,d:[0,0],nd:[0,-1],sp:6.2+level*.25};
   S=NAMES.map(([n,col],i)=>({n,col,i,r:9,c:9+Math.min(i,2),x:9+Math.min(i,2),y:9,d:[0,0],st:i===0?'exit':'home',wait:i*2.2,sp:5.2+level*.3,fz:0})); fright=0; mode='scatter'; modeT=0; trail=[]; }
  function layout(F){ cs=Math.floor(Math.min((F.W-16)/Cw,(F.H-36)/Rw)); ox=Math.round((F.W-cs*Cw)/2); oy=Math.round(30+(F.H-30-cs*Rw)/2); }
  function buildWall(F){ const d=Math.min(window.devicePixelRatio||1,2); const c=document.createElement('canvas'); c.width=Math.ceil(cs*Cw*d); c.height=Math.ceil(cs*Rw*d); const g=c.getContext('2d'); g.scale(d,d);
   g.lineCap='round'; for(const [lw,blur,col] of [[6,14,'rgba(47,168,255,.55)'],[2.4,6,'#6fe8ff']]){ g.strokeStyle=col; g.lineWidth=lw; g.shadowColor='#2fa8ff'; g.shadowBlur=blur; g.beginPath();
    for(let r=0;r<Rw;r++) for(let cc=0;cc<Cw;cc++){ const ch=G[r][cc]; if(ch!=='#') continue; const x=cc*cs, y=r*cs; const op=(rr,c2)=>{ const k=G[rr]&&G[rr][c2]; return k!==undefined&&k!=='#'&&k!==' '; };
     if(op(r-1,cc)){ g.moveTo(x+2,y+2); g.lineTo(x+cs-2,y+2); } if(op(r+1,cc)){ g.moveTo(x+2,y+cs-2); g.lineTo(x+cs-2,y+cs-2); } if(op(r,cc-1)){ g.moveTo(x+2,y+2); g.lineTo(x+2,y+cs-2); } if(op(r,cc+1)){ g.moveTo(x+cs-2,y+2); g.lineTo(x+cs-2,y+cs-2); } } g.stroke(); }
   g.shadowBlur=0; for(let r=0;r<Rw;r++) for(let cc=0;cc<Cw;cc++) if(G[r][cc]==='-'){ g.fillStyle='#ff7ad9'; g.fillRect(cc*cs+2,r*cs+cs/2-2,cs-4,4); }
   wall=c; wallSize=cs; }
  /* a sentinel's target, each its own way */
  function targetOf(s){ if(s.st==='eyes'||s.st==='home') return [9,10]; if(s.st==='exit') return [7,10];
   if(mode==='scatter') return [[-2,Cw-2],[-2,1],[Rw+1,Cw-1],[Rw+1,0]][s.i];
   if(s.i===0) return [P.r,P.c]; if(s.i===1) return [P.r+P.d[0]*4,P.c+P.d[1]*4];
   if(s.i===2){ const dd=Math.hypot(s.r-P.r,s.c-P.c); return dd<7?[P.r,P.c]:[Rw-2,Cw-2]; } return [rnd(Rw),rnd(Cw)]; }
  function stepEntity(e,sp,dt,choose){ const tx=e.c+e.d[1], ty=e.r+e.d[0]; let moveLeft=sp*dt;
   while(moveLeft>0){ const atX=Math.abs(e.x-e.c)<1e-6&&Math.abs(e.y-e.r)<1e-6; if(atX){ const nd=choose(e); e.d=nd||[0,0]; if(!nd) return; }
    const goalC=e.c+e.d[1], goalR=e.r+e.d[0]; const dx=goalC-e.x, dy=goalR-e.y; const dist=Math.abs(dx)+Math.abs(dy); if(dist<=moveLeft){ e.x=goalC; e.y=goalR; moveLeft-=dist; e.c=goalC; e.r=goalR; if(e.c<0){ e.c=Cw-1; e.x=Cw-1; } if(e.c>=Cw){ e.c=0; e.x=0; } } else { e.x+=Math.sign(dx)*moveLeft; e.y+=Math.sign(dy)*moveLeft; moveLeft=0; } } }
  /* turning back halfway between two cells heads for the cell just left */
  function reverse(e){ const atX=Math.abs(e.x-e.c)<1e-6&&Math.abs(e.y-e.r)<1e-6; if(!atX&&(e.d[0]||e.d[1])){ e.c+=e.d[1]; e.r+=e.d[0]; } e.d=[-e.d[0],-e.d[1]]; }
  function playerChoose(e){ if(open(e.r+P.nd[0],e.c+P.nd[1])) return P.nd; if(open(e.r+e.d[0],e.c+e.d[1])&&(e.d[0]||e.d[1])) return e.d; return null; }
  function sentChoose(s){ const [tr,tc]=targetOf(s); let best=null, bd=1e9; const opts=DIRS.filter(([dr,dc])=>openS(s.r+dr,s.c+dc,s)&&!(dr===-s.d[0]&&dc===-s.d[1]&&(s.d[0]||s.d[1])));
   const pool=opts.length?opts:DIRS.filter(([dr,dc])=>openS(s.r+dr,s.c+dc,s)); if(!pool.length) return null;
   if((fright>0&&s.st==='chase')||(s.i===3&&s.st==='chase'&&mode==='chase'&&Math.random()<.5)) { const p=pool[rnd(pool.length)]; return [p[0],p[1]]; }
   pool.forEach(([dr,dc])=>{ const d2=(s.r+dr-tr)**2+(s.c+dc-tc)**2; if(d2<bd){ bd=d2; best=[dr,dc]; } }); return best; }
  function die(F){ lives--; deathT=1.4; F.burst(ox+P.x*cs+cs/2,oy+P.y*cs+cs/2,'#ffe94a',40,220,1); F.shake=10; F.snd(120,.4); if(lives<=0){ setTimeout(()=>F.end('The sentinels caught the comet on level '+level+'.'),600); } }
  let F; F=KPRO.frame(ctx,'pro_maze',{title:'Neon Labyrinth',ratio:1,maxW:620,hFrac:.74,charge:.002,cannonHelp:'A full charge fires an EMP: every sentinel freezes and the sparks around you are swept up.',hint:'Collect every spark; a power core lets you send the sentinels home. Press ▶ Start.',go:'Arrows, W A S D or swipe to steer.',
   pad:[['◀','ArrowLeft'],['▲','ArrowUp'],['▼','ArrowDown'],['▶','ArrowRight']],
   reset(F){ lives=3; level=1; load(); spawn(); deathT=0; },
   hud:F=>'Level '+level+' · '+F.score.toLocaleString()+' · '+'❤'.repeat(Math.max(0,lives))+' · sparks '+dots,
   cannon(F){ S.forEach(s=>{ if(s.st==='chase'){ s.fz=3; } }); fright=Math.max(fright,3+frightMax*.5); let n=0; for(let r=P.r-3;r<=P.r+3;r++) for(let c=P.c-3;c<=P.c+3;c++){ if(G[r]&&(G[r][c]==='.'||G[r][c]==='o')){ G[r][c]='_'; dots--; n++; } } F.add(n*10); F.ring(ox+P.x*cs+cs/2,oy+P.y*cs+cs/2,'#6fe8ff',cs*8); F.text(F.W/2,oy+cs*2,'💥 EMP','#6fe8ff',28); if(dots<=0) nextLevel(F); },
   key(F,e,down){ if(!down) return false; const k=e.key.length===1?e.key.toLowerCase():e.key; const m={ArrowLeft:[0,-1],a:[0,-1],ArrowRight:[0,1],d:[0,1],ArrowUp:[-1,0],w:[-1,0],ArrowDown:[1,0],s:[1,0]}[k]; if(m){ P.nd=m; return true; } return false; },
   pointer(F,t,x,y){ if(t==='down'){ F.sw={x,y}; } else if((t==='move'||t==='up')&&F.sw){ const dx=x-F.sw.x, dy=y-F.sw.y; if(Math.max(Math.abs(dx),Math.abs(dy))>18){ P.nd=Math.abs(dx)>Math.abs(dy)?[0,Math.sign(dx)]:[Math.sign(dy),0]; F.sw={x,y}; } if(t==='up') F.sw=null; } },
   update(F,dt){ layout(F); if(deathT>0){ deathT-=dt; if(deathT<=0&&lives>0) spawn(); return; }
    modeT+=dt; if(fright<=0){ const cyc=mode==='scatter'?7:20; if(modeT>cyc){ mode=mode==='scatter'?'chase':'scatter'; modeT=0; S.forEach(s=>{ if(s.st==='chase') reverse(s); }); } } else fright-=dt;
    if((P.d[0]||P.d[1])&&P.nd[0]===-P.d[0]&&P.nd[1]===-P.d[1]) reverse(P);
    stepEntity(P,P.sp,dt,playerChoose); trail.unshift([P.x,P.y]); if(trail.length>14) trail.pop();
    const ch=G[P.r]&&G[P.r][P.c]; if(ch==='.'){ G[P.r][P.c]='_'; dots--; F.add(10); F.feed(.004); if(dots%2===0) F.snd(880,.02); } else if(ch==='o'){ G[P.r][P.c]='_'; dots--; F.add(50); fright=frightMax-Math.min(4,level*.4); eaten=0; S.forEach(s=>{ if(s.st==='chase') reverse(s); }); F.ring(ox+P.x*cs+cs/2,oy+P.y*cs+cs/2,'#ff7ad9',cs*6); F.snd(330,.15); }
    if(dots<=0){ nextLevel(F); return; }
    S.forEach(s=>{ if(s.fz>0){ s.fz-=dt; return; } if(s.st==='home'){ s.wait-=dt; if(s.wait<=0){ s.st='exit'; } return; }
     const sp=s.st==='eyes'?11:(fright>0&&s.st==='chase'?s.sp*.55:(s.r===9&&(s.c<3||s.c>Cw-4)?s.sp*.5:s.sp));
     stepEntity(s,sp,dt,sentChoose); if(s.st==='exit'&&s.r<=7) s.st='chase'; if(s.st==='eyes'&&s.r===9&&s.c===10){ s.st='exit'; }
     const d=Math.hypot(s.x-P.x,s.y-P.y); if(d<.6&&s.st==='chase'){ if(fright>0){ s.st='eyes'; eaten++; const pts=200*Math.pow(2,eaten-1); F.add(pts); F.feed(.08); F.text(ox+s.x*cs+cs/2,oy+s.y*cs,'+'+pts,s.col,20); F.burst(ox+s.x*cs+cs/2,oy+s.y*cs+cs/2,s.col,20,200,.7); F.snd(1100,.1); } else die(F); } }); },
   draw(F,dt){ const g=F.g; layout(F); const bg=g.createRadialGradient(F.W/2,F.H/2,20,F.W/2,F.H/2,F.W*.8); bg.addColorStop(0,'#0b1440'); bg.addColorStop(1,'#020310'); g.fillStyle=bg; g.fillRect(0,0,F.W,F.H);
    if(!wall||wallSize!==cs) buildWall(F); g.drawImage(wall,ox,oy,cs*Cw,cs*Rw);
    g.globalCompositeOperation='lighter'; for(let r=0;r<Rw;r++) for(let c=0;c<Cw;c++){ const ch=G[r][c]; if(ch==='.'){ g.fillStyle='rgba(255,233,140,.9)'; g.beginPath(); g.arc(ox+c*cs+cs/2,oy+r*cs+cs/2,Math.max(1.6,cs*.09),0,7); g.fill(); } else if(ch==='o'){ const p=.6+.4*Math.sin(F.t*6); const gr=g.createRadialGradient(ox+c*cs+cs/2,oy+r*cs+cs/2,0,ox+c*cs+cs/2,oy+r*cs+cs/2,cs*.55); gr.addColorStop(0,'rgba(255,255,255,'+p+')'); gr.addColorStop(.4,'rgba(255,122,217,'+p+')'); gr.addColorStop(1,'rgba(255,122,217,0)'); g.fillStyle=gr; g.beginPath(); g.arc(ox+c*cs+cs/2,oy+r*cs+cs/2,cs*.55,0,7); g.fill(); } }
    /* the comet and its tail */ if(deathT<=0||Math.sin(F.t*30)>0){ trail.forEach(([x,y],i)=>{ g.fillStyle='rgba(255,200,80,'+(.35*(1-i/trail.length))+')'; g.beginPath(); g.arc(ox+x*cs+cs/2,oy+y*cs+cs/2,cs*.38*(1-i/trail.length),0,7); g.fill(); });
     const px=ox+P.x*cs+cs/2, py=oy+P.y*cs+cs/2; const cg=g.createRadialGradient(px,py,0,px,py,cs*.7); cg.addColorStop(0,'#ffffff'); cg.addColorStop(.35,'#ffe94a'); cg.addColorStop(1,'rgba(255,120,40,0)'); g.fillStyle=cg; g.beginPath(); g.arc(px,py,cs*.7,0,7); g.fill(); }
    g.globalCompositeOperation='source-over';
    S.forEach(s=>{ const x=ox+s.x*cs+cs/2, y=oy+s.y*cs+cs/2, R=cs*.42; g.save(); g.translate(x,y);
     if(s.st==='eyes'){ g.fillStyle='#fff'; g.beginPath(); g.arc(-R*.35,0,R*.25,0,7); g.arc(R*.35,0,R*.25,0,7); g.fill(); g.restore(); return; }
     const glitch=fright>0&&s.st==='chase'; const col=glitch?((fright<2&&Math.sin(F.t*16)>0)?'#ffffff':'#3d5bff'):s.col; g.rotate(Math.sin(F.t*2+s.i)*.25); g.shadowColor=col; g.shadowBlur=s.fz>0?2:14; g.fillStyle=col; g.beginPath();
     const n=[3,4,4,6][s.i], rot=[-Math.PI/2,Math.PI/4,0,0][s.i]; for(let k=0;k<n;k++){ const a=rot+k*Math.PI*2/n; const xx=Math.cos(a)*R*1.05, yy=Math.sin(a)*R*1.05; k?g.lineTo(xx,yy):g.moveTo(xx,yy); } g.closePath(); g.fill(); g.shadowBlur=0;
     g.rotate(-Math.sin(F.t*2+s.i)*.25); g.fillStyle='#fff'; const ex=s.d[1]*R*.18, ey=s.d[0]*R*.18; g.beginPath(); g.arc(-R*.32+ex,-R*.1+ey,R*.2,0,7); g.arc(R*.32+ex,-R*.1+ey,R*.2,0,7); g.fill(); g.fillStyle='#0a0620'; g.beginPath(); g.arc(-R*.32+ex*1.6,-R*.1+ey*1.6,R*.09,0,7); g.arc(R*.32+ex*1.6,-R*.1+ey*1.6,R*.09,0,7); g.fill();
     if(s.fz>0){ g.strokeStyle='rgba(111,232,255,.9)'; g.lineWidth=2; g.strokeRect(-R,-R,R*2,R*2); } g.restore(); }); } });
  function nextLevel(F){ level++; F.add(1000); F.text(F.W/2,F.H/2,'MAZE CLEAR · LEVEL '+level,'#7cff8a',26); F.snd(990,.25); load(); spawn(); }
  return {state:()=>({level,lives,dots,score:F.score,P:{r:P.r,c:P.c},fright}),F};
 });
})();
