(()=>{ /* 🧾 SERVICES (v249): a platform of links to the services people need most, each opening the provider's own official website in a
   new tab: ⭐ the top 20, then every category (government, health insurance, car insurance, mortgages and homes, banking and credit,
   jobs, shopping and delivery, travel and rides, phone and internet, taxes and legal). KAN-IN is not affiliated with any of them,
   takes no payment through them, and asks nothing of the person; it only links. The 💥 cannon picks a service. */
 const $=id=>document.getElementById(id); const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const say=m=>{ try{ toast(m); }catch(_){ } };
 const C=[['gov','🏛','Government',[['USA.gov · every U.S. government service','https://www.usa.gov'],['IRS · taxes and refunds','https://www.irs.gov'],['Social Security','https://www.ssa.gov'],['Medicare','https://www.medicare.gov'],['USPS · mail, stamps, tracking','https://www.usps.com'],['Passports (State Department)','https://travel.state.gov'],['Veterans Affairs','https://www.va.gov'],['Federal Student Aid (FAFSA)','https://studentaid.gov'],['Login.gov','https://www.login.gov'],['USAJOBS · federal jobs','https://www.usajobs.gov']]],
  ['health','🩺','Health insurance',[['HealthCare.gov · marketplace plans','https://www.healthcare.gov'],['Medicaid','https://www.medicaid.gov'],['UnitedHealthcare','https://www.uhc.com'],['Blue Cross Blue Shield','https://www.bcbs.com'],['Aetna','https://www.aetna.com'],['Cigna','https://www.cigna.com'],['Kaiser Permanente','https://www.kp.org']]],
  ['car','🚗','Car insurance',[['GEICO','https://www.geico.com'],['Progressive','https://www.progressive.com'],['State Farm','https://www.statefarm.com'],['Allstate','https://www.allstate.com'],['USAA (military families)','https://www.usaa.com'],['Liberty Mutual','https://www.libertymutual.com']]],
  ['home','🏠','Mortgages and homes',[['Rocket Mortgage','https://www.rocketmortgage.com'],['Zillow','https://www.zillow.com'],['Realtor.com','https://www.realtor.com'],['Redfin','https://www.redfin.com'],['Consumer Financial Protection Bureau · mortgage help','https://www.consumerfinance.gov']]],
  ['bank','💳','Banking and credit',[['Chase','https://www.chase.com'],['Bank of America','https://www.bankofamerica.com'],['Wells Fargo','https://www.wellsfargo.com'],['Capital One','https://www.capitalone.com'],['AnnualCreditReport.com · free credit reports','https://www.annualcreditreport.com'],['Credit Karma','https://www.creditkarma.com']]],
  ['jobs','💼','Jobs',[['Indeed','https://www.indeed.com'],['LinkedIn','https://www.linkedin.com'],['USAJOBS','https://www.usajobs.gov']]],
  ['shop','🛒','Shopping and delivery',[['Amazon','https://www.amazon.com'],['Walmart','https://www.walmart.com'],['Target','https://www.target.com'],['Instacart','https://www.instacart.com'],['DoorDash','https://www.doordash.com']]],
  ['travel','✈️','Travel and rides',[['Uber','https://www.uber.com'],['Lyft','https://www.lyft.com'],['Expedia','https://www.expedia.com'],['Airbnb','https://www.airbnb.com']]],
  ['phone','📡','Phone and internet',[['Verizon','https://www.verizon.com'],['AT&T','https://www.att.com'],['T-Mobile','https://www.t-mobile.com']]],
  ['legal','⚖️','Taxes and legal',[['IRS Free File','https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free'],['TurboTax','https://turbotax.intuit.com'],['LegalZoom','https://www.legalzoom.com']]]];
 const TOP=['USA.gov · every U.S. government service','IRS · taxes and refunds','Social Security','HealthCare.gov · marketplace plans','Medicare','USPS · mail, stamps, tracking','GEICO','Progressive','State Farm','Rocket Mortgage','Zillow','Chase','AnnualCreditReport.com · free credit reports','Indeed','LinkedIn','Amazon','Uber','Expedia','TurboTax','USAJOBS · federal jobs'];
 const ALL=[]; C.forEach(([k,i,l,L])=>L.forEach(([n,u])=>{ if(!ALL.some(x=>x.n===n)) ALL.push({k,i,n,u,cat:l}); }));
 let cat='top', q='';
 const css=document.createElement('style'); css.textContent=`
#kServices{position:fixed;inset:0;right:var(--kRailW,58px);z-index:8560;overflow-y:auto;background:radial-gradient(circle at 50% 0,#13285a,#050914 70%);color:#eef4ff;font:15px/1.5 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 40px}
#kServices[hidden]{display:none!important}
#kServices .svIn{max-width:1100px;margin:0 auto}
#kServices h2{font:900 28px/1.1 system-ui,sans-serif;margin:4px 0;color:#8fc4ff}
#kServices .svTop{display:flex;justify-content:space-between;align-items:center;gap:8px}
#kServices .svRow{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
#kServices button{min-height:44px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif}
#kServices .svRow button.on{background:#8fc4ff!important;color:#050914!important}
#kServices input[type=search]{width:100%;box-sizing:border-box;min-height:46px;border-radius:12px;padding:0 14px;font:16px system-ui,sans-serif}
#kServices .svGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-top:10px}
#kServices .svCard{background:linear-gradient(160deg,rgba(24,44,90,.85),rgba(8,14,32,.9));border:1px solid rgba(143,196,255,.35);border-radius:4px 16px 4px 16px;padding:12px;display:flex;flex-direction:column;gap:6px}
#kServices .svCard b{font:900 15.5px system-ui,sans-serif}
#kServices .svCard small{color:#a9c8ff;font-weight:700}
#kServices .svCard a{align-self:flex-start;padding:6px 12px;border-radius:3px 10px 3px 10px;background:#8fc4ff;color:#050914;font:900 13px system-ui,sans-serif;text-decoration:none}
#kServices .svCard.hl{outline:3px solid #ffe94a}
#kServices .svNote{font-size:13px;opacity:.85;margin-top:14px}`; document.head.appendChild(css);
 function box(){ let d=$('kServices'); if(d) return d; d=document.createElement('div'); d.id='kServices'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Services'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-sv]'); if(!b) return; e.stopPropagation(); const k=b.dataset.sv; if(k==='x') return close(); if(k==='cat'){ cat=b.dataset.v; q=''; paint(); } if(k==='rand') random(); });
  d.addEventListener('input',e=>{ if(e.target.dataset.sv==='q'){ q=e.target.value; grid(); } }); return d; }
 const list=()=>{ if(q) return ALL.filter(x=>(x.n+' '+x.cat).toLowerCase().includes(q.toLowerCase())); if(cat==='top') return TOP.map(n=>ALL.find(x=>x.n===n)).filter(Boolean); return ALL.filter(x=>x.k===cat); };
 function grid(){ const g=$('kServices')&&$('kServices').querySelector('.svGrid'); if(!g) return; const L=list(); g.innerHTML=L.map((x,i)=>'<div class="svCard" data-n="'+esc(x.n)+'"><b>'+(cat==='top'&&!q?(i+1)+'. ':'')+x.i+' '+esc(x.n)+'</b><small>'+esc(x.cat)+'</small><a href="'+x.u+'" target="_blank" rel="noopener">Open the official site ↗</a></div>').join('')||'<p>No service matches.</p>'; }
 function paint(){ const d=$('kServices'); if(!d||d.hidden) return; d.innerHTML='<div class="svIn"><div class="svTop"><h2>🧾 Services</h2><button type="button" data-sv="x" data-noul>✕ Close</button></div><p>The services people need most, one tap to each one’s own official website.</p><div class="svRow"><button type="button" data-sv="cat" data-v="top" class="'+(cat==='top'?'on':'')+'" data-noul>⭐ Top 20</button>'+C.map(([k,i,l])=>'<button type="button" data-sv="cat" data-v="'+k+'" class="'+(cat===k?'on':'')+'" data-noul>'+i+' '+esc(l)+'</button>').join('')+'<button type="button" data-sv="rand" data-noul>💥 Pick one</button></div><input type="search" data-sv="q" placeholder="🔎 Search '+ALL.length+' services" value="'+esc(q)+'"><div class="svGrid"></div><p class="svNote">These links open the providers’ own websites in a new tab. KAN-IN is not affiliated with them, takes no payment through them and asks you for nothing. Check the address bar before entering personal details: government sites end in .gov.</p><p class="svNote">© 2026 The Omni-Compass LLC and Omni-Galaxy Multi-Media Studios. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com</p></div>'; grid(); }
 function random(){ cat='top'; q=''; paint(); const L=list(); const i=Math.floor(Math.random()*L.length); const c=$('kServices').querySelectorAll('.svCard')[i]; if(c){ c.classList.add('hl'); c.scrollIntoView({block:'center',behavior:'smooth'}); setTimeout(()=>c.classList.remove('hl'),2500); say('💥 '+L[i].n); } }
 function open(c){ const d=box(); if(typeof c==='string') cat=c; try{ ['kKnow','kNews','kRelig','kMarket','kKara','kAcct','kSports'].forEach(id=>{ const x=$(id); if(x&&x!==d) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } d.hidden=false; paint(); }
 function close(){ const d=$('kServices'); if(d) d.hidden=true; }
 const hook=()=>{ try{ if(window.KCANNON&&!KCANNON.SHOT.kServices){ KCANNON.SHOT.kServices=()=>{ random(); return true; }; KCANNON.NAME.kServices='Services'; } }catch(_){ } }; hook(); setTimeout(hook,3000);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Platforms','🧾','Services: government, insurance, mortgages, banking, jobs and more, with links','Services',()=>open()); });
 window.KSERVICES={open,close,random,count:()=>ALL.length};
})();
