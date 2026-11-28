(()=>{ /* 🎛 THE CONTROL DECK (v263). One floating dashboard rides on top of the Music Studio, Karaoke and the Virtual DJ, and drives
   that screen's own engine, so the controls a person needs are always in one place, in sight, whatever is scrolled or open:
   • TRANSPORT, always showing: ⏮ back to bar 1 · ▶ play · ■ stop · ● record · 🔁 loop, the playhead (bar . beat), the tempo.
   • ✏ EDIT (studio): bars as blocks, the way a production program edits a song. Pick a bar and a length, then ⧉ Copy, ✂ Cut,
     📋 Paste, ⧉ Duplicate (the copy lands right after itself), ➕ Insert blank bars (the bars after move right and the loop grows),
     ➖ Delete bars (the bars after close the gap), 🗑 Clear. Every edit moves the drums, the keyboard and composer notes, the
     instrument tracks, the chord chart and the mix automation together, and ↶ Undo takes it back. Ctrl/⌘ + Shift + C, X, V, D.
   • 📁 FILE: 🆕 New, 📂 Open (a project file or the library), 💾 Save (a project file with every sound, or a WAV), 📥 Load a sound.
   • ✂ PUNCH (drop in, drop out): pick the In bar and the Out bar and press ● with ✂ Punch on. The loop plays from the top; the
     recording lands only between In and Out, and everything outside stays exactly as it was (it is locked while you record).
     ⇄ Replace wipes the old part between In and Out as the take drops in; Overdub adds to it. 🔂 One pass drops out at Out.
     With the Microphone or Vocals chosen, the take is recorded from the In bar to the Out bar and placed on its bars.
   • 📈 MIX AUTOMATION: the 40-track console records your hands. Modes, as in a studio console: Off · Read (the faders move by
     themselves along what was recorded) · Touch (moving a fader writes while you hold it, and it returns to the line when you let
     go) · Latch (writes from your first move until ■ Stop) · Write (every 🅰 armed strip is written for the whole pass, then the
     deck drops to Touch). Volume and pan are written per step, play live and go into the WAV. 🔒 locks a lane; 🗑 clears it.
   • ⌨ KEY MAP: the split keyboard for this screen. On Karaoke and the DJ the keys work at once: the left hand (1 2 3 4 · Q W E R
     · A S D F · Z X C V) brings up and plays the 16 pads (on the DJ: deck A on 1234 QWER and deck B on 7890 UIOP), the right hand
     (Y U I O P [ ] \ white · 7 8 0 - = black) the piano, and H ⏮ · J ▶ · K ■ · L ● · ; ↶ drive this screen's transport.
   The deck folds to a small 🎛 tab, and can be dragged by its title bar; it remembers where it was put. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const vis=el=>!!el&&!el.hidden&&el.getClientRects().length>0&&getComputedStyle(el).visibility!=='hidden'&&getComputedStyle(el).display!=='none';
 const isOpen=k=>{ try{ return KRAIL.FLOAT.isOpen(k); }catch(_){ return false; } };
 const SIZES=[1,2,4,8,16,20,24,32];
 const spb=()=>{ try{ return PS().spbN||16; }catch(_){ return 16; } }, nBars=()=>{ try{ return PS().barsN||1; }catch(_){ return 1; } };
 const live=c=>{ try{ return c===PS().ac(); }catch(_){ return false; } };
 const btn=(root,re)=>[...((root&&root.querySelectorAll)?root.querySelectorAll('button'):[])].find(b=>re.test(b.textContent.replace(/\s+/g,' ').trim()));
 const clickBtn=(root,re)=>{ const b=btn(root,re); if(b){ b.click(); return true; } return false; };

 /* ================= where the deck is: the screen in front ================= */
 let LASTWIN='';
 document.addEventListener('pointerdown',e=>{ const t=e.target; if(!t.closest||t.closest('#kDeck')) return; const f=t.closest('.kFloat.kFOn,.kWin'); if(f) LASTWIN=f.id==='djSec'?'dj':(f.id||'win'); else if(t.closest('#pad,#kKara')) LASTWIN='page'; },true);
 const OVL=['kAcct','kArr','kFind','kLegal','kOwner','kAudit','kVG','kProj','kSocial','kDoor','kDance','kCBeat','kHumor','kJump','kLock','kKnow','kNews','kRelig','kReligX','kMarket','kSports','kServices','kZRingPage','kSndSheet','kKeysPop','kEasel','kAI'];
 function ctx(){ const B=document.body; if(B.classList.contains('gated')) return null; const ag=$('kAgree'); if(ag&&vis(ag)) return null;
  const t=$('tourTab'); if(t&&vis(t)&&t.getBoundingClientRect().width>40) return null;
  for(const id of OVL){ if(vis($(id))) return null; }
  let cur=''; try{ cur=KRAIL.cur(); }catch(_){ }
  /* the DJ deck takes over when the Virtual DJ is the window the person touched last; another window touched gives the screen's own deck back */
  const dj=$('djSec'); if(isOpen('dj')&&vis(dj)&&LASTWIN==='dj') return 'dj';
  if(cur==='kKara'||vis($('kKara'))) return 'kara';
  const pad=$('pad'); if(cur==='pad'&&pad&&pad.classList.contains('on')) return 'studio';
  return null; }

 /* ================= the clock: one hook on the studio's own step clock ================= */
 const POS={s:0,at:0};
 function hook(c,dest,t,s){ try{ readSched(c,dest,t,s); }catch(_){ }
  if(!live(c)) return; const d=Math.max(0,(t-c.currentTime)*1000);
  try{ punchSched(c,t,s); }catch(_){ }
  setTimeout(()=>{ POS.s=s; POS.at=performance.now(); try{ writeStep(s); }catch(_){ } try{ guardStep(s); }catch(_){ } lcd(); },d); }
 let hooked=false; const tryHook=()=>{ const P=PS(); if(hooked||!P||!P.STEPHOOKS) return; P.STEPHOOKS.push(hook); hooked=true;
  if(P.EXT&&!P.EXT.some(x=>x.key==='mixauto')) P.EXT.push({key:'mixauto',full:async()=>auPack(),load:async o=>{ auUnpack(o); auSave(); paintAuto(); }}); };

 /* ================= ✏ EDIT: bars as blocks ================= */
 function arrays(){ const a=[]; const T=window.THEORY; if(T&&T.CT) ['bass','chords','melody','gtr'].forEach(k=>{ if(Array.isArray(T.CT[k])) a.push(T.CT[k]); });
  try{ if(window.KEYS&&Array.isArray(KEYS.KT)) a.push(KEYS.KT); }catch(_){ } try{ ((window.SEQ&&SEQ.ITR)||[]).forEach(t=>{ if(t&&Array.isArray(t.notes)) a.push(t.notes); }); }catch(_){ } return a; }
 const chart=()=>{ try{ return Array.isArray(THEORY.chart)?THEORY.chart:null; }catch(_){ return null; } };
 function snap(){ const P=PS(); return {bars:nBars(),steps:P.pads.map(p=>p.steps.slice()),offs:P.pads.map(p=>p.offs?Object.assign({},p.offs):null),notes:arrays().map(a=>a.map(n=>Object.assign({},n))),chart:(chart()||[]).map(c=>c&&Object.assign({},c)),au:auClone(),lanes:lanesClone()}; }
 function restore(o){ const P=PS(); if(o.bars!==nBars()) setBarsQuiet(o.bars); P.pads.forEach((p,i)=>{ p.steps=o.steps[i].slice(); if(o.offs[i]) p.offs=Object.assign({},o.offs[i]); else delete p.offs; });
  arrays().forEach((a,i)=>{ if(o.notes[i]) a.splice(0,a.length,...o.notes[i].map(n=>Object.assign({},n))); });
  try{ if(o.chart.length) THEORY.setChart(o.chart.map(c=>c&&Object.assign({},c))); }catch(_){ } AU.ch=o.au; lanesPut(o.lanes); auSave(); refresh(); }
 function setBarsQuiet(n){ try{ PS().setBars(n); }catch(_){ } }
 function refresh(){ try{ PS().refresh(); }catch(_){ } try{ THEORY.redraw(); }catch(_){ } try{ SEQ.renderSq(); }catch(_){ } try{ KSEQ.paint&&KSEQ.paint(); }catch(_){ } paintAuto(); }
 function undoable(name,fn){ const o=snap(); fn(); try{ KUNDO.push(()=>restore(o),name); }catch(_){ } }
 /* the drawn shape lanes of 📈 Automation move with the bars too */
 const LANES=()=>Array.isArray(window.AUTOMATION)?window.AUTOMATION:[];
 const lanesClone=()=>LANES().map(l=>Float32Array.from(l.pts));
 const lanesPut=a=>LANES().forEach((l,i)=>{ if(a[i]) l.pts.set(a[i]); });
 /* one bar range [from, from+len) of everything, as a block */
 function grab(from,len){ const s=spb(), lo=from*s, hi=(from+len)*s; const P=PS();
  return {len,steps:P.pads.map(p=>p.steps.slice(lo,hi)),offs:P.pads.map(p=>{ const o={}; Object.entries(p.offs||{}).forEach(([k,v])=>{ if(+k>=lo&&+k<hi) o[+k-lo]=v; }); return o; }),
   notes:arrays().map(a=>a.filter(n=>n.s>=lo&&n.s<hi).map(n=>Object.assign({},n,{s:n.s-lo}))),chart:(chart()||[]).slice(from,from+len).map(c=>c&&Object.assign({},c)),
   au:Object.fromEntries(Object.entries(AU.ch).map(([ci,L])=>[ci,{v:L.v.slice(lo,hi),p:L.p.slice(lo,hi)}])),lanes:LANES().map(l=>Array.from(l.pts.slice(lo,hi)))}; }
 function wipe(from,len){ const s=spb(), lo=from*s, hi=(from+len)*s; const P=PS(); P.pads.forEach(p=>{ for(let i=lo;i<hi;i++) p.steps[i]=0; if(p.offs) Object.keys(p.offs).forEach(k=>{ if(+k>=lo&&+k<hi) delete p.offs[k]; }); });
  arrays().forEach(a=>{ for(let i=a.length-1;i>=0;i--) if(a[i].s>=lo&&a[i].s<hi) a.splice(i,1); });
  Object.values(AU.ch).forEach(L=>{ for(let i=lo;i<hi;i++){ L.v[i]=null; L.p[i]=null; } }); }
 function put(blk,at){ const s=spb(), lo=at*s; const len=Math.min(blk.len,nBars()-at); if(len<=0) return 0; const n=len*s; wipe(at,len); const P=PS();
  P.pads.forEach((p,i)=>{ (blk.steps[i]||[]).slice(0,n).forEach((v,k)=>{ if(v) p.steps[lo+k]=v; }); const of=blk.offs[i]||{}; Object.entries(of).forEach(([k,v])=>{ if(+k<n){ p.offs=p.offs||{}; p.offs[lo+(+k)]=v; } }); });
  arrays().forEach((a,i)=>(blk.notes[i]||[]).filter(x=>x.s<n).forEach(x=>a.push(Object.assign({},x,{s:x.s+lo}))));
  const ch=chart(); if(ch&&blk.chart.length){ const c2=ch.slice(); const L0=c2.length; blk.chart.slice(0,len).forEach((c,k)=>{ c2[at+k]=c; }); for(let i=0;i<c2.length;i++) if(c2[i]==null) c2[i]=L0?c2[i%L0]:blk.chart[0]; try{ THEORY.setChart(c2.filter(c=>c!=null)); }catch(_){ } }
  Object.entries(blk.au).forEach(([ci,b])=>{ const L=lane(+ci); for(let k=0;k<n;k++){ L.v[lo+k]=b.v[k]==null?null:b.v[k]; L.p[lo+k]=b.p[k]==null?null:b.p[k]; } });
  LANES().forEach((l,i)=>{ const b=blk.lanes[i]; if(b) for(let k=0;k<n&&k<b.length;k++) l.pts[lo+k]=b[k]; });
  return len; }
 let CLIP=null; const SEL={from:0,len:1,at:0};
 const clampSel=()=>{ const n=nBars(); SEL.from=Math.max(0,Math.min(n-1,SEL.from)); SEL.at=Math.max(0,Math.min(n-1,SEL.at)); };
 const selLen=()=>Math.max(1,Math.min(SEL.len,nBars()-SEL.from));
 const barsWord=n=>n+' bar'+(n>1?'s':'');
 const ED={
  copy(){ clampSel(); CLIP=grab(SEL.from,selLen()); say('⧉ Copied '+barsWord(CLIP.len)+' from bar '+(SEL.from+1)+': drums, notes, chords and mix automation. Pick a bar and 📋 Paste.'); paintDeck(); },
  cut(){ clampSel(); const len=selLen(); undoable('cut bars',()=>{ CLIP=grab(SEL.from,len); wipe(SEL.from,len); refresh(); }); say('✂ Cut '+barsWord(len)+' from bar '+(SEL.from+1)+'. 📋 Paste puts them anywhere; ↶ Undo puts them back.'); paintDeck(); },
  paste(){ clampSel(); if(!CLIP) return say('Copy some bars first: ⧉ Copy or ✂ Cut.'); let n=0; undoable('paste bars',()=>{ n=put(CLIP,SEL.at); refresh(); }); say(n?'📋 Pasted '+barsWord(n)+' at bar '+(SEL.at+1)+(n<CLIP.len?' (the rest is past the end of the loop)':'')+'.':'Nothing pasted: that bar is past the loop.'); },
  dup(){ clampSel(); const len=selLen(); const blk=grab(SEL.from,len); const at=SEL.from+len; undoable('duplicate bars',()=>{ if(at+len>nBars()){ const need=SIZES.find(x=>x>=at+len); if(need) setBarsQuiet(need); } put(blk,at); refresh(); }); SEL.from=at; SEL.at=at; say('⧉ Duplicated '+barsWord(len)+' to bar '+(at+1)+'. Press again to keep going.'); paintDeck(); },
  insert(){ clampSel(); const len=SEL.len, B=nBars(), at=SEL.from; let msg=''; undoable('insert bars',()=>{ const tail=grab(at,B-at); const want=B+len; const nb=SIZES.find(x=>x>=want);
    if(nb){ setBarsQuiet(nb); wipe(at,nb-at); put(tail,at+len); msg='➕ '+barsWord(len)+' of silence inserted at bar '+(at+1)+'; the loop is now '+barsWord(nb)+'.'; }
    else { wipe(at,B-at); const kept=put(tail,at+len); msg='➕ '+barsWord(len)+' inserted at bar '+(at+1)+'. The loop is at its longest (32 bars), so the last '+barsWord(tail.len-kept)+' moved past the end. ↶ Undo brings them back.'; }
    refresh(); }); say(msg); paintDeck(); },
  del(){ clampSel(); const B=nBars(), at=SEL.from, len=Math.min(SEL.len,B-at); let msg=''; undoable('delete bars',()=>{ const tail=at+len<B?grab(at+len,B-at-len):null; wipe(at,B-at); if(tail) put(tail,at);
    const left=B-len; const nb=SIZES.find(x=>x>=Math.max(1,left)); if(nb&&nb<B) setBarsQuiet(nb); msg='➖ '+barsWord(len)+' deleted at bar '+(at+1)+'; the bars after it closed the gap'+(nb&&nb<B?' and the loop is now '+barsWord(nb):'')+'.'; refresh(); }); say(msg); paintDeck(); },
  clear(){ clampSel(); const len=selLen(); undoable('clear bars',()=>{ wipe(SEL.from,len); refresh(); }); say('🗑 Bars '+(SEL.from+1)+(len>1?'–'+(SEL.from+len):'')+' are clear. ↶ Undo brings them back.'); },
  double(){ try{ BAREDIT.doubleLoop(); }catch(_){ say('Open the 🎛 Studio first.'); } setTimeout(paintDeck,120); } };
 addEventListener('keydown',e=>{ if(!(e.ctrlKey||e.metaKey)||!e.shiftKey||e.altKey) return; const t=e.target; if(t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable)) return; if(ctx()!=='studio') return;
  const k=({KeyC:'copy',KeyX:'cut',KeyV:'paste',KeyD:'dup'})[e.code]; if(!k) return; e.preventDefault(); e.stopImmediatePropagation(); ED[k](); },true);

 /* ================= ✂ PUNCH: drop in, drop out ================= */
 const PU=Object.assign({on:false,inB:2,outB:2,rep:false,once:false},getLS('kanin-punch1',{})); PU.on=false;
 const puSave=()=>putLS('kanin-punch1',{inB:PU.inB,outB:PU.outB,rep:PU.rep,once:PU.once});
 const prange=()=>{ const n=nBars(); const a=Math.max(1,Math.min(n,PU.inB)), b=Math.max(a,Math.min(n,PU.outB)); return [(a-1)*spb(),b*spb(),a,b]; };
 const recWhat=()=>{ const r=$('ktRecWhat'); return r?r.value:'pads'; };
 const padRec=()=>{ const b=$('padRecLive'); return !!b&&b.classList.contains('rec'); };
 const keyRec=()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); };
 const recActive=()=>padRec()||keyRec();
 let GS=null, wasRec=false, inside=false, dropped=false;
 /* the outside of the punch is photographed the instant record is pressed, before any hit can land */
 document.addEventListener('click',e=>{ if(!PU.on||GS) return; const b=e.target.closest&&e.target.closest('#padRecLive,#kbRec,#ktRec'); if(b) guardTake(); },true);
 function guardTake(){ const P=PS(); GS={at:performance.now(),steps:P.pads.map(p=>p.steps.slice()),offs:P.pads.map(p=>Object.assign({},p.offs||{})),keep:arrays().map(a=>a.map(n=>Object.assign({},n))),sig:arrays().map(a=>new Set(a.map(n=>JSON.stringify(n))))}; inside=false; dropped=false; }
 function guardNotes(){ if(!GS) return false; const [lo,hi]=prange(); let ch=false;
  arrays().forEach((a,i)=>{ const sig=GS.sig[i]; if(!sig) return; for(let j=a.length-1;j>=0;j--){ const n=a[j]; if(n.s>=lo&&n.s<hi) continue; if(!sig.has(JSON.stringify(n))){ a.splice(j,1); ch=true; } }
   const now=new Set(a.map(n=>JSON.stringify(n))); GS.keep[i].forEach(n=>{ if((n.s<lo||n.s>=hi)&&!now.has(JSON.stringify(n))){ a.push(Object.assign({},n)); ch=true; } }); }); return ch; }
 function guardPads(){ if(!GS) return false; const [lo,hi]=prange(); const P=PS(), T=P.total; let ch=false; P.pads.forEach((p,i)=>{ const o=GS.steps[i], of=GS.offs[i]; for(let k=0;k<T;k++){ if(k>=lo&&k<hi) continue; if((p.steps[k]||0)!==(o[k]||0)){ p.steps[k]=o[k]||0; ch=true; if(p.offs){ if(of[k]!=null) p.offs[k]=of[k]; else delete p.offs[k]; } } } }); return ch; }
 function guardEnd(){ const a=guardPads(), b=guardNotes(); GS=null; wasRec=false; if(a||b) refresh(); }
 setInterval(()=>{ if(wasRec&&!(PU.on&&recActive())) guardEnd(); else if(GS&&!wasRec&&!recActive()&&performance.now()-GS.at>2500) GS=null; },250);
 function guardStep(s){ const on=PU.on&&recActive();
  if(on&&!wasRec&&!GS) guardTake(); if(!on&&wasRec){ guardEnd(); return; } wasRec=on; if(!on||!GS) return;
  const [lo,hi,a,b]=prange(); const P=PS(), T=P.total; let ch=false;
  if(guardPads()) ch=true;
  if(s>=lo&&s<hi){ if(!inside&&s===lo){ inside=true; if(PU.rep&&!dropped){ dropped=true; const bank=Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0));
     if(padRec()) for(let i=bank*16;i<bank*16+16;i++){ const p=P.pads[i]; for(let k=lo;k<hi;k++) p.steps[k]=0; if(p.offs) Object.keys(p.offs).forEach(k=>{ if(+k>=lo&&+k<hi) delete p.offs[k]; }); }
     if(keyRec()){ try{ const K=KEYS.KT; for(let j=K.length-1;j>=0;j--) if(K[j].s>=lo&&K[j].s<hi) K.splice(j,1); }catch(_){ } }
     ch=true; say('⇄ Dropped in at bar '+a+': the old part is replaced while you play.'); } else if(!dropped){ dropped=true; say('✂ Dropped in at bar '+a+'. Play now; only bars '+a+(b>a?'–'+b:'')+' are recorded.'); } } }
  else if(inside){ inside=false; if(guardNotes()) ch=true; if(PU.once){ stopRec(); say('✂ Dropped out after bar '+b+'. The take is in; everything outside stayed as it was.'); } }
  if(s%spb()===0&&guardNotes()) ch=true; if(ch) refreshSoon(); }
 let rT=0; const refreshSoon=()=>{ if(rT) return; rT=setTimeout(()=>{ rT=0; try{ PS().refresh(); }catch(_){ } },120); };
 function stopRec(){ const kt=$('ktRec'); if(kt&&kt.classList.contains('on')) kt.click(); else { if(padRec()) press('padRecLive'); if(keyRec()) press('kbRec'); } }
 /* the microphone, dropped in on the bar: recorded from In to Out and placed on those bars of a vocal track */
 let VP=null;
 async function vocalPunch(){ const P=PS(); if(!P) return; if(VP){ return say('A punch take is already waiting for bar '+PU.inB+'.'); }
  let st; try{ st=await navigator.mediaDevices.getUserMedia({audio:true}); }catch(_){ return say('🎙 The microphone is not available here: allow it in the browser, or use the downloaded app.'); }
  const [lo,hi,a,b]=prange(); VP={st,lo,hi,a,b,armed:true}; if(!P.playing){ try{ P.play(); }catch(_){ } } setRecLamp(true); say('🎙 Punch take armed: it drops in at bar '+a+' and out after bar '+b+'.'); }
 function punchSched(c,t,s){ if(!VP||!VP.armed||s!==VP.lo) return; VP.armed=false; const v=VP; const barSec=PS().stepDur()*spb(); const L=v.b-v.a+1;
  const ch=[]; let mr; try{ mr=new MediaRecorder(v.st); }catch(_){ VP=null; setRecLamp(false); return say('This browser cannot record the microphone.'); }
  mr.ondataavailable=e=>ch.push(e.data); mr.onstop=async()=>{ v.st.getTracks().forEach(x=>x.stop()); VP=null; setRecLamp(false);
   try{ const P=PS(); const cx=P.ac(); const buf=(window.TRIMLAT||(x=>x))(await cx.decodeAudioData(await new Blob(ch).arrayBuffer()),cx); const i0=v.a-1;
    if(PU.rep) (P.tracks||[]).forEach(k=>{ if(k.vocal) for(let x=i0;x<i0+L;x++) k.on[x]=false; });
    window.PADADDLOOP(buf,'🎙 Punch take · bars '+v.a+(L>1?'–'+v.b:''),L,{mode:'native',vocal:true,on:new Array(32).fill(false).map((_,x)=>x>=i0&&x<i0+L)});
    say('🎙 Punch take placed on bars '+v.a+(L>1?'–'+v.b:'')+(PU.rep?', replacing the takes under it there':'')+'. It is on the vocal strip of the mixing board.'); }catch(_){ say('That take could not be read here.'); } };
  const wait=Math.max(0,(t-c.currentTime)*1000-30); setTimeout(()=>{ try{ mr.start(); say('🎙 Recording bars '+v.a+(L>1?'–'+v.b:'')+'…'); setTimeout(()=>{ try{ mr.stop(); }catch(_){ } },L*barSec*1000+150); }catch(_){ VP=null; setRecLamp(false); } },wait); }
 let recLamp=false; const setRecLamp=v=>{ recLamp=v; paintDeck(); };

 /* ================= 📈 MIX AUTOMATION: the console records your hands ================= */
 const MODES=[['off','Off'],['read','Read'],['touch','Touch'],['latch','Latch'],['write','Write']];
 const AU={mode:getLS('kanin-automode','read'),ch:{}}; if(!MODES.some(m=>m[0]===AU.mode)) AU.mode='read';
 const N=512; const lane=ci=>AU.ch[ci]||(AU.ch[ci]={v:new Array(N).fill(null),p:new Array(N).fill(null),lock:false,arm:false});
 const hasData=L=>!!L&&(L.v.some(x=>x!=null)||L.p.some(x=>x!=null));
 const auClone=()=>{ const o={}; Object.entries(AU.ch).forEach(([k,L])=>o[k]={v:L.v.slice(),p:L.p.slice(),lock:L.lock,arm:L.arm}); return o; };
 const r3=x=>Math.round(x*1000)/1000;
 function auPack(){ const ch={}; Object.entries(AU.ch).forEach(([k,L])=>{ if(!hasData(L)&&!L.arm&&!L.lock) return; const sp=a=>a.map((x,i)=>x==null?null:[i,r3(x)]).filter(Boolean); ch[k]={v:sp(L.v),p:sp(L.p),lock:!!L.lock,arm:!!L.arm}; }); return {mode:AU.mode,ch}; }
 function auUnpack(o){ AU.ch={}; if(!o||typeof o!=='object') return; if(MODES.some(m=>m[0]===o.mode)) AU.mode=o.mode; Object.entries(o.ch||{}).forEach(([k,x])=>{ const L=lane(+k); (x.v||[]).forEach(([i,v])=>{ if(i<N) L.v[i]=v; }); (x.p||[]).forEach(([i,v])=>{ if(i<N) L.p[i]=v; }); L.lock=!!x.lock; L.arm=!!x.arm; }); }
 let sT=0; const auSave=()=>{ clearTimeout(sT); sT=setTimeout(()=>{ putLS('kanin-mixauto1',auPack()); putLS('kanin-automode',AU.mode); },400); };
 auUnpack(getLS('kanin-mixauto1',null));
 const touch=new Map(); /* 'ci:k' → time of the last move (k: v volume, p pan) */ const held=new Set(), latched=new Set();
 const writing=(ci,k)=>{ const id=ci+':'+k; if(AU.mode==='touch') return held.has(id)||(touch.has(id)&&performance.now()-touch.get(id)<450); if(AU.mode==='latch') return latched.has(id); if(AU.mode==='write') return latched.has(id)||!!(AU.ch[ci]&&AU.ch[ci].arm); return false; };
 const stripOf=el=>el&&el.closest&&el.closest('#padMixer .mxs');
 document.addEventListener('pointerdown',e=>{ const t=e.target; if(!t.closest) return; const f=t.closest('#padMixer .mxs input.mxv, #padMixer .mxs .knb'); if(!f) return; const s=stripOf(f); if(!s) return; const ci=+s.dataset.c; if(isNaN(ci)) return; const k=f.classList.contains('mxv')?'v':'p'; held.add(ci+':'+k); },true);
 const release=()=>{ held.clear(); }; addEventListener('pointerup',release,true); addEventListener('pointercancel',release,true);
 document.addEventListener('input',e=>{ const t=e.target; if(!t.matches||!t.matches('#padMixer .mxs input.mxv, #padMixer .mxs input.mxp')) return; if(window.__kdMotor) return; const s=stripOf(t); const ci=+s.dataset.c; if(isNaN(ci)) return; const k=t.classList.contains('mxv')?'v':'p'; const id=ci+':'+k; touch.set(id,performance.now());
  try{ if(PS().playing&&(AU.mode==='latch'||AU.mode==='write')) latched.add(id); }catch(_){ } },true);
 function writeStep(s){ const P=PS(); if(!P||!P.playing||AU.mode==='off'||AU.mode==='read') return; const MIX=P.MIX; let any=false;
  const ids=new Set([...held,...touch.keys(),...latched]); if(AU.mode==='write') Object.entries(AU.ch).forEach(([ci,L])=>{ if(L.arm){ ids.add(ci+':v'); ids.add(ci+':p'); } });
  ids.forEach(id=>{ const [c,k]=id.split(':'); const ci=+c; if(!writing(ci,k)) return; const m=MIX[ci]; if(!m) return; const L=lane(ci); if(L.lock) return; L[k][s%N]=k==='v'?m.vol:m.pan; any=true; });
  if(any){ auSave(); paintAutoSoon(); } }
 function readSched(c,dest,t,s){ if(AU.mode==='off') return; const P=PS(); if(!P||!P.strip) return; const MIX=P.MIX; const anySolo=MIX.some(m=>m&&m.solo); const L0=live(c);
  for(const k0 in AU.ch){ const ci=+k0, L=AU.ch[k0]; const m=MIX[ci]; if(!m) continue;
   for(const k of ['v','p']){ const val=L[k][s%N]; if(val==null) continue; if(L0&&writing(ci,k)) continue; const S=P.strip(c,dest,ci); if(!S) continue;
    if(k==='v'){ const g=(m.mute||(anySolo&&!m.solo))?0:val; try{ S.g.gain.setTargetAtTime(g,t,.012); }catch(_){ } } else if(S.p){ try{ S.p.pan.setTargetAtTime(val,t,.012); }catch(_){ } }
    if(L0){ const d=Math.max(0,(t-c.currentTime)*1000); setTimeout(()=>motor(ci,k,val),d); } } } }
 /* the faders move by themselves, like a console's motorized faders */
 function motor(ci,k,val){ const P=PS(); const m=P&&P.MIX[ci]; if(!m||writing(ci,k)) return; if(k==='v') m.vol=val; else m.pan=val; const s=document.querySelector('#padMixer .mxs[data-c="'+ci+'"]'); if(!s) return;
  window.__kdMotor=true; try{ if(k==='v'){ const f=s.querySelector('input.mxv'); if(f) f.value=String(Math.round(val*100)); } else { const f=s.querySelector('input.mxp'); if(f) f.value=String(Math.round(val*100)); const kn=s.querySelector('.knb'); if(kn) kn.style.setProperty('--rot',(val*135)+'deg'); } } finally { window.__kdMotor=false; } }
 /* after ■ Stop: a Write pass drops to Touch, Latch lets go */
 let wasPlay=false; setInterval(()=>{ let p=false; try{ p=!!PS().playing; }catch(_){ } if(wasPlay&&!p){ latched.clear(); touch.clear(); if(AU.mode==='write'){ AU.mode='touch'; auSave(); say('📈 The Write pass is in. The console is on Touch now, so the next pass plays it back and only your hands change it.'); paintDeck(); } } wasPlay=p; },250);
 /* 🅰 on every console strip: arm it for Write; a lit A shows the strips that have automation */
 function strips(){ const mx=$('padMixer'); if(!mx) return; mx.querySelectorAll('.mxs').forEach(s=>{ const ci=+s.dataset.c; if(isNaN(ci)||s.classList.contains('master')) return; const mb=s.querySelector('.mxb'); if(!mb) return;
  let a=mb.querySelector('[data-a="auto"]'); if(!a){ a=document.createElement('button'); a.type='button'; a.dataset.a='auto'; a.textContent='A'; a.setAttribute('data-noul',''); mb.appendChild(a); }
  const L=AU.ch[ci]; const on=!!(L&&L.arm), has=hasData(L); a.className=(on?'kdArm ':'')+(has?'kdHas':''); a.title=(on?'🅰 Armed for Write':'🅰 Arm for Write')+(has?' · this strip has automation'+(L.lock?' (locked)':''):''); a.setAttribute('aria-pressed',on?'true':'false'); }); }
 document.addEventListener('click',e=>{ const a=e.target.closest&&e.target.closest('#padMixer .mxb [data-a="auto"]'); if(!a) return; e.preventDefault(); e.stopImmediatePropagation(); const ci=+a.closest('.mxs').dataset.c; const L=lane(ci); L.arm=!L.arm; auSave(); strips(); paintAuto();
  say(L.arm?'🅰 Strip '+(ci+1)+' is armed: in Write mode it is written for the whole pass.':'Strip '+(ci+1)+' is no longer armed.'); },true);
 setInterval(strips,900);
 const chName=ci=>{ const s=document.querySelector('#padMixer .mxs[data-c="'+ci+'"] small'); return s?(s.getAttribute('title')||s.textContent).trim():'Track '+(ci+1); };
 function spark(L,k){ const n=Math.max(16,(()=>{ try{ return PS().total; }catch(_){ return 16; } })()); const W=120,H=22; let d=''; let pen=false;
  for(let i=0;i<n;i++){ const v=L[k][i]; if(v==null){ pen=false; continue; } const y=k==='v'?H-2-Math.min(1,v/1.5)*(H-4):H/2-v*(H/2-2); const x=i/(n-1||1)*W; d+=(pen?'L':'M')+x.toFixed(1)+' '+y.toFixed(1); pen=true; }
  return '<svg viewBox="0 0 '+W+' '+H+'" width="'+W+'" height="'+H+'" aria-hidden="true"><rect width="'+W+'" height="'+H+'" rx="4" fill="#050a18"/>'+(k==='p'?'<line x1="0" x2="'+W+'" y1="'+H/2+'" y2="'+H/2+'" stroke="#223"/>':'')+(d?'<path d="'+d+'" fill="none" stroke="'+(k==='v'?'#00e5ff':'#ffb347')+'" stroke-width="1.6"/>':'<text x="6" y="15" fill="#667" font-size="10">no moves</text>')+'</svg>'; }
 let paT=0; const paintAutoSoon=()=>{ if(paT) return; paT=setTimeout(()=>{ paT=0; paintAuto(); },500); };
 function paintAuto(){ const box=document.querySelector('#kDeck [data-pane="auto"] .kdLanes'); if(!box) return; const ids=Object.keys(AU.ch).map(Number).filter(ci=>hasData(AU.ch[ci])||AU.ch[ci].arm||AU.ch[ci].lock).sort((a,b)=>a-b);
  box.innerHTML=ids.length?ids.map(ci=>{ const L=AU.ch[ci]; return '<div class="kdLane"><b title="'+esc(chName(ci))+'">'+(ci+1)+' · '+esc(chName(ci)).slice(0,18)+'</b><span>VOL '+spark(L,'v')+'</span><span>PAN '+spark(L,'p')+'</span><button type="button" data-d="arm" data-ci="'+ci+'" class="'+(L.arm?'on':'')+'" title="Arm this strip for Write">🅰</button><button type="button" data-d="lock" data-ci="'+ci+'" class="'+(L.lock?'on':'')+'" title="Lock this lane: nothing writes over it">🔒</button><button type="button" data-d="wipe" data-ci="'+ci+'" title="Clear this lane">🗑</button></div>'; }).join('')
   :'<div class="kdNote">No automation yet. Put the console on Latch, press ▶ and move any fader or pan knob on the mixing board: the moves are recorded. Read plays them back.</div>'; }

 /* ================= the deck itself ================= */
 const TITLE={studio:'🎛 Studio deck',kara:'🎤 Karaoke deck',dj:'🎧 DJ deck'};
 const TABS={studio:[['edit','✏ Edit'],['file','📁 File'],['punch','✂ Punch'],['auto','📈 Automation'],['keys','⌨ Key map'],['steps','📖 Steps']],kara:[['take','🎙 Takes'],['file','📁 File'],['punch','✂ Punch'],['keys','⌨ Key map'],['steps','📖 Steps']],dj:[['decks','💿 Decks'],['fx','🎛 FX'],['file','📁 File'],['keys','⌨ Key map'],['steps','📖 Steps']]};
 /* 📖 the deck's own operating steps, button by button, for each screen */
 const STEPS={studio:[['Make a 4-bar beat and record it',['🥁 Pads opens the beat machine (or press 1 on the keyboard).','Loop 4 bars: ✏ Edit → ⏩ Double loop twice, or 4 in the beat machine’s BARS.','● starts the loop with the count-in and records what you hit; the left hand plays the pads (1 2 3 4 · Q W E R · A S D F · Z X C V).','■ stops; ↶ Undo takes back the last hit.']],
   ['Punch a new part into bars 3 to 4',['✂ Punch → ✂ Punch on.','In + / − to 3, Out + / − to 4; ⇄ Replace to wipe the old part there, 🔂 One pass to stop after it.','● Record bars 3–4: the loop plays from bar 1 and only bars 3 to 4 take the new part; the rest stays locked.','Choose 🎙 Microphone to sing the bars instead: the take is placed on bars 3 to 4.']],
   ['Copy a bar, insert a bar, move a section',['✏ Edit: Bar − / + picks the bar, the length picks how many.','⧉ Copy, then at − / + and 📋 Paste; ⧉ Duplicate puts the copy right after itself.','➕ Insert pushes the bars after it right and grows the loop; ➖ Delete closes the gap.','Ctrl/⌘ + Shift + C, X, V, D do the same from the keyboard; ↶ Undo reverses any edit.']],
   ['Record a fader move (mix automation)',['📈 Automation → mode 📈 Latch.','▶ plays; move any fader or pan knob on the mixing board (🎚 Console takes you there).','■ stops: the moves are kept. Mode 📈 Read plays them back and the faders move by themselves.','🔒 locks a lane, 🗑 clears it, 🅰 arms a strip for a full Write pass.']],
   ['Work on the console with every window open',['Open 🥁 🎹 🎧 🎤 🎼 from the window tabs: all of them live at once.','⤢ Tidy lays them side by side; drag a title bar to move one, its corner to size it.','A window’s tab (or its ▁) folds it away to reach the mixing board; the tab brings it back.','M and S on a window mute or solo its own strips; L on console strips links them into a fader group.']]],
  kara:[['Sing a take over the beat',['🎤 Karaoke pad: ▶ plays the song.','🎙 Record a take (or L on the keyboard), sing, ■ to finish; ↶ Undo take removes it.','⏺ Auto records the chosen number of bars by itself.']],
   ['Play pads and piano while singing',['Press any pad key (1 2 3 4 · Q W E R · A S D F · Z X C V): the pads come up over the song and play.','Press a piano key (Y U I O P [ ] \\ · 7 8 0 - =): the keyboard comes up and plays.','Both play on the song’s beat and land on their own strips of the mixing board.']],
   ['Punch a sung part into chosen bars',['✂ Punch → In and Out.','● Record bars …: the take starts on the In bar and stops after the Out bar, placed on those bars.']]],
  dj:[['Mix two tracks',['📁 Load deck A and 📁 Load deck B (or 📼 My beat on A / B).','A ▶ plays deck A; 🔗 syncs both to the beat; B ▶ starts deck B.','💿 Decks: slide the crossfader from A to B; ⇤ ⇹ ⇥ snap it.','● records the mix; 💥 lets the cannon auto-mix.']],
   ['The keyboard as a DJ controller',['Left hand 1 2 3 4 · Q W E R drive deck A, right hand 7 8 9 0 · U I O P drive deck B: hot cues, play, nudge.','🎛 FX → 🎧 Pads as DJ controller puts the 16 pads on the decks: cues, rolls, FX and the sampler.']]]};
 const stepsHTML=c=>(STEPS[c]||[]).map(([h,L],i)=>'<details class="kdHow"'+(i?'':' open')+'><summary>'+esc(h)+'</summary><ol>'+L.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ol></details>').join('');
 const ST=Object.assign({min:matchMedia('(max-width:700px)').matches,tab:{studio:'edit',kara:'take',dj:'decks'},pos:{}},getLS('kanin-deck1',{})); if(!ST.tab||typeof ST.tab!=='object') ST.tab={studio:'edit',kara:'take',dj:'decks'}; if(!ST.pos||typeof ST.pos!=='object') ST.pos={};
 const stSave=()=>putLS('kanin-deck1',{min:ST.min,tab:ST.tab,pos:ST.pos});
 const css=document.createElement('style'); css.textContent=`
#kDeck{position:fixed;z-index:9400;left:16px;bottom:calc(14px + env(safe-area-inset-bottom,0px));width:min(540px,calc(100vw - var(--kRailW,58px) - 32px));max-height:min(62vh,520px);overflow:auto;box-sizing:border-box;padding:6px 8px 8px;border-radius:14px;background:rgba(8,10,30,.97);border:1px solid rgba(255,233,74,.7);box-shadow:0 10px 34px rgba(0,0,0,.6),0 0 22px rgba(255,233,74,.18);color:#eef3ff;font:600 13px system-ui,sans-serif;touch-action:manipulation}
#kDeck[hidden]{display:none!important}
#kDeck .kdHead{display:flex;align-items:center;gap:8px;cursor:grab;user-select:none;padding:2px 2px 6px}
#kDeck .kdHead b{font:900 13px ui-monospace,monospace;letter-spacing:.08em;color:#ffe94a;text-transform:uppercase;white-space:nowrap}
#kDeck .kdLcd{flex:1;min-width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;padding:3px 8px;border-radius:6px;background:#bfd98a;color:#18220a;font:800 12.5px ui-monospace,monospace}
#kDeck .kdLcd.rec{background:#ff8a8a;color:#2a0000}
#kDeck button,#kDeck select{min-height:40px;border-radius:10px;padding:0 10px;font:800 13px system-ui,sans-serif;background:#1a1f45;color:#fff;border:1px solid #3a4280;cursor:pointer}
#kDeck button.on{background:#ffe94a;color:#14163a;border-color:#fff}
#kDeck button:focus-visible,#kDeck select:focus-visible{outline:3px solid #6fb8ff;outline-offset:1px}
#kDeck .kdT{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
#kDeck .kdT button{min-width:44px;font-size:16px}
#kDeck .kdT [data-d="play"]{background:#0f6b3a}#kDeck .kdT [data-d="stop"]{background:#6b1420}#kDeck .kdT [data-d="rec"]{background:#3a0f14;color:#ff6b6b}
#kDeck .kdT [data-d="rec"].on{background:#ff3b3b;color:#fff;box-shadow:0 0 12px #ff3b3b}
#kDeck .kdT .kdBpm{display:flex;align-items:center;gap:3px;margin-left:auto;font:800 12px ui-monospace,monospace}
#kDeck .kdT .kdBpm button{min-width:36px;font-size:15px;padding:0 6px}
#kDeck .kdWins{display:flex;flex-wrap:wrap;gap:4px;margin:7px 0 0;padding-top:6px;border-top:1px dashed #2c3470}
#kDeck .kdWins button{min-height:36px;font-size:12.5px;padding:0 9px}
#kDeck .kdWins .kdAdd{display:inline-flex;align-items:center;padding:0 6px;font:900 11.5px ui-monospace,monospace;letter-spacing:.06em;color:#ffe94a;text-transform:uppercase}
#kDeck .kdWins button.fold{background:#2a2350;border-style:dashed;color:#ffe94a}
#kDeck .kdTabs{display:flex;flex-wrap:wrap;gap:4px;margin:7px 0 6px}
#kDeck .kdTabs button{min-height:34px;font-size:12.5px;padding:0 9px;border-radius:999px}
#kDeck .kdPane{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
#kDeck .kdPane[hidden]{display:none}
#kDeck .kdStep{display:inline-flex;align-items:center;gap:2px;padding:0 4px;border-radius:10px;background:#0c1030;border:1px solid #2c3470}
#kDeck .kdStep b{min-width:56px;text-align:center;font:800 12.5px ui-monospace,monospace}
#kDeck .kdStep button{min-width:34px;padding:0 4px}
#kDeck .kdNote{flex-basis:100%;font:600 12.5px/1.5 system-ui,sans-serif;color:#c9d2ee}
#kDeck .kdLanes{flex-basis:100%;display:flex;flex-direction:column;gap:4px}
#kDeck .kdLane{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:4px 6px;border-radius:10px;background:#0c1030}
#kDeck .kdLane b{min-width:120px;font:800 12px ui-monospace,monospace;color:#9fe8ff}
#kDeck .kdLane span{display:inline-flex;align-items:center;gap:4px;font:700 10.5px ui-monospace,monospace;color:#8b95a7}
#kDeck .kdLane button{min-height:34px;min-width:36px;padding:0 6px}
#kDeck .kdKeys{flex-basis:100%;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:6px}
#kDeck .kdKeys div{padding:6px 8px;border-radius:10px;background:#0c1030;font:600 12px/1.55 system-ui,sans-serif}
#kDeck .kdKeys b{display:block;color:#ffe94a;font:900 12px system-ui,sans-serif;margin-bottom:2px}
#kDeck .kdKeys kbd{display:inline-block;min-width:16px;padding:0 4px;margin:1px;border-radius:4px;background:#f4f1e8;color:#14163a;font:800 11.5px ui-monospace,monospace;text-align:center}
#kDeck .kdHow{flex-basis:100%;padding:4px 8px;border-radius:10px;background:#0c1030}
#kDeck .kdHow summary{cursor:pointer;min-height:34px;display:flex;align-items:center;font:800 13px system-ui,sans-serif;color:#ffe94a}
#kDeck .kdHow ol{margin:4px 0 6px 18px;padding:0;font:600 12.5px/1.6 system-ui,sans-serif;color:#dfe6ff}
#kDeck input[type=range]{flex:1;min-width:120px;accent-color:#ffe94a}
#kDeck.min{width:auto;max-height:none;overflow:visible;padding:4px 6px}
#kDeck.min .kdBody{display:none}
#kDeck.min .kdHead{padding:0}
#kDeck.min .kdLcd{max-width:120px}
#kDeck.drag .kdHead{cursor:grabbing}
#padMixer .mxb [data-a="auto"]{min-width:22px}
#padMixer .mxb [data-a="auto"].kdHas{color:#00e5ff;border-color:#00e5ff}
#padMixer .mxb [data-a="auto"].kdArm{background:#ff3b3b!important;color:#fff!important}
@media (max-width:700px){ #kDeck{left:8px;width:calc(100vw - var(--kRailW,68px) - 16px);max-height:56vh} #kDeck.min{width:auto} }`; document.head.appendChild(css);
 const deck=document.createElement('div'); deck.id='kDeck'; deck.hidden=true; deck.setAttribute('role','region'); deck.setAttribute('aria-label','Control deck'); document.body.appendChild(deck);
 let CX=null;
 const step=(id,label,val)=>'<span class="kdStep" role="group" aria-label="'+esc(label)+'"><button type="button" data-d="'+id+'-" aria-label="'+esc(label)+' down">−</button><b>'+esc(val)+'</b><button type="button" data-d="'+id+'+" aria-label="'+esc(label)+' up">+</button></span>';
 const opt=(v,t,sel)=>'<option value="'+v+'"'+(String(v)===String(sel)?' selected':'')+'>'+esc(t)+'</option>';
 function transport(c){ if(c==='studio') return '<button type="button" data-d="rew" title="Back to bar 1 (H)">⏮</button><button type="button" data-d="play" title="Play or pause (J or Space)">▶</button><button type="button" data-d="stop" title="Stop (K)">■</button><button type="button" data-d="rec" title="Record (L): pads, keys, microphone, vocals or the whole mix">●</button><button type="button" data-d="loop" title="Loop on or off">🔁</button><span class="kdBpm"><button type="button" data-d="bpm-" aria-label="Tempo down">−</button><span data-v="bpm">90</span><span>BPM</span><button type="button" data-d="bpm+" aria-label="Tempo up">+</button></span>';
  if(c==='kara') return '<button type="button" data-d="krew" title="Back to the start (H)">⏮</button><button type="button" data-d="kplay" title="Play the song (J)">▶</button><button type="button" data-d="kpause" title="Pause">⏸</button><button type="button" data-d="kstop" title="Stop (K)">■</button><button type="button" data-d="krec" title="Record a take live (L)">●</button><button type="button" data-d="knext" title="Next song">⏭</button><button type="button" data-d="kauto" title="Auto-record the chosen number of bars">⏺ Auto</button>';
  return '<button type="button" data-d="aplay" title="Deck A: play or pause (J)">A ▶</button><button type="button" data-d="acue" title="Deck A: cue">A ⏮</button><button type="button" data-d="sync" title="Sync both decks to the beat">🔗</button><button type="button" data-d="bplay" title="Deck B: play or pause">B ▶</button><button type="button" data-d="bcue" title="Deck B: cue">B ⏮</button><button type="button" data-d="djrec" title="Record the mix (L)">●</button><button type="button" data-d="djauto" title="Auto-mix by the cannon">💥</button>'; }
 function pane(c,t){ clampSel();
  if(t==='edit') return step('from','Bar','Bar '+(SEL.from+1))+'<select data-d="len" data-die="off" aria-label="How many bars">'+[1,2,4,8,16,32].map(n=>opt(n,barsWord(n),SEL.len)).join('')+'</select><button type="button" data-d="copy" title="Copy (Ctrl/⌘+Shift+C)">⧉ Copy</button><button type="button" data-d="cut" title="Cut (Ctrl/⌘+Shift+X)">✂ Cut</button>'+step('at','Paste at','at '+(SEL.at+1))+'<button type="button" data-d="paste" title="Paste (Ctrl/⌘+Shift+V)">📋 Paste</button><button type="button" data-d="dup" title="Duplicate right after (Ctrl/⌘+Shift+D)">⧉ Duplicate</button><button type="button" data-d="ins">➕ Insert</button><button type="button" data-d="del">➖ Delete</button><button type="button" data-d="clr">🗑 Clear</button><button type="button" data-d="dbl">⏩ Double loop</button><button type="button" data-d="undo">↶ Undo</button><button type="button" data-d="tools" title="The channel rack’s step tools: draw, erase, select, velocity">✏ Step tools</button><div class="kdNote">Loop: '+barsWord(nBars())+(CLIP?' · clipboard: '+barsWord(CLIP.len):' · clipboard empty')+'. Bars move with their drums, notes, chords and mix automation.</div>';
  if(t==='file'){ if(c==='studio') return '<button type="button" data-d="new">🆕 New</button><button type="button" data-d="open">📂 Open project</button><button type="button" data-d="lib">📚 Library</button><button type="button" data-d="save">💾 Save project</button><button type="button" data-d="wav">⬇ Save WAV</button><button type="button" data-d="loadsnd" title="Load a sound onto the selected pad">📥 Load sound</button><button type="button" data-d="upload">⬆ Upload a sound</button><div class="kdNote">💾 Save project keeps every sound, loop, take and the mix automation in one file; 📂 Open project brings it all back.</div>';
   if(c==='kara') return '<button type="button" data-d="knew">🆕 New song</button><button type="button" data-d="klyr">⬇ Load lyrics</button><button type="button" data-d="kbeat">🥁 New beat</button><button type="button" data-d="lib">📚 Library</button><button type="button" data-d="kbounce">🧲 Bounce takes</button><button type="button" data-d="save">💾 Save project</button><button type="button" data-d="open">📂 Open project</button>';
   return '<button type="button" data-d="djnew">🆕 New DJ set</button><button type="button" data-d="djlib">📚 Library</button><button type="button" data-d="aload">📁 Load deck A</button><button type="button" data-d="bload">📁 Load deck B</button><button type="button" data-d="abeat">📼 My beat on A</button><button type="button" data-d="bbeat">📼 My beat on B</button>'; }
  if(t==='punch'){ const [,,a,b]=prange(); const w=recWhat(); const rw='<select data-d="recwhat" data-die="off" aria-label="What to record">'+[['pads','🥁 Pads'],['keys','🎹 Keys'],['mic','🎙 Microphone'],['vocals','🎤 Vocals over the loop'],['mix','🎚 The whole mix (WAV)']].map(([v,x])=>opt(v,x,w)).join('')+'</select>';
   return '<button type="button" data-d="pon" class="'+(PU.on?'on':'')+'" aria-pressed="'+PU.on+'">✂ Punch '+(PU.on?'on':'off')+'</button>'+step('pin','In bar','In '+a)+step('pout','Out bar','Out '+b)+'<button type="button" data-d="prep" class="'+(PU.rep?'on':'')+'" title="Replace wipes the old part between In and Out as you drop in">'+(PU.rep?'⇄ Replace':'➕ Overdub')+'</button><button type="button" data-d="ponce" class="'+(PU.once?'on':'')+'" title="Stop recording when the playhead leaves the Out bar">🔂 One pass</button>'+(c==='studio'?rw:'')+'<button type="button" data-d="prec" class="'+(recLamp?'on':'')+'">● Record bars '+a+(b>a?'–'+b:'')+'</button><div class="kdNote">'+(c==='kara'?'The take is sung from bar '+a+' to bar '+b+' over the same beat and lands on the vocal strip.':'With ✂ Punch on, ● plays from bar 1 and records only bars '+a+(b>a?'–'+b:'')+'; everything outside stays locked as it was. Pads and Keys drop in on the grid; Microphone and Vocals are recorded from bar '+a+' and placed on those bars.')+'</div>'; }
  if(t==='auto') return '<select data-d="amode" data-die="off" aria-label="Automation mode">'+MODES.map(([v,x])=>opt(v,'📈 '+x,AU.mode)).join('')+'</select><button type="button" data-d="amix">🎚 Show the console</button><button type="button" data-d="ashape">✏ Draw a shape</button><button type="button" data-d="alockall">🔒 Lock all</button><button type="button" data-d="aclear">🗑 Clear all</button><div class="kdNote">'+({off:'Off: the faders stay where you put them.',read:'Read: ▶ plays the recorded moves; the faders move by themselves.',touch:'Touch: hold a fader and move it while it plays; it writes while held and returns to the line when you let go.',latch:'Latch: your first move starts writing, and it keeps writing where you leave it until ■ Stop.',write:'Write: every 🅰 armed strip is written from ▶ to ■, then the deck goes to Touch.'})[AU.mode]+'</div><div class="kdLanes"></div>';
  if(t==='take') return '<button type="button" data-d="klive">🎙 Record live</button><button type="button" data-d="kundo">↶ Undo last take</button><button type="button" data-d="klayers">▶ Play the layers</button><button type="button" data-d="klstop">■ Stop the layers</button><button type="button" data-d="klayer">⏺ New layer</button><button type="button" data-d="kpads">🥁 Pads</button><button type="button" data-d="kkeys">🎹 Keys</button><button type="button" data-d="kdj">🎧 DJ decks</button><button type="button" data-d="kmix">🎚 Mixing board</button>';
  if(t==='decks') return '<label class="kdNote" style="flex-basis:auto">A</label><input type="range" min="0" max="100" value="'+xfVal()+'" data-d="xf" aria-label="Crossfader: deck A to deck B"><label class="kdNote" style="flex-basis:auto">B</label><button type="button" data-d="xfa">⇤ A</button><button type="button" data-d="xfc">⇹ Mid</button><button type="button" data-d="xfb">B ⇥</button><div class="kdNote">The crossfader blends deck A into deck B; ⇤ ⇹ ⇥ snap it. Each deck plays through its own strip on the mixing board (29 and 30), so the console automation records DJ moves too.</div>';
  if(t==='fx') return ['Echo throw','Filter sweep','Brake','Spinback','Stutter'].map(x=>'<button type="button" data-d="fx" data-fx="'+x+'">'+({'Echo throw':'🔊','Filter sweep':'🌊','Brake':'🛑','Spinback':'🌀','Stutter':'⚡'})[x]+' '+x+'</button>').join('')+'<button type="button" data-d="djpads">🎧 Pads as DJ controller</button><div class="kdNote">FX hit deck A (the deck playing, if only one is). 🎧 Pads as DJ controller puts the 16 pads on the decks: hot cues, rolls, FX and the sampler.</div>';
  if(t==='keys') return keyMap(c);
  if(t==='steps') return '<div class="kdNote">Every step names the button to press. The windows, the deck and the console are one studio: what one does, the others hear.</div>'+stepsHTML(c);
  return ''; }
 const kb=s=>s.split(' ').map(k=>'<kbd>'+esc(k)+'</kbd>').join('');
 function keyMap(c){ const L='<div><b>⌨ Left hand · the 16 pads</b>'+kb('1 2 3 4')+'<br>'+kb('Q W E R')+'<br>'+kb('A S D F')+'<br>'+kb('Z X C V')+'</div>';
  const R='<div><b>⌨ Right hand · the piano</b>white '+kb('Y U I O P [ ] \\')+'<br>black '+kb('7 8 0 - =')+'<br>octave '+kb(', .')+'</div>';
  const T='<div><b>⌨ Transport</b>'+kb('H')+' ⏮ '+kb('J')+' ▶ '+kb('K')+' ■ '+kb('L')+' ● '+kb(';')+' ↶<br>'+kb('Space')+' play / stop</div>';
  const E=c==='studio'?'<div><b>⌨ Edit bars</b>Ctrl/⌘ + Shift + '+kb('C')+' copy '+kb('X')+' cut '+kb('V')+' paste '+kb('D')+' duplicate<br>Ctrl/⌘ + '+kb('Z')+' undo</div>':c==='dj'?'<div><b>⌨ DJ decks</b>deck A '+kb('1 2 3 4 Q W E R')+'<br>deck B '+kb('7 8 9 0 U I O P')+'<br>'+kb('`')+' pads: beat ⇄ DJ</div>':'<div><b>⌨ Karaoke</b>the pads and the piano come up over the song at the first key; sing, hit and play together on one beat.</div>';
  const S='<div><b>⌨ Screens</b>Alt + '+kb('S')+' studio '+kb('K')+' karaoke '+kb('G')+' games<br>Alt + '+kb('/')+' every shortcut · '+kb('Esc')+' close</div>';
  return '<div class="kdKeys">'+L+R+T+E+S+'</div>'; }
 function xfVal(){ const x=$('djX'); return x?Math.round((+x.value-(+x.min||0))/((+x.max||100)-(+x.min||0))*100):50; }
 let built='';
 function paintDeck(){ const c=CX; if(!c) return; const tabs=TABS[c]; let t=ST.tab[c]; if(!tabs.some(x=>x[0]===t)) t=ST.tab[c]=tabs[0][0];
  const sig=c+'|'+t+'|'+ST.min+'|'+JSON.stringify(SEL)+'|'+PU.on+PU.inB+PU.outB+PU.rep+PU.once+recLamp+'|'+AU.mode+'|'+nBars()+'|'+(CLIP?CLIP.len:0)+'|'+recWhat()+'|'+(window.KWIN?KWIN.sig():'');
  if(sig===built){ lcd(); return; } built=sig;
  deck.className=ST.min?'min':''; deck.dataset.cx=c;
  deck.innerHTML='<div class="kdHead" title="Drag to move the deck"><b>'+TITLE[c]+'</b><span class="kdLcd" aria-live="off"></span><button type="button" data-d="fold" aria-label="'+(ST.min?'Open the deck':'Fold the deck')+'" title="'+(ST.min?'Open the deck':'Fold the deck')+'">'+(ST.min?'▴':'▾')+'</button></div><div class="kdBody"><div class="kdT" role="toolbar" aria-label="Transport">'+transport(c)+'</div>'+(window.KWIN?'<div class="kdWins" role="toolbar" aria-label="Windows: open, fold to a tab, bring back">'+KWIN.rowHTML(c)+'</div>':'')+'<div class="kdTabs" role="tablist">'+tabs.map(([k,x])=>'<button type="button" role="tab" data-tab="'+k+'" class="'+(k===t?'on':'')+'" aria-selected="'+(k===t)+'">'+x+'</button>').join('')+'</div><div class="kdPane" data-pane="'+t+'">'+pane(c,t)+'</div></div>';
  if(t==='auto') paintAuto(); place(); lcd(); }
 function lcd(){ const el=deck.querySelector('.kdLcd'); if(!el||!CX) return; let txt=''; let rec=false;
  if(CX==='studio'){ const P=PS(); const s=POS.s, n=spb(); const bar=Math.floor(s/n)+1, beat=Math.floor((s%n)/Math.max(1,n/4))+1; const pl=P&&P.playing;
   rec=recActive()||recLamp||(!!$('ktRec')&&$('ktRec').classList.contains('on')); const [,,a,b]=prange();
   txt=(pl?'▶ ':'■ ')+bar+'.'+beat+' / '+nBars()+' bars'+(rec?' · ● REC':'')+(PU.on?' · ✂ '+a+'–'+b:'')+(AU.mode!=='off'?' · 📈 '+AU.mode.toUpperCase():'');
   const v=deck.querySelector('[data-v="bpm"]'); const bp=$('padBpm'); if(v&&bp&&v.textContent!==bp.value) v.textContent=bp.value;
   const pb=deck.querySelector('[data-d="play"]'); if(pb){ pb.textContent=pl?'⏸':'▶'; pb.classList.toggle('on',!!pl); }
   const rb=deck.querySelector('.kdT [data-d="rec"]'); if(rb) rb.classList.toggle('on',rec);
   const lb=deck.querySelector('[data-d="loop"]'); const kl=$('ktLoop'); if(lb) lb.classList.toggle('on',!kl||kl.classList.contains('on')); }
  else if(CX==='kara'){ const a=[...document.querySelectorAll('#kKara audio,#kKara video')].find(m=>!m.paused); txt=a?'▶ '+fmt(a.currentTime)+' / '+fmt(a.duration||0):'■ ready'; let P; try{ P=PS(); }catch(_){ } if(P&&P.playing) txt+=' · beat ▶'; if(recLamp) { txt+=' · ● REC'; rec=true; } }
  else { let D=null; try{ D=DJBOOTH.D; }catch(_){ } const st=k=>D&&D[k]&&D[k].playing?'▶':'■'; txt='A '+st('A')+' · B '+st('B')+' · X '+xfVal()+'%'; const r=$('djRec'); if(r&&/■|Stop|recording/i.test(r.textContent)){ txt+=' · ● REC'; rec=true; } }
  if(el.textContent!==txt) el.textContent=txt; el.classList.toggle('rec',rec); }
 const fmt=x=>{ x=Math.max(0,+x||0); return Math.floor(x/60)+':'+String(Math.floor(x%60)).padStart(2,'0'); };
 /* dragging by the title bar; the place is remembered per screen */
 function place(){ const p=ST.pos[CX]; if(!p){ deck.style.left=''; deck.style.top=''; deck.style.bottom=''; return; } const r=deck.getBoundingClientRect(); const rw=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--kRailW'))||58;
  const x=Math.max(8,Math.min(innerWidth-rw-r.width-8,p.x)), y=Math.max(8,Math.min(innerHeight-Math.min(r.height,80)-8,p.y)); deck.style.left=x+'px'; deck.style.top=y+'px'; deck.style.bottom='auto'; }
 let dg=null; deck.addEventListener('pointerdown',e=>{ const h=e.target.closest('.kdHead'); if(!h||e.target.closest('button')) return; const r=deck.getBoundingClientRect(); dg={dx:e.clientX-r.left,dy:e.clientY-r.top,id:e.pointerId,moved:false}; try{ h.setPointerCapture(e.pointerId); }catch(_){ } });
 deck.addEventListener('pointermove',e=>{ if(!dg) return; const x=e.clientX-dg.dx, y=e.clientY-dg.dy; if(!dg.moved&&Math.abs(x-deck.getBoundingClientRect().left)+Math.abs(y-deck.getBoundingClientRect().top)<4) return; dg.moved=true; deck.classList.add('drag'); ST.pos[CX]={x,y}; place(); });
 const dEnd=()=>{ if(dg&&dg.moved) stSave(); dg=null; deck.classList.remove('drag'); }; deck.addEventListener('pointerup',dEnd); deck.addEventListener('pointercancel',dEnd);
 deck.addEventListener('dblclick',e=>{ if(e.target.closest('.kdHead')&&!e.target.closest('button')){ delete ST.pos[CX]; stSave(); place(); say('🎛 The deck is back in its corner.'); } });

 /* ================= every button, wired to the screen's own engine ================= */
 const kara=()=>$('kKara'), djs=()=>$('djSec');
 const deckBtn=(d,re)=>btn($('deck'+d),re);
 const bpmStep=d=>{ const b=$('padBpm'); if(!b) return; b.value=String(Math.max(40,Math.min(240,(+b.value||90)+d))); b.dispatchEvent(new Event('input',{bubbles:true})); b.dispatchEvent(new Event('change',{bubbles:true})); };
 const xfSet=v=>{ const x=$('djX'); if(!x) return say('Open the 🎧 DJ decks first.'); const lo=+x.min||0, hi=+x.max||100; x.value=String(lo+(hi-lo)*v/100); x.dispatchEvent(new Event('input',{bubbles:true})); x.dispatchEvent(new Event('change',{bubbles:true})); };
 const deckHas=k=>{ try{ return !!DJBOOTH.D[k].buf; }catch(_){ return false; } };
 /* a karaoke button that only changes the page's status line says so on the deck too */
 const karaSays=fb=>{ const m=document.querySelector('#kKara .kkMsg'); const t0=m?m.textContent:''; setTimeout(()=>{ const t1=m?m.textContent:''; say(t1&&t1!==t0?t1:fb); },250); };
 function karaDev(re,what){ const ok=clickBtn(kara(),re); if(!ok) say('Open 🎤 Karaoke first.'); return ok; }
 function act(d,el){ const P=PS();
  switch(d){
   case 'fold': ST.min=!ST.min; stSave(); built=''; paintDeck(); return;
   case 'rew': if(!press('ktRew')){ try{ P.stop(); }catch(_){ } } POS.s=0; break;
   case 'play': if(P.playing){ if(!press('padStop')) P.stop(); } else { if(!press('padPlay')) P.play(); } break;
   case 'stop': if(!press('ktStop')){ try{ P.stop(); }catch(_){ } } if(VP){ try{ VP.st.getTracks().forEach(x=>x.stop()); }catch(_){ } VP=null; setRecLamp(false); } break;
   case 'rec': case 'prec': recPress(d==='prec'); break;
   case 'loop': if(!press('ktLoop')) say('The loop switch is on the studio transport.'); break;
   case 'bpm-': bpmStep(-1); break; case 'bpm+': bpmStep(1); break;
   case 'from-': if(SEL.from<=0) say('Bar 1 is the first bar of the loop.'); SEL.from--; break; case 'from+': if(SEL.from>=nBars()-1) say('Bar '+nBars()+' is the last bar of the loop. ⏩ Double loop or ➕ Insert makes it longer.'); SEL.from++; break;
   case 'at-': if(SEL.at<=0) say('Bar 1 is the first bar of the loop.'); SEL.at--; break; case 'at+': if(SEL.at>=nBars()-1) say('Bar '+nBars()+' is the last bar of the loop.'); SEL.at++; break;
   case 'copy': ED.copy(); break; case 'cut': ED.cut(); break; case 'paste': ED.paste(); break; case 'dup': ED.dup(); break;
   case 'ins': ED.insert(); break; case 'del': ED.del(); break; case 'clr': ED.clear(); break; case 'dbl': ED.double(); break;
   case 'undo': try{ if(!KUNDO.count){ say('Nothing to undo yet: every edit made here can be taken back, one at a time.'); break; } KUNDO.any(); }catch(_){ press('kUndoAll'); } break;
   case 'tools': try{ if(window.KSEQTOOLS&&KSEQTOOLS.open) KSEQTOOLS.open(); else { const g=$('padSteps')||$('padGrid'); g&&g.scrollIntoView({behavior:'smooth',block:'center'}); } }catch(_){ } say('✏ The step tools are on the channel rack: draw, erase, select a block, velocity, copy and paste steps.'); break;
   case 'new': clickBtn(document.querySelector('.kBar[data-sc="pad"]'),/New/)||say('Press 🆕 New on the studio bar.'); break;
   case 'lib': { const sc=CX==='kara'?null:document.querySelector('.kBar[data-sc="pad"]'); if(!(sc&&clickBtn(sc,/Library/))){ try{ KPROJ.open(); }catch(_){ say('Open 📁 Projects from the rail.'); } } break; }
   case 'open': press('padOpen')||say('Open the 🎛 Studio first.'); break;
   case 'save': press('padProj')||say('Open the 🎛 Studio first.'); break;
   case 'wav': press('padWav'); break;
   case 'loadsnd': case 'upload': { const go=()=>{ const ok=d==='loadsnd'?(clickBtn($('mpcBar'),/^⬇\s*LOAD/)||clickBtn($('mpcBar'),/All sounds/)):clickBtn($('mpcBar'),/UPLOAD|Upload my/); say(ok?(d==='loadsnd'?'📥 Pick a sound for the selected pad from the beat machine’s sound drawer.':'⬆ Choose a sound file: it lands on the selected pad.'):'Open the 🥁 Pads first.'); }; if(!isOpen('pads')){ try{ KRAIL.FLOAT.open('pads'); }catch(_){ } setTimeout(go,350); } else go(); break; }
   case 'pon': PU.on=!PU.on; if(PU.on&&nBars()<2) say('✂ Punch is on. The loop is 1 bar long, so In and Out are bar 1: make the loop longer to punch a part of it.'); else say(PU.on?'✂ Punch is on: ● records only the bars between In and Out.':'✂ Punch is off: ● records the whole loop.'); break;
   case 'pin-': if(PU.inB<=1) say('In is already bar 1.'); PU.inB=Math.max(1,PU.inB-1); break; case 'pin+': PU.inB=Math.min(nBars(),PU.inB+1); if(PU.outB<PU.inB) PU.outB=PU.inB; break;
   case 'pout-': PU.outB=Math.max(1,PU.outB-1); if(PU.inB>PU.outB) PU.inB=PU.outB; break; case 'pout+': if(PU.outB>=nBars()) say('Out is already the last bar ('+nBars()+'). Make the loop longer to punch further.'); PU.outB=Math.min(nBars(),PU.outB+1); break;
   case 'prep': PU.rep=!PU.rep; say(PU.rep?'⇄ Replace: the old part between In and Out is wiped as the take drops in.':'➕ Overdub: the take is added on top of what is there.'); break;
   case 'ponce': PU.once=!PU.once; break;
   case 'amix': { const m=$('padMixer'); if(m) m.scrollIntoView({behavior:'smooth',block:'start'}); break; }
   case 'ashape': { const a=$('autoCv'); if(a) a.scrollIntoView({behavior:'smooth',block:'center'}); say('✏ Draw a channel’s volume across the loop with your finger or mouse; it multiplies with the recorded moves.'); break; }
   case 'alockall': { const ids=Object.keys(AU.ch).filter(k=>hasData(AU.ch[k])); const all=ids.every(k=>AU.ch[k].lock); ids.forEach(k=>AU.ch[k].lock=!all); auSave(); paintAuto(); say(ids.length?(all?'🔓 Every lane is open for writing.':'🔒 Every lane is locked: nothing writes over them.'):'There is no automation to lock yet.'); break; }
   case 'aclear': { const o=auClone(); AU.ch={}; auSave(); paintAuto(); strips(); try{ KUNDO.push(()=>{ AU.ch=o; auSave(); paintAuto(); strips(); },'mix automation'); }catch(_){ } say('🗑 Every automation lane is clear. ↶ Undo brings them back.'); break; }
   case 'arm': case 'lock': case 'wipe': { const ci=+el.dataset.ci; const L=lane(ci); if(d==='arm') L.arm=!L.arm; if(d==='lock') L.lock=!L.lock; if(d==='wipe'){ const o={v:L.v.slice(),p:L.p.slice()}; L.v.fill(null); L.p.fill(null); try{ KUNDO.push(()=>{ L.v=o.v; L.p=o.p; auSave(); paintAuto(); },'an automation lane'); }catch(_){ } } auSave(); paintAuto(); strips(); return; }
   case 'krew': karaDev(/^⏮$/); break; case 'kplay': karaDev(/^▶ Play$/); break; case 'kpause': karaDev(/^⏸ Pause$/); break; case 'kstop': karaDev(/^■ Stop$/); break;
   case 'knext': karaDev(/^⏭ Next song/); karaSays('⏭ The next song in the list is loaded.'); break; case 'kauto': karaDev(/Auto-record$/); break; case 'krec': case 'klive': karaDev(/^🎙 Record live/); break;
   case 'kundo': { let n0=0; try{ n0=KKARA.takes().length; }catch(_){ } if(!n0){ say('There is no take to undo yet: 🎙 Record live makes one.'); break; } karaDev(/^↶ Undo last take/); break; }
   case 'klayers': { let n0=0; try{ n0=KKARA.takes().length; }catch(_){ } if(!n0){ say('There are no layers yet: record a take or ⏺ New layer first.'); break; } karaDev(/^▶ Play the layers$/); break; } case 'klstop': karaDev(/^■ Stop the layers/); break; case 'klayer': karaDev(/^⏺ Record a new/); break;
   case 'kpads': karaDev(/^🥁 Pads$/); break; case 'kkeys': karaDev(/^🎹 Keys$/); break; case 'kdj': karaDev(/^🎧 DJ decks$/); break; case 'kmix': karaDev(/^🎚 Mixing board$/); say('🎚 The mixing board: every take is on its microphone strip, every device on its own strip.'); break;
   case 'knew': { const ta=kara()&&kara().querySelector('textarea'); if(ta){ const o=ta.value; ta.value=''; ta.dispatchEvent(new Event('input',{bubbles:true})); try{ KUNDO.push(()=>{ ta.value=o; ta.dispatchEvent(new Event('input',{bubbles:true})); },'the lyrics'); }catch(_){ } ta.focus(); say('🆕 A new song: type, paste or speak the lyrics. ↶ Undo brings the old ones back.'); } break; }
   case 'klyr': karaDev(/^⬇ Load these lyrics/); break; case 'kbeat': karaDev(/^💥 New beat/); break; case 'kbounce': karaDev(/^🧲 Bounce/); break;
   case 'aplay': deckBtn('A',/^(▶ Play|⏸ Pause|⏸)/)?deckBtn('A',/^(▶ Play|⏸ Pause|⏸)/).click():say('Open the 🎧 DJ decks first.'); break;
   case 'bplay': deckBtn('B',/^(▶ Play|⏸ Pause|⏸)/)?deckBtn('B',/^(▶ Play|⏸ Pause|⏸)/).click():say('Open the 🎧 DJ decks first.'); break;
   case 'acue': case 'bcue': { const k=d==='acue'?'A':'B'; if(!deckHas(k)){ say('Deck '+k+' is empty: 📁 File → Load deck '+k+' (or 📼 My beat on '+k+') first.'); break; } (deckBtn(k,/Cue$/)||{click(){}}).click(); say('⏮ Deck '+k+' is back on its cue point.'); break; }
   case 'sync': { const a=deckBtn('A',/^🔗 Sync/), b=deckBtn('B',/^🔗 Sync/); a&&a.click(); b&&b.click(); say('🔗 Both decks follow the studio tempo.'); break; }
   case 'djrec': press('djRec'); break; case 'djauto': press('djAuto'); break;
   case 'xfa': xfSet(0); break; case 'xfc': xfSet(50); break; case 'xfb': xfSet(100); break;
   case 'djnew': clickBtn(djs(),/New DJ set/); break; case 'djlib': clickBtn(djs(),/^📚 Library/); break;
   case 'aload': (deckBtn('A',/Load a track/)||{click(){}}).click(); break; case 'bload': (deckBtn('B',/Load a track/)||{click(){}}).click(); break;
   case 'abeat': (deckBtn('A',/Load my beat/)||{click(){}}).click(); break; case 'bbeat': (deckBtn('B',/Load my beat/)||{click(){}}).click(); break;
   case 'fx': { let D=null; try{ D=DJBOOTH.D; }catch(_){ } if(!(D&&((D.A&&D.A.playing)||(D.B&&D.B.playing)))){ say('🎛 '+el.dataset.fx+' works on a playing deck: load a track and press A ▶ or B ▶ first.'); break; } const side=D&&D.B&&D.B.playing&&!(D.A&&D.A.playing)?'B':'A'; const f=btn($('deck'+side),new RegExp('^'+el.dataset.fx+'$'))||btn(djs(),new RegExp('^'+el.dataset.fx+'$')); if(f) f.click(); else say('Open the 🎧 DJ decks first.'); break; }
   case 'djpads': try{ KWIRE.setMode(KWIRE.mode==='beat'?'cue':'beat'); say(KWIRE.mode==='beat'?'🥁 The pads play the beat machine again.':'🎧 The pads drive the decks: deck A on the top rows, deck B on the bottom rows.'); }catch(_){ } break;
  }
  paintDeck(); }
 function recPress(fromPunch){ const P=PS(); if(fromPunch&&!PU.on){ PU.on=true; }
  if(PU.on&&CX==='kara'){ return vocalPunch(); }
  if(PU.on&&(recWhat()==='mic'||recWhat()==='vocals')){ return vocalPunch(); }
  if(PU.on){ const [,,a,b]=prange(); if(!P.playing){ /* start from the top so the take drops in on its bar */ } press('ktRec')||press(recWhat()==='keys'?'kbRec':'padRecLive'); say('● Recording with ✂ Punch: only bars '+a+(b>a?'–'+b:'')+' take the new part.'); return; }
  press('ktRec')||press('padRecLive'); }
 deck.addEventListener('click',e=>{ const wb=e.target.closest('[data-w]'); if(wb){ e.stopPropagation(); try{ KWIN.tab(wb.dataset.w); }catch(_){ } built=''; setTimeout(()=>{ built=''; paintDeck(); },120); setTimeout(()=>{ built=''; paintDeck(); },900); return; } const tb=e.target.closest('[data-tab]'); if(tb){ e.stopPropagation(); ST.tab[CX]=tb.dataset.tab; stSave(); built=''; paintDeck(); return; } const b=e.target.closest('button[data-d]'); if(!b) return; e.stopPropagation(); act(b.dataset.d,b); puSave(); });
 deck.addEventListener('change',e=>{ const t=e.target; e.stopPropagation(); if(t.dataset.d==='len'){ SEL.len=+t.value; } if(t.dataset.d==='amode'){ AU.mode=t.value; latched.clear(); auSave(); say('📈 Automation: '+t.options[t.selectedIndex].text.replace('📈 ','')+'.'); }
  if(t.dataset.d==='recwhat'){ const r=$('ktRecWhat'); if(r){ r.value=t.value; r.dispatchEvent(new Event('change',{bubbles:true})); } } built=''; paintDeck(); });
 deck.addEventListener('input',e=>{ const t=e.target; if(t.dataset.d==='xf'){ e.stopPropagation(); xfSet(+t.value); lcd(); } });

 /* ================= the split keyboard on Karaoke and the DJ ================= */
 const PADC=['Digit1','Digit2','Digit3','Digit4','KeyQ','KeyW','KeyE','KeyR','KeyA','KeyS','KeyD','KeyF','KeyZ','KeyX','KeyC','KeyV'];
 const PIANOC={KeyY:0,Digit7:1,KeyU:2,Digit8:3,KeyI:4,KeyO:5,Digit0:6,KeyP:7,Minus:8,BracketLeft:9,Equal:10,BracketRight:11,Backslash:12};
 const DJBC=['Digit7','Digit8','Digit9','Digit0','KeyU','KeyI','KeyO','KeyP'];
 const TKEYS={KeyH:'rew',KeyJ:'play',KeyK:'stop',KeyL:'rec',Semicolon:'undo'};
 const typing=t=>t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable);
 const heldK=new Map();
 addEventListener('keydown',e=>{ if(e.ctrlKey||e.metaKey||e.altKey||e.shiftKey||typing(e.target)) return; const c=CX; const code=e.code||'';
  /* 🎛 the studio starts with no device windows: the first pad key brings the pads up and plays, the first piano key brings the keyboard up */
  if(c==='studio'){ if(e.repeat) return; const p=PADC.indexOf(code); let djp=false; try{ djp=KWIRE.mode!=='beat'; }catch(_){ }
   if(p>=0&&!isOpen('pads')&&!djp){ e.preventDefault(); e.stopImmediatePropagation(); try{ KRAIL.FLOAT.open('pads'); }catch(_){ } say('🥁 The pads are added: your left hand plays them (1 2 3 4 · Q W E R · A S D F · Z X C V).'); setTimeout(()=>{ try{ const bank=Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0)); PADSTUDIO.hitPad(bank*16+p); }catch(_){ } },300); return; }
   if((code in PIANOC)&&!isOpen('keys')&&!heldK.has(code)){ e.preventDefault(); e.stopImmediatePropagation(); const n=PIANOC[code]; heldK.set(code,n); try{ KRAIL.FLOAT.open('keys'); }catch(_){ } say('🎹 The keyboard is added: your right hand plays it.'); setTimeout(()=>{ try{ KEYS.down(n); }catch(_){ } },300); return; }
   return; }
  if(c!=='kara'&&c!=='dj') return;
  const over=document.body.classList.contains('kDevOver')||($('pad')&&$('pad').classList.contains('on'));
  /* the transport keys drive this screen's own transport when no device window owns them */
  if(TKEYS[code]&&!(isOpen('pads')||isOpen('keys'))){ if(e.repeat) return; const a=TKEYS[code]; const map=c==='kara'?{rew:'krew',play:'kplay',stop:'kstop',rec:'krec',undo:'kundo'}:{rew:'acue',play:'aplay',stop:'aplay',rec:'djrec',undo:'undo'};
   if(c==='dj'&&a==='stop'){ let D=null; try{ D=DJBOOTH.D; }catch(_){ } ['A','B'].forEach(k=>{ if(D&&D[k]&&D[k].playing){ const b=deckBtn(k,/^(⏸ Pause|⏸)/); b&&b.click(); } }); }
   else act(map[a]); e.preventDefault(); e.stopImmediatePropagation(); flashDeck(map[a]); return; }
  /* 🎧 the DJ: deck A on the left hand, deck B on the right hand, at once */
  if(c==='dj'&&!isOpen('pads')){ const a=PADC.slice(0,8).indexOf(code), b=DJBC.indexOf(code); if(a>=0||b>=0){ e.preventDefault(); e.stopImmediatePropagation(); if(e.repeat) return; try{ if(KWIRE.mode==='beat') KWIRE.setMode('cue'); KWIRE.act(a>=0?a:8+b); }catch(_){ } return; } }
  if(c!=='kara') return; /* a device that is already up plays through the split keyboard itself; one that is not comes up here */
  /* 🎤 Karaoke: the first pad key brings the pads up over the song and plays; the first piano key brings the keys up and plays */
  const p=PADC.indexOf(code); if(p>=0){ e.preventDefault(); e.stopImmediatePropagation(); if(e.repeat) return; if(!isOpen('pads')){ karaDev(/^🥁 Pads$/); say('🥁 The pads are up over the song: your left hand plays them.'); } setTimeout(()=>{ try{ const bank=Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0)); PADSTUDIO.hitPad(bank*16+p); }catch(_){ } },isOpen('pads')?0:450); return; }
  if(code in PIANOC){ e.preventDefault(); e.stopImmediatePropagation(); if(e.repeat||heldK.has(code)) return; const n=PIANOC[code]; heldK.set(code,n); const play=()=>{ try{ KEYS.down(n); }catch(_){ } }; if(!isOpen('keys')){ karaDev(/^🎹 Keys$/); say('🎹 The keys are up over the song: your right hand plays them.'); setTimeout(play,450); } else play(); } },true);
 addEventListener('keyup',e=>{ const code=e.code||''; if(heldK.has(code)){ const n=heldK.get(code); heldK.delete(code); setTimeout(()=>{ try{ KEYS.up(n); }catch(_){ } },20); } },true);
 const flashDeck=d=>{ const b=deck.querySelector('[data-d="'+d+'"]'); if(b){ b.classList.add('on'); setTimeout(()=>b.classList.remove('on'),160); } };

 /* ================= keep the deck on the right screen ================= */
 let djO=false;
 setInterval(()=>{ tryHook(); const dO=isOpen('dj'); if(dO&&!djO) LASTWIN='dj'; djO=dO; const c=ctx(); if(c!==CX){ CX=c; built=''; } deck.hidden=!c; if(c) paintDeck(); },400);
 setInterval(()=>{ if(CX) lcd(); },200);
 window.KDECK={get cx(){ return CX; },act,ED,PU,AU,get CLIP(){ return CLIP; },get SEL(){ return SEL; },vocalPunch,lane,paintDeck,auPack,auUnpack,prange};
})();
