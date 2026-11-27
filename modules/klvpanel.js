(()=>{ /* LEVEL PANELS AND ONE UNDO (v209). The level a person picks decides how much control they see.
   🟢 Easy: the most elementary panels. The home page is a few giant buttons, the Studio is a few giant buttons over the 16 pads, the
   rail and the remote carry only the essentials, and the Menu shows only the most used. 🟡 Everyday: the tools creators use.
   🔴 Pro: every engine, knob and library. Nothing is deleted: a higher level brings everything back.
   ↶ UNDO: one button, pinned on every screen at every level (and Ctrl+Z / ⌘Z), takes back the last move: a knob, slider, picker or
   switch anywhere, or the screen's own last edit (the beat, the drawing, the take). It goes back step by step to the last save. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const lv=()=>{ try{ return KLEVEL.get(); }catch(_){ return 'avg'; } };
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 const press=sel=>{ const b=document.querySelector(sel); if(b){ b.click(); return true; } return false; };
 const fold=()=>{ try{ LAUNCHPAD.fold(); }catch(_){ } };
 const studio=then=>{ try{ KRAIL.goTo('pad'); }catch(_){ } if(then) setTimeout(then,900); };
 /* ── the giant-button panels ── */
 const css=document.createElement('style'); css.textContent=`
.kEasy{display:none;margin:10px auto;max-width:min(1800px,100%);box-sizing:border-box;padding:clamp(10px,1.4vw,28px);border:3px solid #ffe94a;border-radius:clamp(14px,1.4vw,28px);background:linear-gradient(160deg,#1c1850,#0d0b2a);color:#fff}
html.lvl-easy .kEasy{display:block}
.kEasy h3{margin:0 0 4px;font:900 clamp(20px,2.2vw,44px)/1.15 system-ui,sans-serif;color:#ffe94a;text-wrap:balance}
.kEasy p{margin:0 0 clamp(8px,1vw,18px);font:600 clamp(15px,1.3vw,26px)/1.45 system-ui,sans-serif;color:#d9d4ff}
.kEasy .ezGrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(clamp(130px,16vw,340px),1fr));gap:clamp(8px,1vw,20px)}
.kEasy .ezGrid button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(4px,.5vw,10px);min-height:clamp(96px,11vw,240px)!important;padding:clamp(8px,1vw,20px)!important;border-radius:clamp(14px,1.3vw,26px)!important;border:2px solid rgba(255,255,255,.25)!important;background:#2a2470!important;color:#fff!important;font:800 clamp(16px,1.5vw,30px)/1.2 system-ui,sans-serif!important;white-space:normal!important;overflow-wrap:anywhere;text-align:center;box-sizing:border-box;min-width:0}
.kEasy .ezGrid button i{font-style:normal;font-size:clamp(32px,3.6vw,84px);line-height:1}
.kEasy .ezGrid button.go{background:#137a3f!important}.kEasy .ezGrid button.st{background:#b3172f!important}.kEasy .ezGrid button.ud{background:#ffe94a!important;color:#14163a!important}
.kEasy .ezMore{margin-top:clamp(8px,1vw,18px);display:flex;flex-wrap:wrap;gap:8px;align-items:center;font:700 clamp(14px,1.2vw,24px)/1.4 system-ui,sans-serif;color:#bfb8ff}
.kEasy .ezMore button{min-height:44px;padding:4px 14px!important;border-radius:999px!important;font:800 clamp(14px,1.2vw,24px) system-ui,sans-serif!important}
html.lvl-easy #rDock#rDock :is(#kdProj,#kdSocial,#kdAI,#kdPanel,#kdTour,#kdIDJ){display:none!important}
html.lvl-easy #rDock#rDock button[data-kd-i]::before{font-size:calc(var(--kRailW,58px) * .44)!important}
html.lvl-easy #tourTab>*:not(.lpHead):not(.kLvlRow):not(.kStart):not([data-easy]){display:none!important}
html.lvl-easy #tourTab .kStartB[data-easy]{min-height:clamp(64px,7vw,140px)!important;font:800 clamp(17px,1.5vw,30px)/1.25 system-ui,sans-serif!important}
#kUndoAll{position:fixed;z-index:9760;top:calc(8px + env(safe-area-inset-top,0px));right:calc(var(--kRailW,58px) + 10px);min-height:44px!important;min-width:44px;padding:4px 12px!important;border-radius:999px!important;background:#ffe94a!important;color:#14163a!important;font:900 15px system-ui,sans-serif!important;border:2px solid #14163a!important;box-shadow:0 4px 16px rgba(0,0,0,.5)}
#kUndoAll[hidden]{display:none!important}body.gated #kUndoAll{display:none!important}
@media (min-width:1700px){ #kUndoAll,#kXAll{min-height:56px!important;font-size:20px!important;padding:6px 18px!important} }
@media (min-width:2500px){ #kUndoAll,#kXAll{min-height:72px!important;font-size:26px!important;padding:8px 24px!important} }`; document.head.appendChild(css);
 const btn=(i,l,cls,act)=>'<button type="button" data-ez="'+act+'" class="'+(cls||'')+'" data-noul><i>'+i+'</i>'+l+'</button>';
 const more='<div class="ezMore">Want more buttons? <button type="button" data-ez="lv:avg" data-noul>🟡 Everyday</button><button type="button" data-ez="lv:pro" data-noul>🔴 Pro</button></div>';
 const HOME=[['📖','Make a story','','story'],['🥁','Make a beat','go','beat'],['🎤','Sing karaoke','','sing'],['😂','Laugh','','laugh'],['🕹','Play a game','','game'],['🎨','Draw','','draw'],['♈','LuvMyZodiac','','zod'],['👤','My profile','','me'],['🤖','Ask for help','','help'],['📰','News','','news'],['✝️','Religion','','faith'],['📈','Stock market','','market'],['🗺','Show me around','','tour']];
 const STU=[['🎲','Make me a beat','go','auto'],['▶','Play','go','play'],['■','Stop','st','stop'],['🎨','Change the style','','style'],['↶','Undo','ud','undo'],['💾','Save','','save'],['🎤','Sing on it','','sing'],['❓','How do I?','','how']];
 const ACT={
  story:()=>{ fold(); try{ GOHOME(); }catch(_){ } setTimeout(()=>{ press('#mQP')||press('#qpBtn'); setTimeout(()=>{ const d=document.querySelector('section.desk'); if(d&&d.getClientRects().length) d.scrollIntoView({behavior:'smooth',block:'start'}); say('📖 Your story is written. Scroll to read it, or tap 📖 Make a story again for another.'); },1800); },150); },
  beat:()=>{ fold(); studio(()=>{ press('#cAuto'); say('🥁 A beat is ready. Tap ▶ Play.'); }); },
  sing:()=>{ fold(); try{ KKARA.open(); }catch(_){ } },
  laugh:()=>{ fold(); try{ KHUMOR.open('day'); }catch(_){ } },
  game:()=>{ fold(); try{ KRAIL.goTo('gamesDock'); setTimeout(()=>{ try{ KGSIMPLE.show('groups'); }catch(_){ } },450); }catch(_){ try{ KVG.open(); }catch(__){ } } },
  news:()=>{ fold(); try{ KNEWS.open('today'); }catch(_){ } },
  faith:()=>{ fold(); try{ KRELIG.open('big'); }catch(_){ } },
  market:()=>{ fold(); try{ KMARKET.open('today'); }catch(_){ } },
  draw:()=>{ fold(); try{ KEASEL.open(); }catch(_){ } },
  zod:()=>{ fold(); try{ KRAIL.goTo('zodDock'); }catch(_){ } },
  me:()=>{ fold(); try{ KPROFILE.open(); }catch(_){ try{ KRAIL.goTo('kProfile'); }catch(_){ } } },
  help:()=>{ fold(); try{ KAI.open(); }catch(_){ press('#askBtn'); } },
  tour:()=>{ fold(); press('#kHomeBar [data-ka="tour"]')||press('#ttTour'); },
  auto:()=>{ press('#cAuto'); say('🎲 A new beat is written. Tap ▶ Play.'); },
  play:()=>{ try{ KSTUDIO.play(); }catch(_){ press('#bbPlay'); } },
  stop:()=>{ try{ KREMOTE.act.stop(); }catch(_){ press('#bbStop'); } },
  style:()=>{ const s=$('padKit'); if(!s||!s.options.length) return say('Open the Studio first.'); s.selectedIndex=(s.selectedIndex+1)%s.options.length; s.dispatchEvent(new Event('change',{bubbles:true})); say('🎨 Style: '+s.options[s.selectedIndex].text+'. Tap ▶ Play to hear it.'); },
  undo:()=>KUNDO.any(),
  save:()=>{ try{ KREMOTE.act.save(); }catch(_){ press('#padSave'); } },
  how:()=>say('Tap a colored pad to hear it. Tap 🎲 Make me a beat for a whole beat, then ▶ Play. ↶ Undo takes back your last move.')};
 function panel(id,where,pos,title,sub,list){ let p=$(id); const host=typeof where==='function'?where():where; if(!host) return; if(p&&p.isConnected) return p;
  p=document.createElement('div'); p.id=id; p.className='kEasy'; p.innerHTML='<h3>'+title+'</h3><p>'+sub+'</p><div class="ezGrid">'+list.map(x=>btn(x[0],x[1],x[2],x[3])).join('')+'</div>'+more;
  host.insertAdjacentElement(pos,p); p.addEventListener('click',e=>{ const b=e.target.closest('[data-ez]'); if(!b) return; e.preventDefault(); e.stopPropagation(); const a=b.dataset.ez; if(a.startsWith('lv:')){ try{ KLEVEL.set(a.slice(3)); }catch(_){ } return; } const f=ACT[a]; if(f) f(); }); return p; }
 /* what each level hides: on Easy the deep parts of home and the Studio step aside (nothing deleted) */
 const HOME_DEEP=['master','contents','manual','monitors','control','s-rail','s-words','s-drive','shape','outputs','s-referee'];
 const HOME_DEEP_CLS=['nav.stagenav','section.monitors','section.bay','section.deck','section.outbay'];
 const PAD_DEEP=[]; /* the Studio keeps every part at every level: the sequencer and mixer first, every module below */
 const EASY_MENU=/^(🎲 Games|📰 Current News|✝️ Cultures & Religion|📈 Stock Market|🍳 Recipes|📁 Projects|🎛 Studio|🎤 Karaoke|📖 Make a story|😂 Laugh|🕹 Video games|♈ LuvMyZodiac|👤 My profile|🎨 The Easel|🤖 AI|🗺 Show me around|🎵 Music|🧭 Omni-Compass)/;
 const tagLv=e=>{ if(e&&e.dataset.lvl!=='avg'&&e.dataset.lvl!=='pro') e.dataset.lvl='avg'; };
 let easyPadFor='';
 function tag(){ HOME_DEEP.forEach(id=>tagLv($(id))); HOME_DEEP_CLS.forEach(s=>document.querySelectorAll('.wrap>'+s).forEach(tagLv)); PAD_DEEP.forEach(id=>tagLv($(id)));
  /* the Studio hides nothing on any level */
  const t=$('tourTab'); if(t) t.querySelectorAll('.kStartB').forEach(b=>{ const on=EASY_MENU.test(b.textContent.trim()); if(on&&!b.hasAttribute('data-easy')) b.setAttribute('data-easy',''); });
  panel('kEasyHome',()=>document.querySelector('.wrap>header.mast')||document.querySelector('.wrap>header'),'afterend','🟢 What do you want to do?','Tap one big button. That is all it takes.',HOME);
    /* the pads keep floating over the sequencer on every level */
  panel('kEasyStudio',()=>$('bbBar'),'beforebegin','🟢 Easy Studio','Tap 🎲 Make me a beat, then ▶ Play. Or tap the colored pads below to play sounds yourself.',STU); }
 setInterval(tag,1000); tag();
 /* ── ONE UNDO ── every knob, slider, picker and switch remembers its last value; the screen's own undo covers its own edits */
 const stack=[]; const lastAct={}; const OWN=new Set(['pad','kKara','kEasel','gamesDock','musicDock']); let restoring=false;
 const valOf=e=>e.type==='checkbox'||e.type==='radio'?e.checked:e.value;
 const isCtl=e=>e&&e.matches&&e.matches('input,select,textarea')&&!/^(file|password|button|submit|hidden)$/.test(e.type||'')&&!e.closest('#kAI,#gateWrap,.kSearch');
 const nameOf=e=>{ const l=e.closest('label'); const t=(e.getAttribute('aria-label')||e.title||(l&&l.textContent)||e.name||e.id||'a setting').trim().replace(/\s+/g,' '); return t.slice(0,40); };
 const snap=e=>{ if(isCtl(e)&&e.__kuOld===undefined) e.__kuOld=valOf(e); };
 document.addEventListener('focusin',e=>snap(e.target),true); document.addEventListener('pointerdown',e=>{ const c=e.target.closest&&e.target.closest('input,select,textarea'); if(c) snap(c); const l=e.target.closest&&e.target.closest('label'); if(l){ const i=l.querySelector('input,select'); if(i) snap(i); } },true);
 document.addEventListener('change',e=>{ const t=e.target; if(restoring||!isCtl(t)) return; const old=t.__kuOld; const now=valOf(t); t.__kuOld=now; if(old===undefined||old===now) return; stack.push({el:t,old,now,at:performance.now(),scr:cur(),name:nameOf(t)}); if(stack.length>200) stack.shift(); paintU(); },true);
 const PINS='#kSeqTools,#k40Seq,#kFXRet,#kkMix,.kStrip,#kKbd,#kRemote,#rDock,#kXAll,#kUndoAll,#tourTab,.kEasy [data-ez="undo"],.kEasy [data-ez="save"],.kEasy [data-ez="play"],.kEasy [data-ez="stop"],.kEasy [data-ez="how"]';
 const SAVES='[id$="Save"],[data-kk="save"],[data-pj="save"],[data-r="save"],[data-ez="save"]';
 document.addEventListener('click',e=>{ const t=e.target; if(!t.closest) return; if(t.closest(SAVES)||/^💾/.test((t.closest('button')||{}).textContent||'')){ stack.length=0; Object.keys(lastAct).forEach(k=>delete lastAct[k]); setTimeout(paintU,50); return; } if(t.closest(PINS)) return; if(t.closest('button,canvas,.pd,[data-step]')) lastAct[cur()]=performance.now(); },true);
 function undoOne(){ const g=stack.pop(); if(!g) return false; if(g.fn){ try{ g.fn(); }catch(_){ } say('↶ Undid: '+g.name+(stack.length?' · '+stack.length+' more to undo':'')); paintU(); return true; } if(g.el&&g.el.isConnected){ restoring=true; try{ if(g.el.type==='checkbox'||g.el.type==='radio') g.el.checked=g.old; else g.el.value=g.old; g.el.__kuOld=g.old; g.el.dispatchEvent(new Event('input',{bubbles:true})); g.el.dispatchEvent(new Event('change',{bubbles:true})); }catch(_){ } restoring=false; say('↶ Undid: '+g.name+(stack.length?' · '+stack.length+' more to undo':'')); } else return undoOne(); paintU(); return true; }
 function any(){ const id=cur(); const g=stack.length?stack[stack.length-1]:null; const own=OWN.has(id);
  if(g&&(!own||g.at>=(lastAct[id]||0))) return undoOne();
  if(own){ try{ KREMOTE.undoScreen(); }catch(_){ } return true; }
  say('Nothing to undo since your last save.'); return false; }
 document.addEventListener('keydown',e=>{ if(!(e.ctrlKey||e.metaKey)||e.shiftKey||e.altKey||(e.key||'').toLowerCase()!=='z') return; const t=e.target; if(t&&(t.isContentEditable||/^(INPUT|TEXTAREA)$/.test(t.tagName)&&!/^(range|checkbox|radio|color)$/.test(t.type||''))) return; if(document.body.classList.contains('gated')) return; e.preventDefault(); any(); },true);
 /* the pinned ↶ Undo: beside ✕ Close at the top, on every screen where there is something to take back */
 function paintU(){ let b=$('kUndoAll'); if(!b){ b=document.createElement('button'); b.type='button'; b.id='kUndoAll'; b.setAttribute('data-noul',''); b.setAttribute('aria-label','Undo the last move'); b.title='Undo the last move (Ctrl+Z)'; b.textContent='↶ Undo'; b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); any(); }); document.body.appendChild(b); }
  const t=$('tourTab'); const menuOpen=t&&t.getClientRects().length&&getComputedStyle(t).display!=='none'&&t.getBoundingClientRect().width>40; const id=cur();
  const narrow=innerWidth<600; const tx=narrow?'↶':'↶ Undo'; if(b.textContent!==tx) b.textContent=tx; const xc=$('kXAll'); if(xc){ const t2=narrow?'✕':'✕ Close'; if(xc.textContent!==t2) xc.textContent=t2; }
  b.hidden=!!menuOpen||!(stack.length||OWN.has(id)); if(b.hidden) return; const x=$('kXAll'); const rw=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58;
  const off=(x&&!x.hidden&&x.getClientRects().length)?x.getBoundingClientRect().width+8:0; b.style.right=(rw+10+off)+'px'; }
 setInterval(paintU,400);
 window.KUNDO={push:(fn,name)=>{ stack.push({fn,name:name||'the last edit',at:performance.now(),scr:cur()}); if(stack.length>200) stack.shift(); paintU(); },any,undo:undoOne,get count(){ return stack.length; },saved:()=>{ stack.length=0; paintU(); }};
 window.KEASY={act:ACT,tag};
})();
