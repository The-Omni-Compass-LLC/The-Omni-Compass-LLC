(()=>{ /* 🎼 TRACK SEQUENCER (v242), built the way Reason, an MPC and a Triton link their tracks: every track is its own instrument
   with its own sound, and the controller you play (the 16 pads or the keyboard) is routed to the track you select.
     • PAD TRACKS A, B, C and D are the beat machine's four banks. Each holds its own 16 sounds and its own recorded hits, so
       Pads A can be a drum kit, Pads B a bass, Pads C strings and Pads D vocal chops, all playing together. Select a pad track
       and the 16 pads switch to that bank: what you hit plays its sounds and records onto it. The name shows what is loaded.
     • KEYBOARD TRACKS, as many as you like. Each keeps its own sound: one of the keyboard's instruments or any sound from the
       🗂 SOUNDS browser (a recorded violin, a choir, an 808, your own upload). Select one and the keyboard plays its sound and
       records onto it; select another and the keyboard moves there with that track's sound.
   ● REC records the selected track in real time (or on the grid when 🧲 Q is on); every pass of the loop adds to it (overdub).
   Every track plays back with its OWN sound, whatever is loaded on the pads or keys later, from one clock: M mutes, S solos
   (pad tracks mute and solo in the WAV export too), Q snaps a track to the grid, 🗑 clears it, ✕ removes a keyboard track,
   tap a note to delete it, and ↶ Undo brings any of it back. Saved on this device.
   THE MIXING BOARD: every track has its own strip (CH on each track): Pads A on strips 1–16 (one per pad), Pads B on 17,
   the first keyboard track on 18 (the keyboard's own), Pads C, Pads D and every other keyboard track on strips 41 and up, each
   named for what is loaded on it. The 🎤 Karaoke takes ride the same timeline as audio tracks on their microphone strips (24–28). */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PS=()=>window.PADSTUDIO; const BK='ABCD';
 const COLORS=['#ff7ad9','#6fe8ff','#ffd166','#7dffb0','#b98cff','#ff9f6b','#9fd0ff','#ffe94a'];
 const ICON={piano:'🎹',epiano:'🎹',organ:'🎹',strings:'🎻',harp:'🪕',guitar:'🎸',brass:'🎺',flute:'🪈',bells:'🔔',marimba:'🔔',vibes:'🔔',kalimba:'🔔',pad:'🌫',lead:'🎛',pluck:'🎛',chip:'👾',bass:'🎸',choir:'🗣'};
 const instName=v=>{ const p=$('kbPre'); const o=p&&[...p.options].find(x=>x.value===v); return o?o.text:v; };
 /* ---------- the tracks ---------- */
 const stored=getLS('kanin-seq-tracks',null);
 let tracks=Array.isArray(stored)?stored:[];
 const oldDrums=tracks.find(t=>t.id==='drums');
 const pads4=[0,1,2,3].map(b=>tracks.find(t=>t.kind==='pads'&&t.bank===b)||{id:'p'+BK[b],kind:'pads',bank:b,mute:!!(b===0&&oldDrums&&oldDrums.mute),solo:!!(b===0&&oldDrums&&oldDrums.solo)});
 let keys0=tracks.filter(t=>t.kind==='keys');
 if(!stored||!keys0.length) keys0=[{id:'k1',kind:'keys',sound:{type:'preset',v:'piano'},notes:[],vol:1},{id:'k2',kind:'keys',sound:{type:'preset',v:'bass'},notes:[],vol:1}].map(n=>{ const o=keys0.find(t=>t.id===n.id); return o||n; });
 keys0.forEach(t=>{ t.notes=Array.isArray(t.notes)?t.notes:[]; t.vol=t.vol==null?1:t.vol; t.takes=[]; if(!t.sound) t.sound={type:'preset',v:t.preset||'piano'}; delete t.preset; });
 tracks=pads4.concat(keys0);
 const padT=()=>tracks.filter(t=>t.kind==='pads'); const keysT=()=>tracks.filter(t=>t.kind==='keys'); const byId=id=>tracks.find(t=>t.id===id);
 let selKeys=getLS('kanin-seq-armed','k1'); if(!byId(selKeys)||byId(selKeys).kind!=='keys') selKeys=(keysT()[0]||{}).id;
 let selPad='p'+BK[Math.max(0,Math.min(3,+(($('padBank')||{}).value)||0))];
 let focus=getLS('kanin-seq-focus',selKeys); if(!byId(focus)) focus=selKeys;
 let saveT=0; const save=()=>{ clearTimeout(saveT); saveT=setTimeout(()=>{ putLS('kanin-seq-tracks',tracks.map(t=>{ const o=Object.assign({},t); delete o.takes; delete o.name; return o; })); putLS('kanin-seq-armed',selKeys); putLS('kanin-seq-focus',focus); },400); }; save();
 const audible=t=>{ const solo=tracks.some(x=>x.solo)||kTakes().some(x=>x.solo); return !t.mute&&(!solo||t.solo); };
 /* ---------- the mixing board: a strip for every track ---------- */
 let CH={};
 function chans(){ const used=new Set(); try{ (window.SQITR||[]).forEach((t,i)=>used.add(K40.slot(i))); }catch(_){ } const m={pA:0,pB:16}; let c=40; const next=()=>{ while(used.has(c)) c++; return c++; }; m.pC=next(); m.pD=next(); keysT().forEach((t,j)=>{ m[t.id]=j===0?17:next(); }); CH=m; return m; }
 window.KPADCH=i=>{ const b=Math.floor(i/16); return b===1?16:b===2?CH.pC:b===3?CH.pD:16; };
 window.KCHNAMES=n=>{ const out=n.slice(); const put=(ci,nm)=>{ if(ci==null) return; while(out.length<=ci) out.push('➕ Track '+(out.length+1)); out[ci]=nm; }; padT().forEach(t=>{ if(t.bank) put(CH[t.id],nameOf(t)); }); keysT().forEach((t,j)=>put(CH[t.id],j===0?'Keyboard · '+nameOf(t).replace(/^\S+\s/,''):nameOf(t))); return out; };
 let chSig=''; function chSync(){ chans(); let sig=''; try{ sig=JSON.stringify(CH)+tracks.map(t=>nameOf(t)).join('|'); }catch(_){ } if(sig!==chSig){ chSig=sig; try{ PS().renderMixer(); }catch(_){ } } }
 const chLabel=t=>{ if(t.kind==='pads'&&t.bank===0) return 'CH 1–16'; const c=CH[t.id]; return c==null?'':'CH '+(c+1); };
 /* ---------- the Karaoke takes: audio tracks on the same timeline ---------- */
 const kTakes=()=>{ try{ return (window.KKARA&&KKARA.takes())||[]; }catch(_){ return []; } };
 const rows=()=>tracks.concat(kTakes().map((k,i)=>({id:'kt'+i,kind:'take',take:k,ti:i})));
 /* ---------- each track's own sound ---------- */
 const IDB=(()=>{ let dbp=null; const open=()=>dbp||(dbp=new Promise((res,rej)=>{ try{ const r=indexedDB.open('kanin-seq',1); r.onupgradeneeded=()=>r.result.createObjectStore('smp'); r.onsuccess=()=>res(r.result); r.onerror=()=>rej(r.error); }catch(e){ rej(e); } }));
  return { put:async(k,v)=>{ try{ const db=await open(); await new Promise((res,rej)=>{ const tx=db.transaction('smp','readwrite'); tx.objectStore('smp').put(v,k); tx.oncomplete=res; tx.onerror=()=>rej(tx.error); }); return true; }catch(_){ return false; } },
   get:async k=>{ try{ const db=await open(); return await new Promise((res,rej)=>{ const q=db.transaction('smp').objectStore('smp').get(k); q.onsuccess=()=>res(q.result||null); q.onerror=()=>rej(q.error); }); }catch(_){ return null; } } }; })();
 const BUF=new Map(), PEND=new Map();
 const rootOf=name=>{ const m=String(name||'').match(/(?:^|[^A-Za-z])([A-G])(#|b|s)?-?\d(?!\d)/); if(!m) return 60; const pc={C:0,D:2,E:4,F:5,G:7,A:9,B:11}[m[1]]+(m[2]==='#'||m[2]==='s'?1:m[2]==='b'?-1:0); return 60+((pc%12)+12)%12; };
 function resolveBuf(t){ if(!t||t.sound.type!=='sample') return Promise.resolve(null); if(BUF.has(t.id)) return Promise.resolve(BUF.get(t.id)); if(PEND.has(t.id)) return PEND.get(t.id);
  const src=t.sound.src||{}; const p=(async()=>{ let b=null; try{
   if(src.t==='lib'){ const it=(SNDLIB.items||[]).find(x=>x.cat===src.cat&&x.name===src.name); if(it) b=await SNDLIB.render(it); }
   else if(src.t==='rec'){ const R=await VCSL.load(); const it=(R||VCSL.list()||[]).find(x=>x.p===src.p&&x.k===src.k); if(it) b=await VCSL.get(it); }
   else if(src.t==='upload'&&src.key){ const ab=await IDB.get(src.key); if(ab) b=await PS().ac().decodeAudioData(ab.slice(0)); } }catch(_){ }
   if(b) BUF.set(t.id,b); PEND.delete(t.id); return b; })(); PEND.set(t.id,p); return p; }
 function smpVoice(c,dest,at,buf,m,root,vel,len){ const s=c.createBufferSource(); s.buffer=buf; s.playbackRate.value=Math.pow(2,(m-root)/12); const g=c.createGain(); g.gain.setValueAtTime(0,at); g.gain.linearRampToValueAtTime(.9*vel,at+.003); g.gain.setValueAtTime(.9*vel,at+len); g.gain.linearRampToValueAtTime(0,at+len+.25); s.connect(g); g.connect(dest); s.start(at); s.stop(at+len+.3); }
 let quiet=false; const setSel=(id,v,ev)=>{ const s=$(id); if(!s||![...s.options].some(o=>o.value===String(v))) return false; if(s.value===String(v)) return true; quiet=true; s.value=String(v); (ev||['input','change']).forEach(e=>s.dispatchEvent(new Event(e,{bubbles:true}))); quiet=false; return true; };
 /* put a keyboard track's sound on the keyboard */
 async function loadOnKeys(t){ if(!t||t.kind!=='keys') return; if(t.sound.type==='preset'){ setSel('kbPre',t.sound.v); return; } const b=await resolveBuf(t); if(!b){ say('🎙 '+t.sound.name+' did not load. Pick its sound again in 🗂 SOUNDS.'); return; } if(selKeys!==t.id) return; try{ KEYS.setSample(b); }catch(_){ } setSel('kbRoot',t.sound.root||60,['change']); setSel('kbPre','sample'); }
 /* ---------- names: what is loaded on each track ---------- */
 function padNames(b){ const P=PS(); const names=[]; if(!P||!P.pads) return names; for(let j=0;j<16;j++){ const pd=P.pads[b*16+j]; const n=pd&&String(pd.name||'').trim(); if(n&&!names.includes(n)) names.push(n); } return names; }
 function nameOf(t){ if(t.kind==='pads'){ const ns=padNames(t.bank), sig=ns.join('|'); const what=t.label&&t.sig===sig?t.label:(ns.slice(0,3).join(', ')+(ns.length>3?'…':'')); return '🥁 Pads '+BK[t.bank]+(what?' · '+what:''); }
  return t.sound.type==='sample'?'🎙 '+t.sound.name:(ICON[t.sound.v]||'🎹')+' '+instName(t.sound.v); }
 const names=()=>tracks.forEach(t=>{ t.name=nameOf(t); });
 const hitsOf=t=>{ const P=PS(); let n=0; if(!P||!P.pads) return 0; const T=P.total||16; for(let j=0;j<16;j++){ const pd=P.pads[t.bank*16+j]; if(!pd) continue; (pd.steps||[]).forEach((v,s)=>{ if(v&&s<T) n++; }); n+=(pd.xh||[]).length; } return n; };
 /* ---------- the keyboard records into its selected track ---------- */
 function target(){ const t=byId(selKeys); window.KTARGET=t&&t.kind==='keys'?t.notes:null; }
 setTimeout(function adopt(){ try{ const kt=KEYS.KT; if(kt&&kt.length&&!getLS('kanin-seq-adopted',false)){ const k1=byId('k1')||keysT()[0]; if(k1){ k1.notes.push(...kt.map(n=>Object.assign({},n))); kt.length=0; save(); } putLS('kanin-seq-adopted',true); } }catch(_){ setTimeout(adopt,1500); } target(); },1200);
 /* playback: every keyboard track with its own sound, from the beat's own clock (the WAV export renders the same) */
 let hooked=false; function hook(){ const P=PS(); if(hooked||!P||!P.STEPHOOKS||!window.KEYS) return; hooked=true;
  P.STEPHOOKS.push((c,dest,t,s,sd)=>{ const live=c===P.ac();
   keysT().forEach(tr=>{ if(!audible(tr)) return; const ci=CH[tr.id]==null?17:CH[tr.id]; let kin=dest; try{ kin=ci===17?P.SD(c,live?KEYS.fxIn():dest,17):P.SD(c,dest,ci); }catch(_){ } const smp=tr.sound.type==='sample'; const buf=smp?BUF.get(tr.id):null; if(smp&&!buf){ resolveBuf(tr); return; }
    tr.notes.forEach(n=>{ if(n.s<P.total&&Math.floor(n.s)===s){ const at=t+(n.s-s)*sd, len=Math.max(.05,(n.len||1)*sd), vel=(n.v||.8)*tr.vol; try{ if(smp) smpVoice(c,kin,at,buf,n.m,tr.sound.root||60,vel,len); else KEYS.voice(c,kin,at,n.m,vel,len,tr.sound.v); }catch(_){ } } }); }); }); }
 /* pad tracks: mute and solo per bank, through the beat machine's own arrangement mask, so the export follows */
 (function mask(){ const prev=window.ARRMASK; if(typeof prev!=='function'||prev.__seq) return void setTimeout(mask,1000); const f=function(id,bar){ if(typeof id==='string'&&/^p\d+$/.test(id)){ const t=padT()[Math.floor(+id.slice(1)/16)]; if(t&&!audible(t)) return false; } return prev.apply(this,arguments); }; f.__seq=true; window.ARRMASK=f; })();
 /* takes: each REC on the keyboard starts a take on its track, so ↶ takes the last take back */
 const recOn=()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); };
 const padRec=()=>{ const b=$('padRecLive'); return !!b&&(b.classList.contains('rec')||/on$/i.test(b.textContent.trim())); };
 let wasRec=false; setInterval(()=>{ const r=recOn(); if(r&&!wasRec){ const t=byId(selKeys); if(t&&t.kind==='keys') t.takes.push(t.notes.length); } if(!r&&wasRec) save(); wasRec=r; },150);
 function undoTake(t){ t=t||byId(selKeys); if(!t||t.kind!=='keys') return false; const at=t.takes.pop(); if(at==null){ if(!t.notes.length) return false; const n=t.notes.pop(); try{ KUNDO.push(()=>{ t.notes.push(n); save(); paint(); },'a note'); }catch(_){ } save(); paint(); return true; } const gone=t.notes.splice(at); save(); paint(); say('↶ The last take on '+nameOf(t)+' is gone ('+gone.length+' note'+(gone.length===1?'':'s')+').'); return true; }
 function padState(t){ const P=PS(); return [...Array(16)].map((_,j)=>{ const pd=P.pads[t.bank*16+j]; return [j,(pd.steps||[]).slice(),Object.assign({},pd.offs||{}),(pd.xh||[]).map(h=>h.slice())]; }); }
 function padRestore(t,st){ const P=PS(); st.forEach(([j,steps,offs,xh])=>{ const pd=P.pads[t.bank*16+j]; if(!pd) return; pd.steps=steps; pd.offs=offs; pd.xh=xh; }); try{ P.refresh(); }catch(_){ } paint(); }
 function clearTrack(t){ if(!t) return; if(t.kind==='pads'){ const P=PS(); if(!P) return; const st=padState(t); for(let j=0;j<16;j++){ const pd=P.pads[t.bank*16+j]; if(!pd) continue; (pd.steps||[]).fill(0); pd.offs={}; pd.xh=[]; } try{ P.refresh(); }catch(_){ } paint(); say('🗑 '+nameOf(t)+' is empty; its sounds stay loaded. ↶ Undo brings the hits back.'); try{ KUNDO.push(()=>padRestore(t,st),nameOf(t)); }catch(_){ } return; }
  const old=t.notes.slice(); t.notes.length=0; t.takes=[]; save(); paint(); say('🗑 '+nameOf(t)+' is empty. ↶ Undo brings it back.'); try{ KUNDO.push(()=>{ t.notes.push(...old); save(); paint(); },nameOf(t)); }catch(_){ } }
 function quantTrack(t){ if(!t) return; const P=PS(); if(!P) return; const T=Math.max(1,P.total||16);
  if(t.kind==='pads'){ const st=padState(t); for(let j=0;j<16;j++){ const pd=P.pads[t.bank*16+j]; if(!pd) continue; pd.offs={}; (pd.xh||[]).forEach(h=>{ const q=((Math.round(h[0]+(h[1]||0))%T)+T)%T; if(!pd.steps[q]) pd.steps[q]=1; }); pd.xh=[]; } try{ P.refresh(); }catch(_){ } paint(); say('🧲 '+nameOf(t)+' snapped to the grid.'); try{ KUNDO.push(()=>padRestore(t,st),'the quantize'); }catch(_){ } return; }
  if(!t.notes.length) return; const old=t.notes.map(n=>Object.assign({},n)); t.notes.forEach(n=>{ n.s=Math.round(n.s)%T; }); save(); paint(); say('🧲 '+nameOf(t)+' snapped to 1/16.'); try{ KUNDO.push(()=>{ t.notes.length=0; t.notes.push(...old); save(); paint(); },'the quantize'); }catch(_){ } }
 function removeTrack(t){ if(!t||t.kind!=='keys') return; if(keysT().length<2) return say('Keep at least one keyboard track. 🗑 clears it instead.'); const at=tracks.indexOf(t); tracks.splice(at,1); if(selKeys===t.id){ selKeys=keysT()[0].id; target(); loadOnKeys(byId(selKeys)); } if(focus===t.id) focus=selKeys; save(); chSync(); paint(); say('✕ '+nameOf(t)+' removed. ↶ Undo brings it back.'); try{ KUNDO.push(()=>{ tracks.splice(at,0,t); save(); paint(); },nameOf(t)); }catch(_){ } }
 /* the keyboard window's UNDO and CLEAR work on the keyboard's track */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#kbDash .kDevTx [data-tx="undo"],#kbDash .kDevTx [data-tx="clear"]'); if(!b) return; const t=byId(selKeys); if(!t||t.kind!=='keys') return; e.stopImmediatePropagation(); e.preventDefault(); if(b.dataset.tx==='undo'){ if(!undoTake(t)) say('Nothing to undo on '+nameOf(t)+'.'); } else clearTrack(t); },true);
 /* ---------- the links: the controller follows the track, the track follows the controller ---------- */
 const dev=t=>t&&t.kind==='pads'?'pads':'keys';
 function select(id,silent){ const t=byId(id); if(!t) return; focus=id; const F=(()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } })();
  if(t.kind==='pads'){ selPad=id; setSel('padBank',t.bank); try{ PS().refresh(); }catch(_){ } try{ F&&F.open('pads'); }catch(_){ } try{ KKEYROUTE.owner='pads'; }catch(_){ } if(!silent) say('● '+nameOf(t)+': the 16 pads play bank '+BK[t.bank]+"'s sounds and record onto this track."); }
  else { selKeys=id; target(); try{ F&&F.open('keys'); }catch(_){ } try{ KKEYROUTE.owner='keys'; }catch(_){ } loadOnKeys(t); if(!silent) say('● '+nameOf(t)+': the keyboard plays this sound and records onto this track.'); }
  save(); paint(); }
 /* the pads' own bank buttons move the pad track; the keyboard's own instrument becomes its track's sound */
 document.addEventListener('change',e=>{ if(quiet) return; const el=e.target; if(el.id==='padBank'){ const b=+el.value||0; selPad='p'+BK[b]; paint(); }
  if(el.id==='kbPre'){ const t=byId(selKeys); if(t&&el.value!=='sample'&&!(t.sound.type==='preset'&&t.sound.v===el.value)){ const was=t.sound; t.sound={type:'preset',v:el.value}; BUF.delete(t.id); save(); paint(); try{ KUNDO.push(()=>{ t.sound=was; BUF.delete(t.id); save(); paint(); if(selKeys===t.id) loadOnKeys(t); },'the track sound'); }catch(_){ } } } },true);
 document.addEventListener('change',async e=>{ const el=e.target; if(el.id!=='kbSampleFile') return; const f=el.files&&el.files[0]; const t=byId(selKeys); if(!f||!t) return; try{ const ab=await f.arrayBuffer(); const b=await PS().ac().decodeAudioData(ab.slice(0)); const key='up:'+t.id+':'+Date.now().toString(36); const kept=await IDB.put(key,ab); t.sound={type:'sample',name:f.name.replace(/\.[a-z0-9]+$/i,'').slice(0,40),src:{t:'upload',key},root:+(($('kbRoot')||{}).value)||60}; BUF.set(t.id,b); save(); paint(); if(!kept) say('🎙 '+f.name+' plays on this track for this visit (this browser would not keep it).'); }catch(_){ } },true);
 /* called by the 🗂 SOUNDS browser */
 function keysSound(o){ const t=byId(selKeys); if(!t||!o||!o.buf) return; const was=t.sound, wb=BUF.get(t.id); t.sound={type:'sample',name:String(o.name||'Sound').slice(0,40),src:o.src||{t:'mem'},root:o.root||rootOf(o.name)}; BUF.set(t.id,o.buf); setSel('kbRoot',t.sound.root,['change']); save(); paint(); try{ KUNDO.push(()=>{ t.sound=was; if(wb) BUF.set(t.id,wb); else BUF.delete(t.id); save(); paint(); if(selKeys===t.id) loadOnKeys(t); },'the track sound'); }catch(_){ } }
 function padLabel(b,label){ const t=padT()[b]; if(!t) return; t.label=String(label||'').slice(0,40); t.sig=padNames(b).join('|'); save(); paint(); }
 /* ---------- the window ---------- */
 const css=document.createElement('style'); css.textContent=`
#kSeqWin{display:none;color:#e9ecf5;font:13px/1.4 system-ui,sans-serif}
#kSeqWin.kFOn{display:flex!important;flex-direction:column}
#kSeqWin .sqTop{display:flex;flex-wrap:wrap;gap:5px;align-items:center;padding:6px 0}
#kSeqWin .sqTop button{min-height:38px!important;padding:0 10px!important;border-radius:9px!important;font:800 12.5px system-ui,sans-serif!important}
#kSeqWin .sqTop .lcd{font:700 12px ui-monospace,monospace;background:linear-gradient(180deg,#c6d6a6,#a9bd87);color:#1b2410;border-radius:6px;padding:6px 9px;border:2px solid #0b0c10;white-space:nowrap}
#kSeqWin .sqTop button.on{background:#ffe94a!important;color:#14163a!important}
#kSeqWin .sqTop button.rec.on{background:#ff2d4f!important;color:#fff!important}
#kSeqWin .sqBody{display:grid;grid-template-columns:minmax(250px,300px) minmax(0,1fr);border:1px solid #3a3f4d;border-radius:10px;overflow:auto;background:#11131a;min-height:0}
#kSeqWin .sqHeads{display:flex;flex-direction:column;border-right:1px solid #3a3f4d;background:#191c25}
#kSeqWin .sqRuler{height:24px;box-sizing:border-box;border-bottom:1px solid #3a3f4d;font:800 11px system-ui,sans-serif;color:#9aa3b8;display:flex;align-items:center;padding:0 8px}
#kSeqWin .sqHead{height:62px;box-sizing:border-box;border-bottom:1px solid #2a2e3a;padding:4px 6px;display:flex;flex-direction:column;justify-content:center;gap:4px;cursor:pointer}
#kSeqWin .sqHead.sel{background:#24202c}
#kSeqWin .sqHead.focus{background:#2a1520;box-shadow:inset 3px 0 0 #ff2d4f}
#kSeqWin .sqHead .n{display:flex;align-items:center;gap:6px;font:800 12.5px system-ui,sans-serif;white-space:nowrap;overflow:hidden;min-width:0}
#kSeqWin .sqHead .n i{width:10px;height:10px;border-radius:3px;flex:none}
#kSeqWin .sqHead .n b{overflow:hidden;text-overflow:ellipsis;min-width:0}
#kSeqWin .sqHead .n small{color:#9aa3b8;flex:none}
#kSeqWin .sqHead .n em{font:900 9.5px system-ui,sans-serif;font-style:normal;background:#ff2d4f;color:#fff;border-radius:4px;padding:1px 4px;flex:none}
#kSeqWin .sqHead .c{display:flex;gap:3px;align-items:center}
#kSeqWin .sqHead .c button{min-height:26px!important;min-width:26px!important;padding:0 5px!important;border-radius:6px!important;font:900 11px system-ui,sans-serif!important}
#kSeqWin .sqHead .c button.on{background:#ffe94a!important;color:#14163a!important}
#kSeqWin .sqHead .c button.arm.on{background:#ff2d4f!important;color:#fff!important}
#kSeqWin .sqHead select{min-height:24px;max-width:100%;min-width:0;flex:1 1 auto;font:800 12px system-ui,sans-serif;border-radius:6px}
#kSeqWin .sqHead input[type=range]{width:44px}
#kSeqWin .sqTL{position:relative;min-width:0;overflow:hidden}
#kSeqWin canvas{display:block;width:100%;cursor:pointer}
#kSeqWin .sqHint{font:600 12px system-ui,sans-serif;color:#9aa3b8;padding:6px 2px}
@media (max-width:760px){ #kSeqWin .sqBody{grid-template-columns:156px minmax(0,1fr)} #kSeqWin .sqHead input[type=range],#kSeqWin .sqHead [data-tk="q"],#kSeqWin .sqHead [data-tk="del"],#kSeqWin .sqHead [data-tk="dev"]{display:none} }`; document.head.appendChild(css);
 const ROWH=62, RULER=24;
 function box(){ let w=$('kSeqWin'); if(w) return w; const pad=$('pad'); if(!pad) return null; w=document.createElement('div'); w.id='kSeqWin'; pad.appendChild(w);
  w.innerHTML='<div class="sqTop"><button type="button" data-sq="rew" data-noul>⏮</button><button type="button" data-sq="play" data-noul>▶ PLAY</button><button type="button" data-sq="stop" data-noul>■ STOP</button><button type="button" class="rec" data-sq="rec" data-noul>● REC</button><span class="lcd" id="sqLcd">BAR 01.1.00</span><button type="button" data-sq="loop" data-noul>🔄 LOOP</button><button type="button" data-sq="q" data-noul>🧲 Q</button><button type="button" data-sq="add" data-noul>＋ Keyboard track</button><button type="button" data-sq="mix" data-noul>🎚 Mixer</button><button type="button" data-sq="demo" data-noul>🎬 Demo</button></div>'+
   '<div class="sqBody"><div class="sqHeads"><div class="sqRuler">TRACKS · tap one to play and record on it</div><div id="sqHeads"></div></div><div class="sqTL"><canvas id="sqCv"></canvas></div></div><div class="sqHint">Tap a track: the pads (Pads A to D) or the keyboard (every 🎹 track) move to it, with its own sound. ⬇ LOAD puts any sound on it. ● REC records it. Tap a note to delete it. Space plays and stops.</div>';
  w.addEventListener('click',onClick); w.addEventListener('change',onChange); w.addEventListener('input',e=>{ const id=e.target.dataset.vol; if(id){ const t=byId(id); if(t){ t.vol=(+e.target.value)/100; save(); } } });
  w.querySelector('#sqCv').addEventListener('click',onCanvas);
  w.addEventListener('focusin',e=>{ const sel=e.target.closest&&e.target.closest('select[data-pre]'); if(sel&&sel.dataset.pre!==selKeys) select(sel.dataset.pre,true); });
  return w; }
 function heads(){ const H=$('sqHeads'); if(!H) return; names(); const pre=$('kbPre'); const opts=pre?[...pre.options].filter(o=>o.value!=='sample'):[];
  const btn=(tk,id,lab,ttl,cls)=>'<button type="button" data-tk="'+tk+'" data-id="'+id+'"'+(cls?' class="'+cls+'"':'')+' title="'+ttl+'" aria-label="'+ttl+'" data-noul>'+lab+'</button>';
  const html=rows().map((t,i)=>{ const col=COLORS[i%COLORS.length];
   if(t.kind==='take'){ const k=t.take, ci=(()=>{ try{ return K40.voxCi(t.ti); }catch(_){ return 23; } })(); return '<div class="sqHead" data-tr="'+t.id+'"><div class="n"><i style="background:'+col+'"></i><b title="'+esc(k.name)+'">🎤 '+esc(k.name)+'</b><small>'+(k.buf?k.buf.duration.toFixed(1)+' s':'')+' · CH '+(ci+1)+'</small></div><div class="c">'+btn('tmute',t.id,'M','Mute this take',k.mute?'on':'')+btn('tsolo',t.id,'S','Solo this take',k.solo?'on':'')+btn('tplay',t.id,'▶','Play the takes with the beat')+btn('tstop',t.id,'■','Stop the takes')+btn('kara',t.id,'🎤','Open Karaoke')+'</div></div>'; } const sel=t.id===selPad||t.id===selKeys, foc=t.id===focus; const cls='sqHead'+(sel?' sel':'')+(foc?' focus':'');
   const recNow=foc&&(t.kind==='pads'?padRec():recOn());
   if(t.kind==='pads') return '<div class="'+cls+'" data-tr="'+t.id+'"><div class="n"><i style="background:'+col+'"></i><b title="'+esc(t.name)+'">'+esc(t.name)+'</b><small>'+hitsOf(t)+' · '+chLabel(t)+'</small>'+(t.id===selPad?'<em>PADS</em>':'')+(recNow?'<em>REC</em>':'')+'</div><div class="c">'+btn('sel',t.id,'●','Select: the 16 pads play and record this track','arm'+(sel?' on':''))+btn('mute',t.id,'M','Mute',t.mute?'on':'')+btn('solo',t.id,'S','Solo',t.solo?'on':'')+btn('snd',t.id,'⬇ LOAD','Load sounds onto this track (the 16 pads of its bank)')+btn('q',t.id,'Q','Snap this track to the grid')+btn('clr',t.id,'🗑','Clear the hits on this track')+btn('dev',t.id,'🥁','Open the pads')+'</div></div>';
   const smp=t.sound.type==='sample';
   return '<div class="'+cls+'" data-tr="'+t.id+'"><div class="n"><i style="background:'+col+'"></i><select data-pre="'+t.id+'" aria-label="This track\'s sound" data-nodice data-die="1">'+(smp?'<option value="__smp" selected>🎙 '+esc(t.sound.name)+'</option>':'')+opts.map(o=>'<option value="'+o.value+'"'+(!smp&&o.value===t.sound.v?' selected':'')+'>'+(ICON[o.value]||'🎹')+' '+esc(o.text)+'</option>').join('')+'</select><small>'+t.notes.length+' · '+chLabel(t)+'</small>'+(t.id===selKeys?'<em>KEYS</em>':'')+(recNow?'<em>REC</em>':'')+'</div><div class="c">'+btn('sel',t.id,'●','Select: the keyboard plays and records this track','arm'+(sel?' on':''))+btn('mute',t.id,'M','Mute',t.mute?'on':'')+btn('solo',t.id,'S','Solo',t.solo?'on':'')+btn('snd',t.id,'⬇ LOAD','Load any sound onto this track')+'<input type="range" min="0" max="150" value="'+Math.round(t.vol*100)+'" data-vol="'+t.id+'" data-die="1" aria-label="Volume">'+btn('q',t.id,'Q','Snap this track to 1/16')+btn('clr',t.id,'🗑','Clear this track')+btn('del',t.id,'✕','Remove this track')+'</div></div>'; }).join('');
  if(H.dataset.h!==html){ const ae=document.activeElement; if(ae&&H.contains(ae)&&ae.tagName==='SELECT') return; H.dataset.h=html; H.innerHTML=html; } }
 let lastStep=-1, stepAt=0;
 function draw(){ const cv=$('sqCv'); if(!cv||!cv.getClientRects().length) return; const P=PS(); if(!P) return; const RW=rows(); const W=cv.clientWidth||600, H=RULER+RW.length*ROWH; const dpr=Math.min(2,devicePixelRatio||1); if(cv.width!==Math.round(W*dpr)||cv.height!==Math.round(H*dpr)){ cv.width=Math.round(W*dpr); cv.height=Math.round(H*dpr); cv.style.height=H+'px'; }
  const g=cv.getContext('2d'); g.setTransform(dpr,0,0,dpr,0,0); g.clearRect(0,0,W,H); const total=P.total||16, spb=P.spbN||16, bars=P.barsN||1; const x=s=>s/total*W;
  g.fillStyle='#191c25'; g.fillRect(0,0,W,RULER); g.font='800 11px system-ui,sans-serif'; g.textBaseline='middle';
  for(let s=0;s<=total;s++){ const X=Math.round(x(s))+.5; const isBar=s%spb===0, isBeat=s%(spb/4)===0; g.strokeStyle=isBar?'#596079':isBeat?'#363b4b':'#232734'; g.beginPath(); g.moveTo(X,isBar?0:RULER); g.lineTo(X,H); g.stroke(); if(isBar&&s<total){ g.fillStyle='#c9cede'; g.fillText(String(s/spb+1),X+4,RULER/2); } }
  RW.forEach((t,i)=>{ const y=RULER+i*ROWH; g.fillStyle=i%2?'#14161e':'#171a23'; g.fillRect(0,y,W,ROWH);
   if(t.kind==='take'){ const k=t.take; const col=COLORS[i%COLORS.length]; g.globalAlpha=(k.mute||(kTakes().some(x=>x.solo)&&!k.solo))?.3:1; if(k.buf){ const sec=total/(spb/4)*60/P.bpm(); const w=Math.min(W,k.buf.duration/sec*W); const d=k.buf.getChannelData(0), n=Math.max(1,Math.floor(w)); const per=Math.max(1,Math.floor(Math.min(d.length,sec*k.buf.sampleRate)/Math.max(1,W))); g.fillStyle=col; for(let X=0;X<n;X++){ let m=0; const o=X*per; for(let j=0;j<per;j+=16) m=Math.max(m,Math.abs(d[o+j]||0)); const h=Math.max(1,m*(ROWH-10)); g.fillRect(X,y+ROWH/2-h/2,1,h); } if(k.buf.duration>sec){ g.fillStyle='#c9cede'; g.font='700 11px system-ui,sans-serif'; g.fillText('→ '+k.buf.duration.toFixed(1)+' s take (the loop is '+sec.toFixed(1)+' s)',8,y+12); } } g.globalAlpha=1; return; } if(t.id===focus){ g.fillStyle='rgba(255,45,79,.09)'; g.fillRect(0,y,W,ROWH); } else if(t.id===selPad||t.id===selKeys){ g.fillStyle='rgba(255,233,74,.05)'; g.fillRect(0,y,W,ROWH); } const col=COLORS[i%COLORS.length]; g.globalAlpha=audible(t)?1:.3;
   if(t.kind==='pads'){ const base=t.bank*16; let any=false; const rh=(ROWH-8)/16; for(let p=0;p<16;p++){ const pd=P.pads[base+p]; if(!pd) continue; const yy=y+4+p*rh; g.fillStyle=col; (pd.steps||[]).forEach((on,s)=>{ if(on&&s<total){ any=true; g.fillRect(x(s+((pd.offs&&pd.offs[s])||0))+1,yy,Math.max(2,x(1)-2),Math.max(2,rh-1)); } }); (pd.xh||[]).forEach(h=>{ const s=h[0]+(h[1]||0); if(s<total){ any=true; g.fillStyle='#fff'; g.fillRect(x(s),yy,2,Math.max(2,rh-1)); g.fillStyle=col; } }); }
    if(!any){ g.fillStyle='#596079'; g.font='700 11px system-ui,sans-serif'; g.fillText(t.id===focus?'● selected: press REC and play the pads':'empty: tap the track, then REC',8,y+ROWH/2); } }
   else { const ns=t.notes.filter(n=>n.s<total); if(ns.length){ let lo=Math.min(...ns.map(n=>n.m)), hi=Math.max(...ns.map(n=>n.m)); if(hi-lo<12){ const mid=(lo+hi)/2; lo=mid-6; hi=mid+6; } ns.forEach(n=>{ const yy=y+ROWH-6-(n.m-lo)/(hi-lo||1)*(ROWH-14); g.fillStyle=col; g.fillRect(x(n.s),yy-3,Math.max(3,x(n.len||1)),6); }); } else { g.fillStyle='#596079'; g.font='700 11px system-ui,sans-serif'; g.fillText(t.id===focus?'● selected: press REC and play the keyboard':'empty: tap the track, then REC',8,y+ROWH/2); } }
   g.globalAlpha=1; });
  const st=typeof (window.PADS||{}).step==='number'?Math.max(0,PADS.step):0; if(st!==lastStep){ lastStep=st; stepAt=performance.now(); } const frac=P.playing?Math.min(.999,(performance.now()-stepAt)/(60000/P.bpm()/4)):0; const px=x(st+frac);
  if(P.playing){ g.strokeStyle='#ffe94a'; g.lineWidth=2; g.beginPath(); g.moveTo(px,0); g.lineTo(px,H); g.stroke(); g.lineWidth=1; }
  const lcd=$('sqLcd'); if(lcd){ const perBeat=Math.max(1,spb/4), inBar=st%spb; const ft=byId(focus); const txt='BAR '+String(Math.floor(st/spb)%bars+1).padStart(2,'0')+'.'+(Math.floor(inBar/perBeat)+1)+'.'+String(Math.floor(((inBar%perBeat)+frac)/perBeat*96)).padStart(2,'0')+'  '+Math.round(P.bpm())+' BPM  '+bars+' BAR'+(bars>1?'S':'')+(ft?'  TRK '+(ft.kind==='pads'?'PADS '+BK[ft.bank]:(tracks.indexOf(ft)-3)):''); if(lcd.textContent!==txt) lcd.textContent=txt; }
  const w=$('kSeqWin'); if(w){ w.querySelector('[data-sq="play"]').classList.toggle('on',!!P.playing); w.querySelector('[data-sq="rec"]').classList.toggle('on',recOn()||padRec()); w.querySelector('[data-sq="q"]').classList.toggle('on',(window.PADRECMODE||'live')!=='live'); } }
 function paint(){ if(!$('kSeqWin')) return; heads(); draw(); }
 function onCanvas(e){ const cv=e.currentTarget, P=PS(); const r=cv.getBoundingClientRect(); const X=e.clientX-r.left, Y=e.clientY-r.top; const i=Math.floor((Y-RULER)/ROWH); const t=rows()[i]; if(!t||t.kind==='take') return; const total=P.total||16; const s=X/r.width*total;
  if(t.kind!=='keys'){ select(t.id); return; } const ns=t.notes.filter(n=>n.s<total); if(!ns.length){ select(t.id); return; } let lo=Math.min(...ns.map(n=>n.m)), hi=Math.max(...ns.map(n=>n.m)); if(hi-lo<12){ const mid=(lo+hi)/2; lo=mid-6; hi=mid+6; } const y0=RULER+i*ROWH;
  const hit=t.notes.findIndex(n=>{ if(n.s>=total) return false; const yy=y0+ROWH-6-(n.m-lo)/(hi-lo||1)*(ROWH-14); return s>=n.s-.3&&s<=n.s+Math.max(.4,(n.len||1))&&Math.abs(Y-yy)<=6; });
  if(hit<0){ select(t.id); return; } const [n]=t.notes.splice(hit,1); save(); paint(); say('🗑 Note deleted. ↶ Undo brings it back.'); try{ KUNDO.push(()=>{ t.notes.push(n); save(); paint(); },'a note'); }catch(_){ } }
 const NEXT=['strings','pad','lead','epiano','organ','brass','pluck','bells','choir','marimba','guitar','flute','harp','vibes','kalimba','chip','piano','bass'];
 function addTrack(){ const used=keysT().map(t=>t.sound.v); const v=NEXT.find(p=>!used.includes(p)&&$('kbPre')&&[...$('kbPre').options].some(o=>o.value===p))||'piano'; const id='k'+Date.now().toString(36); tracks.push({id,kind:'keys',sound:{type:'preset',v},notes:[],vol:1,takes:[]}); save(); chSync(); select(id,true); say('＋ A new keyboard track ('+instName(v)+') is selected. 🗂 on it picks any sound; ● REC records it.'); }
 function openSounds(t){ select(t.id,true); setTimeout(()=>{ const bar=$(dev(t)==='pads'?'mpcBar':'kbDash'); const b=bar&&bar.querySelector('.kScr [data-sf="snd"]'); const d=bar&&bar.querySelector('.kScr .kDrawer'); if(b&&d&&d.hidden) b.click(); say('🗂 Pick a category, then a group, then a sound: it loads onto '+nameOf(t).replace(/ · .*$/,'')+'.'); },450); }
 function onClick(e){ const b=e.target.closest('[data-sq],[data-tk],[data-tr]'); if(!b) return; if(b.tagName==='SELECT'||b.tagName==='INPUT'||e.target.tagName==='SELECT'||e.target.tagName==='INPUT') return; e.stopPropagation();
  const R=(()=>{ try{ return KREMOTE.act; }catch(_){ return null; } })();
  if(b.dataset.sq){ const k=b.dataset.sq; const ft=byId(focus), d=dev(ft);
   if(k==='rew'){ try{ KDEVTX.act(d,'rew'); }catch(_){ R&&R.rew(); } } if(k==='play'){ try{ KDEVTX.act(d,'play'); }catch(_){ try{ PS().play(); }catch(__){ } } } if(k==='stop'){ try{ KDEVTX.act(d,'stop'); }catch(_){ try{ PS().stop(); }catch(__){ } } }
   if(k==='rec'){ if(ft) select(ft.id,true); const was=d==='pads'?padRec():recOn(); try{ KDEVTX.act(d,'rec'); }catch(_){ const rb=$(d==='pads'?'padRecLive':'kbRec'); if(rb) rb.click(); } if(!was) setTimeout(()=>{ try{ if(!PS().playing) KDEVTX.act(d,'play'); }catch(_){ } },250); }
   if(k==='loop'){ try{ KDISPLAY.loop(); }catch(_){ } } if(k==='q'){ const s=document.querySelector('.kPadMode [data-pl="snap"]'); if(s) s.click(); }
   if(k==='add') addTrack(); if(k==='mix'){ const m=$('padMixer'); if(m){ try{ KRAIL.FLOAT.close('seq'); }catch(_){ } m.scrollIntoView({block:'start',behavior:'smooth'}); } } if(k==='demo'){ try{ KDEMO.start(); }catch(_){ say('The demo is loading. Try again in a moment.'); } }
   setTimeout(paint,80); return; }
  if(b.dataset.tk&&/^kt\d+$/.test(b.dataset.id||'')){ const k=b.dataset.tk, T=kTakes()[+b.dataset.id.slice(2)]; const kk=s=>{ const x=document.querySelector('#kKara [data-kk="'+s+'"]'); if(x) x.click(); };
   const ti=+b.dataset.id.slice(2); const own=a=>document.querySelector('#kKara [data-kk="'+a+'"][data-i="'+ti+'"]');
   if(T&&k==='tmute'){ const o=own('lmute'); if(o) o.click(); else T.mute=!T.mute; } if(T&&k==='tsolo'){ const o=own('lsolo'); if(o) o.click(); else T.solo=!T.solo; } if(k==='tplay') kk('lbeat'); if(k==='tstop') kk('lstop'); if(k==='kara'){ try{ KKARA.open(); }catch(_){ } }
   setTimeout(paint,60); return; }
  if(b.dataset.tr&&/^kt\d+$/.test(b.dataset.tr)) return;
  if(b.dataset.tk){ const k=b.dataset.tk, t=byId(b.dataset.id); if(!t) return;
   if(k==='sel') select(t.id); if(k==='mute'){ t.mute=!t.mute; save(); } if(k==='solo'){ t.solo=!t.solo; save(); }
   if(k==='q') quantTrack(t); if(k==='clr') clearTrack(t); if(k==='del') removeTrack(t); if(k==='snd') openSounds(t); if(k==='dev') select(t.id);
   setTimeout(paint,60); return; }
  if(b.dataset.tr) select(b.dataset.tr); }
 function onChange(e){ const id=e.target.dataset.pre; if(!id) return; e.stopPropagation(); const t=byId(id); if(!t||e.target.value==='__smp') return; const was=t.sound; t.sound={type:'preset',v:e.target.value}; BUF.delete(t.id); save(); try{ KUNDO.push(()=>{ t.sound=was; BUF.delete(t.id); save(); paint(); if(selKeys===t.id) loadOnKeys(t); },'the track sound'); }catch(_){ } if(selKeys===id) loadOnKeys(t); const H=$('sqHeads'); if(H) H.dataset.h=''; e.target.blur(); paint(); }
 /* ---------- the floating window, opened from the transport bar, the Studio, the Menu and Find ---------- */
 function register(){ let F; try{ F=KRAIL.FLOAT; }catch(_){ return false; } if(!F||!F.add) return false; if(!box()) return false;
  F.add('seq',{get:()=>$('kSeqWin'),t:'🎼 Track sequencer',i:'🎼',l:'Tracks'});
  if(!getLS('kanin-float-seq',null)){ const W=innerWidth-(innerWidth<=760?58:76), H=innerHeight; putLS('kanin-float-seq',innerWidth<=760?{x:4,y:56,w:W-8,h:Math.round(H*.7)}:{x:8,y:Math.round(H*.46),w:W-16,h:Math.round(H*.5)}); }
  return true; }
 function open(){ try{ if(KRAIL.cur()!=='pad') KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ if(!register()) return; try{ KRAIL.FLOAT.open('seq'); }catch(_){ } paint(); },KRAIL&&KRAIL.cur&&KRAIL.cur()==='pad'?0:900); }
 function close(){ try{ KRAIL.FLOAT.close('seq'); }catch(_){ } }
 function bbBtn(){ const bb=$('bbBar'); if(!bb||bb.querySelector('[data-sqo]')) return; const b=document.createElement('button'); b.type='button'; b.dataset.sqo='1'; b.setAttribute('data-noul',''); b.textContent='🎼 Tracks'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); const on=(()=>{ try{ return KRAIL.FLOAT.isOpen('seq'); }catch(_){ return false; } })(); if(on) close(); else open(); },true); bb.appendChild(b); }
 chans(); setInterval(()=>{ hook(); register(); bbBtn(); target(); names(); chSync(); const s=$('padBank'); if(s){ const id='p'+BK[+s.value||0]; if(id!==selPad){ selPad=id; } } const w=$('kSeqWin'); if(w&&w.classList.contains('kFOn')&&!w.classList.contains('kFOff')) heads(); },700);
 setTimeout(()=>{ const t=byId(selKeys); if(t&&t.sound.type==='sample') resolveBuf(t); },2500);
 (function loop(){ requestAnimationFrame(loop); const w=$('kSeqWin'); if(w&&w.classList.contains('kFOn')&&!w.classList.contains('kFOff')) draw(); })();
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Studio','🎼','Track sequencer: pad tracks and keyboard tracks, each with its own sound','Studio',()=>open()); });
 window.KSEQ={open,close,get tracks(){ names(); return tracks; },get armed(){ return focus; },get keysId(){ return selKeys; },get padId(){ return selPad; },arm:id=>select(id),select,add:addTrack,undo:undoTake,clear:id=>clearTrack(byId(id)),quant:id=>quantTrack(byId(id)),remove:id=>removeTrack(byId(id)),keysSound,padLabel,nameOf,resolveBuf,paint,get channels(){ return Object.assign({},CH); }};
})();
