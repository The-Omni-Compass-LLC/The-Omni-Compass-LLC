const {chromium,devices}=require('playwright');
(async()=>{ const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']}); const out={};
 for(const [dev,opt] of [['laptop',{viewport:{width:1440,height:900}}],['phone',devices['iPhone 13']]]){
  const ctx=await b.newContext(opt); const p=await ctx.newPage(); let errs=[]; p.on('pageerror',e=>errs.push((e.message||'').slice(0,140)));
  await p.goto('http://localhost:8771/pub6/ptest.html',{waitUntil:'load'}); await p.waitForTimeout(4000);
  await p.evaluate(()=>{ try{ sessionStorage.setItem('kanin-agree-s','1'); }catch(_){ } const a=document.getElementById('kAgree'); if(a) a.hidden=true; document.body.classList.remove('gated'); });
  const home=async()=>{ await p.evaluate(()=>{ try{ GOHOME(); }catch(_){ } try{ KRAIL.goTo('home'); }catch(_){ } ['kLegal','kServices','kSports','kNews','kMarket','kRelig','kKnow','kAcct','kSndSheet'].forEach(id=>{ const x=document.getElementById(id); if(x) x.hidden=true; }); }); await p.waitForTimeout(500); };
  const openMenu=async()=>{ await p.evaluate(()=>{ const m=document.getElementById('lpMenu'); if(m) m.click(); }); await p.waitForTimeout(700); };
  await openMenu();
  const labels=await p.evaluate(()=>[...document.querySelectorAll('#tourTab button')].filter(x=>x.getClientRects().length).map(x=>x.textContent.trim()).filter(t=>t&&!/^(Hide|✕|Close)/.test(t)));
  const rows=[];
  const probe=()=>p.evaluate(()=>{ const vis=el=>{ const s=getComputedStyle(el),r=el.getBoundingClientRect(); return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0; };
    const tops=[...document.querySelectorAll('body > *, body > * > [id]')].filter(el=>{ const s=getComputedStyle(el); return (s.position==='fixed'||s.position==='absolute')&&vis(el)&&el.getBoundingClientRect().height>300&&el.getBoundingClientRect().width>280&&!/bgfx|flashbang|kShotCv|tourRing|rDock|kPanelStrip|padBg/.test(el.id); });
    const top=tops.sort((a,b)=>(+getComputedStyle(b).zIndex||0)-(+getComputedStyle(a).zIndex||0))[0];
    let cur=''; try{ cur=KRAIL.cur(); }catch(_){ }
    const root=top||document.body; const btns=[...root.querySelectorAll('button')].filter(vis);
    const close=btns.some(x=>/✕|Close|Back/.test(x.textContent))||!!document.querySelector('[data-rbtn="close"],#kRemote [data-r="close"]');
    const tabs=[...root.querySelectorAll('[role=tab],.tabs button,.kTabs button,.vgTabs button,.svRow button,[data-tab]')].filter(vis).length;
    return {cur,top:top?(top.id||top.className.split(' ')[0]):'(page)',btns:btns.length,tabs,close,wide:document.documentElement.scrollWidth>innerWidth+2}; });
  for(const L of labels){ errs=[]; await home(); await openMenu();
   await p.evaluate(L=>{ const x=[...document.querySelectorAll('#tourTab button')].find(b=>b.textContent.trim()===L); if(x) x.click(); },L); await p.waitForTimeout(1400);
   const r=await probe();
   /* click every tab on that screen */
   const tabErr=await p.evaluate(async()=>{ const sl=ms=>new Promise(r=>setTimeout(r,ms)); const vis=el=>el.getClientRects().length>0; const T=[...document.querySelectorAll('[role=tab],.kTabs button,.vgTabs button,.svRow button[data-sv="cat"],.sbTabs button')].filter(vis).slice(0,40); let n=0; for(const t of T){ try{ t.click(); n++; }catch(e){ return 'tab error '+e.message; } await sl(60); } return n; });
   rows.push({L,...r,tabsClicked:tabErr,errs:errs.slice(0,2)}); }
  /* the rail */
  const rail=await p.evaluate(()=>[...document.querySelectorAll('#rDock button,#kRail button,.kRail button')].filter(x=>x.getClientRects().length).map(x=>x.textContent.trim()).filter(Boolean));
  const railRows=[];
  for(const L of rail){ errs=[]; await home(); await p.evaluate(L=>{ const x=[...document.querySelectorAll('#rDock button,#kRail button,.kRail button')].find(b=>b.textContent.trim()===L&&b.getClientRects().length); if(x) x.click(); },L); await p.waitForTimeout(1300); const r=await probe(); railRows.push({L,...r,errs:errs.slice(0,2)}); }
  out[dev]={menu:rows,rail:railRows}; await ctx.close(); }
 require('fs').writeFileSync('shots/tmenu255.json',JSON.stringify(out,null,1));
 for(const [d,o] of Object.entries(out)){ const bad=o.menu.filter(r=>r.errs.length||(r.top==='(page)'&&!r.cur)||!r.close||r.wide); const badR=o.rail.filter(r=>r.errs.length||r.wide);
  console.log(d,'menu entries',o.menu.length,'rail',o.rail.length,'problems',bad.length+badR.length); bad.concat(badR).forEach(r=>console.log('  ',JSON.stringify(r))); }
 await b.close(); })();
