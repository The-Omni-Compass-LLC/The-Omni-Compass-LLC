/* ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   THE OMNI-COMPASS LAW, FORMALLY (the governing core of every governor below; kept in the source, not on screen).
   Definitions. A muscle m has a measured state x_m(t) (a level in dB, a pace in words per minute, a frame time in ms, an offset in
   steps), a native setting n_m (what the equipment does on its own), and a band B_m = [ℓ_m, h_m] containing n_m. The cushions are
   c⁻ = ℓ + κ(h − ℓ) and c⁺ = h − κ(h − ℓ) with κ = 0.05. The two antagonist forces, with softness σ_m > 0, are
        F↑(x) = tanh((c⁻ − x)/σ) for x < c⁻, else 0;      F↓(x) = tanh((x − c⁺)/σ) for x > c⁺, else 0,
   and the law is the net pull Φ(x) = F↑(x) − F↓(x) ∈ (−1, 1). The governed actuator u_m (a gain, a rate, a resolution, a pull) moves
        u_{k+1} = Π_U( u_k · exp(η_m Φ(x_k)) )        (multiplicative actuators: gain, rate, resolution)
        u_{k+1} = Π_U( u_k + η_m Φ(x_k) )             (additive actuators: an offset)
   where Π_U clips to the admissible set U_m, whose upper end is the muscle's own limit and, for a level, the native setting itself.
   Properties. (1) Bounded: |Φ| < 1, so one step never moves u by more than η: smooth, never hammering. (2) Dead zone: Φ = 0 on
   [c⁻, c⁺], so a muscle inside its cushions is left exactly as native left it. (3) Restoring: Φ points into the band on both sides,
   so for any actuator monotone in x the band is attracting; with η small against the plant's gain the iteration is a contraction
   outside the cushions and settles inside them. (4) Never past the limit: Π_U holds u inside U, whatever x does. (5) Do no harm:
   when the governor is switched off, u returns to native (u = 1 or u = 0) and the equipment runs exactly as it was built.
   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── */
