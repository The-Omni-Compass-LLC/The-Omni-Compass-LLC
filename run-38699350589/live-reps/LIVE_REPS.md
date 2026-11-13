# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.915 |
| node-hours | 1.494 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 164.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 163.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 228.9 | 130.8 |
| response time (ms), 95th percentile | 413.6 | 167.6 |
| response time (ms), 99th percentile | 1837 | 741.4 |
| time over the response line (% of samples) | 8.217 | 5.327 |
| failed requests (%) | 4.795 | 4.031 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.5967 |
| utilisation (used / allocatable) | 0.06956 | 0.06831 |
| CPU used (cores), mean | 1.645 | 1.616 |
| Omni's own CPU (cores), mean | 0 | 0.00935 |
| CPU used with Omni's own (cores), mean | 1.645 | 1.626 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 408.5 | 410.8 |
| HPA replicas, mean | 8.674 | 9.638 |
| pods started | 4.8 | 5.8 |
| pod start wait, total (s) | 15.6 | 22.4 |
| pod start wait, mean (s) | 2.868 | 4.232 |
| host CPU busy, the real machine under kind (%) | 47 | 46.22 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.915 | +0.0% | -0.002878 to +0.005493 | no |
| node-hours | 1.494 | 1.49 | -0.3% | -0.01363 to +0.00574 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 164.8 | -0.5% | -2.06 to +0.5065 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 163.2 | -0.5% | -2.027 to +0.5316 | no |
| response time (ms), mean | 228.9 | 130.8 | -42.9% | -158.2 to -38.14 | yes: GAIN |
| response time (ms), 95th percentile | 413.6 | 167.6 | -59.5% | -295.6 to -196.4 | yes: GAIN |
| response time (ms), 99th percentile | 1837 | 741.4 | -59.6% | -2074 to -117.8 | yes: GAIN |
| time over the response line (% of samples) | 8.217 | 5.327 | -35.2% | -4.015 to -1.766 | yes: GAIN |
| failed requests (%) | 4.795 | 4.031 | -15.9% | -1.318 to -0.2097 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.4 | -23.9% | -2.458 to -0.9422 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.5 | +29.5 (native is 0) | +24.9 to +34.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.5967 | +46.7% | -0.1363 to +0.5163 | no |
| utilisation (used / allocatable) | 0.06956 | 0.06831 | -1.8% | -0.003227 to +0.000728 | no |
| CPU used (cores), mean | 1.645 | 1.616 | -1.8% | -0.07561 to +0.01739 | no |
| Omni's own CPU (cores), mean | 0 | 0.00935 | +0.00935 (native is 0) | +0.008108 to +0.01059 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.626 | -1.2% | -0.06532 to +0.0258 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 408.5 | 410.8 | +0.6% | -10.3 to +14.91 | no |
| HPA replicas, mean | 8.674 | 9.638 | +11.1% | +0.3184 to +1.61 | yes: power given |
| pods started | 4.8 | 5.8 | +20.8% | -0.7843 to +2.784 | no |
| pod start wait, total (s) | 15.6 | 22.4 | +43.6% | -10.64 to +24.24 | no |
| pod start wait, mean (s) | 2.868 | 4.232 | +47.6% | -3.031 to +5.759 | no |
| host CPU busy, the real machine under kind (%) | 47 | 46.22 | -1.7% | -1.793 to +0.2316 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 76 | 15.3 |  |
| machine down | omni | 42 | 8.9 | -34 s (-45%) |
| spike | native | 255 | 62.9 |  |
| spike | omni | 241 | 52.5 | -14 s (-5%) |
| runaway pod started | native | 108 | 11.1 |  |
| runaway pod started | omni | 80 | 6.7 | -28 s (-26%) |
| probe blind | native | 65 | 0.5 |  |
| probe blind | omni | 60 | 0.1 | -5 s (-8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*