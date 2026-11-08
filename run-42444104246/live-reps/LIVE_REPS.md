# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.947 | 5.02 |
| node-hours | 2.513 | 2.514 | 2.075 | 2.105 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.7 | 273.7 | 274.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.7 | 240.6 | 243.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 385.8 | 422.6 | 375.9 | 419.8 |
| response time (ms), 95th percentile | 1415 | 1858 | 1574 | 1973 |
| response time (ms), 99th percentile | 2003 | 2579 | 2223 | 2759 |
| time over the response line (% of samples) | 17.22 | 14.35 | 17.35 | 15.22 |
| failed requests (%) | 0 | 0.01205 | 0 | 0.01105 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9 | 9.6 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 110.1 | 70.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 23.19 | 10.51 | 30.96 |
| utilisation (used / allocatable) | 0.0621 | 0.0633 | 0.0768 | 0.07617 |
| CPU used (cores), mean | 1.49 | 1.519 | 1.493 | 1.519 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07111 | 0.07862 |
| CPU used with Omni's own (cores), mean | 1.49 | 1.519 | 1.565 | 1.598 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 441.2 | 385.8 | 384.6 |
| HPA replicas, mean | 1.922 | 2.023 | 2.363 | 2.132 |
| pods started | 0 | 0.2 | 1.8 | 0.8 |
| pod start wait, total (s) | 0 | 0.3 | 3.8 | 1.7 |
| pod start wait, mean (s) | 0 | 0.3 | 1.258 | 0.65 |
| host CPU busy, the real machine under kind (%) | 42.38 | 45.18 | 45.53 | 49.17 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 798.1 | 836 | 807.9 | 854.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.245 | 4.175 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.9833 | 0.05833 | 1.15 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.1 | 0.4 | 3.8 |
| queue: job turnaround, submitted to done, mean (s) | 105.2 | 137.4 | 112.3 | 155.5 |
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
| worker nodes in service, mean | 6 | 5.02 | −16.3% | −1.6641 to −0.2955 | yes: GAIN |
| node-hours | 2.514 | 2.105 | −16.3% | −0.6983 to −0.1192 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.1 | +0.1% | −0.7205 to +1.4658 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 243.3 | −11.1% | −52.1709 to −8.6463 | yes: GAIN |
| response time (ms), mean | 422.6 | 419.8 | −0.7% | −31.9486 to +26.2263 | no |
| response time (ms), 95th percentile | 1858 | 1973 | +6.2% | −90.1526 to +321.4386 | no |
| response time (ms), 99th percentile | 2579 | 2759 | +7.0% | −63.2059 to +423.0271 | no |
| time over the response line (% of samples) | 14.35 | 15.22 | +6.1% | −0.8056 to +2.5527 | no |
| failed requests (%) | 0.01205 | 0.01105 | −8.3% | −0.0400 to +0.0380 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 10.9 | +21.1% | −0.3481 to +4.1481 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.2 | +70.200 (native is 0) | +35.2599 to +105.1401 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.19 | 30.96 | +33.5% | +0.1305 to +15.4061 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0633 | 0.07617 | +20.3% | +0.0031 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 1.519 | −0.0% | −0.0145 to +0.0139 | no |
| Omni's own CPU (cores), mean | 0 | 0.07862 | +0.079 (native is 0) | +0.0701 to +0.0871 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 1.598 | +5.2% | +0.0599 to +0.0968 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.2 | 384.6 | −12.8% | −100.1401 to −13.0857 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.132 | +5.4% | −0.0877 to +0.3062 | no |
| pods started | 0.2 | 0.8 | +300.0% | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | −0.2588 to +3.0588 | no |
| pod start wait, mean (s) | 0.3 | 0.65 | +116.7% | −0.1845 to +0.8845 | no |
| host CPU busy, the real machine under kind (%) | 45.18 | 49.17 | +8.8% | +3.3482 to +4.6449 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836 | 854.1 | +2.2% | +7.0367 to +29.1633 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.175 | −30.4% | −2.8853 to −0.7649 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9833 | 1.15 | +16.9% | −0.0882 to +0.4215 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.8 | +81.0% | −0.0538 to +3.4538 | no |
| queue: job turnaround, submitted to done, mean (s) | 137.4 | 155.5 | +13.2% | +9.4190 to +26.8727 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.514 | +0.0% | −0.0067 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.7 | +0.3% | −0.1366 to +1.5817 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.7 | +0.3% | −0.1366 to +1.5817 | no |
| response time (ms), mean | 385.8 | 422.6 | +9.6% | +0.6736 to +73.0308 | yes: LOSS |
| response time (ms), 95th percentile | 1415 | 1858 | +31.3% | +84.1126 to +801.6724 | yes: LOSS |
| response time (ms), 99th percentile | 2003 | 2579 | +28.7% | +127.0762 to +1023.9374 | yes: LOSS |
| time over the response line (% of samples) | 17.22 | 14.35 | −16.7% | −5.2994 to −0.4447 | yes: GAIN |
| failed requests (%) | 0 | 0.01205 | +0.012 (native is 0) | −0.0152 to +0.0393 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9 | −2.2% | −1.8450 to +1.4450 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 23.19 | +117.8% | +7.8014 to +17.2786 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0621 | 0.0633 | +1.9% | −0.0005 to +0.0029 | no |
| CPU used (cores), mean | 1.49 | 1.519 | +1.9% | −0.0112 to +0.0691 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.49 | 1.519 | +1.9% | −0.0112 to +0.0691 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 441.2 | −1.5% | −21.8078 to +8.7072 | no |
| HPA replicas, mean | 1.922 | 2.023 | +5.2% | +0.0086 to +0.1929 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 42.38 | 45.18 | +6.6% | +1.9509 to +3.6483 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 798.1 | 836 | +4.7% | +12.2985 to +63.5015 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.9833 | +1585.7% | +0.5710 to +1.2790 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.1 | +600.0% | −0.0407 to +3.6407 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.2 | 137.4 | +30.6% | +12.0997 to +52.2337 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.947 | −17.5% | −1.8490 to −0.2563 | yes: GAIN |
| node-hours | 2.513 | 2.075 | −17.4% | −0.7703 to −0.1056 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.7 | +0.3% | −0.1500 to +1.5536 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 240.6 | −11.9% | −57.5455 to −7.3175 | yes: GAIN |
| response time (ms), mean | 385.8 | 375.9 | −2.6% | −31.7714 to +11.9936 | no |
| response time (ms), 95th percentile | 1415 | 1574 | +11.3% | +23.5216 to +295.1084 | yes: LOSS |
| response time (ms), 99th percentile | 2003 | 2223 | +10.9% | −94.7879 to +533.1241 | no |
| time over the response line (% of samples) | 17.22 | 17.35 | +0.7% | −0.3605 to +0.6162 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.6 | +4.3% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.1 | +110.100 (native is 0) | +37.9414 to +182.2586 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 10.51 | −1.3% | −1.3981 to +1.1214 | no |
| utilisation (used / allocatable) | 0.0621 | 0.0768 | +23.7% | +0.0036 to +0.0258 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.49 | 1.493 | +0.2% | −0.0341 to +0.0404 | no |
| Omni's own CPU (cores), mean | 0 | 0.07111 | +0.071 (native is 0) | +0.0643 to +0.0780 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.49 | 1.565 | +5.0% | +0.0325 to +0.1160 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 385.8 | −13.8% | −105.9487 to −18.0164 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.363 | +23.0% | +0.2208 to +0.6620 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.6417 to +2.9583 | yes: power given |
| pod start wait, total (s) | 0 | 3.8 | +3.800 (native is 0) | +1.1492 to +6.4508 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.258 | +1.258 (native is 0) | +0.4245 to +2.0921 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.38 | 45.53 | +7.4% | +2.6326 to +3.6767 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 798.1 | 807.9 | +1.2% | +1.1385 to +18.4615 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.245 | −29.3% | −2.8715 to −0.6385 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05833 | 0.0% | raw −0.0344 to +0.0344 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.2 | 112.3 | +6.8% | −0.6724 to +14.8808 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.947 | −17.5% | −1.8490 to −0.2563 | yes: GAIN |
| node-hours | 2.514 | 2.075 | −17.5% | −0.7719 to −0.1063 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.7 | −0.0% | −0.7661 to +0.7245 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 240.6 | −12.1% | −58.0904 to −8.2179 | yes: GAIN |
| response time (ms), mean | 422.6 | 375.9 | −11.1% | −85.5208 to −7.9613 | yes: GAIN |
| response time (ms), 95th percentile | 1858 | 1574 | −15.3% | −597.0272 to +29.8722 | no |
| response time (ms), 99th percentile | 2579 | 2223 | −13.8% | −764.6569 to +51.9795 | no |
| time over the response line (% of samples) | 14.35 | 17.35 | +20.9% | +0.7673 to +5.2325 | yes: LOSS |
| failed requests (%) | 0.01205 | 0 | −100.0% | −0.0393 to +0.0152 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.6 | +6.7% | −1.1586 to +2.3586 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.1 | +110.100 (native is 0) | +37.9414 to +182.2586 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.19 | 10.51 | −54.7% | −17.7574 to −7.5993 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0633 | 0.0768 | +21.3% | +0.0015 to +0.0255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 1.493 | −1.7% | −0.0383 to −0.0133 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07111 | +0.071 (native is 0) | +0.0643 to +0.0780 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 1.565 | +3.0% | +0.0280 to +0.0627 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.2 | 385.8 | −12.6% | −104.6033 to −6.2613 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.363 | +16.8% | +0.1451 to +0.5362 | yes: power given |
| pods started | 0.2 | 1.8 | +800.0% | +0.5231 to +2.6769 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.8 | +1166.7% | +0.9264 to +6.0736 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.258 | +319.4% | +0.1138 to +1.8029 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.18 | 45.53 | +0.8% | −0.2823 to +0.9925 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836 | 807.9 | −3.4% | −47.5100 to −8.6900 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.245 | −29.3% | −2.8715 to −0.6385 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9833 | 0.05833 | −94.1% | −1.2773 to −0.5727 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 0.4 | −81.0% | −3.5790 to +0.1790 | no |
| queue: job turnaround, submitted to done, mean (s) | 137.4 | 112.3 | −18.2% | −40.4240 to −9.7010 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.02 | −16.3% | −1.6641 to −0.2955 | yes: GAIN |
| node-hours | 2.513 | 2.105 | −16.2% | −0.6965 to −0.1187 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 274.1 | +0.4% | +0.1317 to +2.0588 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 243.3 | −10.9% | −51.6447 to −7.7273 | yes: GAIN |
| response time (ms), mean | 385.8 | 419.8 | +8.8% | −8.0223 to +76.0043 | no |
| response time (ms), 95th percentile | 1415 | 1973 | +39.5% | +163.9798 to +953.0912 | yes: LOSS |
| response time (ms), 99th percentile | 2003 | 2759 | +37.7% | +234.4543 to +1276.3805 | yes: LOSS |
| time over the response line (% of samples) | 17.22 | 15.22 | −11.6% | −5.1593 to +1.1623 | no |
| failed requests (%) | 0 | 0.01105 | +0.011 (native is 0) | −0.0139 to +0.0360 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.9 | +18.5% | +0.7433 to +2.6567 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.2 | +70.200 (native is 0) | +35.2599 to +105.1401 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 30.96 | +190.7% | +8.2880 to +32.3287 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0621 | 0.07617 | +22.7% | +0.0055 to +0.0227 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.49 | 1.519 | +1.9% | −0.0125 to +0.0699 | no |
| Omni's own CPU (cores), mean | 0 | 0.07862 | +0.079 (native is 0) | +0.0701 to +0.0871 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.49 | 1.598 | +7.2% | +0.0629 to +0.1517 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 384.6 | −14.1% | −100.2562 to −26.0702 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.132 | +10.9% | +0.0152 to +0.4048 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| pod start wait, total (s) | 0 | 1.7 | +1.700 (native is 0) | −0.2676 to +3.6676 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.650 (native is 0) | −0.1049 to +1.4049 | no |
| host CPU busy, the real machine under kind (%) | 42.38 | 49.17 | +16.0% | +5.6865 to +7.9059 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 798.1 | 854.1 | +7.0% | +20.2935 to +91.7065 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.175 | −30.4% | −2.8853 to −0.7649 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1.15 | +1871.4% | +0.6575 to +1.5258 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 3.8 | +1166.7% | +0.6537 to +6.3463 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.2 | 155.5 | +47.8% | +22.9155 to +77.7095 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*