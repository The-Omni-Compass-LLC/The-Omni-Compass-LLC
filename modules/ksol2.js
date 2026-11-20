(()=>{ /* 🂡 FOUR MORE PATIENCE GAMES (v224): Scorpion, Canfield, Baker's Dozen and Calculation, on the shared table engine
   (tap a card, tap where it goes; tap twice to send it home; Auto, Undo, Keys: Space draws, A auto, U undo). Traditional public-domain rules. */
 const G0=window.GAMES; if(!G0||!G0.reg||!G0._sol) return; const S=G0._sol, L=G0.lib, shuffle=L.shuffle, mkDeck=L.mkDeck; const CAT='Cards';
 const {TabSol,emptySt,topRowFound,tabCols,foundOK,flipTops,fcount,red}=S;
 const up=c=>{ c.up=true; return c; }, down=c=>{ c.up=false; return c; };
 /* ───── SCORPION ───── */
 G0.reg('c_scorpion','Scorpion Solitaire',CAT,'Seven columns of seven cards; in the first four columns the top three cards are face down. Three cards wait in the reserve. Build down in the same suit (a 7♥ goes on an 8♥). Any face-up card may be moved, together with every card on top of it, even if they are not in order. Only a King (with whatever is on it) may fill an empty column. Tap the reserve once to deal its three cards onto the first three columns. A complete run from King down to Ace in one suit leaves the table by itself; clear all four to win.',ctx=>{
  const G={cols:7,maxw:84,nf:4,hasStock:true,
   deal(){ const d=shuffle(mkDeck(true)), st=emptySt(4,7); for(let t=0;t<7;t++) for(let k=0;k<7;k++){ const c=d.pop(); c.up=!(t<4&&k<3); st.p['t'+t].push(c); } st.p.s=d.map(down); return st; },
   layout(B){ return [{id:'s',x:0,y:0,count:1}].concat(topRowFound(B,4,3),tabCols(B,7,B.ch+16)); },
   pick(st,id,i){ return id.charAt(0)==='t'&&st.p[id][i].up; },
   drop(st,cs,from,id){ if(id.charAt(0)!=='t'||from.charAt(0)==='f') return false; const T=st.p[id]; if(!T.length) return cs[0].r===13; const t=T[T.length-1]; return t.up&&t.s===cs[0].s&&t.r===cs[0].r+1; },
   targets(st){ const a=[],e=[]; for(let t=0;t<7;t++){ (st.p['t'+t].length?a:e).push('t'+t); } return a.concat(e); },
   pointless(st,id,i,to){ return i===0&&!st.p[to].length; },
   stock(st){ if(!st.p.s.length) return 'The reserve is already dealt.'; for(let t=0;t<3&&st.p.s.length;t++) st.p['t'+t].push(up(st.p.s.pop())); return true; },
   after(st){ flipTops(st,'t'); for(let t=0;t<7;t++){ const C=st.p['t'+t]; if(C.length<13) continue; const run=C.slice(-13); if(run.every((c,k)=>c.up&&c.s===run[0].s&&c.r===13-k)){ for(let f=0;f<4;f++){ if(!st.p['f'+f].length){ st.p['f'+f]=C.splice(-13).reverse(); break; } } flipTops(st,'t'); } } },
   won(st){ return fcount(st)===52; },
   status(st){ return 'Runs cleared '+(fcount(st)/13)+'/4 · Reserve '+st.p.s.length; }};
  return TabSol(ctx,G); });
 /* ───── CANFIELD ───── */
 G0.reg('c_canfield','Canfield',CAT,'Thirteen cards form the reserve (only its top card shows), four cards start the tableau and one card starts the first foundation: its rank is the base every foundation starts from (the other three start when a card of that rank turns up). Build the foundations up in suit from the base, going round the corner from King to Ace. Build the tableau down in alternating colors, also round the corner (an Ace may go on a 2, a King on an Ace); move whole columns together. An empty column fills itself from the reserve (and from the waste once the reserve is gone). Tap the stock to turn three cards; turn through it as often as you like. Win by building all 52 cards onto the foundations.',ctx=>{
  let base=1; const nx=r=>r===13?1:r+1;
  const G={cols:7,maxw:84,nf:4,hasStock:true,w3:3,
   deal(){ const d=shuffle(mkDeck(true)), st=emptySt(4,4); st.p.r=[]; for(let k=0;k<13;k++) st.p.r.push(down(d.pop())); up(st.p.r[12]); const b=up(d.pop()); base=b.r; st.base=base; st.p.f0.push(b); for(let t=0;t<4;t++) st.p['t'+t].push(up(d.pop())); st.p.s=d.map(down); st.p.w=[]; return st; },
   layout(B){ return [{id:'s',x:0,y:0,count:1},{id:'w',x:B.colW,y:0,fan:'w3'}].concat(topRowFound(B,4,3)).concat([{id:'r',x:0,y:B.ch+16,count:1}]).concat(tabCols(B,4,B.ch+16,3)); },
   pick(st,id,i){ const P=st.p[id]; if(id==='r'||id==='w') return i===P.length-1&&P[i].up; return id.charAt(0)==='t'&&P[i].up; },
   drop(st,cs,from,id){ const c=cs[0]; if(from.charAt(0)==='f') return false;
    if(id.charAt(0)==='f'){ if(cs.length!==1) return false; const F=st.p[id]; if(!F.length) return c.r===(st.base||base)&&!['f0','f1','f2','f3'].some(f=>st.p[f].length&&st.p[f][0].s===c.s); return F[0].s===c.s&&c.r===nx(F[F.length-1].r); }
    if(id.charAt(0)!=='t') return false; const T=st.p[id]; if(!T.length) return true; const t=T[T.length-1]; return red(t)!==red(c)&&nx(c.r)===t.r; },
   targets(){ return ['f0','f1','f2','f3','t0','t1','t2','t3']; },
   pointless(st,id,i,to){ return id.charAt(0)==='t'&&i===0&&!st.p[to].length; },
   stock(st){ if(!st.p.s.length){ if(!st.p.w.length) return 'The stock is empty.'; st.p.s=st.p.w.reverse().map(down); st.p.w=[]; return true; } for(let k=0;k<3&&st.p.s.length;k++) st.p.w.push(up(st.p.s.pop())); return true; },
   after(st){ for(let t=0;t<4;t++){ const T=st.p['t'+t]; if(T.length) continue; if(st.p.r.length) T.push(up(st.p.r.pop())); else if(st.p.w.length) T.push(st.p.w.pop()); } if(st.p.r.length) up(st.p.r[st.p.r.length-1]); },
   safe(st,c){ return true; },
   won(st){ return fcount(st)===52; },
   status(st){ return 'Base rank '+L.rl(st.base||base)+' · Foundations '+fcount(st)+'/52 · Reserve '+st.p.r.length+' · Stock '+st.p.s.length; }};
  return TabSol(ctx,G); });
 /* ───── BAKER'S DOZEN ───── */
 G0.reg('c_bakers','Baker’s Dozen',CAT,'Thirteen columns of four cards, all face up; any King is moved under the other cards of its column at the deal. Build the four foundations up in suit from Ace to King. On the columns build down by one, in any suit, moving one card at a time. An empty column stays empty. There is no stock: plan ahead.',ctx=>{
  const G={cols:7,maxw:70,nf:4,
   deal(){ const d=shuffle(mkDeck(true)), st=emptySt(4,13); for(let t=0;t<13;t++){ const C=[]; for(let k=0;k<4;k++) C.push(up(d.pop())); C.sort((a,b)=>(b.r===13)-(a.r===13)); st.p['t'+t]=C; } return st; },
   layout(B){ const a=topRowFound(B,4,1.5), gap=Math.round(B.ch*3.1); for(let t=0;t<13;t++){ const row=t<7?0:1, col=t<7?t:t-7+0.5; a.push({id:'t'+t,x:col*B.colW,y:B.ch+14+row*gap,fan:'down',room:row?undefined:gap-B.ch-10}); } return a; },
   pick(st,id,i){ return id.charAt(0)==='t'&&i===st.p[id].length-1; },
   drop(st,cs,from,id){ if(cs.length!==1||from.charAt(0)==='f') return false; if(id.charAt(0)==='f') return foundOK(st,cs,id); if(id.charAt(0)!=='t') return false; const T=st.p[id]; if(!T.length) return false; return T[T.length-1].r===cs[0].r+1; },
   targets(){ const a=['f0','f1','f2','f3']; for(let t=0;t<13;t++) a.push('t'+t); return a; },
   autoSafe:true, safe(st,c){ return S.safeF(st,c,4); },
   won(st){ return fcount(st)===52; },
   status(st){ return 'Foundations '+fcount(st)+'/52'; }};
  return TabSol(ctx,G); });
 /* ───── CALCULATION ───── */
 G0.reg('c_calc','Calculation (Broken Intervals)',CAT,'A patience of arithmetic. An Ace, a 2, a 3 and a 4 start four foundations. Each foundation counts by its own step, ignoring suits and going round after the King: the first by ones (A 2 3 … K), the second by twos (2 4 6 8 10 Q A 3 5 7 9 J K), the third by threes (3 6 9 Q 2 5 8 J A 4 7 10 K), the fourth by fours (4 8 Q 3 7 J 2 6 10 A 5 9 K). Tap the stock to turn one card; it must go onto a foundation that wants it or onto one of the four waste piles before you turn the next. Only the top card of a waste pile may be played, and only to a foundation. Win by finishing all four foundations on a King.',ctx=>{
  const want=(F,i)=>{ const top=F[F.length-1].r; return ((top-1+(i+1))%13)+1; };
  const G={cols:6,maxw:84,nf:4,hasStock:true,
   deal(){ const d=mkDeck(true), st=emptySt(4,4); [1,2,3,4].forEach((r,i)=>{ const k=d.findIndex(c=>c.r===r&&c.s===i); st.p['f'+i].push(up(d.splice(k,1)[0])); }); st.p.s=shuffle(d).map(down); st.p.w=[]; return st; },
   layout(B){ return [{id:'s',x:0,y:0,count:1},{id:'w',x:B.colW,y:0}].concat(topRowFound(B,4,2)).concat(tabCols(B,4,B.ch+16,2)); },
   pick(st,id,i){ const P=st.p[id]; return (id==='w'||id.charAt(0)==='t')&&i===P.length-1; },
   drop(st,cs,from,id){ if(cs.length!==1||from.charAt(0)==='f') return false; const c=cs[0]; if(id.charAt(0)==='f'){ const i=+id.slice(1), F=st.p[id]; if(F[F.length-1].r===13&&F.length===13) return false; return c.r===want(F,i); } if(id.charAt(0)==='t') return from==='w'; return false; },
   targets(){ return ['f0','f1','f2','f3']; },
   stock(st){ if(st.p.w.length) return 'Place the turned card first: on a foundation or a waste pile.'; if(!st.p.s.length) return 'The stock is used up.'; st.p.w.push(up(st.p.s.pop())); return true; },
   won(st){ return fcount(st)===52; },
   status(st){ return 'Foundations '+fcount(st)+'/52 · next: '+[0,1,2,3].map(i=>{ const F=st.p['f'+i]; return !F.length?'–':F.length===13?'✓':L.rl(want(F,i)); }).join(' · ')+' · Stock '+st.p.s.length; }};
  return TabSol(ctx,G); });
})();
