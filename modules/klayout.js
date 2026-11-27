(()=>{ /* 🪟 THE MUSIC STUDIO'S PANELS, LAID OUT FOR THE SCREEN (v245). Every device is its own floating panel and any number can be up at
   once over the mixing board: 🥁 pads, 🎹 keyboard, 🎼 track sequencer, 🎧 DJ decks, 🎤 Karaoke mic. One tap on 🪟 ARRANGE lays the open
   panels out for the screen you are on:
   • A LAPTOP OR A BIG MONITOR tiles them side by side across the whole screen, full height, none covering another: pads, keyboard,
     track sequencer, DJ decks and mic, each as wide as the screen allows (a big monitor gives each more room).
   • A PHONE stacks them full width, one in front, with a strip of panel buttons at the bottom to bring any panel to the front.
   Drag any panel by its top bar to move it anywhere, stack them or set them side by side; ▁ shrinks one, ✕ closes it; every panel stays
   live wherever it sits. ● REC on the pads or the keyboard records both: one sequencer, one mixing board. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const F=()=>{ try{ return KRAIL.FLOAT; }catch(_){ return null; } };
 const KEYS=[['pads','🥁','Pads',1],['keys','🎹','Keys',1.5],['rack','🎛','Steps',1.6],['dj','🎧','DJ',1.3],['kara','🎤','Mic',.9],['seq','🎼','Tracks',0]];
 const phone=()=>innerWidth<=760;
 const openKeys=()=>KEYS.filter(([k])=>{ try{ return F().isOpen(k); }catch(_){ return false; } });
 const put=(k,g)=>{ try{ localStorage.setItem('kanin-float-'+k,JSON.stringify(g)); }catch(_){ } };
 function arrange(quiet){ const f=F(); if(!f) return; let L=openKeys(); if(!L.length){ ['pads','keys','seq'].forEach(k=>{ try{ f.open(k); }catch(_){ } }); L=openKeys(); }
  const W=innerWidth-(phone()?58:76), H=innerHeight, gap=8; let top=8; const bb=$('bbBar'); if(!phone()&&bb&&bb.getClientRects().length){ const r=bb.getBoundingClientRect(); if(r.bottom>0&&r.bottom<H*.6) top=Math.round(r.bottom)+4; }
  if(phone()){ L.forEach(([k])=>put(k,{x:4,y:56,w:W-8,h:Math.round(H*.72)})); }
  else { const WT={pads:1,keys:1.4,rack:1.6,dj:1.2,kara:.9,seq:1.6}; const order=['pads','keys','rack','seq','dj','kara']; const cols=order.map(k=>L.find(x=>x[0]===k)).filter(Boolean); const tot=cols.reduce((a,[k])=>a+WT[k],0)||1; const avail=W-gap*(cols.length+1); let x=gap;
   cols.forEach(([k])=>{ const w=Math.max(280,Math.round(avail*WT[k]/tot)); put(k,{x:Math.min(x,W-w-gap),y:top,w,h:H-top-gap}); x+=w+gap; }); }
  L.forEach(([k])=>{ try{ f.open(k); }catch(_){ } }); if(!quiet) say(phone()?'🪟 The panels are stacked for the phone: the strip at the bottom brings any one to the front.':'🪟 The panels are laid out across the screen over the mixing board. Drag any top bar to move one.'); paint(); }
 /* the phone strip: bring any open panel to the front */
 const css=document.createElement('style'); css.textContent=`
#kPanelStrip{position:fixed;z-index:9740;left:calc(6px + env(safe-area-inset-left,0px));right:calc(var(--kRailW,58px) + 6px);bottom:calc(6px + env(safe-area-inset-bottom,0px));display:none;gap:6px;justify-content:center;background:rgba(10,8,30,.92);border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:6px}
#kPanelStrip.on{display:flex}
#kPanelStrip button{flex:1 1 0;min-height:44px!important;border-radius:10px!important;font:800 13px system-ui,sans-serif!important;padding:0 4px!important}`; document.head.appendChild(css);
 function strip(){ let s=$('kPanelStrip'); if(!s){ s=document.createElement('div'); s.id='kPanelStrip'; s.setAttribute('role','toolbar'); s.setAttribute('aria-label','Panels'); s.addEventListener('click',e=>{ const b=e.target.closest('[data-pk]'); if(!b) return; e.stopPropagation(); try{ F().open(b.dataset.pk); }catch(_){ } }); document.body.appendChild(s); } return s; }
 function paint(){ const pad=$('pad'); const live=!!pad&&(pad.classList.contains('on')||document.body.classList.contains('kDevOver')); const L=live?openKeys():[]; const s=strip(); const on=phone()&&L.length>=2; s.classList.toggle('on',on); if(on){ const h=L.map(([k,i,l])=>'<button type="button" data-pk="'+k+'" data-noul>'+i+' '+l+'</button>').join(''); if(s.dataset.h!==h){ s.dataset.h=h; s.innerHTML=h; } }
  const bb=$('bbBar'); if(bb&&!bb.querySelector('[data-arr]')){ const b=document.createElement('button'); b.type='button'; b.dataset.arr='1'; b.setAttribute('data-noul',''); b.textContent='🪟 Arrange'; b.title='Lay the open panels out for this screen'; b.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); arrange(); },true); bb.appendChild(b); } }
 /* 🔗 ONE RECORD BUTTON FOR THE WHOLE RIG: the pads and the keyboard feed one sequencer and one mixing board, so ● REC on either one
    records both (each onto its selected track), and stopping either stops both. */
 const padRec=()=>{ const b=$('padRecLive'); return !!b&&(b.classList.contains('rec')||/on$/i.test(b.textContent.trim())); };
 const keyRec=()=>{ const b=$('kbRec'); return !!b&&(b.classList.contains('rec')||/: on$/i.test(b.textContent.trim())); };
 let was={p:false,k:false}, syncing=false;
 setInterval(()=>{ if(syncing) return; const p=padRec(), k=keyRec(); if(p!==was.p&&k===was.k&&p!==k){ syncing=true; const b=$('kbRec'); if(b) b.click(); setTimeout(()=>{ syncing=false; was={p:padRec(),k:keyRec()}; },250); return; }
  if(k!==was.k&&p===was.p&&p!==k){ syncing=true; const b=$('padRecLive'); if(b) b.click(); setTimeout(()=>{ syncing=false; was={p:padRec(),k:keyRec()}; },250); return; } was={p,k}; },120);
 setInterval(paint,800);
 window.KLAYOUT={arrange,get recording(){ return padRec()||keyRec(); }};
})();
