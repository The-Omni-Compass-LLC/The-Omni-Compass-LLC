# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.511 | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | 158.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | 158.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 145.4 | 76.5 | 79.22 |
| response time (ms), 95th percentile | 314.9 | 109.1 | 109 |
| response time (ms), 99th percentile | 521.9 | 140.6 | 137.4 |
| time over the response line (% of samples) | 1.692 | 0 | 0.2874 |
| failed requests (%) | 0 | 0 | 0.03681 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | 27.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.2933 | 0.1017 |
| utilisation (used / allocatable) | 0.03747 | 0.03627 | 0.03674 |
| CPU used (cores), mean | 0.8993 | 0.8705 | 0.8818 |
| Omni's own CPU (cores), mean | 0 | 0.03549 | 0.03639 |
| CPU used with Omni's own (cores), mean | 0.8993 | 0.906 | 0.9182 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.5 | 747 | 735.2 |
| HPA replicas, mean | 8.501 | 8.822 | 9.376 |
| pods started | 5.5 | 4.1 | 10.2 |
| pod start wait, total (s) | 8.8 | 7.1 | 16.7 |
| pod start wait, mean (s) | 1.593 | 1.79 | 1.665 |
| host CPU busy, the real machine under kind (%) | 27.76 | 28.09 | 28.66 |
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
| node-hours | 1.511 | 1.513 | +0.1% | −0.0000 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | −0.1% | −0.4171 to +0.1202 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | −0.1% | −0.4171 to +0.1202 | no |
| response time (ms), mean | 145.4 | 76.5 | −47.4% | −88.7895 to −49.1065 | yes: GAIN |
| response time (ms), 95th percentile | 314.9 | 109.1 | −65.4% | −262.4970 to −149.1270 | yes: GAIN |
| response time (ms), 99th percentile | 521.9 | 140.6 | −73.1% | −502.1507 to −260.4209 | yes: GAIN |
| time over the response line (% of samples) | 1.692 | 0 | −100.0% | −2.9948 to −0.3885 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +17.1293 to +19.6707 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.2933 | +179.4% | +0.0083 to +0.3684 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03747 | 0.03627 | −3.2% | −0.0020 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8993 | 0.8705 | −3.2% | −0.0474 to −0.0102 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03549 | +0.035 (native is 0) | +0.0313 to +0.0397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8993 | 0.906 | +0.7% | −0.0082 to +0.0216 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.5 | 747 | +2.4% | +8.9702 to +26.0267 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.501 | 8.822 | +3.8% | −0.0321 to +0.6728 | no |
| pods started | 5.5 | 4.1 | −25.5% | −2.7985 to −0.0015 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 7.1 | −19.3% | −4.9176 to +1.5176 | no |
| pod start wait, mean (s) | 1.593 | 1.79 | +12.3% | −0.2472 to +0.6405 | no |
| host CPU busy, the real machine under kind (%) | 27.76 | 28.09 | +1.2% | +0.0137 to +0.6403 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.515 | +0.2% | −0.0025 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.7 | +0.1% | −0.3905 to +0.6743 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.7 | +0.1% | −0.3905 to +0.6743 | no |
| response time (ms), mean | 145.4 | 79.22 | −45.5% | −86.8447 to −45.6119 | yes: GAIN |
| response time (ms), 95th percentile | 314.9 | 109 | −65.4% | −263.1313 to −148.5567 | yes: GAIN |
| response time (ms), 99th percentile | 521.9 | 137.4 | −73.7% | −508.8938 to −260.1346 | yes: GAIN |
| time over the response line (% of samples) | 1.692 | 0.2874 | −83.0% | −2.7641 to −0.0445 | yes: GAIN |
| failed requests (%) | 0 | 0.03681 | +0.037 (native is 0) | −0.0056 to +0.0792 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0.5 | −68.8% | −2.8986 to +0.6986 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.2 | +27.200 (native is 0) | +21.2553 to +33.1447 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.1017 | −3.2% | −0.1776 to +0.1710 | no |
| utilisation (used / allocatable) | 0.03747 | 0.03674 | −1.9% | −0.0015 to +0.0001 | no |
| CPU used (cores), mean | 0.8993 | 0.8818 | −1.9% | −0.0368 to +0.0018 | no |
| Omni's own CPU (cores), mean | 0 | 0.03639 | +0.036 (native is 0) | +0.0326 to +0.0401 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8993 | 0.9182 | +2.1% | +0.0021 to +0.0356 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.5 | 735.2 | +0.8% | −14.3044 to +25.7387 | no |
| HPA replicas, mean | 8.501 | 9.376 | +10.3% | +0.6675 to +1.0811 | yes: power given |
| pods started | 5.5 | 10.2 | +85.5% | +3.4361 to +5.9639 | yes: power given |
| pod start wait, total (s) | 8.8 | 16.7 | +89.8% | +5.0497 to +10.7503 | yes: LOSS |
| pod start wait, mean (s) | 1.593 | 1.665 | +4.5% | −0.3297 to +0.4734 | no |
| host CPU busy, the real machine under kind (%) | 27.76 | 28.66 | +3.2% | +0.5279 to +1.2713 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0038 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.7 | +0.2% | −0.2806 to +0.8613 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.7 | +0.2% | −0.2806 to +0.8613 | no |
| response time (ms), mean | 76.5 | 79.22 | +3.6% | +1.2467 to +4.1928 | yes: LOSS |
| response time (ms), 95th percentile | 109.1 | 109 | −0.0% | −1.5067 to +1.4427 | no |
| response time (ms), 99th percentile | 140.6 | 137.4 | −2.3% | −12.7193 to +6.2625 | no |
| time over the response line (% of samples) | 0 | 0.2874 | +0.287 (native is 0) | +0.1666 to +0.4082 | yes: LOSS |
| failed requests (%) | 0 | 0.03681 | +0.037 (native is 0) | −0.0056 to +0.0792 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 27.2 | +47.8% | +2.7229 to +14.8771 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 25 | −75.0% | −113.7064 to −36.2936 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.1017 | −65.3% | −0.4697 to +0.0864 | no |
| utilisation (used / allocatable) | 0.03627 | 0.03674 | +1.3% | +0.0000 to +0.0009 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8705 | 0.8818 | +1.3% | +0.0010 to +0.0216 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03549 | 0.03639 | +2.5% | −0.0000 to +0.0018 | no |
| CPU used with Omni's own (cores), mean | 0.906 | 0.9182 | +1.3% | +0.0014 to +0.0230 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747 | 735.2 | −1.6% | −27.0618 to +3.4991 | no |
| HPA replicas, mean | 8.822 | 9.376 | +6.3% | +0.1637 to +0.9443 | yes: power given |
| pods started | 4.1 | 10.2 | +148.8% | +4.4671 to +7.7329 | yes: power given |
| pod start wait, total (s) | 7.1 | 16.7 | +135.2% | +6.5428 to +12.6572 | yes: LOSS |
| pod start wait, mean (s) | 1.79 | 1.665 | −7.0% | −0.3911 to +0.1415 | no |
| host CPU busy, the real machine under kind (%) | 28.09 | 28.66 | +2.0% | +0.1481 to +0.9971 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*