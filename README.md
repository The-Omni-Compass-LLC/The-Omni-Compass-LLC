*© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# KAN-IN™ · Multimedia Studio Platform: source

Built and powered by The Omni-Compass LLC · presents · DD Universe Multi-Media Studios' KAN-IN™.

This branch holds the app's source only. It is kept apart from `main` (the Omni-Compass engine) and is never merged into it.

| Path | What it is |
|---|---|
| `canon/canon.html` | The whole app in one file: every screen, engine and module, as published (version 195, build 20261119235523). |
| `modules/` | The newest modules, each also inside `canon.html`: the right-edge rail and panel (`krail.js`), levels (`klevel.js`), speed, click and timer (`kspeed.js`), options, layers and libraries (`kopts.js`), humor (`kfun.js`), the cannon jump generator (`kjump.js`), karaoke live (`kkara.js`), the owner's word (`kowner.js`), the video games (`kg4src.js`, built into `kgames4.js`) and their lobby, controller and controls monitor (`kvg.js`), the mobile hits (`kgames3.js`), the fixes from the whole-app inspection (`kfix191.js`), the studio console, rail and Menu order (`kstudio.js`), DD Universe Social with profiles (`ksocial.js`) the private on-device library (`klib.js`), the centered landing page (`kcenter.js`), the floating remote control (`kremote.js`), the Easel (`keasel.js`) and the AI chat (`kai.js`). |
| `brand/` | The DD Universe Multi-Media Studios logo as used on the landing page (transparent WebP). |
| `build/` | The build: `addmod.py` puts a module into `canon.html`; `mkall.sh` builds the release into `pub/`. The voice recordings and the VCSL sample library are large and live in the published build, not here. |

Published at https://claude.ai/artifact/QZfheRnZwtzM4zFb65WUh9 (version 195).

*© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
