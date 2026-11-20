(()=>{ /* 🀄 MAHJONG (v220): Tile-Matching Solitaire (every layout dealt solvable; hint, shuffle, undo) and four-player Mahjong against
   three computer players by the classic rules: draw and discard, claim a discard for a pung, a kong or (from the player before you)
   a chow, and go out with four sets and a pair, or seven pairs. Scoring counts self-draw, all pungs, half and full flush, seven
   pairs and dragon pungs. Phone first. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h; const CAT='Mahjong'; const rn=n=>Math.floor(Math.random()*n);
 const css=document.createElement('style'); css.textContent=`
.mjT{position:relative;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;width:var(--mw,36px);height:calc(var(--mw,36px)*1.32);background:linear-gradient(160deg,#fffdf4,#e9e1c8);border:1.5px solid #6b5a33;border-radius:5px;box-shadow:2px 3px 0 #b9a46d,3px 5px 4px rgba(0,0,0,.45);padding:0!important;min-height:0!important;margin:1px;line-height:1;flex:none;font-family:"Noto Serif CJK SC","Songti SC","SimSun",serif}
.mjT b{font:900 calc(var(--mw,36px)*.42)/1 system-ui,sans-serif}.mjT i{font-style:normal;font-size:calc(var(--mw,36px)*.42);line-height:1.05}
.mjT.m b,.mjT.m i{color:#c41f1f}.mjT.s b,.mjT.s i{color:#167a3a}.mjT.p b,.mjT.p i{color:#1d4fb8}.mjT.z i{font-size:calc(var(--mw,36px)*.62);color:#111}.mjT.zr i{color:#c41f1f}.mjT.zg i{color:#167a3a}.mjT.zw i{color:#1d4fb8}.mjT.f i{font-size:calc(var(--mw,36px)*.5);color:#a0522d}
.mjT.sel{outline:3px solid #ffe94a;transform:translateY(-5px)}.mjT.hint{outline:3px solid #2fd27a}.mjT.dim{filter:brightness(.72)}.mjT.back{background:linear-gradient(160deg,#1d8a5a,#0b4a2e)}
.mjBoard{position:relative;margin:6px auto;touch-action:manipulation}
.mjBoard .mjT{position:absolute}
.mjRow{display:flex;flex-wrap:wrap;gap:1px;justify-content:center;align-items:flex-end;margin:4px 0;min-height:30px}
.mjLbl{font:800 13px system-ui,sans-serif;color:#fff;text-align:center;margin:3px 0}.mjLbl b{color:#ffe94a}
.mjBtns{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}.mjBtns button{min-height:46px;border-radius:12px;padding:4px 14px!important;font:800 14px system-ui,sans-serif}
.mjBtns button.go{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important}
.mjFelt{background:radial-gradient(ellipse at 50% 30%,#1f8a4c,#0b5a2e 70%,#063d1f);border:8px solid #5a3417;border-radius:18px;padding:6px}
.mjSeat{display:flex;flex-wrap:wrap;align-items:center;gap:4px;justify-content:center;margin:2px 0}
.mjSeat .nm{font:800 12px system-ui,sans-serif;color:#fff;background:rgba(0,0,0,.4);border-radius:8px;padding:2px 6px}.mjSeat.act .nm{box-shadow:0 0 0 2px #ffe94a}
.mjPond{display:flex;flex-wrap:wrap;gap:1px;justify-content:center;min-height:40px;background:rgba(0,0,0,.15);border-radius:10px;padding:4px;margin:4px 0}`; document.head.appendChild(css);
 const HON={z1:'東',z2:'南',z3:'西',z4:'北',z5:'中',z6:'發',z7:'白'}, SUITCH={m:'萬',s:'竹',p:'筒'}, FL=['梅','蘭','菊','竹','春','夏','秋','冬'];
 const NAME=c=>c[0]==='z'?['East','South','West','North','Red dragon','Green dragon','White dragon'][+c[1]-1]+' tile':c[0]==='f'?'flower':c[1]+' of '+{m:'characters',s:'bamboo',p:'dots'}[c[0]];
 function tileEl(c,w,o){ o=o||{}; const cls=c[0]==='z'?'z'+(c==='z5'?' zr':c==='z6'?' zg':c==='z7'?' zw':''):c[0]==='f'?'f':c[0]; const e=h('button',{type:'button',className:'mjT '+(o.back?'back':cls)+(o.cls?' '+o.cls:''),'aria-label':o.back?'face-down tile':NAME(c)}); e.style.setProperty('--mw',w+'px');
  if(!o.back){ if(c[0]==='z') e.appendChild(h('i',null,HON[c])); else if(c[0]==='f') e.appendChild(h('i',null,FL[+c[1]])); else { e.appendChild(h('b',null,c[1])); e.appendChild(h('i',null,SUITCH[c[0]])); } } return e; }
 const ALL=[]; ['m','s','p'].forEach(s=>{ for(let n=1;n<=9;n++) ALL.push(s+n); }); for(let n=1;n<=7;n++) ALL.push('z'+n);
 const ord=c=>({m:0,s:1,p:2,z:3,f:4}[c[0]])*10+ +c[1]; const srt=a=>a.sort((x,y)=>ord(x)-ord(y));
 /* ───── Tile-Matching Solitaire ───── */
 function layout(){ const P=[]; for(let r=0;r<8;r++) for(let c=0;c<6;c++) P.push({x:2*c,y:2*r,z:0}); for(let r=0;r<6;r++) for(let c=0;c<4;c++) P.push({x:2+2*c,y:2+2*r,z:1}); for(let r=0;r<4;r++) for(let c=0;c<2;c++) P.push({x:4+2*c,y:4+2*r,z:2}); P.push({x:5,y:6,z:3},{x:5,y:8,z:3}); return P; }
 function freeIn(P,set,i){ const a=P[i]; for(const j of set){ if(j===i) continue; const b=P[j]; if(b.z>a.z&&Math.abs(b.x-a.x)<2&&Math.abs(b.y-a.y)<2) return false; } let lb=false, rb=false; for(const j of set){ if(j===i) continue; const b=P[j]; if(b.z===a.z&&Math.abs(b.y-a.y)<2){ if(b.x===a.x-2) lb=true; if(b.x===a.x+2) rb=true; } } return !(lb&&rb); }
 function deal(P,idxs){ for(let tries=0;tries<200;tries++){ const left=new Set(idxs), order=[]; let ok=true; while(left.size){ const fr=[...left].filter(i=>freeIn(P,left,i)); if(fr.length<2){ ok=false; break; } const a=fr.splice(rn(fr.length),1)[0], b=fr[rn(fr.length)]; left.delete(a); left.delete(b); order.push([a,b]); } if(ok) return order; } return null; }
 G.reg('mj_solitaire','Mahjong Tile-Matching Solitaire',CAT,'Clear the stack by matching pairs of identical tiles. A tile can be taken when nothing sits on top of it and its left or right side is open. Every deal is solvable; Hint shows a pair, Shuffle re-deals what is left (still solvable), Undo takes back a match.',ctx=>{
  const P=layout(); let face=[], on=new Set(), sel=null, hist=[], hint=null, start=0;
  const info=h('div',{className:'mjLbl'}); const board=h('div',{className:'mjBoard'}); const btns=h('div',{className:'mjBtns'}); ctx.area.append(info,board,btns);
  const mk=(l,f,c)=>{ const b=h('button',{type:'button',className:c||''},l); b.addEventListener('click',f); btns.appendChild(b); }; mk('💡 Hint',()=>{ hint=pairs()[0]||null; if(!hint) ctx.status('No moves: tap Shuffle.'); draw(); }); mk('🔀 Shuffle',()=>{ reface([...on]); hint=null; draw(); ctx.status('Shuffled.'); }); mk('↶ Undo',()=>{ const u=hist.pop(); if(u){ u.forEach(i=>on.add(i)); draw(); } }); mk('🀄 New deal',newDeal,'go');
  function reface(idxs){ const order=deal(P,idxs); if(!order) return; const types=[]; const pool=L.shuffle(ALL.concat(ALL)); let k=0; order.forEach(([a,b])=>{ const t=pool[k++%pool.length]; face[a]=t; face[b]=t; }); }
  function newDeal(){ face=new Array(P.length); on=new Set(P.map((_,i)=>i)); hist=[]; sel=null; hint=null; reface([...on]); start=performance.now(); draw(); ctx.status('Match identical free tiles.'); }
  const isFree=i=>freeIn(P,on,i);
  function pairs(){ const fr=[...on].filter(isFree); for(let a=0;a<fr.length;a++) for(let b=a+1;b<fr.length;b++) if(face[fr[a]]===face[fr[b]]) return [[fr[a],fr[b]]]; return []; }
  function draw(){ const W=Math.min(ctx.W(),560); const tw=Math.floor(W/6.8), th=Math.round(tw*1.32); board.style.width=(tw*6+tw*.3)+'px'; board.style.height=(th*8+th*.3)+'px'; board.innerHTML='';
   [...on].sort((a,b)=>P[a].z-P[b].z||P[a].y-P[b].y||P[a].x-P[b].x).forEach(i=>{ const p=P[i]; const free=isFree(i); const e=tileEl(face[i],tw-2,{cls:(sel===i?'sel ':'')+(hint&&hint.includes(i)?'hint ':'')+(free?'':'dim')}); e.style.left=(p.x*tw/2-p.z*3)+'px'; e.style.top=(p.y*th/2-p.z*4)+'px'; e.style.zIndex=String(p.z*100+p.y); e.addEventListener('click',()=>tap(i)); board.appendChild(e); });
   info.textContent='Tiles left '+on.size+' · moves available '+(()=>{ const fr=[...on].filter(isFree); let n=0; for(let a=0;a<fr.length;a++) for(let b=a+1;b<fr.length;b++) if(face[fr[a]]===face[fr[b]]) n++; return n; })(); }
  function tap(i){ if(!isFree(i)){ ctx.status('That tile is blocked.'); return; } if(sel===null||sel===i){ sel=sel===i?null:i; return draw(); } if(face[sel]===face[i]){ on.delete(sel); on.delete(i); hist.push([sel,i]); try{ L.beep(880,.05); }catch(_){ } sel=null; hint=null; if(!on.size){ const s=Math.round((performance.now()-start)/1000); ctx.status('Cleared in '+Math.floor(s/60)+':'+String(s%60).padStart(2,'0')+'!'); } else if(!pairs().length) ctx.status('No moves left: tap Shuffle.'); } else sel=i; draw(); }
  newDeal(); return {state:()=>({left:on.size})};
 });
 /* ───── Four-player Mahjong ───── */
 const counts=a=>{ const m={}; a.forEach(c=>m[c]=(m[c]||0)+1); return m; };
 function sets(m,need){ if(need===0) return true; const k=Object.keys(m).filter(c=>m[c]>0).sort((a,b)=>ord(a)-ord(b))[0]; if(!k) return false; if(m[k]>=3){ m[k]-=3; const ok=sets(m,need-1); m[k]+=3; if(ok) return true; }
  if(k[0]!=='z'){ const n=+k[1], a=k[0]+(n+1), b=k[0]+(n+2); if(n<=7&&m[a]>0&&m[b]>0){ m[k]--; m[a]--; m[b]--; const ok=sets(m,need-1); m[k]++; m[a]++; m[b]++; if(ok) return true; } } return false; }
 function isWin(conc,melds){ const need=4-melds.length; if(conc.length!==need*3+2) return false; const m=counts(conc); if(!melds.length&&Object.values(m).every(v=>v===2)&&conc.length===14) return 'seven'; for(const k of Object.keys(m)) if(m[k]>=2){ m[k]-=2; const ok=sets(m,need); m[k]+=2; if(ok) return 'std'; } return false; }
 function score(conc,melds,self,kind){ let f=1; const all=conc.concat(...melds.map(x=>x.t)); const suits=new Set(all.filter(c=>c[0]!=='z').map(c=>c[0])); const hon=all.some(c=>c[0]==='z'); const why=['win'];
  if(self){ f++; why.push('self-drawn'); } if(kind==='seven'){ f+=4; why.push('seven pairs'); } if(suits.size===1&&!hon){ f+=6; why.push('full flush'); } else if(suits.size===1&&hon){ f+=3; why.push('half flush'); }
  const m=counts(conc); const pungs=melds.filter(x=>x.k!=='chow').length; const chows=melds.filter(x=>x.k==='chow').length; if(kind==='std'&&!chows&&isAllP(m,4-melds.length)){ f+=3; why.push('all pungs'); }
  ['z5','z6','z7'].forEach(d=>{ if(melds.some(x=>x.k!=='chow'&&x.t[0]===d)||(m[d]||0)>=3){ f++; why.push('dragon pung'); } }); return {f,why}; }
 function isAllP(m,need){ const mm=Object.assign({},m); for(const k of Object.keys(mm)) if(mm[k]>=2){ mm[k]-=2; let ok=Object.values(mm).every(v=>v%3===0); mm[k]+=2; if(ok) return true; } return false; }
 G.reg('mj_four','Mahjong (4 players)',CAT,'Classic four-player Mahjong: you and three computer players, 136 tiles. Each turn draw a tile, then discard one. Claim a discard to make a pung (three alike), a kong (four alike) or, from the player before you, a chow (a run of three). Go out with four sets and a pair, or seven pairs. Scores: 1 for the win, +1 self-drawn, +3 all pungs, +3 half flush, +6 full flush, +4 seven pairs, +1 each dragon pung; the discarder pays, or everyone pays on a self-draw.',ctx=>{ const setTimeout=(f,ms)=>ctx.after(ms,f);
  const N=['You','East AI','South AI','West AI'];
  const st={wall:[],hands:[[],[],[],[]],melds:[[],[],[],[]],ponds:[[],[],[],[]],turn:0,dealer:0,score:[0,0,0,0],phase:'idle',last:null,sel:null,claim:null,msg:''};
  const felt=h('div',{className:'mjFelt'}); const seats=h('div'); const pond=h('div',{className:'mjPond','aria-label':'Discards'}); const mineM=h('div',{className:'mjRow'}); const mine=h('div',{className:'mjRow'}); const btns=h('div',{className:'mjBtns'}); const info=h('div',{className:'mjLbl'});
  felt.append(seats,pond); ctx.area.append(info,felt,mineM,mine,btns);
  const W=()=>Math.max(22,Math.min(42,Math.floor((ctx.W()-16)/14.5)));
  function newHand(){ st.wall=L.shuffle(ALL.flatMap(c=>[c,c,c,c])); for(let i=0;i<4;i++){ st.hands[i]=srt(st.wall.splice(0,13)); st.melds[i]=[]; st.ponds[i]=[]; } st.turn=st.dealer; st.last=null; st.claim=null; st.sel=null; st.msg='New hand. '+N[st.dealer]+' deals.'; draw(st.turn); }
  function draw(i){ if(!st.wall.length){ st.phase='over'; st.msg='The wall is empty: a drawn hand. No one scores.'; return render(); } const t=st.wall.pop(); st.hands[i].push(t); srt(st.hands[i]); st.phase='discard'; st.drawn=t;
   if(isWin(st.hands[i],st.melds[i])){ if(i===0){ st.msg='You can win on your own draw! Tap 🀄 Mahjong.'; return render(); } return win(i,null); }
   if(i===0){ st.msg='Your turn: tap a tile, then Discard.'; return render(); } render(); setTimeout(()=>aiDiscard(i),550); }
  function useful(hd,c){ const m=counts(hd); let s=(m[c]||0)*3; if(c[0]!=='z'){ const n=+c[1]; [-2,-1,1,2].forEach(d=>{ if(m[c[0]+(n+d)]) s+=Math.abs(d)===1?2:1; }); if(n===1||n===9) s-=.5; } else if((m[c]||0)===1) s-=1; return s; }
  function aiDiscard(i){ const hd=st.hands[i]; let best=hd[0], bs=1e9; hd.forEach(c=>{ const s=useful(hd,c)+Math.random()*.3; if(s<bs){ bs=s; best=c; } }); discard(i,best); }
  function discard(i,c){ const hd=st.hands[i]; hd.splice(hd.indexOf(c),1); st.ponds[i].push(c); st.last={c,from:i}; st.phase='claims'; try{ L.beep(500,.03); }catch(_){ } claims(); }
  function claims(){ const {c,from}=st.last; const order=[1,2,3].map(k=>(from+k)%4);
   for(const i of order) if(isWin(st.hands[i].concat([c]),st.melds[i])){ if(i===0){ st.claim={win:true,c}; return offer(); } return win(i,from); }
   for(const i of order){ const n=st.hands[i].filter(x=>x===c).length; if(n>=2){ if(i===0){ st.claim={pung:true,kong:n>=3,c}; break; } if(Math.random()<.75){ return meld(i,n>=3?'kong':'pung',c); } } }
   const nx=(from+1)%4; const ch=chows(st.hands[nx],c); if(ch.length){ if(nx===0){ st.claim=Object.assign(st.claim||{c},{chow:ch}); } else if(!st.claim&&Math.random()<.4) return meld(nx,'chow',c,ch[0]); }
   if(st.claim&&(st.claim.pung||st.claim.chow)) return offer(); st.claim=null; st.turn=nx; setTimeout(()=>draw(st.turn),nx===0?200:350); }
  function chows(hd,c){ if(c[0]==='z') return []; const s=c[0], n=+c[1], m=counts(hd), R=[]; [[n-2,n-1],[n-1,n+1],[n+1,n+2]].forEach(([a,b])=>{ if(a>=1&&b<=9&&m[s+a]&&m[s+b]) R.push([s+a,s+b]); }); return R; }
  function meld(i,k,c,pair){ const hd=st.hands[i]; st.ponds[st.last.from].pop(); let t; if(k==='chow'){ pair.forEach(x=>hd.splice(hd.indexOf(x),1)); t=srt(pair.concat([c])); } else { const n=k==='kong'?3:2; for(let j=0;j<n;j++) hd.splice(hd.indexOf(c),1); t=new Array(n+1).fill(c); }
   st.melds[i].push({k,t}); st.msg=N[i]+(i?' calls ':' call ')+k.toUpperCase()+'!'; st.claim=null; st.turn=i; try{ L.beep(700,.08); }catch(_){ } if(k==='kong') return draw(i); st.phase='discard'; if(i===0){ st.msg+=' Now discard.'; return render(); } render(); setTimeout(()=>aiDiscard(i),500); }
  function win(i,from){ const conc=from===null?st.hands[i]:st.hands[i].concat([st.last.c]); if(from!==null){ st.hands[i].push(st.last.c); st.ponds[from].pop(); } const kind=isWin(conc,st.melds[i]); const sc=score(conc,st.melds[i],from===null,kind); const pts=sc.f*8;
   if(from===null){ for(let j=0;j<4;j++) if(j!==i){ st.score[j]-=pts; st.score[i]+=pts; } } else { st.score[from]-=pts*3; st.score[i]+=pts*3; }
   st.phase='over'; st.msg='🀄 MAHJONG! '+N[i]+(i?' wins':' win')+' ('+sc.why.join(', ')+': '+sc.f+' faan, '+(from===null?pts+' from each player':pts*3+' from '+N[from])+').'; st.dealer=i===st.dealer?st.dealer:(st.dealer+1)%4; try{ L.beep(1200,.3); }catch(_){ } render(); }
  function offer(){ st.phase='offer'; st.msg=N[st.last.from]+' discarded '+NAME(st.last.c)+'. Claim it?'; render(); }
  function pass(){ const nx=(st.last.from+1)%4; st.claim=null; st.turn=nx; draw(nx); }
  function render(){ const w=W(); info.textContent=N.map((n,i)=>n+' '+st.score[i]).join(' · ')+' · wall '+st.wall.length;
   seats.innerHTML=''; [1,2,3].forEach(i=>{ const r=h('div',{className:'mjSeat'+(st.turn===i&&st.phase!=='over'?' act':'')}); r.appendChild(h('span',{className:'nm'},N[i]+' · '+st.hands[i].length)); st.melds[i].forEach(m=>m.t.forEach(c=>r.appendChild(tileEl(c,w*.6)))); if(st.phase==='over') st.hands[i].forEach(c=>r.appendChild(tileEl(c,w*.6))); seats.appendChild(r); });
   pond.innerHTML=''; st.ponds.forEach((p,i)=>p.forEach((c,j)=>{ const e=tileEl(c,w*.62); if(st.last&&st.last.from===i&&j===p.length-1&&st.phase!=='over') e.classList.add('hint'); pond.appendChild(e); }));
   mineM.innerHTML=''; st.melds[0].forEach(m=>{ m.t.forEach(c=>mineM.appendChild(tileEl(c,w*.8))); mineM.appendChild(h('span',{style:'width:6px'})); });
   mine.innerHTML=''; st.hands[0].forEach((c,idx)=>{ const e=tileEl(c,w,{cls:(st.sel===idx?'sel ':'')+(st.drawn===c&&idx===st.hands[0].lastIndexOf(c)&&st.turn===0&&st.phase==='discard'?'hint':'')}); e.addEventListener('click',()=>{ if(st.turn!==0||st.phase!=='discard') return; st.sel=st.sel===idx?null:idx; render(); }); e.addEventListener('dblclick',()=>{ if(st.turn===0&&st.phase==='discard'){ st.sel=null; discard(0,c); } }); mine.appendChild(e); });
   btns.innerHTML=''; const B=(l,f,c)=>{ const b=h('button',{type:'button',className:c||''},l); b.addEventListener('click',f); btns.appendChild(b); };
   if(st.phase==='discard'&&st.turn===0){ if(isWin(st.hands[0],st.melds[0])) B('🀄 Mahjong!',()=>win(0,null),'go'); B('⬇ Discard',()=>{ if(st.sel===null) return ctx.status('Tap a tile first.'); const c=st.hands[0][st.sel]; st.sel=null; discard(0,c); },st.sel!==null?'go':''); }
   if(st.phase==='offer'&&st.claim){ const c=st.claim.c; if(st.claim.win) B('🀄 Mahjong!',()=>win(0,st.last.from),'go'); if(st.claim.kong) B('Kong (4 × '+NAME(c)+')',()=>meld(0,'kong',c),'go'); if(st.claim.pung) B('Pung (3 × '+NAME(c)+')',()=>meld(0,'pung',c),'go'); (st.claim.chow||[]).forEach(p=>B('Chow '+srt(p.concat([c])).map(x=>x[1]).join('-'),()=>meld(0,'chow',c,p),'go')); B('Pass',pass); }
   if(st.phase==='over'||st.phase==='idle') B('🀄 Deal a new hand',newHand,'go');
   ctx.status(st.msg); }
  render(); newHand(); window.__kgst=()=>st; return {state:()=>st};
 });
})();
