(()=>{ /* 📰 CURRENT NEWS (v238): its own platform inside KAN-IN, matching the Current News page of www.omni-galaxy.com.
   Today’s headlines are gathered by the studio from named news sources and kept in the app’s own database with the date they were
   gathered and a link to each story (the app cannot load the web by itself, so the list is as fresh as its date says). Every topic
   has one-tap links to the major newsrooms, there is local news for any town, a fact-check shelf, live world clocks, and Ask AI to
   explain a story in plain words. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const safeURL=u=>/^https:\/\//.test(String(u||''))?String(u):'';
 const TOPICS=[['top','⭐ Top stories',[['AP News','https://apnews.com/'],['Reuters','https://www.reuters.com/'],['BBC News','https://www.bbc.com/news'],['NPR News','https://www.npr.org/sections/news/'],['Google News','https://news.google.com/']]],
  ['world','🌍 World',[['AP World','https://apnews.com/world-news'],['Reuters World','https://www.reuters.com/world/'],['BBC World','https://www.bbc.com/news/world'],['Al Jazeera','https://www.aljazeera.com/'],['The Guardian World','https://www.theguardian.com/world']]],
  ['us','🇺🇸 United States',[['AP U.S.','https://apnews.com/us-news'],['Reuters U.S.','https://www.reuters.com/world/us/'],['NPR National','https://www.npr.org/sections/national/'],['PBS NewsHour','https://www.pbs.org/newshour/'],['USA Today','https://www.usatoday.com/news/nation/']]],
  ['politics','🏛 Politics',[['AP Politics','https://apnews.com/politics'],['Reuters Politics','https://www.reuters.com/world/us/'],['NPR Politics','https://www.npr.org/sections/politics/'],['Politico','https://www.politico.com/'],['The Hill','https://thehill.com/']]],
  ['business','💼 Business & money',[['AP Business','https://apnews.com/business'],['Reuters Business','https://www.reuters.com/business/'],['CNBC','https://www.cnbc.com/'],['MarketWatch','https://www.marketwatch.com/'],['Yahoo Finance','https://finance.yahoo.com/']]],
  ['tech','💻 Technology',[['AP Technology','https://apnews.com/technology'],['Reuters Technology','https://www.reuters.com/technology/'],['The Verge','https://www.theverge.com/'],['Ars Technica','https://arstechnica.com/'],['TechCrunch','https://techcrunch.com/']]],
  ['science','🔬 Science & space',[['AP Science','https://apnews.com/science'],['NASA News','https://www.nasa.gov/news/'],['Science News','https://www.sciencenews.org/'],['Scientific American','https://www.scientificamerican.com/'],['New Scientist','https://www.newscientist.com/']]],
  ['health','🏥 Health',[['AP Health','https://apnews.com/health'],['Reuters Health','https://www.reuters.com/business/healthcare-pharmaceuticals/'],['CDC Newsroom','https://www.cdc.gov/media/'],['WHO News','https://www.who.int/news'],['NPR Health','https://www.npr.org/sections/health/']]],
  ['sports','⚽ Sports',[['AP Sports','https://apnews.com/sports'],['ESPN','https://www.espn.com/'],['BBC Sport','https://www.bbc.com/sport'],['CBS Sports','https://www.cbssports.com/'],['Yahoo Sports','https://sports.yahoo.com/']]],
  ['ent','🎬 Entertainment',[['AP Entertainment','https://apnews.com/entertainment'],['Variety','https://variety.com/'],['The Hollywood Reporter','https://www.hollywoodreporter.com/'],['Billboard','https://www.billboard.com/'],['Rolling Stone','https://www.rollingstone.com/']]],
  ['weather','⛅ Weather',[['National Weather Service','https://www.weather.gov/'],['NOAA','https://www.noaa.gov/news'],['National Hurricane Center','https://www.nhc.noaa.gov/'],['Weather Underground','https://www.wunderground.com/'],['AccuWeather','https://www.accuweather.com/']]]];
 const CHECK=[['AP Fact Check','https://apnews.com/hub/ap-fact-check'],['Reuters Fact Check','https://www.reuters.com/fact-check/'],['PolitiFact','https://www.politifact.com/'],['FactCheck.org','https://www.factcheck.org/'],['Snopes','https://www.snopes.com/']];
 const CLOCKS=[['New York','America/New_York'],['Los Angeles','America/Los_Angeles'],['London','Europe/London'],['Paris','Europe/Paris'],['Dubai','Asia/Dubai'],['Mumbai','Asia/Kolkata'],['Beijing','Asia/Shanghai'],['Tokyo','Asia/Tokyo'],['Sydney','Australia/Sydney'],['Lagos','Africa/Lagos'],['São Paulo','America/Sao_Paulo'],['Mexico City','America/Mexico_City']];
 const HOWTO=[['Who wrote it?','A named newsroom and reporter you can check.'],['When?','Look at the date: old stories get shared as new.'],['Where is the proof?','Good stories name sources, documents and places.'],['Who else says so?','Check whether two or three other newsrooms report the same thing.'],['Is it news or opinion?','Opinion pages argue a side; news pages report facts.'],['Does it make you angry fast?','Stories built to enrage are often slanted. Slow down and check.']];
 let tab=getLS('kanin-news-tab','today'), topic=getLS('kanin-news-topic','top'), town=getLS('kanin-news-town',''), q='', items=null, gathered='', loadState='idle', busy=null, sample=null, aiAns='', clock=0, unsub=null;
 (async()=>{ try{ if(window.claude&&claude.use) sample=await claude.use('sample'); }catch(_){ sample=null; } })();
 async function load(){ if(loadState!=='idle') return; /* asked once per visit; never again from inside a paint */ loadState='loading'; let db=null; try{ if(window.claude&&claude.use) db=await claude.use('db'); }catch(_){ db=null; }
  if(!db){ loadState='none'; paintBody(); return; }
  const to=setTimeout(()=>{ if(loadState==='loading'){ loadState='none'; paintBody(); } },10000);
  try{ unsub=db.collection('news/today/items').orderBy('rank').limit(60).onSnapshot(snap=>{ clearTimeout(to); const L=[]; snap.forEach(d=>{ const x=d.data()||{}; L.push(x); }); items=L; loadState='done';
     db.doc('news/today').get().then(m=>{ const x=m&&m.exists?m.data():null; gathered=x&&x.gathered?String(x.gathered):''; paintBody(); }).catch(()=>paintBody()); },()=>{ clearTimeout(to); loadState='none'; paintBody(); }); }
  catch(_){ clearTimeout(to); loadState='none'; paintBody(); } }
 const css=document.createElement('style'); css.textContent=`
#kNews{position:fixed;inset:0;z-index:9700;overflow:auto;color:#eef2fb;background:linear-gradient(180deg,#14161d 0,#1b1f2a 50%,#101219 100%);padding:14px 16px calc(230px + env(safe-area-inset-bottom,0px));padding-right:calc(var(--kRailW,58px) + 16px);font:15px/1.55 system-ui,sans-serif}
#kNews[hidden]{display:none!important}
#kNews .nwIn{max-width:980px;margin:0 auto}
#kNews .nwBrand{font:700 11.5px ui-monospace,monospace;letter-spacing:.1em;color:#ff8a65;text-transform:uppercase}
#kNews h2{font:900 clamp(26px,5.5vw,40px)/1.12 Georgia,'Times New Roman',serif;color:#fff;margin:8px 0 4px;text-wrap:balance}
#kNews h3{font:800 18px/1.3 Georgia,serif;color:#fff;margin:0 0 4px}
#kNews .nwSub{color:#b9c2d6;font-size:14px;margin:0 0 10px}
#kNews .nwTabs{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
#kNews .nwTabs button{min-height:42px!important;border-radius:12px!important;padding:4px 12px!important;font:800 14px system-ui,sans-serif!important}
#kNews .nwTabs button[aria-pressed="true"]{background:#ff8a65!important;color:#1a0d07!important}
#kNews .nwCtl{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:6px 0 12px}
#kNews .nwCtl select,#kNews .nwCtl input{min-height:40px;border-radius:10px;font:600 14px system-ui,sans-serif;padding:4px 8px;max-width:100%;box-sizing:border-box}
#kNews .nwCtl input{flex:1 1 200px}
#kNews .nwGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
#kNews .nwCard{background:rgba(255,255,255,.05);border:1px solid rgba(255,138,101,.3);border-radius:14px;padding:12px;min-width:0}
#kNews .nwStory{border-left:4px solid #ff8a65;background:rgba(255,255,255,.04);border-radius:10px;padding:10px 12px;margin:0 0 10px}
#kNews .nwStory b{display:block;font:800 17px/1.35 Georgia,serif;color:#fff}
#kNews .nwStory p{margin:4px 0 6px;font-size:14px;color:#d8deeb}
#kNews .nwTag{display:inline-block;font:800 11px system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#ffb199;margin-right:8px}
#kNews .nwMeta{font-size:12.5px;color:#9aa6bd}
#kNews a.nwGo{display:inline-flex;align-items:center;min-height:38px;padding:0 12px;border-radius:10px;background:#7a2e17;color:#fff;font:800 13.5px system-ui,sans-serif;text-decoration:none;margin:3px 4px 3px 0}
#kNews a{color:#9fd0ff}
#kNews .nwRow{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
#kNews .nwRow button{min-height:38px!important;padding:4px 10px!important;border-radius:10px!important;font:700 13px system-ui,sans-serif!important}
#kNews .nwClocks{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}
#kNews .nwClk{border-radius:12px;padding:8px 10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12)}
#kNews .nwClk b{display:block;font:800 22px ui-monospace,monospace;color:#fff}
#kNews .nwNote{font-size:12.5px;color:#9aa6bd;line-height:1.5}
#kNews .nwWarn{background:rgba(255,200,60,.1);border:1px solid rgba(255,200,60,.4);border-radius:12px;padding:8px 12px;font-size:13.5px;color:#ffe6a3;margin:8px 0}
#kNews textarea{width:100%;min-height:80px;border-radius:12px;font:15px system-ui,sans-serif;padding:8px;box-sizing:border-box}
#kNews .nwAns{white-space:pre-wrap;background:rgba(0,0,0,.3);border-radius:12px;padding:12px;margin-top:8px;min-height:24px}
@media (max-width:560px){ #kNews .nwGrid{grid-template-columns:minmax(0,1fr)} }`; document.head.appendChild(css);
 function box(){ let d=$('kNews'); if(d) return d; d=document.createElement('div'); d.id='kNews'; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Current news'); d.hidden=true; document.body.appendChild(d);
  d.addEventListener('click',onClick); d.addEventListener('change',onChange); d.addEventListener('input',e=>{ if(e.target.dataset.nw==='q'){ q=e.target.value; paintBody(); } }); return d; }
 const hit=(...xs)=>{ const t=q.trim().toLowerCase(); if(!t) return true; const s=xs.join(' ').toLowerCase(); return t.split(/\s+/).every(w=>s.includes(w)); };
 const links=L=>L.map(([n,u])=>'<a class="nwGo" href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(n)+' ↗</a>').join('');
 function story(x,i){ const u=safeURL(x.url); return '<div class="nwStory"><span class="nwTag">'+esc(x.topic||'News')+'</span><b>'+esc(x.title)+'</b>'+(x.summary?'<p>'+esc(x.summary)+'</p>':'')+'<div class="nwMeta">'+esc(x.source||'')+(x.date?' · '+esc(x.date):'')+'</div><div class="nwRow">'+(u?'<a class="nwGo" href="'+esc(u)+'" target="_blank" rel="noopener">Read the story ↗</a>':'')+'<button type="button" data-nw="read" data-i="'+i+'" data-noul>🔊 Read aloud</button><button type="button" data-nw="explain" data-i="'+i+'" data-noul>🤖 Explain it</button></div></div>'; }
 function paintBody(){ const B=$('nwBody'); if(!B) return; let h='';
  if(tab==='today'){ load();
   if(loadState==='done'&&items&&items.length){ const L=items.map((x,i)=>[x,i]).filter(([x])=>hit(x.title,x.summary,x.source,x.topic)); h='<p class="nwSub">'+L.length+' headlines'+(gathered?', gathered '+esc(gathered):'')+'. Each links to the newsroom that reported it. For the newest news since then, open a newsroom under 🗂 Topics.</p>'+(L.map(([x,i])=>story(x,i)).join('')||'<p>Nothing matches your search.</p>'); }
   else if(loadState==='loading'||loadState==='idle') h='<p class="nwSub">Loading today’s headlines…</p>';
   else h='<div class="nwWarn">Today’s headline list opens when you are signed in to claude.ai. Every newsroom below works for everyone.</div><h3>⭐ Top stories now</h3><div>'+links(TOPICS[0][2])+'</div>';
   h+='<h3 style="margin-top:16px">🕒 The time around the world</h3><div class="nwClocks" id="nwClocks"></div>'; }
  else if(tab==='topics'){ const T=TOPICS.find(t=>t[0]===topic)||TOPICS[0]; h='<p class="nwSub">Pick a topic; each button opens that newsroom’s live page in a new tab.</p><div class="nwGrid">'+TOPICS.filter(t=>hit(t[1],t[2].map(x=>x[0]).join(' '))).map(t=>'<div class="nwCard"'+(t===T?' style="border-color:#ff8a65"':'')+'><h3>'+t[1]+'</h3>'+links(t[2])+'</div>').join('')+'</div>'; }
  else if(tab==='local'){ const t=town.trim(); h='<div class="nwCard"><h3>📍 News near me</h3><p class="nwNote">Type a town, city, state or country.</p><div class="nwCtl"><input id="nwTown" data-nw="town" value="'+esc(town)+'" placeholder="e.g. Orlando, Florida" aria-label="Town or city"><button type="button" data-nw="townGo" data-noul>Show news</button></div>'+
    (t?'<div>'+links([['Google News: '+t,'https://news.google.com/search?q='+encodeURIComponent(t)],['Weather: '+t,'https://www.google.com/search?q='+encodeURIComponent('weather '+t)],['Local TV and papers: '+t,'https://www.google.com/search?q='+encodeURIComponent(t+' local news')],['Events: '+t,'https://www.google.com/search?q='+encodeURIComponent(t+' events this week')],['Traffic: '+t,'https://www.google.com/search?q='+encodeURIComponent(t+' traffic')]])+'</div>':'')+'</div>'; }
  else if(tab==='check'){ h='<p class="nwSub">Before you share a story, check it.</p><div class="nwGrid">'+HOWTO.map(x=>'<div class="nwCard"><h3>'+esc(x[0])+'</h3><p>'+esc(x[1])+'</p></div>').join('')+'</div><h3 style="margin-top:14px">🔎 Fact-checkers</h3><div>'+links(CHECK)+'</div>'; }
  else if(tab==='ask'){ h='<div class="nwCard"><h3>🤖 Ask about the news</h3><p class="nwNote">The AI explains a story, a word or the background in plain language. It does not see today’s news by itself: paste the headline or the story’s text in your question.</p><textarea id="nwAsk" placeholder="Paste a headline and ask: what does this mean? Why does it matter?"></textarea><div class="nwRow"><button type="button" data-nw="aiGo" data-noul>Ask</button><button type="button" data-nw="aiStop" data-noul>⏹ Stop</button><button type="button" data-nw="aiRead" data-noul>🔊 Read the answer</button></div><div class="nwAns" id="nwAns"></div>'+(sample?'':'<p class="nwNote">The AI answers inside claude.ai. Here, open the 🤖 AI screen from the Menu.</p>')+'</div>'; }
  B.innerHTML=h; if(tab==='today'){ tickClocks(); if(!clock) clock=setInterval(tickClocks,1000); } if(tab==='ask'){ const a=$('nwAns'); if(a) a.textContent=aiAns; } }
 function tickClocks(){ const el=$('nwClocks'); if(!el){ clearInterval(clock); clock=0; return; } const now=new Date(); el.innerHTML=CLOCKS.map(([c,tz])=>{ let t='', d=''; try{ t=new Intl.DateTimeFormat('en-US',{timeZone:tz,hour:'numeric',minute:'2-digit'}).format(now); d=new Intl.DateTimeFormat('en-US',{timeZone:tz,weekday:'short',month:'short',day:'numeric'}).format(now); }catch(_){ } return '<div class="nwClk"><span>'+esc(c)+'</span><b>'+esc(t)+'</b><span class="nwNote">'+esc(d)+'</span></div>'; }).join(''); }
 function paint(){ const d=box(); const T=[['today','📰 Today'],['topics','🗂 Topics'],['local','📍 Near me'],['check','✅ Check a story'],['ask','🤖 Ask AI']];
  d.innerHTML='<div class="kBar" data-sc="kNews"><button type="button" data-ka="close" data-nw="close" aria-label="Close">✕</button></div><div class="nwIn"><div class="nwBrand">The Omni-Compass LLC · Omni-Galaxy Multi-Media Studios’ KAN-IN™ · on Omni-Galaxy · Current News</div><h2>📰 Current News</h2>'+
   '<p class="nwSub">Today’s headlines with their sources, '+TOPICS.length+' topics and '+TOPICS.reduce((n,t)=>n+t[2].length,0)+' newsrooms, local news for any town, and a fact-check shelf.</p>'+
   '<div class="nwTabs" role="tablist">'+T.map(([k,t])=>'<button type="button" data-nw="tab" data-t="'+k+'" aria-pressed="'+(tab===k)+'" data-noul>'+t+'</button>').join('')+'</div>'+
   '<div class="nwCtl"><input type="search" data-nw="q" aria-label="Search the news" placeholder="🔎 Search headlines and topics" value="'+esc(q)+'"><select data-nw="topic" aria-label="Topic" data-nodice>'+TOPICS.map(t=>'<option value="'+t[0]+'"'+(topic===t[0]?' selected':'')+'>'+t[1]+'</option>').join('')+'</select></div>'+
   '<div id="nwBody"></div><p class="nwNote" style="margin-top:16px">Headlines belong to the newsrooms that reported them; each links to its source. © 2026 The Omni-Compass LLC. All rights reserved.</p></div>';
  paintBody(); }
 function speak(t){ try{ speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(t); try{ const v=window.KVOICE&&KVOICE('en'); if(v) u.voice=v; }catch(_){ } speechSynthesis.speak(u); }catch(_){ say('Read-aloud is not available on this device.'); } }
 async function ask(text){ if(!sample){ try{ close(); KAI.open(text); }catch(_){ } return; } if(busy) try{ busy.abort(); }catch(_){ } busy=new AbortController(); aiAns='Thinking…'; const a=$('nwAns'); if(a) a.textContent=aiAns;
  const prompt='You explain news stories inside a family-friendly multimedia app. You cannot see today’s news: work only from what the user gives you and well-known background, and say plainly when something may have changed since your knowledge. Be neutral and factual, present the main sides fairly, no opinions of your own, under 220 words, plain language, no markdown headings.\n\nQuestion: '+text;
  try{ const r=await sample(prompt,{signal:busy.signal,cache:false,onText:({text:t})=>{ aiAns=t; const el=$('nwAns'); if(el) el.textContent=t; }}); aiAns=(r&&r.text)||aiAns; const el=$('nwAns'); if(el) el.textContent=aiAns; }
  catch(e){ if(e&&e.name==='AbortError') return; aiAns=e&&e.code==='rate_limited'?'The AI is busy right now. Try again in a minute.':e&&e.code==='not_granted'?'The AI is switched off for this page.':'The AI could not answer just now. Try again.'; const el=$('nwAns'); if(el) el.textContent=aiAns; } finally{ busy=null; } }
 function onClick(e){ const b=e.target.closest('[data-nw]'); if(!b) return; const k=b.dataset.nw;
  if(k==='close') return close();
  if(k==='tab'){ tab=b.dataset.t; putLS('kanin-news-tab',tab); return paint(); }
  if(k==='read'){ const x=items&&items[+b.dataset.i]; if(x) speak(x.title+'. '+(x.summary||'')+' From '+(x.source||'the newsroom')+'.'); return; }
  if(k==='explain'){ const x=items&&items[+b.dataset.i]; if(!x) return; tab='ask'; paint(); const t=$('nwAsk'); const qq='Explain this news story in plain words, with the background someone needs: "'+x.title+'". '+(x.summary||''); if(t) t.value=qq; return ask(qq); }
  if(k==='townGo'){ const i=$('nwTown'); town=(i&&i.value||'').slice(0,80); putLS('kanin-news-town',town); return paintBody(); }
  if(k==='aiGo'){ const t=$('nwAsk'); const v=t&&t.value.trim(); if(!v) return say('Type a question first.'); return ask(v); }
  if(k==='aiStop'){ if(busy) try{ busy.abort(); }catch(_){ } try{ speechSynthesis.cancel(); }catch(_){ } return; }
  if(k==='aiRead'){ if(aiAns) speak(aiAns); return; } }
 function onChange(e){ const k=e.target.dataset.nw; if(!k) return; e.stopPropagation(); if(k==='topic'){ topic=e.target.value; putLS('kanin-news-topic',topic); tab='topics'; putLS('kanin-news-tab',tab); paint(); } }
 function open(which){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ }
  if(typeof which==='string'&&['today','topics','local','check','ask'].includes(which)) tab=which; d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kNews'); if(d) d.hidden=true; clearInterval(clock); clock=0; try{ speechSynthesis.cancel(); }catch(_){ } if(busy) try{ busy.abort(); }catch(_){ } }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&$('kNews')&&!$('kNews').hidden) close(); });
 try{ const gh=window.GOHOME; if(gh&&!gh.__knw){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__knw=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(!e.target.closest) return; if(e.target.closest('#kdHome,#lpMenu')) return close(); const r=e.target.closest('#rDock button'); if(r&&$('kNews')&&!$('kNews').hidden) close(); },true);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Current News','📰','Current News: today’s headlines','news',()=>open('today')); TOPICS.forEach(t=>add('Current News','📰',t[1].replace(/^\S+\s/,'')+' news','topic',()=>{ topic=t[0]; open('topics'); })); add('Current News','📍','Local news near me','news',()=>open('local')); add('Current News','✅','Fact-check a story','news',()=>open('check')); });
 window.KNEWS={open,close,get items(){ return (items||[]).slice(); },get state(){ return loadState; }};
})();
