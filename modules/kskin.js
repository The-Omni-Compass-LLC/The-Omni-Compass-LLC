(()=>{ /* ⬡ THE 2026 SKIN (v246). One look for the whole platform, a different shape for each kind of control, so a hand knows what it is
   touching before reading it:
   • DEVICE PANELS (pads, keyboard, tracks, DJ, mic) sit in a HUD frame: dark glass, a neon edge, corner brackets, a grid-lined title bar.
   • TRANSPORT keys are round hardware buttons (▶ green, ■ red, ● record red with a lit ring, ⏮ ↶ steel); SOFT KEYS under each screen
     are backlit rubber keys; the ⚙ More key is a hexagon.
   • MENU ENTRIES are angled holographic cards; EASY tiles are cut-corner plates; the RAIL is a column of glass keys with a lit edge.
   • CHIPS and small buttons are beveled tags; the big go-buttons are angled with a light sweep.
   The shapes never change what a control does, its size or its key. */
 const css=document.createElement('style'); css.id='kSkin246'; css.textContent=`
:root{--k6a:#2ad4ff;--k6b:#b46bff;--k6c:#ff2d95;--k6g:#00e08a;--k6r:#ff2d55;--k6glass:rgba(14,16,34,.82);--k6edge:rgba(42,212,255,.55)}
/* ── device panels: the HUD frame ── */
html body .kFloat.kFOn:not(.kFOff){background:linear-gradient(160deg,rgba(18,22,44,.94),rgba(8,9,22,.96))!important;border:1px solid var(--k6edge)!important;border-radius:14px!important;box-shadow:0 0 0 1px rgba(180,107,255,.25),0 18px 48px rgba(0,0,0,.6),inset 0 0 40px rgba(42,212,255,.06)!important;backdrop-filter:blur(8px)}
html body .kFloat.kFOn:not(.kFOff)::before,html body .kFloat.kFOn:not(.kFOff)::after{content:"";position:absolute;width:18px;height:18px;pointer-events:none;z-index:3}
html body .kFloat.kFOn:not(.kFOff)::before{left:-1px;top:-1px;border-left:3px solid var(--k6a);border-top:3px solid var(--k6a);border-top-left-radius:14px}
html body .kFloat.kFOn:not(.kFOff)::after{right:-1px;bottom:-1px;border-right:3px solid var(--k6b);border-bottom:3px solid var(--k6b);border-bottom-right-radius:14px}
html body .kFloat .kFHead{background:linear-gradient(90deg,rgba(42,212,255,.16),rgba(180,107,255,.12)),repeating-linear-gradient(90deg,transparent 0 11px,rgba(255,255,255,.04) 11px 12px)!important;border-bottom:1px solid var(--k6edge)!important;letter-spacing:.04em;text-transform:none}
html body .kFloat .kFHead b{font-family:ui-monospace,SFMono-Regular,Menlo,monospace!important;font-weight:800!important;color:#bff3ff!important;text-shadow:0 0 10px rgba(42,212,255,.45)}
html body .kFloat .kFHead [data-fh]{border-radius:8px!important;background:rgba(255,255,255,.06)!important;border:1px solid rgba(255,255,255,.18)!important}
html body .kFloat .kFHead [data-fh="x"],html body .kFloat .kFHead [data-fh]:last-child{border-color:rgba(255,45,85,.6)!important;color:#ffb3c4!important}
/* ── transport: round hardware buttons ── */
html body :is(#mpcBar,#kbDash) .kDevTx button{border-radius:50%/46%!important;background:radial-gradient(circle at 50% 30%,#3a4058,#171a28 70%)!important;border:1px solid rgba(255,255,255,.18)!important;box-shadow:inset 0 2px 0 rgba(255,255,255,.12),inset 0 -3px 6px rgba(0,0,0,.6),0 3px 8px rgba(0,0,0,.5)!important;color:#e9f6ff!important}
html body :is(#mpcBar,#kbDash) .kDevTx button[data-tx="play"]{background:radial-gradient(circle at 50% 30%,#2fe38f,#0b6b3d 72%)!important;border-color:#7dffb8!important}
html body :is(#mpcBar,#kbDash) .kDevTx button[data-tx="stop"]{background:radial-gradient(circle at 50% 30%,#ff6b7f,#8f1026 72%)!important;border-color:#ffb3c0!important}
html body :is(#mpcBar,#kbDash) .kDevTx button[data-tx="rec"]{background:radial-gradient(circle at 50% 30%,#ff4d6d,#7a0a1f 72%)!important;border-color:#ff8fa3!important;box-shadow:0 0 0 2px rgba(255,45,85,.35),0 0 14px rgba(255,45,85,.45),inset 0 2px 0 rgba(255,255,255,.15)!important}
html body .kDevTx button:active{transform:translateY(1px) scale(.97)}
/* ── soft keys under the screens: backlit rubber ── */
html body :is(#mpcBar,#kbDash) .kScr button[data-sf]{border-radius:7px 7px 11px 11px!important;background:linear-gradient(180deg,#2b3045,#191c2b)!important;border:1px solid rgba(255,255,255,.14)!important;border-bottom:3px solid rgba(42,212,255,.55)!important;box-shadow:0 2px 6px rgba(0,0,0,.5)!important;color:#dff7ff!important}
html body .kScr [data-sf].on,html body .kScr [data-sf][aria-pressed="true"]{border-bottom-color:#ffe94a!important;box-shadow:0 0 12px rgba(255,233,74,.35)!important}
/* ── ⚙ More: a hexagon ── */
html body .kEzMore{clip-path:polygon(12% 0,88% 0,100% 50%,88% 100%,12% 100%,0 50%)!important;border-radius:0!important;background:linear-gradient(135deg,#3b2a7a,#1b1640)!important;color:#e9dcff!important;border:0!important;padding:0 16px!important}
html body .kEzMore.on{background:linear-gradient(135deg,#ffe94a,#ffb800)!important;color:#14163a!important}
/* ── the transport bar and the DJ mode bar ── */
html body #bbBar button,html body .kDjBar button{border-radius:4px 12px 4px 12px!important;background:linear-gradient(180deg,rgba(42,212,255,.14),rgba(20,22,44,.9))!important;border:1px solid rgba(42,212,255,.4)!important}
html body .kDjBar button.on{background:linear-gradient(135deg,#ffe94a,#ffb800)!important;color:#14163a!important}
html body .kDjBar button.dj.on{background:linear-gradient(135deg,#2ad4ff,#1f7dff)!important;color:#04121f!important}
/* ── the track sequencer ── */
html body #kSeqWin .sqTop button{border-radius:4px 12px 4px 12px!important}
html body #kSeqWin .sqHead .c button{border-radius:5px!important;border:1px solid rgba(255,255,255,.16)!important}
html body #kSeqWin .sqHead .c button.arm.on{box-shadow:0 0 10px rgba(255,45,85,.6)!important}
html body #kSeqWin .sqBody{border-color:var(--k6edge)!important;box-shadow:inset 0 0 30px rgba(42,212,255,.05)}
/* ── the menu: angled holographic cards ── */
html body #tourTab .kStartB{border-radius:6px 18px 6px 18px!important;background:linear-gradient(135deg,rgba(122,44,255,.9),rgba(255,45,149,.85))!important;border:1px solid rgba(255,255,255,.35)!important;box-shadow:0 6px 18px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.35)!important;position:relative;overflow:hidden}
html body #tourTab .kStartB::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.18) 45%,transparent 60%);transform:translateX(-120%);transition:transform .6s ease;pointer-events:none}
html body #tourTab .kStartB:hover::after{transform:translateX(120%)}
html body #tourTab .kMenuH{font-family:ui-monospace,Menlo,monospace!important;letter-spacing:.06em}
/* ── Easy tiles: cut-corner plates ── */
html body .kEasy .ezGrid button{clip-path:polygon(0 0,calc(100% - 18px) 0,100% 18px,100% 100%,18px 100%,0 calc(100% - 18px));border-radius:0!important;background:linear-gradient(160deg,#2c2780,#15123f)!important;border:0!important;box-shadow:inset 0 0 0 2px rgba(42,212,255,.35)!important}
html body .kEasy .ezGrid button.go{background:linear-gradient(160deg,#18a957,#0b5e32)!important}
html body .kEasy .ezGrid button.st{background:linear-gradient(160deg,#d42a44,#7c0a1d)!important}
html body .kEasy .ezGrid button.ud{background:linear-gradient(160deg,#ffe94a,#ffb800)!important;color:#14163a!important}
html body .kEasy{border-image:linear-gradient(135deg,var(--k6a),var(--k6b),var(--k6c)) 1!important;border-radius:0!important}
html body .kEzRow button{border-radius:4px 14px 4px 14px!important}
/* ── the rail: glass keys with a lit edge ── */
html body #rDock#rDock > button{background:linear-gradient(180deg,rgba(30,34,64,.92),rgba(12,13,30,.92))!important;border:1px solid rgba(42,212,255,.35)!important;border-left:3px solid var(--k6a)!important;border-radius:10px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 4px 12px rgba(0,0,0,.4)!important}
html body #rDock#rDock > button:hover{border-left-color:var(--k6c)!important;box-shadow:0 0 14px rgba(42,212,255,.35)!important}
/* ── my page and its cards ── */
html body #kAcct .kaCard{background:linear-gradient(160deg,rgba(24,26,54,.85),rgba(10,10,26,.85))!important;border:1px solid var(--k6edge)!important;border-radius:4px 18px 4px 18px!important;box-shadow:inset 0 0 30px rgba(42,212,255,.05)}
html body #kAcct button{border-radius:4px 12px 4px 12px!important}
html body #kAcct .kaGo{clip-path:polygon(0 0,calc(100% - 14px) 0,100% 50%,calc(100% - 14px) 100%,0 100%);border-radius:0!important;padding-right:26px!important}
html body #kAcct .kaChip,html body .kEzMoreChip{border-radius:3px 10px 3px 10px!important}
html body #kAcct .kaStats div{border-left:3px solid var(--k6a);border-radius:2px 10px 2px 10px!important}
/* ── the cannon: a rotating targeting ring ── */
#kCannonBtn::before{content:"";position:absolute;inset:-7px;border-radius:50%;border:2px dashed rgba(255,233,74,.7);animation:k6spin 6s linear infinite;pointer-events:none}
@keyframes k6spin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){ #kCannonBtn::before{animation:none} html body #tourTab .kStartB::after{display:none} }
/* ── compress: a little tighter everywhere it is safe ── */
html body .kDevTx{gap:4px!important}
html body .kScr .kSoft{gap:4px!important}`; document.head.appendChild(css);
 window.KSKIN={version:'246'};
})();
