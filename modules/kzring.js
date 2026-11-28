(()=>{ /* ♈ THE ZODIAC RING, LIVE (v256): a medallion of the twelve signs heads LuvMyZodiac, drawn by the app itself and moving with the real
   sky. Its gold rim holds the twelve sectors in their element colours (fire, earth, air, water) with each sign's symbol; inside, the Sun,
   the Moon and the eight planets stand at their true ecliptic longitudes for this minute, computed on the device by the same astronomy as
   the rest of LuvMyZodiac (℞ marks a planet in retrograde), and the Sun's sign glows. Tap a sign to open it; 🎡 spins the ring and opens
   the sign it lands on; ⏪ ⏩ step through days and ▶ returns to now. ⛶ opens the ring as its own live page, full size, with every
   planet's sign and degree and a slider a year either way. Aries 0° sits at the left and the signs run counter-clockwise, as on a chart. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const VS='︎';
 const SIGNS=[['Aries','♈','fire'],['Taurus','♉','earth'],['Gemini','♊','air'],['Cancer','♋','water'],['Leo','♌','fire'],['Virgo','♍','earth'],['Libra','♎','air'],['Scorpio','♏','water'],['Sagittarius','♐','fire'],['Capricorn','♑','earth'],['Aquarius','♒','air'],['Pisces','♓','water']];
 const ELC={fire:'#ff6b4a',earth:'#6ad38b',air:'#ffd84a',water:'#5ab8ff'};
 const BODIES=[['Sun','☉','#ffd84a'],['Moon','☽','#e8eefc'],['Mercury','☿','#c9b6ff'],['Venus','♀','#ff9ad5'],['Mars','♂','#ff6b4a'],['Jupiter','♃','#ffb86b'],['Saturn','♄','#d8c38a'],['Uranus','♅','#7fe8ff'],['Neptune','♆','#7aa8ff'],['Pluto','♇','#c08cff']];
 const FONT='"Segoe UI Symbol","Noto Sans Symbols 2","Noto Sans Symbols","DejaVu Sans","Apple Symbols",serif';
 let dayOff=0, rot=0, spin=null, hover=-1, sky=null, skyAt=0, pulse=0;
 const when=()=>new Date(Date.now()+dayOff*864e5);
 function getSky(){ const t=when(); if(sky&&Math.abs(t-skyAt)<30000) return sky; skyAt=+t; try{ sky=ZODIAC4.skyAt(t); }catch(_){ try{ sky={pos:{Sun:{lon:ZODIAC2.sunLon(ZODIAC2.jd(t))},Moon:{lon:ZODIAC2.moonLon(ZODIAC2.jd(t))}},phase:null}; }catch(__){ sky=null; } } return sky; }
 const signOf=L=>Math.floor((((L%360)+360)%360)/30);
 const ang=L=>Math.PI-(L+rot)*Math.PI/180;
 const css=document.createElement('style'); css.textContent=`
#kZRing{margin:0 0 14px;display:flex;flex-direction:column;align-items:center;gap:8px}
#kZRing canvas,#kZRingPage canvas{display:block;max-width:100%;touch-action:manipulation;cursor:pointer}
#kZRing .zrBar,#kZRingPage .zrBar{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
#kZRing .zrBar button,#kZRingPage .zrBar button{min-height:40px;padding:0 12px;border-radius:4px 12px 4px 12px;font:800 13px system-ui,sans-serif}
#kZRing .zrNow{font:700 13px system-ui,sans-serif;color:#ffd27a;text-align:center}
#kZRingPage{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9600;overflow-y:auto;background:radial-gradient(circle at 50% 30%,#1a1038,#05030f 75%);color:#f3eeff;font:15px/1.5 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 30px}
#kZRingPage[hidden]{display:none!important}
#kZRingPage .zpIn{max-width:1200px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
#kZRingPage .zpTop{padding-right:min(300px,34vw);display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
#kZRingPage h2{margin:0;font:900 clamp(20px,3.6vw,30px) system-ui,sans-serif;color:#ffd27a}
#kZRingPage .zpBody{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:14px;align-items:start}
@media (max-width:860px){#kZRingPage .zpBody{grid-template-columns:minmax(0,1fr)}}
#kZRingPage table{width:100%;border-collapse:collapse;font-size:14px}
#kZRingPage td,#kZRingPage th{padding:5px 6px;border-bottom:1px solid rgba(255,210,122,.25);text-align:left}
#kZRingPage th{color:#ffd27a}
#kZRingPage input[type=range]{width:100%;accent-color:#ffd27a}
#kZRingPage .zpNote{font-size:12.5px;opacity:.8}`; document.head.appendChild(css);
 /* drawing the medallion */
 function draw(cv,S,big){ const dpr=Math.min(2,window.devicePixelRatio||1); if(cv.width!==Math.round(S*dpr)){ cv.width=Math.round(S*dpr); cv.height=Math.round(S*dpr); cv.style.width=S+'px'; cv.style.height=S+'px'; }
  const x=cv.getContext('2d'); x.setTransform(dpr,0,0,dpr,0,0); x.clearRect(0,0,S,S); const c=S/2, R=S*.48, r1=R*.92, r2=R*.7, r3=R*.56, r4=R*.36; const sk=getSky(); const sunL=sk&&sk.pos&&sk.pos.Sun?sk.pos.Sun.lon:null; const sunS=sunL==null?-1:signOf(sunL);
  /* the medallion's ground and gold rim */
  let g=x.createRadialGradient(c,c,R*.1,c,c,R); g.addColorStop(0,'#1d1450'); g.addColorStop(1,'#07051a'); x.fillStyle=g; x.beginPath(); x.arc(c,c,R,0,7); x.fill();
  g=x.createLinearGradient(0,0,S,S); g.addColorStop(0,'#fff1b0'); g.addColorStop(.35,'#d9a630'); g.addColorStop(.6,'#ffe38a'); g.addColorStop(1,'#a8741a'); x.strokeStyle=g; x.lineWidth=R*.05; x.beginPath(); x.arc(c,c,R-R*.025,0,7); x.stroke();
  x.lineWidth=1.5; x.beginPath(); x.arc(c,c,r1,0,7); x.stroke(); x.beginPath(); x.arc(c,c,r2,0,7); x.stroke();
  /* twelve sectors */
  SIGNS.forEach(([n,gl,el],k)=>{ const a0=ang(k*30), a1=ang(k*30+30); x.beginPath(); x.arc(c,c,r1,a1,a0); x.arc(c,c,r2,a0,a1,true); x.closePath();
   const on=k===sunS, hv=k===hover; x.fillStyle=ELC[el]+(hv?'66':on?(Math.round(40+30*Math.sin(pulse))).toString(16).padStart(2,'0'):'22'); x.fill();
   x.strokeStyle='rgba(255,227,138,.55)'; x.lineWidth=1; x.beginPath(); x.moveTo(c+Math.cos(a0)*r2,c+Math.sin(a0)*r2); x.lineTo(c+Math.cos(a0)*r1,c+Math.sin(a0)*r1); x.stroke();
   const am=ang(k*30+15), rm=(r1+r2)/2; x.save(); x.translate(c+Math.cos(am)*rm,c+Math.sin(am)*rm); x.fillStyle=on||hv?'#fff':ELC[el]; x.font='700 '+Math.round(R*.13)+'px '+FONT; x.textAlign='center'; x.textBaseline='middle'; if(on){ x.shadowColor=ELC[el]; x.shadowBlur=14; } x.fillText(gl+VS,0,big?-R*.025:0); x.shadowBlur=0;
   if(big){ x.font='700 '+Math.round(R*.035)+'px system-ui,sans-serif'; x.fillStyle='rgba(255,241,200,.85)'; x.fillText(n.toUpperCase(),0,R*.075); } x.restore(); });
  /* degree ticks on the inner edge */
  x.strokeStyle='rgba(255,227,138,.6)'; for(let d=0;d<360;d+=big?1:5){ const a=ang(d), l=d%30===0?R*.06:d%10===0?R*.035:d%5===0?R*.022:R*.01; x.lineWidth=d%10===0?1.2:.7; x.beginPath(); x.moveTo(c+Math.cos(a)*r2,c+Math.sin(a)*r2); x.lineTo(c+Math.cos(a)*(r2-l),c+Math.sin(a)*(r2-l)); x.stroke(); }
  /* the bodies at their longitudes, stacked inward where they crowd */
  const P=[]; if(sk&&sk.pos) BODIES.forEach(([n,gl,col])=>{ const p=sk.pos[n]; if(p&&isFinite(p.lon)) P.push({n,gl,col,L:p.lon,retro:!!p.retro}); }); P.sort((a,b)=>a.L-b.L);
  const placed=[]; P.forEach(p=>{ let lvl=0; while(placed.some(q=>q.lvl===lvl&&Math.abs(((p.L-q.L+540)%360)-180)>180-7)) lvl++; p.lvl=lvl; placed.push(p); });
  P.forEach(p=>{ const a=ang(p.L), rr=r3-p.lvl*R*.085; x.strokeStyle=p.col+'aa'; x.lineWidth=1; x.beginPath(); x.moveTo(c+Math.cos(a)*(r2-R*.065),c+Math.sin(a)*(r2-R*.065)); x.lineTo(c+Math.cos(a)*(rr+R*.045),c+Math.sin(a)*(rr+R*.045)); x.stroke();
   x.save(); x.translate(c+Math.cos(a)*rr,c+Math.sin(a)*rr); x.fillStyle='rgba(5,3,15,.75)'; x.beginPath(); x.arc(0,0,R*.045,0,7); x.fill(); x.fillStyle=p.col; x.font='700 '+Math.round(R*.075)+'px '+FONT; x.textAlign='center'; x.textBaseline='middle'; x.fillText(p.gl+VS,0,0);
   if(p.retro){ x.font='800 '+Math.round(R*.035)+'px system-ui,sans-serif'; x.fillStyle='#ff9a9a'; x.fillText('℞',R*.05,-R*.035); } x.restore(); });
  /* the centre: what the sky says now */
  g=x.createRadialGradient(c,c,0,c,c,r4); g.addColorStop(0,'#2a1d6e'); g.addColorStop(1,'#0b0726'); x.fillStyle=g; x.beginPath(); x.arc(c,c,r4,0,7); x.fill(); x.strokeStyle='rgba(255,227,138,.7)'; x.lineWidth=1.5; x.stroke();
  x.textAlign='center'; x.textBaseline='middle'; const hs=hover>=0?SIGNS[hover]:null;
  if(hs){ x.fillStyle=ELC[hs[2]]; x.font='700 '+Math.round(R*.16)+'px '+FONT; x.fillText(hs[1]+VS,c,c-R*.08); x.fillStyle='#fff'; x.font='800 '+Math.round(R*.06)+'px system-ui,sans-serif'; x.fillText(hs[0],c,c+R*.08); x.font='600 '+Math.round(R*.038)+'px system-ui,sans-serif'; x.fillStyle='#ffd27a'; x.fillText('Tap to open',c,c+R*.17); }
  else if(sk&&sk.pos&&sk.pos.Sun){ const s=sk.pos.Sun.lon, m=sk.pos.Moon&&sk.pos.Moon.lon; x.fillStyle='#ffd84a'; x.font='800 '+Math.round(R*.062)+'px system-ui,sans-serif'; x.fillText('☉ '+SIGNS[signOf(s)][0]+' '+Math.floor(s%30)+'°',c,c-R*.1);
   if(m!=null){ x.fillStyle='#e8eefc'; x.font='700 '+Math.round(R*.05)+'px system-ui,sans-serif'; x.fillText('☽ '+SIGNS[signOf(m)][0]+' '+Math.floor(m%30)+'°'+(sk.phase&&sk.phase.illum!=null?' · '+Math.round(sk.phase.illum*100)+'%':''),c,c); }
   const t=when(); x.fillStyle='#bfb3ff'; x.font='600 '+Math.round(R*.036)+'px system-ui,sans-serif'; x.fillText((dayOff?'':'Live · ')+t.toLocaleString(undefined,{month:'short',day:'numeric',year:'numeric',hour:'numeric',minute:'2-digit'}),c,c+R*.1); }
  /* the pointer at the top, where a spin lands */
  x.fillStyle='#ffe38a'; x.beginPath(); x.moveTo(c,c-R+R*.005); x.lineTo(c-R*.035,c-R-R*.05); x.lineTo(c+R*.035,c-R-R*.05); x.closePath(); x.fill(); }
 /* which sign is under a point */
 function signAt(cv,S,ev){ const r=cv.getBoundingClientRect(); const px=(ev.clientX-r.left)*(S/r.width)-S/2, py=(ev.clientY-r.top)*(S/r.height)-S/2; const d=Math.hypot(px,py), R=S*.48; if(d<R*.36||d>R) return -1; const th=Math.atan2(py,px); const L=((Math.PI-th)*180/Math.PI-rot+720)%360; return signOf(L); }
 function openSign(k){ if(k<0) return; const s=$('zodSel'); if(s){ s.value=String(k); s.dispatchEvent(new Event('change',{bubbles:true})); s.dispatchEvent(new Event('input',{bubbles:true})); } const pg=$('kZRingPage'); if(pg&&!pg.hidden) pg.hidden=true; try{ const d=$('zodDock'); if(d&&d.hidden){ KRAIL.goTo('zodDock'); } }catch(_){ } setTimeout(()=>{ const card=$('zodCard')||$('zodSky'); if(card) card.scrollIntoView({behavior:'smooth',block:'start'}); },250); say(SIGNS[k][1]+' '+SIGNS[k][0]+' opened.'); }
 function doSpin(){ if(spin) return; const turns=720+Math.random()*720, t0=performance.now(), r0=rot, dur=2600; spin={t0,r0,turns,dur}; }
 function stepSpin(){ if(!spin) return; const k=Math.min(1,(performance.now()-spin.t0)/spin.dur); const e=1-Math.pow(1-k,3); rot=(spin.r0+spin.turns*e)%360; if(k>=1){ spin=null; /* the sign under the pointer at the top */ const L=((Math.PI-(-Math.PI/2))*180/Math.PI-rot+720)%360; const s=signOf(L); setTimeout(()=>{ rot=0; openSign(s); },500); } }
 function bar(inPage){ return '<div class="zrBar"><button type="button" data-zr="-30" data-noul title="Back 30 days">⏪ 30 d</button><button type="button" data-zr="-1" data-noul title="Back a day">◀ 1 d</button><button type="button" data-zr="now" data-noul title="Back to now">▶ Now</button><button type="button" data-zr="1" data-noul title="Forward a day">1 d ▶</button><button type="button" data-zr="30" data-noul title="Forward 30 days">30 d ⏩</button><button type="button" data-zr="spin" data-noul title="Spin the ring and open the sign it lands on">🎡 Spin</button>'+(inPage?'':'<button type="button" data-zr="page" data-noul title="The ring as its own live page">⛶ Full page</button>')+'</div>'; }
 function wire(host){ host.addEventListener('click',e=>{ const b=e.target.closest('[data-zr]'); if(!b) return; e.stopPropagation(); const v=b.dataset.zr; if(v==='now') dayOff=0; else if(v==='spin') doSpin(); else if(v==='page') return page(); else dayOff+=+v; sky=null; table(); const sl=$('kZRingPage')&&$('kZRingPage').querySelector('input[type=range]'); if(sl) sl.value=String(dayOff); }); }
 function canvasEvents(cv,getS){ cv.addEventListener('pointermove',e=>{ hover=signAt(cv,getS(),e); }); cv.addEventListener('pointerleave',()=>{ hover=-1; }); cv.addEventListener('click',e=>{ const k=signAt(cv,getS(),e); if(k>=0) openSign(k); }); }
 /* the ring at the head of LuvMyZodiac */
 function mount(){ const d=$('zodDock'); if(!d||d.hidden) return; if($('kZRing')) return; const box=document.createElement('section'); box.id='kZRing'; box.setAttribute('aria-label','The zodiac ring, live');
  box.innerHTML='<canvas aria-label="The twelve signs with the Sun, the Moon and the planets where they are now"></canvas>'+bar(false); d.insertBefore(box,d.firstChild); wire(box); const cv=box.querySelector('canvas'); canvasEvents(cv,()=>sizeIn()); }
 const sizeIn=()=>{ const b=$('kZRing'); const w=b?b.getBoundingClientRect().width:400; return Math.max(240,Math.min(520,w-8,Math.round(innerHeight*.62))); };
 /* the ring as its own live page */
 function page(){ let p=$('kZRingPage'); if(!p){ p=document.createElement('div'); p.id='kZRingPage'; p.hidden=true; p.setAttribute('role','dialog'); p.setAttribute('aria-label','The zodiac ring, live page'); document.body.appendChild(p);
   p.innerHTML='<div class="zpIn"><div class="zpTop"><h2>♈ The Zodiac Ring · the sky now</h2><button type="button" data-zp="x" data-noul style="min-height:44px;padding:0 16px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif">✕ Close</button></div><div class="zpBody"><div><canvas aria-label="The zodiac ring"></canvas>'+bar(true)+'<label class="zpNote">Days from today: <input type="range" min="-365" max="365" step="1" value="0" data-nodice data-die="1" aria-label="Days from today"></label></div><div><table aria-label="Where each body is"><thead><tr><th>Body</th><th>Sign</th><th>Degree</th><th></th></tr></thead><tbody></tbody></table><p class="zpNote">Positions are computed on this device from published orbital formulas (tropical zodiac), accurate to about a degree; astrology itself is presented as tradition and entertainment, not science.</p><p class="zpNote">© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com</p></div></div></div>';
   p.addEventListener('click',e=>{ if(e.target.closest('[data-zp="x"]')){ e.stopPropagation(); p.hidden=true; } }); wire(p); p.querySelector('input[type=range]').addEventListener('input',e=>{ dayOff=+e.target.value; sky=null; table(); }); canvasEvents(p.querySelector('canvas'),()=>sizePg()); }
  p.hidden=false; table(); }
 const sizePg=()=>{ const p=$('kZRingPage'); const w=p?p.querySelector('.zpBody > div').getBoundingClientRect().width:600; return Math.max(260,Math.min(760,w-8,Math.round(innerHeight*.78))); };
 function table(){ const p=$('kZRingPage'); if(!p||p.hidden) return; const sk=getSky(); const tb=p.querySelector('tbody'); if(!tb||!sk||!sk.pos) return; tb.innerHTML=BODIES.map(([n,gl,col])=>{ const q=sk.pos[n]; if(!q) return ''; const L=((q.lon%360)+360)%360, s=SIGNS[signOf(L)]; return '<tr><td><span style="color:'+col+';font-family:'+FONT.replace(/"/g,"'")+'">'+gl+VS+'</span> '+n+'</td><td>'+s[1]+VS+' '+s[0]+'</td><td>'+Math.floor(L%30)+'° '+String(Math.floor((L%1)*60)).padStart(2,'0')+'′</td><td>'+(q.retro?'℞ retrograde':'')+'</td></tr>'; }).join(''); }
 /* the clock: draw what is on screen, about 30 times a second */
 /* draws only while a ring is on screen; otherwise it looks again twice a second instead of every frame */
 let last=0; const onScreen=()=>{ const b=$('kZRing'), p=$('kZRingPage'); return !!((b&&b.getClientRects().length)||(p&&!p.hidden)); };
 function tick(t){ if(!onScreen()){ setTimeout(()=>requestAnimationFrame(tick),500); return; } requestAnimationFrame(tick); if(t-last<33) return; last=t; pulse+=.08; stepSpin();
  const b=$('kZRing'); if(b&&b.getClientRects().length){ const cv=b.querySelector('canvas'); if(cv) draw(cv,sizeIn(),false); }
  const p=$('kZRingPage'); if(p&&!p.hidden){ const cv=p.querySelector('canvas'); if(cv) draw(cv,sizePg(),true); if(t-(tick.tb||0)>30000){ tick.tb=t; sky=null; table(); } } }
 requestAnimationFrame(tick); setInterval(mount,800);
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Play','♈','The Zodiac Ring: the twelve signs with the Sun, Moon and planets where they are now','Zodiac ring',()=>page()); }); }catch(_){ }
 window.KZRING={page,spin:doSpin,openSign,setDay:d=>{ dayOff=+d||0; sky=null; table(); },get sky(){ return getSky(); },SIGNS};
})();
