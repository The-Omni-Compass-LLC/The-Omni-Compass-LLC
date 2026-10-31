# The core's Monte Carlo: 500 runs from the jump generator (base 1529763604), example: heavy outside demand, a strong swing, little headroom, one digest

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each run: omnicompass/core.simulate, 20 macro steps of 10 fourth-order Runge–Kutta micro steps (Δt 0.1 s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 mod 2³², mulberry32, the live engine's own generator). Conveyed: 5 macro steps in a row in one basin (|U ∓ 1| ≤ 0.1); certified: 10. Written 2026-10-25T10:23:13Z. Class S.

**Digest c794429c4700b3989aba7fcab2ce8e6a4ebc16c7b94ee44a15e51c263d67286e** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port of the core and shows its own digest beside this one.

**The C++ twin** (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) on the same draws: digest c794429c4700b3989aba7fcab2ce8e6a4ebc16c7b94ee44a15e51c263d67286e, the same; 2000 of 2000 run-ways agree to 1e-9, largest difference 0.0e+00. The draws themselves, the injection: SHA-256 9af11493721beb83676673e97c8129c901bad0dc6a3c9912d8f6337e5e50a983.

**Your own system: example: heavy outside demand, a strong swing, little headroom.** An example of a system file, not any real stack: the outside demand into E high, the swing of the bath strong and fast, the headroom E_max small, the double well shallow. Its ranges (the rest are the engine's own): beta_ext 0.6 to 1; c 3 to 5; E_max 1 to 3; omega_B 2 to 5; mu 2 to 3.

| way | conveyed | certified | mean step conveyed | in a basin at step 20 |
|---|---:|---:|---:|---:|
| Omni-Compass on top, toward the nearest basin | 500 of 500 | 500 of 500 | 5.538 | 500 of 500 |
| native: the plant alone, u = 0 | 374 of 500 | 243 of 500 | 12.216578 | 345 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 | 500 of 500 | 6.73 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 | 500 of 500 | 5.532 | 500 of 500 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
