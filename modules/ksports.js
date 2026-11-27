(()=>{ /* 🏆 SPORTS (v247): a platform of its own. Every major sport in the world by family (team ball sports, racket, combat, racing and
   motor, water, winter, strength and precision, mind and electronic), each with how you win, how many play, and its biggest
   competitions; search across all of them; and TODAY IN SPORTS, a board of results and stories that is kept in the platform's shared
   database and refreshes on every screen the moment a verified item is posted (only verified items are posted, each with its source).
   The 💥 cannon fires a random sport. */
 const $=id=>document.getElementById(id); const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const say=m=>{ try{ toast(m); }catch(_){ } };
 const FAM=[['team','⚽','Team ball sports'],['racket','🎾','Racket sports'],['combat','🥊','Combat sports'],['race','🏎','Racing and motor'],['water','🏊','Water sports'],['winter','⛷','Winter sports'],['solo','🏅','Athletics, strength and precision'],['mind','♟','Mind and electronic']];
 /* [family, icon, name, how you win, players, biggest competitions] */
 const S=[
 ['team','🏈','American football','Score more points by carrying or passing the ball into the end zone (touchdown, 6) or kicking it through the uprights (field goal, 3).','11 a side','NFL and the Super Bowl; NCAA college football'],
 ['team','⚽','Soccer (association football)','Score more goals by getting the ball into the net without using hands or arms (except the goalkeeper).','11 a side','FIFA World Cup, UEFA Champions League, Premier League, MLS'],
 ['team','🏀','Basketball','Score more points by shooting through the hoop: 2 points, 3 from beyond the arc, 1 per free throw.','5 a side','NBA, WNBA, FIBA World Cup, NCAA March Madness, Olympics'],
 ['team','⚾','Baseball','Score more runs by hitting the pitch and rounding all four bases over nine innings.','9 a side','MLB and the World Series, World Baseball Classic, NPB'],
 ['team','🥎','Softball','Like baseball on a smaller field with a larger ball pitched underhand, usually seven innings.','9 a side','WBSC Softball World Cup, NCAA Women’s College World Series, Olympics'],
 ['team','🏒','Ice hockey','Score more goals by shooting the puck into the net with a stick, on ice.','6 a side','NHL and the Stanley Cup, IIHF World Championship, Olympics'],
 ['team','🏑','Field hockey','Score more goals by hitting the ball into the net with a stick, from inside the shooting circle.','11 a side','FIH Hockey World Cup, Olympics, FIH Pro League'],
 ['team','🏉','Rugby union','Score more points with tries (5), conversions (2), penalties and drop goals (3); the ball is passed backward.','15 a side','Rugby World Cup, Six Nations, The Rugby Championship'],
 ['team','🏉','Rugby league','A faster rugby: tries (4), conversions (2), six tackles before handing over the ball.','13 a side','Rugby League World Cup, NRL, Super League, State of Origin'],
 ['team','🏏','Cricket','Score more runs than the other side; bowlers try to take ten wickets.','11 a side','ICC Cricket World Cup, T20 World Cup, the Ashes, IPL'],
 ['team','🏐','Volleyball','Win sets by grounding the ball on the other side of the net in three touches or fewer.','6 a side','FIVB World Championship, Volleyball Nations League, Olympics'],
 ['team','🏐','Beach volleyball','Volleyball on sand with two players a side, best of three sets.','2 a side','Beach Pro Tour, World Championships, Olympics'],
 ['team','🤾','Handball','Score more goals by throwing the ball into the net from outside the goal area.','7 a side','IHF World Championship, EHF Champions League, Olympics'],
 ['team','🤽','Water polo','Score more goals by throwing the ball into the net while swimming, without touching the bottom.','7 a side','World Aquatics Championships, Olympics'],
 ['team','🥍','Lacrosse','Score more goals by shooting the ball into the net with a netted stick.','10 a side (field)','World Lacrosse Championship, PLL, NCAA'],
 ['team','🏉','Australian rules football','Score goals (6) and behinds (1) by kicking the ball between posts on an oval field.','18 a side','AFL and the AFL Grand Final'],
 ['team','🏐','Netball','Score goals by shooting into a ring with no backboard; no running with the ball.','7 a side','Netball World Cup, Commonwealth Games'],
 ['team','🥏','Ultimate','Score by catching the disc in the end zone; no running with it, self-refereed.','7 a side','WFDF World Championships, UFA'],
 ['team','🏑','Hurling','An Irish game: strike the ball with a stick over the bar (1 point) or into the net (3).','15 a side','All-Ireland Senior Hurling Championship'],
 ['team','⚽','Gaelic football','An Irish game played with hands and feet: over the bar for 1, into the net for 3.','15 a side','All-Ireland Senior Football Championship'],
 ['racket','🎾','Tennis','Win points, games and sets by hitting the ball over the net into the opponent’s court so it cannot be returned.','1 or 2 a side','The four Grand Slams (Australian Open, French Open, Wimbledon, US Open), ATP and WTA Finals'],
 ['racket','🏸','Badminton','Win rallies by landing the shuttlecock on the other side; games to 21.','1 or 2 a side','BWF World Championships, All England Open, Olympics'],
 ['racket','🏓','Table tennis','Win rallies on a table across a low net; games to 11.','1 or 2 a side','World Table Tennis Championships, WTT series, Olympics'],
 ['racket','🎾','Squash','Win rallies by hitting the ball off the front wall of a closed court so the opponent cannot return it.','1 a side','PSA World Championships, British Open'],
 ['racket','🏓','Pickleball','Win rallies with paddles and a plastic ball on a small court; serve underhand.','1 or 2 a side','PPA Tour, Major League Pickleball, USA Pickleball Nationals'],
 ['racket','🎾','Padel','Win rallies in a walled court; the ball may bounce off the glass walls.','2 a side','Premier Padel, World Padel Championships'],
 ['combat','🥊','Boxing','Win by knockout or on the judges’ cards by landing clean punches over the rounds.','1 against 1','World title fights (WBA, WBC, IBF, WBO), Olympics'],
 ['combat','🥋','Mixed martial arts (MMA)','Win by knockout, submission or decision, striking and grappling.','1 against 1','UFC, PFL, ONE Championship'],
 ['combat','🤼','Wrestling','Win by pinning the opponent’s shoulders to the mat or on points.','1 against 1','World Wrestling Championships, Olympics (freestyle and Greco-Roman), NCAA'],
 ['combat','🥋','Judo','Win by a full throw (ippon), a hold-down or a submission.','1 against 1','World Judo Championships, Olympics'],
 ['combat','🥋','Karate','Score points with controlled strikes (kumite) or perform forms (kata).','1 against 1','Karate World Championships, Premier League'],
 ['combat','🥋','Taekwondo','Score points with kicks and punches to the body protector and head, kicks scoring higher.','1 against 1','World Taekwondo Championships, Olympics'],
 ['combat','🤺','Fencing','Score touches with a foil, épée or sabre.','1 against 1','World Fencing Championships, Olympics'],
 ['combat','🥊','Kickboxing','Win by knockout or points using punches and kicks.','1 against 1','GLORY, ONE Championship, K-1'],
 ['race','🏎','Formula 1','Score points by finishing high in races; the most points wins the world championship.','about 20 drivers','FIA Formula One World Championship (Monaco, Silverstone, Monza…)'],
 ['race','🏁','NASCAR','Stock-car racing on ovals and road courses; playoffs decide the champion.','about 36 cars','NASCAR Cup Series, the Daytona 500'],
 ['race','🏎','IndyCar','Open-wheel racing on ovals, road and street courses.','about 27 cars','IndyCar Series, the Indianapolis 500'],
 ['race','🏍','MotoGP','Motorcycle racing on circuits; points decide the champion.','about 22 riders','MotoGP World Championship'],
 ['race','🏇','Horse racing','The first horse past the post wins; jockeys ride flat races or over jumps.','a field of horses','Kentucky Derby, Royal Ascot, Melbourne Cup, the Grand National'],
 ['race','🚴','Cycling','Fastest time over a race or stage; points and mountain jerseys too.','teams of riders','Tour de France, Giro d’Italia, Vuelta, World Championships, Olympics'],
 ['race','🏃','Marathon','Run 42.195 km (26.2 miles) fastest.','a field of runners','World Marathon Majors (Boston, London, Berlin, Chicago, New York, Tokyo, Sydney), Olympics'],
 ['water','🏊','Swimming','Fastest time over a distance in freestyle, backstroke, breaststroke, butterfly or medley.','individual and relay','World Aquatics Championships, Olympics'],
 ['water','🤿','Diving','Judges score dives from springboard and platform for difficulty and execution.','individual and synchronized','World Aquatics Championships, Olympics'],
 ['water','🚣','Rowing','Fastest boat over 2,000 m.','1, 2, 4 or 8 rowers','World Rowing Championships, Olympics, the Boat Race'],
 ['water','⛵','Sailing','Finish races fastest using the wind; points across a series.','a crew or solo','America’s Cup, SailGP, Olympics'],
 ['water','🏄','Surfing','Judges score the best waves ridden in a heat.','individual','World Surf League Championship Tour, Olympics'],
 ['winter','⛷','Alpine skiing','Fastest down a course of gates: downhill, super-G, giant slalom, slalom.','individual','FIS Alpine World Cup, World Championships, Winter Olympics'],
 ['winter','🏂','Snowboarding','Judged tricks (halfpipe, slopestyle, big air) or racing (parallel, boardercross).','individual','FIS World Cup, X Games, Winter Olympics'],
 ['winter','⛸','Figure skating','Judges score jumps, spins and footwork in short and free programs.','singles, pairs, ice dance','ISU World Championships, Grand Prix, Winter Olympics'],
 ['winter','🥌','Curling','Slide stones toward the house; the stones closest to the centre score.','4 a side','World Curling Championships, Winter Olympics'],
 ['winter','🏒','Speed skating','Fastest time around an oval or in short-track packs.','individual','ISU World Cup, Winter Olympics'],
 ['solo','⛳','Golf','Finish the course in the fewest strokes.','individual or team','The four majors (Masters, PGA Championship, US Open, The Open), Ryder Cup, Solheim Cup'],
 ['solo','🏃','Athletics (track and field)','Run fastest, jump highest or farthest, throw farthest.','individual and relay','World Athletics Championships, Diamond League, Olympics'],
 ['solo','🤸','Gymnastics','Judges score routines on apparatus for difficulty and execution.','individual and team','World Gymnastics Championships, Olympics'],
 ['solo','🏋','Weightlifting','Lift the most weight in the snatch and the clean and jerk.','individual','IWF World Championships, Olympics'],
 ['solo','🏹','Archery','Score the most points shooting arrows at a target.','individual and team','World Archery Championships, Olympics'],
 ['solo','🎯','Darts','Score down from 501 to exactly zero, finishing on a double.','1 against 1','PDC World Darts Championship, Premier League'],
 ['solo','🎱','Snooker and pool','Pot balls in order and score more than the opponent.','1 against 1','World Snooker Championship (the Crucible), WPA World Pool Championship'],
 ['solo','🎳','Bowling','Knock down the most pins over ten frames; a perfect game is 300.','individual or team','PBA Tour, USBC Masters'],
 ['solo','🧗','Sport climbing','Climb highest or fastest: lead, bouldering and speed.','individual','IFSC World Cup, World Championships, Olympics'],
 ['solo','🛹','Skateboarding','Judges score tricks in street and park runs.','individual','World Skateboarding Championships, X Games, Olympics'],
 ['solo','🏊','Triathlon','Swim, cycle and run in one race, fastest time wins.','individual','Ironman World Championship, World Triathlon Championship Series, Olympics'],
 ['solo','🐎','Equestrian','Show jumping, dressage and eventing, scored for faults, marks and time.','rider and horse','FEI World Equestrian Games, Olympics'],
 ['mind','♟','Chess','Checkmate the opponent’s king.','1 against 1','World Chess Championship, Candidates Tournament, Chess Olympiad'],
 ['mind','🎮','Esports','Teams or players compete in video games: league seasons and world finals.','1 or teams','League of Legends Worlds, The International (Dota 2), CS2 Majors, Valorant Champions'],
 ['mind','🃏','Poker','Win chips with the best hand or by making others fold.','a table of players','World Series of Poker Main Event']];
 /* 🏟 LEAGUES & LINKS (v248): every major professional, college and international league and governing body, with its official site,
    plus the big scores and news sites; and 🎲 BETTING, a tab of licensed sportsbooks for adults where betting is legal, opened only
    after a 21+ and legal-where-I-am confirmation, with the problem-gambling helpline on the same screen. */
 const LG=[['🇺🇸 American professional',[['🏈','NFL','https://www.nfl.com'],['🏀','NBA','https://www.nba.com'],['🏀','WNBA','https://www.wnba.com'],['⚾','MLB','https://www.mlb.com'],['🏒','NHL','https://www.nhl.com'],['⚽','MLS','https://www.mlssoccer.com'],['⚽','NWSL','https://www.nwslsoccer.com'],['⛳','PGA Tour','https://www.pgatour.com'],['⛳','LPGA','https://www.lpga.com'],['🏁','NASCAR','https://www.nascar.com'],['🏎','IndyCar','https://www.indycar.com'],['🥋','UFC','https://www.ufc.com'],['🥍','Premier Lacrosse League','https://premierlacrosseleague.com']]],
  ['🎓 College',[['🎓','NCAA (all sports, March Madness)','https://www.ncaa.com'],['🏈','College Football Playoff','https://collegefootballplayoff.com'],['🎓','NAIA','https://www.naia.org']]],
  ['🌍 International and world',[['⚽','FIFA (World Cup)','https://www.fifa.com'],['⚽','UEFA (Champions League, Euros)','https://www.uefa.com'],['⚽','Premier League','https://www.premierleague.com'],['⚽','LaLiga','https://www.laliga.com'],['⚽','Bundesliga','https://www.bundesliga.com'],['⚽','Serie A','https://www.legaseriea.it'],['⚽','Ligue 1','https://www.ligue1.com'],['⚽','Liga MX','https://ligamx.net'],['🏎','Formula 1','https://www.formula1.com'],['🏍','MotoGP','https://www.motogp.com'],['🎾','ATP Tour','https://www.atptour.com'],['🎾','WTA','https://www.wtatennis.com'],['🏏','ICC cricket','https://www.icc-cricket.com'],['🏏','IPL','https://www.iplt20.com'],['🏉','World Rugby','https://www.world.rugby'],['🏉','NRL','https://www.nrl.com'],['🏉','AFL','https://www.afl.com.au'],['🏀','FIBA','https://www.fiba.basketball'],['🏀','EuroLeague','https://www.euroleaguebasketball.net'],['🏒','IIHF','https://www.iihf.com'],['🏃','World Athletics','https://worldathletics.org'],['🏊','World Aquatics','https://www.worldaquatics.com'],['⛷','FIS skiing','https://www.fis-ski.com'],['🚴','Tour de France','https://www.letour.fr'],['🥋','ONE Championship','https://www.onefc.com'],['🏅','Olympics','https://www.olympics.com']]],
  ['📺 Scores and news',[['📺','ESPN','https://www.espn.com'],['📺','CBS Sports','https://www.cbssports.com'],['📺','BBC Sport','https://www.bbc.com/sport'],['📺','Yahoo Sports','https://sports.yahoo.com'],['📺','Sky Sports','https://www.skysports.com'],['📰','The Athletic','https://www.nytimes.com/athletic/']]]];
 const BOOKS=[['FanDuel Sportsbook','https://sportsbook.fanduel.com'],['DraftKings Sportsbook','https://sportsbook.draftkings.com'],['BetMGM','https://sports.betmgm.com'],['Caesars Sportsbook','https://www.caesars.com/sportsbook-and-casino'],['Fanatics Sportsbook','https://sportsbook.fanatics.com'],['bet365','https://www.bet365.com']];
 let view='sports', betOK=false;
 const ext=(u,t)=>'<a class="spLink" href="'+u+'" target="_blank" rel="noopener">'+t+' ↗</a>';
 function leaguesHTML(){ return LG.map(([g,L])=>'<h3 class="spH">'+g+'</h3><div class="spGrid">'+L.map(([i,n,u])=>'<div class="spCard"><h3>'+i+' '+esc(n)+'</h3>'+ext(u,'Official site')+'</div>').join('')+'</div>').join(''); }
 function betHTML(){ const warn='<p class="spWarn">🔞 Betting is for adults only (21+ in most U.S. states) and only where it is legal. KAN-IN does not take bets; these links leave the app for the sportsbook’s own site. Gambling problem? Call 1-800-GAMBLER (U.S.) or visit '+ext('https://www.ncpgambling.org','the National Council on Problem Gambling')+'.</p>';
  if(!betOK) return '<div class="spLive"><h3>🎲 Sports betting links</h3>'+warn+'<button type="button" data-sp="betok" data-noul>✅ I am 21 or older and betting is legal where I am</button></div>';
  return '<div class="spLive"><h3>🎲 Sports betting links</h3>'+warn+'<div class="spGrid">'+BOOKS.map(([n,u])=>'<div class="spCard"><h3>🎲 '+esc(n)+'</h3>'+ext(u,'Open')+'</div>').join('')+'</div></div>'; }
 let fam='all', q='', live=[], liveState='idle';
 async function loadLive(){ if(liveState!=='idle') return; liveState='loading'; try{ const db=await claude.use('db'); if(!db){ liveState='none'; paint(); return; } const to=setTimeout(()=>{ if(liveState==='loading'){ liveState='none'; paint(); } },10000);
   db.collection('sports/today/items').orderBy('rank').limit(40).onSnapshot(s=>{ clearTimeout(to); live=s.docs.map(d=>d.data()||{}); liveState='done'; paint(); },()=>{ clearTimeout(to); liveState='none'; paint(); }); }catch(_){ liveState='none'; paint(); } }
 const css=document.createElement('style'); css.textContent=`
#kSports{position:fixed;inset:0;right:var(--kRailW,58px);z-index:8560;overflow-y:auto;background:radial-gradient(circle at 50% 0,#0f3d2e,#04110c 70%);color:#eafff4;font:15px/1.5 system-ui,sans-serif;padding:calc(12px + env(safe-area-inset-top,0px)) max(14px,env(safe-area-inset-left,0px)) 40px}
#kSports[hidden]{display:none!important}
#kSports .spIn{max-width:1100px;margin:0 auto}
#kSports h2{font:900 28px/1.1 system-ui,sans-serif;margin:4px 0;color:#7dffb8}
#kSports .spTop{display:flex;justify-content:space-between;align-items:center;gap:8px}
#kSports .spRow{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
#kSports button{min-height:44px;padding:0 14px;border-radius:4px 12px 4px 12px;font:800 14px system-ui,sans-serif}
#kSports .spRow button.on{background:#7dffb8!important;color:#04110c!important}
#kSports input[type=search]{width:100%;box-sizing:border-box;min-height:46px;border-radius:12px;padding:0 14px;font:16px system-ui,sans-serif}
#kSports .spGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
#kSports .spCard{background:linear-gradient(160deg,rgba(20,60,44,.85),rgba(6,20,14,.9));border:1px solid rgba(125,255,184,.35);border-radius:4px 16px 4px 16px;padding:12px}
#kSports .spCard h3{margin:0 0 4px;font:900 17px system-ui,sans-serif}
#kSports .spCard p{margin:4px 0;font-size:14px}
#kSports .spCard small{display:block;color:#9fe8c4;font-weight:700}
#kSports .spLive{background:rgba(0,0,0,.3);border:1px solid rgba(255,233,74,.4);border-radius:14px;padding:12px;margin:10px 0}
#kSports .spLive h3{margin:0 0 6px;color:#ffe94a}
#kSports .spItem{padding:8px 0;border-top:1px solid rgba(255,255,255,.1)}
#kSports .spItem:first-of-type{border-top:0}
#kSports .spItem a{color:#7ff;font-weight:700}
#kSports .spCard.hl{outline:3px solid #ffe94a}
#kSports .spLink{display:inline-block;margin-top:6px;padding:6px 12px;border-radius:3px 10px 3px 10px;background:#7dffb8;color:#04110c!important;font:900 13px system-ui,sans-serif;text-decoration:none}
#kSports .spH{margin:16px 0 6px;font:900 18px system-ui,sans-serif;color:#ffe94a}
#kSports .spWarn{background:rgba(255,45,85,.12);border:1px solid rgba(255,45,85,.45);border-radius:10px;padding:8px 10px;font-size:13.5px}
#kSports .spWarn a{color:#04110c}`; document.head.appendChild(css);
 function box(){ let d=$('kSports'); if(d) return d; d=document.createElement('div'); d.id='kSports'; d.className='kHas'; d.hidden=true; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Sports'); document.body.appendChild(d);
  d.addEventListener('click',e=>{ const b=e.target.closest('[data-sp]'); if(!b) return; e.stopPropagation(); const k=b.dataset.sp; if(k==='x') return close(); if(k==='fam'){ fam=b.dataset.v; paint(true); } if(k==='rand') return random(); if(k==='view'){ view=b.dataset.v; paint(true); } if(k==='betok'){ betOK=true; paint(true); } });
  d.addEventListener('input',e=>{ if(e.target.dataset.sp==='q'){ q=e.target.value; paintList(); } }); return d; }
 const list=()=>S.filter(x=>(q||fam==='all'||x[0]===fam)&&(!q||(x[2]+' '+x[3]+' '+x[5]).toLowerCase().includes(q.toLowerCase())));
 function card(x,i){ return '<div class="spCard" data-i="'+i+'"><h3>'+x[1]+' '+esc(x[2])+'</h3><p>'+esc(x[3])+'</p><small>👥 '+esc(x[4])+'</small><small>🏆 '+esc(x[5])+'</small></div>'; }
 function liveHTML(){ if(liveState==='loading'||liveState==='idle') return '<div class="spLive"><h3>📡 Today in sports</h3><p>Loading the board…</p></div>';
  if(!live.length) return '<div class="spLive"><h3>📡 Today in sports</h3><p>No verified results are posted on the board right now. Results and stories appear here, on every screen at once, as soon as they are checked against their source.</p></div>';
  return '<div class="spLive"><h3>📡 Today in sports</h3>'+live.map(x=>'<div class="spItem"><b>'+esc(x.sport?x.sport+' · ':'')+esc(x.title||'')+'</b><div>'+esc(x.summary||'')+'</div>'+(typeof x.url==='string'&&x.url.startsWith('https://')?'<a href="'+esc(x.url)+'" target="_blank" rel="noopener">Source ↗</a>':'')+'</div>').join('')+'</div>'; }
 function paint(full){ const d=$('kSports'); if(!d||d.hidden) return; if(full||!d.querySelector('.spIn')){ d.innerHTML='<div class="spIn"><div class="spTop"><h2>🏆 Sports</h2><button type="button" data-sp="x" data-noul>✕ Close</button></div><div class="spLiveBox"></div><div class="spRow"><button type="button" data-sp="fam" data-v="all" class="'+(fam==='all'?'on':'')+'" data-noul>🌍 All '+S.length+'</button>'+FAM.map(([k,i,l])=>'<button type="button" data-sp="fam" data-v="'+k+'" class="'+(fam===k?'on':'')+'" data-noul>'+i+' '+esc(l)+'</button>').join('')+'<button type="button" data-sp="rand" data-noul>💥 Random sport</button></div><div class="spRow"><button type="button" data-sp="view" data-v="sports" class="'+(view==='sports'?'on':'')+'" data-noul>🏅 Every sport</button><button type="button" data-sp="view" data-v="leagues" class="'+(view==='leagues'?'on':'')+'" data-noul>🏟 Leagues & links</button><button type="button" data-sp="view" data-v="bet" class="'+(view==='bet'?'on':'')+'" data-noul>🎲 Betting (21+)</button></div><input type="search" data-sp="q" placeholder="🔎 Search every sport, rule and competition" value="'+esc(q)+'"><div class="spGrid"></div><p style="opacity:.7;font-size:12.5px;margin-top:16px">© 2026 The Omni-Compass LLC and DD Universe Multi-Media Studios. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com</p></div>'; paintList(); }
  const lb=d.querySelector('.spLiveBox'); if(lb){ const h=liveHTML(); if(lb.dataset.h!==h){ lb.dataset.h=h; lb.innerHTML=h; } } }
 function paintList(){ const d0=$('kSports'); const g=d0&&d0.querySelector('.spGrid'); if(!g) return; if(view!=='sports'){ g.outerHTML='<div class="spGrid spAlt"></div>'; const a=d0.querySelector('.spAlt'); a.outerHTML='<div class="spAltBox">'+(view==='leagues'?leaguesHTML():betHTML())+'</div>'; const qi=d0.querySelector('[data-sp="q"]'); if(qi) qi.style.display='none'; return; } const L=list(); g.innerHTML=L.map(x=>card(x,S.indexOf(x))).join('')||'<p>No sport matches.</p>'; }
 function random(){ fam='all'; q=''; paint(true); const i=Math.floor(Math.random()*S.length); const c=$('kSports').querySelector('.spCard[data-i="'+i+'"]'); if(c){ c.classList.add('hl'); c.scrollIntoView({block:'center',behavior:'smooth'}); setTimeout(()=>c.classList.remove('hl'),2500); say('💥 '+S[i][1]+' '+S[i][2]); } }
 function open(){ const d=box(); try{ ['kKnow','kNews','kRelig','kMarket','kKara','kAcct'].forEach(id=>{ const x=$(id); if(x&&x!==d) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } d.hidden=false; paint(true); loadLive(); }
 function close(){ const d=$('kSports'); if(d) d.hidden=true; }
 try{ if(window.KCANNON){ KCANNON.SHOT.kSports=()=>{ random(); return true; }; KCANNON.NAME.kSports='Sports'; } }catch(_){ }
 setTimeout(()=>{ try{ if(window.KCANNON&&!KCANNON.SHOT.kSports){ KCANNON.SHOT.kSports=()=>{ random(); return true; }; KCANNON.NAME.kSports='Sports'; } }catch(_){ } },3000);
 (window.KFINDX=window.KFINDX||[]).push(add=>{ add('Platforms','🏆','Sports: every sport, every league with links, today in sports, betting links (21+)','Sports',()=>open()); });
 window.KSPORTS={open,close,random,list:()=>S.slice()};
})();
