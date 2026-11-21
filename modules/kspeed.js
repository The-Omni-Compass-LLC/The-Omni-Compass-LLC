(()=>{ /* ⏱ THE SPEED KNOB, THE CLICK AND THE BEAT LIGHT (v225), built into both floating devices (the 16 pads and the keyboard).
   The knob is the studio's one tempo (40 to 240 BPM): drag it up or down, roll the wheel, or use the arrow keys; its gauge shows where
   you are, green to red. 🔔 CLICK switches the studio's metronome. The light flashes on every beat (red on bar one). The sequencer,
   the mixing board and every device follow the same tempo, because it is the same control. */
 const $=id=>document.getElementById(id); const PS=()=>window.PADSTUDIO; const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const clickOn=()=>{ const c=$('padClick'); const t=c?c.textContent:''; return /on/i.test(t)&&!/off/i.test(t); };
 const bpmNow=()=>{ const b=$('padBpm'); return Math.max(40,Math.min(240,+(b&&b.value)||90)); };
 const setBpm=v=>{ const b=$('padBpm'); if(!b) return; v=Math.round(Math.max(40,Math.min(240,v))); if(+b.value===v) return; b.value=String(v); b.dispatchEvent(new Event('input',{bubbles:true})); b.dispatchEvent(new Event('change',{bubbles:true})); };
 const css=document.createElement('style'); css.textContent=`
#mpcBar [data-m="bpm"],#mpcBar #mpcBpm,#mpcBar [data-m="click"],#kbDash [data-k="bpm"],#kbDash #kbDashBpm{display:none!important}
.kSpd{display:flex;align-items:center;gap:6px;flex:none}
html body .kSpd .knob{width:58px!important;height:58px!important;min-width:0!important;max-width:58px!important;flex:none;cursor:ns-resize;touch-action:none;border-radius:50%!important;outline:none;background:none!important;border:0!important;padding:0!important;margin:0!important;box-shadow:none!important;display:block}
.kSpd .knob:focus-visible{box-shadow:0 0 0 3px #ffe94a}
.kSpd .knob text{font:900 17px ui-monospace,monospace;fill:#fff}
.kSpd .knob .u{font:800 8px system-ui,sans-serif;fill:#9aa3b8;letter-spacing:.08em}
.kSpd .col{display:flex;flex-direction:column;gap:4px;align-items:center}
.kSpd .fine{display:flex;gap:3px}
.kSpd .fine button{min-height:26px!important;min-width:30px!important;padding:0!important;border-radius:8px!important;font:900 13px system-ui,sans-serif!important;background:#2c303b!important;color:#fff!important;border:2px solid #444a5a!important}
.kSpd .clk{min-height:44px!important;min-width:56px;border-radius:10px!important;font:900 13px/1.1 system-ui,sans-serif!important;padding:0 6px!important;background:#2c303b!important;color:#f2f2f2!important;border:2px solid #444a5a!important;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.kSpd .clk.on{background:#ffe94a!important;color:#14163a!important;border-color:#ffe94a!important}
.kSpd .led{width:14px;height:14px;border-radius:50%;background:#2a2f3a;border:2px solid #444a5a;flex:none}
.kSpd .led.b{background:#7cff8a;box-shadow:0 0 10px #7cff8a}.kSpd .led.d{background:#ff3b4f;box-shadow:0 0 12px #ff3b4f}
.kSpd .lbl{font:800 10px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.08em;text-transform:uppercase}
@media (max-height:700px){ html body .kSpd .knob{width:44px!important;height:44px!important;max-width:44px!important} .kSpd .col > .lbl{display:none} .kSpd .clk{min-height:36px!important;min-width:48px} .kSpd .fine button{min-height:22px!important} }`; document.head.appendChild(css);
 const R=24, C=29, A0=-135, A1=135; const pt=a=>{ const r=(a-90)*Math.PI/180; return [C+R*Math.cos(r),C+R*Math.sin(r)]; };
 const arc=(a,b)=>{ const [x0,y0]=pt(a), [x1,y1]=pt(b); return 'M'+x0.toFixed(2)+' '+y0.toFixed(2)+' A'+R+' '+R+' 0 '+(b-a>180?1:0)+' 1 '+x1.toFixed(2)+' '+y1.toFixed(2); };
 const col=f=>f<.5?'#7cff8a':f<.78?'#ffe94a':'#ff6b6b';
 function knobSVG(v){ const f=(v-40)/200, a=A0+f*(A1-A0); const [px,py]=pt(a); return '<svg viewBox="0 0 58 58" width="100%" height="100%" aria-hidden="true"><circle cx="29" cy="29" r="27" fill="#14161c" stroke="#3a3f4d" stroke-width="2"/><path d="'+arc(A0,A1)+'" stroke="#2c303b" stroke-width="5" fill="none" stroke-linecap="round"/><path d="'+arc(A0,Math.max(A0+1,a))+'" stroke="'+col(f)+'" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="'+px.toFixed(2)+'" cy="'+py.toFixed(2)+'" r="3.5" fill="#fff"/><text x="29" y="32" text-anchor="middle">'+v+'</text><text class="u" x="29" y="42" text-anchor="middle">BPM</text></svg>'; }
 function block(){ const d=document.createElement('div'); d.className='kSpd'; d.innerHTML='<div class="col"><span class="lbl">Speed</span><div class="knob" role="slider" tabindex="0" aria-label="Speed (tempo)" aria-valuemin="40" aria-valuemax="240"></div></div><div class="col"><div class="fine"><button type="button" data-sp="-1" aria-label="One slower" data-noul>−</button><button type="button" data-sp="1" aria-label="One faster" data-noul>+</button></div><span class="led" aria-hidden="true"></span></div><button type="button" class="clk" data-sp="click" title="Metronome click" data-noul>🔔<span>Click</span></button>';
  const k=d.querySelector('.knob'); let drag=null;
  k.addEventListener('pointerdown',e=>{ drag={y:e.clientY,v:bpmNow()}; try{ k.setPointerCapture(e.pointerId); }catch(_){ } e.preventDefault(); e.stopPropagation(); });
  k.addEventListener('pointermove',e=>{ if(!drag) return; setBpm(drag.v+(drag.y-e.clientY)/2.5); paint(); });
  const end=()=>{ drag=null; }; k.addEventListener('pointerup',end); k.addEventListener('pointercancel',end);
  k.addEventListener('wheel',e=>{ e.preventDefault(); setBpm(bpmNow()+(e.deltaY<0?1:-1)*(e.shiftKey?5:1)); paint(); },{passive:false});
  k.addEventListener('keydown',e=>{ const s={ArrowUp:1,ArrowRight:1,ArrowDown:-1,ArrowLeft:-1,PageUp:10,PageDown:-10}[e.key]; if(s){ e.preventDefault(); e.stopPropagation(); setBpm(bpmNow()+s); paint(); } });
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-sp]'); if(!b) return; e.stopPropagation(); if(b.dataset.sp==='click') press('padClick'); else setBpm(bpmNow()+(+b.dataset.sp)); paint(); });
  return d; }
 function ensure(host){ if(!host) return null; let d=host.querySelector('.kSpd'); if(d) return d; const row=host.querySelector('.mr2'); if(!row) return null; d=block(); row.insertBefore(d,row.firstChild); return d; }
 let lastV=-1, lastClick=null;
 function paint(){ const v=bpmNow(), ck=clickOn(); document.querySelectorAll('.kSpd').forEach(d=>{ const k=d.querySelector('.knob'); if(k.__v!==v){ k.innerHTML=knobSVG(v); k.__v=v; k.setAttribute('aria-valuenow',String(v)); } d.querySelector('.clk').classList.toggle('on',ck); }); }
 /* the beat light follows the loop's own playhead */
 let lastBeat=-1; function led(){ const P=window.PADS||{}; const ps=PS(); const spb=(ps&&ps.spbN)||16, per=Math.max(1,spb/4); let cls=''; if(P.playing&&P.step>=0){ const beat=Math.floor(P.step/per); if(P.step%per===0||beat!==lastBeat){ lastBeat=beat; } const within=(P.step%per)/per; if(within<0.5) cls=P.step%spb<per?'d':'b'; } else lastBeat=-1; document.querySelectorAll('.kSpd .led').forEach(l=>{ if(l.className!=='led'+(cls?' '+cls:'')) l.className='led'+(cls?' '+cls:''); }); requestAnimationFrame(led); }
 requestAnimationFrame(led);
 setInterval(()=>{ const pad=$('pad'); if(!pad||!pad.classList.contains('on')) return; ensure($('mpcBar')); ensure($('kbDash')); paint(); },300);
 window.KSPEED={setBpm,bpm:bpmNow,paint};
})();
