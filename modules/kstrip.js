(()=>{ /* THE CONSOLE KNOBS (v210): every strip of the 40-track mixer gets a full channel strip of real knobs wired into the sound:
   GAIN (trim, ±12 dB) · LOW CUT (20–400 Hz) · HI (8 kHz shelf, ±12 dB) · MID (bell, ±12 dB) · MID ƒ (200 Hz–5 kHz) · LO (120 Hz shelf,
   ±12 dB) · REV (send to the reverb bus) · ECHO (send to the echo bus). The console's returns sit beside them: reverb level and size,
   echo level, time (locked to the tempo) and feedback. Karaoke gets its own 8-track mixer (mics 1–5, DJ A and B, the backing),
   the same tracks as the console, so a move on either one shows on both. Drag a knob up or down, scroll it, use the arrow keys;
   double-tap puts it back to the middle. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const MIX=()=>(PS()&&PS().MIX)||[];
 const K=[['trim','GAIN',-12,12,.5,0,'dB'],['hpf','CUT',20,400,5,20,'Hz'],['hi','HI',-12,12,.5,0,'dB'],['mid','MID',-12,12,.5,0,'dB'],['mf','MID ƒ',200,5000,25,1000,'Hz'],['lo','LO',-12,12,.5,0,'dB'],['rv','REV',0,1,.02,0,'%'],['dl','ECHO',0,1,.02,0,'%']];
 const fmt=(v,u)=>u==='s'?(+v).toFixed(2)+'s':u==='%'?Math.round(v*100)+'%':u==='Hz'?(v>=1000?(v/1000).toFixed(1)+'k':Math.round(v)):(v>0?'+':'')+(+v).toFixed(1);
 const css=document.createElement('style'); css.textContent=`
.kKnob{position:relative;display:flex;flex-direction:column;align-items:center;gap:1px;cursor:ns-resize;touch-action:none;user-select:none;-webkit-user-select:none;outline:none}
.kKnob .kd{width:var(--kz,26px);height:var(--kz,26px);border-radius:50%;background:radial-gradient(circle at 35% 30%,#5a5f7a,#1c1f2e 70%);border:2px solid #0b0d18;box-shadow:0 0 0 2px var(--kc,#6fe8ff) inset,0 2px 4px rgba(0,0,0,.6);position:relative}
.kKnob .kd::after{content:"";position:absolute;left:50%;top:2px;width:2px;height:42%;margin-left:-1px;background:#fff;border-radius:2px;transform-origin:50% calc(var(--kz,26px)/2 - 2px);transform:rotate(var(--a,0deg))}
.kKnob b{font:800 8px/1 system-ui,sans-serif;color:var(--kc,#6fe8ff);letter-spacing:.02em;white-space:nowrap}
.kKnob i{font:600 8px/1 ui-monospace,monospace;font-style:normal;color:#cfd;white-space:nowrap}
.kKnob:focus-visible .kd{outline:2px solid #ffe94a;outline-offset:2px}
html body #padMixer#padMixer .mxs .kStrip{display:flex;flex-direction:column;align-items:center;gap:3px;width:100%;padding-bottom:4px;border-bottom:1px solid rgba(255,255,255,.12);margin-bottom:2px}
@media (min-width:1700px){ .kKnob{--kz:34px} .kKnob b,.kKnob i{font-size:10.5px} }
@media (min-width:2500px){ .kKnob{--kz:48px} .kKnob b,.kKnob i{font-size:14px} }
#kFXRet{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;margin:6px 0;padding:8px 10px;border:1px solid rgba(111,232,255,.4);border-radius:12px;background:linear-gradient(180deg,#141a2e,#0a0d1a)}
#kFXRet>b{font:900 clamp(12px,1vw,18px) system-ui,sans-serif;color:#9ff;align-self:center}
#kFXRet .kKnob{--kz:40px} #kFXRet .kKnob b,#kFXRet .kKnob i{font-size:11px}
#kFXRet select,#kFXRet button{min-height:36px;border-radius:9px;font:700 12px system-ui,sans-serif}
#kkMix{margin:10px 0;padding:8px;border:2px solid #ff7ad9;border-radius:14px;background:linear-gradient(180deg,#1d1030,#0a0716)}
#kkMix h4{margin:0 0 6px;font:900 clamp(14px,1.1vw,22px) system-ui,sans-serif;color:#ff9ae6}
#kkMix .kmGrid{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:6px}
@media (max-width:640px){ #kkMix .kmGrid{grid-template-columns:repeat(4,minmax(0,1fr))} }
#kkMix .kms{display:flex;flex-direction:column;align-items:center;gap:4px;padding:6px 3px;border:1px solid rgba(255,255,255,.15);border-radius:10px;background:rgba(255,255,255,.04);min-width:0}
#kkMix .kms small{font:800 clamp(10px,.8vw,15px)/1.15 system-ui,sans-serif;color:#fff;text-align:center;overflow-wrap:anywhere}
#kkMix .kms input[type=range]{width:100%}
#kkMix .kms .mb{display:flex;gap:3px}
#kkMix .kms .mb button{min-height:30px;min-width:30px;border-radius:7px;font:800 12px system-ui,sans-serif}
#kkMix .kms .mb button.on{background:#ffe94a!important;color:#14163a!important}
#kkMix .kms .mb button.m.on{background:#b3172f!important;color:#fff!important}
#kkMix .kms .kq{display:grid;grid-template-columns:1fr 1fr;gap:4px}`; document.head.appendChild(css);
 const COLR={trim:'#ffe94a',hpf:'#ff9f43',hi:'#6fe8ff',mid:'#7dff8a',mf:'#7dff8a',lo:'#ff7ad9',rv:'#b48cff',dl:'#b48cff'};
 function knob(ci,k){ const d=K.find(x=>x[0]===k); const m=MIX()[ci]||{}; const v=m[k]!=null?m[k]:d[5]; const f=(v-d[2])/(d[3]-d[2]);
  return '<div class="kKnob" role="slider" tabindex="0" data-ci="'+ci+'" data-k="'+k+'" aria-label="'+d[1]+' track '+(+ci+1)+'" aria-valuemin="'+d[2]+'" aria-valuemax="'+d[3]+'" aria-valuenow="'+v+'" style="--kc:'+COLR[k]+';--a:'+Math.round(-135+270*f)+'deg" title="'+d[1]+' · '+fmt(v,d[6])+' '+(d[6]==='%'?'':d[6])+' · drag, scroll or arrows · double-tap resets"><div class="kd"></div><b>'+d[1]+'</b><i>'+fmt(v,d[6])+'</i></div>'; }
 function setK(el,v){ const ci=+el.dataset.ci, k=el.dataset.k; const d=K.find(x=>x[0]===k)||FXK.find(x=>x[0]===k); if(!d) return; v=Math.max(d[2],Math.min(d[3],Math.round(v/d[4])*d[4])); const f=(v-d[2])/(d[3]-d[2]);
  el.style.setProperty('--a',Math.round(-135+270*f)+'deg'); el.setAttribute('aria-valuenow',v); const i=el.querySelector('i'); if(i) i.textContent=fmt(v,d[6]);
  if(el.dataset.fx){ window.KFX[k]=v; try{ KFXAPPLY(); }catch(_){ } return; }
  const X=MIX(); while(X.length<=ci) X.push({vol:.9,pan:0,mute:false,solo:false}); X[ci][k]=v; try{ PS().mixApply(); }catch(_){ }
  document.querySelectorAll('.kKnob[data-ci="'+ci+'"][data-k="'+k+'"]').forEach(o=>{ if(o!==el){ o.style.setProperty('--a',Math.round(-135+270*f)+'deg'); const j=o.querySelector('i'); if(j) j.textContent=fmt(v,d[6]); } }); }
 const val=el=>+el.getAttribute('aria-valuenow');
 const defOf=el=>{ const d=K.find(x=>x[0]===el.dataset.k)||FXK.find(x=>x[0]===el.dataset.k); return d?d[5]:0; };
 let drag=null;
 document.addEventListener('pointerdown',e=>{ const el=e.target.closest&&e.target.closest('.kKnob'); if(!el) return; e.preventDefault(); e.stopPropagation(); const d=K.find(x=>x[0]===el.dataset.k)||FXK.find(x=>x[0]===el.dataset.k); drag={el,y:e.clientY,v:val(el),span:d[3]-d[2],old:val(el)}; try{ el.setPointerCapture(e.pointerId); }catch(_){ } el.focus({preventScroll:true}); },true);
 document.addEventListener('pointermove',e=>{ if(!drag) return; const dy=drag.y-e.clientY; setK(drag.el,drag.v+dy/(e.shiftKey?600:150)*drag.span); },true);
 const up=()=>{ if(!drag) return; const d=drag; drag=null; const nv=val(d.el); if(nv!==d.old){ try{ KUNDO.push(()=>setK(d.el.isConnected?d.el:document.querySelector('.kKnob[data-ci="'+d.el.dataset.ci+'"][data-k="'+d.el.dataset.k+'"]')||d.el,d.old),'Knob '+d.el.dataset.k.toUpperCase()); }catch(_){ } } };
 document.addEventListener('pointerup',up,true); document.addEventListener('pointercancel',up,true);
 document.addEventListener('wheel',e=>{ const el=e.target.closest&&e.target.closest('.kKnob'); if(!el) return; e.preventDefault(); const d=K.find(x=>x[0]===el.dataset.k)||FXK.find(x=>x[0]===el.dataset.k); setK(el,val(el)-Math.sign(e.deltaY)*d[4]*(e.shiftKey?1:2)); },{passive:false,capture:true});
 document.addEventListener('keydown',e=>{ const el=e.target.closest&&e.target.closest('.kKnob'); if(!el) return; const d=K.find(x=>x[0]===el.dataset.k)||FXK.find(x=>x[0]===el.dataset.k); const st=d[4]*(e.shiftKey?10:1); if(e.key==='ArrowUp'||e.key==='ArrowRight'){ e.preventDefault(); e.stopPropagation(); setK(el,val(el)+st); } if(e.key==='ArrowDown'||e.key==='ArrowLeft'){ e.preventDefault(); e.stopPropagation(); setK(el,val(el)-st); } if(e.key==='Home'||e.key==='0'){ e.preventDefault(); setK(el,defOf(el)); } },true);
 document.addEventListener('dblclick',e=>{ const el=e.target.closest&&e.target.closest('.kKnob'); if(el){ e.preventDefault(); setK(el,defOf(el)); } },true);
 /* every strip of the 40-track console */
 function strips(){ const m=$('padMixer'); if(!m) return; m.querySelectorAll('.mxs[data-c]').forEach(st=>{ if(st.querySelector('.kStrip')) return; const ci=+st.dataset.c; const w=document.createElement('div'); w.className='kStrip'; w.innerHTML=K.map(x=>knob(ci,x[0])).join(''); st.insertBefore(w,st.firstChild); }); }
 /* the console's returns: reverb and echo */
 const FXK=[['rvRet','REV LEVEL',0,1.5,.02,.8,'%'],['rvSize','REV SIZE',.4,6,.1,2.4,'s'],['dlRet','ECHO LEVEL',0,1.5,.02,.7,'%'],['dlTime','ECHO TIME',.05,1.5,.01,.33,'s'],['dlFb','FEEDBACK',0,.9,.02,.38,'%']];
 function fxKnob(k){ const d=FXK.find(x=>x[0]===k); const v=(window.KFX&&KFX[k]!=null)?KFX[k]:d[5]; const f=(v-d[2])/(d[3]-d[2]); return '<div class="kKnob" role="slider" tabindex="0" data-fx="1" data-ci="-1" data-k="'+k+'" aria-label="'+d[1]+'" aria-valuemin="'+d[2]+'" aria-valuemax="'+d[3]+'" aria-valuenow="'+v+'" style="--kc:#b48cff;--a:'+Math.round(-135+270*f)+'deg"><div class="kd"></div><b>'+d[1]+'</b><i>'+fmt(v,d[6])+'</i></div>'; }
 function returns(){ const m=$('padMixer'); if(!m||$('kFXRet')) return; const r=document.createElement('div'); r.id='kFXRet'; r.innerHTML='<b>🎛 Returns</b>'+FXK.map(x=>fxKnob(x[0])).join('')+'<label style="font:700 12px system-ui;color:#cfd">Echo on the beat <select data-sync><option value="">free</option><option value="0.25">1/16</option><option value="0.5">1/8</option><option value="0.75" selected>3/16</option><option value="1">1/4</option><option value="1.5">3/8</option><option value="2">1/2</option></select></label><button type="button" data-flat data-noul>⟲ Flat EQ on all 40</button>';
  m.insertAdjacentElement('beforebegin',r);
  r.addEventListener('change',e=>{ const s=e.target.closest('[data-sync]'); if(!s||!s.value) return; let bpm=90; try{ bpm=PS().bpm(); }catch(_){ } const t=Math.min(1.5,(60/bpm)*(+s.value)); const el=r.querySelector('[data-k="dlTime"]'); if(el) setK(el,t); say('Echo locked to '+s.options[s.selectedIndex].text+' at '+bpm+' BPM.'); });
  r.addEventListener('click',e=>{ if(!e.target.closest('[data-flat]')) return; e.stopPropagation(); const X=MIX(); X.forEach(m=>{ ['trim','hi','mid','lo','rv','dl'].forEach(k=>m[k]=0); m.hpf=20; m.mf=1000; }); try{ PS().mixApply(); }catch(_){ } document.querySelectorAll('.kStrip').forEach(s=>s.remove()); strips(); paintKK(true); say('⟲ Every strip is flat again.'); }); }
 /* the karaoke's own 8-track mixer: the same tracks as the console */
 const KK8=[[23,'🎤 Mic 1 · lead'],[24,'🎤 Mic 2 · backup'],[25,'🎤 Mic 3 · ad-libs'],[26,'🎤 Mic 4 · harmony'],[27,'🎤 Mic 5 · hook'],[28,'🎧 DJ A'],[29,'🎧 DJ B'],[22,'🎶 Backing']];
 function paintKK(force){ const kk=$('kKara'); if(!kk||!kk.getClientRects().length) return; let box=$('kkMix'); if(box&&!force) return; const X=MIX();
  const html='<h4>🎚 Karaoke mixer · 8 tracks, the same as the studio console (tracks '+KK8.map(x=>x[0]+1).join(', ')+')</h4><div class="kmGrid">'+KK8.map(([ci,n])=>{ const m=X[ci]||{vol:.9}; return '<div class="kms" data-ci="'+ci+'"><small>'+(ci+1)+' · '+n+'</small><div class="kq">'+['hi','mid','lo','rv','dl','trim'].map(k=>knob(ci,k)).join('')+'</div><input type="range" min="0" max="150" value="'+Math.round((m.vol==null?.9:m.vol)*100)+'" data-kv aria-label="Level '+n+'"><div class="mb"><button type="button" class="m'+(m.mute?' on':'')+'" data-km="m" data-noul>M</button><button type="button" class="'+(m.solo?'on':'')+'" data-km="s" data-noul>S</button></div></div>'; }).join('')+'</div>';
  if(!box){ box=document.createElement('div'); box.id='kkMix'; const anchor=$('kkLayers')||kk.querySelector('.kkIn')||kk.firstElementChild; if(anchor&&anchor.parentNode) anchor.parentNode.insertBefore(box,anchor); else kk.appendChild(box);
   box.addEventListener('input',e=>{ const r=e.target.closest('[data-kv]'); if(!r) return; const ci=+r.closest('.kms').dataset.ci; const X=MIX(); while(X.length<=ci) X.push({vol:.9,pan:0,mute:false,solo:false}); X[ci].vol=+r.value/100; try{ PS().mixApply(); PS().renderMixer(); }catch(_){ } });
   box.addEventListener('click',e=>{ const b=e.target.closest('[data-km]'); if(!b) return; e.stopPropagation(); const ci=+b.closest('.kms').dataset.ci; const X=MIX(); while(X.length<=ci) X.push({vol:.9,pan:0,mute:false,solo:false}); if(b.dataset.km==='m') X[ci].mute=!X[ci].mute; else X[ci].solo=!X[ci].solo; try{ PS().mixApply(); PS().renderMixer(); }catch(_){ } paintKK(true); }); }
  box.innerHTML=html; }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')){ strips(); returns(); } paintKK(false); },700);
 window.KSTRIP={knobs:K,returns:FXK,set:(ci,k,v)=>{ const el=document.querySelector('.kKnob[data-ci="'+ci+'"][data-k="'+k+'"]'); if(el) setK(el,v); else { const X=MIX(); if(X[ci]){ X[ci][k]=v; try{ PS().mixApply(); }catch(_){ } } } }};
})();
