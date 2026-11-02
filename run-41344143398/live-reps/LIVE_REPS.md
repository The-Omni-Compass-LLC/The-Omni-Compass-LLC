# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.89 | 6.931 |
| node-hours | 5.041 | 5.025 | 4.56 | 2.904 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.2 | 523.8 | 504.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.2 | 489 | 345.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 464.7 | 120 | 423.1 | 69.17 |
| response time (ms), 95th percentile | 1693 | 170 | 1722 | 86.87 |
| response time (ms), 99th percentile | 2315 | 195.8 | 2316 | 113.7 |
| time over the response line (% of samples) | 21.92 | 0.003824 | 20.51 | 0.003597 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | 11.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 71.9 | 26.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 0 | 15.81 | 0.025 |
| utilisation (used / allocatable) | 0.03309 | 0.005896 | 0.03589 | 0.008714 |
| CPU used (cores), mean | 1.588 | 0.283 | 1.561 | 0.242 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01228 | 0.00883 |
| CPU used with Omni's own (cores), mean | 1.588 | 0.283 | 1.573 | 0.2508 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 4303 | 756.2 | 3439 |
| HPA replicas, mean | 4.106 | 4.212 | 4.224 | 4.486 |
| pods started | 0.1 | 0.7 | 0.5 | 1.8 |
| pod start wait, total (s) | 0.3 | 1.3 | 1.1 | 3 |
| pod start wait, mean (s) | 0.3 | 1 | 0.85 | 1.667 |
| host CPU busy, the real machine under kind (%) | 48.74 | 14.57 | 50 | 15.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 823.5 | 1504 | 829.1 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.02 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1158 | 0.07083 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1474 | 0.4 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 1158 | 136.4 | 1160 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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
| worker nodes in service, mean | 12 | 6.931 | −42.2% | −5.2613 to −4.8759 | yes: GAIN |
| node-hours | 5.025 | 2.904 | −42.2% | −2.2016 to −2.0393 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 504.5 | +0.1% | −0.2529 to +0.9179 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 345.3 | −31.5% | −165.1013 to −152.8004 | yes: GAIN |
| response time (ms), mean | 120 | 69.17 | −42.3% | −59.0392 to −42.5683 | yes: GAIN |
| response time (ms), 95th percentile | 170 | 86.87 | −48.9% | −97.6490 to −68.5280 | yes: GAIN |
| response time (ms), 99th percentile | 195.8 | 113.7 | −41.9% | −98.7968 to −65.2948 | yes: GAIN |
| time over the response line (% of samples) | 0.003824 | 0.003597 | −5.9% | −0.0007 to +0.0003 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +24.8395 to +28.1605 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.025 | +0.025 (native is 0) | −0.0315 to +0.0815 | no |
| utilisation (used / allocatable) | 0.005896 | 0.008714 | +47.8% | +0.0027 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.283 | 0.242 | −14.5% | −0.0452 to −0.0368 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00883 | +0.009 (native is 0) | +0.0080 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.283 | 0.2508 | −11.4% | −0.0360 to −0.0284 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4303 | 3439 | −20.1% | −979.8665 to −748.3587 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.212 | 4.486 | +6.5% | +0.1036 to +0.4453 | yes: power given |
| pods started | 0.7 | 1.8 | +157.1% | +0.4737 to +1.7263 | yes: power given |
| pod start wait, total (s) | 1.3 | 3 | +130.8% | +0.8047 to +2.5953 | yes: LOSS |
| pod start wait, mean (s) | 1 | 1.667 | +66.7% | −0.2022 to +1.5355 | no |
| host CPU busy, the real machine under kind (%) | 14.57 | 15.59 | +7.0% | +0.8107 to +1.2232 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1504 | 1507 | +0.2% | +0.9491 to +3.6509 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1160 | +0.2% | +0.1963 to +3.4454 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 1476 | +0.1% | +0.1166 to +3.2834 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1160 | +0.2% | +0.1963 to +3.4454 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.041 | 5.025 | −0.3% | −0.0317 to −0.0010 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.2 | −4.1% | −24.0782 to −19.3151 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.2 | −4.1% | −24.0782 to −19.3151 | yes: GAIN |
| response time (ms), mean | 464.7 | 120 | −74.2% | −572.2249 to −117.1697 | yes: GAIN |
| response time (ms), 95th percentile | 1693 | 170 | −90.0% | −2590.1553 to −455.0417 | yes: GAIN |
| response time (ms), 99th percentile | 2315 | 195.8 | −91.5% | −3560.1265 to −678.5511 | yes: GAIN |
| time over the response line (% of samples) | 21.92 | 0.003824 | −100.0% | −31.1015 to −12.7244 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | −100.0% | −15.6679 to −7.1321 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 0 | −100.0% | −16.8884 to −6.9116 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03309 | 0.005896 | −82.2% | −0.0302 to −0.0242 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.588 | 0.283 | −82.2% | −1.4502 to −1.1607 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.588 | 0.283 | −82.2% | −1.4502 to −1.1607 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 4303 | +436.0% | +3225.7425 to +3775.0654 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.106 | 4.212 | +2.6% | −0.1100 to +0.3217 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0.3 | 1.3 | +333.3% | −0.1681 to +2.1681 | no |
| pod start wait, mean (s) | 0.3 | 1 | +233.3% | −0.1953 to +1.5953 | no |
| host CPU busy, the real machine under kind (%) | 48.74 | 14.57 | −70.1% | −38.5111 to −29.8154 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.5 | 1504 | +82.7% | +602.9422 to +758.6578 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1158 | +1462468.4% | +1155.8906 to +1159.6844 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1474 | +245566.7% | +1471.3712 to +1475.4288 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 1158 | +765.4% | +946.6867 to +1101.4633 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.3% | −2.2433 to +0.0215 | no |
| node-hours | 5.041 | 4.56 | −9.6% | −0.9660 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 523.8 | −0.4% | −3.6166 to −0.5539 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 489 | −7.0% | −73.6341 to −0.0989 | yes: GAIN |
| response time (ms), mean | 464.7 | 423.1 | −8.9% | −68.9373 to −14.1977 | yes: GAIN |
| response time (ms), 95th percentile | 1693 | 1722 | +1.7% | −152.6136 to +211.6706 | no |
| response time (ms), 99th percentile | 2315 | 2316 | +0.1% | −226.0083 to +228.4753 | no |
| time over the response line (% of samples) | 21.92 | 20.51 | −6.4% | −3.2023 to +0.3863 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 11.6 | +1.8% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.9 | +71.900 (native is 0) | +39.7254 to +104.0746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 15.81 | +32.9% | −3.9025 to +11.7291 | no |
| utilisation (used / allocatable) | 0.03309 | 0.03589 | +8.5% | −0.0007 to +0.0063 | no |
| CPU used (cores), mean | 1.588 | 1.561 | −1.7% | −0.0831 to +0.0279 | no |
| Omni's own CPU (cores), mean | 0 | 0.01228 | +0.012 (native is 0) | +0.0109 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.588 | 1.573 | −1.0% | −0.0708 to +0.0402 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 756.2 | −5.8% | −106.8683 to +13.6136 | no |
| HPA replicas, mean | 4.106 | 4.224 | +2.9% | −0.1974 to +0.4342 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −0.8101 to +2.4101 | no |
| pod start wait, mean (s) | 0.3 | 0.85 | +183.3% | −0.7609 to +1.8609 | no |
| host CPU busy, the real machine under kind (%) | 48.74 | 50 | +2.6% | +0.5921 to +1.9292 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.5 | 829.1 | +0.7% | −10.2742 to +21.4742 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.02 | −16.5% | −3.8473 to −0.1083 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.07083 | −10.5% | −0.0900 to +0.0733 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 136.4 | +2.0% | −10.1284 to +15.4367 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.3% | −2.2433 to +0.0215 | no |
| node-hours | 5.025 | 4.56 | −9.3% | −0.9441 to +0.0140 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 523.8 | +3.9% | +16.0886 to +23.1342 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 489 | −3.0% | −53.2890 to +22.9493 | no |
| response time (ms), mean | 120 | 423.1 | +252.7% | +59.6258 to +546.6338 | yes: LOSS |
| response time (ms), 95th percentile | 170 | 1722 | +913.2% | +348.4931 to +2755.7609 | yes: LOSS |
| response time (ms), 99th percentile | 195.8 | 2316 | +1083.3% | +519.5807 to +3721.5639 | yes: LOSS |
| time over the response line (% of samples) | 0.003824 | 20.51 | +536204.5% | +11.2544 to +29.7555 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.6 | +11.600 (native is 0) | +6.9987 to +16.2013 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.9 | +71.900 (native is 0) | +39.7254 to +104.0746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 15.81 | +15.813 (native is 0) | +4.1012 to +27.5255 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005896 | 0.03589 | +508.7% | +0.0279 to +0.0321 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.283 | 1.561 | +451.5% | +1.1155 to +1.4402 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01228 | +0.012 (native is 0) | +0.0109 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.283 | 1.573 | +455.9% | +1.1279 to +1.4523 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4303 | 756.2 | −82.4% | −3861.4553 to −3232.6075 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.212 | 4.224 | +0.3% | −0.3567 to +0.3817 | no |
| pods started | 0.7 | 0.5 | −28.6% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 1.3 | 1.1 | −15.4% | −1.3583 to +0.9583 | no |
| pod start wait, mean (s) | 1 | 0.85 | −15.0% | −1.2433 to +0.9433 | no |
| host CPU busy, the real machine under kind (%) | 14.57 | 50 | +243.1% | +30.7729 to +40.0749 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1504 | 829.1 | −44.9% | −767.0592 to −583.3408 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.07083 | −100.0% | −1159.7038 to −1155.8879 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 0.4 | −100.0% | −1475.7112 to −1471.4888 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 136.4 | −88.2% | −1109.2846 to −933.5571 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.931 | −42.2% | −5.2613 to −4.8759 | yes: GAIN |
| node-hours | 5.041 | 2.904 | −42.4% | −2.2197 to −2.0538 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.5 | −4.1% | −23.6184 to −19.1099 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 345.3 | −34.3% | −185.1988 to −176.0962 | yes: GAIN |
| response time (ms), mean | 464.7 | 69.17 | −85.1% | −630.3152 to −160.6869 | yes: GAIN |
| response time (ms), 95th percentile | 1693 | 86.87 | −94.9% | −2683.0811 to −528.2929 | yes: GAIN |
| response time (ms), 99th percentile | 2315 | 113.7 | −95.1% | −3657.5867 to −745.1825 | yes: GAIN |
| time over the response line (% of samples) | 21.92 | 0.003597 | −100.0% | −31.1019 to −12.7245 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | −100.0% | −15.6679 to −7.1321 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +24.8395 to +28.1605 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 0.025 | −99.8% | −16.8275 to −6.9225 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03309 | 0.008714 | −73.7% | −0.0274 to −0.0214 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.588 | 0.242 | −84.8% | −1.4933 to −1.1995 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00883 | +0.009 (native is 0) | +0.0080 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.588 | 0.2508 | −84.2% | −1.4837 to −1.1914 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 3439 | +328.4% | +2463.3502 to +2809.2325 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.106 | 4.486 | +9.3% | +0.1652 to +0.5954 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +1.1111 to +2.2889 | yes: power given |
| pod start wait, total (s) | 0.3 | 3 | +900.0% | +1.4361 to +3.9639 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.667 | +455.6% | +0.4946 to +2.2388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.74 | 15.59 | −68.0% | −37.4012 to −28.8914 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.5 | 1507 | +83.0% | +605.8730 to +760.3270 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1160 | +1464768.4% | +1156.8572 to +1162.3595 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245850.0% | +1472.3307 to +1477.8693 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 1160 | +766.8% | +949.2731 to +1102.5186 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*