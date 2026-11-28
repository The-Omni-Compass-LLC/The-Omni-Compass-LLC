(()=>{ /* 🛠 THE v260 SWEEP FIXES: what the whole-app sweep (every screen, every button, dropdown and slider, on a laptop and a phone)
   found, fixed in one place.
   1. Rows of tabs that ran past the screen's right edge on a laptop now wrap onto a second line, so every tab is in view; on a
      phone they still slide sideways, with a fade at the edge that says there is more.
   2. A ■ Stop pressed when nothing is playing now says so, instead of doing nothing silently.
   3. Music's page buttons say when there is nothing to page through.
   1b. The 🛠 Tools tempo − and + buttons are 40 px wide, big enough for a finger on a phone.
   1c. The Easel's tool row and the story's stage tabs and the Recipes tabs slide sideways on a phone with the same fade cue; the 💥 Surprise-me
       lock buttons are 38 px on a phone (they were 25 by 20).
   8. A screen whose own button sat under the floating 🛠 Tools / ✕ moves its content down just enough to clear them.
   9. The chord chart never has an empty bar (doubling a loop with a short progression left gaps that stopped four buttons).
   10. Karaoke's notes also show at the bottom when its status line is scrolled out of sight.
   7. The 💥 CANNON steps aside when it would sit on a pinned control (on a phone it covered the AI's ➤ Send).
   4-6. AI Send with an empty box, the story player before any canvas, and a contents entry whose section is not built yet each
      say what to do, instead of doing nothing. */
 const css=document.createElement('style'); css.id='kfix260css'; css.textContent=`
@media (min-width:700px){
 .ghTabs{flex-wrap:wrap!important;overflow-x:visible!important}
}
#kToolsPop .rmTools .bpm button{min-width:40px!important;min-height:40px!important;font-size:18px!important}
@media (max-width:760px){
 [data-kj="lock"]{min-width:38px!important;min-height:38px!important;font-size:18px!important}
}
@media (max-width:699px){
 .stagenav,#kRec .rcTabs{-webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);padding-right:24px!important}
 #kEasel .eaBar{-webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);padding-right:24px!important}
 .ghTabs{-webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);padding-right:24px!important}
}`; document.head.appendChild(css);
 /* 2. ■ Stop with nothing playing: one short note */
 const say=m=>{ try{ toast(m); }catch(_){ } };
 const playing=()=>{ try{ if(window.PADSTUDIO&&PADSTUDIO.playing) return true; }catch(_){ } try{ if(window.speechSynthesis&&(speechSynthesis.speaking||speechSynthesis.pending)) return true; }catch(_){ } try{ if([...document.querySelectorAll('audio,video')].some(m=>!m.paused&&!m.muted)) return true; }catch(_){ } try{ if(window.MUSIC&&MUSIC.playing) return true; }catch(_){ } return false; };
 /* 3. Music's ◀ Page back / Next page ▶ with no results, or already at the first or last page: a note instead of nothing */
 const pager=(id,edge)=>addEventListener('click',e=>{ if(!(e.target.closest&&e.target.closest('#'+id))) return; const r=document.getElementById('mRes'); const before=r?r.innerHTML:''; if(!r||!r.children.length){ setTimeout(()=>say('🔎 Search first, then turn the pages of the results.'),60); return; } setTimeout(()=>{ const r2=document.getElementById('mRes'); if(r2&&r2.innerHTML===before) say(edge); },600); },true);
 pager('mPgPrev','◀ This is the first page of results.'); pager('mPgNext','That is the last page of results ▶');
 /* 4. AI ➤ Send with nothing typed: say what to do and put the cursor in the box */
 addEventListener('click',e=>{ if(!(e.target.closest&&e.target.closest('#kAI [data-ai="send"]'))) return; const i=document.getElementById('aiIn'); if(i&&!i.value.trim()){ say('🤖 Type or say a question first, then press ➤ Send.'); try{ i.focus(); }catch(_){ } } },true);
 /* 7. The 💥 CANNON steps out of the way. It floats at the bottom centre; on a phone it could sit on top of a control that cannot be
    scrolled out from under it (the AI's ➤ Send, a screen's bottom bar). Every second it looks at what lies under it; if a pinned
    button, box or slider is there, it moves to the first nearby spot that is clear, and returns home when the way is clear again.
    A cannon the person has dragged to a place of their own is never moved. */
 const INT='button,a[href],input,select,textarea,[role=button],summary,label';
 const scroller=el=>{ for(let e=el.parentElement;e&&e!==document.body;e=e.parentElement){ const s=getComputedStyle(e); if(/(auto|scroll)/.test(s.overflowY+s.overflowX)&&(e.scrollHeight>e.clientHeight+4||e.scrollWidth>e.clientWidth+4)) return e; } return null; };
 const pinned=el=>{ const sc=scroller(el); if(!sc) return true; for(let e=el;e&&e!==sc;e=e.parentElement){ const p=getComputedStyle(e).position; if(p==='sticky'||p==='fixed') return true; } return false; };
 const blocked=(c,dx,dy)=>{ const r=c.getBoundingClientRect(); const L=r.left+dx, T=r.top+dy; const rd=document.getElementById('rDock'); const RL=rd&&rd.getClientRects().length?Math.min(innerWidth,rd.getBoundingClientRect().left):innerWidth; if(L<4||T<4||L+r.width>RL-4||T+r.height>innerHeight-2) return 99; const pts=[[.5,.5],[.2,.2],[.8,.2],[.2,.8],[.8,.8]]; let n=0; for(const [fx,fy] of pts){ for(const el of document.elementsFromPoint(L+r.width*fx,T+r.height*fy)){ if(el===c||c.contains(el)) continue; const i=el.closest&&el.closest(INT); if(i&&!c.contains(i)&&i.getClientRects().length&&pinned(i)){ n++; break; } } } return n; };
 let home=true;
 setInterval(()=>{ const c=document.getElementById('kCannonBtn'); if(!c||!c.getClientRects().length||c.style.left||c.style.top) return; let saved=null; try{ saved=localStorage.getItem('kanin-cannon-pos'); }catch(_){ } if(saved&&saved!=='null') return;
  const prev=c.style.translate; c.style.translate=''; if(!blocked(c,0,0)){ if(!home){ home=true; } return; }
  const C=[[0,-78],[0,-156],[-110,0],[110,0],[-110,-78],[110,-78],[0,-234]]; let best=null, bn=99; for(const [dx,dy] of C){ const n=blocked(c,dx,dy); if(n<bn){ bn=n; best=[dx,dy]; } if(!n) break; }
  if(best&&bn<99){ c.style.translate=best[0]+'px '+best[1]+'px'; home=false; } else c.style.translate=prev; },1000);
 /* 8. Nothing hides under the floating 🛠 Tools / ✕ buttons at the top right. When a screen opens with one of its own buttons under
    them (the AI's 🧹 New chat on a phone, Ask's 🔊 Answers aloud, the games hub's All games), that screen's content moves down just
    far enough to clear them. */
 const CL=['kToolsBtn','kXAll','kUndoAll'];
 const hit=(a,b)=>a.left<b.right+4&&a.right>b.left-4&&a.top<b.bottom+4&&a.bottom>b.top-4;
 setInterval(()=>{ const rs=CL.map(id=>document.getElementById(id)).filter(e=>e&&e.getClientRects().length&&getComputedStyle(e).visibility!=='hidden').map(e=>e.getBoundingClientRect()); if(!rs.length) return; const low=Math.max(...rs.map(r=>r.bottom));
  for(const el of document.body.children){ if(!el.id||CL.includes(el.id)||/^(rDock|kRail|bgfx|flashbang|kShotCv|kCannonBtn|toast)$/.test(el.id)||el.hidden||el.dataset.kfixTop) continue; const st=getComputedStyle(el); if(st.position!=='fixed'||st.display==='none') continue; const R=el.getBoundingClientRect(); if(R.width<innerWidth*.5||R.height<innerHeight*.5||R.top>40) continue; if(el.scrollTop>4) continue;
   const under=[...el.querySelectorAll(INT)].some(i=>{ if(!i.getClientRects().length) return false; const r=i.getBoundingClientRect(); return r.width>0&&rs.some(c=>hit(r,c)); });
   if(under){ const pt=parseFloat(st.paddingTop)||0; const need=Math.ceil(low+6-R.top); if(need>pt){ el.style.paddingTop=need+'px'; el.dataset.kfixTop='1'; } } } },700);
 /* 9. The chord chart never has an empty bar. Doubling a 16-bar loop that had a 4-chord progression left bars 5 to 16 empty, and
    four buttons then stopped with an error (Translate, Story → beat, Beat → story, the storyboard). The copy is fixed at its source;
    this guard also fills any empty bar that arrives another way (an older saved song) by repeating the progression. */
 const fillChart=a=>{ if(!Array.isArray(a)) return a; let L0=0; while(L0<a.length&&a[L0]!=null) L0++; if(L0===a.length) return a; const out=a.slice(); for(let i=0;i<out.length;i++) if(out[i]==null) out[i]=L0?out[i%L0]:null; return out.filter(c=>c!=null); };
 const guardTheory=()=>{ const T=window.THEORY; if(!T||T.__kfix||typeof T.setChart!=='function') return; const f=T.setChart; T.setChart=function(a){ return f.call(this,fillChart(a)); }; T.__kfix=true; };
 guardTheory(); setInterval(()=>{ guardTheory(); try{ const T=window.THEORY; if(T&&Array.isArray(T.chart)&&T.chart.some(c=>c==null)) T.setChart(T.chart); }catch(_){ } },1500);
 /* 10. A screen's own status line that is scrolled out of sight (Karaoke's note sat 1,000 px above the layer buttons) is also shown
    as a short note at the bottom, so a press never looks like it did nothing. */
 const mirror=id=>{ let last=''; new MutationObserver(()=>{ const m=document.getElementById(id); if(!m) return; const t=(m.textContent||'').trim(); if(!t||t===last) return; last=t; const r=m.getBoundingClientRect(); const seen=r.bottom>0&&r.top<innerHeight&&m.getClientRects().length; if(!seen) say(t); }).observe(document.body,{subtree:true,childList:true,characterData:true}); };
 ['kkMsg'].forEach(mirror);
 /* 4b. Mutate's 📖 Use as my writing with nothing mutated yet */
 addEventListener('click',e=>{ if(!(e.target.closest&&e.target.closest('#mutToBook'))) return; const o=document.getElementById('mutOut'); if(o&&!o.value.trim()) say('🧬 Mutate some text first (type or paste it, then press Mutate); then use it as your writing.'); },true);
 /* 5. The story player's ◀◀ and ▶▶ before any canvas has landed */
 addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#pPrev,#pNext'); if(!b) return; let n=0; try{ n=(typeof MON!=='undefined'&&MON.items)?MON.items.length:0; }catch(_){ } if(!n) say('Land some canvases first (⚡ Quick Pick does it in one tap), then step through them with ◀◀ and ▶▶.'); },true);
 /* 6. A contents entry whose section is not built yet: say when it appears, instead of scrolling nowhere */
 addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#toc2 [data-goto]'); if(!b||b.dataset.goto==='s-extra') return; const t=document.getElementById(b.dataset.goto); const shown=t&&!t.hidden&&!t.closest('[hidden]')&&t.getClientRects().length; if(!shown){ const name=(b.textContent||'').replace(/^[\d.\s]+/,'').trim()||'That section'; setTimeout(()=>say('“'+name+'” appears once a story is built (⚡ Quick Pick builds one in a tap).'),60); } },true);
 addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('button'); if(!b) return; const t=(b.textContent||'').trim(); if(!/^(⏹|■)\uFE0F?\s*Stop( reading| the layers| the beat| everything)?$/.test(t)) return; if(playing()) return; /* checked before the button's own handler runs, so a real stop never shows this note */ setTimeout(()=>say('■ Nothing is playing right now.'),60); },true);
})();
