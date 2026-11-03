# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.944 | 5.997 |
| node-hours | 2.514 | 2.518 | 2.076 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 272.4 | 274.3 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 272.4 | 241.1 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 423.2 | 138.8 | 410.3 | 114.6 |
| response time (ms), 95th percentile | 1583 | 238.3 | 1741 | 252.5 |
| response time (ms), 99th percentile | 2172 | 333.2 | 2428 | 361.4 |
| time over the response line (% of samples) | 20.44 | 0.187 | 20.41 | 0.2342 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0 | 10.2 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 112.7 | 101.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.25 | 1235 | 12.33 | 1323 |
| utilisation (used / allocatable) | 0.06349 | 0.0599 | 0.07898 | 0.05861 |
| CPU used (cores), mean | 1.524 | 1.438 | 1.516 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07072 | 0.06948 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.438 | 1.587 | 1.475 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 452.2 | 378.3 | 461.3 |
| HPA replicas, mean | 2.04 | 1.994 | 2.296 | 2.113 |
| pods started | 0.2 | 0.1 | 1.2 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.1 | 2.4 | 1 |
| pod start wait, mean (s) | 0.1 | 0.1 | 1.175 | 0.6 |
| host CPU busy, the real machine under kind (%) | 43.42 | 45.07 | 46.05 | 46.74 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 805 | 1456 | 817.3 | 1482 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.413 | 5.906 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 165.8 | 0.09583 | 195 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 777.6 | 0.7 | 810.7 |
| queue: job turnaround, submitted to done, mean (s) | 112.4 | 898.2 | 122.7 | 913.6 |
| queue: jobs unfinished at the window's end | 0 | 13.3 | 0 | 13.8 |
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
| worker nodes in service, mean | 6 | 5.997 | −0.1% | −0.0103 to +0.0040 | no |
| node-hours | 2.518 | 2.514 | −0.1% | −0.0123 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.7 | −0.3% | −1.8501 to +0.4450 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.6 | −0.3% | −1.8890 to +0.2840 | no |
| response time (ms), mean | 138.8 | 114.6 | −17.5% | −31.4501 to −17.0283 | yes: GAIN |
| response time (ms), 95th percentile | 238.3 | 252.5 | +5.9% | +6.3362 to +21.9548 | yes: LOSS |
| response time (ms), 99th percentile | 333.2 | 361.4 | +8.4% | +12.6621 to +43.6211 | yes: LOSS |
| time over the response line (% of samples) | 0.187 | 0.2342 | +25.2% | −0.0532 to +0.1476 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.1 | +101.100 (native is 0) | +88.0995 to +114.1005 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1235 | 1323 | +7.2% | +35.7141 to +140.9526 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0599 | 0.05861 | −2.2% | −0.0027 to +0.0001 | no |
| CPU used (cores), mean | 1.438 | 1.406 | −2.2% | −0.0659 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0 | 0.06948 | +0.069 (native is 0) | +0.0621 to +0.0769 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.438 | 1.475 | +2.6% | +0.0050 to +0.0707 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.2 | 461.3 | +2.0% | −0.7577 to +18.9147 | no |
| HPA replicas, mean | 1.994 | 2.113 | +6.0% | −0.0744 to +0.3121 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 0.1 | 1 | +900.0% | −0.5484 to +2.3484 | no |
| pod start wait, mean (s) | 0.1 | 0.6 | +500.0% | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 45.07 | 46.74 | +3.7% | +0.8073 to +2.5281 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1456 | 1482 | +1.7% | −20.3277 to +71.1277 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.906 | −1.6% | −1.2849 to +1.0974 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 165.8 | 195 | +17.7% | −3.0319 to +61.5485 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 777.6 | 810.7 | +4.3% | −135.5277 to +201.7277 | no |
| queue: job turnaround, submitted to done, mean (s) | 898.2 | 913.6 | +1.7% | −26.6073 to +57.4573 | no |
| queue: jobs unfinished at the window's end | 13.3 | 13.8 | +3.8% | −1.6125 to +2.6125 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.518 | +0.2% | −0.0069 to +0.0145 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 272.4 | −0.5% | −3.7429 to +1.2441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 272.4 | −0.5% | −3.7429 to +1.2441 | no |
| response time (ms), mean | 423.2 | 138.8 | −67.2% | −434.2938 to −134.4396 | yes: GAIN |
| response time (ms), 95th percentile | 1583 | 238.3 | −84.9% | −2077.4339 to −612.8811 | yes: GAIN |
| response time (ms), 99th percentile | 2172 | 333.2 | −84.7% | −2831.7038 to −846.6924 | yes: GAIN |
| time over the response line (% of samples) | 20.44 | 0.187 | −99.1% | −31.4658 to −9.0475 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0 | −100.0% | −14.6845 to −5.3155 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.25 | 1235 | +10875.8% | +953.5610 to +1493.8523 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06349 | 0.0599 | −5.7% | −0.0093 to +0.0021 | no |
| CPU used (cores), mean | 1.524 | 1.438 | −5.7% | −0.2229 to +0.0505 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.524 | 1.438 | −5.7% | −0.2229 to +0.0505 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 452.2 | +3.3% | −24.1503 to +53.2959 | no |
| HPA replicas, mean | 2.04 | 1.994 | −2.2% | −0.1710 to +0.0795 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 45.07 | +3.8% | −1.1301 to +4.4360 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805 | 1456 | +80.9% | +591.0375 to +711.5625 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 165.8 | +248525.0% | +113.9215 to +217.4451 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 777.6 | +155420.0% | +600.7254 to +953.4746 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 112.4 | 898.2 | +699.4% | +660.4348 to +911.1902 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.3 | +13.300 (native is 0) | +6.6832 to +19.9168 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.944 | −17.6% | −2.0160 to −0.0951 | yes: GAIN |
| node-hours | 2.514 | 2.076 | −17.4% | −0.8388 to −0.0370 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.3 | +0.2% | −0.2107 to +1.4354 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 241.1 | −11.9% | −62.9665 to −2.2212 | yes: GAIN |
| response time (ms), mean | 423.2 | 410.3 | −3.0% | −26.4609 to +0.7790 | no |
| response time (ms), 95th percentile | 1583 | 1741 | +9.9% | +64.3786 to +250.1404 | yes: LOSS |
| response time (ms), 99th percentile | 2172 | 2428 | +11.8% | +116.6495 to +395.3135 | yes: LOSS |
| time over the response line (% of samples) | 20.44 | 20.41 | −0.2% | −1.8388 to +1.7667 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.2 | +2.0% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.7 | +112.700 (native is 0) | +41.0628 to +184.3372 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.25 | 12.33 | +9.6% | −0.6991 to +2.8525 | no |
| utilisation (used / allocatable) | 0.06349 | 0.07898 | +24.4% | +0.0021 to +0.0289 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.516 | −0.5% | −0.0454 to +0.0305 | no |
| Omni's own CPU (cores), mean | 0 | 0.07072 | +0.071 (native is 0) | +0.0638 to +0.0777 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.587 | +4.2% | +0.0189 to +0.1077 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 378.3 | −13.6% | −109.4542 to −9.2963 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.04 | 2.296 | +12.6% | +0.0265 to +0.4862 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 0.2 | 2.4 | +1100.0% | +0.1268 to +4.2732 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.175 | +1075.0% | +0.1827 to +1.9673 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.42 | 46.05 | +6.0% | +1.6632 to +3.5871 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805 | 817.3 | +1.5% | +5.5304 to +19.0696 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.413 | −26.4% | −2.9122 to −0.2608 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.09583 | +43.7% | −0.0439 to +0.1022 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | −0.6793 to +1.0793 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.4 | 122.7 | +9.2% | +3.7344 to +16.9323 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.944 | −17.6% | −2.0160 to −0.0951 | yes: GAIN |
| node-hours | 2.518 | 2.076 | −17.5% | −0.8459 to −0.0376 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 274.3 | +0.7% | −0.7478 to +4.4714 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 241.1 | −11.5% | −63.9883 to +1.2994 | no |
| response time (ms), mean | 138.8 | 410.3 | +195.6% | +125.4831 to +417.5685 | yes: LOSS |
| response time (ms), 95th percentile | 238.3 | 1741 | +630.4% | +742.3995 to +2262.4345 | yes: LOSS |
| response time (ms), 99th percentile | 333.2 | 2428 | +628.7% | +1024.3315 to +3166.0277 | yes: LOSS |
| time over the response line (% of samples) | 0.187 | 20.41 | +10811.3% | +9.7383 to +30.7029 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.2 | +10.200 (native is 0) | +5.3042 to +15.0958 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.7 | +112.700 (native is 0) | +41.0628 to +184.3372 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1235 | 12.33 | −99.0% | −1492.1097 to −953.1503 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0599 | 0.07898 | +31.8% | +0.0110 to +0.0272 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.438 | 1.516 | +5.5% | −0.0914 to +0.2489 | no |
| Omni's own CPU (cores), mean | 0 | 0.07072 | +0.071 (native is 0) | +0.0638 to +0.0777 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.438 | 1.587 | +10.4% | −0.0268 to +0.3257 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.2 | 378.3 | −16.4% | −88.3182 to −59.5779 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.994 | 2.296 | +15.2% | +0.0472 to +0.5571 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1198 to +2.0802 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.4 | +2300.0% | +0.3910 to +4.2090 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.175 | +1075.0% | +0.3208 to +1.8292 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.07 | 46.05 | +2.2% | −2.5698 to +4.5141 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1456 | 817.3 | −43.9% | −697.8352 to −580.1648 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 165.8 | 0.09583 | −99.9% | −217.4103 to −113.8981 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 777.6 | 0.7 | −99.9% | −953.1811 to −600.6189 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 898.2 | 122.7 | −86.3% | −896.3805 to −654.5778 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.3 | 0 | −100.0% | −19.9168 to −6.6832 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.997 | −0.1% | −0.0103 to +0.0040 | no |
| node-hours | 2.514 | 2.514 | +0.0% | −0.0079 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 271.7 | −0.7% | −4.7503 to +0.8463 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 271.6 | −0.7% | −4.7518 to +0.6479 | no |
| response time (ms), mean | 423.2 | 114.6 | −72.9% | −464.7042 to −152.5077 | yes: GAIN |
| response time (ms), 95th percentile | 1583 | 252.5 | −84.1% | −2062.1674 to −599.8566 | yes: GAIN |
| response time (ms), 99th percentile | 2172 | 361.4 | −83.4% | −2807.3342 to −814.7788 | yes: GAIN |
| time over the response line (% of samples) | 20.44 | 0.2342 | −98.9% | −31.4273 to −8.9917 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0.2 | −98.0% | −14.3839 to −5.2161 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.1 | +101.100 (native is 0) | +88.0995 to +114.1005 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.25 | 1323 | +11660.9% | +1060.2484 to +1563.8316 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06349 | 0.05861 | −7.7% | −0.0113 to +0.0015 | no |
| CPU used (cores), mean | 1.524 | 1.406 | −7.7% | −0.2701 to +0.0346 | no |
| Omni's own CPU (cores), mean | 0 | 0.06948 | +0.069 (native is 0) | +0.0621 to +0.0769 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.475 | −3.2% | −0.1942 to +0.0975 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 461.3 | +5.4% | −19.4105 to +66.7131 | no |
| HPA replicas, mean | 2.04 | 2.113 | +3.6% | −0.0540 to +0.2002 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.5953 to +1.1953 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.7379 to +2.3379 | no |
| pod start wait, mean (s) | 0.1 | 0.6 | +500.0% | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 46.74 | +7.6% | +0.1023 to +6.5391 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805 | 1482 | +84.1% | +620.0284 to +733.3716 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.906 | −1.6% | −1.2849 to +1.0974 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 195 | +292412.5% | +144.4674 to +245.4160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 810.7 | +162040.0% | +659.9511 to +960.4489 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 112.4 | 913.6 | +713.1% | +694.4015 to +908.0735 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.8 | +13.800 (native is 0) | +7.7417 to +19.8583 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*