# Demand that wanders: up and down one step at a time: native against compass, ten paired repetitions on real Kubernetes

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37262791694, the live controller frozen at rules 1-8 (commit 353903683009; amendment 9, the brake at the idle floor, could not fire in this run: the service was never at its floor). Raw files with their SHA-256 sums: `results/live/raw/run-37262791694/`. Rebuilt with `python3 tools/live_reps.py` on those files.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.881 |
| node-hours | 4.515 | 4.426 |
| energy, parked workers still on at idle power (Wh, declared model) | 506.9 | 505.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 506.9 | 498.6 |
| response time (ms), mean | 243.6 | 130.9 |
| response time (ms), 95th percentile | 637.1 | 263.8 |
| response time (ms), 99th percentile | 2200 | 1279 |
| time over the response line (% of samples) | 12.39 | 6.324 |
| failed requests (%) | 5.214 | 4.614 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.885 | 0.8967 |
| utilisation (used / allocatable) | 0.08658 | 0.08535 |
| CPU used (cores), mean | 2.078 | 2.02 |
| Omni's own CPU (cores), mean | 0 | 0.00784 |
| CPU used with Omni's own (cores), mean | 2.078 | 2.028 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 353 | 358.8 |
| HPA replicas, mean | 9.523 | 9.246 |
| pods started | 5.2 | 5 |
| pod start wait, total (s) | 21.7 | 21.8 |
| pod start wait, mean (s) | 3.624 | 3.606 |
| host CPU busy, the real machine under kind (%) | 58.69 | 57.39 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.881 | -2.0% | -0.2413 to +0.002558 | no |
| node-hours | 4.515 | 4.426 | -2.0% | -0.1801 to +0.0007365 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 506.9 | 505.3 | -0.3% | -1.987 to -1.088 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 506.9 | 498.6 | -1.6% | -15.37 to -1.183 | yes: GAIN |
| response time (ms), mean | 243.6 | 130.9 | -46.3% | -148.5 to -76.86 | yes: GAIN |
| response time (ms), 95th percentile | 637.1 | 263.8 | -58.6% | -502.6 to -244.1 | yes: GAIN |
| response time (ms), 99th percentile | 2200 | 1279 | -41.9% | -1318 to -524.8 | yes: GAIN |
| time over the response line (% of samples) | 12.39 | 6.324 | -48.9% | -8.683 to -3.441 | yes: GAIN |
| failed requests (%) | 5.214 | 4.614 | -11.5% | -1.149 to -0.05216 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.885 | 0.8967 | +1.3% | -0.287 to +0.3104 | no |
| utilisation (used / allocatable) | 0.08658 | 0.08535 | -1.4% | -0.002133 to -0.0003232 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.078 | 2.02 | -2.8% | -0.08078 to -0.03423 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00784 | +0.00784 (native is 0) | +0.006798 to +0.008882 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.078 | 2.028 | -2.4% | -0.07338 to -0.02595 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 353 | 358.8 | +1.7% | +2.171 to +9.563 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.523 | 9.246 | -2.9% | -0.5239 to -0.03085 | yes: GAIN |
| pods started | 5.2 | 5 | -3.8% | -0.9388 to +0.5388 | no |
| pod start wait, total (s) | 21.7 | 21.8 | +0.5% | -8.487 to +8.687 | no |
| pod start wait, mean (s) | 3.624 | 3.606 | -0.5% | -1.183 to +1.146 | no |
| host CPU busy, the real machine under kind (%) | 58.69 | 57.39 | -2.2% | -1.86 to -0.7391 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
