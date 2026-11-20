# The 500-run set from the jump generator, base 1840383715: the report for the CTO

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Engine omni-v27 (digest 34548e45437a05bd, 65 files); the set written 2026-11-20T18:13:55Z; GitHub run 44790056675 (engine-runs, commit `aaa7a0de30`, https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/44790056675). Evidence class S: the engine's own models, run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live engine's monograph, section 4.1). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The answer

Omni-Compass brought 500 of 500 runs to a stable basin. The plant left alone brought 471. Omni-Compass certified 500; the plant alone 423. Omni-Compass got there in 5.55 macro steps on average; the plant alone took 9.59. Every gauge reads GAIN, in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the page's own code, computed it independently and gave the same digest on all 500 runs. That is not an opinion. It is arithmetic, and anyone can repeat it.

| Gauge (what it is for) | Native alone | Omni-Compass on top | Change against native | 95% interval | Reading |
|---|---|---|---|---|---|
| runs brought to a basin, conveyed (more is better) | 471 of 500 | 500 of 500 | up 6.2% | raw +3.9 to +8.2 points | GAIN |
| runs certified in a basin (more is better) | 423 of 500 | 500 of 500 | up 18.2% | raw +12.4 to +18.8 points | GAIN |
| macro steps to be conveyed, mean (fewer is better) | 9.594 | 5.552 | down 42.1% | raw −4.38 to −3.70 steps | GAIN |

## 2. The proof: three implementations, one digest

| Set | The Python's digest | The C++ harness | The live page's own code |
|---|---|---|---|
| the engine's runs | `9cf2bfa93972c685…` | `9cf2bfa93972c685…`, the same, 500 of 500 runs agree | `9cf2bfa93972c685…`, the same |
| the core's Monte Carlo | `1d179164fcf2df58…` | `1d179164fcf2df58…`, the same, 2000 of 2000 run-ways agree | `1d179164fcf2df58…`, the same |

The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by the page or the C++ is checked against the Python's rung.

| Rung | Runs | The Python's digest | The C++ harness's digest | The same |
|---|---|---|---|---|
| 1 | 1 | `6cdac5779590d913…` | `6cdac5779590d913…` | yes |
| 2 | 10 | `f738a614daed9930…` | `f738a614daed9930…` | yes |
| 3 | 100 | `538097e3aee5dc8f…` | `538097e3aee5dc8f…` | yes |
| 4 | 500 | `9cf2bfa93972c685…` | `9cf2bfa93972c685…` | yes |

## 3. Every way of the core's Monte Carlo

| Way | Conveyed (95% interval) | Certified | Mean step conveyed | In a basin at the last step |
|---|---|---|---|---|
| Omni-Compass on top, toward the nearest basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.552 | 500 of 500 |
| native: the plant alone, u = 0 | 471 of 500 (91.8% to 95.9%) | 423 of 500 | 9.594 | 468 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 6.720 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.538 | 500 of 500 |

## 4. Check it yourself

```
bash scripts/prove_runs.sh 1840383715 500
```

Or run the public workflow `prove-runs.yml` on GitHub, or the container `deploy/Dockerfile.proof`. The same base gives the same digests on any machine. A different digest is a fault, and it would show.

## 5. Where it stops

- This is a model (class S): the engine's own mathematics on its own ranges, not a benchmark of real software.
- The measured results (class L, live software; class P, a physical meter) are the three-run tables, each on its own engine, read by the same key, losses included.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
