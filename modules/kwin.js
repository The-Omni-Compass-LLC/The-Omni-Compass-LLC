(()=>{ /* 🪟 THE FLOATING STUDIO (v263). Every device is its own window, all of them can be open at once, and each floats over the
   mixing board, which stays underneath, the way a virtual studio works:
     🥁 the 16-pad beat machine (MPC) · 🎹 the MIDI keyboard · 🎧 the Virtual DJ (two turntables, the mixer and crossfader in the
     middle) · 🎤 the Karaoke pad · 🎼 the Sequencer and editor (step grid, 40-track arranger, piano roll).
   • Drag any window by its title bar, size it from its corner, and click it to bring it to the front.
   • ▁ folds a window to its title bar (a tab), so the console underneath can be reached; the deck's window tabs do the same:
     a closed window opens, an open one folds out of the way, a folded one comes back. ⤢ Tidy lays every open window side by side;
     ▁ Fold all tucks them all away at once.
   • M and S on a device's title bar mute or solo that device's own strips on the mixing board (pads 1–17, keyboard 18, microphones
     24–28, decks 29–30), so the windows and the console are one instrument.
   • 🔗 L on a console strip links it: every linked strip moves, mutes and solos together (a fader group). */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const vis=el=>!!el&&!el.hidden&&el.getClientRects().length>0&&getComputedStyle(el).visibility!=='hidden'&&getComputedStyle(el).display!=='none';
 const btn=(root,re)=>[...((root&&root.querySelectorAll)?root.querySelectorAll('button'):[])].find(b=>re.test(b.textContent.replace(/\s+/g,' ').trim()));
 const clickBtn=(root,re)=>{ const b=btn(root,re); if(b){ b.click(); return true; } return false; };
 const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const rail=()=>parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58;
 const studioOn=()=>{ const p=$('pad'); return !!p&&p.classList.contains('on'); };
 const devOver=()=>document.body.classList.contains('kDevOver');
 const karaOn=()=>vis($('kKara'));
 const pin=()=>{ const pm=document.querySelector('#pad .pmain'); return pm&&pm.parentElement; };
 /* the device windows the rail already floats, and the console strips each one plays through */
 const KR={pads:()=>document.querySelector('#pad .pmain'),keys:()=>$('kbTop'),dj:()=>$('djSec')};
 const GROUPS={pads:Array.from({length:17},(_,i)=>i),keys:[17],kara:[23,24,25,26,27],dj:[28,29]};
 const NAMES={pads:'🥁 Pads',keys:'🎹 Keys',dj:'🎧 DJ',kara:'🎤 Karaoke',seq:'🎼 Sequencer'};
 const S={open:Object.assign({kara:false,seq:false},getLS('kanin-wins1',{})),seqTab:getLS('kanin-seqtab','steps')}; const sSave=()=>putLS('kanin-wins1',S.open);

 /* ================= the window frame ================= */
 const css=document.createElement('style'); css.textContent=`
.kWin{position:fixed;left:var(--wx,16px);top:var(--wy,70px);width:var(--ww,380px);height:var(--wh,auto);max-height:calc(100vh - 12px);max-width:calc(100vw - 12px);z-index:var(--wz,80);display:flex;flex-direction:column;box-sizing:border-box;background:rgba(7,10,28,.985);color:#eef3ff;border:1px solid #6fb8ff;border-radius:12px;box-shadow:0 12px 40px rgba(0,0,0,.65),0 0 18px rgba(111,184,255,.2);visibility:visible!important;pointer-events:auto!important;overflow:hidden;resize:both;min-width:250px;min-height:44px;font:600 13px system-ui,sans-serif}
.kWin[hidden]{display:none!important}
.kWin .kwHead{flex:0 0 auto;display:flex;align-items:center;gap:5px;padding:5px 6px 5px 10px;background:linear-gradient(90deg,#14204a,#0b1230);border-bottom:1px solid #2c3a78;cursor:move;touch-action:none;user-select:none;-webkit-user-select:none}
.kWin .kwHead b{flex:1;min-width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;font:800 14px system-ui,sans-serif;color:#ffe94a}
.kWin .kwHead button,.kFHead [data-kw]{min-width:36px;min-height:34px;padding:0 6px;border-radius:8px;font:900 13px system-ui,sans-serif}
.kFHead [data-kw].on,.kWin .kwHead [data-kw].on{background:#ffe94a!important;color:#14163a!important}
.kFHead [data-kw="m"].on,.kWin .kwHead [data-kw="m"].on{background:#ff5a5a!important;color:#fff!important}
.kWin .kwBody{flex:1 1 auto;min-height:0;overflow:auto;padding:8px}
.kWin.min{height:auto!important;resize:none}.kWin.min .kwBody{display:none}
.kWin .kwRow{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin:0 0 6px}
.kWin .kwRow b.lab{font:900 11px ui-monospace,monospace;letter-spacing:.08em;color:#8fb3ff;text-transform:uppercase;min-width:52px}
.kWin .kwRow button,.kWin .kwRow select{min-height:40px;border-radius:10px;padding:0 10px;font:800 13px system-ui,sans-serif}
.kWin .kwLcd{margin:0 0 8px;padding:8px 10px;border-radius:8px;background:#03070f;border:1px solid rgba(0,229,255,.35);font:700 15px/1.45 system-ui,sans-serif;color:#7ff;min-height:44px}
.kWin .kwLcd small{display:block;color:#7f8aa8;font:600 12.5px system-ui,sans-serif}
.kWin .kwTabs{display:flex;flex-wrap:wrap;gap:4px;margin:0 0 8px;position:sticky;top:-8px;z-index:2;background:rgba(7,10,28,.985);padding:4px 0}
.kWin .kwTabs button{min-height:36px;border-radius:999px;padding:0 12px;font:800 12.5px system-ui,sans-serif}
.kWin .kwTabs button.on{background:#ffe94a;color:#14163a}
#kWin_seq[data-show="steps"] :is(#k40Seq,#rollWrap),#kWin_seq[data-show="t40"] :is(#crSec,#rollWrap),#kWin_seq[data-show="roll"] :is(#crSec,#k40Seq){display:none!important}
#kWin_seq #kSeqTabs{display:none!important}
#kWin_seq #crSec,#kWin_seq #k40Seq,#kWin_seq #rollWrap{max-width:none!important;margin:0!important}
/* the Virtual DJ, wide: deck A, the mixer and crossfader in the middle, deck B */
#djSec.kdjWide #djWrap{display:grid!important;grid-template-columns:minmax(0,1fr) minmax(176px,220px) minmax(0,1fr)!important;align-items:start!important;gap:10px!important}
#djSec.kdjWide #djWrap>*{min-width:0!important;width:auto!important;max-width:none!important;flex:none!important}
#djSec.kdjWide #djWrap canvas[id$="Plat"]{width:min(100%,240px)!important;height:auto!important;aspect-ratio:1;display:block;margin:0 auto}
#djSec.kdjWide #djWrap canvas.wave{width:100%!important}
#djSec.kdjWide #djWrap .kgrid{grid-template-columns:repeat(auto-fit,minmax(110px,1fr))!important}
/* 🔗 L on each console strip */
#padMixer .mxb [data-a="link"]{min-width:22px}
#padMixer .mxb [data-a="link"].on{background:#6fb8ff!important;color:#06102a!important}
#padMixer .mxs.kLinked{box-shadow:inset 0 0 0 2px #6fb8ff}`; document.head.appendChild(css);
 const W={};
 function mk(key,title,group){ const el=document.createElement('div'); el.className='kWin'; el.id='kWin_'+key; el.hidden=true; el.setAttribute('role','dialog'); el.setAttribute('aria-label',title.replace(/^\S+ /,''));
  el.innerHTML='<div class="kwHead" title="Drag to move; drag the bottom-right corner to size"><b></b>'+(group?'<button type="button" data-kw="m" data-noul title="Mute this device’s strips on the mixing board">M</button><button type="button" data-kw="s" data-noul title="Solo this device’s strips">S</button>':'')+'<button type="button" data-kw="min" data-noul aria-label="Fold to a tab" title="Fold to a tab">▁</button><button type="button" data-kw="x" data-noul aria-label="Close" title="Close">✕</button></div><div class="kwBody"></div>';
  el.querySelector('.kwHead b').textContent=title; W[key]={el,title,group,built:false};
  const hd=el.querySelector('.kwHead'); let dg=null;
  hd.addEventListener('pointerdown',e=>{ if(e.target.closest('button')) return; const r=el.getBoundingClientRect(); dg={dx:e.clientX-r.left,dy:e.clientY-r.top}; try{ hd.setPointerCapture(e.pointerId); }catch(_){ } e.preventDefault(); });
  hd.addEventListener('pointermove',e=>{ if(!dg) return; const x=Math.max(0,Math.min(innerWidth-rail()-80,e.clientX-dg.dx)), y=Math.max(0,Math.min(innerHeight-44,e.clientY-dg.dy)); el.style.setProperty('--wx',x+'px'); el.style.setProperty('--wy',y+'px'); });
  const end=()=>{ if(dg){ dg=null; geoSave(key); } }; hd.addEventListener('pointerup',end); hd.addEventListener('pointercancel',end);
  try{ new ResizeObserver(()=>{ if(!el.hidden&&!el.classList.contains('min')){ clearTimeout(el.__rs); el.__rs=setTimeout(()=>geoSave(key),400); } }).observe(el); }catch(_){ }
  hd.addEventListener('click',e=>{ const b=e.target.closest('[data-kw]'); if(!b) return; e.stopPropagation(); const k=b.dataset.kw; if(k==='min'){ fold(key,!el.classList.contains('min')); } else if(k==='x') close(key); else grpSet(key,k); });
  return el; }
 function geoSave(key){ const el=W[key]&&W[key].el; if(!el||el.hidden) return; const r=el.getBoundingClientRect(); if(r.width<200) return; putLS('kanin-win-'+key,{x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:el.classList.contains('min')?null:Math.round(r.height)}); }
 function geo(key){ const Wd=innerWidth-rail()-16, H=innerHeight; const g=getLS('kanin-win-'+key,null); const phone=innerWidth<=760;
  if(g&&g.w>=240&&g.x>=0&&g.x<Wd-40&&g.y>=0&&g.y<H-40) return {x:g.x,y:g.y,w:Math.min(g.w,Wd),h:g.h&&g.h>=120?Math.min(g.h,H-16):null};
  if(phone) return {x:4,y:key==='seq'?40:Math.round(H*.3),w:Wd,h:key==='seq'?Math.round(H*.6):null};
  return key==='seq'?{x:16,y:64,w:Math.min(1000,Wd-16),h:Math.min(580,H-150)}:{x:Math.max(8,Wd-376),y:70,w:368,h:null}; }
 function place(key){ const el=W[key].el, g=geo(key); el.style.setProperty('--wx',g.x+'px'); el.style.setProperty('--wy',g.y+'px'); el.style.setProperty('--ww',g.w+'px'); if(g.h) el.style.setProperty('--wh',g.h+'px'); else el.style.removeProperty('--wh'); }
 /* one stacking order for every floating window: the one touched last is on top */
 const zOf=el=>parseInt(getComputedStyle(el).zIndex)||0;
 function front(el){ const pr=el.parentElement; let m=0; document.querySelectorAll('.kFloat.kFOn,.kWin:not([hidden])').forEach(x=>{ if(x!==el&&x.parentElement===pr) m=Math.max(m,zOf(x)); });
  m=Math.max(m,pr===document.body?8700:72); /* never under the studio's own bars (the floating windows' base layer is 70) */ if(el.classList.contains('kWin')) el.style.setProperty('--wz',String(m+1)); else el.style.setProperty('--fz',String(m+1)); }
 document.addEventListener('pointerdown',e=>{ const f=e.target.closest&&e.target.closest('.kFloat.kFOn,.kWin'); if(f) setTimeout(()=>front(f),0); },true);
 /* where a window lives: inside the studio with the other devices (so they share one stacking order), or over the Karaoke page */
 function home(key){ const el=W[key].el; const p=pin(); const want=(studioOn()||devOver())&&p?p:document.body; if(el.parentElement!==want){ want.appendChild(el); front(el); } }
 function allowed(key){ if(key==='seq') return studioOn(); return studioOn()||karaOn(); }
 function open(key){ const w=W[key]; if(!w) return; build(key); S.open[key]=true; sSave(); home(key); w.el.hidden=!allowed(key); w.el.classList.remove('min'); place(key); front(w.el); if(key==='seq') seqShow(S.seqTab); paint(key); }
 function close(key){ const w=W[key]; if(!w) return; S.open[key]=false; sSave(); w.el.hidden=true; if(key==='seq') putBack(); }
 function fold(key,v){ if(KR[key]){ const el=KR[key](); if(el){ el.classList.toggle('kMin',v); if(!v) front(el); } return; } const w=W[key]; if(!w) return; w.el.classList.toggle('min',v); if(!v) front(w.el); geoSave(key); }

 /* ================= 🎤 the Karaoke pad ================= */
 const kara=()=>$('kKara');
 const K={ /* each action: on the Karaoke page when it is open, on the studio's own beat, prompter and vocal booth otherwise */
  rew:()=>karaOn()?clickBtn(kara(),/^⏮$/):press('ktRew'), play:()=>karaOn()?clickBtn(kara(),/^▶ Play$/):(PS()&&!PS().playing?press('padPlay'):true),
  pause:()=>karaOn()?clickBtn(kara(),/^⏸ Pause$/):press('padStop'), stop:()=>karaOn()?clickBtn(kara(),/^■ Stop$/):press('padStop'), next:()=>karaOn()?clickBtn(kara(),/^⏭ Next song/):openKara(),
  take:()=>karaOn()?clickBtn(kara(),/^🎙 Record live/):press('vocRec'), auto:()=>karaOn()?clickBtn(kara(),/Auto-record$/):press('vocRec'),
  punch:()=>{ try{ KDECK.PU.on=true; KDECK.vocalPunch(); }catch(_){ say('Open the 🎛 Studio first.'); } },
  undo:()=>karaOn()?clickBtn(kara(),/^↶ Undo last take/):(()=>{ try{ KUNDO.any(); }catch(_){ } })(),
  layers:()=>clickBtn(kara(),/^▶ Play the layers$/)||say('Layers are on the 🎤 Karaoke page: open it with 🎤 Open karaoke.'), lstop:()=>clickBtn(kara(),/^■ Stop the layers/), layer:()=>clickBtn(kara(),/^⏺ Record a new/)||say('Open the 🎤 Karaoke page to record layers.'), bounce:()=>clickBtn(kara(),/^🧲 Bounce/),
  prompt:()=>{ if(press('tpFullGo')) return; say('The full-screen prompter is in the 🎛 Studio.'); }, read:()=>press('tpSay'),
  lyrics:()=>{ const ta=karaOn()?kara().querySelector('textarea'):($('tpText')||$('padLyr')); if(ta){ ta.scrollIntoView({behavior:'smooth',block:'center'}); ta.focus(); say('✍ Write or paste the lyrics, one line per bar.'); } },
  open:()=>openKara() };
 function openKara(){ try{ KKARA.open(); }catch(_){ say('Karaoke is still loading.'); } }
 const mirror=(src,id,label)=>{ const o=$(src); if(!o||o.options.length<5) return ''; return '<label class="lab" style="display:flex;align-items:center;gap:6px"><b class="lab">'+label+'</b><select data-mirror="'+src+'" data-die="off" aria-label="'+label+'">'+[...o.options].map(x=>'<option value="'+x.value+'"'+(x.selected?' selected':'')+'>'+x.text.replace(/[<>&]/g,'')+'</option>').join('')+'</select></label>'; };
 function karaBody(){ const kOn=karaOn();
  return '<div class="kwLcd" data-k="lcd">🎤 Ready to sing.<small>Lines light here on their bar.</small></div>'+
   '<div class="kwRow"><b class="lab">Song</b><button type="button" data-ka="rew" title="Back to the start">⏮</button><button type="button" data-ka="play" title="Play">▶</button><button type="button" data-ka="pause" title="Pause">⏸</button><button type="button" data-ka="stop" title="Stop">■</button><button type="button" data-ka="next" title="'+(kOn?'Next song':'Open the karaoke page')+'">⏭</button></div>'+
   '<div class="kwRow"><b class="lab">Mic</b><button type="button" data-ka="take">🎙 Record a take</button><button type="button" data-ka="punch" title="Drop in at the deck’s In bar, out after its Out bar">✂ Punch take</button><button type="button" data-ka="undo">↶ Undo take</button>'+(kOn?'<button type="button" data-ka="auto">⏺ Auto-record</button>':'')+'</div>'+
   '<div class="kwRow">'+(kOn?mirror('kkBars','','Length')+mirror('kkLive','','Voice'):mirror('vocBars','','Length')+mirror('robVoice','','Robot'))+'</div>'+
   '<div class="kwRow"><b class="lab">Lyrics</b><button type="button" data-ka="lyrics">✍ Write</button><button type="button" data-ka="prompt">⛶ Prompter</button><button type="button" data-ka="read">🗣 Read lines</button></div>'+
   (kOn?'<div class="kwRow"><b class="lab">Layers</b><button type="button" data-ka="layers">▶ Play</button><button type="button" data-ka="lstop">■ Stop</button><button type="button" data-ka="layer">⏺ New layer</button><button type="button" data-ka="bounce">🧲 Bounce</button></div>':'<div class="kwRow"><button type="button" data-ka="open">🎤 Open the karaoke page</button></div>'); }
 function karaLcd(){ const el=W.kara&&W.kara.el.querySelector('[data-k="lcd"]'); if(!el||W.kara.el.hidden) return; let a='',b='';
  if(karaOn()){ const m=[...kara().querySelectorAll('audio,video')].find(x=>!x.paused); const on=kara().querySelector('.tpLine.on,.kkLine.on,.on[data-line]'); a=on?on.textContent.trim():(m?'▶ '+t(m.currentTime)+' / '+t(m.duration||0):'🎤 Karaoke ready. ▶ plays the song.'); b=m?'Singing over the song':'Press ▶, then 🎙 Record a take'; }
  else { const on=document.querySelector('#tpView .tpLine.on'); const nx=on&&on.nextElementSibling; a=on?on.textContent.trim():'🎤 Sing over the studio beat.'; b=nx?'next: '+nx.textContent.trim():(PS()&&PS().playing?'The beat is playing':'▶ plays the beat; lines from the prompter light here'); }
  const h=escH(a)+'<small>'+escH(b)+'</small>'; if(el.__h!==h){ el.__h=h; el.innerHTML=h; } }
 const escH=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])).slice(0,160);
 const t=x=>{ x=Math.max(0,+x||0); return Math.floor(x/60)+':'+String(Math.floor(x%60)).padStart(2,'0'); };

 /* ================= 🎼 the Sequencer and editor: the studio's own step grid, 40-track arranger and piano roll, floating ================= */
 const SEQN=['kSeqTabs','crSec','k40Seq','rollWrap']; const PH={};
 function seqBody(){ return '<div class="kwTabs" role="tablist"><button type="button" data-st="steps" role="tab">🥁 Step grid</button><button type="button" data-st="t40" role="tab">🎚 40-track arranger</button><button type="button" data-st="roll" role="tab">🎹 Piano roll</button></div><div class="kwHost"></div>'; }
 function pull(){ const host=W.seq.el.querySelector('.kwHost'); if(!host) return; SEQN.forEach(id=>{ const n=$(id); if(!n||host.contains(n)) return; if(!PH[id]){ PH[id]=document.createComment('kwin:'+id); } if(!PH[id].parentNode) n.parentNode.insertBefore(PH[id],n); host.appendChild(n); }); }
 function putBack(){ SEQN.forEach(id=>{ const n=$(id), p=PH[id]; if(n&&p&&p.parentNode){ p.parentNode.insertBefore(n,p); p.remove(); } }); }
 function seqShow(tab){ const w=W.seq; if(!w) return; pull(); S.seqTab=tab; putLS('kanin-seqtab',tab); w.el.dataset.show=tab; w.el.querySelectorAll('[data-st]').forEach(b=>{ b.classList.toggle('on',b.dataset.st===tab); b.setAttribute('aria-selected',String(b.dataset.st===tab)); });
  const tb=$('kSeqTabs'); if(tb&&tab!=='roll'){ const b=tb.querySelector('[data-tab="'+(tab==='t40'?'40':'beat')+'"]'); if(b) b.click(); }
  try{ if(tab==='t40') SEQ.renderSq&&SEQ.renderSq(); }catch(_){ } }

 function build(key){ const w=W[key]; if(!w) return; const body=w.el.querySelector('.kwBody'); if(key==='kara'){ body.innerHTML=karaBody(); w.sig=karaOn(); }
  if(key==='seq'&&!w.built){ body.innerHTML=seqBody(); w.built=true; } }
 mk('kara','🎤 Karaoke pad',true); mk('seq','🎼 Sequencer & editor',false);
 W.kara.el.addEventListener('click',e=>{ const b=e.target.closest('[data-ka]'); if(!b) return; e.stopPropagation(); const f=K[b.dataset.ka]; if(f) f(); setTimeout(karaLcd,150); });
 W.kara.el.addEventListener('change',e=>{ const s=e.target.closest('[data-mirror]'); if(!s) return; e.stopPropagation(); const o=$(s.dataset.mirror); if(o){ o.value=s.value; o.dispatchEvent(new Event('change',{bubbles:true})); } });
 W.seq.el.addEventListener('click',e=>{ const b=e.target.closest('[data-st]'); if(!b) return; e.stopPropagation(); seqShow(b.dataset.st); });

 /* ================= M and S: each device and its own strips on the console ================= */
 function grpState(g){ const M=PS()&&PS().MIX; const ci=GROUPS[g]; if(!M||!ci) return {m:false,s:false}; const c=ci.filter(i=>M[i]); return {m:!!c.length&&c.every(i=>M[i].mute),s:!!c.length&&c.every(i=>M[i].solo)}; }
 function nudgeConsole(){ const f=document.querySelector('#padMixer .mxs input.mxv'); if(!f) return; window.__kdMotor=true; try{ f.dispatchEvent(new Event('input',{bubbles:true})); }finally{ window.__kdMotor=false; } }
 function grpSet(g,k){ const P=PS(); if(!P||!GROUPS[g]) return; const M=P.MIX; const st=grpState(g); const v=!(k==='m'?st.m:st.s); GROUPS[g].forEach(i=>{ while(M.length<=i) M.push({vol:.9,pan:0,mute:false,solo:false}); M[i][k==='m'?'mute':'solo']=v; });
  try{ P.mixApply(); }catch(_){ } try{ P.renderMixer(); }catch(_){ } nudgeConsole(); paintHeads(); const n=NAMES[g]||g; say((k==='m'?(v?'🔇 '+n+' muted':'🔊 '+n+' back in the mix'):(v?'🎯 '+n+' soloed: only it plays':'🎯 '+n+' solo off'))+' (mixing board strips '+GROUPS[g].map(i=>i+1).join(', ').replace(/^(\d+), .*, (\d+)$/,'$1–$2')+').'); }
 function paintHeads(){ Object.keys(KR).forEach(k=>{ const el=KR[k](); const hd=el&&el.querySelector(':scope > .kFHead'); if(!hd) return; if(!hd.querySelector('[data-kw="m"]')){ const mb=hd.querySelector('[data-fh="min"]'); const m=document.createElement('button'); m.type='button'; m.dataset.kw='m'; m.setAttribute('data-noul',''); m.textContent='M'; m.title='Mute this device’s strips on the mixing board'; const s=m.cloneNode(); s.dataset.kw='s'; s.textContent='S'; s.title='Solo this device’s strips'; hd.insertBefore(m,mb); hd.insertBefore(s,mb); }
   const st=grpState(k); hd.querySelector('[data-kw="m"]').classList.toggle('on',st.m); hd.querySelector('[data-kw="s"]').classList.toggle('on',st.s); });
  const st=grpState('kara'); const hd=W.kara.el.querySelector('.kwHead'); hd.querySelector('[data-kw="m"]').classList.toggle('on',st.m); hd.querySelector('[data-kw="s"]').classList.toggle('on',st.s); }
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('.kFHead [data-kw]'); if(!b) return; e.preventDefault(); e.stopImmediatePropagation(); const f=b.closest('.kFloat'); const k=Object.keys(KR).find(x=>KR[x]()===f); if(k) grpSet(k,b.dataset.kw); },true);

 /* ================= 🔗 linked strips: a fader group ================= */
 const LINK=new Set(getLS('kanin-link1',[])); const lSave=()=>putLS('kanin-link1',[...LINK]);
 function linkStrips(){ const mx=$('padMixer'); if(!mx) return; mx.querySelectorAll('.mxs').forEach(s=>{ const ci=+s.dataset.c; if(isNaN(ci)||s.classList.contains('master')) return; const mb=s.querySelector('.mxb'); if(!mb) return; let a=mb.querySelector('[data-a="link"]'); if(!a){ a=document.createElement('button'); a.type='button'; a.dataset.a='link'; a.textContent='L'; a.setAttribute('data-noul',''); mb.appendChild(a); }
  const on=LINK.has(ci); a.classList.toggle('on',on); a.title=on?'🔗 Linked: moves, mutes and solos with every L strip. Press to unlink.':'🔗 Link this strip to the fader group'; s.classList.toggle('kLinked',on); }); }
 document.addEventListener('click',e=>{ const a=e.target.closest&&e.target.closest('#padMixer .mxb [data-a="link"]'); if(a){ e.preventDefault(); e.stopImmediatePropagation(); const ci=+a.closest('.mxs').dataset.c; if(LINK.has(ci)) LINK.delete(ci); else LINK.add(ci); lSave(); linkStrips(); say(LINK.has(ci)?'🔗 Strip '+(ci+1)+' is linked ('+LINK.size+' in the group): moving one moves them all.':'Strip '+(ci+1)+' is unlinked.'); return; }
  const ms=e.target.closest&&e.target.closest('#padMixer .mxb [data-a="m"],#padMixer .mxb [data-a="s"]'); if(!ms) return; const ci=+ms.closest('.mxs').dataset.c; if(!LINK.has(ci)||LINK.size<2) return; const k=ms.dataset.a==='m'?'mute':'solo';
  setTimeout(()=>{ const P=PS(); const M=P.MIX; const v=!!(M[ci]&&M[ci][k]); LINK.forEach(j=>{ if(M[j]) M[j][k]=v; }); try{ P.mixApply(); P.renderMixer(); }catch(_){ } },0); },true);
 document.addEventListener('input',e=>{ const t=e.target; if(window.__kdMotor||window.__kwLink||!t.matches||!t.matches('#padMixer .mxs input.mxv,#padMixer .mxs input.mxp')) return; const s=t.closest('.mxs'); const ci=+s.dataset.c; if(!LINK.has(ci)||LINK.size<2) return; const P=PS(); const M=P.MIX; if(!M[ci]) return;
  const vol=t.classList.contains('mxv'); const now=+t.value/100, was=vol?M[ci].vol:M[ci].pan; const d=now-was; if(!d) return;
  window.__kwLink=true; try{ LINK.forEach(j=>{ if(j===ci||!M[j]) return; const lo=vol?0:-1, hi=vol?1.5:1; const v=Math.max(lo,Math.min(hi,(vol?M[j].vol:M[j].pan)+d)); if(vol) M[j].vol=v; else M[j].pan=v; const st=document.querySelector('#padMixer .mxs[data-c="'+j+'"]'); if(st){ const f=st.querySelector(vol?'input.mxv':'input.mxp'); if(f) f.value=String(Math.round(v*100)); if(!vol){ const kn=st.querySelector('.knb'); if(kn) kn.style.setProperty('--rot',(v*135)+'deg'); } } }); setTimeout(()=>{ try{ P.mixApply(); }catch(_){ } },0); }finally{ window.__kwLink=false; } },true);

 /* ================= the window tabs the deck shows, and Tidy / Fold all ================= */
 function state(k){ if(KR[k]){ const el=KR[k](); const o=!!(F()&&F().isOpen(k))&&(studioOn()||devOver()); if(!o) return 'closed'; return el&&el.classList.contains('kMin')?'folded':'open'; }
  if(k==='console') return 'closed'; const w=W[k]; if(!w||!S.open[k]||w.el.hidden) return 'closed'; return w.el.classList.contains('min')?'folded':'open'; }
 function openAny(k){ if(KR[k]){ if(karaOn()&&!studioOn()){ const re={pads:/^🥁 Pads$/,keys:/^🎹 Keys$/,dj:/^🎧 DJ decks$/}[k]; if(!clickBtn(kara(),re)) say('Open the 🎛 Studio first.'); return; } if(!studioOn()){ try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ try{ F().open(k); }catch(_){ } },700); return; } try{ F().open(k); }catch(_){ } return; }
  if(k==='seq'&&!studioOn()){ if(karaOn()&&clickBtn(kara(),/^🎼 Tracks$/)) return; try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>open('seq'),800); return; }
  open(k); }
 function tab(k){ if(k==='console') return consoleView(); if(k==='tidy') return tidy(); if(k==='foldall') return foldAll(); const st=state(k);
  if(st==='closed'){ openAny(k); say(NAMES[k]+' is open. Its tab folds it out of the way and brings it back.'); } else if(st==='open'){ fold(k,true); say(NAMES[k]+' is folded to its tab: the mixing board underneath is free. The tab brings it back.'); } else fold(k,false); }
 function consoleView(){ if(karaOn()&&!studioOn()){ if(!clickBtn(kara(),/^🎚 Mixing board$/)) say('Open the 🎛 Studio for the mixing board.'); return; } if(!studioOn()){ try{ KRAIL.goTo('pad'); }catch(_){ } } setTimeout(()=>{ const m=$('padMixer'); if(m) m.scrollIntoView({behavior:'smooth',block:'start'}); say('🎚 The mixing board is underneath. Fold a window with ▁ or its tab to reach a strip; the tab brings it back.'); },studioOn()?0:800); }
 const openList=()=>['pads','keys','dj','kara','seq'].filter(k=>state(k)!=='closed');
 function foldAll(){ const L=openList(); if(!L.length) return say('No window is open.'); const any=L.some(k=>state(k)==='open'); L.forEach(k=>fold(k,any)); say(any?'▁ Every window is folded to its tab. The console is free.':'Every window is back.'); }
 function tidy(){ const L=openList(); if(!L.length) return say('Open a window first: 🥁 🎹 🎧 🎤 🎼.'); L.forEach(k=>fold(k,false));
  /* the windows share the band under the studio's transport bar (the beat machine keeps to that band), down to the bottom; the deck folds to its tab */
  const bb=$('bbBar'); const top=(studioOn()&&innerWidth>760&&bb&&bb.getClientRects().length)?Math.max(8,Math.round(bb.getBoundingClientRect().bottom)+4):8; const x0=8, y0=Math.min(top,Math.round(innerHeight*.45)), x1=innerWidth-rail()-8, y1=innerHeight-8;
  try{ if(L.length>=3&&window.KDECK&&!document.getElementById('kDeck').classList.contains('min')) KDECK.act('fold'); }catch(_){ }
  const n=L.length, rowsN=innerWidth<=760?n:(n<=3?1:2); const per=[]; for(let r=0;r<rowsN;r++) per.push(Math.ceil((n-per.reduce((a,b)=>a+b,0))/(rowsN-r)));
  const ch=Math.max(150,(y1-y0-(rowsN-1)*8)/rowsN); let i0=0; const cells=[]; per.forEach((m,r)=>{ const cw=(x1-x0-(m-1)*8)/m; for(let c=0;c<m;c++) cells.push({x:x0+c*(cw+8),y:y0+r*(ch+8),w:cw,h:ch}); i0+=m; });
  L.forEach((k,i)=>{ const C=cells[i]; const x=Math.round(C.x), y=Math.round(C.y), w=Math.round(C.w), h=Math.round(C.h);
   if(KR[k]){ const el=KR[k](); if(!el) return; el.style.setProperty('--fx',x+'px'); el.style.setProperty('--fy',y+'px'); el.style.setProperty('--fw',w+'px'); el.style.setProperty('--fh',h+'px'); el.style.setProperty('--fmh',h+'px'); el.style.setProperty('height',h+'px','important'); el.style.setProperty('max-height',h+'px','important'); el.dataset.kwTidy='1'; }
   else { const el=W[k].el; el.style.setProperty('--wx',x+'px'); el.style.setProperty('--wy',y+'px'); el.style.setProperty('--ww',w+'px'); el.style.setProperty('--wh',h+'px'); geoSave(k); } });
  say('⤢ '+n+' window'+(n>1?'s':'')+' side by side. Drag any title bar to move it; ▁ folds it.'); }
 function rowHTML(cx){ const L=[['pads','🥁','Pads'],['keys','🎹','Keys'],['dj','🎧','DJ'],['kara','🎤','Karaoke'],['seq','🎼','Sequencer']];
  return L.map(([k,i,n])=>{ const st=state(k); return '<button type="button" data-w="'+k+'" class="kdW '+(st==='open'?'on':st==='folded'?'fold':'')+'" aria-pressed="'+(st!=='closed')+'" title="'+n+': '+(st==='closed'?'open it':st==='open'?'fold it to its tab':'bring it back')+'">'+i+' '+n+(st==='folded'?' ▴':'')+'</button>'; }).join('')+
   '<button type="button" data-w="console" title="The mixing board underneath">🎚 Console</button><button type="button" data-w="tidy" title="Lay every open window side by side">⤢ Tidy</button><button type="button" data-w="foldall" title="Fold every window to its tab, or bring them all back">▁ Fold all</button>'; }
 const sig=()=>['pads','keys','dj','kara','seq'].map(state).join(',');

 /* ================= keep everything in step ================= */
 let djWas=false;
 setInterval(()=>{ ['kara','seq'].forEach(k=>{ const w=W[k]; if(!S.open[k]){ if(!w.el.hidden) w.el.hidden=true; return; } home(k); const ok=allowed(k); if(ok){ if(k==='kara'&&w.sig!==karaOn()) build('kara'); if(k==='seq'&&w.built) pull(); } w.el.hidden=!ok; if(!ok&&k==='seq') putBack(); });
  Object.keys(KR).forEach(k=>{ const el=KR[k](); if(el&&el.dataset.kwTidy&&!(F()&&F().isOpen(k))){ el.style.removeProperty('height'); el.style.removeProperty('max-height'); delete el.dataset.kwTidy; } });
  paintHeads(); linkStrips(); karaLcd();
  const dj=$('djSec'); const djOn=!!(dj&&F()&&F().isOpen('dj')); if(djOn&&!djWas&&innerWidth>=1100){ const r=dj.getBoundingClientRect(); if(r.width<=780){ const w=Math.min(1120,innerWidth-rail()-24); dj.style.setProperty('--fw',w+'px'); dj.style.setProperty('--fx',Math.max(8,Math.min(r.left,innerWidth-rail()-w-8))+'px'); } } djWas=djOn;
  if(dj) dj.classList.toggle('kdjWide',djOn&&dj.getBoundingClientRect().width>=820); },500);
 function paint(){ }
 window.KWIN={open,close,fold,tab,state,rowHTML,sig,tidy,foldAll,grpSet,grpState,GROUPS,LINK,get wins(){ return W; },seqShow,openAny};
})();
