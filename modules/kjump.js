(()=>{ /* THE CANNON JUMP GENERATOR: one shot of the cannon jumps through every realm of KAN-IN at once (story, beat, key, mode, chords,
   song form and tone, humor, music mood, zodiac, metaphor, voice, language, video, game, compass letter). Each landing can feed the next,
   a dimension inside a dimension. Lock any realm and the others keep jumping; flip A to Z, flop to the neighbour; score every jump in five ways;
   then build the whole landing into the app. Every draw comes from the Omni-Compass cannon itself. */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const say=m=>{ try{ toast(m); }catch(_){ } }; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const opt=id=>{ const e=$(id); return e&&e.tagName==='SELECT'?[...e.options].filter(o=>!o.disabled&&o.value!=='').map(o=>({v:o.value,t:o.text.trim()})):[]; };
 const set=(id,v)=>{ const e=$(id); if(!e) return false; e.value=v; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); return true; };
 const press=id=>{ const b=$(id); if(b){ b.click(); return true; } return false; };
 const go=async(sc,w)=>{ try{ KBAR.go(sc); }catch(_){ } await sleep(w||800); };
 const LETTERS='ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'.split('');
 /* the realms: each knows its own options (read live from the app) and how to build its landing */
 const R=[
  {id:'story',i:'📖',n:'Story',o:()=>{ const s=(window.KSTARTER&&KSTARTER.STORIES)||[]; return [{v:'qp',t:'A fresh 20-canvas story, every canvas fired'}].concat(s.map((x,i)=>({v:'s'+i,t:x.t}))); },size:()=>{ try{ let p=1; for(let i=0;i<20;i++){ const n=(typeof wheelList==='function')?wheelList(i).length:6; p*=Math.max(1,n); } return p; }catch(_){ return Math.pow(6,20); } },
   build:async v=>{ if(v==='qp'){ try{ STORYLIB.fresh(); }catch(_){ } await sleep(400); press('qpBtn'); await sleep(3600); const d=$('qpDone'); if(d) d.hidden=true; } else { const st=KSTARTER.STORIES[+v.slice(1)]; if(st) await KSTARTER.loadStory(st); } }},
  {id:'genre',i:'🥁',n:'Beat genre',o:()=>opt('cGen'),sc:'pad',set:'cGen'},
  {id:'key',i:'🎼',n:'Key',o:()=>opt('cKey'),sc:'pad',set:'cKey'},
  {id:'mode',i:'🎚',n:'Mode',o:()=>opt('cMode'),sc:'pad',set:'cMode'},
  {id:'prog',i:'🎹',n:'Chords',o:()=>opt('cProg'),sc:'pad',set:'cProg'},
  {id:'form',i:'✍',n:'Song form',o:()=>opt('swForm'),sc:'swDock',set:'swForm'},
  {id:'tone',i:'🎭',n:'Song tone',o:()=>opt('swTone'),sc:'swDock',set:'swTone'},
  {id:'joke',i:'😂',n:'Humor',o:()=>{ const J=(window.KHUMOR&&KHUMOR.jokes)||{}; return [].concat(...Object.keys(J).map(k=>J[k].map(t=>({v:t,t:k+': '+t})))); }},
  {id:'mood',i:'♪',n:'Music mood',o:()=>opt('mMood'),sc:'musicDock',set:'mMood'},
  {id:'sign',i:'💞',n:'Zodiac sign',o:()=>opt('zodSel'),sc:'zodDock',set:'zodSel'},
  {id:'subject',i:'✒️',n:'Metaphor: the subject',o:()=>opt('mwT'),sc:'craftDock',set:'mwT'},
  {id:'image',i:'🌊',n:'Metaphor: the image',o:()=>opt('mwD'),sc:'craftDock',set:'mwD'},
  {id:'voice',i:'🎙',n:'Narrator voice',o:()=>opt('vdVoicePick'),sc:'voiceDock',set:'vdVoicePick'},
  {id:'lang',i:'🌐',n:'Language',o:()=>opt('lTo'),sc:'langDock',set:'lTo'},
  {id:'film',i:'🎬',n:'Film continuity',o:()=>opt('aivCont'),sc:'aivDock',set:'aivCont'},
  {id:'game',i:'🎲',n:'Game',o:()=>((window.GAMES&&GAMES.list)||[]).map(g=>({v:g.id,t:g.name+' · '+g.cat}))},
  {id:'letter',i:'🧭',n:'Compass letter',o:()=>LETTERS.map((L,i)=>({v:String(i),t:L+' · place '+(i+1)+' of 24'}))}];
 const LEVELS=[['Spark',3],['Flame',6],['Comet',10],['Star',13],['Omni',R.length]];
 const TIERS=[['Spark',0],['Flame',150],['Comet',250],['Star',330],['Galaxy',400],['Omni',450]];
 let depth=getLS('kanin-jump-depth',4), mode=getLS('kanin-jump-mode','chain'), cur={}, locks=getLS('kanin-jump-locks',{}), last=null, streak=0, best=getLS('kanin-jump-best',0), hist=getLS('kanin-jump-hist',[]), score=null, used=[];
 function draws(n){ const out=[]; let r=null; try{ r=UNILAW.fire('games',{quiet:true}); }catch(_){ } for(let i=0;i<n;i++){ if(!r||i%8===0&&i){ try{ r=UNILAW.fire('games',{quiet:true}); }catch(_){ r=null; } } const a=r?(r.land[i%8]/24+(r.first||0))%1:Math.random(); out.push(a); } return {u:out,k:r?r.k:Math.floor(Math.random()*24)}; }
 function pickRealms(){ const n=LEVELS[Math.max(0,Math.min(4,depth-1))][1]; const order=R.map((x,i)=>i); const d=draws(R.length).u; order.sort((a,b)=>d[a]-d[b]); const s=new Set(order.slice(0,n)); Object.keys(locks).forEach(id=>{ const i=R.findIndex(x=>x.id===id); if(i>=0) s.add(i); }); return R.map((x,i)=>i).filter(i=>s.has(i)); }
 function jump(){ const ids=pickRealms(); const D=draws(R.length); const prev=cur; const next={}; let carry=D.k;
  ids.forEach((ri,j)=>{ const r=R[ri], O=r.o(); if(!O.length) return; if(locks[r.id]&&prev[r.id]!=null){ next[r.id]=prev[r.id]; return; }
   let idx=Math.floor(D.u[ri]*O.length); if(mode==='chain'){ idx=(idx+carry)%O.length; carry=(carry*7+idx+3)%997; } else if(mode==='mirror'&&j%2){ const pr=next[R[ids[j-1]].id]; if(pr!=null) idx=(O.length-1-(pr%O.length)+O.length)%O.length; }
   next[r.id]=idx; });
  used=ids.filter(ri=>next[R[ri].id]!=null); last=prev; cur=next; streak++; rate(); hist.unshift({cur,used:used.map(ri=>R[ri].id),score:score.total,t:Date.now()}); hist=hist.slice(0,12); putLS('kanin-jump-hist',hist); draw(); try{ $('kJump').querySelector('.kjRes').scrollIntoView({block:'nearest'}); }catch(_){ } }
 function flip(){ used.forEach(ri=>{ const r=R[ri], O=r.o(); if(cur[r.id]!=null&&!locks[r.id]) cur[r.id]=O.length-1-cur[r.id]; }); rate(); draw(); say('🔀 Flipped: every landing jumped to its mirror, A to Z.'); }
 function flop(){ used.forEach(ri=>{ const r=R[ri], O=r.o(); if(cur[r.id]!=null&&!locks[r.id]) cur[r.id]=(cur[r.id]+1)%O.length; }); rate(); draw(); say('🔁 Flopped: every landing stepped to its neighbour.'); }
 const label=r=>{ const O=r.o(); const i=cur[r.id]; return i==null||!O[i]?'':O[i].t; };
 const count=ids=>ids.reduce((p,ri)=>{ const r=R[ri]; const n=r.size?r.size():r.o().length; return p*Math.max(1,n); },1);
 const SUP='⁰¹²³⁴⁵⁶⁷⁸⁹'; function words(n){ if(!isFinite(n)) return 'more than anyone can count'; if(n>=1e27){ const e=Math.floor(Math.log10(n)), m=n/Math.pow(10,e); return m.toFixed(1)+' × 10'+String(e).split('').map(d=>SUP[+d]).join('')+' (a trillion trillion trillion and beyond)'; } const U=[[1e24,'septillion'],[1e21,'sextillion'],[1e18,'quintillion'],[1e15,'quadrillion'],[1e12,'trillion'],[1e9,'billion'],[1e6,'million'],[1e3,'thousand']]; for(const [v,w] of U){ if(n>=v){ const x=n/v; return (x>=1000?Math.round(x).toLocaleString():x>=100?Math.round(x):x.toFixed(1))+' '+w; } } return Math.round(n).toLocaleString(); }
 function rate(){ const all=count(R.map((x,i)=>i)), here=count(used);
  const rarity=Math.max(0,Math.min(100,Math.round(Math.log10(Math.max(10,here))*5)));
  const m=(label(R[3])||'').toLowerCase(), t=(label(R[6])||'').toLowerCase(), mo=(label(R[8])||'').toLowerCase(), g=(label(R[1])||'').toLowerCase(); let agree=0, clash=0;
  const minor=/minor|aeolian|phrygian|locrian|dorian/.test(m), major=/major|ionian|lydian|mixolydian/.test(m), dark=/dark|sad|angry|mystery|horror|noir|tense/.test(t+' '+mo), bright=/hope|happy|joy|uplift|romantic|calm|focus|party|bright/.test(t+' '+mo);
  if(minor&&dark) agree++; if(major&&bright) agree++; if(minor&&bright) clash++; if(major&&dark) clash++; if(/lo-fi|ambient|chill/.test(g)&&/calm|focus|space|sleep/.test(mo)) agree++; if(/trap|drill|metal|rock/.test(g)&&/calm|sleep/.test(mo)) clash++;
  const harmony=Math.max(0,Math.min(100,55+agree*15-clash*10+used.length));
  const changed=last?used.filter(ri=>last[R[ri].id]!==cur[R[ri].id]).length:used.length; const surprise=used.length?Math.round(changed/used.length*100):0;
  const reach=Math.round(used.length/R.length*100), str=Math.min(100,streak*10);
  const total=rarity+harmony+surprise+reach+str; let tier=TIERS[0][0]; TIERS.forEach(([n,v])=>{ if(total>=v) tier=n; });
  if(total>best){ best=total; putLS('kanin-jump-best',best); }
  score={rarity,harmony,surprise,reach,streak:str,total,tier,all,here}; }
 async function buildAll(){ if(!used.length) return say('Press 💥 Jump first.'); const page=$('kJump'); page.hidden=true; const done=[];
  try{ const st=used.find(ri=>R[ri].id==='story'); if(st!=null){ const r=R[st]; await r.build(r.o()[cur.story].v); done.push(r.n); }
   const bySc={}; used.forEach(ri=>{ const r=R[ri]; if(r.sc&&cur[r.id]!=null) (bySc[r.sc]=bySc[r.sc]||[]).push(r); });
   for(const sc of Object.keys(bySc)){ await go(sc); bySc[sc].forEach(r=>{ const O=r.o(); if(O[cur[r.id]]) set(r.set,O[cur[r.id]].v); done.push(r.n); });
    if(sc==='pad'){ await sleep(250); press('cAuto'); await sleep(1200); }
    if(sc==='swDock'){ const jk=used.find(ri=>R[ri].id==='joke'); if(jk!=null) set('swTopic',R[jk].o()[cur.joke].v.slice(0,180)); await sleep(200); press('swFire'); await sleep(800); }
    if(sc==='craftDock'){ await sleep(150); press('mwGo'); } if(sc==='zodDock'){ await sleep(150); press('zodSpin'); } }
   const gm=used.find(ri=>R[ri].id==='game'); if(gm!=null) done.push('Game ready');
  }catch(e){ say('The build stopped at one step: '+(e&&e.message||'')); }
  try{ GOHOME(); }catch(_){ } await sleep(300); page.hidden=false; built=done; draw(); const b=page.querySelector('.kjBuilt'); if(b) b.scrollIntoView({block:'start'}); say('Built: '+done.length+' pieces from one cannon shot.'); }
 let built=[];
 const css=document.createElement('style'); css.textContent=`
#kJump{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(12px + env(safe-area-inset-top,0px)) 14px 40px;background:radial-gradient(circle at 50% 0,#3a1450,#07051a 70%);color:#eef;font:15px/1.5 system-ui,sans-serif}
#kJump[hidden]{display:none!important}#kJump .kjIn{max-width:1000px;margin:0 auto}
#kJump h2{font:900 26px/1.15 system-ui,sans-serif;margin:6px 0 2px;color:#ffe94a}#kJump h3{font:800 18px/1.2 system-ui,sans-serif;margin:20px 0 8px;border-top:1px solid rgba(255,255,255,.15);padding-top:14px}
#kJump .kjBrand{font:700 11px ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:#7ff}
#kJump .kjBig{font:900 22px/1.2 system-ui,sans-serif;color:#7ff}
#kJump .kjRow{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}#kJump .kjRow button,#kJump select{min-height:46px;border-radius:12px;padding:0 14px;font:700 15px system-ui,sans-serif}
#kJump .kjRow button.kjFire{background:#ff4f6d!important;color:#fff!important;font-size:18px;flex:1 1 180px}
#kJump .kjRes{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px}
#kJump .kjCell{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.16);border-radius:12px;padding:10px 12px;display:flex;gap:10px;align-items:flex-start}
#kJump .kjCell.lk{border-color:#ffe94a;background:rgba(255,233,74,.08)}#kJump .kjCell .kjI{font-size:22px}#kJump .kjCell b{display:block;font:800 11px ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;color:#7ff}
#kJump .kjCell span{display:block;font:600 15px/1.35 system-ui,sans-serif}#kJump .kjCell button{margin-left:auto;min-width:40px;min-height:36px;border-radius:8px}
#kJump .kjBars{display:grid;gap:6px}#kJump .kjBar{display:grid;grid-template-columns:110px 1fr 44px;gap:8px;align-items:center;font:600 14px system-ui,sans-serif}
#kJump .kjBar i{display:block;height:12px;border-radius:6px;background:linear-gradient(90deg,#7ff,#ffe94a,#ff4f6d)}#kJump .kjBar s{display:block;height:12px;border-radius:6px;background:rgba(255,255,255,.12);text-decoration:none;overflow:hidden}
#kJump .kjN{font-size:13px;opacity:.8}#kJump .kjHist button{min-height:38px;border-radius:10px;padding:0 10px;font:600 13px system-ui,sans-serif}`; document.head.appendChild(css);
 function box(){ let d=$('kJump'); if(!d){ d=document.createElement('div'); d.id='kJump'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Cannon jump generator'); document.body.appendChild(d); d.addEventListener('click',onClick); d.addEventListener('change',e=>{ if(e.target.id==='kjDepth'){ depth=+e.target.value; putLS('kanin-jump-depth',depth); } if(e.target.id==='kjMode'){ mode=e.target.value; putLS('kanin-jump-mode',mode); } }); } return d; }
 function draw(){ const d=box(); const all=count(R.map((x,i)=>i)); const S=score;
  d.innerHTML='<div class="kBar" data-sc="kJump"><button type="button" data-ka="close" data-kj="close">✕</button></div><div class="kjIn"><div class="kjBrand">The Omni-Compass LLC · DD Universe Multi-Media Studios’ KAN-IN™ · The cannon</div><h2>💥 Cannon Jump Generator</h2>'+
   '<div class="kjN">One shot jumps through every realm of KAN-IN at once. Lock what you love and the rest keeps jumping.</div><div class="kjBig">'+esc(words(all))+' possible landings</div><div class="kjN">'+R.length+' realms, each read live from the app: the story’s 20 canvases, every beat genre, key, mode and chord progression, song forms and tones, '+((window.KHUMOR&&KHUMOR.count)||0)+' jokes, music moods, signs, metaphors, voices, languages, film styles, '+(((window.GAMES&&GAMES.list)||[]).length)+' games and 24 compass letters.</div>'+
   '<div class="kjRow"><label class="kjN" style="display:flex;flex-direction:column;flex:1 1 160px">How deep<select id="kjDepth">'+LEVELS.map(([n,c],i)=>'<option value="'+(i+1)+'"'+(depth===i+1?' selected':'')+'>'+(i+1)+' · '+n+' ('+c+' realms)</option>').join('')+'</select></label><label class="kjN" style="display:flex;flex-direction:column;flex:1 1 160px">How it jumps<select id="kjMode"><option value="free"'+(mode==='free'?' selected':'')+'>Free: every realm on its own</option><option value="chain"'+(mode==='chain'?' selected':'')+'>Chain: each landing feeds the next</option><option value="mirror"'+(mode==='mirror'?' selected':'')+'>Mirror: every other realm flips the one before</option></select></label></div>'+
   '<div class="kjRow"><button type="button" class="kjFire" data-kj="jump" data-noul>💥 Jump</button><button type="button" data-kj="flip" data-noul>🔀 Flip A↔Z</button><button type="button" data-kj="flop" data-noul>🔁 Flop</button><button type="button" data-kj="build" data-noul>▶ Build it all</button><button type="button" data-kj="unlock" data-noul>🔓 Unlock all</button></div>'+
   '<h3>🎯 Where the cannon landed</h3>'+(used.length?'<div class="kjRes">'+used.map(ri=>{ const r=R[ri]; const lk=!!locks[r.id]; return '<div class="kjCell'+(lk?' lk':'')+'"><span class="kjI">'+r.i+'</span><div style="flex:1;min-width:0"><b>'+esc(r.n)+' · '+(r.size?words(r.size()):r.o().length)+' options</b><span>'+esc(label(r))+'</span></div><button type="button" data-kj="lock" data-id="'+r.id+'" aria-label="'+(lk?'Unlock':'Lock')+' '+esc(r.n)+'" data-noul>'+(lk?'🔒':'🔓')+'</button></div>'; }).join('')+'</div>':'<div class="kjN">Press 💥 Jump to fire the cannon.</div>')+
   (S?'<h3>🏆 Score · '+esc(S.tier)+' · '+S.total+' of 500 · best '+best+'</h3><div class="kjBars">'+[['Rarity',S.rarity],['Harmony',S.harmony],['Surprise',S.surprise],['Reach',S.reach],['Streak',S.streak]].map(([n,v])=>'<div class="kjBar"><span>'+n+'</span><s><i style="width:'+v+'%"></i></s><span>'+v+'</span></div>').join('')+'</div><div class="kjN">This landing is one of '+esc(words(S.here))+' with these realms. Levels: Spark, Flame, Comet, Star, Galaxy, Omni.</div>':'')+
   (built.length?'<h3 class="kjBuilt">✅ Built from one shot</h3><div class="kjN">'+built.map(esc).join(' · ')+'</div><div class="kjRow"><button type="button" data-kj="open" data-sc="home" data-noul>📖 The story</button><button type="button" data-kj="open" data-sc="pad" data-noul>🥁 The beat</button><button type="button" data-kj="open" data-sc="swDock" data-noul>✍ The song</button><button type="button" data-kj="open" data-sc="musicDock" data-noul>♪ The music</button><button type="button" data-kj="open" data-sc="zodDock" data-noul>💞 The sign</button><button type="button" data-kj="game" data-noul>🎲 Play the game</button></div>':'')+
   (hist.length?'<h3>🕘 Recent jumps</h3><div class="kjRow kjHist">'+hist.map((h,i)=>'<button type="button" data-kj="hist" data-i="'+i+'" data-noul>#'+(hist.length-i)+' · '+h.score+' pts · '+h.used.length+' realms</button>').join('')+'</div>':'')+'</div>'; }
 function onClick(e){ const b=e.target.closest('[data-kj]'); if(!b) return; const k=b.dataset.kj;
  if(k==='close'){ $('kJump').hidden=true; return; } if(k==='jump') return jump(); if(k==='flip') return flip(); if(k==='flop') return flop(); if(k==='build') return buildAll();
  if(k==='unlock'){ locks={}; putLS('kanin-jump-locks',locks); return draw(); }
  if(k==='lock'){ const id=b.dataset.id; if(locks[id]) delete locks[id]; else locks[id]=1; putLS('kanin-jump-locks',locks); return draw(); }
  if(k==='hist'){ const h=hist[+b.dataset.i]; if(h){ cur=Object.assign({},h.cur); used=h.used.map(id=>R.findIndex(x=>x.id===id)).filter(i=>i>=0); rate(); draw(); } return; }
  if(k==='open'){ $('kJump').hidden=true; const sc=b.dataset.sc; if(sc==='home'){ try{ GOHOME(); }catch(_){ } } else { try{ KRAIL.goTo(sc); }catch(_){ try{ KBAR.go(sc); }catch(__){ } } } return; }
  if(k==='game'){ const gi=R.find(x=>x.id==='game'); const O=gi.o(); const g=O[cur.game]; $('kJump').hidden=true; if(g){ try{ GAMES.open(g.v); }catch(_){ } } else say('Jump with the Game realm in reach (depth 4 or 5).'); return; } }
 function open(){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||GOHOME)(); }catch(_){ } draw(); d.hidden=false; d.scrollTop=0; }
 /* Home, the Menu and Escape close it like every other page; the menu gets a Cannon tab */
 try{ const gh=window.GOHOME; if(gh&&!gh.__kjump){ const w=function(){ const d=$('kJump'); if(d) d.hidden=true; return gh.apply(this,arguments); }; w.__kjump=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')){ const d=$('kJump'); if(d) d.hidden=true; } },true);
 function menu(){ const t=$('tourTab'); if(!t||t.querySelector('.kGrp[data-g="7"]')) return; const h=document.createElement('div'); h.className='kGrp'; h.dataset.g='7'; h.textContent='💥 The cannon'; h.style.order='800'; t.appendChild(h);
  [['ttJump','🎰 Cannon Jump Generator',open],['ttJumpGo','💥 Jump now and build it',async()=>{ open(); jump(); }]].forEach(([id,l,fn],i)=>{ const b=document.createElement('button'); b.type='button'; b.id=id; b.className='ttMusic'; b.textContent=l; b.style.order=String(801+i); b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); fn(); }); t.appendChild(b); }); }
 menu(); setInterval(menu,1500);
 window.KJUMP={open,jump,flip,flop,build:buildAll,realms:R,count:()=>count(R.map((x,i)=>i)),words,state:()=>({cur,used:used.map(i=>R[i].id),score,locks})};
})();
