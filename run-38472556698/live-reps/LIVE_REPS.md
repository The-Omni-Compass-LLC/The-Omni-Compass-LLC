# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 156.5 | 81.5 |
| response time (ms), 95th percentile | 347 | 121.9 |
| response time (ms), 99th percentile | 545.1 | 171.9 |
| time over the response line (% of samples) | 2.109 | 0.02424 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.2117 |
| utilisation (used / allocatable) | 0.03959 | 0.03783 |
| CPU used (cores), mean | 0.9501 | 0.9079 |
| Omni's own CPU (cores), mean | 0 | 0.00817 |
| CPU used with Omni's own (cores), mean | 0.9501 | 0.9161 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 700.3 | 720.2 |
| HPA replicas, mean | 8.834 | 8.31 |
| pods started | 4 | 3.3 |
| pod start wait, total (s) | 11.8 | 10.2 |
| pod start wait, mean (s) | 2.58 | 2.576 |
| host CPU busy, the real machine under kind (%) | 28.45 | 27.75 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.288e-16 to +1.062e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.519 | +0.3% | -0.001653 to +0.009987 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.4 | +0.0% | -0.5919 to +0.6879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.4 | +0.0% | -0.5919 to +0.6879 | no |
| response time (ms), mean | 156.5 | 81.5 | -47.9% | -97.21 to -52.83 | yes: GAIN |
| response time (ms), 95th percentile | 347 | 121.9 | -64.9% | -284.1 to -166 | yes: GAIN |
| response time (ms), 99th percentile | 545.1 | 171.9 | -68.5% | -481.7 to -264.7 | yes: GAIN |
| time over the response line (% of samples) | 2.109 | 0.02424 | -98.9% | -3.313 to -0.8564 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.2117 | +0.8% | -0.1541 to +0.1575 | no |
| utilisation (used / allocatable) | 0.03959 | 0.03783 | -4.4% | -0.003033 to -0.000485 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9501 | 0.9079 | -4.4% | -0.07279 to -0.01164 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00817 | +0.00817 (native is 0) | +0.007093 to +0.009247 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9501 | 0.9161 | -3.6% | -0.06384 to -0.004251 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 700.3 | 720.2 | +2.8% | -1.619 to +41.43 | no |
| HPA replicas, mean | 8.834 | 8.31 | -5.9% | -1.029 to -0.01923 | yes: GAIN |
| pods started | 4 | 3.3 | -17.5% | -1.918 to +0.5181 | no |
| pod start wait, total (s) | 11.8 | 10.2 | -13.6% | -7.224 to +4.024 | no |
| pod start wait, mean (s) | 2.58 | 2.576 | -0.1% | -1.136 to +1.128 | no |
| host CPU busy, the real machine under kind (%) | 28.45 | 27.75 | -2.5% | -1.471 to +0.06923 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*