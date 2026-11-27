(()=>{ /* 🔐 SIGN IN · ACCOUNT · MY PAGE (v243). The first thing after the landing game opens the app (four cannon hits) is SIGN IN.
   • Signing in needs an account. A person with no account is shown CREATE YOUR ACCOUNT (a display name, a unique @handle, an avatar,
     a short bio, interests, the birthday that sets their LuvMyZodiac sign, public or private page, and the house rules), and only
     then SIGN IN. The account is tied to who is viewing (the platform's own sign-in), so nobody needs a password here and nobody can
     sign in as somebody else.
   • MY PAGE: every person gets their own platform inside the platform: a cover in their colour, their avatar, name, @handle and bio,
     followers and following, their posts, their feed (the people they follow, the official DD Universe posts and their own), the
     people directory (search, follow, unfollow, open anyone's page), MY APPS (the parts of KAN-IN they pin to their own page, in their
     own order: their studio, their games, their zodiac, their recipes…) and settings (edit, sign out, delete the account).
   • Posts can share what they made (a beat, a story, a song, a game score: the app it came from is linked), get ❤ likes and 💬 replies.
     Everyone signed in reads every public page; each person writes only their own page (the owner of DD Universe moderates).
   Data: people/<id> (the account and page) and wall/<id> (that person's posts, likes and replies); the profile on the device
   (kanin-me) is kept in step, so the Profile tab, Social and LuvMyZodiac agree. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const getSS=k=>{ try{ return sessionStorage.getItem(k); }catch(_){ return null; } }, putSS=(k,v)=>{ try{ v==null?sessionStorage.removeItem(k):sessionStorage.setItem(k,v); }catch(_){ } };
 const ago=t=>{ const s=(Date.now()-t)/1000; return s<60?'just now':s<3600?Math.floor(s/60)+' min':s<86400?Math.floor(s/3600)+' h':Math.floor(s/86400)+' d'; };
 const AV=['🦁','🐯','🦊','🐼','🐸','🐙','🦄','🐲','🦅','🐬','🦋','🌟','🔥','⚡','🌙','🌈','🎧','🎤','🎸','🥁','🎹','🎬','🎨','🕹','👑','💎','🚀','🤖','👽','🧠','🧙','🦸'];
 const COLS=['#ff2d95','#7a2cff','#00b7ff','#00c46a','#ffb800','#ff5a1f','#e0245e','#14b8a6'];
 const INTERESTS=['Hip-hop','R&B','Pop','Rock','Gospel','Jazz','Country','Latin','Afrobeats','EDM','Comedy','Film','Gaming','Art','Poetry','Astrology','Science','Faith','Fitness','Fashion','Food','Travel','Stories','Beats'];
 const APPS=[['story','📖','Story builder',()=>KRAIL.goTo('home')],['studio','🎛','Studio',()=>KRAIL.goTo('pad')],['tracks','🎼','Track sequencer',()=>KSEQ.open()],['karaoke','🎤','Karaoke',()=>KKARA.open()],['music','🎵','Music',()=>KRAIL.goTo('musicDock')],['games','🕹','Games',()=>KVG.open()],['zodiac','♈','LuvMyZodiac',()=>KRAIL.goTo('zodDock')],['compass','🧭','Omni-Compass',()=>KRAIL.goTo('omniDock')],['recipes','🍳','Recipes',()=>KRAIL.goTo('recipeDock')],['laugh','😂','Laugh',()=>KHUMOR.open('day')],['ai','🤖','AI',()=>KAI.open()],['easel','🎨','The Easel',()=>KEASEL.open()],['video','🎬','Video studio',()=>KRAIL.goTo('aivDock')],['news','📰','Current News',()=>KNEWS.open()],['faith','✝️','Cultures & Religion',()=>KRELIG.open()],['market','📈','Stock Market',()=>KMARKET.open()],['library','📚','My library',()=>KSOCIAL.open('lib')],['projects','📁','Projects',()=>KRAIL.goTo('fileDock')]];
 const appOf=k=>APPS.find(a=>a[0]===k);
 let db=null, user=null, uid=null, state='boot', acct=null, wall=null, people={}, walls={}, unsubP=null, unsubW=null, tab='posts', viewing=null, q='', news=[], assets=null, dls=null;
 const signedIn=()=>!!acct&&getSS('kanin-signed')===uid;
 /* ---------- connect ---------- */
 async function boot(){ try{ if(!window.claude||!claude.use){ state='none'; return; } [db,user]=await Promise.all([claude.use('db').catch(()=>null),claude.use('user').catch(()=>null)]); if(!db||!user){ state='none'; paint(); return; } uid=await user.id().catch(()=>null); if(!uid){ state='none'; paint(); return; }
   state='loading'; const to=setTimeout(()=>{ if(state==='loading'){ state='none'; paint(); } },10000);
   db.doc('people/'+uid).onSnapshot(s=>{ clearTimeout(to); acct=s.exists?s.data():null; state=acct?'have':'new'; paint(); },()=>{ clearTimeout(to); state='none'; paint(); });
   db.doc('wall/'+uid).onSnapshot(s=>{ wall=s.exists?s.data():null; paint(); },()=>{}); }catch(_){ state='none'; paint(); } }
 function listenAll(){ if(!db||unsubP) return; unsubP=db.collection('people').limit(500).onSnapshot(s=>{ people={}; s.docs.forEach(d=>{ people[d.id]=d.data()||{}; }); paint(); },()=>{}); unsubW=db.collection('wall').limit(500).onSnapshot(s=>{ walls={}; s.docs.forEach(d=>{ walls[d.id]=d.data()||{}; }); paint(); },()=>{}); db.collection('news/today/items').orderBy('rank').limit(8).onSnapshot(s=>{ news=s.docs.map(d=>d.data()||{}); paint(); },()=>{}); }
 /* ---------- writes: one at a time, only my own page ---------- */
 let busy=Promise.resolve(); const write=(path,fn)=>{ busy=busy.then(async()=>{ try{ await fn(db.doc(path)); }catch(e){ say(e&&e.code==='not_granted'?'This viewer can read pages but cannot write here. Ask the owner for Contributor access.':'That did not save. Try again.'); throw e; } }).catch(()=>{}); return busy; };
 const myWall=()=>Object.assign({posts:[],likes:[]},wall||{});
 /* ---------- the screens ---------- */
 const css=document.createElement('style'); css.textContent=`
#kAcct{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9700;overflow-y:auto;background:radial-gradient(circle at 50% 0,#3b0f5c,#07051a 70%);color:#eef;font:15px/1.5 system-ui,sans-serif;padding:calc(14px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 40px}
#kAcct[hidden]{display:none!important}
#kAcct .kaIn{max-width:860px;margin:0 auto}
#kAcct .kaCard{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.18);border-radius:18px;padding:16px;margin:12px 0}
#kAcct h2{font:900 26px/1.15 system-ui,sans-serif;margin:4px 0;color:#ffe94a}#kAcct h3{font:800 18px system-ui,sans-serif;margin:4px 0 8px}
#kAcct label{display:block;font:700 13px system-ui,sans-serif;margin:10px 0 4px;color:#cfe}
#kAcct input[type=text],#kAcct input[type=date],#kAcct textarea,#kAcct select{width:100%;box-sizing:border-box;min-height:44px;border-radius:12px;padding:8px 12px;font:16px system-ui,sans-serif}
#kAcct textarea{min-height:80px}
#kAcct .kaRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
#kAcct button{min-height:44px;border-radius:12px;padding:0 16px;font:800 15px system-ui,sans-serif;cursor:pointer}
#kAcct .kaGo{background:linear-gradient(135deg,#ffe94a,#ff7a00)!important;color:#1a0f00!important;font-size:17px!important;min-height:52px!important}
#kAcct .kaChip{min-height:36px;padding:0 12px;border-radius:99px;font:700 13px system-ui,sans-serif}
#kAcct .kaChip.on{background:#ff2d95!important;color:#fff!important}
#kAcct .kaAv{font-size:24px;min-width:44px;padding:0}
#kAcct .kaAv.on{outline:3px solid #ffe94a}
#kAcct .kaCover{border-radius:18px;padding:18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
#kAcct .kaBig{font-size:56px;width:84px;height:84px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:rgba(0,0,0,.25);border:3px solid #fff}
#kAcct .kaName{font:900 24px system-ui,sans-serif}#kAcct .kaHandle{opacity:.85;font-weight:700}
#kAcct .kaTabs{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
#kAcct .kaTabs button.on{background:#ffe94a!important;color:#14163a!important}
#kAcct .kaPost{background:rgba(0,0,0,.25);border-radius:14px;padding:10px 12px;margin:8px 0}
#kAcct .kaPost .who{font-weight:800}#kAcct .kaPost .t{white-space:pre-wrap;word-wrap:break-word;margin:4px 0}
#kAcct .kaPost .kaRow button{min-height:36px;padding:0 10px;font-size:13px}
#kAcct .kaApps{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px}
#kAcct .kaApps button{min-height:64px;font-size:14px;white-space:normal}
#kAcct .kaApps .kaRow{flex-wrap:nowrap!important;gap:4px!important;margin-top:4px}
#kAcct .kaApps .kaRow .kaChip{min-width:0!important;min-height:32px!important;height:32px;padding:0 10px!important;flex:1 1 0;font-size:13px!important}
#kAcct .kaApps [data-app]{font-size:15px!important}
#kAcct .kaPeople .kaPost{display:flex;gap:10px;align-items:center}
#kAcct .kaNote{font-size:13px;opacity:.85}
#kAcct .kaErr{color:#ffb4c8;font-weight:700}
#kAcct .kaStats{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px;margin-top:10px}
#kAcct .kaStats div{background:rgba(0,0,0,.25);border-radius:12px;padding:8px 10px}
#kAcct .kaStats b{display:block;font:900 20px system-ui,sans-serif;color:#ffe94a}
#kAcct .kaStats span{font-size:12.5px;opacity:.85}
#kAcct .kaPost a{color:#7ff;font-weight:700}`; document.head.appendChild(css);
 function host(){ let d=$('kAcct'); if(d) return d; d=document.createElement('div'); d.id='kAcct'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Account and my page'); document.body.appendChild(d); d.addEventListener('click',onClick); d.addEventListener('input',onInput); return d; }
 let form=null; const blankForm=()=>{ const me=getLS('kanin-me',{})||{}; return {name:me.name||'',handle:(me.handle||'').replace(/^@/,''),av:me.av||AV[Math.floor(Math.random()*AV.length)],color:me.color||COLS[0],bio:me.bio||'',birth:me.birth||'',likes:Array.isArray(me.likes)?me.likes.slice(0,8):[],pub:true,rules:false}; };
 const legal='<p class="kaNote">© 2026 The Omni-Compass LLC and DD Universe Multi-Media Studios. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com</p>';
 function render(){ const d=host(); if(d.hidden) return; let h='<div class="kaIn"><div class="kaRow" style="justify-content:space-between"><b style="font:900 14px system-ui,sans-serif;letter-spacing:.08em;color:#7ff">🔐 DD UNIVERSE · MY ACCOUNT</b><button type="button" data-ka="x" data-noul>✕ Close</button></div>';
  if(state==='boot'||state==='loading') h+='<div class="kaCard"><h2>🔐 Sign in</h2><p>Finding your account…</p></div>';
  else if(state==='none') h+='<div class="kaCard"><h2>🔐 Sign in</h2><p>Accounts need the platform\'s sign-in, and this view does not have it (you are signed out, or opened a public copy). Sign in to claude.ai and open the app again to create your account.</p><div class="kaRow"><button type="button" data-ka="guest" data-noul>👀 Look around as a guest</button></div><p class="kaNote">As a guest everything you make stays on this device. Posting, following and your own page need an account.</p></div>';
  else if(state==='new'&&!form) h+='<div class="kaCard"><h2>🔐 Sign in</h2><p class="kaErr">You do not have an account yet, so you cannot sign in.</p><p>Create your account first: it takes a minute and gives you your own page inside DD Universe, with your posts, your people and your apps.</p><div class="kaRow"><button type="button" class="kaGo" data-ka="create" data-noul>✨ Create my account</button><button type="button" data-ka="guest" data-noul>👀 Look around as a guest</button></div></div>';
  else if(state==='new'&&form) h+=formHTML(false);
  else if(state==='have'&&!signedIn()&&!form) h+='<div class="kaCard"><h2>🔐 Sign in</h2><div class="kaCover" style="background:'+esc(acct.color||COLS[0])+'"><div class="kaBig">'+esc(acct.av||'🙂')+'</div><div><div class="kaName">'+esc(acct.name||'')+'</div><div class="kaHandle">@'+esc(acct.handle||'')+'</div></div></div><p>Welcome back. This is your account on this sign-in.</p><div class="kaRow"><button type="button" class="kaGo" data-ka="signin" data-noul>➡ Sign in as @'+esc(acct.handle||'')+'</button></div></div>';
  else if(form) h+=formHTML(true);
  else h+=page();
  d.innerHTML=h+legal+'</div>'; }
 function formHTML(edit){ const f=form; return '<div class="kaCard"><h2>'+(edit?'✏️ Edit my account':'✨ Create your account')+'</h2>'+
  '<label>Display name</label><input type="text" data-f="name" maxlength="40" value="'+esc(f.name)+'" placeholder="Your name">'+
  '<label>@handle (letters, numbers and _, 3 to 20; nobody else can have it)</label><input type="text" data-f="handle" maxlength="20" value="'+esc(f.handle)+'" placeholder="yourhandle"><div class="kaNote" id="kaHandleNote"></div>'+
  '<label>Avatar</label><div class="kaRow">'+AV.map(a=>'<button type="button" class="kaAv'+(a===f.av?' on':'')+'" data-av="'+a+'" data-noul>'+a+'</button>').join('')+'</div>'+
  '<label>Page colour</label><div class="kaRow">'+COLS.map(c=>'<button type="button" class="kaAv'+(c===f.color?' on':'')+'" data-col="'+c+'" style="background:'+c+'" aria-label="Colour '+c+'" data-noul>&nbsp;</button>').join('')+'</div>'+
  '<label>Bio</label><textarea data-f="bio" maxlength="200" placeholder="A line about you">'+esc(f.bio)+'</textarea>'+
  '<label>Birthday (sets your LuvMyZodiac sign; only the month and day show)</label><input type="date" data-f="birth" value="'+esc(f.birth)+'">'+
  '<label>Interests (up to 8)</label><div class="kaRow">'+INTERESTS.map(x=>'<button type="button" class="kaChip'+(f.likes.includes(x)?' on':'')+'" data-like="'+esc(x)+'" data-noul>'+esc(x)+'</button>').join('')+'</div>'+
  '<label>Who sees my page</label><div class="kaRow"><button type="button" class="kaChip'+(f.pub?' on':'')+'" data-pub="1" data-noul>🌐 Everyone signed in</button><button type="button" class="kaChip'+(!f.pub?' on':'')+'" data-pub="0" data-noul>🔒 Hidden (off the people list and feeds)</button></div>'+
  (edit?'':'<label><input type="checkbox" data-f="rules"'+(f.rules?' checked':'')+'> I agree to the house rules: be kind, post only what is mine to share, no hate, no harassment, nothing unsafe. The owner may remove posts that break them.</label>')+
  '<p class="kaErr" id="kaErr"></p><div class="kaRow"><button type="button" class="kaGo" data-ka="'+(edit?'save':'make')+'" data-noul>'+(edit?'💾 Save':'✅ Create my account')+'</button><button type="button" data-ka="cancel" data-noul>Cancel</button></div></div>'; }
 const handleOK=h=>/^[A-Za-z0-9_]{3,20}$/.test(h);
 const taken=h=>Object.entries(people).some(([id,p])=>id!==uid&&String(p.handle||'').toLowerCase()===h.toLowerCase());
 /* ---------- my page and anyone's page ---------- */
 const nameOf=id=>{ const p=people[id]||(id===uid?acct:null)||{}; return {av:p.av||'🙂',name:p.name||'Someone',handle:p.handle||'',color:p.color||COLS[0],pub:p.pub!==false}; };
 const postsOf=id=>{ const w=id===uid?myWall():Object.assign({posts:[]},walls[id]||{}); return (w.posts||[]).map(p=>Object.assign({by:id},p)); };
 const likesFor=(by,pid)=>Object.values(Object.assign({},walls,uid?{[uid]:myWall()}:{})).reduce((n,w)=>n+((w.likes||[]).includes(by+':'+pid)?1:0),0);
 const repliesFor=(by,pid)=>{ const out=[]; Object.entries(Object.assign({},walls,uid?{[uid]:myWall()}:{})).forEach(([id,w])=>(w.posts||[]).forEach(p=>{ if(p.re&&p.re.by===by&&p.re.id===pid) out.push(Object.assign({by:id},p)); })); return out.sort((a,b)=>a.at-b.at); };
 const okURL=u=>typeof u==='string'&&(u.startsWith('/_blob/')||u.startsWith('https://')||u.startsWith('blob:'));
 const mediaTag=(kind,url)=>!okURL(url)?'':kind==='image'?'<img src="'+esc(url)+'" alt="" style="max-width:100%;max-height:280px;border-radius:10px;display:block;margin:6px 0">':kind==='video'?'<video src="'+esc(url)+'" controls playsinline style="max-width:100%;max-height:280px;border-radius:10px;display:block;margin:6px 0"></video>':kind==='audio'?'<audio src="'+esc(url)+'" controls style="width:100%;margin:6px 0"></audio>':'';
 function postHTML(p,deep){ const n=nameOf(p.by); const liked=myWall().likes.includes(p.by+':'+p.id); const a=p.app&&appOf(p.app); const reps=deep?repliesFor(p.by,p.id):[];
  return '<div class="kaPost"><div class="who" data-ka="open" data-id="'+esc(p.by)+'" style="cursor:pointer">'+esc(n.av)+' '+esc(n.name)+' <span class="kaNote">@'+esc(n.handle)+' · '+ago(p.at||Date.now())+'</span></div>'+(p.re?'<div class="kaNote">↪ replying to @'+esc(nameOf(p.re.by).handle)+'</div>':'')+'<div class="t">'+esc(p.text)+'</div>'+(p.media?mediaTag(p.media.type,p.media.url):'')+(a?'<div class="kaRow"><button type="button" data-app="'+a[0]+'" data-noul>'+a[1]+' Open '+esc(a[2])+'</button></div>':'')+
   (p.re?'':'<div class="kaRow"><button type="button" data-ka="like" data-by="'+esc(p.by)+'" data-pid="'+esc(p.id)+'" data-noul>'+(liked?'❤️':'🤍')+' '+likesFor(p.by,p.id)+'</button><button type="button" data-ka="reply" data-by="'+esc(p.by)+'" data-pid="'+esc(p.id)+'" data-noul>💬 '+repliesFor(p.by,p.id).length+'</button>'+(p.by===uid?'<button type="button" data-ka="del" data-pid="'+esc(p.id)+'" data-noul>🗑</button>':'')+'</div>')+
   reps.map(r=>'<div class="kaPost" style="margin-left:18px"><div class="who">'+esc(nameOf(r.by).av)+' '+esc(nameOf(r.by).name)+' <span class="kaNote">'+ago(r.at)+'</span></div><div class="t">'+esc(r.text)+'</div></div>').join('')+'</div>'; }
 function page(){ listenAll(); const id=viewing||uid; const n=nameOf(id), mine=id===uid; const P=people[id]||(mine?acct:{})||{}; const fol=(mine?acct:P).following||[]; const followers=Object.entries(people).filter(([,p])=>(p.following||[]).includes(id)).length;
  let h='<div class="kaCover" style="background:linear-gradient(135deg,'+esc(n.color)+',#14163a)"><div class="kaBig">'+esc(n.av)+'</div><div style="flex:1;min-width:0"><div class="kaName">'+esc(n.name)+'</div><div class="kaHandle">@'+esc(n.handle)+(n.pub?'':' · 🔒 hidden')+'</div><div>'+esc(P.bio||'')+'</div><div class="kaNote">'+followers+' followers · '+fol.length+' following'+((P.likes||[]).length?' · '+esc((P.likes||[]).join(', ')):'')+'</div></div>'+
   (mine?'<div class="kaRow"><button type="button" data-ka="edit" data-noul>✏️ Edit</button></div>':'<div class="kaRow"><button type="button" data-ka="follow" data-id="'+esc(id)+'" data-noul>'+((acct.following||[]).includes(id)?'✓ Following':'➕ Follow')+'</button><button type="button" data-ka="home" data-noul>⬅ My page</button></div>')+'</div>';
  if(!mine){ h+=(n.pub?postsOf(id).filter(p=>!p.re).sort((a,b)=>b.at-a.at).map(p=>postHTML(p,true)).join('')||'<p>No posts yet.</p>':'<p>🔒 This page is hidden.</p>'); return h; }
  const T=[['posts','📝 My posts'],['feed','🌐 My feed'],['cannon','💥 My Cannon'],['people','👥 People'],['apps','📱 My apps'],['set','⚙ Settings']];
  h+='<div class="kaTabs">'+T.map(([k,l])=>'<button type="button" data-tab="'+k+'" class="'+(tab===k?'on':'')+'" data-noul>'+l+'</button>').join('')+'</div>';
  if(tab==='posts'||tab==='feed') h+='<div class="kaCard"><textarea data-f="post" maxlength="500" placeholder="'+(replyTo?'Write your reply…':'What are you making today?')+'"></textarea><div class="kaRow"><select data-f="app" aria-label="Share from" data-nodice data-die="1"><option value="">Share from… (optional)</option>'+APPS.map(a=>'<option value="'+a[0]+'">'+a[1]+' '+esc(a[2])+'</option>').join('')+'</select><button type="button" class="kaGo" data-ka="post" data-noul>'+(replyTo?'💬 Reply':'📣 Post')+'</button>'+(replyTo?'<button type="button" data-ka="noreply" data-noul>Cancel reply</button>':'')+'</div></div>';
  if(tab==='posts') h+=postsOf(uid).filter(p=>!p.re).sort((a,b)=>b.at-a.at).map(p=>postHTML(p,true)).join('')||'<p>Your first post goes here.</p>';
  if(tab==='cannon') h+=cannonHTML();
  if(tab==='feed'&&news.length) h+='<div class="kaCard"><h3>📰 Today\'s headlines</h3>'+news.slice(0,5).map(x=>'<div class="kaPost"><b>'+esc(x.title||'')+'</b><div class="kaNote">'+esc(x.summary||'')+'</div>'+(typeof x.url==='string'&&x.url.startsWith('https://')?'<a href="'+esc(x.url)+'" target="_blank" rel="noopener">Read the source ↗</a>':'')+'</div>').join('')+'<div class="kaRow"><button type="button" data-app="news" data-noul>📰 All the news</button></div></div>';
  if(tab==='feed'){ const ids=[uid].concat(acct.following||[]); const all=[]; ids.forEach(i=>{ if(i===uid||nameOf(i).pub) postsOf(i).filter(p=>!p.re).forEach(p=>all.push(p)); }); all.sort((a,b)=>b.at-a.at); h+=all.slice(0,80).map(p=>postHTML(p,true)).join('')||'<p>Follow people (👥 People) and their posts land here.</p>'; h+='<div class="kaRow"><button type="button" data-ka="official" data-noul>📣 The official DD Universe feed</button></div>'; }
  if(tab==='people'){ const L=Object.entries(people).filter(([i,p])=>i!==uid&&p.pub!==false&&(!q||(p.name+' '+p.handle).toLowerCase().includes(q.toLowerCase()))); h+='<input type="text" data-f="q" placeholder="🔎 Search people" value="'+esc(q)+'"><div class="kaPeople">'+(L.map(([i,p])=>'<div class="kaPost"><div class="kaBig" style="width:48px;height:48px;font-size:28px">'+esc(p.av||'🙂')+'</div><div style="flex:1;min-width:0" data-ka="open" data-id="'+esc(i)+'"><b>'+esc(p.name||'')+'</b> <span class="kaNote">@'+esc(p.handle||'')+'</span><div class="kaNote">'+esc(p.bio||'')+'</div></div><button type="button" data-ka="follow" data-id="'+esc(i)+'" data-noul>'+((acct.following||[]).includes(i)?'✓ Following':'➕ Follow')+'</button></div>').join('')||'<p>No one else yet. Share the app link and they appear here when they make an account.</p>')+'</div>'; }
  if(tab==='apps'){ const pins=acct.apps||['studio','tracks','karaoke','games','zodiac','story']; h+='<div class="kaCard"><h3>📱 My apps</h3><p class="kaNote">Your own page of KAN-IN: tap to open, ★ to pin or unpin, ◀ ▶ to move.</p><div class="kaApps">'+pins.map((k,i)=>{ const a=appOf(k); return a?'<div><button type="button" data-app="'+k+'" style="width:100%" data-noul>'+a[1]+'<br>'+esc(a[2])+'</button><div class="kaRow" style="justify-content:center"><button type="button" class="kaChip" data-mv="'+i+'" data-d="-1" data-noul>◀</button><button type="button" class="kaChip on" data-pin="'+k+'" data-noul>★</button><button type="button" class="kaChip" data-mv="'+i+'" data-d="1" data-noul>▶</button></div></div>':''; }).join('')+'</div><h3 style="margin-top:14px">Add to my page</h3><div class="kaRow">'+APPS.filter(a=>!pins.includes(a[0])).map(a=>'<button type="button" class="kaChip" data-pin="'+a[0]+'" data-noul>☆ '+a[1]+' '+esc(a[2])+'</button>').join('')+'</div></div>'; }
  if(tab==='set') h+='<div class="kaCard"><h3>⚙ Settings</h3><div class="kaRow"><button type="button" data-ka="edit" data-noul>✏️ Edit my account</button><button type="button" data-ka="profile" data-noul>👤 Full profile (zodiac, song, photos)</button><button type="button" data-ka="signout" data-noul>🚪 Sign out</button><button type="button" data-ka="delask" data-noul>🗑 Delete my account</button></div><p class="kaNote" id="kaDelNote"></p></div>';
  return h; }
 /* ---------- 💥 MY CANNON: everything you and the cannon make, held in one place, ready to post ---------- */
 const KIND={audio:['🎵','Sounds and songs','karaoke'],image:['🖼','Pictures and drawings','easel'],video:['🎬','Videos','video'],post:['📝','Posts kept on this device','library'],file:['📄','Files and notes','library']};
 let inv=null, invBusy=false, objURL={}, invArm=null;
 async function loadInv(){ if(invBusy) return; invBusy=true; try{ inv=await KLIB.list(); }catch(_){ inv=[]; } invBusy=false; render(); }
 try{ KLIB.on(()=>{ if(inv!=null){ inv=null; if(tab==='cannon') paint(); } }); }catch(_){ }
 const shots=()=>getLS('kanin-shots',[])||[];
 (function wrapCannon(){ const J=window.KJUMP; if(!J||typeof J.jump!=='function') return void setTimeout(wrapCannon,1500); if(J.jump.__acct) return; const j0=J.jump; const f=function(){ const r=j0.apply(this,arguments); setTimeout(()=>{ try{ const st=J.state()||{}; const L=shots(); L.unshift({at:Date.now(),what:(st.used||[]).slice(-4).join(' · ')||String(st.cur==null?'':st.cur)}); putLS('kanin-shots',L.slice(0,50)); putLS('kanin-shotn',(+getLS('kanin-shotn',0)||0)+1); }catch(_){ } },400); return r; }; f.__acct=true; try{ J.jump=f; }catch(_){ } })();
 function cannonHTML(){ if(inv==null){ loadInv(); return '<div class="kaCard"><p>Opening your inventory…</p></div>'; }
  const n=+getLS('kanin-shotn',0)||0, S=shots(), counts={}; inv.forEach(x=>{ const k=KIND[x.kind]?x.kind:'file'; counts[k]=(counts[k]||0)+1; });
  const stats=[['💥',n,'cannon shots'],['📝',myWall().posts.length,'posts on my page'],['👥',(acct.following||[]).length,'following'],['🎒',inv.length,'things I made']].concat(Object.keys(KIND).map(k=>[KIND[k][0],counts[k]||0,KIND[k][1]]));
  let h='<div class="kaCard"><h3>💥 My Cannon</h3><p class="kaNote">The cannon makes things for you: a story, a beat, a song, a game, a reading. Everything you and the cannon make lands here. Hold it, open it, and post it to your page.</p><div class="kaRow"><button type="button" class="kaGo" data-ka="fire" data-noul>💥 Fire the cannon</button><button type="button" data-ka="lib" data-noul>📚 Whole library</button><button type="button" data-app="projects" data-noul>📁 Projects</button><button type="button" data-ka="mydata" data-noul>⬇ Download my data</button></div><div class="kaStats">'+stats.map(([i,v,l])=>'<div><b>'+i+' '+v+'</b><span>'+esc(l)+'</span></div>').join('')+'</div>'+(S.length?'<h3 style="margin-top:12px">Last shots</h3>'+S.slice(0,5).map(x=>'<div class="kaNote">💥 '+ago(x.at)+' · '+esc(x.what||'a surprise')+'</div>').join(''):'')+'</div>';
  h+='<div class="kaCard"><h3>🎒 My inventory</h3>'+(inv.length?inv.slice(0,40).map(x=>{ const K=KIND[x.kind]||KIND.file; const media=x.blob&&/^(audio|image|video)$/.test(x.kind); return '<div class="kaPost"><div class="who">'+K[0]+' '+esc(x.name||'Untitled')+' <span class="kaNote">'+ago(x.at)+(x.meta&&x.meta.secs?' · '+esc(x.meta.secs)+' s':'')+'</span></div>'+(objURL[x.id]?mediaTag(x.kind,objURL[x.id]):'')+(x.kind==='post'&&x.meta&&x.meta.text?'<div class="t">'+esc(x.meta.text)+'</div>':'')+'<div class="kaRow">'+(media?'<button type="button" data-inv="open" data-id="'+esc(x.id)+'" data-noul>'+(objURL[x.id]?'✕ Hide':'▶ Open')+'</button>':'')+'<button type="button" data-inv="post" data-id="'+esc(x.id)+'" data-noul>📣 Post to my page</button>'+(x.blob?'<button type="button" data-inv="save" data-id="'+esc(x.id)+'" data-noul>⬇ Save</button>':'')+'<button type="button" data-inv="del" data-id="'+esc(x.id)+'" data-noul>'+(invArm===x.id?'Tap again to delete':'🗑')+'</button></div></div>'; }).join(''):'<p>Nothing yet. Fire the cannon, make a beat, sing a take or draw a picture and save it: it shows up here.</p>')+'</div>';
  return h; }
 const extOf=x=>{ const t=(x.blob&&x.blob.type)||''; return /wav/.test(t)?'.wav':/mpeg|mp3/.test(t)?'.mp3':/png/.test(t)?'.png':/jpe?g/.test(t)?'.jpg':/webm/.test(t)?'.webm':/mp4/.test(t)?'.mp4':/json/.test(t)?'.json':/plain/.test(t)?'.txt':''; };
 async function invAct(k,id){ const x=(inv||[]).find(y=>y.id===id); if(!x) return;
  if(k==='open'){ if(objURL[id]){ try{ URL.revokeObjectURL(objURL[id]); }catch(_){ } delete objURL[id]; } else { try{ objURL[id]=URL.createObjectURL(x.blob); }catch(_){ } } return render(); }
  if(k==='save'){ try{ dls=dls||await claude.use('downloads'); if(!dls) throw 0; await dls.save({filename:(x.name||'kan-in')+extOf(x),data:x.blob}); }catch(e){ say(e&&e.code==='declined'?'Not saved.':'This view cannot save files.'); } return; }
  if(k==='del'){ if(invArm!==id){ invArm=id; return render(); } invArm=null; try{ await KLIB.del(id); }catch(_){ } inv=(inv||[]).filter(y=>y.id!==id); say('🗑 Deleted from your library.'); return render(); }
  if(k==='post'){ const K=KIND[x.kind]||KIND.file; let media=null;
   if(x.blob&&/^(audio|image|video)$/.test(x.kind)&&x.blob.size<=20*1024*1024){ try{ assets=assets||await claude.use('assets'); if(assets){ say('📣 Posting '+(x.name||'it')+'…'); const r=await assets.upload(x.blob); if(r&&r.url) media={type:x.kind,url:r.url,id:r.id}; } }catch(_){ media=null; } }
   const w=myWall(); const p={id:Date.now().toString(36),at:Date.now(),text:(K[0]+' '+(x.name||'Something I made')+(x.kind==='post'&&x.meta&&x.meta.text?'\n'+x.meta.text:'')).slice(0,500),app:K[2]}; if(media) p.media=media;
   await write('wall/'+uid,r=>r.set({posts:[p].concat(w.posts||[]).slice(0,60),likes:w.likes||[]})); say(media?'📣 Posted to your page with the '+(x.kind==='image'?'picture':x.kind==='video'?'video':'sound')+'.':'📣 Posted to your page (the title; the file stays on this device for this viewer).'); tab='posts'; return render(); } }
 let replyTo=null, delArm=false;
 /* ---------- actions ---------- */
 async function onClick(e){ const b=e.target.closest('[data-ka],[data-tab],[data-av],[data-col],[data-like],[data-pub],[data-app],[data-pin],[data-mv],[data-inv]'); if(!b) return; e.stopPropagation(); const k=b.dataset.ka;  if(b.dataset.inv) return invAct(b.dataset.inv,b.dataset.id);
  if(k==='fire'){ close(); setTimeout(()=>{ try{ KJUMP.open(); setTimeout(()=>{ try{ KJUMP.jump(); }catch(_){ } },350); }catch(_){ say('The cannon is loading. Try again in a moment.'); } },150); return; }
  if(k==='lib'){ close(); try{ KSOCIAL.open('library'); }catch(_){ } return; }
  if(k==='mydata'){ try{ dls=dls||await claude.use('downloads'); if(!dls) throw 0; const data={account:acct,posts:myWall().posts,likes:myWall().likes,following:acct.following||[],inventory:(inv||[]).map(x=>({name:x.name,kind:x.kind,at:x.at,meta:x.meta})),cannonShots:shots()}; await dls.save({filename:'my-kan-in-data.json',data:JSON.stringify(data,null,2)}); }catch(e2){ say('This view cannot save files.'); } return; }

  if(b.dataset.tab){ tab=b.dataset.tab; viewing=null; return render(); }
  if(b.dataset.av){ form.av=b.dataset.av; return render(); } if(b.dataset.col){ form.color=b.dataset.col; return render(); }
  if(b.dataset.like){ const x=b.dataset.like; form.likes=form.likes.includes(x)?form.likes.filter(y=>y!==x):form.likes.concat(x).slice(0,8); return render(); }
  if(b.dataset.pub){ form.pub=b.dataset.pub==='1'; return render(); }
  if(b.dataset.app){ const a=appOf(b.dataset.app); if(a){ close(); setTimeout(()=>{ try{ a[3](); }catch(_){ say('That part is loading. Try again in a moment.'); } },150); } return; }
  if(b.dataset.pin){ const pins=(acct.apps||['studio','tracks','karaoke','games','zodiac','story']).slice(); const i=pins.indexOf(b.dataset.pin); if(i>=0) pins.splice(i,1); else pins.push(b.dataset.pin); return write('people/'+uid,r=>r.update({apps:pins})); }
  if(b.dataset.mv){ const pins=(acct.apps||['studio','tracks','karaoke','games','zodiac','story']).slice(); const i=+b.dataset.mv, j=i+(+b.dataset.d); if(j<0||j>=pins.length) return; [pins[i],pins[j]]=[pins[j],pins[i]]; return write('people/'+uid,r=>r.update({apps:pins})); }
  if(k==='x'||k==='guest'){ if(k==='guest') putSS('kanin-guest','1'); return close(); }
  if(k==='create'){ form=blankForm(); listenAll(); return render(); }
  if(k==='cancel'){ form=null; return render(); }
  if(k==='make'||k==='save'){ const f=form; const err=m=>{ const el=$('kaErr'); if(el) el.textContent=m; };
   if(!f.name.trim()) return err('Write your display name.'); if(!handleOK(f.handle)) return err('Your @handle needs 3 to 20 letters, numbers or _.'); if(taken(f.handle)) return err('@'+f.handle+' is taken. Pick another.'); if(k==='make'&&!f.rules) return err('Tick the house rules to create your account.');
   const data={name:f.name.trim().slice(0,40),handle:f.handle,av:f.av,color:f.color,bio:f.bio.slice(0,200),birth:f.birth?f.birth.slice(5):'' ,likes:f.likes,pub:f.pub,at:acct&&acct.at||Date.now(),following:acct&&acct.following||[],apps:acct&&acct.apps||['studio','tracks','karaoke','games','zodiac','story']};
   await write('people/'+uid,r=>r.set(data)); const me=getLS('kanin-me',{})||{}; putLS('kanin-me',Object.assign(me,{name:data.name,handle:'@'+data.handle,av:data.av,color:data.color,bio:data.bio,likes:data.likes},f.birth?{birth:f.birth}:{}));
   form=null; putSS('kanin-signed',uid); tab='posts'; say(k==='make'?'✅ Your account is made and you are signed in. This is your page.':'💾 Saved.'); return render(); }
  if(k==='signin'){ putSS('kanin-signed',uid); tab='posts'; viewing=null; listenAll(); say('➡ Signed in as @'+acct.handle+'.'); return render(); }
  if(k==='signout'){ putSS('kanin-signed',null); say('🚪 Signed out. Sign in again from 👤 Profile.'); return render(); }
  if(k==='edit'){ form=Object.assign(blankForm(),{name:acct.name,handle:acct.handle,av:acct.av,color:acct.color,bio:acct.bio,likes:acct.likes||[],pub:acct.pub!==false,rules:true}); return render(); }
  if(k==='profile'){ close(); try{ KPROFILE.open(); }catch(_){ } return; }
  if(k==='official'){ close(); try{ KSOCIAL.open(); }catch(_){ } return; }
  if(k==='open'){ viewing=b.dataset.id===uid?null:b.dataset.id; return render(); } if(k==='home'){ viewing=null; return render(); }
  if(k==='follow'){ const id=b.dataset.id; const f=(acct.following||[]).slice(); const i=f.indexOf(id); if(i>=0) f.splice(i,1); else f.push(id); return write('people/'+uid,r=>r.update({following:f.slice(-500)})); }
  if(k==='post'){ const ta=$('kAcct').querySelector('[data-f="post"]'); const t=(ta&&ta.value||'').trim(); if(!t) return say('Write something first.'); const app=($('kAcct').querySelector('[data-f="app"]')||{}).value||''; const w=myWall(); const p={id:Date.now().toString(36),at:Date.now(),text:t.slice(0,500)}; if(app) p.app=app; if(replyTo) p.re=replyTo; const posts=[p].concat(w.posts||[]).slice(0,60); replyTo=null; await write('wall/'+uid,r=>r.set({posts,likes:w.likes||[]})); say('📣 Posted.'); return; }
  if(k==='reply'){ replyTo={by:b.dataset.by,id:b.dataset.pid}; if(tab!=='posts'&&tab!=='feed') tab='feed'; viewing=null; render(); const ta=$('kAcct').querySelector('[data-f="post"]'); if(ta) ta.focus(); return; }
  if(k==='noreply'){ replyTo=null; return render(); }
  if(k==='like'){ const key=b.dataset.by+':'+b.dataset.pid; const w=myWall(); const L=(w.likes||[]).slice(); const i=L.indexOf(key); if(i>=0) L.splice(i,1); else L.push(key); return write('wall/'+uid,r=>r.set({posts:w.posts||[],likes:L.slice(-400)})); }
  if(k==='del'){ const w=myWall(); const posts=(w.posts||[]).filter(p=>p.id!==b.dataset.pid); return write('wall/'+uid,r=>r.set({posts,likes:w.likes||[]})); }
  if(k==='delask'){ if(!delArm){ delArm=true; const n=$('kaDelNote'); if(n) n.textContent='Tap 🗑 Delete my account again to delete your account, your posts, likes and replies for good.'; return; } delArm=false; await write('wall/'+uid,r=>r.delete()); await write('people/'+uid,r=>r.delete()); putSS('kanin-signed',null); say('🗑 Your account is deleted.'); return render(); } }
 function onInput(e){ const f=e.target.dataset.f; if(!f) return; if(f==='q'){ q=e.target.value; const pos=e.target.selectionStart; render(); const el=$('kAcct').querySelector('[data-f="q"]'); if(el){ el.focus(); try{ el.setSelectionRange(pos,pos); }catch(_){ } } return; }
  if(!form||f==='post'||f==='app') return; form[f]=e.target.type==='checkbox'?e.target.checked:e.target.value; if(f==='handle'){ const n=$('kaHandleNote'); if(n) n.textContent=!form.handle?'':!handleOK(form.handle)?'3 to 20 letters, numbers or _':taken(form.handle)?'@'+form.handle+' is taken':'@'+form.handle+' is free ✓'; } }
 /* repaint on data, but never while someone is typing in the page */
 function paint(){ const d=$('kAcct'); if(!d||d.hidden) return; const ae=document.activeElement; if(ae&&d.contains(ae)&&/^(INPUT|TEXTAREA|SELECT)$/.test(ae.tagName)) return; render(); }
 function open(t){ if(typeof t==='string'){ tab=t; viewing=null; } const d=host(); d.hidden=false; try{ ['kKara','libDock','fileDock','kManual','kMe'].forEach(i=>{ const x=$(i); if(x&&x!==d) x.hidden=true; }); }catch(_){ } render(); }
 function close(){ const d=$('kAcct'); if(d) d.hidden=true; form=null; }
 /* the landing game opens the app, then SIGN IN comes up */
 addEventListener('kanin',e=>{ if(e.detail==='gate-open'&&!signedIn()&&!getSS('kanin-guest')) setTimeout(open,700); });
 /* the rail's 👤 Profile opens the account: sign in first, then my page */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#kdProf,#kdProfile,[data-kd-l="Profile"]'); if(!b) return; e.preventDefault(); e.stopImmediatePropagation(); open(); },true);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('You','🔐','Sign in, my account and my page','Account',()=>open()); });
 boot();
 window.KACCT={open,close,get signedIn(){ return signedIn(); },get account(){ return acct; },get state(){ return state; }};
})();
