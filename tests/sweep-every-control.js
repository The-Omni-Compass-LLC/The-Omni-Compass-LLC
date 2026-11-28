// v260 referee sweep: open every screen, press every button, turn every dropdown, slider and switch, on a laptop or a phone.
// Records: page errors, controls with no visible effect, controls covered by something else, controls too small to tap,
// controls off the screen's edge, outside links without a new tab / noopener, and the page scrolling sideways.
// usage: SWEEP_URL=<app url> node sweep-every-control.js laptop|phone name1,name2,... outdir
const {chromium,devices}=require('playwright'); const fs=require('fs');
const MODE=process.argv[2]||'laptop', ONLY=(process.argv[3]||'').split(',').filter(Boolean), OUT=process.argv[4]||'sweep10';
const M=l=>`(()=>{ const m=document.getElementById('lpMenu'); if(m) m.click(); return new Promise(r=>setTimeout(()=>{ const x=[...document.querySelectorAll('#tourTab button')].find(b=>b.textContent.trim().startsWith(${JSON.stringify(l)})); if(x) x.click(); r(!!x); },600)); })()`;
const SCREENS=[
 ['home',"KRAIL.goTo('home')",'#rDock'],
 ['menu',"(()=>{ const t=document.getElementById('tourTab'); if(!(t&&t.getClientRects().length&&!t.closest('[hidden]'))) document.getElementById('lpMenu').click(); })()",'#tourTab'],
 ['tools',"document.getElementById('kToolsBtn').click()",'#kToolsPop'],
 ['find',"document.getElementById('kdFind').click()",'#kFind'],
 ['keys',"KKEYS.show()",'#kKeysPop'],
 ['audit',"KAUDIT.open()",'#kAudit'],
 ['owner',"KOWNER.open()",'#kOwner'],
 ['vg',"KVG.open()",'#kVG'],
 ['proj',"KPROJ.open()",'#kProj'],
 ['acct',"KACCT.open()",'#kAcct'],
 ['social',"KSOCIAL.open()",'#kSocial'],
 ['aiv',M('🎬 Video studio'),'#aivDock'],
 ['ai',"KAI.open()",'#kAI'],
 ['easel',"KEASEL.open()",'#kEasel'],
 ['pad',"PADSTUDIO.open()",'#pad'],
 ['kara',"KKARA.open()",'#kKara'],
 ['dance',"KDANCE.open('now')",'#kDance'],
 ['door',"KDOOR.open()",'#kDoor'],
 ['cbeat',"KCBEAT.open()",'#kCBeat'],
 ['music',M('🎵 Music'),'#musicDock'],
 ['humor',"KHUMOR.open()",'#kHumor'],
 ['zod',M('♈ LuvMyZodiac'),'#zodDock'],
 ['zring',"KZRING.page()",'#kZRingPage'],
 ['omni',M('🧭 Omni-Compass'),'#omniDock'],
 ['story',M('📖 Make a story'),'.wrap'],
 ['lock',"KLOCK.open()",'#kLock'],
 ['know',"KKNOW.open()",'#kKnow'],
 ['news',"KNEWS.open()",'#kNews'],
 ['relig',"KRELIG.open()",'#kRelig'],
 ['religx',"KRELIGX.open()",'#kReligX'],
 ['market',"KMARKET.open()",'#kMarket'],
 ['sports',"KSPORTS.open()",'#kSports'],
 ['services',"KSERVICES.open()",'#kServices'],
 ['legal',"KLEGAL.open()",'#kLegal'],
 ['jump',"KJUMP.open()",'#kJump'],
 ['games',"GAMES.open()",'#gamesDock'],
 ['sw',"SONGWRITER.open()",'#swDock'],
 ['sbp',"SBP.open()",'#sbp'],
 ['voice',M('🎙 Voices'),'#voiceDock'],
 ['lang',M('🌐 Language'),'#langDock'],
 ['lay',M('🧭 Layers'),'#layDock'],
 ['craft',M('🛠 Craft'),'#craftDock'],
 ['mut',M('🧬 Mutate'),'#mutDock'],
 ['map',M('🗺 All sections'),'#mapDock'],
 ['ask',M('❓ Ask'),'#askDock'],
 ['recipes',M('🍳 Recipes'),''],
 ['keyboards',M('⌨ Keyboards'),''],
 ['storylib',M('🗂 Story library'),''],
 ['tac',"TAC.open()",'#tacMenu'],
 ['hub',"OPSHUB.open()",'#opsHub'],
 ['deadtest',"(()=>{ KKEYS.show(); const i=document.querySelector('#kKeysPop .kkIn'); if(!i.querySelector('.dt')){ const b=document.createElement('button'); b.className='dt'; b.textContent='DEADTEST'; i.appendChild(b); const c=document.createElement('button'); c.className='dt'; c.textContent='LIVETEST'; c.onclick=()=>{ c.textContent='LIVE OK'; }; i.appendChild(c); } })()",'#kKeysPop'],
];
const CLEAN=`(()=>{ const t=f=>{ try{ f(); }catch(e){} };
 t(()=>{ if(KLEVEL.get()!=='pro') KLEVEL.set('pro'); }); t(()=>KAUDIO.stopAll()); t(()=>{ if(PADSTUDIO.playing) PADSTUDIO.stop(); }); t(()=>KTOUR.stop()); t(()=>GUIDE.end&&GUIDE.end()); t(()=>speechSynthesis.cancel());
 t(()=>document.fullscreenElement&&document.exitFullscreen()); t(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; document.body.classList.remove('gated'); }); })()`;
