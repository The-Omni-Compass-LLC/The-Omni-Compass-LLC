# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.697 | 4.508 |
| node-hours | 2.515 | 2.515 | 1.97 | 1.886 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 | 272.5 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.1 | 231.5 | 224.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 324.3 | 344.7 | 313.9 | 345 |
| response time (ms), 95th percentile | 1121 | 1228 | 1251 | 1399 |
| response time (ms), 99th percentile | 1633 | 1723 | 1782 | 2056 |
| time over the response line (% of samples) | 13.26 | 15.43 | 15.14 | 16.33 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.5 | 8.5 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 128.9 | 125.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 12.22 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 10.73 | 11.01 | 12.67 |
| utilisation (used / allocatable) | 0.05852 | 0.05893 | 0.07703 | 0.07755 |
| CPU used (cores), mean | 1.404 | 1.414 | 1.413 | 1.393 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0723 | 0.07573 |
| CPU used with Omni's own (cores), mean | 1.404 | 1.414 | 1.486 | 1.469 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 473.9 | 394.5 | 392.9 |
| HPA replicas, mean | 2.025 | 2.014 | 2.206 | 2.291 |
| pods started | 0.4 | 0.1 | 1 | 1.1 |
| pod start wait, total (s) | 0.9 | 0.5 | 2.4 | 2.9 |
| pod start wait, mean (s) | 0.45 | 0.5 | 1 | 1.15 |
| host CPU busy, the real machine under kind (%) | 40.13 | 41.55 | 43.92 | 44.78 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.6 | 786.9 | 787.7 | 798.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.852 | 3.465 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2333 | 0.1292 | 0.6167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.1 | 0.4 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 81.04 | 90.55 | 91.89 | 102.6 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 4.508 | −24.9% | −2.2556 to −0.7283 | yes: GAIN |
| node-hours | 2.515 | 1.886 | −25.0% | −0.9480 to −0.3091 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.4 | −0.3% | −1.9983 to +0.5614 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 224.6 | −17.5% | −72.0504 to −22.9157 | yes: GAIN |
| response time (ms), mean | 344.7 | 345 | +0.1% | −27.1333 to +27.6321 | no |
| response time (ms), 95th percentile | 1228 | 1399 | +14.0% | +21.0174 to +321.7556 | yes: LOSS |
| response time (ms), 99th percentile | 1723 | 2056 | +19.3% | +30.5106 to +636.1914 | yes: LOSS |
| time over the response line (% of samples) | 15.43 | 16.33 | +5.8% | −0.5696 to +2.3635 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 9.1 | +7.1% | +0.0999 to +1.1001 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.1 | +125.100 (native is 0) | +57.8227 to +192.3773 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 12.67 | +18.1% | +0.0146 to +3.8721 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05893 | 0.07755 | +31.6% | +0.0099 to +0.0273 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.393 | −1.5% | −0.0740 to +0.0313 | no |
| Omni's own CPU (cores), mean | 0 | 0.07573 | +0.076 (native is 0) | +0.0683 to +0.0831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.469 | +3.8% | −0.0036 to +0.1124 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.9 | 392.9 | −17.1% | −122.4390 to −39.6465 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.291 | +13.7% | −0.0024 to +0.5556 | no |
| pods started | 0.1 | 1.1 | +1000.0% | +0.1079 to +1.8921 | yes: power given |
| pod start wait, total (s) | 0.5 | 2.9 | +480.0% | −0.1725 to +4.9725 | no |
| pod start wait, mean (s) | 0.5 | 1.15 | +130.0% | −0.1417 to +1.4417 | no |
| host CPU busy, the real machine under kind (%) | 41.55 | 44.78 | +7.8% | +2.5540 to +3.9069 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.9 | 798.7 | +1.5% | +0.0763 to +23.5237 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.465 | −42.2% | −3.4565 to −1.6129 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.6167 | +164.3% | −0.1608 to +0.9274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 2.5 | +127.3% | −1.5435 to +4.3435 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.55 | 102.6 | +13.3% | +0.4912 to +23.6088 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | −0.0% | −0.0096 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 | +0.1% | −1.1148 to +1.4264 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.1 | +0.1% | −1.1148 to +1.4264 | no |
| response time (ms), mean | 324.3 | 344.7 | +6.3% | −12.0177 to +52.9224 | no |
| response time (ms), 95th percentile | 1121 | 1228 | +9.5% | −47.2169 to +260.1729 | no |
| response time (ms), 99th percentile | 1633 | 1723 | +5.5% | −147.9281 to +327.6811 | no |
| time over the response line (% of samples) | 13.26 | 15.43 | +16.3% | −2.2795 to +6.6109 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.5 | +10.4% | −0.7744 to +2.3744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 10.73 | +2.6% | −1.2576 to +1.8009 | no |
| utilisation (used / allocatable) | 0.05852 | 0.05893 | +0.7% | −0.0020 to +0.0029 | no |
| CPU used (cores), mean | 1.404 | 1.414 | +0.7% | −0.0490 to +0.0689 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.404 | 1.414 | +0.7% | −0.0490 to +0.0689 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 473.9 | −0.5% | −26.1220 to +21.7105 | no |
| HPA replicas, mean | 2.025 | 2.014 | −0.5% | −0.1165 to +0.0954 | no |
| pods started | 0.4 | 0.1 | −75.0% | −0.9786 to +0.3786 | no |
| pod start wait, total (s) | 0.9 | 0.5 | −44.4% | −2.3720 to +1.5720 | no |
| pod start wait, mean (s) | 0.45 | 0.5 | +11.1% | −1.3851 to +1.4851 | no |
| host CPU busy, the real machine under kind (%) | 40.13 | 41.55 | +3.6% | +0.0597 to +2.7910 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 786.9 | +1.3% | −0.8482 to +21.4482 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2333 | +124.0% | +0.0344 to +0.2239 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.1 | +37.5% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.04 | 90.55 | +11.7% | −0.8023 to +19.8273 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.697 | −21.7% | −2.1623 to −0.4432 | yes: GAIN |
| node-hours | 2.515 | 1.97 | −21.7% | −0.9079 to −0.1826 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.5 | +0.2% | −0.0462 to +1.2602 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 231.5 | −14.9% | −67.7399 to −13.0628 | yes: GAIN |
| response time (ms), mean | 324.3 | 313.9 | −3.2% | −44.8621 to +24.0153 | no |
| response time (ms), 95th percentile | 1121 | 1251 | +11.6% | −13.5976 to +273.3846 | no |
| response time (ms), 99th percentile | 1633 | 1782 | +9.1% | −123.8110 to +420.9648 | no |
| time over the response line (% of samples) | 13.26 | 15.14 | +14.2% | −2.4443 to +6.1999 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.5 | +10.4% | −0.8792 to +2.4792 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.9 | +128.900 (native is 0) | +55.0631 to +202.7369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 11.01 | +5.3% | −1.3104 to +2.4237 | no |
| utilisation (used / allocatable) | 0.05852 | 0.07703 | +31.6% | +0.0064 to +0.0306 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.404 | 1.413 | +0.6% | −0.0531 to +0.0711 | no |
| Omni's own CPU (cores), mean | 0 | 0.0723 | +0.072 (native is 0) | +0.0655 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.486 | +5.8% | +0.0166 to +0.1460 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 394.5 | −17.1% | −137.9023 to −25.2914 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.206 | +9.0% | −0.0776 to +0.4404 | no |
| pods started | 0.4 | 1 | +150.0% | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0.9 | 2.4 | +166.7% | −1.0290 to +4.0290 | no |
| pod start wait, mean (s) | 0.45 | 1 | +122.2% | −0.2124 to +1.3124 | no |
| host CPU busy, the real machine under kind (%) | 40.13 | 43.92 | +9.4% | +2.3865 to +5.1904 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 787.7 | +1.4% | −0.7762 to +22.9762 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.852 | −35.8% | −3.3400 to −0.9568 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1292 | +24.0% | −0.0220 to +0.0720 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.4 | −50.0% | −1.6707 to +0.8707 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.04 | 91.89 | +13.4% | +0.2914 to +21.4086 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.697 | −21.7% | −2.1623 to −0.4432 | yes: GAIN |
| node-hours | 2.515 | 1.97 | −21.7% | −0.9039 to −0.1857 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.5 | +0.2% | −0.4026 to +1.3050 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 231.5 | −14.9% | −67.4529 to −13.6613 | yes: GAIN |
| response time (ms), mean | 344.7 | 313.9 | −9.0% | −44.3652 to −17.3864 | yes: GAIN |
| response time (ms), 95th percentile | 1228 | 1251 | +1.9% | −34.8080 to +81.6390 | no |
| response time (ms), 99th percentile | 1723 | 1782 | +3.4% | −60.9364 to +178.3372 | no |
| time over the response line (% of samples) | 15.43 | 15.14 | −1.9% | −1.2813 to +0.7056 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.5 | ±0.0% | −0.5840 to +0.5840 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.9 | +128.900 (native is 0) | +55.0631 to +202.7369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 11.01 | +2.7% | −0.9614 to +1.5314 | no |
| utilisation (used / allocatable) | 0.05893 | 0.07703 | +30.7% | +0.0059 to +0.0303 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.413 | −0.1% | −0.0383 to +0.0364 | no |
| Omni's own CPU (cores), mean | 0 | 0.0723 | +0.072 (native is 0) | +0.0655 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.486 | +5.0% | +0.0317 to +0.1110 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.9 | 394.5 | −16.8% | −137.8905 to −20.8917 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.206 | +9.5% | −0.0835 to +0.4674 | no |
| pods started | 0.1 | 1 | +900.0% | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0.5 | 2.4 | +380.0% | −1.0290 to +4.8290 | no |
| pod start wait, mean (s) | 0.5 | 1 | +100.0% | −1.1605 to +2.1605 | no |
| host CPU busy, the real machine under kind (%) | 41.55 | 43.92 | +5.7% | +2.0859 to +2.6404 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.9 | 787.7 | +0.1% | −1.1312 to +2.7312 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.852 | −35.8% | −3.3400 to −0.9568 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.1292 | −44.6% | −0.1827 to −0.0256 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.4 | −63.6% | −1.5953 to +0.1953 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.55 | 91.89 | +1.5% | −0.0831 to +2.7581 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.508 | −24.9% | −2.2556 to −0.7283 | yes: GAIN |
| node-hours | 2.515 | 1.886 | −25.0% | −0.9524 to −0.3057 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 | −0.2% | −2.1870 to +1.0617 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 224.6 | −17.4% | −72.4527 to −22.2018 | yes: GAIN |
| response time (ms), mean | 324.3 | 345 | +6.4% | −34.3143 to +75.7179 | no |
| response time (ms), 95th percentile | 1121 | 1399 | +24.8% | +11.6015 to +544.1275 | yes: LOSS |
| response time (ms), 99th percentile | 1633 | 2056 | +25.9% | −20.6654 to +867.1204 | no |
| time over the response line (% of samples) | 13.26 | 16.33 | +23.1% | −2.6726 to +8.7978 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 9.1 | +18.2% | −0.3586 to +3.1586 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.1 | +125.100 (native is 0) | +57.8227 to +192.3773 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 12.67 | +21.2% | −0.3282 to +4.7582 | no |
| utilisation (used / allocatable) | 0.05852 | 0.07755 | +32.5% | +0.0101 to +0.0280 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.404 | 1.393 | −0.8% | −0.1033 to +0.0805 | no |
| Omni's own CPU (cores), mean | 0 | 0.07573 | +0.076 (native is 0) | +0.0683 to +0.0831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.469 | +4.6% | −0.0312 to +0.1599 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 392.9 | −17.5% | −127.4400 to −39.0570 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.291 | +13.1% | +0.0278 to +0.5042 | yes: power given |
| pods started | 0.4 | 1.1 | +175.0% | −0.5181 to +1.9181 | no |
| pod start wait, total (s) | 0.9 | 2.9 | +222.2% | −1.9755 to +5.9755 | no |
| pod start wait, mean (s) | 0.45 | 1.15 | +155.6% | −0.3283 to +1.7283 | no |
| host CPU busy, the real machine under kind (%) | 40.13 | 44.78 | +11.6% | +3.0172 to +6.2943 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 798.7 | +2.8% | +0.0078 to +44.1922 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.465 | −42.2% | −3.4565 to −1.6129 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.6167 | +492.0% | −0.0644 to +1.0894 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 2.5 | +212.5% | −0.9347 to +4.3347 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.04 | 102.6 | +26.6% | +0.2260 to +42.8990 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*