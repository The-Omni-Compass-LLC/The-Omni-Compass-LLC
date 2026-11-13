# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1398 | 1394 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1398 | 1394 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 490.2 | 265.1 |
| response time (ms), 95th percentile | 1798 | 771.3 |
| response time (ms), 99th percentile | 5106 | 3835 |
| time over the response line (% of samples) | 29.85 | 15.22 |
| failed requests (%) | 13.4 | 10.05 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.878 | 3.961 |
| utilisation (used / allocatable) | 0.1142 | 0.1111 |
| CPU used (cores), mean | 2.741 | 2.665 |
| Omni's own CPU (cores), mean | 0 | 0.01007 |
| CPU used with Omni's own (cores), mean | 2.741 | 2.676 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 259.4 | 266.4 |
| HPA replicas, mean | 9.937 | 15.51 |
| pods started | 5 | 19.67 |
| pod start wait, total (s) | 23.33 | 54.33 |
| pod start wait, mean (s) | 4.389 | 3.249 |
| host CPU busy, the real machine under kind (%) | 76.56 | 75.14 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.882e-16 to +8.882e-16 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.02 | +0.1% | -0.01607 to +0.03385 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1398 | 1394 | -0.3% | -9.792 to +0.8103 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1398 | 1394 | -0.3% | -9.792 to +0.8103 | no |
| response time (ms), mean | 490.2 | 265.1 | -45.9% | -464.8 to +14.6 | no |
| response time (ms), 95th percentile | 1798 | 771.3 | -57.1% | -2409 to +355.3 | no |
| response time (ms), 99th percentile | 5106 | 3835 | -24.9% | -3753 to +1210 | no |
| time over the response line (% of samples) | 29.85 | 15.22 | -49.0% | -28.95 to -0.3045 | yes: GAIN |
| failed requests (%) | 13.4 | 10.05 | -25.0% | -13.34 to +6.634 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.878 | 3.961 | +37.6% | -0.541 to +2.708 | no |
| utilisation (used / allocatable) | 0.1142 | 0.1111 | -2.8% | -0.005878 to -0.0004082 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.741 | 2.665 | -2.8% | -0.1411 to -0.009796 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01007 | +0.0101 (native is 0) | +0.009126 to +0.01101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.741 | 2.676 | -2.4% | -0.1316 to +0.0008853 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 259.4 | 266.4 | +2.7% | -2.581 to +16.46 | no |
| HPA replicas, mean | 9.937 | 15.51 | +56.1% | +5.076 to +6.073 | yes: power given |
| pods started | 5 | 19.67 | +293.3% | -11.19 to +40.52 | no |
| pod start wait, total (s) | 23.33 | 54.33 | +132.9% | -6.595 to +68.59 | no |
| pod start wait, mean (s) | 4.389 | 3.249 | -26.0% | -7.305 to +5.024 | no |
| host CPU busy, the real machine under kind (%) | 76.56 | 75.14 | -1.8% | -3.815 to +0.9855 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.041 | 119 | 99.2% | 0 | 0.67 | yes |
| omni | 2 | long |  |  |  | 0 | 1.035 | 118 | 98.3% | 0 | 1.07 | yes |
| omni | 3 | long |  |  |  | 0 | 1.026 | 117 | 97.5% | 0 | 0.83 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*