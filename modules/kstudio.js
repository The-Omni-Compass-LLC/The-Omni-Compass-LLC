(()=>{ /* THE STUDIO, TIED TOGETHER:
   · the rail gets 🎛 Studio and 🌐 Social, and its ■ Stop becomes one ▶ Play / ■ Stop button that knows what this screen plays;
   · the mixer becomes one 24-channel console you see whole (all 24 strips + master on one board, banks to focus), with the two DJ decks
     wired in as channels 25 and 26, and a 🎙 Record a track button into the recording booth;
   · the Menu lists the most-used things first: Social, games, video, music, karaoke, humor, then the rest. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const cur=()=>{ try{ return KRAIL.cur(); }catch(_){ return 'home'; } };
 /* ---------- what is playing right now ---------- */
 function playing(){ try{ const P=window.PADSTUDIO; if(P&&(typeof P.playing==='function'?P.playing():P.playing)) return 'the beat'; }catch(_){ }
  try{ const D=DJBOOTH.D; if(D.A.playing||D.B.playing) return 'the DJ decks'; }catch(_){ }
  try{ if(speechSynthesis.speaking) return 'a voice'; }catch(_){ }
  for(const m of document.querySelectorAll('audio,video')){ if(m.id==='mAudio'&&window.KMINI&&KMINI.bgOn&&(!window.KRAIL||KRAIL.cur()!=='musicDock')) continue; if(!m.paused&&!m.ended&&m.currentTime>0&&!m.muted&&m.volume>0) return m.tagName==='VIDEO'?'a video':'a song'; }
  return ''; }
 const press=sel=>{ const b=typeof sel==='string'?document.querySelector(sel):sel; if(b){ b.click(); return true; } return false; };
 /* what ▶ Play means on each screen */
 const PLAY={pad:()=>press('#bbPlay')||(PADSTUDIO.play(),true),kKara:()=>press('#kKara [data-kk="play"]'),musicDock:()=>press('#mPP'),voiceDock:()=>press('#vcRead'),langDock:()=>press('#lRead'),zodDock:()=>press('#zodSay'),omniDock:()=>press('#otPlay'),aivDock:()=>press('#aivPlay'),sbDock:()=>press('#sbpPlay'),sbp:()=>press('#sbpPlay'),mutDock:()=>press('#mutAPlay'),swDock:()=>press('#swBeat'),kHumor:()=>press('#kHumor [data-kh="daysay"]'),kOwner:()=>press('#kOwner [data-ko="say"]'),
  gamesDock:()=>{ const all=[...document.querySelectorAll('#gamesDock button')].filter(x=>x.getClientRects().length&&!x.disabled); const b=all.find(x=>x.closest('.gbar')&&/Start|Play|Resume|again/.test(x.textContent))||all.find(x=>/^▶/.test(x.textContent.trim())&&!/^▶▶/.test(x.textContent.trim())); return b?press(b):false; }};
 const WHAT={pad:'your beat',kKara:'the karaoke track',musicDock:'the music',voiceDock:'the voices',langDock:'the reading',zodDock:'your reading',omniDock:'the compass',aivDock:'the video',sbDock:'the storybook',sbp:'the storybook',mutDock:'the song',swDock:'the song’s beat',kHumor:'the joke of the day',kOwner:'the owner’s word',gamesDock:'the game'};
 function doPlay(){ const id=cur(); const f=PLAY[id]; let ok=false; try{ ok=f?f():false; }catch(_){ }
  if(!ok){ try{ PADSTUDIO.play(); ok=true; say('▶ Playing your beat. Open 🎛 Studio to change it.'); }catch(_){ say('Open a screen with something to play, like 🎛 Studio or 🎤 Karaoke.'); } }
  else say('▶ Playing '+(WHAT[id]||'')+'.'); setTimeout(paintPS,300); }
 /* ---------- the rail ---------- */
 const css=document.createElement('style'); css.textContent=`
html body #rDock#rDock #kdStudio{order:1!important;display:flex!important}
html body #rDock#rDock #kdSocial{order:1!important;display:flex!important}
html body #rDock#rDock #kdProfile{order:1!important;display:flex!important}
html body #rDock#rDock #kdProj{display:flex!important}
html body #rDock#rDock #kStopBtn.kPlay{background:linear-gradient(180deg,#1f9d55,#137a3f)!important;border-color:#7cff8a!important}
html body #rDock#rDock #kStopBtn.kStop{background:linear-gradient(180deg,#d42a44,#9c1028)!important}
@media (max-height:980px){html body #rDock#rDock>button{min-height:0!important;flex:1 1 0!important;max-height:70px!important;padding-top:0!important;padding-bottom:0!important}html body #rDock#rDock>button::before{font-size:min(22px,3.1vh)!important;line-height:1.1!important}html body #rDock#rDock>button::after{font-size:min(11.5px,1.75vh)!important;line-height:1.1!important}html body #rDock#rDock #lpMenu{min-height:0!important;flex:1.2 1 0!important}html body #rDock#rDock{gap:3px!important}}
html body .mast .ddlogo.ddlogo{width:min(500px,100%)!important}
@media (max-width:760px){html body .mast .ddlogo.ddlogo{width:min(calc(100vw - 150px),375px)!important}}
#kStudioHead{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:6px 0 4px}
#kStudioHead b{font:900 16px system-ui,sans-serif;color:#ffe94a;margin-right:6px}
#kStudioHead button{min-height:36px;border-radius:10px;padding:0 10px;font:700 13px system-ui,sans-serif}
#kStudioHead button.on{background:#ffe94a!important;color:#14163a!important}
html body #padMixer#padMixer{display:grid!important;grid-template-columns:repeat(auto-fill,minmax(38px,1fr))!important;overflow:visible!important;scroll-snap-type:none!important;gap:3px!important;padding:8px!important}
html body #padMixer#padMixer .mxs{flex:none!important;min-width:0!important;padding:4px 1px!important;gap:3px!important}
html body #padMixer#padMixer .mxs[hidden]{display:none!important}
html body #padMixer#padMixer .mxm{height:56px!important;width:7px!important}
html body #padMixer#padMixer .mxv{height:92px!important;width:20px!important}
html body #padMixer#padMixer .knb{width:24px!important;height:24px!important}
html body #padMixer#padMixer .knb:after{height:8px!important;top:2px!important;transform-origin:50% 10px!important}
html body #padMixer#padMixer .mxb{flex-direction:column!important;gap:2px!important}
html body #padMixer#padMixer .mxb button{min-width:28px!important;min-height:22px!important;font-size:10px!important}
html body #padMixer#padMixer small{width:100%!important;font-size:8.5px!important;white-space:normal!important;line-height:1.1!important;max-height:3.4em}
#kDjStrips{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 8px}
#kDjStrips .dj{display:flex;align-items:center;gap:6px;border:1px solid #39404d;border-top:4px solid #ff7ad9;border-radius:6px;padding:6px 8px;background:linear-gradient(180deg,#232833,#151922);color:#d6deea;font:700 12px system-ui,sans-serif;flex:1 1 220px}
#kDjStrips input[type=range]{flex:1 1 auto;accent-color:#ff7ad9}
#kDjStrips button{min-height:30px;min-width:34px;border-radius:8px;font:800 12px system-ui,sans-serif}`; document.head.appendChild(css);
 function railBtn(id,i,l,title,fn){ const d=$('rDock'); if(!d) return null; let b=$(id); if(!b){ b=document.createElement('button'); b.type='button'; b.id=id; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); fn(e); }); const home=$('kdHome'); if(home&&home.nextSibling) d.insertBefore(b,home.nextSibling); else d.appendChild(b); } b.dataset.kdI=i; b.dataset.kdL=l; b.title=title; b.setAttribute('aria-label',title); return b; }
 function paintPS(){ const b=$('kStopBtn'); if(!b) return; const p=playing(); const want=p?'Stop':'Play'; if(b.dataset.kdL!==want){ b.dataset.kdL=want; b.dataset.kdI=p?'■':'▶'; } b.classList.toggle('kStop',!!p); b.classList.toggle('kPlay',!p); const t=p?('■ Stop '+p):('▶ Play '+(WHAT[cur()]||'your beat')); if(b.title!==t){ b.title=t; b.setAttribute('aria-label',t); } }
 /* one button, both jobs: when nothing plays, the rail's button plays; when something plays, it stops everything */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#kStopBtn'); if(!b) return; if(playing()) { setTimeout(paintPS,250); return; } e.preventDefault(); e.stopImmediatePropagation(); doPlay(); },true);
 function rail(){ railBtn('kdStudio','🎛','Studio','The studio: sequencer, the 24-channel console, pads, keys, DJ and recording',()=>{ try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ const h=$('kStudioHead'); if(h) h.scrollIntoView({block:'start'}); },1300); });
  railBtn('kdSocial','🌐','Social','DD Universe Social: your profile, your posts, the feed',()=>{ try{ KSOCIAL.open(); }catch(_){ say('Social is loading. Try again in a moment.'); } });
  railBtn('kdProfile','👤','Profile','Your profile: photo, birth date, sign, compass letter, song, posts',()=>{ try{ KPROFILE.open(); }catch(_){ say('The profile is loading. Try again in a moment.'); } });
  railBtn('kdProj','📁','Projects','Projects: save, open, continue and export everything you make',()=>{ try{ KPROJ.open(); }catch(_){ say('Projects is loading. Try again in a moment.'); } });
  paintPS(); }
 setInterval(rail,600); rail();
 /* ---------- the 24-channel console ---------- */
 const BANKS=[['all','All 40'],['r1','1–20'],['r2','21–40'],['drums','🥁 1–16 Pads'],['music','🎹 17–23 Instruments'],['vox','🎤 5 mics 24–28'],['dj','🎧 DJ 29–30'],['midi','🎹 MIDI 31–38, cannon, click']];
 let bank='all';
 function console24(){ const m=$('padMixer'); if(!m) return; const strips=[...m.querySelectorAll('.mxs')];
  strips.forEach(s=>{ const c=+s.dataset.c; const isM=s.dataset.c==null||s.classList.contains('master'); const show=bank==='all'||isM||(bank==='r1'&&c<20)||(bank==='r2'&&c>=20)||(bank==='drums'&&c<16)||(bank==='music'&&c>=16&&c<23)||(bank==='vox'&&c>=23&&c<=27)||(bank==='dj'&&(c===28||c===29))||(bank==='midi'&&c>=30); const hide=!show; if(s.hidden!==hide) s.hidden=hide; });
  if(!$('kStudioHead')){ const h=document.createElement('div'); h.id='kStudioHead'; m.parentNode.insertBefore(h,m); h.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); if(b.dataset.bank){ bank=b.dataset.bank; paintHead(); console24(); const dj=$('kDjStrips'); if(dj&&bank==='dj') dj.scrollIntoView({block:'center'}); } if(b.dataset.st==='rec'){ try{ KKARA.open(); }catch(_){ } } }); paintHead(); }
  if(!$('kDjStrips')){ const w=document.createElement('div'); w.id='kDjStrips'; m.parentNode.insertBefore(w,m.nextSibling); w.innerHTML=['A','B'].map((d,i)=>'<div class="dj"><span>'+(25+i)+' · DJ deck '+d+'</span><input type="range" min="0" max="120" value="100" data-dj="'+d+'" aria-label="DJ deck '+d+' level"><button type="button" data-djm="'+d+'" title="Mute deck '+d+'" data-noul>M</button><button type="button" data-djp="'+d+'" title="Play or pause deck '+d+'" data-noul>▶</button></div>').join('');
   w.addEventListener('input',e=>{ const d=e.target.dataset.dj; if(!d) return; const s=document.querySelector('#deck'+d+' input[data-k="vol"]'); if(s){ s.value=e.target.value; s.dispatchEvent(new Event('input',{bubbles:true})); s.dispatchEvent(new Event('change',{bubbles:true})); } });
   w.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation(); const d=b.dataset.djm||b.dataset.djp; if(b.dataset.djm){ const r=w.querySelector('[data-dj="'+d+'"]'), s=document.querySelector('#deck'+d+' input[data-k="vol"]'); const muted=b.classList.toggle('on'); if(s){ if(muted){ b.dataset.was=s.value; s.value='0'; } else s.value=b.dataset.was||r.value; s.dispatchEvent(new Event('input',{bubbles:true})); } }
    if(b.dataset.djp){ try{ const D=DJBOOTH.D[d]; if(D.playing) DJBOOTH.pause(d); else if(D.buf) DJBOOTH.start(d); else say('Load a track on deck '+d+' first (🎧 DJ on the rail).'); }catch(_){ say('Open 🎧 DJ on the rail once, then try again.'); } } }); }
  const dj=$('kDjStrips'); if(dj) dj.hidden=bank!=='dj'; }
 function paintHead(){ const h=$('kStudioHead'); if(!h) return; const n=($('padMixer')||{querySelectorAll:()=>[]}).querySelectorAll('.mxs[data-c]').length; h.innerHTML='<b>🎚 Console · '+Math.max(40,n)+' tracks + master</b>'+BANKS.map(([k,l])=>'<button type="button" data-bank="'+k+'" class="'+(k===bank?'on':'')+'" data-noul>'+l+'</button>').join('')+'<button type="button" data-st="rec" data-noul>🎙 Record a track</button>'; }
 setInterval(()=>{ const pad=$('pad'); if(pad&&pad.classList.contains('on')) console24(); },900);
 /* ---------- the Menu: most used first ---------- */
 const GMAP={3:1,2:2,1:3,6:4,0:5,4:6,7:7,5:8}; // old drawer → new place (0 is Social & me)
 const SUB={ttPad:1,ttKara:2,ttDJ:3,ttKeys:4,ttMusic:5,ttSw:6,ttBand:7,ttVc:8,ttWatch:9,ttTac:1,ttVid:1,ttVoice:2,ttHumor:1,ttScope:2,ttJoke:3};
 function menu(){ const t=$('tourTab'); if(!t) return; [...t.children].forEach(c=>{ if(c.dataset.kmDone) return; const o=parseInt(c.style.order||'0',10); if(o<100||o>=1000) return; if(c.id==='kSocGrp'||c.dataset.kmSoc) return; const g=Math.floor(o/100)-1; if(!(g in GMAP)) return; const ng=GMAP[g]; const sub=c.classList.contains('kGrp')?0:(SUB[c.id]!=null?SUB[c.id]:10+(o%100)); const no=(ng+1)*100+sub; c.style.order=String(no); c.dataset.kmDone='1'; if(c.dataset.o0!=null) c.dataset.o0=String(no); if(c.classList.contains('kGrp')) c.dataset.g=String(ng); else c.dataset.kg=String(ng); });
  if(!$('kSocGrp')){ const h=document.createElement('div'); h.className='kGrp'; h.id='kSocGrp'; h.dataset.g='0'; h.dataset.kmSoc='1'; h.textContent='🌐 Social and me'; h.style.order='100'; h.setAttribute('role','button'); h.tabIndex=0; t.appendChild(h);
   [['ttSoc','🌐 DD Universe Social',()=>KSOCIAL.open()],['ttProf','👤 My profile',()=>KSOCIAL.open('profile')],['ttMyLib','📚 My library (on this device)',()=>KSOCIAL.open('library')],['ttPost','➕ Make a post',()=>KSOCIAL.open('create')]].forEach(([id,l,fn],i)=>{ const b=document.createElement('button'); b.type='button'; b.id=id; b.className='ttMusic'; b.textContent=l; b.style.order=String(101+i); b.dataset.kg='0'; b.dataset.kmSoc='1'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>{ try{ fn(); }catch(_){ } },120); }); t.appendChild(b); }); }
  /* the big buttons at the top, most used first */
  const st=t.querySelector('.kStart'); if(st&&st.textContent!=='⭐ Most used'){ st.textContent='⭐ Most used'; }
  if(st&&!t.dataset.kmTop&&t.querySelector('.kStartB')){ t.dataset.kmTop='1'; const TOP=[['📁 Projects · my work',()=>KPROJ.open()],['👤 My profile',()=>KPROFILE.open()],['🌐 Social',()=>KSOCIAL.open()],['🕹 Video games',()=>KVG.open()],['🎬 Video studio',()=>KRAIL.goTo('aivDock')],['🤖 AI · talk and create',()=>KAI.open()],['🎨 The Easel · draw',()=>KEASEL.open()],['🎛 Studio · make a beat',()=>KRAIL.goTo('pad')],['🎤 Karaoke · record',()=>KKARA.open()],['🎵 Music',()=>KRAIL.goTo('musicDock')],['😂 Laugh',()=>KHUMOR.open('day')],['♈ LuvMyZodiac',()=>KRAIL.goTo('zodDock')],['🧭 Omni-Compass',()=>KRAIL.goTo('omniDock')],['📖 Make a story',()=>{ GOHOME(); const b=$('mQP')||$('qpBtn'); if(b) b.click(); }],['📚 My library',()=>KSOCIAL.open('library')],['🔒 Lock & shuffle',()=>KLOCK.open()],['🎓 Knowledge library',()=>KKNOW.open()],['💥 Surprise me',()=>{ KJUMP.open(); setTimeout(()=>KJUMP.jump(),300); }],['🗺 Show me around',()=>{ const b=document.querySelector('#kHomeBar [data-ka="tour"]'); if(b) b.click(); }],['🎲 Games · '+((window.GAMES&&GAMES.list&&GAMES.list.length)||239),()=>KRAIL.goTo('gamesDock')],['✍️ Songwriter',()=>KRAIL.goTo('swDock')],['📖 Storybook',()=>KRAIL.goTo('sbDock')],['🎙 Voices',()=>KRAIL.goTo('voiceDock')],['🌐 Language',()=>KRAIL.goTo('langDock')],['🧭 Layers',()=>KRAIL.goTo('layDock')],['🛠 Craft',()=>KRAIL.goTo('craftDock')],['🧬 Mutate',()=>KRAIL.goTo('mutDock')],['🗂 Story library',()=>{ GOHOME(); setTimeout(()=>{ const e=document.getElementById('s-lib'); if(e) e.scrollIntoView({block:'start',behavior:'smooth'}); },500); }],['🗺 All sections',()=>KRAIL.goTo('mapDock')],['❓ Ask KAN-IN',()=>KRAIL.goTo('askDock')]];
   t.querySelectorAll('.kStartB').forEach(b=>b.remove()); TOP.forEach(([l,fn],i)=>{ const b=document.createElement('button'); b.type='button'; b.className='ttMusic kStartB'; b.textContent=l; b.style.order=String(41+i); b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>{ try{ fn(); }catch(_){ } },120); }); t.appendChild(b); }); } }
 setInterval(menu,1000);
 window.KSTUDIO={playing,play:doPlay,bank:b=>{ bank=b; paintHead(); console24(); }};
})();
