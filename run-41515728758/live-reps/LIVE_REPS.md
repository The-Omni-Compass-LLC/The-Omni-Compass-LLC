# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.75 | 4.501 |
| node-hours | 2.516 | 2.515 | 1.993 | 1.886 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 | 272.6 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 | 233.3 | 224.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 321.3 | 268.4 | 304.8 | 244.3 |
| response time (ms), 95th percentile | 1121 | 996.6 | 1247 | 1056 |
| response time (ms), 99th percentile | 1616 | 1590 | 1674 | 1615 |
| time over the response line (% of samples) | 12.69 | 8.705 | 13.2 | 7.69 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.7 | 7.9 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 147.4 | 133.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.71 | 16.07 | 11.37 | 17.86 |
| utilisation (used / allocatable) | 0.05958 | 0.05907 | 0.07627 | 0.07929 |
| CPU used (cores), mean | 1.43 | 1.418 | 1.419 | 1.402 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06777 | 0.07077 |
| CPU used with Omni's own (cores), mean | 1.43 | 1.418 | 1.486 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 469.8 | 393.9 | 384.6 |
| HPA replicas, mean | 1.944 | 2.046 | 2.34 | 2.261 |
| pods started | 0 | 0.3 | 0.6 | 0.8 |
| pod start wait, total (s) | 0 | 0.6 | 1.2 | 1.8 |
| pod start wait, mean (s) | 0 | 0.4 | 0.8 | 0.4533 |
| host CPU busy, the real machine under kind (%) | 40.46 | 41.36 | 43.55 | 44.25 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.8 | 786.7 | 785.4 | 791.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.94 | 3.568 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7833 | 0.1792 | 0.7833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.6 | 0.6 | 2 |
| queue: job turnaround, submitted to done, mean (s) | 82.65 | 95.56 | 90.91 | 101.3 |
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
| worker nodes in service, mean | 6 | 4.501 | −25.0% | −2.3496 to −0.6475 | yes: GAIN |
| node-hours | 2.515 | 1.886 | −25.0% | −0.9841 to −0.2741 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | −0.0% | −0.8168 to +0.6198 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 224.9 | −17.3% | −74.0521 to −20.3616 | yes: GAIN |
| response time (ms), mean | 268.4 | 244.3 | −9.0% | −39.9769 to −8.1984 | yes: GAIN |
| response time (ms), 95th percentile | 996.6 | 1056 | +6.0% | −75.3461 to +194.7551 | no |
| response time (ms), 99th percentile | 1590 | 1615 | +1.6% | −122.8491 to +172.1833 | no |
| time over the response line (% of samples) | 8.705 | 7.69 | −11.7% | −2.1754 to +0.1443 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 6.4 | +12.3% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.5 | +133.500 (native is 0) | +70.2150 to +196.7850 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.07 | 17.86 | +11.1% | −1.6860 to +5.2493 | no |
| utilisation (used / allocatable) | 0.05907 | 0.07929 | +34.2% | +0.0085 to +0.0320 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.402 | −1.1% | −0.0521 to +0.0212 | no |
| Omni's own CPU (cores), mean | 0 | 0.07077 | +0.071 (native is 0) | +0.0623 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.473 | +3.9% | +0.0119 to +0.0988 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.8 | 384.6 | −18.1% | −133.0294 to −37.3900 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.046 | 2.261 | +10.5% | −0.1072 to +0.5380 | no |
| pods started | 0.3 | 0.8 | +166.7% | −0.9405 to +1.9405 | no |
| pod start wait, total (s) | 0.6 | 1.8 | +200.0% | −1.9596 to +4.3596 | no |
| pod start wait, mean (s) | 0.4 | 0.4533 | +13.3% | −0.9654 to +1.0721 | no |
| host CPU busy, the real machine under kind (%) | 41.36 | 44.25 | +7.0% | +2.4880 to +3.2978 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.7 | 791.8 | +0.6% | −1.4076 to +11.6076 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.568 | −40.5% | −3.6453 to −1.2190 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.7833 | 0.0% | raw −0.2351 to +0.2351 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2 | +25.0% | −1.3907 to +2.1907 | no |
| queue: job turnaround, submitted to done, mean (s) | 95.56 | 101.3 | +6.0% | −1.1280 to +12.5530 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.515 | −0.1% | −0.0108 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 | −0.1% | −1.5897 to +0.8700 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 | −0.1% | −1.5897 to +0.8700 | no |
| response time (ms), mean | 321.3 | 268.4 | −16.5% | −90.2090 to −15.6692 | yes: GAIN |
| response time (ms), 95th percentile | 1121 | 996.6 | −11.1% | −221.7683 to −26.8907 | yes: GAIN |
| response time (ms), 99th percentile | 1616 | 1590 | −1.6% | −170.5302 to +118.3300 | no |
| time over the response line (% of samples) | 12.69 | 8.705 | −31.4% | −7.1086 to −0.8631 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.7 | −18.6% | −2.6081 to +0.0081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.71 | 16.07 | +65.6% | +2.2276 to +10.5024 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05958 | 0.05907 | −0.9% | −0.0014 to +0.0004 | no |
| CPU used (cores), mean | 1.43 | 1.418 | −0.9% | −0.0342 to +0.0096 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.43 | 1.418 | −0.9% | −0.0342 to +0.0096 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 469.8 | +1.2% | −2.3741 to +13.7903 | no |
| HPA replicas, mean | 1.944 | 2.046 | +5.2% | −0.0406 to +0.2432 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 40.46 | 41.36 | +2.2% | +0.5058 to +1.2995 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.8 | 786.7 | +1.3% | −0.1282 to +19.9282 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7833 | +1466.7% | +0.5432 to +0.9235 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.6 | +700.0% | +0.7089 to +2.0911 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.65 | 95.56 | +15.6% | +0.2281 to +25.5802 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.75 | −20.8% | −2.0919 to −0.4086 | yes: GAIN |
| node-hours | 2.516 | 1.993 | −20.8% | −0.8784 to −0.1679 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.6 | +0.1% | −0.8702 to +1.2082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 233.3 | −14.4% | −66.2633 to −12.0987 | yes: GAIN |
| response time (ms), mean | 321.3 | 304.8 | −5.1% | −29.3153 to −3.6670 | yes: GAIN |
| response time (ms), 95th percentile | 1121 | 1247 | +11.2% | +25.3511 to +226.3349 | yes: LOSS |
| response time (ms), 99th percentile | 1616 | 1674 | +3.6% | −78.1154 to +193.5298 | no |
| time over the response line (% of samples) | 12.69 | 13.2 | +4.0% | −1.1655 to +2.1906 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.9 | +12.9% | −1.0209 to +2.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 147.4 | +147.400 (native is 0) | +73.1180 to +221.6820 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.71 | 11.37 | +17.1% | −0.3781 to +3.6981 | no |
| utilisation (used / allocatable) | 0.05958 | 0.07627 | +28.0% | +0.0054 to +0.0280 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.43 | 1.419 | −0.8% | −0.0471 to +0.0243 | no |
| Omni's own CPU (cores), mean | 0 | 0.06777 | +0.068 (native is 0) | +0.0601 to +0.0755 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.486 | +3.9% | +0.0141 to +0.0986 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 393.9 | −15.1% | −114.4693 to −26.0486 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.944 | 2.34 | +20.3% | +0.0875 to +0.7034 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.0064 to +2.4064 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.46 | 43.55 | +7.6% | +2.6135 to +3.5692 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.8 | 785.4 | +1.1% | +0.2909 to +16.9091 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.94 | −34.3% | −3.2983 to −0.8207 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1792 | +258.3% | −0.0569 to +0.3153 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | −0.1001 to +0.9001 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.65 | 90.91 | +10.0% | +0.8449 to +15.6718 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.75 | −20.8% | −2.0919 to −0.4086 | yes: GAIN |
| node-hours | 2.515 | 1.993 | −20.7% | −0.8744 to −0.1689 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.6 | +0.2% | −0.3755 to +1.4331 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 233.3 | −14.3% | −65.4348 to −12.2076 | yes: GAIN |
| response time (ms), mean | 268.4 | 304.8 | +13.6% | +1.6280 to +71.2679 | yes: LOSS |
| response time (ms), 95th percentile | 996.6 | 1247 | +25.1% | +162.9418 to +337.4032 | yes: LOSS |
| response time (ms), 99th percentile | 1590 | 1674 | +5.3% | −146.0320 to +313.6466 | no |
| time over the response line (% of samples) | 8.705 | 13.2 | +51.7% | +1.2490 to +7.7479 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 7.9 | +38.6% | −0.2502 to +4.6502 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 147.4 | +147.400 (native is 0) | +73.1180 to +221.6820 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.07 | 11.37 | −29.3% | −8.3772 to −1.0328 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05907 | 0.07627 | +29.1% | +0.0053 to +0.0291 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.419 | +0.1% | −0.0276 to +0.0294 | no |
| Omni's own CPU (cores), mean | 0 | 0.06777 | +0.068 (native is 0) | +0.0601 to +0.0755 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.486 | +4.8% | +0.0354 to +0.1019 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.8 | 393.9 | −16.2% | −126.0000 to −25.9341 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.046 | 2.34 | +14.4% | −0.0074 to +0.5957 | no |
| pods started | 0.3 | 0.6 | +100.0% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 0.6 | 1.2 | +100.0% | −0.9155 to +2.1155 | no |
| pod start wait, mean (s) | 0.4 | 0.8 | +100.0% | −0.5048 to +1.3048 | no |
| host CPU busy, the real machine under kind (%) | 41.36 | 43.55 | +5.3% | +1.8342 to +2.5433 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.7 | 785.4 | −0.2% | −5.9851 to +3.3851 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.94 | −34.3% | −3.2983 to −0.8207 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.1792 | −77.1% | −0.7923 to −0.4161 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.6 | −62.5% | −1.4769 to −0.5231 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 95.56 | 90.91 | −4.9% | −13.0196 to +3.7279 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.501 | −25.0% | −2.3496 to −0.6475 | yes: GAIN |
| node-hours | 2.516 | 1.886 | −25.1% | −0.9897 to −0.2715 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272 | −0.2% | −1.6790 to +0.7623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 224.9 | −17.5% | −75.0757 to −20.0576 | yes: GAIN |
| response time (ms), mean | 321.3 | 244.3 | −24.0% | −108.9248 to −45.1288 | yes: GAIN |
| response time (ms), 95th percentile | 1121 | 1056 | −5.8% | −218.8317 to +89.5817 | no |
| response time (ms), 99th percentile | 1616 | 1615 | −0.1% | −240.1477 to +237.2817 | no |
| time over the response line (% of samples) | 12.69 | 7.69 | −39.4% | −9.0527 to −0.9502 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.4 | −8.6% | −1.4396 to +0.2396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.5 | +133.500 (native is 0) | +70.2150 to +196.7850 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.71 | 17.86 | +83.9% | +4.4330 to +11.8604 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05958 | 0.07929 | +33.1% | +0.0087 to +0.0307 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.43 | 1.402 | −1.9% | −0.0751 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0 | 0.07077 | +0.071 (native is 0) | +0.0623 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.473 | +3.0% | −0.0119 to +0.0980 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 384.6 | −17.1% | −121.0739 to −37.9293 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.944 | 2.261 | +16.3% | +0.0338 to +0.5997 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.4526 to +2.0526 | no |
| pod start wait, total (s) | 0 | 1.8 | +1.800 (native is 0) | −0.9969 to +4.5969 | no |
| pod start wait, mean (s) | 0 | 0.4533 | +0.453 (native is 0) | −0.2307 to +1.1373 | no |
| host CPU busy, the real machine under kind (%) | 40.46 | 44.25 | +9.4% | +3.1827 to +4.4084 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.8 | 791.8 | +1.9% | +2.0452 to +27.9548 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.568 | −40.5% | −3.6453 to −1.2190 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7833 | +1466.7% | +0.4773 to +0.9894 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 2 | +900.0% | +0.2256 to +3.3744 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.65 | 101.3 | +22.5% | +2.7823 to +34.4510 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*