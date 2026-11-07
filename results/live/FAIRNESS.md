# Fairness, a noisy neighbour: native against compass, ten paired repetitions on real Kubernetes

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37262799317, the live controller frozen at rules 1-8 (commit 353903683009; amendment 9, the brake at the idle floor, could not fire in this run: the service was never at its floor). Raw files with their SHA-256 sums: `results/live/raw/run-37262799317/`. Rebuilt with `python3 tools/live_reps.py` on those files.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 171.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 171.9 |
| response time (ms), mean | 514.5 | 437.4 |
| response time (ms), 95th percentile | 2326 | 1975 |
| response time (ms), 99th percentile | 5205 | 5326 |
| time over the response line (% of samples) | 22.71 | 21 |
| failed requests (%) | 3.477 | 3.035 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.355 | 1.208 |
| utilisation (used / allocatable) | 0.09582 | 0.09451 |
| CPU used (cores), mean | 2.3 | 2.268 |
| Omni's own CPU (cores), mean | 0 | 0.01387 |
| CPU used with Omni's own (cores), mean | 2.3 | 2.282 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.4 | 309.2 |
| HPA replicas, mean | 15.14 | 15.09 |
| pods started | 4.7 | 4.1 |
| pod start wait, total (s) | 11.3 | 11.1 |
| pod start wait, mean (s) | 2.18 | 2.122 |
| host CPU busy, the real machine under kind (%) | 66.57 | 66.15 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 263 | 259.8 |
| second app: response time (ms), 99th percentile | 1699 | 1045 |
| second app: time over the response line (% of samples) | 14.04 | 13.76 |
| second app: failed requests (%) | 12.28 | 12.3 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | no |
| node-hours | 1.513 | 1.514 | +0.1% | -0.001286 to +0.00362 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 171.9 | -0.1% | -0.5369 to +0.1619 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 171.9 | -0.1% | -0.5369 to +0.1619 | no |
| response time (ms), mean | 514.5 | 437.4 | -15.0% | -117.7 to -36.47 | yes: GAIN |
| response time (ms), 95th percentile | 2326 | 1975 | -15.1% | -735.1 to +33.07 | no |
| response time (ms), 99th percentile | 5205 | 5326 | +2.3% | -854.2 to +1097 | no |
| time over the response line (% of samples) | 22.71 | 21 | -7.5% | -4.062 to +0.6462 | no |
| failed requests (%) | 3.477 | 3.035 | -12.7% | -1.212 to +0.3279 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.355 | 1.208 | -10.8% | -0.5786 to +0.2852 | no |
| utilisation (used / allocatable) | 0.09582 | 0.09451 | -1.4% | -0.002573 to -4.556e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.3 | 2.268 | -1.4% | -0.06174 to -0.001093 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01387 | +0.0139 (native is 0) | +0.01152 to +0.01622 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.3 | 2.282 | -0.8% | -0.0474 to +0.0123 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.4 | 309.2 | +1.2% | -0.9991 to +8.497 | no |
| HPA replicas, mean | 15.14 | 15.09 | -0.3% | -0.4373 to +0.3388 | no |
| pods started | 4.7 | 4.1 | -12.8% | -1.871 to +0.6707 | no |
| pod start wait, total (s) | 11.3 | 11.1 | -1.8% | -4.942 to +4.542 | no |
| pod start wait, mean (s) | 2.18 | 2.122 | -2.6% | -0.685 to +0.5698 | no |
| host CPU busy, the real machine under kind (%) | 66.57 | 66.15 | -0.6% | -0.9495 to +0.1081 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 263 | 259.8 | -1.2% | -18.88 to +12.53 | no |
| second app: response time (ms), 99th percentile | 1699 | 1045 | -38.5% | -1872 to +563.9 | no |
| second app: time over the response line (% of samples) | 14.04 | 13.76 | -2.0% | -1.094 to +0.545 | no |
| second app: failed requests (%) | 12.28 | 12.3 | +0.2% | -0.4011 to +0.4543 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
