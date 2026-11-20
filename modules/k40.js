(()=>{ /* 40 TRACKS (v210): one track map for the sequencer, the mixer and the MIDI wiring, two rows of 20.
   1–16 the 16 pads, one each · 17 pads B–D · 18 keyboard (MIDI 1) · 19 bass · 20 chords · 21 melody · 22 guitar · 23 wave loops ·
   24–28 five microphones (lead, backup, ad-libs, harmony, hook: karaoke takes 1–5 and on) · 29–30 DJ decks A and B ·
   31–38 MIDI 2–9, each with its own sound wired in from the start · 39 cannon and sound bank · 40 click. All 16 MIDI channels land:
   1 and 16 the keyboard, 2–9 tracks 31–38, 10 the pads, 11–14 bass, chords, melody and guitar, 15 the sound bank. Every strip has an
   input picker, so any source can be wired to any track. Instrument tracks added in the song sequencer land on MIDI 2–9 first.
   The Studio lands on its hero: the sequencer (🥁 beat · 🎚 40 tracks) with the pads or keys floating, then the 40-track mixer;
   every module, effect and editor stays below. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const PS=()=>window.PADSTUDIO;
 const MIDIDEF=[['🎻','Strings','string'],['🎺','Brass','brass'],['🔔','Bells','bell'],['⛪','Organ','organ'],['🪕','Pluck','pluck'],['🎛','Lead synth','lead'],['🌫','Pad','pad'],['🎸','Synth bass','bass']];
 const BASE=['🎤 Mic 2 · backup','🎤 Mic 3 · ad-libs','🎤 Mic 4 · harmony','🎤 Mic 5 · hook','🎧 DJ deck A','🎧 DJ deck B'].concat(MIDIDEF.map((d,k)=>'🎹 MIDI '+(k+2)+' · '+d[1])).concat(['💥 Cannon · sound bank','🕒 Click']);
 const presetFor=ci=>{ const d=MIDIDEF[ci-30]; const O=[...document.querySelectorAll('#kbPre option')].map(o=>o.value); if(!d) return O[0]||'pad'; return O.find(v=>v.toLowerCase().includes(d[2]))||O.find(v=>v.toLowerCase().includes('pad'))||O[0]||'pad'; };
 const SLOTS=[30,31,32,33,34,35,36,37]; /* where song-sequencer instruments land */
 const VOX=[23,24,25,26,27]; const DJC={A:28,B:29};
 let M=Object.assign({vox:{},dj:{},it:{}},getLS('kanin-k40',{}));
 const save=()=>putLS('kanin-k40',M);
 const itr=()=>window.SQITR||[];
 const slot=i=>M.it[i]!=null?M.it[i]:(i<SLOTS.length?SLOTS[i]:40+(i-SLOTS.length));
 function extra(){ const n=BASE.slice(); itr().forEach((t,i)=>{ const c=slot(i); if(c<40){ n[c-24]=n[c-24].replace(/ · .*$/,'')+' · '+t.name; } else n[c-24]='🎹 '+t.name; }); for(let k=0;k<n.length;k++) if(n[k]==null) n[k]='➕ Track '+(25+k); return n; }
 const voxCi=k=>M.vox[k]!=null?M.vox[k]:VOX[k%5];
 const djCi=d=>M.dj[d]!=null?M.dj[d]:DJC[d];
 function mixGain(ci){ const X=PS()&&PS().MIX; if(!X||!X[ci]) return 1; const so=X.some(m=>m&&m.solo); if(X[ci].mute) return 0; if(so&&!X[ci].solo) return 0; return X[ci].vol; }
 const EXT=[]; function track(g,ci,base){ EXT.push({g,ci,base}); if(EXT.length>64) EXT.shift(); }
 function syncExt(){ EXT.forEach(e=>{ try{ e.g.gain.value=e.base*mixGain(e.ci); }catch(_){ } }); ['A','B'].forEach(d=>{ const ci=djCi(d); const s=document.querySelector('#deck'+d+' input[data-k="vol"]'); if(!s) return; const v=String(Math.round(Math.min(1.2,mixGain(ci))*100)); if(s.value!==v){ s.value=v; s.dispatchEvent(new Event('input',{bubbles:true})); } }); }
 function apply(){ itr().forEach((t,i)=>t.ch=slot(i)); window.EXTRACH=extra(); try{ PS().renderMixer(); }catch(_){ } }
 window.K40={slot,extra,voxCi,voxGain:k=>mixGain(voxCi(k)),track,apply,get map(){ return M; }};
 /* ── the mixer: two rows of 20 ── */
 const css=document.createElement('style'); css.textContent=`
html body #padMixer#padMixer{grid-template-columns:repeat(20,minmax(0,1fr))!important}
@media (max-width:999px){ html body #padMixer#padMixer{grid-template-columns:repeat(20,40px)!important;overflow-x:auto!important;overscroll-behavior-x:contain} }
html body #padMixer#padMixer .mxs .k40in{width:100%;max-width:100%;min-height:22px;padding:0!important;font:600 9px system-ui,sans-serif;border-radius:5px;background:#0b1a36;color:#cfe;border:1px solid #2c4a7a;text-overflow:clip}
html body #padMixer#padMixer .mxs .k40in:disabled{opacity:.55}
@media (min-width:1700px){ html body #padMixer#padMixer .mxv{height:130px!important} html body #padMixer#padMixer small{font-size:11px!important} html body #padMixer#padMixer .mxs .k40in{font-size:11px;min-height:28px} html body #padMixer#padMixer .mxb button{min-height:28px!important;font-size:12px!important} }
@media (min-width:2500px){ html body #padMixer#padMixer .mxv{height:180px!important} html body #padMixer#padMixer small{font-size:15px!important} html body #padMixer#padMixer .mxs .k40in{font-size:14px;min-height:36px} html body #padMixer#padMixer .mxb button{min-height:36px!important;min-width:40px!important;font-size:15px!important} }
#kSeqTabs{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 4px}
#kSeqTabs button{min-height:44px;border-radius:12px;padding:4px 14px!important;font:800 clamp(13px,1vw,20px)/1.2 system-ui,sans-serif;white-space:normal}
#kSeqTabs button.on{background:#ffe94a!important;color:#14163a!important}
html[data-seqtab="40"] #crSec{display:none!important}
html:not([data-seqtab="40"]) #k40Seq{display:none!important}
#k40Seq{margin:6px 0 10px;padding:8px 10px;border:1px solid rgba(255,122,217,.55);border-radius:14px;background:linear-gradient(180deg,rgba(26,10,40,.94),rgba(8,6,22,.94));color:#fff}
#k40Seq h4{margin:0 0 6px;font:800 clamp(14px,1.1vw,22px) system-ui,sans-serif;color:#ff9ae6;letter-spacing:.05em;text-transform:uppercase}
#k40Seq .k4Bar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:4px 0 6px}
#k40Seq .k4Bar button{min-height:38px;border-radius:9px;padding:2px 10px!important;font:700 clamp(12px,.9vw,18px) system-ui,sans-serif;white-space:normal}
#k40Seq .k4Bar button.on{background:#ffe94a!important;color:#14163a!important}
#k40Seq .k4Bar b{font:700 clamp(12px,.9vw,18px) system-ui,sans-serif;color:#ffd6f4}
#k40Seq .kWrap{overflow-x:auto;overscroll-behavior-x:contain;max-width:100%}
#k40Grid{display:grid;gap:2px;min-width:min-content}
#k40Grid .h{display:flex;align-items:center;gap:3px;min-width:0;padding:1px 4px;border-radius:6px;background:rgba(255,255,255,.05);font:700 clamp(11px,.85vw,17px)/1.15 system-ui,sans-serif}
#k40Grid .h i{font-style:normal;color:#ffe94a;min-width:2.1em;text-align:right}
#k40Grid .h span{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#k40Grid .h button{min-height:24px!important;min-width:26px!important;padding:0 4px!important;border-radius:6px;font:800 11px system-ui,sans-serif}
#k40Grid .h button.on{background:#ffe94a!important;color:#14163a!important}
#k40Grid .h button.m.on{background:#b3172f!important;color:#fff!important}
#k40Grid .bh{font:700 11px ui-monospace,monospace;color:#9fe;text-align:center;align-self:end}
#k40Grid .c{min-height:clamp(22px,1.6vw,40px);border-radius:5px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);cursor:pointer;touch-action:none}
#k40Grid .c.has{background:linear-gradient(180deg,#ff7ad9,#b04bd0);border-color:#ffd0f2}
#k40Grid .c.off{opacity:.25;background:repeating-linear-gradient(45deg,#333 0 4px,#222 4px 8px)}
#k40Grid .c.sel{outline:2px solid #ffe94a;outline-offset:-2px}
#k40Grid .grp{grid-column:1/-1;font:800 11px ui-monospace,monospace;letter-spacing:.12em;color:#7ff;padding:6px 2px 0}`; document.head.appendChild(css);
 /* every strip's input picker */
 const NATIVE0=[[16,'Pads B–D'],[17,'Keyboard · MIDI 1'],[18,'Bass line'],[19,'Chords'],[20,'Melody'],[21,'Rhythm guitar'],[22,'Wave loops'],[23,'Studio vocals']];
 const NATIVE=NATIVE0; const routeOf=n=>(window.KCHMAP&&KCHMAP[n]!=null)?KCHMAP[n]:n;
 function sources(){ const L=[['none','— empty —']]; NATIVE.forEach(([n,l])=>L.push(['n:'+n,l])); for(let k=0;k<Math.max(5,(window.KKLAYERS&&KKLAYERS.count)?KKLAYERS.count():0);k++) L.push(['v:'+k,'Mic · karaoke take '+(k+1)]); L.push(['dj:A','DJ deck A'],['dj:B','DJ deck B']); itr().forEach((t,i)=>L.push(['it:'+i,'🎹 '+t.name])); MIDIDEF.forEach((d,k)=>L.push(['m:'+(30+k),'MIDI '+(k+2)+' · '+d[1]])); L.push(['m:38','Cannon · sound bank'],['click','Click']); return L; }
 function srcOf(ci){ if(ci<16) return 'pad'; for(const [n] of NATIVE) if(routeOf(n)===ci) return 'n:'+n; for(let k=0;k<Math.max(5,(window.KKLAYERS&&KKLAYERS.count)?KKLAYERS.count():0);k++) if(voxCi(k)===ci) return 'v:'+k; if(ci>=30&&ci<=37) return 'm:'+ci; if(ci===38) return 'm:38'; if(ci===39) return 'click'; for(const d of ['A','B']) if(djCi(d)===ci) return 'dj:'+d; const T=itr(); for(let i=0;i<T.length;i++) if(slot(i)===ci) return 'it:'+i; return 'none'; }
 function setSrc(ci,v){ const [k,x]=v.split(':'); const was=srcOf(ci);
  if(was.startsWith('n:')){ try{ KIO.setRoute(+was.slice(2),+was.slice(2)); }catch(_){ } } if(was.startsWith('v:')) delete M.vox[+was.slice(2)]; if(was.startsWith('dj:')) delete M.dj[was.slice(3)];
  if(k==='n'){ try{ KIO.setRoute(+x,ci); }catch(_){ (window.KCHMAP=window.KCHMAP||{})[+x]=ci; } } else if(k==='v') M.vox[+x]=ci; else if(k==='dj') M.dj[x]=ci; else if(k==='it') M.it[+x]=ci;
  save(); apply(); say('🎚 Track '+(ci+1)+' now takes '+((sources().find(s=>s[0]===v)||[0,'nothing'])[1])+'.'); }
 function pickers(){ const m=$('padMixer'); if(!m) return; const S=sources(); const html=S.map(s=>'<option value="'+s[0]+'">'+s[1]+'</option>').join('');
  m.querySelectorAll('.mxs[data-c]').forEach(st=>{ const ci=+st.dataset.c; let sel=st.querySelector('.k40in'); if(!sel){ sel=document.createElement('select'); sel.className='k40in'; sel.dataset.ci=ci; st.appendChild(sel); }
   if(ci===23){ const sm=st.querySelector('small'); if(sm&&!/Mic 1/.test(sm.textContent)){ sm.innerHTML='24<br>🎤 Mic 1 · lead'; sm.title='Mic 1 · lead vocal'; } }
   if(ci<16){ if(!sel.disabled){ sel.innerHTML='<option>Pad A'+(ci+1)+'</option>'; sel.disabled=true; sel.title='Pad A'+(ci+1)+' is wired to track '+(ci+1); } return; }
   if(sel.dataset.h!==String(S.length)){ sel.innerHTML=html; sel.dataset.h=String(S.length); } const v=srcOf(ci); if(sel.value!==v) sel.value=v; sel.title='Input of track '+(ci+1)+': '+((S.find(s=>s[0]===v)||[0,'empty'])[1]); }); }
 document.addEventListener('change',e=>{ const s=e.target.closest&&e.target.closest('#padMixer .k40in'); if(!s) return; setSrc(+s.dataset.ci,s.value); },true);
 document.addEventListener('input',e=>{ if(e.target.closest&&e.target.closest('#padMixer .mxs')) setTimeout(syncExt,0); },true);
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#padMixer .mxb button')) setTimeout(()=>{ syncExt(); paintSeq(); },30); },true);
 /* ── the 40-track sequencer ── */
 const TRK=()=>{ const N=(()=>{ try{ return PS().pads.slice(0,16).map((p,i)=>'A'+(i+1)+' '+p.name); }catch(_){ return Array.from({length:16},(_,i)=>'Pad A'+(i+1)); } })();
  const R=N.map((n,i)=>({ci:i,name:'🥁 '+n,kind:'pad',pads:[i]}));
  R.push({ci:16,name:'🥁 Pads B–D',kind:'pad',pads:Array.from({length:48},(_,k)=>16+k)},{ci:17,name:'🎹 Keyboard · MIDI 1',kind:'mask',ids:['keys'],arm:'keys'},{ci:18,name:'🎸 Bass line',kind:'mask',ids:['bass']},{ci:19,name:'🎹 Chords',kind:'mask',ids:['chords']},{ci:20,name:'🎼 Melody',kind:'mask',ids:['melody']},{ci:21,name:'🎸 Rhythm guitar',kind:'mask',ids:['gtr']},{ci:22,name:'〰 Wave loops',kind:'loops'},{ci:23,name:'🎤 Mic 1 · lead',kind:'vox'});
  const X=extra(); X.forEach((n,k)=>{ const ci=24+k; const T=itr(); const ii=T.findIndex((t,i)=>slot(i)===ci); R.push({ci,name:n,kind:ii>=0?'itr':(ci===28||ci===29)?'dj':VOX.includes(ci)?'vox':ci===38?'cannon':ci===39?'click':(ci>=30&&ci<=37)?'midi':'aux',it:ii>=0?T[ii]:null}); }); return R; };
 const B=()=>{ try{ return PS().barsN||1; }catch(_){ return 1; } }, spb=()=>{ try{ return PS().spbN; }catch(_){ return 16; } };
 const amask=(id,b)=>!(window.ARRMASK&&ARRMASK(id,b)===false);
 const aset=(id,b,v)=>{ try{ ARRSET(id,b,v); }catch(_){ } };
 const mk=r=>r.kind==='pad'?r.pads.map(i=>'p'+i):r.kind==='mask'?r.ids:r.kind==='itr'?[r.it.id]:r.kind==='loops'?(PS().tracks||[]).map((t,k)=>'loop'+k):['k40_'+r.ci];
 function on(r,b){ if(r.kind==='loops'){ const L=(PS().tracks||[]).filter(t=>t&&t.buf); return !L.length||L.some(t=>t.on[b]!==false); } const ids=mk(r); return ids.some(id=>amask(id,b)); }
 function setOnR(r,b,v){ if(r.kind==='loops'){ (PS().tracks||[]).forEach(t=>{ if(t&&t.on) t.on[b]=v; }); return; } mk(r).forEach(id=>aset(id,b,v)); }
 function has(r,b){ const n=spb(), a=b*n; try{
  if(r.kind==='pad') return r.pads.some(i=>{ const st=PS().pads[i]&&PS().pads[i].steps; if(!st) return false; for(let s=a;s<a+n;s++) if(st[s]) return true; return false; });
  if(r.kind==='itr') return r.it.notes.some(x=>x.s>=a&&x.s<a+n);
  if(r.kind==='loops') return (PS().tracks||[]).some(t=>t&&t.buf);
  if(r.kind==='mask'){ if(r.ids[0]==='keys') return !!(window.KREC&&KREC.length); const c=$('co_'+r.ids[0]); return !!(c&&c.checked&&window.THEORY&&THEORY.CT&&THEORY.CT.chords.length); }
  if(r.kind==='dj'){ const D=window.DJBOOTH&&DJBOOTH.D[r.ci===djCi('A')?'A':'B']; return !!(D&&D.buf); }
 }catch(_){ } return false; }
 let sel=null, clip=null, drag=null, pasteMode=false;
 const snapAll=()=>({p:PS().pads.map(p=>Array.from(p.steps)),it:itr().map(t=>t.notes.map(n=>Object.assign({},n))),m:TRK().map(r=>Array.from({length:B()},(_,b)=>on(r,b)))});
 function remember(name){ const S=snapAll(); try{ KUNDO.push(()=>{ PS().pads.forEach((p,i)=>{ if(S.p[i]) p.steps=S.p[i].slice(); }); itr().forEach((t,i)=>{ if(S.it[i]) t.notes=S.it[i]; }); TRK().forEach((r,k)=>{ (S.m[k]||[]).forEach((v,b)=>setOnR(r,b,v)); }); redraw(); },name); }catch(_){ } }
 function redraw(){ try{ PS().refresh(); }catch(_){ } try{ CRACK.render(); }catch(_){ } try{ SQRENDER(); }catch(_){ } paintSeq(); }
 const rowsSel=()=>{ const R=TRK(); return sel?R.filter(r=>sel.rows.includes(r.ci)):R; };
 const range=()=>sel?[sel.a,sel.b]:[0,B()-1];
 function grab(){ const [a,b]=range(), n=spb(); return {len:b-a+1,rows:rowsSel().map(r=>({ci:r.ci,kind:r.kind,pads:r.kind==='pad'?r.pads.map(i=>({i,v:Array.from(PS().pads[i].steps.slice(a*n,(b+1)*n))})):null,notes:r.kind==='itr'?r.it.notes.filter(x=>x.s>=a*n&&x.s<(b+1)*n).map(x=>Object.assign({},x,{s:x.s-a*n})):null,mask:Array.from({length:b-a+1},(_,k)=>on(r,a+k))}))}; }
 function clearRange(rows,a,b,content){ const n=spb(); rows.forEach(r=>{ if(r.kind==='pad') r.pads.forEach(i=>{ const st=PS().pads[i].steps; for(let s=a*n;s<(b+1)*n;s++) st[s]=0; }); else if(r.kind==='itr') r.it.notes=r.it.notes.filter(x=>!(x.s>=a*n&&x.s<(b+1)*n)); else if(!content) for(let k=a;k<=b;k++) setOnR(r,k,false); }); }
 function put(c,at){ const n=spb(); while(at+c.len>B()&&B()<16){ try{ PS().setBars(B()*2); }catch(_){ break; } } const R=TRK(); c.rows.forEach(x=>{ const r=R.find(y=>y.ci===x.ci); if(!r) return; if(x.pads) x.pads.forEach(p=>{ const st=PS().pads[p.i].steps; p.v.forEach((v,k)=>{ const s=at*n+k; if(s<B()*n) st[s]=v; }); }); else if(x.notes&&r.it){ r.it.notes=r.it.notes.filter(y=>!(y.s>=at*n&&y.s<(at+c.len)*n)).concat(x.notes.map(y=>Object.assign({},y,{s:y.s+at*n}))); } x.mask.forEach((v,k)=>{ if(at+k<B()) setOnR(r,at+k,v); }); }); sel={rows:c.rows.map(x=>x.ci),a:at,b:Math.min(B()-1,at+c.len-1)}; }
 const ACT={
  copy:()=>{ clip=grab(); say('📋 Copied '+clip.len+' bar'+(clip.len>1?'s':'')+' on '+clip.rows.length+' tracks. Tap 📌 Paste, then the bar where it goes.'); },
  cut:()=>{ clip=grab(); remember('Cut'); const [a,b]=range(); clearRange(rowsSel(),a,b,true); redraw(); say('✂ Cut. Tap 📌 Paste, then the bar where it goes.'); },
  paste:()=>{ if(!clip) return say('Copy or cut a section first.'); pasteMode=!pasteMode; paintSeq(); if(pasteMode) say('📌 Tap the bar where the section should start.'); },
  dup:()=>{ const c=grab(); const [,b]=range(); remember('Duplicate'); put(c,b+1); redraw(); say('⧉ Duplicated after itself.'); },
  clear:()=>{ remember('Clear'); const [a,b]=range(); clearRange(rowsSel(),a,b,true); redraw(); say('🗑 Cleared.'); },
  mute:()=>{ remember('Mute bars'); const [a,b]=range(); rowsSel().forEach(r=>{ for(let k=a;k<=b;k++) setOnR(r,k,false); }); redraw(); },
  unmute:()=>{ remember('Unmute bars'); const [a,b]=range(); rowsSel().forEach(r=>{ for(let k=a;k<=b;k++) setOnR(r,k,true); }); redraw(); },
  all:()=>{ sel={rows:TRK().map(r=>r.ci),a:0,b:B()-1}; paintSeq(); },
  none:()=>{ sel=null; pasteMode=false; paintSeq(); },
  undo:()=>{ try{ KUNDO.any(); }catch(_){ } },
  bars:n=>{ remember('Bars'); try{ PS().setBars(n); }catch(_){ } setTimeout(redraw,120); },
  how:()=>say('Each row is one track, each box one bar. Pink boxes have music. Tap a box to switch that bar on or off. Drag across boxes to pick a section, then ✂ Cut, 📋 Copy, 📌 Paste, ⧉ Duplicate or 🗑 Clear it. ↶ Undo takes back the last move.')};
 function rowBtns(r){ const X=PS().MIX[r.ci]||{}; let h='<button type="button" class="m'+(X.mute?' on':'')+'" data-k4="m" title="Mute track '+(r.ci+1)+'">M</button><button type="button" class="'+(X.solo?'on':'')+'" data-k4="s" title="Solo track '+(r.ci+1)+'">S</button>';
  if(r.kind==='vox') h+='<button type="button" data-k4="vox" title="Record vocals in Karaoke">🎤</button>'; else if(r.kind==='dj') h+='<button type="button" data-k4="dj" title="Open the DJ decks">🎧</button>'; else if(r.kind==='cannon') h+='<button type="button" data-k4="fire" title="Fire the cannon: it writes parts on the tracks">💥</button>'; else if(r.arm) h+='<button type="button" data-k4="arm" title="Record the keyboard into the loop">●</button>'; else if(r.kind==='midi'||(r.kind==='aux'&&r.ci>=30)) h+='<button type="button" data-k4="add" title="Write a part for this track (its sound: '+presetFor(r.ci)+')">＋</button>'; else if(r.kind==='click') h+='<button type="button" data-k4="click" title="Click on or off">🕒</button>'; else if(r.kind==='pad') h+='<button type="button" data-k4="edit" title="Edit the steps in the beat sequencer">✏️</button>'; return h; }
 const GRP={0:'1–16 · THE 16 PADS',16:'17–23 · PADS B–D, KEYBOARD AND INSTRUMENTS',23:'24–28 · FIVE MICROPHONES',28:'29–30 · DJ DECKS',30:'31–38 · MIDI 2–9',38:'39–40 · CANNON, SOUND BANK AND CLICK'};
 function paintSeq(){ const g=$('k40Grid'); if(!g||!g.isConnected||document.documentElement.dataset.seqtab!=='40') return; const n=B(); const R=TRK();
  g.style.gridTemplateColumns='minmax(170px,clamp(170px,16vw,360px)) repeat('+n+',minmax(30px,1fr))';
  let h='<div></div>'+Array.from({length:n},(_,b)=>'<div class="bh">'+(b+1)+'</div>').join('');
  R.forEach(r=>{ if(GRP[r.ci]) h+='<div class="grp">'+GRP[r.ci]+'</div>'; h+='<div class="h" data-ci="'+r.ci+'"><i>'+(r.ci+1)+'</i><span title="'+r.name.replace(/"/g,'&quot;')+'">'+r.name+'</span>'+rowBtns(r)+'</div>'; for(let b=0;b<n;b++){ const s=sel&&sel.rows.includes(r.ci)&&b>=sel.a&&b<=sel.b; h+='<div class="c'+(has(r,b)?' has':'')+(on(r,b)?'':' off')+(s?' sel':'')+'" data-ci="'+r.ci+'" data-b="'+b+'" role="button" aria-label="Track '+(r.ci+1)+' bar '+(b+1)+'"></div>'; } });
  g.innerHTML=h; const bar=$('k40Bar'); if(bar){ bar.querySelectorAll('[data-bars]').forEach(x=>x.classList.toggle('on',+x.dataset.bars===n)); const p=bar.querySelector('[data-k4a="paste"]'); if(p) p.classList.toggle('on',pasteMode); const inf=$('k40Info'); if(inf) inf.textContent=(sel?'Picked: tracks '+sel.rows.map(c=>c+1).join(', ').slice(0,60)+' · bars '+(sel.a+1)+'–'+(sel.b+1):'Picked: everything')+' · Copied: '+(clip?clip.len+' bar'+(clip.len>1?'s':''):'nothing'); } }
 function build(){ const cr=$('crSec'); const pad=$('pad'); if(!cr||!pad) return; if(!$('kSeqTabs')){ const t=document.createElement('div'); t.id='kSeqTabs'; t.innerHTML='<button type="button" data-tab="beat" data-noul>🥁 Beat sequencer · the 16 pads</button><button type="button" data-tab="40" data-noul>🎚 40-track sequencer</button>'; cr.insertAdjacentElement('beforebegin',t);
   t.addEventListener('click',e=>{ const b=e.target.closest('[data-tab]'); if(!b) return; e.stopPropagation(); tab(b.dataset.tab); }); }
  if(!$('k40Seq')){ const s=document.createElement('div'); s.id='k40Seq'; s.innerHTML='<h4>🎚 40-track sequencer · every track by bars</h4><div class="k4Bar" id="k40Bar"><b>Bars</b>'+[1,2,4,8,16].map(n=>'<button type="button" data-bars="'+n+'" data-noul>'+n+'</button>').join('')+'<span style="flex:0 0 8px"></span>'+[['cut','✂ Cut'],['copy','📋 Copy'],['paste','📌 Paste'],['dup','⧉ Duplicate'],['clear','🗑 Clear'],['mute','🔇 Mute bars'],['unmute','🔊 Unmute'],['all','▦ Select all'],['none','⬚ Unselect'],['undo','↶ Undo'],['how','❓ How']].map(([k,l])=>'<button type="button" data-k4a="'+k+'" data-noul>'+l+'</button>').join('')+'</div><div class="k4Bar" style="margin-top:0"><b id="k40Info" style="font-weight:600;color:#d8cfff"></b></div><div class="kWrap"><div id="k40Grid"></div></div>';
   cr.insertAdjacentElement('afterend',s);
   s.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); if(b.dataset.bars) return ACT.bars(+b.dataset.bars); if(b.dataset.k4a) return ACT[b.dataset.k4a]();
    const h=b.closest('.h'); if(!h) return; const ci=+h.dataset.ci; const X=PS().MIX; const r=TRK().find(x=>x.ci===ci); const k=b.dataset.k4;
    if(k==='m'||k==='s'){ while(X.length<=ci) X.push({vol:.9,pan:0,mute:false,solo:false}); if(k==='m') X[ci].mute=!X[ci].mute; else X[ci].solo=!X[ci].solo; try{ PS().mixApply(); PS().renderMixer(); }catch(_){ } syncExt(); paintSeq(); return; }
    if(k==='vox'){ try{ KKARA.open(); }catch(_){ } return; } if(k==='dj'){ try{ KRAIL.FLOAT.open('dj'); }catch(_){ } return; } if(k==='fire'){ const f=$('sqFire'); if(f) f.click(); setTimeout(redraw,400); return; }
    if(k==='arm'){ const a=document.querySelector('#sqGrid [data-arm="keys"]'); if(a) a.click(); return; } if(k==='edit'){ tab('beat'); setTimeout(()=>{ const row=document.querySelector('#crRows .crRow[data-i="'+ci+'"]'); if(row) row.scrollIntoView({block:'center'}); },150); return; }
    if(k==='click'){ const c=$('padClick')||$('ktClick'); if(c) c.click(); return; } if(k==='add'){ const T=itr(); const n0=T.length; const sn=$('sqSnd'); if(sn){ const pr=presetFor(ci); if([...sn.options].some(o=>o.value===pr)) sn.value=pr; } const ad=$('sqAddI'); if(ad) ad.click(); setTimeout(()=>{ const T2=itr(); if(T2.length>n0){ M.it[T2.length-1]=ci; save(); apply(); } redraw(); },200); return; } });
   s.addEventListener('pointerdown',e=>{ const c=e.target.closest('#k40Grid .c'); if(!c) return; e.preventDefault(); const ci=+c.dataset.ci, b=+c.dataset.b; if(pasteMode){ remember('Paste'); put(clip,b); pasteMode=false; redraw(); say('📌 Pasted.'); return; } drag={ci,b,moved:false}; });
   s.addEventListener('pointermove',e=>{ if(!drag) return; const el=document.elementFromPoint(e.clientX,e.clientY); const c=el&&el.closest&&el.closest('#k40Grid .c'); if(!c) return; const ci=+c.dataset.ci, b=+c.dataset.b; if(ci===drag.ci&&b===drag.b&&!drag.moved) return; drag.moved=true; const R=TRK().map(r=>r.ci); const i0=R.indexOf(drag.ci), i1=R.indexOf(ci); sel={rows:R.slice(Math.min(i0,i1),Math.max(i0,i1)+1),a:Math.min(drag.b,b),b:Math.max(drag.b,b)}; paintSeq(); });
   const up=()=>{ if(!drag) return; const d=drag; drag=null; if(!d.moved){ const r=TRK().find(x=>x.ci===d.ci); remember('Bar on/off'); setOnR(r,d.b,!on(r,d.b)); redraw(); } };
   s.addEventListener('pointerup',up); s.addEventListener('pointercancel',up); }
  /* the order under the sequencer: the mixer first, the inputs panel after it */
  const io=$('kIO'), djs=$('kDjStrips'); if(io&&djs&&djs.nextElementSibling!==io) djs.insertAdjacentElement('afterend',io); }
 function tab(t){ const pad=$('pad'); if(!pad) return; document.documentElement.dataset.seqtab=t; putLS('kanin-seqtab',t); const T=$('kSeqTabs'); if(T) T.querySelectorAll('[data-tab]').forEach(b=>b.classList.toggle('on',b.dataset.tab===t)); if(t==='40') paintSeq(); }
 let applied=false, lastSig='';
 setInterval(()=>{ const pad=$('pad'); if(!pad) return; build(); if(!applied&&window.SQITR&&PS()){ applied=true; apply(); tab(getLS('kanin-seqtab','beat')); }
  if(pad.classList.contains('on')){ pickers(); const sig=B()+'|'+itr().length+'|'+(PS().MIX||[]).map(m=>m&&(+m.mute)+''+(+m.solo)).join(''); if(sig!==lastSig){ lastSig=sig; paintSeq(); } } },700);
 /* MIDI channels → tracks: MIDI 1 plays the keyboard (track 18), MIDI 10 plays the 16 pads (notes 36–51), MIDI 2–4 play the instrument tracks 30–32 */
 window.K40.midiTrack=ch=>ch===10?'pads':ch===1?17:ch>=2&&ch<=4?29+(ch-2):17;
 window.K40.presetFor=presetFor; window.K40.tab=tab; window.K40.act=ACT; window.K40.paint=paintSeq;
})();
(()=>{ /* all 16 MIDI channels land on tracks: 1 and 16 the keyboard (track 18), 2–9 tracks 31–38, 10 the pads, 11–14 bass, chords,
   melody and guitar, 15 the cannon and sound bank. Each track plays through its own mixer strip, with its own sound. */
 const prev=window.MIDIHOOK; const CHMAP={2:30,3:31,4:32,5:33,6:34,7:35,8:36,9:37,11:18,12:19,13:20,14:21,15:38}; const TRP={18:'bass',19:'pad',20:'lead',21:'pluck',38:'bell'};
 window.MIDIHOOK=ev=>{ try{ if(prev&&prev(ev)) return true; }catch(_){ }
  try{ const [st,d1,d2]=ev.data; const ch=(st&15)+1; const cmd=st&0xf0; const P=window.PADSTUDIO, K=window.KEYS; if(!P) return false;
   if(ch===10){ if(cmd===0x90&&d2){ const i=((d1-36)%64+64)%64; try{ P.hitPad(i); }catch(_){ } } return true; }
   const ci=CHMAP[ch]; if(ci==null||!K) return false; if(cmd!==0x90||!d2) return true;
   const T=window.SQITR||[]; const i=T.findIndex((t,k)=>K40.slot(k)===ci); const O=[...document.querySelectorAll('#kbPre option')].map(o=>o.value);
   const want=i>=0?T[i].pre:(ci>=30&&ci<=37?K40.presetFor(ci):TRP[ci]); const pre=O.includes(want)?want:(O.find(v=>v.includes(want))||O[0]);
   const c=P.ac(); const o=typeof P.out==='function'?P.out():P.out; K.voice(c,P.SD(c,o,ci),c.currentTime+.005,d1,d2/127,.6,pre); return true; }catch(_){ return false; } };
})();
