(()=>{ /* THE LOGO CANNON FIRES (v199). Its bullet is one die, like every cannon's; it lands in a starburst. The little cannon between KAN and IN never kicks without firing: one clock drives the kick and
   the shot together. Each kick is a real shot: a muzzle flash and smoke, a die on a live arc out of the barrel, and a starburst
   where it lands, like every cannon's hit. Tap the
   cannon to fire it by hand. Nothing fires while the opening game is up, while a screen covers the cannon, with effects off, or
   for people who ask their device for reduced motion. Silent: one sound at a time stays the rule. */
 const GL='ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ', LIMBS=['Story','Beat','Compass','Zodiac','Games','Voice','Film','Clock'];
 const css=document.createElement('style'); css.textContent='html body .hycannon{animation:none!important;cursor:pointer;pointer-events:auto}#kShotCv{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:35}'; document.head.appendChild(css);
 let reduce={matches:false}; try{ reduce=matchMedia('(prefers-reduced-motion: reduce)'); }catch(_){ }
 let cv=null, g=null, dpr=1, parts=[], shells=[], tags=[], raf=0, shot=0, last=0;
 function size(){ if(!cv) return; dpr=Math.min(2,window.devicePixelRatio||1); cv.width=Math.round(innerWidth*dpr); cv.height=Math.round(innerHeight*dpr); }
 function ensure(){ if(cv&&cv.isConnected) return; cv=document.createElement('canvas'); cv.id='kShotCv'; cv.setAttribute('aria-hidden','true'); document.body.appendChild(cv); g=cv.getContext('2d'); size(); }
 addEventListener('resize',size);
 const cannon=()=>document.querySelector('.hycannon');
 const railW=()=>parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58;
 function clear(c,byHand){ if(!c||document.hidden) return false; if(!byHand&&reduce.matches) return false; if(document.body.classList.contains('gated')) return false; if(document.documentElement.dataset.fx==='off'&&!byHand) return false;
  if(!c.getClientRects().length) return false; const r=c.getBoundingClientRect(); if(r.width<8||r.bottom<0||r.top>innerHeight) return false;
  const e=document.elementFromPoint(r.left+r.width*0.5,r.top+r.height*0.5); return !!(e&&(e===c||c.contains(e)||(e.closest&&e.closest('.hy,.kwmH1')))); }
 function letter(i){ try{ const s=UNILAW.state(); const L=s&&s.letters; if(L&&L[i]) return L[i]; }catch(_){ } return GL[(i*7+new Date().getHours())%24]; }
 function fire(byHand){ const c=cannon(); if(!clear(c,byHand)) return false; ensure(); const r=c.getBoundingClientRect(), now=performance.now(); last=now;
  const mx=r.left+r.width*0.83, my=r.top+r.height*0.5, k=r.width/56;
  try{ c.animate([{transform:'translateX(0)'},{transform:'translateX('+(-Math.max(2,r.width*0.08))+'px) rotate(-2deg)',offset:.16},{transform:'translateX(0)'}],{duration:420,easing:'cubic-bezier(.2,.8,.3,1)'}); }catch(_){ }
  /* the shot: a parabola that lands at the muzzle's height, as far as the space before the rail allows */
  const room=Math.max(60,innerWidth-railW()-16-mx), dist=Math.max(50,Math.min(330*Math.max(.7,k),room*0.75)), T=0.85, h=Math.min(70,dist*0.32);
  shells.push({x0:mx,y0:my,dist,h,T,t0:now,trail:[],r:Math.max(3,4.2*k),limb:shot%8,f:1+Math.floor(Math.random()*6),spin:(Math.random()<.5?-1:1)*(9+Math.random()*7)});
  parts.push({kind:'flash',x:mx,y:my,t0:now,life:140,r:Math.max(10,16*k)});
  for(let i=0;i<9;i++) parts.push({kind:'smoke',x:mx,y:my,vx:(30+Math.random()*70)*k,vy:(-25-Math.random()*40)*k,t0:now,life:700+Math.random()*500,r:(4+Math.random()*6)*k});
  shot++; if(!raf) raf=requestAnimationFrame(loop); return true; }
 function burst(x,y,limb,k,now,f){ const cols=['#ffe94a','#ff6ad5','#6fe8ff','#b48cff','#7dff8a','#ffa94d','#ff5a5a','#ffffff'];
  for(let i=0;i<26;i++){ const a=Math.PI*2*i/26+Math.random()*0.2, sp=(90+Math.random()*170)*k; parts.push({kind:'spark',x,y,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp,t0:now,life:520+Math.random()*380,c:cols[(i+limb)%cols.length]}); }
  parts.push({kind:'ring',x,y,t0:now,life:520,r:6*k,c:cols[limb%cols.length]});
  /* the hit is a plain starburst: no number over it */ }
 function loop(now){ raf=0; if(!g) return; g.setTransform(dpr,0,0,dpr,0,0); g.clearRect(0,0,innerWidth,innerHeight);
  shells=shells.filter(s=>{ const t=Math.min(1,(now-s.t0)/1000/s.T); const x=s.x0+s.dist*t, y=s.y0-4*s.h*t*(1-t); s.trail.push([x,y]); if(s.trail.length>10) s.trail.shift();
   s.trail.forEach(([tx,ty],i)=>{ g.globalAlpha=(i+1)/s.trail.length*0.5; g.fillStyle='#ffd34a'; g.beginPath(); g.arc(tx,ty,s.r*(0.35+0.6*i/s.trail.length),0,7); g.fill(); });
   g.globalAlpha=1; /* the shell is a die: it tumbles through the arc and lands on its face */ const face=t<.85?1+((Math.floor(t*22)+s.f)%6):s.f; if(window.KDIE) KDIE(g,x,y,Math.max(11,s.r*3.2),t*s.spin,face,true); else { g.fillStyle='#fff'; g.fillRect(x-s.r*1.5,y-s.r*1.5,s.r*3,s.r*3); }
   if(t>=1){ burst(x,y,(s.limb+s.f-1)%8,s.r/4.2,now,s.f); return false; } return true; });
  parts=parts.filter(p=>{ const a=(now-p.t0)/p.life; if(a>=1) return false; const dt=(now-p.t0)/1000;
   if(p.kind==='flash'){ g.globalAlpha=1-a; const gr=g.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r); gr.addColorStop(0,'#fff'); gr.addColorStop(.4,'#ffe94a'); gr.addColorStop(1,'rgba(255,120,0,0)'); g.fillStyle=gr; g.beginPath(); g.arc(p.x,p.y,p.r,0,7); g.fill(); }
   else if(p.kind==='smoke'){ g.globalAlpha=0.35*(1-a); g.fillStyle='#d8d4f0'; g.beginPath(); g.arc(p.x+p.vx*dt,p.y+p.vy*dt,p.r*(1+a*1.8),0,7); g.fill(); }
   else if(p.kind==='spark'){ g.globalAlpha=1-a; g.strokeStyle=p.c; g.lineWidth=2; const x=p.x+p.vx*dt, y=p.y+p.vy*dt+120*dt*dt; g.beginPath(); g.moveTo(x,y); g.lineTo(x-p.vx*0.03,y-p.vy*0.03); g.stroke(); }
   else if(p.kind==='ring'){ g.globalAlpha=1-a; g.strokeStyle=p.c; g.lineWidth=2.5; g.beginPath(); g.arc(p.x,p.y,p.r+a*40,0,7); g.stroke(); }
   return true; });
  tags=tags.filter(t=>{ const a=(now-t.t0)/t.life; if(a>=1) return false; g.globalAlpha=a<.15?a/.15:1-(a-.15)/.85; g.font='900 '+Math.round(13*Math.max(.85,t.k))+'px system-ui,sans-serif'; g.textAlign='center'; g.lineWidth=3; g.strokeStyle='rgba(10,8,30,.85)'; const y=t.y-18-a*22; g.strokeText(t.txt,t.x,y); g.fillStyle='#ffe94a'; g.fillText(t.txt,t.x,y); return true; });
  g.globalAlpha=1; if(shells.length||parts.length||tags.length) raf=requestAnimationFrame(loop); else g.clearRect(0,0,innerWidth,innerHeight); }
 /* one clock: the kick and the shot are the same event (2.4 s; 4.8 s with effects on Low) */
 setInterval(()=>{ const per=document.documentElement.dataset.fx==='low'?4800:2400; if(performance.now()-last>=per-60) fire(false); },400);
 document.addEventListener('click',e=>{ const c=e.target.closest&&e.target.closest('.hycannon'); if(c){ e.preventDefault(); e.stopPropagation(); fire(true); } },true);
 window.KCANSHOT={fire:()=>fire(true),get shots(){ return shot; }};
})();
