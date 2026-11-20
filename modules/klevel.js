(()=>{ /* LEVELS: one switch on the rail. 🟢 Easy shows only the essentials in plain words and opens the menu with ⭐ Start here;
   🟡 Everyday adds the tools creators use; 🔴 Pro shows every engine, knob and library. Nothing is deleted: a higher level brings it back. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const LV=[['easy','🟢','Easy','Easy: the essentials in plain words. Best for anyone and first-timers.'],['avg','🟡','Everyday','Everyday: the tools creators and influencers use.'],['pro','🔴','Pro','Pro: every engine, knob and library, for producers, writers and engineers.']];
 /* the factory setting: every open of KAN-IN starts on 🟡 Everyday; a person can switch for the visit, and the next open is Everyday again */
 let lv='avg';
 /* which parts belong to which level (anything not listed is for everyone) */
 const MAP={
  avg:['mpcSec','chopSec','seSec','slSec','vcSec','bandSec','sqWrap','sesWrap','kbWrap','rollWrap','autoSec','shSec','tpWrap','zodExtra','z4Today','z4Chart','z4Moons','z4China','z4Syn','z4Spin','z4Beat','z4Book','omniOrg','swAna','kkIn','kkOut'],
  pro:['brainSec','ofWrap','mrSec','msSec','rkWrap','formWrap','ssWrap','z4Live','z4Knobs','z4Blood','z4Deep','omniMath']};
 function tag(){ Object.keys(MAP).forEach(l=>MAP[l].forEach(id=>{ const e=$(id); if(!e) return; const t=(id==='kkIn'||id==='kkOut')?e:e; if(t.dataset.lvl!==l) t.dataset.lvl=l; })); document.querySelectorAll('section.kLib[id^="lib-"]').forEach(e=>{ if(e.dataset.lvl!=='avg') e.dataset.lvl='avg'; }); const mh=[...document.querySelectorAll('#pad h4')].find(h=>h.textContent.trim().startsWith('🎚 Mixer')); }
 const css=document.createElement('style'); css.textContent=`
html.lvl-easy [data-lvl="avg"],html.lvl-easy [data-lvl="pro"],html.lvl-avg [data-lvl="pro"]{display:none!important}
html body #rDock#rDock #kdLvl{order:4!important;display:flex!important}
#tourTab .kStart{grid-column:1/-1;order:40;font:900 16px/1.2 system-ui,sans-serif;color:#ffe94a;padding:8px 2px 2px}
#tourTab .kStartB{order:41;min-height:58px!important;font:800 16px/1.2 system-ui,sans-serif!important}
#tourTab .kLvlRow{grid-column:1/-1;order:2;display:flex;gap:6px;flex-wrap:wrap}
#tourTab .kLvlRow button,#kPanel .kLvlRow button{flex:1 1 90px;min-height:44px;border-radius:12px;font:700 14px system-ui,sans-serif}
#tourTab .kLvlRow button.on,#kPanel .kLvlRow button.on{background:#ffe94a!important;color:#14163a!important}
#kPanel .kLvlRow{display:flex;gap:6px;flex-wrap:wrap;margin:2px 0 8px}`; document.head.appendChild(css);
 function apply(quiet){ const h=document.documentElement; h.classList.remove('lvl-easy','lvl-avg','lvl-pro'); h.classList.add('lvl-'+lv); tag(); rail(); document.querySelectorAll('.kLvlRow button').forEach(b=>b.classList.toggle('on',b.dataset.lv===lv)); if(!quiet){ const L=LV.find(x=>x[0]===lv); say(L[1]+' '+L[3]); } }
 function setLv(v,quiet){ lv=v; putLS('kanin-level',lv); apply(quiet); panelLv(); }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#mFactory')) setTimeout(()=>{ setLv('avg',true); const t=document.querySelector('#tourTab .kLvlRow'); if(t) t.innerHTML=row(); },60); },true);
 function rail(){ const d=$('rDock'); if(!d) return; let b=$('kdLvl'); const L=LV.find(x=>x[0]===lv); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kdLvl'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); const i=LV.findIndex(x=>x[0]===lv); setLv(LV[(i+1)%LV.length][0]); }); d.appendChild(b); } b.dataset.kdI=L[1]; b.dataset.kdL=L[2]; b.title='Level: '+L[3]+' Tap to change.'; b.setAttribute('aria-label','Level: '+L[2]+'. Tap to change.'); }
 const row=()=>'<span class="kN" style="flex:1 1 100%;font:700 12px ui-monospace,monospace;letter-spacing:.1em;color:#7ff">HOW DO YOU WANT TO USE KAN-IN?</span>'+LV.map(x=>'<button type="button" data-lv="'+x[0]+'" class="'+(x[0]===lv?'on':'')+'" title="'+x[3]+'" data-noul>'+x[1]+' '+x[2]+'</button>').join('');
 /* the menu: a level switch and, for everyone, ⭐ Start here with plain big buttons */
 const go=fn=>()=>{ try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(fn,120); };
 const START=[['📖 Make a story',go(()=>{ try{ GOHOME(); }catch(_){ } const b=$('mQP')||$('qpBtn'); if(b) b.click(); })],['🥁 Make a beat',go(()=>{ try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ const a=$('cAuto'); if(a) a.click(); say('A beat is ready: press ▶ Play in the ⚙ Panel or on the bar.'); },1200); })],['🎤 Sing karaoke',go(()=>{ try{ KKARA.open(); }catch(_){ } })],['😂 Laugh',go(()=>{ try{ KHUMOR.open('day'); }catch(_){ } })],['🕹 Play a game',go(()=>{ try{ if(window.KVG) KVG.open(); else GAMES.open('m_merge'); }catch(_){ } })],['🌞 My horoscope',go(()=>{ try{ KSTARS.day(true); }catch(_){ } })],['💥 Surprise me',go(()=>{ try{ KJUMP.open(); setTimeout(()=>KJUMP.jump(),300); }catch(_){ } })],['🗺 Show me around',go(()=>{ const b=document.querySelector('#kHomeBar [data-ka="tour"]'); if(b) b.click(); })]];
 function menu(){ const t=$('tourTab'); if(!t) return; const lr=t.querySelector('.kLvlRow'), st=t.querySelector('.kStart'); if(lr&&lr.style.order!=='2') lr.style.order='2'; if(st&&st.style.order!=='40') st.style.order='40'; if(!t.querySelector('.kLvlRow')){ const r=document.createElement('div'); r.className='kLvlRow'; r.style.order='2'; r.innerHTML=row(); t.appendChild(r); r.addEventListener('click',e=>{ e.stopPropagation(); const b=e.target.closest('[data-lv]'); if(b){ setLv(b.dataset.lv); r.innerHTML=row(); } }); }
  if(!t.querySelector('.kStart')){ const h=document.createElement('div'); h.className='kStart'; h.style.order='40'; h.textContent='⭐ Start here'; t.appendChild(h); START.forEach(([l,fn],i)=>{ const b=document.createElement('button'); b.type='button'; b.className='ttMusic kStartB'; b.textContent=l; b.style.order=String(41+i); b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); fn(); }); t.appendChild(b); }); } }
 /* the control panel: the same switch at the top; on Easy the technical drawers step aside */
 function panelLv(){ const p=$('kPanel'); if(!p||p.hidden) return; let r=p.querySelector('.kLvlRow'); if(!r){ r=document.createElement('div'); r.className='kLvlRow'; const head=p.querySelector('.kpHead'); if(head) head.insertAdjacentElement('afterend',r); else p.prepend(r); r.addEventListener('click',e=>{ const b=e.target.closest('[data-lv]'); if(b){ e.stopPropagation(); setLv(b.dataset.lv); } }); } r.innerHTML=row();
  p.querySelectorAll('details').forEach(d=>{ const t=(d.querySelector('summary')||{}).textContent||''; const tech=/^(⧉|🎛|🔊)/.test(t.trim()); const show=lv==='pro'||(lv==='avg'&&!/^⧉/.test(t.trim()))||!tech; d.hidden=!show; }); }
 try{ new MutationObserver(()=>panelLv()).observe(document.body,{childList:true}); }catch(_){ }
 setInterval(()=>{ tag(); rail(); menu(); const p=$('kPanel'); if(p&&!p.hidden&&!p.querySelector('.kLvlRow')) panelLv(); },1000);
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdPanel')) setTimeout(panelLv,30); },true);
 apply(true); menu();
 window.KLEVEL={get:()=>lv,set:setLv,levels:LV.map(x=>x[0]),factory:'avg'};
})();
