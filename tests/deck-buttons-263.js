const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{ window.__toasts=[]; const t=setInterval(()=>{ if(window.toast&&!window.toast.__w){ const o=window.toast; window.toast=function(m){ window.__toasts.push(String(m)); return o.apply(this,arguments); }; window.toast.__w=1; } },50); });
await p.goto('http://localhost:8771/pub6/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
await p.evaluate(()=>{ PADSTUDIO.open(); }); await p.waitForTimeout(2000); await p.evaluate(()=>PADSTUDIO.setBars(4)); await p.waitForTimeout(300);
const res=[]; const skip=/new|open|save|wav|upload|loadsnd|lib|fold|tools/;
const tabs=await p.evaluate(()=>[...document.querySelectorAll('#kDeck [data-tab]')].map(x=>x.dataset.tab));
for(const t of tabs){ await p.evaluate(t=>document.querySelector('#kDeck [data-tab="'+t+'"]').click(),t); await p.waitForTimeout(300);
 const ds=await p.evaluate(()=>[...document.querySelectorAll('#kDeck .kdPane button[data-d]')].map(x=>x.dataset.d));
 for(const d of ds){ if(skip.test(d)) { res.push(t+'/'+d+':skipped(file dialog or page)'); continue; } const before=await p.evaluate(()=>({h:document.getElementById('kDeck').innerHTML.length,t:window.__toasts.length,s:JSON.stringify([KDECK.PU,KDECK.AU.mode,KDECK.SEL,PADSTUDIO.playing,PADSTUDIO.barsN])}));
  const ok=await p.evaluate(d=>{ const b=document.querySelector('#kDeck .kdPane button[data-d="'+d+'"]'); if(!b) return false; b.click(); return true; },d); await p.waitForTimeout(250);
  const after=await p.evaluate(()=>({h:document.getElementById('kDeck').innerHTML.length,t:window.__toasts.length,s:JSON.stringify([KDECK.PU,KDECK.AU.mode,KDECK.SEL,PADSTUDIO.playing,PADSTUDIO.barsN])}));
  const eff=after.t>before.t||after.s!==before.s||after.h!==before.h; res.push(t+'/'+d+':'+(ok?(eff?'ok':'NO EFFECT'):'missing')); }
 await p.evaluate(()=>{ try{ PADSTUDIO.stop(); }catch(_){ } }); }
// transport
for(const d of ['play','stop','rew','loop','bpm+','bpm-']){ const b0=await p.evaluate(()=>[PADSTUDIO.playing,document.getElementById('padBpm').value,(document.getElementById('ktLoop')||{}).className].join()); await p.evaluate(d=>document.querySelector('#kDeck .kdT [data-d="'+d+'"]').click(),d); await p.waitForTimeout(250); const b1=await p.evaluate(()=>[PADSTUDIO.playing,document.getElementById('padBpm').value,(document.getElementById('ktLoop')||{}).className].join()); res.push('T/'+d+':'+(b0!==b1||d==='stop'||d==='rew'?'ok':'NO EFFECT')); }
await p.evaluate(()=>{ try{ PADSTUDIO.stop(); }catch(_){ } });
console.log(res.filter(x=>!/:ok$/.test(x)).join('\n')||'all ok'); console.log('total',res.length,'errs',errs.slice(0,5)); await b.close(); })();
