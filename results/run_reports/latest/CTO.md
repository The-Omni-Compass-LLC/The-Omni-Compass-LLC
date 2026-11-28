# The 500-run set from the jump generator, base 3187436294: the report for the CTO

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Engine omni-v27 (digest 34548e45437a05bd, 65 files); the set written 2026-11-28T10:52:47Z; GitHub run 46137109254 (engine-runs, commit `327b8ea6cc`, https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/46137109254). Evidence class S: the engine's own models, run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live engine's monograph, section 4.1). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The answer

Omni-Compass brought 500 of 500 runs to a stable basin. The plant left alone brought 480. Omni-Compass certified 500; the plant alone 437. Omni-Compass got there in 5.59 macro steps on average; the plant alone took 9.64. Every gauge reads GAIN, in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the page's own code, computed it independently and gave the same digest on all 500 runs. That is not an opinion. It is arithmetic, and anyone can repeat it.

| Gauge (what it is for) | Native alone | Omni-Compass on top | Change against native | 95% interval | Reading |
|---|---|---|---|---|---|
| runs brought to a basin, conveyed (more is better) | 480 of 500 | 500 of 500 | up 4.2% | raw +2.4 to +6.1 points | GAIN |
| runs certified in a basin (more is better) | 437 of 500 | 500 of 500 | up 14.4% | raw +9.9 to +15.8 points | GAIN |
| macro steps to be conveyed, mean (fewer is better) | 9.637 | 5.590 | down 42.0% | raw −4.38 to −3.72 steps | GAIN |

## 2. The proof: three implementations, one digest

| Set | The Python's digest | The C++ harness | The live page's own code |
|---|---|---|---|
| the engine's runs | `73a5138981384318…` | `73a5138981384318…`, the same, 500 of 500 runs agree | `73a5138981384318…`, the same |
| the core's Monte Carlo | `a44ad71830cf284e…` | `a44ad71830cf284e…`, the same, 2000 of 2000 run-ways agree | `a44ad71830cf284e…`, the same |

The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by the page or the C++ is checked against the Python's rung.

| Rung | Runs | The Python's digest | The C++ harness's digest | The same |
|---|---|---|---|---|
| 1 | 1 | `a8f63b9ed973d142…` | `a8f63b9ed973d142…` | yes |
| 2 | 10 | `614330e7b4fa20ff…` | `614330e7b4fa20ff…` | yes |
| 3 | 100 | `44fc46f44894d8b7…` | `44fc46f44894d8b7…` | yes |
| 4 | 500 | `73a5138981384318…` | `73a5138981384318…` | yes |

## 3. Every way of the core's Monte Carlo

| Way | Conveyed (95% interval) | Certified | Mean step conveyed | In a basin at the last step |
|---|---|---|---|---|
| Omni-Compass on top, toward the nearest basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.590 | 500 of 500 |
| native: the plant alone, u = 0 | 480 of 500 (93.9% to 97.4%) | 437 of 500 | 9.637 | 478 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 6.710 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.578 | 500 of 500 |

## 4. Check it yourself

```
bash scripts/prove_runs.sh 3187436294 500
```

Or run the public workflow `prove-runs.yml` on GitHub, or the container `deploy/Dockerfile.proof`. The same base gives the same digests on any machine. A different digest is a fault, and it would show.

## 5. Where it stops

- This is a model (class S): the engine's own mathematics on its own ranges, not a benchmark of real software.
- The measured results (class L, live software; class P, a physical meter) are the three-run tables, each on its own engine, read by the same key, losses included.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
