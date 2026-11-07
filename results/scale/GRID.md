# The six organisms: the full grid

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models of the plants, not hardware). Every organism runs native (its own controllers) and native with Omni-Compass on top (the compass law on every muscle, Omni v3, `docs/OMNI_V3.md`) on the same seed, the same load and the same clock. **Size** is the number of copies of the organism governed together on one clock: 1, 10, 100 and 1,000 clusters. **Runs** are paired seeds from 7000 on; 1, 10, 100 and 1,000 runs are the first N of the same set, so each block nests inside the next. Built by `tools/grid.py` from the saved receipts in `results/scale/receipts/`; the v1 grid and its receipts are kept in `results/scale/v1/`. How to read it: `docs/HOW_TO_READ_THE_RESULTS.md`.

Sources:
- 1x: GitHub Actions workflow `six`, run 38013481499 (Omni v3, commit 3aac0ab7d384); the pooled receipt `six-receipts/SIX.md`, archived in `results/live/raw/run-38013481499/`.
- 10x: GitHub Actions workflow `six`, run 38013486081 (Omni v3, commit 3aac0ab7d384); the pooled receipt `six-receipts/SIX.md`, archived in `results/live/raw/run-38013486081/`.
- 100x: GitHub Actions workflow `six`, run 38013490262 (Omni v3, commit 3aac0ab7d384); the pooled receipt `six-receipts/SIX.md`, archived in `results/live/raw/run-38013490262/`.
- 1000x: GitHub Actions workflow `six`, run 37578946088 (Omni v3, commit 3edcfb68a6c6); the pooled receipt `six-receipts/SIX.md`, archived in `results/live/raw/run-37578946088/`.
- 1,000 runs at 1,000 clusters is not run: about 6,000 machine-hours, beyond the machines available.
- 100 runs at 1,000 clusters is not run yet: about 650 runner-hours (one run of the four stacked at 1,000 copies takes 2 to 3 hours).

## Work per energy, with Omni-Compass on top against native (the aim is higher)

| Organism (muscles) | 1x, 1 run | 1x, 10 runs | 1x, 100 runs | 1x, 1000 runs | 10x, 1 run | 10x, 10 runs | 10x, 100 runs | 10x, 1000 runs | 100x, 1 run | 100x, 10 runs | 100x, 100 runs | 100x, 1000 runs | 1000x, 1 run | 1000x, 10 runs | 1000x, 100 runs | 1000x, 1000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud (430) | +0.077% | +0.087% | +0.084% | +0.085% | +0.083% | +0.084% | +0.083% | +0.082% | +0.085% | +0.083% | +0.083% | to run | +0.083% | +0.083% | not run yet | not run |
| Physics / Robotics / Autonomous (376) | +0.093% | +0.061% | +0.064% | +0.064% | +0.070% | +0.067% | +0.070% | +0.070% | +0.070% | +0.068% | +0.069% | to run | +0.072% | +0.070% | not run yet | not run |
| Energy / Facility / Industrial (470) | +0.318% | +0.390% | +0.366% | +0.368% | +0.356% | +0.349% | +0.360% | +0.358% | +0.357% | +0.358% | +0.364% | to run | +0.360% | +0.365% | not run yet | not run |
| Distribution / Specialized (440) | +0.214% | +0.164% | +0.176% | +0.171% | +0.201% | +0.190% | +0.194% | +0.192% | +0.206% | +0.203% | +0.205% | to run | +0.209% | +0.211% | not run yet | not run |
| The four stacked, duplicates kept (1716) | +0.401% | +0.393% | +0.368% | +0.354% | +0.375% | +0.366% | +0.361% | +0.362% | +0.368% | +0.364% | +0.364% | to run | +0.360% | +0.364% | not run yet | not run |
| The whole tower, every muscle once (945) | +0.318% | +0.387% | +0.365% | +0.367% | +0.356% | +0.348% | +0.359% | +0.357% | +0.357% | +0.357% | +0.363% | to run | +0.359% | +0.364% | not run yet | not run |

## Energy, with Omni-Compass on top against native (the aim is lower)

| Organism (muscles) | 1x, 1 run | 1x, 10 runs | 1x, 100 runs | 1x, 1000 runs | 10x, 1 run | 10x, 10 runs | 10x, 100 runs | 10x, 1000 runs | 100x, 1 run | 100x, 10 runs | 100x, 100 runs | 100x, 1000 runs | 1000x, 1 run | 1000x, 10 runs | 1000x, 100 runs | 1000x, 1000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud (430) | -0.077% | -0.087% | -0.084% | -0.085% | -0.082% | -0.083% | -0.082% | -0.082% | -0.085% | -0.083% | -0.083% | to run | -0.083% | -0.083% | not run yet | not run |
| Physics / Robotics / Autonomous (376) | -0.092% | -0.066% | -0.064% | -0.064% | -0.069% | -0.069% | -0.070% | -0.070% | -0.070% | -0.069% | -0.070% | to run | -0.072% | -0.071% | not run yet | not run |
| Energy / Facility / Industrial (470) | -0.317% | -0.389% | -0.364% | -0.367% | -0.354% | -0.348% | -0.358% | -0.357% | -0.356% | -0.357% | -0.363% | to run | -0.359% | -0.364% | not run yet | not run |
| Distribution / Specialized (440) | -0.213% | -0.164% | -0.176% | -0.171% | -0.200% | -0.189% | -0.193% | -0.192% | -0.205% | -0.203% | -0.205% | to run | -0.208% | -0.210% | not run yet | not run |
| The four stacked, duplicates kept (1716) | -0.399% | -0.391% | -0.366% | -0.353% | -0.373% | -0.364% | -0.360% | -0.361% | -0.367% | -0.363% | -0.363% | to run | -0.359% | -0.363% | not run yet | not run |
| The whole tower, every muscle once (945) | -0.317% | -0.388% | -0.363% | -0.366% | -0.354% | -0.347% | -0.357% | -0.356% | -0.355% | -0.356% | -0.362% | to run | -0.358% | -0.363% | not run yet | not run |

