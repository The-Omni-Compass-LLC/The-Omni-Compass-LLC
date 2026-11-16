# The 500-run set from the jump generator, base 841704626: the report for the engineer

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Engine omni-v26 (digest 75d3c22eed4473b9, 65 files); the set written 2026-11-16T02:38:04Z; GitHub run 43791377586 (engine-runs, commit `66c71e0bfc`, https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/43791377586). Evidence class S: the engine's own models, run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live engine's monograph, section 4.1). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The answer

Omni-Compass brought 500 of 500 runs to a stable basin. The plant left alone brought 474. Omni-Compass certified 500; the plant alone 425. Omni-Compass got there in 5.55 macro steps on average; the plant alone took 9.85. Every gauge reads GAIN, in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the page's own code, computed it independently and gave the same digest on all 500 runs. That is not an opinion. It is arithmetic, and anyone can repeat it.

| Gauge (what it is for) | Native alone | Omni-Compass on top | Change against native | 95% interval | Reading |
|---|---|---|---|---|---|
| runs brought to a basin, conveyed (more is better) | 474 of 500 | 500 of 500 | up 5.5% | raw +3.4 to +7.5 points | GAIN |
| runs certified in a basin (more is better) | 425 of 500 | 500 of 500 | up 17.6% | raw +12.0 to +18.4 points | GAIN |
| macro steps to be conveyed, mean (fewer is better) | 9.854 | 5.548 | down 43.7% | raw −4.66 to −3.95 steps | GAIN |

## 2. The proof: three implementations, one digest

| Set | The Python's digest | The C++ harness | The live page's own code |
|---|---|---|---|
| the engine's runs | `662488489f6a18ba…` | `662488489f6a18ba…`, the same, 500 of 500 runs agree | `662488489f6a18ba…`, the same |
| the core's Monte Carlo | `87b7f0ca77af844e…` | `87b7f0ca77af844e…`, the same, 2000 of 2000 run-ways agree | `87b7f0ca77af844e…`, the same |

The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by the page or the C++ is checked against the Python's rung.

| Rung | Runs | The Python's digest | The C++ harness's digest | The same |
|---|---|---|---|---|
| 1 | 1 | `6e787ff67f1a8192…` | `6e787ff67f1a8192…` | yes |
| 2 | 10 | `f21514559e9040b5…` | `f21514559e9040b5…` | yes |
| 3 | 100 | `e20b1e087cfbf845…` | `e20b1e087cfbf845…` | yes |
| 4 | 500 | `662488489f6a18ba…` | `662488489f6a18ba…` | yes |

## 3. Every way of the core's Monte Carlo

| Way | Conveyed (95% interval) | Certified | Mean step conveyed | In a basin at the last step |
|---|---|---|---|---|
| Omni-Compass on top, toward the nearest basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.548 | 500 of 500 |
| native: the plant alone, u = 0 | 474 of 500 (92.5% to 96.4%) | 425 of 500 | 9.854 | 474 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 6.680 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.544 | 500 of 500 |

## 4. The mathematics

The seeds. Run k of the set draws its seed from the jump generator and feeds a mulberry32 stream:

  seedₖ = base + k·0x9E3779B9 mod 2³²,  k = 0, 1, …, 499;  base = 841704626

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

Each of the 500 runs is 288 decisions of the brain (RK4), 80 steps of the compass law and one give-back trial judged by the verdict. The verdict allowed 194 of 500 trials (34.6% to 43.1% at 95%) and refused the rest. The verdict is do no harm as a trigger (the monograph, section 3.6): on log costs, d[v] = mean ln y[trial] − mean ln y[ref] with interval d[v] ± 1.96·se and allowance ln(1 + tol); an interval wholly above zero is a LOSS and the step is undone, otherwise the step stands only if the median and the mean lie within the allowance. Over all runs the brain's pushes sum to 1708.150; grants to expand 647982, to contract 226429. Every run's receipt is in `SET_ENGINE_RUNS.csv` beside this report.

## 6. Check it yourself

```
cmake -S cpp -B build && cmake --build build --target oc_engine_runs oc_core_runs
python3 tools/engine_runs.py --runs 500 --base 841704626 --cpp build/oc_engine_runs --out er.json
python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all --runs 500 --base 841704626
python3 tools/core_runs.py --runs 500 --base 841704626 --cpp build/oc_core_runs --out cr.json
```

Both digests equal the records' or the run is wrong: `662488489f6a18baca8f5af4f4cd8af6669ae6e033f5d2dc85d4d44208ed3074` and `87b7f0ca77af844edb4b8e5679d47d865a0b056ca8d44eb7d5535391f75c888c`. The records: `results/engine_runs/ENGINE_RUNS_500_841704626.md` and `results/core_runs/CORE_RUNS_500_841704626.md`.

## 7. Where it stops

- This is a model (class S). It is never offered as a result on real software, a chip or a cloud.
- The mean step to be conveyed is over the runs that were conveyed; native's unconveyed runs are counted in the conveyed share, not in the mean.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
