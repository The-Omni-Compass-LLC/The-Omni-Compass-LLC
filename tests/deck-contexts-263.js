const {chromium,devices}=require('playwright');(async()=>{ const b=await chromium.launch(); const out={};
{ const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub7/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
// DJ context
await p.evaluate(()=>{ PADSTUDIO.open(); }); await p.waitForTimeout(2000); await p.evaluate(()=>{ KRAIL.FLOAT.close('pads'); KRAIL.FLOAT.open('dj'); }); await p.waitForTimeout(900);
await p.mouse.click(700,30); await p.waitForTimeout(600);
out.djCx=await p.evaluate(()=>KDECK.cx); out.djWide=await p.evaluate(()=>{ const d=document.getElementById('djSec'); const r=d.getBoundingClientRect(); return d.classList.contains('kdjWide')+' w'+Math.round(r.width)+' '+[...document.getElementById('djWrap').children].map(x=>Math.round(x.getBoundingClientRect().x)).join(','); });
await p.screenshot({path:'shots/t263-dj.png'});
const m0=await p.evaluate(()=>KWIRE.mode); await p.keyboard.press('Digit1'); await p.waitForTimeout(300); out.djKey=m0+'→'+await p.evaluate(()=>KWIRE.mode);
await p.evaluate(()=>KWIRE.setMode('beat'));
// karaoke context
await p.evaluate(()=>KKARA.open()); await p.waitForTimeout(1500);
out.karaCx=await p.evaluate(()=>KDECK.cx);
await p.evaluate(()=>{ const b=document.querySelector('#kDeck [data-w="kara"]'); b&&b.click(); }); await p.waitForTimeout(800);
out.karaWin=await p.evaluate(()=>{ const w=document.getElementById('kWin_kara'); const r=w.getBoundingClientRect(); return {hidden:w.hidden,par:w.parentElement.tagName,z:getComputedStyle(w).zIndex,r:[r.x,r.y,r.width,r.height].map(Math.round).join(','),btns:w.querySelectorAll('button').length,sel:[...w.querySelectorAll('select')].map(x=>x.options.length).join(',')}; });
const hit0=await p.evaluate(()=>window.LASTKEYPAD||null);
await p.keyboard.press('KeyQ'); await p.waitForTimeout(900);
out.karaQ=await p.evaluate(()=>({over:document.body.classList.contains('kDevOver'),padsOpen:KRAIL.FLOAT.isOpen('pads')}));
await p.keyboard.down('KeyY'); await p.waitForTimeout(700); await p.keyboard.up('KeyY'); await p.waitForTimeout(300);
out.karaY=await p.evaluate(()=>({keysOpen:KRAIL.FLOAT.isOpen('keys')}));
await p.screenshot({path:'shots/t263-kara.png'});
out.errs=errs.slice(0,6); }
{ const p=await (await b.newContext({...devices['iPhone 13']})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub7/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; });
await p.evaluate(()=>{ PADSTUDIO.open(); }); await p.waitForTimeout(2000);
out.phone=await p.evaluate(()=>{ const d=document.getElementById('kDeck'); const r=d.getBoundingClientRect(); return {hidden:d.hidden,min:d.classList.contains('min'),r:[r.x,r.y,r.width,r.height].map(Math.round).join(','),vw:innerWidth,sx:document.documentElement.scrollWidth}; });
await p.evaluate(()=>KDECK.act('fold')); await p.waitForTimeout(400);
out.phoneOpen=await p.evaluate(()=>{ const d=document.getElementById('kDeck'); const r=d.getBoundingClientRect(); const over=[...d.querySelectorAll('button')].filter(b=>{ const q=b.getBoundingClientRect(); return q.right>innerWidth+1||q.left<-1; }).length; return {r:[r.x,r.y,r.width,r.height].map(Math.round).join(','),over,small:[...d.querySelectorAll('button')].filter(b=>b.getBoundingClientRect().height<34&&b.getClientRects().length).length}; });
await p.screenshot({path:'shots/t263-phone.png'});
out.phoneErrs=errs.slice(0,6); }
console.log(JSON.stringify(out,null,1)); await b.close(); })();
