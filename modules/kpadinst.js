(()=>{ /* 🎹 ANY INSTRUMENT ON THE 16 PADS (v233). The pad machine's "Pad sounds" list turns the 16 pads of the bank on screen into any of the
   keyboard's 18 instruments (grand piano, electric piano, organ, strings, synth pad, synth lead, synth bass, brass, bells, choir, pluck,
   8-bit, marimba, vibraphone, kalimba, harp, nylon guitar, flute). Each pad gets one note, rendered from the keyboard's own voice and
   loaded onto the pad, so a pad hit, a recorded tap and every sequenced step play it. Notes: the scale of your key (16 steps up from
   the root), all 12 semitones and on, or a chord on each pad. "The bank's own sounds" puts the drums, bass, keys or effects back. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } }; const P=()=>window.PADSTUDIO;
 const INST=[['own','The bank’s own sounds'],['piano','Grand piano'],['epiano','Electric piano'],['organ','Organ'],['strings','Strings'],['pad','Synth pad'],['lead','Synth lead'],['bass','Synth bass'],['brass','Brass'],['bells','Bells'],['choir','Choir'],['pluck','Pluck'],['chip','8-bit'],['marimba','Marimba'],['vibes','Vibraphone'],['kalimba','Kalimba'],['harp','Harp'],['guitar','Nylon guitar'],['flute','Flute']];
 const LAY=[['scale','Notes of my key'],['chrom','Every semitone'],['chord','A chord on each pad'],['penta','Pentatonic'],['blues','Blues scale']];
 const OCT=[['2','Octave 2 (low)'],['3','Octave 3'],['4','Octave 4 (middle)'],['5','Octave 5'],['6','Octave 6 (high)']];
 const NN=['C','C♯','D','D♯','E','F','F♯','G','G♯','A','A♯','B'];
 let inst='own', lay='scale', oct='3', busy=false; const saved={};
 function keyRoot(){ const k=$('cKey'); const v=(k&&(k.value||k.options[k.selectedIndex]&&k.options[k.selectedIndex].text))||'C'; const m=String(v).trim().match(/^([A-G])([#♯b♭]?)/i); if(!m) return 0; let n=['C','D','E','F','G','A','B'].indexOf(m[1].toUpperCase()); n=[0,2,4,5,7,9,11][n]; if(/[#♯]/.test(m[2])) n++; if(/[b♭]/.test(m[2])) n--; return (n+12)%12; }
 function isMinor(){ const md=$('cMode'); const v=String(md&&(md.value+' '+(md.options[md.selectedIndex]||{}).text)||'').toLowerCase(); return /minor|aeolian|dorian|phrygian|locrian/.test(v); }
 function notes(){ const root=12*(+oct+1)+keyRoot(); const sc=isMinor()?[0,2,3,5,7,8,10]:[0,2,4,5,7,9,11]; const pen=isMinor()?[0,3,5,7,10]:[0,2,4,7,9]; const out=[];
  for(let i=0;i<16;i++){ if(lay==='chrom') out.push([root+i]); else if(lay==='blues'){ const bl=[0,3,5,6,7,10]; out.push([root+12*Math.floor(i/6)+bl[i%6]]); }
   else if(lay==='penta') out.push([root+12*Math.floor(i/5)+pen[i%5]]);
   else { const deg=i%7, o=Math.floor(i/7); const n=root+12*o+sc[deg]; if(lay==='chord'){ const n3=root+12*o+sc[(deg+2)%7]+(deg+2>=7?12:0), n5=root+12*o+sc[(deg+4)%7]+(deg+4>=7?12:0); out.push([n,n3,n5]); } else out.push([n]); } }
  return out; }
 const nm=ms=>ms.map(m=>NN[m%12]+(Math.floor(m/12)-1)).join(' ');
 async function render(midis,preset){ const sr=44100, len=preset==='pad'||preset==='strings'||preset==='choir'?2.4:1.8; const oc=new OfflineAudioContext(1,Math.ceil(sr*len),sr); const g=oc.createGain(); g.gain.value=midis.length>1?.55:.9; g.connect(oc.destination);
  midis.forEach(m=>{ try{ KEYS.voice(oc,g,0,m,.9,len*.55,preset); }catch(_){ } }); const buf=await oc.startRendering();
  /* every instrument lands on the pads at the same peak level (0.7), so switching sounds does not jump in volume */
  const d=buf.getChannelData(0); let pk=0; for(let i=0;i<d.length;i++){ const a=Math.abs(d[i]); if(a>pk) pk=a; } if(pk>1e-4){ const k=.7/pk; for(let i=0;i<d.length;i++) d[i]*=k; } return buf; }
 function bank(){ const b=$('padBank'); return Math.max(0,Math.min(3,+(b&&b.value)||0)); }
 async function apply(){ const ps=P(); if(!ps||!window.KEYS) return say('Open 🎛 Studio first.'); if(busy) return; busy=true; const b=bank(), base=b*16;
  try{ if(inst==='own'){ let n=0; for(let i=base;i<base+16;i++){ const s=saved[i]; if(s){ Object.assign(ps.pads[i],s); delete saved[i]; n++; } } try{ ps.refresh(); }catch(_){ } say(n?'🥁 Bank '+'ABCD'[b]+' has its own sounds back.':'🥁 Bank '+'ABCD'[b]+' already has its own sounds.'); return; }
   const label=(INST.find(x=>x[0]===inst)||[,''])[1]; say('🎹 Loading '+label+' onto bank '+'ABCD'[b]+'…'); const ns=notes();
   for(let k=0;k<16;k++){ const i=base+k, pd=ps.pads[i]; if(!pd) continue; if(!saved[i]) saved[i]={buf:pd.buf,rbuf:pd.rbuf,snd:pd.snd,name:pd.name,trim:pd.trim,cut:pd.cut}; const buf=await render(ns[k],inst); ps.setBuf(i,buf,label+' '+nm(ns[k]),true); }
   try{ ps.refresh(); }catch(_){ } try{ KUNDO.push(()=>{ for(let i=base;i<base+16;i++){ const s=saved[i]; if(s){ Object.assign(ps.pads[i],s); delete saved[i]; } } try{ ps.refresh(); }catch(_){ } },'the pad sounds'); }catch(_){ }
   say('🎹 Bank '+'ABCD'[b]+' now plays '+label+': '+nm(ns[0])+' to '+nm(ns[15])+'. Tap a pad or play the loop.'); }
  finally{ busy=false; } }
 const css=document.createElement('style'); css.textContent=`
.kPadInst{display:flex;align-items:center;gap:6px;flex:none}
.kPadInst select{min-height:36px;max-width:170px;border-radius:8px;font:700 12.5px system-ui,sans-serif}
.kPadInst .lbl{font:800 10px system-ui,sans-serif;color:#9aa3b8;letter-spacing:.08em;text-transform:uppercase}`; document.head.appendChild(css);
 function ensure(){ const bar=$('mpcBar'); if(!bar) return; const row=bar.querySelector('.mr2')||bar; if(row.querySelector('.kPadInst')) return; const d=document.createElement('div'); d.className='kPadInst';
  d.innerHTML='<span class="lbl">Pad sounds</span><select data-pi="inst" aria-label="Pad sounds" data-nodice>'+INST.map(([v,t])=>'<option value="'+v+'">'+t+'</option>').join('')+'</select><select data-pi="lay" aria-label="Pad notes" data-nodice>'+LAY.map(([v,t])=>'<option value="'+v+'">'+t+'</option>').join('')+'</select><select data-pi="oct" aria-label="Pad octave" data-nodice>'+OCT.map(([v,t])=>'<option value="'+v+'"'+(v===oct?' selected':'')+'>'+t+'</option>').join('')+'</select>';
  d.addEventListener('change',e=>{ const k=e.target.dataset.pi; if(!k) return; e.stopPropagation(); if(k==='inst') inst=e.target.value; if(k==='lay') lay=e.target.value; if(k==='oct') oct=e.target.value; if(inst!=='own'||k==='inst') apply(); });
  row.appendChild(d); }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')) ensure(); },600);
 window.KPADINST={instruments:INST.map(x=>x[0]),set(o){ if(o.inst) inst=o.inst; if(o.lay) lay=o.lay; if(o.oct) oct=String(o.oct); return apply(); },notes,get state(){ return {inst,lay,oct,bank:bank()}; }};
})();
