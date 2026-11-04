# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.511 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 164.4 | 84.64 | 87.56 |
| response time (ms), 95th percentile | 366.3 | 124.6 | 125.1 |
| response time (ms), 99th percentile | 593.8 | 172.2 | 165.9 |
| time over the response line (% of samples) | 2.345 | 0.03629 | 0.2924 |
| failed requests (%) | 0 | 0 | 0.09938 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.9 | 24.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.2933 | 0.02667 |
| utilisation (used / allocatable) | 0.04042 | 0.03901 | 0.03992 |
| CPU used (cores), mean | 0.97 | 0.9362 | 0.958 |
| Omni's own CPU (cores), mean | 0 | 0.03818 | 0.0388 |
| CPU used with Omni's own (cores), mean | 0.97 | 0.9743 | 0.9968 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 674 | 692.8 | 681 |
| HPA replicas, mean | 8.892 | 9.281 | 9.549 |
| pods started | 4.7 | 4.4 | 9.7 |
| pod start wait, total (s) | 6.6 | 6 | 17.6 |
| pod start wait, mean (s) | 1.422 | 1.364 | 1.827 |
| host CPU busy, the real machine under kind (%) | 29.73 | 30.1 | 30.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0073 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | −0.3% | −1.0018 to +0.0275 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | −0.3% | −1.0018 to +0.0275 | no |
| response time (ms), mean | 164.4 | 84.64 | −48.5% | −98.9753 to −60.6314 | yes: GAIN |
| response time (ms), 95th percentile | 366.3 | 124.6 | −66.0% | −295.9123 to −187.4107 | yes: GAIN |
| response time (ms), 99th percentile | 593.8 | 172.2 | −71.0% | −520.1672 to −322.9346 | yes: GAIN |
| time over the response line (% of samples) | 2.345 | 0.03629 | −98.5% | −3.5311 to −1.0870 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.6226 to −0.7774 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.9 | +20.900 (native is 0) | +19.6633 to +22.1367 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.2933 | −31.8% | −0.5980 to +0.3247 | no |
| utilisation (used / allocatable) | 0.04042 | 0.03901 | −3.5% | −0.0022 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.97 | 0.9362 | −3.5% | −0.0525 to −0.0153 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03818 | +0.038 (native is 0) | +0.0337 to +0.0427 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.97 | 0.9743 | +0.4% | −0.0109 to +0.0195 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 674 | 692.8 | +2.8% | +9.1243 to +28.5617 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.892 | 9.281 | +4.4% | −0.0048 to +0.7818 | no |
| pods started | 4.7 | 4.4 | −6.4% | −1.3690 to +0.7690 | no |
| pod start wait, total (s) | 6.6 | 6 | −9.1% | −2.8670 to +1.6670 | no |
| pod start wait, mean (s) | 1.422 | 1.364 | −4.1% | −0.4013 to +0.2856 | no |
| host CPU busy, the real machine under kind (%) | 29.73 | 30.1 | +1.3% | +0.1341 to +0.6139 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0076 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.3 | −0.0% | −0.9568 to +0.8190 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.3 | −0.0% | −0.9568 to +0.8190 | no |
| response time (ms), mean | 164.4 | 87.56 | −46.8% | −96.9790 to −56.7937 | yes: GAIN |
| response time (ms), 95th percentile | 366.3 | 125.1 | −65.8% | −296.4575 to −185.9505 | yes: GAIN |
| response time (ms), 99th percentile | 593.8 | 165.9 | −72.1% | −537.7927 to −317.9423 | yes: GAIN |
| time over the response line (% of samples) | 2.345 | 0.2924 | −87.5% | −3.3069 to −0.7989 | yes: GAIN |
| failed requests (%) | 0 | 0.09938 | +0.099 (native is 0) | +0.0176 to +0.1812 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0.4 | −81.8% | −3.4792 to −0.1208 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.5 | +24.500 (native is 0) | +19.4730 to +29.5270 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.02667 | −93.8% | −0.7998 to −0.0068 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04042 | 0.03992 | −1.2% | −0.0010 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.97 | 0.958 | −1.2% | −0.0229 to −0.0011 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0388 | +0.039 (native is 0) | +0.0348 to +0.0428 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.97 | 0.9968 | +2.8% | +0.0166 to +0.0369 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 674 | 681 | +1.0% | +0.4395 to +13.6594 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.892 | 9.549 | +7.4% | +0.4576 to +0.8546 | yes: power given |
| pods started | 4.7 | 9.7 | +106.4% | +3.9337 to +6.0663 | yes: power given |
| pod start wait, total (s) | 6.6 | 17.6 | +166.7% | +7.7307 to +14.2693 | yes: LOSS |
| pod start wait, mean (s) | 1.422 | 1.827 | +28.5% | −0.0011 to +0.8114 | no |
| host CPU busy, the real machine under kind (%) | 29.73 | 30.8 | +3.6% | +0.7739 to +1.3717 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.513 | +0.1% | −0.0044 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.3 | +0.3% | −0.3706 to +1.2072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.3 | +0.3% | −0.3706 to +1.2072 | no |
| response time (ms), mean | 84.64 | 87.56 | +3.4% | −0.2101 to +6.0441 | no |
| response time (ms), 95th percentile | 124.6 | 125.1 | +0.4% | −2.1299 to +3.0449 | no |
| response time (ms), 99th percentile | 172.2 | 165.9 | −3.7% | −28.7112 to +16.0780 | no |
| time over the response line (% of samples) | 0.03629 | 0.2924 | +705.8% | +0.1601 to +0.3522 | yes: LOSS |
| failed requests (%) | 0 | 0.09938 | +0.099 (native is 0) | +0.0176 to +0.1812 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 20.9 | 24.5 | +17.2% | −1.4938 to +8.6938 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 13.33 | −83.3% | −120.8681 to −12.4652 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.02667 | −90.9% | −0.5384 to +0.0050 | no |
| utilisation (used / allocatable) | 0.03901 | 0.03992 | +2.3% | +0.0003 to +0.0015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9362 | 0.958 | +2.3% | +0.0078 to +0.0360 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03818 | 0.0388 | +1.6% | −0.0002 to +0.0015 | no |
| CPU used with Omni's own (cores), mean | 0.9743 | 0.9968 | +2.3% | +0.0088 to +0.0361 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.8 | 681 | −1.7% | −20.4266 to −3.1605 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.281 | 9.549 | +2.9% | −0.1608 to +0.6959 | no |
| pods started | 4.4 | 9.7 | +120.5% | +4.2310 to +6.3690 | yes: power given |
| pod start wait, total (s) | 6 | 17.6 | +193.3% | +8.4153 to +14.7847 | yes: LOSS |
| pod start wait, mean (s) | 1.364 | 1.827 | +33.9% | +0.1936 to +0.7324 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.1 | 30.8 | +2.3% | +0.3605 to +1.0371 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*