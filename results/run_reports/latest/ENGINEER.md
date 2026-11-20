# The 500-run set from the jump generator, base 1840383715: the report for the engineer

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

## 4. The mathematics

The seeds. Run k of the set draws its seed from the jump generator and feeds a mulberry32 stream:

  seedₖ = base + k·0x9E3779B9 mod 2³²,  k = 0, 1, …, 499;  base = 1840383715

The core (the monograph, section 3.2): the state z = (E, U, I[U], S, B, Ḃ) evolves by

  dE/dt = −α[E]·E + β[int] + β[ext] + v[eff]

  dU/dt = μ·U·(1 − U²) − (dE/dt)/E[max] − λ[U]·U + u[U],  |u[U]| ≤ U[auth]

  dI[U]/dt = (1 − U) − σ₁·E − δ·S − λ[I]·I[U]

  dS/dt = δ − α[s]·S − (3/4)·β[s]·S²,  dB/dt = Ḃ,  dḂ/dt = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B

integrated by the classical fourth-order Runge–Kutta method, 10 micro steps in each of 20 macro steps of Δt = 0.1 s, the command held through all four stages. Native is the plant left to its double well (u[U] = 0); Omni-Compass on top applies

  u[U] = sat(−f[U](z, t) + K[P]·(σ − U)),  K[P] = 12.0,  U[auth] = 25.0

A run is conveyed after 5 macro steps in a row in one basin, |U ∓ 1| ≤ 0.1, and certified at 10.

The intervals. A share k of n is given its Wilson score interval; a difference of two shares Newcombe's hybrid score interval (his method 10); a difference of two mean steps Welch's interval, the Satterthwaite degrees of freedom and the exact Student t quantile (`omnicompass/student_t.py`). The mean step is over the runs conveyed.

## 5. The engine's runs: the brain, the compass law and the verdict

Each of the 500 runs is 288 decisions of the brain (RK4), 80 steps of the compass law and one give-back trial judged by the verdict. The verdict allowed 202 of 500 trials (36.2% to 44.8% at 95%) and refused the rest. The verdict is do no harm as a trigger (the monograph, section 3.6): on log costs, d[v] = mean ln y[trial] − mean ln y[ref] with interval d[v] ± 1.96·se and allowance ln(1 + tol); an interval wholly above zero is a LOSS and the step is undone, otherwise the step stands only if the median and the mean lie within the allowance. Over all runs the brain's pushes sum to 1707.571; grants to expand 647514, to contract 227990. Every run's receipt is in `SET_ENGINE_RUNS.csv` beside this report.

## 6. Check it yourself

```
cmake -S cpp -B build && cmake --build build --target oc_engine_runs oc_core_runs
python3 tools/engine_runs.py --runs 500 --base 1840383715 --cpp build/oc_engine_runs --out er.json
python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all --runs 500 --base 1840383715
python3 tools/core_runs.py --runs 500 --base 1840383715 --cpp build/oc_core_runs --out cr.json
```

Both digests equal the records' or the run is wrong: `9cf2bfa93972c68527253804c2e04774a5ff708b2e66c8ca49ba2da1005df764` and `1d179164fcf2df58b39a6b6dbb3d6ee64b1c57cef8fe895400babbb2278f8ff9`. The records: `results/engine_runs/ENGINE_RUNS_500_1840383715.md` and `results/core_runs/CORE_RUNS_500_1840383715.md`.

## 7. Where it stops

- This is a model (class S). It is never offered as a result on real software, a chip or a cloud.
- The mean step to be conveyed is over the runs that were conveyed; native's unconveyed runs are counted in the conveyed share, not in the mean.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
