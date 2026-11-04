# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.989 | 4.634 |
| node-hours | 2.515 | 2.514 | 2.088 | 1.944 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 | 272.7 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 273 | 240.9 | 230 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 357.8 | 306.3 | 345.6 | 292.1 |
| response time (ms), 95th percentile | 1282 | 1216 | 1418 | 1322 |
| response time (ms), 99th percentile | 1777 | 1848 | 1923 | 1960 |
| time over the response line (% of samples) | 14.44 | 10.51 | 14.35 | 10.24 |
| failed requests (%) | 0 | 0 | 0.01117 | 0.03448 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6 | 8.6 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 128.4 | 137 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 17.3 | 13.24 | 22.32 |
| utilisation (used / allocatable) | 0.06093 | 0.06178 | 0.07613 | 0.08017 |
| CPU used (cores), mean | 1.462 | 1.483 | 1.47 | 1.463 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06813 | 0.07356 |
| CPU used with Omni's own (cores), mean | 1.462 | 1.483 | 1.538 | 1.536 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.2 | 450.4 | 394.3 | 376.6 |
| HPA replicas, mean | 1.978 | 2.018 | 2.356 | 2.212 |
| pods started | 0 | 0 | 1.5 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 4.1 | 1.1 |
| pod start wait, mean (s) | 0 | 0 | 1.508 | 0.5 |
| host CPU busy, the real machine under kind (%) | 41.83 | 43.07 | 44.98 | 45.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 793.2 | 804.8 | 801.9 | 814.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.418 | 3.773 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.7833 | 0.2542 | 0.8292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | 1 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 99.18 | 115.3 | 107.3 | 123.4 |
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
| worker nodes in service, mean | 6 | 4.634 | −22.8% | −2.2325 to −0.4988 | yes: GAIN |
| node-hours | 2.514 | 1.944 | −22.7% | −0.9339 to −0.2069 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −0.8152 to +0.6630 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 230 | −15.8% | −70.7398 to −15.3207 | yes: GAIN |
| response time (ms), mean | 306.3 | 292.1 | −4.6% | −39.0538 to +10.6449 | no |
| response time (ms), 95th percentile | 1216 | 1322 | +8.7% | −33.9351 to +246.4361 | no |
| response time (ms), 99th percentile | 1848 | 1960 | +6.1% | +2.0131 to +222.5627 | yes: LOSS |
| time over the response line (% of samples) | 10.51 | 10.24 | −2.5% | −2.0125 to +1.4769 | no |
| failed requests (%) | 0 | 0.03448 | +0.034 (native is 0) | −0.0435 to +0.1125 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.3 | +5.0% | −0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137 | +137.000 (native is 0) | +62.9673 to +211.0327 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 22.32 | +29.0% | +0.1706 to +9.8594 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06178 | 0.08017 | +29.8% | +0.0070 to +0.0297 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.483 | 1.463 | −1.4% | −0.0643 to +0.0243 | no |
| Omni's own CPU (cores), mean | 0 | 0.07356 | +0.074 (native is 0) | +0.0667 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.483 | 1.536 | +3.6% | +0.0039 to +0.1032 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.4 | 376.6 | −16.4% | −117.9061 to −29.7363 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.018 | 2.212 | +9.7% | −0.0637 to +0.4533 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.9358 to +3.1358 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 43.07 | 45.87 | +6.5% | +2.2684 to +3.3405 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.8 | 814.5 | +1.2% | +2.0995 to +17.3005 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.773 | −37.1% | −3.4872 to −0.9673 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.8292 | +5.9% | −0.1387 to +0.2303 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.9 | +26.7% | −0.5048 to +1.3048 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 123.4 | +7.0% | −0.0054 to +16.1304 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.514 | −0.0% | −0.0067 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 | +0.1% | −0.3501 to +0.7563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 273 | +0.1% | −0.3501 to +0.7563 | no |
| response time (ms), mean | 357.8 | 306.3 | −14.4% | −90.5222 to −12.4815 | yes: GAIN |
| response time (ms), 95th percentile | 1282 | 1216 | −5.2% | −186.7242 to +54.2622 | no |
| response time (ms), 99th percentile | 1777 | 1848 | +4.0% | −178.1818 to +320.9026 | no |
| time over the response line (% of samples) | 14.44 | 10.51 | −27.2% | −6.9289 to −0.9292 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6 | −22.1% | −3.5485 to +0.1485 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 17.3 | +49.2% | +0.7904 to +10.6196 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06093 | 0.06178 | +1.4% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.462 | 1.483 | +1.4% | +0.0033 to +0.0378 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.462 | 1.483 | +1.4% | +0.0033 to +0.0378 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.2 | 450.4 | −1.3% | −10.3313 to −1.1493 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.018 | +2.0% | −0.0617 to +0.1407 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.83 | 43.07 | +2.9% | +0.7204 to +1.7449 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.2 | 804.8 | +1.5% | +0.3900 to +22.8100 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.7833 | +944.4% | +0.5827 to +0.8340 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | +275.0% | +0.8738 to +1.3262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 99.18 | 115.3 | +16.3% | +1.2708 to +31.0042 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.989 | −16.8% | −1.9307 to −0.0908 | yes: GAIN |
| node-hours | 2.515 | 2.088 | −17.0% | −0.8089 to −0.0440 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.7 | −0.0% | −1.0236 to +0.7689 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 240.9 | −11.7% | −60.7544 to −2.9128 | yes: GAIN |
| response time (ms), mean | 357.8 | 345.6 | −3.4% | −27.2935 to +2.8368 | no |
| response time (ms), 95th percentile | 1282 | 1418 | +10.7% | −1.2957 to +274.4077 | no |
| response time (ms), 99th percentile | 1777 | 1923 | +8.3% | −1.2303 to +294.8907 | no |
| time over the response line (% of samples) | 14.44 | 14.35 | −0.6% | −0.8480 to +0.6731 | no |
| failed requests (%) | 0 | 0.01117 | +0.011 (native is 0) | −0.0141 to +0.0364 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.6 | +11.7% | −0.1366 to +1.9366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.4 | +128.400 (native is 0) | +64.1415 to +192.6585 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 13.24 | +14.1% | −0.8476 to +4.1276 | no |
| utilisation (used / allocatable) | 0.06093 | 0.07613 | +24.9% | +0.0020 to +0.0284 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.462 | 1.47 | +0.5% | −0.0257 to +0.0415 | no |
| Omni's own CPU (cores), mean | 0 | 0.06813 | +0.068 (native is 0) | +0.0609 to +0.0753 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.538 | +5.2% | +0.0380 to +0.1141 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.2 | 394.3 | −13.6% | −111.9380 to −11.8393 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.356 | +19.1% | +0.0889 to +0.6674 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.4204 to +2.5796 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +0.4926 to +7.7074 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.508 | +1.508 (native is 0) | +0.4849 to +2.5317 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.83 | 44.98 | +7.5% | +2.6206 to +3.6730 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.2 | 801.9 | +1.1% | −0.9090 to +18.3090 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.418 | −26.4% | −2.9088 to −0.2544 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.2542 | +238.9% | −0.2007 to +0.5590 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1 | +150.0% | −0.5285 to +1.7285 | no |
| queue: job turnaround, submitted to done, mean (s) | 99.18 | 107.3 | +8.2% | +0.2528 to +15.9972 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.989 | −16.8% | −1.9307 to −0.0908 | yes: GAIN |
| node-hours | 2.514 | 2.088 | −16.9% | −0.8109 to −0.0412 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.7 | −0.1% | −0.9856 to +0.3247 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 240.9 | −11.7% | −61.1334 to −2.9400 | yes: GAIN |
| response time (ms), mean | 306.3 | 345.6 | +12.8% | −5.9674 to +84.5143 | no |
| response time (ms), 95th percentile | 1216 | 1418 | +16.7% | +40.5993 to +364.9747 | yes: LOSS |
| response time (ms), 99th percentile | 1848 | 1923 | +4.1% | −86.9911 to +237.9307 | no |
| time over the response line (% of samples) | 10.51 | 14.35 | +36.5% | +1.3631 to +6.3200 | yes: LOSS |
| failed requests (%) | 0 | 0.01117 | +0.011 (native is 0) | −0.0141 to +0.0364 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 8.6 | +43.3% | −0.1018 to +5.3018 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.4 | +128.400 (native is 0) | +64.1415 to +192.6585 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 13.24 | −23.5% | −7.6959 to −0.4341 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06178 | 0.07613 | +23.2% | +0.0011 to +0.0276 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.483 | 1.47 | −0.9% | −0.0448 to +0.0195 | no |
| Omni's own CPU (cores), mean | 0 | 0.06813 | +0.068 (native is 0) | +0.0609 to +0.0753 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.483 | 1.538 | +3.7% | +0.0192 to +0.0918 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.4 | 394.3 | −12.5% | −105.8775 to −6.4192 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.018 | 2.356 | +16.8% | +0.0497 to +0.6277 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.4204 to +2.5796 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +0.4926 to +7.7074 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.508 | +1.508 (native is 0) | +0.4849 to +2.5317 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.07 | 44.98 | +4.4% | +1.6036 to +2.2247 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.8 | 801.9 | −0.4% | −8.8509 to +3.0509 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.418 | −26.4% | −2.9088 to −0.2544 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.2542 | −67.6% | −0.8560 to −0.2024 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1 | −33.3% | −1.4079 to +0.4079 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 107.3 | −6.9% | −17.4668 to +1.4418 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.634 | −22.8% | −2.2325 to −0.4988 | yes: GAIN |
| node-hours | 2.515 | 1.944 | −22.7% | −0.9321 to −0.2093 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 | +0.0% | −0.6808 to +0.9349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 230 | −15.7% | −70.4292 to −15.2250 | yes: GAIN |
| response time (ms), mean | 357.8 | 292.1 | −18.4% | −94.9489 to −36.4637 | yes: GAIN |
| response time (ms), 95th percentile | 1282 | 1322 | +3.1% | −103.3168 to +183.3558 | no |
| response time (ms), 99th percentile | 1777 | 1960 | +10.3% | −97.4237 to +464.7203 | no |
| time over the response line (% of samples) | 14.44 | 10.24 | −29.1% | −7.4794 to −0.9143 | yes: GAIN |
| failed requests (%) | 0 | 0.03448 | +0.034 (native is 0) | −0.0435 to +0.1125 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6.3 | −18.2% | −2.8775 to +0.0775 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137 | +137.000 (native is 0) | +62.9673 to +211.0327 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 22.32 | +92.4% | +1.6738 to +19.7662 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06093 | 0.08017 | +31.6% | +0.0080 to +0.0304 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.462 | 1.463 | +0.0% | −0.0470 to +0.0481 | no |
| Omni's own CPU (cores), mean | 0 | 0.07356 | +0.074 (native is 0) | +0.0667 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.536 | +5.1% | +0.0215 to +0.1267 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.2 | 376.6 | −17.4% | −123.8300 to −35.2930 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.212 | +11.8% | −0.0263 to +0.4949 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.9358 to +3.1358 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 41.83 | 45.87 | +9.7% | +3.2802 to +4.7941 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.2 | 814.5 | +2.7% | +4.3390 to +38.2610 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.773 | −37.1% | −3.4872 to −0.9673 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.8292 | +1005.6% | +0.5139 to +0.9944 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | +375.0% | +0.3690 to +2.6310 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 99.18 | 123.4 | +24.4% | +4.4626 to +43.9374 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*