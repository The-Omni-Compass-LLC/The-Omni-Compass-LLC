(()=>{ /* 🎲 ANCIENT AND MATHEMATICAL BOARD GAMES (v225): Nim, Oware (Abapa), the Royal Game of Ur and Senet, each against the
   computer, with option rows. Traditional public-domain games; the Senet rules follow the widely used Kendall reconstruction. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h; const CAT='Board';
 const OPT=(ctx,id,defs)=>window.KGOPT?KGOPT.row(ctx,id,defs):Object.fromEntries(defs.map(d=>[d[0],d[3]]));
 const css=document.createElement('style'); css.textContent=`
#gamesDock .k6{width:100%;max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:8px;align-items:center;color:#fff;font:700 14px system-ui,sans-serif}
#gamesDock .k6Bar{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}
#gamesDock .k6Bar button{min-height:44px;padding:0 14px;border-radius:12px;font:800 14px system-ui,sans-serif}
#gamesDock .k6Bar button.go{background:linear-gradient(180deg,#ffe94a,#e0a10c)!important;color:#1a1200!important}
#gamesDock .k6Msg{min-height:1.5em;text-align:center;color:#ffe9b0}
#gamesDock .nimRow{display:flex;gap:6px;align-items:center;justify-content:center;min-height:58px;flex-wrap:wrap}
#gamesDock .nimRow b{width:26px;color:#ffe94a;text-align:right}
#gamesDock .nimS{width:16px;height:54px;border-radius:8px;background:linear-gradient(180deg,#ffd27a,#c27a12);border:2px solid #3a2200;cursor:pointer;padding:0!important;min-height:0!important}
#gamesDock .nimS.sel{background:linear-gradient(180deg,#ff6b6b,#a01818);transform:translateY(-6px)}
#gamesDock .owB{display:grid;grid-template-columns:auto repeat(6,minmax(0,1fr)) auto;gap:6px;align-items:center;background:linear-gradient(180deg,#6b3a12,#4a250a);border-radius:22px;padding:10px;width:100%;box-shadow:inset 0 0 18px rgba(0,0,0,.6)}
#gamesDock .owP{aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 40% 35%,#3a1d06,#1e0d02);border:2px solid #8a5a2a;display:flex;align-items:center;justify-content:center;font:900 clamp(14px,4vw,24px) system-ui;color:#ffe9b0;cursor:pointer;padding:0!important;min-height:0!important;position:relative}
#gamesDock .owP.mine{border-color:#ffe94a}#gamesDock .owP.can{box-shadow:0 0 0 3px #ffe94a}#gamesDock .owP.last{box-shadow:0 0 0 3px #7cff8a}
#gamesDock .owP i{position:absolute;inset:18%;border-radius:50%;background:radial-gradient(circle,#d9c7a0 0 2px,transparent 3px) 0 0/9px 9px;opacity:.55;pointer-events:none}
#gamesDock .owS{grid-row:1/3;width:clamp(44px,10vw,70px);height:100%;min-height:110px;border-radius:30px;background:#1e0d02;border:2px solid #8a5a2a;display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 22px system-ui;color:#ffe94a}
#gamesDock .owS small{font:700 11px system-ui;color:#d8c0a0}
#gamesDock .urB{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:4px;width:100%;max-width:560px}
#gamesDock .urC{aspect-ratio:1;border-radius:8px;background:#3d2a6e;border:2px solid #6b56b0;display:flex;align-items:center;justify-content:center;position:relative;padding:0!important;min-height:0!important;cursor:pointer}
#gamesDock .urC.ros{background:radial-gradient(circle,#ffe94a 0 18%,#d63f6a 19% 34%,#2c7be5 35% 52%,#3d2a6e 53%)}
#gamesDock .urC.gap{visibility:hidden}
#gamesDock .urC.can{box-shadow:0 0 0 3px #7cff8a}
#gamesDock .urPc{width:70%;height:70%;border-radius:50%;border:3px solid #fff;box-shadow:0 3px 0 rgba(0,0,0,.4)}
#gamesDock .urPc.p0{background:radial-gradient(circle at 35% 30%,#fff7c8,#e0a10c)}#gamesDock .urPc.p1{background:radial-gradient(circle at 35% 30%,#9ad7ff,#1e5fbf)}
#gamesDock .urRack{display:flex;gap:4px;align-items:center;justify-content:center;flex-wrap:wrap;min-height:34px}
#gamesDock .urRack .urPc{width:26px;height:26px;cursor:pointer}#gamesDock .urRack .urPc.can{box-shadow:0 0 0 3px #7cff8a}
#gamesDock .dice{display:flex;gap:6px;justify-content:center}
#gamesDock .dice span{width:30px;height:30px;clip-path:polygon(50% 0,100% 100%,0 100%);background:#c9b28a;display:flex;align-items:flex-end;justify-content:center}
#gamesDock .dice span.on::after{content:'';width:8px;height:8px;border-radius:50%;background:#fff;margin-bottom:5px}
#gamesDock .snB{display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:3px;width:100%;max-width:640px;background:#7a5a2a;padding:6px;border-radius:10px}
#gamesDock .snC{aspect-ratio:1;background:#e8d3a0;border-radius:5px;display:flex;align-items:center;justify-content:center;position:relative;font:900 clamp(11px,2.6vw,18px) system-ui;color:#7a5a2a;padding:0!important;min-height:0!important;cursor:pointer}
#gamesDock .snC small{position:absolute;left:2px;top:0;font:700 9px system-ui;color:#9a7a4a}
#gamesDock .snC.can{box-shadow:0 0 0 3px #1fa34a inset}
#gamesDock .snC.to{box-shadow:0 0 0 3px #ffe94a inset}
#gamesDock .snPc{width:72%;height:72%;border:2px solid #fff;box-shadow:0 2px 0 rgba(0,0,0,.35)}
#gamesDock .snPc.p0{border-radius:50% 50% 8% 8%;background:#b8322a}#gamesDock .snPc.p1{border-radius:30%;background:#1e4fa0}
#gamesDock .sticks{display:flex;gap:5px;justify-content:center}
#gamesDock .sticks span{width:12px;height:46px;border-radius:6px;background:#3a2200;border:2px solid #c9b28a}#gamesDock .sticks span.w{background:#f6efd8}`; document.head.appendChild(css);
 const bar=(root)=>{ const b=h('div',{className:'k6Bar'}); root.appendChild(b); return b; };
 const btn=(b,l,f,c)=>{ const e=h('button',{type:'button',className:c||''},l); e.addEventListener('click',f); b.appendChild(e); return e; };
 const beep=(f,d)=>{ try{ L.beep(f,d||.04); }catch(_){ } };
 const rnd=n=>Math.floor(Math.random()*n);

 /* ───────── NIM ───────── */
 const FIRST=[['me','You'],['ai','Computer'],['coin','Toss a coin'],['loser','The loser of the last game'],['winner','The winner of the last game']];
 const firstOf=(o,lastW)=>o==='ai'?1:o==='coin'?rnd(2):o==='loser'?(lastW==null?0:1-lastW):o==='winner'?(lastW==null?0:lastW):0;
 G.reg('b_nim','Nim',CAT,'Rows of matchsticks lie on the table. On your turn take sticks from one row only: tap a stick and every stick to its right in that row is picked too, then press Take. Pick the rules above: in normal Nim whoever takes the last stick wins; in misère whoever takes the last stick loses; the “at most 3” games limit a turn to 1, 2 or 3 sticks; “21” is one row of 21 where taking the last stick loses. The computer solves every position exactly, so on Hard it never slips; on Easy it often does.',ctx=>{
  const O=OPT(ctx,'b_nim',[['rows','Rows',[['1,3,5,7','1 · 3 · 5 · 7 (classic)'],['3,4,5','3 · 4 · 5'],['2,3,4,5,6','2 to 6'],['1,2,3,4,5,6,7','1 to 7'],['5,5,5','5 · 5 · 5']],'1,3,5,7'],['mode','Rules',[['normal','Normal: last stick wins'],['misere','Misère: last stick loses'],['cap3','At most 3 a turn, last wins'],['cap3m','At most 3 a turn, last loses'],['21','One row of 21, at most 3, last loses']],'normal'],['first','First move',FIRST,'me']]);
  const cap=O.mode==='cap3'||O.mode==='cap3m'||O.mode==='21'?3:99, lastLoses=O.mode==='misere'||O.mode==='cap3m'||O.mode==='21';
  const st={rows:[],turn:0,sel:null,over:false,msg:''}; let lastW=null; const root=h('div',{className:'k6'}); ctx.area.appendChild(root);
  const memo=new Map(); /* win(rows): can the player to move force a win? */
  function win(R){ const k=R.slice().sort().join(','); if(memo.has(k)) return memo.get(k); const tot=R.reduce((a,b)=>a+b,0); let res; if(!tot) res=lastLoses; else { res=false; outer: for(let i=0;i<R.length;i++){ if(i&&R[i]===R[i-1]) continue; for(let t=1;t<=Math.min(R[i],cap);t++){ const n=R.slice(); n[i]-=t; if(!win(n)){ res=true; break outer; } } } } memo.set(k,res); return res; }
  function best(){ const R=st.rows; for(let i=0;i<R.length;i++) for(let t=1;t<=Math.min(R[i],cap);t++){ const n=R.slice(); n[i]-=t; if(!win(n)) return [i,t]; } return null; }
  function deal(){ st.rows=O.mode==='21'?[21]:String(O.rows).split(',').map(Number); st.sel=null; st.over=false; st.turn=firstOf(O.first,lastW); st.msg=st.turn?'The computer starts.':'Your turn: tap a stick.'; render(); if(st.turn) ctx.after(900,ai); }
  function take(r,n,who){ st.rows[r]-=n; beep(who?330:560); st.sel=null; const left=st.rows.reduce((a,b)=>a+b,0);
   if(!left){ st.over=true; const winner=lastLoses?1-who:who; lastW=winner?1:0; st.msg=(who?'The computer took the last stick. ':'You took the last stick. ')+(winner?'The computer wins.':'You win! 🎉'); render(); return; }
   st.turn=1-who; st.msg=who?'The computer took '+n+' from row '+(r+1)+'. Your turn.':'You took '+n+'. The computer thinks…'; render(); if(st.turn) ctx.after(900,ai); }
  function ai(){ if(st.over) return; const noise=[0.55,0.25,0][ctx.diff||0]; let m=Math.random()<noise?null:best(); if(!m){ const nz=st.rows.map((x,i)=>[x,i]).filter(x=>x[0]>0); const [x,i]=nz[rnd(nz.length)]; m=[i,1+rnd(Math.min(x,cap))]; } take(m[0],m[1],1); }
  function render(){ root.innerHTML=''; st.rows.forEach((n,r)=>{ const row=h('div',{className:'nimRow'}); row.appendChild(h('b',null,String(r+1)));
    for(let k=0;k<n;k++){ const s=h('button',{type:'button',className:'nimS'+(st.sel&&st.sel.r===r&&k>=st.sel.k?' sel':''),'aria-label':'Row '+(r+1)+' stick '+(k+1)}); s.addEventListener('click',()=>{ if(st.over||st.turn) return; const k2=Math.max(k,n-cap); st.sel={r,k:k2}; st.msg='Take '+(n-k2)+' from row '+(r+1)+'? Press Take.'+(n-k>cap?' (At most '+cap+' a turn.)':''); render(); }); row.appendChild(s); }
    if(!n) row.appendChild(h('span',{style:'opacity:.5'},'empty')); root.appendChild(row); });
   root.appendChild(h('div',{className:'k6Msg'},st.msg)); const b=bar(root);
   if(!st.over&&!st.turn&&st.sel) btn(b,'✋ Take '+(st.rows[st.sel.r]-st.sel.k),()=>take(st.sel.r,st.rows[st.sel.r]-st.sel.k,0),'go');
   btn(b,'🔁 New game',deal); ctx.status(st.msg+' · '+(lastLoses?'last stick loses':'last stick wins')+(cap<99?' · at most '+cap+' a turn':'')); }
  deal(); window.__kgst=()=>st; return {state:()=>st,api:{best,win}};
 });

 /* ───────── OWARE (ABAPA) ───────── */
 G.reg('b_oware','Oware (Abapa)',CAT,'The West African count-and-capture game. Twelve pits, four seeds in each; the bottom row is yours. Tap one of your pits to scoop its seeds and sow them one by one, counterclockwise, into the following pits (a pit of twelve or more skips the pit it came from). If your last seed lands in the computer’s row and makes 2 or 3 there, you capture them, and also the pit before it if that now holds 2 or 3, and so on back along the computer’s row. You may not take every seed the computer has (a grand slam captures nothing). If the computer’s row is empty you must give it seeds if you can. First to 25 seeds wins.',ctx=>{
  const O=OPT(ctx,'b_oware',[['first','First move',FIRST,'me'],['seeds','Seeds per pit',[[2,'2 (very short)'],[3,'3 (short game)'],[4,'4 (standard)'],[5,'5 (long game)'],[6,'6 (longest)']],4]]); let lastW=null;
  const st={p:[],s:[0,0],turn:0,over:false,msg:'',last:-1,moves:0};
  const root=h('div',{className:'k6'}); ctx.area.appendChild(root);
  const side=(i,who)=>who?i>=6:i<6;
  function sow(p,from,who){ const b=p.slice(); let n=b[from]; b[from]=0; let i=from; while(n){ i=(i+1)%12; if(i===from) continue; b[i]++; n--; } let cap=0; const opp=k=>who?k<6:k>=6; let j=i; const caps=[]; while(opp(j)&&(b[j]===2||b[j]===3)){ caps.push(j); j=(j+11)%12; }
   const oppTotal=b.reduce((a,v,k)=>a+(opp(k)?v:0),0); const capSum=caps.reduce((a,k)=>a+b[k],0); if(caps.length&&capSum<oppTotal){ caps.forEach(k=>{ cap+=b[k]; b[k]=0; }); } return {b,cap,last:i}; }
  function legal(p,who){ const L=[]; for(let i=who?6:0;i<(who?12:6);i++) if(p[i]) L.push(i); const oppEmpty=p.reduce((a,v,k)=>a+((who?k<6:k>=6)?v:0),0)===0; if(oppEmpty){ const F=L.filter(i=>{ const r=sow(p,i,who).b; return r.reduce((a,v,k)=>a+((who?k<6:k>=6)?v:0),0)>0; }); return F; } return L; }
  function deal(){ st.p=Array(12).fill(+O.seeds); st.s=[0,0]; st.over=false; st.last=-1; st.moves=0; st.turn=firstOf(O.first,lastW); st.msg=st.turn?'The computer sows first.':'Your turn: tap one of your pits (bottom row).'; render(); if(st.turn) ctx.after(900,ai); }
  function finish(){ st.over=true; const w=st.s[0]>st.s[1]?0:st.s[1]>st.s[0]?1:-1; if(w>=0) lastW=w; st.msg='Final: you '+st.s[0]+', computer '+st.s[1]+'. '+(w<0?'A draw.':w?'The computer wins.':'You win! 🎉'); render(); }
  function move(i,who){ const r=sow(st.p,i,who); st.p=r.b; st.s[who]+=r.cap; st.last=r.last; st.moves++; beep(who?330:560); st.msg=(who?'The computer sowed pit '+(12-i):'You sowed')+(r.cap?' and captured '+r.cap+'.':'.');
   const total=st.target||(+O.seeds*12); if(st.s[0]>total/2||st.s[1]>total/2) return finish();
   const nx=1-who; if(!legal(st.p,nx).length){ // the next player cannot move: the mover takes what is left on the board
    st.s[who]+=st.p.reduce((a,b)=>a+b,0); st.p=Array(12).fill(0); return finish(); }
   if(st.moves>400){ for(let k=0;k<12;k++){ st.s[k<6?0:1]+=st.p[k]; st.p[k]=0; } return finish(); }
   st.turn=nx; render(); if(st.turn) ctx.after(800,ai); }
  function search(p,s,who,d,a,b){ if(d===0) return s[1]-s[0]; const L=legal(p,who); if(!L.length) return s[1]-s[0]+(who?-1:1)*p.reduce((x,y)=>x+y,0);
   if(who){ let v=-1e9; for(const i of L){ const r=sow(p,i,1); const ns=[s[0],s[1]+r.cap]; v=Math.max(v,search(r.b,ns,0,d-1,a,b)); a=Math.max(a,v); if(a>=b) break; } return v; }
   let v=1e9; for(const i of L){ const r=sow(p,i,0); const ns=[s[0]+r.cap,s[1]]; v=Math.min(v,search(r.b,ns,1,d-1,a,b)); b=Math.min(b,v); if(a>=b) break; } return v; }
  function ai(){ if(st.over) return; const L=legal(st.p,1); const depth=[2,4,7][ctx.diff||0]; let best=L[0],bv=-1e9; L.sort(()=>Math.random()-.5).forEach(i=>{ const r=sow(st.p,i,1); const v=search(r.b,[st.s[0],st.s[1]+r.cap],0,depth-1,-1e9,1e9); if(v>bv){ bv=v; best=i; } }); move(best,1); }
  function render(){ root.innerHTML=''; const B=h('div',{className:'owB'}); const can=st.turn===0&&!st.over?legal(st.p,0):[];
   const store=(who)=>{ const e=h('div',{className:'owS'},[String(st.s[who]),h('small',null,who?'computer':'you')]); return e; };
   B.appendChild(store(1)); for(let k=11;k>=6;k--){ const e=h('div',{className:'owP'+(st.last===k?' last':''),'aria-label':'computer pit '+(12-k)+': '+st.p[k]+' seeds'},[h('i'),String(st.p[k])]); B.appendChild(e); } const s0=store(0); s0.style.gridColumn='8'; s0.style.gridRow='1/3'; B.appendChild(s0);
   for(let k=0;k<6;k++){ const e=h('button',{type:'button',className:'owP mine'+(can.includes(k)?' can':'')+(st.last===k?' last':''),'aria-label':'your pit '+(k+1)+': '+st.p[k]+' seeds'},[h('i'),String(st.p[k])]); e.style.gridRow='2'; e.style.gridColumn=String(k+2); e.addEventListener('click',()=>{ if(can.includes(k)) move(k,0); else if(!st.over&&!st.turn) { st.msg=st.p[k]?'You must give the computer seeds: pick a pit that reaches its row.':'That pit is empty.'; render(); } }); B.appendChild(e); }
   root.appendChild(B); root.appendChild(h('div',{className:'k6Msg'},st.msg)); const b=bar(root); btn(b,'🔁 New game',deal); ctx.status(st.msg+' · You '+st.s[0]+' · Computer '+st.s[1]); }
  deal(); window.__kgst=()=>st; return {state:()=>st,api:{legal:w=>legal(st.p,w),move}};
 });

 /* ───────── THE ROYAL GAME OF UR ───────── */
 G.reg('b_ur','Royal Game of Ur',CAT,'The race game from ancient Mesopotamia, 4,500 years old. Each side has seven pieces to run along its own route: four squares on its own side, eight down the shared middle row and back onto its own side for two more, then off the board by an exact throw. Throw four tetrahedral dice: the marked tips showing (0 to 4) is your move. Land on an enemy piece in the middle row to send it home; you may not land on your own piece. The five rosettes give another throw, and the middle rosette is a safe square nobody can be knocked off. First to bring all seven home wins.',ctx=>{
  const O=OPT(ctx,'b_ur',[['pieces','Pieces each',[[3,'3 (quick)'],[4,'4'],[5,'5'],[6,'6'],[7,'7 (classic)']],7],['first','First move',FIRST,'me']]); let lastW=null;
  const ROS=new Set([4,8,14]); const N=()=>+O.pieces;
  const st={pc:[[],[]],turn:0,roll:null,dice:[],over:false,msg:'',can:[]};
  const root=h('div',{className:'k6'}); ctx.area.appendChild(root);
  /* cell of a route square p (1–14) for side who: row 0 is the computer's, 1 the shared middle, 2 yours */
  const cell=(p,who)=>{ if(p>=5&&p<=12) return [1,p-5]; const row=who?0:2; if(p<=4) return [row,4-p]; return [row,7-(p-13)]; };
  function deal(){ st.pc=[Array(N()).fill(0),Array(N()).fill(0)]; st.over=false; st.roll=null; st.turn=firstOf(O.first,lastW); st.msg=st.turn?'The computer throws first.':'Your turn: throw the dice.'; render(); if(st.turn) ctx.after(800,ai); }
  function throwD(){ st.dice=[0,0,0,0].map(()=>rnd(2)); st.roll=st.dice.reduce((a,b)=>a+b,0); beep(500,.03); }
  function moves(who,r){ if(!r) return []; const mine=st.pc[who], opp=st.pc[1-who]; const out=[]; mine.forEach((p,i)=>{ if(p===15) return; const t=p+r; if(t>15) return; if(t<15&&mine.some((q,j)=>j!==i&&q===t)) return; if(t===8&&opp.includes(8)) return; if(out.some(m=>m.from===p)) return; out.push({i,from:p,to:t}); }); return out; }
  function apply(who,m){ const opp=st.pc[1-who]; st.pc[who][m.i]=m.to; let note=''; if(m.to>=5&&m.to<=12){ const k=opp.indexOf(m.to); if(k>=0){ opp[k]=0; note=' and knocked a piece home'; beep(220,.12); } } beep(who?340:600);
   if(st.pc[who].every(p=>p===15)){ st.over=true; lastW=who; st.msg=who?'The computer brought all its pieces home. It wins.':'All your pieces are home: you win! 🎉'; render(); return; }
   const again=ROS.has(m.to); st.msg=(who?'The computer moved'+note:'You moved'+note)+(again?' and landed on a rosette: throw again.':'.'); st.roll=null; if(!again) st.turn=1-who; render(); if(st.turn===1) ctx.after(900,ai); }
  function pass(who){ st.msg=(who?'The computer':'You')+' threw '+st.roll+(st.roll?' but cannot move.':': no move.'); st.roll=null; st.turn=1-who; render(); if(st.turn===1) ctx.after(1100,ai); }
  function ai(){ if(st.over) return; throwD(); render(); ctx.after(700,()=>{ const M=moves(1,st.roll); if(!M.length) return pass(1); const opp=st.pc[0];
    const sc=m=>{ let v=m.to*0.3; if(m.to===15) v+=8; if(ROS.has(m.to)) v+=6; if(m.to>=5&&m.to<=12&&opp.includes(m.to)) v+=10; if(m.from>=5&&m.from<=12&&m.from!==8) v+=2; if(m.to>=5&&m.to<=12&&m.to!==8){ for(let d=1;d<=4;d++) if(opp.includes(m.to-d)) v-=2.5; } if(m.from===0) v+=1; return v+(ctx.diff===0?Math.random()*8:ctx.diff===1?Math.random()*3:0); };
    M.sort((a,b)=>sc(b)-sc(a)); apply(1,M[0]); }); }
  function render(){ root.innerHTML=''; const myM=st.turn===0&&st.roll!=null&&!st.over?moves(0,st.roll):[];
   const rack=(who,label)=>{ const r=h('div',{className:'urRack'}); r.appendChild(h('span',null,label+': '+st.pc[who].filter(p=>p===0).length+' waiting · '+st.pc[who].filter(p=>p===15).length+' home ')); st.pc[who].forEach((p,i)=>{ if(p!==0) return; const can=who===0&&myM.find(m=>m.from===0); const e=h('div',{className:'urPc p'+who+(can?' can':'')}); if(can) e.addEventListener('click',()=>apply(0,can)); r.appendChild(e); }); return r; };
   root.appendChild(rack(1,'🔵 Computer'));
   const B=h('div',{className:'urB'}); for(let row=0;row<3;row++) for(let col=0;col<8;col++){ const gap=row!==1&&(col===4||col===5); const ros=(row!==1&&(col===0||col===6))||(row===1&&col===3);
    const c=h('button',{type:'button',className:'urC'+(gap?' gap':'')+(ros?' ros':''),'aria-label':'square'}); if(!gap){ for(const who of [0,1]) st.pc[who].forEach(p=>{ if(p<1||p>14) return; const [r2,c2]=cell(p,who); if(r2===row&&c2===col) c.appendChild(h('div',{className:'urPc p'+who})); });
     const m=myM.find(m=>m.from>0&&m.from<15&&(()=>{ const [r2,c2]=cell(m.from,0); return r2===row&&c2===col; })()); if(m){ c.classList.add('can'); c.addEventListener('click',()=>apply(0,m)); } }
    B.appendChild(c); } root.appendChild(B); root.appendChild(rack(0,'🟡 You'));
   const D=h('div',{className:'dice'}); (st.dice.length?st.dice:[0,0,0,0]).forEach(x=>D.appendChild(h('span',{className:x?'on':''}))); root.appendChild(D);
   root.appendChild(h('div',{className:'k6Msg'},st.msg+(st.roll!=null?' · Throw: '+st.roll:''))); const b=bar(root);
   if(!st.over&&st.turn===0&&st.roll==null) btn(b,'🎲 Throw',()=>{ throwD(); const M=moves(0,st.roll); st.msg=M.length?'You threw '+st.roll+': tap a glowing piece.':''; if(!M.length){ render(); return ctx.after(900,()=>pass(0)); } if(M.length===1&&st.pc[0].filter(p=>p===0).length===N()) return apply(0,M[0]); render(); },'go');
   const off=myM.find(m=>m.to===15); if(off) btn(b,'🏠 Bring one home',()=>apply(0,off),'go');
   btn(b,'🔁 New game',deal); ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st,api:{moves,apply,throwD}};
 });

 /* ───────── SENET ───────── */
 G.reg('b_senet','Senet',CAT,'The board game of ancient Egypt: thirty squares in three rows, read like a snake (left to right, then right to left, then left to right). Each side has five pieces, set out alternately on the first ten squares. Throw the four sticks: the white faces showing count 1 to 4, and none showing counts 5. A throw of 1, 4 or 5 earns another throw. Move one piece forward that many squares. Land on a lone enemy piece to swap places with it; two of a kind side by side protect each other, and three in a row also block anyone from passing. Square 15 is the House of Rebirth. Every piece must stop on square 26, the House of Happiness, before going on. From 26: a 1 falls into the Water (27) and goes back to 15; a 2, 3 or 4 moves to 28, 29 or 30; a 5 bears the piece off. From 28, 29 or 30 a piece leaves with exactly 3, 2 or 1. First to bear off all five wins.',ctx=>{
  const O=OPT(ctx,'b_senet',[['first','First throw',FIRST,'me'],['pieces','Pieces each',[[3,'3 (quick)'],[4,'4'],[5,'5 (classic)'],[6,'6'],[7,'7 (long)']],5]]); let lastW=null;
  const st={b:Array(31).fill(-1),off:[0,0],turn:0,roll:null,sticks:[],over:false,msg:''};
  const root=h('div',{className:'k6'}); ctx.area.appendChild(root);
  const GLY={15:'☥',26:'✶',27:'≈',28:'Ⅲ',29:'Ⅱ',30:'☀'};
  function deal(){ st.b=Array(31).fill(-1); const n=+O.pieces; for(let k=0;k<2*n;k++) st.b[k+1]=k%2; st.off=[0,0]; st.over=false; st.roll=null; st.turn=firstOf(O.first,lastW); st.msg=st.turn?'The computer throws first.':'Your turn: throw the sticks.'; render(); if(st.turn) ctx.after(800,ai); }
  function throwS(){ st.sticks=[0,0,0,0].map(()=>rnd(2)); const w=st.sticks.reduce((a,b)=>a+b,0); st.roll=w||5; beep(480,.03); }
  const guarded=(sq,who)=>(st.b[sq-1]===who)||(st.b[sq+1]===who&&sq+1<=30);
  function blocked(from,to,opp){ for(let s=from+1;s<to-1;s++){ if(st.b[s]===opp&&st.b[s+1]===opp&&st.b[s+2]===opp) return true; } return false; }
  function target(from,r){ if(from<26){ const t=from+r; if(t>26) return null; return t; } if(from===26){ return r===5?31:26+r; } const need={28:3,29:2,30:1}[from]; return r===need?31:null; }
  function moves(who,r){ const out=[], opp=1-who; for(let s=1;s<=30;s++){ if(st.b[s]!==who) continue; const t=target(s,r); if(t==null) continue; if(t===31){ out.push({from:s,to:31}); continue; } if(s<26&&t>26) continue; if(st.b[t]===who) continue; if(st.b[t]===opp&&(guarded(t,opp)||t===26||t>26)) continue; if(blocked(s,t+1,opp)) continue; out.push({from:s,to:t}); } return out; }
  function apply(who,m){ const opp=1-who; let note=''; st.b[m.from]=-1;
   if(m.to===31){ st.off[who]++; note=' bore a piece off'; beep(880,.1); }
   else if(m.to===27){ let r=15; while(st.b[r]!==-1&&r>1) r--; st.b[r]=who; note=' fell into the Water and went back to '+r; beep(200,.15); }
   else { if(st.b[m.to]===opp){ st.b[m.from]=opp; note=' swapped places with an enemy piece'; } st.b[m.to]=who; beep(who?340:600); }
   if(st.off[who]>=+O.pieces){ st.over=true; lastW=who; st.msg=who?'The computer bore off all its pieces. It wins.':'All your pieces are borne off: you win! 🎉'; render(); return; }
   const again=[1,4,5].includes(st.roll); st.msg=(who?'The computer':'You')+note+'.'+(again?' Another throw.':''); st.roll=null; if(!again) st.turn=opp; render(); if(st.turn===1) ctx.after(900,ai); }
  function pass(who){ st.msg=(who?'The computer':'You')+' threw '+st.roll+' and cannot move.'; st.roll=null; st.turn=1-who; render(); if(st.turn===1) ctx.after(1100,ai); }
  function ai(){ if(st.over) return; throwS(); render(); ctx.after(700,()=>{ const M=moves(1,st.roll); if(!M.length) return pass(1);
    const sc=m=>{ let v=m.to; if(m.to===31) v+=40; if(m.to===27) v-=30; if(st.b[m.to]===0) v+=12; if(m.to===26) v+=8; if(guarded(m.to,1)) v+=3; if(m.from<=10) v+=1; return v+(ctx.diff===0?Math.random()*15:ctx.diff===1?Math.random()*5:0); };
    M.sort((a,b)=>sc(b)-sc(a)); apply(1,M[0]); }); }
  const pos=s=>{ const row=Math.floor((s-1)/10), k=(s-1)%10; return [row,row===1?9-k:k]; };
  function render(){ root.innerHTML=''; const myM=st.turn===0&&st.roll!=null&&!st.over?moves(0,st.roll):[]; const B=h('div',{className:'snB'}); const cells=[];
   for(let s=1;s<=30;s++){ const [r,c]=pos(s); const m=myM.find(x=>x.from===s); const e=h('button',{type:'button',className:'snC'+(m?' can':''),'aria-label':'square '+s},[h('small',null,String(s)),GLY[s]||'']); e.style.gridRow=String(r+1); e.style.gridColumn=String(c+1); if(st.b[s]>=0){ e.textContent=''; e.appendChild(h('small',null,String(s))); e.appendChild(h('div',{className:'snPc p'+st.b[s]})); } if(m) e.addEventListener('click',()=>apply(0,m)); B.appendChild(e); }
   root.appendChild(B); const S=h('div',{className:'sticks'}); (st.sticks.length?st.sticks:[0,0,0,0]).forEach(x=>S.appendChild(h('span',{className:x?'w':''}))); root.appendChild(S);
   root.appendChild(h('div',{className:'k6Msg'},st.msg+(st.roll!=null?' · Throw: '+st.roll:'')+' · Off: you '+st.off[0]+', computer '+st.off[1])); const b=bar(root);
   if(!st.over&&st.turn===0&&st.roll==null) btn(b,'🪵 Throw the sticks',()=>{ throwS(); const M=moves(0,st.roll); st.msg=M.length?'You threw '+st.roll+': tap a glowing piece.':''; if(!M.length){ render(); return ctx.after(900,()=>pass(0)); } render(); },'go');
   btn(b,'🔁 New game',deal); ctx.status(st.msg); }
  deal(); window.__kgst=()=>st; return {state:()=>st,api:{moves,apply,throwS}};
 });
})();
