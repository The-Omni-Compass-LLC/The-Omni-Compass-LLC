(()=>{ /* 🧭 THE AI ON THE OMNI-COMPASS (v212): every request to the AI runs through the Omni-Compass before it leaves the page.
   1. The reading: the request is sorted onto one of the compass's eight limbs (Story, Beat, Compass, Zodiac, Games, Voice, Film,
      Clock); the live law engine gives that limb's ring letter, and the letter's lens steers the angle of the answer.
   2. The governor: the compass law sits on top of the AI's own sense of length. The length the request asks for is the native
      setting; a band around it with 5% cushions holds the answer, two antagonist forces push back from the edges, smoothed with
      tanh so it never hammers; every answer read back moves the state, so length stays steady and inside the band.
   Shown on screen: the letter and the limb, never the equations. Switch: 🧭 in the AI's header. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const LIMBS=['Story','Beat','Compass','Zodiac','Games','Voice','Film','Clock'];
 const LENS={'Α':'origin: where it all begins','Ε':'energy: drive and momentum','Ζ':'zeal: passion and heat','Δ':'direction: a clear path to the goal','Η':'harmony: balance and resolution','Θ':'theme: the deeper meaning','Β':'the bridge: connections and turns','Ι':'identity: whose story it is','Κ':'craft: technique and detail','Λ':'logic: cause and reason','Μ':'memory: the past that shapes it','Ν':'novelty: the surprising and new','Ω':'the outcome: the ending it earns','Ξ':'exchange: dialogue and give-and-take','Ο':'order: structure and form','Π':'pulse: rhythm and pace','Ρ':'resonance: feeling that lingers','Σ':'synthesis: parts brought together','Γ':'ground: the concrete and real','Τ':'tension: conflict and stakes','Υ':'unity: one voice, one whole','Ψ':'psyche: the inner mind','Φ':'flow: ease and movement','Χ':'change: transformation'};
 let on=getLS('kanin-ai-compass',true), last=null; const X=getLS('kanin-ai-compass-x',{});
 const KW=[[1,/\b(beat|song|rap|lyric|verse|hook|chorus|music|melody|chord|bpm|drum|producer?)\b/i],[3,/\b(zodiac|horoscope|sign|astrolog|birth ?chart|moon|aries|taurus|gemini|cancer|leo|virgo|libra|scorpio|sagittarius|capricorn|aquarius|pisces)\b/i],[4,/\b(game|level|puzzle|quest|player|score)\b/i],[5,/\b(voice|read (it )?aloud|speak|narrat|pronounc|accent)\b/i],[6,/\b(film|movie|video|script|scene|shot|screenplay|trailer)\b/i],[7,/\b(time|clock|schedule|plan|today|tomorrow|week|calendar|deadline)\b/i],[2,/\b(compass|omni|direction|decide|choice|which way)\b/i]];
 const limbOf=q=>{ for(const [i,re] of KW) if(re.test(q)) return i; return 0; };
 function nativeLen(q){ const m=/(\d{2,4})\s*(words?|lines?)/i.exec(q); if(m) return Math.max(20,Math.min(1500,+m[1]*(/line/i.test(m[2])?9:1)));
  if(/\b(short|brief|quick|one line|tl;?dr|in a sentence)\b/i.test(q)) return 60; if(/\b(song|poem|story|script|scene|chapter|lyrics|rap)\b/i.test(q)) return 350; if(/\b(list|steps|plan|outline)\b/i.test(q)) return 200; return 140; }
 /* the compass law: band, cushions, two forces, tanh smoothing */
 function govern(kind,n0){ const lo=n0*0.8, hi=n0*1.2, span=hi-lo, cl=lo+0.05*span, ch=hi-0.05*span, s=Math.max(10,0.1*n0); const x=X[kind]!=null?X[kind]:n0;
  const up=x<cl?Math.tanh((cl-x)/s):0, dn=x>ch?Math.tanh((x-ch)/s):0; let t=x+0.5*span*(up-dn); if(!up&&!dn) t=x+0.25*span*Math.tanh((n0-x)/s); t=Math.max(lo,Math.min(hi,t)); return {target:Math.round(t),lo:Math.round(lo),hi:Math.round(hi)}; }
 function reading(q){ const limb=limbOf(q); let L=null; try{ L=UNILAW.state().letters[limb]; }catch(_){ } if(!L){ const R='ΑΕΖΔΗΘΒΙΚΛΜΝΩΞΟΠΡΣΓΤΥΨΦΧ'; L=R[(new Date().getHours()*7+limb*3)%24]; } const n0=nativeLen(q); const kind=LIMBS[limb]; const g=govern(kind,n0); return {limb,kind,L,lens:LENS[L]||'',n0,...g}; }
 function frame(q){ if(!on) return ''; const r=reading(q); last=r; paint();
  return '[Omni-Compass reading for this answer · limb: '+r.kind+' · ring letter '+r.L+(r.lens?' ('+r.lens+')':'')+'. Let this lens shape the angle of the answer without naming the compass unless asked. Length governor: aim for about '+r.target+' words, staying between '+r.lo+' and '+r.hi+', unless the person asked for a different length.'+(window.KGOV?' Governors on now: '+Object.entries(KGOV.on).filter(e=>e[1]).map(e=>e[0]).join(', ')+'.':'')+']'; }
 function observe(text){ if(!last||!text) return; const w=(String(text).trim().match(/\S+/g)||[]).length; const k=last.kind; X[k]=X[k]==null?w:Math.round(0.6*X[k]+0.4*w); putLS('kanin-ai-compass-x',X); }
 function paint(){ const a=document.querySelector('#kAI [data-ai="auto"]'); if(!a) return; let c=$('kAiCompass'); if(!c){ c=document.createElement('button'); c.type='button'; c.id='kAiCompass'; c.setAttribute('data-noul',''); a.insertAdjacentElement('afterend',c);
   c.addEventListener('click',e=>{ e.stopPropagation(); on=!on; putLS('kanin-ai-compass',on); paint(); say(on?'🧭 Omni-Compass ON: every answer is steered by the compass and held in its band.':'🧭 Omni-Compass OFF: the AI answers on its own.'); }); }
  const t=on?('🧭 Compass ON'+(last?' · '+last.L+' '+last.kind:'')):'🧭 Compass OFF'; if(c.textContent!==t) c.textContent=t; c.classList.toggle('on',on); c.setAttribute('aria-pressed',String(on)); c.title=on?(last?'Last answer steered by '+last.kind+' letter '+last.L+(last.lens?' ('+last.lens+')':'')+', held near '+last.target+' words. Tap to turn off.':'Every answer is steered by the Omni-Compass. Tap to turn off.'):'Tap to steer every answer with the Omni-Compass.'; }
 setInterval(paint,800);
 window.KOMNIAI={frame,observe,reading,get on(){ return on; }};
})();
