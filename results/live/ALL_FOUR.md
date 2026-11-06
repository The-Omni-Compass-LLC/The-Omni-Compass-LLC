# All four in one run: more work, faster, fewer machines, less energy: native against compass, ten paired repetitions on real Kubernetes

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37262789900, the live controller frozen at rules 1-8 (commit 353903683009; amendment 9, the brake at the idle floor, could not fire in this run: the service was never at its floor). Raw files with their SHA-256 sums: `results/live/raw/run-37262789900/`. Rebuilt with `python3 tools/live_reps.py` on those files.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.933 |
| node-hours | 4.51 | 4.462 |
| energy, parked workers still on at idle power (Wh, declared model) | 514.4 | 513.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.4 | 509.5 |
| response time (ms), mean | 268.5 | 150.7 |
| response time (ms), 95th percentile | 741.1 | 273.1 |
| response time (ms), 99th percentile | 2544 | 2031 |
| time over the response line (% of samples) | 17.88 | 10.61 |
| failed requests (%) | 9.856 | 8.632 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.48 |
| utilisation (used / allocatable) | 0.09873 | 0.09724 |
| CPU used (cores), mean | 2.37 | 2.314 |
| Omni's own CPU (cores), mean | 0 | 0.00858 |
| CPU used with Omni's own (cores), mean | 2.37 | 2.322 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313.8 | 320 |
| HPA replicas, mean | 9.491 | 9.075 |
| pods started | 4.5 | 4.9 |
| pod start wait, total (s) | 14.6 | 15.5 |
| pod start wait, mean (s) | 2.69 | 2.781 |
| host CPU busy, the real machine under kind (%) | 66.77 | 65.6 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.933 | -1.1% | -0.1301 to -0.003607 | yes: GAIN |
| node-hours | 4.51 | 4.462 | -1.1% | -0.09388 to -0.001734 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 514.4 | 513.2 | -0.2% | -2.14 to -0.143 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.4 | 509.5 | -1.0% | -8.426 to -1.403 | yes: GAIN |
| response time (ms), mean | 268.5 | 150.7 | -43.9% | -151.7 to -83.89 | yes: GAIN |
| response time (ms), 95th percentile | 741.1 | 273.1 | -63.1% | -625.9 to -310.1 | yes: GAIN |
| response time (ms), 99th percentile | 2544 | 2031 | -20.2% | -1483 to +457.3 | no |
| time over the response line (% of samples) | 17.88 | 10.61 | -40.7% | -10.26 to -4.292 | yes: GAIN |
| failed requests (%) | 9.856 | 8.632 | -12.4% | -1.913 to -0.5334 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.48 | +30.3% | -0.1365 to +0.3598 | no |
| utilisation (used / allocatable) | 0.09873 | 0.09724 | -1.5% | -0.002657 to -0.0003366 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.37 | 2.314 | -2.4% | -0.07066 to -0.04113 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00858 | +0.00858 (native is 0) | +0.00729 to +0.00987 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.37 | 2.322 | -2.0% | -0.06302 to -0.03162 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313.8 | 320 | +2.0% | +2.475 to +9.981 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.491 | 9.075 | -4.4% | -0.7764 to -0.05564 | yes: GAIN |
| pods started | 4.5 | 4.9 | +8.9% | -0.5656 to +1.366 | no |
| pod start wait, total (s) | 14.6 | 15.5 | +6.2% | -6.161 to +7.961 | no |
| pod start wait, mean (s) | 2.69 | 2.781 | +3.4% | -0.8044 to +0.9873 | no |
| host CPU busy, the real machine under kind (%) | 66.77 | 65.6 | -1.7% | -1.515 to -0.8193 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.6 |  |  | 10 |
| compass | 30.6 | +41.7% | +6.7 to +11.3 | 10 |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
