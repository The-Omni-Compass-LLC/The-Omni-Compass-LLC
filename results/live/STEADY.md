# Steady same work: the load in steps, fixed rate: native against compass, ten paired repetitions on real Kubernetes

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37262793752, the live controller frozen at rules 1-8 (commit 353903683009; amendment 9, the brake at the idle floor, could not fire in this run: the service was never at its floor). Raw files with their SHA-256 sums: `results/live/raw/run-37262793752/`. Rebuilt with `python3 tools/live_reps.py` on those files.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.887 |
| node-hours | 1.518 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 157 |
| response time (ms), mean | 143.8 | 76.55 |
| response time (ms), 95th percentile | 326.3 | 116.9 |
| response time (ms), 99th percentile | 516.7 | 168.5 |
| time over the response line (% of samples) | 1.915 | 0.01212 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2617 | 0.48 |
| utilisation (used / allocatable) | 0.03756 | 0.03649 |
| CPU used (cores), mean | 0.9015 | 0.8596 |
| Omni's own CPU (cores), mean | 0 | 0.00974 |
| CPU used with Omni's own (cores), mean | 0.9015 | 0.8693 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.2 | 756 |
| HPA replicas, mean | 8.538 | 8.107 |
| pods started | 4.5 | 3.9 |
| pod start wait, total (s) | 14 | 17.4 |
| pod start wait, mean (s) | 2.76 | 3.634 |
| host CPU busy, the real machine under kind (%) | 27.11 | 26.6 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.887 | -1.9% | -0.164 to -0.06174 | yes: GAIN |
| node-hours | 1.518 | 1.491 | -1.8% | -0.0396 to -0.0144 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | -0.1% | -0.6873 to +0.2697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 157 | -1.5% | -3.394 to -1.323 | yes: GAIN |
| response time (ms), mean | 143.8 | 76.55 | -46.8% | -92.07 to -42.51 | yes: GAIN |
| response time (ms), 95th percentile | 326.3 | 116.9 | -64.2% | -281.8 to -137 | yes: GAIN |
| response time (ms), 99th percentile | 516.7 | 168.5 | -67.4% | -464.4 to -232.1 | yes: GAIN |
| time over the response line (% of samples) | 1.915 | 0.01212 | -99.4% | -3.046 to -0.7601 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2617 | 0.48 | +83.4% | +0.06686 to +0.3698 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03756 | 0.03649 | -2.9% | -0.002601 to +0.0004555 | no |
| CPU used (cores), mean | 0.9015 | 0.8596 | -4.6% | -0.08053 to -0.003236 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00974 | +0.00974 (native is 0) | +0.008207 to +0.01127 | yes: power given |
| CPU used with Omni's own (cores), mean | 0.9015 | 0.8693 | -3.6% | -0.06947 to +0.005187 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.2 | 756 | +0.6% | -29.28 to +38.84 | no |
| HPA replicas, mean | 8.538 | 8.107 | -5.1% | -0.9537 to +0.09078 | no |
| pods started | 4.5 | 3.9 | -13.3% | -2.039 to +0.8385 | no |
| pod start wait, total (s) | 14 | 17.4 | +24.3% | -3.755 to +10.55 | no |
| pod start wait, mean (s) | 2.76 | 3.634 | +31.7% | -0.827 to +2.575 | no |
| host CPU busy, the real machine under kind (%) | 27.11 | 26.6 | -1.9% | -1.379 to +0.3596 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
