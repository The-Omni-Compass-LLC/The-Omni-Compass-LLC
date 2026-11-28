(()=>{ /* 🔒 LOCK & SHUFFLE · LOOP TOOLS (v198). Lock any piece of the story or the beat, then shuffle the rest: a partial shuffle moves a few
   unlocked pieces, a complete shuffle moves every unlocked piece; locked pieces never move. Loop tools: double the loop 1 → 2 → 4 → 8 → 16 → 32
   bars, copy a bar and paste it over another, every edit undoable. */
 const $=id=>document.getElementById(id); const Q=s=>[...document.querySelectorAll(s)];
 const say=m=>{ try{ toast(m); }catch(_){ } }; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const clone=o=>JSON.parse(JSON.stringify(o==null?null:o));
 const LOCK=Object.assign({},getLS('kanin-locks',{})); const saveL=()=>putLS('kanin-locks',LOCK);
 /* a shuffle never lands on adult-only settings: those stay a person's own choice */
 const ADULT=/\bX\b|adults? only|18\+|\bmature\b|restricted|^R\b|new adult|^adult$/i;
 const fire=e=>{ ['input','change'].forEach(t=>e.dispatchEvent(new Event(t,{bubbles:true}))); };
 function pickSel(sel){ if(!sel||sel.disabled) return false; const o=[...sel.options].filter(q=>!q.disabled&&q.value!==''&&q.value!==sel.value&&!ADULT.test(q.text.trim())); if(!o.length) return false; sel.value=o[Math.floor(Math.random()*o.length)].value; fire(sel); return true; }
 function keyOf(e){ if(e.dataset.cat) return 'cat:'+e.dataset.cat; if(e.id) return '#'+e.id; const cr=e.closest('.castRow'); if(cr) return 'cast:'+cr.dataset.ck+':'+cr.dataset.k+':'+(e.dataset.cf||''); const dr=e.closest('.cabDrawer[data-k]'); if(dr) return 'cab:'+dr.dataset.k; const lb=e.closest('label'); const t=lb?[...lb.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim():''; const box=e.closest('[id]'); return (box?box.id:'')+':'+(e.getAttribute('aria-label')||t); }
 const some=(arr,frac)=>{ const a=arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a.slice(0,Math.max(1,Math.ceil(a.length*frac))); };

 /* ================= THE STORY ================= */
 const SEL=g=>g.els().filter(e=>e.tagName==='SELECT');
 const STORY=[
  {k:'s-content',ic:'📜',n:'Content · the canvases',els:()=>[],run:async full=>{ const b=$(full?'qpBtn':'caQP')||$('qpBtn'); if(!b) return false; b.click(); await sleep(full?2600:1400); return true; }},
  {k:'s-story',ic:'🧵',n:'Storyline · order and architecture',els:()=>Q('#cabGrid select'),extra:async full=>{ if(full){ const b=$('oShuffle'); if(b){ b.click(); await sleep(250); } } }},
  {k:'s-cast',ic:'🎭',n:'Characters',els:()=>Q('#s-cast select,#s-cast input[data-cf="name"]'),run:async full=>{ const d=Q('#s-cast [data-cf="dice"]'); const pick=full?d:some(d,0.34); pick.forEach(b=>b.click()); await sleep(250); return pick.length>0; }},
  {k:'s-demo',ic:'👥',n:'Audience and age group',els:()=>Q('#layAud select,#catRows select[data-cat="audience"],#catRows select[data-cat="rating"]')},
  {k:'s-genre',ic:'🎬',n:'Genre and kind of work',els:()=>Q('#layKind select,#catRows select[data-cat="format"],#catRows select[data-cat="sub"]')},
  {k:'s-tone',ic:'🎨',n:'Tone and pace',els:()=>Q('#layTone select,#catRows select[data-cat="tone"],#catRows select[data-cat="pace"],#catRows select[data-cat="hook"]')},
  {k:'s-form',ic:'📐',n:'Form · point of view, tense, scale',els:()=>Q('#layForm select,#catRows select[data-cat="pov"],#catRows select[data-cat="distance"],#catRows select[data-cat="tense"],#catRows select[data-cat="scale"],#catRows select[data-cat="span"]')}];
 async function shuffleSels(g,full){ const n0=SEL(g).length; if(!n0) return false; const one=Math.floor(Math.random()*n0); let did=false;
  for(let i=0;i<24;i++){ const L=SEL(g); if(i>=L.length) break; if(full||i===one){ if(pickSel(L[i])) did=true; await sleep(70); } }
  if(g.extra) await g.extra(full); return did; }
 const snapG=g=>g.els().map(e=>({key:keyOf(e),v:e.value}));
 async function restoreG(g,snap){ for(const s of snap){ const e=g.els().find(x=>keyOf(x)===s.key); if(e&&e.value!==s.v){ e.value=s.v; fire(e); await sleep(60); } } }
 let busy=false, lastStory=null;
 async function shuffleStory(full,box){ if(busy) return; const open=STORY.filter(g=>!LOCK[g.k]); if(!open.length) return note(box,'🔒 Everything is locked. Unlock a piece to shuffle it.');
  busy=true; note(box,(full?'🎲 Complete shuffle':'🔀 Partial shuffle')+': the cannon is moving the unlocked pieces…');
  try{ UNILAW.fire('story',{quiet:true}); }catch(_){ }
  lastStory=STORY.map(g=>[g.k,snapG(g)]);
  const held=STORY.filter(g=>LOCK[g.k]).map(g=>[g,snapG(g)]);
  const targets=(full?open:some(open,0.4)).sort((a,b)=>(a.k==='s-content'?-1:0)-(b.k==='s-content'?-1:0));
  const moved=[];
  for(const g of targets){ let ok=false; try{ ok=g.run?await g.run(full):await shuffleSels(g,full); }catch(_){ } if(ok) moved.push(g.ic+' '+g.n); }
  for(const [g,s] of held) await restoreG(g,s);
  busy=false; paintAll();
  note(box,(moved.length?(full?'🎲 Complete shuffle: ':'🔀 Partial shuffle: ')+moved.join(' · ')+' moved.':'Nothing could move: open the story builder or the Layers once so its pieces are on the page.')+(held.length?' Held by your locks: '+held.map(([g])=>g.ic+' '+g.n).join(' · ')+'.':'')); }
 async function undoStory(box){ if(busy) return note(box,'One moment: the shuffle is still landing.'); if(!lastStory) return note(box,'No story shuffle to undo yet.'); for(const [k,s] of lastStory){ const g=STORY.find(x=>x.k===k); if(g) await restoreG(g,s); } lastStory=null; note(box,'↶ The story settings are back as they were. The book’s own ↶ Undo in Master control takes back the canvases.'); }

 /* ================= THE BEAT ================= */
 const PS=()=>window.PADSTUDIO, TH=()=>window.THEORY;
 const LANES=[['bass','🎸','Bass line'],['chords','🎹','Chords'],['melody','🎵','Melody'],['gtr','🎶','Rhythm guitar']];
 const BEAT=[{k:'b-tempo',ic:'⏱',n:'Tempo'},{k:'b-genre',ic:'🎶',n:'Genre and style'},{k:'b-key',ic:'🎼',n:'Key and mode'},{k:'b-prog',ic:'🔗',n:'Chord progression'}]
  .concat(LANES.map(([k,ic,n])=>({k:'b-'+k,ic,n,lane:k}))).concat([{k:'b-drums',ic:'🥁',n:'Drums (every drum track)'}]);
 const hasHits=(i)=>{ const P=PS(); if(!P) return false; const L=P.bars*P.spb, st=P.pads[i].steps; for(let s=0;s<L;s++) if(st[s]) return true; return false; };
 function beatSnap(){ const P=PS(), T=TH(); return {bars:P.bars,steps:P.pads.map(p=>p.steps.slice()),on:P.tracks.map(k=>(k.on||[]).slice()),CT:T?clone(T.CT):null,chart:T?clone(T.chart):null,ui:['padBpm','cGen','cKey','cMode','cProg','cBars'].map(id=>[id,($(id)||{}).value])}; }
 async function beatRestore(o){ const P=PS(), T=TH(); if(!P||!o) return; if(P.bars!==o.bars) P.setBars(o.bars); o.ui.forEach(([id,v])=>{ const e=$(id); if(e&&v!=null&&e.value!==v){ e.value=v; if(id==='padBpm') fire(e); } }); P.pads.forEach((p,i)=>{ p.steps=o.steps[i].slice(); }); P.tracks.forEach((k,i)=>{ if(o.on[i]) k.on=o.on[i].slice(); }); if(T&&o.CT){ T.setCT(clone(o.CT)); try{ T.setChart(clone(o.chart)||[]); }catch(_){ T.redraw(); } } P.refresh(); }
 function vary(st,i,L,spb){ const on=[]; for(let s=0;s<L;s++) if(st[s]) on.push(s); if(!on.length) return false;
  const anchor=s=>{ const p=s%spb; return (i<=1&&p===0)||((i===2||i===3)&&(p===spb/4||p===3*spb/4)); };
  const keep=on.filter(anchor), free=on.filter(s=>!anchor(s)), vel=st[on[0]]||1, out=new Array(L).fill(0); keep.forEach(s=>out[s]=st[s]);
  const mode=free.length?Math.floor(Math.random()*3):0;
  if(mode===0) free.forEach(s=>{ let t=(s+(Math.random()<.5?-1:1)+L)%L; if(out[t]||anchor(t)) t=s; out[t]=st[s]; });
  else if(mode===1){ const n=free.length, rot=Math.floor(Math.random()*L); for(let j=0;j<n;j++){ let t=(Math.floor(j*L/n)+rot)%L, g=0; while(out[t]&&g++<L) t=(t+1)%L; out[t]=vel; } }
  else free.forEach(s=>{ const b=Math.floor(s/spb)*spb; let t=b+(spb-1-s%spb); if(out[t]) t=s; out[t]=st[s]; });
  for(let s=0;s<L;s++) st[s]=out[s]; return true; }
 let lastBeat=null;
 async function shuffleBeat(full,box){ const P=PS(), T=TH(); if(!P||!T) return note(box,'Open the 🎛 Studio once so the beat is on the page, then shuffle.'); if(busy) return;
  const laneHeld=LANES.filter(([k])=>LOCK['b-'+k]); const harmony=laneHeld.length>0;
  const isOpen=g=>!LOCK[g.k]&&!(harmony&&(g.k==='b-key'||g.k==='b-prog'));
  const drumOpen=[...Array(16).keys()].filter(i=>!LOCK['b-drums']&&!LOCK['p-'+i]);
  const open=BEAT.filter(isOpen).filter(g=>g.k!=='b-drums'||drumOpen.length);
  if(!open.length) return note(box,'🔒 Everything is locked. Unlock a piece to shuffle it.');
  busy=true; try{ UNILAW.fire('beat',{quiet:true}); }catch(_){ }
  const snap=beatSnap(); lastBeat=snap; const oldBars=P.bars;
  const T0=new Set((full?open:some(open,0.4)).map(g=>g.k)); const moved=[];
  if(T0.has('b-tempo')){ const e=$('padBpm'); if(e){ const lo=70,hi=150; let v; do{ v=lo+Math.floor(Math.random()*(hi-lo+1)); }while(v===+e.value); e.value=String(v); fire(e); moved.push('⏱ Tempo '+v+' BPM'); } }
  let harm=false;
  if(T0.has('b-genre')&&pickSel($('cGen'))){ harm=true; moved.push('🎶 Genre: '+$('cGen').selectedOptions[0].text); await sleep(60); if(harmony){ snap.ui.forEach(([id,v])=>{ if(/^c(Key|Mode|Prog)$/.test(id)&&$(id)&&v!=null) $(id).value=v; }); } }
  if(T0.has('b-key')){ let k=pickSel($('cKey')); if(full) k=pickSel($('cMode'))||k; if(k){ harm=true; moved.push('🎼 Key: '+$('cKey').selectedOptions[0].text+' '+$('cMode').value); } }
  if(T0.has('b-prog')&&pickSel($('cProg'))){ harm=true; moved.push('🔗 Progression: '+$('cProg').selectedOptions[0].text); }
  const laneT=LANES.filter(([k])=>T0.has('b-'+k));
  if(laneT.length||harm){ const cb=$('cBars'); if(cb&&[...cb.options].some(o=>+o.value===P.bars)) cb.value=String(P.bars);
   try{ if(harm&&!harmony) T.compose(); const s=$('cShuf'); if(s) s.click(); else T.composeKeep(); }catch(_){ }
   await sleep(80); if(P.bars!==oldBars) P.setBars(oldBars);
   const CT=clone(T.CT)||{}; LANES.forEach(([k])=>{ if(!T0.has('b-'+k)&&!(harm&&!harmony&&!LOCK['b-'+k])) CT[k]=clone(snap.CT[k]||[]); if(LOCK['b-'+k]) CT[k]=clone(snap.CT[k]||[]); });
   if(harmony){ try{ T.setChart(clone(snap.chart)||[]); }catch(_){ } }
   T.setCT(CT); T.redraw(); laneT.forEach(([k,ic,n])=>moved.push(ic+' '+n)); }
  /* the drums: every drum track not chosen or locked comes back exactly as it was */
  let drumPick=[];
  if(T0.has('b-drums')){ drumPick=full?drumOpen:some(drumOpen.filter(hasHits).length?drumOpen.filter(hasHits):drumOpen,0.3);
   if(!P.pads.slice(0,16).some((p,i)=>hasHits(i))){ const cd=$('cDrums'); const was=cd&&cd.value; if(cd&&(was==='keep'||was==='none')) cd.value='genre'; try{ T.writeDrums(); }catch(_){ } if(cd&&was!=null) cd.value=was; }
   else drumPick.forEach(i=>vary(P.pads[i].steps,i,P.bars*P.spb,P.spb));
   moved.push('🥁 '+(drumPick.length===drumOpen.length?'Drums':drumPick.map(i=>P.pads[i].name).join(', '))); }
  for(let i=0;i<16;i++) if(!drumPick.includes(i)) P.pads[i].steps=snap.steps[i].slice();
  P.refresh(); busy=false; paintAll();
  const held=BEAT.filter(g=>LOCK[g.k]).map(g=>g.ic+' '+g.n).concat([...Array(16).keys()].filter(i=>LOCK['p-'+i]).map(i=>'🥁 '+P.pads[i].name));
  note(box,(full?'🎲 Complete shuffle: ':'🔀 Partial shuffle: ')+(moved.join(' · ')||'nothing moved')+'.'+(held.length?' Held by your locks: '+held.join(' · ')+'.':'')+(harmony?' Key and chords stay with your locked lanes, so everything stays in tune.':'')+' ↶ Undo puts it back.'); }
 async function undoBeat(box){ if(busy) return note(box,'One moment: the shuffle is still landing.'); if(!lastBeat) return note(box,'No beat shuffle to undo yet.'); await beatRestore(lastBeat); lastBeat=null; note(box,'↶ The beat is back as it was before the shuffle.'); }

 /* ================= LOOP TOOLS: double, copy a bar, paste a bar ================= */
 const EXT=k=>{ try{ return PS().EXT.find(x=>x.key===k); }catch(_){ return null; } };
 const UNDO=[]; let CLIP=null;
 async function loopSnap(){ const o=beatSnap(); for(const k of ['keys','seq']){ const x=EXT(k); if(x){ try{ o[k]=clone(await x.full()); }catch(_){ } } } return o; }
 async function loopRestore(o){ await beatRestore(o); for(const k of ['keys','seq']){ const x=EXT(k); if(x&&o[k]){ try{ await x.load(clone(o[k])); }catch(_){ } } } PS().refresh(); }
 const dblNotes=(a,L)=>{ const f=(a||[]).filter(n=>n.s<L); return f.concat(f.map(n=>Object.assign({},n,{s:n.s+L}))); };
 async function double(box){ const P=PS(); if(!P) return note(box,'Open the 🎛 Studio first.'); const b=P.bars; if(b>=32) return note(box,'The loop is at its longest: 32 bars.');
  const nb=Math.min(32,b*2), L=b*P.spb; UNDO.push(await loopSnap()); if(UNDO.length>20) UNDO.shift();
  P.setBars(nb);
  const T=TH(); if(T){ const CT={}; Object.entries(T.CT||{}).forEach(([k,a])=>CT[k]=dblNotes(a,L)); const ch=clone(T.chart)||[]; T.setCT(CT); try{ T.setChart(ch.length===b?ch.concat(clone(ch)):ch); }catch(_){ T.redraw(); } const cb=$('cBars'); if(cb&&[...cb.options].some(o=>+o.value===nb)) cb.value=String(nb); }
  const xk=EXT('keys'); if(xk){ try{ const o=await xk.full(); o.kt=dblNotes(o.kt,L); await xk.load(o); }catch(_){ } }
  const xs=EXT('seq'); if(xs){ try{ const o=clone(await xs.full()); (o.ITR||[]).forEach(t=>t.notes=dblNotes(t.notes,L)); Object.keys(o.MASK||{}).forEach(k=>{ const m=o.MASK[k]; if(Array.isArray(m)) o.MASK[k]=m.slice(0,b).concat(m.slice(0,b)); else if(m&&typeof m==='object') for(let i=0;i<b;i++) if(i in m) m[i+b]=m[i]; }); await xs.load(o); }catch(_){ } }
  P.refresh(); paintAll(); note(box,'🔁 Loop doubled: '+b+' → '+nb+' bar'+(nb>1?'s':'')+'. Every drum, lane and recording was copied, so it plays the same twice; now change the new half. ↶ Undo puts it back.'); }
 function barNotes(a,b,spb){ return (a||[]).filter(n=>Math.floor(n.s/spb)===b).map(n=>Object.assign({},n,{s:n.s-b*spb})); }
 async function copyBar(box){ const P=PS(); if(!P) return note(box,'Open the 🎛 Studio first.'); const b=+(($('kLoopFrom')||{}).value||0), spb=P.spb; const T=TH(); const xk=EXT('keys'); let kt=[]; if(xk){ try{ kt=(await xk.full()).kt||[]; }catch(_){ } }
  CLIP={from:b,steps:P.pads.map(p=>p.steps.slice(b*spb,(b+1)*spb)),CT:T?Object.fromEntries(Object.entries(T.CT||{}).map(([k,a])=>[k,barNotes(a,b,spb)])):{},kt:barNotes(kt,b,spb)};
  note(box,'⧉ Bar '+(b+1)+' is copied: drums, lanes and keys. Pick a bar and press 📋 Paste bar.'); }
 async function pasteBar(box){ const P=PS(); if(!P) return note(box,'Open the 🎛 Studio first.'); if(!CLIP) return note(box,'Copy a bar first with ⧉ Copy bar.'); const to=+(($('kLoopTo')||{}).value||0), spb=P.spb;
  UNDO.push(await loopSnap()); if(UNDO.length>20) UNDO.shift();
  P.pads.forEach((p,i)=>{ for(let s=0;s<spb;s++) p.steps[to*spb+s]=CLIP.steps[i][s]||0; });
  const put=(a,c)=>(a||[]).filter(n=>Math.floor(n.s/spb)!==to).concat((c||[]).map(n=>Object.assign({},n,{s:n.s+to*spb})));
  const T=TH(); if(T){ const CT={}; Object.entries(T.CT||{}).forEach(([k,a])=>CT[k]=put(a,CLIP.CT[k])); T.setCT(CT); T.redraw(); }
  const xk=EXT('keys'); if(xk){ try{ const o=await xk.full(); o.kt=put(o.kt,CLIP.kt); await xk.load(o); }catch(_){ } }
  P.refresh(); note(box,'📋 Bar '+(CLIP.from+1)+' is pasted over bar '+(to+1)+'. ↶ Undo puts it back.'); }
 async function undoLoop(box){ const o=UNDO.pop(); if(!o) return note(box,'Nothing to undo in the loop tools yet.'); await loopRestore(o); paintAll(); note(box,'↶ The loop is back as it was: '+o.bars+' bar'+(o.bars>1?'s':'')+'.'); }

 /* ================= THE BOXES ================= */
 const css=document.createElement('style'); css.textContent=`
.kLockBox{border:1px solid rgba(255,233,74,.45);border-radius:14px;padding:10px 12px;margin:8px 0 14px;background:rgba(255,233,74,.05)}
.kLockBox h4{margin:0 0 4px!important;color:#ffe94a!important;font-size:15px!important}
.kLockBox .kLockN{margin:0 0 8px;font-size:12.5px;opacity:.85;line-height:1.45}
.kLockChips{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 8px}
.kLockChips button{min-height:36px!important;padding:4px 10px!important;border-radius:999px!important;font-size:12.5px!important}
.kLockChips button[aria-pressed="true"]{background:#7a5a00!important;color:#fff!important;border-color:#ffe94a!important}
.kLockChips button.kHeld{opacity:.6}
.kLockRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.kLockRow button{min-height:40px!important}
.kLockMsg{margin-top:8px;font-size:12.5px;line-height:1.45;min-height:1em}
.kLockSub{font-size:12px;opacity:.8;margin:6px 0 2px}
#kLoopRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:6px 0;padding:6px 8px;border:1px dashed rgba(0,229,255,.4);border-radius:10px}
#kLoopRow button{min-height:36px!important}
#kLoopPath b{color:#ffe94a}
#kLock{position:fixed;inset:0;z-index:9700;background:rgba(5,6,22,.97);overflow:auto;padding:14px 16px calc(230px + env(safe-area-inset-bottom,0px));padding-right:calc(var(--kRailW,58px) + 16px);color:#fff}
#kLock[hidden]{display:none!important}
#kLock .kLkIn{max-width:860px;margin:0 auto}
#kLock .kLkTabs{display:flex;gap:6px;margin:6px 0 10px}
#kLock .kLkTabs button[aria-pressed="true"]{background:#137a3f!important}`; document.head.appendChild(css);
 function note(box,m){ (box?[box]:Q('.kLockBox')).forEach(b=>{ const x=b.querySelector('.kLockMsg'); if(x) x.textContent=m; }); say(m.length>120?m.slice(0,118)+'…':m); }
 function chip(k,ic,n,extra){ return '<button type="button" data-lock="'+k+'" aria-pressed="'+!!LOCK[k]+'" class="'+(extra||'')+'" data-noul>'+(LOCK[k]?'🔒 ':'🔓 ')+ic+' '+esc(n)+'</button>'; }
 function boxHTML(scope){ const P=PS(); const harmony=LANES.some(([k])=>LOCK['b-'+k]);
  if(scope==='story') return '<h4>🔒 Lock & Shuffle · the story</h4><p class="kLockN">Lock what you want to keep: the content, the storyline, the characters, the audience, the genre, the tone, the form. 🔀 Partial shuffle lets the cannon move a few unlocked pieces; 🎲 Complete shuffle moves every unlocked piece. Locked pieces never move.</p><div class="kLockChips">'+STORY.map(g=>chip(g.k,g.ic,g.n)).join('')+'</div><div class="kLockRow"><button type="button" data-lk="part" data-noul>🔀 Partial shuffle</button><button type="button" data-lk="full" data-noul>🎲 Complete shuffle</button><button type="button" data-lk="lockall" data-noul>🔒 Lock all</button><button type="button" data-lk="none" data-noul>🔓 Unlock all</button><button type="button" data-lk="undo" data-noul>↶ Undo</button></div><div class="kLockMsg" role="status"></div>';
  const tracks=P?[...Array(16).keys()].filter(i=>hasHits(i)||LOCK['p-'+i]):[];
  return '<h4>🔒 Lock & Shuffle · the beat</h4><p class="kLockN">Lock the parts of the beat you love and shuffle the rest. Lock a lane (bass, chords, melody, guitar) and the key and chords stay with it, so everything stays in tune. Lock single drum tracks below.</p><div class="kLockChips">'+BEAT.map(g=>chip(g.k,g.ic,g.n,harmony&&(g.k==='b-key'||g.k==='b-prog')&&!LOCK[g.k]?'kHeld':'')).join('')+'</div>'+
   '<div class="kLockSub">Drum tracks in this loop'+(tracks.length?'':': none yet. Write or tap a beat and they appear here.')+'</div><div class="kLockChips" data-tr="1">'+tracks.map(i=>chip('p-'+i,'🥁',P.pads[i].name)).join('')+'</div>'+
   '<div class="kLockRow"><button type="button" data-lk="part" data-noul>🔀 Partial shuffle</button><button type="button" data-lk="full" data-noul>🎲 Complete shuffle</button><button type="button" data-lk="lockall" data-noul>🔒 Lock all</button><button type="button" data-lk="none" data-noul>🔓 Unlock all</button><button type="button" data-lk="undo" data-noul>↶ Undo</button></div><div class="kLockMsg" role="status"></div>'; }
 function paint(box){ const m=box.querySelector('.kLockMsg'); const keep=m?m.textContent:''; box.innerHTML=boxHTML(box.dataset.scope); const n=box.querySelector('.kLockMsg'); if(n) n.textContent=keep; box.dataset.sig=sig(box.dataset.scope); }
 const sig=scope=>scope==='beat'&&PS()?[...Array(16).keys()].map(i=>hasHits(i)?1:0).join('')+JSON.stringify(LOCK):JSON.stringify(LOCK);
 function paintAll(){ Q('.kLockBox[data-scope="story"],.kLockBox[data-scope="beat"]').forEach(paint); paintLoop(); }
 function onBox(e){ const box=e.target.closest('.kLockBox'); if(!box) return; const b=e.target.closest('button'); if(!b||(!b.dataset.lock&&!b.dataset.lk)) return; e.stopPropagation(); const scope=box.dataset.scope;
  if(b.dataset.lock){ const k=b.dataset.lock; LOCK[k]=!LOCK[k]; if(!LOCK[k]) delete LOCK[k]; saveL(); paintAll(); return note(box,(LOCK[k]?'🔒 Locked: ':'🔓 Unlocked: ')+b.textContent.replace(/^[🔒🔓]\s*/u,'')+'.'); }
  const a=b.dataset.lk; if(!a) return;
  if(a==='lockall'||a==='none'){ const keys=scope==='story'?STORY.map(g=>g.k):BEAT.map(g=>g.k).concat([...Array(16).keys()].map(i=>'p-'+i)); keys.forEach(k=>{ if(a==='lockall'&&(k.indexOf('p-')!==0||hasHits(+k.slice(2)))) LOCK[k]=true; else delete LOCK[k]; }); saveL(); paintAll(); return note(box,a==='lockall'?'🔒 Every piece is locked.':'🔓 Every piece is unlocked.'); }
  if(a==='undo') return scope==='story'?undoStory(box):undoBeat(box);
  const full=a==='full'; return scope==='story'?shuffleStory(full,box):shuffleBeat(full,box); }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('.kLockBox')) onBox(e); },true);
 function mkBox(scope){ const d=document.createElement('div'); d.className='kLockBox'; d.dataset.scope=scope; paint(d); return d; }
 /* the loop row beside the loop length */
 function paintLoop(){ const r=$('kLoopRow'), P=PS(); if(!r||!P) return; const b=P.bars; const path=[1,2,4,8,16,32].map(n=>n===b?'<b>'+n+'</b>':n).join(' → '); const p=$('kLoopPath'); if(p) p.innerHTML=path;
  ['kLoopFrom','kLoopTo'].forEach(id=>{ const s=$(id); if(!s) return; if(s.options.length!==b){ const v=Math.min(b-1,+s.value||0); s.innerHTML=[...Array(b).keys()].map(i=>'<option value="'+i+'">'+(i+1)+'</option>').join(''); s.value=String(v); } }); }
 function mountLoop(){ if($('kLoopRow')) return; const lb=$('padLoopBars'); const host=lb&&lb.closest('label'); if(!host||!host.parentElement) return;
  const r=document.createElement('div'); r.id='kLoopRow'; r.innerHTML='<button type="button" data-lp="dbl" data-noul>×2 Double the loop</button><span class="kLockN" id="kLoopPath"></span><label>Bar <select id="kLoopFrom" aria-label="Bar to copy"></select></label><button type="button" data-lp="copy" data-noul>⧉ Copy bar</button><label>onto bar <select id="kLoopTo" aria-label="Bar to paste over"></select></label><button type="button" data-lp="paste" data-noul>📋 Paste bar</button><button type="button" data-lp="undo" data-noul>↶ Undo</button><span class="kLockMsg" role="status" style="flex-basis:100%"></span>';
  host.parentElement.insertBefore(r,host.nextSibling); r.classList.add('kLockBox'); r.dataset.scope='loop'; r.style.border='1px dashed rgba(0,229,255,.4)';
  r.addEventListener('click',e=>{ const b=e.target.closest('[data-lp]'); if(!b) return; e.stopPropagation(); const a=b.dataset.lp; if(a==='dbl') double(r); else if(a==='copy') copyBar(r); else if(a==='paste') pasteBar(r); else undoLoop(r); },true); paintLoop(); }
 function mount(){ if(!$('kLockStory')){ const drift=$('s-drift'); if(drift&&drift.parentElement){ const d=mkBox('story'); d.id='kLockStory'; drift.parentElement.insertBefore(d,drift); } }
  if(!$('kLockBeat')){ const cw=$('cmpWrap'); if(cw&&cw.parentElement){ const d=mkBox('beat'); d.id='kLockBeat'; cw.parentElement.insertBefore(d,cw); } }
  mountLoop(); }
 /* repaint the drum chips when the beat changes, only while a beat box is on screen */
 setInterval(()=>{ mount(); Q('.kLockBox[data-scope="beat"]').forEach(b=>{ if(b.getClientRects().length&&b.dataset.sig!==sig('beat')) paint(b); }); paintLoop(); },1500);
 /* the floating Lock & Shuffle, from the Menu and the remote */
 function open(scope){ let d=$('kLock'); if(!d){ d=document.createElement('div'); d.id='kLock'; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Lock and shuffle'); d.hidden=true; document.body.appendChild(d);
   d.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; if(b.dataset.lkx!=null){ e.stopPropagation(); close(); } if(b.dataset.lkt){ e.stopPropagation(); draw(b.dataset.lkt); } }); }
  const draw=sc=>{ d.innerHTML='<div class="kBar" data-sc="kLock"><button type="button" data-ka="close" data-lkx="1" aria-label="Close">✕</button></div><div class="kLkIn"><div class="kLockN">The Omni-Compass LLC · Omni-Galaxy Multi-Media Studios’ KAN-IN™</div><h2>🔒 Lock & Shuffle</h2><div class="kLkTabs"><button type="button" data-lkt="story" aria-pressed="'+(sc==='story')+'" data-noul>📖 The story</button><button type="button" data-lkt="beat" aria-pressed="'+(sc==='beat')+'" data-noul>🎛 The beat</button></div></div>'; const b=mkBox(sc); d.querySelector('.kLkIn').appendChild(b); };
  draw(scope==='beat'?'beat':'story'); d.hidden=false; d.scrollTop=0; }
 function close(){ const d=$('kLock'); if(d) d.hidden=true; }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&$('kLock')&&!$('kLock').hidden) close(); });
 try{ const gh=window.GOHOME; if(gh&&!gh.__klk){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__klk=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(!e.target.closest) return; if(e.target.closest('#kdHome,#lpMenu')) return close(); const r=e.target.closest('#rDock button,#tourTab button'); if(r&&r.id!=='ttLock'&&$('kLock')&&!$('kLock').hidden) close(); },true);
 /* the Menu: 🔒 Lock & shuffle beside the story and the beat */
 setInterval(()=>{ const t=$('tourTab'); if(!t||$('ttLock')) return; const b=document.createElement('button'); b.type='button'; b.id='ttLock'; b.className='ttMusic'; b.textContent='🔒 Lock & shuffle · keep what you love, shuffle the rest'; b.style.order='101'; b.dataset.kg='0'; b.dataset.kmDone='1'; b.setAttribute('data-noul',''); b.style.gridColumn='1/-1'; b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>open(),120); }); t.appendChild(b); },900);
 window.KLOCK={open,close,shuffleStory,shuffleBeat,double:()=>double($('kLoopRow')),copyBar:()=>copyBar($('kLoopRow')),pasteBar:()=>pasteBar($('kLoopRow')),undoLoop:()=>undoLoop($('kLoopRow')),LOCK,mount,get busy(){ return busy; }};
 setTimeout(mount,1200);
})();
