# The live benchmark engine: acceptance in a real browser

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read on 2026-10-31 00:56 UTC by `tools/live_engine_acceptance.py` (`docs/engine/accept_live_engine.js`, Chromium through Playwright) from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` and, the same thirteen checks with the same result, from its one-file copy `docs/live/index.html`. Each line is what the browser read; a check that did not run says so.

| Check | Result | What the browser read | The rule |
|---|---|---|---|
| The page opens | **PASS** | loaded in 4863 ms; 53.0 MB as rendered | the load event within 180 s |
| Its title | **PASS** | “The Omni-Compass Live Benchmark Engine” | The Omni-Compass Live Benchmark Engine |
| The engine it names | **PASS** | data-engine omni-v22, prose omni-v22; the repository: omni-v22 | the engine `tools/omni_version.py` reads |
| No error in the page | **PASS** | 0 page errors, 0 console errors | none |
| Every contents link lands | **PASS** | 1210 links, 0 broken | none broken |
| GAIN is a green circle | **PASS** | border-radius 50%, rgb(80, 200, 120); drawn 4308 times | round, green |
| STEADY is a yellow diamond | **PASS** | rotated 45° (matrix(0.707107, 0.707107, -…), rgb(245, 197, 24); drawn 3469 times | a square turned 45°, yellow |
| LOSS is a red octagonal stop sign | **PASS** | the word's plate clipped to an octagon, rgb(255, 77, 85), a white octagon inside; drawn 3519 times | an octagon, red |
| The four live words | **PASS** | GAINING, STEADY, REDLINING, AWAITING, OVER THE LINE; 62 monitors, 910 signals | GAINING, STEADY, REDLINING, AWAITING, OVER THE LINE |
| The reflex runs on the engine's own numbers | **PASS** | the page {"streak": 3, "relief": 0.05, "margin": 0.05, "hold": 10, "holdMax": 160}; `omnicompass/immune.py` {"streak": 3, "relief": 0.05, "margin": 0.05, "hold": 10, "holdMax": 160} | equal, every one a knob on the panel |
| The reflex acts under a surge | **PASS** | decision 42: 0 hand-backs to native, 18 stays, 0 held native now | a hand-back or a stay recorded |
| The kill switch | **PASS** | pressed: every side native (True); pressed again: Omni-Compass on (True) | off at once, on again |
| A phone, 390 px | **PASS** | page 390 px wide on a 390 px screen; wide tables scroll inside their own box | no sideways scroll of the page |

## What the page's controls are

| Control | What it is |
|---|---|
| The monitors' recorded views, the receipts, the trading floor, the audit | read-only displays of committed receipts, each traced to its file and run |
| The live model, the mechanism's knobs, the reflex's knobs, the dial, the faults, the kill switch on the page | an interactive model in the browser (class S); nothing it does reaches any machine |
| The Prometheus reader | read-only queries to a Prometheus the viewer names; nothing is written |
| The run buttons | links to GitHub's own pages, where a person with access starts a workflow; the page starts nothing |
| Physical actuators | none: no control on this page writes to a real system; the engine's real writes are the governors' (`omni_controller/`), under their own authority and kill switch |

The page makes no request to any server of its own; it opens as one file, offline, or from any static host.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
