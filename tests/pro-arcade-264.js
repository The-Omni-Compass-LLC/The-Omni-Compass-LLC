const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
const out={}; const sl=ms=>p.waitForTimeout(ms);
const open=async id=>{ await p.evaluate(id=>GAMES.open(id),id); await sl(1200); await p.evaluate(()=>{ const b=[...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Start/.test(x.textContent)); b&&b.click(); }); await sl(400); };
const st=()=>p.evaluate(()=>{ const i=GAMES._cur(); return i&&i.state?JSON.parse(JSON.stringify(i.state())):null; });
const cannon=async()=>{ return p.evaluate(()=>{ const btn=[...document.querySelectorAll('#gamesDock .kProBar button')].find(x=>/Cannon:/.test(x.textContent)); if(btn&&/off/.test(btn.textContent)) btn.click(); const i=GAMES._cur(); i.F.charge=1; const s0=i.F.score; const e=new KeyboardEvent('keydown',{key:'c',bubbles:true}); document.dispatchEvent(e); window.dispatchEvent(new KeyboardEvent('keydown',{key:'c',bubbles:true})); return {before:s0,charge:i.F.charge,btn:btn&&btn.textContent}; }); };
const keys=async (list,n,gap)=>{ for(let i=0;i<n;i++){ const k=list[Math.floor(Math.random()*list.length)]; await p.keyboard.down(k); await sl(gap); await p.keyboard.up(k); } };
// 1 prism
await open('pro_prism'); for(let i=0;i<30;i++){ const ks=['ArrowLeft','ArrowRight','ArrowUp','ArrowDown']; await keys(ks,2,10); await p.keyboard.press('Space'); await keys([ks[Math.floor(Math.random()*4)]],1,10); await p.keyboard.press('Space'); await sl(350); }
out.prism=await st(); const c1=await cannon(); await sl(1500); out.prismCannon={...c1,after:(await st())}; await p.screenshot({path:'shots/g-prism.png'});
// 2 maze
await open('pro_maze'); await keys(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'],40,250); out.maze=await st(); const c2=await cannon(); await sl(600); out.mazeCannon={...c2,after:await st()}; await p.screenshot({path:'shots/g-maze.png'});
// 3 fight
await open('pro_fight'); await sl(1800); for(let i=0;i<60;i++){ await keys(['ArrowRight','ArrowRight','z','x','z','s','ArrowUp','a'],1,90); } out.fight=await st(); const c3=await cannon(); await sl(700); out.fightCannon={...c3,after:await st()}; await p.screenshot({path:'shots/g-fight.png'});
// 4 mind: answer correctly in logic and math, then speed
await open('pro_mind'); for(let i=0;i<4;i++){ await p.evaluate(()=>{ const i=GAMES._cur(); const s=i.state(); if(s.mode==='mem'){ } }); await sl(100); }
await p.evaluate(()=>{ const i=GAMES._cur(); i.setMode(3); i.F.start(); }); await sl(300); for(let k=0;k<6;k++){ await p.evaluate(()=>{ const i=GAMES._cur(); const s=i.state(); i.pick(s.opts.indexOf(s.Q.ans)); }); await sl(200); } out.mindMath=await st(); await p.screenshot({path:'shots/g-mind.png'});
await p.evaluate(()=>{ const i=GAMES._cur(); i.setMode(2); i.F.start(); }); await sl(300); for(let k=0;k<4;k++){ await p.evaluate(()=>{ const i=GAMES._cur(); const s=i.state(); i.pick(s.opts.indexOf(s.Q.ans)); }); await sl(200); } out.mindLogic=await st();
const c4=await cannon(); await sl(300); out.mindCannon={...c4,after:await st()};
// 5 rune
await open('pro_rune'); await keys(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'],120,40); out.rune=await st(); const c5=await cannon(); await sl(500); out.runeCannon={...c5,after:await st()}; await p.screenshot({path:'shots/g-rune.png'});
// 6 city
await open('pro_city'); await p.keyboard.down('ArrowUp'); for(let i=0;i<20;i++){ const k=Math.random()<.5?'ArrowLeft':'ArrowRight'; await p.keyboard.down(k); await sl(220); await p.keyboard.up(k); await sl(150); } out.city=await st(); const c6=await cannon(); await sl(500); out.cityCannon={...c6,after:await st()}; await p.screenshot({path:'shots/g-city.png'}); await p.keyboard.up('ArrowUp');
out.list=await p.evaluate(()=>(Array.isArray(GAMES.list)?GAMES.list:Object.values(GAMES.list)).filter(g=>/^pro_/.test(g.id)).map(g=>g.cat+':'+g.name).join(' | '));
console.log(JSON.stringify(out,null,1)); console.log('errs',errs.slice(0,8)); await b.close(); })();
