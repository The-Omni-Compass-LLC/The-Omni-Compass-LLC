(()=>{ /* 🁫 DOMINOES (v220): Draw, Block and All Fives on a double-six set, and Mexican Train on a double-twelve set; you against one to
   three computer players, phone first. Tap a tile to play it; when it fits both ends, pick the end. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h; const CAT='Dominoes';
 const css=document.createElement('style'); css.textContent=`
.dmT{display:inline-flex;flex-direction:column;width:var(--dw,34px);height:calc(var(--dw,34px)*2);background:linear-gradient(160deg,#fffdf6,#e8e0cc);border:1.5px solid #3a2a12;border-radius:6px;box-shadow:0 2px 3px rgba(0,0,0,.45);padding:0!important;min-height:0!important;margin:1px;flex:none;vertical-align:middle}
.dmT.h{flex-direction:row;width:calc(var(--dw,34px)*2);height:var(--dw,34px)}
.dmT .hf{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);padding:12%;gap:2%}
.dmT .hf+.hf{border-top:1.5px solid #3a2a12}.dmT.h .hf+.hf{border-top:none;border-left:1.5px solid #3a2a12}
.dmT .pp{border-radius:50%;background:#1b1b1b;width:70%;height:70%;margin:auto}
.dmT .hf.n7 .pp,.dmT .hf.n8 .pp,.dmT .hf.n9 .pp{width:60%;height:60%}
.dmT .num{grid-column:1/-1;grid-row:1/-1;display:flex;align-items:center;justify-content:center;font:900 calc(var(--dw,34px)*.42) system-ui,sans-serif;color:#1b1b1b}
.dmT.pl{outline:3px solid #ffe94a;outline-offset:1px}.dmT.sel{transform:translateY(-6px);outline:3px solid #2fd27a}
.dmT.back{background:linear-gradient(160deg,#2a6fd6,#123a7a)}
.dmFelt{background:radial-gradient(ellipse at 50% 30%,#1f8a4c,#0b5a2e 70%,#063d1f);border:8px solid #5a3417;border-radius:18px;padding:8px;min-height:140px;display:flex;flex-wrap:wrap;align-content:flex-start;align-items:center;gap:1px;justify-content:center}
.dmRow{display:flex;flex-wrap:wrap;gap:2px;justify-content:center;align-items:flex-end;margin:6px 0;min-height:40px}
.dmLbl{font:800 13px system-ui,sans-serif;color:#fff;text-align:center;margin:4px 0}.dmLbl b{color:#ffe94a}
.dmBtns{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}.dmBtns button{min-height:46px;border-radius:12px;padding:4px 14px!important;font:800 14px system-ui,sans-serif}
.dmBtns button.go{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important}
.dmTrain{display:flex;align-items:center;gap:4px;flex-wrap:wrap;background:rgba(0,0,0,.18);border-radius:10px;padding:4px 6px;margin:3px 0;width:100%}
.dmTrain>b{font:800 12px system-ui,sans-serif;color:#fff;min-width:80px}.dmTrain.open>b::after{content:" 🚂 open";color:#ffe94a}
.dmTrain.can{box-shadow:0 0 0 2px #ffe94a}`; document.head.appendChild(css);
 const PIPS={0:[],1:[4],2:[0,8],3:[0,4,8],4:[0,2,6,8],5:[0,2,4,6,8],6:[0,2,3,5,6,8]};
 function half(n){ const d=h('div',{className:'hf n'+n}); if(n<=6){ const on=new Set(PIPS[n]); for(let i=0;i<9;i++) d.appendChild(on.has(i)?h('div',{className:'pp'}):h('div',null)); } else d.appendChild(h('div',{className:'num'},String(n))); return d; }
 function tile(t,o){ o=o||{}; const e=h('button',{type:'button',className:'dmT'+(o.h?' h':'')+(o.back?' back':'')+(o.cls?' '+o.cls:''),'aria-label':o.back?'face-down domino':'domino '+t[0]+'–'+t[1]}); e.style.setProperty('--dw',(o.w||34)+'px'); if(!o.back){ e.appendChild(half(t[0])); e.appendChild(half(t[1])); } return e; }
 const set=n=>{ const s=[]; for(let a=0;a<=n;a++) for(let b=a;b<=n;b++) s.push([a,b]); return L.shuffle(s); };
 const pips=hand=>hand.reduce((a,t)=>a+t[0]+t[1],0);
 const fits=(t,v)=>t[0]===v||t[1]===v;
 const NAMES=['You','Ace','Blaze','Coco'];
 function setup(ctx){ const st={n:2}; const sel=h('select',{'aria-label':'Players'},[2,3,4].map(n=>h('option',{value:String(n)},n+' players'))); return {sel,st}; }
 /* ───── the line games: Draw, Block, All Fives ───── */
 function lineGame(kind){ return ctx=>{ const setTimeout=(f,ms)=>ctx.after(ms,f);
  const st={players:[],bone:[],chain:[],ends:null,turn:0,scores:[0,0,0,0],n:2,over:false,pend:null,msg:'',target:kind==='fives'?150:100};
  const top=h('div',{className:'dmBtns'}); const pSel=h('select',{'aria-label':'Players'},[2,3,4].map(n=>h('option',{value:String(n)},n+' players'))); top.appendChild(pSel); const newB=h('button',{type:'button',className:'go'},'🁫 New game'); top.appendChild(newB); ctx.area.appendChild(top);
  const info=h('div',{className:'dmLbl'}); const opp=h('div',{className:'dmRow'}); const felt=h('div',{className:'dmFelt','aria-label':'The line of play'}); const mine=h('div',{className:'dmRow'}); const btns=h('div',{className:'dmBtns'});
  [info,opp,felt,mine,btns].forEach(e=>ctx.area.appendChild(e));
  const W=()=>Math.max(24,Math.min(40,Math.floor((ctx.W()-20)/12)));
  function round(){ const s=set(6); st.bone=s; st.players=[]; for(let i=0;i<st.n;i++) st.players.push(st.bone.splice(0,st.n===2?7:st.n===3?6:5)); st.chain=[]; st.ends=null; st.pend=null; st.over=false;
   let best=-1, who=0, bt=null; st.players.forEach((hd,i)=>hd.forEach(t=>{ if(t[0]===t[1]&&t[0]>best){ best=t[0]; who=i; bt=t; } })); if(!bt){ who=0; bt=st.players[0].reduce((a,t)=>t[0]+t[1]>a[0]+a[1]?t:a); }
   st.turn=who; play(who,bt,'R'); next(); }
  function score5(){ if(kind!=='fives'||!st.chain.length) return 0; const a=st.chain[0], z=st.chain[st.chain.length-1]; let s=(a[0]===a[1]?a[0]*2:a[0])+(z[0]===z[1]?z[1]*2:z[1]); if(st.chain.length===1) s=a[0]+a[1]; return s%5===0?s:0; }
  function play(i,t,side){ const hd=st.players[i]; hd.splice(hd.indexOf(t),1); let tt=t.slice();
   if(!st.chain.length){ st.chain.push(tt); st.ends=[tt[0],tt[1]]; }
   else if(side==='L'){ if(tt[1]!==st.ends[0]) tt=[tt[1],tt[0]]; st.chain.unshift(tt); st.ends[0]=tt[0]; } else { if(tt[0]!==st.ends[1]) tt=[tt[1],tt[0]]; st.chain.push(tt); st.ends[1]=tt[1]; }
   const sc=score5(); if(sc){ st.scores[i]+=sc; st.msg=NAMES[i]+(i?' scores ':' score ')+sc+'!'; } try{ L.beep(380,.04); }catch(_){ } }
  const playable=hd=>hd.filter(t=>!st.ends||fits(t,st.ends[0])||fits(t,st.ends[1]));
  function endRound(winner,blocked){ st.over=true; let pts=0; st.players.forEach((hd,i)=>{ if(i!==winner) pts+=pips(hd); }); if(blocked){ pts=0; st.players.forEach((hd,i)=>{ if(i!==winner) pts+=pips(hd)-pips(st.players[winner]); }); pts=Math.max(0,pts); }
   if(kind==='fives') pts=Math.round(pts/5)*5; st.scores[winner]+=pts; st.msg=(blocked?'Blocked! ':'')+NAMES[winner]+(winner?' wins':' win')+' the hand +'+pts+'.'; const champ=st.scores.findIndex(s=>s>=st.target); if(champ>=0&&champ<st.n) st.msg+=' '+NAMES[champ]+(champ?' wins':' win')+' the game at '+st.scores[champ]+'!'; render(); }
  function next(){ if(st.over) return render(); const hd=st.players[st.turn]; if(!hd.length) return endRound(st.turn,false);
   const nt=(st.turn+1)%st.n; st.turn=nt; const ph=st.players[nt]; let pl=playable(ph);
   while(!pl.length&&kind!=='block'&&st.bone.length){ ph.push(st.bone.pop()); pl=playable(ph); }
   if(!pl.length){ const stuck=st.players.every(p=>!playable(p).length)&&(kind==='block'||!st.bone.length); if(stuck){ let w=0; st.players.forEach((p,i)=>{ if(pips(p)<pips(st.players[w])) w=i; }); return endRound(w,true); } st.msg=NAMES[nt]+(nt?' passes.':' pass.'); return nt===0?(render(),setTimeout(next,700)):setTimeout(next,450); }
   if(nt===0){ st.msg=st.msg||'Your turn: tap a lit tile.'; return render(); } render(); setTimeout(()=>{ ai(nt); },600); }
  function sim(t,side){ if(!st.ends) return 0; const a=st.chain[0], z=st.chain[st.chain.length-1]; let L0=a, R0=z; const tt=side==='L'?(t[1]===st.ends[0]?t:[t[1],t[0]]):(t[0]===st.ends[1]?t:[t[1],t[0]]); if(side==='L') L0=tt; else R0=tt;
  const sum=(L0[0]===L0[1]?L0[0]*2:L0[0])+(R0[0]===R0[1]?R0[1]*2:R0[1]); return sum%5===0?sum:0; }
 function ai(i){ const pl=playable(st.players[i]); let best=null, bs=-1, side='R'; pl.forEach(t=>['L','R'].forEach(sd=>{ if(st.ends&&!fits(t,st.ends[sd==='L'?0:1])) return; let s=t[0]+t[1]+(t[0]===t[1]?3:0); if(kind==='fives') s+=sim(t,sd)*3; if(s>bs){ bs=s; best=t; side=sd; } }));
   if(kind==='fives'&&st.msg&&/scores/.test(st.msg)) st.msg=''; play(i,best,side); if(!st.players[i].length) return endRound(i,false); next(); }
  function render(){ const w=W(); info.innerHTML=''; info.appendChild(h('span',null,st.players.slice(0,st.n).map((p,i)=>NAMES[i]+' '+st.scores[i]+(i===st.turn&&!st.over?' ◀':'')).join(' · ')+' · first to '+st.target+(kind!=='block'?' · boneyard '+st.bone.length:'')));
   opp.innerHTML=''; for(let i=1;i<st.n;i++){ const r=h('span',{className:'dmLbl',style:'margin:0 6px'},NAMES[i]+' '); st.players[i].forEach(()=>r.appendChild(tile([0,0],{back:true,w:Math.max(14,w*.45)}))); opp.appendChild(r); }
   felt.innerHTML=''; st.chain.forEach(t=>felt.appendChild(tile(t,{h:t[0]!==t[1],w:Math.max(20,w*.8)})));
   mine.innerHTML=''; const myTurn=st.turn===0&&!st.over; const pl=myTurn?playable(st.players[0]):[]; st.players[0]&&st.players[0].forEach(t=>{ const e=tile(t,{w,cls:pl.includes(t)?'pl':''}); if(st.pend===t) e.classList.add('sel'); e.addEventListener('click',()=>tap(t)); mine.appendChild(e); });
   btns.innerHTML=''; if(st.pend){ const b1=h('button',{type:'button',className:'go'},'◀ Left end ('+st.ends[0]+')'), b2=h('button',{type:'button',className:'go'},'Right end ('+st.ends[1]+') ▶'); b1.addEventListener('click',()=>mePlay(st.pend,'L')); b2.addEventListener('click',()=>mePlay(st.pend,'R')); btns.append(b1,b2); }
   if(st.over){ const nb=h('button',{type:'button',className:'go'},st.scores.some(s=>s>=st.target)?'🁫 New game':'▶ Next hand'); nb.addEventListener('click',()=>{ if(st.scores.some(s=>s>=st.target)) st.scores=[0,0,0,0]; st.msg=''; round(); }); btns.appendChild(nb); }
   ctx.status(st.msg||(myTurn?'Your turn.':'')); }
  function tap(t){ if(st.turn!==0||st.over) return; if(!playable(st.players[0]).includes(t)) return ctx.status('That tile does not fit an open end ('+(st.ends?st.ends.join(' and '):'')+').');
   const a=fits(t,st.ends[0]), b=fits(t,st.ends[1]); if(a&&b&&st.ends[0]!==st.ends[1]){ st.pend=t; render(); return; } mePlay(t,a?'L':'R'); }
  function mePlay(t,side){ st.pend=null; st.msg=''; play(0,t,side); if(!st.players[0].length) return endRound(0,false); next(); }
  newB.addEventListener('click',()=>{ st.n=+pSel.value; st.scores=[0,0,0,0]; st.msg=''; round(); }); st.n=2; round(); window.__kgst=()=>st; return {state:()=>st}; }; }
 G.reg('dm_draw','Draw Dominoes',CAT,'Double-six set. Match a tile to an open end of the line; if you cannot play, draw from the boneyard until you can. First out wins the hand and scores the pips left in the other hands. First to 100.',lineGame('draw'));
 G.reg('dm_block','Block Dominoes',CAT,'Double-six set, no boneyard: if you cannot play, you pass. When nobody can play, the lightest hand wins. First to 100.',lineGame('block'));
 G.reg('dm_fives','All Fives (Muggins)',CAT,'Double-six set with a boneyard. Every time the two open ends add up to a multiple of five (a double at an end counts both halves) you score that sum on the spot. Going out scores the rest of the pips, rounded to fives. First to 150.',lineGame('fives'));
 /* ───── Mexican Train ───── */
 G.reg('dm_train','Mexican Train',CAT,'Double-twelve set. The engine (12–12) starts in the middle. Play on your own train, on the Mexican train, or on anyone’s train that is open (a train opens when its owner cannot play). Play a double and you go again. Can’t play: draw one; still can’t: your train opens. First out ends the round; everyone else scores their pips, and the lowest total after the rounds wins.',ctx=>{ const setTimeout=(f,ms)=>ctx.after(ms,f);
  const st={n:2,players:[],bone:[],trains:[],eng:12,turn:0,round:1,rounds:4,tot:[0,0,0,0],over:false,msg:'',sel:null};
  const top=h('div',{className:'dmBtns'}); const pSel=h('select',{'aria-label':'Players'},[2,3,4].map(n=>h('option',{value:String(n)},n+' players'))); const rSel=h('select',{'aria-label':'Rounds'},[[4,'Short game · 4 rounds'],[13,'Full game · 13 rounds']].map(([v,l])=>h('option',{value:String(v)},l))); const nb=h('button',{type:'button',className:'go'},'🚂 New game'); top.append(pSel,rSel,nb); ctx.area.appendChild(top);
  const info=h('div',{className:'dmLbl'}); const board=h('div',{className:'dmFelt',style:'flex-direction:column;align-items:stretch'}); const mine=h('div',{className:'dmRow'}); const btns=h('div',{className:'dmBtns'}); [info,board,mine,btns].forEach(e=>ctx.area.appendChild(e));
  const W=()=>Math.max(22,Math.min(36,Math.floor((ctx.W()-20)/13)));
  function startRound(){ st.bone=set(12); const engT=st.bone.find(t=>t[0]===st.eng&&t[1]===st.eng); st.bone.splice(st.bone.indexOf(engT),1); const k=st.n===2?15:st.n===3?13:12; st.players=[]; for(let i=0;i<st.n;i++) st.players.push(st.bone.splice(0,k));
   st.trains=[]; for(let i=0;i<st.n;i++) st.trains.push({owner:i,tiles:[],end:st.eng,open:false}); st.trains.push({owner:-1,tiles:[],end:st.eng,open:true,mex:true}); st.turn=(st.round-1)%st.n; st.over=false; st.msg='Round '+st.round+': the engine is '+st.eng+'–'+st.eng+'.'; st.sel=null; turnStart(); }
  const canOn=(i,tr)=>tr.mex||tr.owner===i||tr.open;
  const moves=i=>{ const M=[]; st.players[i].forEach(t=>st.trains.forEach((tr,k)=>{ if(canOn(i,tr)&&fits(t,tr.end)) M.push([t,k]); })); return M; };
  function put(i,t,k){ const tr=st.trains[k]; const hd=st.players[i]; hd.splice(hd.indexOf(t),1); const tt=t[0]===tr.end?t.slice():[t[1],t[0]]; tr.tiles.push(tt); tr.end=tt[1]; if(tr.owner===i) tr.open=false; try{ L.beep(380,.04); }catch(_){ } return tt[0]===tt[1]; }
  function turnStart(){ if(st.over) return render(); const i=st.turn; if(i===0){ if(!moves(0).length){ if(st.bone.length){ st.players[0].push(st.bone.pop()); st.msg='You drew a tile.'; } if(!moves(0).length){ st.trains[0].open=true; st.msg='No play: your train is open.'; render(); return setTimeout(endTurn,800); } } st.msg=st.msg||'Your turn: tap a tile, then a lit train.'; return render(); }
   render(); setTimeout(()=>aiTurn(i),650); }
  function aiTurn(i){ let again=true, guard=0; while(again&&guard++<4){ again=false; let M=moves(i); if(!M.length&&st.bone.length){ st.players[i].push(st.bone.pop()); M=moves(i); } if(!M.length){ st.trains[i].open=true; break; }
    M.sort((a,b)=>((b[0][0]+b[0][1])+(st.trains[b[1]].owner===i?6:0))-((a[0][0]+a[0][1])+(st.trains[a[1]].owner===i?6:0))); const [t,k]=M[0]; const dbl=put(i,t,k); if(!st.players[i].length) return endRound(i); if(dbl) again=true; }
   endTurn(); }
  function endTurn(){ if(st.over) return; st.turn=(st.turn+1)%st.n; st.msg=''; turnStart(); }
  function endRound(w){ st.over=true; st.players.forEach((hd,i)=>{ st.tot[i]+=pips(hd); }); st.msg=NAMES[w]+(w?' goes':' go')+' out! Round '+st.round+' scores: '+st.players.map((hd,i)=>NAMES[i]+' '+pips(hd)).join(', ')+'.'; if(st.round>=st.rounds){ let b=0; st.tot.slice(0,st.n).forEach((v,i)=>{ if(v<st.tot[b]) b=i; }); st.msg+=' Game over: '+NAMES[b]+(b?' wins':' win')+' with '+st.tot[b]+'.'; } render(); }
  function render(){ const w=W(); info.textContent='Round '+st.round+' of '+st.rounds+' · '+st.tot.slice(0,st.n).map((v,i)=>NAMES[i]+' '+v).join(' · ')+' (low wins) · boneyard '+st.bone.length;
   board.innerHTML=''; board.appendChild(h('div',{className:'dmLbl'},['Engine ',tile([st.eng,st.eng],{w:w*.8,h:false})]));
   st.trains.forEach((tr,k)=>{ const can=st.sel&&st.turn===0&&canOn(0,tr)&&fits(st.sel,tr.end); const row=h('div',{className:'dmTrain'+(tr.open&&!tr.mex?' open':'')+(can?' can':''),role:'button','aria-label':(tr.mex?'Mexican train':NAMES[tr.owner]+' train')+' ends in '+tr.end}); row.appendChild(h('b',null,tr.mex?'🇲🇽 Mexican':(tr.owner?NAMES[tr.owner]+'’s':'Your')+' train'));
    tr.tiles.slice(-8).forEach(t=>row.appendChild(tile(t,{h:t[0]!==t[1],w:w*.62}))); row.appendChild(h('span',{className:'dmLbl'},'→ '+tr.end)); row.addEventListener('click',()=>{ if(can) mePut(k); }); board.appendChild(row); });
   mine.innerHTML=''; const M=st.turn===0&&!st.over?moves(0):[]; st.players[0]&&st.players[0].slice().sort((a,b)=>a[0]-b[0]||a[1]-b[1]).forEach(t=>{ const e=tile(t,{w,cls:M.some(m=>m[0]===t)?'pl':''}); if(st.sel===t) e.classList.add('sel'); e.addEventListener('click',()=>{ if(st.turn!==0||st.over) return; if(!M.some(m=>m[0]===t)) return ctx.status('That tile fits no train you can use.'); st.sel=t; const opts=M.filter(m=>m[0]===t); if(opts.length===1) return mePut(opts[0][1]); render(); ctx.status('Now tap the lit train to play it on.'); }); mine.appendChild(e); });
   btns.innerHTML=''; if(st.over){ const b=h('button',{type:'button',className:'go'},st.round>=st.rounds?'🚂 New game':'▶ Next round'); b.addEventListener('click',()=>{ if(st.round>=st.rounds){ newGame(); } else { st.round++; st.eng=Math.max(0,st.eng-1); startRound(); } }); btns.appendChild(b); }
   ctx.status(st.msg); }
  function mePut(k){ const t=st.sel; st.sel=null; const dbl=put(0,t,k); if(!st.players[0].length) return endRound(0); if(dbl){ st.msg='A double: play again.'; if(!moves(0).length){ if(st.bone.length) st.players[0].push(st.bone.pop()); if(!moves(0).length){ st.trains[0].open=true; return endTurn(); } } return render(); } endTurn(); }
  function newGame(){ st.n=+pSel.value; st.rounds=+rSel.value; st.round=1; st.eng=12; st.tot=[0,0,0,0]; startRound(); }
  nb.addEventListener('click',newGame); newGame(); window.__kgst=()=>st; return {state:()=>st};
 });
})();