(()=>{ /* 🧭 OMNI-COMPASS GOVERNORS (v213): the compass law on every piece of equipment, each on top of that equipment's own setting.
   The law, the same everywhere: a band around the native setting, 5% cushions inside its edges, two antagonist forces pushing back
   from the edges, smoothed with tanh so it never hammers; a muscle is driven to its own limit and never past it.
   · Master: the studio's output is read 20 times a second; peaks are held inside their band and never allowed to clip; when the
     music is quiet again the level returns to the mixer's own setting, never above it.
   · DJ decks: each loaded track's loudness is read and both decks are held inside one band, so a mix never jumps in level.
   · Karaoke: every vocal take is read and set inside the band before it plays, so no take is buried or blasting.
   · Sequencer: a hit recorded live keeps its feel inside the cushion; a hit that lands far off the grid is pulled toward it, harder
     the farther off it is.
   · The AI: every request carries its compass reading and length band (🧭 in the AI).
   · The cannon story: every shot of the cannon runs through the unified law engine; its letters show here.
   Each governor has its own switch and a live gauge on the board in the Studio, above the console. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const ON=Object.assign({master:true,dj:true,kara:true,groove:true,music:true,voice:true,frame:true},getLS('kanin-gov',{}));
 const dB=x=>20*Math.log10(Math.max(1e-6,x)), lin=d=>Math.pow(10,d/20);
 /* the law: returns the pull toward the band (positive up, negative down) */
 function law(x,lo,hi,s){ const span=hi-lo, cl=lo+.05*span, ch=hi-.05*span; if(x<cl) return Math.tanh((cl-x)/s); if(x>ch) return -Math.tanh((x-ch)/s); return 0; }
 const G={music:{x:null,g:1},voice:{wpm:null,r:1,n:0},frame:{ms:null,dpr:null,nat:null},master:{x:null,g:1,lo:-12,hi:-1,min:-48,max:0},dj:{A:null,B:null,fA:1,fB:1},kara:{x:null,f:1,n:0},groove:{x:0,n:0,pulled:0},ai:{},cannon:{}};
 /* ── master ── */
 let gov=null, an=null, buf=null;
 function hook(c,OUT){ if(gov) return; try{ gov=c.createGain(); an=c.createAnalyser(); an.fftSize=1024; buf=new Float32Array(an.fftSize); try{ OUT.disconnect(c.destination); }catch(_){ } OUT.connect(gov); gov.connect(c.destination); gov.connect(an); }catch(_){ gov=null; } }
 (window.PADBUS_HOOKS=window.PADBUS_HOOKS||[]).push(hook);
 function master(){ if(!gov){ try{ const P=window.PADSTUDIO; if(P&&P.playing){ const o=P.out(); if(o) hook(o.context,o); } }catch(_){ } } if(!gov||!an) return; an.getFloatTimeDomainData(buf); let pk=0; for(let i=0;i<buf.length;i++){ const v=Math.abs(buf[i]); if(v>pk) pk=v; }
  const M=G.master; const pre=pk/Math.max(1e-6,M.g); const pd=dB(pre); M.x=dB(pk); if(!ON.master){ if(M.g!==1){ M.g=1; gov.gain.setTargetAtTime(1,gov.context.currentTime,.05); } return; }
  if(pk<1e-4){ M.x=null; } const f=pk<1e-4?0:law(pd+dB(M.g),M.lo,M.hi,3); let g=M.g; if(f<0) g*=lin(6*f*.05*20); else if(pd+dB(g)<M.hi-3) g=Math.min(1,g*lin(.6)); g=Math.max(lin(-18),Math.min(1,g)); if(Math.abs(g-M.g)>1e-4){ M.g=g; gov.gain.setTargetAtTime(g,gov.context.currentTime,.03); } }
 /* ── loudness of a recording (for the decks and the takes) ── */
 function rmsOf(b){ if(!b) return null; if(b.__krms!=null) return b.__krms; let s=0,n=0; const step=Math.max(1,Math.floor(b.length/40000)); for(let ch=0;ch<b.numberOfChannels;ch++){ const d=b.getChannelData(ch); for(let i=0;i<d.length;i+=step){ s+=d[i]*d[i]; n++; } } const r=n?dB(Math.sqrt(s/n)):-90; b.__krms=r; return r; }
 function trim(r,target,width){ if(r==null||r<-80) return 1; const f=law(r,target-width,target+width,2); if(!f) return 1; const off=r<target?(target-width*.9)-r:(target+width*.9)-r; return Math.max(lin(-12),Math.min(lin(12),lin(off*Math.abs(f)))); }
 /* ── DJ decks ── */
 function dj(){ let D=null; try{ D=DJBOOTH.D; }catch(_){ } if(!D) return; ['A','B'].forEach(d=>{ const k=D[d]; if(!k||!k.vol) return; const r=rmsOf(k.buf); G.dj[d]=r; const f=ON.dj&&k.buf?trim(r,-16,2):1; G.dj['f'+d]=f; const sl=document.querySelector('#deck'+d+' input[data-k="vol"]'); const v=sl?(+sl.value)/100:.9; const want=v*f; if(Math.abs(k.vol.gain.value-want)>.004){ try{ k.vol.gain.setTargetAtTime(want,k.vol.context.currentTime,.06); }catch(_){ k.vol.gain.value=want; } } }); }
 /* ── karaoke takes (called by the karaoke as each take starts) ── */
 function take(t){ if(!ON.kara||!t||!t.buf) return 1; const r=rmsOf(t.buf); const f=trim(r,-18,2); G.kara={x:r,f,n:(G.kara.n||0)+1}; return f; }
 /* ── sequencer: live hits keep their feel inside the cushion, far ones are pulled to the grid ── */
 function groove(off){ if(!ON.groove||!isFinite(off)) return off; const a=Math.abs(off), c=.03, s=.12; G.groove.x=a; G.groove.n++; if(a<=c) return off; const ex=a-c; const out=Math.sign(off)*(c+ex*(1-.6*Math.tanh(ex/s))); G.groove.pulled=Math.round((1-Math.abs(out)/a)*100); return out; }
 /* ── the Music screen's score generator: its own bus (compressor → master → speakers) ── */
 let man=null, mbuf=null;
 function music(){ const B=window.MUSICBUS; if(!B||!B.master) return; const c=B.c; if(!man){ try{ man=c.createAnalyser(); man.fftSize=1024; mbuf=new Float32Array(man.fftSize); B.master.connect(man); }catch(_){ return; } }
  const sl=$('mVol'); const v=sl?(+sl.value)/100:.7; const M=G.music; if(!(window.MUSIC&&MUSIC.playing)){ M.x=null; } man.getFloatTimeDomainData(mbuf); let pk=0; for(let i=0;i<mbuf.length;i++){ const a=Math.abs(mbuf[i]); if(a>pk) pk=a; }
  if(pk>1e-4) M.x=dB(pk); let g=M.g; if(!ON.music) g=1; else if(pk>1e-4){ const f=law(dB(pk),-14,-3,3); if(f<0) g*=lin(6*f); else if(dB(pk)<-6) g=Math.min(1,g*lin(.5)); }
  g=Math.max(lin(-18),Math.min(1,g)); M.g=g; const want=v*g; if(Math.abs(B.master.gain.value-want)>.003){ try{ B.master.gain.setTargetAtTime(want,c.currentTime,.04); }catch(_){ B.master.gain.value=want; } } }
 /* ── the voice readers: the speaking pace is held inside the band people follow best (145–175 words a minute) ── */
 (function(){ const S=window.speechSynthesis; if(!S||S.__kgov) return; S.__kgov=1; const speak=S.speak.bind(S);
  S.speak=function(u){ try{ if(u&&ON.voice){ const nat=u.rate||1; u.__nat=nat; u.rate=Math.max(.5,Math.min(2,nat*G.voice.r)); const words=(String(u.text||'').match(/\S+/g)||[]).length; let t0=0; u.addEventListener('start',()=>{ t0=performance.now(); }); u.addEventListener('end',()=>{ if(!t0||words<6) return; const min=(performance.now()-t0)/60000; if(min<=0) return; const wpm=words/min; const V=G.voice; V.wpm=wpm; V.n++; const f=law(wpm,145,175,12); V.r=Math.max(.8,Math.min(1.25,V.r*Math.exp(.25*f))); }); } }catch(_){ } return speak(u); }; })();
 /* ── frames: the video studio, the 143 games and every animation hold their frame time in band; the drawing sharpness is the
    actuator, never above the screen's own ── */
 (function(){ const nat=window.devicePixelRatio||1; G.frame.nat=nat; let dpr=nat, ema=null, last=0, cnt=0;
  try{ Object.defineProperty(window,'devicePixelRatio',{configurable:true,get:()=>ON.frame?dpr:nat}); }catch(_){ }
  const tick=t=>{ requestAnimationFrame(tick); if(last){ const d=t-last; if(d>0&&d<250){ ema=ema==null?d:ema*.92+d*.08; } } last=t; if(++cnt%30) return; if(ema==null) return; G.frame.ms=ema; G.frame.dpr=dpr;
   if(!ON.frame){ if(dpr!==nat){ dpr=nat; dispatchEvent(new Event('resize')); } return; }
   const f=law(ema,8,22,3); let n=dpr; if(f<0) n=Math.max(1,Math.round(dpr*Math.exp(.25*f)*4)/4); else if(ema<15&&dpr<nat) n=Math.min(nat,Math.round(dpr*Math.exp(.12)*4)/4);
   if(n!==dpr){ dpr=n; G.frame.dpr=dpr; dispatchEvent(new Event('resize')); } };
  requestAnimationFrame(tick); })();
 /* ── the board: one gauge per governor ── */
 const css=document.createElement('style'); css.textContent=`
#kGovBoard{margin:8px 0;padding:8px 10px;border:2px solid #ffe94a;border-radius:14px;background:linear-gradient(180deg,#1e1a08,#0d0b04);color:#fff}
#kGovBoard h4{margin:0 0 6px;font:900 clamp(13px,1vw,20px) system-ui,sans-serif;color:#ffe94a;letter-spacing:.04em}
#kGovBoard .gvGrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:8px}
#kGovBoard .gv{border:1px solid rgba(255,233,74,.3);border-radius:10px;padding:6px 8px;min-width:0;background:rgba(255,255,255,.03)}
#kGovBoard .gv b{display:block;font:800 clamp(12px,.9vw,17px) system-ui,sans-serif;color:#fff;overflow-wrap:anywhere}
#kGovBoard .gv i{display:block;font:600 clamp(11px,.8vw,15px)/1.35 system-ui,sans-serif;font-style:normal;color:#e8dfb0;min-height:2.7em;overflow-wrap:anywhere}
#kGovBoard .gv button{min-height:32px;border-radius:8px;font:800 12px system-ui,sans-serif;margin-top:4px}
#kGovBoard .gv button.on{background:#ffe94a!important;color:#14163a!important}
#kGovBoard .bar{position:relative;height:14px;border-radius:7px;background:#2a2a2a;margin:5px 0;overflow:hidden}
#kGovBoard .bar .band{position:absolute;top:0;bottom:0;background:rgba(125,255,138,.28);border-left:3px solid rgba(255,233,74,.8);border-right:3px solid rgba(255,90,90,.8)}
#kGovBoard .bar .nd{position:absolute;top:-2px;bottom:-2px;width:3px;margin-left:-1px;background:#fff;box-shadow:0 0 6px #fff}`; document.head.appendChild(css);
 const pct=(v,a,b)=>Math.max(0,Math.min(100,(v-a)/(b-a)*100));
 function bar(v,a,b,lo,hi){ return '<div class="bar"><div class="band" style="left:'+pct(lo,a,b)+'%;width:'+(pct(hi,a,b)-pct(lo,a,b))+'%"></div>'+(v==null?'':'<div class="nd" style="left:'+pct(v,a,b)+'%"></div>')+'</div>'; }
 const sw=(k)=>'<button type="button" data-gv="'+k+'" class="'+(ON[k]?'on':'')+'" aria-pressed="'+ON[k]+'" data-noul>'+(ON[k]?'🧭 ON':'🧭 OFF')+'</button>';
 function rows(){ const M=G.master, J=G.dj, K=G.kara, Q=G.groove; let ai=null; try{ ai=window.KOMNIAI; }catch(_){ } let L=[]; try{ L=UNILAW.state().letters; }catch(_){ }
  const R=[];
  R.push('<div class="gv"><b>🎚 Master</b>'+bar(M.x,M.min,M.max,M.lo,M.hi)+'<i>'+(M.x==null?'Waiting for sound.':'Peak '+M.x.toFixed(1)+' dB · held '+(M.g<.999?(dB(M.g)).toFixed(1)+' dB under the mixer':'at the mixer’s own level')+'. Peaks held under the top of the band.')+'</i>'+sw('master')+'</div>');
  const dj=d=>J[d]==null?'deck '+d+' empty':'deck '+d+' '+J[d].toFixed(1)+' dB → '+(dB(J['f'+d])>=0?'+':'')+dB(J['f'+d]).toFixed(1)+' dB';
  R.push('<div class="gv"><b>🎧 DJ decks</b>'+bar(J.A==null?(J.B==null?null:J.B+dB(J.fB)):J.A+dB(J.fA),-40,0,-18,-14)+'<i>'+dj('A')+' · '+dj('B')+'. Both held in one band.</i>'+sw('dj')+'</div>');
  R.push('<div class="gv"><b>🎤 Karaoke takes</b>'+bar(K.x==null?null:K.x+dB(K.f),-40,0,-20,-16)+'<i>'+(K.x==null?'Plays when a take plays.':'Last take '+K.x.toFixed(1)+' dB → '+(dB(K.f)>=0?'+':'')+dB(K.f).toFixed(1)+' dB · '+K.n+' takes set')+'</i>'+sw('kara')+'</div>');
  R.push('<div class="gv"><b>🥁 Sequencer · live hits</b>'+bar(Q.x,0,.5,0,.25)+'<i>'+(Q.n?'Last hit '+Math.round(Q.x*100)+'% of a step off the grid'+(Q.pulled?' · pulled '+Q.pulled+'% toward it':' · kept as played')+'.':'Record pads live to see it work.')+'</i>'+sw('groove')+'</div>');
  const Mu=G.music, V=G.voice, F=G.frame;
  R.push('<div class="gv"><b>🎵 Music score</b>'+bar(Mu.x,-48,0,-14,-3)+'<i>'+(Mu.x==null?'Plays when the score plays.':'Peak '+Mu.x.toFixed(1)+' dB · '+(Mu.g<.999?'held '+dB(Mu.g).toFixed(1)+' dB under your volume':'at your own volume'))+'</i>'+sw('music')+'</div>');
  R.push('<div class="gv"><b>🗣 Voice readers</b>'+bar(V.wpm,90,230,145,175)+'<i>'+(V.wpm==null?'Reads when a voice reads.':'Last reading '+Math.round(V.wpm)+' words a minute · pace ×'+V.r.toFixed(2))+'</i>'+sw('voice')+'</div>');
  R.push('<div class="gv"><b>🖥 Frames · video studio, 143 games, animations</b>'+bar(F.ms,0,40,8,22)+'<i>'+(F.ms==null?'Measuring.':'Frame '+F.ms.toFixed(1)+' ms ('+Math.round(1000/F.ms)+' a second) · sharpness '+(F.dpr||1)+(F.dpr<F.nat?' of '+F.nat:' (the screen’s own)'))+'</i>'+sw('frame')+'</div>');
  R.push('<div class="gv"><b>🤖 The AI</b>'+bar(null,0,1,.4,.6)+'<i>'+(ai?(ai.on?'Every answer steered by the compass and held in its length band.':'Off: turn 🧭 on in the AI.'):'Open 🤖 AI.')+'</i></div>');
  R.push('<div class="gv"><b>💥 The cannon story</b>'+bar(null,0,1,.4,.6)+'<i>'+(L.length?'Every shot runs the law engine · letters now: '+L.join(' '):'The law engine answers on the first shot.')+'</i></div>');
  return R.join(''); }
 function board(){ const fx=$('kFXRet')||$('padMixer'); if(!fx) return; let b=$('kGovBoard'); if(!b){ b=document.createElement('div'); b.id='kGovBoard'; b.innerHTML='<h4>🧭 Omni-Compass governors · the compass law on every piece of equipment</h4><div class="gvGrid"></div>'; fx.insertAdjacentElement('beforebegin',b);
   b.addEventListener('click',e=>{ const x=e.target.closest('[data-gv]'); if(!x) return; e.stopPropagation(); const k=x.dataset.gv; ON[k]=!ON[k]; putLS('kanin-gov',ON); paintB(); say('🧭 '+({master:'Master',dj:'DJ decks',kara:'Karaoke takes',groove:'Sequencer live hits',music:'Music score',voice:'Voice readers',frame:'Frames'}[k])+' governor '+(ON[k]?'ON':'OFF')+'.'); }); } paintB(); }
 function paintB(){ const g=document.querySelector('#kGovBoard .gvGrid'); if(g&&g.getClientRects().length) g.innerHTML=rows(); }
 setInterval(()=>{ try{ master(); }catch(_){ } try{ music(); }catch(_){ } },50);
 setInterval(()=>{ try{ dj(); }catch(_){ } const pad=$('pad'); if(pad&&pad.classList.contains('on')) board(); },500);
 setInterval(()=>{ const t=$('tourTab'); if(t&&!$('ttGov')){ const b=document.createElement('button'); b.type='button'; b.id='ttGov'; b.className='ttMusic kStartB'; b.textContent='🧭 Omni-Compass governors'; b.style.order='71'; b.setAttribute('data-noul',''); b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } try{ KRAIL.goTo('pad'); }catch(_){ } setTimeout(()=>{ board(); const g=$('kGovBoard'); if(g) g.scrollIntoView({block:'start',behavior:'smooth'}); },1400); }); t.appendChild(b); } },1000);
 window.KGOV={names:['master','dj','kara','groove','music','voice','frame'],law,groove,take,state:G,get on(){ return Object.assign({},ON); },set:(k,v)=>{ ON[k]=!!v; putLS('kanin-gov',ON); }};
})();
