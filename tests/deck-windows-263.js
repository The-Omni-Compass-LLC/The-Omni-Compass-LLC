const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub7/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; });
await p.evaluate(()=>{ KAUDIO.gesture&&KAUDIO.gesture(); PADSTUDIO.open(); }); await p.waitForTimeout(2500);
const out={};
out.deck=await p.evaluate(()=>{ const d=document.getElementById('kDeck'); return {hidden:d.hidden,cx:KDECK.cx,z:getComputedStyle(d).zIndex,wins:[...d.querySelectorAll('[data-w]')].map(x=>x.textContent.trim()).join('|')}; });
// open every window via the deck tabs
for(const k of ['keys','dj','kara','seq']){ await p.evaluate(k=>{ const b=document.querySelector('#kDeck [data-w="'+k+'"]'); b&&b.click(); },k); await p.waitForTimeout(700); }
out.states=await p.evaluate(()=>['pads','keys','dj','kara','seq'].map(k=>k+':'+KWIN.state(k)).join(' '));
await p.evaluate(()=>document.querySelector('#kDeck [data-w="tidy"]').click()); await p.waitForTimeout(800);
await p.screenshot({path:'shots/t263-tidy.png'});
out.rects=await p.evaluate(()=>{ const r=e=>{ if(!e) return null; const b=e.getBoundingClientRect(); return [b.x,b.y,b.width,b.height].map(Math.round).join(','); }; return {pads:r(document.querySelector('#pad .pmain')),keys:r(document.getElementById('kbTop')),dj:r(document.getElementById('djSec')),kara:r(document.getElementById('kWin_kara')),seq:r(document.getElementById('kWin_seq')),seqHas:['crSec','k40Seq','rollWrap'].map(i=>i+':'+!!document.querySelector('#kWin_seq #'+i)).join(' ')}; });
// fold all then bring back
await p.evaluate(()=>document.querySelector('#kDeck [data-w="foldall"]').click()); await p.waitForTimeout(500);
out.folded=await p.evaluate(()=>['pads','keys','dj','kara','seq'].map(k=>k+':'+KWIN.state(k)).join(' '));
await p.evaluate(()=>document.querySelector('#kDeck [data-w="foldall"]').click()); await p.waitForTimeout(500);
// M on pads header
out.mute=await p.evaluate(()=>{ const hd=document.querySelector('#pad .pmain > .kFHead'); const m=hd&&hd.querySelector('[data-kw="m"]'); if(!m) return 'no M'; m.click(); const a=PADSTUDIO.MIX.slice(0,17).every(x=>x.mute); m.click(); const b=PADSTUDIO.MIX.slice(0,17).every(x=>!x.mute); return a+'/'+b; });
// bar edit: put hits in bar 1, set 4 bars, copy bar1 -> paste at bar 3, insert, delete
out.edit=await p.evaluate(async()=>{ const P=PADSTUDIO; P.setBars(4); await new Promise(r=>setTimeout(r,200)); const s=P.spbN; P.pads.forEach(x=>x.steps.fill(0)); P.pads[0].steps[0]=1; P.pads[2].steps[4]=1; const cnt=b=>P.pads.reduce((a,x)=>a+x.steps.slice(b*s,b*s+s).filter(Boolean).length,0);
 KDECK.SEL.from=0; KDECK.SEL.len=1; KDECK.ED.copy(); KDECK.SEL.at=2; KDECK.ED.paste(); const r1=[0,1,2,3].map(cnt).join('');
 KDECK.SEL.from=1; KDECK.SEL.len=1; KDECK.ED.insert(); await new Promise(r=>setTimeout(r,200)); const r2=P.barsN+':'+[...Array(P.barsN).keys()].map(cnt).join('');
 KDECK.SEL.from=1; KDECK.SEL.len=1; KDECK.ED.del(); await new Promise(r=>setTimeout(r,200)); const r3=P.barsN+':'+[...Array(P.barsN).keys()].map(cnt).join('');
 KDECK.SEL.from=0; KDECK.ED.dup(); const r4=P.barsN+':'+[...Array(P.barsN).keys()].map(cnt).join('');
 KUNDO.any(); const r5=P.barsN+':'+[...Array(P.barsN).keys()].map(cnt).join('');
 return {copyPaste:r1,insert:r2,del:r3,dup:r4,undo:r5}; });
