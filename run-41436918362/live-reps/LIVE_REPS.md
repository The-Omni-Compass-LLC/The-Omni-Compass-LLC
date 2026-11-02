# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.1 | 158.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.1 | 158.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 137.5 | 72.78 | 75.46 |
| response time (ms), 95th percentile | 305.8 | 107.7 | 107.3 |
| response time (ms), 99th percentile | 487.8 | 139.9 | 143.8 |
| time over the response line (% of samples) | 1.696 | 0 | 0.2186 |
| failed requests (%) | 0 | 0 | 0.08688 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | 31.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.16 | 0.13 |
| utilisation (used / allocatable) | 0.03596 | 0.03456 | 0.03508 |
| CPU used (cores), mean | 0.8631 | 0.8293 | 0.8419 |
| Omni's own CPU (cores), mean | 0 | 0.03472 | 0.03591 |
| CPU used with Omni's own (cores), mean | 0.8631 | 0.8641 | 0.8778 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.3 | 812.2 | 796.7 |
| HPA replicas, mean | 8.206 | 8.433 | 9.072 |
| pods started | 5.5 | 3.8 | 10.9 |
| pod start wait, total (s) | 7.5 | 6.2 | 20.1 |
| pod start wait, mean (s) | 1.37 | 1.754 | 1.895 |
| host CPU busy, the real machine under kind (%) | 26.57 | 26.74 | 27.43 |
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
| node-hours | 1.514 | 1.514 | −0.0% | −0.0018 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.1 | −0.2% | −0.6267 to −0.0217 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.1 | −0.2% | −0.6267 to −0.0217 | yes: GAIN |
| response time (ms), mean | 137.5 | 72.78 | −47.1% | −91.4617 to −37.9953 | yes: GAIN |
| response time (ms), 95th percentile | 305.8 | 107.7 | −64.8% | −276.0328 to −120.1772 | yes: GAIN |
| response time (ms), 99th percentile | 487.8 | 139.9 | −71.3% | −486.6852 to −209.1752 | yes: GAIN |
| time over the response line (% of samples) | 1.696 | 0 | −100.0% | −3.1534 to −0.2380 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 | −100.0% | −3.3189 to −0.0811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +16.7073 to +20.0927 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.16 | −62.5% | −0.6149 to +0.0816 | no |
| utilisation (used / allocatable) | 0.03596 | 0.03456 | −3.9% | −0.0023 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8631 | 0.8293 | −3.9% | −0.0558 to −0.0116 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03472 | +0.035 (native is 0) | +0.0297 to +0.0398 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8631 | 0.8641 | +0.1% | −0.0170 to +0.0190 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.3 | 812.2 | +2.8% | +1.5617 to +42.2600 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.206 | 8.433 | +2.8% | −0.1211 to +0.5749 | no |
| pods started | 5.5 | 3.8 | −30.9% | −3.0081 to −0.3919 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 6.2 | −17.3% | −3.7093 to +1.1093 | no |
| pod start wait, mean (s) | 1.37 | 1.754 | +28.1% | +0.1429 to +0.6257 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.57 | 26.74 | +0.6% | −0.3525 to +0.6801 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | 0.0% | raw −0.0086 to +0.0086 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | −0.1% | −1.0095 to +0.6013 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | −0.1% | −1.0095 to +0.6013 | no |
| response time (ms), mean | 137.5 | 75.46 | −45.1% | −88.5761 to −35.5183 | yes: GAIN |
| response time (ms), 95th percentile | 305.8 | 107.3 | −64.9% | −277.0838 to −119.8762 | yes: GAIN |
| response time (ms), 99th percentile | 487.8 | 143.8 | −70.5% | −486.7642 to −201.2426 | yes: GAIN |
| time over the response line (% of samples) | 1.696 | 0.2186 | −87.1% | −2.9175 to −0.0368 | yes: GAIN |
| failed requests (%) | 0 | 0.08688 | +0.087 (native is 0) | +0.0026 to +0.1712 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0.3 | −82.4% | −3.2221 to +0.4221 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.1 | +31.100 (native is 0) | +23.0746 to +39.1254 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.13 | −69.5% | −0.6369 to +0.0436 | no |
| utilisation (used / allocatable) | 0.03596 | 0.03508 | −2.5% | −0.0019 to +0.0001 | no |
| CPU used (cores), mean | 0.8631 | 0.8419 | −2.5% | −0.0445 to +0.0022 | no |
| Omni's own CPU (cores), mean | 0 | 0.03591 | +0.036 (native is 0) | +0.0311 to +0.0408 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8631 | 0.8778 | +1.7% | −0.0049 to +0.0344 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.3 | 796.7 | +0.8% | −18.1644 to +31.0390 | no |
| HPA replicas, mean | 8.206 | 9.072 | +10.6% | +0.8155 to +0.9177 | yes: power given |
| pods started | 5.5 | 10.9 | +98.2% | +4.2715 to +6.5285 | yes: power given |
| pod start wait, total (s) | 7.5 | 20.1 | +168.0% | +10.5159 to +14.6841 | yes: LOSS |
| pod start wait, mean (s) | 1.37 | 1.895 | +38.4% | +0.2380 to +0.8134 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.57 | 27.43 | +3.2% | +0.4143 to +1.2937 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0087 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 158.3 | +0.1% | −0.8045 to +1.0447 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 158.3 | +0.1% | −0.8045 to +1.0447 | no |
| response time (ms), mean | 72.78 | 75.46 | +3.7% | +0.3235 to +5.0391 | yes: LOSS |
| response time (ms), 95th percentile | 107.7 | 107.3 | −0.3% | −1.7592 to +1.0092 | no |
| response time (ms), 99th percentile | 139.9 | 143.8 | +2.8% | −8.7251 to +16.5787 | no |
| time over the response line (% of samples) | 0 | 0.2186 | +0.219 (native is 0) | +0.0986 to +0.3385 | yes: LOSS |
| failed requests (%) | 0 | 0.08688 | +0.087 (native is 0) | +0.0026 to +0.1712 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 31.1 | +69.0% | +4.8638 to +20.5362 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 50 | −50.0% | −107.4893 to +7.4893 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.13 | −18.8% | −0.1687 to +0.1087 | no |
| utilisation (used / allocatable) | 0.03456 | 0.03508 | +1.5% | −0.0000 to +0.0011 | no |
| CPU used (cores), mean | 0.8293 | 0.8419 | +1.5% | −0.0001 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0.03472 | 0.03591 | +3.4% | +0.0006 to +0.0017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8641 | 0.8778 | +1.6% | +0.0007 to +0.0268 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 812.2 | 796.7 | −1.9% | −29.1670 to −1.7801 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.433 | 9.072 | +7.6% | +0.2939 to +0.9855 | yes: power given |
| pods started | 3.8 | 10.9 | +186.8% | +6.0100 to +8.1900 | yes: power given |
| pod start wait, total (s) | 6.2 | 20.1 | +224.2% | +10.8944 to +16.9056 | yes: LOSS |
| pod start wait, mean (s) | 1.754 | 1.895 | +8.1% | −0.1153 to +0.3981 | no |
| host CPU busy, the real machine under kind (%) | 26.74 | 27.43 | +2.6% | +0.3137 to +1.0667 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*