(()=>{ /* 🆕 ALWAYS THE NEWEST VERSION (v257). The link never changes: every update is published to the same link, so anyone who opens it
   gets the newest version. A copy that is already open checks the published build stamp every two minutes and whenever it comes back
   on screen; when a newer build is out it saves the work in progress and loads the new version by itself, without asking. It waits only
   while something would be lost by reloading (a recording, a beat or a song playing, a video, words being typed), and loads the moment
   that stops. The same works when the app is hosted on its own website. */
 const B=String(window.KANIN_BUILD||''); if(!B) return; const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const KEY='kanin-auto-upd'; let pending=null, told=false;
 function busy(){ try{ const P=window.PADSTUDIO; if(P&&P.playing) return 'the beat is playing'; }catch(_){ }
  const rec=document.querySelector('#padRecLive.rec,#kbRec.rec,.rec[data-ku-rec],[data-recording="1"]'); if(rec) return 'a recording is running';
  try{ if(window.KKARA&&KKARA.recording) return 'a karaoke take is recording'; }catch(_){ }
  if([...document.querySelectorAll('audio,video')].some(m=>!m.paused&&!m.ended&&m.currentTime>0)) return 'something is playing';
  const a=document.activeElement; if(a&&(/^(TEXTAREA)$/.test(a.tagName)||a.isContentEditable||(a.tagName==='INPUT'&&/^(text|search|email|url)$/i.test(a.type)&&a.value))) return 'you are typing';
  return ''; }
 function saveAll(){ try{ STORYLIB.autosave(); }catch(_){ } try{ FILES.kinds.forEach(k=>{ try{ if(FILES.cur(k)) FILES.save(k); }catch(_){ } }); }catch(_){ } }
 function load(nv){ let tried=null; try{ tried=JSON.parse(sessionStorage.getItem(KEY)||'null'); }catch(_){ } if(tried&&tried.to===nv&&Date.now()-tried.at<180000) return; /* tried just now: the host will serve it on the next open */
  saveAll(); try{ sessionStorage.setItem(KEY,JSON.stringify({to:nv,at:Date.now()})); sessionStorage.setItem('kanin-keep-book','1'); }catch(_){ }
  const o=$('kUpd'); if(o) o.remove(); say('🆕 Loading the newest version… your work is saved.'); setTimeout(()=>{ try{ location.reload(); }catch(_){ } },1200); }
 async function check(){ try{ const r=await fetch('version.json?a='+Date.now(),{cache:'no-store'}); if(!r.ok) return; const j=await r.json(); const nv=j&&j.v?String(j.v):''; if(!(nv&&nv>B)) return; pending=nv; tryLoad(); }catch(_){ } }
 const WHEN={'the beat is playing':'the beat stops','a recording is running':'the recording stops','a karaoke take is recording':'the take ends','something is playing':'playback stops','you are typing':'you finish typing'};
 function tryLoad(){ if(!pending) return; const why=busy(); if(why){ const o=$('kUpd'); if(o) o.remove(); if(!told){ told=true; say('🆕 A new version is ready. It loads by itself as soon as '+(WHEN[why]||'this stops')+'.'); } return; } load(pending); }
 setTimeout(check,15000); setInterval(check,2*60*1000); setInterval(tryLoad,15000);
 document.addEventListener('visibilitychange',()=>{ if(document.visibilityState==='visible') check(); });
 window.KAUTOUPD={check,busy,get pending(){ return pending; }};
})();
