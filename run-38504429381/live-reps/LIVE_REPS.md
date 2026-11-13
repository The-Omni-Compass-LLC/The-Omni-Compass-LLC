# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.265 |
| node-hours | 2.519 | 2.207 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 251.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 572.8 | 505.1 |
| response time (ms), 95th percentile | 3429 | 3352 |
| response time (ms), 99th percentile | 5142 | 5042 |
| time over the response line (% of samples) | 16.31 | 15.87 |
| failed requests (%) | 0.01015 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 195.2 | 197 |
| utilisation (used / allocatable) | 0.06496 | 0.07374 |
| CPU used (cores), mean | 1.559 | 1.549 |
| Omni's own CPU (cores), mean | 0 | 0.02409 |
| CPU used with Omni's own (cores), mean | 1.559 | 1.573 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.6 | 388.6 |
| HPA replicas, mean | 1.956 | 2.097 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 3.4 |
| pod start wait, mean (s) | 0 | 1.7 |
| host CPU busy, the real machine under kind (%) | 44.39 | 45.33 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 609.2 | 614.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.265 | -12.2% | -1.127 to -0.3426 | yes: GAIN |
| node-hours | 2.519 | 2.207 | -12.4% | -0.4778 to -0.146 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.5 | -0.1% | -0.9785 to +0.3546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 251.4 | -8.5% | -35.66 to -11.18 | yes: GAIN |
| response time (ms), mean | 572.8 | 505.1 | -11.8% | -88.4 to -47.11 | yes: GAIN |
| response time (ms), 95th percentile | 3429 | 3352 | -2.2% | -214.4 to +61.11 | no |
| response time (ms), 99th percentile | 5142 | 5042 | -1.9% | -298.4 to +98.34 | no |
| time over the response line (% of samples) | 16.31 | 15.87 | -2.7% | -0.9923 to +0.09916 | no |
| failed requests (%) | 0.01015 | 0 | -100.0% | -0.03312 to +0.01281 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 195.2 | 197 | +0.9% | -4.292 to +7.899 | no |
| utilisation (used / allocatable) | 0.06496 | 0.07374 | +13.5% | +0.003218 to +0.01435 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.559 | 1.549 | -0.7% | -0.03858 to +0.01777 | no |
| Omni's own CPU (cores), mean | 0 | 0.02409 | +0.0241 (native is 0) | +0.01997 to +0.02821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.559 | 1.573 | +0.9% | -0.01682 to +0.04418 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.6 | 388.6 | -8.3% | -62.6 to -7.346 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.956 | 2.097 | +7.2% | -0.1681 to +0.4501 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 3.4 | +3.4 (native is 0) | -4.291 to +11.09 | no |
| pod start wait, mean (s) | 0 | 1.7 | +1.7 (native is 0) | -2.145 to +5.545 | no |
| host CPU busy, the real machine under kind (%) | 44.39 | 45.33 | +2.1% | +0.4158 to +1.471 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 609.2 | 614.8 | +0.9% | -0.7192 to +11.92 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 | -20.2% | -1.799 to -0.6303 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*