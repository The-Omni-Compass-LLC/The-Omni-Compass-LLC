(()=>{ /* 🎰 THE REAL TABLES, PART 2 (v217): Blackjack, Texas Hold'em (six seats), Baccarat and Sic Bo, laid out and played by the
   real rules, phone first and scaling up. Play chips only: no money, no prizes. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h, PK=G._t&&G._t.poker; const rn=n=>Math.floor(Math.random()*n);
 const getC=()=>{ try{ const s=localStorage.getItem('kanGamesChips'); if(s===null) return 1000; const v=+s; return isFinite(v)?Math.max(0,v):1000; }catch(_){ return 1000; } };
 const setC=v=>{ v=Math.max(0,Math.round(v)); try{ localStorage.setItem('kanGamesChips',String(v)); }catch(_){ } document.querySelectorAll('#gamesDock .chipsNow').forEach(s=>s.textContent=v); return v; };
 const CH=[[5,'#d62a36','#fff'],[10,'#2a6fd6','#fff'],[25,'#1e9c4a','#fff'],[100,'#111','#fff'],[500,'#7b3fc4','#fff']];
 const css=document.createElement('style'); css.textContent=`
.k2Felt{background:radial-gradient(ellipse at 50% 20%,#1f8a4c,#0b5a2e 70%,#063d1f);border:8px solid #5a3417;border-radius:22px 22px 120px 120px/22px 22px 60px 60px;box-shadow:inset 0 0 40px rgba(0,0,0,.55),0 8px 24px rgba(0,0,0,.6);padding:10px 8px 18px;color:#fff;text-align:center}
.k2Rule{font:700 clamp(10px,1vw,13px) Georgia,serif;color:#ffe9a8;letter-spacing:.08em;text-transform:uppercase;margin:4px 0;opacity:.9}
.k2Row{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;align-items:center;min-height:30px;margin:4px 0}
.k2Lbl{font:800 clamp(12px,1.1vw,16px) system-ui,sans-serif;color:#fff;margin:2px 0}
.k2Lbl b{color:#ffe94a}
.k2Hand{display:inline-flex;flex-direction:column;align-items:center;gap:2px;padding:4px;border-radius:10px;margin:2px}
.k2Hand.cur{box-shadow:0 0 0 3px #ffe94a}
.k2Btns{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}
.k2Btns button{min-height:48px;min-width:64px;border-radius:12px;padding:4px 14px!important;font:900 15px system-ui,sans-serif}
.k2Btns button.go{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important;border:2px solid #fff3b0!important}
.k2Btns button:disabled{opacity:.35}
.k2Chips{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;align-items:center;margin:6px 0}
.k2Chip{width:44px;height:44px;border-radius:50%;border:4px dashed rgba(255,255,255,.85)!important;font:900 12px system-ui,sans-serif!important;padding:0!important;min-height:0!important;box-shadow:0 3px 6px rgba(0,0,0,.5)}
.k2Chip.on{outline:3px solid #ffe94a;outline-offset:2px;transform:translateY(-3px)}
.k2Bank{font:800 15px system-ui,sans-serif;color:#ffe94a;width:100%;text-align:center} .k2Bank small{font:600 11px system-ui,sans-serif;color:#cfc8a0}
.k2Spot{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;min-width:64px;min-height:64px;border:2px solid rgba(255,255,255,.8);border-radius:50%;font:800 12px system-ui,sans-serif;color:#fff;background:rgba(0,0,0,.12);position:relative;padding:4px!important}
.k2Spot b{font:900 15px system-ui,sans-serif;color:#ffe94a}
.k2Grid{display:grid;gap:3px}
.k2Grid button{min-height:42px;border:2px solid rgba(255,255,255,.8)!important;border-radius:6px!important;background:rgba(0,0,0,.12)!important;color:#fff!important;font:800 clamp(11px,1.1vw,15px)/1.15 system-ui,sans-serif!important;padding:3px!important;position:relative}
.k2Grid button small{display:block;font:700 10px system-ui,sans-serif;color:#ffe94a}
.k2Grid button.win{box-shadow:0 0 0 3px #ffe94a,0 0 14px #ffe94a!important}
.k2Stack{position:absolute;right:2px;top:2px;min-width:22px;height:22px;border-radius:50%;font:900 10px/22px system-ui,sans-serif;text-align:center;border:2px dashed rgba(255,255,255,.9);pointer-events:none}
.k2Oval{position:relative;width:100%;aspect-ratio:1.55/1;background:radial-gradient(ellipse at 50% 40%,#1f8a4c,#0b5a2e 70%,#063d1f);border:10px solid #5a3417;border-radius:50%;box-shadow:inset 0 0 40px rgba(0,0,0,.6),0 8px 24px rgba(0,0,0,.6)}
@media (max-width:560px){ .k2Oval{aspect-ratio:.82/1;border-radius:46%} }
.k2Seat{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:2px;min-width:78px;font:700 11px system-ui,sans-serif;color:#fff;text-align:center}
.k2Seat .nm{background:rgba(0,0,0,.6);border-radius:8px;padding:2px 6px;white-space:nowrap}
.k2Seat .nm b{color:#ffe94a}
.k2Seat.act .nm{box-shadow:0 0 0 2px #ffe94a}
.k2Seat.out{opacity:.4}
.k2Seat .bt{font:800 11px system-ui,sans-serif;color:#ffe94a;min-height:14px}
.k2Center{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:4px}
.k2Pot{font:900 14px system-ui,sans-serif;color:#ffe94a;background:rgba(0,0,0,.45);border-radius:999px;padding:2px 10px}
.k2Dlr{display:inline-block;width:18px;height:18px;border-radius:50%;background:#fff;color:#111;font:900 10px/18px system-ui;text-align:center}
.k2Bead{display:grid;grid-template-rows:repeat(6,16px);grid-auto-flow:column;grid-auto-columns:16px;gap:2px;justify-content:start;overflow-x:auto;max-width:100%;padding:4px;background:#f4f1e6;border-radius:8px;margin:6px auto}
.k2Bead i{width:16px;height:16px;border-radius:50%;font:900 9px/16px system-ui;text-align:center;color:#fff;font-style:normal}`; document.head.appendChild(css);
 function bankRow(ctx,st){ const cs=h('div',{className:'k2Chips'}); cs.appendChild(h('div',{className:'k2Bank'},['Chips: ',h('b',{className:'chipsNow'},String(getC())),' ',h('small',null,'· play chips only, no money')]));
  CH.forEach(([v,bg,fg])=>{ const b=h('button',{type:'button',className:'k2Chip'+(st.chip===v?' on':''),style:'background:'+bg+';color:'+fg,'aria-label':v+' chip'},String(v)); b.addEventListener('click',()=>{ st.chip=v; cs.querySelectorAll('.k2Chip').forEach(x=>x.classList.toggle('on',x===b)); }); cs.appendChild(b); });
  const rf=h('button',{type:'button'},'Refill'); rf.addEventListener('click',()=>{ setC(1000); ctx.status('Chips refilled to 1,000.'); }); cs.appendChild(rf); ctx.area.appendChild(cs); }
 const shoe=n=>{ let d=[]; for(let i=0;i<n;i++) d=d.concat(L.mkDeck(false)); return L.shuffle(d); };
 const stackEl=v=>{ let c=CH[0]; CH.forEach(x=>{ if(v>=x[0]) c=x; }); return h('span',{className:'k2Stack',style:'background:'+c[1]+';color:'+c[2]},String(v)); };
 /* ───────── BLACKJACK ───────── */
 const bv=c=>c.r===14?11:c.r>=10?10:c.r;
 const tot=cs=>{ let t=0,a=0; cs.forEach(c=>{ t+=bv(c); if(c.r===14) a++; }); while(t>21&&a){ t-=10; a--; } return {t,soft:a>0}; };
 G.reg('kc_blackjack','🂡 Blackjack Table (real)','Casino','The real table: six decks, the dealer stands on soft 17, blackjack pays 3 to 2, insurance pays 2 to 1. Double down on any first two cards; split pairs up to four hands (split aces get one card each). Pick a chip, tap the betting circle, then Deal.',ctx=>{
  const st={chip:10,bet:0,shoe:shoe(6),dealer:[],hands:[],cur:0,phase:'bet',ins:0,last:0};
  bankRow(ctx,st); const felt=h('div',{className:'k2Felt'}); ctx.area.appendChild(felt); const btns=h('div',{className:'k2Btns'}); ctx.area.appendChild(btns);
  const draw=()=>{ if(st.shoe.length<52){ st.shoe=shoe(6); ctx.status('New shoe shuffled.'); } return st.shoe.pop(); };
  const W=()=>L.cardW(ctx,6,70);
  function render(){ felt.innerHTML=''; const w=W(); felt.appendChild(h('div',{className:'k2Rule'},'Blackjack pays 3 to 2 · Dealer stands on soft 17 · Insurance pays 2 to 1'));
   const dl=st.dealer, hide=st.phase==='play'||st.phase==='ins'; const dr=h('div',{className:'k2Row'}); dl.forEach((c,i)=>dr.appendChild(L.cardEl(c,w,hide&&i===1))); felt.appendChild(h('div',{className:'k2Lbl'},['Dealer ',dl.length?h('b',null,hide?String(bv(dl[0])):String(tot(dl).t)):''])); felt.appendChild(dr);
   const hr=h('div',{className:'k2Row'}); if(st.hands.length){ st.hands.forEach((hd,i)=>{ const box=h('div',{className:'k2Hand'+(st.phase==='play'&&i===st.cur?' cur':'')}); const r=h('div',{className:'k2Row'}); hd.cards.forEach(c=>r.appendChild(L.cardEl(c,w*(st.hands.length>2?.8:1),false))); const t=tot(hd.cards); box.appendChild(r); box.appendChild(h('div',{className:'k2Lbl'},[h('b',null,(t.soft&&t.t<21?'soft ':'')+t.t),' · bet '+hd.bet+(hd.res?' · '+hd.res:'')])); hr.appendChild(box); }); }
   else { const sp=h('button',{type:'button',className:'k2Spot','aria-label':'Betting circle'},['BET',h('b',null,String(st.bet||0))]); sp.addEventListener('click',()=>{ if(st.phase!=='bet') return; if(getC()<st.chip) return ctx.status('Not enough chips.'); st.bet+=st.chip; setC(getC()-st.chip); render(); }); hr.appendChild(sp); }
   felt.appendChild(hr); buttons(); }
  function B(l,f,c,dis){ const b=h('button',{type:'button',className:c||''},l); b.disabled=!!dis; b.addEventListener('click',f); btns.appendChild(b); }
  function buttons(){ btns.innerHTML=''; const hd=st.hands[st.cur];
   if(st.phase==='bet'){ B('🂠 Deal',deal,'go',!st.bet); B('Clear bet',()=>{ setC(getC()+st.bet); st.bet=0; render(); },'',!st.bet); if(st.last&&!st.bet) B('🔁 Rebet '+st.last,()=>{ if(getC()<st.last) return ctx.status('Not enough chips.'); st.bet=st.last; setC(getC()-st.last); render(); }); }
   else if(st.phase==='ins'){ B('Insurance ('+Math.floor(st.hands[0].bet/2)+')',()=>insure(true),'go'); B('No insurance',()=>insure(false)); }
   else if(st.phase==='play'&&hd){ const two=hd.cards.length===2; B('Hit',hit,'go'); B('Stand',stand); B('Double',dbl,'',!(two&&getC()>=hd.bet)); B('Split',split,'',!(two&&hd.cards[0].r===hd.cards[1].r||two&&bv(hd.cards[0])===10&&bv(hd.cards[1])===10&&hd.cards[0].r===hd.cards[1].r)||st.hands.length>=4||getC()<hd.bet); }
   else if(st.phase==='done') B('🔁 Next hand',()=>{ st.phase='bet'; st.dealer=[]; st.hands=[]; st.bet=0; render(); },'go'); }
  function deal(){ st.last=st.bet; st.hands=[{cards:[draw(),draw()],bet:st.bet,done:false}]; st.bet=0; st.dealer=[draw(),draw()]; st.cur=0; L.beep&&L.beep(500,.05);
   if(st.dealer[0].r===14){ st.phase='ins'; ctx.status('Dealer shows an ace. Insurance?'); return render(); } peek(); }
  function insure(yes){ const hd=st.hands[0]; if(yes){ const c=Math.floor(hd.bet/2); if(getC()>=c){ st.ins=c; setC(getC()-c); } } peek(); }
  function peek(){ const dBJ=tot(st.dealer).t===21, pBJ=tot(st.hands[0].cards).t===21;
   if(st.ins){ if(dBJ){ setC(getC()+st.ins*3); ctx.status('Insurance pays 2 to 1.'); } st.ins=0; }
   if(dBJ||pBJ){ const hd=st.hands[0]; if(dBJ&&pBJ){ setC(getC()+hd.bet); hd.res='push'; } else if(pBJ){ setC(getC()+hd.bet+Math.floor(hd.bet*1.5)); hd.res='BLACKJACK! +'+Math.floor(hd.bet*1.5); } else hd.res='dealer blackjack'; st.phase='done'; ctx.status(hd.res); return render(); }
   st.phase='play'; ctx.status('Your move: Hit, Stand, Double or Split.'); render(); }
  function hit(){ const hd=st.hands[st.cur]; hd.cards.push(draw()); if(tot(hd.cards).t>=21) next(); else render(); }
  function stand(){ next(); }
  function dbl(){ const hd=st.hands[st.cur]; setC(getC()-hd.bet); hd.bet*=2; hd.cards.push(draw()); next(); }
  function split(){ const hd=st.hands[st.cur]; setC(getC()-hd.bet); const c2=hd.cards.pop(); const nh={cards:[c2,draw()],bet:hd.bet,aces:c2.r===14}; hd.cards.push(draw()); hd.aces=c2.r===14; st.hands.splice(st.cur+1,0,nh); if(hd.aces){ st.cur=st.hands.length; return dealerPlay(); } render(); }
  function next(){ st.cur++; while(st.cur<st.hands.length&&st.hands[st.cur].aces) st.cur++; if(st.cur>=st.hands.length) dealerPlay(); else render(); }
  function dealerPlay(){ st.phase='dealer'; const live=st.hands.some(hd=>tot(hd.cards).t<=21); if(live){ while(true){ const t=tot(st.dealer); if(t.t<17) st.dealer.push(draw()); else break; } }
   const dt=tot(st.dealer).t; let net=0; st.hands.forEach(hd=>{ const pt=tot(hd.cards).t; if(pt>21){ hd.res='bust'; net-=hd.bet; } else if(dt>21||pt>dt){ setC(getC()+hd.bet*2); hd.res='win +'+hd.bet; net+=hd.bet; } else if(pt===dt){ setC(getC()+hd.bet); hd.res='push'; } else { hd.res='lose'; net-=hd.bet; } });
   st.phase='done'; ctx.status('Dealer '+(dt>21?'busts with '+dt:'has '+dt)+' · '+(net>0?'you win '+net:net<0?'you lose '+(-net):'push')+'.'); render(); }
  render(); return {state:()=>st};
 });
 /* ───────── TEXAS HOLD'EM, SIX SEATS ───────── */
 G.reg('kc_holdem','🂮 Texas Hold’em Table (real)','Casino','A six-seat no-limit table: you and five computer players, blinds 5 and 10. Buy in for 500 chips from your bank (Cash out puts your stack back). Two cards each, then the flop, the turn and the river, with a round of betting on each. Best five-card hand wins; split pots and side pots are worked out like a real dealer does.',ctx=>{
  if(!PK){ ctx.status('The poker engine is loading.'); return; }
  const NAMES=['You','Ace','Blaze','Coco','Dex','Echo'];
  const st={seats:NAMES.map((n,i)=>({n,stack:i?500+rn(6)*50:0,cards:[],bet:0,tot:0,fold:false,allin:false,out:false,me:i===0,last:''})),btn:rn(6),deck:[],board:[],pot:0,cur:0,toCall:0,minR:10,street:'idle',busy:false,raiseTo:20};
  const table=h('div',{className:'k2Oval'}); ctx.area.appendChild(table); const btns=h('div',{className:'k2Btns'}); ctx.area.appendChild(btns);
  const pos=[[50,90],[10,66],[12,24],[50,8],[88,24],[90,66]];
  const me=()=>st.seats[0]; const live=()=>st.seats.filter(s=>!s.out&&!s.fold); const act=()=>st.seats.filter(s=>!s.out&&!s.fold&&!s.allin);
  function render(){ table.innerHTML=''; const w=Math.max(28,Math.min(48,Math.floor((table.clientWidth||ctx.W())/9)));
   st.seats.forEach((s,i)=>{ const showAll=st.street==='show'; const d=h('div',{className:'k2Seat'+(st.cur===i&&st.street!=='idle'&&st.street!=='show'?' act':'')+(s.out||s.fold?' out':''),style:'left:'+pos[i][0]+'%;top:'+pos[i][1]+'%'});
    const cr=h('div',{className:'k2Row',style:'min-height:0;margin:0'}); s.cards.forEach(c=>cr.appendChild(L.cardEl(c,w,!(s.me||showAll&&!s.fold)))); d.appendChild(cr);
    d.appendChild(h('div',{className:'nm'},[i===st.btn?h('span',{className:'k2Dlr'},'D'):'',' '+s.n+' ',h('b',null,String(s.stack))])); d.appendChild(h('div',{className:'bt'},s.bet?'bet '+s.bet:s.last)); table.appendChild(d); });
   const c=h('div',{className:'k2Center'}); const br=h('div',{className:'k2Row',style:'margin:0'}); st.board.forEach(cc=>br.appendChild(L.cardEl(cc,w,false))); for(let k=st.board.length;k<5;k++) br.appendChild(h('div',{style:'width:'+w+'px;height:'+Math.round(w*1.4)+'px;border:1px dashed rgba(255,255,255,.3);border-radius:6px'}));
   c.appendChild(br); c.appendChild(h('div',{className:'k2Pot'},'Pot '+(st.pot+st.seats.reduce((a,s)=>a+s.bet,0)))); table.appendChild(c); buttons(); }
  function B(l,f,c,dis){ const b=h('button',{type:'button',className:c||''},l); b.disabled=!!dis; b.addEventListener('click',f); btns.appendChild(b); }
  function buttons(){ btns.innerHTML=''; const m=me();
   if(st.street==='idle'||st.street==='show'){ if(m.stack<=0||m.out){ B('Buy in 500',()=>{ if(getC()<500) return ctx.status('You need 500 chips in your bank.'); setC(getC()-500); m.stack=500; m.out=false; render(); },'go'); } else B('▶ Deal next hand',hand,'go'); if(m.stack>0) B('Cash out '+m.stack,()=>{ setC(getC()+m.stack); m.stack=0; m.out=true; ctx.status('Cashed out to your bank.'); render(); }); return; }
   if(st.cur!==0||m.fold||m.allin) return; const need=st.toCall-m.bet; const minTo=Math.min(m.stack+m.bet,st.toCall+st.minR);
   B('Fold',()=>me_act('fold')); B(need>0?'Call '+Math.min(need,m.stack):'Check',()=>me_act('call'),'go');
   const opts=[[minTo,'Min '+minTo],[Math.min(m.stack+m.bet,st.toCall+Math.max(st.minR,Math.round((st.pot+st.seats.reduce((a,s)=>a+s.bet,0)+need)/2))),'½ pot'],[Math.min(m.stack+m.bet,st.toCall+Math.max(st.minR,st.pot+st.seats.reduce((a,s)=>a+s.bet,0)+need)),'Pot']];
   const seen={}; opts.forEach(([to,l])=>{ if(to>st.toCall&&!seen[to]&&to<m.stack+m.bet){ seen[to]=1; B('Raise to '+to+' ('+l+')',()=>me_act('raise',to)); } }); B('All in '+(m.stack),()=>me_act('raise',m.stack+m.bet)); }
  function hand(){ const alive=st.seats.filter(s=>s.stack>0); st.seats.forEach(s=>{ if(!s.me&&s.stack<=0){ s.stack=500; } s.out=s.stack<=0; s.cards=[]; s.bet=0; s.tot=0; s.fold=false; s.allin=false; s.last=''; });
   if(st.seats.filter(s=>!s.out).length<2) return ctx.status('Not enough players.'); do{ st.btn=(st.btn+1)%6; }while(st.seats[st.btn].out);
   st.deck=L.shuffle(L.mkDeck(false)); st.board=[]; st.pot=0; for(let r=0;r<2;r++) st.seats.forEach(s=>{ if(!s.out) s.cards.push(st.deck.pop()); });
   const nx=i=>{ do{ i=(i+1)%6; }while(st.seats[i].out); return i; }; const sb=nx(st.btn), bb=nx(sb); post(sb,5); post(bb,10); st.toCall=10; st.minR=10; st.street='pre'; st.cur=nx(bb); st.acted=new Set(); ctx.status('Your cards: '+me().cards.map(L.cname).join(' and ')+'.'); render(); loop(); }
  function post(i,a){ const s=st.seats[i]; const x=Math.min(a,s.stack); s.stack-=x; s.bet+=x; s.tot+=x; if(!s.stack) s.allin=true; s.last=a===5?'small blind':'big blind'; }
  function nextSeat(i){ for(let k=1;k<=6;k++){ const j=(i+k)%6; const s=st.seats[j]; if(!s.out&&!s.fold&&!s.allin) return j; } return -1; }
  function doAct(i,a,to){ const s=st.seats[i]; const need=st.toCall-s.bet;
   if(a==='fold'){ s.fold=true; s.last='fold'; }
   else if(a==='call'){ const x=Math.min(need,s.stack); s.stack-=x; s.bet+=x; s.tot+=x; s.last=x?'call '+x:'check'; if(!s.stack) s.allin=true; }
   else { to=Math.max(Math.min(to,s.stack+s.bet),Math.min(s.stack+s.bet,st.toCall+st.minR)); const x=to-s.bet; s.stack-=x; s.bet=to; s.tot+=x; if(to>st.toCall){ st.minR=Math.max(st.minR,to-st.toCall); st.toCall=to; st.acted=new Set(); } s.last=(s.stack?'raise to ':'all in ')+to; if(!s.stack) s.allin=true; }
   st.acted.add(i); L.beep&&L.beep(a==='fold'?200:420,.03); }
  function roundDone(){ const A=act(); if(live().length<=1) return true; return A.every(s=>st.acted.has(st.seats.indexOf(s))&&s.bet===st.toCall)||A.length===0||(A.length===1&&A[0].bet>=st.toCall&&st.acted.has(st.seats.indexOf(A[0]))); }
  function me_act(a,to){ if(st.cur!==0) return; doAct(0,a,to); advance(); }
  function advance(){ if(roundDone()) return street(); st.cur=nextSeat(st.cur); if(st.cur<0) return street(); render(); loop(); }
  function loop(){ if(st.busy) return; const s=st.seats[st.cur]; if(!s||s.me||st.street==='idle'||st.street==='show'){ render(); return; } st.busy=true; render();
   setTimeout(()=>{ st.busy=false; if(st.street==='idle'||st.street==='show') return; botAct(st.cur); advance(); },550+rn(500)); }
  function botAct(i){ const s=st.seats[i]; const need=st.toCall-s.bet; const nOpp=Math.max(1,live().length-1); let eq=.5; try{ eq=PK.equity(s.cards,st.board,nOpp,120); }catch(_){ }
   const pot=st.pot+st.seats.reduce((a,x)=>a+x.bet,0); const odds=need>0?need/(pot+need):0; const r=Math.random();
   if(need>0&&eq<odds*.9&&r>.1) return doAct(i,'fold'); if(eq>.62&&r<.7||eq>.45&&r<.12) return doAct(i,'raise',st.toCall+Math.max(st.minR,Math.round(pot*(eq>.75?.9:.55)))); return doAct(i,'call'); }
  function collect(){ st.seats.forEach(s=>{ st.pot+=s.bet; s.bet=0; }); st.toCall=0; st.minR=10; st.acted=new Set(); }
  function street(){ collect(); if(live().length<=1) return showdown(); const order={pre:'flop',flop:'turn',turn:'river',river:'show'}; st.street=order[st.street];
   if(st.street==='flop') st.board.push(st.deck.pop(),st.deck.pop(),st.deck.pop()); else if(st.street==='turn'||st.street==='river') st.board.push(st.deck.pop()); else return showdown();
   st.seats.forEach(s=>{ if(!s.fold&&!s.out) s.last=''; }); if(act().length<=1){ render(); return setTimeout(street,700); } st.cur=nextSeat(st.btn); render(); loop(); }
  function showdown(){ st.street='show'; while(st.board.length<5&&live().length>1) st.board.push(st.deck.pop()); const L2=live(); let lines=[];
   if(L2.length===1){ L2[0].stack+=st.pot; lines.push(L2[0].n+' wins '+st.pot+' (everyone folded)'); }
   else { const sc=new Map(); L2.forEach(s=>sc.set(s,PK.ev7(s.cards.concat(st.board)))); const contrib=st.seats.map(s=>s.tot); let levels=[...new Set(st.seats.filter(s=>!s.out&&s.tot>0).map(s=>s.tot))].sort((a,b)=>a-b), prev=0;
    levels.forEach(lv=>{ let pot=0; st.seats.forEach(s=>{ pot+=Math.max(0,Math.min(s.tot,lv)-prev); }); const elig=L2.filter(s=>s.tot>=lv); if(!elig.length||!pot){ prev=lv; return; } const top=Math.max(...elig.map(s=>sc.get(s))); const win=elig.filter(s=>sc.get(s)===top); const share=Math.floor(pot/win.length); win.forEach(s=>s.stack+=share); win[0].stack+=pot-share*win.length; lines.push(win.map(s=>s.n).join(' & ')+' win'+(win.length>1?'':'s')+' '+pot+' with '+PK.name(top)); prev=lv; }); }
   st.pot=0; ctx.status(lines.join(' · ')); render(); }
  render(); ctx.status('Buy in for 500 from your bank, then Deal.'); return {state:()=>st};
 });
 /* ───────── BACCARAT (punto banco) ───────── */
 const pv=c=>c.r>=10&&c.r<=13?0:c.r===14?1:c.r; const pts=cs=>cs.reduce((a,c)=>a+pv(c),0)%10;
 G.reg('kc_baccarat','🂱 Baccarat Table (real)','Casino','Punto banco by the real tableau, from an eight-deck shoe. Bet Player (1 to 1), Banker (0.95 to 1, the house keeps 5%), Tie (8 to 1; Player and Banker push), or the pair bets (11 to 1). Closest to 9 wins; the third-card rules are dealt for you, exactly as a casino does. The bead plate keeps the history.',ctx=>{
  const st={chip:10,bets:{},shoe:shoe(8),P:[],Bk:[],hist:[],phase:'bet',res:null};
  bankRow(ctx,st); const felt=h('div',{className:'k2Felt'}); ctx.area.appendChild(felt); const btns=h('div',{className:'k2Btns'}); ctx.area.appendChild(btns);
  const draw=()=>{ if(st.shoe.length<20) st.shoe=shoe(8); return st.shoe.pop(); };
  const AREAS=[['ppair','Player Pair','11:1'],['tie','TIE','8 to 1'],['bpair','Banker Pair','11:1'],['player','PLAYER','1 to 1'],['banker','BANKER','0.95 to 1']];
  function render(){ felt.innerHTML=''; const w=L.cardW(ctx,7,64); felt.appendChild(h('div',{className:'k2Rule'},'Tie pays 8 to 1 · Banker pays 0.95 to 1 · Pairs pay 11 to 1'));
   const hands=h('div',{className:'k2Row',style:'gap:14px'}); [['PLAYER',st.P],['BANKER',st.Bk]].forEach(([n,cs])=>{ const b=h('div',{className:'k2Hand'}); const r=h('div',{className:'k2Row'}); cs.forEach(c=>r.appendChild(L.cardEl(c,w,false))); b.appendChild(h('div',{className:'k2Lbl'},[n+' ',cs.length?h('b',null,String(pts(cs))):''])); b.appendChild(r); hands.appendChild(b); }); felt.appendChild(hands);
   const gr=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(3,minmax(0,1fr))'}); AREAS.forEach(([k,l,p],i)=>{ const b=h('button',{type:'button',style:i>=3?'grid-column:span '+(i===3?'1':'2'):'' },[l,h('small',null,p)]); if(st.bets[k]) b.appendChild(stackEl(st.bets[k])); if(st.res&&st.res.win.includes(k)) b.classList.add('win'); b.addEventListener('click',()=>{ if(st.phase!=='bet') return; if(getC()<st.chip) return ctx.status('Not enough chips.'); st.bets[k]=(st.bets[k]||0)+st.chip; setC(getC()-st.chip); render(); }); gr.appendChild(b); });
   felt.appendChild(gr); const bead=h('div',{className:'k2Bead','aria-label':'Bead plate'}); st.hist.slice(-60).forEach(r=>bead.appendChild(h('i',{style:'background:'+(r==='P'?'#2a6fd6':r==='B'?'#d62a36':'#1e9c4a')},r))); felt.appendChild(bead); buttons(); }
  function buttons(){ btns.innerHTML=''; const any=Object.keys(st.bets).length; const B=(l,f,c,d)=>{ const b=h('button',{type:'button',className:c||''},l); b.disabled=!!d; b.addEventListener('click',f); btns.appendChild(b); };
   if(st.phase==='bet'){ B('🂠 Deal',deal,'go',!any); B('Clear',()=>{ setC(getC()+Object.values(st.bets).reduce((a,c)=>a+c,0)); st.bets={}; render(); },'',!any); } else B('🔁 Next hand',()=>{ st.phase='bet'; st.P=[]; st.Bk=[]; st.bets={}; st.res=null; render(); },'go'); }
  function deal(){ const P=[draw(),draw()], Bk=[draw(),draw()]; let p=pts(P), b=pts(Bk);
   if(p<8&&b<8){ let p3=null; if(p<=5){ p3=draw(); P.push(p3); } if(p3===null){ if(b<=5) Bk.push(draw()); } else { const t=pv(p3); const drawB=b<=2||(b===3&&t!==8)||(b===4&&t>=2&&t<=7)||(b===5&&t>=4&&t<=7)||(b===6&&(t===6||t===7)); if(drawB) Bk.push(draw()); } }
   p=pts(P); b=pts(Bk); st.P=P; st.Bk=Bk; const w=p>b?'player':b>p?'banker':'tie'; const win=[w]; if(P[0].r===P[1].r) win.push('ppair'); if(Bk[0].r===Bk[1].r) win.push('bpair'); st.res={win}; st.hist.push(w==='player'?'P':w==='banker'?'B':'T');
   let back=0, net=0; Object.entries(st.bets).forEach(([k,a])=>{ let m=-1; if(k===w) m=k==='banker'?.95:k==='tie'?8:1; else if(w==='tie'&&(k==='player'||k==='banker')) m=0; if((k==='ppair'||k==='bpair')&&win.includes(k)) m=11; if(m>=0){ back+=a+Math.floor(a*m); net+=Math.floor(a*m); } else net-=a; }); if(back) setC(getC()+back);
   st.phase='done'; ctx.status((w==='tie'?'Tie '+p+'–'+b:(w==='player'?'Player':'Banker')+' wins '+Math.max(p,b)+' to '+Math.min(p,b))+' · '+(net>0?'you win '+net:net<0?'you lose '+(-net):'push')+'.'); render(); }
  render(); return {state:()=>st};
 });
 /* ───────── SIC BO ───────── */
 const TOT={4:50,17:50,5:18,16:18,6:14,15:14,7:12,14:12,8:8,13:8,9:6,12:6,10:6,11:6};
 G.reg('kc_sicbo','🎲 Sic Bo Table (real)','Casino','Three dice under the shaker, and the real layout: Small (4–10) and Big (11–17) pay 1 to 1 and lose to any triple; totals pay 6 to 50 to 1; a double pays 8 to 1, a specific triple 150 to 1, any triple 24 to 1; each two-dice combination pays 5 to 1; a single number pays 1, 2 or 3 to 1 for one, two or three dice.',ctx=>{
  const st={chip:10,bets:{},d:[1,2,3],phase:'bet',win:[],rolling:false};
  bankRow(ctx,st); const S=Math.min(ctx.W(),520), Hh=Math.round(S*.36); const cv=h('canvas',{width:S*2,height:Hh*2,style:'width:'+S+'px;max-width:100%;display:block;margin:0 auto 6px;border-radius:14px;background:radial-gradient(ellipse,#1f8a4c,#0b5a2e)'}); const g=cv.getContext('2d'); g.scale(2,2); ctx.area.appendChild(cv);
  const felt=h('div',{className:'k2Felt'}); ctx.area.appendChild(felt); const btns=h('div',{className:'k2Btns'}); ctx.area.appendChild(btns);
  const PIP={1:[[.5,.5]],2:[[.28,.28],[.72,.72]],3:[[.28,.28],[.5,.5],[.72,.72]],4:[[.28,.28],[.72,.28],[.28,.72],[.72,.72]],5:[[.28,.28],[.72,.28],[.5,.5],[.28,.72],[.72,.72]],6:[[.28,.24],[.72,.24],[.28,.5],[.72,.5],[.28,.76],[.72,.76]]};
  function dice(vals,rot){ g.clearRect(0,0,S,Hh); const s=Hh*.42; vals.forEach((v,i)=>{ const x=S*(.3+i*.2), y=Hh*.5+(i===1?-Hh*.08:Hh*.06); g.save(); g.translate(x,y); g.rotate((rot||0)*(i+1)*.7); g.fillStyle='rgba(0,0,0,.3)'; g.fillRect(-s/2+4,-s/2+6,s,s); const gr=g.createLinearGradient(-s/2,-s/2,s/2,s/2); gr.addColorStop(0,'#fff'); gr.addColorStop(1,'#d9d0c8'); g.fillStyle=gr; L.rr(g,-s/2,-s/2,s,s,s*.18); g.fill(); g.fillStyle=v===1||v===4?'#d62a36':'#111'; PIP[v].forEach(([px,py])=>{ g.beginPath(); g.arc(-s/2+px*s,-s/2+py*s,s*.09,0,7); g.fill(); }); g.restore(); }); }
  function cell(k,l,p,span){ const b=h('button',{type:'button',style:span?'grid-column:span '+span:''},[l,h('small',null,p)]); if(st.bets[k]) b.appendChild(stackEl(st.bets[k])); if(st.win.includes(k)) b.classList.add('win'); b.addEventListener('click',()=>{ if(st.phase!=='bet'||st.rolling) return; if(getC()<st.chip) return ctx.status('Not enough chips.'); st.bets[k]=(st.bets[k]||0)+st.chip; setC(getC()-st.chip); render(); }); return b; }
  function render(){ felt.innerHTML=''; felt.appendChild(h('div',{className:'k2Rule'},'Small 4–10 · Big 11–17 · lose to any triple'));
   const g1=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(4,minmax(0,1fr))'}); g1.appendChild(cell('small','SMALL','4–10 · 1:1')); g1.appendChild(cell('odd','ODD','1:1')); g1.appendChild(cell('even','EVEN','1:1')); g1.appendChild(cell('big','BIG','11–17 · 1:1')); felt.appendChild(g1);
   const g2=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(7,minmax(0,1fr));margin-top:4px'}); /* the doubles */
   g2.innerHTML=''; for(let n=1;n<=6;n++) g2.appendChild(cell('dbl'+n,n+' '+n,'8:1')); g2.appendChild(cell('anyt','ANY TRIPLE','24:1')); felt.appendChild(g2);
   const g3=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(6,minmax(0,1fr));margin-top:4px'}); for(let n=1;n<=6;n++) g3.appendChild(cell('tri'+n,n+n+''+n,'150:1')); felt.appendChild(g3);
   const g4=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(7,minmax(0,1fr));margin-top:4px'}); for(let t=4;t<=17;t++) g4.appendChild(cell('t'+t,String(t),TOT[t]+':1')); felt.appendChild(g4);
   const g5=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(5,minmax(0,1fr));margin-top:4px'}); for(let a=1;a<=6;a++) for(let b=a+1;b<=6;b++) g5.appendChild(cell('c'+a+b,a+'·'+b,'5:1')); felt.appendChild(g5);
   const g6=h('div',{className:'k2Grid',style:'grid-template-columns:repeat(6,minmax(0,1fr));margin-top:4px'}); for(let n=1;n<=6;n++) g6.appendChild(cell('s'+n,'ONE '+n,'1·2·3 to 1')); felt.appendChild(g6);
   btns.innerHTML=''; const any=Object.keys(st.bets).length; const B=(l,f,c,d)=>{ const b=h('button',{type:'button',className:c||''},l); b.disabled=!!d; b.addEventListener('click',f); btns.appendChild(b); };
   if(st.phase==='bet'){ B('🎲 Shake and roll',roll,'go',!any||st.rolling); B('Clear',()=>{ setC(getC()+Object.values(st.bets).reduce((a,c)=>a+c,0)); st.bets={}; render(); },'',!any||st.rolling); } else B('🔁 Next roll',()=>{ st.phase='bet'; st.bets={}; st.win=[]; render(); },'go'); }
  function roll(){ if(st.rolling) return; st.rolling=true; const fin=[1+rn(6),1+rn(6),1+rn(6)]; const t0=performance.now(); render();
   ctx.raf((dt,t)=>{ const k=Math.min(1,(t-t0)/1300); dice(k<.85?[1+rn(6),1+rn(6),1+rn(6)]:fin,(1-k)*8); if(k>=1){ st.rolling=false; settle(fin); return false; } }); }
  function settle(d){ const s=d[0]+d[1]+d[2], tri=d[0]===d[1]&&d[1]===d[2], cnt=n=>d.filter(x=>x===n).length; const W=[];
   if(!tri&&s<=10) W.push('small'); if(!tri&&s>=11) W.push('big'); if(!tri&&s%2) W.push('odd'); if(!tri&&s%2===0) W.push('even'); if(TOT[s]) W.push('t'+s); if(tri){ W.push('anyt','tri'+d[0]); } for(let n=1;n<=6;n++){ if(cnt(n)>=2) W.push('dbl'+n); if(cnt(n)) W.push('s'+n); } for(let a=1;a<=6;a++) for(let b=a+1;b<=6;b++) if(cnt(a)&&cnt(b)) W.push('c'+a+b);
   const pay=k=>k==='small'||k==='big'||k==='odd'||k==='even'?1:k[0]==='t'&&k!=='tri'?TOT[+k.slice(1)]:k==='anyt'?24:k.startsWith('tri')?150:k.startsWith('dbl')?8:k[0]==='c'?5:k[0]==='s'?cnt(+k.slice(1)):0;
   let back=0, net=0; Object.entries(st.bets).forEach(([k,a])=>{ if(W.includes(k)){ const m=pay(k); back+=a+a*m; net+=a*m; } else net-=a; }); if(back) setC(getC()+back);
   st.win=W; st.phase='done'; ctx.status('🎲 '+d.join(' · ')+' = '+s+(tri?' · TRIPLE':'')+' · '+(net>0?'you win '+net:net<0?'you lose '+(-net):'even')+'.'); render(); }
  dice(st.d,0); render(); return {state:()=>st};
 });
})();
