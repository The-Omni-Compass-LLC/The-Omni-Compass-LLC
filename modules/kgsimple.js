(()=>{ /* 🎮 SIMPLE GAMES (v238): the Games screen made elementary, for everyone, on every screen. Opening Games shows eight big picture
   groups, the same as the Games page of www.omni-galaxy.com: Cards, Board & Tiles, Dice & Casino, Word & Puzzle, Arcade, Sports &
   Carnival, Solitaire and Game Shows, plus the games played lately. Tap a group, tap a game: the game opens with four big buttons
   only (🗂 Games, 🆕 New, ↶ Undo, ❓ How to play). Every expert control (the dropdowns, dice, hub, records) is still there behind
   ⚙ All options, and 🧒 Simple brings this view back. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const SOL=/solitaire|spider|freecell|yukon|forty thieves|golf|tripeaks|tri-peaks|pyramid|accordion|clock patience|canfield|scorpion|baker|calculation/i;
 const GROUPS=[['cards','🃏','Cards','Poker, Blackjack, Go Fish, Spades, Hearts…',g=>g.cat==='Cards'&&!SOL.test(g.name)],['board','♟','Board & Tiles','Chess, Checkers, Dominoes, Mahjong…',g=>g.cat==='Board'||g.cat==='Dominoes'||g.cat==='Mahjong'],
  ['dice','🎲','Dice & Casino','Yacht, Farkle, Roulette, Slots, Bingo… play chips only',g=>g.cat==='Dice'||g.cat==='Casino'],['word','🔤','Word & Puzzle','Word Hunt, Crossword, Sudoku, Memory…',g=>g.cat==='Word'||g.cat==='Puzzle'],
  ['arcade','🕹','Arcade','Serpent, Brick Breaker, the video games…',g=>g.cat==='Arcade'||g.cat==='Mobile hits'||g.cat==='Video games'],['sports','⚽','Sports & Carnival','Ring Toss, Skee-Ball, Cornhole…',g=>g.cat==='Carnival & Sports'],
  ['sol','🂡','Solitaire','Klondike, Spider, FreeCell, Pyramid…',g=>g.cat==='Cards'&&SOL.test(g.name)],['shows','📺','Game Shows','Spin & Solve, Money Ladder…',g=>g.cat==='Game Shows']];
 let simple=getLS('kanin-gsimple',true), view='groups', grp='', picking=true, wasOpen=false, pickAt=0;
 let recent=getLS('kanin-gsimple-recent',[]); if(!Array.isArray(recent)) recent=[];
 const list=()=>{ try{ return (window.GAMES&&GAMES.list)||[]; }catch(_){ return []; } };
 const css=document.createElement('style'); css.textContent=`
#gamesDock.gsimp .gmTop .ocBrand,#gamesDock.gsimp .gmTop .gmSel,#gamesDock.gsimp .gmTop .gbar,#gamesDock.gsimp #gcBar,#gamesDock.gsimp .ghStrip{display:none!important}
#gamesDock.gsimp #gmMini{display:flex!important;box-sizing:border-box;width:calc(100% - 118px);max-width:calc(100% - 118px)}
#gamesDock.gsimp #gmMini [data-gm="opts"]{display:none!important}
#gamesDock.gsimp .kKeyMon,#gamesDock.gsimp .kLib{display:none!important}
@media (min-width:761px){ #gamesDock.gsimp{padding-top:72px!important} #gamesDock.gsimp #gmMini{position:fixed!important;top:calc(8px + env(safe-area-inset-top,0px));left:12px;z-index:9600;width:auto!important;max-width:calc(100vw - var(--kRailW,58px) - 280px)!important;background:rgba(24,14,80,.94);border:2px solid #b9a6ff;border-radius:16px;padding:6px 8px!important;box-shadow:0 8px 24px rgba(0,0,0,.45)} #gamesDock.gsimp #gmMini button{min-height:46px!important;font-size:16px!important} }
#gsPick{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9650;overflow:auto;background:linear-gradient(180deg,#2a1680 0,#1c0f5c 55%,#120a3e 100%);color:#fff;padding:calc(14px + env(safe-area-inset-top,0px)) 16px calc(200px + env(safe-area-inset-bottom,0px));font:16px/1.5 system-ui,sans-serif;box-sizing:border-box}
#gsPick[hidden]{display:none!important}
#gsPick .gsIn{max-width:1000px;margin:0 auto}
#gsPick h2{font:900 clamp(28px,6vw,44px)/1.1 system-ui,sans-serif;margin:4px 0 2px}
#gsPick .gsSub{font:600 17px system-ui,sans-serif;color:#d9d0ff;margin:0 0 14px}
#gsPick .gsTiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}
#gsPick .gsTile{display:flex!important;flex-direction:column;align-items:flex-start;gap:4px;min-height:120px!important;padding:14px!important;border-radius:20px!important;text-align:left;background:linear-gradient(160deg,#4b2fd6,#2b188f)!important;border:2px solid #b9a6ff!important}
#gsPick .gsTile:hover{border-color:#ffe94a!important}
#gsPick .gsTile i{font-style:normal;font-size:44px;line-height:1}
#gsPick .gsTile b{font:900 22px system-ui,sans-serif}
#gsPick .gsTile small{font:600 13.5px/1.35 system-ui,sans-serif;color:#e4dcff}
#gsPick .gsTile em{font:800 12px system-ui,sans-serif;font-style:normal;color:#ffe94a}
#gsPick .gsGames{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
#gsPick .gsGame{display:flex!important;flex-direction:column;align-items:flex-start;gap:2px;min-height:72px!important;padding:10px 14px!important;border-radius:16px!important;text-align:left;font:800 18px system-ui,sans-serif!important}
#gsPick .gsGame small{font:600 13px/1.35 system-ui,sans-serif;color:#d9d0ff}
#gsPick .gsBar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 12px}
#gsPick .gsBar button{min-height:48px!important;padding:0 16px!important;border-radius:14px!important;font:900 16px system-ui,sans-serif!important}
#gsPick .gsBack{background:#ffe94a!important;color:#14163a!important;border-color:#ffe94a!important}
#gsPick .gsRecent{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 4px}
#gsPick .gsRecent button{min-height:44px!important;border-radius:999px!important;padding:0 14px!important;font:800 15px system-ui,sans-serif!important}
#gsPick .gsExpert{margin-top:22px;font:600 14px system-ui,sans-serif;color:#cfc4ff}
#gsPick .gsExpert button{min-height:40px!important;border-radius:12px!important;padding:0 12px!important;font:700 14px system-ui,sans-serif!important}
#gsSimpleBtn{position:fixed;z-index:9640;left:calc(10px + env(safe-area-inset-left,0px));bottom:calc(150px + env(safe-area-inset-bottom,0px));min-height:44px!important;border-radius:999px!important;padding:0 14px!important;font:900 15px system-ui,sans-serif!important;background:#ffe94a!important;color:#14163a!important;border:2px solid #fff!important;box-shadow:0 6px 18px rgba(0,0,0,.45)}
#gsSimpleBtn[hidden]{display:none!important}
@media (max-width:560px){ #gsPick .gsTiles{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px} #gsPick .gsTile{min-height:112px!important;padding:12px!important} #gsPick .gsTile i{font-size:38px} #gsPick .gsTile b{font-size:18px} #gsPick .gsTile small{display:none} #gsPick .gsGames{grid-template-columns:minmax(0,1fr)} }`; document.head.appendChild(css);
 const dock=()=>$('gamesDock');
 const dockOpen=()=>{ const d=dock(); if(!d||d.hidden) return false; const cs=getComputedStyle(d); return cs.display!=='none'&&d.getBoundingClientRect().width>40; };
 function pickEl(){ let p=$('gsPick'); if(p) return p; p=document.createElement('div'); p.id='gsPick'; p.hidden=true; p.setAttribute('role','dialog'); p.setAttribute('aria-label','Pick a game'); document.body.appendChild(p);
  p.addEventListener('click',onPick); return p; }
 const first=s=>{ const t=String(s||'').replace(/\s+/g,' ').trim(); const m=t.match(/^.{0,90}?[.!?](\s|$)/); return (m?m[0]:t.slice(0,90)).trim(); };
 function paintPick(){ const p=pickEl(); const L=list(); let h='<div class="gsIn">';
  if(view==='groups'){ const rc=recent.map(id=>L.find(g=>g.id===id)).filter(Boolean).slice(0,6);
   h+='<h2>🎮 Games</h2><p class="gsSub">Tap a group. Then tap a game. That’s it.</p><div class="gsTiles">'+GROUPS.map(([k,ic,nm,sm,f])=>{ const n=L.filter(f).length; return '<button type="button" class="gsTile" data-gs="grp" data-k="'+k+'" data-noul><i>'+ic+'</i><b>'+esc(nm)+'</b><small>'+esc(sm)+'</small><em>'+n+' games</em></button>'; }).join('')+'</div>'+
    (rc.length?'<div class="gsRecent"><b style="width:100%">⭐ Played lately</b>'+rc.map(g=>'<button type="button" data-gs="game" data-id="'+esc(g.id)+'" data-noul>▶ '+esc(g.name)+'</button>').join('')+'</div>':'')+
    '<p class="gsExpert">Want every control? <button type="button" data-gs="expert" data-noul>⚙ All options</button></p>'; }
  else { const G=GROUPS.find(x=>x[0]===grp)||GROUPS[0]; const games=L.filter(G[4]);
   h+='<div class="gsBar"><button type="button" class="gsBack" data-gs="back" data-noul>◀ All groups</button></div><h2>'+G[1]+' '+esc(G[2])+'</h2><p class="gsSub">'+games.length+' games. Tap one to play. The computer plays every empty seat.</p><div class="gsGames">'+games.map(g=>'<button type="button" class="gsGame" data-gs="game" data-id="'+esc(g.id)+'" data-noul>▶ '+esc(g.name)+'<small>'+esc(first(g.how))+'</small></button>').join('')+'</div>'; }
  p.innerHTML=h+'</div>'; }
 function showPick(v){ view=v||'groups'; picking=true; pickAt=Date.now(); const p=pickEl(); paintPick(); p.hidden=false; p.scrollTop=0; paintBtn(); }
 function hidePick(){ picking=false; const p=$('gsPick'); if(p) p.hidden=true; paintBtn(); }
 function play(id){ const g=list().find(x=>x.id===id); if(!g) return; recent=[id,...recent.filter(x=>x!==id)].slice(0,8); putLS('kanin-gsimple-recent',recent); hidePick(); try{ GAMES.open(id); }catch(_){ } setTimeout(()=>{ try{ KGPHONE.focusBoard(); }catch(_){ } const d=dock(); if(d) try{ (document.getElementById('gmMini')||d).scrollIntoView({block:'start'}); }catch(_){ } },120); say('▶ '+g.name+'. Tap 🗂 Games to pick another.'); }
 function onPick(e){ const b=e.target.closest('[data-gs]'); if(!b) return; e.stopPropagation(); const k=b.dataset.gs;
  if(k==='grp'){ grp=b.dataset.k; view='list'; paintPick(); pickEl().scrollTop=0; return; }
  if(k==='back'){ view='groups'; paintPick(); return; }
  if(k==='game') return play(b.dataset.id);
  if(k==='expert'){ simple=false; putLS('kanin-gsimple',false); hidePick(); paint(); say('⚙ All options shown. Tap 🧒 Simple to go back.'); return; } }
 function paintBtn(){ let b=$('gsSimpleBtn'); const want=dockOpen()&&!simple; if(!b){ if(!want) return; b=document.createElement('button'); b.type='button'; b.id='gsSimpleBtn'; b.setAttribute('data-noul',''); b.textContent='🧒 Simple'; b.title='Big buttons, fewer controls'; b.addEventListener('click',e=>{ e.stopPropagation(); simple=true; putLS('kanin-gsimple',true); paint(); showPick('groups'); }); document.body.appendChild(b); }
  if(b.hidden!==!want) b.hidden=!want; }
 function paint(){ const d=dock(); if(!d) return; d.classList.toggle('gsimp',!!simple); paintBtn(); }
 /* the slim bar’s 🗂 All games goes back to the big groups; the old ⚙ Options is replaced by ⚙ All options inside the picker */
 document.addEventListener('click',e=>{ if(!simple||!e.target.closest) return; const b=e.target.closest('#gmMini [data-gm="all"]'); if(b){ e.stopImmediatePropagation(); e.preventDefault(); showPick('groups'); } },true);
 /* the rail’s 🕹 Games button opens the big groups straight away (the long list of every game stays under 🕹 Video games in the Menu) */
 document.addEventListener('click',e=>{ if(!simple||!e.target.closest) return; const b=e.target.closest('#kdGames'); if(!b) return; e.stopImmediatePropagation(); e.preventDefault(); try{ if(!dockOpen()) KRAIL.goTo('gamesDock'); }catch(_){ } setTimeout(()=>{ paint(); showPick('groups'); wasOpen=dockOpen(); },dockOpen()?0:450); },true);
 /* the slim bar names its first button for what it does here */
 function relabel(){ const a=document.querySelector('#gmMini [data-gm="all"]'); if(a&&simple&&a.textContent!=='🗂 Games'){ a.textContent='🗂 Games'; const m=a.parentElement; if(m&&m.firstChild!==a) m.insertBefore(a,m.firstChild); } }
 setInterval(()=>{ const open=dockOpen(); if(open&&!wasOpen){ paint(); if(simple) showPick('groups'); } if(!open&&wasOpen){ hidePick(); } if(!open){ const p=$('gsPick'); if(p&&!p.hidden) p.hidden=true; }
  wasOpen=open; if(open){ paint(); relabel(); } else paintBtn(); },300);
 /* opening a game any other way (Find, a link, the remote) closes the picker */
 const wrap=()=>{ const G=window.GAMES; if(!G||typeof G.open!=='function'||G.open.__gs) return; const f=G.open; const w=function(...a){ const r=f.apply(this,a); if(picking&&Date.now()-pickAt>1500) hidePick(); /* a game asked for by name (Find, a link, Video games, a shortcut): the picker steps aside for it (v261) */ if(a[0]&&typeof a[0]==='string'){ [60,400,900].forEach(ms=>setTimeout(()=>{ if(picking) hidePick(); },ms)); } return r; }; w.__gs=1; G.open=w; }; setInterval(wrap,700);
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'){ const p=$('gsPick'); if(p&&!p.hidden&&view==='list'){ view='groups'; paintPick(); e.stopPropagation(); } } },true);
 window.KGSIMPLE={show:showPick,hide:hidePick,get simple(){ return simple; },set simple(v){ simple=!!v; putLS('kanin-gsimple',simple); paint(); },groups:GROUPS.map(g=>g[0])};
})();
