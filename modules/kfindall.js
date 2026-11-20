(()=>{ /* 🔎 ASK OR SEARCH (v219): one window, reachable from every screen (🔎 Find on the rail, the / key, or Ctrl/⌘ K). Type or
   talk; it searches everything KAN-IN holds (every screen and Menu item, every game, the 1,000 recipes, the Studio's sections, the
   knowledge library) and takes you straight there. When nothing matches, the question goes to the AI, which can answer it or open
   the right place itself. */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const css=document.createElement('style'); css.textContent=`
#kFind{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9785;background:rgba(6,4,20,.97);display:flex;flex-direction:column;padding:calc(10px + env(safe-area-inset-top,0px)) 12px 12px;color:#fff;font:15px/1.4 system-ui,sans-serif}
#kFind[hidden]{display:none!important}
#kFind .fdTop{display:flex;gap:8px;align-items:center;max-width:900px;width:100%;margin:0 auto}
#kFind input{flex:1 1 auto;min-width:0;min-height:52px;border-radius:14px;border:2px solid #6fe8ff;background:#0c1a33;color:#fff;font:18px system-ui,sans-serif;padding:0 14px}
#kFind .fdX{min-height:52px;min-width:52px;border-radius:999px!important;background:#b3172f!important;color:#fff!important;font:900 18px system-ui!important;border:2px solid #fff!important}
#kFind .fdList{flex:1 1 auto;overflow-y:auto;max-width:900px;width:100%;margin:8px auto 0;-webkit-overflow-scrolling:touch}
#kFind h4{margin:12px 0 4px;font:900 13px ui-monospace,monospace;letter-spacing:.1em;color:#6fe8ff;text-transform:uppercase}
#kFind .fdR{display:flex;align-items:center;gap:10px;width:100%;min-height:52px;text-align:left;border-radius:12px!important;padding:6px 12px!important;margin:4px 0;background:#13223f!important;color:#fff!important;border:1px solid rgba(111,232,255,.25)!important;font:700 15px system-ui,sans-serif!important}
#kFind .fdR small{display:block;font:600 12px system-ui,sans-serif;color:#9fd8e8}
#kFind .fdR i{font-style:normal;font-size:22px;flex:none;width:30px;text-align:center}
#kFind .fdAI{background:linear-gradient(180deg,#ffd84a,#e0a10c)!important;color:#1a1200!important}
#kFind .fdAI small{color:#4a3800}
#kFind .fdHint{font:600 13px system-ui,sans-serif;color:#9fb3d8;max-width:900px;margin:6px auto 0;width:100%}`; document.head.appendChild(css);
 let IDX=null;
 function build(){ const L=[]; const add=(grp,icon,label,sub,go)=>L.push({grp,icon,label,sub:sub||'',go,t:(label+' '+(sub||'')).toLowerCase()});
  const t=$('tourTab'); if(t) [...t.querySelectorAll('button')].forEach(b=>{ if(b.closest('.kLvlRow')) return; const tx=(b.textContent||'').trim().replace(/\s+/g,' '); if(!tx||tx.length>80) return; add('Places in KAN-IN','📍',tx,'from the Menu',()=>{ b.click(); }); });
  [['🏠 Home',()=>{ try{ GOHOME(); }catch(_){ } }],['🎛 Studio',()=>KRAIL.goTo('pad')],['🎤 Karaoke',()=>KKARA.open()],['🤖 AI',()=>KAI.open()],['🍳 Recipes',()=>KREC.open()],['⌨ Keyboards and controllers',()=>KKBD.open()],['🎵 Music',()=>KRAIL.goTo('musicDock')],['👤 My profile',()=>KPROFILE.open()],['🌐 Social',()=>KSOCIAL.open()],['📁 Projects',()=>KPROJ.open()],['🎨 Easel',()=>KEASEL.open()],['🕹 All games',()=>KRAIL.goTo('gamesDock')],['🎓 Knowledge library',()=>KKNOW.open()],['🔒 Lock & shuffle',()=>KLOCK.open()]].forEach(([l,f])=>add('Places in KAN-IN',l.split(' ')[0],l.slice(l.indexOf(' ')+1),'screen',()=>{ try{ f(); }catch(_){ } }));
  try{ (KEYMAP.SECTIONS||[]).forEach(([,n,sel])=>add('Studio','🎛',n,'Studio section',()=>{ KRAIL.goTo('pad'); setTimeout(()=>{ const e=document.querySelector(sel); if(e) e.scrollIntoView({block:'start',behavior:'smooth'}); },1300); })); }catch(_){ }
  [['🎚 Mixer · 40 tracks','#padMixer'],['🎚 40-track sequencer','#k40Seq'],['🧭 Omni-Compass governors','#kGovBoard'],['🎛 Console returns · reverb and echo','#kFXRet'],['🎚 Inputs','#kIO']].forEach(([n,sel])=>add('Studio','🎛',n.slice(n.indexOf(' ')+1),'Studio',()=>{ KRAIL.goTo('pad'); setTimeout(()=>{ if(sel==='#k40Seq'){ try{ K40.tab('40'); }catch(_){ } } const e=document.querySelector(sel); if(e) e.scrollIntoView({block:'start',behavior:'smooth'}); },1300); }));
  try{ GAMES.list.forEach(g=>add('Games','🕹',g.name,g.cat,()=>{ try{ KRAIL.goTo('gamesDock'); }catch(_){ } setTimeout(()=>GAMES.open(g.id),300); })); }catch(_){ }
  try{ KREC.dishes().forEach(d=>add('Recipes','🍳',d.name,d.cul+' · '+d.ing,()=>KREC.open(d.name))); }catch(_){ }
  IDX=L; return L; }
 function search(q){ const L=IDX||build(); const words=q.toLowerCase().split(/\s+/).filter(Boolean); if(!words.length) return [];
  let R=L.map(x=>{ let s=0; for(const w of words){ const i=x.t.indexOf(w); if(i<0) return null; s+=(i===0?6:x.t.indexOf(' '+w)>=0?3:1)+(x.label.toLowerCase().includes(w)?4:0); } return [s,x]; }).filter(Boolean);
  if(!R.length) R=L.map(x=>{ const s=words.filter(w=>x.t.includes(w)).length; return s?[s,x]:null; }).filter(Boolean);
  const seen=new Set(); return R.sort((a,b)=>b[0]-a[0]).map(r=>r[1]).filter(x=>{ const k=x.grp+'|'+x.label; if(seen.has(k)) return false; seen.add(k); return true; }); }
 function box(){ let b=$('kFind'); if(b) return b; b=document.createElement('div'); b.id='kFind'; b.hidden=true; b.setAttribute('role','dialog'); b.setAttribute('aria-label','Ask or search');
  b.innerHTML='<div class="fdTop"><input id="fdQ" type="search" placeholder="Ask or search anything in KAN-IN…" aria-label="Ask or search" autocomplete="off"><button type="button" class="fdX" data-fd="x" aria-label="Close">✕</button></div><div class="fdHint">Type or tap 🎤 and talk: a screen, a game, a dish, a knob, a question. Enter opens the top result.</div><div class="fdList" id="fdList"></div>';
  document.body.appendChild(b); let res=[];
  const draw=()=>{ const q=$('fdQ').value.trim(); res=search(q); const L=$('fdList'); if(!q){ L.innerHTML=''; return; } const groups={}; res.slice(0,60).forEach((x,i)=>{ (groups[x.grp]=groups[x.grp]||[]).push([x,i]); });
   L.innerHTML=Object.entries(groups).map(([g,xs])=>'<h4>'+esc(g)+' · '+xs.length+'</h4>'+xs.slice(0,g==='Recipes'||g==='Games'?12:10).map(([x,i])=>'<button type="button" class="fdR" data-i="'+i+'"><i>'+x.icon+'</i><span>'+esc(x.label)+'<small>'+esc(x.sub)+'</small></span></button>').join('')).join('')
    +'<h4>Ask the AI</h4><button type="button" class="fdR fdAI" data-fd="ai"><i>🤖</i><span>'+(res.length?'Ask the AI: “':'Nothing found here. Ask the AI: “')+esc(q)+'”<small>It answers, or opens the right place for you</small></span></button>'
    +'<button type="button" class="fdR" data-fd="know"><i>🎓</i><span>Look it up in the knowledge library<small>“'+esc(q)+'”</small></span></button>'; };
  b.addEventListener('input',e=>{ if(e.target.id==='fdQ') draw(); });
  b.addEventListener('keydown',e=>{ if(e.target.id==='fdQ'&&e.key==='Enter'){ e.preventDefault(); if(res[0]) go(res[0]); else ask(); } });
  b.addEventListener('click',e=>{ const t=e.target.closest('button'); if(!t) return; e.stopPropagation(); if(t.dataset.fd==='x') return close(); if(t.dataset.fd==='ai') return ask(); if(t.dataset.fd==='know') return know(); const x=res[+t.dataset.i]; if(x) go(x); });
  return b; }
 function go(x){ close(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>{ try{ x.go(); }catch(_){ } },80); }
 function ask(){ const q=$('fdQ').value.trim(); close(); try{ KAI.open(); setTimeout(()=>{ try{ KAI.send(q); }catch(_){ } },350); }catch(_){ } }
 function know(){ const q=$('fdQ').value.trim(); close(); try{ KKNOW.open(); setTimeout(()=>{ const k=$('knQ'); if(k){ k.value=q; k.dispatchEvent(new Event('input',{bubbles:true})); } },250); }catch(_){ } }
 function open(q){ IDX=null; const b=box(); b.hidden=false; const i=$('fdQ'); i.value=q||''; i.dispatchEvent(new Event('input',{bubbles:true})); setTimeout(()=>{ try{ i.focus(); }catch(_){ } },30); }
 function close(){ const b=$('kFind'); if(b) b.hidden=true; }
 document.addEventListener('keydown',e=>{ const b=$('kFind'); if(e.key==='Escape'&&b&&!b.hidden){ e.stopPropagation(); close(); return; } const t=e.target; const typing=t&&(t.isContentEditable||/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)); if(document.body.classList.contains('gated')) return;
  if(((e.ctrlKey||e.metaKey)&&(e.key||'').toLowerCase()==='k')||(!typing&&e.key==='/')){ e.preventDefault(); e.stopPropagation(); open(); } },true);
 setInterval(()=>{ const d=$('rDock'); if(d&&!$('kdFind')){ const b=document.createElement('button'); b.type='button'; b.id='kdFind'; b.setAttribute('data-noul',''); b.dataset.kdI='🔎'; b.dataset.kdL='Find'; b.title='Ask or search anything (/ or Ctrl+K)'; b.setAttribute('aria-label','Ask or search'); b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); const m=$('lpMenu'); if(m&&m.nextSibling) d.insertBefore(b,m.nextSibling); else d.appendChild(b); } },1000);
 const css2=document.createElement('style'); css2.textContent='html body #rDock#rDock #kdFind{order:3!important;display:flex!important}'; document.head.appendChild(css2);
 window.KFINDALL={open,close,search:q=>search(q).slice(0,20).map(x=>x.grp+': '+x.label)};
})();
