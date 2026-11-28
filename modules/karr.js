(()=>{ /* 🎼 THE SONG ARRANGER (v261). A whole song, section by section, as long as it needs to be. Each section is a scene of the
   studio (A to H: a loop with its drums, bass, chords, melody and keys), a name (Intro, Verse, Chorus…), how many times it plays and
   its lyrics. ▶ Play song plays the sections in order on the studio's own clock: at the end of a section's last pass the next scene is
   loaded just before its first beat is scheduled, so the song moves on without a gap and without the 32-bar limit of a single loop.
   ⚡ Make 5 scenes builds an intro, verse, pre-chorus, chorus and breakdown from the loop you have; the templates lay out common song
   forms; ⬇ Export renders every section in turn and joins them into one WAV; 💾 keeps the arrangement in the library. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const P=()=>window.PADSTUDIO, S=()=>window.KSCN;
 const TYPES=[['Intro','#5b8cff'],['Verse','#2fbf71'],['Pre-chorus','#18a3a3'],['Chorus','#ff8a3d'],['Hook','#ff5ea8'],['Bridge','#a66bff'],['Drop','#ff3b3b'],['Breakdown','#7f8cff'],['Solo','#e0b400'],['Interlude','#8fa3b8'],['Outro','#5b6b8c']];
 const COL=n=>(TYPES.find(t=>t[0]===n)||TYPES[0])[1];
 const SHORT={Intro:'In',Verse:'V','Pre-chorus':'Pre',Chorus:'Ch',Hook:'Hk',Bridge:'Br',Drop:'Dr',Breakdown:'Bd',Solo:'So',Interlude:'It',Outro:'Out'};
 const SLOTS='ABCDEFGH'.split('');
 /* song forms: [section, scene, passes]. The ⚡ scenes: A intro, B verse, C pre-chorus, D chorus, E breakdown */
 const TPL={
  'Pop':[['Intro','A',1],['Verse','B',2],['Pre-chorus','C',1],['Chorus','D',2],['Verse','B',2],['Pre-chorus','C',1],['Chorus','D',2],['Bridge','E',1],['Chorus','D',2],['Outro','A',1]],
  'Hip-hop':[['Intro','A',1],['Hook','D',2],['Verse','B',4],['Hook','D',2],['Verse','B',4],['Hook','D',2],['Outro','A',1]],
  'Trap':[['Intro','A',2],['Hook','D',2],['Verse','B',4],['Hook','D',2],['Breakdown','E',1],['Verse','B',2],['Hook','D',2],['Outro','A',1]],
  'R&B':[['Intro','A',1],['Verse','B',2],['Pre-chorus','C',1],['Chorus','D',2],['Verse','B',2],['Chorus','D',2],['Bridge','E',1],['Chorus','D',2],['Outro','A',2]],
  'EDM / house':[['Intro','A',2],['Breakdown','E',1],['Pre-chorus','C',1],['Drop','D',2],['Breakdown','E',1],['Pre-chorus','C',1],['Drop','D',2],['Outro','A',2]],
  'Rock':[['Intro','A',1],['Verse','B',2],['Chorus','D',2],['Verse','B',2],['Chorus','D',2],['Solo','C',2],['Chorus','D',2],['Outro','A',1]],
  'Ballad':[['Intro','A',1],['Verse','B',2],['Chorus','D',1],['Verse','B',2],['Chorus','D',1],['Bridge','E',1],['Chorus','D',2],['Outro','A',1]],
  'Country':[['Intro','A',1],['Verse','B',2],['Chorus','D',2],['Verse','B',2],['Chorus','D',2],['Bridge','E',1],['Chorus','D',2],['Outro','A',1]],
  'Reggaeton':[['Intro','A',1],['Hook','D',2],['Verse','B',2],['Pre-chorus','C',1],['Hook','D',2],['Verse','B',2],['Hook','D',2],['Outro','A',1]],
  'Short (about a minute)':[['Intro','A',1],['Verse','B',1],['Chorus','D',1],['Outro','A',1]]};
 let A={name:'My song',sections:[]}, sel=0;
 const LS='kanin-arr1'; const keep=()=>{ try{ localStorage.setItem(LS,JSON.stringify(A)); }catch(_){ } };
 try{ const v=JSON.parse(localStorage.getItem(LS)||'null'); if(v&&Array.isArray(v.sections)) A=v; }catch(_){ }
 const sec=(n,s,r,ly)=>({n:n||'Verse',s:s||'A',r:Math.max(1,Math.min(16,+r||1)),ly:ly||''});
 const scene=k=>{ try{ return S()&&S().all()[k]; }catch(_){ return null; } };
 const barsOf=x=>{ const sc=scene(x.s); return (sc?sc.bars:0)*x.r; };
 const secs=()=>{ try{ return 60/P().bpm()*4; }catch(_){ return 2.67; } }; /* seconds in one 4-beat bar */
 const tm=t=>{ t=Math.round(t); return Math.floor(t/60)+':'+String(t%60).padStart(2,'0'); };
 /* ---------- ⚡ five scenes from the loop you have ---------- */
 function quick(){ const ps=P(), sx=S(); if(!ps||!sx) return say('Open the 🎛 Studio first.'); const T=ps.total; const base=ps.pads.map(p=>p.steps.slice(0,T)); if(!base.some(a=>a.some(Boolean))) return say('Make a beat in the 🎛 Studio first (or press ✨ Auto-create there), then ⚡ Make 5 scenes.');
  const spb=ps.spb, bars=ps.bars; const put=(slot,fn)=>{ ps.pads.forEach((p,i)=>{ const a=new Array(512).fill(0); for(let s=0;s<T;s++) a[s]=base[i][s]; p.steps=a; }); fn&&fn(ps.pads,T,spb,bars); sx.save(slot); };
  put('B',null); /* the verse: the loop as it is */
  put('A',(pd,T)=>{ pd.forEach((p,i)=>{ if(![4,5,11,12].includes(i)) for(let s=0;s<T;s++) p.steps[s]=0; }); for(let s=0;s<T;s+=spb/2) pd[4].steps[s]=pd[4].steps[s]||1; });  /* intro: hats, ride and shaker over the chords */
  put('C',(pd,T)=>{ const L=T-spb; for(let s=L+spb/2;s<T;s++) pd[2].steps[s]=1; [7,8,9].forEach((i,k)=>{ pd[i].steps[L+spb/2+k*2]=1; }); });  /* pre-chorus: a snare roll and a tom fill into the chorus */
  put('D',(pd,T)=>{ pd[10].steps[0]=1; for(let s=0;s<T;s++){ if(s%(spb/4)===spb/8) pd[5].steps[s]=1; if(pd[2].steps[s]) pd[3].steps[s]=1; } });  /* chorus: crash on the one, open hats on the off-beats, claps on the snares */
  put('E',(pd,T)=>{ pd.forEach((p,i)=>{ if(i!==0&&i!==15&&i!==11) for(let s=0;s<T;s++) p.steps[s]=0; }); for(let s=0;s<T;s++) pd[0].steps[s]=(s%spb===0)?1:0; });  /* breakdown: the kick on each bar's one, the chords breathe */
  sx.load('B',false); render(); say('⚡ Five scenes from your loop: A intro, B verse, C pre-chorus, D chorus, E breakdown. Pick a song form or build your own.'); }
 /* ---------- playing the song on the studio's clock ---------- */
 const R={on:false,i:0,pass:0,t0:0,hooked:false,bar:0};
 function hook(){ const ps=P(); if(R.hooked||!ps||!ps.STEPHOOKS) return; R.hooked=true;
  ps.STEPHOOKS.push((c,dest,t,s,sd)=>{ if(!R.on||c!==ps.ac()) return; const T=ps.total, spb=ps.spb;
   if(s%spb===0){ const b=Math.floor(s/spb); const d=Math.max(0,(t-c.currentTime)*1000); setTimeout(()=>{ R.bar=b; live(); },d); }
   if(s===T-1){ R.pass++; const cur=A.sections[R.i]; if(cur&&R.pass>=cur.r){ const at=t+sd; let n=R.i+1; while(n<A.sections.length&&!scene(A.sections[n].s)) n++;
     if(n>=A.sections.length){ R.on=false; const lastS=cur.s; const sc=scene(lastS);
      /* the song ends on this step: a silent loop goes in now, so the step the clock has already looked ahead to plays nothing; the last scene comes back once it has stopped */
      try{ S().put('__end',{bars:sc.bars,spb:sc.spb,steps:ps.pads.map(()=>[]),CT:{bass:[],chords:[],melody:[],gtr:[]},KT:[],chart:sc.chart}); S().load('__end',true); }catch(_){ }
      setTimeout(()=>{ try{ ps.stop(); }catch(_){ } try{ S().load(lastS,true); S().del('__end'); }catch(_){ } render(); say('🎼 The song is done. ▶ Play it again, or ⬇ Export it as one WAV.'); },Math.max(0,(at-c.currentTime)*1000)+60); return; }
     /* swap now, on the loop's last step, inside the studio's clock: the very next step it schedules is the new scene's one */
     R.i=n; R.pass=0; window.__padWrap=true; S().load(A.sections[n].s,true); window.__padWrap=false; setTimeout(()=>{ R.bar=0; live(); },Math.max(0,(at-c.currentTime)*1000)); } } }); }
 function play(from){ const ps=P(), sx=S(); if(!ps||!sx) return say('Open the 🎛 Studio first.'); if(!A.sections.length) return say('Add sections first: pick a song form, or ➕ Add a section.');
  let i=Math.max(0,from||0); while(i<A.sections.length&&!scene(A.sections[i].s)) i++; if(i>=A.sections.length) return say('These sections use empty scenes. Press ⚡ Make 5 scenes, or save loops as scenes in the 🎛 Studio (Scenes and song).');
  hook(); if(ps.playing) ps.stop(); sx.load(A.sections[i].s,true); R.on=true; R.i=i; R.pass=0; R.bar=0; R.t0=Date.now(); try{ window.KAUDIO&&KAUDIO.gesture&&KAUDIO.gesture(); }catch(_){ } ps.play(); render(); live(); }
 function stop(){ R.on=false; try{ if(P().playing) P().stop(); }catch(_){ } render(); }
 /* ---------- one WAV of the whole song ---------- */
 async function exportWav(){ const ps=P(), sx=S(); if(!ps||!sx) return say('Open the 🎛 Studio first.'); const L=A.sections.filter(x=>scene(x.s)); if(!L.length) return say('Nothing to export yet: the sections need scenes.'); if(!ps.renderBeat||!ps.toWav) return say('This studio cannot render here.');
  stop(); say('⬇ Rendering '+L.length+' sections… this takes a few seconds.'); const parts=[];
  try{ for(const x of L){ sx.load(x.s,true); const b=await ps.renderBeat(x.r); const keepS=Math.round(scene(x.s).bars*ps.spb*x.r*ps.stepDur()*b.sampleRate); parts.push({b,n:Math.min(b.length,keepS)}); }
   const last=parts[parts.length-1]; last.n=last.b.length; const sr=parts[0].b.sampleRate, ch=2, tot=parts.reduce((a,p)=>a+p.n,0); const oc=new OfflineAudioContext(ch,tot,sr); const out=oc.createBuffer(ch,tot,sr); let o=0;
   for(const p of parts){ for(let c=0;c<ch;c++){ const src=p.b.getChannelData(Math.min(c,p.b.numberOfChannels-1)).subarray(0,p.n); out.getChannelData(c).set(src,o); } o+=p.n; }
   const name=(A.name||'My song')+' (arranged)'; let saved=false; try{ if(window.KLIB&&KLIB.saveAudio){ await KLIB.saveAudio(out,name,{from:'Song Arranger',sections:L.length}); saved=true; } }catch(_){ }
   try{ const blob=new Blob([ps.toWav(out)],{type:'audio/wav'}); if(window.KLIB&&KLIB.download) KLIB.download(blob,name+'.wav'); }catch(_){ }
   sx.load(L[0].s,false); say('⬇ '+name+': '+tm(tot/sr)+(saved?', saved in 📚 My library':'')+'.'); }catch(e){ say('The song could not be rendered here.'); } }
 /* ---------- the library ---------- */
 async function saveLib(){ try{ if(!window.KLIB) throw 0; const scenes={}; A.sections.forEach(x=>{ const sc=scene(x.s); if(sc) scenes[x.s]=sc; }); const blob=new Blob([JSON.stringify({arr:A,scenes})],{type:'application/json'}); await KLIB.save({kind:'arrangement',name:A.name||'My song',blob,meta:{from:'Song Arranger',sections:A.sections.length}}); say('💾 '+(A.name||'My song')+' is in 📚 My library, with its scenes.'); }catch(_){ say('It could not be saved here.'); } }
 async function openLib(){ const box=$('kArr').querySelector('.arLib'); try{ const L=(await KLIB.list()).filter(x=>x.kind==='arrangement'); box.innerHTML=L.length?L.map(x=>'<button type="button" data-ar="libopen" data-id="'+esc(x.id)+'" data-noul>📂 '+esc(x.name)+'</button>').join(''):'<span class="arNote">No saved songs yet: 💾 Save keeps this one.</span>'; box.hidden=false; }catch(_){ box.innerHTML='<span class="arNote">The library is not open here.</span>'; box.hidden=false; } }
 async function libOpen(id){ try{ const x=await KLIB.get(id); const o=JSON.parse(await x.blob.text()); if(o.scenes) Object.entries(o.scenes).forEach(([k,v])=>S().put(k,v)); A=o.arr; sel=0; keep(); render(); say('📂 '+A.name+' is open: '+A.sections.length+' sections.'); }catch(_){ say('That song could not be opened.'); } }
 /* ---------- the screen ---------- */
 const css=document.createElement('style'); css.textContent=`
#kArr{position:fixed;inset:0;right:var(--kRailW,58px);z-index:9500;background:linear-gradient(180deg,#0b0a22,#140d33);color:#eef;overflow-y:auto;font:15px/1.5 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 90px}
#kArr[hidden]{display:none!important}
#kArr .arIn{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
#kArr h2{margin:0;font:900 24px system-ui,sans-serif;color:#ffe94a}
#kArr .arTop{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;padding-right:120px}
#kArr .arRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
#kArr button,#kArr select,#kArr input{min-height:42px;border-radius:4px 12px 4px 12px;border:1.5px solid #8f86ff;background:#231d5c;color:#fff;font:800 14px system-ui,sans-serif;padding:0 12px}
#kArr button.go{background:linear-gradient(180deg,#2fd27a,#139a52);border-color:#9effc6}
#kArr button.on{background:linear-gradient(180deg,#ffd84a,#e0a10c);color:#1a1200;border-color:#ffe94a}
#kArr .arName{flex:1;min-width:160px}
#kArr .arTime{display:flex;gap:2px;height:46px;border-radius:8px;overflow:hidden;border:1px solid #3a3380;background:#0a0920}
#kArr .arTime div{display:flex;align-items:center;justify-content:center;font:800 11px system-ui;color:#0b0820;cursor:pointer;min-width:6px;white-space:nowrap;overflow:hidden;position:relative}
#kArr .arTime div.sel{outline:3px solid #fff;outline-offset:-3px}
#kArr .arTime div.now::after{content:'';position:absolute;left:0;top:0;bottom:0;width:var(--p,0%);background:rgba(255,255,255,.35)}
#kArr .arTime div.empty{background:repeating-linear-gradient(45deg,#333,#333 4px,#222 4px,#222 8px)!important;color:#bbb}
#kArr .arLive{display:flex;flex-direction:column;gap:2px;padding:10px 12px;border-radius:6px 16px 6px 16px;background:#1d1640;border:1px solid #ff8ad8}
#kArr .arLive b{font:900 18px system-ui;color:#ffe94a}
#kArr .arLive .ly{font:800 22px/1.35 system-ui,sans-serif;white-space:pre-wrap;color:#fff}
#kArr .arList{display:flex;flex-direction:column;gap:6px}
#kArr .arSec{display:grid;grid-template-columns:10px minmax(0,1fr);gap:8px;padding:8px;border-radius:8px;background:#17123a;border:1px solid #2e2770}
#kArr .arSec.sel{border-color:#ffe94a}
#kArr .arSec .tag{border-radius:4px}
#kArr .arSec textarea{width:100%;min-height:54px;border-radius:8px;border:1px solid #3a3380;background:#0c0a26;color:#fff;font:15px/1.45 system-ui;padding:6px 8px;box-sizing:border-box}
#kArr .arNote{opacity:.8;font-size:13px}
#kArr .arLib{display:flex;flex-wrap:wrap;gap:6px}
#kArr .arTime .ls{display:none}
#kArr .arSec select{max-width:100%}
@media (max-width:700px){ #kArr{padding-top:calc(64px + env(safe-area-inset-top,0px))} #kArr .arTop{padding-right:0} #kArr .arTime .lf{display:none} #kArr .arTime .ls{display:inline} #kArr .arTime div{font-size:10px} }`; document.head.appendChild(css);
 function box(){ let d=$('kArr'); if(d) return d; d=document.createElement('div'); d.id='kArr'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Song Arranger'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-ar]'); if(!b) return; const k=b.dataset.ar, i=+b.dataset.i;
   if(k==='x') return close(); if(k==='play') return R.on?stop():play(sel); if(k==='fromtop') return play(0); if(k==='quick') return quick(); if(k==='export') return exportWav(); if(k==='save') return saveLib(); if(k==='open') return openLib(); if(k==='libopen') return libOpen(b.dataset.id);
   if(k==='add'){ const last=A.sections[A.sections.length-1]; A.sections.push(sec(last?'Chorus':'Intro',last?'D':'A',2)); sel=A.sections.length-1; keep(); return render(); }
   if(k==='sel'||k==='blk'){ sel=i; render(); if(R.on&&k==='blk') play(i); return; }
   if(k==='up'&&i>0){ [A.sections[i-1],A.sections[i]]=[A.sections[i],A.sections[i-1]]; sel=i-1; keep(); return render(); }
   if(k==='down'&&i<A.sections.length-1){ [A.sections[i+1],A.sections[i]]=[A.sections[i],A.sections[i+1]]; sel=i+1; keep(); return render(); }
   if(k==='dup'){ A.sections.splice(i+1,0,JSON.parse(JSON.stringify(A.sections[i]))); sel=i+1; keep(); return render(); }
   if(k==='del'){ A.sections.splice(i,1); sel=Math.max(0,Math.min(sel,A.sections.length-1)); keep(); return render(); }
   if(k==='savescene'){ const x=A.sections[i]; if(!S()) return say('Open the 🎛 Studio first.'); S().save(x.s); render(); return say('💾 The loop in the studio is now scene '+x.s+' ('+x.n+').'); }
   if(k==='hear'){ const x=A.sections[i]; if(!scene(x.s)) return say('Scene '+x.s+' is empty: 💾 put the studio loop in it first.'); stop(); S().load(x.s,false); try{ P().play(); }catch(_){ } return say('▶ Scene '+x.s+' ('+x.n+') is looping in the studio. ■ Stop when done.'); } });
  d.addEventListener('change',e=>{ const t=e.target, k=t.dataset.ar, i=+t.dataset.i; if(k==='tpl'){ const f=TPL[t.value]; if(!f) return; A.sections=f.map(x=>sec(x[0],x[1],x[2])); sel=0; keep(); render(); const miss=[...new Set(A.sections.map(x=>x.s))].filter(s=>!scene(s)); return say('🎼 '+t.value+': '+A.sections.length+' sections.'+(miss.length?' Scenes '+miss.join(' ')+' are empty: press ⚡ Make 5 scenes.':'')); }
   if(k==='n'){ A.sections[i].n=t.value; } if(k==='s'){ A.sections[i].s=t.value; } if(k==='r'){ A.sections[i].r=+t.value; } if(k==='name'){ A.name=t.value.trim()||'My song'; } keep(); render(); });
  d.addEventListener('input',e=>{ const t=e.target; if(t.dataset.ar==='ly'){ A.sections[+t.dataset.i].ly=t.value; keep(); if(R.on&&+t.dataset.i===R.i) live(); } });
  return d; }
 function live(){ const d=$('kArr'); if(!d||d.hidden) return; const L=d.querySelector('.arLive'); if(!L) return; const tot=A.sections.reduce((a,x)=>a+barsOf(x),0), bs=secs();
  if(!R.on){ L.innerHTML='<b>'+(A.sections.length?A.sections.length+' sections · '+tot+' bars · '+tm(tot*bs):'No sections yet')+'</b><span class="arNote">▶ Play song plays every section in order on the studio’s clock, with no 32-bar limit. Tap a block to choose it; while the song plays, tap a block to jump there.</span>'; return; }
  const x=A.sections[R.i]; if(!x) return; const sc=scene(x.s), b=(sc?sc.bars:1); let done=0; for(let k=0;k<R.i;k++) done+=barsOf(A.sections[k]); done+=R.pass*b+R.bar;
  L.innerHTML='<b>▶ '+esc(x.n)+' · pass '+(R.pass+1)+' of '+x.r+' · bar '+(R.bar+1)+' of '+b+'</b><span class="arNote">'+tm(done*bs)+' / '+tm(tot*bs)+' · section '+(R.i+1)+' of '+A.sections.length+' · scene '+x.s+'</span>'+(x.ly?'<div class="ly">'+esc(x.ly)+'</div>':'');
  d.querySelectorAll('.arTime div').forEach((el,k)=>{ el.classList.toggle('now',k===R.i); if(k===R.i) el.style.setProperty('--p',Math.round(((R.pass*b+R.bar)/(b*x.r))*100)+'%'); }); }
 function render(){ const d=box(); const tot=A.sections.reduce((a,x)=>a+barsOf(x),0)||1;
  const opts=(arr,v)=>arr.map(o=>'<option'+(String(o)===String(v)?' selected':'')+'>'+esc(o)+'</option>').join('');
  d.innerHTML='<div class="arIn"><div class="arTop"><h2>🎼 Song Arranger</h2><button type="button" data-ar="x" data-noul>✕ Close</button></div>'+
   '<div class="arRow"><input class="arName" data-ar="name" value="'+esc(A.name)+'" aria-label="Song name" maxlength="80"><button type="button" class="go'+(R.on?' on':'')+'" data-ar="play" data-noul>'+(R.on?'■ Stop':'▶ Play song')+'</button><button type="button" data-ar="fromtop" data-noul>⏮ From the top</button></div>'+
   '<div class="arRow"><label>Song form <select data-die="off" data-ar="tpl" aria-label="Song form"><option value="">Pick a form…</option>'+Object.keys(TPL).map(k=>'<option>'+esc(k)+'</option>').join('')+'</select></label><button type="button" data-ar="quick" data-noul>⚡ Make 5 scenes from my loop</button><button type="button" data-ar="add" data-noul>➕ Add a section</button></div>'+
   '<div class="arTime">'+A.sections.map((x,i)=>{ const sc=scene(x.s); const w=sc?barsOf(x):1; return '<div data-ar="blk" data-i="'+i+'" class="'+(i===sel?'sel ':'')+(sc?'':'empty')+'" style="flex:'+w+';background:'+COL(x.n)+'" title="'+esc(x.n)+' · scene '+x.s+(sc?' · '+barsOf(x)+' bars':' · empty')+'"><span class="lf">'+esc(x.n)+'</span><span class="ls">'+esc(SHORT[x.n]||x.n.slice(0,3))+'</span></div>'; }).join('')+'</div>'+
   '<div class="arLive"></div>'+
   '<div class="arRow"><button type="button" data-ar="export" data-noul>⬇ Export the song as one WAV</button><button type="button" data-ar="save" data-noul>💾 Save to my library</button><button type="button" data-ar="open" data-noul>📂 Open a saved song</button></div><div class="arLib" hidden></div>'+
   '<div class="arList">'+A.sections.map((x,i)=>{ const sc=scene(x.s); return '<div class="arSec'+(i===sel?' sel':'')+'"><div class="tag" style="background:'+COL(x.n)+'"></div><div><div class="arRow"><b>'+(i+1)+'.</b>'+
    '<select data-die="off" data-ar="n" data-i="'+i+'" aria-label="Section">'+opts(TYPES.map(t=>t[0]),x.n)+'</select>'+
    '<select data-die="off" data-ar="s" data-i="'+i+'" aria-label="Scene">'+SLOTS.map(k=>'<option value="'+k+'"'+(k===x.s?' selected':'')+'>Scene '+k+(scene(k)?' · '+scene(k).bars+' bar'+(scene(k).bars>1?'s':''):' · empty')+'</option>').join('')+'</select>'+
    '<select data-die="off" data-ar="r" data-i="'+i+'" aria-label="Plays">'+[1,2,3,4,6,8,12,16].map(n=>'<option value="'+n+'"'+(n===x.r?' selected':'')+'>×'+n+'</option>').join('')+'</select>'+
    '<span class="arNote">'+(sc?barsOf(x)+' bars · '+tm(barsOf(x)*secs()):'scene '+x.s+' is empty')+'</span>'+
    '<button type="button" data-ar="hear" data-i="'+i+'" title="Loop this scene in the studio" data-noul>🔊</button><button type="button" data-ar="savescene" data-i="'+i+'" title="Put the studio’s loop in this scene" data-noul>💾 Loop → '+x.s+'</button>'+
    '<button type="button" data-ar="up" data-i="'+i+'" aria-label="Move up" data-noul>▲</button><button type="button" data-ar="down" data-i="'+i+'" aria-label="Move down" data-noul>▼</button><button type="button" data-ar="dup" data-i="'+i+'" aria-label="Copy" data-noul>⧉</button><button type="button" data-ar="del" data-i="'+i+'" aria-label="Remove" data-noul>✕</button></div>'+
    '<textarea data-ar="ly" data-i="'+i+'" placeholder="Lyrics for this '+esc(x.n.toLowerCase())+' (they show here, big, while the song plays)" aria-label="Lyrics">'+esc(x.ly)+'</textarea></div></div>'; }).join('')+'</div>'+
   (A.sections.length?'':'<p class="arNote">Start with ⚡ Make 5 scenes from the loop in the studio, then pick a song form. Or build it yourself: ➕ Add a section, choose its scene and how many times it plays.</p>')+'</div>'; live(); }
 function open(){ const d=box(); render(); d.hidden=false; d.scrollTop=0; }
 function close(){ stop(); const d=$('kArr'); if(d) d.hidden=true; }
 /* the scenes stay on this device: saved compactly (only the steps that sound) whenever one is saved, and put back when the app opens */
 const SLS='kanin-scenes1';
 const pack=sc=>({bars:sc.bars,spb:sc.spb,st:sc.steps.map(a=>{ const o=[]; (a||[]).forEach((v,i)=>{ if(v) o.push(v===1?i:[i,v]); }); return o; }),CT:sc.CT,KT:sc.KT,chart:sc.chart});
 const unpack=o=>({bars:o.bars,spb:o.spb,steps:o.st.map(l=>{ const a=new Array(o.bars*o.spb).fill(0); l.forEach(x=>{ if(Array.isArray(x)) a[x[0]]=x[1]; else a[x]=1; }); return a; }),CT:o.CT,KT:o.KT||[],chart:o.chart||[]});
 const persist=()=>{ try{ const all=S().all(), o={}; Object.keys(all).filter(k=>SLOTS.includes(k)).forEach(k=>o[k]=pack(all[k])); localStorage.setItem(SLS,JSON.stringify(o)); }catch(_){ } };
 (function wire(){ const sx=S(); if(!sx||!sx.save){ return setTimeout(wire,1000); } if(sx.__kept) return; sx.__kept=true;
  try{ const o=JSON.parse(localStorage.getItem(SLS)||'null'); if(o&&!Object.keys(sx.all()).length) Object.entries(o).forEach(([k,v])=>sx.put(k,unpack(v))); }catch(_){ }
  const f1=sx.save, f2=sx.put, f3=sx.del; sx.save=k=>{ const r=f1(k); if(SLOTS.includes(k)) persist(); return r; }; sx.put=(k,v)=>{ f2(k,v); if(SLOTS.includes(k)) persist(); }; sx.del=k=>{ f3(k); if(SLOTS.includes(k)) persist(); }; })();
 /* a button beside 🎼 Build song in the studio, and an entry in Find */
 setInterval(()=>{ const b=$('ktBuild'); if(b&&!$('ktArr')){ const a=document.createElement('button'); a.type='button'; a.id='ktArr'; a.setAttribute('data-noul',''); a.title='Arrange a whole song, section by section'; a.textContent='🎼 Arranger'; a.addEventListener('click',open); b.insertAdjacentElement('afterend',a); } },1500);
 try{ (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Studio','🎼','Song Arranger: intro, verse, chorus, bridge… a whole song','Arranger',()=>open()); }); }catch(_){ }
 window.KARR={open,close,play,stop,quick,exportWav,get song(){ return A; },set song(v){ A=v; keep(); render(); },get state(){ return {on:R.on,i:R.i,pass:R.pass,bar:R.bar}; },TPL:Object.keys(TPL)};
})();
