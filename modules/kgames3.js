(()=>{ /* MOBILE HITS: our own games in the most-played phone styles, each with a KAN-IN twist.
   Every game shares one frame: how to play, Start, Pause, Restart, score, best score (kept on this device), sound on or off, touch and keys. */
 const CAT='Mobile hits';
 const rnd=n=>Math.floor(Math.random()*n), rr=(a,b)=>a+Math.random()*(b-a), cl=(v,a,b)=>Math.max(a,Math.min(b,v)), pick=a=>a[rnd(a.length)];
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const COL=['#ff4f6d','#ffe94a','#6fe8ff','#7cff8a','#c38bff','#ff9a3c','#ff7ad9'];
 function rrect(g,x,y,w,h,r){ g.beginPath(); g.moveTo(x+r,y); g.arcTo(x+w,y,x+w,y+h,r); g.arcTo(x+w,y+h,x,y+h,r); g.arcTo(x,y+h,x,y,r); g.arcTo(x,y,x+w,y,r); g.closePath(); }
 function frame(ctx,id,o){ const L=GAMES.lib; const W=Math.round(Math.min(ctx.W(),o.maxW||720)); const H=Math.round(Math.min(W*(o.ratio||0.75),Math.max(300,window.innerHeight*0.62))); const B=L.mkCanvas(ctx,W,H); const g=B.g;
  const F={W,H,g,cv:B.cv,score:0,best:getLS('kanin-best-'+id,0),running:false,paused:false,over:false,t:0,keys:{},muted:getLS('kanin-gmute',false),down:false,px:0,py:0};
  F.snd=(f,d)=>{ if(F.muted) return; try{ ctx.beep(f,d||0.05); }catch(_){ } };
  F.add=n=>{ F.score+=n; };
  F.msg=t=>ctx.status(t);
  F.end=m=>{ if(F.over) return; F.over=true; F.running=false; if(F.score>F.best){ F.best=F.score; putLS('kanin-best-'+id,F.best); m+=' A new best!'; } ctx.status(m+' Score '+F.score+' · best '+F.best+'. Press ↺ Restart or tap the board to play again.'); F.snd(160,.25); paint(); };
  F.win=m=>F.end(m||'You won!');
  const reset=()=>{ F.score=0; F.over=false; F.t=0; F.paused=false; o.reset(F); };
  const start=()=>{ if(F.over) reset(); F.running=true; F.paused=false; paint(); ctx.status(o.go||'Go!'); };
  const bar=h('div',{className:'gbar'}); const bStart=h('button',{type:'button'},'▶ Start'); const bRe=h('button',{type:'button'},'↺ Restart'); const bS=h('button',{type:'button','aria-label':'Sound on or off'},F.muted?'🔇 Sound off':'🔊 Sound on');
  bStart.addEventListener('click',()=>{ if(!F.running||F.over) start(); else { F.paused=!F.paused; paint(); ctx.status(F.paused?'Paused. Press ▶ Resume.':'Playing.'); } });
  bRe.addEventListener('click',()=>{ reset(); start(); });
  bS.addEventListener('click',()=>{ F.muted=!F.muted; putLS('kanin-gmute',F.muted); bS.textContent=F.muted?'🔇 Sound off':'🔊 Sound on'; });
  bar.appendChild(bStart); bar.appendChild(bRe); bar.appendChild(bS); (o.buttons?o.buttons(F):[]).forEach(b=>{ const x=h('button',{type:'button'},b[0]); x.addEventListener('click',()=>{ if(!F.running&&!F.over&&!b[2]) start(); b[1](x); }); bar.appendChild(x); }); ctx.area.appendChild(bar);
  function paint(){ bStart.textContent=!F.running||F.over?(F.over?'▶ Play again':'▶ Start'):(F.paused?'▶ Resume':'⏸ Pause'); }
  const pos=e=>{ const r=B.cv.getBoundingClientRect(); return [(e.clientX-r.left)*W/(r.width||1),(e.clientY-r.top)*H/(r.height||1)]; };
  B.cv.style.touchAction='none';
  B.cv.addEventListener('pointerdown',e=>{ if(e.button>0) return; e.preventDefault(); [F.px,F.py]=pos(e); F.down=true; try{ B.cv.setPointerCapture(e.pointerId); }catch(_){ } if(F.over){ reset(); start(); return; } if(!F.running){ start(); if(o.tapStarts===false) return; } if(F.paused) return; o.pointer&&o.pointer(F,'down',F.px,F.py); });
  B.cv.addEventListener('pointermove',e=>{ [F.px,F.py]=pos(e); if(F.running&&!F.paused) o.pointer&&o.pointer(F,'move',F.px,F.py); });
  const up=e=>{ [F.px,F.py]=pos(e); const was=F.down; F.down=false; if(was&&F.running&&!F.paused) o.pointer&&o.pointer(F,'up',F.px,F.py); };
  B.cv.addEventListener('pointerup',up); B.cv.addEventListener('pointercancel',up);
  ctx.key((e,down)=>{ const k=e.key; if(down&&(k==='p'||k==='P')&&F.running){ F.paused=!F.paused; paint(); return true; }
   if(down&&!F.running&&(k===' '||k==='Enter')){ start(); return true; }
   if(F.running&&!F.paused&&o.key){ const r=o.key(F,e,down); if(r) return true; }
   if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown',' '].indexOf(k)>=0){ F.keys[k]=down; return true; } return false; });
  reset();
  ctx.raf(dt=>{ if(F.running&&!F.paused&&!F.over){ F.t+=dt; o.update&&o.update(F,dt); } o.draw(F);
   g.fillStyle='rgba(0,0,0,.45)'; g.fillRect(0,0,W,24); g.fillStyle='#ffe94a'; g.font='bold 14px system-ui,sans-serif'; g.textAlign='left'; g.textBaseline='alphabetic'; g.fillText((o.hud?o.hud(F):'Score '+F.score)+'  ·  best '+F.best,8,17);
   if(!F.running||F.paused||F.over){ g.fillStyle='rgba(6,4,24,.72)'; g.fillRect(0,H/2-46,W,92); g.fillStyle='#fff'; g.textAlign='center'; g.font='bold 20px system-ui,sans-serif'; g.fillText(F.over?'Game over · score '+F.score:F.paused?'Paused':o.title,W/2,H/2-8); g.font='15px system-ui,sans-serif'; g.fillStyle='#ffe94a'; g.fillText(F.over?'Tap here or ↺ Restart to play again':F.paused?'Press ▶ Resume or P':'Tap here or press ▶ Start',W/2,H/2+20); } });
  ctx.status(o.hint||'Press ▶ Start.');
  return F; }
 const h=(t,a,c)=>GAMES.lib.h(t,a,c);
 function reg(id,name,how,init){ const go=()=>{ if(!window.GAMES||!GAMES.reg||!GAMES.lib) return false; GAMES.reg(id,name,CAT,how,init); return true; }; if(!go()){ let n=0; const t=setInterval(()=>{ if(go()||++n>40) clearInterval(t); },500); } }

 /* 1 · GEM CANNON: match three, with line blasts and compass bombs */
 reg('m_gems','Gem Cannon','Swap two side-by-side gems to line up three or more of a kind. Four in a row makes a line blaster; five makes a compass bomb that clears every gem of one colour. Reach the target score before your moves run out to go up a level. Tap a gem, then the one next to it (or swipe). Keys: arrows move, Space picks and swaps.',ctx=>{
  const N=8, T=6; let gr, cell, ox, oy, sel=null, cur={r:0,c:0}, phase='idle', flash=0, clear=null, moves, level, target, combo=0;
  const SH=['●','◆','▲','★','■','✚'];
  const mk=t=>({t,sp:0,oy:0});
  const F=frame(ctx,'m_gems',{ratio:1.12,title:'Gem Cannon',go:'Swap gems to match three.',hint:'Press ▶ Start, then swap gems.',
   reset(F){ cell=Math.floor(Math.min(F.W,F.H-30)/N); ox=Math.floor((F.W-cell*N)/2); oy=28; moves=25; level=1; target=1500; combo=0; sel=null; phase='idle'; do{ gr=[]; for(let r=0;r<N;r++){ gr.push([]); for(let c=0;c<N;c++){ let t; do{ t=rnd(T); }while((c>1&&gr[r][c-1].t===t&&gr[r][c-2].t===t)||(r>1&&gr[r-1][c].t===t&&gr[r-2][c].t===t)); gr[r].push(mk(t)); } } }while(!anyMove()); },
   pointer(F,ty,x,y){ if(phase!=='idle') return; const c=Math.floor((x-ox)/cell), r=Math.floor((y-oy)/cell); if(r<0||r>=N||c<0||c>=N) return; if(ty==='down'){ if(sel&&Math.abs(sel.r-r)+Math.abs(sel.c-c)===1){ swap(sel,{r,c}); sel=null; } else sel={r,c,sx:x,sy:y}; } else if(ty==='move'&&sel&&sel.sx!=null){ const dx=x-sel.sx, dy=y-sel.sy; if(Math.abs(dx)>cell*.45||Math.abs(dy)>cell*.45){ const t=Math.abs(dx)>Math.abs(dy)?{r:sel.r,c:sel.c+Math.sign(dx)}:{r:sel.r+Math.sign(dy),c:sel.c}; const a=sel; sel=null; if(t.r>=0&&t.r<N&&t.c>=0&&t.c<N) swap(a,t); } } else if(ty==='up'&&sel) sel.sx=null; },
   key(F,e,d){ if(!d) return false; const m={ArrowUp:[-1,0],ArrowDown:[1,0],ArrowLeft:[0,-1],ArrowRight:[0,1]}[e.key]; if(m){ const t={r:cl(cur.r+m[0],0,N-1),c:cl(cur.c+m[1],0,N-1)}; if(sel&&phase==='idle'){ swap(sel,t); sel=null; } cur=t; return true; } if(e.key===' '||e.key==='Enter'){ if(phase==='idle') sel=sel?null:{r:cur.r,c:cur.c}; return true; } return false; },
   update(F,dt){ let moving=false; for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const g0=gr[r][c]; if(g0&&g0.oy){ g0.oy=g0.oy<0?Math.min(0,g0.oy+dt*cell*11):Math.max(0,g0.oy-dt*cell*11); if(g0.oy) moving=true; } }
    if(phase==='fall'&&!moving){ const m=findMatches(); if(m.size){ startClear(m); } else { phase='idle'; combo=0; if(F.score>=target){ level++; target+=1500+level*600; moves+=20; F.msg('Level '+level+'! Twenty more moves.'); F.snd(880,.12); } else if(moves<=0){ F.end('Out of moves.'); } if(!anyMove()){ shuffle(); F.msg('No moves left, so the board was reshuffled.'); } } }
    if(phase==='clear'){ flash-=dt; if(flash<=0) applyClear(); } },
   draw(F){ const g=F.g; g.fillStyle='#120a2a'; g.fillRect(0,0,F.W,F.H); for(let r=0;r<N;r++) for(let c=0;c<N;c++){ g.fillStyle=(r+c)%2?'#1c1240':'#221650'; g.fillRect(ox+c*cell,oy+r*cell,cell,cell); const q=gr[r][c]; if(!q) continue; const x=ox+c*cell+cell/2, y=oy+r*cell+cell/2+q.oy; const fl=clear&&clear.has(r*N+c)&&phase==='clear';
     g.globalAlpha=fl?0.4+0.6*Math.abs(Math.sin(flash*40)):1; g.fillStyle=COL[q.t]; g.beginPath(); g.arc(x,y,cell*.4,0,7); g.fill(); g.fillStyle='rgba(255,255,255,.35)'; g.beginPath(); g.arc(x-cell*.12,y-cell*.12,cell*.13,0,7); g.fill(); g.fillStyle='#14102e'; g.font='bold '+Math.round(cell*.36)+'px system-ui'; g.textAlign='center'; g.textBaseline='middle'; g.fillText(SH[q.t],x,y+1);
     if(q.sp===1||q.sp===2){ g.strokeStyle='#fff'; g.lineWidth=3; g.beginPath(); if(q.sp===1){ g.moveTo(x-cell*.4,y); g.lineTo(x+cell*.4,y); } else { g.moveTo(x,y-cell*.4); g.lineTo(x,y+cell*.4); } g.stroke(); }
     if(q.sp===3){ g.fillStyle='#fff'; g.beginPath(); g.arc(x,y,cell*.42,0,7); g.fill(); g.fillStyle='#14102e'; g.fillText('🧭',x,y+1); } g.globalAlpha=1; }
    const mark=(p,c)=>{ if(!p) return; g.strokeStyle=c; g.lineWidth=3; g.strokeRect(ox+p.c*cell+2,oy+p.r*cell+2,cell-4,cell-4); }; mark(cur,'rgba(255,255,255,.35)'); mark(sel,'#ffe94a'); g.textBaseline='alphabetic'; },
   hud:F=>'Score '+F.score+' / '+target+' · moves '+moves+' · level '+level});
  function at(p){ return gr[p.r][p.c]; }
  function findMatches(){ const s=new Set(); for(let r=0;r<N;r++){ let run=1; for(let c=1;c<=N;c++){ if(c<N&&gr[r][c]&&gr[r][c-1]&&gr[r][c].t===gr[r][c-1].t&&gr[r][c].sp!==3) run++; else { if(run>=3) for(let k=c-run;k<c;k++) s.add(r*N+k); run=1; } } }
   for(let c=0;c<N;c++){ let run=1; for(let r=1;r<=N;r++){ if(r<N&&gr[r][c]&&gr[r-1][c]&&gr[r][c].t===gr[r-1][c].t&&gr[r][c].sp!==3) run++; else { if(run>=3) for(let k=r-run;k<r;k++) s.add(k*N+c); run=1; } } } return s; }
  function runLen(p){ const t=at(p).t; let a=1,b=1; for(let c=p.c-1;c>=0&&gr[p.r][c].t===t;c--) a++; for(let c=p.c+1;c<N&&gr[p.r][c].t===t;c++) a++; for(let r=p.r-1;r>=0&&gr[r][p.c].t===t;r--) b++; for(let r=p.r+1;r<N&&gr[r][p.c].t===t;r++) b++; return [a,b]; }
  function swap(a,b){ if(phase!=='idle'||moves<=0) return; const A=at(a), Bq=at(b);
   if(A.sp===3||Bq.sp===3){ const t=A.sp===3?Bq.t:A.t; const s=new Set(); for(let r=0;r<N;r++) for(let c=0;c<N;c++) if(gr[r][c].t===t) s.add(r*N+c); s.add(a.r*N+a.c); s.add(b.r*N+b.c); moves--; F.snd(990,.12); startClear(s); return; }
   gr[a.r][a.c]=Bq; gr[b.r][b.c]=A; const m=findMatches(); if(!m.size){ gr[a.r][a.c]=A; gr[b.r][b.c]=Bq; F.snd(140,.06); F.msg('No match there. Try another swap.'); return; }
   moves--; F.snd(620,.04); [b,a].forEach(p=>{ const [x,y]=runLen(p), q=at(p); if(x>=5||y>=5){ q.keep=3; } else if(x===4){ q.keep=1; } else if(y===4){ q.keep=2; } }); startClear(m); }
  function startClear(s){ let grow=true; while(grow){ grow=false; [...s].forEach(i=>{ const r=Math.floor(i/N), c=i%N, q=gr[r][c]; if(!q||q.done) return; q.done=1; if(q.sp===1) for(let k=0;k<N;k++){ if(!s.has(r*N+k)){ s.add(r*N+k); grow=true; } } if(q.sp===2) for(let k=0;k<N;k++){ if(!s.has(k*N+c)){ s.add(k*N+c); grow=true; } } }); }
   clear=s; phase='clear'; flash=0.22; combo++; F.add(s.size*10*combo); if(combo>1) F.msg('Combo ×'+combo+'!'); F.snd(500+combo*90,.05); }
  function applyClear(){ for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const q=gr[r][c]; if(!q) continue; delete q.done; if(clear.has(r*N+c)){ if(q.keep){ q.sp=q.keep; delete q.keep; } else gr[r][c]=null; } else delete q.keep; }
   for(let c=0;c<N;c++){ let w=N-1; for(let r=N-1;r>=0;r--){ const q=gr[r][c]; if(q){ if(w!==r){ gr[w][c]=q; gr[r][c]=null; q.oy-=(w-r)*cell; } w--; } } for(let r=w,k=1;r>=0;r--,k++){ const q=mk(rnd(T)); q.oy=-(w+1)*cell-k*4; gr[r][c]=q; } }
   clear=null; phase='fall'; }
  function anyMove(){ for(let r=0;r<N;r++) for(let c=0;c<N;c++){ if(gr[r][c].sp===3) return true; for(const [dr,dc] of [[0,1],[1,0]]){ const r2=r+dr,c2=c+dc; if(r2>=N||c2>=N) continue; const a=gr[r][c]; gr[r][c]=gr[r2][c2]; gr[r2][c2]=a; const ok=findMatches().size>0; gr[r2][c2]=gr[r][c]; gr[r][c]=a; if(ok) return true; } } return false; }
  function shuffle(){ let tries=0; do{ const all=[].concat(...gr); for(let i=all.length-1;i>0;i--){ const j=rnd(i+1); [all[i],all[j]]=[all[j],all[i]]; } for(let r=0;r<N;r++) for(let c=0;c<N;c++) gr[r][c]=all[r*N+c]; tries++; }while((findMatches().size||!anyMove())&&tries<50); }
  return {state:()=>({score:F.score,moves,level,phase})}; });

 /* 2 · BUBBLE BLASTER: aim the compass cannon, pop three of a colour */
 reg('m_bubbles','Bubble Blaster','Aim the compass cannon and fire coloured bubbles at the cluster above. Join three or more of one colour to pop them; bubbles left hanging drop for double points. Every seventh shot is a star bomb that bursts everything near where it lands. The ceiling creeps down every eight shots, so clear the board before it reaches the cannon. Drag to aim and let go to fire, or use Left/Right and Space.',ctx=>{
  const C=11; let R, gr, shift, shot, cur, nxt, ang, shots, level, ncol, rowH, maxRows, pops;
  const off=r=>((r+shift)%2)*R, cols=r=>((r+shift)%2)?C-1:C, px=(r,c)=>R+c*2*R+off(r), py=r=>28+R+r*rowH;
  const F=frame(ctx,'m_bubbles',{ratio:1.25,maxW:560,title:'Bubble Blaster',go:'Aim and fire.',hint:'Press ▶ Start, then drag to aim and let go to fire.',
   reset(F){ R=F.W/(C*2+1); rowH=R*Math.sqrt(3); maxRows=Math.floor((F.H-28-70)/rowH); level=1; ncol=4; newBoard(); },
   pointer(F,t,x,y){ if(shot) return; const a=Math.atan2(F.H-36-y,x-F.W/2); ang=cl(a,0.18,Math.PI-0.18); if(t==='up') fire(); },
   key(F,e,d){ if(!d) return false; if(e.key==='ArrowLeft'){ ang=cl(ang+0.06,0.18,Math.PI-0.18); return true; } if(e.key==='ArrowRight'){ ang=cl(ang-0.06,0.18,Math.PI-0.18); return true; } if(e.key===' '||e.key==='ArrowUp'){ fire(); return true; } return false; },
   update(F,dt){ if(F.keys.ArrowLeft) ang=cl(ang+dt*1.6,0.18,Math.PI-0.18); if(F.keys.ArrowRight) ang=cl(ang-dt*1.6,0.18,Math.PI-0.18);
    if(shot){ for(let s=0;s<4;s++){ shot.x+=shot.vx*dt/4; shot.y+=shot.vy*dt/4; if(shot.x<R){ shot.x=R; shot.vx=-shot.vx; } if(shot.x>F.W-R){ shot.x=F.W-R; shot.vx=-shot.vx; } let hit=shot.y<=28+R; if(!hit){ for(let r=0;r<gr.length&&!hit;r++) for(let c=0;c<gr[r].length;c++){ if(gr[r][c]<0) continue; const dx=px(r,c)-shot.x, dy=py(r)-shot.y; if(dx*dx+dy*dy<(2*R*0.86)**2){ hit=true; break; } } } if(hit){ land(); break; } } }
    pops=pops.filter(p=>{ p.t+=dt; p.y+=p.vy*dt; p.vy+=900*dt; return p.t<1.2; }); },
   draw(F){ const g=F.g; g.fillStyle='#0b0820'; g.fillRect(0,0,F.W,F.H); g.strokeStyle='rgba(255,79,109,.5)'; g.setLineDash([6,6]); g.beginPath(); g.moveTo(0,py(maxRows)-R); g.lineTo(F.W,py(maxRows)-R); g.stroke(); g.setLineDash([]);
    for(let r=0;r<gr.length;r++) for(let c=0;c<gr[r].length;c++) if(gr[r][c]>=0) ball(g,px(r,c),py(r),gr[r][c]);
    pops.forEach(p=>{ g.globalAlpha=Math.max(0,1-p.t); ball(g,p.x,p.y,p.c); g.globalAlpha=1; });
    const cx=F.W/2, cy=F.H-36; g.strokeStyle='rgba(255,255,255,.25)'; g.setLineDash([4,8]); g.beginPath(); g.moveTo(cx,cy); g.lineTo(cx+Math.cos(ang)*F.H*.45,cy-Math.sin(ang)*F.H*.45); g.stroke(); g.setLineDash([]);
    g.fillStyle='#2a2f7a'; g.beginPath(); g.arc(cx,cy,R*1.6,0,7); g.fill(); g.save(); g.translate(cx,cy); g.rotate(-ang); g.fillStyle='#ffe94a'; g.fillRect(0,-R*.35,R*2.2,R*.7); g.restore();
    if(shot) ball(g,shot.x,shot.y,shot.c); else ball(g,cx,cy,cur); ball(g,cx+R*3.2,cy+8,nxt,0.7); g.fillStyle='#cfd6ff'; g.font='12px system-ui'; g.textAlign='left'; g.fillText('next',cx+R*4.2,cy+12); },
   hud:F=>'Score '+F.score+' · level '+level+' · shots '+(8-shots%8)+' to drop'});
  function ball(g,x,y,c,s){ s=s||1; if(c===9){ g.fillStyle='#fff'; g.beginPath(); g.arc(x,y,R*.92*s,0,7); g.fill(); g.fillStyle='#ff9a3c'; g.font='bold '+Math.round(R*1.1*s)+'px system-ui'; g.textAlign='center'; g.textBaseline='middle'; g.fillText('★',x,y+1); g.textBaseline='alphabetic'; return; } g.fillStyle=COL[c]; g.beginPath(); g.arc(x,y,R*.92*s,0,7); g.fill(); g.fillStyle='rgba(255,255,255,.4)'; g.beginPath(); g.arc(x-R*.3*s,y-R*.3*s,R*.28*s,0,7); g.fill(); }
  function present(){ const s=new Set(); gr.forEach(row=>row.forEach(v=>{ if(v>=0&&v<9) s.add(v); })); return [...s]; }
  function rc(){ const p=present(); return p.length?pick(p):rnd(ncol); }
  function newBoard(){ shift=0; gr=[]; for(let r=0;r<5+Math.min(3,level);r++){ gr.push(Array.from({length:cols(r)},()=>rnd(ncol))); } shots=0; shot=null; pops=[]; ang=Math.PI/2; cur=rc(); nxt=rc(); }
  function fire(){ if(shot||F.over) return; shots++; const sp=F.H*1.9; shot={x:F.W/2,y:F.H-36,vx:Math.cos(ang)*sp,vy:-Math.sin(ang)*sp,c:shots%7===0?9:cur}; cur=nxt; nxt=rc(); F.snd(700,.03); }
  function nb(r,c){ const o=(r+shift)%2, out=[[r,c-1],[r,c+1]]; const up=o?[[r-1,c],[r-1,c+1]]:[[r-1,c-1],[r-1,c]], dn=o?[[r+1,c],[r+1,c+1]]:[[r+1,c-1],[r+1,c]]; return out.concat(up,dn).filter(([a,b])=>a>=0&&a<gr.length&&b>=0&&b<gr[a].length); }
  function land(){ let best=null, bd=1e9; const r0=cl(Math.round((shot.y-28-R)/rowH),0,maxRows); for(let r=Math.max(0,r0-1);r<=Math.min(maxRows,r0+1);r++){ while(gr.length<=r) gr.push(Array.from({length:cols(gr.length)},()=>-1)); for(let c=0;c<gr[r].length;c++){ if(gr[r][c]>=0) continue; const d=(px(r,c)-shot.x)**2+(py(r)-shot.y)**2; if(d<bd&&(r===0||nb(r,c).some(([a,b])=>gr[a][b]>=0))){ bd=d; best=[r,c]; } } }
   if(!best){ shot=null; return; } const [r,c]=best; const col=shot.c; gr[r][c]=col; shot=null;
   if(col===9){ let n=0; for(let a=0;a<gr.length;a++) for(let b=0;b<gr[a].length;b++){ if(gr[a][b]>=0&&(px(a,b)-px(r,c))**2+(py(a)-py(r))**2<(R*5)**2){ pops.push({x:px(a,b),y:py(a),vy:-80,t:0,c:gr[a][b]}); gr[a][b]=-1; n++; } } F.add(n*15); F.snd(300,.2); drop(); after(); return; }
   const seen=new Set([r+','+c]), st=[[r,c]], grp=[]; while(st.length){ const [a,b]=st.pop(); grp.push([a,b]); nb(a,b).forEach(([x,y])=>{ const k=x+','+y; if(!seen.has(k)&&gr[x][y]===col){ seen.add(k); st.push([x,y]); } }); }
   if(grp.length>=3){ grp.forEach(([a,b])=>{ pops.push({x:px(a,b),y:py(a),vy:-60,t:0,c:col}); gr[a][b]=-1; }); F.add(grp.length*10); F.snd(880,.06); drop(); }
   after(); }
  function drop(){ const keep=new Set(), st=[]; (gr[0]||[]).forEach((v,c)=>{ if(v>=0){ keep.add('0,'+c); st.push([0,c]); } }); while(st.length){ const [a,b]=st.pop(); nb(a,b).forEach(([x,y])=>{ const k=x+','+y; if(!keep.has(k)&&gr[x][y]>=0){ keep.add(k); st.push([x,y]); } }); }
   let n=0; for(let a=0;a<gr.length;a++) for(let b=0;b<gr[a].length;b++) if(gr[a][b]>=0&&!keep.has(a+','+b)){ pops.push({x:px(a,b),y:py(a),vy:0,t:0,c:gr[a][b]}); gr[a][b]=-1; n++; } if(n){ F.add(n*20); F.msg(n+' bubbles dropped: double points.'); } }
  function after(){ while(gr.length&&gr[gr.length-1].every(v=>v<0)) gr.pop();
   if(!gr.length||gr.every(row=>row.every(v=>v<0))){ F.add(500*level); level++; ncol=Math.min(7,ncol+1); F.msg('Board cleared! Level '+level+'.'); F.snd(990,.2); newBoard(); return; }
   if(shots%8===0){ shift=(shift+1)%2; gr.unshift(Array.from({length:cols(0)},()=>rc())); F.msg('The ceiling dropped a row.'); }
   if(gr.length>maxRows) F.end('The bubbles reached the cannon.'); if(present().indexOf(cur)<0) cur=rc(); if(present().indexOf(nxt)<0) nxt=rc(); }
  return {state:()=>({score:F.score,level,rows:gr.length})}; });

 /* 3 · COMET FLAP: tap to keep the comet in the air */
 reg('m_flap','Comet Flap','Tap (or press Space or Up) to give the comet a lift and thread it through the gaps in the asteroid columns. Each column passed scores a point. Golden zodiac stars give a shield that saves you from one crash. The gaps narrow as you go.',ctx=>{
  let y, vy, cols, stars, shield, sp, gap, nextX;
  const F=frame(ctx,'m_flap',{ratio:1.2,maxW:560,title:'Comet Flap',go:'Tap to fly!',hint:'Press ▶ Start, then tap to fly.',
   reset(F){ y=F.H*.45; vy=0; cols=[]; stars=[]; shield=0; sp=150; gap=F.H*.34; nextX=F.W*.8; },
   pointer(F,t){ if(t==='down') flap(); },
   key(F,e,d){ if(d&&(e.key===' '||e.key==='ArrowUp')){ flap(); return true; } return false; },
   update(F,dt){ vy+=F.H*2.3*dt; y+=vy*dt; const x0=F.W*.25; sp=150+F.score*3; gap=Math.max(F.H*.22,F.H*.34-F.score*2); nextX-=sp*dt;
    if(nextX<F.W){ const top=rr(50,F.H-gap-30); cols.push({x:F.W+30,top,gap,passed:false}); if(Math.random()<.35) stars.push({x:F.W+30+110,y:rr(60,F.H-40)}); nextX+=F.W*.42; }
    cols.forEach(c=>{ c.x-=sp*dt; if(!c.passed&&c.x+28<x0){ c.passed=true; F.add(1); F.snd(760,.03); } }); cols=cols.filter(c=>c.x>-60); stars.forEach(s=>s.x-=sp*dt); stars=stars.filter(s=>{ if(Math.hypot(s.x-x0,s.y-y)<26){ shield=1; F.snd(1100,.1); F.msg('Shield up! It saves you from one crash.'); return false; } return s.x>-20; });
    let crash=y>F.H-10||y<26; cols.forEach(c=>{ if(x0+12>c.x-28&&x0-12<c.x+28&&(y-12<c.top||y+12>c.top+c.gap)) crash=true; });
    if(crash){ if(shield){ shield=0; vy=-F.H*.6; y=cl(y,40,F.H-40); cols.forEach(c=>{ if(Math.abs(c.x-x0)<60) c.x=-100; }); F.msg('The shield took the hit.'); F.snd(300,.1); } else F.end('Crash!'); } },
   draw(F){ const g=F.g; const gr=g.createLinearGradient(0,0,0,F.H); gr.addColorStop(0,'#08061c'); gr.addColorStop(1,'#241050'); g.fillStyle=gr; g.fillRect(0,0,F.W,F.H);
    for(let i=0;i<40;i++){ g.fillStyle='rgba(255,255,255,.5)'; g.fillRect((i*97+F.t*-20*(1+i%3))%F.W+F.W*(((i*97-F.t*20*(1+i%3))<0)?1:0),(i*53)%F.H,2,2); }
    cols.forEach(c=>{ g.fillStyle='#5a4a8a'; rrect(g,c.x-28,0,56,c.top,8); g.fill(); rrect(g,c.x-28,c.top+c.gap,56,F.H-c.top-c.gap,8); g.fill(); g.fillStyle='#7d6bb5'; g.fillRect(c.x-28,c.top-10,56,10); g.fillRect(c.x-28,c.top+c.gap,56,10); });
    stars.forEach(s=>{ g.fillStyle='#ffe94a'; g.font='22px system-ui'; g.textAlign='center'; g.fillText('★',s.x,s.y+8); });
    const x0=F.W*.25; for(let i=1;i<7;i++){ g.globalAlpha=.5-i*.07; g.fillStyle='#6fe8ff'; g.beginPath(); g.arc(x0-i*7,y+i*vy*.004,12-i,0,7); g.fill(); } g.globalAlpha=1; g.fillStyle='#fff'; g.beginPath(); g.arc(x0,y,12,0,7); g.fill(); if(shield){ g.strokeStyle='#ffe94a'; g.lineWidth=3; g.beginPath(); g.arc(x0,y,18,0,7); g.stroke(); } },
   hud:F=>'Score '+F.score+(shield?' · 🛡 shield':'')});
  function flap(){ if(!F.running||F.over) return; vy=-F.H*.62; F.snd(520,.02); }
  return {state:()=>({score:F.score,y})}; });

 /* 4 · TOWER GUARD: build towers along the path */
 reg('m_towers','Tower Guard','Enemies march along the path toward your gate. Tap an empty square to build the tower you picked: ⚡ Laser (quick), 💥 Cannon (hits a group), ❄ Frost (slows them). Tap a tower to upgrade it. Each enemy stopped pays coins; each one that reaches the gate costs a life. Press ▶ Next wave when you are ready, or wait for it.',ctx=>{
  const CC=12, RR=8; let cs, path, pts, ens, tws, shots, coins, lives, wave, spawn, wtimer, kind='laser', fx;
  const TW={laser:{n:'⚡',cost:40,rng:2.3,rate:.35,dmg:6,col:'#6fe8ff'},cannon:{n:'💥',cost:70,rng:2.7,rate:1.2,dmg:18,col:'#ff9a3c',splash:1},frost:{n:'❄',cost:55,rng:2.1,rate:.8,dmg:3,col:'#c3f0ff',slow:1}};
  const PATH=[[0,1],[3,1],[3,5],[6,5],[6,2],[9,2],[9,6],[11,6]];
  const F=frame(ctx,'m_towers',{ratio:0.75,title:'Tower Guard',go:'Build towers, then send the wave.',hint:'Press ▶ Start, pick a tower, tap a square.',
   buttons:F=>[['⚡ Laser 40',b=>pickK('laser',b)],['💥 Cannon 70',b=>pickK('cannon',b)],['❄ Frost 55',b=>pickK('frost',b)],['▶ Next wave',()=>{ if(!spawn.left) startWave(); }]],
   reset(F){ cs=Math.floor(Math.min(F.W/CC,(F.H-28)/RR)); path=new Set(); pts=[]; for(let i=0;i<PATH.length-1;i++){ const [a,b]=PATH[i],[c,d]=PATH[i+1]; const sx=Math.sign(c-a), sy=Math.sign(d-b); let x=a,y=b; while(x!==c||y!==d){ path.add(x+','+y); x+=sx; y+=sy; } path.add(c+','+d); } PATH.forEach(([x,y])=>pts.push([x*cs+cs/2,28+y*cs+cs/2])); ens=[]; tws=[]; shots=[]; fx=[]; coins=120; lives=20; wave=0; spawn={left:0,t:0}; wtimer=8; },
   pointer(F,t,x,y){ if(t!=='down') return; const c=Math.floor(x/cs), r=Math.floor((y-28)/cs); if(c<0||c>=CC||r<0||r>=RR) return; const ex=tws.find(w=>w.c===c&&w.r===r); if(ex){ const cost=Math.round(TW[ex.k].cost*0.8*ex.lv); if(ex.lv>=3) return F.msg('That tower is at its top level.'); if(coins<cost) return F.msg('Upgrading needs '+cost+' coins.'); coins-=cost; ex.lv++; F.snd(880,.06); return F.msg(TW[ex.k].n+' tower upgraded to level '+ex.lv+'.'); }
    if(path.has(c+','+r)) return F.msg('That square is the road. Build beside it.'); const T=TW[kind]; if(coins<T.cost) return F.msg('You need '+T.cost+' coins for that tower.'); coins-=T.cost; tws.push({c,r,k:kind,lv:1,cd:0}); F.snd(600,.05); },
   update(F,dt){ if(!spawn.left&&!ens.length){ wtimer-=dt; if(wtimer<=0) startWave(); }
    if(spawn.left){ spawn.t-=dt; if(spawn.t<=0){ spawn.left--; spawn.t=0.8; const hp=20+wave*12; ens.push({i:0,x:pts[0][0],y:pts[0][1],hp,max:hp,sp:cs*(1.1+wave*.04),slow:0,boss:spawn.left===0&&wave%5===0}); const e=ens[ens.length-1]; if(e.boss){ e.hp*=5; e.max=e.hp; e.sp*=.7; } } }
    ens.forEach(e=>{ const s=e.sp*(e.slow>0?0.45:1); e.slow-=dt; let d=s*dt; while(d>0&&e.i<pts.length-1){ const [tx,ty]=pts[e.i+1], dx=tx-e.x, dy=ty-e.y, L=Math.hypot(dx,dy); if(L<=d){ e.x=tx; e.y=ty; e.i++; d-=L; } else { e.x+=dx/L*d; e.y+=dy/L*d; d=0; } } if(e.i>=pts.length-1){ e.gone=1; lives-=e.boss?5:1; F.snd(120,.1); } });
    tws.forEach(w=>{ w.cd-=dt; if(w.cd>0) return; const T=TW[w.k], x=w.c*cs+cs/2, y=28+w.r*cs+cs/2, rg=T.rng*cs*(1+(w.lv-1)*.15); let tgt=null, far=-1; ens.forEach(e=>{ if(e.hp>0&&Math.hypot(e.x-x,e.y-y)<=rg&&e.i>far){ far=e.i; tgt=e; } }); if(!tgt) return; w.cd=T.rate; const dmg=T.dmg*(1+(w.lv-1)*.6);
     if(T.splash) shots.push({x,y,tx:tgt.x,ty:tgt.y,t:0,dmg}); else { tgt.hp-=dmg; if(T.slow) tgt.slow=1.5; fx.push({x1:x,y1:y,x2:tgt.x,y2:tgt.y,t:.08,c:T.col}); } });
    shots.forEach(s=>{ s.t+=dt*3; if(s.t>=1){ s.done=1; ens.forEach(e=>{ if(Math.hypot(e.x-s.tx,e.y-s.ty)<cs*1.1) e.hp-=s.dmg; }); fx.push({ring:1,x:s.tx,y:s.ty,t:.25,c:'#ff9a3c'}); } }); shots=shots.filter(s=>!s.done);
    ens.forEach(e=>{ if(e.hp<=0&&!e.gone){ e.gone=1; coins+=5+wave+(e.boss?40:0); F.add(10+wave*2+(e.boss?200:0)); } }); ens=ens.filter(e=>!e.gone); fx.forEach(f=>f.t-=dt); fx=fx.filter(f=>f.t>0);
    if(lives<=0) F.end('The gate fell on wave '+wave+'.'); },
   draw(F){ const g=F.g; g.fillStyle='#0e1a12'; g.fillRect(0,0,F.W,F.H); for(let r=0;r<RR;r++) for(let c=0;c<CC;c++){ g.fillStyle=path.has(c+','+r)?'#5a4a2a':((r+c)%2?'#173a22':'#1b4227'); g.fillRect(c*cs,28+r*cs,cs-1,cs-1); }
    g.fillStyle='#ffe94a'; g.font=Math.round(cs*.6)+'px system-ui'; g.textAlign='center'; g.textBaseline='middle'; g.fillText('🏰',pts[pts.length-1][0],pts[pts.length-1][1]);
    tws.forEach(w=>{ const x=w.c*cs+cs/2, y=28+w.r*cs+cs/2; g.fillStyle='#2a2f7a'; g.beginPath(); g.arc(x,y,cs*.42,0,7); g.fill(); g.fillStyle='#fff'; g.font=Math.round(cs*.48)+'px system-ui'; g.fillText(TW[w.k].n,x,y+1); for(let i=0;i<w.lv;i++){ g.fillStyle='#ffe94a'; g.fillRect(x-cs*.3+i*cs*.22,y+cs*.3,cs*.16,4); } });
    ens.forEach(e=>{ g.fillStyle=e.boss?'#ff4f6d':(e.slow>0?'#9fdcff':'#c38bff'); g.beginPath(); g.arc(e.x,e.y,cs*(e.boss?.38:.26),0,7); g.fill(); g.fillStyle='#000'; g.fillRect(e.x-cs*.3,e.y-cs*.45,cs*.6,4); g.fillStyle='#7cff8a'; g.fillRect(e.x-cs*.3,e.y-cs*.45,cs*.6*Math.max(0,e.hp/e.max),4); });
    shots.forEach(s=>{ const x=s.x+(s.tx-s.x)*s.t, y=s.y+(s.ty-s.y)*s.t-Math.sin(s.t*Math.PI)*cs; g.fillStyle='#ff9a3c'; g.beginPath(); g.arc(x,y,4,0,7); g.fill(); });
    fx.forEach(f=>{ g.strokeStyle=f.c; g.lineWidth=2; g.beginPath(); if(f.ring) g.arc(f.x,f.y,cs*(1.2-f.t*3),0,7); else { g.moveTo(f.x1,f.y1); g.lineTo(f.x2,f.y2); } g.stroke(); }); g.textBaseline='alphabetic'; },
   hud:F=>'Score '+F.score+' · 🪙 '+coins+' · ❤ '+lives+' · wave '+wave+(spawn.left||ens.length?'':' · next in '+Math.ceil(wtimer)+'s')+' · building '+TW[kind].n});
  function pickK(k,b){ kind=k; F.msg('Building '+TW[k].n+' towers ('+TW[k].cost+' coins). Tap an empty square.'); }
  function startWave(){ wave++; spawn={left:6+wave*2,t:0}; wtimer=10; F.msg('Wave '+wave+(wave%5===0?': a boss is coming!':'.')); F.snd(440,.08); }
  return {state:()=>({score:F.score,wave,coins,lives,towers:tws.length})}; });

 /* 5 · SLINGSHOT SIEGE: pull back, launch, topple the towers */
 reg('m_sling','Slingshot Siege','Pull back on the slingshot and let go to launch a stone at the towers. Knock out every drone (the red orbs) before your stones run out. Blocks crack when hit and the ones above fall; a drone falls with its block. Unused stones are worth a bonus. Drag from the slingshot to aim; or Left/Right to aim, Up/Down for power and Space to launch.',ctx=>{
  let sx, sy, stone, flying, aim, cols, drones, stones, level, cw, bh, ground, parts, VW=600, VH=380;
  const F=frame(ctx,'m_sling',{ratio:0.62,title:'Slingshot Siege',go:'Drag back and let go.',hint:'Press ▶ Start, then drag back from the slingshot.',
   reset(F){ VW=F.W; VH=F.H; level=1; build(); },
   pointer(F,t,x,y){ if(flying) return; if(t==='down'&&Math.hypot(x-sx,y-sy)<80) aim={x,y,on:true}; else if(t==='move'&&aim&&aim.on){ aim.x=x; aim.y=y; } else if(t==='up'&&aim&&aim.on){ launch((sx-aim.x)*6,(sy-aim.y)*6); aim=null; } },
   key(F,e,d){ if(!d) return false; if(!aim) aim={a:-0.7,p:0.7,key:1}; if(e.key==='ArrowLeft') aim.a-=0.05; else if(e.key==='ArrowRight') aim.a+=0.05; else if(e.key==='ArrowUp') aim.p=cl(aim.p+0.05,.2,1); else if(e.key==='ArrowDown') aim.p=cl(aim.p-0.05,.2,1); else if(e.key===' '){ if(!flying){ const v=aim.p*900; launch(Math.cos(aim.a)*v,Math.sin(aim.a)*v); } return true; } else return false; return true; },
   update(F,dt){ parts=parts.filter(p=>{ p.t+=dt; p.x+=p.vx*dt; p.y+=p.vy*dt; p.vy+=600*dt; return p.t<1; });
    cols.forEach(col=>col.forEach(b=>{ if(b.y<b.ty){ b.y=Math.min(b.ty,b.y+dt*400); } }));
    if(flying){ for(let s=0;s<3;s++){ stone.vy+=900*dt/3; stone.x+=stone.vx*dt/3; stone.y+=stone.vy*dt/3; if(stone.y>ground-8){ stone.y=ground-8; stone.vy*=-0.35; stone.vx*=0.7; }
      cols.forEach((col,ci)=>{ const x0=colX(ci); if(stone.x+8<x0||stone.x-8>x0+cw) return; for(let k=col.length-1;k>=0;k--){ const b=col[k]; if(stone.y+8>b.y&&stone.y-8<b.y+bh){ const hit=Math.hypot(stone.vx,stone.vy)/250; b.hp-=hit; stone.vx*=-0.3; stone.vy*=0.5; stone.x+=stone.vx>0?6:-6; F.snd(220,.04); burst(stone.x,stone.y,'#c9a46a'); if(b.hp<=0) breakBlock(ci,k); return; } } });
      drones.forEach(d=>{ if(!d.dead&&Math.hypot(stone.x-d.x,stone.y-d.y)<20){ kill(d); stone.vx*=.6; } }); }
     if(Math.abs(stone.vx)<20&&stone.y>=ground-9||stone.x>F.W+40||stone.x<-40){ flying=false; settle(); } }
    drones.forEach(d=>{ if(d.on!=null){ const col=cols[d.ci]; const ty=ground-col.length*bh-12; if(d.y<ty) d.y=Math.min(ty,d.y+dt*400); if(d.fell&&d.y>=ty-1&&!d.dead) kill(d); } }); },
   draw(F){ const g=F.g; const sky=g.createLinearGradient(0,0,0,F.H); sky.addColorStop(0,'#2a1f6a'); sky.addColorStop(1,'#ff9a6a'); g.fillStyle=sky; g.fillRect(0,0,F.W,F.H); g.fillStyle='#2a5a2a'; g.fillRect(0,ground,F.W,F.H-ground);
    cols.forEach((col,ci)=>col.forEach(b=>{ g.fillStyle=b.hp>1.5?'#c9a46a':b.hp>0.7?'#a8834e':'#7a5a34'; g.fillRect(colX(ci),b.y,cw,bh-2); g.strokeStyle='rgba(0,0,0,.3)'; g.strokeRect(colX(ci),b.y,cw,bh-2); }));
    drones.forEach(d=>{ if(d.dead) return; g.fillStyle='#ff4f6d'; g.beginPath(); g.arc(d.x,d.y,12,0,7); g.fill(); g.fillStyle='#fff'; g.fillRect(d.x-5,d.y-3,3,3); g.fillRect(d.x+2,d.y-3,3,3); });
    parts.forEach(p=>{ g.globalAlpha=1-p.t; g.fillStyle=p.c; g.fillRect(p.x,p.y,3,3); }); g.globalAlpha=1;
    g.strokeStyle='#5a3a1a'; g.lineWidth=6; g.beginPath(); g.moveTo(sx,ground); g.lineTo(sx,sy+10); g.stroke();
    if(!flying&&stones>0){ let ax=sx, ay=sy; if(aim&&aim.on){ ax=aim.x; ay=aim.y; } else if(aim&&aim.key){ ax=sx-Math.cos(aim.a)*aim.p*70; ay=sy-Math.sin(aim.a)*aim.p*70; } g.strokeStyle='#3a2a1a'; g.lineWidth=3; g.beginPath(); g.moveTo(sx-8,sy); g.lineTo(ax,ay); g.lineTo(sx+8,sy); g.stroke(); g.fillStyle='#777'; g.beginPath(); g.arc(ax,ay,8,0,7); g.fill();
     if(aim){ const vx=aim.on?(sx-aim.x)*6:Math.cos(aim.a)*aim.p*900, vy=aim.on?(sy-aim.y)*6:Math.sin(aim.a)*aim.p*900; g.fillStyle='rgba(255,255,255,.6)'; let x=sx, y=sy, wx=vx, wy=vy; for(let i=0;i<14;i++){ for(let s=0;s<4;s++){ wy+=900*0.025/4; x+=wx*0.025/4; y+=wy*0.025/4; } g.fillRect(x,y,3,3); } } }
    if(flying){ g.fillStyle='#777'; g.beginPath(); g.arc(stone.x,stone.y,8,0,7); g.fill(); } },
   hud:F=>'Score '+F.score+' · stones '+stones+' · drones '+drones.filter(d=>!d.dead).length+' · level '+level});
  function colX(i){ return VW*0.48+i*(cw+cw*.55); }
  function build(){ ground=VH-30; sx=VW*0.14; sy=ground-70; cw=Math.max(22,VW*0.055); bh=Math.max(16,VH*0.07); const n=3+Math.min(3,level); cols=[]; drones=[]; parts=[]; flying=false; aim=null; stones=3+Math.min(3,Math.ceil(level/2)+1);
   for(let i=0;i<n;i++){ const ht=2+rnd(3+Math.min(3,level)); const col=[]; for(let k=0;k<ht;k++){ const ty=ground-(k+1)*bh; col.push({y:ty,ty,hp:2}); } cols.push(col); if(Math.random()<.65||i===n-1) drones.push({ci:i,on:true,x:colX(i)+cw/2,y:ground-ht*bh-12}); } }
  function launch(vx,vy){ if(flying||stones<=0||F.over) return; const sp=Math.hypot(vx,vy); if(sp<60) return; if(sp>950){ vx*=950/sp; vy*=950/sp; } stone={x:sx,y:sy,vx,vy}; flying=true; stones--; F.snd(400,.05); }
  function breakBlock(ci,k){ const col=cols[ci]; burst(colX(ci)+cw/2,col[k].y+bh/2,'#c9a46a'); col.splice(k,1); F.add(50); col.forEach((b,i)=>{ b.ty=ground-(i+1)*bh; }); drones.forEach(d=>{ if(d.ci===ci&&!d.dead) d.fell=true; }); }
  function kill(d){ d.dead=true; F.add(500); F.snd(880,.1); burst(d.x,d.y,'#ff4f6d'); }
  function burst(x,y,c){ for(let i=0;i<12;i++){ const a=Math.random()*7, v=rr(60,200); parts.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v-80,t:0,c}); } }
  function settle(){ if(drones.every(d=>d.dead)){ F.add(stones*1000); F.msg('Every drone down! '+stones+' stones left: +'+(stones*1000)+'. Level '+(level+1)+'.'); level++; build(); return; } if(stones<=0) F.end('Out of stones.'); }
  return {state:()=>({score:F.score,stones,level,drones:drones.filter(d=>!d.dead).length})}; });

 /* 6 · STAR SLICER: swipe to slice the planets, never the bombs */
 reg('m_slice','Star Slicer','Planets fly up from below: swipe across them to slice them. Slice three or more in one swipe for a combo. Do not slice the bombs. Let three planets fall unsliced and the game ends. Keys: arrows move the blade and it cuts as it moves.',ctx=>{
  let obs, trail, lives, nextT, halves, kx, ky, swipeHits;
  const F=frame(ctx,'m_slice',{ratio:0.9,maxW:640,title:'Star Slicer',go:'Swipe to slice!',hint:'Press ▶ Start, then swipe across the planets.',tapStarts:false,
   reset(F){ obs=[]; trail=[]; lives=3; nextT=0.6; halves=[]; kx=F.W/2; ky=F.H/2; swipeHits=0; },
   pointer(F,t,x,y){ if(t==='down'){ trail=[{x,y,t:F.t}]; swipeHits=0; } else if(t==='move'&&F.down){ const p=trail[trail.length-1]; trail.push({x,y,t:F.t}); if(p) cut(p.x,p.y,x,y); } else if(t==='up'){ if(swipeHits>=3){ F.add(swipeHits*2); F.msg('Combo ×'+swipeHits+'! +'+(swipeHits*2)); F.snd(990,.1); } swipeHits=0; } },
   update(F,dt){ nextT-=dt; if(nextT<=0){ nextT=Math.max(0.35,1.1-F.t*0.01); const n=1+rnd(Math.min(4,1+Math.floor(F.t/20))); for(let i=0;i<n;i++){ const bomb=Math.random()<Math.min(0.22,0.06+F.t*0.002); obs.push({x:rr(F.W*.15,F.W*.85),y:F.H+20,vx:rr(-90,90),vy:-rr(F.H*1.15,F.H*1.45),r:rr(18,28),c:pick(COL),bomb,rot:0,vr:rr(-3,3)}); } }
    const kb=(F.keys.ArrowLeft?-1:0)+(F.keys.ArrowRight?1:0), kv=(F.keys.ArrowUp?-1:0)+(F.keys.ArrowDown?1:0); if(kb||kv){ const ox=kx, oy=ky; kx=cl(kx+kb*500*dt,0,F.W); ky=cl(ky+kv*500*dt,30,F.H); trail.push({x:kx,y:ky,t:F.t}); cut(ox,oy,kx,ky); }
    const G=F.H*1.25; obs.forEach(o=>{ o.vy+=G*dt; o.x+=o.vx*dt; o.y+=o.vy*dt; o.rot+=o.vr*dt; if(o.y>F.H+40&&o.vy>0){ o.gone=1; if(!o.bomb&&!o.cut){ lives--; F.snd(150,.1); F.msg(lives>0?'One got away. '+lives+' left.':''); if(lives<=0) F.end('Three planets got away.'); } } }); obs=obs.filter(o=>!o.gone&&!o.cut);
    halves.forEach(p=>{ p.vy+=G*dt; p.x+=p.vx*dt; p.y+=p.vy*dt; p.t+=dt; }); halves=halves.filter(p=>p.t<1.5); trail=trail.filter(p=>F.t-p.t<0.18); },
   draw(F){ const g=F.g; g.fillStyle='#0b0620'; g.fillRect(0,0,F.W,F.H);
    obs.forEach(o=>{ g.save(); g.translate(o.x,o.y); g.rotate(o.rot); if(o.bomb){ g.fillStyle='#222'; g.beginPath(); g.arc(0,0,o.r,0,7); g.fill(); g.strokeStyle='#ff4f6d'; g.lineWidth=3; g.stroke(); g.fillStyle='#ffe94a'; g.font='bold '+Math.round(o.r)+'px system-ui'; g.textAlign='center'; g.textBaseline='middle'; g.fillText('✷',0,1); } else { g.fillStyle=o.c; g.beginPath(); g.arc(0,0,o.r,0,7); g.fill(); g.strokeStyle='rgba(255,255,255,.5)'; g.lineWidth=2; g.beginPath(); g.ellipse(0,0,o.r*1.4,o.r*.35,0,0,7); g.stroke(); } g.restore(); });
    halves.forEach(p=>{ g.globalAlpha=Math.max(0,1-p.t/1.5); g.fillStyle=p.c; g.beginPath(); g.arc(p.x,p.y,p.r,p.a,p.a+Math.PI); g.fill(); }); g.globalAlpha=1;
    if(trail.length>1){ g.strokeStyle='#fff'; g.lineCap='round'; for(let i=1;i<trail.length;i++){ g.lineWidth=2+i*0.8; g.beginPath(); g.moveTo(trail[i-1].x,trail[i-1].y); g.lineTo(trail[i].x,trail[i].y); g.stroke(); } }
    g.textBaseline='alphabetic'; for(let i=0;i<3;i++){ g.fillStyle=i<3-lives?'#ff4f6d':'rgba(255,255,255,.25)'; g.font='bold 18px system-ui'; g.textAlign='right'; g.fillText('✕',F.W-8-i*20,46); } },
   hud:F=>'Score '+F.score});
  function cut(x1,y1,x2,y2){ const dx=x2-x1, dy=y2-y1, L2=dx*dx+dy*dy||1; obs.forEach(o=>{ if(o.cut) return; let t=((o.x-x1)*dx+(o.y-y1)*dy)/L2; t=cl(t,0,1); const px=x1+dx*t, py=y1+dy*t; if(Math.hypot(o.x-px,o.y-py)<o.r){ o.cut=1; if(o.bomb){ F.snd(80,.4); halves.push({x:o.x,y:o.y,vx:-80,vy:-200,r:o.r,a:0,c:'#ff4f6d',t:0}); F.end('You sliced a bomb!'); return; } F.add(1); swipeHits++; F.snd(700+swipeHits*60,.03); const a=Math.atan2(dy,dx); halves.push({x:o.x,y:o.y,vx:o.vx-120,vy:o.vy-60,r:o.r,a:a,c:o.c,t:0},{x:o.x,y:o.y,vx:o.vx+120,vy:o.vy-60,r:o.r,a:a+Math.PI,c:o.c,t:0}); } }); }
  return {state:()=>({score:F.score,lives})}; });

 /* 7 · POCKET PET: a little star creature that grows with care */
 reg('m_pet','Pocket Pet','Kanny is a little star creature who lives on this device. Feed, play, clean and put it to sleep to keep its four meters up; it grows from an egg to a shining star as it is cared for. Meters drop slowly in real time, even when the app is closed, but Kanny never dies: it only gets sad. Play opens a catch game: tap the ball five times.',ctx=>{
  const K='kanin-pet'; let P=getLS(K,null); const now=()=>Date.now();
  if(!P) P={name:'Kanny',born:now(),last:now(),h:80,f:80,e:80,c:80,xp:0,asleep:false};
  const STAGES=[['Egg',0],['Baby',40],['Kid',150],['Teen',400],['Star',900]];
  const stage=()=>{ let s=0; STAGES.forEach((x,i)=>{ if(P.xp>=x[1]) s=i; }); return s; };
  let ball=null, catches=0, msg='', bob=0;
  function decay(){ const mins=(now()-P.last)/60000; if(mins<=0) return; const k=P.asleep?0.4:1; P.h=cl(P.h-mins*0.5*k,0,100); P.f=cl(P.f-mins*0.6*k,0,100); P.c=cl(P.c-mins*0.3*k,0,100); P.e=P.asleep?cl(P.e+mins*2,0,100):cl(P.e-mins*0.4,0,100); if(P.asleep&&P.e>=100){ P.asleep=false; } P.last=now(); putLS(K,P); }
  function care(field,amt,xp,text,f){ decay(); if(P.asleep&&field!=='e') return F.msg(P.name+' is asleep. Let it rest, or tap 😴 to wake it.'); const before=P[field]; P[field]=cl(P[field]+amt,0,100); P.xp+=before<90?xp:Math.ceil(xp/4); putLS(K,P); F.score=P.xp; msg=text; F.snd(f||660,.06); const s=stage(); if(s>(P.lastStage||0)){ P.lastStage=s; putLS(K,P); msg=P.name+' grew into a '+STAGES[s][0]+'!'; F.snd(990,.2); } F.msg(msg); }
  const F=frame(ctx,'m_pet',{ratio:0.8,maxW:600,title:'Pocket Pet',go:'Look after '+P.name+'.',hint:'Press ▶ Start to visit '+P.name+'.',
   buttons:F=>[['🍎 Feed',()=>care('h',25,6,'Yum! '+P.name+' ate.',600)],['🎾 Play',()=>{ if(P.asleep) return F.msg(P.name+' is asleep.'); ball={x:F.W/2,y:F.H/2,vx:rr(-220,220),vy:rr(-220,220)}; catches=0; F.msg('Tap the ball five times!'); }],['🛁 Clean',()=>care('c',40,5,P.name+' is sparkling clean.',800)],['😴 Sleep',()=>{ decay(); P.asleep=!P.asleep; putLS(K,P); F.msg(P.asleep?P.name+' is sleeping. Energy comes back while it rests.':P.name+' woke up.'); }],['✏ Rename',()=>{ let n=''; try{ n=(window.KSTARS&&KSTARS.profile&&KSTARS.profile().name)||''; }catch(_){ } const names=['Kanny','Nova','Pip','Comet','Luma','Zuzu','Orbit','Bean']; const i=(names.indexOf(P.name)+1)%names.length; P.name=n&&P.name!==n?n.split(' ')[0]+'’s star':names[i]; putLS(K,P); F.msg('Now called '+P.name+'. Tap again for another name.'); }]],
   reset(F){ decay(); F.score=P.xp; },
   pointer(F,t,x,y){ if(t!=='down') return; if(ball&&Math.hypot(x-ball.x,y-ball.y)<36){ catches++; F.snd(700+catches*80,.05); ball.vx*=1.15; ball.vy*=1.15; if(catches>=5){ ball=null; care('f',35,10,'What a game! '+P.name+' had fun.',990); P.e=cl(P.e-8,0,100); putLS(K,P); } } else if(!ball){ F.msg(['❤','✨','😊','🎵'][rnd(4)]+' '+P.name+' loves that.'); P.f=cl(P.f+1,0,100); putLS(K,P); } },
   update(F,dt){ bob+=dt; if(Math.floor(F.t)%5===0) decay(); if(ball){ ball.x+=ball.vx*dt; ball.y+=ball.vy*dt; if(ball.x<20||ball.x>F.W-20) ball.vx*=-1; if(ball.y<40||ball.y>F.H-20) ball.vy*=-1; ball.x=cl(ball.x,20,F.W-20); ball.y=cl(ball.y,40,F.H-20); } F.score=P.xp; },
   draw(F){ const g=F.g; const s=stage(); g.fillStyle=P.asleep?'#0a0a2a':'#1a1450'; g.fillRect(0,0,F.W,F.H); const cx=F.W/2, cy=F.H*0.48+Math.sin(bob*2)*4, R=Math.min(F.W,F.H)*(0.12+s*0.025);
    const low=Math.min(P.h,P.f,P.e,P.c); const mood=low<15?'sad':low<40?'meh':'happy';
    if(s===0){ g.fillStyle='#fff3c4'; g.beginPath(); g.ellipse(cx,cy,R*.8,R,0,0,7); g.fill(); g.strokeStyle='#ffe94a'; g.lineWidth=3; g.stroke(); g.fillStyle='#c38bff'; g.font='bold 14px system-ui'; g.textAlign='center'; g.fillText('egg · '+Math.max(0,40-P.xp)+' care points to hatch',cx,cy+R+26); }
    else { g.fillStyle=['','#ffd166','#ffe94a','#ffb703','#fff'][s]; g.beginPath(); for(let i=0;i<10;i++){ const a=-Math.PI/2+i*Math.PI/5, rad=i%2?R*.55:R; g.lineTo(cx+Math.cos(a)*rad,cy+Math.sin(a)*rad); } g.closePath(); g.fill(); if(s===4){ g.shadowColor='#fff'; g.shadowBlur=30; g.fill(); g.shadowBlur=0; }
     g.fillStyle='#14102e'; if(P.asleep){ g.fillRect(cx-R*.3,cy-R*.1,R*.2,3); g.fillRect(cx+R*.1,cy-R*.1,R*.2,3); g.fillStyle='#cfd6ff'; g.font='bold 20px system-ui'; g.fillText('z z z',cx+R,cy-R); } else { g.beginPath(); g.arc(cx-R*.2,cy-R*.1,R*.08,0,7); g.arc(cx+R*.2,cy-R*.1,R*.08,0,7); g.fill(); g.strokeStyle='#14102e'; g.lineWidth=3; g.beginPath(); if(mood==='happy') g.arc(cx,cy+R*.05,R*.2,0.2,Math.PI-0.2); else if(mood==='meh'){ g.moveTo(cx-R*.15,cy+R*.15); g.lineTo(cx+R*.15,cy+R*.15); } else g.arc(cx,cy+R*.3,R*.18,Math.PI+0.3,-0.3); g.stroke(); } }
    g.textAlign='center'; g.fillStyle='#fff'; g.font='bold 16px system-ui'; g.fillText(P.name+' · '+STAGES[s][0]+(P.asleep?' · asleep':''),cx,52);
    [['🍎 Food',P.h],['🎾 Fun',P.f],['⚡ Energy',P.e],['🛁 Clean',P.c]].forEach(([n,v],i)=>{ const bw=(F.W-50)/4, x=10+i*(bw+10), y=F.H-34; g.fillStyle='rgba(255,255,255,.15)'; g.fillRect(x,y,bw,12); g.fillStyle=v<20?'#ff4f6d':v<50?'#ffe94a':'#7cff8a'; g.fillRect(x,y,bw*v/100,12); g.fillStyle='#fff'; g.font='12px system-ui'; g.textAlign='left'; g.fillText(n+' '+Math.round(v),x,y-4); });
    if(ball){ g.fillStyle='#ff7ad9'; g.beginPath(); g.arc(ball.x,ball.y,16,0,7); g.fill(); g.fillStyle='#fff'; g.font='12px system-ui'; g.textAlign='center'; g.fillText(catches+'/5',ball.x,ball.y+4); } },
   hud:F=>'Care points '+P.xp+' · '+STAGES[stage()][0]});
  return {state:()=>({xp:P.xp,stage:stage(),h:Math.round(P.h)})}; });

 /* 8 · RUNE DUEL: a card battle against the Oracle */
 reg('m_duel','Rune Duel','A card battle against the Oracle. Each turn you get one more mana (up to ten) and draw a card. Tap a card you can pay for to play it: strikes and spells hurt, shields soak damage, heals mend. Press End turn when you are done. Bring the Oracle from 30 to 0 before it does the same to you. Keys: 1 to 5 play a card, E ends the turn.',ctx=>{
  const POOL=[['Strike',1,'dmg',3,'⚔'],['Twin Strike',2,'dmg2',2,'⚔⚔'],['Lightning',2,'dmg',4,'⚡'],['Fireball',3,'dmg',6,'🔥'],['Comet',5,'dmg',10,'☄'],['Shield',1,'arm',4,'🛡'],['Frost Ward',2,'arm',6,'❄'],['Heal',2,'heal',5,'✚'],['Drain',3,'drain',3,'🌙'],['Star Mana',0,'mana',1,'★']];
  let me, ai, turn, cards, msgT, over2;
  const mkSide=()=>({hp:30,arm:0,mana:0,max:0,hand:[],deck:Array.from({length:24},()=>POOL[rnd(POOL.length)])});
  const draw1=s=>{ if(s.deck.length&&s.hand.length<6) s.hand.push(s.deck.pop()); };
  const F=frame(ctx,'m_duel',{ratio:0.95,maxW:640,title:'Rune Duel',go:'Your turn: play a card.',hint:'Press ▶ Start to duel the Oracle.',
   buttons:F=>[['⏭ End turn',()=>endTurn()]],
   reset(F){ me=mkSide(); ai=mkSide(); for(let i=0;i<4;i++){ draw1(me); draw1(ai); } turn='me'; me.max=1; me.mana=1; over2=false; },
   pointer(F,t,x,y){ if(t!=='down'||turn!=='me') return; const i=cardAt(x,y); if(i>=0) play(me,ai,i); },
   key(F,e,d){ if(!d) return false; if(/^[1-6]$/.test(e.key)){ if(turn==='me') play(me,ai,+e.key-1); return true; } if(e.key==='e'||e.key==='E'){ endTurn(); return true; } return false; },
   update(F,dt){ if(turn==='ai'&&F.t>msgT) aiStep(); },
   draw(F){ const g=F.g; g.fillStyle='#160d2e'; g.fillRect(0,0,F.W,F.H); const side=(s,y,name,icon)=>{ g.fillStyle='rgba(255,255,255,.08)'; g.fillRect(10,y,F.W-20,52); g.fillStyle='#fff'; g.font='bold 16px system-ui'; g.textAlign='left'; g.fillText(icon+' '+name,20,y+22); g.font='14px system-ui'; g.fillText('❤ '+s.hp+'   🛡 '+s.arm+'   💧 '+s.mana+'/'+s.max+'   🂠 '+s.deck.length,20,y+42); g.fillStyle='#ff4f6d'; g.fillRect(F.W*0.55,y+14,F.W*0.4*Math.max(0,s.hp)/30,10); g.strokeStyle='#fff'; g.strokeRect(F.W*0.55,y+14,F.W*0.4,10); };
    side(ai,32,'The Oracle','🔮'); g.fillStyle='#c38bff'; g.font='14px system-ui'; g.textAlign='left'; g.fillText('Oracle holds '+ai.hand.length+' cards',20,104);
    g.fillStyle='#ffe94a'; g.font='bold 15px system-ui'; g.textAlign='center'; g.fillText(turn==='me'?'Your turn':'The Oracle is thinking…',F.W/2,F.H*0.42);
    side(me,F.H-200,'You','🧭');
    cards=[]; const n=me.hand.length, cw=Math.min(100,(F.W-20)/Math.max(n,1)-8), ch=cw*1.35, y=F.H-140; me.hand.forEach((c,i)=>{ const x=10+i*(cw+8); cards.push([x,y,cw,ch]); const can=turn==='me'&&c[1]<=me.mana; g.fillStyle=can?'#2a2f7a':'#2a2340'; rrect(g,x,y,cw,ch,8); g.fill(); g.strokeStyle=can?'#ffe94a':'#555'; g.lineWidth=2; g.stroke(); g.fillStyle='#6fe8ff'; g.font='bold 14px system-ui'; g.textAlign='left'; g.fillText('💧'+c[1],x+6,y+18); g.textAlign='center'; g.font=Math.round(cw*.32)+'px system-ui'; g.fillText(c[4],x+cw/2,y+ch*.52); g.fillStyle='#fff'; g.font='bold '+Math.round(Math.max(10,cw*.12))+'px system-ui'; g.fillText(c[0],x+cw/2,y+ch*.78); g.font=Math.round(Math.max(9,cw*.11))+'px system-ui'; g.fillStyle='#cfd6ff'; g.fillText(desc(c),x+cw/2,y+ch*.92); g.fillStyle='#ffe94a'; g.textAlign='left'; g.fillText(String(i+1),x+cw-14,y+18); }); },
   hud:F=>'Wins '+F.score});
  function desc(c){ return c[2]==='dmg'?c[3]+' damage':c[2]==='dmg2'?'2 × '+c[3]:c[2]==='arm'?'+'+c[3]+' shield':c[2]==='heal'?'+'+c[3]+' life':c[2]==='drain'?c[3]+' dmg, +'+c[3]+' life':'+1 mana'; }
  function cardAt(x,y){ for(let i=0;i<(cards||[]).length;i++){ const [a,b,w,hh]=cards[i]; if(x>=a&&x<=a+w&&y>=b&&y<=b+hh) return i; } return -1; }
  function hit(t,n){ const s=Math.min(t.arm,n); t.arm-=s; t.hp-=n-s; }
  function play(s,o,i){ const c=s.hand[i]; if(!c||over2) return false; if(c[1]>s.mana){ if(s===me) F.msg('Not enough mana for '+c[0]+'.'); return false; } s.mana-=c[1]; s.hand.splice(i,1);
   if(c[2]==='dmg') hit(o,c[3]); else if(c[2]==='dmg2'){ hit(o,c[3]); hit(o,c[3]); } else if(c[2]==='arm') s.arm=Math.min(15,s.arm+c[3]); else if(c[2]==='heal') s.hp=Math.min(30,s.hp+c[3]); else if(c[2]==='drain'){ hit(o,c[3]); s.hp=Math.min(30,s.hp+c[3]); } else if(c[2]==='mana') s.mana+=1;
   F.snd(s===me?660:330,.06); F.msg((s===me?'You played ':'The Oracle played ')+c[0]+'.'); check(); return true; }
  function check(){ if(ai.hp<=0&&!over2){ over2=true; F.add(1); F.end('You beat the Oracle with '+me.hp+' life left!'); } else if(me.hp<=0&&!over2){ over2=true; F.end('The Oracle won this duel.'); } }
  function endTurn(){ if(turn!=='me'||over2||!F.running) return; turn='ai'; ai.max=Math.min(10,ai.max+1); ai.mana=ai.max; draw1(ai); msgT=F.t+0.7; }
  function aiStep(){ if(over2) return; const opts=ai.hand.map((c,i)=>({c,i})).filter(o=>o.c[1]<=ai.mana); if(opts.length){ const val=c=>c[2]==='heal'?(ai.hp<15?9:1):c[2]==='arm'?(me.hand.length>2?3:1):c[2]==='mana'?2:(c[3]*(c[2]==='dmg2'?2:1)+(me.hp<=c[3]?50:0)); opts.sort((a,b)=>val(b.c)-val(a.c)); play(ai,me,opts[0].i); msgT=F.t+0.8; return; }
   turn='me'; me.max=Math.min(10,me.max+1); me.mana=me.max; draw1(me); F.msg('Your turn.'); if(!me.hand.length&&!me.deck.length) F.end('You ran out of cards.'); }
  return {state:()=>({me:me.hp,ai:ai.hp,turn})}; });

 /* 9 · CRYPT CRAWL: a turn-based dungeon of floors */
 reg('m_crypt','Crypt Crawl','Explore the crypt one step at a time. Walk into a monster to fight it; monsters move when you move. Potions (✚) heal, gold (◆) scores, and the stairs (▼) take you a floor deeper, where the monsters are tougher and you grow stronger. Arrows or swipes move; tap a square next to you to step there.',ctx=>{
  const CW=17, CH=12; let map, seen, hero, mons, items, floor, stairs, log, sx0, sy0;
  const MT=[['🦇','Bat',4,2],['🟢','Slime',7,2],['💀','Skeleton',10,3],['👹','Ogre',16,5],['🐉','Wyrm',26,7]];
  const F=frame(ctx,'m_crypt',{ratio:0.75,title:'Crypt Crawl',go:'Find the stairs.',hint:'Press ▶ Start, then move with arrows or swipes.',
   reset(F){ floor=1; hero={x:0,y:0,hp:20,max:20,atk:4,xp:0,lv:1}; gen(); },
   pointer(F,t,x,y){ const cs=Math.min(F.W/CW,(F.H-28)/CH); if(t==='down'){ sx0=x; sy0=y; } else if(t==='up'){ const dx=x-sx0, dy=y-sy0; if(Math.abs(dx)+Math.abs(dy)>20){ Math.abs(dx)>Math.abs(dy)?step(Math.sign(dx),0):step(0,Math.sign(dy)); } else { const c=Math.floor(x/cs), r=Math.floor((y-28)/cs); const ddx=c-hero.x, ddy=r-hero.y; if(Math.abs(ddx)+Math.abs(ddy)===1) step(ddx,ddy); else if(ddx||ddy) Math.abs(ddx)>Math.abs(ddy)?step(Math.sign(ddx),0):step(0,Math.sign(ddy)); } } },
   key(F,e,d){ if(!d) return false; const m={ArrowUp:[0,-1],ArrowDown:[0,1],ArrowLeft:[-1,0],ArrowRight:[1,0]}[e.key]; if(m){ step(m[0],m[1]); return true; } return false; },
   draw(F){ const g=F.g; const cs=Math.min(F.W/CW,(F.H-28)/CH), ox=(F.W-cs*CW)/2; g.fillStyle='#07060f'; g.fillRect(0,0,F.W,F.H); g.textAlign='center'; g.textBaseline='middle';
    for(let y=0;y<CH;y++) for(let x=0;x<CW;x++){ if(!seen[y][x]) continue; const vis=Math.hypot(x-hero.x,y-hero.y)<=4.5; g.globalAlpha=vis?1:0.4; g.fillStyle=map[y][x]?'#2b2440':'#120f20'; g.fillRect(ox+x*cs,28+y*cs,cs-1,cs-1); if(stairs.x===x&&stairs.y===y){ g.fillStyle='#ffe94a'; g.font=Math.round(cs*.7)+'px system-ui'; g.fillText('▼',ox+x*cs+cs/2,28+y*cs+cs/2); } }
    items.forEach(it=>{ if(!seen[it.y][it.x]) return; g.globalAlpha=Math.hypot(it.x-hero.x,it.y-hero.y)<=4.5?1:0.4; g.fillStyle=it.k==='p'?'#7cff8a':'#6fe8ff'; g.font='bold '+Math.round(cs*.6)+'px system-ui'; g.fillText(it.k==='p'?'✚':'◆',ox+it.x*cs+cs/2,28+it.y*cs+cs/2); });
    g.globalAlpha=1; mons.forEach(m=>{ if(Math.hypot(m.x-hero.x,m.y-hero.y)>4.5) return; g.font=Math.round(cs*.7)+'px system-ui'; g.fillText(m.t[0],ox+m.x*cs+cs/2,28+m.y*cs+cs/2); g.fillStyle='#000'; g.fillRect(ox+m.x*cs+2,28+m.y*cs+2,cs-4,3); g.fillStyle='#ff4f6d'; g.fillRect(ox+m.x*cs+2,28+m.y*cs+2,(cs-4)*m.hp/m.max,3); });
    g.fillStyle='#fff'; g.beginPath(); g.arc(ox+hero.x*cs+cs/2,28+hero.y*cs+cs/2,cs*.36,0,7); g.fill(); g.fillStyle='#2a2f7a'; g.font='bold '+Math.round(cs*.5)+'px system-ui'; g.fillText('@',ox+hero.x*cs+cs/2,28+hero.y*cs+cs/2+1); g.textBaseline='alphabetic'; },
   hud:F=>'❤ '+hero.hp+'/'+hero.max+' · ⚔ '+hero.atk+' · lv '+hero.lv+' · floor '+floor+' · score '+F.score});
  function gen(){ map=Array.from({length:CH},()=>Array(CW).fill(0)); seen=Array.from({length:CH},()=>Array(CW).fill(false)); const rooms=[]; for(let t=0;t<40&&rooms.length<6;t++){ const w=3+rnd(4), hh=2+rnd(3), x=1+rnd(CW-w-1), y=1+rnd(CH-hh-1); if(rooms.some(r=>x<r.x+r.w+1&&x+w+1>r.x&&y<r.y+r.h+1&&y+hh+1>r.y)) continue; rooms.push({x,y,w,h:hh}); for(let yy=y;yy<y+hh;yy++) for(let xx=x;xx<x+w;xx++) map[yy][xx]=1; }
   for(let i=1;i<rooms.length;i++){ const a=rooms[i-1], b=rooms[i]; let x=a.x+(a.w>>1), y=a.y+(a.h>>1); const tx=b.x+(b.w>>1), ty=b.y+(b.h>>1); while(x!==tx){ map[y][x]=1; x+=Math.sign(tx-x); } while(y!==ty){ map[y][x]=1; y+=Math.sign(ty-y); } map[y][x]=1; }
   const free=()=>{ for(let t=0;t<500;t++){ const r=pick(rooms), x=r.x+rnd(r.w), y=r.y+rnd(r.h); if(map[y][x]&&!(x===hero.x&&y===hero.y)&&!mons.some(m=>m.x===x&&m.y===y)&&!items.some(i=>i.x===x&&i.y===y)&&!(stairs&&stairs.x===x&&stairs.y===y)) return {x,y}; } return {x:rooms[0].x,y:rooms[0].y}; };
   const r0=rooms[0]; hero.x=r0.x; hero.y=r0.y; mons=[]; items=[]; stairs=null; const last=rooms[rooms.length-1]; stairs={x:last.x+last.w-1,y:last.y+last.h-1};
   const n=3+floor; for(let i=0;i<n;i++){ const p=free(); const t=MT[Math.min(MT.length-1,rnd(Math.min(MT.length,1+Math.floor(floor/2)+1)))]; mons.push({x:p.x,y:p.y,t,hp:t[2]+floor,max:t[2]+floor,atk:t[3]+Math.floor(floor/3)}); }
   for(let i=0;i<2+rnd(3);i++){ const p=free(); items.push({x:p.x,y:p.y,k:Math.random()<.45?'p':'g'}); } look(); }
  function look(){ for(let y=0;y<CH;y++) for(let x=0;x<CW;x++) if(Math.hypot(x-hero.x,y-hero.y)<=4.5) seen[y][x]=true; }
  function step(dx,dy){ if(!F.running||F.over||F.paused) return; const nx=hero.x+dx, ny=hero.y+dy; if(nx<0||ny<0||nx>=CW||ny>=CH||!map[ny][nx]) return; const m=mons.find(q=>q.x===nx&&q.y===ny);
   if(m){ const d=hero.atk+rnd(3); m.hp-=d; F.snd(300,.04); if(m.hp<=0){ mons=mons.filter(q=>q!==m); F.add(20*floor); hero.xp+=m.t[2]; F.msg('You defeated the '+m.t[1]+'.'); if(hero.xp>=hero.lv*12){ hero.lv++; hero.max+=5; hero.hp=hero.max; hero.atk+=2; F.msg('Level up! Level '+hero.lv+': stronger and fully healed.'); F.snd(990,.15); } } else F.msg('You hit the '+m.t[1]+' for '+d+'.'); }
   else { hero.x=nx; hero.y=ny; const it=items.find(i=>i.x===nx&&i.y===ny); if(it){ items=items.filter(i=>i!==it); if(it.k==='p'){ hero.hp=Math.min(hero.max,hero.hp+8); F.msg('A potion: +8 life.'); F.snd(800,.06); } else { F.add(10*floor); F.msg('Gold!'); F.snd(1000,.04); } } if(nx===stairs.x&&ny===stairs.y){ floor++; F.add(100*floor); F.msg('Down to floor '+floor+'.'); F.snd(500,.15); gen(); return; } }
   mons.forEach(q=>{ const ddx=hero.x-q.x, ddy=hero.y-q.y; if(Math.abs(ddx)+Math.abs(ddy)===1){ const d=Math.max(1,q.atk-0+rnd(2)); hero.hp-=d; F.snd(150,.05); F.msg('The '+q.t[1]+' hits you for '+d+'.'); } else if(Math.hypot(ddx,ddy)<6){ const opts=Math.abs(ddx)>Math.abs(ddy)?[[Math.sign(ddx),0],[0,Math.sign(ddy)]]:[[0,Math.sign(ddy)],[Math.sign(ddx),0]]; for(const [ax,ay] of opts){ const tx=q.x+ax, ty=q.y+ay; if((ax||ay)&&map[ty]&&map[ty][tx]&&!mons.some(o=>o.x===tx&&o.y===ty)&&!(tx===hero.x&&ty===hero.y)){ q.x=tx; q.y=ty; break; } } } });
   look(); if(hero.hp<=0){ hero.hp=0; F.end('You fell on floor '+floor+'.'); } }
  return {state:()=>({hp:hero.hp,floor,score:F.score})}; });

 /* 10 · NEON KART: three laps against three rivals */
 reg('m_kart','Neon Kart','Race three laps around the neon track against three rivals. Your kart speeds up by itself; steer with Left and Right (or hold the left or right half of the track). Stay on the road: the grass slows you. Blue boost pads give a burst of speed. Finish first for the most points.',ctx=>{
  let P, karts, cps, track, lap, done, place, tw, boosts, startT, cdown;
  const F=frame(ctx,'m_kart',{ratio:0.68,title:'Neon Kart',go:'Race!',hint:'Press ▶ Start: three laps, steer with Left/Right.',
   reset(F){ const W=F.W, H=F.H; const cx=W/2, cy=28+(H-28)/2, rx=W*0.4, ry=(H-28)*0.38; track=[]; for(let i=0;i<64;i++){ const a=i/64*Math.PI*2; const wob=1+0.18*Math.sin(a*3); track.push([cx+Math.cos(a)*rx*wob,cy+Math.sin(a)*ry*(1+0.12*Math.cos(a*2))]); } tw=Math.max(34,Math.min(W,H)*0.11); boosts=[16,48];
    const mk=(i,c,ai)=>{ const p=track[0], q=track[1], a=Math.atan2(q[1]-p[1],q[0]-p[0]); const side=(i%2?1:-1)*tw*0.22, back=Math.floor(i/2)*22; return {x:p[0]-Math.cos(a)*back+Math.cos(a+Math.PI/2)*side,y:p[1]-Math.sin(a)*back+Math.sin(a+Math.PI/2)*side,a,v:0,c,ai,idx:0,laps:0,prog:0,skill:rr(.86,.97),fin:0}; };
    karts=[mk(0,'#ffe94a',false),mk(1,'#ff4f6d',true),mk(2,'#6fe8ff',true),mk(3,'#7cff8a',true)]; P=karts[0]; done=false; startT=F.t; cdown=2.5; },
   pointer(F,t,x){ },
   update(F,dt){ if(cdown>0){ cdown-=dt; if(cdown<=0) F.snd(880,.15); return; } const steerTouch=F.down?(F.px<F.W/2?-1:1):0; karts.forEach(k=>{ if(k.fin) { k.v*=0.98; } let st=0;
     if(!k.ai){ st=(F.keys.ArrowLeft?-1:0)+(F.keys.ArrowRight?1:0)+steerTouch; } else { const tg=track[(k.idx+4)%track.length]; let d=Math.atan2(tg[1]-k.y,tg[0]-k.x)-k.a; while(d>Math.PI) d-=Math.PI*2; while(d<-Math.PI) d+=Math.PI*2; st=cl(d*3,-1,1); }
     const off=dist(k)>tw/2; const top=(k.ai?240*k.skill:250)*(off?0.45:1)*(k.boost>0?1.6:1); k.boost=(k.boost||0)-dt; k.v+=(top-k.v)*dt*1.6; if(!k.fin) k.a+=st*dt*2.6*(0.4+k.v/300); k.x+=Math.cos(k.a)*k.v*dt; k.y+=Math.sin(k.a)*k.v*dt;
     const near=nearest(k); if(boosts.includes(near)&&!off&&!(k.lastB===near)){ k.boost=1.1; k.lastB=near; if(!k.ai) F.snd(990,.08); } if(!boosts.includes(near)) k.lastB=null;
     const n=track.length; let d=near-k.idx; if(d<-n/2) d+=n; if(d>n/2) d-=n; if(d>0&&d<8){ if(near<k.idx&&k.idx>n-8){ k.laps++; if(!k.ai&&k.laps<3) { F.msg('Lap '+(k.laps+1)+' of 3.'); F.snd(700,.08); } if(k.laps>=3&&!k.fin){ k.fin=F.t; } } k.idx=near; } k.prog=k.laps*n+k.idx; });
    for(let i=0;i<karts.length;i++) for(let j=i+1;j<karts.length;j++){ const a=karts[i], b=karts[j], dx=b.x-a.x, dy=b.y-a.y, d=Math.hypot(dx,dy); if(d<16&&d>0){ const push=(16-d)/2; a.x-=dx/d*push; a.y-=dy/d*push; b.x+=dx/d*push; b.y+=dy/d*push; } }
    if(P.fin&&!done){ done=true; const pl=1+karts.filter(k=>k!==P&&k.fin&&k.fin<P.fin).length; const t=(P.fin-startT-2.5).toFixed(1); F.add([0,3000,2000,1200,600][pl]+Math.max(0,Math.round((120-t)*10))); F.end('Finished '+['','1st','2nd','3rd','4th'][pl]+' in '+t+' s.'); } },
   draw(F){ const g=F.g; g.fillStyle='#0b2a14'; g.fillRect(0,0,F.W,F.H); g.lineJoin='round'; g.lineCap='round'; const path=()=>{ g.beginPath(); track.forEach((p,i)=>i?g.lineTo(p[0],p[1]):g.moveTo(p[0],p[1])); g.closePath(); };
    g.strokeStyle='#ff7ad9'; g.lineWidth=tw+8; path(); g.stroke(); g.strokeStyle='#2a2440'; g.lineWidth=tw; path(); g.stroke(); g.strokeStyle='rgba(255,255,255,.18)'; g.setLineDash([10,14]); g.lineWidth=2; path(); g.stroke(); g.setLineDash([]);
    boosts.forEach(b=>{ const p=track[b]; g.fillStyle='#4fb3ff'; g.beginPath(); g.arc(p[0],p[1],tw*.28,0,7); g.fill(); g.fillStyle='#fff'; g.font='bold 14px system-ui'; g.textAlign='center'; g.fillText('»',p[0],p[1]+5); });
    const s=track[0], s2=track[1], a=Math.atan2(s2[1]-s[1],s2[0]-s[0]); g.save(); g.translate(s[0],s[1]); g.rotate(a+Math.PI/2); for(let i=-3;i<3;i++){ g.fillStyle=i%2?'#fff':'#000'; g.fillRect(i*tw/6,-4,tw/6,8); } g.restore();
    karts.forEach(k=>{ g.save(); g.translate(k.x,k.y); g.rotate(k.a); g.fillStyle=k.c; rrect(g,-10,-6,20,12,3); g.fill(); g.fillStyle='#111'; g.fillRect(-8,-8,5,3); g.fillRect(3,-8,5,3); g.fillRect(-8,5,5,3); g.fillRect(3,5,5,3); if(k.boost>0){ g.fillStyle='#4fb3ff'; g.fillRect(-16,-3,6,6); } g.restore(); });
    if(cdown>0){ g.fillStyle='#ffe94a'; g.font='bold 48px system-ui'; g.textAlign='center'; g.fillText(cdown>1.7?'3':cdown>0.9?'2':'1',F.W/2,F.H/2+16); } },
   hud:F=>{ const pl=1+karts.filter(k=>k!==P&&k.prog>P.prog).length; return 'Lap '+Math.min(3,P.laps+1)+'/3 · place '+pl+'/4 · '+Math.max(0,F.t-startT-2.5).toFixed(1)+' s'; }});
  function nearest(k){ let b=0, bd=1e9; for(let i=0;i<track.length;i++){ const d=(track[i][0]-k.x)**2+(track[i][1]-k.y)**2; if(d<bd){ bd=d; b=i; } } return b; }
  function dist(k){ let bd=1e9; for(let i=0;i<track.length;i++){ const p=track[i], q=track[(i+1)%track.length]; const dx=q[0]-p[0], dy=q[1]-p[1]; let t=((k.x-p[0])*dx+(k.y-p[1])*dy)/(dx*dx+dy*dy); t=cl(t,0,1); const d=Math.hypot(k.x-p[0]-dx*t,k.y-p[1]-dy*t); if(d<bd) bd=d; } return bd; }
  return {state:()=>({lap:P.laps,prog:P.prog,v:Math.round(P.v)})}; });

 /* 11 · MERGE MOONS: slide and merge, from pebbles to a galaxy */
 reg('m_merge','Merge Moons','Slide every tile on the board in one direction. Two matching bodies that meet merge into the next one up: pebble, rock, moonlet, moon, Mars, Earth, Neptune, Saturn, Jupiter, star, Sun, galaxy. Each move brings a new pebble. Make the Sun to win, then keep going. Arrows or swipes.',ctx=>{
  const N=4, NM=['','Pebble','Rock','Moonlet','Moon','Mars','Earth','Neptune','Saturn','Jupiter','Star','Sun','Galaxy','Nebula','Cosmos'], CL=['','#8d8d9a','#a88f6a','#c7c7d6','#e8e8f0','#d9653b','#3b82d9','#4f6bd9','#d9b36a','#c98a52','#ffe94a','#ff9a3c','#c38bff','#ff7ad9','#6fe8ff'];
  let b, won, sx0, sy0, anim;
  const F=frame(ctx,'m_merge',{ratio:1.08,maxW:520,title:'Merge Moons',go:'Slide to merge.',hint:'Press ▶ Start, then swipe or use the arrows.',
   reset(F){ b=Array.from({length:N},()=>Array(N).fill(0)); won=false; add(); add(); anim=0; },
   pointer(F,t,x,y){ if(t==='down'){ sx0=x; sy0=y; } else if(t==='up'){ const dx=x-sx0, dy=y-sy0; if(Math.max(Math.abs(dx),Math.abs(dy))<24) return; Math.abs(dx)>Math.abs(dy)?move(dx>0?'R':'L'):move(dy>0?'D':'U'); } },
   key(F,e,d){ if(!d) return false; const m={ArrowLeft:'L',ArrowRight:'R',ArrowUp:'U',ArrowDown:'D'}[e.key]; if(m){ move(m); return true; } return false; },
   update(F,dt){ anim=Math.max(0,anim-dt*6); },
   draw(F){ const g=F.g; const S=Math.min(F.W,F.H-34)-16, cs=S/N, ox=(F.W-S)/2, oy=30; g.fillStyle='#120c2c'; g.fillRect(0,0,F.W,F.H); g.fillStyle='#211a48'; rrect(g,ox-6,oy-6,S+12,S+12,12); g.fill();
    for(let r=0;r<N;r++) for(let c=0;c<N;c++){ const v=b[r][c], x=ox+c*cs+4, y=oy+r*cs+4, w=cs-8; g.fillStyle=v?'#2a2260':'#1a1440'; rrect(g,x,y,w,w,10); g.fill(); if(!v) continue; const s=v>=13?1:(0.5+v*0.04); g.fillStyle=CL[Math.min(v,14)]; g.beginPath(); g.arc(x+w/2,y+w*.44,w*.32*s,0,7); g.fill(); if(v===8){ g.strokeStyle='#f3d8a0'; g.lineWidth=3; g.beginPath(); g.ellipse(x+w/2,y+w*.44,w*.42,w*.1,-.3,0,7); g.stroke(); } g.fillStyle='#fff'; g.font='bold '+Math.round(w*.15)+'px system-ui'; g.textAlign='center'; g.fillText(NM[Math.min(v,14)],x+w/2,y+w*.9); } },
   hud:F=>'Score '+F.score+(won?' · ☀ Sun made!':'')});
  function add(){ const e=[]; for(let r=0;r<N;r++) for(let c=0;c<N;c++) if(!b[r][c]) e.push([r,c]); if(!e.length) return; const [r,c]=pick(e); b[r][c]=Math.random()<0.9?1:2; }
  function line(i,d){ const out=[]; for(let k=0;k<N;k++){ if(d==='L') out.push([i,k]); if(d==='R') out.push([i,N-1-k]); if(d==='U') out.push([k,i]); if(d==='D') out.push([N-1-k,i]); } return out; }
  function move(d){ if(!F.running||F.over) return; let moved=false; for(let i=0;i<N;i++){ const cells=line(i,d); const vals=cells.map(([r,c])=>b[r][c]).filter(Boolean); const res=[]; for(let k=0;k<vals.length;k++){ if(k+1<vals.length&&vals[k]===vals[k+1]){ const nv=vals[k]+1; res.push(nv); F.add(Math.pow(2,nv)); if(nv===11&&!won){ won=true; F.msg('You made the Sun! Keep going for a galaxy.'); F.snd(990,.25); } k++; } else res.push(vals[k]); } while(res.length<N) res.push(0); cells.forEach(([r,c],k)=>{ if(b[r][c]!==res[k]){ moved=true; b[r][c]=res[k]; } }); }
   if(moved){ add(); F.snd(500,.03); anim=1; if(!canMove()) F.end('No moves left.'); } }
  function canMove(){ for(let r=0;r<N;r++) for(let c=0;c<N;c++){ if(!b[r][c]) return true; if(c<N-1&&b[r][c]===b[r][c+1]) return true; if(r<N-1&&b[r][c]===b[r+1][c]) return true; } return false; }
  return {state:()=>({score:F.score,max:Math.max(...b.flat())})}; });
})();
