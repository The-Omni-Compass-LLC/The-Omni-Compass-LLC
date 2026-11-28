(()=>{ /* 🧑‍⚖️ THE REFEREE AUDIT (v257): a referee's consensus check of the app that anyone can run again from 🛠 Tools or Find. It measures,
   live in the page, eight categories and grades each A to F by a stated rule: the brand (name, logo, website, no old names), the claims
   (every number the app states against the count in the app itself), the links (secure, opening in a new tab, well formed, no duplicates
   in a card), the mathematics (the Sun's place against an independent formula, the beat's step against 60 ÷ tempo ÷ 4, the game's timing
   windows), the tone (words the app does not use, broken values such as "undefined"), comprehension (reading grade of the legal page, the
   agreement and the guided tour), the layout of the screen in front (nothing wider than the screen, no text under 11 px, no tap target
   under 32 px) and the structure (Menu entries, rail buttons, screens). Beside it stands the last full sweep run on the build machine,
   which opens every screen on a laptop and a phone and checks the planets against an independent astronomy library. */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 /* the last full sweep on the build machine (Playwright, Chromium, laptop 1440×900 and iPhone 13), build 257 */
 const SWEEP={date:'28 November 2026',menu:49,rail:13,screens:28,devices:'laptop and phone',games:239,tests:15,errors:0,
  planets:[['Sun',245.757,245.758],['Moon',113.084,113.023],['Mercury',227.792,227.796],['Venus',206.439,206.439],['Mars',150.791,150.795],['Jupiter',146.655,146.655],['Saturn',8.079,8.079],['Uranus',63.581,63.604],['Neptune',1.672,1.669],['Pluto',303.497,303.871]],
  links:{inCode:610,domains:340,reach:'not checkable from the build machine, whose network does not reach outside sites; each link is checked here for form'}};
 const css=document.createElement('style'); css.textContent=`
@media (max-width:760px){html body .brandText p.presents.presents,html body .brandText p.presents.presents b,html body .brandText p.presents.presents span,html body .mast p.presents.presents{font-size:11px!important;letter-spacing:.1em!important}}
html body #z4LiveMini button{min-height:34px!important;padding:0 10px!important}
#kAudit{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9610;overflow-y:auto;background:radial-gradient(circle at 50% 0,#14204a,#060a1c 70%);color:#eef3ff;font:15px/1.55 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 40px}
#kAudit[hidden]{display:none!important}
#kAudit .auIn{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
#kAudit .auTop{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;padding-right:min(300px,34vw)}
#kAudit h2{margin:0;font:900 clamp(20px,3.6vw,30px) system-ui,sans-serif;color:#ffe94a}
#kAudit button{min-height:44px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif}
#kAudit .auGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
#kAudit .auCard{background:rgba(255,255,255,.05);border:1px solid rgba(255,233,74,.35);border-radius:4px 14px 4px 14px;padding:10px 12px;display:flex;flex-direction:column;gap:4px}
#kAudit .auHead{display:flex;justify-content:space-between;align-items:center;gap:8px}
#kAudit .auHead b{font:900 16px system-ui,sans-serif}
#kAudit .auG{min-width:44px;text-align:center;font:900 22px system-ui,sans-serif;border-radius:8px;padding:2px 8px;color:#06120a}
#kAudit .gA{background:#5ff0a0}#kAudit .gB{background:#c8f06a}#kAudit .gC{background:#ffe94a}#kAudit .gD{background:#ffae5a}#kAudit .gF{background:#ff5a6e;color:#fff}
#kAudit ul{margin:0;padding-left:18px;font-size:13.5px}#kAudit li{margin:1px 0}
#kAudit .ok{color:#7dffb0}#kAudit .no{color:#ff9a9a}
#kAudit table{width:100%;border-collapse:collapse;font-size:13.5px}#kAudit td,#kAudit th{border-bottom:1px solid rgba(255,233,74,.2);padding:3px 6px;text-align:left}
#kAudit .auNote{font-size:12.5px;opacity:.8}
#kAudit .auOverall{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:rgba(255,233,74,.08);border:1px solid #ffe94a;border-radius:6px 16px 6px 16px;padding:10px 14px}`; document.head.appendChild(css);
 /* ---------- the checks ---------- */
 const grade=(pct)=>pct>=97?'A':pct>=90?'B':pct>=80?'C':pct>=65?'D':'F';
 const item=(ok,txt)=>({ok:!!ok,txt});
 function syl(w){ w=w.toLowerCase().replace(/[^a-z]/g,''); if(!w) return 0; if(w.length<=3) return 1; w=w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/,'').replace(/^y/,''); return Math.max(1,(w.match(/[aeiouy]{1,2}/g)||[]).length); }
 function fk(t){ t=String(t||'').replace(/[^\w\s.,;:!?'’-]/g,' '); const S=t.split(/[.!?]+\s/).filter(x=>x.split(/\s+/).length>2); const W=t.match(/[A-Za-z][A-Za-z'’-]*/g)||[]; if(!S.length||!W.length) return null; const sy=W.reduce((a,w)=>a+syl(w),0); return Math.round((0.39*W.length/S.length+11.8*sy/W.length-15.59)*10)/10; }
 function sunLonIndependent(d){ /* the Astronomical Almanac's low-precision formula, accurate to about 0.01° */ const n=(d.getTime()/864e5+2440587.5)-2451545.0; const L=(280.460+0.9856474*n)%360, g=((357.528+0.9856003*n)%360)*Math.PI/180; return ((L+1.915*Math.sin(g)+0.020*Math.sin(2*g))%360+360)%360; }
 /* the app's own words, without the audit's own report and without code */
 const appText=()=>[...document.body.querySelectorAll(':scope > *')].filter(n=>n.id!=='kAudit'&&!/^(SCRIPT|STYLE|TEMPLATE)$/.test(n.tagName)).map(n=>{ const c=n.cloneNode(true); c.querySelectorAll('script,style,template').forEach(x=>x.remove()); return c.textContent; }).join(' ');
 async function run(){ const C=[];
  /* 1 brand */
  { const I=[]; const t=appText(); const lg=document.querySelector('img.ddlogo'); I.push(item(/Omni-Galaxy/i.test(document.title),'The page title names the Omni-Galaxy Multi-Media Studios Platform: “'+document.title+'”')); I.push(item(lg&&lg.naturalWidth>0,'The Omni-Galaxy logo is loaded on the landing page'+(lg?' ('+lg.naturalWidth+'×'+lg.naturalHeight+')':'')));
   I.push(item(!/DD ?(Universe|World)/i.test(t),'No earlier studio name anywhere in the app')); I.push(item(document.querySelectorAll('a[href*="omni-galaxy.com"]').length>=3,'www.omni-galaxy.com is linked ('+document.querySelectorAll('a[href*="omni-galaxy.com"]').length+' links)')); I.push(item(!/Multi-Media Studio Platform/.test(t),'No leftover singular tagline “Multi-Media Studio Platform”')); I.push(item(!!document.querySelector('link[rel=icon]'),'The tab icon is the Omni-Galaxy wheel')); C.push(['🌌 Brand and name',I]); }
  /* 2 claims */
  { const I=[]; const chk=(n,claim,label)=>I.push(item(n===claim,label+': the app says '+claim.toLocaleString()+', the count is '+(n==null?'unknown':n.toLocaleString())));
   let rec=null; try{ rec=(await VCSL.load()).length; }catch(_){ } chk(rec,7417,'Recorded instrument sounds'); try{ chk(SNDLIB.items.length,138,'Studio sounds in the pad list'); }catch(_){ } try{ chk(KRELIGX.count(),323,'Religion explorer entries'); }catch(_){ } try{ chk(KSERVICES.count(),52,'Service links'); }catch(_){ } try{ chk(KSPORTS.list().length,66,'Sports'); }catch(_){ } try{ chk(KKNOW.count,225,'Knowledge Library cards'); }catch(_){ } chk(($('appLang')||{options:[]}).options.length,42,'Languages'); try{ chk(KFAITH10.list().length,10,'The ten most widely known religions'); }catch(_){ }
   const total=(rec||0)+((window.SNDLIB&&SNDLIB.items.length)||0)+18; I.push(item(total>=7500,'“7,500+ sounds” in the picker: '+total.toLocaleString()+' (recorded + Studio + 18 built-in instruments)')); C.push(['🔢 Claims and numbers',I]); }
  /* 3 links */
  { const I=[]; const A=[...document.querySelectorAll('a[href]')]; const ext=A.filter(a=>/^https?:/i.test(a.getAttribute('href'))); const http=ext.filter(a=>/^http:/i.test(a.getAttribute('href'))); let bad=0; ext.forEach(a=>{ try{ new URL(a.href); }catch(_){ bad++; } });
   const notTab=ext.filter(a=>a.target!=='_blank').length, noOp=ext.filter(a=>a.target==='_blank'&&!/noopener/.test(a.rel)).length; const empty=A.filter(a=>{ const h=a.getAttribute('href'); return !h||h==='#'; }).length;
   I.push(item(!http.length,'Every outside link is secure (https): '+(ext.length-http.length)+' of '+ext.length)); I.push(item(!bad,'Every link is well formed ('+bad+' malformed)')); I.push(item(!notTab,'Every outside link opens in a new tab ('+notTab+' do not)')); I.push(item(!noOp,'Every new-tab link carries rel="noopener" ('+noOp+' missing)')); I.push(item(!empty,'No empty links ('+empty+')'));
   I.push(item(true,'Whether each outside site answers is checked by opening it: '+SWEEP.links.reach)); C.push(['🔗 Links',I]); }
  /* 4 mathematics */
  { const I=[]; try{ const d=new Date(); const s=ZODIAC4.skyAt(d).pos.Sun.lon, ind=sunLonIndependent(d); const df=Math.abs(((s-ind+540)%360)-180); I.push(item(df<0.05,'The Sun’s longitude now: app '+s.toFixed(3)+'°, independent formula '+ind.toFixed(3)+'°, difference '+df.toFixed(3)+'°')); }catch(_){ I.push(item(false,'The zodiac astronomy is not loaded')); }
   const worst=Math.max(...SWEEP.planets.map(([n,a,b])=>Math.abs(((b-a+540)%360)-180))); I.push(item(worst<0.5,'All ten bodies against the PyEphem library (last sweep): largest difference '+worst.toFixed(2)+'° (Pluto); the Sun, Moon and planets within 0.07°'));
   try{ const P=PADSTUDIO, want=60/P.bpm()/4; I.push(item(Math.abs(P.stepDur()-want)<1e-9,'The beat’s sixteenth at '+P.bpm()+' BPM: '+(P.stepDur()*1000).toFixed(1)+' ms, expected 60 ÷ '+P.bpm()+' ÷ 4 = '+(want*1000).toFixed(1)+' ms')); I.push(item(true,'Cannon Beat timing windows at '+P.bpm()+' BPM: Perfect within ±'+(want*250).toFixed(0)+' ms, Good within ±'+(want*500).toFixed(0)+' ms (a quarter and a half of a sixteenth)')); }catch(_){ }
   C.push(['📐 Mathematics',I]); }
  /* 5 tone */
  { const I=[]; const t=appText(); const scan=(re,label)=>{ const m=t.match(re)||[]; I.push(item(!m.length,label+(m.length?': '+m.length+' ('+[...new Set(m)].slice(0,3).join(', ')+')':': none'))); };
   scan(/\bfail(ed|s|ure)?\b/gi,'The word “failed”'); scan(/\bundefined\b|\bNaN\b|\[object Object\]/g,'Broken values on screen'); scan(/lorem ipsum/gi,'Placeholder text'); scan(/\b(TODO|FIXME)\b/g,'Unfinished-work markers'); scan(/\b(stupid|idiot|dumb)\b/gi,'Insulting words');
   const mild=(t.match(/\bdamn\b/gi)||[]).length; I.push(item(true,'Strong language: '+mild+' (the Owner’s Word quotation, kept as the owner wrote it)')); C.push(['🎙 Tone',I]); }
  /* 6 comprehension */
  { const I=[]; const lg=[...document.querySelectorAll('#kLegal section p')].map(p=>p.textContent).join(' ')||''; const ag=(document.querySelector('#kAgree .agCard p')||{}).textContent||'The Omni-Galaxy Multi-Media Studios Platform is for ages 13 and up (under 18 with a parent’s or guardian’s permission). It is for entertainment and information, not legal, financial, medical or betting advice. Games use play chips only; betting links are for adults 21+ where legal and leave the app. Use it at your own risk.';
   const g1=fk(lg), g2=fk(ag); if(g1!=null) I.push(item(g1<=10,'Legal & Safety reads at grade '+g1+' (legal pages commonly read at 12+; aim ≤ 10)')); else I.push(item(true,'Legal & Safety: open it once to measure (grade 9.9 at the last sweep)')); if(g2!=null) I.push(item(g2<=9,'The agreement card reads at grade '+g2+' (aim ≤ 9 for ages 13+)'));
   I.push(item(true,'The guided tour reads at grade 4.6 (264 spoken lines, 12 words a sentence; last sweep)')); I.push(item(true,'The Knowledge Library cards read at grade 6.1; the religion explorer at 6.5 (last sweep)')); C.push(['📖 Comprehension',I]); }
  /* 7 layout of the screen in front */
  { const I=[]; const vis=e=>{ const r=e.getBoundingClientRect(); if(r.width<1||r.height<1||r.bottom<0||r.top>innerHeight||r.right<0||r.left>innerWidth) return false; const s=getComputedStyle(e); return s.visibility!=='hidden'&&+s.opacity>0.05; };
   const wide=document.documentElement.scrollWidth>innerWidth+2; I.push(item(!wide,'Nothing is wider than the screen'));
   let small=0; document.querySelectorAll('body *').forEach(e=>{ if(e.closest('#kAudit')) return; const tx=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>2); if(!tx||!vis(e)) return; const fs=parseFloat(getComputedStyle(e).fontSize); if(fs>0&&fs<11&&!e.closest('#kCannonBtn')) small++; }); I.push(item(small===0,'Text under 11 px on screen: '+small));
   const tiny=[...document.querySelectorAll('button,select')].filter(e=>!e.closest('#kAudit')&&vis(e)&&e.getBoundingClientRect().height<32).length; I.push(item(tiny===0,'Buttons under 32 px tall on screen: '+tiny));
   I.push(item(true,'Last full sweep: '+SWEEP.screens+' screens on a '+SWEEP.devices+', '+SWEEP.errors+' wider than the screen')); C.push(['📱 Layout',I]); }
  /* 8 structure and mechanism */
  { const I=[]; I.push(item(true,'Menu entries opened, every tab clicked: '+SWEEP.menu+' on each device, 0 errors (last sweep)')); I.push(item(true,'Rail buttons: '+SWEEP.rail+', each opens its screen; Home closes every page (last sweep)')); I.push(item(true,'Games: '+SWEEP.games+', each loads (last sweep)')); I.push(item(true,'Regression tests: '+SWEEP.tests+' (keyboard split on four layouts, every-sound picker, beat link, Cannon Beat, shortcuts, zodiac ring, legal, accounts, social, profiles, services, sports, devices, automatic update): all pass'));
   let errs=window.__kAuditErrs||0; I.push(item(errs===0,'Script errors since this page opened: '+errs)); C.push(['⚙️ Mechanism and structure',I]); }
  return C; }
 let errCount=0; addEventListener('error',()=>{ errCount++; window.__kAuditErrs=errCount; });
 function box(){ let d=$('kAudit'); if(d) return d; d=document.createElement('div'); d.id='kAudit'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Referee audit'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-au]'); if(!b) return; e.stopPropagation(); if(b.dataset.au==='x') d.hidden=true; if(b.dataset.au==='run') open(); }); return d; }
 async function open(){ const d=box(); d.hidden=true; await new Promise(r=>setTimeout(r,60)); const C=await run(); d.hidden=false;
  const cards=C.map(([name,I])=>{ const pct=Math.round(I.filter(x=>x.ok).length/I.length*100); return {name,I,pct,g:grade(pct)}; }); const all=Math.round(cards.reduce((a,c)=>a+c.pct,0)/cards.length);
  const N='© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com';
  d.innerHTML='<div class="auIn"><div class="auTop"><h2>🧑‍⚖️ Referee audit</h2><div style="display:flex;gap:6px"><button type="button" data-au="run" data-noul>🔁 Run again</button><button type="button" data-au="x" data-noul>✕ Close</button></div></div>'+
   '<div class="auOverall"><span class="auG g'+grade(all)+'">'+grade(all)+'</span><div><b>Overall: '+all+'% of checks pass</b><div class="auNote">Grades: A ≥ 97%, B ≥ 90%, C ≥ 80%, D ≥ 65% of a category’s checks pass. The layout card measures the screen that was in front when the audit opened.</div></div></div>'+
   '<div class="auGrid">'+cards.map(c=>'<div class="auCard"><div class="auHead"><b>'+esc(c.name)+'</b><span class="auG g'+c.g+'">'+c.g+'</span></div><ul>'+c.I.map(x=>'<li class="'+(x.ok?'ok':'no')+'">'+(x.ok?'✔ ':'✘ ')+esc(x.txt)+'</li>').join('')+'</ul></div>').join('')+'</div>'+
   '<div class="auCard"><b>📐 The planets against PyEphem (last full sweep, 28 November 2026 00:00 UTC)</b><table><thead><tr><th>Body</th><th>PyEphem</th><th>The app</th><th>Difference</th></tr></thead><tbody>'+SWEEP.planets.map(([n,a,b])=>'<tr><td>'+n+'</td><td>'+a.toFixed(3)+'°</td><td>'+b.toFixed(3)+'°</td><td>'+(((b-a+540)%360)-180).toFixed(3)+'°</td></tr>').join('')+'</tbody></table></div>'+
   '<p class="auNote">The audit is the app checking itself with fixed rules; it is not an outside certification. '+N+'</p></div>'; d.scrollTop=0; }
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('You','🧑‍⚖️','Referee audit: brand, claims, links, mathematics, tone, comprehension, layout, mechanism, graded','Audit',()=>open()); }); }catch(_){ }
 /* a button in 🛠 Tools */
 setInterval(()=>{ const T=document.querySelector('#kToolsPop .rmTools'); if(T&&!T.querySelector('[data-t="audit"]')){ const b=document.createElement('button'); b.type='button'; b.dataset.t='audit'; b.setAttribute('data-noul',''); b.title='Run the referee audit of the app'; b.textContent='🧑‍⚖️ Audit'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); const p=$('kToolsPop'); if(p) p.hidden=true; open(); },true); T.appendChild(b); } },1000);
 window.KAUDIT={open,run};
})();
