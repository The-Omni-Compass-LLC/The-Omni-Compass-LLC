# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.916 |
| node-hours | 1.486 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.3 | 162.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.8 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 181.9 | 100.8 |
| response time (ms), 95th percentile | 419 | 181.6 |
| response time (ms), 99th percentile | 1910 | 888.4 |
| time over the response line (% of samples) | 6.316 | 3.762 |
| failed requests (%) | 2.653 | 2.342 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6 | 0.93 |
| utilisation (used / allocatable) | 0.05899 | 0.05847 |
| CPU used (cores), mean | 1.396 | 1.383 |
| Omni's own CPU (cores), mean | 0 | 0.00894 |
| CPU used with Omni's own (cores), mean | 1.396 | 1.392 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 483.5 |
| HPA replicas, mean | 8.178 | 10.89 |
| pods started | 5.4 | 10.5 |
| pod start wait, total (s) | 31.2 | 37.8 |
| pod start wait, mean (s) | 5.022 | 3.468 |
| host CPU busy, the real machine under kind (%) | 40.29 | 40.03 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.917 | 5.916 | -0.0% | -0.009106 to +0.005884 | no |
| node-hours | 1.486 | 1.49 | +0.3% | -0.005663 to +0.01372 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.3 | 162.7 | +0.2% | -0.5344 to +1.292 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.8 | 161.1 | +0.2% | -0.6089 to +1.296 | no |
| response time (ms), mean | 181.9 | 100.8 | -44.6% | -105 to -57.26 | yes: GAIN |
| response time (ms), 95th percentile | 419 | 181.6 | -56.7% | -319.2 to -155.6 | yes: GAIN |
| response time (ms), 99th percentile | 1910 | 888.4 | -53.5% | -1749 to -294.6 | yes: GAIN |
| time over the response line (% of samples) | 6.316 | 3.762 | -40.4% | -3.976 to -1.132 | yes: GAIN |
| failed requests (%) | 2.653 | 2.342 | -11.7% | -0.8893 to +0.2669 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6 | 0.93 | +55.0% | -0.2581 to +0.9181 | no |
| utilisation (used / allocatable) | 0.05899 | 0.05847 | -0.9% | -0.002463 to +0.001412 | no |
| CPU used (cores), mean | 1.396 | 1.383 | -0.9% | -0.05811 to +0.03274 | no |
| Omni's own CPU (cores), mean | 0 | 0.00894 | +0.00894 (native is 0) | +0.007465 to +0.01041 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.396 | 1.392 | -0.3% | -0.04815 to +0.04066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 483.5 | -0.2% | -14.87 to +12.72 | no |
| HPA replicas, mean | 8.178 | 10.89 | +33.2% | +1.913 to +3.517 | yes: power given |
| pods started | 5.4 | 10.5 | +94.4% | +3.333 to +6.867 | yes: power given |
| pod start wait, total (s) | 31.2 | 37.8 | +21.2% | -11.34 to +24.54 | no |
| pod start wait, mean (s) | 5.022 | 3.468 | -30.9% | -4.163 to +1.055 | no |
| host CPU busy, the real machine under kind (%) | 40.29 | 40.03 | -0.7% | -1.058 to +0.531 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 58 | 14.4 |  |
| machine down | omni | 34 | 7.8 | -23 s (-40%) |
| spike | native | 203 | 38.9 |  |
| spike | omni | 163 | 30.5 | -40 s (-20%) |
| runaway pod started | native | 53 | 5.3 |  |
| runaway pod started | omni | 44 | 3.7 | -9 s (-18%) |
| probe blind | native | 62 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -2 s (-3%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*