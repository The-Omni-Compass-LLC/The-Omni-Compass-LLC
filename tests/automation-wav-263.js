const {chromium}=require('playwright');(async()=>{ const b=await chromium.launch(); const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8771/pub7/ptest.html'); await p.waitForTimeout(5000); await p.evaluate(()=>{ const a=document.getElementById('kAgree'); if(a) a.hidden=true; KAUDIO.gesture&&KAUDIO.gesture(); });
await p.evaluate(()=>{ PADSTUDIO.open(); }); await p.waitForTimeout(2000);
const r=await p.evaluate(async()=>{ const sl=ms=>new Promise(r=>setTimeout(r,ms)); const P=PADSTUDIO; P.setBars(1); await sl(150); P.pads.forEach(x=>x.steps.fill(0)); for(let s=0;s<16;s++) P.pads[0].steps[s]=1;
 const rms=async()=>{ const buf=await P.renderBeat(1); const d=buf.getChannelData(0); const n=d.length, h=Math.floor(n/2); let a=0,b2=0; for(let i=0;i<h;i++) a+=d[i]*d[i]; for(let i=h;i<n;i++) b2+=d[i]*d[i]; return [Math.sqrt(a/h),Math.sqrt(b2/(n-h))]; };
 KDECK.AU.mode='off'; const flat=await rms();
 const L=KDECK.lane(0); for(let s=0;s<16;s++) L.v[s]=s<8?1:0.05; KDECK.AU.mode='read'; const auto=await rms();
 // write mode: arm strip 2, play briefly, stop → mode touch
 L.v.fill(null); KDECK.AU.mode='write'; KDECK.lane(2).arm=true; P.play(); await sl(900); P.stop(); await sl(600); const after=KDECK.AU.mode; const w=KDECK.lane(2).v.filter(x=>x!=null).length; KDECK.lane(2).arm=false; KDECK.lane(2).v.fill(null); KDECK.lane(2).p.fill(null); KDECK.AU.mode='read';
 return {flat:flat.map(x=>x.toFixed(4)),auto:auto.map(x=>x.toFixed(4)),ratio2nd:(auto[1]/flat[1]).toFixed(3),ratio1st:(auto[0]/flat[0]).toFixed(3),writeThen:after,writtenSteps:w}; });
console.log(JSON.stringify(r)); console.log('errs',errs.slice(0,5)); await b.close(); })();
