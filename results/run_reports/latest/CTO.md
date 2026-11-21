# The 500-run set from the jump generator, base 1892211197: the report for the CTO

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Engine omni-v27 (digest 34548e45437a05bd, 65 files); the set written 2026-11-21T00:10:51Z; GitHub run 44841884157 (engine-runs, commit `5b0bd1712f`, https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/44841884157). Evidence class S: the engine's own models, run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live engine's monograph, section 4.1). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The answer

Omni-Compass brought 500 of 500 runs to a stable basin. The plant left alone brought 475. Omni-Compass certified 500; the plant alone 438. Omni-Compass got there in 5.60 macro steps on average; the plant alone took 9.45. Every gauge reads GAIN, in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the page's own code, computed it independently and gave the same digest on all 500 runs. That is not an opinion. It is arithmetic, and anyone can repeat it.

| Gauge (what it is for) | Native alone | Omni-Compass on top | Change against native | 95% interval | Reading |
|---|---|---|---|---|---|
| runs brought to a basin, conveyed (more is better) | 475 of 500 | 500 of 500 | up 5.3% | raw +3.2 to +7.3 points | GAIN |
| runs certified in a basin (more is better) | 438 of 500 | 500 of 500 | up 14.2% | raw +9.7 to +15.6 points | GAIN |
| macro steps to be conveyed, mean (fewer is better) | 9.453 | 5.600 | down 40.8% | raw −4.17 to −3.53 steps | GAIN |

## 2. The proof: three implementations, one digest

| Set | The Python's digest | The C++ harness | The live page's own code |
|---|---|---|---|
| the engine's runs | `aea7ce2efe9c567c…` | `aea7ce2efe9c567c…`, the same, 500 of 500 runs agree | `aea7ce2efe9c567c…`, the same |
| the core's Monte Carlo | `3398a63b5259a406…` | `3398a63b5259a406…`, the same, 2000 of 2000 run-ways agree | `3398a63b5259a406…`, the same |

The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by the page or the C++ is checked against the Python's rung.

| Rung | Runs | The Python's digest | The C++ harness's digest | The same |
|---|---|---|---|---|
| 1 | 1 | `234a467e3ba79630…` | `234a467e3ba79630…` | yes |
| 2 | 10 | `1a88149c378874ff…` | `1a88149c378874ff…` | yes |
| 3 | 100 | `7728d2c2525a4472…` | `7728d2c2525a4472…` | yes |
| 4 | 500 | `aea7ce2efe9c567c…` | `aea7ce2efe9c567c…` | yes |

## 3. Every way of the core's Monte Carlo

| Way | Conveyed (95% interval) | Certified | Mean step conveyed | In a basin at the last step |
|---|---|---|---|---|
| Omni-Compass on top, toward the nearest basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.600 | 500 of 500 |
| native: the plant alone, u = 0 | 475 of 500 (92.7% to 96.6%) | 438 of 500 | 9.453 | 478 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 6.724 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.594 | 500 of 500 |

## 4. Check it yourself

```
bash scripts/prove_runs.sh 1892211197 500
```

Or run the public workflow `prove-runs.yml` on GitHub, or the container `deploy/Dockerfile.proof`. The same base gives the same digests on any machine. A different digest is a fault, and it would show.

## 5. Where it stops

- This is a model (class S): the engine's own mathematics on its own ranges, not a benchmark of real software.
- The measured results (class L, live software; class P, a physical meter) are the three-run tables, each on its own engine, read by the same key, losses included.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
