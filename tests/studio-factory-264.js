const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const out={}; for(const [n,o] of [['laptop',{viewport:{width:1440,height:900}}],['small',{viewport:{width:1280,height:720}}]]){ const p=await (await b.newContext(o)).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
await p.evaluate(()=>{ PADSTUDIO.open(); }); await p.waitForTimeout(2500);
const R={}; R.start=await p.evaluate(()=>['pads','keys','dj','kara','seq'].map(k=>k+':'+KWIN.state(k)).join(' ')+' | row: '+[...document.querySelectorAll('#kDeck .kdWins > *')].map(x=>x.textContent.trim()).join(' / ').slice(0,120));
const inView=()=>p.evaluate(()=>{ const rs=[]; [['pads',document.querySelector('#pad .pmain')],['keys',document.getElementById('kbTop')],['dj',document.getElementById('djSec')],['kara',document.getElementById('kWin_kara')],['seq',document.getElementById('kWin_seq')]].forEach(([k,e])=>{ if(!e||!e.getClientRects().length||getComputedStyle(e).display==='none') return; const r=e.getBoundingClientRect(); rs.push(k+'['+[r.x,r.y,r.width,r.height].map(Math.round).join(',')+(r.top>=0&&r.bottom<=innerHeight+1&&r.left>=0&&r.right<=innerWidth?' IN':' OUT')+']'); }); return rs.join(' '); });
for(const k of ['pads','keys','dj']){ await p.evaluate(k=>document.querySelector('#kDeck [data-w="'+k+'"]').click(),k); await p.waitForTimeout(1600); R['after_'+k]=await inView(); }
await p.screenshot({path:'shots/t264-'+n+'.png'});
// drag pads window to the top-left corner
const hd=await p.evaluate(()=>{ const h=document.querySelector('#pad .pmain > .kFHead'); const r=h.getBoundingClientRect(); return [r.x+60,r.y+15]; });
await p.mouse.move(hd[0],hd[1]); await p.mouse.down(); await p.mouse.move(80,30,{steps:8}); await p.mouse.up(); await p.waitForTimeout(1500);
R.dragged=await p.evaluate(()=>{ const r=document.querySelector('#pad .pmain').getBoundingClientRect(); return [r.x,r.y].map(Math.round).join(','); });
out[n]={R,errs:errs.slice(0,4)}; }
// key opens pads in studio
{ const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); PADSTUDIO.open(); }); await p.waitForTimeout(2500);
 await p.keyboard.press('KeyQ'); await p.waitForTimeout(800); await p.keyboard.down('KeyU'); await p.waitForTimeout(500); await p.keyboard.up('KeyU'); await p.waitForTimeout(600);
 out.keys=await p.evaluate(()=>'pads:'+KRAIL.FLOAT.isOpen('pads')+' keys:'+KRAIL.FLOAT.isOpen('keys')); }
console.log(JSON.stringify(out,null,1)); await b.close(); })();
