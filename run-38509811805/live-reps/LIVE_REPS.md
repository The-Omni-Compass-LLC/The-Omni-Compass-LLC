# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.336 |
| energy, parked workers still on at idle power (Wh, declared model) | 481.5 | 479.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.5 | 479.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 275.5 | 137.4 |
| response time (ms), 95th percentile | 714.8 | 277.4 |
| response time (ms), 99th percentile | 1355 | 739.8 |
| time over the response line (% of samples) | 13.52 | 2.969 |
| failed requests (%) | 1.241 | 1.068 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9033 | 1.468 |
| utilisation (used / allocatable) | 0.07898 | 0.07604 |
| CPU used (cores), mean | 1.896 | 1.825 |
| Omni's own CPU (cores), mean | 0 | 0.0094 |
| CPU used with Omni's own (cores), mean | 1.896 | 1.834 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 400 |
| HPA replicas, mean | 9.675 | 11.33 |
| pods started | 5.6 | 15.9 |
| pod start wait, total (s) | 21.3 | 38.5 |
| pod start wait, mean (s) | 3.388 | 2.478 |
| host CPU busy, the real machine under kind (%) | 54.54 | 53.2 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.995e-16 to +8.895e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.336 | +0.1% | -0.004772 to +0.01144 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 481.5 | 479.9 | -0.3% | -2.78 to -0.4379 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.5 | 479.9 | -0.3% | -2.78 to -0.4379 | yes: GAIN |
| response time (ms), mean | 275.5 | 137.4 | -50.1% | -183.3 to -92.9 | yes: GAIN |
| response time (ms), 95th percentile | 714.8 | 277.4 | -61.2% | -564.2 to -310.7 | yes: GAIN |
| response time (ms), 99th percentile | 1355 | 739.8 | -45.4% | -815.7 to -415.2 | yes: GAIN |
| time over the response line (% of samples) | 13.52 | 2.969 | -78.0% | -15.51 to -5.586 | yes: GAIN |
| failed requests (%) | 1.241 | 1.068 | -13.9% | -0.3156 to -0.02977 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9033 | 1.468 | +62.5% | -0.3096 to +1.44 | no |
| utilisation (used / allocatable) | 0.07898 | 0.07604 | -3.7% | -0.003692 to -0.002201 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.896 | 1.825 | -3.7% | -0.08861 to -0.05282 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0094 | +0.0094 (native is 0) | +0.007482 to +0.01132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.896 | 1.834 | -3.2% | -0.07761 to -0.04502 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 400 | +3.3% | +9.863 to +15.86 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.675 | 11.33 | +17.1% | +0.04073 to +3.266 | yes: power given |
| pods started | 5.6 | 15.9 | +183.9% | +6.455 to +14.15 | yes: power given |
| pod start wait, total (s) | 21.3 | 38.5 | +80.8% | +2.038 to +32.36 | yes: LOSS |
| pod start wait, mean (s) | 3.388 | 2.478 | -26.9% | -2.743 to +0.9236 | no |
| host CPU busy, the real machine under kind (%) | 54.54 | 53.2 | -2.5% | -1.625 to -1.062 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*