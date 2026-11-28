(()=>{ /* 📁 PROJECTS: the person's own place. Their profile on top, then everything they have made, in drawers: stories, beats and
   instrumentals, songs and lyrics, karaoke takes, DJ sets, art and drawings, photos, videos, posts, charts and readings. Every piece
   can be continued, renamed, duplicated, deleted, and exported in the right format:
   sound WAV (studio) or WebM audio (shares anywhere, and the one claude.ai lets a page save) · words PDF, Word (.doc) or text ·
   drawings PNG · photos JPG · video MP4 / WebM · any project as a KAN-IN project file (.json) to open again on any device.
   It all lives on this device, private to the person. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const ago=t=>{ const s=(Date.now()-t)/1000; return s<60?'just now':s<3600?Math.floor(s/60)+' min ago':s<86400?Math.floor(s/3600)+' h ago':new Date(t).toLocaleDateString(); };
 const CATS=[['all','🗂 Everything'],['story','📖 Stories'],['beat','🥁 Beats & instrumentals'],['song','✍ Songs, lyrics & scripts'],['vocal','🎤 Karaoke & vocals'],['dj','🎧 DJ sets'],['art','🎨 Art & drawings'],['photo','📷 Photos'],['video','🎬 Videos'],['post','🌐 Posts'],['chart','🧭 Charts & readings'],['other','🧬 Everything else']];
 const FK={beat:'beat',music:'beat',dj:'dj',song:'song',prompter:'song',mutation:'song',translation:'story',craft:'story',video:'video',chart:'chart',compass:'chart',voices:'vocal'};
 const NEW=[['📖','New story',()=>{ try{ GOHOME(); }catch(_){ } const b=$('mQP')||$('qpBtn'); if(b) b.click(); }],['🥁','New beat',()=>{ try{ KRAIL.goTo('pad'); }catch(_){ } }],['🎤','New song in Karaoke',()=>{ try{ KKARA.open(); }catch(_){ } }],['🎧','New DJ set',()=>{ try{ KRAIL.goTo('pad'); setTimeout(()=>KRAIL.FLOAT.toggle('dj'),1200); }catch(_){ } }],['🎨','New drawing',()=>{ try{ KEASEL.open(); }catch(_){ } }],['🌐','New post',()=>{ try{ KSOCIAL.open('create'); }catch(_){ } }],['🤖','Write with AI',()=>{ try{ KAI.open(); }catch(_){ } }]];
 let cat='all', items=[], urls={};
 const css=document.createElement('style'); css.textContent=`
#kProj{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(10px + env(safe-area-inset-top,0px)) max(12px,env(safe-area-inset-left,0px)) 40px 12px;background:radial-gradient(circle at 50% -10%,#1d3b2c,#071410 62%);color:#effff6;font:15px/1.5 system-ui,sans-serif}
#kProj[hidden]{display:none!important}
#kProj .pjIn{max-width:980px;margin:0 auto}
#kProj h2{font:900 26px/1.15 system-ui,sans-serif;margin:4px 0;color:#7cff8a;text-align:center}
#kProj .pjMe{display:flex;align-items:center;gap:12px;justify-content:center;flex-wrap:wrap;background:rgba(255,255,255,.06);border:1px solid rgba(124,255,138,.3);border-radius:16px;padding:10px;margin:8px 0}
#kProj .pjAv{width:52px;height:52px;border-radius:50%;background:#16342a;display:flex;align-items:center;justify-content:center;font-size:30px;overflow:hidden}
#kProj .pjAv img{width:100%;height:100%;object-fit:cover}
#kProj .pjRow{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}
#kProj .pjRow button{min-height:42px;border-radius:12px;padding:0 12px;font:800 13.5px system-ui,sans-serif}
#kProj .pjCats{position:sticky;top:-10px;z-index:2;background:linear-gradient(180deg,#0b1f17 75%,transparent);padding:8px 0}
#kProj .pjCats button.on{background:#7cff8a!important;color:#07140f!important}
#kProj .pjGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
#kProj .pjCard{background:rgba(255,255,255,.06);border:1px solid rgba(124,255,138,.25);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px;min-width:0}
#kProj .pjCard b{font-size:15px;word-break:break-word}
#kProj .pjN{font-size:12.5px;opacity:.82}
#kProj .pjCard img,#kProj .pjCard video{max-width:100%;border-radius:10px;max-height:180px;object-fit:cover}
#kProj .pjCard audio{width:100%}
#kProj .pjAct{display:flex;flex-wrap:wrap;gap:4px}
#kProj .pjAct button,#kProj .pjAct select{min-height:38px;border-radius:9px;padding:0 9px;font:700 12.5px system-ui,sans-serif}
#kProj .pjExp{background:#1f9d55!important;color:#fff!important}`; document.head.appendChild(css);
 function box(){ let d=$('kProj'); if(d) return d; d=document.createElement('div'); d.id='kProj'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Projects'); document.body.appendChild(d); d.addEventListener('click',onClick); d.addEventListener('change',onChange); return d; }
 async function gather(){ const out=[];
  try{ const L=await FILES.list(); (L||[]).forEach(f=>out.push({src:'file',id:f.id,kind:f.kind,cat:FK[f.kind]||'other',name:f.name||f.title||((FILES.kinds.find?FILES.kinds.find(k=>(k.kind||k)===f.kind):null)||{}).label||f.kind,at:f.at||0})); }catch(_){ }
  try{ const M=await KLIB.list(); M.forEach(m=>{ const t=(m.blob&&m.blob.type)||''; const from=(m.meta||{}).from||''; const c=m.kind==='post'?'post':t.startsWith('audio')?(from==='karaoke'?'vocal':from==='studio'?'beat':'vocal'):t.startsWith('image')?(from==='easel'||(m.meta||{}).meme?'art':'photo'):t.startsWith('video')?'video':'other'; out.push({src:'lib',id:m.id,kind:m.kind,cat:c,name:m.name,at:m.at,type:t,meta:m.meta||{}}); }); }catch(_){ }
  return out.sort((a,b)=>(b.at||0)-(a.at||0)); }
 async function media(id){ if(urls[id]) return urls[id]; try{ const it=await KLIB.get(id); if(it&&it.blob){ urls[id]=URL.createObjectURL(it.blob); return urls[id]; } }catch(_){ } return null; }
 function fmtOpts(it){ if(it.src==='file') return [['json','KAN-IN project file (.json)'],['txt','Words as text (.txt)'],['pdf','Words as PDF'],['doc','Words as Word (.doc)']];
  if(it.cat==='post') return [['pdf','PDF'],['doc','Word (.doc)'],['txt','Text (.txt)']];
  const t=it.type||''; if(t.startsWith('audio')) return [['webm','WebM audio (shares anywhere)'],['wav','WAV (studio quality)']];
  if(t.startsWith('image')) return [['png','PNG (sharp, see-through)'],['jpg','JPG (photo)']];
  if(t.startsWith('video')) return [['orig',t.includes('mp4')?'MP4 video':'WebM video']];
  return [['orig','The file as it is']]; }
 async function paint(){ const d=$('kProj'); if(!d||d.hidden) return; items=await gather(); let me=null; try{ me=KSOCIAL.me(); }catch(_){ }
  const counts={}; items.forEach(i=>{ counts[i.cat]=(counts[i.cat]||0)+1; }); let story=0; try{ story=STORYLIB.count(); }catch(_){ } if(story) counts.story=(counts.story||0)+1;
  const shown=items.filter(i=>cat==='all'||i.cat===cat); let used=''; try{ const u=await KLIB.usage(); if(u&&u.usage) used=(u.usage/1048576).toFixed(1)+' MB used on this device'; }catch(_){ }
  let photo=''; if(me&&me.photo){ const u=await media(me.photo); if(u) photo='<img alt="" src="'+u+'">'; }
  let cards=''; if((cat==='all'||cat==='story')&&story) cards+='<div class="pjCard"><b>📖 My story library</b><div class="pjN">'+story+' stor'+(story===1?'y':'ies')+' · every canvas and draft</div><div class="pjAct"><button type="button" data-pj="stories" data-noul>📂 Open my stories</button><button type="button" data-pj="storyNew" data-noul>➕ New story</button></div></div>';
  for(const it of shown){ let pv=''; if(it.src==='lib'){ const u=await media(it.id); if(u){ pv=it.type.startsWith('image')?'<img alt="" src="'+u+'">':it.type.startsWith('audio')?'<audio controls src="'+u+'"></audio>':it.type.startsWith('video')?'<video controls playsinline src="'+u+'"></video>':''; } if(it.kind==='post') pv='<div class="pjN">'+esc(((it.meta||{}).text||'').slice(0,140))+'</div>'; }
   const lab=(CATS.find(c=>c[0]===it.cat)||['','🧬'])[1].split(' ')[0];
   cards+='<div class="pjCard" data-src="'+it.src+'" data-id="'+esc(it.id)+'"><b>'+lab+' '+esc(it.name||'Untitled')+'</b><div class="pjN">'+(it.src==='file'?'Project · '+esc(it.kind):'Saved file')+' · '+ago(it.at)+'</div>'+pv+
    '<div class="pjAct">'+(it.src==='file'?'<button type="button" data-pj="cont" data-noul>▶ Continue</button>':'')+(it.src==='lib'&&it.kind!=='post'?'<button type="button" data-pj="post" data-noul>🌐 Post</button>':'')+'<select data-pj="fmt" aria-label="Export format">'+fmtOpts(it).map(([v,l])=>'<option value="'+v+'">'+l+'</option>').join('')+'</select><button type="button" class="pjExp" data-pj="exp" data-noul>💾 Export</button><button type="button" data-pj="ren" data-noul>✏</button>'+(it.src==='lib'?'<button type="button" data-pj="dup" data-noul>⧉</button>':'')+'<button type="button" data-pj="del" data-noul>🗑</button></div></div>'; }
  if(!cards) cards='<div class="pjN" style="text-align:center">Nothing here yet. Start something new above.</div>';
  d.innerHTML='<div class="kBar" data-sc="kProj"><button type="button" data-ka="close" data-pj="close">✕</button></div><div class="pjIn"><h2>📁 Projects</h2>'+
   '<div class="pjMe"><div class="pjAv">'+(photo||esc(me&&me.avatar||'🌟'))+'</div><div><b>'+esc(me&&me.name||'Your profile')+'</b><div class="pjN">'+(me&&me.handle?'@'+esc(me.handle)+' · ':'')+items.length+' saved pieces · '+esc(used)+'</div></div><button type="button" data-pj="profile" data-noul>👤 '+(me&&me.name?'Edit profile':'Make your profile')+'</button><button type="button" data-pj="close" data-noul>✕ Close</button></div>'+
   '<div class="pjRow">'+NEW.map(([i,l],n)=>'<button type="button" data-pj="new" data-n="'+n+'" data-noul>'+i+' '+l+'</button>').join('')+'<label class="pjN" style="display:inline-flex;gap:6px;align-items:center">📥 Bring in a file or project <input type="file" id="pjIn" accept="audio/*,video/*,image/*,.json,.txt"></label></div>'+
   '<div class="pjRow pjCats" role="tablist">'+CATS.map(([k,l])=>'<button type="button" role="tab" data-pj="cat" data-c="'+k+'" class="'+(k===cat?'on':'')+'" data-noul>'+l+(k==='all'?' · '+(items.length+(story?1:0)):counts[k]?' · '+counts[k]:'')+'</button>').join('')+'</div>'+
   '<div class="pjGrid">'+cards+'</div><p class="pjN" style="text-align:center;margin-top:18px">Your projects are kept on this device, private to you. 💾 Export saves a copy you can keep, send or open anywhere. © 2026 The Omni-Compass LLC and Omni-Galaxy Multi-Media Studios.</p></div>'; }
 /* ---------- exporting ---------- */
 const safe=n=>(n||'kan-in').replace(/[^\w\- ]+/g,'').trim().slice(0,60)||'kan-in';
 const inFrame=(()=>{ try{ return window.self!==window.top; }catch(_){ return true; } })();
 async function save(blob,name){ if(inFrame&&!/\.(webm|mp4|m4a|txt|json|png|jpg|jpeg|webp|gif|pdf|csv|md)$/i.test(name)) return say('Inside claude.ai this page can save WebM audio, MP4, PDF, PNG, JPG, text and project files. '+name.split('.').pop().toUpperCase()+' files save when KAN-IN runs on its own website.'); const ok=await KLIB.download(blob,name); say(ok?'💾 Saving '+name+'…':'This page could not save the file here.'); }
 function textOf(obj){ const seen=new Set(), out=[]; const walk=(v,k)=>{ if(v==null) return; if(typeof v==='string'){ const t=v.trim(); if(t.length>2&&!/^data:|^[A-Za-z0-9+/=]{80,}$|^#[0-9a-f]{3,8}$/i.test(t)&&!seen.has(t)){ seen.add(t); out.push(t); } return; } if(Array.isArray(v)) return v.forEach(x=>walk(x)); if(typeof v==='object') Object.keys(v).forEach(kk=>walk(v[kk],kk)); }; walk(obj); return out.join('\n\n'); }
 async function pdf(title,text){ if(!window.jspdf){ await new Promise((res,rej)=>{ const s=document.createElement('script'); s.src='https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js'; s.onload=res; s.onerror=rej; document.head.appendChild(s); }); }
  const doc=new jspdf.jsPDF({unit:'pt',format:'letter'}); const M=54, W=612-M*2; let y=M; doc.setFont('helvetica','bold'); doc.setFontSize(18); doc.splitTextToSize(title,W).forEach(l=>{ doc.text(l,M,y); y+=24; }); y+=6; doc.setFont('helvetica','normal'); doc.setFontSize(12);
  for(const l of doc.splitTextToSize(text.replace(/[^\x09\x0a\x0d\x20-\x7e -ÿ’‘“”–—…•]/g,''),W)){ if(y>792-M){ doc.addPage(); y=M; } doc.text(l,M,y); y+=17; }
  doc.setFontSize(9); doc.text('© 2026 The Omni-Compass LLC and Omni-Galaxy Multi-Media Studios. All rights reserved.',M,792-24); return doc.output('blob'); }
 const docx=(title,text)=>new Blob(['<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><title>'+esc(title)+'</title></head><body style="font-family:Calibri,Arial,sans-serif;font-size:12pt"><h1>'+esc(title)+'</h1>'+text.split(/\n{2,}/).map(p=>'<p>'+esc(p).replace(/\n/g,'<br>')+'</p>').join('')+'<p style="font-size:9pt;color:#666">© 2026 The Omni-Compass LLC and Omni-Galaxy Multi-Media Studios. All rights reserved.</p></body></html>'],{type:'application/msword'});
 async function toWebm(blob){ const c=new (window.AudioContext||window.webkitAudioContext)(); const buf=await c.decodeAudioData(await blob.arrayBuffer()); const dest=c.createMediaStreamDestination(); const s=c.createBufferSource(); s.buffer=buf; s.connect(dest); const mt=['audio/webm;codecs=opus','audio/webm','audio/mp4'].find(t=>window.MediaRecorder&&MediaRecorder.isTypeSupported(t)); if(!mt) throw new Error('no recorder'); const mr=new MediaRecorder(dest.stream,{mimeType:mt}); const ch=[]; mr.ondataavailable=e=>ch.push(e.data); const done=new Promise(r=>mr.onstop=r); mr.start(); s.start(); say('🎵 Making the shareable copy: it takes as long as the sound plays ('+buf.duration.toFixed(0)+' s).'); await new Promise(r=>setTimeout(r,buf.duration*1000+250)); mr.stop(); await done; c.close(); return {blob:new Blob(ch,{type:mt.split(';')[0]}),ext:mt.includes('mp4')?'m4a':'webm'}; }
 async function exportIt(card,fmt){ const id=card.dataset.id, src=card.dataset.src;
  if(src==='file'){ let rec=null; try{ rec=await FILES.get(id); }catch(_){ } if(!rec) return say('That project could not be read.'); const name=safe(rec.name||rec.kind);
   if(fmt==='json') return save(new Blob([JSON.stringify({app:'KAN-IN',by:'Omni-Galaxy Multi-Media Studios Platform',v:1,project:rec},null,1)],{type:'application/json'}),name+'.json');
   const text=textOf(rec.data||rec); if(fmt==='txt') return save(new Blob([text],{type:'text/plain'}),name+'.txt'); if(fmt==='doc') return save(docx(name,text),name+'.doc'); if(fmt==='pdf'){ try{ return save(await pdf(name,text),name+'.pdf'); }catch(_){ return say('The PDF maker did not load. Try again when you are online.'); } } return; }
  const it=await KLIB.get(id); if(!it) return; const name=safe(it.name);
  if(it.kind==='post'){ const text=(it.meta||{}).text||''; if(fmt==='txt') return save(new Blob([text],{type:'text/plain'}),name+'.txt'); if(fmt==='doc') return save(docx(name,text),name+'.doc'); try{ return save(await pdf(name,text),name+'.pdf'); }catch(_){ return say('The PDF maker did not load.'); } }
  const t=it.blob.type||'';
  if(t.startsWith('audio')){ if(fmt==='wav') return save(it.blob,name+'.wav'); try{ const r=await toWebm(it.blob); return save(r.blob,name+'.'+r.ext); }catch(_){ return say('This browser cannot make that copy; try 💾 WAV.'); } }
  if(t.startsWith('image')){ if(fmt==='png'&&t==='image/png') return save(it.blob,name+'.png'); const im=await new Promise((res,rej)=>{ const i=new Image(); i.onload=()=>res(i); i.onerror=rej; i.src=URL.createObjectURL(it.blob); }); const cv=document.createElement('canvas'); cv.width=im.naturalWidth; cv.height=im.naturalHeight; const g=cv.getContext('2d'); if(fmt==='jpg'){ g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height); } g.drawImage(im,0,0); const b=await new Promise(r=>cv.toBlob(r,fmt==='jpg'?'image/jpeg':'image/png',.92)); return save(b,name+'.'+(fmt==='jpg'?'jpg':'png')); }
  const ext=(t.split('/')[1]||'bin').replace('quicktime','mov').replace(/;.*/,''); return save(it.blob,name+'.'+ext); }
 async function onClick(e){ const b=e.target.closest('[data-pj]'); if(!b||b.tagName==='SELECT') return; e.stopPropagation(); const k=b.dataset.pj, card=b.closest('.pjCard[data-id]');
  switch(k){
   case 'close': return close();
   case 'cat': cat=b.dataset.c; return paint();
   case 'profile': close(); try{ KSOCIAL.open('profile'); }catch(_){ } return;
   case 'new': close(); try{ NEW[+b.dataset.n][2](); }catch(_){ } return;
   case 'stories': close(); try{ STORYLIB.open(); }catch(_){ } return;
   case 'storyNew': close(); try{ STORYLIB.fresh(); }catch(_){ NEW[0][2](); } return;
   case 'cont': if(card){ close(); try{ await FILES.open(card.dataset.id); say('▶ Picking up where you left off.'); }catch(_){ say('That project could not be opened.'); } } return;
   case 'post': if(card){ close(); try{ KSOCIAL.compose({text:'',media:card.dataset.id}); }catch(_){ } } return;
   case 'exp': if(card){ const f=card.querySelector('select[data-pj="fmt"]'); await exportIt(card,f?f.value:'orig'); } return;
   case 'dup': if(card){ const it=await KLIB.get(card.dataset.id); if(it){ const n=Object.assign({},it); delete n.id; n.at=Date.now(); n.name=it.name+' (copy)'; await KLIB.save(n); say('⧉ A copy is in your projects.'); paint(); } } return;
   case 'ren': if(card){ const nb=card.querySelector('b'); const inp=document.createElement('input'); inp.type='text'; inp.maxLength=60; inp.value=nb.textContent.replace(/^\S+\s/,''); inp.style.minHeight='40px'; nb.replaceWith(inp); inp.focus(); const done=async()=>{ const v=inp.value.trim(); if(v){ if(card.dataset.src==='lib') await KLIB.update(card.dataset.id,{name:v}); else say('Rename a project inside its own screen (▶ Continue, then its title).'); } paint(); }; inp.addEventListener('keydown',ev=>{ if(ev.key==='Enter') done(); }); inp.addEventListener('blur',done); } return;
   case 'del': if(card){ if(!b.dataset.sure){ b.dataset.sure='1'; b.textContent='Tap again to delete'; return; } if(card.dataset.src==='lib'){ await KLIB.del(card.dataset.id); say('🗑 Deleted from this device.'); paint(); } else say('Projects are deleted from their own screen’s 📁 Library.'); } return; } }
 async function onChange(e){ const t=e.target; if(t.id==='pjIn'&&t.files&&t.files[0]){ const f=t.files[0]; t.value='';
   if(/\.json$/i.test(f.name)){ try{ const o=JSON.parse(await f.text()); if(o&&o.project&&o.project.kind){ say('📥 Project file read. Open its screen and use 📁 Library → Open to load it.'); await KLIB.save({kind:'file',name:f.name.replace(/\.json$/,''),blob:new Blob([JSON.stringify(o)],{type:'application/json'}),meta:{project:true}}); } }catch(_){ say('That file is not a KAN-IN project.'); } return paint(); }
   await KLIB.save({kind:/^audio/.test(f.type)?'audio':/^video/.test(f.type)?'video':/^image/.test(f.type)?'image':'file',name:f.name.replace(/\.[^.]+$/,''),blob:f}); say('📥 Added to your projects.'); paint(); } }
 function open(c){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner','kVG','kSocial','kAI','kEasel'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ } if(c) cat=c; d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kProj'); if(d) d.hidden=true; }
 try{ const gh=window.GOHOME; if(gh&&!gh.__kpj){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kpj=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')) close(); },true);
 /* the Menu: 📁 Projects first in "Me" */
 setInterval(()=>{ const t=$('tourTab'); if(!t||$('ttProj')) return; const b=document.createElement('button'); b.type='button'; b.id='ttProj'; b.className='ttMusic'; b.textContent='📁 Projects · my profile, my files, my work'; b.style.order='100'; b.dataset.kg='0'; b.dataset.kmSoc='1'; b.dataset.kmDone='1'; b.setAttribute('data-noul',''); b.style.gridColumn='1/-1'; b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(open,120); }); t.appendChild(b); const g=$('kSocGrp'); if(g) g.textContent='👤 Me: projects, profile and social'; },900);
 window.KPROJ={open,close};
})();
