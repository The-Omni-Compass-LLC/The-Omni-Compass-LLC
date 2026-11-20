(()=>{ /* 🌐 DD UNIVERSE SOCIAL · profile, posts, feed, likes, comments, meme maker, and MY LIBRARY.
   Each person's profile, posts and library live on THEIR device (private to them). The official feed is posted by the owner of
   DD Universe Multi-Media Studios and is read by everyone signed in. Opening posting to the whole public needs DD Universe's own server. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const ago=t=>{ const s=(Date.now()-t)/1000; return s<60?'just now':s<3600?Math.floor(s/60)+' min ago':s<86400?Math.floor(s/3600)+' h ago':Math.floor(s/86400)+' d ago'; };
 const AV=['🦁','🐯','🦊','🐼','🐨','🐸','🐙','🦄','🐲','🦅','🐬','🦋','🌟','🔥','⚡','🌙','🌈','🎧','🎤','🎸','🥁','🎹','🎬','🎨','🕹','👑','💎','🚀','🛸','🤖','👽','🧠','🧙','🦸','🥷','🧜'];
 const GEN=['Hip-hop','R&B','Pop','Rock','Gospel','Jazz','Country','Latin','Afrobeats','EDM','Comedy','Film','Gaming','Art','Poetry','Astrology','Science','Faith','Fitness','Fashion','Food','Travel'];
 let me=getLS('kanin-me',null), tab='feed', official=[], offState='off', mine=[], isOwner=false, draft={text:'',media:null,meme:null}, urls={};
 const needMe=()=>!me||!me.name;
 /* ---------- the official feed (shared; only the owner posts) ---------- */
 let db=null, user=null, assets=null;
 async function boot(){ try{ if(!window.claude||!claude.use) return; [db,user]=await Promise.all([claude.use('db').catch(()=>null),claude.use('user').catch(()=>null)]); isOwner=!!(user&&user.isOwner&&await user.isOwner()); if(isOwner) assets=await claude.use('assets').catch(()=>null);
   if(!db){ offState='none'; return; } offState='loading'; const to=setTimeout(()=>{ if(offState==='loading'){ offState='none'; paint(); } },10000);
   db.collection('social/official/posts').orderBy('at','desc').limit(60).onSnapshot(snap=>{ clearTimeout(to); official=snap.docs.map(d=>Object.assign({id:d.id,official:true},d.data())); offState='ok'; paint(); },()=>{ clearTimeout(to); offState='none'; paint(); }); }catch(_){ offState='none'; } }
 /* ---------- my posts (on this device) ---------- */
 async function loadMine(){ try{ mine=await KLIB.list('post'); }catch(_){ mine=[]; } }
 async function mediaURL(id){ if(!id) return null; if(urls[id]) return urls[id]; try{ const it=await KLIB.get(id); if(!it||!it.blob) return null; urls[id]={url:URL.createObjectURL(it.blob),type:(it.blob.type||'').split('/')[0],name:it.name}; return urls[id]; }catch(_){ return null; } }
 const css=document.createElement('style'); css.textContent=`
#kSocial{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(10px + env(safe-area-inset-top,0px)) max(12px,env(safe-area-inset-left,0px)) 40px 12px;background:radial-gradient(circle at 50% -10%,#3b1670,#0a0618 62%);color:#f1ecff;font:15px/1.5 system-ui,sans-serif}
#kSocial[hidden]{display:none!important}
#kSocial .soIn{max-width:720px;margin:0 auto}
#kSocial .soBrand{font:700 11.5px ui-monospace,monospace;letter-spacing:.12em;color:#c9a7ff;text-transform:uppercase}
#kSocial h2{font:900 26px/1.15 system-ui,sans-serif;margin:4px 0 6px;color:#fff}
#kSocial h3{font:800 17px system-ui,sans-serif;margin:16px 0 8px}
#kSocial .soTabs{position:sticky;top:-10px;z-index:3;display:flex;gap:6px;flex-wrap:wrap;padding:8px 0;background:linear-gradient(180deg,#1b0d3a 70%,transparent)}
#kSocial .soTabs button{flex:1 1 90px;min-height:44px;border-radius:12px;font:800 14px system-ui,sans-serif}
#kSocial .soTabs button.on{background:#ffe94a!important;color:#14163a!important}
#kSocial .soCard{background:rgba(255,255,255,.06);border:1px solid rgba(201,167,255,.28);border-radius:16px;padding:12px;margin:10px 0}
#kSocial .soHead{display:flex;align-items:center;gap:10px}
#kSocial .soAv{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;background:#2a1d55;flex:0 0 auto;overflow:hidden}
#kSocial .soAv img{width:100%;height:100%;object-fit:cover}
#kSocial .soWho b{display:block;font-size:15px}#kSocial .soWho span{font-size:12.5px;opacity:.75}
#kSocial .soBadge{font:800 10.5px system-ui,sans-serif;background:#ffe94a;color:#14163a;border-radius:6px;padding:1px 6px;margin-left:6px}
#kSocial .soText{white-space:pre-wrap;word-break:break-word;margin:8px 0;font-size:15.5px}
#kSocial .soMedia img,#kSocial .soMedia video{max-width:100%;border-radius:12px;display:block;margin:6px 0;max-height:70vh}
#kSocial .soMedia audio{width:100%;margin:6px 0}
#kSocial .soAct{display:flex;gap:6px;flex-wrap:wrap}
#kSocial .soAct button,#kSocial .soRow button{min-height:40px;border-radius:10px;padding:0 12px;font:700 13.5px system-ui,sans-serif}
#kSocial .soAct button.on{background:#ff4f6d!important;color:#fff!important}
#kSocial textarea,#kSocial input[type=text]{width:100%;box-sizing:border-box;border-radius:12px;padding:10px;font:15px system-ui,sans-serif;min-height:44px}
#kSocial textarea{min-height:110px}
#kSocial .soRow{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin:8px 0}
#kSocial .soN{font-size:13px;opacity:.85}
#kSocial .soGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(52px,1fr));gap:6px}
#kSocial .soGrid button{min-height:52px;font-size:26px;border-radius:12px}
#kSocial .soGrid button.on{outline:3px solid #ffe94a}
#kSocial .soChips{display:flex;flex-wrap:wrap;gap:6px}
#kSocial .soChips button{min-height:36px;border-radius:18px;padding:0 12px;font:700 13px system-ui,sans-serif}
#kSocial .soChips button.on{background:#c9a7ff!important;color:#14163a!important}
#kSocial .soCom{margin-top:8px;padding-top:8px;border-top:1px solid rgba(255,255,255,.12);font-size:14px}
#kSocial .soCom div{margin:4px 0}
#kSocial .soLib{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
#kSocial .soLib .soCard{margin:0}
#kSocial canvas.soMeme{max-width:100%;border-radius:12px;display:block;margin:6px 0}
html body #rDock#rDock #kdSocial.on{background:#ffe94a!important}`; document.head.appendChild(css);
 function box(){ let d=$('kSocial'); if(!d){ d=document.createElement('div'); d.id='kSocial'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','DD Universe Social'); document.body.appendChild(d); d.addEventListener('click',onClick); d.addEventListener('change',onChange); d.addEventListener('input',onInput); } return d; }
 const av=(p)=>'<div class="soAv">'+(p&&p.photoUrl?'<img alt="" src="'+esc(p.photoUrl)+'">':esc((p&&p.avatar)||'🌟'))+'</div>';
 const TABS=[['feed','🏠 Feed'],['create','➕ Create'],['profile','👤 Profile'],['library','📚 Library'],['about','ℹ About']];
 async function paint(){ const d=box(); if(d.hidden) return; await loadMine(); if(me&&me.photo){ const u=await mediaURL(me.photo); me.photoUrl=u&&u.url; }
  let body='';
  if(needMe()&&tab!=='about') body=profileForm(true);
  else if(tab==='feed') body=await feed(); else if(tab==='create') body=createForm(); else if(tab==='profile') body=await profile(); else if(tab==='library') body=await library(); else body=about();
  d.innerHTML='<div class="kBar" data-sc="kSocial"><button type="button" data-ka="close" data-so="close">✕</button></div><div class="soIn"><div class="soBrand">The Omni-Compass LLC · DD Universe Multi-Media Studios · Social</div><h2>🌐 DD Universe Social</h2>'+
   '<div class="soTabs" role="tablist">'+TABS.map(([k,l])=>'<button type="button" role="tab" data-so="tab" data-t="'+k+'" class="'+(k===tab?'on':'')+'" aria-selected="'+(k===tab)+'" data-noul>'+l+'</button>').join('')+'<button type="button" data-so="close" data-noul>✕</button></div>'+body+
   '<p class="soN" style="margin-top:24px">© 2026 The Omni-Compass LLC and DD Universe Multi-Media Studios. All rights reserved.</p></div>';
  hydrate(); }
 /* ---------- feed ---------- */
 async function postCard(p){ const off=!!p.official; const who=off?{avatar:'💜',name:'DD Universe Multi-Media Studios'}:me; const m=p.meta||{};
  let media=''; if(off&&p.mediaUrl){ const t=p.mediaType||''; media=t.startsWith('video')?'<video controls playsinline src="'+esc(p.mediaUrl)+'"></video>':t.startsWith('audio')?'<audio controls src="'+esc(p.mediaUrl)+'"></audio>':'<img alt="" src="'+esc(p.mediaUrl)+'">'; }
  if(!off&&m.mediaId){ const u=await mediaURL(m.mediaId); if(u) media=u.type==='video'?'<video controls playsinline src="'+u.url+'"></video>':u.type==='audio'?'<audio controls src="'+u.url+'"></audio>':'<img alt="" src="'+u.url+'">'; }
  const liked=off?getLS('kanin-likes',{})[p.id]:m.liked; const likes=off?(liked?1:0):(m.likes||0); const coms=off?(getLS('kanin-offcom',{})[p.id]||[]):(m.comments||[]);
  return '<div class="soCard" data-pid="'+esc(p.id)+'" data-off="'+(off?1:0)+'"><div class="soHead">'+(off?'<div class="soAv">💜</div>':av(me))+'<div class="soWho"><b>'+esc(who.name||'You')+(off?'<span class="soBadge">OFFICIAL</span>':'')+'</b><span>'+(off?'@dduniverse':'@'+esc(me.handle||'you'))+' · '+ago(p.at||Date.now())+(off?'':' · 🔒 on this device')+'</span></div></div>'+
   (p.text||m.text?'<div class="soText">'+esc(p.text||m.text)+'</div>':'')+'<div class="soMedia">'+media+'</div>'+
   '<div class="soAct"><button type="button" data-so="like" class="'+(liked?'on':'')+'" data-noul>❤ '+likes+'</button><button type="button" data-so="com" data-noul>💬 '+coms.length+'</button><button type="button" data-so="share" data-noul>📤 Share</button>'+((!off)||(off&&isOwner)?'<button type="button" data-so="del" data-noul>🗑 Delete</button>':'')+'</div>'+
   '<div class="soCom">'+coms.map(c=>'<div>'+(c.me?esc(me.avatar||'🌟')+' <b>'+esc(me.name||'You')+'</b>':'💬')+' '+esc(c.t)+' <span class="soN">· '+ago(c.at)+'</span></div>').join('')+'<div class="soRow"><input type="text" data-com="'+esc(p.id)+'" placeholder="Write a comment…" aria-label="Write a comment" maxlength="400"><button type="button" data-so="send" data-noul>Send</button></div></div></div>'; }
 async function feed(){ const all=[...official,...mine].sort((a,b)=>(b.at||0)-(a.at||0)); let h='<div class="soRow"><button type="button" data-so="tab" data-t="create" data-noul>➕ Make a post</button><button type="button" data-so="studioPost" data-noul>🎛 Post my beat</button><button type="button" data-so="jokePost" data-noul>😂 Post today’s joke</button><button type="button" data-so="scopePost" data-noul>♈ Post my LuvMyZodiac reading</button></div>';
  if(offState==='loading') h+='<div class="soN">Loading the official feed…</div>';
  if(!all.length) h+='<div class="soCard"><b>Your feed is empty.</b><div class="soN">Make your first post: a thought, a photo, a video, a meme, a song you recorded in 🎤 Karaoke or a beat from 🎛 Studio.</div></div>';
  for(const p of all) h+=await postCard(p); return h; }
 /* ---------- create ---------- */
 function createForm(){ return '<div class="soCard"><div class="soHead">'+av(me)+'<div class="soWho"><b>'+esc(me.name)+'</b><span>@'+esc(me.handle||'you')+'</span></div></div>'+
   '<textarea id="soText" maxlength="2000" placeholder="What’s happening? Say it, sing it, show it.">'+esc(draft.text)+'</textarea>'+
   '<div class="soRow"><label class="soN">📷 Photo or 🎥 video <input type="file" id="soFile" accept="image/*,video/*,audio/*"></label><label class="soN">📱 Shoot now <input type="file" id="soCam" accept="image/*,video/*" capture="environment"></label></div>'+
   '<div class="soRow"><button type="button" data-so="fromlib" data-noul>📚 From my library</button><button type="button" data-so="meme" data-noul>🖼 Meme maker</button><button type="button" data-so="studioPost" data-noul>🎛 My beat</button><button type="button" data-so="jokePost" data-noul>😂 Joke of the day</button><button type="button" data-so="scopePost" data-noul>♈ LuvMyZodiac reading</button></div>'+
   '<div id="soPick"></div><div id="soPrev" class="soMedia"></div>'+
   '<div class="soRow"><button type="button" data-so="post" data-noul style="background:#ffe94a;color:#14163a">🚀 Post</button>'+(isOwner?'<button type="button" data-so="postoff" data-noul>📣 Post to everyone (official)</button>':'')+'<span class="soN">'+(isOwner?'Post keeps it on this device; 📣 Official goes to everyone signed in.':'Your posts are kept on this device, private to you.')+'</span></div></div>'; }
 /* ---------- profile ---------- */
 function profileForm(first){ const p=me||{avatar:'🌟',name:'',handle:'',bio:'',genres:[]}; return '<div class="soCard">'+(first?'<h3>👋 Make your profile</h3><div class="soN">It stays on this device. Pick a name and a character, and everything you make is yours: your posts, songs, beats, photos and stories.</div>':'<h3>✏ Edit your profile</h3>')+
   '<div class="soRow">'+av(p)+'<label class="soN">🖼 Profile photo <input type="file" id="soPhoto" accept="image/*"></label></div>'+
   '<label class="soN">Your name</label><input type="text" id="soName" maxlength="40" value="'+esc(p.name)+'" placeholder="Your name or stage name">'+
   '<label class="soN">@handle</label><input type="text" id="soHandle" maxlength="24" value="'+esc(p.handle)+'" placeholder="yourname">'+
   '<label class="soN">About you</label><textarea id="soBio" maxlength="300" placeholder="A line about you, your music, your art.">'+esc(p.bio||'')+'</textarea>'+
   '<h3>Pick your character</h3><div class="soGrid">'+AV.map(a=>'<button type="button" data-so="av" data-a="'+a+'" class="'+(a===p.avatar?'on':'')+'" data-noul>'+a+'</button>').join('')+'</div>'+
   '<h3>What are you into?</h3><div class="soChips">'+GEN.map(g=>'<button type="button" data-so="gen" data-g="'+esc(g)+'" class="'+((p.genres||[]).includes(g)?'on':'')+'" data-noul>'+esc(g)+'</button>').join('')+'</div>'+
   '<div class="soRow"><button type="button" data-so="saveme" data-noul style="background:#ffe94a;color:#14163a">💾 Save my profile</button></div></div>'; }
 async function profile(){ const n=mine.length, likes=mine.reduce((a,p)=>a+((p.meta||{}).likes||0),0); let sign=''; try{ const z=KSTARS.profile(); sign=z&&z.sign?(' · '+z.sign):''; }catch(_){ }
  let h='<div class="soCard"><div class="soHead">'+av(me)+'<div class="soWho"><b>'+esc(me.name)+'</b><span>@'+esc(me.handle||'you')+sign+'</span></div></div><div class="soText">'+esc(me.bio||'')+'</div><div class="soChips">'+(me.genres||[]).map(g=>'<button type="button" class="on" data-noul>'+esc(g)+'</button>').join('')+'</div><div class="soRow soN">'+n+' posts · '+likes+' likes</div><div class="soRow"><button type="button" data-so="editme" data-noul>✏ Edit profile</button><button type="button" data-so="horo" data-noul>🌞 My daily reading</button></div></div>';
  if(tab==='profile'&&profile.edit) h+=profileForm(false);
  h+='<h3>My posts</h3>'; for(const p of mine) h+=await postCard(p); if(!n) h+='<div class="soN">No posts yet.</div>'; return h; }
 /* ---------- my library ---------- */
 async function library(){ let items=[]; try{ items=(await KLIB.list()).filter(x=>x.kind!=='post'); }catch(_){ }
  const u=await KLIB.usage(); const used=u&&u.usage?(u.usage/1048576).toFixed(1)+' MB used on this device':'';
  let h='<div class="soCard"><b>📚 My library</b><div class="soN">Everything here is on this device, private to you. '+esc(used)+'</div><div class="soRow"><label class="soN">➕ Add a file <input type="file" id="soAdd" accept="audio/*,video/*,image/*" multiple></label><button type="button" data-so="projects" data-noul>📁 My projects (beats, songs, stories)</button><button type="button" data-so="kara" data-noul>🎤 Record in Karaoke</button></div></div>';
  if(!items.length) return h+'<div class="soN">Nothing here yet. Record a take in 🎤 Karaoke and press 📚 Save to my library, or add a file.</div>';
  h+='<div class="soLib">'; for(const it of items){ const m=await mediaURL(it.id); const t=m?m.type:'';
   h+='<div class="soCard" data-lid="'+it.id+'"><b>'+esc(it.name)+'</b><div class="soN">'+(t==='audio'?'🎵 Sound':t==='video'?'🎥 Video':t==='image'?'🖼 Picture':'📄 File')+((it.meta||{}).secs?' · '+it.meta.secs+' s':'')+' · '+ago(it.at)+'</div><div class="soMedia">'+(m?(t==='video'?'<video controls playsinline src="'+m.url+'"></video>':t==='audio'?'<audio controls src="'+m.url+'"></audio>':t==='image'?'<img alt="" src="'+m.url+'">':''):'')+'</div>'+
    '<div class="soAct"><button type="button" data-so="lpost" data-noul>🌐 Post</button>'+(t==='audio'?'<button type="button" data-so="ltrack" data-noul>➕ Track</button><button type="button" data-so="ldeck" data-noul>💿 Deck</button>':'')+'<button type="button" data-so="ldl" data-noul>💾</button><button type="button" data-so="lren" data-noul>✏</button><button type="button" data-so="ldel" data-noul>🗑</button></div></div>'; }
  return h+'</div>'; }
 function about(){ return '<div class="soCard"><h3>How DD Universe Social works</h3><div class="soText">• Your profile, your posts and your library are kept on this device, private to you. Nobody else sees them unless you share or download them.\n• Official posts come from DD Universe Multi-Media Studios and reach everyone signed in.\n• 🗑 Delete removes a post or file from this device for good.\n• 📤 Share copies your words or saves your file so you can send it anywhere.</div>'+
   (isOwner?'<h3>📣 Owner tools</h3><div class="soText">You can post to everyone with 📣 Post to everyone (official) in ➕ Create, and delete any official post. Letting every visitor post to everyone needs DD Universe’s own server (accounts, storage and moderation); this page stays the front door.</div>':'')+'</div>'; }
 /* ---------- after drawing: previews and the meme maker ---------- */
 async function hydrate(){ const pv=$('soPrev'); if(pv){ if(draft.media){ const m=await mediaURL(draft.media); pv.innerHTML=m?(m.type==='video'?'<video controls playsinline src="'+m.url+'"></video>':m.type==='audio'?'<audio controls src="'+m.url+'"></audio>':'<img alt="" src="'+m.url+'">')+'<div class="soRow"><button type="button" data-so="unattach" data-noul>✕ Remove</button></div>':''; } else pv.innerHTML=''; } }
 async function memeUI(){ const pk=$('soPick'); if(!pk) return; const imgs=(await KLIB.list()).filter(x=>x.blob&&/^image/.test(x.blob.type)); pk.innerHTML='<div class="soCard"><b>🖼 Meme maker</b><div class="soRow"><label class="soN">Picture <input type="file" id="soMemeImg" accept="image/*"></label>'+(imgs.length?'<select id="soMemeLib" aria-label="A picture from my library"><option value="">…or one from my library</option>'+imgs.map(x=>'<option value="'+x.id+'">'+esc(x.name)+'</option>').join('')+'</select>':'')+'</div><input type="text" id="soTop" placeholder="Top line" maxlength="80"><input type="text" id="soBot" placeholder="Bottom line" maxlength="80" style="margin-top:6px"><canvas class="soMeme" id="soMemeCv" width="600" height="600"></canvas><div class="soRow"><button type="button" data-so="memeuse" data-noul>✅ Use this meme</button></div></div>'; draft.meme={img:null}; drawMeme(); }
 function drawMeme(){ const cv=$('soMemeCv'); if(!cv) return; const g=cv.getContext('2d'); const im=draft.meme&&draft.meme.img; if(im){ const w=600, h=Math.round(600*im.height/im.width); cv.width=w; cv.height=Math.min(h,900); g.drawImage(im,0,0,cv.width,cv.height); } else { cv.width=600; cv.height=600; const gr=g.createLinearGradient(0,0,600,600); gr.addColorStop(0,'#3b1670'); gr.addColorStop(1,'#ff4f6d'); g.fillStyle=gr; g.fillRect(0,0,600,600); }
  const line=(t,y)=>{ if(!t) return; let fs=58; g.font='900 '+fs+'px Impact, "Arial Black", system-ui, sans-serif'; while(g.measureText(t.toUpperCase()).width>cv.width-30&&fs>22){ fs-=4; g.font='900 '+fs+'px Impact, "Arial Black", system-ui, sans-serif'; } g.textAlign='center'; g.lineWidth=Math.max(4,fs/8); g.strokeStyle='#000'; g.fillStyle='#fff'; g.strokeText(t.toUpperCase(),cv.width/2,y(fs)); g.fillText(t.toUpperCase(),cv.width/2,y(fs)); };
  line(($('soTop')||{}).value,fs=>fs+10); line(($('soBot')||{}).value,()=>cv.height-22); }
 const loadImg=blob=>new Promise((res,rej)=>{ const i=new Image(); i.onload=()=>res(i); i.onerror=rej; i.src=URL.createObjectURL(blob); });
 /* ---------- actions ---------- */
 async function addFile(f,name){ const it=await KLIB.save({kind:/^audio/.test(f.type)?'audio':/^video/.test(f.type)?'video':/^image/.test(f.type)?'image':'file',name:name||f.name.replace(/\.[^.]+$/,''),blob:f}); return it; }
 async function makePost(text,mediaId){ if(!text.trim()&&!mediaId) return say('Write something or add a picture, video or sound first.'); await KLIB.save({kind:'post',name:(text||'Post').slice(0,40),meta:{text:text.trim(),mediaId,likes:0,liked:false,comments:[]}}); draft={text:'',media:null,meme:null}; say('🚀 Posted. It is on your profile and in your feed, on this device.'); tab='feed'; paint(); }
 async function postOfficial(text,mediaId){ if(!isOwner||!db) return say('Only the owner posts to everyone.'); let mediaUrl='', mediaType=''; if(mediaId){ const it=await KLIB.get(mediaId); if(it&&it.blob){ if(!assets) return say('Uploading needs the owner’s upload permission on this page.'); try{ const r=await assets.upload(it.blob); mediaUrl=r.url; mediaType=it.blob.type; }catch(e){ return say('The file could not be uploaded: '+(e&&e.message||'')); } } }
  try{ await db.collection('social/official/posts').doc(KLIB.uid()).set({text:text.trim().slice(0,2000),mediaUrl,mediaType,at:Date.now()}); draft={text:'',media:null,meme:null}; say('📣 Posted to everyone.'); tab='feed'; paint(); }catch(e){ say('The official post did not go through: '+(e&&e.message||e&&e.code||'')); } }
 async function onClick(e){ const b=e.target.closest('[data-so]'); if(!b) return; e.stopPropagation(); const k=b.dataset.so; const card=b.closest('[data-pid]'), lc=b.closest('[data-lid]');
  switch(k){
   case 'close': return close();
   case 'tab': tab=b.dataset.t; profile.edit=false; return paint();
   case 'av': (me=me||{}).avatar=b.dataset.a; b.parentNode.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b)); return;
   case 'gen': { me=me||{}; const g=b.dataset.g; me.genres=me.genres||[]; me.genres=me.genres.includes(g)?me.genres.filter(x=>x!==g):me.genres.concat([g]); b.classList.toggle('on'); return; }
   case 'saveme': { me=me||{}; me.name=($('soName').value||'').trim(); me.handle=($('soHandle').value||'').trim().replace(/[^\w.]/g,'').slice(0,24)||me.name.toLowerCase().replace(/[^\w]/g,'').slice(0,20); me.bio=($('soBio').value||'').trim(); me.avatar=me.avatar||'🌟'; if(!me.name) return say('Pick a name first.'); me.created=me.created||Date.now(); const keep=Object.assign({},me); delete keep.photoUrl; putLS('kanin-me',keep); try{ const z=KSTARS.profile(); if(z&&!z.name){ z.name=me.name; KSTARS.save&&KSTARS.save(z); } }catch(_){ } say('💾 Profile saved on this device.'); profile.edit=false; return paint(); }
   case 'editme': profile.edit=true; return paint();
   case 'horo': close(); try{ KSTARS.day(true); }catch(_){ } return;
   case 'post': return makePost(($('soText')||{}).value||draft.text,draft.media);
   case 'postoff': return postOfficial(($('soText')||{}).value||draft.text,draft.media);
   case 'unattach': draft.media=null; return hydrate();
   case 'meme': return memeUI();
   case 'memeuse': { const cv=$('soMemeCv'); if(!cv) return; cv.toBlob(async bl=>{ const it=await KLIB.save({kind:'image',name:'Meme '+new Date().toLocaleDateString(),blob:bl,meta:{meme:true}}); draft.media=it.id; draft.text=($('soText')||{}).value||draft.text; $('soPick').innerHTML=''; hydrate(); say('🖼 Meme ready. Press 🚀 Post.'); },'image/png'); return; }
   case 'fromlib': { const pk=$('soPick'); const items=(await KLIB.list()).filter(x=>x.kind!=='post'&&x.blob); pk.innerHTML='<div class="soCard"><b>📚 Pick from my library</b>'+(items.length?'<div class="soRow">'+items.slice(0,40).map(x=>'<button type="button" data-so="pick" data-id="'+x.id+'" data-noul>'+(/^audio/.test(x.blob.type)?'🎵':/^video/.test(x.blob.type)?'🎥':'🖼')+' '+esc(x.name)+'</button>').join('')+'</div>':'<div class="soN">Your library is empty.</div>')+'</div>'; return; }
   case 'pick': draft.media=b.dataset.id; draft.text=($('soText')||{}).value||draft.text; $('soPick').innerHTML=''; return hydrate();
   case 'studioPost': { try{ const P=window.PADSTUDIO; if(!P||!P.renderBeat) throw 0; say('🎛 Rendering your beat…'); const buf=await P.renderBeat(1,8); if(!buf||!buf.duration) throw 0; const it=await KLIB.saveAudio(buf,'My beat '+P.bpm()+' BPM',{from:'studio'}); draft.media=it.id; tab='create'; paint(); }catch(_){ say('Open 🎛 Studio and make a beat first, then press 🎛 My beat.'); } return; }
   case 'jokePost': { let t=''; try{ const j=KHUMOR.today(); t=Array.isArray(j)?j[1]:(j&&j.text)||String(j||''); }catch(_){ } draft.text='😂 '+(t||''); tab='create'; return paint(); }
   case 'scopePost': { let t=''; try{ const z=KSTARS.profile(); t='🌞 Today for '+(z&&z.sign?z.sign:'my sign')+': '; }catch(_){ } draft.text=t+'(open ♈ LuvMyZodiac and paste today’s reading)'; tab='create'; return paint(); }
   case 'like': if(card){ const id=card.dataset.pid; if(card.dataset.off==='1'){ const L=getLS('kanin-likes',{}); L[id]=!L[id]; putLS('kanin-likes',L); } else { const it=mine.find(p=>p.id===id); if(it){ const m=Object.assign({},it.meta); m.liked=!m.liked; m.likes=Math.max(0,(m.likes||0)+(m.liked?1:-1)); await KLIB.update(id,{meta:m}); } } paint(); } return;
   case 'com': if(card){ const i=card.querySelector('[data-com]'); if(i) i.focus(); } return;
   case 'send': if(card){ const i=card.querySelector('[data-com]'); const t=(i&&i.value||'').trim(); if(!t) return; const id=card.dataset.pid; if(card.dataset.off==='1'){ const C=getLS('kanin-offcom',{}); (C[id]=C[id]||[]).push({t,at:Date.now(),me:true}); putLS('kanin-offcom',C); } else { const it=mine.find(p=>p.id===id); if(it){ const m=Object.assign({},it.meta); m.comments=(m.comments||[]).concat([{t,at:Date.now(),me:true}]); await KLIB.update(id,{meta:m}); } } paint(); } return;
   case 'share': if(card){ const txt=card.querySelector('.soText'); const t=(txt&&txt.textContent||'')+'\n— DD Universe Multi-Media Studios'; try{ await navigator.clipboard.writeText(t); say('📤 Copied. Paste it anywhere.'); }catch(_){ say('Select the words and copy them to share.'); } } return;
   case 'del': if(card){ const id=card.dataset.pid; if(card.dataset.off==='1'){ if(isOwner&&db){ try{ await db.collection('social/official/posts').doc(id).delete(); say('🗑 Official post deleted.'); }catch(_){ say('It could not be deleted.'); } } } else { if(!b.dataset.sure){ b.dataset.sure='1'; b.textContent='Tap again to delete'; return; } await KLIB.del(id); say('🗑 Deleted from this device.'); paint(); } } return;
   case 'projects': close(); try{ FILES.dock(); }catch(_){ try{ KRAIL.goTo('fileDock'); }catch(__){ } } return;
   case 'kara': close(); try{ KKARA.open(); }catch(_){ } return;
   case 'lpost': if(lc){ draft.media=lc.dataset.lid; tab='create'; paint(); } return;
   case 'ltrack': case 'ldeck': if(lc){ try{ const it=await KLIB.get(lc.dataset.lid); const c=(PADSTUDIO&&PADSTUDIO.ac&&PADSTUDIO.ac())||new AudioContext(); const buf=await c.decodeAudioData(await it.blob.arrayBuffer()); if(k==='ltrack'){ const bars=Math.max(1,Math.min(32,Math.round(buf.duration/(240/PADSTUDIO.bpm())))); PADADDLOOP(buf,it.name,bars,{mode:'native',vocal:true,on:new Array(32).fill(false).map((_,i)=>i<bars)}); say('➕ '+it.name+' is on the vocal track (channel 24).'); } else { DJBOOTH.loadBuf('B',buf,it.name); say('💿 '+it.name+' is on DJ deck B.'); } }catch(_){ say('Open 🎛 Studio once, then try again.'); } } return;
   case 'ldl': if(lc){ const it=await KLIB.get(lc.dataset.lid); if(it&&it.blob){ const ext=(it.blob.type.split('/')[1]||'bin').replace('jpeg','jpg').replace(/;.*/,''); const ok=await KLIB.download(it.blob,(it.name||'file').replace(/[^\w\- ]+/g,'')+'.'+ext); say(ok?'💾 Saving…':'Saving files is not allowed here.'); } } return;
   case 'lren': if(lc){ const it=await KLIB.get(lc.dataset.lid); const nb=lc.querySelector('b'); const inp=document.createElement('input'); inp.type='text'; inp.value=it.name; inp.maxLength=60; nb.replaceWith(inp); inp.focus(); inp.addEventListener('keydown',async ev=>{ if(ev.key==='Enter'){ await KLIB.update(it.id,{name:inp.value.trim()||it.name}); paint(); } }); inp.addEventListener('blur',async()=>{ await KLIB.update(it.id,{name:inp.value.trim()||it.name}); paint(); }); } return;
   case 'ldel': if(lc){ if(!b.dataset.sure){ b.dataset.sure='1'; b.textContent='Tap again'; return; } await KLIB.del(lc.dataset.lid); say('🗑 Deleted from this device.'); paint(); } return; } }
 async function onChange(e){ const t=e.target; const f=t.files&&t.files[0];
  if((t.id==='soFile'||t.id==='soCam')&&f){ draft.text=($('soText')||{}).value||draft.text; const it=await addFile(f); draft.media=it.id; t.value=''; return hydrate(); }
  if(t.id==='soPhoto'&&f){ const it=await addFile(f,'Profile photo'); me=me||{}; me.photo=it.id; const keep=Object.assign({},me); delete keep.photoUrl; putLS('kanin-me',keep); return paint(); }
  if(t.id==='soAdd'&&t.files){ for(const x of t.files) await addFile(x); say('➕ Added to your library.'); t.value=''; return paint(); }
  if(t.id==='soMemeImg'&&f){ draft.meme={img:await loadImg(f)}; return drawMeme(); }
  if(t.id==='soMemeLib'&&t.value){ const it=await KLIB.get(t.value); if(it&&it.blob){ draft.meme={img:await loadImg(it.blob)}; drawMeme(); } } }
 function onInput(e){ if(e.target.id==='soTop'||e.target.id==='soBot') drawMeme(); if(e.target.id==='soText') draft.text=e.target.value; if(e.target.dataset&&e.target.dataset.com!=null&&e.key==='Enter'){} }
 document.addEventListener('keydown',e=>{ const t=e.target; if(t&&t.dataset&&t.dataset.com!=null&&e.key==='Enter'){ const card=t.closest('[data-pid]'); const b=card&&card.querySelector('[data-so="send"]'); if(b) b.click(); } },true);
 function open(which){ if(!me) me=getLS('kanin-me',null); const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner','kVG'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ } if(which) tab=which; d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kSocial'); if(d) d.hidden=true; }
 function compose(o){ draft={text:o&&o.text||'',media:o&&o.media||null,meme:null}; open('create'); }
 try{ const gh=window.GOHOME; if(gh&&!gh.__ksoc){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__ksoc=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')) close(); },true);
 setInterval(()=>{ const b=$('kdSocial'), d=$('kSocial'); if(b) b.classList.toggle('on',!!(d&&!d.hidden)); },700);
 setTimeout(boot,1500);
 window.KSOCIAL={open,close,compose,me:()=>me};
})();
