(()=>{ /* THE RIGHT RAIL: one strip down the right edge, top to bottom, holds every control. Home, this screen's control panel, Karaoke,
   the virtual tour, Ask, Stop, and the Menu at the bottom. The bars that sat on top of each screen are gone; everything lives in the rail.
   Every link lands exactly on what it names: Beat Maker on the 16 pads, Keyboard on the keyboard, DJ on the DJ booth. */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const sleep=ms=>new Promise(r=>setTimeout(r,ms)); const say=m=>{ try{ toast(m); }catch(_){ } };
 const shown=e=>!!(e&&!e.hidden&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().height>0);
 const SCREENS='#pad.on,#swDock,#zodDock,#omniDock,#opsHub,#gamesDock,#tac,#libDock,#fileDock,#sbDock,#musicDock,#aivDock,#voiceDock,#langDock,#layDock,#craftDock,#mutDock,#mapDock,#askDock,#kHumor,#kJump,#kKara,#kOwner,#kVG';
 const css=document.createElement('style'); css.id='kRailCss';
 css.textContent=`
:root{--kRailW:58px;--kDockH:0px;--rdockH:0px}
@media (min-width:761px){:root{--kRailW:76px}}
html body .kBar,html body #kHomeBar,html body .kStick{display:none!important}
html body{padding-bottom:0!important;padding-right:var(--kRailW)!important;box-sizing:border-box}
html body #rDock#rDock{position:fixed!important;top:0!important;bottom:0!important;right:0!important;left:auto!important;width:var(--kRailW)!important;height:auto!important;max-width:none!important;margin:0!important;padding:calc(6px + env(safe-area-inset-top,0px)) max(4px,env(safe-area-inset-right,0px)) calc(6px + env(safe-area-inset-bottom,0px)) 4px!important;box-sizing:border-box!important;display:flex!important;flex-direction:column!important;flex-wrap:nowrap!important;align-items:stretch!important;justify-content:flex-start!important;gap:5px!important;background:rgba(9,11,38,.98)!important;border-top:0!important;border-left:1px solid rgba(255,233,74,.35)!important;box-shadow:-6px 0 20px rgba(0,0,0,.5)!important;z-index:9900!important;transform:none!important;overflow-y:auto!important;overflow-x:hidden!important}
html body.gated #rDock#rDock{display:none!important}
html body #rDock#rDock button{flex:0 0 auto!important;width:100%!important;max-width:none!important;min-height:52px!important;height:auto!important;order:5}
html body #rDock#rDock :is(#kFreeze,#imPad,#imTog,#kdRemote,#kdNet,#kmOpen),html body #rDock#rDock #inMode button{display:none!important}
html body #rDock#rDock #kdHome{order:1!important}html body #rDock#rDock #kdPanel{order:2!important}html body #rDock#rDock #kdKara{order:3!important}html body #rDock#rDock #kdTour{order:4!important}html body #rDock#rDock #askBtn{order:5!important}html body #rDock#rDock #kStopBtn{order:6!important}
html body #rDock#rDock .kdSpace{order:7!important;flex:1 1 auto!important;min-height:4px}
html body #rDock#rDock #lpMenu{order:9!important;min-height:60px!important}
html body #rDock#rDock :is(#kdHome,#kdPanel,#kdKara,#kdTour){display:flex!important}
html body #rDock#rDock #kdPanel.on{background:#ffe94a!important}html body #rDock#rDock #kdPanel.on::before,html body #rDock#rDock #kdPanel.on::after{color:#14163a!important}
html body #rDock#rDock button[data-kd-i]::after{font-size:10px!important;white-space:normal!important;text-align:center;line-height:1.05!important}
@media (min-width:761px){ html body #rDock#rDock button[data-kd-i]::after{font-size:11.5px!important} html body #rDock#rDock button[data-kd-i]::before{font-size:21px!important} }
html body :is(${SCREENS},#sbp:not([hidden])):not([hidden]){top:0!important;left:0!important;right:var(--kRailW)!important;bottom:0!important;width:auto!important;height:auto!important;max-width:none!important;max-height:none!important;margin:0!important;border-radius:0!important;transform:none!important}
html body :is(#kManual,#kDay,#kCan,#kMe,#kNetCard,#playMode,#tpFull,#qpDone,#rmtPanel,#kbusCard,#kUpd){right:var(--kRailW)!important;max-width:calc(100vw - var(--kRailW))!important}
html body :is(#kFix,#kDayChip,#gtCard){left:auto!important;right:calc(var(--kRailW) + 10px)!important;transform:none!important;bottom:calc(12px + env(safe-area-inset-bottom,0px))!important;max-width:calc(100vw - var(--kRailW) - 20px)!important}
html body #tourCard{right:calc(var(--kRailW) + 12px)!important}
html body #tourMini{right:calc(var(--kRailW) + 8px)!important;bottom:calc(12px + env(safe-area-inset-bottom,0px))!important;max-width:calc(100vw - var(--kRailW) - 16px)!important}
html body #toast{right:calc(var(--kRailW) + 10px)!important;left:auto!important;transform:none!important;max-width:calc(100vw - var(--kRailW) - 20px)!important}
html body #tourTab.lp{left:8px!important;right:calc(var(--kRailW) + 8px)!important;bottom:8px!important;top:auto!important;width:auto!important;max-width:760px!important;margin-left:auto!important;max-height:calc(100vh - 16px)!important;transform:none!important}
#kPanel{position:fixed;top:0;bottom:0;right:var(--kRailW);width:min(400px,calc(100vw - var(--kRailW)));z-index:9890;background:#0d1036;color:#eef;border-left:2px solid #ffe94a;box-shadow:-10px 0 30px rgba(0,0,0,.6);overflow-y:auto;box-sizing:border-box;padding:calc(10px + env(safe-area-inset-top,0px)) 12px calc(16px + env(safe-area-inset-bottom,0px)) 12px;font:15px/1.4 system-ui,sans-serif}
#kPanel[hidden]{display:none}
#kPanel .kpHead{display:flex;align-items:center;gap:8px;position:sticky;top:-10px;background:#0d1036;padding:6px 0 8px;z-index:2}
#kPanel .kpHead h3{flex:1;margin:0;font:800 17px/1.2 system-ui,sans-serif;color:#ffe94a}
#kPanel details{border:1px solid rgba(255,255,255,.16);border-radius:12px;margin:8px 0;background:rgba(255,255,255,.04)}
#kPanel summary{cursor:pointer;padding:12px;font:700 15px system-ui,sans-serif;color:#fff;list-style-position:inside}
#kPanel .kpL{display:grid;grid-template-columns:1fr;gap:6px;padding:0 10px 10px}
#kPanel .kpL button[data-kp^="gd"]{font-weight:500!important;cursor:default}
#kPanel .kpL button{text-align:left;padding:11px 12px;border-radius:10px;font:600 14.5px/1.25 system-ui,sans-serif;cursor:pointer;min-height:44px}
#kPanel .kpX{min-width:44px;min-height:44px;border-radius:10px;font-size:18px}
#kPanel .kpTr{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:4px 0 6px}
#kPanel .kpTr button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;min-height:58px;border-radius:12px;padding:4px 2px}
#kPanel .kpTr button span{font-size:22px;line-height:1}
#kPanel .kpTr button small{font:700 11.5px system-ui,sans-serif}
#kPanel .kpTr button[data-kp="tr:stop"]{background:#b3172f!important}
#kPanel .kpTr button[data-kp="tr:rec"]{background:#ff2d55!important}
#kPanel .kpTr button[data-kp="tr:jump"]{background:#ffe94a!important;color:#14163a!important}
#kPanel .kpTrN{font-size:12.5px;line-height:1.45;opacity:.88;margin:0 2px 8px}
`;
 document.head.appendChild(css);
 /* ---------- which screen is open ---------- */
 const NAMES={home:'Home'}; try{ (window.KBAR&&KBAR.screens||[]).forEach(s=>NAMES[s.id]=s.name); }catch(_){ }
 function cur(){ const ds=[...document.querySelectorAll(SCREENS+',#sbp')].filter(d=>shown(d)&&getComputedStyle(d).position==='fixed'); if(!ds.length) return 'home'; ds.sort((a,b)=>(+getComputedStyle(b).zIndex||0)-(+getComputedStyle(a).zIndex||0)); return ds[0].id; }
 const nameOf=id=>{ try{ if(!NAMES[id]&&window.KBAR) KBAR.screens.forEach(s=>NAMES[s.id]=s.name); }catch(_){ } return NAMES[id]||({gamesDock:'Games',opsHub:'Game hub',libDock:'Story library',fileDock:'Library',sbp:'Storybook',tac:'TAC-OPS',kHumor:'Humor',kJump:'Cannon Jump Generator',kKara:'Karaoke Live',kOwner:'The owner’s word',kVG:'Video games'}[id])||id; };
 /* ---------- landing exactly on what a link names ---------- */
 const byHead=t=>{ const hs=[...document.querySelectorAll('h2,h3,h4')].filter(h=>!h.closest('.kBar,.ocSec,.ocBrand,[id^=lib-]')&&h.textContent.trim().startsWith(t)); return hs[0]||null; };
 const T=sel=>sel.startsWith('@')?byHead(sel.slice(1)):document.querySelector(sel);
 function scroller(el){ let n=el.parentElement; while(n&&n!==document.body){ const cs=getComputedStyle(n); if(/(auto|scroll)/.test(cs.overflowY)&&n.scrollHeight>n.clientHeight+4) return n; n=n.parentElement; } return document.scrollingElement||document.documentElement; }
 function land(sel){ const el=typeof sel==='string'?T(sel):sel; if(!el) return false; const fk=floatOf(el); if(fk){ FLOAT.open(fk); return true; } const box=el; const sc=scroller(box); let stick=0; try{ const bb=$('bbBar'); if(bb&&sc.contains(bb)&&getComputedStyle(bb).position==='sticky') stick=bb.getBoundingClientRect().height; }catch(_){ }
  const top=box.getBoundingClientRect().top-(sc===document.scrollingElement||sc===document.documentElement?0:sc.getBoundingClientRect().top); sc.scrollTop=Math.max(0,sc.scrollTop+top-stick-8); try{ box.animate([{outline:'3px solid #ffe94a'},{outline:'3px solid transparent'}],{duration:1400}); }catch(_){ } return true; }
 const LAND={pad:'#padGrid',djSec:'#djSec',kBand:'#bandSec',kSounds:'#vcSec',keys:'#kbKeys'};
 let want=null, wantAt=0; const aim=(sel)=>{ want=sel; wantAt=Date.now(); [700,1500].forEach(ms=>setTimeout(()=>{ if(want===sel&&Date.now()-wantAt<2500) land(sel); },ms)); setTimeout(()=>{ if(want===sel) want=null; },1700); };
 function goTo(id,sel){ if(id==='kKara'){ closePanel(); try{ KKARA.open(); }catch(_){ } return; } if(id==='kJump'){ closePanel(); try{ KJUMP.open(); }catch(_){ } return; } if(id==='kHumor'){ closePanel(); try{ KHUMOR.open(); }catch(_){ } return; } if(id==='kOwner'){ closePanel(); try{ KOWNER.open(); }catch(_){ } return; } if(id==='kVG'){ closePanel(); try{ KVG.open(); }catch(_){ } return; } try{ ['kManual','kMe','kCan','kNetCard','kDay','libDock','fileDock'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } const target=sel||LAND[id]; if(target) want=target, wantAt=Date.now(); try{ KBAR.go(id==='keys'?'pad':id); }catch(_){ } if(target) aim(target); closePanel(); }
 /* every way into the Beat Maker lands on the pads unless it asked for another part */
 try{ const pad=$('pad'); let was=pad&&pad.classList.contains('on'); if(pad) new MutationObserver(()=>{ const on=pad.classList.contains('on'); if(on&&!was){ setTimeout(beatBase,50); if(!(want&&Date.now()-wantAt<2500)) aim('#padGrid'); } was=on; }).observe(pad,{attributes:true,attributeFilter:['class']}); }catch(_){ }
 const MAPID={ttPad:'#padGrid',ttDJ:'#djSec',ttBand:'#bandSec',ttVc:'#vcSec',ttWatch:null};
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#tourTab button'); if(b&&MAPID[b.id]){ want=MAPID[b.id]; wantAt=Date.now(); aim(MAPID[b.id]); } },true);
 /* ---------- the rail's own buttons ---------- */
 function railBtn(id,i,l,title,fn){ const d=$('rDock'); if(!d) return; let b=$(id); if(!b){ b=document.createElement('button'); b.type='button'; b.id=id; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); fn(e); }); d.appendChild(b); } b.dataset.kdI=i; b.dataset.kdL=l; b.title=title; b.setAttribute('aria-label',l); }
 function rail(){ const d=$('rDock'); if(!d) return; if(!d.querySelector('.kdSpace')){ const s=document.createElement('span'); s.className='kdSpace'; d.appendChild(s); }
  railBtn('kdHome','🏠','Home','Home: close this screen and go to the landing page',()=>{ closePanel(); try{ GOHOME(); }catch(_){ } setTimeout(()=>{ try{ LAUNCHPAD.fold(); }catch(_){ } scrollTo(0,0); },200); });
  railBtn('kdPanel','⚙','Panel','This screen’s control panel',()=>{ const p=$('kPanel'); if(p&&!p.hidden) closePanel(); else openPanel(); });
  railBtn('kdKara','🎤','Karaoke','Karaoke: your lyrics on the beat, full screen',karaoke);
  railBtn('kdTour','🗺','Tour','The virtual tour of the whole app',()=>{ closePanel(); clickAct('home','tour'); });
  const st=$('kStopBtn'); if(st){ st.dataset.kdI='■'; st.dataset.kdL='Stop'; } const ask=$('askBtn'); if(ask){ ask.dataset.kdI='🎙'; ask.dataset.kdL='Ask'; }
  const pb=$('kdPanel'); if(pb) pb.classList.toggle('on',!!($('kPanel')&&!$('kPanel').hidden)); }
 function clickAct(sc,ka){ const b=document.querySelector('.kBar[data-sc="'+sc+'"] [data-ka="'+ka+'"]')||document.querySelector('#kHomeBar [data-ka="'+ka+'"]'); if(b){ b.click(); return true; } return false; }
 async function karaoke(){ closePanel(); if(window.KKARA&&KKARA.open){ KKARA.open(); return; } try{ KAUDIO&&KAUDIO.gesture&&KAUDIO.gesture(); }catch(_){ } goTo('pad','#tpWrap'); await sleep(900); const s=$('tpSrc'); if(s){ s.value='lyr'; s.dispatchEvent(new Event('change',{bubbles:true})); }
  const box=$('tpText'); const lyr=($('padLyr')&&$('padLyr').value)||''; if(!lyr.trim()&&$('padLyrAI')){ $('padLyrAI').click(); await sleep(900); }
  const play=$('padPlay'); if(play&&!/stop|❚❚|pause/i.test(play.textContent)) play.click(); await sleep(300); const f=$('tpFullGo'); if(f) f.click(); say('Karaoke: sing along as each line lights on the beat. ■ Stop ends it.'); }
 /* ---------- one control panel, in drawers ---------- */
 const DEEP={pad:[['🥁 The 16 pads','#padGrid'],['🎹 Keyboard','@🎹 Keyboard'],['🎛 Channel rack','#crSec'],['🎚 MPC controls','#mpcSec'],['🎼 Composer','#cmpWrap'],['🎹 Piano roll','#rollWrap'],['🎚 Mixer','@🎚 Mixer'],['🎤 Vocals','#vocSec'],['📜 Teleprompter (karaoke)','#tpWrap'],['🎧 DJ booth','#djSec'],['🎛 Story band (20 tracks)','#bandSec'],['📚 Sound library','#slSec'],['🎻 Recorded instruments','#vcSec'],['🎛 Morph synth','#msSec'],['📈 Automation','#autoSec'],['🎚 Sample editor','#seSec'],['✂ Wave chopper','#chopSec'],['🎚 Song sequencer','#sqWrap'],['🟩 Session board','#sesWrap'],['🗄 The rack','#rkWrap'],['🎚 Effects rack','#kbWrap'],['🧠 Studio brain','#brainSec'],['🎲 Shuffle engine','#shSec'],['🎓 Music referee','#mrSec'],['🧭 Field engine','#ofWrap']]};
 function parts(id){ if(DEEP[id==='djSec'||id==='kBand'||id==='kSounds'?'pad':id]) return DEEP[id==='djSec'||id==='kBand'||id==='kSounds'?'pad':id].filter(x=>{ const e=T(x[1]); if(!e) return false; const l=e.closest('[data-lvl]'); return !(l&&getComputedStyle(l).display==='none'); });
  const root=id==='home'?document.querySelector('.wrap'):$(id); if(!root) return []; const out=[], seen=new Set();
  root.querySelectorAll('h2,h3,h4,summary.kLibS').forEach(h=>{ if(h.closest('.kBar,.ocSec,.ocBrand,.ocFoot,details:not([open])>*:not(summary),#kPanel,#tourTab')||!h.getClientRects().length) return; let t=h.textContent.trim().replace(/\s+/g,' '); if(!t||t.length<2||seen.has(t)) return; seen.add(t); out.push([t.length>48?t.slice(0,46)+'…':t,h]); });
  return out.slice(0,40); }

 /* how each new page works, control by control, in plain formal words */
 const GUIDES={
  kKara:[['🎙 Microphone','Turns the input on and shows its level for four seconds. Inside claude.ai the page frame blocks microphones for everyone; on KAN-IN’s own website it records live.'],['🎧 Headphones: hear myself','Sends your voice back to you, with the chosen voice effect, while you record. Use headphones so the speakers do not feed back.'],['Input and Output','Input chooses the microphone. Output moves every sound KAN-IN is playing to the chosen speakers or headphones, where the browser allows it.'],['⏮','Restarts the beat from the top.'],['▶ Play','Starts the beat.'],['⏸ Pause','Stops the beat; ▶ Play starts it again.'],['■ Stop','Stops every sound and the reading voice.'],['⏭ Next song','The cannon writes a new song and a new beat.'],['⏺ Auto-record','Counts in four beats, starts the beat and the lyrics, records the chosen number of bars, stops by itself, and puts the take on the vocal track when that box is ticked.'],['✕ Close','Closes Karaoke and returns to where you were.'],['1 · The song','Load lyrics from the Songwriter, the Beat Maker, the prompter or your comedy bit; let the cannon write a song; or write lyrics from your story. 🗣 Speak lyrics in writes what you say; 🔊 reads them out; 🤖 the robot singer sings them on the melody.'],['2 · The beat','Play or stop the beat, let the cannon pick a new one, or connect a MIDI keyboard to play the keys.'],['3 · Perform','🎙 Record live starts and stops a take by hand; 🎤 Sing along shows the lyrics full screen on the beat; 📁 Bring in a recording adds any audio file as a take.'],['4 · Your takes','Each take: choose a voice and hear it, make a new take with that voice, put it on the vocal track (channel 24), chop it in Mutate, put it on DJ deck B, save it (.webm inside claude.ai, .wav on the website) or delete it.'],['5 · Build the song','Puts every take on the track, puts the lyrics in the prompter, and opens the studio on the sequencer and the mixing board.']],
  kHumor:[['😂 Joke of the day','A new joke every day, the same for everyone on that day. Save it, hear it, or use it.'],['🗂 Every kind of joke','Each tab lists every joke of that kind; My favourites and My jokes hold what you saved and wrote.'],['On every joke','☆ Save keeps it; ＋ Add to my bit puts it in your comedy bit; 🔊 reads it; 📋 copies it; ➡ Use it picks it for sending.'],['➡ Use a joke','Sends the picked joke into a song or poem, the prompter script, the Mutate studio or the translator.'],['✏ Write your own','Write a set-up and a punchline and save it to My jokes.'],['🎭 Comedy bit builder','Your picked jokes in order: move them, remove them, perform them aloud, copy them, or send the bit to the prompter as a script.'],['💥 Cannon joke','The cannon picks a joke from every kind at once.']],
  kJump:[['💥 Jump','Fires the cannon through every realm in reach and lands each one on one of its options.'],['How deep','Spark to Omni: how many realms one shot reaches, from 3 to all of them.'],['How it jumps','Free: every realm lands on its own. Chain: each landing feeds the next. Mirror: every other realm lands opposite the one before.'],['🔒 on a realm','Keeps that landing while everything else jumps.'],['🔀 Flip A↔Z','Turns every unlocked landing to its mirror option; flipping twice returns it.'],['🔁 Flop','Steps every unlocked landing to its neighbouring option.'],['🏆 Score','Five measures of each jump: Rarity, Harmony, Surprise, Reach and Streak, out of 500, with levels from Spark to Omni.'],['▶ Build it all','Builds the whole landing into the app: the story, the beat, the song and every setting; then shows where each piece went.'],['🕘 Recent jumps','Brings back any of your last twelve jumps.']]};

 /* THE TRANSPORT: the same eight buttons at the top of every control panel, each doing this screen's own job */
 const C=id=>()=>{ const b=$(id); if(b){ b.click(); return true; } say('That control is not on this screen yet.'); return false; };
 const Q=sel=>()=>{ const b=document.querySelector(sel); if(b){ b.click(); return true; } return false; };
 const stopAll=()=>{ const b=$('kStopBtn'); if(b) b.click(); else try{ KAUDIO.stopAll(); }catch(_){ } };
 const toTop=()=>{ const id=cur(); const r=(id!=='home'&&$(id))||document.scrollingElement||document.documentElement; try{ r.scrollTo({top:0,behavior:'smooth'}); }catch(_){ try{ r.scrollTop=0; }catch(__){ } } };
 let partIx=-1; const nextPart=()=>{ const ps=parts(cur()); if(!ps.length) return toTop(); partIx=(partIx+1)%ps.length; land(ps[partIx][1]); say('⏭ '+ps[partIx][0]); };
 const karaRec=()=>{ if(window.KKARA){ KKARA.open(); setTimeout(()=>{ const b=document.querySelector('#kKara [data-kk="auto"]'); if(b) b.click(); },500); } };
 function shuffleHere(){ const id=cur(), root=id==='home'?document.querySelector('.wrap'):$(id); if(!root) return; const sels=[...root.querySelectorAll('select')].filter(e=>!e.closest('.kBar,[id^=lib-],#kPanel,#tourTab')&&e.getClientRects().length&&e.options.length>1&&!/lang|voice|kind|who|city|role/i.test(e.id)).slice(0,30); let n=0;
  sels.forEach(e=>{ let x=Math.random(); try{ x=UNILAW.fire('games',{quiet:true}).first; }catch(_){ } const o=[...e.options].filter(q=>!q.disabled); const q=o[Math.floor(x*o.length)]; if(q&&q.value!==e.value){ e.value=q.value; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); n++; } }); say('🔀 The cannon re-picked '+n+' setting'+(n===1?'':'s')+' on this screen.'); }
 const jumpGen=()=>{ try{ KJUMP.open(); setTimeout(()=>KJUMP.jump(),300); }catch(_){ } };
 const D={back:['⏮','Back',['back to the top',toTop]],play:['▶','Play',['plays this screen',()=>{ if(!clickAct(cur(),'start')) say('Nothing plays on this screen.'); }]],pause:['⏸','Pause',['pauses',stopAll]],stop:['■','Stop',['stops every sound',stopAll]],rec:['⏺','Record',['records you in Karaoke Live',karaRec]],shuf:['🔀','Shuffle',['the cannon re-picks every setting here',shuffleHere]],jump:['💥','Jump',['the cannon jumps every realm at once',jumpGen]],next:['⏭','Next',['goes to the next part of this screen',nextPart]]};
 const TR={
  pad:{back:['rewinds the loop',C('ktRew')],play:['plays the beat',C('bbPlay')],pause:['stops the loop',C('bbStop')],rec:['records what you play on the pads and keys into the pattern',C('bbRec')],shuf:['a mystery shuffle move on the beat',C('shRand')],jump:['fires the cannon at the beat',C('bmFire')],next:['the Composer writes a new beat',C('cAuto')]},
  djSec:{play:['starts the cannon auto-mix',C('djAuto')],rec:['records the mix',C('djRec')],jump:['the cannon mixes the decks',C('djAuto')]},
  home:{play:['the guided tour with voice',C('mTour')],shuf:['Quick Pick: all 20 canvases land again',C('mQP')],next:['rewrites this story',C('mRew')],rec:['records you reading or singing in Karaoke Live',karaRec]},
  sbp:{back:['the page before',C('sbpPrev')],play:['tells the story aloud',C('sbpPlay')],next:['the next page',Q('#sbp [id*=Next]')],shuf:['shuffles the book’s beat',C('sbpBeat')]},
  musicDock:{back:['the song before',C('mPrev')],play:['plays or pauses the score',C('mPP')],pause:['plays or pauses the score',C('mPP')],stop:['stops the music',C('mStop')],next:['the next song',C('mNext')],shuf:['shuffles the songs',C('mShuf')],jump:['shuffles the beat under the score',C('mShufBeat')]},
  swDock:{play:['puts the lyrics on the beat',C('swBeat')],shuf:['shuffles the verses',C('swShuf')],jump:['fires the cannon: writes the song',C('swFire')],next:['a mystery form',C('swMyst')]},
  zodDock:{back:['the page before',C('z4BkPrev')],play:['reads the sign aloud',C('zodSay')],stop:['stops the reading and music',C('z4Stop')],next:['the next page',C('z4BkNext')],shuf:['a mystery sign',C('zodMyst')],jump:['fires the cannon at the zodiac',C('zodSpin')]},
  omniDock:{back:['the letter before',C('otPrev')],play:['plays this letter',C('otPlay')],stop:['stops the compass',C('otStop')],next:['the next letter',C('otNext')],shuf:['rolls and fires',C('otBoom2')],jump:['fires the cannon',C('otBoom')]},
  voiceDock:{play:['reads the whole story',C('vcRead')],stop:['stops reading',C('vcStop')]},
  langDock:{play:['reads the translation aloud',C('lRead')],stop:['stops reading',C('lStopR')]},
  aivDock:{play:['plays the movie',C('aivPlay')],stop:['stops the movie',C('aivStop')]},
  mutDock:{play:['plays the mutated song',C('mutAPlay')],jump:['mutates it',C('mutAGo')]},
  craftDock:{shuf:['a new metaphor',C('mwGo')],jump:['fires the cannon at your writing',C('crFire')],next:['a new practice line',C('drGo')]},
  layDock:{shuf:['spins every layer',C('layRandom')]},
  gamesDock:{play:['starts the game',()=>{ const b=[...document.querySelectorAll('#gamesDock .gbar button')].reverse().find(x=>/Start|Play|Resume|again/.test(x.textContent)); if(b) b.click(); }],pause:['pauses the game',()=>{ const b=[...document.querySelectorAll('#gamesDock .gbar button')].reverse().find(x=>/Pause/.test(x.textContent)); if(b) b.click(); }],next:['a new game',()=>{ const b=[...document.querySelectorAll('#gamesDock button')].find(x=>/^New game/.test(x.textContent.trim())); if(b) b.click(); }],shuf:['a surprise game',()=>{ const b=[...document.querySelectorAll('#gamesDock button')].find(x=>/Surprise me/.test(x.textContent)); if(b) b.click(); }]},
  kKara:{back:['back to the top of the beat',Q('#kKara [data-kk="back"]')],play:['plays the beat',Q('#kKara [data-kk="play"]')],pause:['pauses the beat',Q('#kKara [data-kk="pause"]')],rec:['auto-records your take',Q('#kKara [data-kk="auto"]')],next:['the cannon writes the next song',Q('#kKara [data-kk="next"]')],jump:['the cannon writes a song and a beat',Q('#kKara [data-kk="cannon"]')]},
  kHumor:{play:['reads the joke of the day',Q('#kHumor [data-kh="daysay"]')],shuf:['jokes of a surprise kind',Q('#kHumor [data-kh="rnd"]')],jump:['the cannon picks a joke',Q('#kHumor [data-kh="cannon"]')]},
  kJump:{play:['builds the landing into the app',Q('#kJump [data-kj="build"]')],shuf:['flips every landing A↔Z',Q('#kJump [data-kj="flip"]')],next:['flops every landing to its neighbour',Q('#kJump [data-kj="flop"]')],jump:['jumps',Q('#kJump [data-kj="jump"]')]}};
 const trOf=id=>{ const t=TR[id]||{}; const out={}; Object.keys(D).forEach(k=>{ out[k]=t[k]||D[k][2]; }); return out; };
 function transportHTML(id){ const t=trOf(id); return '<div class="kpTr" role="toolbar" aria-label="Transport">'+Object.keys(D).map(k=>'<button type="button" data-kp="tr:'+k+'" title="'+esc(D[k][1]+': '+t[k][0])+'" data-noul><span>'+D[k][0]+'</span><small>'+D[k][1]+'</small></button>').join('')+'</div><div class="kpTrN">'+Object.keys(D).map(k=>'<b>'+D[k][0]+'</b> '+esc(t[k][0])).join(' · ')+'</div>'; }
 let curId='home';
 function openPanel(){ curId=cur(); let p=$('kPanel'); if(!p){ p=document.createElement('div'); p.id='kPanel'; p.setAttribute('role','dialog'); p.setAttribute('aria-label','Control panel'); document.body.appendChild(p); p.addEventListener('click',onPanel); }
  const ps=parts(curId); const G=GUIDES[curId]; const groups=[
   ...(G?[['📖 How this page works',G.map((g,i)=>['gd'+i,g[0]+' · '+g[1]]),true]]:[]),
   ['📍 Go to a part of this screen',ps.map((x,i)=>['p'+i,x[0]]),true],
   ['⧉ Float a part over the screen',ps.map((x,i)=>['f'+i,'⧉ '+x[0]])],
   ...(curId==='pad'?[['🎛 Beat Maker tools',[...document.querySelectorAll('#bmTabs button')].map((b,i)=>['bt'+i,b.textContent.trim()])]]:[]),
   ['📁 File',[['a:new','🆕 New'],['a:lib','📚 Library and starter shelf'],['save','💾 Save now'],['a:start','▶ Start / play'],['a:stop','■ Stop everything'],['a:close','✕ Close this screen']]],
   ['❓ Help',[['a:tut','🎓 Learn this screen (tutorial)'],['a:man','📖 Manual for this screen'],['a:tour','🗺 Tour this screen'],['vt','🌍 Virtual tour of the whole app'],['ask','🎙 Ask KAN-IN']]],
   ['👤 You',[['now','🕰 Fire this moment into the story'],['me','👤 My profile and daily reading'],['can','💥 Cannon control'],['a:tr','🔀 Translate or send this piece']]],
   ['🔊 Sound and screen',[['frz','❚❚ Freeze or release motion'],['fpad','🥁 Pads and keys, full screen'],['kara','🎤 Karaoke'],['pb:Touch','👆 Play by touch'],['pb:Keyboard','⌨ Play by keyboard'],['pb:Both','👆⌨ Play by both'],['km','⌨ Key map'],['rmt','📡 Remote control'],['net','🟢 Online or offline']]],
   ['🧭 Every screen',[['menu','☰ Open the main menu'],['g:pad','🥁 Beat Maker (lands on the pads)'],['g:keys','🎹 Keyboard'],['g:djSec','🎧 Virtual DJ'],['g:kBand','🎛 Story band'],['g:kSounds','🎻 Recorded sounds'],['g:swDock','✍ Songwriter & Poet'],['g:sbDock','🎞 Storyboard'],['g:musicDock','♪ Music'],['g:aivDock','🎬 Video'],['g:voiceDock','🎙 Voices'],['g:langDock','🌐 Language'],['g:zodDock','💞 Zodiac'],['g:omniDock','🧭 Compass'],['g:gamesDock','🎲 Games'],['g:opsHub','🎮 Game hub'],['g:kHumor','😂 Humor'],['g:kJump','💥 Cannon Jump Generator'],['g:kKara','🎤 Karaoke Live']]]];
  p.innerHTML='<div class="kpHead"><h3>⚙ '+esc(nameOf(curId))+' · control panel</h3><button type="button" class="kpX" data-kp="x" aria-label="Close the control panel" data-noul>✕</button></div>'+transportHTML(curId)+groups.map(([t,items,open])=>items.length?'<details'+(open?' open':'')+'><summary>'+esc(t)+' · '+items.length+'</summary><div class="kpL">'+items.map(([k,l])=>'<button type="button" data-kp="'+esc(k)+'" data-noul>'+esc(l)+'</button>').join('')+'</div></details>':'').join('');
  p._parts=ps; p.hidden=false; rail(); }
 function closePanel(){ const p=$('kPanel'); if(p) p.hidden=true; rail(); }
 function onPanel(e){ const b=e.target.closest('[data-kp]'); if(!b) return; const k=b.dataset.kp, p=$('kPanel'), sc=curId;
  if(k==='x') return closePanel();
  if(k.startsWith('tr:')){ const t=trOf(sc)[k.slice(3)]; try{ KAUDIO&&KAUDIO.gesture&&KAUDIO.gesture(); }catch(_){ } if(t) t[1](); return; }
  if(/^p\d+$/.test(k)){ const it=p._parts[+k.slice(1)]; closePanel(); if(it) land(it[1]); return; }
  if(/^gd\d+$/.test(k)) return;
  if(/^f\d+$/.test(k)){ const it=p._parts[+k.slice(1)]; closePanel(); if(it) FLOAT.part(it[1],it[0]); return; }
  if(/^bt\d+$/.test(k)){ const b2=[...document.querySelectorAll('#bmTabs button')][+k.slice(2)]; closePanel(); if(b2) b2.click(); return; }
  if(k==='now'){ const nb=[...document.querySelectorAll('.ocNow button')].find(x=>x.offsetParent!==null||true); closePanel(); if(nb) nb.click(); return; }
  if(k.startsWith('a:')){ const ka=k.slice(2); closePanel(); if(!clickAct(sc==='home'?'home':sc,ka)) clickAct('home',ka); return; }
  if(k.startsWith('g:')){ const id=k.slice(2); goTo(id); return; }
  if(k.startsWith('pb:')){ const w=k.slice(3); const btn=[...document.querySelectorAll('#inMode button')].find(x=>x.textContent.includes(w)&&!x.id); closePanel(); if(btn){ btn.click(); say('Play by '+w.toLowerCase()+'.'); } return; }
  closePanel();
  const C=id=>{ const x=$(id); if(x) x.click(); };
  ({save:()=>{ try{ const k2={pad:'beat',djSec:'dj',swDock:'song',aivDock:'video',mutDock:'mutation',langDock:'translation',zodDock:'chart',omniDock:'compass',voiceDock:'voices',musicDock:'music',craftDock:'craft'}[sc]; if(k2){ FILES.save(k2); say('Saved in your Library.'); } else { STORYLIB.autosave&&STORYLIB.autosave(); say('Your story is saved in the Library.'); } }catch(_){ say('Saved.'); } },
   vt:()=>clickAct('home','tour'), ask:()=>C('askBtn'), me:()=>{ try{ KSTARS.open(); }catch(_){ } }, can:()=>{ try{ KCANNON.open(); }catch(_){ } }, frz:()=>C('kFreeze'), fpad:()=>C('imPad'), kara:karaoke, km:()=>C('kmOpen'), rmt:()=>C('kdRemote'), net:()=>C('kdNet'),
   menu:()=>{ const m=$('lpMenu'); if(m) m.click(); }}[k]||(()=>{}))(); }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'){ const p=$('kPanel'); if(p&&!p.hidden){ e.stopImmediatePropagation(); closePanel(); } } },true);
 /* the home page opens clean: the menu waits behind ☰ at the bottom of the rail */
 try{ const gh=window.GOHOME; if(gh&&!gh.__krail){ const w=function(){ const r=gh.apply(this,arguments); setTimeout(()=>{ try{ if(!window.__kMenuWanted) LAUNCHPAD.fold(); }catch(_){ } },60); return r; }; w.__krail=1; window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#lpMenu')){ window.__kMenuWanted=true; closePanel(); setTimeout(()=>{ window.__kMenuWanted=false; },900); } },true);
 /* a Keyboard link in the main menu, beside the Beat Maker */
 function menuLinks(){ const t=$('tourTab'); if(!t||$('ttKeys')) return; const mk=(id,txt,fn,order)=>{ const b=document.createElement('button'); b.type='button'; b.id=id; b.className='ttMusic'; b.textContent=txt; b.setAttribute('data-noul',''); b.style.order=order; b.addEventListener('click',e=>{ e.stopPropagation(); fn(); setTimeout(()=>{ try{ LAUNCHPAD.fold(); }catch(_){ } },60); }); t.appendChild(b); };
  mk('ttKeys','🎹 Keyboard',()=>goTo('keys'),'202'); mk('ttKara','🎤 Karaoke',karaoke,'209'); }
 /* the main menu opens only from ☰ Menu (or while a guided tour shows it); nothing else pops it over the page */
 let allowAt=0; window.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#lpMenu,#ttMenuOpen')) allowAt=Date.now(); },true);
 const tourBusy=()=>{ const c=$('tourCard'), g=$('gtCard'); return shown(c)||shown(g); };
 function guardMenu(){ const t=$('tourTab'); if(!t||t.__kguard) return; t.__kguard=1; new MutationObserver(()=>{ if(!t.classList.contains('lpc')&&Date.now()-allowAt>1500&&!tourBusy()&&!document.body.classList.contains('gated')){ try{ LAUNCHPAD.fold(); }catch(_){ } } }).observe(t,{attributes:true,attributeFilter:['class']}); try{ if(window.LAUNCH==='open'&&!tourBusy()&&!document.body.classList.contains('gated')) LAUNCHPAD.fold(); }catch(_){ } }
 guardMenu(); setInterval(()=>{ guardMenu(); try{ const t=$('tourTab'); if(t&&window.LAUNCH==='open'&&Date.now()-allowAt>1500&&!tourBusy()&&!document.body.classList.contains('gated')&&!t.matches(':hover')&&!t.contains(document.activeElement)){} }catch(_){ } },1500);

 /* ---------- FLOATING INSTRUMENTS: the base stays put, the tools float over it ---------- */
 const fcss=document.createElement('style'); fcss.textContent=`
.kFloat{position:fixed!important;z-index:var(--fz,70)!important;left:var(--fx,8px)!important;top:var(--fy,70px)!important;width:var(--fw,420px)!important;max-width:calc(100vw - var(--kRailW) - 8px)!important;height:var(--fh,auto)!important;max-height:calc(100vh - 16px)!important;overflow:auto!important;background:#0d1036!important;border:2px solid #ffe94a!important;border-radius:12px!important;box-shadow:0 18px 44px rgba(0,0,0,.65)!important;resize:both!important;margin:0!important;padding:0 8px 8px!important;box-sizing:border-box!important;transform:none!important}
.kFloat.kMin{height:auto!important;max-height:46px!important;overflow:hidden!important;resize:none!important}
.kFOff{display:none!important}
.kFloat.pmain{grid-template-columns:minmax(0,1fr)!important}
.kFloat > *{min-width:0!important;max-width:100%!important;box-sizing:border-box}
.kFHead b{min-width:0}
.kFHead{position:sticky;top:0;display:flex;align-items:center;gap:6px;padding:6px;margin:0 -8px 6px;background:#1a1f6e;cursor:move;touch-action:none;z-index:5;border-radius:10px 10px 0 0;user-select:none;-webkit-user-select:none}
.kFloat:not(.kFOn) > .kFHead{display:none}
.kFHead b{flex:1;font:700 14px/1.2 system-ui,sans-serif;color:#ffe94a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kFHead button{min-width:40px;min-height:36px;padding:0 8px;border-radius:8px;font-size:16px}
html body #bmTabs,html body .kHas .ocNow{display:none!important}
html body #pad #bbBar{flex-wrap:wrap!important;max-width:100%!important}
html body #pad #crPats,html body #pad #crSec .kgrid,html body #pad #crVel{max-width:100%;overflow-x:auto}
html body #pad #crSec{max-width:100%;overflow-x:auto;box-sizing:border-box}
html body #rDock#rDock :is(#kdIPads,#kdIKeys,#kdIDJ){order:4!important;display:flex!important}
html body #rDock#rDock :is(#kdIPads,#kdIKeys,#kdIDJ).on{background:#ffe94a!important}html body #rDock#rDock :is(#kdIPads,#kdIKeys,#kdIDJ).on::before,html body #rDock#rDock :is(#kdIPads,#kdIKeys,#kdIDJ).on::after{color:#14163a!important}
html body #rDock#rDock :is(#kdIPads,#kdIKeys,#kdIDJ)[hidden]{display:none!important}`; document.head.appendChild(fcss);
 const INST={pads:{get:()=>document.querySelector('#pad .pmain'),t:'🥁 Beat machine · 16 pads',i:'🥁',l:'Pads'},keys:{get:()=>$('kbTop'),t:'🎹 MIDI keyboard',i:'🎹',l:'Keys'},dj:{get:()=>$('djSec'),t:'🎧 Virtual DJ',i:'🎧',l:'DJ'}};
 const GEN={}; let fz=70;
 const isPhone=()=>innerWidth<=760;
 function geo(key){ const W=innerWidth-(isPhone()?58:76), H=innerHeight; const g=(()=>{ try{ return JSON.parse(localStorage.getItem('kanin-float-'+key)||'null'); }catch(_){ return null; } })(); if(g&&g.x<W-40&&g.y<H-40) return g;
  if(isPhone()) return {x:4,y:key==='keys'?Math.round(H*0.42):56,w:W-8,h:null};
  return ({pads:{x:Math.round(W*0.42),y:70,w:Math.min(520,Math.round(W*0.55)),h:null},keys:{x:16,y:Math.round(H*0.48),w:Math.min(640,Math.round(W*0.6)),h:null},dj:{x:Math.round(W*0.2),y:90,w:Math.min(720,Math.round(W*0.7)),h:null}})[key]||{x:Math.round(W*0.25),y:80,w:Math.min(560,Math.round(W*0.6)),h:null}; }
 const topMin=()=>{ const b=document.getElementById('bbBar'); const pad=document.getElementById('pad'); if(!b||!pad||!pad.classList.contains('on')||!b.getClientRects().length) return 0; return Math.max(0,Math.round(b.getBoundingClientRect().bottom)+4); };
 function place(el,g){ g.y=Math.max(g.y,topMin()); el.style.setProperty('--fx',Math.round(g.x)+'px'); el.style.setProperty('--fy',Math.round(g.y)+'px'); el.style.setProperty('--fw',Math.round(g.w)+'px'); if(g.h) el.style.setProperty('--fh',Math.round(g.h)+'px'); else el.style.removeProperty('--fh'); }
 function save(key,el){ const r=el.getBoundingClientRect(); try{ localStorage.setItem('kanin-float-'+key,JSON.stringify({x:r.left,y:r.top,w:r.width,h:el.classList.contains('kMin')?null:r.height})); }catch(_){ } }
 function front(el){ fz+=1; el.style.setProperty('--fz',String(el.parentElement===document.body?9600+fz:fz)); }
 function head(key,el,title,generic){ let hd=el.querySelector(':scope > .kFHead'); if(hd) return hd; hd=document.createElement('div'); hd.className='kFHead'; hd.innerHTML='<b></b><button type="button" data-fh="min" aria-label="Shrink or grow" data-noul>▁</button><button type="button" data-fh="x" aria-label="'+(generic?'Put it back in the page':'Put it away')+'" data-noul>'+(generic?'⤓':'✕')+'</button>'; hd.querySelector('b').textContent=title; el.insertBefore(hd,el.firstChild);
  let drag=null; hd.addEventListener('pointerdown',e=>{ if(e.target.closest('button')) return; front(el); const r=el.getBoundingClientRect(); drag={dx:e.clientX-r.left,dy:e.clientY-r.top}; try{ hd.setPointerCapture(e.pointerId); }catch(_){ } e.preventDefault(); });
  hd.addEventListener('pointermove',e=>{ if(!drag) return; const W=innerWidth-(isPhone()?58:76); const x=Math.max(0,Math.min(W-60,e.clientX-drag.dx)), y=Math.max(topMin(),Math.min(innerHeight-44,e.clientY-drag.dy)); el.style.setProperty('--fx',x+'px'); el.style.setProperty('--fy',y+'px'); });
  const end=()=>{ if(drag){ drag=null; save(key,el); } }; hd.addEventListener('pointerup',end); hd.addEventListener('pointercancel',end);
  hd.addEventListener('click',e=>{ const b=e.target.closest('[data-fh]'); if(!b) return; e.stopPropagation(); if(b.dataset.fh==='min'){ el.classList.toggle('kMin'); save(key,el); } else FLOAT.close(key); });
  el.addEventListener('pointerdown',()=>front(el),true); try{ new ResizeObserver(()=>{ if(el.classList.contains('kFOn')&&!drag) clearTimeout(el.__rs), el.__rs=setTimeout(()=>save(key,el),400); }).observe(el); }catch(_){ } return hd; }
 const FLOAT={
  open(key){ const I=INST[key]||GEN[key]; if(!I) return; const el=I.get(); if(!el) return; if(key==='keys'){ const tb=$('trBar'); if(tb&&tb.parentElement!==el) el.appendChild(tb); } head(key,el,I.t,!!GEN[key]); el.classList.add('kFloat','kFOn'); el.classList.remove('kFOff','kMin'); place(el,geo(key)); front(el); railInst(); },
  close(key){ const I=INST[key]||GEN[key]; if(!I) return; const el=I.get(); if(!el) return; if(GEN[key]){ el.classList.remove('kFloat','kFOn','kMin'); const hd=el.querySelector(':scope > .kFHead'); if(hd) hd.remove(); delete GEN[key]; } else { el.classList.add('kFOff'); el.classList.remove('kFOn'); } railInst(); },
  toggle(key){ const I=INST[key]; const el=I&&I.get(); if(el&&el.classList.contains('kFOn')&&!el.classList.contains('kFOff')) FLOAT.close(key); else FLOAT.open(key); },
  add(key,def){ INST[key]=def; },
  isOpen(key){ const I=INST[key]||GEN[key]; const el=I&&I.get(); return !!(el&&el.classList.contains('kFOn')&&!el.classList.contains('kFOff')); },
  part(target,title){ const el=typeof target==='string'?T(target):target; if(!el) return; const fk=floatOf(el); if(fk) return FLOAT.open(fk); const root=$(cur())||document.querySelector('.wrap'); let blk=el.closest('.bmSec,section,details,[id$=Wrap],[id$=Sec],[id$=Box],.card')||el.parentElement; if(!blk||blk===root||blk.contains(root)||blk.classList.contains('kHas')) blk=el.parentElement; if(!blk||blk===root) return say('That part cannot float here.'); const key='g'+(blk.id||Math.random().toString(36).slice(2,7)); GEN[key]={get:()=>blk,t:'⧉ '+String(title||'').replace(/^⧉ /,'')}; FLOAT.open(key); say('Floating. Drag it by its top bar; ⤓ puts it back in the page.'); }};
 function floatOf(el){ for(const k of Object.keys(INST)){ const f=INST[k].get(); if(f&&(f===el||f.contains(el))) return k; } return null; }
 /* the Beat Maker's base: the transport on top, then the sequencer, then the mixing board; the instruments float over them */
 function beatBase(){ const cr=$('crSec'); if(!cr) return; const pin=cr.parentElement; { const kids=[...pin.children]; const mh=kids.find(c=>c.tagName==='H4'&&c.textContent.trim().startsWith('🎚 Mixer')); const pm=$('padMixer'); const pmain=pin.querySelector(':scope > .pmain'); if(mh&&pm&&pmain){ const grp=[]; let n=mh; while(n){ grp.push(n); if(n===pm) break; n=n.nextElementSibling; } const pt=pin.querySelector(':scope > .ptop'), mpc=$('mpcSec'); if(pt) grp.push(pt); if(mpc&&mpc.parentElement===pin) grp.push(mpc); let ok=true; for(let i=0;i<grp.length;i++){ if((grp[i+1]||pmain)!==grp[i].nextElementSibling){ ok=false; break; } } if(!ok) grp.forEach(x=>pin.insertBefore(x,pmain)); } }
  ['keys','dj'].forEach(k=>{ const el=INST[k].get(); if(el&&!el.classList.contains('kFOn')) el.classList.add('kFloat','kFOff'); }); if(!FLOAT.isOpen('pads')) FLOAT.open('pads'); const sc=$('pad'); if(sc&&!(want&&want!=='#padGrid'&&Date.now()-wantAt<2500)) sc.scrollTop=0; }
 function railInst(){ const onPad=cur()==='pad'||cur()==='djSec'; [['pads','kdIPads'],['keys','kdIKeys'],['dj','kdIDJ']].forEach(([k,id])=>{ railBtn(id,INST[k].i,INST[k].l,'Show or hide the '+INST[k].t.replace(/^\S+ /,''),()=>{ if(cur()!=='pad') goTo('pad'); setTimeout(()=>FLOAT.toggle(k),cur()==='pad'?0:900); }); const b=$(id); if(b){ b.hidden=!onPad; b.classList.toggle('on',FLOAT.isOpen(k)); } }); }
 /* the transport bar's Pads and Keys buttons call the floating instruments */
 document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('#bbBar button'); if(!b) return; const t=b.textContent; const k=/Pads/.test(t)?'pads':/Keys/.test(t)?'keys':null; if(k){ e.stopImmediatePropagation(); e.preventDefault(); FLOAT.toggle(k); } },true);
 rail(); menuLinks(); setInterval(()=>{ rail(); menuLinks(); try{ railInst(); }catch(_){ } },1200);
 window.KRAIL={land,goTo,openPanel,closePanel,cur,karaoke,parts,FLOAT,beatBase};
})();
