# The core's Monte Carlo: 500 runs from the jump generator (base 375788817), example: heavy outside demand, a strong swing, little headroom, one digest

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each run: omnicompass/core.simulate, 20 macro steps of 10 fourth-order Runge–Kutta micro steps (Δt 0.1 s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 mod 2³², mulberry32, the live engine's own generator). Conveyed: 5 macro steps in a row in one basin (|U ∓ 1| ≤ 0.1); certified: 10. Written 2026-11-12T23:05:04Z. Class S.

**Digest 333517aee5267d9c52160fcafac08a4ae3d9033098a35c5537713bd26555577d** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port of the core and shows its own digest beside this one.

**The C++ twin** (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) on the same draws: digest 333517aee5267d9c52160fcafac08a4ae3d9033098a35c5537713bd26555577d, the same; 2000 of 2000 run-ways agree to 1e-9, largest difference 0.0e+00. The draws themselves, the injection: SHA-256 28e908884c3af8f85ed2720eaf541efd664fedb5847c7c59353753587d5e4a68.

**Your own system: example: heavy outside demand, a strong swing, little headroom.** An example of a system file, not any real stack: the outside demand into E high, the swing of the bath strong and fast, the headroom E_max small, the double well shallow. Its ranges (the rest are the engine's own): beta_ext 0.6 to 1; c 3 to 5; E_max 1 to 3; omega_B 2 to 5; mu 2 to 3.

| way | conveyed | certified | mean step conveyed | in a basin at step 20 |
|---|---:|---:|---:|---:|
| Omni-Compass on top, toward the nearest basin | 500 of 500 | 500 of 500 | 5.546 | 500 of 500 |
| native: the plant alone, u = 0 | 384 of 500 | 233 of 500 | 12.078125 | 337 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 | 500 of 500 | 6.704 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 | 500 of 500 | 5.538 | 500 of 500 |

**The live engine page's own port of the core** (run in node) on the same 500 runs in four ways: digest 333517aee5267d9c52160fcafac08a4ae3d9033098a35c5537713bd26555577d, the same; 2000 of 2000 lines agree, largest difference 0.0e+00. The page checked: SHA-256 5c9568ee0ca0c4467e3570693a6cbadec7be8b5feeebd5207a0f425194cf043c.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*