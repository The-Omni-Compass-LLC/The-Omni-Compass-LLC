(()=>{ /* 🂡 MORE CARD GAMES, part 1 (v221): Gin Rummy, Old Maid, Slapjack, Egyptian Ratscrew, Cheat, President and Speed, each by
   its traditional public-domain rules, against computer players. Phone first: big buttons, tap a card, tap where it goes. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h, SU=L.SU, VS=L.VS||'', rl=L.rl, cname=L.cname, cardEl=L.cardEl, shuffle=L.shuffle; const CAT='Cards';
 const css=document.createElement('style'); css.textContent=`
#gamesDock .kcBar{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}
#gamesDock .kcBar button{min-height:46px;border-radius:12px;padding:4px 14px!important;font:800 14px system-ui,sans-serif}
#gamesDock .kcBar button.go{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important}
#gamesDock .kcBar button:disabled{opacity:.45}
#gamesDock .kcBig{font-size:22px!important;min-height:70px!important;min-width:170px;border-radius:999px!important;background:linear-gradient(180deg,#ff5a6e,#b3172f)!important;color:#fff!important;border:3px solid #fff!important}
#gamesDock .kcMid{display:flex;gap:12px;justify-content:center;align-items:center;flex-wrap:wrap;margin:10px 0;min-height:60px}
#gamesDock .kcPile{display:inline-flex;flex-direction:column;align-items:center;gap:3px;color:#fff;font:700 12px system-ui,sans-serif;border-radius:10px;padding:3px;cursor:pointer}
#gamesDock .kcPile.can{outline:3px solid #2fd27a;box-shadow:0 0 12px #2fd27a}
#gamesDock .kcMeld{display:inline-flex;gap:2px;padding:3px;margin:2px;border-radius:8px;background:rgba(111,232,255,.16)}
#gamesDock .kcDead{display:inline-flex;gap:2px;padding:3px;margin:2px;border-radius:8px;background:rgba(255,90,110,.16)}
#gamesDock .kcBig.hot{animation:kcHot .3s ease-in-out 2}@keyframes kcHot{50%{transform:scale(1.08)}}
#gamesDock .felt .cards .gcard{position:relative}`; document.head.appendChild(css);
 const NM=['You','Nova','Orion','Vega'];
 const sortH=a=>a.sort((x,y)=>x.s-y.s||x.r-y.r);
 const bar=ctx=>{ const b=h('div',{className:'kcBar'}); ctx.area.appendChild(b); return b; };
 const btn=(b,l,f,c)=>{ const e=h('button',{type:'button',className:c||''},l); e.addEventListener('click',f); b.appendChild(e); return e; };
 const seat=(name,info,turn,els,cls)=>{ const s=h('div',{className:'seat'+(turn?' turn':'')+(cls?' '+cls:'')}); s.appendChild(h('div',{className:'nm'},name)); if(info) s.appendChild(h('div',{className:'ch'},info)); if(els&&els.length){ const cs=h('div',{className:'cards'}); els.forEach(e=>cs.appendChild(e)); s.appendChild(cs); } return s; };
 const backs=(n,w)=>Array.from({length:Math.min(n,7)},()=>cardEl({r:2,s:0},w,true));
 const cw=(ctx,n,max)=>Math.max(30,Math.min(max||62,Math.floor((ctx.W()-12)/n)-4));
 const T=(ctx,ms,fn)=>ctx.after(ms,fn);
 /* ───────── GIN RUMMY ───────── */
 const gv=c=>Math.min(10,c.r);
 function melds(hand){ const cand=[]; const byR={}; hand.forEach((c,i)=>(byR[c.r]=byR[c.r]||[]).push(i));
  Object.values(byR).forEach(ix=>{ if(ix.length===3) cand.push(ix.slice()); if(ix.length===4){ cand.push(ix.slice()); for(let k=0;k<4;k++) cand.push(ix.filter((_,j)=>j!==k)); } });
  for(let s=0;s<4;s++){ const ix=hand.map((c,i)=>[c,i]).filter(x=>x[0].s===s).sort((a,b)=>a[0].r-b[0].r); for(let a=0;a<ix.length;a++){ const run=[ix[a][1]]; for(let b=a+1;b<ix.length&&ix[b][0].r===ix[b-1][0].r+1;b++){ run.push(ix[b][1]); if(run.length>=3) cand.push(run.slice()); } } }
  const val=hand.map(gv), total=val.reduce((a,b)=>a+b,0), cm=cand.map(ix=>ix.reduce((m,i)=>m|(1<<i),0)), cv=cand.map(ix=>ix.reduce((a,i)=>a+val[i],0)); let best={dw:total,used:[]};
  (function rec(st,mask,used,mv){ if(total-mv<best.dw) best={dw:total-mv,used:used.slice()}; for(let k=st;k<cm.length;k++){ if(cm[k]&mask) continue; used.push(k); rec(k+1,mask|cm[k],used,mv+cv[k]); used.pop(); } })(0,0,[],0);
  const u=new Set(); const ms=best.used.map(k=>cand[k].map(i=>{ u.add(i); return hand[i]; }).sort((a,b)=>a.r-b.r)); return {dw:best.dw,melds:ms,dead:hand.filter((_,i)=>!u.has(i))}; }
 function layoff(ms,dead){ ms=ms.map(m=>m.slice()); const rem=dead.slice(); let ch=true; while(ch){ ch=false; for(const c of rem.slice()){ for(const m of ms){ const set=m.every(x=>x.r===m[0].r); let ok=false; if(set) ok=c.r===m[0].r&&m.length<4; else if(c.s===m[0].s){ const lo=Math.min(...m.map(x=>x.r)), hi=Math.max(...m.map(x=>x.r)); ok=c.r===lo-1||c.r===hi+1; } if(ok){ m.push(c); rem.splice(rem.indexOf(c),1); ch=true; break; } } } } return rem; }
 G.reg('gin','Gin Rummy',CAT,'Two players, ten cards each. Make melds: three or four of a kind, or runs of three or more in one suit (ace is low). On your turn take the top discard or the top of the stock, then discard one card. When the cards left out of your melds (your deadwood) add up to 10 or less you may Knock; with no deadwood at all it is Gin. Face cards count 10, aces 1. The other player lays off cards onto your melds; the lower deadwood scores the difference, a defender who ties or beats the knocker scores 25 more (an undercut), and Gin scores 25 plus the other hand. First to 100.',ctx=>{
  const st={hand:[[],[]],stock:[],pile:[],turn:0,phase:'draw',took:null,sel:null,score:[0,0],msg:'',over:false,reveal:null};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx);
  function deal(){ const d=shuffle(L.mkDeck(true)); st.hand=[d.splice(0,10),d.splice(0,10)]; st.pile=[d.pop()]; st.stock=d; st.turn=0; st.phase='draw'; st.took=null; st.sel=null; st.over=false; st.reveal=null; st.msg='Your turn: take the top discard or a card from the stock.'; render(); }
  function draw(i,fromPile){ const c=fromPile?st.pile.pop():st.stock.pop(); st.hand[i].push(c); st.took=fromPile?c:null; return c; }
  function voidHand(){ st.over=true; st.phase='over'; st.msg='The stock is down to two cards: the hand is void, no one scores.'; render(); }
  function settle(k,gin){ const o=1-k; const km=melds(st.hand[k]); const dm=melds(st.hand[o]); let ddead=gin?dm.dead:layoff(km.melds,dm.dead); const kd=km.dw, dd=ddead.reduce((a,c)=>a+gv(c),0); let pts, who, why;
   if(gin){ who=k; pts=25+dd; why='Gin! 25 + '+dd; } else if(dd<=kd){ who=o; pts=25+(kd-dd); why='Undercut! 25 + '+(kd-dd); } else { who=k; pts=dd-kd; why='Knock: '+dd+' − '+kd; }
   st.score[who]+=pts; st.over=true; st.phase='over'; st.reveal={km,dm}; st.msg=why+' = '+pts+' to '+NM[who]+'. '+(st.score[who]>=100?NM[who]+(who?' wins':' win')+' the game!':''); render(); }
  function discard(i,c,knock){ const hd=st.hand[i]; hd.splice(hd.indexOf(c),1); st.pile.push(c); st.took=null; st.sel=null; try{ L.beep(440,.04); }catch(_){ }
   if(knock){ return settle(i,melds(hd).dw===0); } st.turn=1-i; if(st.stock.length<=2) return voidHand(); if(st.turn===1){ st.phase='ai'; st.msg=NM[i]+' discarded '+cname(c)+'.'; render(); T(ctx,800,ai); } else { st.phase='draw'; st.msg='Nova discarded '+cname(c)+'. Your turn: take it or draw from the stock.'; render(); } }
  function ai(){ const hd=st.hand[1], top=st.pile[st.pile.length-1], cur=melds(hd).dw; let bestW=1e9; hd.forEach(x=>{ const t=hd.filter(y=>y!==x).concat([top]); bestW=Math.min(bestW,melds(t).dw); });
   const take=top&&bestW<cur-(ctx.diff?0:2); draw(1,take); let best=null, bd=1e9; hd.forEach(x=>{ if(x===st.took) return; const d=melds(hd.filter(y=>y!==x)).dw-gv(x)*.01; if(d<bd){ bd=d; best=x; } });
   const left=melds(hd.filter(y=>y!==best)).dw; const at=ctx.diff===0?10:ctx.diff===1?(st.stock.length<18?10:7):(st.stock.length<14?10:left===0?0:4); const knock=left<=at;
   st.msg='Nova '+(take?'took '+cname(top):'drew from the stock')+(knock?' and knocks!':'.'); discard(1,best,knock); }
  function render(){ const w=cw(ctx,11,58); root.innerHTML='';
   const oppEls=st.reveal?[]:backs(st.hand[1].length,Math.round(w*.55)); const os=seat('Nova · '+st.score[1],st.reveal?'':'10 cards',st.turn===1&&!st.over,oppEls); if(st.reveal){ const m=st.reveal.dm; m.melds.forEach(x=>{ const g=h('span',{className:'kcMeld'}); x.forEach(c=>g.appendChild(cardEl(c,Math.round(w*.62)))); os.appendChild(g); }); const g=h('span',{className:'kcDead'}); m.dead.forEach(c=>g.appendChild(cardEl(c,Math.round(w*.62)))); if(m.dead.length) os.appendChild(g); } root.appendChild(h('div',{className:'grow'},[os]));
   const mid=h('div',{className:'kcMid'}); const canDraw=st.turn===0&&st.phase==='draw'&&!st.over;
   const sp=h('div',{className:'kcPile'+(canDraw?' can':''),role:'button','aria-label':'Stock'},[st.stock.length?cardEl({r:2,s:0},w,true):h('div',{className:'gslot',style:'width:'+w+'px;height:'+Math.round(w*1.4)+'px'}),'Stock '+st.stock.length]); sp.addEventListener('click',()=>{ if(canDraw){ const c=draw(0,false); st.phase='discard'; st.msg='You drew '+cname(c)+'. Tap a card, then Discard or Knock.'; render(); } }); mid.appendChild(sp);
   const top=st.pile[st.pile.length-1]; const dp=h('div',{className:'kcPile'+(canDraw&&top?' can':''),role:'button','aria-label':'Discard pile'},[top?cardEl(top,w):h('div',{className:'gslot',style:'width:'+w+'px;height:'+Math.round(w*1.4)+'px'}),'Discard']); dp.addEventListener('click',()=>{ if(canDraw&&top){ draw(0,true); st.phase='discard'; st.msg='You took '+cname(top)+'. Now discard a different card.'; render(); } }); mid.appendChild(dp); root.appendChild(mid);
   root.appendChild(h('div',{className:'glog'},st.msg));
   const me=st.hand[0]; const m=melds(me); const mine=h('div',{className:'seat'+(st.turn===0&&!st.over?' turn':''),style:'max-width:none'}); mine.appendChild(h('div',{className:'nm'},'You · '+st.score[0]+' · deadwood '+m.dw));
   const cs=h('div',{className:'cards'}); const tap=c=>{ if(st.phase!=='discard'||st.turn!==0) return; st.sel=st.sel===c?null:c; render(); };
   m.melds.forEach(x=>{ const g=h('span',{className:'kcMeld'}); x.forEach(c=>{ const e=cardEl(c,w,false,st.sel===c?'sel lift':''); e.addEventListener('click',()=>tap(c)); g.appendChild(e); }); cs.appendChild(g); });
   const dg=h('span',{className:'kcDead'}); sortH(m.dead.slice()).forEach(c=>{ const e=cardEl(c,w,false,st.sel===c?'sel lift':''); e.addEventListener('click',()=>tap(c)); dg.appendChild(e); }); if(m.dead.length) cs.appendChild(dg); mine.appendChild(cs); root.appendChild(mine);
   B.innerHTML=''; if(st.over){ btn(B,st.score.some(s=>s>=100)?'🂡 New game':'▶ Next hand',()=>{ if(st.score.some(s=>s>=100)) st.score=[0,0]; deal(); },'go'); }
   else if(st.phase==='discard'){ const ok=st.sel&&st.sel!==st.took; const left=st.sel?melds(me.filter(x=>x!==st.sel)).dw:99; btn(B,'⬇ Discard',()=>{ if(ok) discard(0,st.sel,false); else ctx.status(st.sel?'You cannot throw back the card you just took.':'Tap a card first.'); },ok?'go':'');
    const kb=btn(B,left===0?'🏆 Gin!':'✊ Knock ('+(st.sel?left:'?')+')',()=>{ if(ok&&left<=10) discard(0,st.sel,true); },ok&&left<=10?'go':''); kb.disabled=!(ok&&left<=10); }
   ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
 /* ───────── OLD MAID ───────── */
 G.reg('oldmaid','Old Maid',CAT,'One queen is taken out, so one queen (the Old Maid) can never be paired. Pairs of the same rank are put down at once. On your turn take one face-down card from the player on your left; if it pairs, put the pair down. Players who run out of cards are safe. Whoever is left holding the Old Maid loses.',ctx=>{
  const st={hand:[[],[],[],[]],turn:0,over:false,msg:'',out:[],safe:[]};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx);
  function pairs(i){ const by={}; st.hand[i].forEach(c=>(by[c.r]=by[c.r]||[]).push(c)); let n=0; Object.values(by).forEach(a=>{ while(a.length>=2){ const x=a.pop(), y=a.pop(); st.hand[i]=st.hand[i].filter(c=>c!==x&&c!==y); n++; } }); return n; }
  const alive=i=>st.hand[i].length>0; const nextAlive=i=>{ for(let k=1;k<=4;k++){ const j=(i+k)%4; if(alive(j)) return j; } return -1; };
  function deal(){ const d=shuffle(L.mkDeck(false).filter(c=>!(c.r===12&&c.s===3))); st.hand=[[],[],[],[]]; d.forEach((c,k)=>st.hand[k%4].push(c)); [0,1,2,3].forEach(pairs); st.turn=0; st.over=false; st.safe=[]; st.msg='Pairs are down. Your turn: take a card from '+NM[nextAlive(0)]+'.'; check(); render(); }
  function check(){ const al=[0,1,2,3].filter(alive); [0,1,2,3].forEach(i=>{ if(!alive(i)&&!st.safe.includes(i)) st.safe.push(i); }); if(al.length===1){ st.over=true; st.msg=(al[0]===0?'You are':NM[al[0]]+' is')+' left with the Old Maid! '+(al[0]===0?'You lose this one.':'You are safe.'); return true; } return false; }
  function take(i,j,idx){ const c=st.hand[j].splice(idx,1)[0]; st.hand[i].push(c); const n=pairs(i); st.msg=(i?NM[i]+' takes':'You take')+' a card from '+(j?NM[j]:'you')+(i===0?' ('+cname(c)+')':'')+(n?' and '+(i?'puts':'put')+' down a pair.':'.'); if(check()) return render(); st.turn=nextAlive(i); render(); if(st.turn!==0) T(ctx,750,()=>ai(st.turn)); else st.msg+=' Your turn: take a card from '+NM[nextAlive(0)]+'.'; render(); }
  function ai(i){ if(st.over) return; const j=nextAlive(i); take(i,j,Math.floor(Math.random()*st.hand[j].length)); }
  function render(){ const w=cw(ctx,10,56); root.innerHTML=''; const top=h('div',{className:'grow'}); const src=st.turn===0&&!st.over?nextAlive(0):-1;
   for(let i=1;i<4;i++){ const els=st.hand[i].map((c,idx)=>{ const e=cardEl(c,Math.round(w*.6),!st.over,src===i?'play':''); if(src===i){ e.style.cursor='pointer'; e.addEventListener('click',()=>take(0,i,idx)); } return e; }); top.appendChild(seat(NM[i],alive(i)?st.hand[i].length+' cards':'safe ✓',st.turn===i&&!st.over,els,alive(i)?'':'win')); }
   root.appendChild(top); root.appendChild(h('div',{className:'glog'},st.msg)); const me=h('div',{className:'seat'+(st.turn===0&&!st.over?' turn':''),style:'max-width:none'}); me.appendChild(h('div',{className:'nm'},alive(0)?'Your hand':'You are safe ✓')); const cs=h('div',{className:'cards'}); sortH(st.hand[0].slice()).forEach(c=>cs.appendChild(cardEl(c,w,false,c.r===12?'kc':''))); me.appendChild(cs); root.appendChild(me);
   B.innerHTML=''; btn(B,'🔀 Shuffle my hand',()=>{ st.hand[0]=shuffle(st.hand[0]); render(); }); if(st.over) btn(B,'🃏 Deal again',deal,'go'); ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
 /* ───────── SLAPJACK and EGYPTIAN RATSCREW ───────── */
 function slapGame(rat){ return ctx=>{
  const st={p:[[],[],[]],center:[],turn:0,chal:null,seq:0,over:false,msg:'',flips:0,burn:[]};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx);
  const alive=i=>st.p[i].length>0; const nxt=i=>{ for(let k=1;k<=3;k++){ const j=(i+k)%3; if(alive(j)) return j; } return i; };
  function slappable(){ const c=st.center, n=c.length; if(!n) return false; if(!rat) return c[n-1].r===11; if(n>=2&&c[n-1].r===c[n-2].r) return 'a double'; if(n>=3&&c[n-1].r===c[n-3].r) return 'a sandwich'; return false; }
  function deal(){ const d=shuffle(L.mkDeck(false)); st.p=[[],[],[]]; d.forEach((c,k)=>st.p[k%3].push(c)); st.center=[]; st.burn=[]; st.turn=0; st.chal=null; st.over=false; st.flips=0; st.msg='Your flip first. '+(rat?'Slap a double or a sandwich; face cards set a challenge.':'Slap every jack!'); render(); }
  function win(i,why){ st.p[i]=st.center.concat(st.burn,st.p[i]); st.center=[]; st.burn=[]; st.chal=null; st.seq++; st.turn=i; st.msg=(i?NM[i]+' takes':'You take')+' the pile'+(why?' ('+why+')':'')+'!'; try{ L.beep(i?300:880,.08); }catch(_){ } end(); }
  function end(){ const al=[0,1,2].filter(alive); if(al.length===1&&!st.center.length){ st.over=true; st.msg+=' '+(al[0]===0?'You win with all 52 cards!':NM[al[0]]+' has every card.'); }
   if(st.flips>700){ st.over=true; let b=0; [0,1,2].forEach(i=>{ if(st.p[i].length>st.p[b].length) b=i; }); st.msg='Time! '+(b?NM[b]+' wins':'You win')+' with the most cards ('+st.p[b].length+').'; }
   render(); if(!st.over) sched(); }
  function slap(i){ if(st.over) return; const ok=slappable(); if(ok){ win(i,ok===true?'a jack':ok); return; } if(!alive(i)){ if(i===0){ st.msg='No cards: wait for a good slap to get back in.'; render(); } return; } const c=st.p[i].pop(); st.burn.unshift(c); st.msg=(i?NM[i]+' slaps':'You slap')+' wrong and '+(i?'burns':'burn')+' a card.'; if(i===0) try{ L.beep(160,.1); }catch(_){ } render(); sched(); }
  function flip(i){ if(st.over||st.turn!==i||!alive(i)) return; const c=st.p[i].pop(); st.center.push(c); st.flips++; st.seq++; try{ L.beep(520+i*60,.03); }catch(_){ } const s=st.seq; st.msg=(i?NM[i]+' flips ':'You flip ')+cname(c)+'.';
   if(rat){ const face={11:1,12:2,13:3,14:4}[c.r]; if(face){ st.chal={owner:i,left:face}; st.turn=nxt(i); st.msg+=' '+(st.turn?NM[st.turn]+' has':'You have')+' '+face+' '+(face>1?'tries':'try')+' to play a face card or an ace.'; }
    else if(st.chal){ st.chal.left--; if(st.chal.left<=0||!alive(i)){ const ow=st.chal.owner; st.msg+=' '+(ow?NM[ow]:'You')+' will take it…'; st.turn=-1; render(); aiSlaps(s); T(ctx,1300,()=>{ if(st.seq===s) win(ow,'the challenge'); }); return; } }
    else st.turn=nxt(i); }
   else st.turn=nxt(i);
   if(!alive(st.turn)) st.turn=nxt(st.turn); render(); aiSlaps(s); sched(); }
  function aiSlaps(s){ if(!slappable()) { [1,2].forEach(i=>{ if(Math.random()<(ctx.diff===2?.01:.04)) T(ctx,500+Math.random()*900,()=>{ if(st.seq===s) slap(i); }); }); return; } [1,2].forEach(i=>{ const base=ctx.diff===0?900:ctx.diff===1?650:430; T(ctx,base+Math.random()*base*.8,()=>{ if(st.seq===s&&slappable()) slap(i); }); }); }
  function sched(){ if(st.over||st.turn<0) return; if(!alive(st.turn)){ const n=nxt(st.turn); if(n!==st.turn&&alive(n)){ st.turn=n; render(); } } if(st.turn===0||!alive(st.turn)) return; const s=st.seq, t=st.turn; T(ctx,700+Math.random()*300,()=>{ if(st.seq===s&&st.turn===t) flip(t); }); }
  function render(){ const w=cw(ctx,6,74); root.innerHTML=''; const top=h('div',{className:'grow'}); for(let i=1;i<3;i++) top.appendChild(seat(NM[i],st.p[i].length+' cards',st.turn===i&&!st.over,backs(Math.min(3,st.p[i].length),Math.round(w*.45)),alive(i)?'':'out')); root.appendChild(top);
   const mid=h('div',{className:'kcMid'}); const pile=h('div',{style:'position:relative;width:'+(w*1.8)+'px;height:'+(w*1.6)+'px'}); st.center.slice(-4).forEach((c,k,a)=>{ const e=cardEl(c,w); e.style.position='absolute'; e.style.left=(k*w*.25)+'px'; e.style.top=(k%2*4)+'px'; e.style.transform='rotate('+((k-a.length/2)*7)+'deg)'; pile.appendChild(e); }); mid.appendChild(h('div',{className:'kcPile'},[pile,'Pile '+st.center.length+(st.burn.length?' + '+st.burn.length+' burned':'')+(st.chal?' · challenge: '+st.chal.left+' left':'')])); root.appendChild(mid);
   root.appendChild(h('div',{className:'glog'},st.msg)); const mine=h('div',{className:'kcPile'+(st.turn===0&&alive(0)&&!st.over?' can':''),role:'button','aria-label':'Your pile: flip'},[alive(0)?cardEl({r:2,s:0},w,true):h('div',{className:'gslot',style:'width:'+w+'px;height:'+Math.round(w*1.4)+'px'}),'You · '+st.p[0].length+' cards']); mine.addEventListener('click',()=>flip(0)); const sl=h('button',{type:'button',className:'kcBig'+(slappable()?' hot':''),'aria-label':'Slap'},'✋ SLAP!'); sl.addEventListener('click',()=>slap(0)); root.appendChild(h('div',{className:'kcMid'},st.over?[mine]:[mine,sl]));
   B.innerHTML=''; if(st.over) btn(B,'🃏 Deal again',deal,'go'); else { const f=btn(B,'🂠 Flip (F)',()=>flip(0),st.turn===0?'go':''); f.disabled=st.turn!==0||!alive(0); }
   ctx.status(st.msg); }
  ctx.key((e,down)=>{ if(!down) return; const k=(e.key||'').toLowerCase(); if(k===' '||k==='s'){ e.preventDefault&&e.preventDefault(); slap(0); } else if(k==='f'||k==='enter') flip(0); });
  deal(); window.__kgst=()=>st; return {state:()=>st}; }; }
 G.reg('slapjack','Slapjack',CAT,'The deck is dealt out face down. Take turns flipping your top card onto the pile. The moment a jack lands, slap it (the SLAP button, Space or S): the first slap takes the whole pile. Slap anything else and you burn a card. Run out of cards and you are out unless you win the next jack. Win every card.',slapGame(false));
 G.reg('ratscrew','Egyptian Ratscrew',CAT,'Flip in turn onto the pile. Slap a double (two of a rank in a row) or a sandwich (two of a rank with one card between) to take the pile; a wrong slap burns a card. A face card or ace sets a challenge: the next player must play a face card or ace within 1 (jack), 2 (queen), 3 (king) or 4 (ace) tries, or the challenger takes the pile. Win every card. Space or S slaps, F flips.',slapGame(true));
 /* ───────── CHEAT (I DOUBT IT) ───────── */
 G.reg('cheat','Cheat (I Doubt It)',CAT,'All the cards are dealt to four players. Turns go in rank order: aces, then twos, threes and up to kings, then aces again. On your turn put one to four cards face down and say they are the rank called; they do not have to be. Anyone may call Cheat! If the cards were not all that rank the player takes the whole pile; if they were, the caller takes it. First to get rid of every card wins.',ctx=>{
  const st={hand:[[],[],[],[]],pile:[],need:1,turn:0,last:null,phase:'play',sel:[],over:false,msg:''};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx); const RK=r=>({1:'aces',11:'jacks',12:'queens',13:'kings'}[r]||r+'s');
  function deal(){ const d=shuffle(L.mkDeck(true)); st.hand=[[],[],[],[]]; d.forEach((c,k)=>st.hand[k%4].push(c)); st.pile=[]; st.need=1; st.turn=0; st.last=null; st.phase='play'; st.sel=[]; st.over=false; st.msg='Your turn: play 1 to 4 cards as aces.'; render(); }
  function play(i,cards){ cards.forEach(c=>st.hand[i].splice(st.hand[i].indexOf(c),1)); st.pile.push(...cards); st.last={i,cards,rank:st.need}; st.msg=(i?NM[i]+' puts down ':'You put down ')+cards.length+' '+(cards.length>1?RK(st.need):RK(st.need).replace(/s$/,''))+'.'; st.sel=[]; try{ L.beep(420,.04); }catch(_){ }
   if(i!==0){ st.phase='doubt'; render(); return; } render(); T(ctx,700,()=>aiDoubt([1,2,3])); }
  function aiCalls(j){ const L0=st.last; const mine=st.hand[j].filter(c=>c.r===L0.rank).length; if(mine+L0.cards.length>4) return true; let p=[.06,.12,.18][ctx.diff]||.12; if(L0.cards.length>=3) p+=.25; if(st.hand[L0.i].length===0) p+=.5; if(st.hand[L0.i].length<=2) p+=.2; return Math.random()<p; }
  function aiDoubt(order){ for(const j of order){ if(j===st.last.i) continue; if(aiCalls(j)) return resolve(j); } advance(); }
  function resolve(j){ const L0=st.last; const lie=L0.cards.some(c=>c.r!==L0.rank); const taker=lie?L0.i:j; st.hand[taker].push(...st.pile); st.pile=[]; st.msg=(j?NM[j]+' calls':'You call')+' Cheat! The cards were '+L0.cards.map(cname).join(' ')+'. '+(lie?(L0.i?NM[L0.i]+' was':'You were')+' cheating and '+(L0.i?'takes':'take'):(j?NM[j]+' was wrong and takes':'You were wrong and take'))+' the pile.'; try{ L.beep(lie?880:200,.1); }catch(_){ } advance(); }
  function advance(){ const L0=st.last; if(L0&&!st.hand[L0.i].length){ st.over=true; st.msg+=' '+(L0.i?NM[L0.i]+' is out of cards and wins!':'You are out of cards: you win!'); return render(); } st.need=st.need%13+1; st.turn=(st.turn+1)%4; st.phase='play'; if(st.turn===0){ st.msg+=' Your turn: play as '+RK(st.need)+'.'; render(); return; } render(); T(ctx,900,aiPlay); }
  function aiPlay(){ const i=st.turn, hd=st.hand[i]; const real=hd.filter(c=>c.r===st.need); let cards=real.slice(0,4); if(!cards.length||(Math.random()<.2&&cards.length<3&&hd.length>cards.length+1)){ const others=hd.filter(c=>c.r!==st.need).sort((a,b)=>Math.abs(a.r-st.need)>Math.abs(b.r-st.need)?-1:1); cards=cards.concat(others.slice(0,cards.length?1:(Math.random()<.3?2:1))); } play(i,cards.slice(0,4)); }
  function render(){ const w=cw(ctx,13,54); root.innerHTML=''; const top=h('div',{className:'grow'}); for(let i=1;i<4;i++) top.appendChild(seat(NM[i],st.hand[i].length+' cards',st.turn===i&&!st.over,backs(Math.min(4,st.hand[i].length),Math.round(w*.45)))); root.appendChild(top);
   root.appendChild(h('div',{className:'kcMid'},[h('div',{className:'kcPile'},[st.pile.length?cardEl({r:2,s:0},w,true):h('div',{className:'gslot',style:'width:'+w+'px;height:'+Math.round(w*1.4)+'px'}),'Pile '+st.pile.length]),h('div',{style:'color:#ffe94a;font:900 20px system-ui'},'Now: '+RK(st.need))]));
   root.appendChild(h('div',{className:'glog'},st.msg)); const me=h('div',{className:'seat'+(st.turn===0&&!st.over?' turn':''),style:'max-width:none'}); me.appendChild(h('div',{className:'nm'},'Your hand · '+st.hand[0].length)); const cs=h('div',{className:'cards'});
   st.hand[0].slice().sort((a,b)=>a.r-b.r||a.s-b.s).forEach(c=>{ const on=st.sel.includes(c); const e=cardEl(c,w,false,(on?'sel lift':'')+(c.r===st.need?' play':'')); e.addEventListener('click',()=>{ if(st.turn!==0||st.phase!=='play'||st.over) return; if(on) st.sel=st.sel.filter(x=>x!==c); else if(st.sel.length<4) st.sel.push(c); render(); }); cs.appendChild(e); }); me.appendChild(cs); root.appendChild(me);
   B.innerHTML=''; if(st.over) btn(B,'🃏 Deal again',deal,'go'); else if(st.phase==='doubt'){ btn(B,'🚨 Cheat!',()=>resolve(0),'go'); btn(B,'👍 Let it go',()=>{ st.phase='wait'; render(); T(ctx,500,()=>aiDoubt([1,2,3].filter(j=>j!==st.last.i))); }); }
   else if(st.turn===0){ const b=btn(B,'Play '+st.sel.length+' as '+RK(st.need),()=>{ if(st.sel.length) play(0,st.sel.slice()); },st.sel.length?'go':''); b.disabled=!st.sel.length; }
   ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
 /* ───────── PRESIDENT ───────── */
 G.reg('president','President',CAT,'Four players, all the cards dealt. Threes are lowest, then up to kings, aces, and twos are highest. The holder of the 3♣ leads one card, a pair, three or four of one rank. Each player must beat it with the same number of cards of a higher rank, or pass. When everyone passes, the last player to play leads again. First out is President, then Vice President, Vice Scum, and last is the Scum. Next hand the Scum hands the President their two best cards and gets two back (one each between the Vice President and Vice Scum).',ctx=>{
  const TI=['President','Vice President','Vice Scum','Scum'];
  const st={hand:[[],[],[],[]],cur:null,last:-1,passed:new Set(),turn:0,done:[],sel:[],over:false,msg:'',pts:[0,0,0,0],prev:null,round:0};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx); const V=c=>c.r===2?15:c.r;
  const active=()=>[0,1,2,3].filter(i=>!st.done.includes(i));
  function deal(){ const d=shuffle(L.mkDeck(false)); st.hand=[[],[],[],[]]; d.forEach((c,k)=>st.hand[k%4].push(c)); st.round++; let note='';
   if(st.prev){ const [P,VP,VS2,S]=st.prev; const give=(a,b,n,best)=>{ const s=st.hand[a].slice().sort((x,y)=>V(x)-V(y)); const g=best?s.slice(-n):s.slice(0,n); g.forEach(c=>{ st.hand[a].splice(st.hand[a].indexOf(c),1); st.hand[b].push(c); }); return g; };
    const g1=give(S,P,2,true), g2=give(P,S,2,false), g3=give(VS2,VP,1,true), g4=give(VP,VS2,1,false); note=' Cards traded: '+NM[S]+' → '+NM[P]+' '+g1.map(cname).join(' ')+'; '+NM[P]+' → '+NM[S]+' '+g2.map(cname).join(' ')+'; '+NM[VS2]+' → '+NM[VP]+' '+g3.map(cname).join(' ')+'; '+NM[VP]+' → '+NM[VS2]+' '+g4.map(cname).join(' ')+'.'; }
   st.done=[]; st.cur=null; st.last=-1; st.passed=new Set(); st.sel=[]; st.over=false; st.turn=st.prev?st.prev[3]:st.hand.findIndex(hd=>hd.some(c=>c.r===3&&c.s===3)); st.msg=(st.turn?NM[st.turn]+' leads.':'You lead.')+note; render(); if(st.turn) T(ctx,900,ai); }
  function valid(cards){ if(!cards.length||!cards.every(c=>c.r===cards[0].r)) return false; if(!st.cur) return true; return cards.length===st.cur.n&&V(cards[0])>st.cur.v; }
  function play(i,cards){ cards.forEach(c=>st.hand[i].splice(st.hand[i].indexOf(c),1)); st.cur={n:cards.length,v:V(cards[0]),cards}; st.last=i; st.passed=new Set(); st.sel=[]; st.msg=(i?NM[i]+' plays ':'You play ')+cards.map(cname).join(' ')+'.'; try{ L.beep(400+V(cards[0])*20,.04); }catch(_){ }
   if(!st.hand[i].length){ st.done.push(i); st.msg+=' '+(i?NM[i]+' is out':'You are out')+': '+TI[st.done.length-1]+'!'; if(st.done.length===3){ const l=active()[0]; st.done.push(l); st.done.forEach((p,k)=>st.pts[p]+=3-k); st.prev=st.done.slice(); st.over=true; st.msg+=' '+(l?NM[l]+' is':'You are')+' the Scum.'; return render(); } } step(); }
  function pass(i){ st.passed.add(i); st.msg=(i?NM[i]+' passes.':'You pass.'); step(); }
  function step(){ const others=active().filter(j=>j!==st.last); if(st.cur&&others.every(j=>st.passed.has(j))){ let lead=st.last; if(st.done.includes(lead)){ lead=nextFrom(lead); } st.cur=null; st.passed=new Set(); st.turn=lead; st.msg+=' Everyone passed: '+(lead?NM[lead]+' leads.':'you lead.'); }
   else st.turn=nextFrom(st.turn); render(); if(st.turn!==0&&!st.over) T(ctx,800,ai); }
  function nextFrom(i){ for(let k=1;k<=4;k++){ const j=(i+k)%4; if(!st.done.includes(j)) return j; } return i; }
  function groups(hd){ const by={}; hd.forEach(c=>(by[V(c)]=by[V(c)]||[]).push(c)); return Object.keys(by).map(Number).sort((a,b)=>a-b).map(v=>by[v]); }
  function ai(){ const i=st.turn; if(st.over||i===0) return; const gs=groups(st.hand[i]); if(!st.cur){ const g=gs.find(x=>V(x[0])<15)||gs[0]; return play(i,g); } const opt=gs.filter(g=>g.length>=st.cur.n&&V(g[0])>st.cur.v); const pick=opt.find(g=>g.length===st.cur.n)||opt[0]; if(pick&&!(ctx.diff===2&&V(pick[0])>=14&&st.hand[i].length>6&&Math.random()<.6)) return play(i,pick.slice(0,st.cur.n)); pass(i); }
  function render(){ const w=cw(ctx,13,54); root.innerHTML=''; const top=h('div',{className:'grow'}); for(let i=1;i<4;i++){ const k=st.done.indexOf(i); top.appendChild(seat(NM[i]+' · '+st.pts[i],k>=0?TI[k]:st.hand[i].length+' cards'+(st.passed.has(i)?' · pass':''),st.turn===i&&!st.over,backs(Math.min(4,st.hand[i].length),Math.round(w*.45)),k>=0?'win':'')); } root.appendChild(top);
   const mid=h('div',{className:'kcMid'}); if(st.cur) st.cur.cards.forEach(c=>mid.appendChild(cardEl(c,w))); else mid.appendChild(h('div',{style:'color:#ffe94a;font:800 16px system-ui'},'Lead anything')); root.appendChild(mid);
   root.appendChild(h('div',{className:'glog'},st.msg)); const k0=st.done.indexOf(0); const me=h('div',{className:'seat'+(st.turn===0&&!st.over?' turn':''),style:'max-width:none'}); me.appendChild(h('div',{className:'nm'},'You · '+st.pts[0]+(k0>=0?' · '+TI[k0]:''))); const cs=h('div',{className:'cards'});
   st.hand[0].slice().sort((a,b)=>V(a)-V(b)||a.s-b.s).forEach(c=>{ const on=st.sel.includes(c); const e=cardEl(c,w,false,on?'sel lift':''); e.addEventListener('click',()=>{ if(st.turn!==0||st.over) return; if(on) st.sel=st.sel.filter(x=>x!==c); else { st.sel=st.sel.filter(x=>x.r===c.r); st.sel.push(c); } render(); }); cs.appendChild(e); }); me.appendChild(cs); root.appendChild(me);
   B.innerHTML=''; if(st.over) btn(B,'🃏 Next hand',deal,'go'); else if(st.turn===0){ const ok=valid(st.sel); const b=btn(B,'▶ Play'+(st.sel.length?' '+st.sel.length:''),()=>{ if(valid(st.sel)) play(0,st.sel.slice()); },ok?'go':''); b.disabled=!ok; if(st.cur) btn(B,'Pass',()=>{ st.sel=[]; pass(0); }); }
   ctx.status(st.msg+(st.turn===0&&!st.over&&st.cur?' Beat '+st.cur.n+' × '+rl(st.cur.v===15?2:st.cur.v)+'.':'')); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
 /* ───────── SPEED ───────── */
 G.reg('speed','Speed',CAT,'A race, no turns. You and Nova each have five cards in hand and a draw pile. Play any card that is one rank above or below either middle pile (kings and aces wrap around): tap the card, and if it fits both piles tap the pile you want. Your hand refills from your draw pile. When neither of you can play, a card from each side pile is turned onto the middle. First to play out every card wins. Difficulty sets Nova’s speed.',ctx=>{
  const st={draw:[[],[]],hand:[[],[]],side:[[],[]],mid:[[],[]],sel:null,over:false,msg:'',stuckAt:0,next:0};
  const root=h('div',{className:'felt'}); ctx.area.appendChild(root); const B=bar(ctx); const rk=c=>c.r%13; const fits=(c,p)=>{ const t=p[p.length-1]; if(!t) return false; const d=Math.abs(rk(c)-rk(t)); return d===1||d===12; };
  const refill=i=>{ while(st.hand[i].length<5&&st.draw[i].length) st.hand[i].push(st.draw[i].pop()); };
  const movesOf=i=>{ const M=[]; st.hand[i].forEach(c=>[0,1].forEach(k=>{ if(fits(c,st.mid[k])) M.push([c,k]); })); return M; };
  function deal(){ const d=shuffle(L.mkDeck(false)); st.draw=[d.splice(0,15),d.splice(0,15)]; st.hand=[d.splice(0,5),d.splice(0,5)]; st.side=[d.splice(0,6),d.splice(0,5)]; st.mid=[[st.side[0].pop()],[d.pop()]]; st.side[1].push(...d); st.sel=null; st.over=false; st.stuckAt=0; st.next=performance.now()+1500; st.msg='Go! Play one up or one down.'; render(); }
  function put(i,c,k){ if(st.over) return; st.hand[i].splice(st.hand[i].indexOf(c),1); st.mid[k].push(c); refill(i); st.stuckAt=0; try{ L.beep(i?340:720,.03); }catch(_){ } if(!st.hand[i].length&&!st.draw[i].length){ st.over=true; st.msg=i?'Nova played out first: Nova wins!':'You played out first: you win!'; } render(); }
  function flipSides(){ for(let k=0;k<2;k++){ if(!st.side[k].length){ const pool=[]; st.mid.forEach(p=>pool.push(...p.splice(0,p.length-1))); st.side=[shuffle(pool.slice(0,Math.ceil(pool.length/2))),shuffle(pool.slice(Math.ceil(pool.length/2)))]; break; } } for(let k=0;k<2;k++) if(st.side[k].length) st.mid[k].push(st.side[k].pop()); st.stuckAt=0; st.msg='Nobody could play: new middle cards.'; render(); }
  ctx.every(120,()=>{ if(st.over) return; const now=performance.now(); const sp=[1700,1150,720][ctx.diff]||1150; if(now>=st.next){ const M=movesOf(1); if(M.length){ const [c,k]=M[Math.floor(Math.random()*M.length)]; put(1,c,k); } st.next=now+sp*(.7+Math.random()*.6); }
   if(!movesOf(0).length&&!movesOf(1).length){ if(!st.stuckAt) { st.stuckAt=now; render(); } else if(now-st.stuckAt>1400) flipSides(); } });
  function render(){ const w=cw(ctx,6,76); root.innerHTML=''; root.appendChild(h('div',{className:'grow'},[seat('Nova',st.hand[1].length+' in hand · '+st.draw[1].length+' to draw',false,backs(st.hand[1].length,Math.round(w*.5)))]));
   const mid=h('div',{className:'kcMid'}); mid.appendChild(h('div',{className:'kcPile'},[st.side[0].length?cardEl({r:2,s:0},Math.round(w*.6),true):'',String(st.side[0].length)]));
   [0,1].forEach(k=>{ const p=st.mid[k], t=p[p.length-1]; const can=st.sel&&fits(st.sel,p); const e=h('div',{className:'kcPile'+(can?' can':''),role:'button','aria-label':'Middle pile '+(k+1)},[t?cardEl(t,w):'','Pile '+(k+1)]); e.addEventListener('click',()=>{ if(st.sel&&fits(st.sel,p)){ const c=st.sel; st.sel=null; put(0,c,k); } }); mid.appendChild(e); });
   mid.appendChild(h('div',{className:'kcPile'},[st.side[1].length?cardEl({r:2,s:0},Math.round(w*.6),true):'',String(st.side[1].length)])); root.appendChild(mid);
   root.appendChild(h('div',{className:'glog'},st.msg+(st.stuckAt&&!st.over?' Nobody can play…':''))); const me=h('div',{className:'seat turn',style:'max-width:none'}); me.appendChild(h('div',{className:'nm'},'You · '+st.draw[0].length+' to draw')); const cs=h('div',{className:'cards'});
   st.hand[0].forEach(c=>{ const ok=fits(c,st.mid[0])||fits(c,st.mid[1]); const e=cardEl(c,w,false,(st.sel===c?'sel lift':'')+(ok?' play':' dim')); e.addEventListener('click',()=>{ if(st.over) return; const ks=[0,1].filter(k=>fits(c,st.mid[k])); if(!ks.length){ ctx.status('That card is not one away from either pile.'); return; } if(ks.length===1){ st.sel=null; return put(0,c,ks[0]); } st.sel=c; render(); }); cs.appendChild(e); }); me.appendChild(cs); root.appendChild(me);
   B.innerHTML=''; if(st.over) btn(B,'⚡ Play again',deal,'go'); else if(st.stuckAt) btn(B,'🂠 Turn new middle cards',flipSides,'go'); ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st};
 });
})();
