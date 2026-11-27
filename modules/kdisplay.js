(()=>{ /* 🖥 THE SCREEN ON TOP OF EACH DEVICE (v241), laid out the way the hardware is:
   🥁 the beat machine like an MPC: a backlit screen (program/kit, bank, tempo, BAR · BEAT · TICK, record state, loop length,
      quantize, latch, note repeat, the selected pad and its hits in the loop), and under it the function buttons:
      ◀ KIT ▶ · PAD BANK A B C D · 🗂 SOUNDS · ⬆ UPLOAD · 🔒 LATCH · 🔁 NOTE REPEAT · 🔄 LOOP 1/2/4/8 · 🧲 Q · 👆 TAP TEMPO.
   🎹 the keyboard like a workstation (Korg Triton, Yamaha Motif): a screen (PROG number and name, octave, tempo, position, record
      state, the keys track and the last note) and ◀ PROG ▶ · OCT − + · 🗂 SOUNDS · ⬆ UPLOAD · 🔒 LATCH · 🎼 ARP · 🔄 LOOP · 🧲 Q · 👆 TAP.
   🗂 SOUNDS opens a drawer in the device: every kit, every library group onto the 16 pads, any instrument onto the pads, any sound
   onto the keys, your own uploads and the microphone. Recording is real time (as played, every tick) unless 🧲 Q is on; REC over
   a playing loop adds to it (overdub). */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const PS=()=>window.PADSTUDIO; const NN=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
 const nm=m=>NN[((m%12)+12)%12]+(Math.floor(m/12)-1);
 const fire=(el,ev)=>{ if(el) el.dispatchEvent(new Event(ev||'change',{bubbles:true})); };
 const step=(sel,d,skip)=>{ const s=$(sel)||document.querySelector(sel); if(!s||!s.options||!s.options.length) return null; let i=s.selectedIndex; for(let n=0;n<s.options.length;n++){ i=(i+d+s.options.length)%s.options.length; if(!skip||!skip(s.options[i])) break; } s.selectedIndex=i; fire(s,'input'); fire(s); return s.options[i].text; };
 const css=document.createElement('style'); css.textContent=`
.kScr{margin:0 0 6px;padding:7px;border-radius:12px;background:linear-gradient(180deg,#2b2e36,#16181d);border:1px solid #444a58;box-shadow:inset 0 1px 0 rgba(255,255,255,.08)}
.kLcd{border-radius:7px;padding:6px 9px;font:700 12.5px/1.45 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;letter-spacing:.02em;text-transform:uppercase;white-space:pre;overflow:hidden;border:2px solid #0b0c10;box-shadow:inset 0 0 14px rgba(0,0,0,.35)}
.kScr.mpc .kLcd{background:linear-gradient(180deg,#c6d6a6,#a9bd87);color:#1b2410}
.kScr.wks .kLcd{background:linear-gradient(180deg,#bcd3ee,#9db9dc);color:#0d1b33}
.kLcd .r{display:flex;justify-content:space-between;gap:8px}
.kLcd .r span{overflow:hidden;text-overflow:clip}
.kLcd b.on{background:#1b2410;color:#c6d6a6;padding:0 3px;border-radius:2px}
.kScr.wks .kLcd b.on{background:#0d1b33;color:#bcd3ee}
.kLcd b.rec{background:#b3172f;color:#fff;padding:0 3px;border-radius:2px;animation:kScrRec 1s steps(2) infinite}
@keyframes kScrRec{50%{opacity:.35}}
.kSoft{display:grid;grid-template-columns:repeat(auto-fill,minmax(58px,1fr));gap:4px;margin-top:6px}
.kSoft button span{font-size:15px;line-height:1}
.kSoft button{display:flex!important;flex-direction:column;align-items:center;justify-content:center;gap:1px;min-height:44px!important;padding:2px 2px!important;border-radius:8px!important;font:900 10px/1.05 system-ui,sans-serif!important;word-break:keep-all!important;overflow-wrap:normal!important;letter-spacing:.02em;color:#e9ecf5!important;background:linear-gradient(180deg,#4a4f5e,#30343f)!important;border:1px solid #20232b!important;box-shadow:0 2px 0 #0d0e12;white-space:nowrap;overflow:hidden}
.kSoft button:active{transform:translateY(1px);box-shadow:none}
.kSoft button.on{background:linear-gradient(180deg,#ffe94a,#e0c400)!important;color:#14163a!important}
.kSoft button.bank{background:linear-gradient(180deg,#5b3bd6,#3a2399)!important}.kSoft button.bank.on{background:linear-gradient(180deg,#ffe94a,#e0c400)!important;color:#14163a!important}
.kDrawer{margin-top:6px;padding:8px;border-radius:10px;background:#11131a;border:1px solid #3a3f4d;display:grid;gap:6px}
.kDrawer[hidden]{display:none!important}
.kDrawer label{display:flex;flex-direction:column;gap:3px;font:800 10.5px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.06em;text-transform:uppercase}
.kDrawer select{min-height:38px;border-radius:8px;font:700 13px system-ui,sans-serif;width:100%;box-sizing:border-box}
.kDrawer .dRow{display:flex;flex-wrap:wrap;gap:6px}
.kDrawer .dRow button{flex:1 1 140px;min-height:40px!important;border-radius:10px!important;font:800 12.5px system-ui,sans-serif!important}
@media (max-width:760px),(max-height:700px){ .kScr{padding:5px;margin-bottom:4px} .kLcd{font-size:10.5px;line-height:1.35;padding:4px 7px} .kLcd .r:nth-child(n+3){display:none}
 .kSoft{display:flex!important;flex-wrap:nowrap;overflow-x:auto;gap:4px;margin-top:4px;-webkit-overflow-scrolling:touch;scrollbar-width:none} .kSoft::-webkit-scrollbar{display:none}
 .kSoft button{flex:0 0 56px;min-height:38px!important;font-size:9.5px!important} .kSoft button span{font-size:13px}
 .kDevTx{grid-template-columns:repeat(7,minmax(0,1fr))!important;gap:3px!important} .kDevTx button{min-height:44px!important;font-size:8.5px!important;padding:1px!important} .kDevTx button span{font-size:15px!important}
 #kbDash .kDevTx{grid-template-columns:repeat(8,minmax(0,1fr))!important} }`; document.head.appendChild(css);
 /* ---------- shared actions ---------- */
 let taps=[];
 function tap(){ const now=performance.now(); taps=taps.filter(t=>now-t<2500); taps.push(now); if(taps.length<2) return say('👆 Keep tapping in time…'); const iv=[]; for(let i=1;i<taps.length;i++) iv.push(taps[i]-taps[i-1]); const avg=iv.reduce((a,b)=>a+b,0)/iv.length; const bpm=Math.max(40,Math.min(240,Math.round(60000/avg))); const b=$('padBpm'); if(b){ b.value=String(bpm); fire(b,'input'); fire(b); } say('👆 Tempo '+bpm+' BPM'); }
 const LOOPS=[1,2,4,8];
 function loop(){ const ps=PS(); if(!ps) return; const cur=ps.barsN||1; const nx=LOOPS[(LOOPS.indexOf(cur)+1)%LOOPS.length]||1; let ok=false; const btn=document.querySelector('#mpcBar [data-m="bars"][data-v="'+nx+'"]'); if(btn){ btn.click(); ok=(ps.barsN===nx); } if(!ok){ try{ ps.setBars(nx); ok=true; }catch(_){ } } say('🔄 Loop: '+(ps.barsN||nx)+' bar'+((ps.barsN||nx)>1?'s':'')+'.'); }
 function quant(){ const b=document.querySelector('.kPadMode [data-pl="snap"]'); if(b) b.click(); else say('Open the pad machine once to set quantize.'); }
 const padMode=()=>{ try{ return KPADLATCH.mode; }catch(_){ return 'hit'; } };
 function setPadMode(m,rate){ const s=document.querySelector('.kPadMode [data-pl="mode"]'); if(rate){ const r=document.querySelector('.kPadMode [data-pl="rate"]'); if(r){ r.value=String(rate); fire(r); } } if(s){ s.value=m; fire(s); } else { try{ KPADLATCH.mode=m; }catch(_){ } } }
 const REP=[['0','OFF'],['4','1/16'],['2','1/8'],['6','1/16T'],['8','1/32']];
 function repeat(){ const r=document.querySelector('.kPadMode [data-pl="rate"]'); const on=padMode()==='hold'; const curR=r?r.value:'4'; let idx=on?REP.findIndex(x=>x[0]===curR):0; idx=(idx+1)%REP.length; if(REP[idx][0]==='0'){ setPadMode('hit'); say('🔁 Note repeat off.'); } else { setPadMode('hold',REP[idx][0]); say('🔁 Note repeat '+REP[idx][1]+': hold a pad and it repeats in time.'); } }
 function latchPads(){ const on=/^latch/.test(padMode()); setPadMode(on?'hit':'latch'); }
 /* ---------- the sounds drawer ---------- */
 async function fillGroups(sel,first){ let G=[]; try{ G=await KBANK.groups(); }catch(_){ } sel.innerHTML='<option value="">'+first+'</option>'+G.map(([v,t])=>'<option value="'+esc(v)+'">'+esc(t)+'</option>').join(''); }
 function drawer(dev,host){ let d=host.querySelector(':scope > .kDrawer'); if(d) return d; d=document.createElement('div'); d.className='kDrawer'; d.hidden=true;
  if(dev==='pads'){ const kit=$('padKit'); d.innerHTML='<label>Drum kit<select data-dw="kit">'+(kit?[...kit.options].map(o=>'<option value="'+o.value+'">'+esc(o.text)+'</option>').join(''):'')+'</select></label>'+
    '<label>Library sounds onto the 16 pads<select data-dw="lib"><option value="">Pick a sound group…</option></select></label>'+
    '<label>An instrument on the pads<select data-dw="inst">'+(window.KPADINST?KPADINST.instruments.map(v=>'<option value="'+v+'">'+(v==='own'?'The bank’s own sounds':v.charAt(0).toUpperCase()+v.slice(1))+'</option>').join(''):'')+'</select></label>'+
    '<div class="dRow"><button type="button" data-dw="up" data-noul>📁 Upload my sounds to the pads</button><button type="button" data-dw="mic" data-noul>🎙 Record a sound to the selected pad</button><button type="button" data-dw="own" data-noul>↩ The kit’s own sounds</button></div>';
   fillGroups(d.querySelector('[data-dw="lib"]'),'Pick a sound group…'); }
  else { const pre=$('kbPre'); d.innerHTML='<label>Keyboard sound (program)<select data-dw="pre">'+(pre?[...pre.options].map(o=>'<option value="'+o.value+'">'+esc(o.text)+'</option>').join(''):'')+'</select></label>'+
    '<label>A library sound across the keys<select data-dw="kgrp"><option value="">Pick a sound group…</option></select></label><label>…then the sound<select data-dw="ksnd"><option value="">Pick a sound…</option></select></label>'+
    '<div class="dRow"><button type="button" data-dw="kup" data-noul>📁 Upload my own sample to play on the keys</button></div>';
   fillGroups(d.querySelector('[data-dw="kgrp"]'),'Pick a sound group…'); }
  d.addEventListener('change',async e=>{ const k=e.target.dataset.dw; if(!k) return; e.stopPropagation(); const v=e.target.value;
   if(k==='kit'){ const s=$('padKit'); if(s){ s.value=v; fire(s,'input'); fire(s); say('🥁 Kit: '+s.options[s.selectedIndex].text); } }
   if(k==='lib'&&v){ try{ KBANK.loadPads(v,0); }catch(_){ say('Open the pad machine first.'); } }
   if(k==='inst'){ try{ KPADINST.set({inst:v}); }catch(_){ } }
   if(k==='pre'){ const s=$('kbPre'); if(s){ s.value=v; fire(s); say('🎹 Program: '+s.options[s.selectedIndex].text); } }
   if(k==='kgrp'){ const s=d.querySelector('[data-dw="ksnd"]'); let L=[]; try{ L=v?await KBANK.itemsOf(v):[]; }catch(_){ } s.innerHTML='<option value="">Pick a sound…</option>'+L.map((x,i)=>'<option value="'+i+'">'+esc(x.name)+'</option>').join(''); }
   if(k==='ksnd'&&v!==''){ try{ KBANK.loadKeys(d.querySelector('[data-dw="kgrp"]').value,+v); }catch(_){ } } });
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-dw]'); if(!b||b.tagName!=='BUTTON') return; e.stopPropagation(); const k=b.dataset.dw;
   if(k==='up'){ const u=$('padUp'); if(u) u.click(); } if(k==='mic'){ const m=$('padMic'); if(m) m.click(); } if(k==='own'){ try{ KBANK.loadPads('own',0); }catch(_){ } try{ KPADINST.set({inst:'own'}); }catch(_){ } }
   if(k==='kup'){ const u=$('kbSampleBtn'); if(u) u.click(); } });
  host.appendChild(d); return d; }
 /* ---------- building the two screens ---------- */
 const SOFT={pads:[['kitp','◀','KIT'],['kitn','▶','KIT'],['bank0','A','BANK','bank'],['bank1','B','BANK','bank'],['bank2','C','BANK','bank'],['bank3','D','BANK','bank'],['snd','⬇','LOAD'],['up','⬆','UPLOAD'],['latch','🔒','LATCH'],['rep','🔁','REPEAT'],['loop','🔄','LOOP'],['q','🧲','Q'],['tap','👆','TAP']],
  keys:[['prgp','◀','PROG'],['prgn','▶','PROG'],['octd','−','OCT'],['octu','+','OCT'],['snd','⬇','LOAD'],['up','⬆','UPLOAD'],['latch','🔒','LATCH'],['arp','🎼','ARP'],['loop','🔄','LOOP'],['q','🧲','Q'],['tap','👆','TAP']]};
 function build(dev){ const bar=dev==='pads'?$('mpcBar'):$('kbDash'); if(!bar) return null; let s=bar.querySelector(':scope > .kScr'); if(s){ if(bar.firstElementChild!==s) bar.insertBefore(s,bar.firstChild); return s; }
  s=document.createElement('div'); s.className='kScr '+(dev==='pads'?'mpc':'wks'); s.setAttribute('role','group'); s.setAttribute('aria-label',dev==='pads'?'Beat machine screen':'Keyboard screen');
  s.innerHTML='<div class="kLcd" aria-live="off"></div><div class="kSoft">'+SOFT[dev].map(([k,i,l,c])=>'<button type="button" data-sf="'+k+'"'+(c?' class="'+c+'"':'')+' title="'+l+(c?' '+i:'')+'" data-noul><span>'+i+'</span>'+l+'</button>').join('')+'</div>';
  drawer(dev,s);
  s.addEventListener('click',e=>{ const b=e.target.closest('[data-sf]'); if(!b) return; e.stopPropagation(); const k=b.dataset.sf;
   if(k==='snd'){ const d=s.querySelector('.kDrawer'); d.hidden=!d.hidden; b.classList.toggle('on',!d.hidden); try{ KPADFLOAT.fit(dev); }catch(_){ } return; }
   if(dev==='pads'){
    if(k==='kitp'||k==='kitn'){ const t=step('padKit',k==='kitn'?1:-1); if(t) say('🥁 Kit: '+t); }
    if(k.startsWith('bank')){ const s2=$('padBank'); if(s2){ s2.value=k.slice(4); fire(s2,'input'); fire(s2); try{ PS().refresh(); }catch(_){ } say('🥁 Pad bank '+'ABCD'[+k.slice(4)]+'.'); } }
    if(k==='up'){ const u=$('padUp'); if(u) u.click(); }
    if(k==='latch'){ latchPads(); } if(k==='rep') repeat(); }
   else {
    if(k==='prgp'||k==='prgn'){ const t=step('kbPre',k==='prgn'?1:-1,o=>o.value==='sample'); if(t) say('🎹 Program: '+t); }
    if(k==='octd'||k==='octu'){ const o=document.querySelector('#kbDash [data-k="'+(k==='octd'?'octdn':'octup')+'"]'); if(o) o.click(); else step('kbOct',k==='octu'?1:-1); }
    if(k==='up'){ const u=$('kbSampleBtn'); if(u) u.click(); }
    if(k==='latch'){ const o=document.querySelector('#kbDash .mr [data-k="latch"]'); if(o) o.click(); }
    if(k==='arp'){ const t=step('kbArp',1); if(t) say('🎼 Arpeggiator: '+t+'. Hold notes and it plays them in time.'); } }
   if(k==='loop') loop(); if(k==='q') quant(); if(k==='tap') tap(); setTimeout(paint,60); });
  bar.insertBefore(s,bar.firstChild); return s; }
 /* ---------- the live readout ---------- */
 let lastStep=-1, stepAt=0;
 function pos(){ const ps=PS(), P=window.PADS||{}; const spb=(ps&&ps.spbN)||16, bars=(ps&&ps.barsN)||1; const playing=!!(ps&&ps.playing); let st=typeof P.step==='number'?Math.max(0,P.step):0; if(st!==lastStep){ lastStep=st; stepAt=performance.now(); }
  const bpm=(ps&&ps.bpm&&ps.bpm())||90; const stepMs=60000/bpm/4; const frac=playing?Math.min(.999,(performance.now()-stepAt)/stepMs):0; const perBeat=Math.max(1,spb/4);
  const bar=Math.floor(st/spb)%bars+1, inBar=st%spb, beat=Math.floor(inBar/perBeat)+1, tick=Math.floor(((inBar%perBeat)+frac)/perBeat*96);
  return {bar,beat,tick,bars,bpm:Math.round(bpm),playing}; }
 const pad=(n,w)=>String(n).padStart(w,'0');
 function line(l,r){ return '<div class="r"><span>'+l+'</span><span>'+(r||'')+'</span></div>'; }
 function paint(){ ['pads','keys'].forEach(dev=>{ const s=build(dev); if(!s||!s.getClientRects().length) return; const lcd=s.querySelector('.kLcd'); const p=pos(); const md=window.PADRECMODE||'live'; const qtxt=md==='live'?'Q OFF·REAL TIME':'Q '+({step:'1/16','8':'1/8','4':'1/4','32':'1/32'}[md]||md);
   let html='';
   if(dev==='pads'){ const kit=$('padKit'), bank=$('padBank'); const ki=kit?kit.selectedIndex:0; const kn=kit&&kit.options[ki]?kit.options[ki].text:'—'; const bi=bank?+bank.value:0; const bn=bank&&bank.options[bi]?bank.options[bi].text.split('·').pop().trim():'';
    const rec=(()=>{ const b=$('padRecLive'); return !!b&&(b.classList.contains('rec')||/on$/i.test(b.textContent.trim())); })();
    const sel=document.querySelector('#padGrid .pd.sel'); const si=sel?+sel.dataset.i:0; const pd=PS()&&PS().pads[si]; const hits=pd?((pd.steps||[]).filter(Boolean).length+(pd.xh||[]).length):0; const pnm=pd?String(pd.name||'').toUpperCase():''; const lab='ABCD'[Math.floor(si/16)]+(si%16+1);
    const mdp=padMode(); const lat=/^latch/.test(mdp); const rep=mdp==='hold'?(REP.find(x=>x[0]===((document.querySelector('.kPadMode [data-pl="rate"]')||{}).value||'4'))||['','1/16'])[1]:'';
    html=line('PGM '+pad(ki+1,2)+' '+esc(kn),'BANK '+'ABCD'[bi]+' '+esc(bn))+line((rec?'<b class="rec">● REC</b> ':'')+(p.playing?'<b class="on">▶ PLAY</b>':'■ STOP')+'  BAR '+pad(p.bar,2)+'.'+p.beat+'.'+pad(p.tick,2),p.bpm+' BPM')+
     line('LOOP '+p.bars+' BAR'+(p.bars>1?'S':'')+'  '+qtxt,(lat?'<b class="on">LATCH</b> ':'')+(rep?'<b class="on">RPT '+rep+'</b>':''))+line('PAD '+lab+' '+esc(pnm),hits+' HIT'+(hits===1?'':'S')+' IN LOOP');
    s.querySelectorAll('[data-sf^="bank"]').forEach(b=>b.classList.toggle('on',+b.dataset.sf.slice(4)===bi)); s.querySelector('[data-sf="latch"]').classList.toggle('on',lat); s.querySelector('[data-sf="rep"]').classList.toggle('on',!!rep); }
   else { const pre=$('kbPre'), oct=$('kbOct'), arp=$('kbArp'); const pi=pre?pre.selectedIndex:0; const pn=pre&&pre.options[pi]?pre.options[pi].text:'—'; const ov=oct&&oct.options[oct.selectedIndex]?oct.options[oct.selectedIndex].text:'C3';
    const rec=(()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); })(); let KT=[]; try{ KT=KEYS.KT||[]; }catch(_){ }
    const last=KT.length?nm(KT[KT.length-1].m):'—'; const lat=!!window.KBLATCH; const av=arp&&arp.value!=='off'?arp.options[arp.selectedIndex].text:'';
    html=line('PROG '+pad(pi+1,3)+': '+esc(pn),'OCT '+esc(ov))+line((rec?'<b class="rec">● REC</b> ':'')+(p.playing?'<b class="on">▶ PLAY</b>':'■ STOP')+'  BAR '+pad(p.bar,2)+'.'+p.beat+'.'+pad(p.tick,2),p.bpm+' BPM')+
     line('LOOP '+p.bars+' BAR'+(p.bars>1?'S':'')+'  '+qtxt,(lat?'<b class="on">LATCH</b> ':'')+(av?'<b class="on">ARP '+esc(av)+'</b>':''))+(()=>{ let nmT='KEYS TRACK', cnt=KT.length, lst=last; try{ const T=KSEQ.tracks.find(x=>x.id===(KSEQ.keysId||KSEQ.armed)); if(T&&T.kind==='keys'){ nmT='● '+T.name.replace(/^\S+\s/,'').toUpperCase(); cnt=T.notes.length; lst=cnt?nm(T.notes[cnt-1].m):'—'; } }catch(_){ } return line(esc(nmT)+': '+cnt+' NOTE'+(cnt===1?'':'S'),'LAST '+lst); })();
    s.querySelector('[data-sf="latch"]').classList.toggle('on',lat); s.querySelector('[data-sf="arp"]').classList.toggle('on',!!av); }
   s.querySelector('[data-sf="q"]').classList.toggle('on',md!=='live');
   if(lcd.dataset.h!==html){ lcd.dataset.h=html; lcd.innerHTML=html; } }); }
 setInterval(paint,120);
 window.KDISPLAY={paint,tap,loop};
})();
