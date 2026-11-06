# The core's Monte Carlo: 500 runs from the jump generator (base 3654435075), example: heavy outside demand, a strong swing, little headroom, one digest

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each run: omnicompass/core.simulate, 20 macro steps of 10 fourth-order Runge–Kutta micro steps (Δt 0.1 s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 mod 2³², mulberry32, the live engine's own generator). Conveyed: 5 macro steps in a row in one basin (|U ∓ 1| ≤ 0.1); certified: 10. Written 2026-11-06T23:24:53Z. Class S.

**Digest d99a8f27efba16e8c91da37fa2b63ee22740e930164ccdfa736eb5fe5adcf31b** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port of the core and shows its own digest beside this one.

**The C++ twin** (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) on the same draws: digest d99a8f27efba16e8c91da37fa2b63ee22740e930164ccdfa736eb5fe5adcf31b, the same; 2000 of 2000 run-ways agree to 1e-9, largest difference 0.0e+00. The draws themselves, the injection: SHA-256 470944e883c2015fc9bdaea9d2eb0ef354d4b3a5a1f8116edae4126ede34fe8d.

**Your own system: example: heavy outside demand, a strong swing, little headroom.** An example of a system file, not any real stack: the outside demand into E high, the swing of the bath strong and fast, the headroom E_max small, the double well shallow. Its ranges (the rest are the engine's own): beta_ext 0.6 to 1; c 3 to 5; E_max 1 to 3; omega_B 2 to 5; mu 2 to 3.

| way | conveyed | certified | mean step conveyed | in a basin at step 20 |
|---|---:|---:|---:|---:|
| Omni-Compass on top, toward the nearest basin | 500 of 500 | 500 of 500 | 5.534 | 500 of 500 |
| native: the plant alone, u = 0 | 374 of 500 | 224 of 500 | 12.644385 | 350 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 | 500 of 500 | 6.728 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 | 500 of 500 | 5.524 | 500 of 500 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
