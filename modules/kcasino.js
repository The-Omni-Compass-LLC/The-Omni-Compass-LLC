(()=>{ /* 🎰 THE REAL TABLES (v215): casino games laid out and played the way the real tables are. Play chips only: no money, no prizes.
   🎡 Roulette Table: the real wheel (European 37 pockets or American 38, in the true wheel order) turns one way while the ball runs
   the other, drops off the track and settles in a pocket; the real layout (0 and 00, 1 to 36 in three rows of twelve, red and
   black, the 2-to-1 columns, the dozens, 1–18, even, red, black, odd, 19–36); chips stack where you tap; undo, clear, rebet,
   history. 🎲 Craps Table: the real layout (pass line, don't pass bar, come, field, the six place numbers with the point puck, the
   odds behind the line, any seven, any craps, the hardways) and the real rules; two dice thrown across the felt with a button. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h; const rn=n=>Math.floor(Math.random()*n);
 const NOTE='Play chips only — no money, no prizes.';
 const getC=()=>{ try{ const s=localStorage.getItem('kanGamesChips'); if(s===null) return 1000; const v=+s; return isFinite(v)?Math.max(0,v):1000; }catch(_){ return 1000; } };
 const setC=v=>{ v=Math.max(0,Math.round(v)); try{ localStorage.setItem('kanGamesChips',String(v)); }catch(_){ } document.querySelectorAll('#gamesDock .chipsNow').forEach(s=>s.textContent=v); return v; };
 const CHIPS=[[1,'#f4f4f4','#333'],[5,'#d62a36','#fff'],[10,'#2a6fd6','#fff'],[25,'#1e9c4a','#fff'],[100,'#111','#fff'],[500,'#7b3fc4','#fff']];
 const css=document.createElement('style'); css.textContent=`
.kcTop{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:center;margin:6px 0}
.kcTop .kcChips{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}
.kcChip{width:46px;height:46px;border-radius:50%;border:4px dashed rgba(255,255,255,.85)!important;font:900 13px system-ui,sans-serif!important;box-shadow:0 3px 6px rgba(0,0,0,.5),inset 0 0 0 3px rgba(0,0,0,.25);padding:0!important;min-height:0!important}
.kcChip.on{outline:3px solid #ffe94a;outline-offset:2px;transform:translateY(-3px)}
.kcBank{font:800 15px system-ui,sans-serif;color:#ffe94a} .kcBank small{display:block;font:600 11px system-ui,sans-serif;color:#cfc8a0}
.kcBtns{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}
.kcBtns button{min-height:46px;border-radius:12px;padding:4px 16px!important;font:900 15px system-ui,sans-serif}
.kcBtns button.go{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important;border:2px solid #fff3b0!important;font-size:18px}
.kcFelt{background:radial-gradient(ellipse at 50% 30%,#1f8a4c,#0b5a2e 70%,#063d1f);border:10px solid #5a3417;border-radius:22px;box-shadow:inset 0 0 40px rgba(0,0,0,.55),0 8px 24px rgba(0,0,0,.6);padding:10px;color:#fff;position:relative}
.kcLay{display:grid;gap:3px;user-select:none;-webkit-user-select:none}
.kcLay button{position:relative;min-height:38px;padding:2px!important;border:2px solid rgba(255,255,255,.85)!important;border-radius:4px!important;background:transparent!important;color:#fff!important;font:900 clamp(12px,1.4vw,18px) Georgia,serif!important;box-shadow:none!important}
.kcLay button.r{background:#b3172f!important} .kcLay button.b{background:#151515!important} .kcLay button.g{background:#0f7a3c!important}
.kcLay button.o{font:800 clamp(11px,1.1vw,15px) system-ui,sans-serif!important;letter-spacing:.04em}
.kcLay button.win{box-shadow:0 0 0 3px #ffe94a,0 0 16px #ffe94a!important}
.kcStack{position:absolute;right:2px;bottom:2px;min-width:22px;height:22px;border-radius:50%;font:900 10px/22px system-ui,sans-serif;text-align:center;border:2px dashed rgba(255,255,255,.9);box-shadow:0 2px 3px rgba(0,0,0,.6);pointer-events:none}
.kcHist{display:flex;gap:3px;flex-wrap:wrap;justify-content:center;margin:4px 0}
.kcHist i{font-style:normal;min-width:26px;height:26px;border-radius:50%;font:900 12px/26px system-ui,sans-serif;text-align:center;color:#fff;border:1px solid rgba(255,255,255,.4)}
.kcMsg{text-align:center;font:800 clamp(14px,1.3vw,19px)/1.4 system-ui,sans-serif;color:#fff;min-height:1.4em;margin:4px 0}
.kcWheel{display:block;margin:0 auto;max-width:100%;height:auto}
.kcCraps{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:4px}
.kcCraps button{min-height:44px;border:2px solid rgba(255,255,255,.85)!important;border-radius:6px!important;background:rgba(0,0,0,.08)!important;color:#fff!important;font:900 clamp(12px,1.3vw,17px) Georgia,serif!important;position:relative;padding:4px!important;line-height:1.15}
.kcCraps button small{display:block;font:700 10px system-ui,sans-serif;color:#ffe94a;letter-spacing:.03em}
.kcCraps .wide{grid-column:1/-1} .kcCraps .half{grid-column:span 3} .kcCraps .third{grid-column:span 2}
.kcCraps button.pt{box-shadow:inset 0 0 0 3px #fff!important}
.kcPuck{position:absolute;top:2px;left:2px;width:24px;height:24px;border-radius:50%;font:900 8px/24px system-ui,sans-serif;text-align:center;box-shadow:0 2px 4px rgba(0,0,0,.6)}
.kcPuck.on{background:#fff;color:#111} .kcPuck.off{background:#111;color:#fff;border:1px solid #fff}
.kcDice{display:block;width:100%;height:auto;border-radius:12px;background:linear-gradient(180deg,#0b5a2e,#0f6e38);box-shadow:inset 0 0 18px rgba(0,0,0,.5);margin-bottom:6px}`; document.head.appendChild(css);
 function chipColor(v){ let c=CHIPS[0]; CHIPS.forEach(x=>{ if(v>=x[0]) c=x; }); return c; }
 function stackEl(v){ const c=chipColor(v); return h('span',{className:'kcStack',style:'background:'+c[1]+';color:'+c[2]},String(v)); }
 function topBar(ctx,st){ const bankEl=h('div',{className:'kcBank'},['Chips: ',h('b',{className:'chipsNow'},String(getC())),h('small',null,NOTE)]);
  const cs=h('div',{className:'kcChips',role:'radiogroup','aria-label':'Chip value'}); CHIPS.forEach(([v,bg,fg])=>{ const b=h('button',{type:'button',className:'kcChip'+(st.chip===v?' on':''),style:'background:'+bg+';color:'+fg,'aria-label':v+' chip'},String(v)); b.addEventListener('click',()=>{ st.chip=v; cs.querySelectorAll('.kcChip').forEach(x=>x.classList.toggle('on',x===b)); }); cs.appendChild(b); });
  const ref=h('button',{type:'button'},'Refill to 1,000'); ref.addEventListener('click',()=>{ setC(1000); ctx.status('Chips refilled to 1,000.'); });
  ctx.area.appendChild(h('div',{className:'kcTop'},[bankEl,cs,ref])); }
 /* ───────── ROULETTE ───────── */
 const REDS=new Set([1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]);
 const EU=[0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26];
 const US=[0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,'00',27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2];
 const colOf=n=>n===0||n==='00'?'g':REDS.has(n)?'r':'b';
 function pays(k,n){ if(n===0||n==='00') return k==='s'+n?35:-1; if(k[0]==='s') return k==='s'+n?35:-1; const v=+n;
  const W={red:REDS.has(v),black:!REDS.has(v),odd:v%2===1,even:v%2===0,low:v<=18,high:v>=19,d1:v<=12,d2:v>12&&v<=24,d3:v>24,c1:v%3===1,c2:v%3===2,c3:v%3===0};
  if(k in W) return W[k]?(k[0]==='d'||k[0]==='c'?2:1):-1; return -1; }
 G.reg('kc_roulette','🎡 Roulette Table (real)','Casino','The real table: a wheel in the true pocket order and the full layout. Pick a chip, tap the layout to bet (tap again to add), then spin. A number pays 35 to 1; a column or a dozen pays 2 to 1; red, black, odd, even, 1–18 and 19–36 pay even money. The ball lands, the winning spot lights up, and the table pays. Play chips only.',ctx=>{
  const st={us:false,bets:{},chip:10,undo:[],lastBets:null,hist:[],spinning:false,sid:0,win:null};
  topBar(ctx,st);
  const S=Math.max(240,Math.min(ctx.W(),440)); const cv=h('canvas',{className:'kcWheel',width:S*2,height:S*2,style:'width:'+S+'px'}); const g=cv.getContext('2d'); g.scale(2,2); ctx.area.appendChild(cv);
  const msg=h('div',{className:'kcMsg'},'Place your bets.'); ctx.area.appendChild(msg); const hist=h('div',{className:'kcHist','aria-label':'Last numbers'}); ctx.area.appendChild(hist);
  const wsel=h('select',{'aria-label':'Wheel'},[h('option',{value:'eu'},'European wheel · single zero'),h('option',{value:'us'},'American wheel · 0 and 00')]); wsel.addEventListener('change',()=>{ if(st.spinning){ wsel.value=st.us?'us':'eu'; return; } st.us=wsel.value==='us'; refund(); draw(0,null); layout(); });
  const btns=h('div',{className:'kcBtns'}); const mk=(l,f,c)=>{ const b=h('button',{type:'button',className:c||''},l); b.addEventListener('click',f); btns.appendChild(b); return b; };
  mk('🎡 Spin',spin,'go'); mk('↶ Undo bet',()=>{ if(st.spinning) return; const u=st.undo.pop(); if(!u) return; st.bets[u[0]]-=u[1]; if(st.bets[u[0]]<=0) delete st.bets[u[0]]; setC(getC()+u[1]); layout(); });
  mk('✕ Clear bets',()=>{ if(!st.spinning){ refund(); layout(); } }); mk('🔁 Rebet',()=>{ if(st.spinning||!st.lastBets) return; const need=Object.values(st.lastBets).reduce((a,c)=>a+c,0); if(getC()<need) return ctx.status('Not enough chips to rebet.'); refund(); Object.entries(st.lastBets).forEach(([k,v])=>{ st.bets[k]=v; st.undo.push([k,v]); }); setC(getC()-need); layout(); });
  btns.appendChild(wsel); ctx.area.appendChild(btns);
  const felt=h('div',{className:'kcFelt'}); const lay=h('div',{className:'kcLay'}); felt.appendChild(lay); ctx.area.appendChild(felt);
  function refund(){ const s=Object.values(st.bets).reduce((a,c)=>a+c,0); if(s) setC(getC()+s); st.bets={}; st.undo=[]; }
  function place(k){ if(st.spinning) return; if(getC()<st.chip){ ctx.status('Not enough chips. Tap Refill.'); return; } st.bets[k]=(st.bets[k]||0)+st.chip; st.undo.push([k,st.chip]); setC(getC()-st.chip); try{ ctx.beep&&ctx.beep(660,.03); }catch(_){ } layout(); }
  function cell(k,label,cls,area){ const b=h('button',{type:'button',className:cls,style:'grid-area:'+area,'aria-label':'Bet on '+label},label); if(st.bets[k]) b.appendChild(stackEl(st.bets[k])); if(st.win!=null&&pays(k,st.win)>0) b.classList.add('win'); b.addEventListener('click',()=>place(k)); lay.appendChild(b); }
  function layout(){ lay.innerHTML=''; const wide=(felt.clientWidth||ctx.W())>=560; const z=st.us?[0,'00']:[0];
   if(wide){ lay.style.gridTemplateColumns='minmax(34px,1.1fr) repeat(12,minmax(0,1fr)) minmax(40px,1.2fr)'; lay.style.gridTemplateRows='repeat(3,minmax(40px,auto)) minmax(36px,auto) minmax(36px,auto)';
    if(z.length===1) cell('s0','0','g','1 / 1 / 4 / 2'); else { cell('s0','0','g','1 / 1 / 2 / 2'); cell('s00','00','g','2 / 1 / 4 / 2'); }
    for(let n=1;n<=36;n++){ const c=Math.ceil(n/3)+1, r=3-((n-1)%3); cell('s'+n,String(n),colOf(n),r+' / '+c+' / '+(r+1)+' / '+(c+1)); }
    ['c3','c2','c1'].forEach((k,i)=>cell(k,'2 to 1','o',(i+1)+' / 14 / '+(i+2)+' / 15'));
    ['d1','d2','d3'].forEach((k,i)=>cell(k,['1st 12','2nd 12','3rd 12'][i],'o','4 / '+(2+i*4)+' / 5 / '+(6+i*4)));
    [['low','1 – 18'],['even','EVEN'],['red','◆ RED'],['black','◆ BLACK'],['odd','ODD'],['high','19 – 36']].forEach(([k,l],i)=>cell(k,l,'o'+(k==='red'?' r':k==='black'?' b':''),'5 / '+(2+i*2)+' / 6 / '+(4+i*2)));
   } else { lay.style.gridTemplateColumns='minmax(44px,1fr) repeat(3,minmax(0,1.3fr)) minmax(44px,1fr)'; lay.style.gridTemplateRows='minmax(36px,auto) repeat(12,minmax(34px,auto)) minmax(36px,auto)';
    if(z.length===1) cell('s0','0','g','1 / 2 / 2 / 5'); else { cell('s0','0','g','1 / 2 / 2 / 3'); cell('s00','00','g','1 / 3 / 2 / 5'); }
    for(let n=1;n<=36;n++){ const r=Math.ceil(n/3)+1, c=((n-1)%3)+2; cell('s'+n,String(n),colOf(n),r+' / '+c+' / '+(r+1)+' / '+(c+1)); }
    ['c1','c2','c3'].forEach((k,i)=>cell(k,'2:1','o','14 / '+(2+i)+' / 15 / '+(3+i)));
    ['d1','d2','d3'].forEach((k,i)=>cell(k,['1st 12','2nd 12','3rd 12'][i],'o',(2+i*4)+' / 1 / '+(6+i*4)+' / 2'));
    [['low','1–18'],['even','EVEN'],['red','RED'],['black','BLACK'],['odd','ODD'],['high','19–36']].forEach(([k,l],i)=>cell(k,l,'o'+(k==='red'?' r':k==='black'?' b':''),(2+i*2)+' / 5 / '+(4+i*2)+' / 6'));
   }
   hist.innerHTML=''; st.hist.slice(-14).reverse().forEach(n=>{ const c=colOf(n); hist.appendChild(h('i',{style:'background:'+(c==='r'?'#b3172f':c==='b'?'#151515':'#0f7a3c')},String(n))); }); }
  const wheel=()=>st.us?US:EU;
  function draw(wa,ball){ const R=S/2, cx=R, cy=R, n=wheel().length, seg=2*Math.PI/n; g.clearRect(0,0,S,S);
   let gr=g.createRadialGradient(cx,cy,R*.6,cx,cy,R); gr.addColorStop(0,'#6b3a17'); gr.addColorStop(.7,'#4a2610'); gr.addColorStop(1,'#2a1407'); g.fillStyle=gr; g.beginPath(); g.arc(cx,cy,R-1,0,7); g.fill();
   g.fillStyle='#1b120a'; g.beginPath(); g.arc(cx,cy,R*.86,0,7); g.fill(); g.strokeStyle='rgba(255,220,150,.35)'; g.lineWidth=1.5; g.beginPath(); g.arc(cx,cy,R*.86,0,7); g.stroke();
   const r1=R*.74, r0=R*.52; for(let i=0;i<n;i++){ const a0=wa+i*seg-Math.PI/2-seg/2, a1=a0+seg, v=wheel()[i], c=colOf(v); g.beginPath(); g.arc(cx,cy,r1,a0,a1); g.arc(cx,cy,r0,a1,a0,true); g.closePath(); g.fillStyle=c==='r'?'#c41f35':c==='b'?'#141414':'#118a45'; g.fill(); g.strokeStyle='#d8b45a'; g.lineWidth=1.2; g.stroke();
    g.save(); g.translate(cx,cy); g.rotate(a0+seg/2+Math.PI/2); g.fillStyle='#fff'; g.font='bold '+Math.max(8,S/30)+'px Georgia,serif'; g.textAlign='center'; g.fillText(String(v),0,-r1+S/26); g.restore(); }
   gr=g.createRadialGradient(cx-R*.12,cy-R*.12,R*.05,cx,cy,r0); gr.addColorStop(0,'#c98a3c'); gr.addColorStop(.6,'#7a4518'); gr.addColorStop(1,'#3c1e08'); g.fillStyle=gr; g.beginPath(); g.arc(cx,cy,r0,0,7); g.fill();
   g.save(); g.translate(cx,cy); g.rotate(wa); g.strokeStyle='#f3d27a'; g.lineWidth=S/70; g.lineCap='round'; for(let k=0;k<4;k++){ g.rotate(Math.PI/2); g.beginPath(); g.moveTo(0,0); g.lineTo(0,-r0*.62); g.stroke(); g.fillStyle='#f3d27a'; g.beginPath(); g.arc(0,-r0*.62,S/80,0,7); g.fill(); }
   g.fillStyle='#f6e2a0'; g.beginPath(); g.arc(0,0,S/30,0,7); g.fill(); g.restore();
   if(ball){ const bx=cx+Math.cos(ball.a)*ball.r, by=cy+Math.sin(ball.a)*ball.r; g.fillStyle='rgba(0,0,0,.35)'; g.beginPath(); g.arc(bx+2,by+2,S/44,0,7); g.fill(); const bg=g.createRadialGradient(bx-S/120,by-S/120,1,bx,by,S/44); bg.addColorStop(0,'#fff'); bg.addColorStop(1,'#b9b9b9'); g.fillStyle=bg; g.beginPath(); g.arc(bx,by,S/44,0,7); g.fill(); }
   g.fillStyle='#ffe94a'; g.beginPath(); g.moveTo(cx-6,4); g.lineTo(cx+6,4); g.lineTo(cx,14); g.closePath(); g.fill(); }
  function spin(){ if(st.spinning) return; if(!Object.keys(st.bets).length){ msg.textContent='Place a bet first: pick a chip and tap the layout.'; return; }
   st.spinning=true; st.win=null; layout(); const sid=++st.sid; const W=wheel(), n=W.length, idx=rn(n), res=W[idx], seg=2*Math.PI/n; const T=6200, t0=performance.now(); const w0=Math.random()*Math.PI*2; msg.textContent='No more bets. The ball is rolling…';
   const R=S/2, track=R*.8, pocket=R*.63; const pc=idx*seg-Math.PI/2;
   ctx.raf((dt,t)=>{ if(sid!==st.sid||!st.spinning) return false; const k=Math.min(1,(t-t0)/T); const wa=w0+Math.PI*5*(1-Math.pow(1-k,2)); const kb=Math.min(1,k/.86), eb=1-Math.pow(1-kb,3);
    const a=wa+pc-Math.PI*12*(1-eb); let r=track; if(k>.58){ const s=Math.min(1,(k-.58)/.28); r=pocket+(track-pocket)*(1-s)+Math.sin(s*Math.PI*4)*(1-s)*S/60; } draw(wa,{a,r:k>=.86?pocket:r});
    if(k>=1){ st.spinning=false; st.win=res; st.hist.push(res); let back=0, won=0; Object.entries(st.bets).forEach(([kk,amt])=>{ const m=pays(kk,res); if(m>0){ back+=amt*(m+1); won+=amt*m; } }); if(back) setC(getC()+back);
     const lost=Object.entries(st.bets).filter(([kk])=>pays(kk,res)<0).reduce((a,[,v])=>a+v,0); st.lastBets=Object.assign({},st.bets); st.bets={}; st.undo=[];
     const net=won-lost; msg.textContent=res+' '+(colOf(res)==='r'?'RED':colOf(res)==='b'?'BLACK':'GREEN')+' · '+(won?'won '+won+(lost?', lost '+lost:'')+' · net '+(net>=0?'+':'−')+Math.abs(net)+' chips':'The house takes '+lost+'.'); ctx.status(won?'Winner: '+won+' chips.':'No win this spin. Rebet or place new bets.'); layout(); return false; } });
  }
  draw(0,null); layout(); addEventListener('resize',()=>{ if(lay.isConnected) layout(); });
  return {state:()=>({bets:st.bets,hist:st.hist,spinning:st.spinning}),_pays:pays,spin,place};
 });
 /* ───────── CRAPS ───────── */
 const TRUE={4:2,10:2,5:1.5,9:1.5,6:1.2,8:1.2}, PLACE={4:1.8,10:1.8,5:1.4,9:1.4,6:7/6,8:7/6}, HARD={4:7,10:7,6:9,8:9};
 G.reg('kc_craps','🎲 Craps Table (real)','Casino','The real craps table and rules. On the come-out roll the pass line wins on 7 or 11 and loses on 2, 3 or 12; any other number becomes the point (the puck turns ON). Then the pass line wins if the point repeats before a 7. Don\'t pass is the opposite (12 pushes). Take odds behind the line at true odds once a point is on. Come bets work like the pass line on their own number. The field pays on 2, 3, 4, 9, 10, 11, 12 (2 pays double, 12 triple). Place bets pay 9:5 on 4 and 10, 7:5 on 5 and 9, 7:6 on 6 and 8. Any seven pays 4:1, any craps 7:1, hard 4 and 10 pay 7:1, hard 6 and 8 pay 9:1. Pick a chip, tap the table, press Roll.',ctx=>{
  const st={chip:10,point:null,bets:{},come:0,comePts:{},hist:[],rolling:false,rid:0,d:[3,4],undo:[]};
  topBar(ctx,st);
  const S=Math.max(240,Math.min(ctx.W(),560)), Hh=Math.round(S*.42); const cv=h('canvas',{className:'kcDice',width:S*2,height:Hh*2,style:'width:'+S+'px;max-width:100%'}); const g=cv.getContext('2d'); g.scale(2,2); ctx.area.appendChild(cv);
  const msg=h('div',{className:'kcMsg'},'Come-out roll. Bet the pass line, then roll.'); ctx.area.appendChild(msg); const hist=h('div',{className:'kcHist','aria-label':'Last rolls'}); ctx.area.appendChild(hist);
  const btns=h('div',{className:'kcBtns'}); const mk=(l,f,c)=>{ const b=h('button',{type:'button',className:c||''},l); b.addEventListener('click',f); btns.appendChild(b); return b; };
  mk('🎲 Roll the dice',roll,'go'); mk('↶ Undo bet',()=>{ if(st.rolling) return; const u=st.undo.pop(); if(!u) return; const [k,v]=u; if(k==='pass'&&st.point) return msg.textContent='The pass line can’t come down once a point is on.'; st.bets[k]-=v; if(st.bets[k]<=0) delete st.bets[k]; setC(getC()+v); table(); });
  ctx.area.appendChild(btns);
  const felt=h('div',{className:'kcFelt'}); const grid=h('div',{className:'kcCraps'}); felt.appendChild(grid); ctx.area.appendChild(felt);
  function can(k){ if(k==='pass'||k==='dpass') return !st.point||!!st.bets[k]; if(k==='odds') return !!st.point&&!!st.bets.pass&&((st.bets.odds||0)+st.chip<=3*st.bets.pass); if(k==='come') return !!st.point; return true; }
  function bet(k){ if(st.rolling) return; if(!can(k)){ msg.textContent=k==='odds'?(st.point?'Odds go behind a pass line bet, up to 3 times it.':'Odds open once a point is on.'):k==='come'?'Come bets open once a point is on.':'Line bets go down on the come-out roll.'; return; } if(getC()<st.chip){ ctx.status('Not enough chips. Tap Refill.'); return; }
   st.bets[k]=(st.bets[k]||0)+st.chip; st.undo.push([k,st.chip]); setC(getC()-st.chip); try{ ctx.beep&&ctx.beep(620,.03); }catch(_){ } table(); }
  function B(k,label,sub,cls){ const b=h('button',{type:'button',className:cls||''},[label,sub?h('small',null,sub):null]); if(st.bets[k]) b.appendChild(stackEl(st.bets[k])); b.addEventListener('click',()=>bet(k)); grid.appendChild(b); return b; }
  function table(){ grid.innerHTML='';
   [4,5,6,8,9,10].forEach(n=>{ const b=B('pl'+n,n===6?'SIX':n===9?'NINE':String(n),'place '+(n===6||n===8?'7:6':n===5||n===9?'7:5':'9:5'),st.point===n?'pt':''); const pk=h('span',{className:'kcPuck '+(st.point===n?'on':'off')},st.point===n?'ON':''); if(st.point===n) b.appendChild(pk); if(st.comePts[n]) b.appendChild(h('span',{className:'kcStack',style:'left:2px;right:auto;bottom:2px;background:#f4f4f4;color:#111'},'C'+st.comePts[n])); });
   B('come','COME','pays 1:1 · on its own number','wide');
   B('field','FIELD','2 · 3 · 4 · 9 · 10 · 11 · 12 — 2 pays double, 12 triple','wide');
   B('dpass','DON’T PASS BAR','12 pushes','half'); B('odds','PASS ODDS','true odds · up to 3×','half');
   B('pass','PASS LINE',st.point?'point is '+st.point:'come-out roll','wide');
   B('any7','ANY SEVEN','4 to 1','third'); B('anyc','ANY CRAPS','2 · 3 · 12 · 7 to 1','third'); B('h4','HARD 4','2+2 · 7 to 1','third'); B('h10','HARD 10','5+5 · 7 to 1','third'); B('h6','HARD 6','3+3 · 9 to 1','third'); B('h8','HARD 8','4+4 · 9 to 1','third');
   const pk=h('div',{className:'kcMsg',style:'margin:6px 0 0'},(st.point?'Puck ON · point '+st.point:'Puck OFF · come-out roll')); grid.appendChild(pk); grid.lastChild.className='kcMsg wide';
   hist.innerHTML=''; st.hist.slice(-14).reverse().forEach(r=>hist.appendChild(h('i',{style:'background:'+(r[0]+r[1]===7?'#b3172f':'#14316b')},String(r[0]+r[1])))); }
  /* the dice: thrown across the felt, they hit the back wall and settle */
  const PIPS={1:[[.5,.5]],2:[[.25,.25],[.75,.75]],3:[[.25,.25],[.5,.5],[.75,.75]],4:[[.25,.25],[.75,.25],[.25,.75],[.75,.75]],5:[[.25,.25],[.75,.25],[.5,.5],[.25,.75],[.75,.75]],6:[[.25,.22],[.75,.22],[.25,.5],[.75,.5],[.25,.78],[.75,.78]]};
  function die(x,y,s,rot,v,tilt){ g.save(); g.translate(x,y); g.fillStyle='rgba(0,0,0,.35)'; g.beginPath(); g.ellipse(s*.12,s*.62,s*.55,s*.16,0,0,7); g.fill(); g.rotate(rot); const w=s*(1-Math.abs(tilt)*.25); const gr=g.createLinearGradient(-w/2,-s/2,w/2,s/2); gr.addColorStop(0,'#fff6f0'); gr.addColorStop(1,'#d9c9c0');
   g.fillStyle=gr; L.rr?L.rr(g,-w/2,-s/2,w,s,s*.18):g.fillRect(-w/2,-s/2,w,s); if(!L.rr){ } g.fill&&g.fill(); g.strokeStyle='rgba(0,0,0,.25)'; g.lineWidth=1; g.strokeRect&&0; g.fillStyle='#b3172f';
   (PIPS[v]||[]).forEach(([px,py])=>{ g.beginPath(); g.arc(-w/2+px*w,-s/2+py*s,s*.085,0,7); g.fill(); }); g.restore(); }
  function scene(d,pos){ g.clearRect(0,0,S,Hh); g.fillStyle='rgba(255,255,255,.08)'; g.font='bold '+Math.round(Hh*.16)+'px Georgia,serif'; g.textAlign='center'; g.fillText('KAN-IN CRAPS',S/2,Hh*.58); g.strokeStyle='rgba(255,233,74,.5)'; g.lineWidth=3; g.beginPath(); g.moveTo(S-8,8); g.lineTo(S-8,Hh-8); g.stroke();
   const s=Math.min(Hh*.42,S*.13); pos.forEach((p,i)=>die(p.x,p.y,s,p.r,d[i],p.t)); }
  function roll(){ if(st.rolling) return; if(!Object.keys(st.bets).length&&!Object.keys(st.comePts).length){ msg.textContent='Place a bet first: pick a chip and tap the table.'; return; }
   st.rolling=true; const rid=++st.rid; const fin=[1+rn(6),1+rn(6)]; const T=1500, t0=performance.now(); msg.textContent='Dice are out…';
   const P=[{x0:S*.08,y0:Hh*.3,x1:S*.66,y1:Hh*.45,r:Math.random()*6},{x0:S*.12,y0:Hh*.7,x1:S*.8,y1:Hh*.6,r:Math.random()*6}];
   ctx.raf((dt,t)=>{ if(rid!==st.rid||!st.rolling) return false; const k=Math.min(1,(t-t0)/T); const e=1-Math.pow(1-k,3); const faces=k<.9?[1+rn(6),1+rn(6)]:fin;
    const pos=P.map((p,i)=>{ let x=p.x0+(p.x1-p.x0)*e; if(k>.55&&k<.75) x+=Math.sin((k-.55)/.2*Math.PI)*-S*.05; const bounce=Math.abs(Math.sin(e*Math.PI*3))*(1-e)*Hh*.18; return {x,y:p.y0+(p.y1-p.y0)*e-bounce,r:p.r*(1-e)*8+(i?-.12:.1),t:(1-e)*Math.sin(t/60+i)}; });
    scene(faces,pos); if(k>=1){ st.rolling=false; settle(fin); return false; } });
  }
  function settle(d){ const s=d[0]+d[1], hard=d[0]===d[1]; st.hist.push(d); let out=[]; const pay=(k,mult)=>{ const a=st.bets[k]; if(!a) return; setC(getC()+a+a*mult); out.push('+'+Math.round(a*mult)+' '+k); delete st.bets[k]; }; const lose=k=>{ if(st.bets[k]){ out.push('−'+st.bets[k]+' '+k); delete st.bets[k]; } }; const push=k=>{ const a=st.bets[k]; if(a){ setC(getC()+a); out.push('push '+k); delete st.bets[k]; } };
   /* one-roll bets */
   if(st.bets.field){ if([3,4,9,10,11].includes(s)) pay('field',1); else if(s===2) pay('field',2); else if(s===12) pay('field',3); else lose('field'); }
   if(st.bets.any7){ s===7?pay('any7',4):lose('any7'); } if(st.bets.anyc){ [2,3,12].includes(s)?pay('anyc',7):lose('anyc'); }
   /* hardways stay up until they hit, roll easy, or a seven */
   [4,6,8,10].forEach(n=>{ const k='h'+n; if(!st.bets[k]) return; if(s===n&&hard) pay(k,HARD[n]); else if(s===n||s===7) lose(k); });
   /* place bets work when a point is on */
   if(st.point){ [4,5,6,8,9,10].forEach(n=>{ const k='pl'+n; if(!st.bets[k]) return; if(s===n){ const a=st.bets[k]; const w=Math.floor(a*PLACE[n]); setC(getC()+w); out.push('+'+w+' place '+n); } else if(s===7) lose(k); }); }
   /* come points already on numbers */
   Object.keys(st.comePts).forEach(n=>{ n=+n; const a=st.comePts[n]; if(s===n){ setC(getC()+a*2); out.push('+'+a+' come '+n); delete st.comePts[n]; } else if(s===7){ out.push('−'+a+' come '+n); delete st.comePts[n]; } });
   /* a new come bet travels */
   if(st.bets.come){ if(s===7||s===11) pay('come',1); else if([2,3,12].includes(s)) lose('come'); else { st.comePts[s]=(st.comePts[s]||0)+st.bets.come; out.push('come → '+s); delete st.bets.come; } }
   /* the line */
   let say='';
   if(!st.point){ if(s===7||s===11){ pay('pass',1); lose('dpass'); say=s+' · natural, the pass line wins.'; } else if(s===2||s===3){ lose('pass'); pay('dpass',1); say=s+' · craps, the pass line loses.'; } else if(s===12){ lose('pass'); push('dpass'); say='12 · craps, pass loses, don’t pass pushes.'; } else { st.point=s; say='The point is '+s+'. Puck ON. Roll it again before a 7.'; } }
   else { if(s===st.point){ pay('pass',1); if(st.bets.odds) pay('odds',TRUE[s]); lose('dpass'); say=s+' · the point hits! Pass line and odds win. Puck OFF.'; st.point=null; }
    else if(s===7){ lose('pass'); lose('odds'); pay('dpass',1); say='7 · seven out. The pass line loses, don’t pass wins. Puck OFF.'; st.point=null; } else say=s+' rolled'+(hard?' the hard way':'')+'. The point is still '+st.point+'.'; }
   st.undo=st.undo.filter(([k])=>st.bets[k]); msg.textContent='🎲 '+d[0]+' + '+d[1]+' = '+say; ctx.status(out.length?out.join(' · '):'No bets settled this roll.'); table(); }
  scene(st.d,[{x:S*.42,y:Hh*.5,r:.1,t:0},{x:S*.6,y:Hh*.52,r:-.15,t:0}]); table(); addEventListener('resize',()=>{ if(grid.isConnected) table(); });
  return {state:()=>({bets:st.bets,point:st.point,comePts:st.comePts,hist:st.hist}),roll,bet,settle};
 });
})();
