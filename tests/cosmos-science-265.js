const {chromium,devices}=require('playwright');(async()=>{ const b=await chromium.launch(); const out={};
for(const [n,o] of [['laptop',{viewport:{width:1440,height:900}}],['phone',devices['iPhone 13']]]){ const p=await (await b.newContext(o)).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; }); await p.waitForTimeout(800);
const R={}; R.nowbar=await p.evaluate(()=>{ const b=document.getElementById('kNowBar'); return b?[...b.querySelectorAll('button')].map(x=>x.textContent).join(' | '):'none'; });
// menu
await p.evaluate(()=>document.getElementById('lpMenu').click()); await p.waitForTimeout(900);
R.menu=await p.evaluate(()=>{ const t=document.getElementById('tourTab'); const btns=[...t.querySelectorAll('button')].filter(x=>x.getClientRects().length&&+getComputedStyle(x).order>=30&&+getComputedStyle(x).order<90); const L=btns.filter(x=>getComputedStyle(x).gridColumnStart==='1').length, Rr=btns.filter(x=>getComputedStyle(x).gridColumnStart==='2').length; const cos=btns.find(x=>/Cosmos/.test(x.textContent)), sci=btns.find(x=>/Science & Tech/.test(x.textContent)); const heads=[...t.querySelectorAll('.kMenuC')].map(h=>h.textContent+'@'+Math.round(h.getBoundingClientRect().top)).join(' | '); return {left:L,right:Rr,cos:cos&&cos.textContent,sci:sci&&sci.textContent,heads}; });
await p.evaluate(()=>{ const t=document.getElementById('tourTab'); [...t.querySelectorAll('button')].find(x=>/Cosmos ·/.test(x.textContent)).click(); }); await p.waitForTimeout(1500);
R.cosmos=await p.evaluate(()=>{ const d=document.getElementById('kCosmos'); const cv=document.getElementById('cosOrr'); return {open:!d.hidden,cards:d.querySelectorAll('.pCard').length,tabs:[...d.querySelectorAll('[data-p="cab"]')].map(x=>x.textContent).join(' | '),sky:(d.querySelectorAll('.pPanel')[1]||{}).textContent.slice(0,260),cv:cv?Math.round(cv.getBoundingClientRect().width):0,date:(document.getElementById('cosDate')||{}).textContent,sx:document.documentElement.scrollWidth+'/'+innerWidth}; });
await p.evaluate(()=>{ const i=document.querySelector('#kCosmos input[type=search]'); i.value='black hole'; i.dispatchEvent(new Event('input',{bubbles:true})); }); await p.waitForTimeout(300);
R.search=await p.evaluate(()=>document.querySelectorAll('#kCosmos .pCard').length);
await p.evaluate(()=>{ document.querySelector('#kCosmos [data-p="spd"][data-v="12"]').click(); }); await p.waitForTimeout(1200); R.orrDate=await p.evaluate(()=>(document.getElementById('cosDate')||{}).textContent);
await p.screenshot({path:'shots/c-cosmos-'+n+'.png'});
await p.keyboard.press('Escape'); await p.waitForTimeout(300); R.escClosed=await p.evaluate(()=>document.getElementById('kCosmos').hidden);
await p.evaluate(()=>KSCI.open()); await p.waitForTimeout(1000);
R.sci=await p.evaluate(()=>{ const d=document.getElementById('kSci'); const els=d.querySelectorAll('.pel'); const fe=[...els].find(x=>x.dataset.z==='26'); fe.click(); const info=d.querySelector('.pElInfo').textContent; const t=d.querySelector('.ptab').getBoundingClientRect(); return {els:els.length,cards:d.querySelectorAll('.pCard').length,tabs:d.querySelectorAll('[data-p="cab"]').length,info:info.slice(0,160),tab:[t.width,t.height].map(Math.round).join('x'),sx:document.documentElement.scrollWidth+'/'+innerWidth}; });
await p.screenshot({path:'shots/c-sci-'+n+'.png'});
R.rand=await p.evaluate(()=>{ KSCI.random(); return !!document.querySelector('#kSci .pCard.hl'); });
out[n]={R,errs:errs.slice(0,5)}; }
console.log(JSON.stringify(out,null,1)); await b.close(); })();
