const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
await p.evaluate(()=>GAMES.open('pro_strike')); await p.waitForTimeout(1200); await p.evaluate(()=>{ [...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Start/.test(x.textContent)).click(); }); await p.waitForTimeout(500);
const st=()=>p.evaluate(()=>GAMES._cur().state());
const s0=await st(); await p.keyboard.down('w'); await p.waitForTimeout(800); await p.keyboard.up('w'); await p.keyboard.down('ArrowRight'); await p.waitForTimeout(500); await p.keyboard.up('ArrowRight'); const s1=await st();
const fps=await p.evaluate(()=>new Promise(r=>{ let n=0; const t0=performance.now(); const f=()=>{ n++; if(performance.now()-t0<2000) requestAnimationFrame(f); else r(Math.round(n/2)); }; requestAnimationFrame(f); }));
// aim at the nearest foe and fire
const shot=await p.evaluate(async()=>{ const i=GAMES._cur(); const s=i.state(); return s; });
for(let k=0;k<8;k++){ await p.evaluate(()=>{ const i=GAMES._cur(); }); await p.keyboard.down('Space'); await p.waitForTimeout(400); await p.keyboard.up('Space'); }
const s2=await st(); await p.keyboard.press('r'); await p.waitForTimeout(1600); const s3=await st(); await p.keyboard.press('2'); await p.waitForTimeout(100); const s4=await st();
await p.screenshot({path:'shots/g-strike.png'});
// teleport next to a terminal and wait for hack
const hk=await p.evaluate(async()=>{ const i=GAMES._cur(); i.tp(19.5,3.5); await new Promise(r=>setTimeout(r,3600)); return i.state().hack; });
const c=await p.evaluate(()=>{ const i=GAMES._cur(); const btn=[...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Cannon:/.test(x.textContent)); if(/off/.test(btn.textContent)) btn.click(); i.F.charge=1; const f0=i.state().foes; i.F.fire(); return f0; }); await p.waitForTimeout(1200); const s5=await st();
console.log(JSON.stringify({s0:[s0.x,s0.y,s0.a],s1:[s1.x,s1.y,s1.a],fps,s2:{foes:s2.foes,score:s2.score,ammo:s2.ammo,hp:s2.hp},s3:s3.ammo,wi:s4.wi,hack:hk,cannon:{before:c,after:s5.foes,score:s5.score}})); console.log('errs',errs.slice(0,5)); await b.close(); })();
