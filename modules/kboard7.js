(()=>{ /* ♞ CHESS VARIANTS, INTERNATIONAL DRAUGHTS AND TABLUT (v225): Chess960 (Fischer random), King of the Hill and Three-Check on
   one variant chess engine (castling generalised for any back rank), 10×10 international draughts with flying kings and the
   majority-capture rule, and Tablut (Linnaeus' Lapland tafl). All against the computer; traditional public-domain rules. */
 const G=window.GAMES; if(!G||!G.reg||!G.lib) return; const L=G.lib, h=L.h; const CAT='Board';
 const OPT=(ctx,id,defs)=>window.KGOPT?KGOPT.row(ctx,id,defs):Object.fromEntries(defs.map(d=>[d[0],d[3]]));
 const beep=(f,d)=>{ try{ L.beep(f,d||.04); }catch(_){ } }; const rnd=n=>Math.floor(Math.random()*n);
 const css=document.createElement('style'); css.textContent=`
#gamesDock .k7{width:100%;max-width:640px;margin:0 auto;display:flex;flex-direction:column;gap:8px;align-items:center;color:#fff;font:700 14px system-ui,sans-serif}
#gamesDock .k7B{display:grid;width:100%;border:4px solid #3b2a16;border-radius:6px;overflow:hidden;box-shadow:0 6px 18px rgba(0,0,0,.5)}
#gamesDock .k7C{aspect-ratio:1;display:flex;align-items:center;justify-content:center;position:relative;padding:0!important;min-height:0!important;border:0!important;border-radius:0!important;font:400 clamp(20px,7vw,46px)/1 "Segoe UI Symbol","Noto Sans Symbols 2","DejaVu Sans",serif;cursor:pointer}
#gamesDock .k7C.l{background:#eed9b6!important}#gamesDock .k7C.d{background:#a87b4f!important}
#gamesDock .k7C.sel{box-shadow:inset 0 0 0 4px #ffe94a}#gamesDock .k7C.last{box-shadow:inset 0 0 0 4px rgba(124,255,138,.75)}#gamesDock .k7C.chk{background:radial-gradient(circle,#ff4f6a 0 40%,transparent 70%)!important}
#gamesDock .k7C .dot{position:absolute;width:28%;height:28%;border-radius:50%;background:rgba(20,120,40,.55)}#gamesDock .k7C .cap{position:absolute;inset:6%;border-radius:50%;border:4px solid rgba(20,120,40,.6)}
#gamesDock .k7C .pw{color:#fff;text-shadow:0 0 2px #000,0 0 2px #000,0 1px 0 #000}#gamesDock .k7C .pb{color:#111;text-shadow:0 0 2px #fff8}
#gamesDock .k7C.hill{outline:3px dashed rgba(255,233,74,.7);outline-offset:-5px}
#gamesDock .k7Bar{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}#gamesDock .k7Bar button{min-height:44px;padding:0 14px;border-radius:12px;font:800 14px system-ui,sans-serif}
#gamesDock .k7Msg{min-height:1.5em;text-align:center;color:#ffe9b0}
#gamesDock .dr{width:78%;height:78%;border-radius:50%;border:3px solid rgba(0,0,0,.35);box-shadow:0 3px 0 rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;font:900 clamp(10px,3vw,20px) system-ui}
#gamesDock .dr.w{background:radial-gradient(circle at 35% 30%,#fff,#d8d0c0);color:#a0702a}#gamesDock .dr.b{background:radial-gradient(circle at 35% 30%,#555,#111);color:#ffe94a}
#gamesDock .k7C.tf{background:#d9c49a!important;outline:1px solid rgba(0,0,0,.15)}#gamesDock .k7C.throne{background:#b8955f!important}#gamesDock .k7C.edge{background:#e6d6b0!important}
#gamesDock .tfP{width:72%;height:72%;border-radius:50%;border:2px solid #000;display:flex;align-items:center;justify-content:center;font:900 clamp(12px,3.6vw,24px) system-ui}
#gamesDock .tfP.a{background:#2b2b2b;color:#fff}#gamesDock .tfP.d{background:#f4efe2;color:#222}#gamesDock .tfP.k{background:radial-gradient(circle,#ffe94a,#c9a20c);color:#3a2a00}`; document.head.appendChild(css);
 const bar=(root)=>{ const b=h('div',{className:'k7Bar'}); root.appendChild(b); return b; };
 const btn=(b,l,f,c)=>{ const e=h('button',{type:'button',className:c||''},l); e.addEventListener('click',f); b.appendChild(e); return e; };

 /* ───────── the variant chess engine ───────── */
 const CV=(()=>{ const KN=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]],KG=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]],BD=[[-1,-1],[-1,1],[1,-1],[1,1]],RD=[[-1,0],[1,0],[0,-1],[0,1]],V={p:100,n:320,b:330,r:500,q:900,k:0};
  const W=p=>p!=='.'&&p<'a', on=(r,c)=>r>=0&&r<8&&c>=0&&c<8;
  function init(rank){ const back=rank||'rnbqkbnr'; const b=(back+'pppppppp'+'.'.repeat(32)+'PPPPPPPP'+back.toUpperCase()).split(''); const kf=back.indexOf('k'), r1=back.indexOf('r'), r2=back.lastIndexOf('r');
   return {b,w:true,cr:{K:56+r2,Q:56+r1,k:r2,q:r1},kf,ep:-1,hm:0,fm:1,chk:{w:0,b:0}}; }
  function attacked(b,sq,byW){ const r=sq>>3,c=sq&7; const pr=byW?r+1:r-1; if(pr>=0&&pr<8) for(const d of [-1,1]){ const cc=c+d; if(cc>=0&&cc<8&&b[pr*8+cc]===(byW?'P':'p')) return true; }
   for(const [dr,dc] of KN){ const rr=r+dr,cc=c+dc; if(on(rr,cc)&&b[rr*8+cc]===(byW?'N':'n')) return true; } for(const [dr,dc] of KG){ const rr=r+dr,cc=c+dc; if(on(rr,cc)&&b[rr*8+cc]===(byW?'K':'k')) return true; }
   const Bq=byW?'B':'b',Rq=byW?'R':'r',Q=byW?'Q':'q'; for(const [dr,dc] of BD){ let rr=r+dr,cc=c+dc; while(on(rr,cc)){ const p=b[rr*8+cc]; if(p!=='.'){ if(p===Bq||p===Q) return true; break; } rr+=dr; cc+=dc; } }
   for(const [dr,dc] of RD){ let rr=r+dr,cc=c+dc; while(on(rr,cc)){ const p=b[rr*8+cc]; if(p!=='.'){ if(p===Rq||p===Q) return true; break; } rr+=dr; cc+=dc; } } return false; }
  const kingSq=(b,w)=>b.indexOf(w?'K':'k'); const inCheck=(s,w)=>attacked(s.b,kingSq(s.b,w),!w);
  function castles(s,ms){ const w=s.w, b=s.b, ks=kingSq(b,w), row=w?56:0; if(ks<0||ks!==row+s.kf||attacked(b,ks,!w)) return;
   for(const side of ['K','Q']){ const key=w?side:side.toLowerCase(); const rs=s.cr[key]; if(rs<0||b[rs]!==(w?'R':'r')) continue; const kd=row+(side==='K'?6:2), rd=row+(side==='K'?5:3);
    const lo=Math.min(ks,rs,kd,rd), hi=Math.max(ks,rs,kd,rd); let ok=true; for(let q=lo;q<=hi;q++){ if(q!==ks&&q!==rs&&b[q]!=='.'){ ok=false; break; } } if(!ok) continue;
    const a=Math.min(ks,kd), z=Math.max(ks,kd); for(let q=a;q<=z;q++){ if(attacked(b,q,!w)){ ok=false; break; } } if(ok) ms.push({f:ks,t:rs,c:side,kd,rd,rs}); } }
  function pseudo(s){ const b=s.b,w=s.w,ms=[]; const addP=(f,t,r1)=>{ if(r1===0||r1===7) 'qrbn'.split('').forEach(x=>ms.push({f,t,p:w?x.toUpperCase():x})); else ms.push({f,t}); };
   for(let sq=0;sq<64;sq++){ const p=b[sq]; if(p==='.'||W(p)!==w) continue; const t=p.toLowerCase(), r=sq>>3, c=sq&7;
    if(t==='p'){ const dir=w?-1:1, r1=r+dir; if(r1>=0&&r1<8&&b[r1*8+c]==='.'){ addP(sq,r1*8+c,r1); if(r===(w?6:1)&&b[(r+2*dir)*8+c]==='.') ms.push({f:sq,t:(r+2*dir)*8+c,dbl:1}); }
     for(const d of [-1,1]){ const cc=c+d; if(cc<0||cc>7||r1<0||r1>7) continue; const to=r1*8+cc, q=b[to]; if(q!=='.'&&W(q)!==w) addP(sq,to,r1); else if(to===s.ep) ms.push({f:sq,t:to,e:1}); } }
    else if(t==='n'||t==='k'){ for(const [dr,dc] of (t==='n'?KN:KG)){ const rr=r+dr,cc=c+dc; if(!on(rr,cc)) continue; const q=b[rr*8+cc]; if(q==='.'||W(q)!==w) ms.push({f:sq,t:rr*8+cc}); } }
    else { const D=t==='b'?BD:t==='r'?RD:BD.concat(RD); for(const [dr,dc] of D){ let rr=r+dr,cc=c+dc; while(on(rr,cc)){ const q=b[rr*8+cc]; if(q==='.') ms.push({f:sq,t:rr*8+cc}); else { if(W(q)!==w) ms.push({f:sq,t:rr*8+cc}); break; } rr+=dr; cc+=dc; } } } }
   castles(s,ms); return ms; }
  function make(s,m){ const b=s.b.slice(), w=s.w, p=b[m.f], cr={...s.cr}; let cap=b[m.t];
   if(m.c){ b[m.f]='.'; b[m.rs]='.'; b[m.kd]=w?'K':'k'; b[m.rd]=w?'R':'r'; cap='.'; }
   else { b[m.t]=m.p||p; b[m.f]='.'; if(m.e){ b[m.t+(w?8:-8)]='.'; cap=w?'p':'P'; } }
   if(p==='K'){ cr.K=-1; cr.Q=-1; } if(p==='k'){ cr.k=-1; cr.q=-1; } for(const k of ['K','Q','k','q']) if(cr[k]===m.f||cr[k]===m.t&&!m.c) cr[k]=-1;
   const n={b,w:!w,cr,kf:s.kf,ep:m.dbl?(m.f+m.t)/2:-1,hm:(p==='P'||p==='p'||cap!=='.')?0:s.hm+1,fm:s.fm+(w?0:1),chk:{...s.chk}}; if(attacked(b,kingSq(b,!w),w)) n.chk[w?'w':'b']++; return n; }
  const legal=s=>pseudo(s).filter(m=>{ const n=make(s,m); return !attacked(n.b,kingSq(n.b,s.w),n.w); });
  const HILL=[27,28,35,36];
  function won(s,variant){ /* who has won by the variant's own goal (the side that just moved is !s.w) */ if(variant==='koth'){ if(HILL.includes(kingSq(s.b,true))) return 'w'; if(HILL.includes(kingSq(s.b,false))) return 'b'; } if(variant==='3check'){ if(s.chk.w>=3) return 'w'; if(s.chk.b>=3) return 'b'; } return null; }
  function evalW(s,variant){ const b=s.b; let v=0; for(let i=0;i<64;i++){ const p=b[i]; if(p==='.') continue; const t=p.toLowerCase(), w=p<'a', r=i>>3, c=i&7; let x=V[t]; const cd=Math.abs(3.5-r)+Math.abs(3.5-c), adv=w?(6-r):(r-1);
    if(t==='n'||t==='b') x+=(7-cd)*6; else if(t==='p') x+=adv*7+((c>=2&&c<=5)?adv*4:0); else if(t==='q') x+=(7-cd)*2; else if(t==='k'){ if(variant==='koth') x+=(7-cd)*28; else x+=w?(r===7?12:-12*(7-r)):(r===0?12:-12*r); }
    v+=w?x:-x; } if(variant==='3check') v+=(s.chk.w-s.chk.b)*170; return v; }
  function search(s,d,a,bt,ply,variant){ const wn=won(s,variant); if(wn) return ((wn==='w')===s.w?1:-1)*(90000-ply); if(d<=0) return (s.w?1:-1)*evalW(s,variant);
   const Lg=legal(s); if(!Lg.length) return inCheck(s,s.w)?-100000+ply:0; if(s.hm>=100) return 0;
   Lg.sort((x,y)=>(s.b[y.t]!=='.')-(s.b[x.t]!=='.')); for(const m of Lg){ const v=-search(make(s,m),d-1,-bt,-a,ply+1,variant); if(v>a) a=v; if(a>=bt) break; } return a; }
  function best(s,depth,variant){ const Lg=legal(s).sort(()=>Math.random()-.5); let bm=null,a=-1e9; for(const m of Lg){ const v=-search(make(s,m),depth-1,-1e9,-a,1,variant); if(v>a||!bm){ a=v; bm=m; } } return bm; }
  function status(s,variant){ const wn=won(s,variant); if(wn) return 'won-'+wn; const Lg=legal(s); if(!Lg.length) return inCheck(s,s.w)?'mate':'stalemate'; if(s.hm>=100) return 'fifty'; return inCheck(s,s.w)?'check':''; }
  return {init,legal,make,status,best,inCheck,HILL}; })();
 function rank960(){ const a=Array(8).fill(''); const ev=[0,2,4,6], od=[1,3,5,7]; a[ev[rnd(4)]]='b'; a[od[rnd(4)]]='b'; const free=()=>a.map((x,i)=>x?-1:i).filter(i=>i>=0); let f=free(); a[f[rnd(f.length)]]='q'; f=free(); a[f.splice(rnd(f.length),1)[0]]='n'; f=free(); a[f[rnd(f.length)]]='n'; f=free(); a[f[0]]='r'; a[f[1]]='k'; a[f[2]]='r'; return a.join(''); }
 const GLY={k:'♚',q:'♛',r:'♜',b:'♝',n:'♞',p:'♟'};
 const SIDES=[['w','White (you move first)'],['b','Black'],['rand','Random colour'],['hot','Two players on this device'],['watch','Watch the computer play itself']];
 function humans(o,coin){ if(o==='hot') return {w:true,b:true}; if(o==='watch') return {w:false,b:false}; const w=o==='w'||(o==='rand'&&coin); return {w,b:!w}; }
 function chessGame(ctx,variant,id){
  const O=OPT(ctx,id,[['side','Who plays',SIDES,'w']].concat(variant==='960'?[['pos','Start position',[['random','A new random one'],['same','The same as last time'],['classic','The classic position (518)'],['bbqnnrkr','BBQNNRKR (position 0)'],['rkrnnqbb','RKRNNQBB (position 959)']],'random']]:[]));
  let st=null, sel=null, last=null, over=false, msg='', lastRank=null, busy=false, H={w:true,b:false};
  const root=h('div',{className:'k7'}); ctx.area.appendChild(root); const isH=w=>w?H.w:H.b; const flip=()=>!H.w&&H.b;
  function newGame(){ H=humans(O.side,Math.random()<.5); let rank='rnbqkbnr'; if(variant==='960'){ if(O.pos==='random'||(O.pos==='same'&&!lastRank)) lastRank=rank960(); else if(O.pos==='classic') lastRank='rnbqkbnr'; else if(O.pos!=='same') lastRank=O.pos; rank=lastRank; }
   st=CV.init(rank); sel=null; last=null; over=false; msg=variant==='960'?'Back rank: '+rank.toUpperCase().split('').join(' ')+'. ':''; msg+=H.w&&H.b?'Two players: White moves first.':!H.w&&!H.b?'The computer plays both sides.':H.w?'You are White: your move.':'You are Black: the computer opens.'; render(); if(!isH(true)) ctx.after(600,ai); }
  const goal={'960':'Checkmate the king. To castle, tap your king, then the rook.','koth':'Checkmate, or walk your king onto one of the four centre squares (the hill) to win.','3check':'Checkmate, or give check three times to win.'}[variant];
  const who=w=>H.w&&H.b?(w?'White':'Black'):!H.w&&!H.b?(w?'White':'Black'):(isH(w)?'You':'The computer');
  function after(m){ last=m; const mover=!st.w; const s=CV.status(st,variant); beep(isH(mover)?560:330);
   if(s.startsWith('won-')){ over=true; const w=s.slice(4)==='w'; msg=who(w)+(H.w!==H.b?(isH(w)?' win':' wins'):' wins')+(variant==='koth'?' by reaching the hill!':' with the third check!')+(isH(w)&&H.w!==H.b?' 🎉':''); }
   else if(s==='mate'){ over=true; const w=!st.w; msg='Checkmate. '+who(w)+(H.w!==H.b&&isH(w)?' win! 🎉':' wins.'); } else if(s==='stalemate'){ over=true; msg='Stalemate: a draw.'; } else if(s==='fifty'){ over=true; msg='Fifty moves without a capture or pawn move: a draw.'; }
   else msg=(s==='check'?'Check! ':'')+(isH(st.w)?(H.w&&H.b?(st.w?'White':'Black')+' to move.':'Your move.'):'The computer thinks…');
   render(); if(!over&&!isH(st.w)) ctx.after(H.w||H.b?350:700,ai); }
  function ai(){ if(over) return; busy=true; render(); setTimeout(()=>{ const m=CV.best(st,[1,2,3][ctx.diff||0],variant); busy=false; if(!m) return; st=CV.make(st,m); after(m); },30); }
  function tap(sq){ if(over||busy||!isH(st.w)) return; const mine=p=>p!=='.'&&(p<'a')===st.w; if(sel!=null){ const Lg=CV.legal(st).filter(m=>m.f===sel&&m.t===sq); if(Lg.length){ const m=Lg.find(x=>!x.p||x.p.toLowerCase()==='q')||Lg[0]; st=CV.make(st,m); sel=null; return after(m); } } sel=mine(st.b[sq])?sq:null; render(); }
  function render(){ root.innerHTML=''; const B=h('div',{className:'k7B',style:'grid-template-columns:repeat(8,minmax(0,1fr))'}); const Lg=sel!=null?CV.legal(st).filter(m=>m.f===sel):[]; const ck=!over&&CV.inCheck(st,st.w)?st.b.indexOf(st.w?'K':'k'):-1;
   for(let i=0;i<64;i++){ const sq=flip()?63-i:i; const r=sq>>3,c=sq&7; const p=st.b[sq]; const e=h('button',{type:'button',className:'k7C '+((r+c)%2?'d':'l')+(sel===sq?' sel':'')+(last&&(last.f===sq||last.t===sq||last.kd===sq)?' last':'')+(sq===ck?' chk':'')+(variant==='koth'&&CV.HILL.includes(sq)?' hill':''),'aria-label':'abcdefgh'[c]+(8-r)+(p!=='.'?' '+p:'')});
    if(p!=='.') e.appendChild(h('span',{className:p<'a'?'pw':'pb'},GLY[p.toLowerCase()])); const tg=Lg.find(m=>m.t===sq); if(tg) e.appendChild(h('i',{className:p!=='.'&&!tg.c?'cap':'dot'})); e.addEventListener('click',()=>tap(sq)); B.appendChild(e); }
   root.appendChild(B); root.appendChild(h('div',{className:'k7Msg'},msg)); if(variant==='3check') root.appendChild(h('div',{className:'k7Msg'},'Checks given · White '+st.chk.w+' / 3 · Black '+st.chk.b+' / 3'));
   const b=bar(root); btn(b,'🔁 New game',newGame); ctx.status(goal+' '+msg); }
  newGame(); window.__kgst=()=>({st,over,msg,H}); return {state:()=>({st,over}),api:{CV,tap,get st(){ return st; }}}; }
 G.reg('b_chess960','Chess960 (Fischer Random)',CAT,'Chess with the pieces on the back rank shuffled: bishops on opposite colours, the king somewhere between the two rooks, the pawns where they always are. Black mirrors White. All the usual rules apply, and castling still works: the king ends on the g-file (short) or c-file (long) with the rook beside it, as long as every square they cross is empty and the king does not pass through check. To castle, tap your king, then the rook. 960 possible starting positions: opening theory goes out of the window.',ctx=>chessGame(ctx,'960','b_chess960'));
 G.reg('b_koth','King of the Hill',CAT,'Ordinary chess with one more way to win: bring your king onto one of the four centre squares (d4, e4, d5, e5: the hill, outlined) and you win at once, as long as the move is legal. Checkmate still wins too. Kings become fighters; guard the centre.',ctx=>chessGame(ctx,'koth','b_koth'));
 G.reg('b_3check','Three-Check',CAT,'Ordinary chess with one more way to win: give check three times. The counter under the board shows every check given; the third one wins the game on the spot. Checkmate still wins too. Keep your king safe from even harmless-looking checks.',ctx=>chessGame(ctx,'3check','b_3check'));

 /* ───────── INTERNATIONAL DRAUGHTS (10×10) ───────── */
 const DR=(()=>{ const D4=[[-1,-1],[-1,1],[1,-1],[1,1]]; const on=(r,c)=>r>=0&&r<10&&c>=0&&c<10;
  function init(){ const b=Array(100).fill(0); for(let r=0;r<10;r++) for(let c=0;c<10;c++){ if((r+c)%2===0) continue; if(r<4) b[r*10+c]=-1; else if(r>5) b[r*10+c]=1; } return {b,turn:1}; }
  /* pieces: 1 white man, 2 white king, -1 black man, -2 black king; white moves up (row decreasing) */
  function caps(b,sq,side,king,taken,path){ const out=[]; const r=sq/10|0,c=sq%10;
   for(const [dr,dc] of D4){ if(king){ let rr=r+dr,cc=c+dc; while(on(rr,cc)&&b[rr*10+cc]===0){ rr+=dr; cc+=dc; } if(!on(rr,cc)) continue; const mid=rr*10+cc; if(Math.sign(b[mid])!==-side||taken.includes(mid)) continue; let lr=rr+dr,lc=cc+dc; while(on(lr,lc)&&b[lr*10+lc]===0){ const to=lr*10+lc; const nb=b.slice(); nb[to]=nb[sq]; nb[sq]=0; const more=caps(nb,to,side,true,taken.concat([mid]),path.concat([to])); if(more.length) out.push(...more); else out.push({path:path.concat([to]),taken:taken.concat([mid])}); lr+=dr; lc+=dc; } }
    else { const mr=r+dr,mc=c+dc, lr=r+2*dr,lc=c+2*dc; if(!on(lr,lc)) continue; const mid=mr*10+mc, to=lr*10+lc; if(Math.sign(b[mid])!==-side||taken.includes(mid)||b[to]!==0) continue; const nb=b.slice(); nb[to]=nb[sq]; nb[sq]=0; const more=caps(nb,to,side,false,taken.concat([mid]),path.concat([to])); if(more.length) out.push(...more); else out.push({path:path.concat([to]),taken:taken.concat([mid])}); } }
   return out; }
  function moves(s){ const b=s.b, side=s.turn; let C=[]; for(let sq=0;sq<100;sq++){ if(Math.sign(b[sq])!==side) continue; const king=Math.abs(b[sq])===2; caps(b,sq,side,king,[],[sq]).forEach(x=>C.push(x)); }
   if(C.length){ const mx=Math.max(...C.map(x=>x.taken.length)); return C.filter(x=>x.taken.length===mx).map(x=>({f:x.path[0],t:x.path[x.path.length-1],path:x.path,taken:x.taken})); }
   const M=[]; for(let sq=0;sq<100;sq++){ if(Math.sign(b[sq])!==side) continue; const r=sq/10|0,c=sq%10, king=Math.abs(b[sq])===2; for(const [dr,dc] of D4){ if(!king&&dr!==-side) continue; let rr=r+dr,cc=c+dc; while(on(rr,cc)&&b[rr*10+cc]===0){ M.push({f:sq,t:rr*10+cc,path:[sq,rr*10+cc],taken:[]}); if(!king) break; rr+=dr; cc+=dc; } } } return M; }
  function make(s,m){ const b=s.b.slice(); const p=b[m.f]; b[m.f]=0; m.taken.forEach(q=>b[q]=0); let np=p; const r=m.t/10|0; if(p===1&&r===0) np=2; if(p===-1&&r===9) np=-2; b[m.t]=np; return {b,turn:-s.turn}; }
  const evalB=b=>b.reduce((a,v,i)=>a+(v===1?100+(9-(i/10|0))*2:v===2?320:v===-1?-100-(i/10|0)*2:v===-2?-320:0),0);
  function search(s,d,a,bt){ const M=moves(s); if(!M.length) return -100000; if(d<=0) return s.turn*evalB(s.b); for(const m of M){ const v=-search(make(s,m),d-1,-bt,-a); if(v>a) a=v; if(a>=bt) break; } return a; }
  function best(s,d){ const M=moves(s).sort(()=>Math.random()-.5); let bm=M[0],a=-1e9; for(const m of M){ const v=-search(make(s,m),d-1,-1e9,-a); if(v>a){ a=v; bm=m; } } return bm; }
  return {init,moves,make,best}; })();
 G.reg('b_draughts10','International Draughts (10×10)',CAT,'The world championship form of checkers, on a 10×10 board with twenty pieces each. Men move one square diagonally forward but capture forwards and backwards. Capturing is compulsory and you must take the largest number of pieces possible; jump on in one turn while you can (captured pieces come off at the end of the move). A man that ends its move on the far row becomes a king, and kings fly: they move and capture any distance along a diagonal. You win when the computer has no piece left or no move. Tap a piece, then where it should end.',ctx=>{
  const O=OPT(ctx,'b_draughts10',[['side','Who plays',SIDES,'w']]);
  let st=null, sel=null, last=null, over=false, msg='', busy=false, H={w:true,b:false}; const isH=t=>t===1?H.w:H.b; let me=1; const root=h('div',{className:'k7'}); ctx.area.appendChild(root);
  function newGame(){ H=humans(O.side,Math.random()<.5); me=H.w?1:-1; st=DR.init(); sel=null; last=null; over=false; msg=H.w&&H.b?'Two players: White moves first.':!H.w&&!H.b?'The computer plays both sides.':H.w?'You are White: your move.':'You are Black: the computer opens.'; render(); if(!isH(1)) ctx.after(600,ai); }
  function after(m,who){ last=m; beep(who?330:560); st=DR.make(st,m); const M=DR.moves(st); const nm=t=>t===1?'White':'Black'; if(!M.length){ over=true; const loser=st.turn; msg=H.w!==H.b?(isH(loser)?'You have no move left: the computer wins.':'The computer has no move left: you win! 🎉'):nm(loser)+' has no move left: '+nm(-loser)+' wins.'; }
   else msg=(m.taken.length?nm(-st.turn)+' took '+m.taken.length+'. ':'')+(isH(st.turn)?(M[0].taken.length?'Capture '+M[0].taken.length+' (the most possible).':(H.w&&H.b?nm(st.turn)+' to move.':'Your move.')):'The computer thinks…'); render(); if(!over&&!isH(st.turn)) ctx.after(H.w||H.b?350:700,ai); }
  function ai(){ if(over) return; busy=true; setTimeout(()=>{ const m=DR.best(st,[1,3,4][ctx.diff||0]); busy=false; if(m) after(m,1); },30); }
  function tap(sq){ if(over||busy||!isH(st.turn)) return; const M=DR.moves(st); if(sel!=null){ const m=M.find(x=>x.f===sel&&x.t===sq); if(m){ sel=null; return after(m,0); } } sel=M.some(x=>x.f===sq)?sq:null; if(sel==null&&Math.sign(st.b[sq])===st.turn) msg=M[0]&&M[0].taken.length?'You must capture (the most pieces possible).':'That piece cannot move.'; render(); }
  function render(){ root.innerHTML=''; const B=h('div',{className:'k7B',style:'grid-template-columns:repeat(10,minmax(0,1fr))'}); const M=sel!=null?DR.moves(st).filter(m=>m.f===sel):[]; const movable=new Set(isH(st.turn)&&!over?DR.moves(st).map(m=>m.f):[]);
   for(let i=0;i<100;i++){ const sq=me===1?i:99-i; const r=sq/10|0,c=sq%10, v=st.b[sq]; const e=h('button',{type:'button',className:'k7C '+((r+c)%2?'d':'l')+(sel===sq?' sel':'')+(last&&(last.f===sq||last.t===sq)?' last':''),'aria-label':'square '+(sq+1)});
    if(v){ const d=h('div',{className:'dr '+(v>0?'w':'b')},Math.abs(v)===2?'♛':''); if(movable.has(sq)&&sel==null) d.style.boxShadow='0 0 0 3px #7cff8a'; e.appendChild(d); } if(M.some(m=>m.t===sq)) e.appendChild(h('i',{className:'dot'})); if((r+c)%2) e.addEventListener('click',()=>tap(sq)); B.appendChild(e); }
   root.appendChild(B); root.appendChild(h('div',{className:'k7Msg'},msg)); const cnt=s=>st.b.filter(v=>Math.sign(v)===s).length; root.appendChild(h('div',{className:'k7Msg'},'Pieces · White '+cnt(1)+' · Black '+cnt(-1))); const b=bar(root); btn(b,'🔁 New game',newGame); ctx.status(msg); }
  newGame(); window.__kgst=()=>({st,over,msg}); return {state:()=>({st,over})};
 });

 /* ───────── TABLUT ───────── */
 G.reg('b_tablut','Tablut',CAT,'The tafl game Linnaeus recorded in Lapland in 1732, on a 9×9 board. The king starts on the central throne with eight defenders; sixteen attackers wait in T-shapes at the edges, and they move first. Every piece moves like a chess rook, any distance in a straight line; only the king may stop on the throne. Capture an enemy piece by sandwiching it between two of yours on a row or column (the empty throne counts as hostile). The defenders win when the king reaches any edge square; the attackers win by surrounding the king on all four sides (three and the throne when he stands beside it), or when the defenders cannot move.',ctx=>{
  const O=OPT(ctx,'b_tablut',[['side','Who plays',[['d','You: the king’s defenders'],['a','You: the attackers (move first)'],['rand','Random side'],['hot','Two players on this device'],['watch','Watch the computer play itself']],'d']]);
  const N=9, TH=40; let me='d', H={a:false,d:true}; const isH=t=>H[t]; const root=h('div',{className:'k7'}); ctx.area.appendChild(root); let st=null, sel=null, over=false, msg='', busy=false, last=null;
  function init(){ const b=Array(81).fill(''); const A=[3,4,5,13,27,36,45,37,35,44,53,43,75,76,77,67]; A.forEach(i=>b[i]='a'); [22,31,38,39,41,42,49,58].forEach(i=>b[i]='d'); b[TH]='k'; return {b,turn:'a'}; }
  const side=p=>p==='a'?'a':p?'d':'';
  const isEdge=i=>{ const r=i/9|0,c=i%9; return r===0||c===0||r===8||c===8; };
  function moves(s,who){ const M=[]; for(let i=0;i<81;i++){ if(side(s.b[i])!==who) continue; const r=i/9|0,c=i%9; for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){ let rr=r+dr,cc=c+dc; while(rr>=0&&rr<9&&cc>=0&&cc<9){ const j=rr*9+cc; if(s.b[j]) break; if(j===TH&&s.b[i]!=='k'){ rr+=dr; cc+=dc; continue; } M.push({f:i,t:j}); rr+=dr; cc+=dc; } } } return M; }
  function hostile(s,j,who){ if(j===TH&&!s.b[TH]) return true; const p=s.b[j]; return !!p&&side(p)!==who&&p!=='k'||(p==='k'&&who==='a'&&false); }
  function make(s,m){ const b=s.b.slice(); b[m.t]=b[m.f]; b[m.f]=''; const who=side(b[m.t]); const r=m.t/9|0,c=m.t%9; const caps=[];
   for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){ const r1=r+dr,c1=c+dc,r2=r+2*dr,c2=c+2*dc; if(r2<0||r2>8||c2<0||c2>8) continue; const j1=r1*9+c1,j2=r2*9+c2; const p1=b[j1]; if(!p1||side(p1)===who||p1==='k') continue; const ally=b[j2]&&side(b[j2])===who&&(b[j2]!=='k'||who==='d'); if(ally||(j2===TH&&!b[TH])){ caps.push(j1); } }
   caps.forEach(j=>b[j]=''); return {b,turn:who==='a'?'d':'a',caps:caps.length}; }
  function result(s){ const k=s.b.indexOf('k'); if(k<0) return 'a'; if(isEdge(k)) return 'd'; const r=k/9|0,c=k%9; const around=[[r-1,c],[r+1,c],[r,c-1],[r,c+1]].map(([rr,cc])=>rr*9+cc); if(around.every(j=>s.b[j]==='a'||(j===TH&&!s.b[TH]))) return 'a'; if(!moves(s,s.turn).length) return s.turn==='a'?'d':'a'; return null; }
  function evalS(s){ const k=s.b.indexOf('k'); if(k<0) return -1000; const r=k/9|0,c=k%9; let v=0; v+=s.b.filter(p=>p==='d').length*12-s.b.filter(p=>p==='a').length*7; const toEdge=Math.min(r,c,8-r,8-c); v+=(4-toEdge)*14; const around=[[r-1,c],[r+1,c],[r,c-1],[r,c+1]].filter(([rr,cc])=>rr>=0&&rr<9&&cc>=0&&cc<9&&s.b[rr*9+cc]==='a').length; v-=around*22;
   /* open lines from the king to an edge */ for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){ let rr=r+dr,cc=c+dc, clear=true; while(rr>=0&&rr<9&&cc>=0&&cc<9){ if(s.b[rr*9+cc]){ clear=false; break; } rr+=dr; cc+=dc; } if(clear) v+=60; } return v; }
  function search(s,d,a,bt){ const res=result(s); if(res) return (res===s.turn?1:-1)*(100000+d); if(d<=0) return (s.turn==='d'?1:-1)*evalS(s); const M=moves(s,s.turn); for(const m of M){ const v=-search(make(s,m),d-1,-bt,-a); if(v>a) a=v; if(a>=bt) break; } return a; }
  function best(s,d){ const M=moves(s,s.turn).sort(()=>Math.random()-.5); let bm=M[0],a=-1e9; for(const m of M){ const n=make(s,m); const r=result(n); if(r===s.turn) return m; const v=-search(n,d-1,-1e9,-a)+(n.caps||0)*4; if(v>a){ a=v; bm=m; } } return bm; }
  function newGame(){ const o=O.side==='rand'?(Math.random()<.5?'a':'d'):O.side; H=o==='hot'?{a:true,d:true}:o==='watch'?{a:false,d:false}:{a:o==='a',d:o==='d'}; me=H.d&&!H.a?'d':'a'; st=init(); sel=null; over=false; last=null; msg=H.a&&H.d?'Two players: the attackers move first.':!H.a&&!H.d?'The computer plays both sides.':H.a?'You lead the attackers: your move.':'You defend the king: the attackers move first.'; render(); if(!isH(st.turn)) ctx.after(600,ai); }
  function after(m,who){ last=m; st=make(st,m); beep(who?330:560); const nm=t=>t==='a'?'The attackers':'The defenders'; const r=result(st); if(r){ over=true; msg=(H.a!==H.d?(isH(r)?'You win! 🎉 ':'The computer wins. '):nm(r)+' win. ')+(r==='d'?'The king escaped to the edge.':'The king is captured.'); } else msg=(st.caps?nm(st.turn==='a'?'d':'a')+' captured '+st.caps+'. ':'')+(isH(st.turn)?(H.a&&H.d?nm(st.turn)+' to move.':'Your move.'):'The computer thinks…'); render(); if(!over&&!isH(st.turn)) ctx.after(H.a||H.d?300:650,ai); }
  function ai(){ if(over) return; busy=true; setTimeout(()=>{ const m=best(st,[1,2,2][ctx.diff||0]); busy=false; if(m) after(m,1); },30); }
  function tap(i){ if(over||busy||!isH(st.turn)) return; if(sel!=null){ const m=moves(st,st.turn).find(x=>x.f===sel&&x.t===i); if(m){ sel=null; return after(m,0); } } sel=side(st.b[i])===st.turn?i:null; render(); }
  function render(){ root.innerHTML=''; const B=h('div',{className:'k7B',style:'grid-template-columns:repeat(9,minmax(0,1fr))'}); const T=sel!=null?moves(st,st.turn).filter(m=>m.f===sel).map(m=>m.t):[];
   for(let i=0;i<81;i++){ const p=st.b[i]; const e=h('button',{type:'button',className:'k7C tf'+(i===TH?' throne':'')+(sel===i?' sel':'')+(last&&(last.f===i||last.t===i)?' last':''),'aria-label':'square '+(i+1)}); if(p) e.appendChild(h('div',{className:'tfP '+(p==='k'?'k':p)},p==='k'?'♔':'')); if(T.includes(i)) e.appendChild(h('i',{className:'dot'})); e.addEventListener('click',()=>tap(i)); B.appendChild(e); }
   root.appendChild(B); root.appendChild(h('div',{className:'k7Msg'},msg)); root.appendChild(h('div',{className:'k7Msg'},'Attackers '+st.b.filter(p=>p==='a').length+' · Defenders '+st.b.filter(p=>p==='d').length)); const b=bar(root); btn(b,'🔁 New game',newGame); ctx.status(msg); }
  newGame(); window.__kgst=()=>({st,over,msg}); return {state:()=>({st,over})};
 });
})();
