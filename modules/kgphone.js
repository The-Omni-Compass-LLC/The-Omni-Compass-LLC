(()=>{ /* THE BOARD FIRST ON A PHONE (v233). On a phone the Games screen used to stack every control above the board (the brand line,
   four dropdowns with dice, the hub buttons, Play, Pause, Restart and Stop, favourites and records), so the board began about 560
   pixels down a 660-pixel screen and taps landed on nothing. Now, on a narrow or short screen, those controls fold into one slim bar
   (⚙ Options, New, Undo, How to play, All games) and the board starts right under it; ⚙ Options opens the full controls again, and
   opening a game scrolls its board into view. The remote still carries Play, Stop, Undo and Close. The on-screen joystick shows only for arcade-style games, unless it is set to Always show. */
 const $=id=>document.getElementById(id);
 let open=false;
 const small=()=>innerWidth<=760||innerHeight<=740;
 const css=document.createElement('style'); css.textContent=`
#gamesDock.gcompact .gmTop .ocBrand,#gamesDock.gcompact .gmTop .gmSel,#gamesDock.gcompact .gmTop .gbar,#gamesDock.gcompact #gcBar,#gamesDock.gcompact .ghStrip{display:none!important}
#gamesDock.gnopad #kPadV{display:none!important}
#gamesDock.gcompact .gmTop{padding-top:4px!important;padding-bottom:0!important;min-height:0!important}
#gmMini{display:none;gap:6px;flex-wrap:nowrap;overflow-x:auto;padding:6px 4px;align-items:center;-webkit-overflow-scrolling:touch;scrollbar-width:none}
#gmMini::-webkit-scrollbar{display:none}
#gamesDock.gsmall #gmMini{display:flex;box-sizing:border-box;width:calc(100% - 118px);max-width:calc(100% - 118px)}
#gmMini button{flex:none;min-height:40px!important;border-radius:10px!important;padding:0 12px!important;font:800 14px system-ui,sans-serif!important;white-space:nowrap}
#gmMini button.on{background:#ffe94a!important;color:#14163a!important}
#gamesDock.gcompact #gmTitle{margin:2px 0 4px!important;font-size:18px!important}`; document.head.appendChild(css);
 const btnByText=re=>[...($('gamesDock')||document).querySelectorAll('button')].find(b=>b.getClientRects().length&&re.test((b.textContent||'').trim())&&!b.closest('#gmMini'));
 const hidden=re=>[...($('gamesDock')||document).querySelectorAll('button')].find(b=>re.test((b.textContent||'').trim())&&!b.closest('#gmMini'));
 function bar(){ const g=$('gamesDock'), t=$('gmTitle'); if(!g||!t) return null; let m=$('gmMini'); if(m) return m;
  m=document.createElement('div'); m.id='gmMini'; m.setAttribute('role','toolbar'); m.setAttribute('aria-label','Game controls');
  m.innerHTML='<button type="button" data-gm="opts" data-noul>⚙ Options</button><button type="button" data-gm="new" data-noul>🆕 New</button><button type="button" data-gm="undo" data-noul>↶ Undo</button><button type="button" data-gm="how" data-noul>❓ How to play</button><button type="button" data-gm="all" data-noul>🗂 All games</button>';
  t.parentNode.insertBefore(m,t);
  m.addEventListener('click',e=>{ const b=e.target.closest('[data-gm]'); if(!b) return; e.stopPropagation(); const k=b.dataset.gm;
   if(k==='opts'){ open=!open; paint(); if(open){ const top=document.querySelector(".gmTop"); if(top) top.scrollIntoView({block:'start'}); } return; }
   const map={new:/^New game$/i,undo:/^↶\s*Undo$/,how:/^How to play$/i,all:/All games$/};
   const real=hidden(map[k]); if(real){ real.click(); if(k!=='how'&&k!=='all') setTimeout(focusBoard,80); } });
  return m; }
 const ACTION=new Set(['Arcade','Video games','Mobile hits','Carnival & Sports']);
 function curCat(){ try{ const sel=[...$('gamesDock').querySelectorAll('select')].find(x=>x.getAttribute('aria-label')==='Game'); const id=sel&&sel.value; const g=(window.GAMES&&GAMES.list||[]).find(x=>x.id===id||x.name===id); return g?g.cat:''; }catch(_){ return ''; } }
 function padWanted(){ let m='auto'; try{ m=JSON.parse(localStorage.getItem('kanin-pad')||'"auto"'); }catch(_){ } if(m==='on') return true; return ACTION.has(curCat()); }
 function paint(){ const g=$('gamesDock'); if(!g) return; const s=small(); g.classList.toggle('gnopad',!padWanted()); g.classList.toggle('gsmall',s); g.classList.toggle('gcompact',s&&!open); const m=bar(); if(m){ const o=m.querySelector('[data-gm="opts"]'); if(o){ o.classList.toggle('on',open); o.textContent=open?'⚙ Hide options':'⚙ Options'; } } }
 function focusBoard(){ if(!small()) return; const t=$('gmMini')||$('gmTitle'); if(t) try{ t.scrollIntoView({block:'start'}); }catch(_){ } }
 /* opening a game folds the options again and brings its board into view */
 function wrap(){ const G=window.GAMES; if(!G||typeof G.open!=='function'||G.open.__kgp) return; const f=G.open; const w=function(...a){ const r=f.apply(this,a); open=false; paint(); setTimeout(focusBoard,60); setTimeout(focusBoard,400); return r; }; w.__kgp=1; G.open=w; }
 addEventListener('resize',paint);
 setInterval(()=>{ wrap(); const g=$('gamesDock'); if(g&&!g.hidden) paint(); },500);
 window.KGPHONE={paint,focusBoard,get options(){ return open; },set options(v){ open=!!v; paint(); }};
})();
