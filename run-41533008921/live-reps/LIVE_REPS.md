# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.518 | 1.51 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 160.2 | 158.4 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 160.2 | 158.4 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 135.3 | 139 | 133.7 | 140.8 |
| response time (ms), 95th percentile | 273.1 | 287 | 271.9 | 278.3 |
| response time (ms), 99th percentile | 384.1 | 392.3 | 369.4 | 407.4 |
| time over the response line (% of samples) | 0.193 | 0.3236 | 0.1668 | 0.4374 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.4 | 7.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.05167 | 0.2617 | 0.545 |
| utilisation (used / allocatable) | 0.03714 | 0.04186 | 0.03788 | 0.04246 |
| CPU used (cores), mean | 0.8913 | 1.005 | 0.9092 | 1.019 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.02879 | 0.04693 |
| CPU used with Omni's own (cores), mean | 0.8913 | 1.005 | 0.938 | 1.066 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.8 | 631.4 | 694.6 | 624.4 |
| HPA replicas, mean | 8.893 | 8.888 | 9.701 | 10.17 |
| pods started | 4.9 | 4.8 | 6.5 | 7.5 |
| pod start wait, total (s) | 6.9 | 7.8 | 11 | 12.2 |
| pod start wait, mean (s) | 1.398 | 1.645 | 1.723 | 1.594 |
| host CPU busy, the real machine under kind (%) | 26.83 | 30.83 | 28.33 | 33.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.511 | −0.5% | −0.0143 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.6 | −0.3% | −1.3392 to +0.2313 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.6 | −0.3% | −1.3392 to +0.2313 | no |
| response time (ms), mean | 139 | 140.8 | +1.3% | −2.7557 to +6.4038 | no |
| response time (ms), 95th percentile | 287 | 278.3 | −3.0% | −22.5851 to +5.1711 | no |
| response time (ms), 99th percentile | 392.3 | 407.4 | +3.9% | −41.1808 to +71.4904 | no |
| time over the response line (% of samples) | 0.3236 | 0.4374 | +35.2% | −0.2483 to +0.4760 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.4 | +7.400 (native is 0) | +3.9911 to +10.8089 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.545 | +954.8% | +0.1599 to +0.8268 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04186 | 0.04246 | +1.4% | −0.0003 to +0.0015 | no |
| CPU used (cores), mean | 1.005 | 1.019 | +1.4% | −0.0071 to +0.0355 | no |
| Omni's own CPU (cores), mean | 0 | 0.04693 | +0.047 (native is 0) | +0.0405 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.005 | 1.066 | +6.1% | +0.0358 to +0.0865 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.4 | 624.4 | −1.1% | −19.2983 to +5.2244 | no |
| HPA replicas, mean | 8.888 | 10.17 | +14.4% | +0.3658 to +2.1979 | yes: power given |
| pods started | 4.8 | 7.5 | +56.3% | +0.7324 to +4.6676 | yes: power given |
| pod start wait, total (s) | 7.8 | 12.2 | +56.4% | +0.3931 to +8.4069 | yes: LOSS |
| pod start wait, mean (s) | 1.645 | 1.594 | −3.1% | −0.2512 to +0.1497 | no |
| host CPU busy, the real machine under kind (%) | 30.83 | 33.11 | +7.4% | +1.5224 to +3.0363 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.518 | +0.4% | −0.0031 to +0.0141 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 160.2 | +1.0% | +0.7040 to +2.4879 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 160.2 | +1.0% | +0.7040 to +2.4879 | yes: power given |
| response time (ms), mean | 135.3 | 139 | +2.7% | +0.4935 to +6.9324 | yes: LOSS |
| response time (ms), 95th percentile | 273.1 | 287 | +5.1% | −3.4859 to +31.1639 | no |
| response time (ms), 99th percentile | 384.1 | 392.3 | +2.1% | −18.8972 to +35.3280 | no |
| time over the response line (% of samples) | 0.193 | 0.3236 | +67.6% | −0.1249 to +0.3860 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.05167 | −73.3% | −0.4231 to +0.1397 | no |
| utilisation (used / allocatable) | 0.03714 | 0.04186 | +12.7% | +0.0040 to +0.0054 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8913 | 1.005 | +12.7% | +0.0966 to +0.1303 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8913 | 1.005 | +12.7% | +0.0966 to +0.1303 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.8 | 631.4 | −10.7% | −84.2504 to −66.5055 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.893 | 8.888 | −0.1% | −0.1367 to +0.1262 | no |
| pods started | 4.9 | 4.8 | −2.0% | −0.8113 to +0.6113 | no |
| pod start wait, total (s) | 6.9 | 7.8 | +13.0% | −0.2898 to +2.0898 | no |
| pod start wait, mean (s) | 1.398 | 1.645 | +17.6% | −0.0204 to +0.5137 | no |
| host CPU busy, the real machine under kind (%) | 26.83 | 30.83 | +14.9% | +3.3823 to +4.6161 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.51 | −0.2% | −0.0093 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | −0.1% | −0.8109 to +0.4556 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | −0.1% | −0.8109 to +0.4556 | no |
| response time (ms), mean | 135.3 | 133.7 | −1.2% | −4.7417 to +1.5968 | no |
| response time (ms), 95th percentile | 273.1 | 271.9 | −0.5% | −20.0099 to +17.5339 | no |
| response time (ms), 99th percentile | 384.1 | 369.4 | −3.8% | −43.0106 to +13.6148 | no |
| time over the response line (% of samples) | 0.193 | 0.1668 | −13.6% | −0.1812 to +0.1287 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.4 | +5.400 (native is 0) | +4.0854 to +6.7146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.2617 | +35.3% | −0.1863 to +0.3230 | no |
| utilisation (used / allocatable) | 0.03714 | 0.03788 | +2.0% | −0.0001 to +0.0016 | no |
| CPU used (cores), mean | 0.8913 | 0.9092 | +2.0% | −0.0017 to +0.0376 | no |
| Omni's own CPU (cores), mean | 0 | 0.02879 | +0.029 (native is 0) | +0.0255 to +0.0321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.938 | +5.2% | +0.0247 to +0.0688 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.8 | 694.6 | −1.7% | −26.2893 to +1.9252 | no |
| HPA replicas, mean | 8.893 | 9.701 | +9.1% | +0.0476 to +1.5681 | yes: power given |
| pods started | 4.9 | 6.5 | +32.7% | −0.0242 to +3.2242 | no |
| pod start wait, total (s) | 6.9 | 11 | +59.4% | +1.6348 to +6.5652 | yes: LOSS |
| pod start wait, mean (s) | 1.398 | 1.723 | +23.2% | +0.1575 to +0.4919 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.83 | 28.33 | +5.6% | +0.8474 to +2.1506 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.51 | −0.6% | −0.0153 to −0.0017 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 158.4 | −1.1% | −2.4274 to −1.1199 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 158.4 | −1.1% | −2.4274 to −1.1199 | yes: GAIN |
| response time (ms), mean | 139 | 133.7 | −3.8% | −8.0846 to −2.4862 | yes: GAIN |
| response time (ms), 95th percentile | 287 | 271.9 | −5.3% | −28.2576 to −1.8964 | yes: GAIN |
| response time (ms), 99th percentile | 392.3 | 369.4 | −5.8% | −45.6007 to −0.2259 | yes: GAIN |
| time over the response line (% of samples) | 0.3236 | 0.1668 | −48.5% | −0.3479 to +0.0343 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.4 | +5.400 (native is 0) | +4.0854 to +6.7146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.2617 | +406.5% | −0.0339 to +0.4539 | no |
| utilisation (used / allocatable) | 0.04186 | 0.03788 | −9.5% | −0.0046 to −0.0034 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.005 | 0.9092 | −9.5% | −0.1094 to −0.0816 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02879 | +0.029 (native is 0) | +0.0255 to +0.0321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.005 | 0.938 | −6.6% | −0.0817 to −0.0517 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.4 | 694.6 | +10.0% | +51.0948 to +75.2969 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 9.701 | +9.1% | +0.0270 to +1.5993 | yes: power given |
| pods started | 4.8 | 6.5 | +35.4% | −0.1790 to +3.5790 | no |
| pod start wait, total (s) | 7.8 | 11 | +41.0% | +0.5707 to +5.8293 | yes: LOSS |
| pod start wait, mean (s) | 1.645 | 1.723 | +4.7% | −0.3056 to +0.4617 | no |
| host CPU busy, the real machine under kind (%) | 30.83 | 28.33 | −8.1% | −2.8428 to −2.1577 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0070 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 159.6 | +0.7% | +0.3488 to +1.7353 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 159.6 | +0.7% | +0.3488 to +1.7353 | yes: power given |
| response time (ms), mean | 135.3 | 140.8 | +4.1% | +1.3641 to +9.7099 | yes: LOSS |
| response time (ms), 95th percentile | 273.1 | 278.3 | +1.9% | −8.9423 to +19.2063 | no |
| response time (ms), 99th percentile | 384.1 | 407.4 | +6.1% | −26.2170 to +72.9574 | no |
| time over the response line (% of samples) | 0.193 | 0.4374 | +126.6% | +0.0271 to +0.4617 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.4 | +7.400 (native is 0) | +3.9911 to +10.8089 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.545 | +181.9% | −0.0626 to +0.7659 | no |
| utilisation (used / allocatable) | 0.03714 | 0.04246 | +14.3% | +0.0041 to +0.0065 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8913 | 1.019 | +14.3% | +0.0981 to +0.1571 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04693 | +0.047 (native is 0) | +0.0405 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 1.066 | +19.6% | +0.1401 to +0.2090 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.8 | 624.4 | −11.7% | −97.4741 to −67.3557 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.893 | 10.17 | +14.4% | +0.3884 to +2.1648 | yes: power given |
| pods started | 4.9 | 7.5 | +53.1% | +0.5434 to +4.6566 | yes: power given |
| pod start wait, total (s) | 6.9 | 12.2 | +76.8% | +1.0341 to +9.5659 | yes: LOSS |
| pod start wait, mean (s) | 1.398 | 1.594 | +14.0% | −0.1435 to +0.5354 | no |
| host CPU busy, the real machine under kind (%) | 26.83 | 33.11 | +23.4% | +5.2569 to +7.3002 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*