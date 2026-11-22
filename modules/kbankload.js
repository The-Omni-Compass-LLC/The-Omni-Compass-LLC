(()=>{ /* 🗃 BANK LOADER (v236): the 16 pads and the keyboard read every sound bank, the way a hardware controller loads a program.
   Pads: "Load bank" puts 16 sounds from any group onto the 16 pads of the bank on screen: the Studio library's groups (kicks, snares,
   claps, hats, cymbals, percussion, 808s, FX, tones, world percussion, foley, synth leads) and the recorded instrument library's
   groups; "Next 16" steps through a big group, "The bank's own sounds" puts the factory sounds back, and ↶ Undo works too.
   Keys: "Keys play" puts any one of those sounds on the keyboard, pitched across the keys like a sampler (the keyboard's own sample
   voice). Touch, the computer keys and a MIDI controller all play whatever is loaded, live, recorded and in the WAV. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } }; const P=()=>window.PADSTUDIO;
 let page=0, cur='', busy=false, pending=null; const saved={};
 const libItems=()=>{ try{ return (window.SNDLIB&&SNDLIB.items)||[]; }catch(_){ return []; } };
 const libCats=()=>{ try{ return SNDLIB.cats(); }catch(_){ return []; } };
 let recIdx=null; async function recList(){ if(recIdx) return recIdx; try{ const L=await VCSL.load(); recIdx=(L||[]); }catch(_){ recIdx=[]; } return recIdx; }
 const recGroups=L=>[...new Set(L.map(x=>x.g||x.i||'Recorded'))];
 async function groups(){ const out=libCats().map(c=>['lib:'+c,'🎛 '+c]); const R=await recList(); recGroups(R).forEach(g=>out.push(['rec:'+g,'🎻 '+g+' (recorded)'])); return out; }
 async function itemsOf(key){ if(key.startsWith('lib:')){ const c=key.slice(4); return libItems().filter(x=>x.cat===c).map(x=>({name:x.name,get:()=>SNDLIB.render(x)})); }
  if(key.startsWith('rec:')){ const g=key.slice(4); const R=await recList(); return R.filter(x=>(x.g||x.i||'Recorded')===g).map(x=>({name:(VCSL.label?VCSL.label(x):x.n)||x.n,get:()=>VCSL.get(x)})); } return []; }
 const bank=()=>{ const b=$('padBank'); return Math.max(0,Math.min(3,+(b&&b.value)||0)); };
 function restore(base){ const ps=P(); let n=0; for(let i=base;i<base+16;i++){ const s=saved[i]; if(s){ Object.assign(ps.pads[i],s); delete saved[i]; n++; } } try{ ps.refresh(); }catch(_){ } return n; }
 async function loadPads(key,pg){ const ps=P(); if(!ps) return say('Open 🎛 Studio first.'); if(busy){ pending=[key,pg]; return; } busy=true; const b=bank(), base=b*16;
  try{ if(key==='own'){ const n=restore(base); say(n?'🥁 Bank '+'ABCD'[b]+' has its own sounds back.':'🥁 Bank '+'ABCD'[b]+' already has its own sounds.'); return; }
   const all=await itemsOf(key); if(!all.length) return say('That bank has no sounds yet.'); const pages=Math.ceil(all.length/16); pg=((pg%pages)+pages)%pages; page=pg; cur=key;
   const pick=all.slice(pg*16,pg*16+16); say('🗃 Loading '+pick.length+' sounds onto bank '+'ABCD'[b]+'…');
   for(let k=0;k<16;k++){ const i=base+k, pd=ps.pads[i]; if(!pd) continue; const it=pick[k%pick.length]; if(!saved[i]) saved[i]={buf:pd.buf,rbuf:pd.rbuf,snd:pd.snd,name:pd.name,trim:pd.trim,cut:pd.cut};
    let buf=null; try{ buf=await it.get(); }catch(_){ } if(buf) ps.setBuf(i,buf,String(it.name).slice(0,18),true); }
   try{ ps.refresh(); }catch(_){ } try{ KUNDO.push(()=>restore(base),'the pad bank'); }catch(_){ }
   say('🗃 Bank '+'ABCD'[b]+' loaded'+(pages>1?' (sounds '+(pg*16+1)+' to '+Math.min(all.length,pg*16+16)+' of '+all.length+')':'')+'. Tap the pads or play them from a MIDI controller.'); paint(); }
  finally{ busy=false; if(pending){ const q=pending; pending=null; loadPads(q[0],q[1]); } } }
 async function loadKeys(key,idx){ if(!window.KEYS||!KEYS.setSample) return say('Open the 🎹 keyboard first.'); const all=await itemsOf(key); const it=all[idx]; if(!it) return; let buf=null; try{ buf=await it.get(); }catch(_){ } if(!buf) return say('That sound did not load. Try another.');
  KEYS.setSample(buf); const pre=$('kbPre'); if(pre&&[...pre.options].some(o=>o.value==='sample')){ pre.value='sample'; pre.dispatchEvent(new Event('change',{bubbles:true})); } say('🎹 The keyboard plays “'+it.name+'” across every key. Pick another sound in the list to switch back.'); }
 const css=document.createElement('style'); css.textContent=`
.kBank{display:flex;align-items:center;gap:6px;flex:none}.kBank select{min-height:36px;max-width:200px;border-radius:8px;font:700 12.5px system-ui,sans-serif}
.kBank button{min-height:36px;border-radius:8px;font:800 12px system-ui,sans-serif;padding:0 8px}.kBank .lbl{font:800 10px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.08em;text-transform:uppercase}`; document.head.appendChild(css);
 async function fill(sel,withOwn){ const G=await groups(); sel.innerHTML=(withOwn?'<option value="own">The bank’s own sounds</option>':'<option value="">Choose a bank…</option>')+G.map(([v,t])=>'<option value="'+v.replace(/"/g,'&quot;')+'">'+t+'</option>').join(''); }
 function paint(){ document.querySelectorAll('.kBank [data-bk="next"]').forEach(b=>{ b.disabled=!cur; }); }
 async function ensure(){ const bar=$('mpcBar'); if(bar){ const row=bar.querySelector('.mr2')||bar; if(!row.querySelector('.kBank')){ const d=document.createElement('div'); d.className='kBank';
    d.innerHTML='<span class="lbl">Load bank</span><select data-bk="bank" aria-label="Load a sound bank onto the pads" data-nodice><option value="own">The bank’s own sounds</option></select><button type="button" data-bk="next" data-noul>⏭ Next 16</button>';
    row.appendChild(d); fill(d.querySelector('select'),true);
    d.addEventListener('change',e=>{ if(e.target.dataset.bk!=='bank') return; e.stopPropagation(); page=0; loadPads(e.target.value,0); });
    d.addEventListener('click',e=>{ if(e.target.closest('[data-bk="next"]')){ e.stopPropagation(); if(cur) loadPads(cur,page+1); } }); paint(); } }
  const kd=$('kbDash'); if(kd){ const row=kd.querySelector('.mr2')||kd; if(!row.querySelector('.kBank')){ const d=document.createElement('div'); d.className='kBank';
    d.innerHTML='<span class="lbl">Keys play</span><select data-bk="kgroup" aria-label="Sound bank for the keys" data-nodice><option value="">Choose a bank…</option></select><select data-bk="ksound" aria-label="Sound for the keys" data-nodice><option value="">Then a sound…</option></select>';
    row.appendChild(d); fill(d.querySelector('[data-bk="kgroup"]'),false);
    d.addEventListener('change',async e=>{ const k=e.target.dataset.bk; if(!k) return; e.stopPropagation(); if(k==='kgroup'){ const all=await itemsOf(e.target.value); const s=d.querySelector('[data-bk="ksound"]'); s.innerHTML='<option value="">Then a sound…</option>'+all.map((x,i)=>'<option value="'+i+'">'+String(x.name).replace(/</g,'&lt;')+'</option>').join(''); }
     if(k==='ksound'&&e.target.value!==''){ const g=d.querySelector('[data-bk="kgroup"]').value; loadKeys(g,+e.target.value); } }); } } }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')) ensure(); },700);
 window.KBANK={groups,loadPads,loadKeys,itemsOf,get state(){ return {cur,page,bank:bank()}; }};
})();
