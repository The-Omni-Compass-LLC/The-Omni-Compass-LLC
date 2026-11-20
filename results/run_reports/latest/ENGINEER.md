# The 500-run set from the jump generator, base 1666194554: the report for the engineer

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Engine omni-v26 (digest 75d3c22eed4473b9, 65 files); the set written 2026-11-19T21:10:41Z; GitHub run 44615867514 (engine-runs, commit `4d660290cf`, https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/44615867514). Evidence class S: the engine's own models, run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live engine's monograph, section 4.1). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The answer

Omni-Compass brought 500 of 500 runs to a stable basin. The plant left alone brought 462. Omni-Compass certified 500; the plant alone 430. Omni-Compass got there in 5.60 macro steps on average; the plant alone took 9.64. Every gauge reads GAIN, in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the page's own code, computed it independently and gave the same digest on all 500 runs. That is not an opinion. It is arithmetic, and anyone can repeat it.

| Gauge (what it is for) | Native alone | Omni-Compass on top | Change against native | 95% interval | Reading |
|---|---|---|---|---|---|
| runs brought to a basin, conveyed (more is better) | 462 of 500 | 500 of 500 | up 8.2% | raw +5.4 to +10.3 points | GAIN |
| runs certified in a basin (more is better) | 430 of 500 | 500 of 500 | up 16.3% | raw +11.1 to +17.3 points | GAIN |
| macro steps to be conveyed, mean (fewer is better) | 9.636 | 5.604 | down 41.8% | raw −4.37 to −3.69 steps | GAIN |

## 2. The proof: three implementations, one digest

| Set | The Python's digest | The C++ harness | The live page's own code |
|---|---|---|---|
| the engine's runs | `1c5a3faf56bf39e2…` | `1c5a3faf56bf39e2…`, the same, 500 of 500 runs agree | `1c5a3faf56bf39e2…`, the same |
| the core's Monte Carlo | `4288fadb1f3e770d…` | `4288fadb1f3e770d…`, the same, 2000 of 2000 run-ways agree | `4288fadb1f3e770d…`, the same |

The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by the page or the C++ is checked against the Python's rung.

| Rung | Runs | The Python's digest | The C++ harness's digest | The same |
|---|---|---|---|---|
| 1 | 1 | `951f6c82f0924709…` | `951f6c82f0924709…` | yes |
| 2 | 10 | `44c3ac13dd38682d…` | `44c3ac13dd38682d…` | yes |
| 3 | 100 | `79994132d4b59478…` | `79994132d4b59478…` | yes |
| 4 | 500 | `1c5a3faf56bf39e2…` | `1c5a3faf56bf39e2…` | yes |

## 3. Every way of the core's Monte Carlo

| Way | Conveyed (95% interval) | Certified | Mean step conveyed | In a basin at the last step |
|---|---|---|---|---|
| Omni-Compass on top, toward the nearest basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.604 | 500 of 500 |
| native: the plant alone, u = 0 | 462 of 500 (89.7% to 94.4%) | 430 of 500 | 9.636 | 479 of 500 |
| Omni-Compass aimed at the wrong basin | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 6.670 | 500 of 500 |
| Omni-Compass on top, the double well's μ at 0 | 500 of 500 (99.2% to 100.0%) | 500 of 500 | 5.594 | 500 of 500 |

## 4. The mathematics

The seeds. Run k of the set draws its seed from the jump generator and feeds a mulberry32 stream:

  seedₖ = base + k·0x9E3779B9 mod 2³²,  k = 0, 1, …, 499;  base = 1666194554

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

Each of the 500 runs is 288 decisions of the brain (RK4), 80 steps of the compass law and one give-back trial judged by the verdict. The verdict allowed 204 of 500 trials (36.6% to 45.2% at 95%) and refused the rest. The verdict is do no harm as a trigger (the monograph, section 3.6): on log costs, d[v] = mean ln y[trial] − mean ln y[ref] with interval d[v] ± 1.96·se and allowance ln(1 + tol); an interval wholly above zero is a LOSS and the step is undone, otherwise the step stands only if the median and the mean lie within the allowance. Over all runs the brain's pushes sum to 1710.456; grants to expand 645780, to contract 228414. Every run's receipt is in `SET_ENGINE_RUNS.csv` beside this report.

## 6. Check it yourself

```
cmake -S cpp -B build && cmake --build build --target oc_engine_runs oc_core_runs
python3 tools/engine_runs.py --runs 500 --base 1666194554 --cpp build/oc_engine_runs --out er.json
python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all --runs 500 --base 1666194554
python3 tools/core_runs.py --runs 500 --base 1666194554 --cpp build/oc_core_runs --out cr.json
```

Both digests equal the records' or the run is wrong: `1c5a3faf56bf39e29fd0be45d852dadd238a80b7c7a083ec61c556274c2bd6f1` and `4288fadb1f3e770d584b624eb6453b460f90c38373f70de6603fcb01d842ae01`. The records: `results/engine_runs/ENGINE_RUNS_500_1666194554.md` and `results/core_runs/CORE_RUNS_500_1666194554.md`.

## 7. Where it stops

- This is a model (class S). It is never offered as a result on real software, a chip or a cloud.
- The mean step to be conveyed is over the runs that were conveyed; native's unconveyed runs are counted in the conveyed share, not in the mean.
- Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
