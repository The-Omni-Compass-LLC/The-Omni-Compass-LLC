(()=>{ /* 🔗 EVERY TOPIC LINKS OUT (v255): every card that names a topic (the Knowledge Library's cards, the religions and traditions, the
   sports, the markets) carries one row of links to where that topic lives on the web: its Wikipedia article (reached through Wikipedia's
   own search, so the link always lands), Britannica, and a web search. The app's own words stay first; the links take the reader further. */
 const enc=encodeURIComponent; const WK=t=>'https://en.wikipedia.org/wiki/Special:Search?go=Go&search='+enc(t), BR=t=>'https://www.britannica.com/search?query='+enc(t), WEB=t=>'https://duckduckgo.com/?q='+enc(t);
 const SEL='.knCard,.rgCard,.spCard,.mkCard';
 const css=document.createElement('style'); css.textContent='.ogLearn{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:6px;font:700 12px system-ui,sans-serif;opacity:.95}.ogLearn span{opacity:.75}.ogLearn a{color:#8ff4ff;text-decoration:none;font-weight:800}.ogLearn a:hover{text-decoration:underline}'; document.head.appendChild(css);
 const clean=t=>String(t||'').replace(/^[\s\d.·:)\-–]+/,'').replace(/[\u{1F000}-\u{1FFFF}\u{2600}-\u{27BF}\u{FE0F}\u{200D}]/gu,'').replace(/\s*[·(].*$/,'').replace(/\s+/g,' ').trim();
 let n=0;
 function add(){ document.querySelectorAll(SEL).forEach(c=>{ if(c.querySelector(':scope > .ogLearn')) return; const t=clean((c.querySelector('b,h3,h4,strong')||{}).textContent); if(!t||t.length<2) return; const d=document.createElement('div'); d.className='ogLearn'; d.innerHTML='<span>🔗 Learn more:</span><a href="'+WK(t)+'" target="_blank" rel="noopener">Wikipedia ↗</a><a href="'+BR(t)+'" target="_blank" rel="noopener">Britannica ↗</a><a href="'+WEB(t)+'" target="_blank" rel="noopener">Web ↗</a>'; c.appendChild(d); n++; }); }
 /* throttled, never starved: a screen that redraws all the time still gets its links */
 let due=false; const mo=new MutationObserver(()=>{ if(due) return; due=true; setTimeout(()=>{ due=false; add(); },400); }); mo.observe(document.documentElement,{childList:true,subtree:true});
 setInterval(add,1500);
 window.KWEB={add,get count(){ return n; }};
})();
