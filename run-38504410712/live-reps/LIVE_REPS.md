# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1390 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1390 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 458.2 | 290.9 |
| response time (ms), 95th percentile | 1705 | 994.3 |
| response time (ms), 99th percentile | 5315 | 4599 |
| time over the response line (% of samples) | 32.35 | 21.93 |
| failed requests (%) | 18.94 | 16.65 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.822 | 2.244 |
| utilisation (used / allocatable) | 0.1104 | 0.1094 |
| CPU used (cores), mean | 2.648 | 2.625 |
| Omni's own CPU (cores), mean | 0 | 0.009333 |
| CPU used with Omni's own (cores), mean | 2.648 | 2.635 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.3 | 305.3 |
| HPA replicas, mean | 9.9 | 13.4 |
| pods started | 6.667 | 10.67 |
| pod start wait, total (s) | 28.67 | 32.67 |
| pod start wait, mean (s) | 3.828 | 3.105 |
| host CPU busy, the real machine under kind (%) | 74.31 | 74.74 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.207e-15 to +2.207e-15 | no |
| node-hours | 12.01 | 12.02 | +0.0% | -0.01471 to +0.02138 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1390 | -0.1% | -6.249 to +4.06 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1390 | -0.1% | -6.249 to +4.06 | no |
| response time (ms), mean | 458.2 | 290.9 | -36.5% | -441.3 to +106.8 | no |
| response time (ms), 95th percentile | 1705 | 994.3 | -41.7% | -2274 to +851.9 | no |
| response time (ms), 99th percentile | 5315 | 4599 | -13.5% | -1669 to +237 | no |
| time over the response line (% of samples) | 32.35 | 21.93 | -32.2% | -31.71 to +10.86 | no |
| failed requests (%) | 18.94 | 16.65 | -12.1% | -7.797 to +3.206 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.822 | 2.244 | -20.5% | -1.791 to +0.6353 | no |
| utilisation (used / allocatable) | 0.1104 | 0.1094 | -0.9% | -0.004864 to +0.002941 | no |
| CPU used (cores), mean | 2.648 | 2.625 | -0.9% | -0.1167 to +0.07059 | no |
| Omni's own CPU (cores), mean | 0 | 0.009333 | +0.00933 (native is 0) | +0.003655 to +0.01501 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.648 | 2.635 | -0.5% | -0.1023 to +0.07484 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.3 | 305.3 | -0.0% | -10.68 to +10.64 | no |
| HPA replicas, mean | 9.9 | 13.4 | +35.3% | -6.326 to +13.32 | no |
| pods started | 6.667 | 10.67 | +60.0% | -2.573 to +10.57 | no |
| pod start wait, total (s) | 28.67 | 32.67 | +14.0% | -55.78 to +63.78 | no |
| pod start wait, mean (s) | 3.828 | 3.105 | -18.9% | -5.076 to +3.63 | no |
| host CPU busy, the real machine under kind (%) | 74.31 | 74.74 | +0.6% | -1.348 to +2.203 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.033 | 117 | 97.5% | 0 | 0.87 | yes |
| omni | 2 | long |  |  |  | 0 | 1.017 | 117 | 97.5% | 0 | 0.94 | yes |
| omni | 3 | long |  |  |  | 0 | 1.067 | 120 | 100.0% | 0 | 1.22 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*