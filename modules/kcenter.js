(()=>{ /* THE LANDING PAGE, CENTERED: the KAN-IN cannon logo, the DD Universe logo, every line of text and every row of chips sit in the
   middle of the screen on a phone, a tablet and a desktop. The page keeps the same space on its left as it does beside the rail. */
 const css=document.createElement('style'); css.textContent=`
html body{margin:0!important;padding-left:max(16px,env(safe-area-inset-left,0px))!important;padding-right:calc(var(--kRailW,58px) + 16px)!important}
html body .wrap{margin-left:auto!important;margin-right:auto!important}
html body .mast,html body .mast .mark,html body .mast .mark>div,html body .mast .brandText{text-align:center!important}
html body .mast .mark{justify-content:center!important;align-items:center!important}
html body .mast .brandRow{justify-content:center!important;align-items:center!important}
html body .mast h1.kwmH1{justify-content:center!important;margin-left:auto!important;margin-right:auto!important;width:100%}
html body .mast p,html body .wrap>p,html body .mast .tag{text-align:center!important;margin-left:auto!important;margin-right:auto!important}
html body .mast .ownerline{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:6px}
html body .mast .chips,html body .wrap .chips{justify-content:center!important;margin-left:auto!important;margin-right:auto!important}
html body #master{text-align:center!important}
html body #master .mStat,html body #master .palRow{justify-content:center!important;align-items:center!important}
html body #master .mStat{flex-direction:column}`; document.head.appendChild(css);
})();
