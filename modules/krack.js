(()=>{ /* 🎛 THE STEP SEQUENCER AS ITS OWN PANEL (v252): the channel rack, a Reason / FL-style grid of 16 steps for every sound, layered
   row under row and played from the same clock, floats like the pads and the keyboard: drag it, stack it, ▁ shrink it, ✕ close it, and
   🪟 Arrange tiles it with the other panels. It opens from 🎛 Steps on the transport bar. */
 const $=id=>document.getElementById(id);
 const css=document.createElement('style'); css.textContent=`
html.lvl-easy #pad #crSec.kFloat.kFOn:not(.kFOff){display:block!important}
#crSec.kFloat.kFOn:not(.kFOff){overflow:auto}
#crSec.kFloat.kFOn button,#crSec.kFloat.kFOn select{max-width:100%}`; document.head.appendChild(css);
 function reg(){ let F; try{ F=KRAIL.FLOAT; }catch(_){ return; } const cr=$('crSec'); if(!F||!F.add||!cr) return; if(!reg.done){ F.add('rack',{get:()=>$('crSec'),t:'🎛 Step sequencer · 16 steps a sound',i:'🎛',l:'Steps'}); reg.done=true;
   try{ if(!localStorage.getItem('kanin-float-rack')){ const W=innerWidth-(innerWidth<=760?58:76); localStorage.setItem('kanin-float-rack',JSON.stringify(innerWidth<=760?{x:4,y:56,w:W-8,h:Math.round(innerHeight*.7)}:{x:Math.round(W*.25),y:120,w:Math.round(W*.7),h:Math.round(innerHeight*.6)})); } }catch(_){ } }
  const bb=$('bbBar'); if(bb&&!bb.querySelector('[data-rko]')){ const b=document.createElement('button'); b.type='button'; b.dataset.rko='1'; b.setAttribute('data-noul',''); b.textContent='🎛 Steps'; b.title='The 16-step sequencer, as a floating panel'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); try{ F.toggle('rack'); }catch(_){ } },true); bb.appendChild(b); } }
 setInterval(reg,900);
 window.KRACK={open:()=>{ try{ KRAIL.FLOAT.open('rack'); }catch(_){ } }};
})();
