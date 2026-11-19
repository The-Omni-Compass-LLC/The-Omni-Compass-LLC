(()=>{ /* MY LIBRARY: everything a person makes (takes, songs, beats, photos, videos, memes, posts) is kept on THEIR device, private to them,
   in the browser's own database (IndexedDB). Nothing leaves the device unless they post it, download it or share it. */
 const DB='kanin-library', ST='items'; let dbp=null;
 const open=()=>dbp||(dbp=new Promise((res,rej)=>{ try{ const r=indexedDB.open(DB,1); r.onupgradeneeded=()=>{ const d=r.result; if(!d.objectStoreNames.contains(ST)){ const s=d.createObjectStore(ST,{keyPath:'id'}); s.createIndex('kind','kind'); s.createIndex('at','at'); } }; r.onsuccess=()=>res(r.result); r.onerror=()=>rej(r.error); }catch(e){ rej(e); } }));
 const tx=async(mode,fn)=>{ const d=await open(); return new Promise((res,rej)=>{ const t=d.transaction(ST,mode); const s=t.objectStore(ST); let out; Promise.resolve(fn(s)).then(v=>{ out=v; }); t.oncomplete=()=>res(out); t.onerror=()=>rej(t.error); t.onabort=()=>rej(t.error); }); };
 const req=r=>new Promise((res,rej)=>{ r.onsuccess=()=>res(r.result); r.onerror=()=>rej(r.error); });
 const uid=()=>Date.now().toString(36)+Math.random().toString(36).slice(2,8);
 const subs=new Set(); const ping=()=>subs.forEach(f=>{ try{ f(); }catch(_){ } });
 async function save(item){ const it=Object.assign({id:uid(),at:Date.now(),kind:'file',name:'Untitled',meta:{}},item); await tx('readwrite',s=>req(s.put(it))); ping(); return it; }
 async function update(id,patch){ const it=await get(id); if(!it) return null; const n=Object.assign({},it,patch); await tx('readwrite',s=>req(s.put(n))); ping(); return n; }
 async function get(id){ return tx('readonly',s=>req(s.get(id))); }
 async function list(kind){ const all=await tx('readonly',s=>req(s.getAll())); return (all||[]).filter(x=>!kind||x.kind===kind||(Array.isArray(kind)&&kind.includes(x.kind))).sort((a,b)=>b.at-a.at); }
 async function del(id){ await tx('readwrite',s=>req(s.delete(id))); ping(); }
 async function usage(){ try{ const e=await navigator.storage.estimate(); return e; }catch(_){ return null; } }
 /* a sound kept as a WAV file, so it plays everywhere */
 function wav(buf){ const ch=Math.min(2,buf.numberOfChannels), sr=buf.sampleRate, n=buf.length, B=new ArrayBuffer(44+n*ch*2), v=new DataView(B); const w=(o,s)=>{ for(let i=0;i<s.length;i++) v.setUint8(o+i,s.charCodeAt(i)); };
  w(0,'RIFF'); v.setUint32(4,36+n*ch*2,true); w(8,'WAVE'); w(12,'fmt '); v.setUint32(16,16,true); v.setUint16(20,1,true); v.setUint16(22,ch,true); v.setUint32(24,sr,true); v.setUint32(28,sr*ch*2,true); v.setUint16(32,ch*2,true); v.setUint16(34,16,true); w(36,'data'); v.setUint32(40,n*ch*2,true);
  let o=44; const D=[...Array(ch)].map((_,i)=>buf.getChannelData(i)); for(let i=0;i<n;i++) for(let c=0;c<ch;c++){ const x=Math.max(-1,Math.min(1,D[c][i])); v.setInt16(o,x<0?x*0x8000:x*0x7fff,true); o+=2; } return new Blob([B],{type:'audio/wav'}); }
 async function saveAudio(buf,name,meta){ return save({kind:'audio',name,blob:wav(buf),meta:Object.assign({secs:+buf.duration.toFixed(1)},meta||{})}); }
 /* offer a file to keep: the claude.ai download where it is allowed, else a normal browser download */
 async function download(blob,filename){ try{ const d=window.claude&&await claude.use('downloads'); if(d){ const ok=/\.(webm|mp4|txt|json|png|jpg|jpeg|webp|gif|pdf|csv|md)$/i.test(filename); if(ok){ await d.save({filename,data:blob}); return true; } } }catch(_){ }
  try{ const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=filename; document.body.appendChild(a); a.click(); setTimeout(()=>{ URL.revokeObjectURL(a.href); a.remove(); },4000); return true; }catch(_){ return false; } }
 window.KLIB={save,update,get,list,del,usage,saveAudio,wav,download,on:f=>{ subs.add(f); return ()=>subs.delete(f); },uid};
})();
