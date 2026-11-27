(()=>{ /* 📐 v224: THE RIGHT-HAND RAIL, READABLE. No empty gap: every button grows into the whole column; ▶ Play sits at the bottom,
   right on top of ☰ Menu; the names are big enough to read (about 12px on a phone, up to 15px on a desktop) and the rail is a
   little wider on phones so no name is cut. */
 const css=document.createElement('style'); css.textContent=`
@media (max-width:760px){ :root{--kRailW:68px!important} }
html body #rDock#rDock#rDock{gap:2px!important;justify-content:stretch!important}
html body #rDock#rDock#rDock .kdSpace{flex:0 0 0px!important;min-height:0!important;height:0!important;margin:0!important;padding:0!important}
html body #rDock#rDock#rDock>button,html body #rDock#rDock#rDock #kStopBtn{flex:1 1 0px!important;min-height:0!important;max-height:96px!important;padding:1px 1px!important;gap:0!important;justify-content:center!important;overflow:hidden!important}
html body #rDock#rDock#rDock #kStopBtn{order:30!important;flex:1.25 1 0px!important}
html body #rDock#rDock#rDock #lpMenu{order:31!important;flex:1.25 1 0px!important;min-height:0!important}
html body #rDock#rDock#rDock>button::before,html body #rDock#rDock#rDock #kStopBtn::before{font-size:var(--rIco,clamp(14px,2.7vh,22px))!important;line-height:1.05!important}
html body #rDock#rDock#rDock>button::after,html body #rDock#rDock#rDock #kStopBtn::after{font-size:var(--rLab,clamp(10px,1.8vh,12.5px))!important;line-height:1.08!important;font-weight:800!important;letter-spacing:-.015em!important;white-space:nowrap!important;max-width:100%!important;overflow:hidden!important;text-overflow:clip!important}

html body #rDock#rDock#rDock>button,html body #rDock#rDock#rDock #kStopBtn{flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;width:100%!important;align-self:stretch!important;margin:0!important;box-sizing:border-box!important}
html body #rDock#rDock#rDock>button::before,html body #rDock#rDock#rDock #kStopBtn::before,html body #rDock#rDock#rDock>button::after,html body #rDock#rDock#rDock #kStopBtn::after{display:block!important;width:100%!important;text-align:center!important;margin:0!important;padding:0!important}
html body #rDock#rDock#rDock #askBtn{border-radius:10px!important;width:100%!important;min-width:0!important}
html.kRail2 body #rDock#rDock#rDock{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;grid-auto-rows:minmax(0,1fr)!important;align-content:stretch!important;gap:2px!important}
html.kRail2 body #rDock#rDock#rDock>button,html.kRail2 body #rDock#rDock#rDock #kStopBtn{max-height:none!important;height:auto!important}
html.kRail2 body #rDock#rDock#rDock #kStopBtn,html.kRail2 body #rDock#rDock#rDock #lpMenu{grid-column:1 / -1!important}
html.kRail2 body #rDock#rDock#rDock .kdSpace{display:none!important}
html body #rDock#rDock#rDock :is(#kdSocial,#kdLvl,#kdTour,#askBtn){display:none!important}
html body #rDock#rDock#rDock #kdHome{order:1!important}html body #rDock#rDock#rDock #kdGames{order:2!important;display:flex!important}html body #rDock#rDock#rDock #kdStudio{order:3!important}html body #rDock#rDock#rDock #kdOmni{order:4!important}html body #rDock#rDock#rDock #kdZod{order:5!important}html body #rDock#rDock#rDock #kdKara{order:6!important}html body #rDock#rDock#rDock #kdAI{order:7!important}html body #rDock#rDock#rDock #kdFind{order:8!important}html body #rDock#rDock#rDock #kdProj{order:9!important}html body #rDock#rDock#rDock #kdProfile{order:10!important}html body #rDock#rDock#rDock #kdPanel{order:11!important}html body #rDock#rDock#rDock #kdIPads{order:12!important}html body #rDock#rDock#rDock #kdIKeys{order:13!important}html body #rDock#rDock#rDock #kdIDJ{order:14!important}html body #rDock#rDock#rDock #kdVG{order:15!important}
html body #rDock#rDock#rDock #kdHome::before{content:'📖'!important}html body #rDock#rDock#rDock #kdHome::after{content:'Story'!important}
html body #tourTab .kMenuH{font:900 15px system-ui,sans-serif;color:#ffe94a;padding:8px 6px 2px;letter-spacing:.02em;align-self:end;border-bottom:2px solid rgba(255,233,74,.45)}
html body #tourTab .kMenuH small{display:block;font:700 11.5px system-ui,sans-serif;color:#d8d0ff;letter-spacing:0}
html body #tourTab > :is(#kStart,.kStart){display:none!important}
html body #tourTab > :is(#kCanRow,.kCanRow){order:90!important}html body #tourTab > :is(#kLvlRow,.kLvlRow){order:91!important}html body #tourTab > :is(#ttOwner,.ttOwner){order:92!important}html body #tourTab > #ttVG{order:93!important;grid-column:1 / -1!important}
html body #tourTab > .kMenuH:first-of-type{grid-column:1!important}`; document.head.appendChild(css);
 /* the fitter: from the rail's own height and the number of buttons it carries now, the biggest icon and name that fit whole */
 const cv=document.createElement('canvas').getContext('2d'); let last='';
 function fit(){ const d=document.getElementById('rDock'); if(!d) return; const bs=[...d.querySelectorAll(':scope > button, :scope #kStopBtn')].filter(b=>!b.hidden&&getComputedStyle(b).display!=='none');
  const n=bs.length; if(!n) return; const cs=getComputedStyle(d); const Hall=d.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom); const W=d.clientWidth-6;
  const root=document.documentElement, base=innerWidth>=2500?124:innerWidth>=1700?96:innerWidth>=761?76:68; const vis=b=>!b.hidden&&getComputedStyle(b).display!=='none'; const per1=(Hall-2*(n-1))/(n+0.5);
  const two=per1<33&&innerWidth>=480; if(two!==root.classList.contains('kRail2')){ root.classList.toggle('kRail2',two); if(two) root.style.setProperty('--kRailW',(base*2)+'px','important'); else root.style.removeProperty('--kRailW'); last=''; return setTimeout(fit,30); }
  const rows=two?Math.ceil((n-2)/2)+2:n; const per=two?(Hall-2*(rows-1))/rows:per1; const big=innerWidth>=1700?1.35:innerWidth>=761?1.15:1;
  let lab=Math.min(15*big,Math.max(9,per*0.34)), ico=Math.min(28*big,Math.max(11,per*0.5));
  const reg=bs.filter(b=>b.id!=='lpMenu'&&b.id!=='kStopBtn'&&b.dataset.kdL); const b0=reg[0]||bs[0], ac=getComputedStyle(b0,'::after'), bc=getComputedStyle(b0); const inner=Math.min(...(reg.length?reg:bs).map(b=>b.clientWidth))-parseFloat(bc.paddingLeft)-parseFloat(bc.paddingRight)-4; cv.font=(ac.fontWeight||'800')+' 100px '+(ac.fontFamily||'system-ui,sans-serif'); const ls=parseFloat(ac.letterSpacing)||0; const longest=Math.max(...(reg.length?reg:bs).map(b=>{ const t=b.dataset.kdL||''; return cv.measureText(t).width/100+(t.length*(ls/ (parseFloat(ac.fontSize)||12))); })); if(longest>0) lab=Math.min(lab,Math.max(8,inner)/longest);
  if(ico*1.05+lab*1.1+3>per){ lab=Math.max(8.5,Math.min(lab,(per-3)*0.4)); ico=Math.max(10,(per-3-lab*1.1)/1.05); }
  const key=n+'|'+Math.round(per*10)+'|'+W; if(key===last) return; last=key; d.style.setProperty('--rLab',lab.toFixed(2)+'px'); d.style.setProperty('--rIco',ico.toFixed(2)+'px'); }
 addEventListener('resize',()=>{ last=''; setTimeout(fit,60); }); setInterval(fit,700); setTimeout(fit,300);

 /* 🕹 Games on the rail, second only to the story builder */
 setInterval(()=>{ const d=document.getElementById('rDock'); if(d&&!document.getElementById('kdGames')){ const b=document.createElement('button'); b.type='button'; b.id='kdGames'; b.setAttribute('data-noul',''); b.dataset.kdI='🕹'; b.dataset.kdL='Games'; b.title='Games: every game in KAN-IN'; b.setAttribute('aria-label','Games'); b.addEventListener('click',e=>{ e.stopPropagation(); try{ const r=document.getElementById('kRec'); if(r) r.hidden=true; }catch(_){ } try{ KVG.open(); }catch(_){ try{ KRAIL.goTo('gamesDock'); }catch(__){ } } }); d.appendChild(b); last=''; }
  const hm=document.getElementById('kdHome'); if(hm&&hm.dataset.kdL!=='Story'){ hm.dataset.kdL='Story'; hm.dataset.kdI='📖'; hm.title='Story builder: make a story (home)'; hm.setAttribute('aria-label','Story builder'); } },800);
 /* ☰ THE MENU IN TWO EVEN COLUMNS (20 and 20, v247), MOST USED FIRST: ✍️ Make on the left, 🎮 Play, explore & you on the right, each in the order people use
    them most (story builder, games, studio, Omni-Compass, LuvMyZodiac first); the cannon, the level and the quote move under the list. */
 const LEFT=['📖 Make a story','🎛 Music Studio','🎬 Demo','🎼 Track sequencer','🎤 Karaoke','🎧 DJ decks','🎵 Music','✍️ Songwriter','🎨 The Easel','🎬 Video studio','🎙 Voices','📖 Storybook','🗂 Story library','📁 Projects','🧭 Layers','🛠 Craft','🧬 Mutate','🌐 Language','🔒 Lock & shuffle','⌨ Keyboards'];
 const RIGHT=['🕹 Video games','🧭 Omni-Compass governors','🧭 Omni-Compass','♈ LuvMyZodiac','🎲 Games','🍳 Recipes','😂 Laugh','🤖 AI','📰 Current News','✝️ Cultures & Religion','📈 Stock Market','🏆 Sports','🎓 Knowledge library','💥 Surprise me','👤 My profile','🌐 Social','📚 My library','❓ Ask KAN-IN','🗺 Show me around','🗺 All sections'];
 const RANK_R=['🕹 Video games','🧭 Omni-Compass','♈ LuvMyZodiac','🎲 Games','🍳 Recipes','😂 Laugh','🤖 AI','📰 Current News','✝️ Cultures & Religion','📈 Stock Market','🏆 Sports','🎓 Knowledge library','💥 Surprise me','👤 My profile','🌐 Social','📚 My library','🧭 Omni-Compass governors','❓ Ask KAN-IN','🗺 Show me around','🗺 All sections'];
 function menu(){ const t=document.getElementById('tourTab'); if(!t||!t.getClientRects().length) return; if(t.style.gridAutoFlow!=='row dense') t.style.gridAutoFlow='row dense';
  if(!t.querySelector('.kMenuH')){ [['✍️ Make','Stories, beats, tracks, songs, art, video',1,36],['🎮 Play, explore & you','Games, sports, news, Zodiac, your profile',2,37]].forEach(([h,sm,col,o])=>{ const e=document.createElement('div'); e.className='kMenuH'; e.innerHTML=h+'<small>'+sm+'</small>'; e.style.gridColumn=String(col); e.style.order=String(o); t.appendChild(e); }); }
  const cnt={1:0,2:0};
  [...t.children].forEach(b=>{ if(b.tagName!=='BUTTON') return; const tx=(b.textContent||'').trim(); if(b.id==='ttVG'){ b.style.order='93'; b.style.gridColumn='1 / -1'; return; }
   let i=LEFT.findIndex(p=>tx.startsWith(p)), col=1; if(i<0){ const m=RIGHT.find(p=>tx.startsWith(p)); if(m){ col=2; i=RANK_R.indexOf(m); } }
   if(i<0) return; if(!b.hasAttribute('data-easy')) b.setAttribute('data-easy',''); /* v242: every entry the same size, both sides even */ const o=String(38+i*2+(col===2?1:0)); if(b.style.order!==o) b.style.order=o; if(b.style.gridColumn!==String(col)) b.style.gridColumn=String(col); cnt[col]++; });
  [['kCanRow','90'],['kLvlRow','91'],['ttOwner','92']].forEach(([id,o])=>{ const e=t.querySelector('#'+id+',.'+id); if(e&&e.style.order!==o) e.style.order=o; }); }
 setInterval(menu,700); document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#lpMenu')) setTimeout(menu,60); },true);
 window.KMENU2={menu};
 window.KRAILFIT=fit;
 /* v228: Recipes alone in the Menu (the cooking school entry is gone). */
 const xs=document.createElement('style'); xs.textContent='#tourTab #ttSchool,#ttSchool{display:none!important}'; document.head.appendChild(xs);
 /* the Menu's game count follows the games as they load (it read 209 when it was made before the last games registered) */
 setInterval(()=>{ const b=document.getElementById('ttVG'); if(b&&window.GAMES&&GAMES.list){ const t='🕹 Video games: '+GAMES.list.length+' games'; if(b.textContent!==t) b.textContent=t; } },2000);
})();
