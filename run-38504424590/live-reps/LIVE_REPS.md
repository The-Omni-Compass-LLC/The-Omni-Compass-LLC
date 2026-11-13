# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.919 |
| node-hours | 1.494 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 162.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 187.6 | 107 |
| response time (ms), 95th percentile | 425.3 | 178.6 |
| response time (ms), 99th percentile | 1231 | 661.3 |
| time over the response line (% of samples) | 7.713 | 5.011 |
| failed requests (%) | 4.456 | 3.857 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7517 | 0.7817 |
| utilisation (used / allocatable) | 0.06799 | 0.06632 |
| CPU used (cores), mean | 1.608 | 1.57 |
| Omni's own CPU (cores), mean | 0 | 0.01045 |
| CPU used with Omni's own (cores), mean | 1.608 | 1.58 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.6 | 427.4 |
| HPA replicas, mean | 8.554 | 11.88 |
| pods started | 5 | 10 |
| pod start wait, total (s) | 24.9 | 31.7 |
| pod start wait, mean (s) | 4.27 | 3.072 |
| host CPU busy, the real machine under kind (%) | 46.1 | 45.36 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.919 | +0.1% | -0.00126 to +0.01047 | no |
| node-hours | 1.494 | 1.489 | -0.4% | -0.01341 to +0.002914 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.2 | -0.6% | -2.082 to -0.05051 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 162.6 | -0.6% | -2.004 to +0.0594 | no |
| response time (ms), mean | 187.6 | 107 | -43.0% | -104.7 to -56.48 | yes: GAIN |
| response time (ms), 95th percentile | 425.3 | 178.6 | -58.0% | -293.6 to -199.9 | yes: GAIN |
| response time (ms), 99th percentile | 1231 | 661.3 | -46.3% | -988.9 to -151.3 | yes: GAIN |
| time over the response line (% of samples) | 7.713 | 5.011 | -35.0% | -3.778 to -1.626 | yes: GAIN |
| failed requests (%) | 4.456 | 3.857 | -13.4% | -1.186 to -0.01087 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7517 | 0.7817 | +4.0% | -0.5502 to +0.6102 | no |
| utilisation (used / allocatable) | 0.06799 | 0.06632 | -2.5% | -0.003377 to +3.546e-05 | no |
| CPU used (cores), mean | 1.608 | 1.57 | -2.4% | -0.0796 to +0.002462 | no |
| Omni's own CPU (cores), mean | 0 | 0.01045 | +0.0105 (native is 0) | +0.009056 to +0.01184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.608 | 1.58 | -1.7% | -0.06807 to +0.01183 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.6 | 427.4 | +1.1% | -5.391 to +14.96 | no |
| HPA replicas, mean | 8.554 | 11.88 | +38.9% | +2.917 to +3.738 | yes: power given |
| pods started | 5 | 10 | +100.0% | +4.326 to +5.674 | yes: power given |
| pod start wait, total (s) | 24.9 | 31.7 | +27.3% | -11.09 to +24.69 | no |
| pod start wait, mean (s) | 4.27 | 3.072 | -28.0% | -4.228 to +1.834 | no |
| host CPU busy, the real machine under kind (%) | 46.1 | 45.36 | -1.6% | -1.492 to +0.007155 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 69 | 14.6 |  |
| machine down | omni | 40 | 8.5 | -29 s (-42%) |
| spike | native | 246 | 59.2 |  |
| spike | omni | 217 | 50.2 | -29 s (-12%) |
| runaway pod started | native | 97 | 9.6 |  |
| runaway pod started | omni | 77 | 6.8 | -20 s (-20%) |
| probe blind | native | 67 | 0.4 |  |
| probe blind | omni | 60 | 0.0 | -7 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*