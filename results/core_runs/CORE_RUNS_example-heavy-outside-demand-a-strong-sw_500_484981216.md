# The core's Monte Carlo: 500 runs from the jump generator (base 484981216), example: heavy outside demand, a strong swing, little headroom, one digest

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each run: omnicompass/core.simulate, 20 macro steps of 10 fourth-order Runge–Kutta micro steps (Δt 0.1 s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 mod 2³², mulberry32, the live engine's own generator). Conveyed: 5 macro steps in a row in one basin (|U ∓ 1| ≤ 0.1); certified: 10. Written 2026-11-13T13:37:39Z. Class S.

**Digest 982d81cf283f253340eabf4c2e9557f651c9f73b2744563e32a78747bd14cf5d** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port of the core and shows its own digest beside this one.

**The C++ twin** (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) on the same draws: digest 982d81cf283f253340eabf4c2e9557f651c9f73b2744563e32a78747bd14cf5d, the same; 2000 of 2000 run-ways agree to 1e-9, largest difference 0.0e+00. The draws themselves, the injection: SHA-256 4e3a205f35baadea0450734d80fa425f2e716a91a9d1eecc7c224aa165c833c6.

**Your own system: example: heavy outside demand, a strong swing, little headroom.** An example of a system file, not any real stack: the outside demand into E high, the swing of the bath strong and fast, the headroom E_max small, the double well shallow. Its ranges (the rest are the engine's own): beta_ext 0.6 to 1; c 3 to 5; E_max 1 to 3; omega_B 2 to 5; mu 2 to 3.

| way | conveyed | certified | mean step conveyed | in a basin at step 20 |
|---|---:|---:|---:|---:|
| Omni-Compass on top, toward the nearest basin | 500 of 500 | 500 of 500 | 5.582 | 500 of 500 |
| native: the plant alone, u = 0 | 373 of 500 | 226 of 500 | 12.230563 | 330 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 | 500 of 500 | 6.714 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 | 500 of 500 | 5.578 | 500 of 500 |

**The live engine page's own port of the core** (run in node) on the same 500 runs in four ways: digest 982d81cf283f253340eabf4c2e9557f651c9f73b2744563e32a78747bd14cf5d, the same; 2000 of 2000 lines agree, largest difference 0.0e+00. The page checked: SHA-256 58037488565af4490d83453243b2fcbb79c698998f4844e8acfa0761b57b49e6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
