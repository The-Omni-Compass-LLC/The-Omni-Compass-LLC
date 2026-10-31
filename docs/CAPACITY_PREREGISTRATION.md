# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written on 12 October 2026, before any run of this test, at the founder's order. The engine is omni-v5 at its default,
the max (`tools/omni_version.py`); nothing in the engine changes for this test.

## The question

Omni-Compass does not have to cut energy or cost to help. It can use capacity the native controller leaves unused and
turn it into more completed work. This test asks that directly: hold native and Omni-Compass on top of native to **the
same resource cap**, at **several cap levels**, and at each level count the **work completed under the same latency and
failure limits**. If Omni completes more at a given cap, it does more with that capacity; if both complete more as the cap
rises, the comparison shows which turns each added unit of capacity into more completed work.

A run with a fixed offered load that both arms serve in full can show only faster service for that load. The KEDA
add-on run of 12 October is such a run: CPU used rose about 32% while the 95th-percentile response fell about 55%, on
the same six workers, with the offered load fixed; it shows faster service for the same work, not yet more completed
work. This test makes the load rise past what the cap can serve, so that completed work can differ.

## Design

- **Platform.** kind on GitHub's own machines, six workers (`deploy/kind/cluster-full.yaml`), the served app php-apache
  (`registry.k8s.io/hpa-example`) under its own HPA (target 50%), as in every kind set. **native**: Kubernetes alone.
  **compass**: Omni-Compass on top of the same (`scripts/kind_bench.sh`, the governor at nice 19: no organism runs here).
  Both arms of a repetition on one runner, each on a fresh cluster, the order rotated by repetition
  (`scripts/kind_paired.sh`).
- **The cap.** A ResourceQuota on the served app's CPU limits (`CAP_CPU_M` millicores in all, counted for the pods of the
  priority class `omni-capped`, so the load generator and the probe are outside it). The API server enforces it in both
  arms: a new pod or a raised limit past it is refused. Neither controller is told of it. **Cap levels: 1, 1.5, 2 and 3
  cores** (1000, 1500, 2000, 3000 millicores).
- **The load.** The work meter (`deploy/kind/loadgen-meter.yaml`): one open-loop generator stepping through rising rates
  (requests per second), each step an equal share of the window, the same requests in both arms whatever the service
  answers. Every request is counted: answered within the line (`SLO_MS`, 500 ms), answered late, failed (an error, or no
  answer within 10 s), or never sent (1,500 already waiting). The warm-up's requests (120 s, the first step's rate) are
  not counted.
- **Window.** 1,200 s per arm.
- **Repetitions.** 5 per cap level in each run; three runs, A, B and C (`tools/confirm_abc.py`, the three-run readings).
- **The rates, frozen on one tuning case.** Before the counted runs, one smoke run at the 2-core cap (one repetition,
  rates 5 10 20 30 40 60) shows where the cap saturates. The counted rates are then written here as an amendment, before
  run A: six steps rising from below what one core serves to above what three cores serve. The tuning case is not
  counted.

## Amendment 1 (12 October 2026, after the tuning case, before run A)

The tuning case (run 38280712498, the 2-core cap, one repetition, rates 5 10 20 30 40 60, not counted; its files in
`results/live/raw/capacity-run-38280712498/`) showed where the cap saturates, in both arms alike:

| Rate (requests a second) | 5 | 10 | 20 | 30 | 40 | 60 |
|---|---:|---:|---:|---:|---:|---:|
| Answered within the line, native | 100% | 90.7% | 1.4% | 0% | 0% | 0% |
| Answered within the line, Omni on top | 99.7% | 93.6% | 1.0% | 0% | 0% | 0% |

Two cores serve about 10 requests a second within the line (a request costs about 0.2 core-seconds of php-apache's CPU),
so one core serves about 5 and three cores about 15, and past the cap the service fails outright (87% of the 20-a-second
step failed). Steps of 5 then 10 then 20 can only say "5" for every cap from 1 to 3 cores, so the counted rates are set
finer, from below what one core serves to above what three cores serve, **eight steps of 150 s: 4 6 8 10 12 14 16 20**
requests a second (the workflow's default from this amendment on). Nothing else changes: the caps, the limits, the
window, the repetitions and the readings are as written above.

## Measures (the same limits in both arms)

- **Completed work**: the requests answered within the line over the whole window (`work_meter.json`, `total.in_time`).
- **Capacity**: the highest step rate the arm served while keeping **both limits**: at least 95% of the step's requests
  answered within the line, and no more than 1% failed or never sent; the first step that breaks a limit ends the count.
- Shown beside: the requests offered, the share failed or never sent, the 95th-percentile response from the probe
  (`scripts/latency_probe.py`).

## Readings

`tools/capacity_report.py` writes one row per cap level and one plain audit line under it:

- the paired difference in completed work (Omni on top minus native, pairs within one job) with its 95% interval:
  **GAIN** (the interval on the side of the gauge's aim), **LOSS** (below zero), or **no difference beyond the noise** (the interval
  includes zero);
- the same for capacity;
- a row where both arms answered at least 99% of everything offered within the line never met its cap: it shows speed,
  not more work, and its audit line says so;
- each step up in the cap: the completed work and the capacity each arm gains per added core.

Across runs A, B and C every row gets one of the three readings of `tools/readings.py`: GAIN or LOSS in all three of
our runs (the same sign in all three, every interval clear of zero, judged by the gauge's aim), STEADY (no difference beyond the noise), or the runs
disagree. Every row is reported, LOSS included; a LOSS's cause is looked for in our own wiring, setup and scoring first.

## Validity

An arm is left out, and listed, when it fails the bench's own checks (`scripts/kind_bench.sh`: the governor's decisions
inside the window, the reset handing every setting back, the work meter's final count present).

## What this test does not show

Energy and the bill are not judged here: the cap is fixed in both arms. The cap is a CPU quota on GitHub's 4-core
machine, shared by the seven kind nodes, not separate machines; a rented cloud run (Azure's managed Kubernetes) is the
place for machines. Evidence class **L** (the real thing: a real cluster, real requests, every answer counted).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
