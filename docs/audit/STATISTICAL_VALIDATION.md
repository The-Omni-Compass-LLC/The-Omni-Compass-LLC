# Statistical validation: every reading reconstructed from its raw values

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Written by `tools/audit_export.py` from `results/verdict_audit/VERDICT_AUDIT.json` (its digest `8aa378506a5bc917`), which `tools/verdict_audit.py` writes from every three-run table's stored native, Omni-Compass and difference. The engine that stands: omni-v23. Every row is in `docs/audit/BENCHMARK_DISCREPANCIES.csv`, one line per gauge, with each run's native and Omni-Compass values, the raw change with its true sign, the key's word, its class, the confidence, the practical significance and the run-to-run stability, apart from one another.

## The rule

- The raw change of a run is 100 × (Omni-Compass − native) / native, with its true sign. Where native stands at zero, the absolute difference is printed and the reading goes by the signs; no percentage is made.
- The gauge's declared aim decides the word, never the sign: time waited, missed or failed that fell is a GAIN; work that rose is a GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given, never a LOSS.
- A mean change under 0.5% of native reads STEADY, under the floor (BELOW PRACTICAL THRESHOLD). STEADY, exactly the same means every run's two values equal to nine decimal places of the value (STEADY (EXACT)); a smaller change measured past that is under the floor, never "the same".
- Runs that moved 0.5% or more in opposite directions read the runs disagree (RUNS DISAGREE), an unresolved reading.
- The confidence stands beside the word and never changes it: strong, every run the mean's way and beyond its noise (its 95% interval clear of zero); moderate, all but one; weak, one; statistically inconclusive, none. A table read by the key before 24 October that printed STEADY, no difference beyond the noise is classed STATISTICALLY INCONCLUSIVE.
- The three runs are three separate GitHub runs on the same engine, each holding its paired repetitions; within a run the 95% interval is the runner's own (Student t on the paired differences); across runs the interval of the mean change is Student t with 2 degrees of freedom on the three runs' changes (`omnicompass/student_t.py`).

## The independent check

Every one of the 11,069 rows was classed twice: as the key wrote it, and by `independent()` in `tools/audit_export.py`, written from the rule above with no code shared with `tools/readings.py` and each run's difference recomputed as Omni-Compass minus native from the stored values. **10,085 agree; 0 differ**; 984 cannot be recomputed from the committed record, for the reasons counted here (none of them is changed by this report: a table's words stay as its runner printed them).

| Why a row cannot be recomputed | the road | superseded | standing | taken out |
|---|---:|---:|---:|---:|
| not recomputable at nine decimals: the committed table printed its changes to two decimals; the runner's raw files hold the values | 73 | 201 | 101 | 0 |
| not recomputable: the printed changes round across the 0.5% floor | 1 | 0 | 0 | 0 |
| not recomputable: the record declares no aim for this gauge (a table of an earlier engine, its words kept as printed) | 570 | 0 | 14 | 24 |

A standing table that cannot be recomputed at nine decimals from the committed table is a traceability gap: its runner's raw files (on the branch `raw`, `scripts/raw_archive.sh open`) hold the values, and the next export reads them there.

## Standing tables, Omni-Compass against its native, by engine

Each benchmark's newest table on its own engine. A table on an older engine stands only until its three runs on the engine that stands land; nothing is read across engines.

| Engine | GAIN | LOSS | POWER GIVEN | STEADY (EXACT) | BELOW PRACTICAL THRESHOLD | STATISTICALLY INCONCLUSIVE | RUNS DISAGREE | RUNS DIFFER IN RIG | INVALID OR MISSING | SHOWN, NEVER JUDGED | TUNING, NEVER COUNTED |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| omni-v21 | 279 | 50 | 99 | 247 | 204 | 0 | 175 | 31 | 0 | 366 | 201 |
| omni-v12 | 139 | 113 | 31 | 90 | 46 | 0 | 96 | 0 | 0 | 216 | 0 |
| **all** | **418** | **163** | **130** | **337** | **250** | **0** | **271** | **31** | **0** | **582** | **201** |

## Confidence of the GAIN, LOSS and power given rows (standing, against native)

| Confidence | Rows |
|---|---:|
| statistically inconclusive | 261 |
| strong | 156 |
| weak | 109 |
| deterministic, reproduced in all three runs | 104 |
| moderate | 77 |
| not recorded (a table that printed its changes only) | 3 |
| 0 of 3 runs beyond their noise | 1 |

## Run-to-run stability (standing, against native, rows that moved)

| The runs | Rows |
|---|---:|
| moved one direction (0.5% or more) | 692 |
| moved in opposite directions (0.5% or more) | 261 |

The rows that disagree are not resolved by this report: each is a test unstable at that gauge, to be looked into (workload instability, the shared runner, baseline drift or too few repetitions) and run again; a disagreement is never counted as a GAIN or a LOSS.

## What this does not show

- Only 12 of the 85 standing tables ran on the engine that stands; the rest stand on the engine their table names until their three runs on it land. No older table's LOSS is presumed repaired.
- The classes describe the recorded runs (evidence class L: live software on GitHub's shared runners; S: our own models). They are not a claim about any other machine, workload or configuration.
- A resource spent that rose is power given: what it bought is in the same table's other rows; nothing here says it was worth it.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
