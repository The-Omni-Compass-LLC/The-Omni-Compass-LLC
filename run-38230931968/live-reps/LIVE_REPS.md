# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.8 | 172 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.8 | 172 |
| response time (ms), mean | 314.8 | 187.3 |
| response time (ms), 95th percentile | 884.3 | 465.6 |
| response time (ms), 99th percentile | 2997 | 2166 |
| time over the response line (% of samples) | 17.9 | 11.27 |
| failed requests (%) | 7.791 | 7.024 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5786 | 0.4619 |
| utilisation (used / allocatable) | 0.09411 | 0.09203 |
| CPU used (cores), mean | 2.259 | 2.209 |
| Omni's own CPU (cores), mean | 0 | 0.01201 |
| CPU used with Omni's own (cores), mean | 2.259 | 2.221 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327.7 | 336.8 |
| HPA replicas, mean | 9.331 | 9.411 |
| pods started | 5.571 | 5 |
| pod start wait, total (s) | 22.71 | 18 |
| pod start wait, mean (s) | 3.802 | 3.21 |
| host CPU busy, the real machine under kind (%) | 64.16 | 63.79 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 24.34 | 25.77 |
| robust: time over the line in the 120 s after the kill (% of samples) | 47.96 | 47.11 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 7 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.603e-16 to +1.168e-15 | same (under one part in a million) |
| node-hours | 1.515 | 1.521 | +0.4% | -0.001724 to +0.01315 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.8 | 172 | +0.1% | -0.481 to +0.8746 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.8 | 172 | +0.1% | -0.481 to +0.8746 | no |
| response time (ms), mean | 314.8 | 187.3 | -40.5% | -200.9 to -54.12 | yes, better |
| response time (ms), 95th percentile | 884.3 | 465.6 | -47.4% | -766 to -71.46 | yes, better |
| response time (ms), 99th percentile | 2997 | 2166 | -27.7% | -1889 to +227.8 | no |
| time over the response line (% of samples) | 17.9 | 11.27 | -37.1% | -11.65 to -1.618 | yes, better |
| failed requests (%) | 7.791 | 7.024 | -9.8% | -1.978 to +0.4455 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5786 | 0.4619 | -20.2% | -0.6158 to +0.3825 | no |
| utilisation (used / allocatable) | 0.09411 | 0.09203 | -2.2% | -0.002989 to -0.001173 | yes, less |
| CPU used (cores), mean | 2.259 | 2.209 | -2.2% | -0.07173 to -0.02815 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01201 | +0.012 (native is 0) | +0.009092 to +0.01494 | yes, more |
| CPU used with Omni's own (cores), mean | 2.259 | 2.221 | -1.7% | -0.06056 to -0.01529 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327.7 | 336.8 | +2.8% | +0.5693 to +17.6 | yes, more |
| HPA replicas, mean | 9.331 | 9.411 | +0.9% | -0.01921 to +0.1802 | no |
| pods started | 5.571 | 5 | -10.3% | -1.748 to +0.6054 | no |
| pod start wait, total (s) | 22.71 | 18 | -20.8% | -14.44 to +5.011 | no |
| pod start wait, mean (s) | 3.802 | 3.21 | -15.6% | -1.807 to +0.6233 | no |
| host CPU busy, the real machine under kind (%) | 64.16 | 63.79 | -0.6% | -0.7381 to -0.01794 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 24.34 | 25.77 | +5.9% | -4.957 to +7.81 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 47.96 | 47.11 | -1.8% | -8.363 to +6.651 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*