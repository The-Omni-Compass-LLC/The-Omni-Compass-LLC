# Faults: machine down, spike, runaway pod, blind probe: native against compass, ten paired repetitions on real Kubernetes

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37262797634, the live controller frozen at rules 1-8 (commit 353903683009; amendment 9, the brake at the idle floor, could not fire in this run: the service was never at its floor). Raw files with their SHA-256 sums: `results/live/raw/run-37262797634/`. Rebuilt with `python3 tools/live_reps.py` on those files.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.901 |
| node-hours | 1.494 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.2 | 166.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.6 | 164.2 |
| response time (ms), mean | 212.1 | 139 |
| response time (ms), 95th percentile | 367.6 | 146.8 |
| response time (ms), 99th percentile | 1361 | 1155 |
| time over the response line (% of samples) | 8.001 | 6.195 |
| failed requests (%) | 5.352 | 4.815 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7017 | 0.165 |
| utilisation (used / allocatable) | 0.07249 | 0.07105 |
| CPU used (cores), mean | 1.715 | 1.678 |
| Omni's own CPU (cores), mean | 0 | 0.00975 |
| CPU used with Omni's own (cores), mean | 1.715 | 1.688 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.6 | 394 |
| HPA replicas, mean | 8.873 | 9.107 |
| pods started | 4.3 | 3.1 |
| pod start wait, total (s) | 22 | 7.4 |
| pod start wait, mean (s) | 4.554 | 1.692 |
| host CPU busy, the real machine under kind (%) | 48.97 | 48.47 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.901 | -0.2% | -0.03653 to +0.008426 | no |
| node-hours | 1.494 | 1.493 | -0.1% | -0.01325 to +0.01013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.2 | 166.1 | -0.1% | -1.088 to +0.8808 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.6 | 164.2 | -0.2% | -1.522 to +0.7814 | no |
| response time (ms), mean | 212.1 | 139 | -34.5% | -131.9 to -14.23 | yes: GAIN |
| response time (ms), 95th percentile | 367.6 | 146.8 | -60.1% | -294.6 to -146.9 | yes: GAIN |
| response time (ms), 99th percentile | 1361 | 1155 | -15.1% | -971.8 to +560.1 | no |
| time over the response line (% of samples) | 8.001 | 6.195 | -22.6% | -3.147 to -0.4666 | yes: GAIN |
| failed requests (%) | 5.352 | 4.815 | -10.0% | -1.216 to +0.143 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7017 | 0.165 | -76.5% | -1.021 to -0.05228 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.07249 | 0.07105 | -2.0% | -0.003503 to +0.0006243 | no |
| CPU used (cores), mean | 1.715 | 1.678 | -2.2% | -0.0862 to +0.01172 | no |
| Omni's own CPU (cores), mean | 0 | 0.00975 | +0.00975 (native is 0) | +0.008975 to +0.01053 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.715 | 1.688 | -1.6% | -0.07635 to +0.02138 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.6 | 394 | +1.6% | -1.974 to +14.61 | no |
| HPA replicas, mean | 8.873 | 9.107 | +2.6% | -0.05157 to +0.5198 | no |
| pods started | 4.3 | 3.1 | -27.9% | -2.54 to +0.1403 | no |
| pod start wait, total (s) | 22 | 7.4 | -66.4% | -34.07 to +4.871 | no |
| pod start wait, mean (s) | 4.554 | 1.692 | -62.9% | -6.589 to +0.8642 | no |
| host CPU busy, the real machine under kind (%) | 48.97 | 48.47 | -1.0% | -1.503 to +0.4991 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; the aim is lower in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 70 | 14.6 |  |
| machine down | omni | 42 | 9.9 | -28 s (-40%) |
| spike | native | 267 | 67.7 |  |
| spike | omni | 266 | 65.4 | -1 s (-0%) |
| runaway pod started | native | 105 | 10.6 |  |
| runaway pod started | omni | 98 | 8.8 | -7 s (-6%) |
| probe blind | native | 66 | 0.4 |  |
| probe blind | omni | 54 | 0.1 | -12 s (-18%) |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
