# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.018 | 1.018 |
| energy, parked workers still on at idle power (Wh, declared model) | 110.8 | 110.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 110.8 | 110.7 |
| response time (ms), mean | 122.6 | 73.56 |
| response time (ms), 95th percentile | 330.3 | 175.4 |
| response time (ms), 99th percentile | 652 | 365.2 |
| time over the response line (% of samples) | 2.056 | 0.5357 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.2667 |
| utilisation (used / allocatable) | 0.0639 | 0.06264 |
| CPU used (cores), mean | 1.534 | 1.503 |
| Omni's own CPU (cores), mean | 0 | 0.0151 |
| CPU used with Omni's own (cores), mean | 1.534 | 1.519 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.8 | 433.7 |
| HPA replicas, mean | 8.804 | 8.959 |
| pods started | 7 | 7 |
| pod start wait, total (s) | 37 | 34 |
| pod start wait, mean (s) | 5.286 | 4.857 |
| host CPU busy, the real machine under kind (%) | 44.7 | 45.05 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 0 | 0 |
| robust: time over the line in the 120 s after the kill (% of samples) | 4.808 | 2.857 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| node-hours | 1.018 | 1.018 | +0.0% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 110.8 | 110.7 | -0.2% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 110.8 | 110.7 | -0.2% | +nan to +nan | no |
| response time (ms), mean | 122.6 | 73.56 | -40.0% | +nan to +nan | no |
| response time (ms), 95th percentile | 330.3 | 175.4 | -46.9% | +nan to +nan | no |
| response time (ms), 99th percentile | 652 | 365.2 | -44.0% | +nan to +nan | no |
| time over the response line (% of samples) | 2.056 | 0.5357 | -73.9% | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.2667 | -50.0% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.0639 | 0.06264 | -2.0% | +nan to +nan | no |
| CPU used (cores), mean | 1.534 | 1.503 | -2.0% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0151 | +0.0151 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 1.534 | 1.519 | -1.0% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.8 | 433.7 | +1.9% | +nan to +nan | no |
| HPA replicas, mean | 8.804 | 8.959 | +1.8% | +nan to +nan | no |
| pods started | 7 | 7 | +0.0% | +nan to +nan | no |
| pod start wait, total (s) | 37 | 34 | -8.1% | +nan to +nan | no |
| pod start wait, mean (s) | 5.286 | 4.857 | -8.1% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 44.7 | 45.05 | +0.8% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |
| robust: failed requests in the 120 s after the kill (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 4.808 | 2.857 | -40.6% | +nan to +nan | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | kill | 7 | yes | yes | 1 | 0.000 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*