const HOME=`(()=>{ const t=f=>{ try{ f(); }catch(e){} }; t(()=>KBEAT.closeAll()); t(()=>GOHOME()); t(()=>KRAIL.goTo('home'));
 ['kLegal','kServices','kSports','kNews','kMarket','kRelig','kReligX','kKnow','kAcct','kSndSheet','kFind','kAudit','kKeysPop','kToolsPop','kLangPop','kZRingPage','kDance','kDoor'].forEach(id=>{ const x=document.getElementById(id); if(x) x.hidden=true; }); })()`;
const TOP=`(sel)=>{ const vis=el=>{ const s=getComputedStyle(el),r=el.getBoundingClientRect(); return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0; };
 for(const q of (sel||'').split(',').filter(Boolean)){ const e=document.querySelector(q); if(e&&vis(e)) return q; }
 const tops=[...document.querySelectorAll('body > *, body > * > [id]')].filter(el=>{ const s=getComputedStyle(el); const r=el.getBoundingClientRect(); return el.id&&(s.position==='fixed'||s.position==='absolute')&&vis(el)&&r.height>200&&r.width>260&&!/bgfx|flashbang|kShotCv|tourRing|rDock|kPanelStrip|padBg|kRail|ktHud/.test(el.id); });
 const top=tops.sort((a,b)=>(+getComputedStyle(b).zIndex||0)-(+getComputedStyle(a).zIndex||0))[0]; return top?'#'+top.id:''; }`;
