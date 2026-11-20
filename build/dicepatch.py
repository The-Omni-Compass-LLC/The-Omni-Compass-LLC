# Applied for v199; v200 then removed the die face shown over each hit (a hit is a plain starburst again).
import re
p='canon/canon.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    pat=re.escape(a); pat=re.sub(r'(\\ )+',r'\\s+',pat)
    ms=list(re.finditer(pat,s))
    assert len(ms)==n,(a[:70],len(ms))
    s=re.sub(pat,lambda m:b,s)
PIPS="const P6={1:[[0,0]],2:[[-1,-1],[1,1]],3:[[-1,-1],[0,0],[1,1]],4:[[-1,-1],[1,-1],[-1,1],[1,1]],5:[[-1,-1],[1,-1],[0,0],[-1,1],[1,1]],6:[[-1,-1],[1,-1],[-1,0],[1,0],[-1,1],[1,1]]};"
DIE="function kDie(c,x,y,S,r,f,glow){ c.save(); c.translate(x,y); c.rotate(r); const h=S/2, q=S*.22; if(glow){ c.shadowColor='rgba(255,233,74,.95)'; c.shadowBlur=S*.9; } c.fillStyle='#ffffff'; c.beginPath(); c.moveTo(-h+q,-h); c.arcTo(h,-h,h,h,q); c.arcTo(h,h,-h,h,q); c.arcTo(-h,h,-h,-h,q); c.arcTo(-h,-h,h,-h,q); c.closePath(); c.fill(); c.shadowBlur=0; c.strokeStyle='#1a1033'; c.lineWidth=Math.max(1,S*.08); c.stroke(); c.fillStyle=f===1?'#e0245e':'#1a1033'; (P6[f]||P6[1]).forEach(([a,b])=>{ c.beginPath(); c.arc(a*S*.27,b*S*.27,S*.1,0,7); c.fill(); }); c.restore(); }"
rep("st.shots.push({g:gi,x:p.x+Math.cos(g.a)*L,y:p.y+Math.sin(g.a)*L,vx:Math.cos(g.a)*1300*dpr,vy:Math.sin(g.a)*1300*dpr,t:0});",
    "st.shots.push({g:gi,x:p.x+Math.cos(g.a)*L,y:p.y+Math.sin(g.a)*L,vx:Math.cos(g.a)*1300*dpr,vy:Math.sin(g.a)*1300*dpr,t:0,f:1+Math.floor(Math.random()*6),spin:(Math.random()<.5?-1:1)*(10+Math.random()*8)});")
rep("x.fillStyle='#fff'; x.beginPath(); x.arc(b.x,b.y,5*dpr,0,7); x.fill();",
    "/* the bullet is a die: it tumbles in flight and lands on its face */ kDie(x,b.x,b.y,13*dpr,b.t*b.spin,b.t<.12?1+((Math.floor(b.t*60)+b.f)%6):b.f,true);")
rep("s.dead=true; hit(s,b.g); return false;","s.dead=true; (st.dtags=st.dtags||[]).push({x:s.x,y:s.y,f:b.f,t:0}); hit(s,b.g); return false;")
rep("st.booms.push({x:b.x,y:b.y,t:0.6,parts:sp});","st.booms.push({x:b.x,y:b.y,t:0.6,parts:sp}); (st.dtags=st.dtags||[]).push({x:b.x,y:b.y,f:b.f,t:0.4});")
rep("st.booms=st.booms.filter(bm=>{ bm.t+=dt;","st.dtags=(st.dtags||[]).filter(d=>{ d.t+=dt; const k=d.t/1.1; if(k>=1) return false; x.globalAlpha=k<.7?1:1-(k-.7)/.3; kDie(x,d.x,d.y-k*26*dpr,(18+16*Math.min(1,k*5))*dpr,0,d.f,true); x.globalAlpha=1; return true; }); st.booms=st.booms.filter(bm=>{ bm.t+=dt;")
rep("const st={shots:[],ships:[],booms:[],fired:0,hits:0,t:0,last:0,done:0,kind:0,sel:0};",
    "const st={shots:[],ships:[],booms:[],dtags:[],fired:0,hits:0,t:0,last:0,done:0,kind:0,sel:0}; "+PIPS+" "+DIE+" window.KDIE=kDie;")
