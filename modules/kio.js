(()=>{ /* 🎚 THE CONSOLE'S INPUTS (v205): every source lined up with its channels, as on a hardware console, and the drum machine's
   timing as on an MPC: record pads in real time, exactly as played, or latched to the step grid or to 1/32 … 1/4; the click can tick on
   the beat, the eighth, the sixteenth, the triplet, the half or the bar. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const REC=[['live','🎵 Real time: exactly as played'],['step','🎯 The step grid (factory)'],['32','Latch 1/32'],['24','Latch 1/16 triplet'],['16','Latch 1/16'],['12','Latch 1/8 triplet'],['8','Latch 1/8'],['4','Latch 1/4']];
 const CLK=[['4','1/4 · every beat (factory)'],['8','1/8'],['16','1/16'],['12','1/8 triplet'],['2','1/2'],['1','1 bar']];
 /* ROUTING: channels 1-16 are the drum pads A1-A16, one pad per channel, locked; every other source has a drop-down that wires it
    into any of channels 17-24 (several sources may share a channel). The engine's own channel for each source is its factory route. */
 const SRC=[['padsBCD',16,'🥁 Pads banks B, C, D (bass, chords, FX, your sounds)'],['keys',17,'🎹 Keyboard and MIDI keys'],['bass',18,'🎸 Bass line'],['chords',19,'🎹 Chords'],['melody',20,'🎵 Melody'],['gtr',21,'🎶 Rhythm guitar'],['loops',22,'🌊 Wave loops and files'],['vox',23,'🎙 Vocals, mic and line in']];
 window.KCHMAP=Object.assign({},getLS('kanin-chmap',{}));
 const routeOf=n=>window.KCHMAP[n]!=null?window.KCHMAP[n]:n;
 function setRoute(native,to){ if(+to===native) delete window.KCHMAP[native]; else window.KCHMAP[native]=+to; putLS('kanin-chmap',window.KCHMAP); labelStrips(); }
 function labelStrips(){ const m=$('padMixer'); if(!m) return; for(let ci=16;ci<24;ci++){ const st=m.querySelector('.mxs[data-c="'+ci+'"]'); if(!st) continue; const sm=st.querySelector('small'); if(!sm) continue; if(sm.dataset.orig==null) sm.dataset.orig=sm.textContent; const feeds=SRC.filter(([,n])=>routeOf(n)===ci).map(([,,l])=>l.replace(/^\S+\s/,'').split(/[ ,(]/)[0]); const txt=feeds.length?feeds.join(' + '):'(open)'; if(sm.textContent!==txt){ sm.textContent=txt; sm.title='Channel '+(ci+1)+': '+txt; } } }
 const chOpts=cur=>Array.from({length:8},(_,k)=>16+k).map(ci=>'<option value="'+ci+'"'+(ci===cur?' selected':'')+'>Channel '+(ci+1)+'</option>').join('');
 window.PADRECMODE=getLS('kanin-recmode','step'); window.PADCLICKDIV=+getLS('kanin-clickdiv',4)||4;
 const opt=(L,v)=>L.map(([k,t])=>'<option value="'+k+'"'+(String(v)===k?' selected':'')+'>'+t+'</option>').join('');
 const css=document.createElement('style'); css.textContent=`
#kIO{border:1px solid rgba(0,229,255,.4);border-radius:12px;padding:8px 10px;margin:8px 0;background:rgba(0,229,255,.05)}
#kIO h4{margin:0 0 6px!important;color:#6fe8ff!important;font-size:14px!important}
#kIO .ioRow{display:grid;grid-template-columns:minmax(150px,1.1fr) 26px minmax(150px,1.4fr) minmax(120px,1fr);gap:6px 8px;align-items:center;padding:6px 0;border-top:1px solid rgba(255,255,255,.08)}
#kIO .ioRow:first-of-type{border-top:0}
#kIO .ioSrc b{display:block;font-size:13.5px}
#kIO .ioSrc span,#kIO .ioSt{font-size:12px;opacity:.8;line-height:1.35}
#kIO .ioArr{text-align:center;color:#ffe94a;font-weight:900}
#kIO select{max-width:100%;min-height:34px}
#kIO .ioBtns{display:flex;flex-wrap:wrap;gap:4px}
#kIO .ioBtns button{min-height:34px!important;padding:2px 8px!important;font-size:12.5px!important}
#kIO .ioCh{display:inline-block;border:1px solid #ffe94a;border-radius:6px;padding:0 6px;font:800 12px ui-monospace,monospace;color:#ffe94a;margin-right:4px}
@media (max-width:700px){ #kIO .ioRow{grid-template-columns:1fr;gap:4px} #kIO .ioArr{display:none} }`; document.head.appendChild(css);
 function mountTiming(){ const rl=$('padRecLive'); if(rl&&!$('padRecMode')){ const l=document.createElement('label'); l.innerHTML='Record timing <select id="padRecMode" aria-label="Record timing">'+opt(REC,window.PADRECMODE)+'</select>'; rl.insertAdjacentElement('afterend',l); }
  const ck=$('padClick'); if(ck&&!$('padClickDiv')){ const l=document.createElement('label'); l.innerHTML='Click every <select id="padClickDiv" aria-label="Click every">'+opt(CLK,window.PADCLICKDIV)+'</select>'; ck.insertAdjacentElement('afterend',l); } }
 const mirror=(id,src)=>{ const s=$(src); if(!s) return '<span class="ioSt">—</span>'; return '<select data-mirror="'+src+'" id="'+id+'">'+[...s.options].map(o=>'<option value="'+o.value+'"'+(o.value===s.value?' selected':'')+'>'+o.textContent+'</option>').join('')+'</select>'; };
 const inFrame=(()=>{ try{ return window.self!==window.top; }catch(_){ return true; } })();
 function paintIO(){ const box=$('kIO'); if(!box) return; const midiInfo=(($('midiInfo')||{}).textContent||'').trim();
  box.innerHTML='<h4>🎚 Inputs · every source lined up with its channels</h4>'+
   '<div class="ioRow"><div class="ioSrc"><b>🥁 Drum pads A1–A16</b><span>Kick, kick 2, snare, clap, hats, rim, toms, crash, ride, shaker, cowbell, snap, 808: one pad per channel, locked</span></div><div class="ioArr">→</div><div><span class="ioCh">1–16</span>one pad on each</div><div class="ioBtns"><button type="button" data-io="pads" data-noul>🥁 Pads</button></div></div>'+
   SRC.map(([k,n,l])=>'<div class="ioRow"><div class="ioSrc"><b>'+l+'</b><span>Factory route: channel '+(n+1)+'</span></div><div class="ioArr">→</div><div><select data-route="'+n+'" aria-label="Channel for '+l+'">'+chOpts(routeOf(n))+'</select></div><div class="ioBtns">'+(routeOf(n)!==n?'<button type="button" data-reset="'+n+'" data-noul>↺ Factory</button>':'')+'</div></div>').join('')+
   '<h4 style="margin-top:10px!important">🎛 Devices and timing</h4>'+
   '<div class="ioRow"><div class="ioSrc"><b>🥁 Drum machine</b><span>64 pads in 4 banks, played by touch, keys, MIDI or the cannon</span></div><div class="ioArr">→</div><div><span class="ioCh">1–16</span>Kick to 808 boom<br><span class="ioSt">Record timing</span> <select id="ioRecMode">'+opt(REC,window.PADRECMODE)+'</select></div><div class="ioBtns"><button type="button" data-io="rec" data-noul>⏺ Record taps</button><button type="button" data-io="tc" data-noul>🎯 Correct timing now</button><button type="button" data-io="pads" data-noul>🥁 Pads</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>🎹 MIDI in</b><span>'+(midiInfo&&!/^Press/.test(midiInfo)?midiInfo.slice(0,90):'Any class-compliant keyboard or pad controller: Akai, Novation, Roland, Yamaha…')+'</span></div><div class="ioArr">→</div><div><span class="ioCh">17</span>Keys or <span class="ioCh">1–16</span>pads<br>'+mirror('ioMidiTo','midiTo')+'</div><div class="ioBtns"><button type="button" data-io="midi" data-noul>🎛 Connect MIDI</button><button type="button" data-io="keys" data-noul>🎹 Keys</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>🎙 Microphone · line in</b><span>'+(inFrame?'Inside claude.ai the page cannot open the microphone: record with the phone’s own recorder in Karaoke. On KAN-IN’s own website it records live.':'Your microphone or audio interface')+'</span></div><div class="ioArr">→</div><div><span class="ioCh">24</span>Vocals<br>'+mirror('ioMicRoute','micRoute')+'</div><div class="ioBtns"><button type="button" data-io="kara" data-noul>🎤 Karaoke booth</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>🎹 Instruments</b><span>Bass, chords, melody, rhythm guitar from the composer</span></div><div class="ioArr">→</div><div><span class="ioCh">17–22</span>Keys, bass, chords, melody, guitar</div><div class="ioBtns"><button type="button" data-io="comp" data-noul>🎼 Composer</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>🌊 Files and loops</b><span>Any sound or video’s audio, chopped or looped</span></div><div class="ioArr">→</div><div><span class="ioCh">23</span>Wave loops</div><div class="ioBtns"><button type="button" data-io="chop" data-noul>✂ Wave chopper</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>💿 DJ decks</b><span>Deck A and deck B</span></div><div class="ioArr">→</div><div><span class="ioCh">25</span>Deck A <span class="ioCh">26</span>Deck B</div><div class="ioBtns"><button type="button" data-io="dj" data-noul>🎧 DJ booth</button></div></div>'+
   '<div class="ioRow"><div class="ioSrc"><b>🕒 Click</b><span>The metronome, on the audio clock with the loop</span></div><div class="ioArr">→</div><div><span class="ioSt">Click every</span> <select id="ioClickDiv">'+opt(CLK,window.PADCLICKDIV)+'</select></div><div class="ioBtns"><button type="button" data-io="click" data-noul>🕒 Click on / off</button></div></div>'; }
 function mountIO(){ if($('kIO')) return; const h=$('kStudioHead'); if(!h||!h.parentNode) return; const d=document.createElement('div'); d.id='kIO'; h.insertAdjacentElement('afterend',d); paintIO();
  d.addEventListener('click',e=>{ const rb=e.target.closest('[data-reset]'); if(rb){ e.stopPropagation(); setRoute(+rb.dataset.reset,+rb.dataset.reset); say('↺ Back on its factory channel.'); return paintIO(); } const b=e.target.closest('[data-io]'); if(!b) return; e.stopPropagation(); const k=b.dataset.io; const press=id=>{ const x=$(id); if(x) x.click(); return !!x; };
   if(k==='rec') return press('padRecLive'); if(k==='tc'){ try{ MPC.tc(true); }catch(_){ say('Pick a timing in the MPC controls first.'); } return; } if(k==='pads'){ try{ KRAIL.FLOAT.toggle('pads'); }catch(_){ } return; }
   if(k==='midi'){ press('midiOn'); setTimeout(paintIO,1500); return; } if(k==='keys'){ try{ KRAIL.FLOAT.toggle('keys'); }catch(_){ } return; } if(k==='kara'){ try{ KKARA.open(); }catch(_){ } return; }
   if(k==='comp'){ const c=$('cmpWrap'); if(c) c.scrollIntoView({block:'start',behavior:'smooth'}); return; } if(k==='chop'){ const c=$('chopSec')||document.querySelector('[id*="chop"]'); if(c) c.scrollIntoView({block:'start',behavior:'smooth'}); return; }
   if(k==='dj'){ try{ KRAIL.FLOAT.toggle('dj'); }catch(_){ } return; } if(k==='click'){ press('padClick'); return; } });
  d.addEventListener('change',e=>{ const t=e.target; if(t.dataset.route!=null){ const n=+t.dataset.route; setRoute(n,+t.value); const L=SRC.find(x=>x[1]===n); say('🎚 '+(L?L[2]:'Source')+' → channel '+(+t.value+1)+'.'); return paintIO(); } if(t.id==='ioRecMode'||t.id==='ioClickDiv') return setTiming(t); const src=t.dataset.mirror; if(src&&$(src)){ $(src).value=t.value; $(src).dispatchEvent(new Event('change',{bubbles:true})); say('🎚 Routed: '+t.selectedOptions[0].textContent+'.'); } }); }
 function setTiming(t){ if(t.id==='padRecMode'||t.id==='ioRecMode'){ window.PADRECMODE=t.value; putLS('kanin-recmode',t.value); ['padRecMode','ioRecMode'].forEach(id=>{ const x=$(id); if(x&&x!==t) x.value=t.value; }); say(t.value==='live'?'🎵 Real time: every pad hit stays exactly where you played it.':t.value==='step'?'🎯 Pad hits latch to the step grid.':'🎯 Pad hits latch to '+t.selectedOptions[0].textContent.replace('Latch ','')+'.'); }
  if(t.id==='padClickDiv'||t.id==='ioClickDiv'){ window.PADCLICKDIV=+t.value; putLS('kanin-clickdiv',+t.value); ['padClickDiv','ioClickDiv'].forEach(id=>{ const x=$(id); if(x&&x!==t) x.value=t.value; }); say('🕒 The click ticks every '+t.selectedOptions[0].textContent.split(' ·')[0]+'.'); } }
 document.addEventListener('change',e=>{ if(e.target&&(e.target.id==='padRecMode'||e.target.id==='padClickDiv')) setTiming(e.target); });
 setInterval(()=>{ mountTiming(); mountIO(); labelStrips(); },1200);
 window.KIO={paint:paintIO,setRoute,routeOf,get recMode(){ return window.PADRECMODE; }};
})();
