(()=>{ /* THE OWNER'S WORD: "My dear Watson, I don't give a damn." The owner's position in plain words: where the line comes from,
   what it means here, its philosophy and its theology, and the creed. Its own page; on the top of the Menu for everyone to see. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const LINE='My dear Watson, I don’t give a damn.';
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const SEC=[
  ['📜 Where the line comes from',[
   'It is two of the most famous lines ever written, put together on purpose.',
   '“My dear Watson” is Sherlock Holmes. In Arthur Conan Doyle’s stories Holmes calls his friend “my dear Watson” and says “Elementary”, but never the two together; “Elementary, my dear Watson” came later, best known from the 1929 film The Return of Sherlock Holmes.',
   '“My dear, I don’t give a damn” is Rhett Butler walking out the door in Margaret Mitchell’s Gone with the Wind (1936). The 1939 film added “Frankly,” and the American Film Institute ranked it the number one movie line of all time.',
   'Put together: the detective’s cold, clear mind and Rhett’s walk-out-the-door freedom. That is the owner’s position.']],
  ['👑 What it means here',[
   'It is a plain statement of proven truth. When the logic is sound, the math adds up and the science is proven, the matter is closed. Opinions, doubt and outside noise do not change a proven fact. They never did.',
   'That is Holmes’s voice. He does not argue and he does not ask for a vote. He lays out the proof and lets it stand.',
   'Natural law and hard facts are a force of their own. They speak for themselves. Nobody votes on gravity.',
   'So I don’t give a damn about the noise. I give everything to the proof, the work and the people it serves. Not caring what the crowd thinks is not the same as not caring: I care about what is real.']],
  ['🧠 The philosophy',[
   'Holmes’s method: “It is a capital mistake to theorise before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.” (A Scandal in Bohemia). Facts first; opinions bend to them, never the other way round.',
   'And: “When you have eliminated the impossible, whatever remains, however improbable, must be the truth.” (The Sign of Four). Once the proof is done, the answer stands, whether anyone likes it or not.',
   'Holmes on feelings: “whatever is emotional is opposed to that true cold reason which I place above all things.” (The Sign of Four). Clear eyes, no drama, the proof first.',
   'The Stoics: Epictetus opens his handbook with “Some things are in our control and others not.” What people think is not in your control; the truth of your work is. The Stoics called a good name an “indifferent”: nice to have, never the thing you live for.',
   'Marcus Aurelius, the emperor who wrote to himself: every man loves himself more than all the rest of men, yet he values their opinion of him more than his own (Meditations, book 12). The owner fixes that mistake.']],
  ['✝ The theology',[
   'The truth was settled before anyone had an opinion about it. Natural law is the order built into creation: it holds whether people believe it or not.',
   '“For the invisible things of him from the creation of the world are clearly seen, being understood by the things that are made.” (Romans 1:20)',
   '“And ye shall know the truth, and the truth shall make you free.” (John 8:32)',
   '“For ever, O LORD, thy word is settled in heaven.” (Psalm 119:89)',
   '“Damn” is a word of judgment: to damn is to condemn. Judgment is not the crowd’s to hand out. So “I don’t give a damn” also means: I don’t take my sentence from the crowd, and I don’t pass one on anybody.',
   '“The fear of man bringeth a snare: but whoso putteth his trust in the LORD shall be safe.” (Proverbs 29:25)',
   '“For do I now persuade men, or God? or do I seek to please men? for if I yet pleased men, I should not be the servant of Christ.” (Galatians 1:10)']],
  ['🔥 The owner’s creed',[
   'Proven is proven. The proof speaks; I don’t have to.',
   'I built it. I own it. I answer for it.',
   'I don’t wait for permission and I don’t beg for applause.',
   'The work speaks. The critics are welcome to listen.',
   'I care about the truth, the people who use what I make, and the work. Everything else is weather.',
   LINE]]];
 const text=()=>LINE+'\n\n'+SEC.map(([h,ps])=>h.replace(/^\S+\s/,'')+'\n'+ps.join('\n')).join('\n\n')+'\n\n— The owner, DD Universe Multi-Media Studios’ KAN-IN™ · The Omni-Compass LLC';
 const css=document.createElement('style'); css.textContent=`
#kOwner{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(14px + env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-left,0px)) 48px 16px;background:radial-gradient(circle at 50% -10%,#3a2a08,#0b0712 62%);color:#f3ecdc;font:16px/1.6 Georgia,'Times New Roman',serif}
#kOwner[hidden]{display:none!important}
#kOwner .koIn{max-width:760px;margin:0 auto}
#kOwner .koBrand{font:700 12px ui-monospace,monospace;letter-spacing:.12em;color:#d9b45a;text-transform:uppercase}
#kOwner h2{font:italic 900 clamp(28px,6vw,46px)/1.12 Georgia,'Times New Roman',serif;color:#ffd76a;margin:12px 0 6px;text-wrap:balance}
#kOwner .koSub{font:600 14px system-ui,sans-serif;color:#cdbf9e;margin-bottom:12px}
#kOwner h3{font:800 19px/1.25 system-ui,sans-serif;color:#fff;margin:26px 0 8px;padding-top:12px;border-top:1px solid rgba(255,215,106,.25)}
#kOwner p{margin:0 0 10px}
#kOwner .koCreed p{font:italic 700 19px/1.45 Georgia,serif;color:#ffe9a8;margin:0 0 6px}
#kOwner .koCreed p:last-child{font-size:24px;color:#ffd76a;margin-top:12px}
#kOwner .koRow{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#kOwner .koRow button{min-height:44px;border-radius:12px;padding:0 14px;font:700 14px system-ui,sans-serif}
#kOwner .koFoot{margin-top:30px;font:12px/1.5 system-ui,sans-serif;color:#a99c80}
#tourTab #ttOwner{grid-column:1/-1;order:3;min-height:52px;font:italic 800 16px/1.25 Georgia,serif!important;color:#ffd76a!important;background:linear-gradient(90deg,#3a2a08,#160f22)!important;border:1px solid #d9b45a!important;border-radius:12px}`; document.head.appendChild(css);
 function box(){ let d=$('kOwner'); if(!d){ d=document.createElement('div'); d.id='kOwner'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','The owner’s word');
   d.innerHTML='<div class="kBar" data-sc="kOwner"><button type="button" data-ka="close" data-ko="close">✕</button></div><div class="koIn"><div class="koBrand">The Omni-Compass LLC · DD Universe Multi-Media Studios’ KAN-IN™ · The owner’s word</div><h2>“'+esc(LINE)+'”</h2><div class="koSub">Proven truth needs nobody’s permission. The owner’s position, in plain words: where the line comes from, what it means here, its philosophy and its theology.</div>'+
    '<div class="koRow"><button type="button" data-ko="say" data-noul>🔊 Read it out</button><button type="button" data-ko="stop" data-noul>⏹ Stop</button><button type="button" data-ko="copy" data-noul>📋 Copy it</button><button type="button" data-ko="prompt" data-noul>🎤 Put it on the prompter</button><button type="button" data-ko="close" data-noul>✕ Close</button></div>'+
    SEC.map(([h,ps],i)=>'<h3>'+esc(h)+'</h3><div class="'+(i===SEC.length-1?'koCreed':'')+'">'+ps.map(p=>'<p>'+esc(p)+'</p>').join('')+'</div>').join('')+
    '<div class="koFoot">Quotations: Arthur Conan Doyle, A Scandal in Bohemia (1891) and The Sign of Four (1890); Margaret Mitchell, Gone with the Wind (1936); Epictetus, Enchiridion 1; Marcus Aurelius, Meditations 12.4; the Bible, King James Version. © 2026 The Omni-Compass LLC. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com</div></div>';
   document.body.appendChild(d);
   d.addEventListener('click',e=>{ const b=e.target.closest('[data-ko]'); if(!b) return; e.stopPropagation(); const k=b.dataset.ko;
    if(k==='close') return close();
    if(k==='stop'){ try{ speechSynthesis.cancel(); }catch(_){ } return; }
    if(k==='say'){ try{ speechSynthesis.cancel(); const parts=text().split(/\n+/).filter(Boolean); parts.forEach(p=>{ const u=new SpeechSynthesisUtterance(p.replace(/[“”]/g,'')); u.rate=0.95; speechSynthesis.speak(u); }); say('🔊 Reading the owner’s word.'); }catch(_){ say('Reading out loud is not available on this device.'); } return; }
    if(k==='copy'){ const t=text(); const done=()=>say('📋 Copied.'); try{ navigator.clipboard.writeText(t).then(done,()=>sel()); }catch(_){ sel(); } return; }
    if(k==='prompt'){ close(); try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ const s=$('tpSrc'), t=$('tpText'); if(s){ s.value='own'; s.dispatchEvent(new Event('change',{bubbles:true})); } if(t){ t.value=SEC[SEC.length-1][1].join('\n'); t.dispatchEvent(new Event('input',{bubbles:true})); } say('🎤 The creed is on the prompter.'); },1200); return; } });
  } return d; }
 function sel(){ const r=document.createRange(); const n=document.querySelector('#kOwner .koCreed'); if(!n) return; r.selectNodeContents(n); const s=getSelection(); s.removeAllRanges(); s.addRange(r); say('Selected: press copy on your keyboard or phone.'); }
 function open(){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kVG'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ } d.hidden=false; d.scrollTop=0; }
 function close(){ const d=$('kOwner'); if(d) d.hidden=true; try{ speechSynthesis.cancel(); }catch(_){ } }
 try{ const gh=window.GOHOME; if(gh&&!gh.__kown){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kown=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')) close(); },true);
 /* on top of the Menu, for everyone */
 function menu(){ const t=$('tourTab'); if(!t||$('ttOwner')) return; const b=document.createElement('button'); b.type='button'; b.id='ttOwner'; b.textContent='👑 “'+LINE+'” · the owner’s word'; b.style.order='3'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); t.appendChild(b); }
 setInterval(()=>{ menu(); const b=$('ttOwner'); if(b&&b.style.order!=='3') b.style.order='3'; },1000); menu();
 window.KOWNER={open,close,line:LINE,text};
})();
