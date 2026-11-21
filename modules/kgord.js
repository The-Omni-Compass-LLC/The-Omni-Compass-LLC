(()=>{ /* GAME FAMILIES IN ORDER OF USE (v230). The Games screen's Category list runs from the families people reach for most to the
   least, each with its count: video games, arcade, cards, board, puzzle, word, mobile hits, game shows, casino, dice, carnival and
   sports, dominoes, mahjong. The values stay the family names, so every part of the games engine reads them as before. */
 const ORDER=['Video games','Arcade','Cards','Board','Puzzle','Word','Mobile hits','Game Shows','Casino','Dice','Carnival & Sports','Dominoes','Mahjong'];
 const rank=v=>{ const i=ORDER.indexOf(v); return i<0?ORDER.length:i; };
 function fix(){ const g=document.getElementById('gamesDock'); if(!g||!window.GAMES||!GAMES.list) return;
  const s=[...g.querySelectorAll('select')].find(x=>x.getAttribute('aria-label')==='Category'); if(!s||!s.options.length) return;
  const cnt={}; GAMES.list.forEach(x=>{ cnt[x.cat]=(cnt[x.cat]||0)+1; });
  const opts=[...s.options]; const sorted=opts.slice().sort((a,b)=>rank(a.value)-rank(b.value));
  const inOrder=sorted.every((o,i)=>o===opts[i]); const label=o=>o.value+(cnt[o.value]?' · '+cnt[o.value]:'');
  if(inOrder&&opts.every(o=>o.textContent===label(o))) return;
  const keep=s.value; sorted.forEach(o=>{ o.textContent=label(o); s.appendChild(o); }); s.value=keep; }
 setInterval(fix,700); fix();
 window.KGORD={order:ORDER,fix};
})();
