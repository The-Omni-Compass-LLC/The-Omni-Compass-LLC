# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 160.5 |
| response time (ms), mean | 118.3 | 74.38 |
| response time (ms), 95th percentile | 244.8 | 115.9 |
| response time (ms), 99th percentile | 350.4 | 144.2 |
| time over the response line (% of samples) | 0.3601 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.39 | 0.3933 |
| utilisation (used / allocatable) | 0.03624 | 0.046 |
| CPU used (cores), mean | 0.8697 | 1.104 |
| Omni's own CPU (cores), mean | 0 | 0.00783 |
| CPU used with Omni's own (cores), mean | 0.8697 | 1.112 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726.7 | 592.5 |
| HPA replicas, mean | 8.825 | 8.873 |
| pods started | 5.3 | 5.3 |
| pod start wait, total (s) | 15.9 | 18.7 |
| pod start wait, mean (s) | 2.92 | 3.412 |
| host CPU busy, the real machine under kind (%) | 25.53 | 32.59 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | same (under one part in a million) |
| node-hours | 1.518 | 1.511 | -0.4% | -0.01436 to +0.00169 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 160.5 | +1.0% | +0.9111 to +2.212 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 160.5 | +1.0% | +0.9111 to +2.212 | yes, worse |
| response time (ms), mean | 118.3 | 74.38 | -37.1% | -60.73 to -27.18 | yes, better |
| response time (ms), 95th percentile | 244.8 | 115.9 | -52.7% | -159.7 to -98.15 | yes, better |
| response time (ms), 99th percentile | 350.4 | 144.2 | -58.9% | -251.3 to -161.1 | yes, better |
| time over the response line (% of samples) | 0.3601 | 0 | -100.0% | -0.6846 to -0.03554 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.39 | 0.3933 | +0.9% | -0.4179 to +0.4245 | no |
| utilisation (used / allocatable) | 0.03624 | 0.046 | +26.9% | +0.006159 to +0.01337 | yes, more |
| CPU used (cores), mean | 0.8697 | 1.104 | +26.9% | +0.1478 to +0.3209 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00783 | +0.00783 (native is 0) | +0.006432 to +0.009228 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8697 | 1.112 | +27.8% | +0.1544 to +0.33 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726.7 | 592.5 | -18.5% | -168.8 to -99.73 | yes, less |
| HPA replicas, mean | 8.825 | 8.873 | +0.5% | -0.3316 to +0.4275 | no |
| pods started | 5.3 | 5.3 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 15.9 | 18.7 | +17.6% | -2.199 to +7.799 | no |
| pod start wait, mean (s) | 2.92 | 3.412 | +16.8% | -0.3649 to +1.348 | no |
| host CPU busy, the real machine under kind (%) | 25.53 | 32.59 | +27.7% | +4.532 to +9.599 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*