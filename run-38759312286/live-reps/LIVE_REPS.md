# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 177.9 | 177.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.9 | 177.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 465.6 | 294.9 |
| response time (ms), 95th percentile | 1372 | 947.8 |
| response time (ms), 99th percentile | 5533 | 4165 |
| time over the response line (% of samples) | 33.53 | 23.28 |
| failed requests (%) | 19.03 | 16.82 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.78 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.22 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2944 | 0.4759 |
| utilisation (used / allocatable) | 0.1226 | 0.1204 |
| CPU used (cores), mean | 2.941 | 2.889 |
| Omni's own CPU (cores), mean | 0 | 0.01457 |
| CPU used with Omni's own (cores), mean | 2.941 | 2.904 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 242.1 | 246.1 |
| HPA replicas, mean | 9.622 | 9.826 |
| pods started | 4.222 | 4.889 |
| pod start wait, total (s) | 11.67 | 12.22 |
| pod start wait, mean (s) | 2.524 | 1.977 |
| host CPU busy, the real machine under kind (%) | 83.81 | 83.12 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 63.06 | 58.32 |
| robust: time over the line in the 120 s after the kill (% of samples) | 85.65 | 86.26 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.867e-16 to +7.788e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.514 | +0.1% | -0.001194 to +0.004157 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 177.9 | 177.6 | -0.2% | -0.7801 to +0.08902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.9 | 177.6 | -0.2% | -0.7801 to +0.08902 | no |
| response time (ms), mean | 465.6 | 294.9 | -36.7% | -212.2 to -129.1 | yes: GAIN |
| response time (ms), 95th percentile | 1372 | 947.8 | -30.9% | -760.1 to -87.8 | yes: GAIN |
| response time (ms), 99th percentile | 5533 | 4165 | -24.7% | -3186 to +450.7 | no |
| time over the response line (% of samples) | 33.53 | 23.28 | -30.6% | -12.47 to -8.045 | yes: GAIN |
| failed requests (%) | 19.03 | 16.82 | -11.6% | -3.235 to -1.186 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.78 | 11 | -13.9% | -2.29 to -1.265 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.22 | +52.2 (native is 0) | +46.3 to +58.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2944 | 0.4759 | +61.6% | -0.266 to +0.6289 | no |
| utilisation (used / allocatable) | 0.1226 | 0.1204 | -1.8% | -0.003048 to -0.001268 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.941 | 2.889 | -1.8% | -0.07314 to -0.03043 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01457 | +0.0146 (native is 0) | +0.01389 to +0.01524 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.941 | 2.904 | -1.3% | -0.05838 to -0.01606 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 242.1 | 246.1 | +1.7% | +1.707 to +6.285 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.622 | 9.826 | +2.1% | -0.07021 to +0.4795 | no |
| pods started | 4.222 | 4.889 | +15.8% | -1.912 to +3.245 | no |
| pod start wait, total (s) | 11.67 | 12.22 | +4.8% | -8.984 to +10.1 | no |
| pod start wait, mean (s) | 2.524 | 1.977 | -21.7% | -1.415 to +0.3208 | no |
| host CPU busy, the real machine under kind (%) | 83.81 | 83.12 | -0.8% | -1.078 to -0.3054 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 63.06 | 58.32 | -7.5% | -14.58 to +5.096 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 85.65 | 86.26 | +0.7% | -3.338 to +4.567 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*