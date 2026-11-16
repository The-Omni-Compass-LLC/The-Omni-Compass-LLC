(()=>{ /* online / offline status, screen addresses (#zodiac, #beats …), and the profile with the daily reading */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const getLS=(k,d)=>{ try{ const v=JSON.parse(localStorage.getItem(k)||'null'); return v==null?d:v; }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){} };
 const say=t=>{ try{ toast(t); }catch(_){} };
 const css=document.createElement('style'); css.textContent=`
#kNet{position:fixed;left:max(12px,env(safe-area-inset-left,0px));bottom:calc(70px + env(safe-area-inset-bottom,0px));z-index:9060;display:inline-flex;align-items:center;gap:6px;min-height:34px;padding:0 10px;border-radius:999px;border:1px solid rgba(255,255,255,.28);background:rgba(6,10,28,.92);color:#e8f0ff;font:700 12.5px system-ui,sans-serif;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.4)}
#kNet.mini{width:30px;min-width:30px;padding:0;justify-content:center}#kNet.mini span{display:none}#kNet i{flex:none;width:10px;height:10px;border-radius:50%;background:#7dff8a;box-shadow:0 0 8px #7dff8a}#kNet.off i{background:#ff6a6a;box-shadow:0 0 8px #ff6a6a}#kNet.hold i{background:#ffe94a;box-shadow:0 0 8px #ffe94a}
@media (max-width:760px){#kNet{bottom:calc(74px + env(safe-area-inset-bottom,0px));min-height:30px;font-size:11.5px;padding:0 8px}}
#kNetCard,#kMe,#kDay{position:fixed;inset:0;z-index:9500;display:flex;align-items:flex-start;justify-content:center;overflow:auto;background:rgba(2,4,14,.78);box-sizing:border-box;padding:calc(12px + env(safe-area-inset-top,0px)) max(10px,env(safe-area-inset-right,0px)) calc(90px + env(safe-area-inset-bottom,0px)) max(10px,env(safe-area-inset-left,0px))}
.kPanel{box-sizing:border-box;width:min(720px,100%);background:linear-gradient(180deg,#0d1640,#070b22);border:1px solid rgba(255,233,74,.55);border-radius:16px;padding:14px;color:#eef;font:400 15px/1.5 system-ui,sans-serif;text-align:left;text-transform:none;letter-spacing:0}
.kPanel h3{margin:0 0 6px;font:800 20px/1.25 system-ui,sans-serif;color:#ffe94a;text-wrap:balance}.kPanel h4{margin:12px 0 6px;font:800 12px ui-monospace,monospace;letter-spacing:.14em;color:#7ff;text-transform:uppercase}
.kPanel p{margin:0 0 8px;color:#d4dcf6}.kPanel .kRowB{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}.kPanel .kGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.kPanel label{display:flex;flex-direction:column;gap:4px;font:700 13px system-ui,sans-serif;color:#cfe}.kPanel input,.kPanel select{box-sizing:border-box;width:100%;min-height:42px;border-radius:10px;border:1px solid rgba(255,255,255,.3);background:#0b1535;color:#fff;padding:0 10px;font:500 15px system-ui,sans-serif}
.kPanel .kChk{flex-direction:row;align-items:center;gap:8px;font-weight:600}.kPanel .kChk input{width:22px;min-height:22px}
:is(.kPanel,html) .kPanel button{min-height:42px;padding:0 12px;border-radius:10px;border:1px solid rgba(255,255,255,.28)!important;background:#111c40!important;color:#e8f0ff!important;font:700 13.5px system-ui,sans-serif;cursor:pointer;width:auto;text-transform:none;letter-spacing:0}
:is(.kPanel,html) .kPanel button.kHot{background:#ffe94a!important;color:#14101c!important}:is(.kPanel,html) .kPanel button.kGo{background:#12a85a!important;color:#02170a!important}:is(.kPanel,html) .kPanel button.kX{background:#3a1420!important;color:#ffd9df!important}:is(.kPanel,html) .kPanel button.on{outline:2px solid #ffe94a}
.kPanel .kSigns{display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:6px}.kPanel .kRead{border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:10px;background:rgba(255,255,255,.03);overflow-wrap:anywhere}.kPanel .kRead div{margin:0 0 6px}.kPanel .kRead table{width:100%;border-collapse:collapse;font-size:13px}.kPanel .kRead td,.kPanel .kRead th{border-top:1px solid rgba(255,255,255,.1);padding:4px;text-align:left}.kPanel .kTblW{overflow-x:auto}
.kPanel a{color:#7ff}.kPanel .kSmall{font-size:12.5px;color:#9fb0d6}`;
 document.head.appendChild(css);

 /* ===== 1. online / offline ===== */
 const NET={ mode:getLS('kanin-net-mode','auto'), online:navigator.onLine!==false, checked:0 };
 const LIMITS=['🧠 The AI Brain (writing, lyrics, translation by AI, Ask answers by AI)','🌐 Online sound and music libraries, and searches','🖼 AI pictures and the AI video studios (they open other websites)','🔗 Links to outside sites: daily horoscopes, dictionaries, video makers','🆕 New versions of KAN-IN (you get them when you are back online)'];
 const WORKS='Everything made on your device keeps working: the story engine and Quick Pick, the Beat Maker and its sounds, the games, LuvMyZodiac’s charts and today’s sky (computed on your device), your saved files and the library.';
 const chip=document.createElement('button'); chip.type='button'; chip.id='kNet'; chip.setAttribute('data-noul',''); chip.setAttribute('aria-live','polite'); document.body.appendChild(chip);
 const isOn=()=>NET.mode!=='offline'&&NET.online;
 function paint(){ const off=!NET.online, hold=NET.mode==='offline'; chip.classList.toggle('off',off&&!hold); chip.classList.toggle('hold',hold); chip.innerHTML='<i></i><span>'+(hold?'Offline mode (by choice)':off?'Offline':'Online')+'</span>'; chip.classList.toggle('mini',!off&&!hold); chip.setAttribute('aria-label',hold?'Offline mode, by your choice. Tap to change it.':off?'Offline. Tap to see what still works.':'Online. Tap for the connection settings.'); chip.title=hold?'You chose offline mode. Tap to change it.':off?'No internet. Tap to see what still works.':'Connected. Tap for the connection settings.'; document.documentElement.classList.toggle('kOffline',!isOn()); }
 let lastSaid=null;
 function setOnline(v,quiet){ const was=NET.online; NET.online=v; paint(); if(quiet||was===v||NET.mode==='offline') return; if(lastSaid===v) return; lastSaid=v;
  if(!v) say('📴 You are offline. KAN-IN keeps working; the AI Brain, online libraries and outside links wait until you are back online. Tap the Offline button at the bottom left for details.'); else say('🟢 You are back online. Everything is available again.'); }
 async function probe(){ NET.checked=Date.now(); if(navigator.onLine===false){ setOnline(false); return; } try{ const c=new AbortController(); const t=setTimeout(()=>c.abort(),6000); const r=await fetch('version.json?n='+Date.now(),{cache:'no-store',signal:c.signal}); clearTimeout(t); setOnline(r.ok||r.status<500); }catch(_){ setOnline(false); } }
 window.addEventListener('online',()=>probe()); window.addEventListener('offline',()=>setOnline(false));
 setTimeout(probe,1500); setInterval(()=>{ if(NET.mode!=='offline') probe(); },NET.online?180000:30000); setInterval(()=>{ if(!NET.online&&NET.mode!=='offline') probe(); },30000);
 /* the factory setting tries to go online; offline by choice keeps the app from reaching out */
 const rawFetch=window.fetch.bind(window);
 window.fetch=function(u,o){ try{ if(NET.mode==='offline'){ const url=new URL(typeof u==='string'?u:(u&&u.url)||'',location.href); if(url.origin!==location.origin) return Promise.reject(new TypeError('KAN-IN is in offline mode by your choice.')); } }catch(_){} return rawFetch(u,o); };
 function netCard(){ let d=$('kNetCard'); if(!d){ d=document.createElement('div'); d.id='kNetCard'; d.setAttribute('role','dialog'); d.setAttribute('aria-modal','true'); document.body.appendChild(d);
   d.addEventListener('click',e=>{ if(e.target===d){ d.hidden=true; return; } const b=e.target.closest('button[data-n]'); if(!b) return; const k=b.dataset.n; if(k==='x'){ d.hidden=true; return; } if(k==='auto'||k==='offline'){ NET.mode=k; putLS('kanin-net-mode',k); paint(); if(k==='auto') probe(); say(k==='auto'?'🟢 Factory setting: KAN-IN always tries to go online.':'📴 Offline mode is on. KAN-IN will not reach the internet until you switch it back.'); netCard(); } if(k==='check'){ b.textContent='Checking…'; probe().then(netCard); } }); }
  const off=!isOn();
  d.innerHTML=`<div class="kPanel"><h3>${NET.mode==='offline'?'📴 Offline mode, by your choice':off?'📴 You are offline':'🟢 You are online'}</h3>
  <p>${NET.mode==='offline'?'KAN-IN is not reaching the internet because you chose offline mode.':off?'Your phone or computer has no internet connection right now. KAN-IN keeps trying by itself every 30 seconds.':'KAN-IN is connected. The factory setting always tries to go online.'}</p>
  <h4>Connection</h4><div class="kRowB"><button type="button" data-n="auto" class="${NET.mode==='auto'?'on kGo':''}" data-noul>🌐 Always try online (factory setting)</button><button type="button" data-n="offline" class="${NET.mode==='offline'?'on kHot':''}" data-noul>📴 Stay offline</button><button type="button" data-n="check" data-noul>↻ Check the connection now</button></div>
  <h4>${off?'Waiting for the internet':'What needs the internet'}</h4><ul>${LIMITS.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>
  <h4>Works offline</h4><p>${esc(WORKS)}</p>
  <p class="kSmall">Last checked ${NET.checked?new Date(NET.checked).toLocaleTimeString():'just now'}.</p>
  <div class="kRowB"><button type="button" class="kX" data-n="x" data-noul>✕ Close</button></div></div>`; d.hidden=false; }
 chip.addEventListener('click',netCard); paint();
 window.KNET={state:()=>({mode:NET.mode,online:NET.online,on:isOn()}),probe,open:netCard,isOn};

 /* ===== 2. screen addresses: a link that ends in #zodiac, #beats … opens that screen ===== */
 const ADDR={home:'home',pad:'beats',djSec:'dj',kBand:'band',kSounds:'sounds',swDock:'songs',sbDock:'board',sbp:'book',musicDock:'music',aivDock:'video',voiceDock:'voices',langDock:'language',layDock:'layers',craftDock:'craft',mutDock:'mutate',mapDock:'map',zodDock:'zodiac',omniDock:'compass',opsHub:'hub',gamesDock:'games',askDock:'ask'};
 const BYADDR=Object.fromEntries(Object.entries(ADDR).map(([k,v])=>[v,k]));
 const EXTRA={library:()=>{ try{ STORYLIB.open(); }catch(_){} },profile:()=>openMe(),horoscope:()=>openDay(true),cannon:()=>{ try{ KCANNON.open(); }catch(_){} }};
 let routing=false;
 function route(){ const h=(location.hash||'').slice(1).toLowerCase(); if(!h||/^book-/.test(h)) return; routing=true; try{ if(EXTRA[h]) EXTRA[h](); else if(BYADDR[h]&&window.KBAR) KBAR.go(BYADDR[h]); }catch(_){} setTimeout(()=>{ routing=false; },400); }
 window.addEventListener('hashchange',route);
 let routed=false; const first=()=>{ if(routed) return; routed=true; setTimeout(route,600); };
 window.addEventListener('kanin',e=>{ if(e.detail==='gate-open') first(); }); setTimeout(first,4500);
 const mark=id=>{ if(routing) return; try{ const a=ADDR[id]; const url=location.pathname+location.search+(a&&a!=='home'?'#'+a:''); history.replaceState(null,'',url); }catch(_){} };
 const goWrap=()=>{ if(!window.KBAR||KBAR.__addr) return !!(window.KBAR&&KBAR.__addr); const g=KBAR.go; KBAR.go=function(id){ const r=g.apply(this,arguments); mark(id); return r; }; KBAR.__addr=1; return true; };
 if(!goWrap()){ const t=setInterval(()=>{ if(goWrap()) clearInterval(t); },700); }
 try{ const gh=window.GOHOME; window.GOHOME=function(){ const r=gh&&gh.apply(this,arguments); if(!routing&&location.hash&&!/^#book-/.test(location.hash)) mark('home'); return r; }; }catch(_){}
 window.KADDR={map:ADDR,route};

 /* ===== 3. the profile and the daily reading ===== */
 const SIGNS=['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces'];
 const GL=['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓'];
 const ELEM=['Fire','Earth','Air','Water'];
 const ANIMALS=['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat','Monkey','Rooster','Dog','Pig'];
 const blankP=()=>({name:'',date:'',time:'',city:'New York',sign:null,daily:true,follow:true,mode:'cannon',focus:'all',at:0});
 let P=Object.assign(blankP(),getLS('kanin-profile',{})); let acct=null;
 const sunFromDate=d=>{ const m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(d||''); if(!m) return null; const M=+m[2], D=+m[3]; const cut=[20,19,21,20,21,21,23,23,23,23,22,22]; const s=(M+8+(D>=cut[M-1]?1:0))%12; return s; };
 const signOf=()=>{ if(P.sign!=null&&P.sign!=='') return +P.sign; if(P.date&&window.ZOD4&&ZOD4.sun){ const s=ZOD4.sun(person()); if(s!=null) return s; } return sunFromDate(P.date); };
 const animalOf=d=>{ const m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(d||''); if(!m) return null; let y=+m[1]; if(+m[2]<2||(+m[2]===2&&+m[3]<5)) y--; return ANIMALS[((y-4)%12+12)%12]; };
 function person(){ try{ const p=ZOD4.blank(); p.name=P.name||'Me'; p.date=P.date; p.time=P.time||'12:00'; p.tu=!P.time; const ci=ZOD4.cityIdx(String(P.city||'').split(',')[0].trim()); if(ci>=0) p.city=ci; return p; }catch(_){ return null; } }
 async function account(){ try{ if(!window.claude||!claude.use) return null; const [db,user]=await Promise.all([claude.use('db').catch(()=>null),claude.use('user').catch(()=>null)]); if(!db||!user) return null; const id=await user.id(); if(!id) return null; return {db,ref:db.doc('data/users/'+id+'/profile')}; }catch(_){ return null; } }
 async function syncIn(){ acct=await account(); if(!acct) return; try{ const s=await acct.ref.get(); if(s&&s.exists){ const o=s.data(); if(o&&(o.at||0)>(P.at||0)){ P=Object.assign(blankP(),o); putLS('kanin-profile',P); tieZodiac(); } } else if(P.at) await acct.ref.set(P); }catch(_){} }
 async function saveP(){ P.at=Date.now(); putLS('kanin-profile',P); tieZodiac(); if(acct){ try{ await acct.ref.set(P); }catch(_){} } }
 function tieZodiac(){ if(!P.follow||!P.date||!window.ZOD4||!ZOD4.store) return; const p=person(); if(p) ZOD4.store({name:p.name,date:p.date,time:p.time,tu:p.tu,city:p.city}); }
 setTimeout(syncIn,2500);

 /* readings: cannon, manual, internet, flip, shuffle, mutate */
 const R=seed=>{ let s=(seed>>>0)||1; return ()=>{ s^=s<<13; s>>>=0; s^=s>>17; s^=s<<5; s>>>=0; return s/4294967296; }; };
 const today=()=>{ const n=new Date(); return n.getFullYear()+'-'+String(n.getMonth()+1).padStart(2,'0')+'-'+String(n.getDate()).padStart(2,'0'); };
 const SITES=s=>{ const n=SIGNS[s], l=n.toLowerCase(); return [['Astrology.com',`https://www.astrology.com/horoscope/daily/${l}.html`],['Horoscope.com',`https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=${s+1}`],['Cafe Astrology',`https://cafeastrology.com/${l}dailyhoroscope.html`],['Astrostyle',`https://astrostyle.com/horoscopes/daily/${l}/`]]; };
 const FOCUS={all:'Everything',love:'Love',work:'Work and money',energy:'Body and energy',create:'Creativity',home:'Home and family'};
 const THEMES={love:['A small kindness opens a door you thought was locked.','Say the thing plainly; it lands softer than you fear.','Give space, and it comes back warmer.','Old warmth returns if you make the first move.','Listen twice as long as you speak tonight.'],work:['Finish the small task first; it frees the big one.','A question you ask today saves a week later.','Check the numbers twice before you sign.','Your idea is ready; show it to one person.','Clear one old promise and the day lightens.'],energy:['Steady: a good day to begin.','Restless: move before you decide.','Quiet: protect your sleep.','Strong in the morning; pace the evening.','Drink water, walk outside, then choose.'],create:['Write the line you keep avoiding.','Take an old idea and flip it inside out.','Make something small and finish it.','Borrow a rhythm from somewhere unexpected.','Let the cannon pick, then make it yours.'],home:['Fix the small thing that keeps catching your eye.','Call the one who always answers.','Cook something slow.','Open a window and change one corner.','Say thank you out loud at home today.']};
 const COLORS=['gold','sea green','violet','ruby','silver','sky blue','amber','rose','indigo','emerald','coral','white'];
 function reading(mode){ const s=signOf(); const t=today(); let seed=(+t.replace(/-/g,''))*31+(s==null?0:s)*977;
  if(mode==='shuffle'||mode==='cannon') seed=Math.floor(Math.random()*1e9); if(mode==='cannon'){ try{ const L=window.UNILAW&&UNILAW.fire&&UNILAW.fire('zodiac',{quiet:true}); if(L&&L.letter) seed=seed^(L.letter.charCodeAt(0)*2654435761); }catch(_){} }
  const r=R(seed); const pick=a=>a[Math.floor(r()*a.length)];
  const flip=mode==='flip'; const sign=s==null?null:(flip?(s+6)%12:s);
  let sky=null; if(P.date&&window.ZOD4){ const p=person(); if(p&&flip){ /* the shadow side: read the opposite sign's day for you */ } if(p) sky=ZOD4.reading(p,new Date()); }
  const focus=P.focus&&P.focus!=='all'?[P.focus]:['love','work','energy'];
  const lines=focus.map(f=>`<div><b>${FOCUS[f]}</b>: ${esc(pick(THEMES[f]))}</div>`).join('');
  const lucky=`<div><b>Lucky number</b> ${1+Math.floor(r()*44)} · <b>colour</b> ${pick(COLORS)} · <b>hour</b> ${1+Math.floor(r()*12)} ${r()<.5?'am':'pm'}</div>`;
  return {sign,flip,html:(flip?'<div class="kSmall">🔀 Flipped: your shadow side today, read through the opposite sign.</div>':'')+lines+lucky+(sky&&!flip?`<h4>Your sky today, from your birth chart</h4><div class="kTblW">${sky.html}</div>`:'')+(s==null?'':''),sky:!!sky}; }
 let lastMode='cannon';
 function openDay(byHand,mode){ const s=signOf(); let d=$('kDay'); if(!d){ d=document.createElement('div'); d.id='kDay'; d.setAttribute('role','dialog'); d.setAttribute('aria-modal','true'); document.body.appendChild(d); d.addEventListener('click',dayClick); }
  if(s==null){ d.innerHTML=`<div class="kPanel"><h3>🌞 Your daily reading</h3><p>Pick your sign for a reading every day, or set up your profile with your birthday for a reading from your own birth chart.</p><div class="kSigns">${SIGNS.map((n,i)=>`<button type="button" data-d="sign" data-i="${i}" data-noul>${GL[i]} ${n}</button>`).join('')}</div><div class="kRowB" style="margin-top:10px"><button type="button" class="kHot" data-d="me" data-noul>👤 Set up my profile</button><button type="button" data-d="later" data-noul>Not now</button><button type="button" class="kX" data-d="never" data-noul>Don’t show it every day</button></div></div>`; d.hidden=false; return; }
  mode=mode||P.mode||'cannon'; lastMode=mode; const r=reading(mode); const sg=r.sign;
  const date=new Date().toLocaleDateString(undefined,{weekday:'long',month:'long',day:'numeric'});
  const off=window.KNET&&!KNET.isOn();
  d.innerHTML=`<div class="kPanel"><h3>${GL[sg]} ${P.name?esc(P.name)+', y':'Y'}our day · ${SIGNS[sg]}</h3><p class="kSmall">${esc(date)} · ${ELEM[sg%4]} sign${P.date&&animalOf(P.date)?' · year of the '+animalOf(P.date):''} · reading made ${({cannon:'by the cannon',manual:'by your choices',internet:'from the internet sites below',flip:'flipped',shuffle:'shuffled',mutate:'to mutate'})[mode]||''}</p>
  <div class="kRead">${r.html}</div>
  <h4>Make it another way</h4><div class="kRowB"><button type="button" data-d="m" data-m="cannon" data-noul>💥 Cannon</button><button type="button" data-d="m" data-m="shuffle" data-noul>🔁 Shuffle</button><button type="button" data-d="m" data-m="flip" data-noul>🔀 Flip</button><button type="button" data-d="manual" data-noul>✋ Manual</button><button type="button" data-d="net" data-noul>🌐 Internet</button><button type="button" data-d="mut" data-noul>🧬 Mutate</button></div>
  <div id="kDayMore"></div>
  <h4>Today on the well-known sites</h4><p class="kSmall">${off?'📴 You are offline: these links open once you are back online.':'These open in a new tab.'}</p><div class="kRowB">${SITES(signOf()).map(([n,u])=>`<a href="${u}" target="_blank" rel="noopener">${esc(n)} ↗</a>`).join(' · ')}</div>
  <div class="kRowB" style="margin-top:12px"><button type="button" class="kGo" data-d="zod" data-noul>💞 Open LuvMyZodiac</button><button type="button" data-d="me" data-noul>👤 My profile</button><button type="button" class="kX" data-d="x" data-noul>✕ Close</button></div>
  <p class="kSmall">Astrology here is a cultural and storytelling tradition, for entertainment and reflection. The planets’ positions are real astronomy computed on your device; the meanings are tradition.</p></div>`;
  d.hidden=false; d.scrollTop=0; if(!byHand) putLS('kanin-day-seen',today()); }
 function dayClick(e){ const d=$('kDay'); if(e.target===d){ d.hidden=true; return; } const b=e.target.closest('button[data-d]'); if(!b) return; const k=b.dataset.d, more=$('kDayMore');
  if(k==='x'||k==='later'){ d.hidden=true; putLS('kanin-day-seen',today()); return; }
  if(k==='never'){ P.daily=false; saveP(); d.hidden=true; say('The daily reading will not pop up. Open it any time from 👤 Me.'); return; }
  if(k==='sign'){ P.sign=+b.dataset.i; saveP(); openDay(true); return; }
  if(k==='me'){ d.hidden=true; openMe(); return; }
  if(k==='zod'){ d.hidden=true; try{ KBAR.go('zodDock'); }catch(_){} return; }
  if(k==='m'){ openDay(true,b.dataset.m); return; }
  if(k==='manual'&&more){ more.innerHTML=`<h4>✋ Manual</h4><div class="kGrid"><label>Focus<select id="kDayFocus">${Object.entries(FOCUS).map(([v,n])=>`<option value="${v}"${P.focus===v?' selected':''}>${n}</option>`).join('')}</select></label><label>Sign<select id="kDaySign">${SIGNS.map((n,i)=>`<option value="${i}"${signOf()===i?' selected':''}>${GL[i]} ${n}</option>`).join('')}</select></label></div><div class="kRowB"><button type="button" class="kGo" data-d="mapply" data-noul>✓ Read it this way</button></div>`; return; }
  if(k==='mapply'){ P.focus=$('kDayFocus').value; P.sign=+$('kDaySign').value; saveP(); openDay(true,'manual'); return; }
  if(k==='net'&&more){ more.innerHTML=`<h4>🌐 Internet</h4><p>${window.KNET&&!KNET.isOn()?'📴 You are offline right now: these open once you are back online.':'Pick a well-known site; it opens in a new tab with today’s reading for your sign.'}</p><div class="kRowB">${SITES(signOf()).map(([n,u])=>`<a href="${u}" target="_blank" rel="noopener">${esc(n)} ↗</a>`).join(' · ')}</div>`; return; }
  if(k==='mut'&&more){ more.innerHTML=`<h4>🧬 Mutate today’s reading into</h4><div class="kRowB"><button type="button" data-d="to" data-to="story" data-noul>📖 The story</button><button type="button" data-d="to" data-to="song" data-noul>✍ A song</button><button type="button" data-d="to" data-to="beat" data-noul>🥁 A beat</button><button type="button" data-d="to" data-to="game" data-noul>🎮 A game</button></div>`; return; }
  if(k==='to'){ const s=signOf(), to=b.dataset.to, text=(d.querySelector('.kRead')||{}).innerText||'';
   d.hidden=true; try{ KAUDIO.gesture(); }catch(_){}
   try{ if(to==='story'){ if(window.KBUS&&KBUS.send) KBUS.send('story',s*2); else KBAR.go('home'); say('Today’s reading went into the story.'); }
    else if(to==='song'){ KBAR.go('swDock'); setTimeout(()=>{ const t=$('swTopic'); if(t){ t.value=SIGNS[s]+' today: '+text.split('\n').slice(0,2).join(' ').slice(0,160); t.dispatchEvent(new Event('input',{bubbles:true})); } say('Your reading is the song’s topic. Press Write.'); },700); }
    else if(to==='beat'){ KBAR.go('pad'); setTimeout(()=>{ try{ const g=$('cGen'); if(g){ const pick=['Afrobeat','House','Trap','Rock','Lo-fi','Jazz','Pop','Ambient','Reggae','Soul','Hip hop','Classical']; const want=pick[s]; const o=[...g.options].find(x=>x.text.toLowerCase().includes(want.toLowerCase())); if(o){ g.value=o.value; g.dispatchEvent(new Event('change',{bubbles:true})); } } }catch(_){} say('The Composer took a genre for '+SIGNS[s]+'. Press Auto-create.'); },900); }
    else if(to==='game'){ KBAR.go('zodDock'); setTimeout(()=>{ const a=$('z4GStart'); if(a) a.scrollIntoView({block:'center'}); say('Star Archer and Zodiac Match are ready below.'); },900); } }catch(_){}
   return; } }
 /* once a day, when the screen is free (no welcome card, no tour, no other panel on top) */
 function freeNow(){ const vis=id=>{ const e=$(id); return !!(e&&!e.hidden&&e.getBoundingClientRect().height>0); }; return !vis('tourCard')&&!vis('gtCard')&&!vis('kManual')&&!vis('kMe')&&!vis('libDock')&&!vis('fileDock')&&!vis('qpDone')&&!vis('kUpd')&&!document.body.classList.contains('gated')&&!(window.KBAR&&KBAR.onScreen&&KBAR.onScreen())&&!vis('kNetCard')&&!vis('kbusCard'); }
 let dayTries=0; const dayT=setInterval(()=>{ dayTries++; if(dayTries>300){ clearInterval(dayT); return; } if(!P.daily||getLS('kanin-day-seen','')===today()){ clearInterval(dayT); return; } if(dayTries<4||!freeNow()) return; clearInterval(dayT); dayChip(); },2000);
 function dayChip(){ putLS('kanin-day-seen',today()); return; let c=$('kDayChip'); if(c){ c.hidden=false; return; } c=document.createElement('div'); c.id='kDayChip'; c.setAttribute('role','status'); c.innerHTML='<button type="button" class="kdcOpen" data-noul>🌞 Your daily reading is ready · <b>Open</b></button><button type="button" class="kdcX" aria-label="Not now" data-noul>✕</button>'; document.body.appendChild(c); c.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; c.hidden=true; if(b.classList.contains('kdcOpen')) openDay(true); }); setTimeout(()=>{ if(c) c.hidden=true; },45000); }

 /* the profile screen */
 function openMe(){ let d=$('kMe'); if(!d){ d=document.createElement('div'); d.id='kMe'; d.setAttribute('role','dialog'); d.setAttribute('aria-modal','true'); document.body.appendChild(d); d.addEventListener('click',meClick); }
  const cities=(window.ZOD4&&ZOD4.cities?ZOD4.cities():['New York']).map(c=>c.split(',')[0]); const s=signOf();
  d.innerHTML=`<div class="kPanel"><h3>👤 My profile</h3><p>${acct?'Kept with your Claude account, so it follows you to any phone or computer where you are signed in. Only you can read it.':'Kept on this device. Sign in to Claude in this browser and it follows your account to every device.'}</p>
  <div class="kGrid"><label>Name<input id="kpName" value="${esc(P.name)}" autocomplete="given-name" placeholder="Your name"></label><label>Birthday<input id="kpDate" type="date" value="${esc(P.date)}"></label><label>Birth time (if you know it)<input id="kpTime" type="time" value="${esc(P.time)}"></label><label>Birth city<select id="kpCity">${cities.map(c=>`<option${c===String(P.city).split(',')[0]?' selected':''}>${esc(c)}</option>`).join('')}</select></label>
  <label>Sign<select id="kpSign"><option value="">From my birthday${P.date&&sunFromDate(P.date)!=null?' ('+SIGNS[sunFromDate(P.date)]+')':''}</option>${SIGNS.map((n,i)=>`<option value="${i}"${P.sign!=null&&P.sign!==''&&+P.sign===i?' selected':''}>${GL[i]} ${n}</option>`).join('')}</select></label>
  <label>My reading is made by<select id="kpMode">${[['cannon','💥 The cannon'],['manual','✋ My choices'],['shuffle','🔁 Shuffle'],['flip','🔀 Flip'],['internet','🌐 The internet sites']].map(([v,n])=>`<option value="${v}"${P.mode===v?' selected':''}>${n}</option>`).join('')}</select></label></div>
  <div class="kRowB"><label class="kChk"><input id="kpDaily" type="checkbox"${P.daily?' checked':''}> Show my reading once a day when I open KAN-IN</label></div>
  <div class="kRowB"><label class="kChk"><input id="kpFollow" type="checkbox"${P.follow?' checked':''}> Keep KAN-IN in line with me: my chart in LuvMyZodiac and my name in the greeting</label></div>
  ${s!=null?`<p>Your sign: <b>${GL[s]} ${SIGNS[s]}</b> · ${ELEM[s%4]}${P.date&&animalOf(P.date)?' · year of the '+animalOf(P.date):''}</p>`:''}
  <div class="kRowB"><button type="button" class="kGo" data-p="save" data-noul>✓ Save my profile</button><button type="button" class="kHot" data-p="day" data-noul>🌞 Today’s reading</button><button type="button" data-p="zod" data-noul>💞 My full chart</button><button type="button" data-p="net" data-noul>🌐 Connection</button><button type="button" data-p="forget" data-noul>🗑 Forget my profile</button><button type="button" class="kX" data-p="x" data-noul>✕ Close</button></div></div>`;
  d.hidden=false; d.scrollTop=0; }
 function readForm(){ P.name=$('kpName').value.trim().slice(0,60); P.date=$('kpDate').value; P.time=$('kpTime').value; P.city=$('kpCity').value; const sg=$('kpSign').value; P.sign=sg===''?null:+sg; P.mode=$('kpMode').value; P.daily=$('kpDaily').checked; P.follow=$('kpFollow').checked; }
 let forgetArm=0;
 async function meClick(e){ const d=$('kMe'); if(e.target===d){ d.hidden=true; return; } const b=e.target.closest('button[data-p]'); if(!b) return; const k=b.dataset.p;
  if(k==='x'){ d.hidden=true; return; }
  if(k==='save'){ readForm(); await saveP(); say(P.name?'Saved, '+P.name+'.':'Saved.'); openMe(); return; }
  if(k==='day'){ readForm(); await saveP(); d.hidden=true; openDay(true); return; }
  if(k==='zod'){ readForm(); await saveP(); d.hidden=true; try{ KBAR.go('zodDock'); }catch(_){} return; }
  if(k==='net'){ d.hidden=true; netCard(); return; }
  if(k==='forget'){ if(Date.now()-forgetArm>4000){ forgetArm=Date.now(); b.textContent='Press again to forget'; return; } P=blankP(); P.at=Date.now(); putLS('kanin-profile',P); if(acct){ try{ await acct.ref.delete(); }catch(_){} } say('Your profile is forgotten.'); openMe(); } }
 document.addEventListener('keydown',e=>{ if(e.key!=='Escape') return; ['kMe','kDay','kNetCard'].forEach(id=>{ const x=$(id); if(x&&!x.hidden) x.hidden=true; }); });
 try{ const gh=window.GOHOME; window.GOHOME=function(){ ['kMe','kDay','kNetCard'].forEach(id=>{ const x=$(id); if(x) x.hidden=true; }); return gh&&gh.apply(this,arguments); }; }catch(_){}
 window.KSTARS={open:openMe,day:openDay,profile:()=>Object.assign({},P),sign:signOf,save:saveP,account:()=>!!acct};
})();
