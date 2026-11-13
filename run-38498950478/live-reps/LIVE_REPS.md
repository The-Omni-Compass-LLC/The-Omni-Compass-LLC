# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 172.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 172.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 547.4 | 425.4 |
| response time (ms), 95th percentile | 2277 | 1966 |
| response time (ms), 99th percentile | 5637 | 4958 |
| time over the response line (% of samples) | 24.96 | 21.21 |
| failed requests (%) | 3.955 | 4.052 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.333 | 1.327 |
| utilisation (used / allocatable) | 0.09861 | 0.0979 |
| CPU used (cores), mean | 2.367 | 2.35 |
| Omni's own CPU (cores), mean | 0 | 0.01098 |
| CPU used with Omni's own (cores), mean | 2.367 | 2.361 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.3 | 300.1 |
| HPA replicas, mean | 15.23 | 15.37 |
| pods started | 4.5 | 3.6 |
| pod start wait, total (s) | 11 | 8.8 |
| pod start wait, mean (s) | 2.231 | 1.926 |
| host CPU busy, the real machine under kind (%) | 68.96 | 68.42 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 286.6 | 277.7 |
| second app: response time (ms), 99th percentile | 1534 | 1367 |
| second app: time over the response line (% of samples) | 14.93 | 14.47 |
| second app: failed requests (%) | 12.97 | 13.34 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.818e-16 to +9.594e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.515 | +0.0% | -0.005315 to +0.006315 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 172.7 | -0.1% | -0.814 to +0.5459 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 172.7 | -0.1% | -0.814 to +0.5459 | no |
| response time (ms), mean | 547.4 | 425.4 | -22.3% | -171.3 to -72.73 | yes: GAIN |
| response time (ms), 95th percentile | 2277 | 1966 | -13.7% | -583.9 to -38.73 | yes: GAIN |
| response time (ms), 99th percentile | 5637 | 4958 | -12.0% | -1904 to +547.2 | no |
| time over the response line (% of samples) | 24.96 | 21.21 | -15.0% | -5.694 to -1.795 | yes: GAIN |
| failed requests (%) | 3.955 | 4.052 | +2.4% | -0.4917 to +0.6851 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.333 | 1.327 | -0.5% | -1.107 to +1.094 | no |
| utilisation (used / allocatable) | 0.09861 | 0.0979 | -0.7% | -0.001325 to -8.064e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.367 | 2.35 | -0.7% | -0.03179 to -0.001935 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01098 | +0.011 (native is 0) | +0.009518 to +0.01244 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.361 | -0.2% | -0.02047 to +0.008707 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.3 | 300.1 | +0.6% | +0.01822 to +3.688 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.23 | 15.37 | +0.9% | -0.1766 to +0.4648 | no |
| pods started | 4.5 | 3.6 | -20.0% | -2.041 to +0.241 | no |
| pod start wait, total (s) | 11 | 8.8 | -20.0% | -5.875 to +1.475 | no |
| pod start wait, mean (s) | 2.231 | 1.926 | -13.7% | -0.854 to +0.2426 | no |
| host CPU busy, the real machine under kind (%) | 68.96 | 68.42 | -0.8% | -1.013 to -0.04935 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 286.6 | 277.7 | -3.1% | -35.09 to +17.15 | no |
| second app: response time (ms), 99th percentile | 1534 | 1367 | -10.9% | -901 to +565.8 | no |
| second app: time over the response line (% of samples) | 14.93 | 14.47 | -3.1% | -0.9654 to +0.0537 | no |
| second app: failed requests (%) | 12.97 | 13.34 | +2.8% | -0.1747 to +0.9066 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*