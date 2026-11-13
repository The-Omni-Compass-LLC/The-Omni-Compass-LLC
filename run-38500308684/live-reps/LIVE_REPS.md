# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.558 |
| node-hours | 2.518 | 1.912 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 226.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 430.7 | 383.5 |
| response time (ms), 95th percentile | 2602 | 2641 |
| response time (ms), 99th percentile | 4147 | 4019 |
| time over the response line (% of samples) | 14.64 | 14.1 |
| failed requests (%) | 0.01081 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 170.8 | 176.3 |
| utilisation (used / allocatable) | 0.05723 | 0.07392 |
| CPU used (cores), mean | 1.374 | 1.356 |
| Omni's own CPU (cores), mean | 0 | 0.02126 |
| CPU used with Omni's own (cores), mean | 1.374 | 1.378 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.1 | 404.9 |
| HPA replicas, mean | 2.125 | 1.983 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 4.6 | 0 |
| pod start wait, mean (s) | 4.6 | 0 |
| host CPU busy, the real machine under kind (%) | 39.07 | 39.7 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 528.7 | 532.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.815 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.558 | -24.0% | -1.871 to -1.013 | yes: GAIN |
| node-hours | 2.518 | 1.912 | -24.0% | -0.7851 to -0.4251 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | -0.0% | -0.9664 to +0.8452 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 226.3 | -16.7% | -58.94 to -31.9 | yes: GAIN |
| response time (ms), mean | 430.7 | 383.5 | -11.0% | -63.45 to -31 | yes: GAIN |
| response time (ms), 95th percentile | 2602 | 2641 | +1.5% | -71.37 to +149 | no |
| response time (ms), 99th percentile | 4147 | 4019 | -3.1% | -285.6 to +30.52 | no |
| time over the response line (% of samples) | 14.64 | 14.1 | -3.7% | -1.075 to -0.004931 | yes: GAIN |
| failed requests (%) | 0.01081 | 0 | -100.0% | -0.03526 to +0.01364 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 170.8 | 176.3 | +3.2% | -0.3271 to +11.36 | no |
| utilisation (used / allocatable) | 0.05723 | 0.07392 | +29.2% | +0.01268 to +0.0207 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.374 | 1.356 | -1.3% | -0.04426 to +0.009588 | no |
| Omni's own CPU (cores), mean | 0 | 0.02126 | +0.0213 (native is 0) | +0.01637 to +0.02615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.374 | 1.378 | +0.3% | -0.02511 to +0.03296 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.1 | 404.9 | -16.5% | -111.3 to -49.27 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.125 | 1.983 | -6.7% | -0.5197 to +0.2349 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 4.6 | 0 | -100.0% | -15.01 to +5.805 | no |
| pod start wait, mean (s) | 4.6 | 0 | -100.0% | -15.01 to +5.805 | no |
| host CPU busy, the real machine under kind (%) | 39.07 | 39.7 | +1.6% | +0.1443 to +1.111 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 528.7 | 532.6 | +0.7% | -3.606 to +11.41 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.815 | -36.4% | -2.708 to -1.663 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*