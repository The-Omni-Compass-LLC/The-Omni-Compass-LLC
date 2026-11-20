(()=>{ /* 👤 THE PROFILE TAB (v203): one page for the person, built like the social apps people know. A cover and a photo, a name,
   an @handle and a bio; the birth date that picks their sign (LuvMyZodiac), their Chinese zodiac and their letter on the Omni-Compass
   ring, which lines the compass of their next book; a profile song with play and stop; their favourite music and story genres and
   interests; and tabs for their posts, photos and videos, music, works and about. Everything is kept on their own device and shared
   with the Social profile and LuvMyZodiac, so the three always agree. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const SIGNS=[['♈','Aries'],['♉','Taurus'],['♊','Gemini'],['♋','Cancer'],['♌','Leo'],['♍','Virgo'],['♎','Libra'],['♏','Scorpio'],['♐','Sagittarius'],['♑','Capricorn'],['♒','Aquarius'],['♓','Pisces']];
 const ANIMALS=['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat','Monkey','Rooster','Dog','Pig'];
 const GL='ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ', GN=['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta','Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega'];
 const MUSIC=['Hip-hop','R&B','Pop','Rock','Gospel','Jazz','Country','Latin','Afrobeats','EDM','Reggae','Blues','Soul','Classical','Lo-fi','Metal','Trap','Drill','House','K-pop'];
 const STORY=['Adventure','Action','Drama','Mystery','Romance','Horror','Science Fiction','Fantasy','Thriller','Literary','Memoir','True Crime','History','Comedy','Poetry'];
 const INTERESTS=['Hip-hop','R&B','Pop','Rock','Gospel','Jazz','Country','Latin','Afrobeats','EDM','Comedy','Film','Gaming','Art','Poetry','Astrology','Science','Faith','Fitness','Fashion','Food','Travel'];
 const AV=['🦁','🐯','🦊','🐼','🐨','🐸','🐙','🦄','🐲','🦅','🐬','🦋','🌟','🔥','⚡','🌙','🌈','🎧','🎤','🎸','🥁','🎹','🎬','🎨','📚','🚀','👑','💎','🌹','🍀','🎯','🎲','🧭','🌊','🌵','🍉'];
 /* the zodiac and the compass from the birth date */
 /* the letter as the Omni-Compass ring holds it (the ring's own order, not the alphabet's) */
 const ring=L=>{ try{ const o=omniInfo(L).o; return [o[0],o[1]]; }catch(_){ return [GL[L],GN[L]]; } };
 const ymd=d=>{ const m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(d||''); return m?[+m[1],+m[2],+m[3]]:null; };
 const sunOf=d=>{ const p=ymd(d); if(!p) return null; const cut=[20,19,21,20,21,21,23,23,23,23,22,22]; return (p[1]+8+(p[2]>=cut[p[1]-1]?1:0))%12; };
 const animalOf=d=>{ const p=ymd(d); if(!p) return null; let y=p[0]; if(p[1]<2||(p[1]===2&&p[2]<5)) y--; return ANIMALS[((y-4)%12+12)%12]; };
 const letterOf=d=>{ const p=ymd(d); if(!p) return null; const t=Date.UTC(p[0],p[1]-1,p[2]), s=Date.UTC(p[0],0,1), doy=Math.floor((t-s)/864e5), len=(p[0]%4===0&&(p[0]%100!==0||p[0]%400===0))?366:365; return Math.min(23,Math.floor(doy*24/len)); };
 /* one person, three places: the Social profile, LuvMyZodiac and this page */
 function me(){ let m=null; try{ m=KSOCIAL.me(); }catch(_){ } if(!m) m=getLS('kanin-me',null); if(!m){ m={name:'',handle:'',bio:'',avatar:'🌟',interests:[],created:Date.now()}; } const x=getLS('kanin-profile-x',{}); return {m,x}; }
 function zprof(){ try{ return KSTARS.profile()||{}; }catch(_){ return {}; } }
 async function saveAll(m,x){ const keep=Object.assign({},m); delete keep.photoUrl; putLS('kanin-me',keep); try{ const live=KSOCIAL.me(); if(live&&live!==m) Object.assign(live,keep); }catch(_){ } putLS('kanin-profile-x',x);
  try{ KSTARS.save({name:m.name||'',date:x.birth||'',time:x.time||'',city:x.city||'New York'}); }catch(_){ } }
 let tab='posts', editing=false, songEl=null, urls=[];
 const css=document.createElement('style'); css.textContent=`
#kProfile{position:fixed;inset:0;z-index:9700;background:rgba(5,6,22,.98);overflow:auto;color:#fff;padding:0 0 calc(230px + env(safe-area-inset-bottom,0px));padding-right:var(--kRailW,58px)}
#kProfile[hidden]{display:none!important}
#kProfile .pfIn{max-width:920px;margin:0 auto;padding:0 16px}
#kProfile .pfCover{height:clamp(120px,24vw,220px);background:linear-gradient(120deg,#3b1670,#ff4f6d 55%,#ffb400);background-size:cover;background-position:center;border-radius:0 0 18px 18px;position:relative}
#kProfile .pfHead{display:flex;gap:14px;align-items:flex-end;margin-top:-54px;padding:0 6px;flex-wrap:wrap;position:relative;z-index:2}
#kProfile .pfAv{width:108px;height:108px;border-radius:50%;border:4px solid #ffe94a;background:#1c1450 center/cover no-repeat;display:flex;align-items:center;justify-content:center;font-size:56px;flex:none;box-shadow:0 6px 20px rgba(0,0,0,.5)}
#kProfile .pfName{flex:1 1 200px;min-width:0;padding-bottom:6px}
#kProfile .pfName h2{margin:0;font-size:24px;line-height:1.15;word-break:break-word}
#kProfile .pfName .h{opacity:.8;font-size:14px}
#kProfile .pfBio{margin:10px 6px;line-height:1.5;font-size:15px;white-space:pre-wrap}
#kProfile .pfChips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 6px}
#kProfile .pfChip{border:1px solid rgba(255,233,74,.5);border-radius:999px;padding:4px 10px;font-size:13px;background:rgba(255,233,74,.07)}
#kProfile .pfStats{display:flex;gap:18px;margin:10px 6px;flex-wrap:wrap}
#kProfile .pfStats b{display:block;font-size:20px;color:#ffe94a}
#kProfile .pfStats span{font-size:12px;opacity:.8}
#kProfile .pfRow{display:flex;flex-wrap:wrap;gap:6px;margin:8px 6px}
#kProfile .pfRow button{min-height:40px!important;border-radius:12px!important}
#kProfile .pfSong{display:flex;align-items:center;gap:8px;margin:8px 6px;padding:8px 10px;border:1px solid rgba(0,229,255,.35);border-radius:12px;background:rgba(0,229,255,.06);flex-wrap:wrap}
#kProfile .pfTabs{display:flex;gap:4px;margin:14px 0 8px;border-bottom:1px solid rgba(255,255,255,.18);overflow-x:auto}
#kProfile .pfTabs button{border:0!important;border-radius:0!important;background:none!important;color:#fff!important;padding:10px 12px!important;min-height:44px!important;font-weight:800;opacity:.7;white-space:nowrap}
#kProfile .pfTabs button[aria-selected="true"]{opacity:1;border-bottom:3px solid #ffe94a!important}
#kProfile .pfGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
#kProfile .pfTile{aspect-ratio:1/1;background:#1c1450 center/cover no-repeat;border-radius:6px;overflow:hidden;position:relative;display:flex;align-items:center;justify-content:center;padding:6px;font-size:12px;line-height:1.3;text-align:center;cursor:pointer;max-width:100%}
#kProfile .pfTile video{width:100%;height:100%;object-fit:cover}
#kProfile .pfTile .lk{position:absolute;left:4px;bottom:4px;font-size:11px;background:rgba(0,0,0,.55);border-radius:6px;padding:1px 5px}
#kProfile .pfList>div{display:flex;gap:8px;align-items:center;padding:8px;border-bottom:1px solid rgba(255,255,255,.1);flex-wrap:wrap}
#kProfile .pfForm{display:grid;gap:10px;margin:10px 6px}
#kProfile .pfForm label{display:grid;gap:4px;font-size:13px;font-weight:700}
#kProfile .pfForm input,#kProfile .pfForm select,#kProfile .pfForm textarea{min-height:40px;font-size:15px;padding:6px 10px;border-radius:10px;max-width:100%}
#kProfile .pfPick{display:flex;flex-wrap:wrap;gap:4px}
#kProfile .pfPick button{min-width:40px;min-height:40px!important;padding:2px 6px!important;font-size:20px!important;border-radius:10px!important}
#kProfile .pfPick button[aria-pressed="true"]{background:#7a5a00!important;outline:2px solid #ffe94a}
#kProfile .pfInt button{font-size:13px!important}
#kProfile .pfN{font-size:12.5px;opacity:.8;line-height:1.5;margin:4px 6px}
@media (max-width:520px){ #kProfile .pfAv{width:88px;height:88px;font-size:46px} #kProfile .pfName h2{font-size:20px} }`; document.head.appendChild(css);
 function box(){ let d=$('kProfile'); if(d) return d; d=document.createElement('div'); d.id='kProfile'; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Your profile'); d.hidden=true; document.body.appendChild(d);
  d.addEventListener('click',onClick); d.addEventListener('change',onChange); return d; }
 const url=b=>{ try{ const u=URL.createObjectURL(b); urls.push(u); return u; }catch(_){ return ''; } };
 function freeUrls(){ urls.forEach(u=>{ try{ URL.revokeObjectURL(u); }catch(_){ } }); urls=[]; }
 async function img(id){ if(!id) return ''; try{ const it=await KLIB.get(id); return it&&it.blob?url(it.blob):''; }catch(_){ return ''; } }
 async function paint(){ const d=box(); freeUrls(); const {m,x}=me(); const z=zprof(); const birth=x.birth||z.date||''; const s=sunOf(birth), an=animalOf(birth), L=letterOf(birth);
  let posts=[], works=[]; try{ posts=await KLIB.list('post'); }catch(_){ } try{ works=(await KLIB.list()).filter(i=>i.kind!=='post'); }catch(_){ }
  const likes=posts.reduce((a,p)=>a+((p.meta&&p.meta.likes)||0),0);
  const cover=await img(x.cover), photo=m.photo?await img(m.photo):'';
  if(editing) return paintEdit(d,m,x,z);
  const chips=[]; if(s!=null) chips.push(SIGNS[s][0]+' '+SIGNS[s][1]); if(an) chips.push('🏮 '+an+' (Chinese zodiac)'); if(L!=null) chips.push('🧭 '+ring(L)[0]+' '+ring(L)[1]+' · your compass letter'); if(x.city||z.city) chips.push('📍 '+(x.city||z.city)); (x.music||[]).forEach(g=>chips.push('🎵 '+g)); (x.story||[]).forEach(g=>chips.push('📖 '+g));
  const song=x.song?('<div class="pfSong"><span>🎶 Profile song: <b>'+esc(x.song.name)+'</b></span><button type="button" data-pf="songplay" data-noul>▶ Play</button><button type="button" data-pf="songstop" data-noul>■ Stop</button></div>'):'';
  d.innerHTML='<div class="kBar" data-sc="kProfile"><button type="button" data-ka="close" data-pf="close" aria-label="Close">✕</button></div><div class="pfCover" style="'+(cover?'background-image:url('+cover+')':'')+'"></div><div class="pfIn">'+
   '<div class="pfHead"><div class="pfAv" style="'+(photo?'background-image:url('+photo+')':'')+'">'+(photo?'':esc(m.avatar||'🌟'))+'</div><div class="pfName"><h2>'+esc(m.name||'Your name')+'</h2><div class="h">@'+esc(m.handle||'yourname')+(m.created?' · joined '+new Date(m.created).toLocaleDateString():'')+'</div></div></div>'+
   (m.bio?'<div class="pfBio">'+esc(m.bio)+'</div>':'<div class="pfN">Add a bio, your birth date, your photo and your song with ✏️ Edit profile.</div>')+
   '<div class="pfChips">'+chips.map(c=>'<span class="pfChip">'+esc(c)+'</span>').join('')+'</div>'+song+
   '<div class="pfStats"><div><b>'+posts.length+'</b><span>posts</span></div><div><b>'+likes+'</b><span>likes</span></div><div><b>'+works.length+'</b><span>works</span></div><div><b>'+(m.interests||[]).length+'</b><span>interests</span></div></div>'+
   '<div class="pfRow"><button type="button" data-pf="edit" data-noul>✏️ Edit profile</button><button type="button" data-pf="post" data-noul>➕ New post</button><button type="button" data-pf="share" data-noul>📤 Share profile</button><button type="button" data-pf="files" data-noul>📁 My files</button><button type="button" data-pf="zod" data-noul>♈ My LuvMyZodiac</button><button type="button" data-pf="compass" data-noul>🧭 Line my compass</button><button type="button" data-pf="align" aria-pressed="'+(x.align!==false)+'" data-noul>'+(x.align!==false?'🧭 Compass follows my profile: ON':'🧭 Compass follows my profile: OFF')+'</button><button type="button" data-pf="feed" data-noul>🌐 Social feed</button></div>'+
   '<div class="pfN">👥 Followers, following and messages between people switch on with the collective platform, on DD Universe Multi-Media Studios’ own server. Today everything here is private to this device until you post or share it.</div>'+
   '<div class="pfTabs" role="tablist">'+[['posts','▦ Posts'],['media','🖼 Photos & videos'],['music','🎵 Music'],['works','📁 Works'],['about','ℹ️ About']].map(([k,l])=>'<button type="button" role="tab" data-pft="'+k+'" aria-selected="'+(tab===k)+'" data-noul>'+l+'</button>').join('')+'</div><div id="pfBody"></div></div>';
  await paintTab(posts,works,m,x,z,birth,s,an,L); }
 async function paintTab(posts,works,m,x,z,birth,s,an,L){ const b=$('pfBody'); if(!b) return;
  if(tab==='posts'){ if(!posts.length){ b.innerHTML='<div class="pfN">No posts yet. Press ➕ New post: a photo, a video, a sound, a meme or words.</div>'; return; }
   const tiles=[]; for(const p of posts.slice(0,60)){ const t=(p.meta&&p.meta.text)||p.name||''; let bg='', inner=esc(t.slice(0,90)); if(p.meta&&p.meta.mediaId){ try{ const it=await KLIB.get(p.meta.mediaId); if(it&&it.blob){ if(/^image/.test(it.blob.type)){ bg=url(it.blob); inner=''; } else if(/^video/.test(it.blob.type)) inner='🎬 '+inner; else if(/^audio/.test(it.blob.type)) inner='🎵 '+inner; } }catch(_){ } }
    tiles.push('<div class="pfTile" data-pf="openfeed" style="'+(bg?'background-image:url('+bg+')':'')+'">'+inner+'<span class="lk">❤ '+((p.meta&&p.meta.likes)||0)+'</span></div>'); }
   b.innerHTML='<div class="pfGrid">'+tiles.join('')+'</div>'; return; }
  if(tab==='media'||tab==='music'){ const want=tab==='media'?/^(image|video)$/:/^audio$/; const L2=works.filter(i=>want.test(i.kind)).slice(0,60);
   if(!L2.length){ b.innerHTML='<div class="pfN">'+(tab==='media'?'No photos or videos yet. Drawings from the Easel, photos and videos you save land here.':'No music yet. Beats, karaoke takes and DJ sets you save land here.')+'</div>'; return; }
   if(tab==='media'){ b.innerHTML='<div class="pfGrid">'+L2.map(i=>{ const u=i.blob?url(i.blob):''; return i.kind==='video'?'<div class="pfTile"><video src="'+u+'" muted playsinline preload="metadata"></video></div>':'<div class="pfTile" style="background-image:url('+u+')"></div>'; }).join('')+'</div>'; return; }
   b.innerHTML='<div class="pfList">'+L2.map(i=>'<div><span>🎵 '+esc(i.name)+'</span><button type="button" data-pf="playlib" data-id="'+esc(i.id)+'" data-noul>▶ Play</button><button type="button" data-pf="songstop" data-noul>■ Stop</button><button type="button" data-pf="setsong" data-id="'+esc(i.id)+'" data-noul>🎶 Make it my profile song</button></div>').join('')+'</div>'; return; }
  if(tab==='works'){ const by={}; works.forEach(i=>{ by[i.kind]=(by[i.kind]||0)+1; }); b.innerHTML='<div class="pfList">'+(Object.keys(by).length?Object.entries(by).map(([k,n])=>'<div><span>'+esc(k)+'</span><b>'+n+'</b></div>').join(''):'<div>No works saved yet.</div>')+'</div><div class="pfRow"><button type="button" data-pf="files" data-noul>📁 Open Projects: every file, continue, export</button></div>'; return; }
  const rows=[['Name',m.name],['Handle','@'+(m.handle||'')],['Birth date',birth],['Birth time',x.time||z.time||''],['Birth city',x.city||z.city||''],['Sun sign',s!=null?SIGNS[s].join(' '):''],['Chinese zodiac',an||''],['Compass letter',L!=null?ring(L)[0]+' '+ring(L)[1]:''],['Music',(x.music||[]).join(', ')],['Stories',(x.story||[]).join(', ')],['Interests',(m.interests||[]).join(', ')],['Website',x.site||'']];
  b.innerHTML='<div class="pfList">'+rows.filter(r=>r[1]).map(([k,v])=>'<div><b style="min-width:120px">'+esc(k)+'</b><span>'+esc(v)+'</span></div>').join('')+'</div><div class="pfN">Your sign comes from your birth date, the same way LuvMyZodiac reads it. Your compass letter is your birthday’s place on the 24-letter Omni-Compass ring; 🧭 Line my compass puts it at the start of your next book. Horoscopes are for entertainment.</div>'; }
 function paintEdit(d,m,x,z){ const sel=(arr,cur)=>arr.map(g=>'<button type="button" data-pfg="'+esc(g)+'" aria-pressed="'+(cur||[]).includes(g)+'" data-noul>'+esc(g)+'</button>').join('');
  d.innerHTML='<div class="kBar" data-sc="kProfile"><button type="button" data-ka="close" data-pf="close" aria-label="Close">✕</button></div><div class="pfIn" style="padding-top:12px"><h2>✏️ Edit profile</h2><div class="pfForm">'+
   '<label>Name<input id="pfNm" maxlength="40" value="'+esc(m.name||'')+'"></label><label>@handle<input id="pfHd" maxlength="24" value="'+esc(m.handle||'')+'"></label><label>Bio<textarea id="pfBio" rows="3" maxlength="300">'+esc(m.bio||'')+'</textarea></label>'+
   '<label>Birth date (picks your sign and your compass letter)<input type="date" id="pfBd" value="'+esc(x.birth||z.date||'')+'"></label><label>Birth time (optional, for LuvMyZodiac’s full chart)<input type="time" id="pfBt" value="'+esc(x.time||z.time||'')+'"></label><label>Birth city<input id="pfBc" maxlength="60" value="'+esc(x.city||z.city||'')+'"></label>'+
   '<label>Photo<input type="file" id="pfPh" accept="image/*"></label><label>Cover picture<input type="file" id="pfCv" accept="image/*"></label>'+
   '<div><b style="font-size:13px">Avatar (shown when there is no photo)</b><div class="pfPick">'+AV.map(a=>'<button type="button" data-pfa="'+a+'" aria-pressed="'+(m.avatar===a)+'" data-noul>'+a+'</button>').join('')+'</div></div>'+
   '<label>Profile song<select id="pfSg"><option value="">Pick from my music…</option></select></label><label>…or upload a song<input type="file" id="pfSu" accept="audio/*"></label>'+
   '<div><b style="font-size:13px">Favourite music genres</b><div class="pfPick pfInt" data-grp="music">'+sel(MUSIC,x.music)+'</div></div>'+
   '<div><b style="font-size:13px">Favourite story genres</b><div class="pfPick pfInt" data-grp="story">'+sel(STORY,x.story)+'</div></div>'+
   '<div><b style="font-size:13px">Interests</b><div class="pfPick pfInt" data-grp="int">'+sel(INTERESTS,m.interests)+'</div></div>'+
   '<label>Website or link<input id="pfWs" maxlength="120" value="'+esc(x.site||'')+'"></label>'+
   '<div class="pfRow"><button type="button" data-pf="save" data-noul>💾 Save profile</button><button type="button" data-pf="cancel" data-noul>Cancel</button></div></div></div>';
  KLIB.list().then(L=>{ const s=$('pfSg'); if(!s) return; L.filter(i=>i.kind==='audio').forEach(i=>{ const o=document.createElement('option'); o.value=i.id; o.textContent=i.name; if(x.song&&x.song.id===i.id) o.selected=true; s.appendChild(o); }); }).catch(()=>{}); }
 let draft=null;
 async function onChange(e){ const t=e.target; if(!draft) return; const f=t.files&&t.files[0];
  if(t.id==='pfPh'&&f){ const it=await KLIB.save({kind:'image',name:'Profile photo',blob:f,meta:{from:'profile'}}); draft.m.photo=it.id||it; say('📷 Photo ready. Press 💾 Save profile.'); }
  if(t.id==='pfCv'&&f){ const it=await KLIB.save({kind:'image',name:'Profile cover',blob:f,meta:{from:'profile'}}); draft.x.cover=it.id||it; say('🖼 Cover ready. Press 💾 Save profile.'); }
  if(t.id==='pfSu'&&f){ const it=await KLIB.save({kind:'audio',name:f.name.replace(/\.[^.]+$/,''),blob:f,meta:{from:'profile'}}); draft.x.song={id:it.id||it,name:f.name.replace(/\.[^.]+$/,'')}; say('🎶 Song ready. Press 💾 Save profile.'); }
  if(t.id==='pfSg'){ draft.x.song=t.value?{id:t.value,name:t.selectedOptions[0].textContent}:null; } }
 function stopSong(){ if(songEl){ try{ songEl.pause(); }catch(_){ } songEl=null; } }
 async function playId(id){ stopSong(); try{ KAUDIO.stopAll(); }catch(_){ } try{ const it=await KLIB.get(id); if(!it||!it.blob) return say('That song is no longer in your library.'); songEl=new Audio(url(it.blob)); songEl.play().catch(()=>say('Tap ▶ Play again to start the song.')); }catch(_){ } }
 async function onClick(e){ const b=e.target.closest('button,[data-pf]'); if(!b) return; const k=b.dataset.pf;
  if(b.dataset.pft){ tab=b.dataset.pft; return paint(); }
  if(b.dataset.pfa&&draft){ draft.m.avatar=b.dataset.pfa; b.parentElement.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b)); return; }
  if(b.dataset.pfg&&draft){ const grp=b.parentElement.dataset.grp, key=grp==='int'?'interests':grp, obj=grp==='int'?draft.m:draft.x; obj[key]=obj[key]||[]; const g=b.dataset.pfg, i=obj[key].indexOf(g); if(i>=0) obj[key].splice(i,1); else obj[key].push(g); b.setAttribute('aria-pressed',i<0); return; }
  switch(k){
   case 'close': return close();
   case 'edit': { const {m,x}=me(); draft={m:Object.assign({},m),x:Object.assign({},x)}; editing=true; return paint(); }
   case 'cancel': draft=null; editing=false; return paint();
   case 'save': { const v=id=>($(id)||{}).value||''; const m=draft.m, x=draft.x; m.name=v('pfNm').trim(); m.handle=v('pfHd').trim().replace(/^@/,'').replace(/[^\w.]/g,'').slice(0,24)||m.name.toLowerCase().replace(/[^\w]/g,'').slice(0,20); m.bio=v('pfBio').trim(); m.avatar=m.avatar||'🌟'; m.created=m.created||Date.now(); x.birth=v('pfBd'); x.time=v('pfBt'); x.city=v('pfBc').trim(); x.site=v('pfWs').trim();
    if(!m.name) return say('Pick a name first.'); await saveAll(m,x); draft=null; editing=false; const s=sunOf(x.birth), L=letterOf(x.birth); say('💾 Profile saved.'+(s!=null?' '+SIGNS[s][0]+' '+SIGNS[s][1]+' is in LuvMyZodiac.':'')+(L!=null?' Your compass letter is '+ring(L)[0]+' '+ring(L)[1]+'.':'')); return paint(); }
   case 'post': close(); try{ KSOCIAL.open('create'); }catch(_){ try{ KSOCIAL.open(); }catch(__){ } } return;
   case 'feed': case 'openfeed': close(); try{ KSOCIAL.open(); }catch(_){ } return;
   case 'files': close(); try{ KPROJ.open(); }catch(_){ } return;
   case 'zod': close(); try{ KRAIL.goTo('zodDock'); }catch(_){ } return;
   case 'compass': { const {x}=me(); const L=letterOf(x.birth||zprof().date); if(L==null) return say('Add your birth date with ✏️ Edit profile first.'); close(); try{ GOHOME(); }catch(_){ } setTimeout(()=>{ try{ omniSpin(false,L); }catch(_){ } const o=$('omniOut'); if(o) o.scrollIntoView({block:'center'}); },400); return say('🧭 The compass turns to your letter: '+ring(L)[0]+' '+ring(L)[1]+'. It steers your next book.'); }
   case 'share': { const {m,x}=me(); const s=sunOf(x.birth), L=letterOf(x.birth); const txt=(m.avatar||'🌟')+' '+(m.name||'')+' @'+(m.handle||'')+(m.bio?'\n'+m.bio:'')+(s!=null?'\n'+SIGNS[s].join(' '):'')+(L!=null?' · 🧭 '+ring(L)[0]:'')+((x.music||[]).length?'\n🎵 '+x.music.join(', '):'')+'\nOn DD Universe Multi-Media Studios’ KAN-IN™'; try{ await navigator.clipboard.writeText(txt); say('📤 Your profile card is copied: paste it anywhere.'); }catch(_){ try{ KSOCIAL.compose({text:txt}); }catch(__){ say(txt); } } return; }
   case 'align': { const {m,x}=me(); x.align=!(x.align!==false); await saveAll(m,x); try{ KSTARS.save({follow:x.align}); }catch(_){ } alignTick(true); paintAlign(); say(x.align?'🧭 ON: the compass and LuvMyZodiac follow your profile: your letter starts every book, your sign drives your readings.':'🧭 OFF: the compass spins free and LuvMyZodiac reads whatever you choose.'); return paint(); }
   case 'songplay': { const {x}=me(); if(x.song) playId(x.song.id); return; }
   case 'songstop': stopSong(); return;
   case 'playlib': return playId(b.dataset.id);
   case 'setsong': { const {m,x}=me(); const it=await KLIB.get(b.dataset.id); x.song={id:b.dataset.id,name:(it&&it.name)||'My song'}; await saveAll(m,x); say('🎶 Profile song set.'); return paint(); } } }
 function open(){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner','kVG','kSocial','kAI','kEasel','kProj','kLock','kKnow'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ }
  editing=false; draft=null; d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kProfile'); if(d) d.hidden=true; stopSong(); }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&$('kProfile')&&!$('kProfile').hidden) close(); });
 try{ const gh=window.GOHOME; if(gh&&!gh.__kpf){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kpf=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(!e.target.closest) return; if(e.target.closest('#kdHome,#lpMenu')) return close(); const r=e.target.closest('#rDock button,#tourTab button'); if(r&&r.id!=='kdProfile'&&r.id!=='ttProfile'&&$('kProfile')&&!$('kProfile').hidden) close(); },true);
 /* the Menu: 👤 My profile at the top of "Me" */
 setInterval(()=>{ const t=$('tourTab'); if(!t||$('ttProfile')) return; const b=document.createElement('button'); b.type='button'; b.id='ttProfile'; b.className='ttMusic'; b.textContent='👤 My profile · photo, birth date, sign, compass, song, posts'; b.style.order='99'; b.dataset.kg='0'; b.dataset.kmDone='1'; b.setAttribute('data-noul',''); b.style.gridColumn='1/-1'; b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(open,120); }); t.appendChild(b); },900);
 /* 🧭 follow or not: while it is ON, the book's compass letter stays on the profile's letter (it turns back after any other spin) */
 let lastAlign=0;
 function alignTick(force){ const {x}=me(); if(x.align===false) return; const L=letterOf(x.birth||zprof().date); if(L==null) return; const o=$('omniOut'); if(!o||typeof window.omniSpin!=='function') return; const now=Date.now(); if(!force&&now-lastAlign<6000) return; if(o.textContent.trim().indexOf(ring(L)[0]+' ')===0) return; if(document.body.classList.contains('gated')) return; lastAlign=now; try{ omniSpin(true,L); }catch(_){ } }
 function paintAlign(){ const sp=$('omniSpin'); if(!sp) return; let b=$('kAlignBtn'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kAlignBtn'; b.setAttribute('data-noul',''); sp.insertAdjacentElement('afterend',b); b.addEventListener('click',async e=>{ e.preventDefault(); e.stopPropagation(); const {m,x}=me(); if(!ymd(x.birth||zprof().date)){ say('Add your birth date in 👤 Profile first: it picks your letter.'); return open(); } x.align=!(x.align!==false); await saveAll(m,x); try{ KSTARS.save({follow:x.align}); }catch(_){ } paintAlign(); alignTick(true); say(x.align?'🧭 ON: the compass follows your profile.':'🧭 OFF: the compass spins free.'); }); }
  const {x}=me(); const has=!!ymd(x.birth||zprof().date), on=x.align!==false&&has; const L=has?letterOf(x.birth||zprof().date):null; const t=on?'🧭 Follows my profile ('+ring(L)[0]+') · ON':'🧭 Follow my profile · OFF'; if(b.textContent!==t) b.textContent=t; b.setAttribute('aria-pressed',on); }
 setInterval(()=>{ paintAlign(); alignTick(false); },2000);
 window.KPROFILE={open,close,sunOf,letterOf,animalOf,alignTick};
})();
