(()=>{ /* 💃 DANCE KARAOKE (v258): karaoke you dance instead of sing. Pick the music (your beat from the beat machine, a DJ deck, a song you
   upload, or a plain count), press ● and dance: the camera records you while the music plays and the frame flashes on every beat, after a
   3-2-1 count-in. Where the browser lets the page use the camera (the platform's own website), the recording carries the music inside it;
   where it does not (inside claude.ai), 📱 records with the phone's own camera app or ⬆ takes a video you already made, and ▶ Play
   together plays your dance and the music side by side from the same count-in. Every dance can be saved to your library, downloaded,
   or posted to your page. 🌍 Dance community holds the dance styles, each with where its dancers share (video platforms and forums),
   and 💥 Cannon challenge lets the cannon pick a style, a tempo and four moves to dance. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); const enc=encodeURIComponent;
 const YT=q=>'https://www.youtube.com/results?search_query='+enc(q), TT=q=>'https://www.tiktok.com/search?q='+enc(q), IG=t=>'https://www.instagram.com/explore/tags/'+enc(t.replace(/[^a-z0-9]/gi,'').toLowerCase())+'/', RD=q=>'https://www.reddit.com/search/?q='+enc(q), WK=q=>'https://en.wikipedia.org/wiki/Special:Search?go=Go&search='+enc(q);
 const PS=()=>window.PADSTUDIO;
 /* the dance styles: [name, one line, tempo range, four signature moves] */
 const STY=[['Hip-hop','Street dance grown from the hip-hop culture of the Bronx in the 1970s.','85–100',['Two-step','Bounce','Body roll','Shoulder lean']],
  ['Breaking','Breakdancing: top rock, footwork, power moves and freezes, battled in cyphers.','110–135',['Top rock','Six-step','Windmill','Baby freeze']],
  ['Popping','Contracting the muscles in time with the beat to make a pop.','95–110',['Arm pop','Neck pop','Wave','Tut']],
  ['Locking','A funk style of quick locks, points and wrist rolls.','100–120',['Lock','Point','Wrist roll','Scooby doo']],
  ['Krump','An expressive, high-energy style from Los Angeles.','95–110',['Chest pop','Stomp','Arm swing','Jab']],
  ['House','Fast footwork and loose upper body to house music.','118–128',['Jack','Loose legs','Shuffle','Heel-toe']],
  ['Shuffle','Running-man and T-step footwork to electronic music.','125–130',['Running man','T-step','Charleston','Spin']],
  ['Afrobeats','Grooves from West African pop, with hips, shoulders and footwork.','100–115',['Shaku shaku','Gwara gwara','Azonto','Shoulder groove']],
  ['Amapiano','South African log-drum grooves with smooth footwork.','110–115',['Pouncing cat','Bacardi step','Shuffle back','Hip roll']],
  ['Dancehall','Jamaican dance with named steps and strong rhythm.','90–100',['Gully creepa','Willie bounce','Bogle','Tek weh yuhself']],
  ['Reggaeton','Latin urban dance on the dembow rhythm.','88–100',['Perreo','Hip sway','Body wave','Step touch']],
  ['Salsa','Latin partner dance counted in eight, on 1 or on 2.','160–220',['Basic step','Cross-body lead','Right turn','Shine']],
  ['Bachata','Dominican partner dance with a tap on the fourth beat.','120–140',['Basic','Side step','Turn','Hip roll']],
  ['K-pop dance','Choreography from Korean pop, sharp and in unison.','100–130',['Point move','Arm wave','Formation change','Hit pose']],
  ['Jazz dance','Theatrical dance of kicks, turns and leaps.','110–140',['Jazz walk','Pas de bourrée','Kick ball change','Pirouette']],
  ['Ballet','Classical dance of turnout, line and technique.','60–120',['Plié','Tendu','Arabesque','Pirouette']],
  ['Contemporary','Expressive dance joining modern, jazz and ballet.','60–110',['Floor roll','Contraction','Release','Spiral']],
  ['Tap','Rhythm made by metal taps on the shoes.','100–200',['Shuffle','Flap','Ball change','Time step']],
  ['Line dance','Rows of dancers doing the same steps to country and pop.','110–130',['Grapevine','Heel dig','Kick','Quarter turn']],
  ['Twerk','A hip-led dance with roots in New Orleans bounce.','95–105',['Bounce','Hip pop','Wind','Drop']],
  ['Waacking','Arm rotations and poses from the disco clubs of Los Angeles.','115–125',['Arm whip','Pose','Strut','Point']],
  ['Voguing','Poses and runway walks from the ballroom scene of New York.','120–130',['Hands','Catwalk','Duckwalk','Dip']],
  ['Bhangra','Energetic folk dance of the Punjab.','90–110',['Bhangra bounce','Shoulder shrug','Jump','Arm raise']],
  ['Flamenco','Spanish dance of footwork, arms and palmas.','90–180',['Zapateado','Braceo','Palmas','Vuelta']]];
 const PLAT=[['TikTok','Short dance videos and challenges','https://www.tiktok.com'],['YouTube Shorts','Short vertical videos','https://www.youtube.com/shorts'],['Instagram Reels','Short videos on Instagram','https://www.instagram.com/reels/'],['Snapchat Spotlight','Short videos on Snapchat','https://www.snapchat.com/spotlight'],['Triller','Music video app','https://triller.co'],['Likee','Short video app','https://likee.video']];
 const LEARN=[['STEEZY','Online dance classes','https://www.steezy.co'],['CLI Studios','Online dance training','https://www.clistudios.com'],['Just Dance Now','Dance game played with a phone','https://justdancenow.com'],['YouTube dance tutorials','Free lessons for every style','https://www.youtube.com/results?search_query=dance+tutorial+for+beginners']];
 const FORUM=[['Reddit: dance','Communities of dancers on Reddit','https://www.reddit.com/search/?q=dance&type=sr'],['Dance-Forums.com','A long-running forum for many styles','https://www.dance-forums.com']];
 let tab='now', music='beat', song=null, stream=null, rec=null, chunks=[], take=null, beatT=null, songEl=null;
 const css=document.createElement('style'); css.textContent=`
#kDance{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9600;overflow-y:auto;background:radial-gradient(circle at 50% 0,#3b0f5c,#08051a 72%);color:#f6eeff;font:15px/1.5 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 40px}
#kDance[hidden]{display:none!important}
#kDance .dkIn{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
#kDance .dkTop{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;padding-right:min(300px,34vw)}
#kDance h2{margin:0;font:900 clamp(22px,4vw,32px) system-ui,sans-serif;color:#ff8ad8}
#kDance button,#kDance select{min-height:44px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif}
#kDance .dkTabs,#kDance .dkRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
#kDance .dkTabs button.on{background:#ff8ad8!important;color:#1a0420!important}
#kDance .dkStage{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px}
@media (max-width:760px){#kDance .dkStage{grid-template-columns:minmax(0,1fr)}}
#kDance .dkScreen{position:relative;aspect-ratio:9/16;max-height:62vh;width:100%;background:#000;border-radius:12px;overflow:hidden;border:4px solid #3a1d63;transition:border-color .06s}
#kDance .dkScreen.flash{border-color:#ff8ad8}
#kDance .dkScreen video{width:100%;height:100%;object-fit:cover;display:block}
#kDance .dkCount{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:900 96px system-ui,sans-serif;color:#fff;text-shadow:0 0 30px #ff8ad8;pointer-events:none}
#kDance .dkTag{position:absolute;left:8px;top:8px;background:rgba(0,0,0,.6);border-radius:999px;padding:2px 10px;font:800 12px system-ui,sans-serif}
#kDance .dkGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
#kDance .dkCard{background:rgba(0,0,0,.3);border-left:3px solid #ff8ad8;border-radius:2px 12px 2px 12px;padding:10px;display:flex;flex-direction:column;gap:4px}
#kDance .dkCard b{font:900 15.5px system-ui,sans-serif}#kDance .dkCard p{margin:0;font-size:13.5px}
#kDance .dkL{display:flex;flex-wrap:wrap;gap:8px;font-size:12.5px}#kDance a{color:#8ff4ff;font-weight:800}
#kDance .dkNote{font-size:12.5px;opacity:.85}
#kDance .dkMoves{display:flex;flex-wrap:wrap;gap:8px}#kDance .dkMoves span{background:#2a1450;border:2px solid #ff8ad8;border-radius:10px;padding:8px 12px;font:900 16px system-ui,sans-serif}`; document.head.appendChild(css);
 function box(){ let d=$('kDance'); if(d) return d; d=document.createElement('div'); d.id='kDance'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Dance Karaoke'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-dk]'); if(!b) return; e.stopPropagation(); const k=b.dataset.dk;
   if(k==='x') return close(); if(k==='tab'){ tab=b.dataset.v; return paint(); } if(k==='cam') return camera(); if(k==='rec') return startRec(); if(k==='stop') return stopAll(); if(k==='play') return playTogether();
   if(k==='save') return save(false); if(k==='post') return save(true); if(k==='dl') return download(); if(k==='chal') return challenge(); });
  d.addEventListener('change',e=>{ const t=e.target; if(t.dataset.dk==='music'){ music=t.value; if(music==='upload') pickSong(); } if(t.dataset.dk==='file'&&t.files[0]){ setTake(t.files[0],'Your video'); t.value=''; } });
  return d; }
 const N='© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com';
 function paint(){ const d=box(); const tabs='<div class="dkTabs">'+[['now','💃 Dance now'],['styles','🌍 Dance community'],['chal','💥 Cannon challenge']].map(([k,l])=>'<button type="button" data-dk="tab" data-v="'+k+'" class="'+(tab===k?'on':'')+'" data-noul>'+l+'</button>').join('')+'</div>'; let body='';
  if(tab==='now') body='<div class="dkRow"><label>🎵 Music <select data-dk="music" aria-label="Music"><option value="beat"'+(music==='beat'?' selected':'')+'>Your beat (the beat machine)</option><option value="dj"'+(music==='dj'?' selected':'')+'>The DJ deck</option><option value="upload"'+(music==='upload'?' selected':'')+'>A song you upload…</option><option value="count"'+(music==='count'?' selected':'')+'>Just the count (no music)</option><option value="none"'+(music==='none'?' selected':'')+'>Silence</option></select></label>'+(song?'<span class="dkNote">🎵 '+esc(song.name)+'</span>':'')+'</div>'+
   '<div class="dkRow"><button type="button" data-dk="cam" data-noul>🎥 Camera</button><button type="button" data-dk="rec" data-noul style="background:#a3122d!important">● Record a dance</button><button type="button" data-dk="stop" data-noul>■ Stop</button><button type="button" data-dk="play" data-noul style="background:#137a3f!important">▶ Play together</button>'+
   '<label class="dkBtn" style="display:inline-flex"><input type="file" accept="video/*" capture="user" data-dk="file" hidden><span style="min-height:44px;display:inline-flex;align-items:center;padding:0 14px;border-radius:4px 12px 4px 12px;background:#2b1d6e;border:1.5px solid #cfc4ff;font:800 14px system-ui,sans-serif;cursor:pointer">📱 Phone camera / ⬆ Upload</span></label></div>'+
   '<div class="dkStage"><div class="dkScreen" data-dk-s="live"><video playsinline muted autoplay></video><span class="dkTag">🎥 You</span><div class="dkCount"></div></div><div class="dkScreen" data-dk-s="take"><video playsinline controls></video><span class="dkTag">💃 Your dance</span></div></div>'+
   '<div class="dkRow"><button type="button" data-dk="save" data-noul>📁 Save to library</button><button type="button" data-dk="post" data-noul>📣 Post to your page</button><button type="button" data-dk="dl" data-noul>⬇ Download</button></div>'+
   '<p class="dkNote">The frame flashes on every beat. Inside claude.ai a page may not use the camera, so 📱 opens your phone’s camera app (or picks a video you made) and ▶ Play together lines it up with the music from the same count-in. On the platform’s own website 🎥 records you live, with the music inside the video.</p>';
  else if(tab==='styles') body='<h3 style="margin:4px 0">Dance styles</h3><div class="dkGrid">'+STY.map(s=>'<div class="dkCard"><b>'+esc(s[0])+'</b><p>'+esc(s[1])+'</p><p class="dkNote">Tempo about '+s[2]+' BPM · moves: '+esc(s[3].join(', '))+'</p><span class="dkL"><a href="'+YT(s[0]+' dance')+'" target="_blank" rel="noopener">YouTube ↗</a><a href="'+TT(s[0]+' dance')+'" target="_blank" rel="noopener">TikTok ↗</a><a href="'+IG(s[0]+'dance')+'" target="_blank" rel="noopener">Instagram ↗</a><a href="'+RD(s[0]+' dance')+'" target="_blank" rel="noopener">Reddit ↗</a><a href="'+WK(s[0]+(s[0]==='Tap'?' dance':''))+'" target="_blank" rel="noopener">About ↗</a></span></div>').join('')+'</div>'+
   '<h3 style="margin:10px 0 4px">Where dancers share</h3><div class="dkGrid">'+PLAT.map(p=>'<div class="dkCard"><b>'+esc(p[0])+'</b><p>'+esc(p[1])+'</p><a href="'+p[2]+'" target="_blank" rel="noopener">Open ↗</a></div>').join('')+'</div>'+
   '<h3 style="margin:10px 0 4px">Learn and talk dance</h3><div class="dkGrid">'+LEARN.concat(FORUM).map(p=>'<div class="dkCard"><b>'+esc(p[0])+'</b><p>'+esc(p[1])+'</p><a href="'+p[2]+'" target="_blank" rel="noopener">Open ↗</a></div>').join('')+'</div>';
  else body='<p>The cannon picks a style, a tempo and four moves. Dance them in order, two eight-counts each, then record and post your take.</p><div class="dkRow"><button type="button" data-dk="chal" data-noul style="background:#ffe94a!important;color:#1a0420!important">💥 Fire the cannon</button></div><div data-dk-c="out"></div>';
  d.innerHTML='<div class="dkIn"><div class="dkTop"><h2>💃 Dance Karaoke</h2><button type="button" data-dk="x" data-noul>✕ Close</button></div>'+tabs+body+'<p class="dkNote">Outside sites open in a new tab and have their own terms; the platform is not affiliated with them. Film only yourself, or people who agreed. '+N+'</p></div>';
  if(tab==='now'){ if(stream){ const v=d.querySelector('[data-dk-s="live"] video'); v.srcObject=stream; } if(take){ const v=d.querySelector('[data-dk-s="take"] video'); v.src=take.url; } } }
 function pickSong(){ const i=document.createElement('input'); i.type='file'; i.accept='audio/*,video/*'; i.onchange=()=>{ const f=i.files[0]; if(f){ song={name:f.name,url:URL.createObjectURL(f)}; paint(); } }; i.click(); }
 async function camera(){ try{ stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'user'},audio:false}); paint(); say('🎥 The camera is on.'); return true; }catch(_){ say('This page may not use the camera here. Use 📱 Phone camera / ⬆ Upload, then ▶ Play together.'); return false; } }
 /* the music, the count-in and the beat flash */
 const bpm=()=>{ try{ return PS().bpm(); }catch(_){ return 100; } };
 function flashOn(){ clearInterval(beatT); const ms=60000/bpm(); beatT=setInterval(()=>{ document.querySelectorAll('#kDance .dkScreen').forEach(s=>{ s.classList.add('flash'); setTimeout(()=>s.classList.remove('flash'),90); }); },ms); }
 function countIn(){ return new Promise(res=>{ const el=document.querySelector('#kDance [data-dk-s="live"] .dkCount')||document.querySelector('#kDance .dkCount'); const ms=60000/bpm(); let n=3; const step=()=>{ if(el) el.textContent=n>0?String(n):''; try{ if(n>0) PS().hitPad(n===1?2:4); }catch(_){ } if(n===0) return res(); n--; setTimeout(step,ms); }; step(); }); }
 function musicStart(){ try{ if(music==='beat'){ const P=PS(); if(P&&!P.playing) P.play(); } else if(music==='dj'){ DJBOOTH.start('A'); } else if(music==='upload'&&song){ songEl=new Audio(song.url); songEl.play().catch(()=>{}); } else if(music==='count'){ const P=PS(); /* a click on every beat */ clearInterval(musicStart.t); musicStart.t=setInterval(()=>{ try{ P.hitPad(4); }catch(_){ } },60000/bpm()); } }catch(_){ } flashOn(); }
 function musicStop(){ try{ const P=PS(); if(P&&P.playing) P.stop(); }catch(_){ } try{ DJBOOTH.pause('A'); }catch(_){ } if(songEl){ try{ songEl.pause(); }catch(_){ } songEl=null; } clearInterval(musicStart.t); clearInterval(beatT); }
 /* recording: the camera, with the app's own sound mixed in where it can be */
 async function startRec(){ if(!stream&&!(await camera())) return; await countIn(); musicStart();
  let tracks=[...stream.getVideoTracks()]; try{ const P=PS(); const c=P.ac(); const dest=c.createMediaStreamDestination(); P.out().connect(dest); startRec.dest=dest; tracks=tracks.concat(dest.stream.getAudioTracks()); }catch(_){ }
  chunks=[]; try{ rec=new MediaRecorder(new MediaStream(tracks)); }catch(_){ say('Recording is not available in this browser.'); return; } rec.ondataavailable=e=>{ if(e.data&&e.data.size) chunks.push(e.data); }; rec.onstop=()=>{ setTake(new Blob(chunks,{type:rec.mimeType||'video/webm'}),'Your dance'); try{ PS().out().disconnect(startRec.dest); }catch(_){ } };
  rec.start(500); say('● Recording your dance. ■ Stop when you are done.'); }
 function stopAll(){ if(rec&&rec.state!=='inactive') rec.stop(); musicStop(); const v=document.querySelector('#kDance [data-dk-s="take"] video'); if(v) v.pause(); }
 function setTake(blob,name){ if(take&&take.url) URL.revokeObjectURL(take.url); take={blob,name,url:URL.createObjectURL(blob),type:blob.type||'video/webm',at:Date.now()}; paint(); say('💃 '+name+' is ready: ▶ Play together, 📁 save, 📣 post or ⬇ download.'); }
 async function playTogether(){ if(!take) return say('Record a dance or pick a video first (📱 Phone camera / ⬆ Upload).'); const v=document.querySelector('#kDance [data-dk-s="take"] video'); v.currentTime=0; v.muted=music!=='none'&&music!=='count'?true:false; await countIn(); musicStart(); v.play().catch(()=>{}); v.onended=()=>musicStop(); }
 async function save(andPost){ if(!take) return say('There is no dance to save yet.'); try{ await KLIB.save({kind:'video',name:'Dance · '+new Date(take.at).toLocaleString(),blob:take.blob,meta:{music,bpm:bpm(),from:'Dance Karaoke'}}); }catch(_){ return say('Your library is not available here.'); }
  if(andPost){ try{ KACCT.open(); }catch(_){ } say('📁 Your dance is in your library. On your page, open 📁 Library or Apps and press 📣 Post on it.'); } else say('📁 Saved to your library.'); }
 async function download(){ if(!take) return say('There is no dance to download yet.'); const ext=/mp4/.test(take.type)?'mp4':'webm'; try{ const ok=await KLIB.download(take.blob,'my-dance.'+ext); if(ok===false) say('Saving files is not allowed here.'); }catch(_){ say('Saving files is not allowed here.'); } }
 function challenge(){ const s=STY[Math.floor(Math.random()*STY.length)]; const [lo,hi]=s[2].split('–').map(Number); const t=Math.round(lo+Math.random()*(Math.min(hi,lo+30)-lo)); const moves=s[3].slice().sort(()=>Math.random()-.5);
  try{ const b=$('padBpm'); if(b){ b.value=String(Math.max(40,Math.min(240,t))); b.dispatchEvent(new Event('change',{bubbles:true})); } }catch(_){ }
  const o=document.querySelector('#kDance [data-dk-c="out"]'); if(o) o.innerHTML='<div class="dkCard"><b>💥 '+esc(s[0])+' at '+t+' BPM</b><p>'+esc(s[1])+'</p><div class="dkMoves">'+moves.map((m,i)=>'<span>'+(i+1)+'. '+esc(m)+'</span>').join('')+'</div><p class="dkNote">Two eight-counts on each move. The beat machine is set to '+t+' BPM: open 💃 Dance now, press ● and go.</p><span class="dkL"><a href="'+YT(s[0]+' '+moves[0]+' tutorial')+'" target="_blank" rel="noopener">Learn “'+esc(moves[0])+'” on YouTube ↗</a></span></div>'; say('💥 '+s[0]+' at '+t+' BPM.'); }
 function open(t){ const d=box(); if(t) tab=t; try{ (window.KBEAT&&KBEAT.closeAll)&&KBEAT.closeAll(); }catch(_){ } d.hidden=false; paint(); d.scrollTop=0; }
 function close(){ stopAll(); if(stream){ stream.getTracks().forEach(t=>t.stop()); stream=null; } const d=$('kDance'); if(d) d.hidden=true; }
 /* a door from the karaoke screen and the Games screen */
 setInterval(()=>{ const k=$('kKara'); if(k&&!k.hidden&&!k.querySelector('[data-dko]')){ const b=document.createElement('button'); b.type='button'; b.dataset.dko='1'; b.setAttribute('data-noul',''); b.textContent='💃 Dance Karaoke: dance to the beat and share it'; b.style.cssText='display:block;margin:8px 0;min-height:52px;padding:0 18px;border-radius:4px 16px 4px 16px;background:#ff8ad8;color:#1a0420;font:900 16px system-ui,sans-serif'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); open('now'); },true); k.insertBefore(b,k.firstElementChild?k.firstElementChild.nextSibling:null); } },1200);
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Play','💃','Dance Karaoke: record yourself dancing to the beat, styles, challenges, where to share','Dance Karaoke',()=>open('now')); }); }catch(_){ }
 try{ const h=()=>{ if(window.KCANNON&&KCANNON.SHOT&&!KCANNON.SHOT.kDance){ KCANNON.SHOT.kDance=()=>{ tab='chal'; paint(); challenge(); return true; }; KCANNON.NAME.kDance='Dance Karaoke'; } }; h(); setTimeout(h,3000); }catch(_){ }
 window.KDANCE={open,close,challenge,STY,get take(){ return take; }};
})();
