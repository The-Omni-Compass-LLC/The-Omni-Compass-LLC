# The batch test: a queue of jobs, cruise and the emergency brake, native against compass, ten paired repetitions

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GitHub Actions run 37344765837, the live controller at rules 1-8 with amendments 9 (idle read from the autoscaler's floor) and 12 (cruise steps back). 240 jobs of real CPU work, 60 at a time, the service's load generator at zero. Raw files with their SHA-256 sums: `results/live/raw/run-37344765837/`. Rebuilt with `python3 tools/live_reps.py`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.761 |
| node-hours | 2.514 | 1.994 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 234.2 |
| response time (ms), mean | 487.6 | 430.4 |
| response time (ms), 95th percentile | 2889 | 2806 |
| response time (ms), 99th percentile | 4464 | 4403 |
| time over the response line (% of samples) | 15.42 | 15.2 |
| failed requests (%) | 0.3096 | 0.2357 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 183.9 | 190.6 |
| utilisation (used / allocatable) | 0.0618 | 0.07738 |
| CPU used (cores), mean | 1.483 | 1.48 |
| Omni's own CPU (cores), mean | 0 | 0.01947 |
| CPU used with Omni's own (cores), mean | 1.483 | 1.5 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.5 | 382.6 |
| HPA replicas, mean | 1.984 | 2.371 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 4.5 | 0 |
| pod start wait, mean (s) | 4.5 | 0 |
| host CPU busy, the real machine under kind (%) | 42.3 | 43.22 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 575.3 | 581.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.055 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.761 | -20.7% | -1.727 to -0.7507 | yes: GAIN |
| node-hours | 2.514 | 1.994 | -20.7% | -0.7245 to -0.3143 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | -0.1% | -0.9578 to +0.6391 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 234.2 | -14.3% | -54.7 to -23.39 | yes: GAIN |
| response time (ms), mean | 487.6 | 430.4 | -11.7% | -81.62 to -32.68 | yes: GAIN |
| response time (ms), 95th percentile | 2889 | 2806 | -2.9% | -216.3 to +51.08 | no |
| response time (ms), 99th percentile | 4464 | 4403 | -1.4% | -322.4 to +201.7 | no |
| time over the response line (% of samples) | 15.42 | 15.2 | -1.5% | -0.7207 to +0.2729 | no |
| failed requests (%) | 0.3096 | 0.2357 | -23.9% | -0.1643 to +0.01647 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 183.9 | 190.6 | +3.7% | -0.2411 to +13.75 | no |
| utilisation (used / allocatable) | 0.0618 | 0.07738 | +25.2% | +0.01067 to +0.0205 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.483 | 1.48 | -0.2% | -0.04514 to +0.03962 | no |
| Omni's own CPU (cores), mean | 0 | 0.01947 | +0.0195 (native is 0) | +0.01539 to +0.02355 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.483 | 1.5 | +1.1% | -0.02802 to +0.06144 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.5 | 382.6 | -14.9% | -95.69 to -38.05 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.371 | +19.5% | +0.09777 to +0.6749 | yes: power given |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 4.5 | 0 | -100.0% | -14.68 to +5.679 | no |
| pod start wait, mean (s) | 4.5 | 0 | -100.0% | -14.68 to +5.679 | no |
| host CPU busy, the real machine under kind (%) | 42.3 | 43.22 | +2.2% | -0.03451 to +1.872 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 575.3 | 581.9 | +1.1% | -6.391 to +19.59 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.055 | -32.4% | -2.572 to -1.319 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