(async()=>{ fs.mkdirSync(OUT,{recursive:true});
 const b=await chromium.launch({args:['--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream','--autoplay-policy=no-user-gesture-required']});
 let ctx,p,errs=[];
 const fresh=async()=>{ try{ if(ctx) await ctx.close(); }catch(_){ }
 ctx=await b.newContext(MODE==='phone'?{...devices['iPhone 13'],permissions:['camera','microphone']}:{viewport:{width:1440,height:900},permissions:['camera','microphone']});
 p=await ctx.newPage(); errs=[];
 p.on('pageerror',e=>errs.push('ERROR '+(e.message||'').slice(0,160)+' @'+((e.stack||'').split('\n')[1]||'').trim().replace(/https?:\/\/[^ )]*\//,'').slice(0,80)));
 p.on('console',m=>{ if(m.type()==='error'&&!/favicon|net::|Failed to load resource|ERR_|AudioContext was not allowed|NotAllowedError|play\(\) request|permission|Content Security|CORS|fetch/i.test(m.text())) errs.push('CONSOLE '+m.text().slice(0,160)); });
 p.on('dialog',d=>d.dismiss().catch(()=>{})); p.on('popup',pp=>pp.close().catch(()=>{}));
 p.on('filechooser',()=>{ });
 await p.addInitScript(()=>{ window.__fx=0; window.__cv=0; window.__ftl=[]; window.__log=[]; window.__rootEl=null; const bump=()=>{ window.__fx++; try{ const st=(new Error().stack||'').split('\n')[3]||''; window.__ftl.push(st.trim().slice(0,90)); if(window.__ftl.length>50) window.__ftl.shift(); }catch(_){ } }; window.open=()=>{ bump(); return null; }; window.__mut=0;
  const start=()=>{ new MutationObserver(m=>{ for(const x of m){ window.__mut++; if(window.__log.length>=20000) continue; const t=x.target.nodeType===3?x.target.parentNode:x.target; let k; if(t===document.body&&x.type==='childList'){ const n=x.addedNodes[0]||x.removedNodes[0]||{}; k='body>'+(n.id||n.className||n.nodeName); } else { const h=t&&t.closest?t.closest('[id]'):null; k=(h?h.id:'doc')+(x.type==='attributes'?'@'+x.attributeName:''); } window.__log.push({t,y:x.type,k,inR:!!(window.__rootEl&&window.__rootEl.contains(t))}); } }).observe(document,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['hidden','open','disabled','aria-pressed','aria-selected','value','src','href','data-on','class','style']}); };
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',start); else start();
  const wrap=(o,k,f2)=>{ try{ const f=o[k]; o[k]=function(){ (f2||bump)(); return f.apply(this,arguments); }; }catch(e){} };
  wrap(AudioScheduledSourceNode.prototype,'start'); wrap(HTMLAnchorElement.prototype,'click'); wrap(HTMLInputElement.prototype,'click'); wrap(URL,'createObjectURL'); wrap(HTMLMediaElement.prototype,'play'); wrap(HTMLMediaElement.prototype,'pause');
  wrap(Element.prototype,'requestFullscreen'); wrap(Storage.prototype,'setItem'); try{ wrap(speechSynthesis,'speak'); }catch(e){} try{ if(navigator.clipboard) wrap(navigator.clipboard,'writeText'); }catch(e){} wrap(document,'execCommand');
  try{ wrap(navigator.mediaDevices,'getUserMedia'); }catch(e){} wrap(window,'fetch'); window.__sc=0; addEventListener('scroll',()=>{ window.__sc++; },true);
  window.__ctl=(Rt)=>[...Rt.querySelectorAll('button,select,input[type=range],input[type=checkbox],input[type=radio],input[type=number],input[type=color],[role=button]:not(button)')].filter(el=>{ const s=getComputedStyle(el),r=el.getBoundingClientRect(); return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0&&!el.closest('[hidden]')&&!el.disabled&&!/sign out|log out|sign-out/i.test(el.textContent||''); });
  window.__sig=el=>el.tagName+'|'+(el.type||'')+'|'+(el.textContent||el.title||el.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ').slice(0,48);
  window.__shot=()=>{ const R=window.__rootEl; if(!R||!R.isConnected) return ''; let h=0; const t=(R.innerText||'')+'|'+[...R.querySelectorAll('input,select,textarea')].map(e=>e.type==='checkbox'||e.type==='radio'?e.checked:e.value).join(',')+'|'+R.querySelectorAll('.on,.active,.sel,[aria-pressed=true],[aria-selected=true],[aria-checked=true]').length+'|'+R.querySelectorAll('[hidden]').length; for(let i=0;i<t.length;i++){ h=(h*31+t.charCodeAt(i))|0; } return t.length+':'+h; };
  window.__m0=()=>{ __log.length=0; __ftl.length=0; __cvs.clear(); window.__shot0=__shot(); window.__snap={t:(document.getElementById('toast')||{}).textContent,a:!!(window.PADSTUDIO&&PADSTUDIO.playing),h:location.hash,sc:__sc}; };
  window.__mIdle=()=>{ window.__shot1=__shot(); window.__shotNoisy=window.__shot1!==window.__shot0; window.__noise=new Set(__log.map(x=>x.k)); window.__noiseP=window.__noiseP||new Set(); __log.forEach(x=>{ if(!x.inR&&!/^body>/.test(x.k)) __noiseP.add(x.k); }); window.__noiseF=new Set(__ftl); window.__noiseCv=new Set(__cvs); window.__scIdle=__sc-__snap.sc; __log.length=0; __ftl.length=0; __cvs.clear(); window.__sc1=__sc; };
  const inNoise=x=>!x.t||__noise.has(x.k)||(window.__noiseP&&__noiseP.has(x.k));
  window.__mAfter=(ctrl,root)=>{ const R=document.querySelector(root); const T=new Set(); for(const x of __log){ if(inNoise(x)) continue; if(x.t===ctrl&&x.y==='attributes') continue; if(window.__dummy&&x.t===window.__dummy) continue; T.add(x.k); }
   return {T:[...T],F:[...new Set(__ftl)].filter(l=>!__noiseF.has(l)),C:[...__cvs].filter(c=>!__noiseCv.has(c)),gone:!(R&&R.getClientRects().length&&!R.closest('[hidden]')),snap:(document.getElementById('toast')||{}).textContent!==__snap.t||!!(window.PADSTUDIO&&PADSTUDIO.playing)!==__snap.a||location.hash!==__snap.h,sc:(__sc-__sc1)>__scIdle*4+1}; };
  window.__calib=(root)=>{ const R=document.querySelector(root); const host=R.querySelector('button')?R.querySelector('button').parentElement:R; const d=document.createElement('button'); d.type='button'; d.textContent='·'; d.style.cssText='min-width:30px;min-height:30px'; host.appendChild(d); window.__dummy=d; return true; };
  window.__calibEnd=(r)=>{ window.__calT=window.__calT||new Set(); r.T.forEach(k=>__calT.add(k)); window.__calF=window.__calF||new Set(); r.F.forEach(k=>__calF.add(k)); window.__calC=new Set(r.C); try{ window.__dummy.remove(); }catch(_){ } };
  window.__effect=(r)=>{ const shotChanged=!window.__shotNoisy&&__shot()!==window.__shot1; const T=r.T.filter(t=>!__calT.has(t)), F=r.F.filter(l=>!__calF.has(l)), C=r.C.filter(c=>!__calC.has(c)); return {did:r.gone||r.snap||r.sc||shotChanged||T.length>0||F.length>0||C.length>0,why:r.gone?'closed':r.snap?'toast/beat/address':shotChanged&&!T.length?'screen text or state changed':r.sc?'scrolled':T.length?'changed '+T.slice(0,3).join(', ')+(T.length>3?' +'+(T.length-3):''):F.length?'called '+F[0].replace(/https?:\/\/[^ )]*\//,''):C.length?'drew':''}; };
  window.__find=(root,sig,n)=>{ const Rt=document.querySelector(root); if(!Rt) return null; let k=0; for(const el of window.__ctl(Rt)){ if(window.__sig(el)===sig){ if(k===n) return el; k++; } } return null; };
  window.__cvs=new Set(); ['fillRect','drawImage','fillText','stroke','fill','putImageData'].forEach(k=>{ const P=CanvasRenderingContext2D.prototype, f=P[k]; P[k]=function(){ window.__cv++; if(window.__cvs.size<400) window.__cvs.add(this.canvas); return f.apply(this,arguments); }; }); });
 await p.goto(process.env.SWEEP_URL||'http://localhost:8771/pub6/ptest.html',{waitUntil:'load'}); await p.waitForTimeout(4500);
 await p.evaluate(()=>{ try{ sessionStorage.setItem('kanin-agree-s','1'); }catch(_){ } }); await p.evaluate(CLEAN);
 };
 const list=ONLY.length?SCREENS.filter(s=>ONLY.includes(s[0])):SCREENS.filter(s=>s[0]!=='deadtest');
 for(const [name,open,sel] of list){ const T0=Date.now(); try{ await fresh(); }catch(e){ console.log(MODE,name,'COULD NOT LOAD',e.message.slice(0,100)); continue; }
 try{
  let root='';
  const reopen=async()=>{ await p.evaluate(CLEAN); await p.evaluate(HOME); await p.waitForTimeout(250); try{ await p.evaluate(open); }catch(e){ errs.push('OPEN '+e.message.slice(0,120)); } await p.waitForTimeout(1100); { let nr=await p.evaluate(`(${TOP})(${JSON.stringify(sel)})`); if(!nr){ await p.waitForTimeout(900); nr=await p.evaluate(`(${TOP})(${JSON.stringify(sel)})`); } root=nr||root; } await p.evaluate(r=>{ window.__root=r; window.__rootEl=r?document.querySelector(r):null; },root); return root; };
  errs=[]; await reopen(); const openErrs=errs.slice();
  const R={screen:name,mode:MODE,root,openErrors:openErrs,controls:0,pressed:0,errors:[],dead:[],covered:[],small:[],offEdge:[],links:{n:0,bad:[]},wide:false,secs:0};
  if(!root){ R.note='screen did not open'; fs.writeFileSync(`${OUT}/${MODE}-${name}.json`,JSON.stringify(R,null,1)); console.log(MODE,name,'DID NOT OPEN',openErrs.join(' | ')); continue; }
  const tag=()=>p.evaluate(([root])=>{ const Rt=document.querySelector(root); if(!Rt) return []; const seen={}; return __ctl(Rt).map(el=>{ const g=__sig(el); const n=seen[g]=(seen[g]===undefined?0:seen[g]+1); el.dataset.sw2=1; return {sig:g,n,t:g.split('|')[2]||el.tagName,tag:el.tagName,type:el.type||''}; }); },[root]);
  let items=await tag(); if(!items.length){ await p.waitForTimeout(2000); items=await tag(); } R.controls=items.length;
  const CAL=async()=>{ await p.evaluate(r=>__calib(r),root); await p.evaluate(()=>__m0()); await p.waitForTimeout(250); await p.evaluate(()=>__mIdle()); await p.evaluate(()=>window.__dummy.click()); await p.waitForTimeout(450); const r=await p.evaluate(rt=>{ const x=__mAfter(window.__dummy,rt); __calibEnd(x); return {T:x.T.length,F:x.F,C:x.C.length}; },root); return r; };
  await p.evaluate(()=>{ window.__noiseP=new Set(); window.__calT=new Set(); window.__calF=new Set(); });
  for(let w=0;w<4;w++){ await p.evaluate(()=>__m0()); await p.waitForTimeout(450); await p.evaluate(()=>__mIdle()); }
  R.calibration=await CAL(); await CAL();
  const lay=await p.evaluate(([root,phone])=>{ const Rt=document.querySelector(root); const W=innerWidth, o=[], sm=[]; Rt.querySelectorAll('[data-sw2]').forEach(el=>{ const r=el.getBoundingClientRect(); if(!r.width) return; const t=(el.textContent||el.title||el.tagName).trim().slice(0,32); if(r.right>W+1||r.left<-1) o.push(t+' x'+Math.round(r.left)+'–'+Math.round(r.right)); if(phone&&(r.width<28||r.height<28)&&el.tagName!=='INPUT') sm.push(t+' '+Math.round(r.width)+'×'+Math.round(r.height)); });
   const A=[...Rt.querySelectorAll('a[href^="http"]')]; const bad=A.filter(a=>a.target!=='_blank'||!/noopener/.test(a.rel||'')||!/^https:/.test(a.href)).map(a=>(a.textContent||'').trim().slice(0,30)+' '+a.href.slice(0,60));
   return {o,sm,links:A.length,bad,wide:document.documentElement.scrollWidth>innerWidth+2}; },[root,MODE==='phone']);
  R.offEdge=lay.o.slice(0,40); R.small=lay.sm.slice(0,60); R.smallCount=lay.sm.length; R.links={n:lay.links,bad:lay.bad.slice(0,20),badCount:lay.bad.length}; R.wide=lay.wide;
  const per={}; R.repeats=0; for(const it of items){ per[it.sig]=(per[it.sig]||0)+1; if(per[it.sig]>3){ R.repeats++; continue; } if(Date.now()-T0>(+process.env.SWEEP_MIN||40)*60*1000){ R.note="stopped at the time limit for one screen"; break; }
   const FIND=`(()=>{ const e=__find(${JSON.stringify(root)},${JSON.stringify(it.sig)},${it.n}); window.__cur=e; return !!e; })()`;
   let here=await p.evaluate(FIND);
   if(!here){ await reopen(); await CAL(); here=await p.evaluate(`(()=>{ const e=__find(${JSON.stringify(root)},${JSON.stringify(it.sig)},${it.n}); window.__cur=e; return !!e; })()`); if(!here){ R.skipped=(R.skipped||0)+1; (R.skippedList=R.skippedList||[]).push(it.t); continue; } }
   const HIT=()=>p.evaluate(()=>{ const e=window.__cur; e.scrollIntoView({block:'center',inline:'nearest'}); const r=e.getBoundingClientRect(); if(r.bottom<0||r.top>innerHeight) return 'off the screen'; const t=document.elementFromPoint(Math.min(innerWidth-1,Math.max(0,r.left+r.width/2)),Math.min(innerHeight-1,Math.max(0,r.top+r.height/2))); if(!t) return 'nothing'; if(e===t||e.contains(t)||t.contains(e)||(e.tagName==='INPUT'&&e.labels&&[...e.labels].some(l=>l.contains(t)))) return 'ok'; return (t.id?'#'+t.id:t.tagName.toLowerCase()+(t.className&&typeof t.className==='string'?'.'+t.className.split(' ')[0]:''))+' “'+(t.textContent||'').trim().slice(0,24)+'”'; });
   let hit=await HIT();
   if(hit!=='ok'){ await reopen(); await CAL(); const ok2=await p.evaluate(`(()=>{ const e=__find(${JSON.stringify(root)},${JSON.stringify(it.sig)},${it.n}); window.__cur=e; return !!e; })()`); if(ok2) hit=await HIT(); }
   if(hit!=='ok') R.covered.push(it.t+' ← '+hit);
   await p.waitForTimeout(80); errs=[]; await p.evaluate(()=>__m0()); await p.waitForTimeout(250); await p.evaluate(()=>__mIdle());
   try{ await p.evaluate(()=>{ const e=window.__cur; const fire=n=>e.dispatchEvent(new Event(n,{bubbles:true}));
     if(e.tagName==='SELECT'){ if(e.options.length>1){ e.selectedIndex=(e.selectedIndex+1)%e.options.length; } fire('input'); fire('change'); }
     else if(e.tagName==='INPUT'&&(e.type==='range'||e.type==='number')){ const mn=+e.min||0, mx=e.max===''?mn+100:+e.max; const v=+e.value; const nv=v<(mn+mx)/2?Math.min(mx,v+(mx-mn)/3):Math.max(mn,v-(mx-mn)/3); e.value=String(e.step&&e.step!=='any'?Math.round(nv/(+e.step))*(+e.step):nv); fire('input'); fire('change'); }
     else if(e.tagName==='INPUT'&&e.type==='color'){ e.value=e.value==='#ff0000'?'#00ff00':'#ff0000'; fire('input'); fire('change'); }
     else e.click(); }); R.pressed++; }catch(e){ errs.push('PRESS '+e.message.slice(0,120)); }
   await p.waitForTimeout(500);
   const ef=await p.evaluate(rt=>__effect(__mAfter(window.__cur,rt)),root); const did=ef.did;
   (R.why=R.why||[]).push(it.t.slice(0,28)+' → '+(ef.why||'nothing')); (R.order=R.order||[]).push([it.sig,it.n]);
   if(!did) R.dead.push(it.t+' ['+it.tag.toLowerCase()+(it.type&&it.tag==='INPUT'?':'+it.type:'')+']');
   if(errs.length) R.errors.push(it.t+' → '+[...new Set(errs)].join(' | ').slice(0,260));
   const still=await p.evaluate(r=>{ const e=document.querySelector(r); return !!(e&&e.getClientRects().length&&!e.closest('[hidden]')); },root);
   if(!still){ await reopen(); await CAL(); } else await p.evaluate(CLEAN);
  }
  R.secs=Math.round((Date.now()-T0)/1000);
  fs.writeFileSync(`${OUT}/${MODE}-${name}.json`,JSON.stringify(R,null,1));
  console.log(`${MODE} ${name} (${root}): ${R.pressed}/${R.controls} pressed · errors ${R.errors.length} · no effect ${R.dead.length} · covered ${R.covered.length} · small ${R.smallCount||0} · repeats sampled ${R.repeats} · skipped ${R.skipped||0} · off edge ${R.offEdge.length} · links ${R.links.n} bad ${R.links.badCount} · wide ${R.wide} · ${R.secs}s`);
 }catch(e){ console.log(MODE,name,'CRASHED',(e.message||'').slice(0,120)); fs.writeFileSync(`${OUT}/${MODE}-${name}.json`,JSON.stringify({screen:name,mode:MODE,crashed:(e.message||'').slice(0,200)},null,1)); }
 }
 await b.close(); })();
