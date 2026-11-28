const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
await p.evaluate(()=>GAMES.open('pro_fight')); await p.waitForTimeout(1200); await p.evaluate(()=>{ [...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Start/.test(x.textContent)).click(); }); await p.waitForTimeout(2600);
const st=()=>p.evaluate(()=>GAMES._cur().state());
await p.keyboard.down('ArrowRight'); await p.waitForTimeout(900); await p.keyboard.up('ArrowRight');
let s0=await st(); for(let i=0;i<14;i++){ await p.keyboard.press('z'); await p.waitForTimeout(300); } const s1=await st();
for(let i=0;i<4;i++){ await p.keyboard.press('z'); await p.waitForTimeout(80); await p.keyboard.press('z'); await p.waitForTimeout(280); await p.keyboard.press('x'); await p.waitForTimeout(500); } const s2=await st();
const c=await p.evaluate(()=>{ const i=GAMES._cur(); const btn=[...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Cannon:/.test(x.textContent)); if(/off/.test(btn.textContent)) btn.click(); i.F.charge=1; const e0=i.state().ehp; i.F.fire(); return {e0,e1:i.state().ehp}; });
console.log(JSON.stringify({s0,s1,s2,c})); console.log('errs',errs); await b.close(); })();
