(()=>{ /* 🟢 EASY MEANS FEW BUTTONS (v244). On the Easy level (the factory level) every device shows only what a first-timer needs, and one
   ⚙ MORE button opens the rest, on that device only:
     🥁 beat machine   ⏮ REWIND · ▶ PLAY · ■ STOP · ● REC · ↶ UNDO · ⬇ LOAD · banks A B C D · 🥁 BEAT / 🎧 DJ
     🎹 keyboard       ⏮ REWIND · ▶ PLAY · ■ STOP · ● REC · ↶ UNDO · ⬇ LOAD · OCT − / OCT +
     🎼 tracks         ⏮ · ▶ · ■ · ● REC · ＋ Keyboard track, and on each track ● select · M · S · ⬇ LOAD
   Everything ⚙ MORE hides still works from its key on the keyboard. Everyday and Pro show every button, as before.
   And one account everywhere: 🌐 Social and 👤 Profile (the rail and the Menu) open your page (sign in first). */
 const $=id=>document.getElementById(id);
 const css=document.createElement('style'); css.textContent=`
html.lvl-easy body:not(.kDemoOn) #mpcBar:not(.kAll) .kScr [data-sf]:not([data-sf="snd"]):not([data-sf^="bank"]){display:none!important}
html.lvl-easy body:not(.kDemoOn) #kbDash:not(.kAll) .kScr [data-sf]:not([data-sf="snd"]):not([data-sf="octd"]):not([data-sf="octu"]){display:none!important}
html.lvl-easy body:not(.kDemoOn) :is(#mpcBar,#kbDash):not(.kAll) .kDevTx :is([data-tx="skip"],[data-tx="clear"],[data-tx="latch"]){display:none!important}
html.lvl-easy body:not(.kDemoOn) #mpcBar:not(.kAll) .kDjBar :is([data-dm="roll"],[data-dm="fx"],[data-dm="samp"],[data-dm="open"]){display:none!important}
html.lvl-easy body:not(.kDemoOn) #mpcBar:not(.kAll) .kDjBar [data-dm="cue"]{font-size:0!important}
html.lvl-easy body:not(.kDemoOn) #mpcBar:not(.kAll) .kDjBar [data-dm="cue"]::after{content:"🎧 DJ";font:900 11.5px system-ui,sans-serif}
html.lvl-easy body:not(.kDemoOn) #kSeqWin:not(.kAll) .sqTop :is([data-sq="loop"],[data-sq="q"],[data-sq="mix"],[data-sq="demo"]){display:none!important}
html.lvl-easy body:not(.kDemoOn) #kSeqWin:not(.kAll) .sqHead :is([data-tk="q"],[data-tk="clr"],[data-tk="del"],[data-tk="dev"],input[type=range]){display:none!important}
.kEzMore{display:none}
html.lvl-easy .kEzMore{display:inline-flex;align-items:center;justify-content:center}
.kEzMore.on{background:#ffe94a!important;color:#14163a!important}`; document.head.appendChild(css);
 function more(host,where,label){ if(!host) return; const at=where?host.querySelector(where):host; if(!at) return; let b=at.querySelector(':scope > .kEzMore'); if(!b){ b=document.createElement('button'); b.type='button'; b.className='kEzMore'; b.setAttribute('data-noul',''); b.title='Show every button on this device'; b.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); host.classList.toggle('kAll'); paint(); try{ KPADFLOAT.fit('pads'); }catch(_){ } }); at.appendChild(b); }
  const on=host.classList.contains('kAll'); const t=on?'⚙ Less':'⚙ More'; if(b.textContent!==t) b.textContent=t; b.classList.toggle('on',on); }
 function paint(){ more($('mpcBar'),':scope > .kDevTx'); more($('kbDash'),':scope > .kDevTx'); more($('kSeqWin'),'.sqTop'); }
 setInterval(paint,700);
 /* one account everywhere */
 const acct=tab=>{ try{ KACCT.open(tab); return true; }catch(_){ return false; } };
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#kdSocial,#tourTab button,#kEasyHome [data-ez="me"]'); if(!b) return; const tx=(b.textContent||'').trim();
  let tab=null; if(b.id==='kdSocial'||/^🌐 Social/.test(tx)) tab='feed'; else if(/^👤 My profile/.test(tx)||b.dataset.ez==='me') tab='posts'; if(!tab) return;
  if(acct(tab)){ e.preventDefault(); e.stopImmediatePropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } } },true);
 window.KEZ={paint};
})();
