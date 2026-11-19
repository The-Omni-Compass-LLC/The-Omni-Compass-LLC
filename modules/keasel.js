(()=>{ /* 🎨 THE EASEL: draw, sketch, paint and design. Pencil, brush, marker, spray, eraser, line, box, circle, text, fill bucket,
   colors, sizes, see-through; add or paste a picture; undo and redo; clear; save to My library, post to Social, download. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } }, putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 const TOOLS=[['pencil','✏','Pencil'],['brush','🖌','Brush'],['marker','🖍','Marker'],['spray','💨','Spray'],['eraser','🧽','Eraser'],['line','／','Line'],['rect','▭','Box'],['ellipse','◯','Circle'],['text','🔤','Text'],['fill','🪣','Fill']];
 const SW=['#000000','#ffffff','#7f7f7f','#ff1744','#ff9100','#ffea00','#00e676','#00b0ff','#2962ff','#d500f9','#ff4081','#8d6e63','#ffcdd2','#c8e6c9','#bbdefb','#fff9c4','#14163a','#ffe94a','#6fe8ff','#7cff8a'];
 const SIZES=[['square','Square 1080 × 1080',1080,1080],['portrait','Post 1080 × 1350',1080,1350],['story','Story 1080 × 1920',1080,1920],['wide','Wide 1920 × 1080',1920,1080],['letter','Page 1275 × 1650',1275,1650]];
 let tool=getLS('kanin-easel-tool','brush'), color=getLS('kanin-easel-color','#2962ff'), size=getLS('kanin-easel-size',12), alpha=getLS('kanin-easel-alpha',1), bg=getLS('kanin-easel-bg','#ffffff'), fmt=getLS('kanin-easel-fmt','square');
 let cv=null, g=null, undoS=[], redoS=[], drawing=null, snap=null, textAt=null;
 const css=document.createElement('style'); css.textContent=`
#kEasel{position:fixed;top:0;left:0;right:var(--kRailW,58px);bottom:0;z-index:8560;overflow-y:auto;box-sizing:border-box;padding:calc(8px + env(safe-area-inset-top,0px)) max(10px,env(safe-area-inset-left,0px)) 150px 10px;background:#1b1830;color:#fff;font:14px/1.4 system-ui,sans-serif}
#kEasel[hidden]{display:none!important}
#kEasel .eaIn{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:8px;align-items:center}
#kEasel h2{margin:2px 0;font:900 22px system-ui,sans-serif;color:#ffe94a;text-align:center}
#kEasel .eaBar{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;align-items:center;width:100%}
#kEasel .eaBar button{min-width:44px;min-height:44px;border-radius:10px;font:800 13px system-ui,sans-serif;padding:0 8px}
#kEasel .eaBar button.on{background:#ffe94a!important;color:#14163a!important}
#kEasel .eaSw{width:30px;height:30px;min-width:30px!important;min-height:30px!important;padding:0!important;border-radius:50%!important;border:2px solid #fff}
#kEasel .eaSw.on{outline:3px solid #ffe94a;outline-offset:2px}
#kEasel label{display:inline-flex;gap:6px;align-items:center;font:700 12.5px system-ui,sans-serif}
#kEasel select,#kEasel input[type=text]{min-height:40px;border-radius:10px}
#kEasel .eaWrap{width:100%;display:flex;justify-content:center}
#kEasel canvas#eaCv{max-width:100%;max-height:72vh;background:repeating-conic-gradient(#ccc 0 25%,#fff 0 50%) 0 0/20px 20px;box-shadow:0 6px 30px rgba(0,0,0,.6);touch-action:none;cursor:crosshair;border-radius:6px}
#kEasel .eaN{font-size:12.5px;opacity:.8;text-align:center}
#kEasel h2{order:0}#kEasel #eaTools{order:1}#kEasel .eaWrap{order:2}#kEasel #eaMsg{order:3}#kEasel .eaBar{order:4}#kEasel #eaTextRow{order:1}
@media (max-width:760px){#kEasel h2{font-size:17px}#kEasel #eaTools{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;padding-bottom:4px}#kEasel #eaTools button{flex:0 0 auto;font-size:12px}#kEasel canvas#eaCv{max-height:58vh}}`; document.head.appendChild(css);
 function box(){ let d=$('kEasel'); if(d) return d; d=document.createElement('div'); d.id='kEasel'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Easel'); document.body.appendChild(d);
  d.innerHTML='<div class="kBar" data-sc="kEasel"><button type="button" data-ka="close" data-ea="close">✕</button></div><div class="eaIn"><h2>🎨 The Easel</h2>'+
   '<div class="eaBar" id="eaTools">'+TOOLS.map(([k,i,l])=>'<button type="button" data-tool="'+k+'" title="'+l+'" data-noul>'+i+' '+l+'</button>').join('')+'</div>'+
   '<div class="eaBar">'+SW.map(c=>'<button type="button" class="eaSw" data-col="'+c+'" style="background:'+c+'" title="'+c+'" aria-label="Color '+c+'" data-noul></button>').join('')+'<label>🎨 <input type="color" id="eaCol" value="'+color+'" aria-label="Any color"></label></div>'+
   '<div class="eaBar"><label>Size <input type="range" id="eaSize" min="1" max="120" value="'+size+'"></label><label>See-through <input type="range" id="eaAlpha" min="0.05" max="1" step="0.05" value="'+alpha+'"></label><label>Paper <select id="eaBg"><option value="#ffffff">White</option><option value="#000000">Black</option><option value="#f6eedc">Sketch paper</option><option value="#14163a">Night</option><option value="transparent">See-through</option></select></label><label>Size of page <select id="eaFmt">'+SIZES.map(s=>'<option value="'+s[0]+'">'+s[1]+'</option>').join('')+'</select></label></div>'+
   '<div class="eaBar"><button type="button" data-ea="undo" data-noul>↶ Undo</button><button type="button" data-ea="redo" data-noul>↷ Redo</button><button type="button" data-ea="clear" data-noul>🧹 Clear</button><label class="eaN" style="opacity:1">🖼 Add a picture <input type="file" id="eaPic" accept="image/*"></label><button type="button" data-ea="save" data-noul>💾 Save to my library</button><button type="button" data-ea="post" data-noul>🌐 Post</button><button type="button" data-ea="dl" data-noul>⬇ Download</button><button type="button" data-ea="ai" data-noul>🤖 AI ideas</button><button type="button" data-ea="close" data-noul>✕ Close</button></div>'+
   '<div class="eaBar" id="eaTextRow" hidden><input type="text" id="eaText" maxlength="120" placeholder="Type, then tap the page where it goes"><button type="button" data-ea="textok" data-noul>✅ Place it</button></div>'+
   '<div class="eaWrap"><canvas id="eaCv" aria-label="Drawing page"></canvas></div><div class="eaN" id="eaMsg">Draw with your finger, a pen or the mouse. Ctrl/⌘ + Z undoes. Paste a picture with Ctrl/⌘ + V.</div></div>';
  cv=$('eaCv'); g=cv.getContext('2d',{willReadFrequently:true}); $('eaBg').value=bg; $('eaFmt').value=fmt; restore();
  d.addEventListener('click',onClick); d.addEventListener('input',onInput); d.addEventListener('change',onChange);
  cv.addEventListener('pointerdown',down); cv.addEventListener('pointermove',move); cv.addEventListener('pointerup',up); cv.addEventListener('pointercancel',up); cv.addEventListener('pointerleave',e=>{ if(drawing&&e.pointerType==='mouse') up(e); });
  paintBar(); return d; }
 function sizeOf(){ return SIZES.find(s=>s[0]===fmt)||SIZES[0]; }
 function fresh(){ const s=sizeOf(); cv.width=s[2]; cv.height=s[3]; if(bg!=='transparent'){ g.fillStyle=bg; g.fillRect(0,0,cv.width,cv.height); } else g.clearRect(0,0,cv.width,cv.height); }
 function restore(){ fresh(); try{ const u=localStorage.getItem('kanin-easel-draft'); if(u){ const im=new Image(); im.onload=()=>{ g.drawImage(im,0,0,cv.width,cv.height); }; im.src=u; } }catch(_){ } }
 let saveT=0; function autosave(){ clearTimeout(saveT); saveT=setTimeout(()=>{ try{ localStorage.setItem('kanin-easel-draft',cv.toDataURL('image/webp',0.8)); }catch(_){ } },800); }
 function push(){ try{ undoS.push(g.getImageData(0,0,cv.width,cv.height)); if(undoS.length>30) undoS.shift(); redoS=[]; }catch(_){ } }
 function undo(){ if(!undoS.length) return say('Nothing to undo.'); redoS.push(g.getImageData(0,0,cv.width,cv.height)); g.putImageData(undoS.pop(),0,0); autosave(); say('↶ Undone.'); }
 function redo(){ if(!redoS.length) return say('Nothing to redo.'); undoS.push(g.getImageData(0,0,cv.width,cv.height)); g.putImageData(redoS.pop(),0,0); autosave(); }
 function clear(){ push(); fresh(); autosave(); say('🧹 A clean page. ↶ Undo brings it back.'); }
 const pt=e=>{ const r=cv.getBoundingClientRect(); return [(e.clientX-r.left)*cv.width/r.width,(e.clientY-r.top)*cv.height/r.height]; };
 const rgba=(c,a)=>{ const n=parseInt(c.slice(1),16); return 'rgba('+(n>>16&255)+','+(n>>8&255)+','+(n&255)+','+a+')'; };
 function style(pr){ const k=cv.width/1080; g.lineCap='round'; g.lineJoin='round'; g.globalCompositeOperation=tool==='eraser'?'destination-out':'source-over';
  const w=size*k*(tool==='pencil'?0.35:tool==='marker'?1.4:1)*(tool==='brush'?(0.4+pr*1.2):1); g.lineWidth=Math.max(1,w); g.strokeStyle=rgba(color,tool==='marker'?Math.min(alpha,0.5):tool==='eraser'?1:alpha); g.fillStyle=rgba(color,alpha); }
 function down(e){ e.preventDefault(); try{ cv.setPointerCapture(e.pointerId); }catch(_){ } const [x,y]=pt(e);
  if(tool==='text'){ const t=($('eaText')||{}).value||''; if(!t.trim()) return say('Type your words above first.'); push(); g.globalCompositeOperation='source-over'; g.fillStyle=rgba(color,alpha); g.font='800 '+Math.round(size*3*cv.width/1080)+'px system-ui,sans-serif'; g.textBaseline='middle'; g.fillText(t,x,y); autosave(); return; }
  if(tool==='fill'){ push(); fill(Math.round(x),Math.round(y)); autosave(); return; }
  push(); drawing={x,y,x0:x,y0:y}; if(/line|rect|ellipse/.test(tool)) snap=g.getImageData(0,0,cv.width,cv.height); else { style(e.pressure||0.5); g.beginPath(); g.moveTo(x,y); g.lineTo(x+0.01,y); g.stroke(); } }
 function move(e){ if(!drawing) return; const [x,y]=pt(e);
  if(/line|rect|ellipse/.test(tool)){ g.putImageData(snap,0,0); style(0.5); g.beginPath(); const {x0,y0}=drawing; if(tool==='line'){ g.moveTo(x0,y0); g.lineTo(x,y); } else if(tool==='rect') g.rect(x0,y0,x-x0,y-y0); else g.ellipse((x0+x)/2,(y0+y)/2,Math.abs(x-x0)/2,Math.abs(y-y0)/2,0,0,Math.PI*2); g.stroke(); return; }
  if(tool==='spray'){ style(0.5); const r=size*2*cv.width/1080; for(let i=0;i<Math.max(8,size);i++){ const a=Math.random()*6.283, d=Math.random()*r; g.fillRect(x+Math.cos(a)*d,y+Math.sin(a)*d,1.6,1.6); } return; }
  style(e.pressure||0.5); g.beginPath(); g.moveTo(drawing.x,drawing.y); g.lineTo(x,y); g.stroke(); drawing.x=x; drawing.y=y; }
 function up(){ if(!drawing) return; drawing=null; snap=null; g.globalCompositeOperation='source-over'; autosave(); }
 function fill(x,y){ const W=cv.width,H=cv.height; const im=g.getImageData(0,0,W,H), d=im.data; const i0=(y*W+x)*4; const t=[d[i0],d[i0+1],d[i0+2],d[i0+3]]; const n=parseInt(color.slice(1),16); const f=[n>>16&255,n>>8&255,n&255,Math.round(alpha*255)];
  if(t.every((v,k)=>Math.abs(v-f[k])<3)) return; const same=i=>Math.abs(d[i]-t[0])+Math.abs(d[i+1]-t[1])+Math.abs(d[i+2]-t[2])+Math.abs(d[i+3]-t[3])<48; const st=[[x,y]];
  while(st.length){ let [cx,cy]=st.pop(); let i=(cy*W+cx)*4; while(cy>=0&&same(i)){ cy--; i-=W*4; } cy++; i+=W*4; let L=false,R=false; while(cy<H&&same(i)){ d[i]=f[0]; d[i+1]=f[1]; d[i+2]=f[2]; d[i+3]=f[3];
    if(cx>0){ if(same(i-4)){ if(!L){ st.push([cx-1,cy]); L=true; } } else L=false; } if(cx<W-1){ if(same(i+4)){ if(!R){ st.push([cx+1,cy]); R=true; } } else R=false; } cy++; i+=W*4; } }
  g.putImageData(im,0,0); }
 async function addPicture(blob){ try{ const im=await new Promise((res,rej)=>{ const i=new Image(); i.onload=()=>res(i); i.onerror=rej; i.src=URL.createObjectURL(blob); }); push(); const s=Math.min(cv.width/im.width,cv.height/im.height,1); const w=im.width*s,h=im.height*s; g.globalCompositeOperation='source-over'; g.globalAlpha=1; g.drawImage(im,(cv.width-w)/2,(cv.height-h)/2,w,h); autosave(); say('🖼 Picture added. Draw on it, or ↶ Undo.'); }catch(_){ say('That picture could not be opened.'); } }
 const blob=()=>new Promise(r=>cv.toBlob(r,'image/png'));
 async function save(){ try{ const it=await KLIB.save({kind:'image',name:'Drawing '+new Date().toLocaleString(),blob:await blob(),meta:{from:'easel'}}); say('💾 Saved to 📚 My library on this device.'); return it; }catch(_){ say('It could not be saved here.'); } }
 async function post(){ const it=await save(); if(it&&window.KSOCIAL){ close(); KSOCIAL.compose({text:'🎨 ',media:it.id}); } }
 async function dl(){ try{ await KLIB.download(await blob(),'kan-in-drawing.png'); }catch(_){ say('Saving files is not allowed here.'); } }
 function paintBar(){ const d=$('kEasel'); if(!d) return; d.querySelectorAll('[data-tool]').forEach(b=>b.classList.toggle('on',b.dataset.tool===tool)); d.querySelectorAll('[data-col]').forEach(b=>b.classList.toggle('on',b.dataset.col===color)); const tr=$('eaTextRow'); if(tr) tr.hidden=tool!=='text'; const c=$('eaCol'); if(c) c.value=color; }
 function onClick(e){ const b=e.target.closest('button'); if(!b) return; e.stopPropagation();
  if(b.dataset.tool){ tool=b.dataset.tool; putLS('kanin-easel-tool',tool); return paintBar(); }
  if(b.dataset.col){ color=b.dataset.col; putLS('kanin-easel-color',color); if(tool==='eraser'){ tool='brush'; } return paintBar(); }
  const a=b.dataset.ea; if(a==='close') return close(); if(a==='undo') return undo(); if(a==='redo') return redo(); if(a==='clear') return clear(); if(a==='save') return save(); if(a==='post') return post(); if(a==='dl') return dl(); if(a==='textok') return say('Now tap the page where the words go.');
  if(a==='ai'){ close(); try{ KAI.open('Give me 5 fun, simple ideas for a drawing I can make on the KAN-IN Easel today, each one sentence, with the colors to use.'); }catch(_){ say('The AI opens from 🤖 AI on the rail.'); } } }
 function onInput(e){ const t=e.target; if(t.id==='eaSize'){ size=+t.value; putLS('kanin-easel-size',size); } if(t.id==='eaAlpha'){ alpha=+t.value; putLS('kanin-easel-alpha',alpha); } if(t.id==='eaCol'){ color=t.value; putLS('kanin-easel-color',color); paintBar(); } }
 function onChange(e){ const t=e.target; if(t.id==='eaPic'&&t.files&&t.files[0]){ addPicture(t.files[0]); t.value=''; } if(t.id==='eaBg'){ bg=t.value; putLS('kanin-easel-bg',bg); clear(); } if(t.id==='eaFmt'){ fmt=t.value; putLS('kanin-easel-fmt',fmt); push(); fresh(); autosave(); undoS=[]; say('📐 New page size. The page starts clean.'); } }
 document.addEventListener('keydown',e=>{ const d=$('kEasel'); if(!d||d.hidden) return; if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='z'){ e.preventDefault(); e.shiftKey?redo():undo(); } },true);
 document.addEventListener('paste',e=>{ const d=$('kEasel'); if(!d||d.hidden) return; const it=[...(e.clipboardData&&e.clipboardData.items||[])].find(x=>x.type.startsWith('image/')); if(it){ e.preventDefault(); addPicture(it.getAsFile()); } });
 function open(){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner','kVG','kSocial','kAI'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ } d.hidden=false; d.scrollTop=0; }
 function close(){ const d=$('kEasel'); if(d) d.hidden=true; }
 try{ const gh=window.GOHOME; if(gh&&!gh.__kea){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kea=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(e.target.closest&&e.target.closest('#kdHome,#lpMenu')) close(); },true);
 window.KEASEL={open,close,undo,redo,clear,save,post};
})();
