(()=>{ /* ⌨ KEYBOARDS AND CONTROLLERS (v210): one panel that shows how every keyboard is wired to the engine, drawn as diagrams.
   Three ways to play, all live at once: your computer keyboard (pads or a two-octave piano), a MIDI keyboard or pad controller on USB,
   and the on-screen pads and piano by touch or mouse. A catalog sorts every keyboard and control panel by category, and every
   shortcut by what it does. Desktop and laptop get the full professional layout; a phone gets a simpler one sized for one hand. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const PADK='1234qwerasdfzxcv', PIANO='zsxdcvgbhnjmq2w3er5t6y7ui', NN=['C','C♯','D','D♯','E','F','F♯','G','G♯','A','A♯','B'];
 const ROWS=[['`','1','2','3','4','5','6','7','8','9','0','-','='],['q','w','e','r','t','y','u','i','o','p','[',']'],['a','s','d','f','g','h','j','k','l',';',"'"],['z','x','c','v','b','n','m',',','.','/']];
 const OFF=[0,.5,.75,1.25];
 const COL={pad:'#ff7ad9',white:'#f4f1e8',black:'#2a2440',tr:'#2fd27a',rec:'#ff5a5a',nav:'#6fb8ff',pitch:'#ffb347',none:'#3a3560'};
 let mode='pads';
 const css=document.createElement('style'); css.textContent=`
#kKbd{position:fixed;inset:0;z-index:9770;background:#08061a;color:#fff;overflow:auto;padding:calc(10px + env(safe-area-inset-top,0px)) calc(var(--kRailW,58px) + 12px) 40px max(12px,env(safe-area-inset-left,0px));box-sizing:border-box}
#kKbd[hidden]{display:none!important}
#kKbd .kbIn{max-width:1500px;margin:0 auto}
#kKbd h2{margin:4px 0 6px;font:900 clamp(20px,2vw,40px)/1.15 system-ui,sans-serif;color:#ffe94a;text-wrap:balance}
#kKbd h3{margin:16px 0 6px;font:800 clamp(16px,1.3vw,28px)/1.2 system-ui,sans-serif;color:#9ff}
#kKbd p,#kKbd li{font:500 clamp(14px,1.05vw,21px)/1.5 system-ui,sans-serif;color:#ddd8ff;max-width:75ch}
#kKbd .kbX{position:sticky;top:0;float:right;min-height:48px;padding:4px 16px!important;border-radius:999px!important;background:#b3172f!important;color:#fff!important;font:900 clamp(15px,1.1vw,22px) system-ui,sans-serif!important;border:2px solid #fff!important;z-index:2}
#kKbd .kbNote{border-left:4px solid #ffe94a;padding:6px 10px;background:rgba(255,233,74,.08);border-radius:8px}
#kKbd .kbWays{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:10px}
#kKbd .kbWay{border:1px solid rgba(255,255,255,.18);border-radius:14px;padding:10px;background:rgba(255,255,255,.04);min-width:0}
#kKbd .kbWay b{display:block;font:800 clamp(16px,1.2vw,24px) system-ui,sans-serif;color:#fff;margin-bottom:4px}
#kKbd button.kb{min-height:48px;min-width:48px;margin:4px 6px 0 0;padding:6px 14px!important;border-radius:12px!important;font:800 clamp(14px,1vw,20px)/1.2 system-ui,sans-serif!important;white-space:normal}
#kKbd button.kb.on{background:#ffe94a!important;color:#14163a!important}
#kKbd .kbSvg{width:100%;max-width:1100px;height:auto;display:block;margin:8px 0}
#kKbd .kbCat{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:10px}
#kKbd .kbCat section{border:1px solid rgba(127,255,255,.25);border-radius:12px;padding:8px 12px;min-width:0}
#kKbd .kbCat h4{margin:2px 0 4px;font:800 clamp(15px,1.1vw,22px) system-ui,sans-serif;color:#ffe94a}
#kKbd .kbCat ul{margin:0;padding-left:18px}
#kKbd table{border-collapse:collapse;width:100%;max-width:900px}
#kKbd td,#kKbd th{border-bottom:1px solid rgba(255,255,255,.12);padding:6px 8px;text-align:left;font:500 clamp(13px,1vw,19px)/1.4 system-ui,sans-serif;color:#e8e4ff;vertical-align:top}
#kKbd th{color:#9ff;font-weight:800}
#kKbd .kbTbl{overflow-x:auto}
#kKbd kbd{display:inline-block;min-width:1.6em;padding:1px 6px;border-radius:6px;border:1px solid #8a83c0;background:#221d44;font:700 .92em ui-monospace,monospace;color:#fff;text-align:center}
#kKbd .kbPhone{display:none}
@media (max-width:700px){ #kKbd .kbDesk{display:none} #kKbd .kbPhone{display:block} }`; document.head.appendChild(css);
 const MAPROWS=()=>{ try{ return window.KEYMAP.MAP.map(r=>({keys:r[4],what:r[5],cat:r[6]})); }catch(_){ return []; } };
 const SECTS=()=>{ try{ return window.KEYMAP.SECTIONS.map(s=>({key:s[0].replace('Key',''),what:s[1]})); }catch(_){ return []; } };
 /* the drawn computer keyboard: each key coloured and labelled by what it does in the chosen mode */
 function qwerty(m){ const U=46, G=5, W=13*(U+G)+80; let h='<svg class="kbSvg" viewBox="0 0 '+W+' 300" role="img" aria-label="Diagram of a computer keyboard in '+m+' mode">';
  const shiftKeys={}; MAPROWS().forEach(r=>{ const mm=/^Shift ([A-Z0-9])$/.exec(r.keys); if(mm) shiftKeys[mm[1].toLowerCase()]=r; });
  ROWS.forEach((row,ri)=>row.forEach((k,ci)=>{ const x=10+(OFF[ri]+ci)*(U+G), y=10+ri*(U+G); let fill=COL.none, lab='', tc='#fff';
   if(m==='pads'){ const i=PADK.indexOf(k); if(i>=0){ fill=COL.pad; lab='A'+(i+1); tc='#14163a'; } }
   else if(m==='piano'){ const i=PIANO.indexOf(k); if(i>=0){ const n=NN[i%12]; const oct=3+Math.floor(i/12); const blk=n.includes('♯'); fill=blk?COL.black:COL.white; tc=blk?'#fff':'#14163a'; lab=n+oct; } }
   else { const r=shiftKeys[k]; if(r){ fill=COL[r.cat]||COL.nav; tc='#14163a'; lab='⇧'+k.toUpperCase(); } if(k==='['||k===']'){ fill=COL.pitch; tc='#14163a'; lab=k==='['?'−1':'+1'; } }
   h+='<g><rect x="'+x+'" y="'+y+'" width="'+U+'" height="'+U+'" rx="8" fill="'+fill+'" stroke="#8a83c0" stroke-width="1.5"/><text x="'+(x+6)+'" y="'+(y+16)+'" font-size="13" font-weight="800" fill="'+tc+'" font-family="system-ui,sans-serif">'+esc(k.toUpperCase())+'</text>'+(lab?'<text x="'+(x+U/2)+'" y="'+(y+U-9)+'" font-size="12" text-anchor="middle" font-weight="700" fill="'+tc+'" font-family="system-ui,sans-serif">'+esc(lab)+'</text>':'')+'</g>'; }));
  const sy=10+4*(U+G); const sx=10+3*(U+G); const sw=6*(U+G)-G; h+='<rect x="'+sx+'" y="'+sy+'" width="'+sw+'" height="'+U+'" rx="8" fill="'+COL.tr+'" stroke="#8a83c0" stroke-width="1.5"/><text x="'+(sx+sw/2)+'" y="'+(sy+28)+'" font-size="15" text-anchor="middle" font-weight="800" fill="#14163a" font-family="system-ui,sans-serif">SPACE · ▶ Play / ■ Stop</text>';
  const ax=10+10*(U+G); [['←',0,1],['↓',1,1],['→',2,1],['↑',1,0]].forEach(([t,dx,dy])=>{ const x=ax+dx*(U*0.8+G), y=sy-(1-dy)*(U*0.8+G)+(dy?0:0)+ (dy?0:0); h+='<rect x="'+x+'" y="'+(dy?sy:sy-U*0.8-G)+'" width="'+(U*0.8)+'" height="'+(U*0.8)+'" rx="7" fill="'+COL.nav+'" stroke="#8a83c0"/><text x="'+(x+U*0.4)+'" y="'+((dy?sy:sy-U*0.8-G)+U*0.55)+'" font-size="16" text-anchor="middle" font-weight="900" fill="#14163a">'+t+'</text>'; });
  h+='<rect x="10" y="'+sy+'" width="'+(U*1.6)+'" height="'+U+'" rx="8" fill="'+COL.rec+'" stroke="#8a83c0"/><text x="'+(10+U*0.8)+'" y="'+(sy+28)+'" font-size="14" text-anchor="middle" font-weight="800" fill="#14163a">ESC ■</text>';
  return h+'</svg>'; }
 /* the drawn MIDI keyboard (two octaves) and the 4 × 4 pad controller with its note numbers */
 function midiKeys(){ const W=15*44+20; let h='<svg class="kbSvg" viewBox="0 0 '+W+' 190" role="img" aria-label="Diagram of a two-octave MIDI keyboard, notes 48 to 72">'; const whites=[]; for(let n=48;n<=72;n++) if(!NN[n%12].includes('♯')) whites.push(n);
  whites.forEach((n,i)=>{ const x=10+i*44; h+='<rect x="'+x+'" y="10" width="42" height="160" rx="5" fill="#f4f1e8" stroke="#555"/><text x="'+(x+21)+'" y="150" font-size="12" text-anchor="middle" font-weight="800" fill="#14163a">'+NN[n%12]+(Math.floor(n/12)-1)+'</text><text x="'+(x+21)+'" y="164" font-size="10" text-anchor="middle" fill="#555">'+n+'</text>'; });
  whites.forEach((n,i)=>{ if(n%12===4||n%12===11||n===72) return; const x=10+i*44+29; h+='<rect x="'+x+'" y="10" width="28" height="98" rx="4" fill="#2a2440" stroke="#000"/><text x="'+(x+14)+'" y="98" font-size="9" text-anchor="middle" fill="#fff">'+(n+1)+'</text>'; });
  return h+'</svg>'; }
 function midiPads(){ let h='<svg class="kbSvg" viewBox="0 0 380 380" style="max-width:380px" role="img" aria-label="Diagram of a 4 by 4 pad controller: notes 36 to 51 play pads A1 to A16">';
  for(let r=0;r<4;r++) for(let c=0;c<4;c++){ const i=r*4+c; const x=10+c*92, y=10+r*92; h+='<rect x="'+x+'" y="'+y+'" width="84" height="84" rx="12" fill="#3a1450" stroke="#ff7ad9" stroke-width="2"/><text x="'+(x+42)+'" y="'+(y+40)+'" font-size="20" text-anchor="middle" font-weight="900" fill="#ff9ae6">A'+(i+1)+'</text><text x="'+(x+42)+'" y="'+(y+64)+'" font-size="14" text-anchor="middle" fill="#fff">note '+(36+i)+'</text>'; }
  return h+'</svg>'; }
 const CH=[['1','🎹 Keyboard','track 18'],['2–9','🎹 MIDI 2–9: strings, brass, bells, organ, pluck, lead synth, pad, synth bass','tracks 31–38'],['10','🥁 The pads: note 36 = A1 … note 51 = A16 (B–D above)','tracks 1–17'],['11','🎸 Bass line','track 19'],['12','🎹 Chords','track 20'],['13','🎼 Melody','track 21'],['14','🎸 Rhythm guitar','track 22'],['15','💥 Cannon · sound bank','track 39'],['16','🎹 Keyboard','track 18']];
 const CAT=[
  ['🥁 Pad keypads',['16 pads in a 4 × 4 grid, one per track (1–16)','64 pads in banks A–D (Shift 1–4 switches banks)','MPC note map: notes 36–51 play A1–A16','Computer keys 1 2 3 4 · Q W E R · A S D F · Z X C V']],
  ['🎹 Piano keyboards',['On-screen piano, two octaves, touch or mouse','Computer keys: Z to M is the lower octave, Q to I the upper one, the row above the black keys','MIDI keyboards of 25, 49, 61 or 88 keys on USB','Octave and transpose: [ and ] (Shift for a whole octave)']],
  ['🎛 Control panels',['The 40-track mixer: a fader, pan, mute, solo and input picker on every strip','The remote: rewind, play, stop, record, undo, loop, save, new, open, close','The transport bar: play, stop, record, pattern, tempo','The Easy panel: giant buttons for first-timers']],
  ['⌨ Shortcut layers',['Transport: Space, Esc, ↑ ↓ tempo, Shift C click, Shift T tap tempo','Record: Shift R pads, Shift K keys, Shift V vocals, Shift M mic, Shift P to a file','Edit: Ctrl/⌘ Z undo, C copy, X cut, V paste, D duplicate, Delete','Build: Shift A auto-create, Shift B build the song, Shift F fire the cannon, Shift G new groove']],
  ['🔌 Ways to wire it',['Plug in: a USB MIDI keyboard or pad controller, then 🔌 Connect','Upload: your own sounds onto any pad or onto the keys','Ours: the on-screen pads and piano, nothing to plug in','Phone: touch only, simpler layout; desktop: everything at once']]];
 function build(){ let d=$('kKbd'); if(d) return d; d=document.createElement('div'); d.id='kKbd'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Keyboards and controllers'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); const a=b.dataset.kb; if(!a) return;
   if(a==='x') return close(); if(a.startsWith('m:')){ mode=a.slice(2); paint(); return; }
   if(a==='midi'){ close(); go(()=>{ const m=$('midiOn'); if(m){ m.scrollIntoView({block:'center'}); m.click(); } }); return; }
   if(a==='pads'||a==='keys'){ close(); go(()=>{ try{ KRAIL.FLOAT.open(a); }catch(_){ } const km=$('kbKeyMode'); if(km&&a==='keys'){ km.value='keys'; km.dispatchEvent(new Event('change',{bubbles:true})); } if(km&&a==='pads'){ km.value='pads'; km.dispatchEvent(new Event('change',{bubbles:true})); } say(a==='keys'?'🎹 The piano is out. Play it with your fingers, the mouse, or the keys Z to M and Q to I.':'🥁 The pads are out. Tap them, or press 1 2 3 4 · Q W E R · A S D F · Z X C V.'); }); return; }
   if(a==='up'){ close(); go(()=>{ const f=$('padFile')||$('padUp'); if(f) f.click(); else say('Open the pads and pick a pad, then load your sound.'); }); return; }
   if(a==='upk'){ close(); go(()=>{ const f=$('kbSampleBtn'); if(f) f.click(); }); return; }
   if(a==='all'){ close(); try{ $('kmOpen').click(); }catch(_){ } return; } });
  return d; }
 const go=fn=>{ try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(fn,900); };
 function paint(){ const d=build(); const ways='<div class="kbWays">'
   +'<div class="kbWay"><b>⌨ Your computer keyboard</b><p>Built in. In pads mode the keys play the 16 pads; in piano mode they play two octaves. Shift and a letter runs a shortcut.</p><button type="button" class="kb" data-kb="pads">🥁 Play the pads</button><button type="button" class="kb" data-kb="keys">🎹 Play the piano</button></div>'
   +'<div class="kbWay"><b>🎹 A MIDI keyboard or pad controller</b><p>Plug it in by USB, then connect. Every one of the 16 MIDI channels lands on its own track (the table below). Works in Chrome and Edge, and in the downloaded app.</p><button type="button" class="kb" data-kb="midi">🔌 Connect MIDI</button></div>'
   +'<div class="kbWay"><b>👆 Ours, on the screen</b><p>The pads and the piano float over the sequencer. Tap them with your fingers or click them. Nothing to plug in.</p><button type="button" class="kb" data-kb="pads">🥁 Floating pads</button><button type="button" class="kb" data-kb="keys">🎹 Floating piano</button></div>'
   +'<div class="kbWay"><b>📤 Upload your own sounds</b><p>Put your own recording on any pad, or a sample on the keys so the whole piano plays it in tune.</p><button type="button" class="kb" data-kb="up">📤 A sound on a pad</button><button type="button" class="kb" data-kb="upk">📤 A sample on the keys</button></div></div>';
  const modes=[['pads','🥁 Pads mode'],['piano','🎹 Piano mode'],['short','⌨ Shortcuts']].map(([k,l])=>'<button type="button" class="kb'+(mode===k?' on':'')+'" data-kb="m:'+k+'">'+l+'</button>').join('');
  const legend={pads:'Pink keys play pads A1–A16, one per track. The layout matches the 4 × 4 pads on the screen: the top row 1 2 3 4 is A1–A4.',piano:'White and black keys play two octaves from C3. Z to M is the lower octave with S D G H J as its black keys; Q to I is the upper octave with 2 3 5 6 7 as its black keys.',short:'Green keys run the transport, red ones record, blue ones move around, orange ones change pitch. Hold Shift with a coloured letter.'}[mode];
  const mapRows=MAPROWS(); const cats={tr:'Transport',rec:'Record',nav:'Move around',pitch:'Pitch'};
  const short='<div class="kbTbl"><table><tr><th>Key</th><th>What it does</th><th>Kind</th></tr>'+mapRows.map(r=>'<tr><td><kbd>'+esc(r.keys)+'</kbd></td><td>'+esc(r.what)+'</td><td>'+esc(cats[r.cat]||r.cat)+'</td></tr>').join('')+'<tr><td><kbd>Ctrl/⌘ Z</kbd></td><td>Undo the last move</td><td>Edit</td></tr><tr><td><kbd>Ctrl/⌘ C · X · V · D</kbd></td><td>Copy, cut, paste, duplicate steps in the sequencer</td><td>Edit</td></tr></table></div>';
  const chans='<div class="kbTbl"><table><tr><th>MIDI channel</th><th>Plays</th><th>Lands on</th></tr>'+CH.map(c=>'<tr><td><kbd>'+c[0]+'</kbd></td><td>'+c[1]+'</td><td>'+c[2]+'</td></tr>').join('')+'</table></div>';
  d.innerHTML='<div class="kbIn"><button type="button" class="kbX" data-kb="x" aria-label="Close">✕ Close</button><h2>⌨ Keyboards and controllers</h2>'
   +'<p class="kbNote"><b>Desktop and laptop:</b> the full professional layout, with your keyboard, a MIDI controller and the finger-sized on-screen pads and piano all live at once. <b>Phone:</b> a simpler layout sized for one hand: touch only, bigger pads, a shorter piano. The desktop layout is the professional one.</p>'
   +'<h3>Three ways to play, all at once</h3>'+ways
   +'<h3>How your computer keyboard is wired</h3><div>'+modes+'</div><p>'+legend+'</p>'+qwerty(mode)
   +'<div class="kbDesk"><h3>How a MIDI keyboard is wired</h3><p>Middle C is note 60. The piano below runs from note 48 (C3) to 72 (C5). Pad controllers send notes 36 to 51 for the 16 pads.</p>'+midiKeys()+midiPads()+'<h3>All 16 MIDI channels, each on its own track</h3>'+chans+'</div>'
   +'<div class="kbPhone"><h3>On a phone</h3><p>Tap the pads and the piano on the screen. A USB keyboard works on phones that allow MIDI. Open this on a desktop or laptop to see the MIDI diagrams and all 16 channels.</p></div>'
   +'<h3>The catalog: every keyboard and control panel by category</h3><div class="kbCat">'+CAT.map(([t,L])=>'<section><h4>'+t+'</h4><ul>'+L.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul></section>').join('')+'</div>'
   +'<h3>Every shortcut</h3>'+short+'<button type="button" class="kb" data-kb="all">⌨ The full key map, layer by layer</button></div>'; }
 function open(m){ if(m) mode=m; paint(); const d=build(); d.hidden=false; d.scrollTop=0; }
 function close(){ const d=$('kKbd'); if(d) d.hidden=true; }
 document.addEventListener('keydown',e=>{ const d=$('kKbd'); if(e.key==='Escape'&&d&&!d.hidden){ e.stopPropagation(); close(); } },true);
 /* the way in: a button beside the sequencer tabs, the Menu, and the ⌨ key map corner */
 setInterval(()=>{ const t=$('kSeqTabs'); if(t&&!t.querySelector('[data-kbo]')){ const b=document.createElement('button'); b.type='button'; b.dataset.kbo='1'; b.setAttribute('data-noul',''); b.textContent='⌨ Keyboards and controllers'; b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); t.appendChild(b); }
  const tt=$('tourTab'); if(tt&&!$('ttKbd')){ const b=document.createElement('button'); b.type='button'; b.id='ttKbd'; b.className='ttMusic kStartB'; b.textContent='⌨ Keyboards and controllers'; b.setAttribute('data-noul',''); b.style.order='70'; b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>open(),120); }); tt.appendChild(b); }
  const im=$('inMode'); if(im&&!im.querySelector('[data-kbo]')){ const b=document.createElement('button'); b.type='button'; b.dataset.kbo='1'; b.textContent='🎹 All keyboards'; b.addEventListener('click',e=>{ e.stopPropagation(); open(); }); im.appendChild(b); } },1000);
 window.KKBD={open,close};
})();