rep("const ships=(G&&G.ships||[]).filter(s=>!s.dead&&s.x>0","const ships=(G&&G.ships||[]).filter(s=>!s.dead&&!s.claimed&&s.x>0")
rep("st.beams.push({x1:c.x+Math.cos(st.cang)*c.R*.62,y1:c.y+Math.sin(st.cang)*c.R*.62,x2:t.x,y2:t.y,t:0}); st.shots++; t.dead=true; st.kills++; boom(t); st.target=null; }",
    "const mx=c.x+Math.cos(st.cang)*c.R*.62, my=c.y+Math.sin(st.cang)*c.R*.62; st.beams.push({x1:mx,y1:my,x2:mx,y2:my,t:0}); (st.dice=st.dice||[]).push({x:mx,y:my,tg:t,t:0,f:1+Math.floor(Math.random()*6)}); t.claimed=true; st.shots++; st.target=null; }")
rep("lx.fillStyle=rg; lx.beginPath(); lx.arc(b.x1,b.y1,26*dpr,0,7); lx.fill(); lx.restore(); return true; });",
    "lx.fillStyle=rg; lx.beginPath(); lx.arc(b.x1,b.y1,26*dpr,0,7); lx.fill(); lx.restore(); return true; });\n  /* the compass's bullet is a die too: it flies to its ship, tumbling, and starbursts on the hit */\n  st.dice=(st.dice||[]).filter(d=>{ d.t+=dt; const tg=d.tg, dx=tg.x-d.x, dy=tg.y-d.y, dd=Math.hypot(dx,dy), step=1500*dpr*dt; if(tg.dead){ boom({x:d.x,y:d.y}); return false; } if(dd<=Math.max(step,16*dpr)){ tg.dead=true; st.kills++; boom(tg); const G3=window.GATE; if(G3) (G3.dtags=G3.dtags||[]).push({x:tg.x,y:tg.y,f:d.f,t:0}); return false; } d.x+=dx/dd*step; d.y+=dy/dd*step; if(window.KDIE) KDIE(lx,d.x,d.y,13*dpr,d.t*14,d.t<.12?1+((Math.floor(d.t*60)+d.f)%6):d.f,true); return d.t<3; });")
rep("BGS.shots.push({tg:tg||null,x0:mx,y0:my,x1:ex,y1:ey,cx:(mx+ex)/2,cy:(my+ey)/2,u:0,","BGS.shots.push({die:1+Math.floor(Math.random()*6),tg:tg||null,x0:mx,y0:my,x1:ex,y1:ey,cx:(mx+ex)/2,cy:(my+ey)/2,u:0,")
rep("x.fillRect(-9,-9,18,18); x.shadowBlur=0; x.strokeStyle='#100e28'; x.lineWidth=2; x.strokeRect(-9,-9,18,18); x.fillStyle='#100e28'; x.font='900 10px \"Orbitron\",sans-serif'; x.textAlign='center'; x.fillText(String(s.die),0,4); x.textAlign='left'; x.restore();",
    "x.restore(); if(window.KDIE) KDIE(x,px,py,18,u*12,u<.85?1+((Math.floor(u*20)+s.die)%6):s.die,true);")
rep('<circle class="ball" cx="104" cy="32" r="4" fill="#ffe94a"/>','<g class="ball"><rect x="98.5" y="26.5" width="11" height="11" rx="2.6" fill="#fff" stroke="#100e28" stroke-width="1.2"/><circle cx="101.3" cy="29.3" r="1.15" fill="#100e28"/><circle cx="104" cy="32" r="1.15" fill="#100e28"/><circle cx="106.7" cy="34.7" r="1.15" fill="#100e28"/></g>')
open(p,'w',encoding='utf-8').write(s); print('ok')
