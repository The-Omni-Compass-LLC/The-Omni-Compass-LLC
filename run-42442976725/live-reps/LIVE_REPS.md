# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.236 | 5.08 |
| node-hours | 2.515 | 2.511 | 2.196 | 2.13 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.1 | 273.9 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 273.1 | 249.9 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 395.9 | 416.7 | 384.5 | 402.9 |
| response time (ms), 95th percentile | 1428 | 1549 | 1578 | 1674 |
| response time (ms), 99th percentile | 1949 | 2202 | 2257 | 2427 |
| time over the response line (% of samples) | 17.32 | 17.7 | 17.71 | 17.77 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.9 | 10 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 98.6 | 101.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 7.407 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.76 | 11.24 | 12.35 | 14.54 |
| utilisation (used / allocatable) | 0.06312 | 0.06282 | 0.07327 | 0.07514 |
| CPU used (cores), mean | 1.515 | 1.508 | 1.512 | 1.513 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07354 | 0.07564 |
| CPU used with Omni's own (cores), mean | 1.515 | 1.508 | 1.586 | 1.589 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.7 | 442.8 | 397.5 | 387.9 |
| HPA replicas, mean | 2.023 | 2.035 | 2.337 | 2.314 |
| pods started | 0.2 | 0.1 | 1.4 | 1.2 |
| pod start wait, total (s) | 0.4 | 0.3 | 3.3 | 2.9 |
| pod start wait, mean (s) | 0.4 | 0.3 | 1.383 | 1.183 |
| host CPU busy, the real machine under kind (%) | 42.96 | 43.82 | 46.3 | 47.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 801.3 | 809.4 | 811.3 | 820 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.679 | 4.359 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1833 | 0.05417 | 0.3167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | 0.3 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 112.1 | 116.2 | 123.5 |
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
| worker nodes in service, mean | 6 | 5.08 | −15.3% | −1.6452 to −0.1949 | yes: GAIN |
| node-hours | 2.511 | 2.13 | −15.2% | −0.6865 to −0.0756 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.7 | +0.2% | −0.3791 to +1.5526 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 244.8 | −10.4% | −51.2598 to −5.3499 | yes: GAIN |
| response time (ms), mean | 416.7 | 402.9 | −3.3% | −26.8763 to −0.8125 | yes: GAIN |
| response time (ms), 95th percentile | 1549 | 1674 | +8.1% | −5.1867 to +256.2857 | no |
| response time (ms), 99th percentile | 2202 | 2427 | +10.2% | +12.7879 to +437.9513 | yes: LOSS |
| time over the response line (% of samples) | 17.7 | 17.77 | +0.4% | −0.5154 to +0.6571 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.5 | +6.1% | −0.4228 to +1.6228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 | +101.300 (native is 0) | +38.0026 to +164.5974 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 14.54 | +29.3% | +0.4626 to +6.1308 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06282 | 0.07514 | +19.6% | +0.0023 to +0.0223 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.508 | 1.513 | +0.3% | −0.0200 to +0.0304 | no |
| Omni's own CPU (cores), mean | 0 | 0.07564 | +0.076 (native is 0) | +0.0687 to +0.0826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.508 | 1.589 | +5.4% | +0.0520 to +0.1097 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.8 | 387.9 | −12.4% | −98.6136 to −11.3347 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.035 | 2.314 | +13.7% | +0.0617 to +0.4959 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | −0.0410 to +2.2410 | no |
| pod start wait, total (s) | 0.3 | 2.9 | +866.7% | −0.2652 to +5.4652 | no |
| pod start wait, mean (s) | 0.3 | 1.183 | +294.4% | −0.4093 to +2.1760 | no |
| host CPU busy, the real machine under kind (%) | 43.82 | 47.11 | +7.5% | +2.8328 to +3.7522 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.4 | 820 | +1.3% | +1.4944 to +19.7056 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 | −27.3% | −2.8108 to −0.4706 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.3167 | +72.7% | −0.0403 to +0.3070 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.1 | +22.2% | −0.3642 to +0.7642 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.1 | 123.5 | +10.2% | +2.9404 to +19.9346 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.511 | −0.1% | −0.0108 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.1 | −0.2% | −1.0430 to +0.1540 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 273.1 | −0.2% | −1.0430 to +0.1540 | no |
| response time (ms), mean | 395.9 | 416.7 | +5.3% | +6.3496 to +35.2774 | yes: LOSS |
| response time (ms), 95th percentile | 1428 | 1549 | +8.4% | +24.6608 to +216.0542 | yes: LOSS |
| response time (ms), 99th percentile | 1949 | 2202 | +12.9% | +53.5117 to +451.0303 | yes: LOSS |
| time over the response line (% of samples) | 17.32 | 17.7 | +2.2% | −0.1967 to +0.9444 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.9 | +6.5% | −0.3656 to +1.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.76 | 11.24 | +4.4% | −1.3992 to +2.3559 | no |
| utilisation (used / allocatable) | 0.06312 | 0.06282 | −0.5% | −0.0015 to +0.0009 | no |
| CPU used (cores), mean | 1.515 | 1.508 | −0.5% | −0.0368 to +0.0225 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.515 | 1.508 | −0.5% | −0.0368 to +0.0225 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.7 | 442.8 | +0.7% | −8.1701 to +14.4172 | no |
| HPA replicas, mean | 2.023 | 2.035 | +0.6% | −0.1365 to +0.1606 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.1366 to +0.9366 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −1.1366 to +0.9366 | no |
| host CPU busy, the real machine under kind (%) | 42.96 | 43.82 | +2.0% | +0.5975 to +1.1269 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.3 | 809.4 | +1.0% | +2.5855 to +13.6145 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1833 | +266.7% | +0.0831 to +0.1836 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 112.1 | +6.0% | +1.1724 to +11.5776 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.236 | −12.7% | −1.4291 to −0.0984 | yes: GAIN |
| node-hours | 2.515 | 2.196 | −12.7% | −0.5935 to −0.0434 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.9 | +0.1% | −0.5938 to +1.2286 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 249.9 | −8.7% | −44.2948 to −3.1413 | yes: GAIN |
| response time (ms), mean | 395.9 | 384.5 | −2.9% | −25.9606 to +3.2278 | no |
| response time (ms), 95th percentile | 1428 | 1578 | +10.5% | +53.4486 to +246.8374 | yes: LOSS |
| response time (ms), 99th percentile | 1949 | 2257 | +15.8% | +89.0433 to +525.9235 | yes: LOSS |
| time over the response line (% of samples) | 17.32 | 17.71 | +2.2% | −0.4493 to +1.2242 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10 | +7.5% | −0.1294 to +1.5294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 98.6 | +98.600 (native is 0) | +36.4682 to +160.7318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.76 | 12.35 | +14.8% | −1.0460 to +4.2293 | no |
| utilisation (used / allocatable) | 0.06312 | 0.07327 | +16.1% | +0.0001 to +0.0202 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.515 | 1.512 | −0.2% | −0.0198 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0 | 0.07354 | +0.074 (native is 0) | +0.0677 to +0.0794 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.515 | 1.586 | +4.7% | +0.0499 to +0.0923 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.7 | 397.5 | −9.6% | −81.4169 to −3.0108 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.337 | +15.5% | +0.0388 to +0.5897 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.3 | +725.0% | +0.6018 to +5.1982 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.383 | +245.8% | +0.0124 to +1.9542 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.96 | 46.3 | +7.8% | +2.9794 to +3.6950 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.3 | 811.3 | +1.2% | +2.4675 to +17.5325 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.679 | −22.0% | −2.3492 to −0.2937 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05417 | +8.3% | −0.0315 to +0.0398 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 116.2 | +9.9% | +3.0646 to +17.7938 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.236 | −12.7% | −1.4291 to −0.0984 | yes: GAIN |
| node-hours | 2.511 | 2.196 | −12.5% | −0.5920 to −0.0376 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.9 | +0.3% | −0.4995 to +2.0232 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 249.9 | −8.5% | −43.7840 to −2.7631 | yes: GAIN |
| response time (ms), mean | 416.7 | 384.5 | −7.7% | −42.3544 to −22.0055 | yes: GAIN |
| response time (ms), 95th percentile | 1549 | 1578 | +1.9% | −15.6648 to +75.2358 | no |
| response time (ms), 99th percentile | 2202 | 2257 | +2.5% | −2.2632 to +112.6880 | no |
| time over the response line (% of samples) | 17.7 | 17.71 | +0.1% | −0.5343 to +0.5614 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10 | +1.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 98.6 | +98.600 (native is 0) | +36.4682 to +160.7318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 12.35 | +9.9% | −1.4976 to +3.7243 | no |
| utilisation (used / allocatable) | 0.06282 | 0.07327 | +16.6% | −0.0004 to +0.0213 | no |
| CPU used (cores), mean | 1.508 | 1.512 | +0.3% | −0.0230 to +0.0325 | no |
| Omni's own CPU (cores), mean | 0 | 0.07354 | +0.074 (native is 0) | +0.0677 to +0.0794 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.508 | 1.586 | +5.2% | +0.0506 to +0.1059 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.8 | 397.5 | −10.2% | −92.4695 to +1.7946 | no |
| HPA replicas, mean | 2.035 | 2.337 | +14.9% | +0.0367 to +0.5677 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.2856 to +2.3144 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.3 | +1000.0% | +0.3236 to +5.6764 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.383 | +361.1% | +0.0482 to +2.1185 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.82 | 46.3 | +5.6% | +2.0348 to +2.9151 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.4 | 811.3 | +0.2% | −0.6335 to +4.4335 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.679 | −22.0% | −2.3492 to −0.2937 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.05417 | −70.5% | −0.1787 to −0.0796 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.3 | −66.7% | −0.9694 to −0.2306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 112.1 | 116.2 | +3.6% | −0.7355 to +8.8438 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.08 | −15.3% | −1.6452 to −0.1949 | yes: GAIN |
| node-hours | 2.515 | 2.13 | −15.3% | −0.6880 to −0.0814 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.7 | +0.1% | −0.5880 to +0.8726 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 244.8 | −10.5% | −51.6837 to −5.8151 | yes: GAIN |
| response time (ms), mean | 395.9 | 402.9 | +1.8% | −19.0289 to +32.9672 | no |
| response time (ms), 95th percentile | 1428 | 1674 | +17.2% | +74.9897 to +416.8243 | yes: LOSS |
| response time (ms), 99th percentile | 1949 | 2427 | +24.5% | +104.5580 to +850.7232 | yes: LOSS |
| time over the response line (% of samples) | 17.32 | 17.77 | +2.6% | −0.2088 to +1.0983 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.5 | +12.9% | +0.1997 to +2.2003 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 | +101.300 (native is 0) | +38.0026 to +164.5974 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.76 | 14.54 | +35.1% | +0.4075 to +7.1425 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06312 | 0.07514 | +19.0% | +0.0025 to +0.0215 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.515 | 1.513 | −0.1% | −0.0339 to +0.0300 | no |
| Omni's own CPU (cores), mean | 0 | 0.07564 | +0.076 (native is 0) | +0.0687 to +0.0826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.515 | 1.589 | +4.9% | +0.0372 to +0.1102 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.7 | 387.9 | −11.8% | −90.2583 to −13.4429 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.314 | +14.4% | +0.0568 to +0.5248 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | −0.0663 to +2.0663 | no |
| pod start wait, total (s) | 0.4 | 2.9 | +625.0% | −0.2857 to +5.2857 | no |
| pod start wait, mean (s) | 0.4 | 1.183 | +195.8% | −0.4646 to +2.0312 | no |
| host CPU busy, the real machine under kind (%) | 42.96 | 47.11 | +9.7% | +3.6180 to +4.6914 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.3 | 820 | +2.3% | +4.5294 to +32.8706 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 | −27.3% | −2.8108 to −0.4706 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.3167 | +533.3% | +0.0644 to +0.4689 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.0214 to +1.3786 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 123.5 | +16.8% | +5.0237 to +30.6013 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*