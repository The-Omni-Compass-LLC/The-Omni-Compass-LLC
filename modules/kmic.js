(()=>{ /* 🎤 TALK INSTEAD OF TYPING (v212): every place you can type has a microphone. Tap into any text box and a 🎤 appears at its
   right edge; tap it and talk, and your words go into the box as you speak. The AI chat keeps its 🎤 beside Send all the time; while
   you talk a big ⬆ Send arrow shows: one push stops listening, waits for your last words and sends, like the Claude app (Send does
   the same). ⚡ Send when I stop sends by itself the moment you stop. The platform holds the microphone and turns
   speech into text with the same service claude.ai's own dictation uses (Chrome, Edge and the Claude desktop app); the page only
   receives the words. Where that is not offered (Safari, the phone apps) the 🎤 opens the box and points to your keyboard's own
   microphone key. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 let D=null, ready=false, target=null, live=false, partial='', autoSend=getLS('kanin-ai-voicesend',false), sending=false, denied=false;
 (async()=>{ try{ if(window.claude&&claude.use) D=await claude.use('dictation'); }catch(_){ D=null; } ready=true;
  if(D){ D.onPartial(({text})=>{ partial=text||''; bubble(); }); D.onFinal(({text})=>insert(text)); D.onState(({state,reason})=>{ live=state!=='idle'; paint(); if(state==='idle'){ partial=''; bubble(); ended(reason); } }); } })();
 const OK=e=>e&&e.isConnected&&!e.disabled&&!e.readOnly&&(e.tagName==='TEXTAREA'||(e.tagName==='INPUT'&&/^(text|search|email|url|tel|)$/.test((e.getAttribute('type')||'').toLowerCase()))||e.isContentEditable)&&!e.closest('#gateWrap,[data-nomic]')&&e.getBoundingClientRect().width>=80;
 const css=document.createElement('style'); css.textContent=`
#kMic{position:fixed;z-index:9790;display:flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;border:2px solid #fff;background:#6b2fd0;color:#fff;font:900 18px system-ui,sans-serif;box-shadow:0 4px 14px rgba(0,0,0,.5);padding:0!important;min-height:0!important}
#kMic[hidden]{display:none!important} #kMic.live{background:#e01e37;animation:kMicP 1.1s ease-in-out infinite}
@keyframes kMicP{50%{box-shadow:0 0 0 8px rgba(224,30,55,.35)}}
@media (prefers-reduced-motion:reduce){ #kMic.live{animation:none} }
#kMicTxt{position:fixed;z-index:9790;max-width:min(520px,calc(100vw - var(--kRailW,58px) - 24px));padding:6px 10px;border-radius:10px;background:rgba(12,10,36,.95);border:1px solid #b48cff;color:#e8e2ff;font:600 italic 14px/1.4 system-ui,sans-serif;pointer-events:none}
#kMicTxt[hidden]{display:none!important}
.kAiMic{min-width:48px;min-height:44px;border-radius:12px!important;font:900 18px system-ui,sans-serif!important}
.kAiMic.live{background:#e01e37!important;color:#fff!important;animation:kMicP 1.1s ease-in-out infinite}
.kAiSendV{min-width:56px;min-height:44px;border-radius:999px!important;background:#ffe94a!important;color:#14163a!important;font:900 20px system-ui,sans-serif!important;box-shadow:0 0 0 3px rgba(255,233,74,.35)}
.kAiSendV[hidden]{display:none!important}
.kAiAuto{min-height:44px;border-radius:12px!important;font:700 12.5px system-ui,sans-serif!important}
.kAiAuto.on{background:#ffe94a!important;color:#14163a!important}
@media (min-width:1700px){ #kMic{width:52px;height:52px;font-size:24px} #kMicTxt{font-size:18px} }`; document.head.appendChild(css);
 function btn(){ let b=$('kMic'); if(b) return b; b=document.createElement('button'); b.type='button'; b.id='kMic'; b.hidden=true; b.setAttribute('data-noul',''); b.textContent='🎤'; document.body.appendChild(b);
  b.addEventListener('pointerdown',e=>e.preventDefault()); /* keep the box focused */
  b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); toggle(target||document.activeElement); }); return b; }
 function place(){ const b=btn(); const f=(live&&target)?target:document.activeElement; if(!OK(f)||document.body.classList.contains('gated')){ if(!live) b.hidden=true; return; } if(f.closest('#kAI')&&!live){ b.hidden=true; return; }
  const r=f.getBoundingClientRect(); if(r.bottom<0||r.top>innerHeight){ b.hidden=!live; return; } const s=b.offsetWidth||40; b.style.left=Math.max(4,Math.min(innerWidth-s-4,r.right-s-4))+'px'; b.style.top=Math.max(4,Math.min(innerHeight-s-4,r.top+Math.min(r.height,48)/2-s/2))+'px'; b.hidden=false; if(!live) target=f; }
 function bubble(){ let t=$('kMicTxt'); if(!t){ t=document.createElement('div'); t.id='kMicTxt'; t.setAttribute('aria-live','polite'); document.body.appendChild(t); } if(!live||!partial||!target){ t.hidden=true; return; } const r=target.getBoundingClientRect(); t.textContent='🎤 '+partial; t.style.left=Math.max(8,r.left)+'px'; t.style.top=Math.min(innerHeight-40,r.bottom+6)+'px'; t.hidden=false; }
 function insert(text){ const f=target; if(!f||!f.isConnected||!text) return; if(f.isContentEditable){ f.focus(); try{ document.execCommand('insertText',false,text); }catch(_){ f.textContent+=text; } return; }
  let v=text; const empty=!f.value; if(empty) v=v.replace(/^\s+/,''); const a=f.selectionStart!=null?f.selectionStart:f.value.length, z=f.selectionEnd!=null?f.selectionEnd:f.value.length;
  if(!empty&&a>0&&!/\s$/.test(f.value.slice(0,a))&&!/^\s/.test(v)) v=' '+v; try{ f.setRangeText(v,a,z,'end'); }catch(_){ f.value+=v; } f.dispatchEvent(new Event('input',{bubbles:true})); }
 function ended(reason){ if(reason==='not_granted'){ denied=true; say('🎤 The microphone is off for this page. Turn it on in the page\'s Permissions menu, or type.'); }
  else if(reason==='unavailable'){ say('🎤 Talking is not available here. Type instead, or use your keyboard\'s own 🎤 key.'); }
  else if(reason==='rate_limited') say('🎤 Too many at once. Try again in a moment.'); else if(reason==='upstream_error') say('🎤 The microphone did not answer. Try again.');
  const f=target; if(f&&f.id==='aiIn'&&(sending||(autoSend&&(reason==='stopped'||reason==='viewer_stopped')))&&f.value.trim()){ sending=false; sendAI(); } sending=false; }
 function sendAI(){ const s=document.querySelector('#kAI [data-ai="send"]'); if(s){ s.__kmicPass=true; setTimeout(()=>{ s.click(); s.__kmicPass=false; },80); } }
 /* ⬆ while talking: stop, wait for the last words, then send */
 function stopAndSend(){ if(D&&(live||D.active())&&target&&target.id==='aiIn'){ sending=true; D.stop().catch(()=>{ sending=false; sendAI(); }); } else sendAI(); }
 document.addEventListener('click',e=>{ const s=e.target.closest&&e.target.closest('#kAI [data-ai="send"]'); if(!s||s.__kmicPass) return; if(live&&target&&target.id==='aiIn'){ e.preventDefault(); e.stopImmediatePropagation(); stopAndSend(); } },true);
 /* tap 🎤: start listening right away (nothing waits before it) or stop */
 function toggle(f){ if(!OK(f)) f=target; if(!OK(f)) return; target=f;
  if(!D){ f.focus(); say(ready?'🎤 Tap the microphone key on your keyboard and talk. (Talking straight into KAN-IN works in Chrome, Edge and the Claude desktop app.)':'🎤 The microphone is getting ready. Tap again in a second.'); return; }
  if(live||D.active()){ D.stop().catch(()=>{}); return; }
  if(denied){ say('🎤 The microphone is off for this page. Turn it on in the page\'s Permissions menu, or type.'); return; }
  try{ f.focus({preventScroll:true}); }catch(_){ } D.start().catch(err=>{ const c=err&&err.code; if(c==='not_granted'){ denied=true; ended('not_granted'); } else if(c==='dismissed') say('🎤 Tap the microphone again when you are ready to talk.'); else if(c==='unavailable') ended('unavailable'); else if(c&&c!=='stopped') ended(c); }); }
 function paint(){ const b=btn(); b.classList.toggle('live',live); b.title=live?'Listening… tap to stop':'Tap and talk instead of typing'; b.setAttribute('aria-label',b.title); b.setAttribute('aria-pressed',String(live));
  const onAi=live&&target&&target.id==='aiIn'; document.querySelectorAll('.kAiSendV').forEach(x=>{ x.hidden=!onAi; }); document.querySelectorAll('.kAiMic').forEach(x=>{ x.classList.toggle('live',live&&target&&target.id==='aiIn'); x.textContent=(live&&target&&target.id==='aiIn')?'■':'🎤'; x.title=(live&&target&&target.id==='aiIn')?'Listening… tap to stop without sending':'Talk to the AI instead of typing'; }); place(); bubble(); }
 /* the AI chat: a 🎤 beside Send, always there, and ⚡ Send when I stop */
 function aiMic(){ const s=document.querySelector('#kAI [data-ai="send"]'); if(!s||s.parentNode.querySelector('.kAiMic')) return; const m=document.createElement('button'); m.type='button'; m.className='kAiMic'; m.setAttribute('data-noul',''); m.textContent='🎤'; m.title='Talk to the AI instead of typing'; m.setAttribute('aria-label','Talk to the AI');
  m.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); toggle($('aiIn')); }); s.insertAdjacentElement('beforebegin',m);
  const v=document.createElement('button'); v.type='button'; v.className='kAiSendV'; v.hidden=true; v.setAttribute('data-noul',''); v.textContent='⬆'; v.title='Stop talking and send'; v.setAttribute('aria-label','Stop talking and send');
  v.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); stopAndSend(); }); m.insertAdjacentElement('afterend',v);
  const a=document.createElement('button'); a.type='button'; a.className='kAiAuto'+(autoSend?' on':''); a.setAttribute('data-noul',''); a.textContent='⚡ Send when I stop'; a.title='When on, your spoken message goes to the AI as soon as you stop talking'; a.setAttribute('aria-pressed',String(autoSend));
  a.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); autoSend=!autoSend; putLS('kanin-ai-voicesend',autoSend); a.classList.toggle('on',autoSend); a.setAttribute('aria-pressed',String(autoSend)); say(autoSend?'⚡ Your spoken message goes to the AI when you stop talking.':'You press Send yourself after talking.'); }); s.insertAdjacentElement('afterend',a); }
 document.addEventListener('focusin',()=>setTimeout(place,0),true);
 document.addEventListener('focusout',()=>setTimeout(()=>{ if(!live&&document.activeElement!==$('kMic')) place(); },120),true);
 addEventListener('scroll',()=>{ place(); bubble(); },true); addEventListener('resize',()=>{ place(); bubble(); });
 setInterval(()=>{ aiMic(); place(); },700);
 window.KMIC={toggle:f=>toggle(f||document.activeElement),get available(){ return !!D; },get listening(){ return live; }};
})();
