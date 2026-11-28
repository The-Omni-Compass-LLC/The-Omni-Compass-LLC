(()=>{ /* 🂡 FIVE-CARD ROW (v261): Omni-Galaxy's own card-and-board game for 2 or 3 players. A 10 × 10 board shows every card of two
   decks except the jacks, each twice, with the four corners free for everyone. Play a card from your hand to put a chip on one of
   its two squares, then draw. Five chips in a line (across, down or diagonal; a corner counts for you) make a row; the first to the
   rows the game asks for wins. A ♦ or ♣ jack is wild: a chip on any free square. A ♠ or ♥ jack bumps one rival chip off the board
   (never one in a finished row). A card whose two squares are both taken is dead: swap it for a new one, once a turn. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h, SU=L.SU, VS=L.VS||'', rl=L.rl, cardEl=L.cardEl, shuffle=L.shuffle;
 const OPT=(ctx,id,defs)=>window.KGOPT?KGOPT.row(ctx,id,defs):Object.fromEntries(defs.map(d=>[d[0],d[3]]));
 const beep=(f,d)=>{ try{ L.beep(f,d||.04); }catch(_){ } };
 const NM=['You','Nova','Orion'], CH=['#2f7bff','#ff4b4b','#2fbf71'];
 /* the board: a fixed layout (the same every game, so it can be learned), made by a seeded shuffle of the 96 non-jack cards */
 const BOARD=(()=>{ const cards=[]; for(let k=0;k<2;k++) for(let s=0;s<4;s++) for(let r=1;r<=13;r++) if(r!==11) cards.push({r,s}); let seed=20261128; const rnd=()=>{ seed=(seed*1103515245+12345)%2147483648; return seed/2147483648; }; for(let i=cards.length-1;i>0;i--){ const j=Math.floor(rnd()*(i+1)); [cards[i],cards[j]]=[cards[j],cards[i]]; }
  const B=[]; let k=0; for(let y=0;y<10;y++){ const row=[]; for(let x=0;x<10;x++){ const corner=(x===0||x===9)&&(y===0||y===9); row.push(corner?null:cards[k++]); } B.push(row); } return B; })();
 const css=document.createElement('style'); css.textContent=`
#gamesDock .fcr{display:flex;flex-direction:column;gap:8px;align-items:center}
#gamesDock .fcrB{display:grid;grid-template-columns:repeat(10,var(--c));gap:2px;background:#0b3d24;padding:4px;border-radius:8px;border:2px solid #d4af37}
#gamesDock .fcrB .q{width:var(--c);height:calc(var(--c)*1.25);border-radius:4px;background:#f7f3e8;color:#111;display:flex;flex-direction:column;align-items:center;justify-content:center;font:800 calc(var(--c)*.32)/1.05 system-ui,sans-serif;position:relative;cursor:pointer;user-select:none}
#gamesDock .fcrB .q.red{color:#c4161c}
#gamesDock .fcrB .q.free{background:linear-gradient(135deg,#ffd84a,#e0a10c);color:#3a2600;font-size:calc(var(--c)*.42)}
#gamesDock .fcrB .q.can{box-shadow:0 0 0 3px #e08a00 inset,0 0 10px 2px #ffe94a;background:#ffec7a;z-index:1}
#gamesDock .fcrB .q.bump{box-shadow:0 0 0 3px #ff5ea8 inset}
#gamesDock .fcrB .q .chip{position:absolute;inset:12%;border-radius:50%;border:2px solid rgba(255,255,255,.85);box-shadow:0 2px 3px rgba(0,0,0,.5)}
#gamesDock .fcrB .q .chip.lock{outline:3px solid #ffe94a;outline-offset:-1px}
#gamesDock .fcrB .q.last{animation:fcrP .8s ease 2}
@keyframes fcrP{50%{transform:scale(1.12)}}
#gamesDock .fcrHand{display:flex;flex-wrap:wrap;gap:4px;justify-content:center}
#gamesDock .fcrHand .gcard{cursor:pointer}
#gamesDock .fcrHand .gcard.sel{outline:3px solid #ffe94a;transform:translateY(-6px)}
#gamesDock .fcrMsg{font:800 14px system-ui,sans-serif;color:#ffe94a;text-align:center;min-height:20px}
#gamesDock .fcrScore{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;font:800 13px system-ui}
#gamesDock .fcrScore span{display:inline-flex;align-items:center;gap:4px}
#gamesDock .fcrScore i{width:14px;height:14px;border-radius:50%;display:inline-block}
#gamesDock .fcrBar{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}
#gamesDock .fcrBar button{min-height:42px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 14px system-ui}`; document.head.appendChild(css);
 G.reg('c_fivecardrow','Five-Card Row (card board game)','Cards','Omni-Galaxy’s own card-and-board game. Play a card to put a chip on one of its two squares on the 10 × 10 board; five in a line across, down or diagonal make a row (a free corner counts for you). A ♦ or ♣ jack is wild (any free square); a ♠ or ♥ jack bumps a rival chip off, never one in a finished row. A card whose two squares are both taken is dead: swap it, once a turn. First to the rows needed wins.',ctx=>{
  const O=OPT(ctx,'c_fivecardrow',[['n','Players',[[2,'You and Nova'],[3,'You, Nova and Orion']],2],['rows','Rows to win',[[1,'One row'],[2,'Two rows'],[3,'Three rows']],2],['lvl','Computer',[[0,'Gentle'],[1,'Steady'],[2,'Sharp'],[3,'Shark'],[4,'Grandmaster']],2],['speed','Computer speed',[[1800,'Slow'],[1200,'Relaxed'],[800,'Normal'],[500,'Quick'],[250,'Lightning']],800]]);
  const N=+O.n, NEED=+O.rows, HS=N===2?7:6;
  const st={chip:[],lock:[],deck:[],hand:[],turn:0,sel:null,rows:Array(N).fill(0),over:false,msg:'',traded:false,last:null};
  const root=h('div',{className:'fcr'}); ctx.area.appendChild(root);
  function deal(){ st.chip=[...Array(10)].map(()=>Array(10).fill(-1)); st.lock=[...Array(10)].map(()=>Array(10).fill(false)); const d=shuffle(L.mkDeck(true).concat(L.mkDeck(true)).filter(c=>!c.j)); st.deck=d; st.hand=[...Array(N)].map(()=>d.splice(0,HS)); st.turn=0; st.sel=null; st.rows=Array(N).fill(0); st.over=false; st.traded=false; st.last=null; st.msg='Your turn: pick a card, then a square that shows it.'; render(); }
  const isCorner=(x,y)=>(x===0||x===9)&&(y===0||y===9);
  const kind=c=>c.r===11?((c.s===2||c.s===3)?'wild':'bump'):'card';
  const owns=(p,x,y)=>x>=0&&y>=0&&x<10&&y<10&&(isCorner(x,y)||st.chip[y][x]===p);
  const spots=c=>{ const out=[]; for(let y=0;y<10;y++) for(let x=0;x<10;x++){ const b=BOARD[y][x]; if(b&&b.r===c.r&&b.s===c.s&&st.chip[y][x]<0) out.push([x,y]); } return out; };
  const freeAll=()=>{ const out=[]; for(let y=0;y<10;y++) for(let x=0;x<10;x++) if(BOARD[y][x]&&st.chip[y][x]<0) out.push([x,y]); return out; };
  const rivals=p=>{ const out=[]; for(let y=0;y<10;y++) for(let x=0;x<10;x++) if(st.chip[y][x]>=0&&st.chip[y][x]!==p&&!st.lock[y][x]) out.push([x,y]); return out; };
  const targets=(p,c)=>kind(c)==='wild'?freeAll():kind(c)==='bump'?rivals(p):spots(c);
  const dead=c=>kind(c)==='card'&&!spots(c).length;
  const DIRS=[[1,0],[0,1],[1,1],[1,-1]];
  /* new rows for p through (x,y): a run of 5 with no locked chip of p's own reused more than once (a second row may share one chip) */
  function newRows(p,x,y){ let made=0; for(const [dx,dy] of DIRS){ const line=[]; for(let k=-9;k<=9;k++){ const X=x+dx*k, Y=y+dy*k; if(X<0||Y<0||X>9||Y>9) continue; line.push([X,Y]); }
    let run=[]; const runs=[]; for(const [X,Y] of line){ if(owns(p,X,Y)) run.push([X,Y]); else { if(run.length>=5) runs.push(run); run=[]; } } if(run.length>=5) runs.push(run);
    for(const r of runs){ for(let i=0;i+5<=r.length;i++){ const seg=r.slice(i,i+5); if(!seg.some(([X,Y])=>X===x&&Y===y)) continue; const shared=seg.filter(([X,Y])=>st.lock[Y][X]).length; if(shared<=1){ seg.forEach(([X,Y])=>{ if(!isCorner(X,Y)) st.lock[Y][X]=true; }); made++; break; } } } } return made; }
  function place(p,i,x,y){ const c=st.hand[p][i]; const k=kind(c); if(k==='bump'){ st.chip[y][x]=-1; st.msg=NM[p]+' bumped a chip off '+lab(BOARD[y][x])+'.'; beep(220,.06); }
   else { st.chip[y][x]=p; const m=newRows(p,x,y); if(m){ st.rows[p]+=m; beep(880,.12); } else beep(p?330:600,.04); st.msg=NM[p]+(k==='wild'?' played a wild jack on ':' played ')+lab(BOARD[y][x])+(m?' and made a row! ('+st.rows[p]+' of '+NEED+')':'')+'.'; }
   st.last=[x,y]; st.hand[p].splice(i,1); if(st.deck.length) st.hand[p].push(st.deck.pop());
   if(st.rows[p]>=NEED){ st.over=true; st.msg=(p?NM[p]+' wins with '+st.rows[p]+' row'+(st.rows[p]>1?'s':''):'🏆 You win with '+st.rows[p]+' row'+(st.rows[p]>1?'s':'')+'!'); try{ ctx.status&&ctx.status(st.msg); }catch(_){ } render(); return; }
   if(!st.hand.some(hd=>hd.length)){ st.over=true; const mx=Math.max(...st.rows), w=st.rows.indexOf(mx), tie=st.rows.filter(v=>v===mx).length>1; st.msg='No cards left. '+(tie?'A draw on rows.':w===0?'🏆 You win on rows ('+mx+').':NM[w]+' wins on rows ('+mx+').'); render(); return; }
   st.turn=(p+1)%N; st.traded=false; st.sel=null; render(); if(st.turn!==0) ctx.after(+O.speed,ai); }
  const lab=b=>b?rl(b.r)+SU[b.s]+VS:'a corner';
  /* the computer: scores every legal move by the lines it builds or blocks */
  function lineScore(p,x,y){ let best=0; for(const [dx,dy] of DIRS){ for(let s=-4;s<=0;s++){ let mine=0, ok=true; for(let k=0;k<5;k++){ const X=x+dx*(s+k), Y=y+dy*(s+k); if(X<0||Y<0||X>9||Y>9){ ok=false; break; } if(X===x&&Y===y){ mine++; continue; } if(owns(p,X,Y)) mine++; else if(st.chip[Y][X]>=0) { ok=false; break; } } if(ok) best=Math.max(best,mine); } } return best; }
  function ai(){ if(st.over) return; const p=st.turn; if(p===0) return; const hd=st.hand[p]; const lvl=+O.lvl;
   for(let i=0;i<hd.length;i++){ if(dead(hd[i])&&!st.traded&&st.deck.length){ hd.splice(i,1); hd.push(st.deck.pop()); st.traded=true; i--; } }
   let best=null, bs=-1e9;
   hd.forEach((c,i)=>{ const k=kind(c); targets(p,c).forEach(([x,y])=>{ let s;
     if(k==='bump'){ const q=st.chip[y][x]; s=Math.pow(lineScore(q,x,y),3)*2-20; }
     else { const mine=lineScore(p,x,y); let block=0; for(let q=0;q<N;q++) if(q!==p) block=Math.max(block,lineScore(q,x,y)); s=Math.pow(mine,3)*3+(mine>=5?1000:0)+Math.pow(block,3)*(lvl>=2?2.6:1.2)+(block>=5?600:0)-(k==='wild'?(mine>=5||block>=5?0:40):0)+(4.5-Math.abs(4.5-x))+(4.5-Math.abs(4.5-y)); }
     s+=Math.random()*(lvl<=0?40:lvl===1?16:lvl===2?6:2); if(s>bs){ bs=s; best=[i,x,y]; } }); });
   if(!best){ st.msg=NM[p]+' has no move and passes.'; st.turn=(p+1)%N; render(); if(st.turn!==0) ctx.after(+O.speed,ai); return; }
   place(p,best[0],best[1],best[2]); }
  function render(){ root.innerHTML=''; const W=(ctx.W&&ctx.W())||360; const c=Math.max(24,Math.min(58,Math.floor((W-40)/10)-2));
   root.appendChild(h('div',{className:'fcrScore'})); const sc=root.lastChild; for(let p=0;p<N;p++){ const s=h('span'); s.appendChild(h('i',{style:'background:'+CH[p]})); s.appendChild(document.createTextNode(NM[p]+': '+st.rows[p]+' / '+NEED+(p===st.turn&&!st.over?' ◀':''))); sc.appendChild(s); }
   root.appendChild(h('div',{className:'fcrMsg'},st.msg));
   const my=st.turn===0&&!st.over; const selC=my&&st.sel!=null?st.hand[0][st.sel]:null; const tg=selC?targets(0,selC):[]; const isT=(x,y)=>tg.some(t=>t[0]===x&&t[1]===y);
   const B=h('div',{className:'fcrB',style:'--c:'+c+'px'}); for(let y=0;y<10;y++) for(let x=0;x<10;x++){ const b=BOARD[y][x]; const q=h('div',{className:'q'+(b?((b.s===1||b.s===2)?' red':''):' free')+(isT(x,y)?(kind(selC)==='bump'?' bump':' can'):'')+(st.last&&st.last[0]===x&&st.last[1]===y?' last':'')});
    if(b){ q.appendChild(h('span',null,rl(b.r))); q.appendChild(h('span',null,SU[b.s]+VS)); } else q.textContent='★';
    if(st.chip[y][x]>=0){ const ch=h('div',{className:'chip'+(st.lock[y][x]?' lock':''),style:'background:'+CH[st.chip[y][x]]}); q.appendChild(ch); }
    q.setAttribute('aria-label',(b?lab(b):'free corner')+(st.chip[y][x]>=0?', '+NM[st.chip[y][x]]+'’s chip':''));
    q.addEventListener('click',()=>{ if(!my||st.sel==null) return; if(!isT(x,y)) return; place(0,st.sel,x,y); }); B.appendChild(q); }
   root.appendChild(B);
   const hand=h('div',{className:'fcrHand'}); st.hand[0].forEach((cd,i)=>{ const e=cardEl(cd,Math.max(34,Math.min(60,Math.floor((W-40)/8))),false,(st.sel===i?'sel':'')+(dead(cd)?' dim':'')); e.title=kind(cd)==='wild'?'Wild jack: any free square':kind(cd)==='bump'?'Bump jack: take a rival chip off':dead(cd)?'Dead card: both squares are taken':'Two squares on the board'; e.addEventListener('click',()=>{ if(!my) return; st.sel=st.sel===i?null:i; const k=kind(cd); st.msg=st.sel==null?'Pick a card.':k==='wild'?'Wild jack: tap any free square.':k==='bump'?'Bump jack: tap a rival chip (not in a finished row).':dead(cd)?'Dead card: both its squares are taken. Swap it below.':'Tap one of the glowing squares.'; render(); }); hand.appendChild(e); });
   root.appendChild(hand);
   const bar=h('div',{className:'fcrBar'}); const add=(t,f)=>{ const b=h('button',{type:'button'},t); b.addEventListener('click',f); bar.appendChild(b); };
   if(my&&selC&&dead(selC)&&!st.traded) add('♻ Swap the dead card',()=>{ st.hand[0].splice(st.sel,1); if(st.deck.length) st.hand[0].push(st.deck.pop()); st.traded=true; st.sel=null; st.msg='Swapped. Pick a card.'; render(); });
   add(st.over?'🔄 Play again':'🔄 New game',deal); root.appendChild(bar); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
})();
