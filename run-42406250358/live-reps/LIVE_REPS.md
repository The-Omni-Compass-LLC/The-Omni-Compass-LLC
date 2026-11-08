# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.511 | 1.512 | 1.513 | 1.513 | 1.512 | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.7 | 157.7 | 157.9 | 157.8 | 157.8 | 157.9 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.7 | 157.7 | 157.9 | 157.8 | 157.8 | 157.9 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 134.5 | 72.16 | 71.24 | 71.2 | 71.32 | 70.96 | 71.36 | 73.01 |
| response time (ms), 95th percentile | 304.6 | 106.4 | 104.2 | 104.1 | 104.1 | 104.4 | 105.2 | 107.5 |
| response time (ms), 99th percentile | 483.7 | 146 | 140.7 | 139.5 | 143.4 | 136.3 | 151 | 147.2 |
| time over the response line (% of samples) | 1.721 | 0 | 0.01212 | 0 | 0.03636 | 0 | 0 | 0.02432 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.5 | 15.1 | 15.9 | 16.6 | 15 | 19.2 | 21.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | nan | 100 | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.02667 | 0.16 | 0.1067 | 0.2133 | 0.08 | 0.105 | 0.165 |
| utilisation (used / allocatable) | 0.03509 | 0.03384 | 0.03365 | 0.03367 | 0.03346 | 0.03354 | 0.03398 | 0.03441 |
| CPU used (cores), mean | 0.842 | 0.8121 | 0.8075 | 0.808 | 0.8031 | 0.8049 | 0.8155 | 0.8258 |
| Omni's own CPU (cores), mean | 0 | 0.03486 | 0.00587 | 0.0065 | 0.00727 | 0.01338 | 0.02396 | 0.06618 |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8469 | 0.8134 | 0.8145 | 0.8103 | 0.8183 | 0.8395 | 0.892 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 828.8 | 832.1 | 831.3 | 841.3 | 840.9 | 826.2 | 813.3 |
| HPA replicas, mean | 8.033 | 8.358 | 7.644 | 7.853 | 7.276 | 7.251 | 8.16 | 8.508 |
| pods started | 5.3 | 4.3 | 4.2 | 3.5 | 3.5 | 3.1 | 4.8 | 5 |
| pod start wait, total (s) | 7.8 | 5.6 | 5.3 | 4.4 | 5.4 | 4.5 | 6.4 | 6.7 |
| pod start wait, mean (s) | 1.47 | 1.37 | 1.264 | 1.407 | 1.575 | 1.542 | 1.318 | 1.36 |
| host CPU busy, the real machine under kind (%) | 26 | 26.42 | 25.19 | 25.45 | 25.22 | 25.45 | 26.02 | 27.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.511 | −0.2% | −0.0087 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.7 | −0.4% | −1.1133 to −0.0998 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.7 | −0.4% | −1.1133 to −0.0998 | yes: GAIN |
| response time (ms), mean | 134.5 | 72.16 | −46.4% | −89.2088 to −35.5661 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 106.4 | −65.1% | −272.0249 to −124.3551 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 146 | −69.8% | −464.6520 to −210.6566 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0 | −100.0% | −3.2076 to −0.2339 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.5 | +18.500 (native is 0) | +17.2726 to +19.7274 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.02667 | −91.2% | −0.5972 to +0.0472 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03384 | −3.6% | −0.0022 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.8121 | −3.6% | −0.0538 to −0.0061 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03486 | +0.035 (native is 0) | +0.0288 to +0.0409 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8469 | +0.6% | −0.0144 to +0.0242 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 828.8 | +2.1% | −0.8913 to +35.6252 | no |
| HPA replicas, mean | 8.033 | 8.358 | +4.0% | −0.1220 to +0.7717 | no |
| pods started | 5.3 | 4.3 | −18.9% | −2.1184 to +0.1184 | no |
| pod start wait, total (s) | 7.8 | 5.6 | −28.2% | −4.3539 to −0.0461 | yes: GAIN |
| pod start wait, mean (s) | 1.47 | 1.37 | −6.8% | −0.3929 to +0.1929 | no |
| host CPU busy, the real machine under kind (%) | 26 | 26.42 | +1.6% | −0.0417 to +0.8752 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0035 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.7 | −0.3% | −0.8489 to −0.1837 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.7 | −0.3% | −0.8489 to −0.1837 | yes: GAIN |
| response time (ms), mean | 134.5 | 71.24 | −47.0% | −90.6311 to −35.9739 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 104.2 | −65.8% | −274.8041 to −125.9739 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 140.7 | −70.9% | −475.3191 to −210.6217 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0.01212 | −99.3% | −3.1801 to −0.2371 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.1 | +15.100 (native is 0) | +13.2701 to +16.9299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.16 | −47.0% | −0.4086 to +0.1252 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03365 | −4.1% | −0.0024 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.8075 | −4.1% | −0.0588 to −0.0103 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00587 | +0.006 (native is 0) | +0.0049 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8134 | −3.4% | −0.0520 to −0.0053 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 832.1 | +2.5% | +6.7632 to +34.5071 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.033 | 7.644 | −4.8% | −1.0469 to +0.2686 | no |
| pods started | 5.3 | 4.2 | −20.8% | −2.3818 to +0.1818 | no |
| pod start wait, total (s) | 7.8 | 5.3 | −32.1% | −5.0290 to +0.0290 | no |
| pod start wait, mean (s) | 1.47 | 1.264 | −14.0% | −0.5280 to +0.1165 | no |
| host CPU busy, the real machine under kind (%) | 26 | 25.19 | −3.1% | −1.4093 to −0.2165 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0022 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.2% | −0.6477 to −0.0761 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.2% | −0.6477 to −0.0761 | yes: GAIN |
| response time (ms), mean | 134.5 | 71.2 | −47.1% | −90.3684 to −36.3314 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 104.1 | −65.8% | −274.9283 to −126.1137 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 139.5 | −71.2% | −474.5343 to −213.8531 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0 | −100.0% | −3.2076 to −0.2339 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +14.4129 to +17.3871 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.1067 | −64.6% | −0.5038 to +0.1138 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03367 | −4.0% | −0.0026 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.808 | −4.0% | −0.0625 to −0.0056 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0065 | +0.007 (native is 0) | +0.0054 to +0.0076 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8145 | −3.3% | −0.0551 to +0.0000 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 831.3 | +2.4% | −2.3537 to +41.9873 | no |
| HPA replicas, mean | 8.033 | 7.853 | −2.2% | −0.9310 to +0.5705 | no |
| pods started | 5.3 | 3.5 | −34.0% | −3.1821 to −0.4179 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 4.4 | −43.6% | −5.8362 to −0.9638 | yes: GAIN |
| pod start wait, mean (s) | 1.47 | 1.407 | −4.3% | −0.3739 to +0.2472 | no |
| host CPU busy, the real machine under kind (%) | 26 | 25.45 | −2.1% | −1.1925 to +0.0830 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.1% | −0.0032 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | −0.3% | −0.8325 to −0.0964 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | −0.3% | −0.8325 to −0.0964 | yes: GAIN |
| response time (ms), mean | 134.5 | 71.32 | −47.0% | −90.2643 to −36.1806 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 104.1 | −65.8% | −274.7619 to −126.2971 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 143.4 | −70.4% | −474.6409 to −205.9255 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0.03636 | −97.9% | −3.1515 to −0.2172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.600 (native is 0) | +12.5228 to +20.6772 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.2133 | −29.3% | −0.3820 to +0.2053 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03346 | −4.6% | −0.0026 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.8031 | −4.6% | −0.0618 to −0.0161 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00727 | +0.007 (native is 0) | +0.0058 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8103 | −3.8% | −0.0534 to −0.0100 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 841.3 | +3.7% | +13.4533 to +46.2758 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.033 | 7.276 | −9.4% | −1.4227 to −0.0915 | yes: GAIN |
| pods started | 5.3 | 3.5 | −34.0% | −2.5388 to −1.0612 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.4 | −30.8% | −3.7572 to −1.0428 | yes: GAIN |
| pod start wait, mean (s) | 1.47 | 1.575 | +7.1% | −0.1789 to +0.3889 | no |
| host CPU busy, the real machine under kind (%) | 26 | 25.22 | −3.0% | −1.3168 to −0.2399 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0025 to +0.0002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | −0.3% | −0.7297 to −0.2133 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | −0.3% | −0.7297 to −0.2133 | yes: GAIN |
| response time (ms), mean | 134.5 | 70.96 | −47.3% | −90.6603 to −36.5035 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 104.4 | −65.7% | −274.3040 to −126.0590 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 136.3 | −71.8% | −479.9344 to −214.9426 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0 | −100.0% | −3.2076 to −0.2339 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +11.1850 to +18.8150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.08 | −73.5% | −0.4490 to +0.0057 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03354 | −4.4% | −0.0025 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.8049 | −4.4% | −0.0589 to −0.0154 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01338 | +0.013 (native is 0) | +0.0108 to +0.0159 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8183 | −2.8% | −0.0435 to −0.0041 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 840.9 | +3.6% | +14.3159 to +44.6237 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.033 | 7.251 | −9.7% | −1.6312 to +0.0682 | no |
| pods started | 5.3 | 3.1 | −41.5% | −2.8573 to −1.5427 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 4.5 | −42.3% | −4.7326 to −1.8674 | yes: GAIN |
| pod start wait, mean (s) | 1.47 | 1.542 | +4.9% | −0.2742 to +0.4176 | no |
| host CPU busy, the real machine under kind (%) | 26 | 25.45 | −2.1% | −1.0293 to −0.0726 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0029 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.3% | −0.7089 to −0.0965 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.3% | −0.7089 to −0.0965 | yes: GAIN |
| response time (ms), mean | 134.5 | 71.36 | −47.0% | −90.1053 to −36.2720 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 105.2 | −65.5% | −274.0996 to −124.5984 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 151 | −68.8% | −455.3489 to −209.9833 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0 | −100.0% | −3.2076 to −0.2339 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +17.8179 to +20.5821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.105 | −65.2% | −0.4598 to +0.0665 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03398 | −3.2% | −0.0021 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.842 | 0.8155 | −3.2% | −0.0502 to −0.0028 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02396 | +0.024 (native is 0) | +0.0199 to +0.0280 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.8395 | −0.3% | −0.0233 to +0.0181 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 826.2 | +1.8% | −1.5763 to +31.1411 | no |
| HPA replicas, mean | 8.033 | 8.16 | +1.6% | −0.0639 to +0.3189 | no |
| pods started | 5.3 | 4.8 | −9.4% | −1.5256 to +0.5256 | no |
| pod start wait, total (s) | 7.8 | 6.4 | −17.9% | −4.1642 to +1.3642 | no |
| pod start wait, mean (s) | 1.47 | 1.318 | −10.4% | −0.5906 to +0.2858 | no |
| host CPU busy, the real machine under kind (%) | 26 | 26.02 | +0.1% | −0.4638 to +0.5026 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0024 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.4991 to +0.1213 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.4991 to +0.1213 | no |
| response time (ms), mean | 134.5 | 73.01 | −45.7% | −88.5178 to −34.5585 | yes: GAIN |
| response time (ms), 95th percentile | 304.6 | 107.5 | −64.7% | −271.4058 to −122.8182 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 147.2 | −69.6% | −456.8540 to −216.1032 | yes: GAIN |
| time over the response line (% of samples) | 1.721 | 0.02432 | −98.6% | −3.1690 to −0.2239 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0544 to +0.0544 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.3 | +21.300 (native is 0) | +19.6811 to +22.9189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.165 | −45.3% | −0.5119 to +0.2386 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03441 | −1.9% | −0.0017 to +0.0004 | no |
| CPU used (cores), mean | 0.842 | 0.8258 | −1.9% | −0.0417 to +0.0092 | no |
| Omni's own CPU (cores), mean | 0 | 0.06618 | +0.066 (native is 0) | +0.0547 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 0.892 | +5.9% | +0.0320 to +0.0680 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 811.4 | 813.3 | +0.2% | −22.2288 to +25.9893 | no |
| HPA replicas, mean | 8.033 | 8.508 | +5.9% | +0.0351 to +0.9146 | yes: power given |
| pods started | 5.3 | 5 | −5.7% | −1.4705 to +0.8705 | no |
| pod start wait, total (s) | 7.8 | 6.7 | −14.1% | −2.8986 to +0.6986 | no |
| pod start wait, mean (s) | 1.47 | 1.36 | −7.5% | −0.3254 to +0.1059 | no |
| host CPU busy, the real machine under kind (%) | 26 | 27.79 | +6.9% | +1.4790 to +2.0949 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0042 to +0.0065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.7 | +0.1% | −0.4268 to +0.6073 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.7 | +0.1% | −0.4268 to +0.6073 | no |
| response time (ms), mean | 72.16 | 71.24 | −1.3% | −2.0578 to +0.2278 | no |
| response time (ms), 95th percentile | 106.4 | 104.2 | −2.1% | −4.2816 to −0.1164 | yes: GAIN |
| response time (ms), 99th percentile | 146 | 140.7 | −3.6% | −14.8185 to +4.1863 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 15.1 | −18.4% | −5.4288 to −1.3712 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.16 | +500.0% | −0.0520 to +0.3187 | no |
| utilisation (used / allocatable) | 0.03384 | 0.03365 | −0.6% | −0.0008 to +0.0004 | no |
| CPU used (cores), mean | 0.8121 | 0.8075 | −0.6% | −0.0186 to +0.0095 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.00587 | −83.2% | −0.0341 to −0.0239 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.8134 | −4.0% | −0.0498 to −0.0173 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 832.1 | +0.4% | −16.9360 to +23.4724 | no |
| HPA replicas, mean | 8.358 | 7.644 | −8.5% | −1.3773 to −0.0506 | yes: GAIN |
| pods started | 4.3 | 4.2 | −2.3% | −1.2410 to +1.0410 | no |
| pod start wait, total (s) | 5.6 | 5.3 | −5.4% | −2.2385 to +1.6385 | no |
| pod start wait, mean (s) | 1.37 | 1.264 | −7.7% | −0.3624 to +0.1510 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 25.19 | −4.7% | −1.8061 to −0.6533 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.513 | +0.2% | −0.0027 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.9 | +0.2% | −0.2791 to +0.7684 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.9 | +0.2% | −0.2791 to +0.7684 | no |
| response time (ms), mean | 72.16 | 71.2 | −1.3% | −2.1131 to +0.1882 | no |
| response time (ms), 95th percentile | 106.4 | 104.1 | −2.2% | −4.2805 to −0.3815 | yes: GAIN |
| response time (ms), 99th percentile | 146 | 139.5 | −4.5% | −16.7133 to +3.6345 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 15.9 | −14.1% | −4.5134 to −0.6866 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1067 | +300.0% | −0.0123 to +0.1723 | no |
| utilisation (used / allocatable) | 0.03384 | 0.03367 | −0.5% | −0.0006 to +0.0003 | no |
| CPU used (cores), mean | 0.8121 | 0.808 | −0.5% | −0.0153 to +0.0072 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.0065 | −81.4% | −0.0334 to −0.0233 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.8145 | −3.8% | −0.0469 to −0.0179 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 831.3 | +0.3% | −14.6944 to +19.5941 | no |
| HPA replicas, mean | 8.358 | 7.853 | −6.0% | −1.1187 to +0.1086 | no |
| pods started | 4.3 | 3.5 | −18.6% | −1.9081 to +0.3081 | no |
| pod start wait, total (s) | 5.6 | 4.4 | −21.4% | −3.3539 to +0.9539 | no |
| pod start wait, mean (s) | 1.37 | 1.407 | +2.7% | −0.2708 to +0.3442 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 25.45 | −3.7% | −1.4634 to −0.4797 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.513 | +0.1% | −0.0038 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.8 | +0.1% | −0.4360 to +0.7202 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.8 | +0.1% | −0.4360 to +0.7202 | no |
| response time (ms), mean | 72.16 | 71.32 | −1.2% | −1.8474 to +0.1774 | no |
| response time (ms), 95th percentile | 106.4 | 104.1 | −2.2% | −4.2576 to −0.4214 | yes: GAIN |
| response time (ms), 99th percentile | 146 | 143.4 | −1.8% | −25.0972 to +19.8394 | no |
| time over the response line (% of samples) | 0 | 0.03636 | +0.036 (native is 0) | −0.0459 to +0.1186 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 16.6 | −10.3% | −5.8389 to +2.0389 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.2133 | +700.0% | +0.0597 to +0.3137 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03384 | 0.03346 | −1.1% | −0.0008 to +0.0001 | no |
| CPU used (cores), mean | 0.8121 | 0.8031 | −1.1% | −0.0197 to +0.0017 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.00727 | −79.1% | −0.0323 to −0.0229 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.8103 | −4.3% | −0.0486 to −0.0246 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 841.3 | +1.5% | −6.8758 to +31.8709 | no |
| HPA replicas, mean | 8.358 | 7.276 | −12.9% | −1.5863 to −0.5776 | yes: GAIN |
| pods started | 4.3 | 3.5 | −18.6% | −2.1403 to +0.5403 | no |
| pod start wait, total (s) | 5.6 | 5.4 | −3.6% | −2.0407 to +1.6407 | no |
| pod start wait, mean (s) | 1.37 | 1.575 | +15.0% | −0.1706 to +0.5806 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 25.22 | −4.5% | −1.6913 to −0.6989 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0038 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.8 | +0.1% | −0.4160 to +0.6861 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.8 | +0.1% | −0.4160 to +0.6861 | no |
| response time (ms), mean | 72.16 | 70.96 | −1.7% | −2.5570 to +0.1681 | no |
| response time (ms), 95th percentile | 106.4 | 104.4 | −1.9% | −3.3662 to −0.6168 | yes: GAIN |
| response time (ms), 99th percentile | 146 | 136.3 | −6.7% | −17.8294 to −1.7390 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 15 | −18.9% | −6.9594 to −0.0406 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.08 | +200.0% | −0.0673 to +0.1740 | no |
| utilisation (used / allocatable) | 0.03384 | 0.03354 | −0.9% | −0.0008 to +0.0002 | no |
| CPU used (cores), mean | 0.8121 | 0.8049 | −0.9% | −0.0185 to +0.0041 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.01338 | −61.6% | −0.0251 to −0.0179 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.8183 | −3.4% | −0.0406 to −0.0168 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 840.9 | +1.5% | −4.6043 to +28.8099 | no |
| HPA replicas, mean | 8.358 | 7.251 | −13.2% | −1.7062 to −0.5065 | yes: GAIN |
| pods started | 4.3 | 3.1 | −27.9% | −2.2003 to −0.1997 | yes: GAIN |
| pod start wait, total (s) | 5.6 | 4.5 | −19.6% | −2.8986 to +0.6986 | no |
| pod start wait, mean (s) | 1.37 | 1.542 | +12.5% | −0.1935 to +0.5368 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 25.45 | −3.7% | −1.4742 to −0.4613 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0035 to +0.0071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.9 | +0.1% | −0.2966 to +0.7044 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.9 | +0.1% | −0.2966 to +0.7044 | no |
| response time (ms), mean | 72.16 | 71.36 | −1.1% | −2.0579 to +0.4556 | no |
| response time (ms), 95th percentile | 106.4 | 105.2 | −1.1% | −3.1687 to +0.8507 | no |
| response time (ms), 99th percentile | 146 | 151 | +3.4% | −3.5261 to +13.5025 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 19.2 | +3.8% | −1.4072 to +2.8072 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.105 | +293.8% | −0.0147 to +0.1714 | no |
| utilisation (used / allocatable) | 0.03384 | 0.03398 | +0.4% | −0.0004 to +0.0007 | no |
| CPU used (cores), mean | 0.8121 | 0.8155 | +0.4% | −0.0105 to +0.0174 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.02396 | −31.3% | −0.0131 to −0.0087 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.8395 | −0.9% | −0.0217 to +0.0068 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 826.2 | −0.3% | −22.7934 to +17.6242 | no |
| HPA replicas, mean | 8.358 | 8.16 | −2.4% | −0.5219 to +0.1272 | no |
| pods started | 4.3 | 4.8 | +11.6% | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 5.6 | 6.4 | +14.3% | −1.3539 to +2.9539 | no |
| pod start wait, mean (s) | 1.37 | 1.318 | −3.8% | −0.5085 to +0.4037 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 26.02 | −1.5% | −0.9779 to +0.1831 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.513 | +0.2% | −0.0026 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 158.1 | +0.3% | −0.1321 to +0.9674 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 158.1 | +0.3% | −0.1321 to +0.9674 | no |
| response time (ms), mean | 72.16 | 73.01 | +1.2% | −0.5269 to +2.2256 | no |
| response time (ms), 95th percentile | 106.4 | 107.5 | +1.0% | −1.1776 to +3.3336 | no |
| response time (ms), 99th percentile | 146 | 147.2 | +0.8% | −11.1060 to +13.4574 | no |
| time over the response line (% of samples) | 0 | 0.02432 | +0.024 (native is 0) | −0.0124 to +0.0610 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 21.3 | +15.1% | +1.4179 to +4.1821 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 80 | −20.0% | −50.1600 to +10.1600 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.165 | +518.8% | −0.0033 to +0.2800 | no |
| utilisation (used / allocatable) | 0.03384 | 0.03441 | +1.7% | −0.0001 to +0.0013 | no |
| CPU used (cores), mean | 0.8121 | 0.8258 | +1.7% | −0.0033 to +0.0308 | no |
| Omni's own CPU (cores), mean | 0.03486 | 0.06618 | +89.8% | +0.0258 to +0.0368 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8469 | 0.892 | +5.3% | +0.0269 to +0.0632 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.8 | 813.3 | −1.9% | −39.4952 to +8.5217 | no |
| HPA replicas, mean | 8.358 | 8.508 | +1.8% | −0.3033 to +0.6033 | no |
| pods started | 4.3 | 5 | +16.3% | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 5.6 | 6.7 | +19.6% | −0.1818 to +2.3818 | no |
| pod start wait, mean (s) | 1.37 | 1.36 | −0.7% | −0.3458 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 26.42 | 27.79 | +5.2% | +0.8624 to +1.8779 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*