(()=>{ /* SPEED, CLICK AND TIME: one drawer in every control panel. Turn the tempo of the beat up or down, switch the click on, speed up or
   slow down every voice, reading and song, raise or lower the tone, set the DJ decks to 33, 45 or 78, and run a stopwatch or a countdown. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 let speed=getLS('kanin-speed',1), tone=getLS('kanin-tone',0);
 /* every voice and every played file follows the speed and tone */
 try{ const S0=speechSynthesis.speak.bind(speechSynthesis); speechSynthesis.speak=function(u){ try{ if(u&&!u.__ks){ u.__ks=1; u.rate=Math.max(0.1,Math.min(10,(u.rate||1)*speed)); u.pitch=Math.max(0,Math.min(2,(u.pitch||1)*Math.pow(2,tone/24))); } }catch(_){ } return S0(u); }; }catch(_){ }
 const fac=()=>speed*(tone===0?1:Math.pow(2,tone/12));
 function tune(m){ try{ if(m.__kBase==null){ if(speed===1&&tone===0) return; m.__kBase=m.playbackRate||1; } m.preservesPitch=tone===0; m.playbackRate=Math.max(0.0625,Math.min(16,m.__kBase*fac())); if(speed===1&&tone===0) m.__kBase=null; }catch(_){ } }
 try{ const P0=HTMLMediaElement.prototype.play; HTMLMediaElement.prototype.play=function(){ tune(this); return P0.apply(this,arguments); }; }catch(_){ }
 function applyMedia(){ document.querySelectorAll('audio,video').forEach(tune); }
 /* the beat's tempo: the Beat Maker's own up and down steps */
 const bpm=()=>{ try{ return Math.round(PADSTUDIO.bpm()); }catch(_){ return 90; } };
 function setBpm(target){ target=Math.max(40,Math.min(240,Math.round(target))); const i=$('padBpm'); if(i){ i.value=String(target); i.dispatchEvent(new Event('input',{bubbles:true})); i.dispatchEvent(new Event('change',{bubbles:true})); const v=$('bbBpmV'); if(v) v.textContent=String(target); if(bpm()===target) return target; } let n=0; const up=$('bbUp'), dn=$('bbDn'); if(!up||!dn) return say('Open the Beat Maker once, then try again.'); while(bpm()<target&&n++<400) up.click(); while(bpm()>target&&n++<800) dn.click(); return bpm(); }
 const clickOn=()=>{ const c=$('padClick'); const t=c?c.textContent:''; return /on/i.test(t)&&!/off/i.test(t); };
 /* the DJ decks: pitch in percent, and record speeds */
 function deckPitch(d,pct){ const s=document.querySelector('#deck'+d+' input[data-k="pitch"]'); if(!s) return false; s.value=String(Math.max(+s.min,Math.min(+s.max,pct))); s.dispatchEvent(new Event('input',{bubbles:true})); s.dispatchEvent(new Event('change',{bubbles:true})); return true; }
 function rpm(r){ const rate=r===45?1.35:r===78?2.34:1; let n=0; try{ ['A','B'].forEach(d=>{ const k=DJBOOTH.D[d]; k.rate=rate; if(k.src&&k.src.playbackRate){ k.src.playbackRate.value=rate*(1+(k.pitch||0)/100); n++; } }); }catch(_){ } say('💿 Decks at '+(r===33?'33⅓':r)+' RPM'+(n?'':' (load and play a track to hear it)')+'.'); }
 /* the timer */
 let swT=0, swOn=false, swStart=0, cdEnd=0, tick=null;
 const fmt=ms=>{ ms=Math.max(0,ms); const m=Math.floor(ms/60000), s=Math.floor(ms/1000)%60, t=Math.floor(ms/100)%10; return String(m).padStart(2,'0')+':'+String(s).padStart(2,'0')+'.'+t; };
 function beep(f,d){ try{ const c=new (window.AudioContext||window.webkitAudioContext)(); const o=c.createOscillator(), g=c.createGain(); o.frequency.value=f; g.gain.value=0.3; o.connect(g); g.connect(c.destination); o.start(); o.stop(c.currentTime+d); setTimeout(()=>c.close(),d*1000+200); }catch(_){ } }
 function loop(){ if(tick) return; tick=setInterval(()=>{ const sw=$('ksSw'), cd=$('ksCd'); if(sw) sw.textContent=fmt(swT+(swOn?Date.now()-swStart:0)); if(cdEnd){ const left=cdEnd-Date.now(); if(cd) cd.textContent=fmt(left); if(left<=0){ cdEnd=0; beep(880,0.25); setTimeout(()=>beep(660,0.35),300); say('⏱ Time is up!'); } } if(!swOn&&!cdEnd){ clearInterval(tick); tick=null; } },100); }
 /* the drawer */
 const css=document.createElement('style'); css.textContent=`#kPanel .ksBox{display:grid;gap:8px;padding:0 10px 10px}#kPanel .ksRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}#kPanel .ksRow button{min-height:40px;min-width:44px;border-radius:10px;padding:0 10px;font:700 14px system-ui,sans-serif}#kPanel .ksRow input[type=range]{flex:1 1 140px;min-width:120px}#kPanel .ksL{font:800 11.5px ui-monospace,monospace;letter-spacing:.08em;color:#7ff;text-transform:uppercase;width:100%}#kPanel .ksV{font:800 17px system-ui,sans-serif;color:#ffe94a;min-width:70px;text-align:center}#kPanel .ksN{font-size:12.5px;opacity:.85}`; document.head.appendChild(css);
 const html=()=>'<details class="ksD" open><summary>⏱ Speed, click and timer</summary><div class="ksBox">'+
  '<div class="ksRow"><span class="ksL">🥁 Beat tempo (beats per minute)</span><button type="button" data-ks="b-10">−10</button><button type="button" data-ks="b-1">−1</button><span class="ksV" id="ksBpm">'+bpm()+' BPM</span><button type="button" data-ks="b+1">+1</button><button type="button" data-ks="b+10">+10</button><button type="button" data-ks="tap">👆 Tap</button><input type="range" id="ksBpmR" min="40" max="240" step="1" value="'+bpm()+'" aria-label="Beat tempo"></div>'+
  '<div class="ksRow"><span class="ksL">🕒 Click (metronome)</span><button type="button" data-ks="click">🕒 Click: '+(clickOn()?'ON':'off')+'</button><span class="ksN">The click counts the beat out loud.</span></div>'+
  '<div class="ksRow"><span class="ksL">⏩ Speed of voices, reading and songs</span><input type="range" id="ksSpd" min="0.5" max="2" step="0.05" value="'+speed+'" aria-label="Speed"><span class="ksV" id="ksSpdV">'+speed.toFixed(2)+'×</span>'+[0.5,0.75,1,1.25,1.5,2].map(v=>'<button type="button" data-ks="s'+v+'">'+v+'×</button>').join('')+'</div>'+
  '<div class="ksRow"><span class="ksL">🎚 Tone (higher or lower)</span><input type="range" id="ksTone" min="-12" max="12" step="1" value="'+tone+'" aria-label="Tone"><span class="ksV" id="ksToneV">'+(tone>0?'+':'')+tone+'</span><button type="button" data-ks="t0">Normal</button><span class="ksN">Moves voices, songs and the keyboard up or down in half steps.</span></div>'+
  '<div class="ksRow"><span class="ksL">💿 DJ decks</span><button type="button" data-ks="r33">33⅓ RPM</button><button type="button" data-ks="r45">45 RPM</button><button type="button" data-ks="r78">78 RPM</button><button type="button" data-ks="p-">Pitch −2%</button><button type="button" data-ks="p0">Pitch 0</button><button type="button" data-ks="p+">Pitch +2%</button></div>'+
  '<div class="ksRow"><span class="ksL">⏱ Stopwatch</span><span class="ksV" id="ksSw">'+fmt(swT+(swOn?Date.now()-swStart:0))+'</span><button type="button" data-ks="sw">'+(swOn?'⏸ Pause':'▶ Start')+'</button><button type="button" data-ks="swr">↺ Reset</button></div>'+
  '<div class="ksRow"><span class="ksL">⏳ Countdown</span><span class="ksV" id="ksCd">'+fmt(cdEnd?cdEnd-Date.now():0)+'</span>'+[1,3,5,10,15].map(m=>'<button type="button" data-ks="cd'+m+'">'+m+' min</button>').join('')+'<button type="button" data-ks="cd0">✕</button></div></div></details>';
 function mount(){ const p=$('kPanel'); if(!p||p.hidden||p.querySelector('.ksD')) return; const anchor=p.querySelector('.kpTrN')||p.querySelector('.kLvlRow')||p.querySelector('.kpHead'); if(!anchor) return; anchor.insertAdjacentHTML('afterend',html()); loop(); }
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#kPanel [data-ks]'); if(!b) return; e.stopPropagation(); const k=b.dataset.ks;
  if(/^b[+-]\d+$/.test(k)){ const v=setBpm(bpm()+parseInt(k.slice(1),10)); upd(); return v&&say('🥁 '+v+' BPM'); }
  if(k==='tap'){ const t=$('padTap'); if(t){ t.click(); setTimeout(upd,50); } else say('Open the Beat Maker once, then try again.'); return; }
  if(k==='click'){ const c=$('padClick')||$('bbClick'); if(c){ c.click(); setTimeout(()=>{ const on=clickOn(); b.textContent='🕒 Click: '+(on?'ON':'off'); say('🕒 Click '+(on?'on: it counts every beat.':'off.')); },60); } else say('Open the Beat Maker once, then try again.'); return; }
  if(/^s[\d.]+$/.test(k)){ speed=+k.slice(1); putLS('kanin-speed',speed); applyMedia(); upd(); return say('⏩ Speed '+speed+'×'); }
  if(k==='t0'){ tone=0; putLS('kanin-tone',tone); applyTone(); upd(); return; }
  if(/^r\d+$/.test(k)) return rpm(+k.slice(1));
  if(k==='p-'||k==='p+'||k==='p0'){ ['A','B'].forEach(d=>{ const s=document.querySelector('#deck'+d+' input[data-k="pitch"]'); const v=s?+s.value:0; deckPitch(d,k==='p0'?0:v+(k==='p+'?2:-2)); }); return say('💿 Deck pitch '+(k==='p0'?'0':k==='p+'?'+2%':'−2%')); }
  if(k==='sw'){ if(swOn){ swT+=Date.now()-swStart; swOn=false; } else { swStart=Date.now(); swOn=true; loop(); } b.textContent=swOn?'⏸ Pause':'▶ Start'; return; }
  if(k==='swr'){ swT=0; swStart=Date.now(); upd(); return; }
  if(/^cd\d+$/.test(k)){ const m=+k.slice(2); cdEnd=m?Date.now()+m*60000:0; loop(); upd(); return m&&say('⏳ Countdown: '+m+' minute'+(m>1?'s':'')+'.'); } },true);
 document.addEventListener('input',e=>{ const t=e.target; if(!t||!t.closest||!t.closest('#kPanel')) return;
  if(t.id==='ksSpd'){ speed=+t.value; putLS('kanin-speed',speed); applyMedia(); upd(); }
  if(t.id==='ksTone'){ tone=+t.value; putLS('kanin-tone',tone); applyTone(); upd(); } },true);
 document.addEventListener('change',e=>{ const t=e.target; if(t&&t.id==='ksBpmR'){ const v=setBpm(+t.value); upd(); if(v) say('🥁 '+v+' BPM'); } },true);
 function applyTone(){ applyMedia(); const tr=$('kbTr'); if(tr){ const v=String(tone); if(tr.tagName==='SELECT'){ const o=[...tr.options].find(o=>o.value===v||parseInt(o.value,10)===tone); if(o) tr.value=o.value; } else tr.value=v; tr.dispatchEvent(new Event('input',{bubbles:true})); tr.dispatchEvent(new Event('change',{bubbles:true})); } }
 function upd(){ const b=$('ksBpm'); if(b) b.textContent=bpm()+' BPM'; const r=$('ksBpmR'); if(r) r.value=bpm(); const s=$('ksSpdV'); if(s) s.textContent=speed.toFixed(2)+'×'; const t=$('ksToneV'); if(t) t.textContent=(tone>0?'+':'')+tone; const cd=$('ksCd'); if(cd) cd.textContent=fmt(cdEnd?cdEnd-Date.now():0); const sw=$('ksSw'); if(sw) sw.textContent=fmt(swT+(swOn?Date.now()-swStart:0)); }
 try{ new MutationObserver(()=>mount()).observe(document.body,{childList:true,subtree:false}); }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdPanel')) setTimeout(mount,60); },true);
 setInterval(()=>{ const p=$('kPanel'); if(p&&!p.hidden&&!p.querySelector('.ksD')) mount(); },700);
 window.KSPEED={setBpm,bpm,rpm,speed:()=>speed,tone:()=>tone,set:(s,t)=>{ if(s!=null){ speed=s; putLS('kanin-speed',s); } if(t!=null){ tone=t; putLS('kanin-tone',t); applyTone(); } applyMedia(); }};
})();
