(()=>{ /* FIT (v209): every label stays inside its button, on a phone, a laptop, a desktop or a TV. The rail's labels are sized from the
   rail's own width, so its longest word ("Everyday", "Projects", "Karaoke") always fits; nothing is cut off with "…". Buttons and labels
   anywhere in the app that would spill out of their box wrap inside it instead. */
 const css=document.createElement('style'); css.textContent=`
html body #rDock#rDock button[data-kd-i]::after{font-size:clamp(8px,calc((var(--kRailW,58px) - 12px) / 5.1),15px)!important;letter-spacing:-.02em!important;text-overflow:clip!important;white-space:nowrap!important;overflow:visible!important;max-width:none!important}
html body #rDock#rDock>button{padding-left:1px!important;padding-right:1px!important;overflow:hidden}
@media (min-width:1700px){ :root{--kRailW:96px} html body #rDock#rDock button[data-kd-i]::before{font-size:30px!important} }
@media (min-width:2500px){ :root{--kRailW:124px} html body #rDock#rDock button[data-kd-i]::before{font-size:40px!important} }
/* any button's own words wrap inside the button instead of running out of it */
html body button:not([data-kd-i]):not(.pd):not(.mxs button){white-space:normal;overflow-wrap:anywhere;max-width:100%}
html body select,html body input{max-width:100%}
/* pop-ups never run under the rail: they stay between the left edge and the rail, and their close button stays in reach */
html body #qpDone{transform:none!important;translate:none!important;left:max(8px,calc((100vw - var(--kRailW,58px) - 960px) / 2))!important;right:max(calc(var(--kRailW,58px) + 8px),calc((100vw + var(--kRailW,58px) - 960px) / 2))!important;font-size:clamp(15px,1vw,22px)!important;width:auto!important;max-width:none!important;box-sizing:border-box!important;overflow-wrap:anywhere}
html body #qpDone button{max-width:100%}`; document.head.appendChild(css);
})();