## Time over the service line, with Omni-Compass on top minus native (percentage points) (the aim is lower; band first holds where it is at or under 0)

| Organism (muscles) | 1x, 1 run | 1x, 10 runs | 1x, 100 runs | 1x, 1000 runs | 10x, 1 run | 10x, 10 runs | 10x, 100 runs | 10x, 1000 runs | 100x, 1 run | 100x, 10 runs | 100x, 100 runs | 100x, 1000 runs | 1000x, 1 run | 1000x, 10 runs | 1000x, 100 runs | 1000x, 1000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud (430) | -0.018 | -0.015 | -0.015 | -0.016 | -0.015 | -0.015 | -0.016 | -0.016 | -0.016 | -0.016 | -0.016 | to run | -0.016 | -0.016 | not run yet | not run |
| Physics / Robotics / Autonomous (376) | -0.017 | -0.012 | -0.011 | -0.011 | -0.008 | -0.010 | -0.011 | -0.011 | -0.012 | -0.012 | -0.011 | to run | -0.011 | -0.011 | not run yet | not run |
| Energy / Facility / Industrial (470) | -0.020 | -0.017 | -0.016 | -0.018 | -0.013 | -0.015 | -0.016 | -0.016 | -0.016 | -0.016 | -0.016 | to run | -0.016 | -0.016 | not run yet | not run |
| Distribution / Specialized (440) | -0.014 | -0.012 | -0.011 | -0.012 | -0.016 | -0.014 | -0.015 | -0.015 | -0.014 | -0.014 | -0.014 | to run | -0.014 | -0.015 | not run yet | not run |
| The four stacked, duplicates kept (1716) | -0.018 | -0.017 | -0.019 | -0.019 | -0.018 | -0.018 | -0.017 | -0.018 | -0.017 | -0.018 | -0.017 | to run | -0.017 | -0.017 | not run yet | not run |
| The whole tower, every muscle once (945) | -0.010 | -0.008 | -0.008 | -0.008 | -0.006 | -0.007 | -0.007 | -0.007 | -0.007 | -0.008 | -0.008 | to run | -0.007 | -0.008 | not run yet | not run |

## Work done, with Omni-Compass on top against native (equal is the guardrail)

| Organism (muscles) | 1x, 1 run | 1x, 10 runs | 1x, 100 runs | 1x, 1000 runs | 10x, 1 run | 10x, 10 runs | 10x, 100 runs | 10x, 1000 runs | 100x, 1 run | 100x, 10 runs | 100x, 100 runs | 100x, 1000 runs | 1000x, 1 run | 1000x, 10 runs | 1000x, 100 runs | 1000x, 1000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud (430) | -0.000% | +0.000% | +0.000% | +0.000% | +0.001% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | to run | +0.000% | +0.000% | not run yet | not run |
| Physics / Robotics / Autonomous (376) | -0.000% | -0.005% | -0.001% | +0.000% | +0.001% | -0.002% | -0.001% | -0.001% | +0.000% | -0.001% | -0.001% | to run | -0.001% | -0.001% | not run yet | not run |
| Energy / Facility / Industrial (470) | -0.000% | -0.000% | -0.000% | +0.000% | +0.001% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | to run | +0.000% | +0.000% | not run yet | not run |
| Distribution / Specialized (440) | -0.000% | +0.000% | -0.000% | +0.000% | +0.001% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | to run | +0.000% | +0.000% | not run yet | not run |
| The four stacked, duplicates kept (1716) | +0.001% | +0.000% | +0.000% | +0.000% | +0.001% | +0.000% | -0.000% | -0.000% | +0.000% | +0.000% | -0.000% | to run | -0.000% | -0.000% | not run yet | not run |
| The whole tower, every muscle once (945) | -0.000% | -0.002% | -0.000% | +0.000% | +0.001% | -0.000% | -0.000% | -0.000% | +0.000% | -0.000% | -0.000% | to run | -0.000% | -0.000% | not run yet | not run |

## Label by the preregistered rule (chosen by code, never by hand)

| Organism (muscles) | 1x, 1 run | 1x, 10 runs | 1x, 100 runs | 1x, 1000 runs | 10x, 1 run | 10x, 10 runs | 10x, 100 runs | 10x, 1000 runs | 100x, 1 run | 100x, 10 runs | 100x, 100 runs | 100x, 1000 runs | 1000x, 1 run | 1000x, 10 runs | 1000x, 100 runs | 1000x, 1000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud (430) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |
| Physics / Robotics / Autonomous (376) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |
| Energy / Facility / Industrial (470) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |
| Distribution / Specialized (440) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |
| The four stacked, duplicates kept (1716) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |
| The whole tower, every muscle once (945) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | GAIN (within the guardrails) | ONE RUN (no label) | GAIN (within the guardrails) | GAIN (within the guardrails) | to run | ONE RUN (no label) | GAIN (within the guardrails) | not run yet | not run |

## Summary of the completed cells

- Cells completed: 78 of 90 (six organisms x 15 size and run cells).
- Band first held: 78 of 78.
- Every knob handed back in every completed cell: True.
- Work done: the largest cost in any completed cell is 0.005% (thermal zones held warmer have a little less margin in a heat spike; `docs/REALMS_PREREGISTRATION.md`), inside the 2% the rule allows (`DISCLOSURES.md`, section 3).
- The full receipt of each size, with the 95% interval of every number, is in `results/scale/receipts/`.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
