*© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# KAN-IN™ · Multi-Media Studio Platform: source

Built and powered by The Omni-Compass LLC · presents · DD Universe Multi-Media Studios' KAN-IN™.

This branch holds the app's source only. It is kept apart from `main` (the Omni-Compass engine) and is never merged into it.

| Path | What it is |
|---|---|
| `canon/canon.html` | The whole app in one file: every screen, engine and module, as published (version 244, build 20261127195105). |
| `modules/` | The newest modules, each also inside `canon.html`: the right-edge rail and panel (`krail.js`), levels (`klevel.js`), speed, click and timer (`kspeed.js`), options, layers and libraries (`kopts.js`), humor (`kfun.js`), the cannon jump generator (`kjump.js`), karaoke live (`kkara.js`), the owner's word (`kowner.js`), the video games (`kg4src.js`, built into `kgames4.js`) and their lobby, controller and controls monitor (`kvg.js`), the mobile hits (`kgames3.js`), the fixes from the whole-app inspection (`kfix191.js`), the studio console, rail and Menu order (`kstudio.js`), DD Universe Social with profiles (`ksocial.js`) the private on-device library (`klib.js`), the centered landing page (`kcenter.js`), the floating remote control (`kremote.js`), the Easel (`keasel.js`) the AI chat (`kai.js`), Projects with every export format (`kprojects.js`), 🔒 Lock & Shuffle with the loop tools (double the loop 1 → 2 → 4 → 8 → 16 → 32 bars, copy and paste a bar; `klock.js`) the knowledge library of music, writing, English, psychology, mathematics and games (`kknow.js`), the logo cannon, which lies flat as the hyphen of KAN-IN, turns up to 45° in two ticks, fires a die and turns back down (`kcanshot.js`) and the levels, which open on Everyday every time (`klevel.js`), the 👤 Profile tab with the birth date that picks the sign and the compass letter and the switch that lets the compass follow the profile or not (`kprofile.js`), the AI's hands: actions the AI can run in the app (`kai.js`), and the console's inputs: drum pads A1–A16 on channels 1–16, every other source wired by drop-down into channels 17–24, MPC-style real-time or latched pad recording, and the click's subdivision (`kio.js`). Every cannon in the opening game and on the landing fires one die as its bullet (`build/dicepatch.py`). Karaoke takes are layers with mute, solo, level, record-over and bounce (`kkara.js`). |
| `brand/` | The DD Universe Multi-Media Studios logo as used on the landing page (transparent WebP). |
| `build/` | The build: `addmod.py` puts a module into `canon.html` (`addmod2.py` replaces one in place, keeping the load order); `mkall.sh` builds the release into `pub/`. The voice recordings and the VCSL sample library are large and live in the published build, not here. |

Published at https://claude.ai/artifact/QZfheRnZwtzM4zFb65WUh9 (version 244).

*© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only. Any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
