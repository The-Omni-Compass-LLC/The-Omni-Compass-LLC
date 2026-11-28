(()=>{ /* 🗂 THE SOUND BROWSER (v242): every sound in KAN-IN, found the way a hardware sampler finds them, one level at a time:
   CATEGORY (drums, bass, pianos and keys, strings and harps, brass, woodwinds, mallets and bells, synths, voices, FX)
   → GROUP or INSTRUMENT (a Studio group, a recorded instrument such as Cello Section or Grand Piano, or a built-in instrument)
   → SOUND, each with ▶ to hear it, → PAD to put it on the selected pad and 🎹 KEYS to play it across the keyboard; a whole group
   or instrument loads onto the 16 pads of the bank on screen in one tap. 13 Studio groups, 7,417 recorded sounds (VCSL and VSCO,
   free to use) and 18 built-in instruments. It lives in 🗂 SOUNDS on the beat machine and on the keyboard. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const PS=()=>window.PADSTUDIO;
 const CATS=[['drums','🥁','Drums & percussion'],['bass','🎸','Bass & 808'],['keys','🎹','Pianos & keys'],['strings','🎻','Strings & harps'],['brass','🎺','Brass'],['winds','🎷','Woodwinds & whistles'],['mallets','🔔','Mallets & bells'],['synth','🎛','Synths & leads'],['voice','🗣','Voices & choir'],['fx','💥','FX, foley & textures']];
 const LIBCAT={'Kicks':'drums','Snares':'drums','Claps and snaps':'drums','Hi-hats closed':'drums','Hi-hats open':'drums','Cymbals and crashes':'drums','Percussion':'drums','World percussion':'drums','808s and bass':'bass','FX':'fx','Foley and textures':'fx','Tones and stabs':'synth','Synth leads and keys':'synth'};
 const INSTCAT={piano:'keys',epiano:'keys',organ:'keys',strings:'strings',harp:'strings',guitar:'strings',brass:'brass',flute:'winds',bells:'mallets',marimba:'mallets',vibes:'mallets',kalimba:'mallets',pad:'synth',lead:'synth',pluck:'synth',chip:'synth',bass:'bass',choir:'voice'};
 function recCat(g,i){ i=String(i||''); if(g==='VSCO Strings') return /contrabass/i.test(i)?'bass':'strings'; if(g==='VSCO Brass'||g==='Lip Aerophones') return 'brass';
  if(g==='VSCO Percussion') return /glock|marimba|xylo/i.test(i)?'mallets':'drums'; if(g==='Struck Idiophones') return /marimba|xylo|vibra|glock|bell|balafon|steel|tubular|celest|chime|gong|crotal|handbell|triangle/i.test(i)?'mallets':'drums';
  if(g==='Struck Membranophones'||g==='Other Membranophones') return 'drums'; if(g==='Plucked Idiophones'||g==='Friction Idiophones') return 'mallets';
  if(g==='Zithers') return /dan tranh|psaltery/i.test(i)?'strings':'keys'; if(g==='Composite Chordophones') return 'strings'; if(g==='TX81Z'||g==='VSCO Keys') return 'keys';
  if(g==='Edge-blown Aerophones') return /organ/i.test(i)?'keys':'winds'; if(g==='Free Aerophones') return /siren/i.test(i)?'fx':'winds'; if(g==='Reed Aerophones'||g==='VSCO Woodwinds') return 'winds'; if(g==='VSCO Miscellania Raw') return 'fx'; return 'fx'; }
 let REC=null; async function rec(){ if(REC) return REC; try{ REC=(await VCSL.load())||[]; }catch(_){ REC=[]; } return REC; }
 const lib=()=>{ try{ return SNDLIB.items||[]; }catch(_){ return []; } };
 const instName=v=>{ const p=$('kbPre'); const o=p&&[...p.options].find(x=>x.value===v); return o?o.text:v; };
 async function sources(cat){ const out=[]; [...new Set(lib().map(x=>x.cat))].filter(c=>LIBCAT[c]===cat).forEach(c=>out.push({t:'lib',key:c,label:'🎛 '+c,n:lib().filter(x=>x.cat===c).length}));
  const R=await rec(); const m=new Map(); R.forEach(x=>{ if(recCat(x.g,x.i)!==cat) return; const k=x.g+'||'+(x.i||''); m.set(k,(m.get(k)||0)+1); }); [...m.entries()].sort((a,b)=>a[0].localeCompare(b[0])).forEach(([k,n])=>{ const [g,i]=k.split('||'); out.push({t:'rec',g,i,label:'🎻 '+(i||g)+' · '+g.replace(/ \(.*\)$/,''),n}); });
  Object.entries(INSTCAT).filter(([,c])=>c===cat).forEach(([v])=>out.push({t:'inst',v,label:'✨ '+instName(v)+' (built-in instrument)',n:0})); return out; }
 async function sounds(src){ if(src.t==='lib') return lib().filter(x=>x.cat===src.key).map(x=>({name:x.name,src:{t:'lib',cat:x.cat,name:x.name},get:()=>SNDLIB.render(x)}));
  if(src.t==='rec'){ const R=await rec(); return R.filter(x=>x.g===src.g&&(x.i||'')===src.i).map(x=>({name:(x.n||'').replace(/^(Main|Close|Mid|Far)\s+/,''),src:{t:'rec',p:x.p,k:x.k},get:()=>VCSL.get(x)})); } return []; }
 /* hear a sound */
 let prev=null; async function hear(get){ try{ const P=PS(); const c=P.ac(); const buf=await get(); if(!buf) return; try{ prev&&prev.stop(); }catch(_){ } const s=c.createBufferSource(); s.buffer=buf; const g=c.createGain(); g.gain.value=.9; s.connect(g); g.connect(c.destination); s.start(); prev=s; }catch(_){ say('That sound did not load. Try another.'); } }
 const bank=()=>{ const b=$('padBank'); return Math.max(0,Math.min(3,+(b&&b.value)||0)); };
 const selPad=()=>{ const T=window.KBROWSE&&KBROWSE.target; if(T!=null&&T>=0) return T; const s=document.querySelector('#padGrid .pd.sel'); return s?+s.dataset.i:bank()*16; };
 async function toPad(it){ const P=PS(); const i=selPad(); const pd=P&&P.pads[i]; if(!pd) return; const old={buf:pd.buf,rbuf:pd.rbuf,snd:pd.snd,name:pd.name,trim:pd.trim,cut:pd.cut}; const buf=await it.get(); if(!buf) return say('That sound did not load. Try another.'); P.setBuf(i,buf,String(it.name).slice(0,18),true); try{ P.refresh(); }catch(_){ } try{ window.KBROWSE.onPad&&KBROWSE.onPad(i,it); }catch(_){ } say('🥁 Pad '+'ABCD'[Math.floor(i/16)]+(i%16+1)+' now plays '+it.name+'.'); try{ KUNDO.push(()=>{ Object.assign(P.pads[i],old); try{ P.refresh(); }catch(_){ } },'the pad sound'); }catch(_){ } }
 async function toKeys(it){ const buf=await it.get(); if(!buf) return say('That sound did not load. Try another.'); try{ KEYS.setSample(buf); }catch(_){ return; } const pre=$('kbPre'); if(pre&&[...pre.options].some(o=>o.value==='sample')){ pre.value='sample'; pre.dispatchEvent(new Event('change',{bubbles:true})); } try{ KSEQ.keysSound({name:it.name,src:it.src,buf}); }catch(_){ } say('🎹 The keys play '+it.name+' across every key'+(window.KSEQ?' (track: '+KSEQ.nameOf(KSEQ.tracks.find(t=>t.id===KSEQ.keysId)||{kind:'keys',sound:{type:'sample',name:it.name}}).replace(/^\S+\s/,'')+')':'')+'.'); }
 async function all16(src,list,page){ const P=PS(); if(!P) return; if(src.t==='lib'){ try{ await KBANK.loadPads('lib:'+src.key,page||0); try{ KSEQ.padLabel(bank(),src.key); }catch(_){ } return; }catch(_){ } }
  const base=bank()*16, pick=list.slice((page||0)*16,(page||0)*16+16); if(!pick.length) return; say('🗂 Loading '+pick.length+' sounds onto bank '+'ABCD'[bank()]+'…'); const olds=[];
  for(let k=0;k<16;k++){ const i=base+k, pd=P.pads[i]; if(!pd) continue; olds.push([i,{buf:pd.buf,rbuf:pd.rbuf,snd:pd.snd,name:pd.name,trim:pd.trim,cut:pd.cut}]); const it=pick[k%pick.length]; let buf=null; try{ buf=await it.get(); }catch(_){ } if(buf) P.setBuf(i,buf,String(it.name).slice(0,18),true); }
  try{ P.refresh(); }catch(_){ } try{ KSEQ.padLabel(bank(),src.i||src.g||src.key); }catch(_){ } say('🗂 Pads '+'ABCD'[bank()]+' plays '+(src.i||src.key)+'.'); try{ KUNDO.push(()=>{ olds.forEach(([i,o])=>Object.assign(P.pads[i],o)); try{ P.refresh(); }catch(_){ } },'the pad bank'); }catch(_){ } }
 /* ---------- the panel ---------- */
 const css=document.createElement('style'); css.textContent=`
.kBrowse{display:flex;flex-direction:column;gap:6px}
.kBrowse .bwPath{display:flex;flex-wrap:wrap;gap:4px;align-items:center;font:800 12px system-ui,sans-serif;color:#9aa3b8}
.kBrowse .bwPath button{min-height:30px!important;padding:0 8px!important;border-radius:8px!important;font:800 12px system-ui,sans-serif!important}
.kBrowse .bwGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:5px;max-height:240px;overflow:auto}
.kBrowse .bwGrid button{min-height:44px!important;border-radius:10px!important;text-align:left;padding:4px 8px!important;font:800 12.5px/1.2 system-ui,sans-serif!important;white-space:normal!important}
.kBrowse .bwGrid button small{display:block;font:600 11px system-ui,sans-serif;color:#9aa3b8}
.kBrowse .bwList{max-height:260px;overflow:auto;display:flex;flex-direction:column;gap:3px}
.kBrowse .bwRow{display:flex;align-items:center;gap:4px;background:#1a1d27;border-radius:8px;padding:3px 4px}
.kBrowse .bwRow span{flex:1;min-width:0;font:700 12px system-ui,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kBrowse .bwRow button{min-height:32px!important;min-width:40px!important;padding:0 7px!important;border-radius:7px!important;font:800 11.5px system-ui,sans-serif!important}
.kBrowse .bwAll{display:flex;flex-wrap:wrap;gap:5px}.kBrowse .bwAll button{flex:1 1 150px;min-height:40px!important;border-radius:10px!important;font:800 12.5px system-ui,sans-serif!important;background:#137a3f!important}
.kBrowse input[type=search]{min-height:36px;border-radius:9px;font:600 13px system-ui,sans-serif;padding:0 9px}`; document.head.appendChild(css);
 const state=new WeakMap();
 function mount(host,dev){ if(!host||host.querySelector(':scope > .kBrowse')) return; const b=document.createElement('div'); b.className='kBrowse'; host.insertBefore(b,host.firstChild); state.set(b,{dev,lvl:0,cat:null,src:null,list:[],page:0,q:''}); render(b);
  b.addEventListener('click',async e=>{ const t=e.target.closest('[data-bw]'); if(!t) return; e.stopPropagation(); const st=state.get(b); const k=t.dataset.bw;
   if(k==='home'){ st.lvl=0; st.cat=null; st.src=null; st.q=''; return render(b); } if(k==='cat'){ st.cat=t.dataset.v; st.lvl=1; st.src=null; return render(b); }
   if(k==='up'){ st.lvl=Math.max(0,st.lvl-1); return render(b); }
   if(k==='src'){ const S=st.srcs[+t.dataset.i]; if(!S) return; if(S.t==='inst'){ if(dev==='keys'){ const pre=$('kbPre'); if(pre){ pre.value=S.v; pre.dispatchEvent(new Event('change',{bubbles:true})); say('🎹 The keys play '+instName(S.v)+'.'); } } else { try{ KPADINST.set({inst:S.v}); }catch(_){ } } return; }
    st.src=S; st.lvl=2; st.page=0; st.list=await sounds(S); return render(b); }
   const it=st.list[+t.dataset.i];
   if(k==='hear'&&it) return hear(it.get); if(k==='pad'&&it) return toPad(it); if(k==='keys'&&it) return toKeys(it);
   if(k==='all') return all16(st.src,st.list,st.page); if(k==='next'){ st.page++; if(st.page*40>=st.list.length) st.page=0; return render(b); } });
  b.addEventListener('input',e=>{ if(e.target.dataset.bw==='q'){ const st=state.get(b); st.q=e.target.value; renderList(b); } }); }
 async function render(b){ const st=state.get(b); const cat=CATS.find(c=>c[0]===st.cat);
  const path='<div class="bwPath"><button type="button" data-bw="home" data-noul>🗂 All sounds</button>'+(cat?' › <button type="button" data-bw="cat" data-v="'+cat[0]+'" data-noul>'+cat[1]+' '+cat[2]+'</button>':'')+(st.lvl===2&&st.src?' › '+esc(st.src.label.replace(/^\S+\s/,'')):'')+'</div>';
  if(st.lvl===0){ b.innerHTML=path+'<div class="bwGrid">'+CATS.map(c=>'<button type="button" data-bw="cat" data-v="'+c[0]+'" data-noul>'+c[1]+' '+c[2]+'</button>').join('')+'</div>'; return; }
  if(st.lvl===1){ b.innerHTML=path+'<div class="bwGrid"><button type="button" disabled>Loading…</button></div>'; st.srcs=await sources(st.cat); b.innerHTML=path+'<div class="bwGrid">'+(st.srcs.map((S,i)=>'<button type="button" data-bw="src" data-i="'+i+'" data-noul>'+esc(S.label)+(S.n?'<small>'+S.n+' sound'+(S.n===1?'':'s')+'</small>':'<small>tap to load</small>')+'</button>').join('')||'<p>Nothing here yet.</p>')+'</div>'; return; }
  b.innerHTML=path+'<div class="bwAll"><button type="button" data-bw="all" data-noul>⬇ Put '+(st.list.length>16?'16 of these':'these')+' on the 16 pads (bank '+'ABCD'[bank()]+')</button>'+(st.list.length>40?'<button type="button" data-bw="next" data-noul style="background:#2a4fa8!important">⏭ Next 40</button>':'')+'</div><input type="search" data-bw="q" placeholder="🔎 Filter these sounds" value="'+esc(st.q)+'"><div class="bwList"></div>'; renderList(b); }
 function renderList(b){ const st=state.get(b); const L=b.querySelector('.bwList'); if(!L) return; const qq=st.q.trim().toLowerCase(); const idx=st.list.map((x,i)=>[x,i]).filter(([x])=>!qq||String(x.name).toLowerCase().includes(qq)); const page=qq?idx.slice(0,80):idx.slice(st.page*40,st.page*40+40);
  L.innerHTML=page.map(([x,i])=>'<div class="bwRow"><button type="button" data-bw="hear" data-i="'+i+'" title="Hear it" data-noul>▶</button><span title="'+esc(x.name)+'">'+esc(x.name)+'</span><button type="button" data-bw="pad" data-i="'+i+'" title="Put it on the selected pad" data-noul>→ Pad</button><button type="button" data-bw="keys" data-i="'+i+'" title="Play it across the keys" data-noul>🎹 Keys</button></div>').join('')||'<p style="color:#9aa3b8">No sound matches.</p>'; }
 setInterval(()=>{ document.querySelectorAll('#mpcBar .kDrawer').forEach(d=>mount(d,'pads')); document.querySelectorAll('#kbDash .kDrawer').forEach(d=>mount(d,'keys')); },800);
 window.KBROWSE={CATS,sources,sounds,mount,target:null,onPad:null};
})();