// automation: latch, play, move fader of strip 3 while playing, stop, read back
out.auto=await p.evaluate(async()=>{ const sl=ms=>new Promise(r=>setTimeout(r,ms)); const P=PADSTUDIO; P.setBars(1); await sl(150); const sel=document.querySelector('#kDeck [data-d="amode"]'); KDECK.AU.mode='latch';
 P.play(); await sl(300); const f=document.querySelector('#padMixer .mxs[data-c="3"] input.mxv'); const vals=[20,40,60,80,100,120,140,60,30];
 for(const v of vals){ f.value=String(v); f.dispatchEvent(new Event('input',{bubbles:true})); await sl(220); }
 await sl(800); P.stop(); await sl(500); const L=KDECK.lane(3); const written=L.v.slice(0,16).filter(x=>x!=null).length; const uniq=new Set(L.v.slice(0,16).filter(x=>x!=null).map(x=>Math.round(x*100))).size;
 KDECK.AU.mode='read'; f.value='90'; f.dispatchEvent(new Event('input',{bubbles:true})); P.play(); const seen=new Set(); for(let i=0;i<20;i++){ await sl(100); seen.add(f.value); } P.stop(); await sl(300);
 const pk=KDECK.auPack(); return {mode:KDECK.AU.mode,written,uniq,readMoves:seen.size,packCh:Object.keys(pk.ch).join(','),stripApi:typeof P.strip}; });
// punch guard: 4 bars, punch bars 2-3, rec pads while hitting pads outside
out.punch=await p.evaluate(async()=>{ const sl=ms=>new Promise(r=>setTimeout(r,ms)); const P=PADSTUDIO; P.setBars(4); await sl(200); P.pads.forEach(x=>x.steps.fill(0)); P.pads[5].steps[0]=1; P.pads[5].steps[60]=1; const before=P.pads.map(x=>x.steps.slice(0,64));
 KDECK.PU.on=true; KDECK.PU.inB=2; KDECK.PU.outB=3; KDECK.PU.rep=false; const rb=document.getElementById('padRecLive'); P.play(); await sl(100); rb.click(); const spbms=P.stepDur()*1000; const t0=performance.now(); let hits=0;
 while(performance.now()-t0<spbms*64*1.05){ P.hitPad(1); hits++; await sl(spbms*2); }
 rb.click(); P.stop(); await sl(400); const s=P.spbN; let outside=0, inside=0; P.pads.forEach((x,i)=>{ for(let k=0;k<64;k++){ if(x.steps[k]!==before[i][k]){ if(k>=s&&k<3*s) inside++; else outside++; } } }); KDECK.PU.on=false; return {hits,inside,outside,kept:P.pads[5].steps[0]+','+P.pads[5].steps[60]}; });
// link strips 5 and 6
out.link=await p.evaluate(()=>{ const P=PADSTUDIO; KWIN.LINK.clear(); KWIN.LINK.add(5); KWIN.LINK.add(6); P.MIX[5].vol=.5; P.MIX[6].vol=.7; const f=document.querySelector('#padMixer .mxs[data-c="5"] input.mxv'); f.value='80'; f.dispatchEvent(new Event('input',{bubbles:true})); const r=P.MIX[5].vol.toFixed(2)+'/'+P.MIX[6].vol.toFixed(2); KWIN.LINK.clear(); return r; });
// dj wide
out.dj=await p.evaluate(()=>{ const d=document.getElementById('djSec'); const w=[...document.getElementById('djWrap').children].map(x=>{ const b=x.getBoundingClientRect(); return Math.round(b.x)+':'+Math.round(b.width); }).join(' '); return {wide:d.classList.contains('kdjWide'),w}; });
console.log(JSON.stringify(out,null,1)); console.log('errs',errs.slice(0,8)); await b.close(); })();
