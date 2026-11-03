# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.507 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.1 | 158.5 | 159.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.1 | 158.5 | 159.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 150 | 157.7 | 150.6 | 156.9 |
| response time (ms), 95th percentile | 298.7 | 312.6 | 298.2 | 303.9 |
| response time (ms), 99th percentile | 412.6 | 425.9 | 411.4 | 419.2 |
| time over the response line (% of samples) | 0.3847 | 0.5569 | 0.2439 | 0.4135 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 6.6 | 8.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6667 | 0.08 | 0.4283 | 0.5733 |
| utilisation (used / allocatable) | 0.0381 | 0.04307 | 0.03904 | 0.04469 |
| CPU used (cores), mean | 0.9145 | 1.034 | 0.9369 | 1.073 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03355 | 0.05416 |
| CPU used with Omni's own (cores), mean | 0.9145 | 1.034 | 0.9705 | 1.127 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.7 | 614.5 | 674.5 | 594.6 |
| HPA replicas, mean | 8.975 | 8.981 | 10.48 | 11.07 |
| pods started | 4.5 | 4.6 | 8.3 | 8.7 |
| pod start wait, total (s) | 7.2 | 6.6 | 11.5 | 13.9 |
| pod start wait, mean (s) | 1.6 | 1.415 | 1.357 | 1.595 |
| host CPU busy, the real machine under kind (%) | 27.73 | 32.05 | 29.58 | 34.92 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.509 | −0.4% | −0.0143 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 159.9 | −0.1% | −1.1623 to +0.7018 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 159.9 | −0.1% | −1.1623 to +0.7018 | no |
| response time (ms), mean | 157.7 | 156.9 | −0.5% | −3.6199 to +2.0392 | no |
| response time (ms), 95th percentile | 312.6 | 303.9 | −2.8% | −22.7988 to +5.4718 | no |
| response time (ms), 99th percentile | 425.9 | 419.2 | −1.6% | −31.7434 to +18.3302 | no |
| time over the response line (% of samples) | 0.5569 | 0.4135 | −25.8% | −0.3866 to +0.0998 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.5 | +8.500 (native is 0) | +5.7971 to +11.2029 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.5733 | +616.7% | +0.1878 to +0.7988 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04307 | 0.04469 | +3.8% | +0.0007 to +0.0025 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.034 | 1.073 | +3.8% | +0.0171 to +0.0606 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05416 | +0.054 (native is 0) | +0.0491 to +0.0592 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.034 | 1.127 | +9.0% | +0.0669 to +0.1192 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 614.5 | 594.6 | −3.3% | −31.6312 to −8.3254 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.981 | 11.07 | +23.3% | +1.1856 to +2.9919 | yes: power given |
| pods started | 4.6 | 8.7 | +89.1% | +2.3658 to +5.8342 | yes: power given |
| pod start wait, total (s) | 6.6 | 13.9 | +110.6% | +4.2270 to +10.3730 | yes: LOSS |
| pod start wait, mean (s) | 1.415 | 1.595 | +12.7% | −0.0519 to +0.4127 | no |
| host CPU busy, the real machine under kind (%) | 32.05 | 34.92 | +8.9% | +2.1484 to +3.5793 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0099 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.1 | +0.7% | +0.0947 to +2.1896 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.1 | +0.7% | +0.0947 to +2.1896 | yes: power given |
| response time (ms), mean | 150 | 157.7 | +5.2% | +3.6448 to +11.9021 | yes: LOSS |
| response time (ms), 95th percentile | 298.7 | 312.6 | +4.7% | +1.7336 to +26.1334 | yes: LOSS |
| response time (ms), 99th percentile | 412.6 | 425.9 | +3.2% | −21.9971 to +48.4613 | no |
| time over the response line (% of samples) | 0.3847 | 0.5569 | +44.8% | −0.1883 to +0.5327 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6667 | 0.08 | −88.0% | −0.9772 to −0.1961 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0381 | 0.04307 | +13.0% | +0.0044 to +0.0055 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9145 | 1.034 | +13.0% | +0.1064 to +0.1320 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9145 | 1.034 | +13.0% | +0.1064 to +0.1320 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.7 | 614.5 | −10.9% | −83.2123 to −67.0726 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.975 | 8.981 | +0.1% | −0.1994 to +0.2120 | no |
| pods started | 4.5 | 4.6 | +2.2% | −0.8802 to +1.0802 | no |
| pod start wait, total (s) | 7.2 | 6.6 | −8.3% | −2.5720 to +1.3720 | no |
| pod start wait, mean (s) | 1.6 | 1.415 | −11.6% | −0.4828 to +0.1128 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 32.05 | +15.6% | +3.9330 to +4.7253 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.507 | −0.5% | −0.0166 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −1.5016 to +0.5186 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −1.5016 to +0.5186 | no |
| response time (ms), mean | 150 | 150.6 | +0.4% | −1.6388 to +2.9595 | no |
| response time (ms), 95th percentile | 298.7 | 298.2 | −0.2% | −9.8421 to +8.8101 | no |
| response time (ms), 99th percentile | 412.6 | 411.4 | −0.3% | −32.6780 to +30.2238 | no |
| time over the response line (% of samples) | 0.3847 | 0.2439 | −36.6% | −0.3946 to +0.1131 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.6 | +6.600 (native is 0) | +5.1615 to +8.0385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6667 | 0.4283 | −35.8% | −0.6147 to +0.1380 | no |
| utilisation (used / allocatable) | 0.0381 | 0.03904 | +2.5% | +0.0002 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9145 | 0.9369 | +2.5% | +0.0060 to +0.0389 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03355 | +0.034 (native is 0) | +0.0310 to +0.0361 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9145 | 0.9705 | +6.1% | +0.0378 to +0.0742 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.7 | 674.5 | −2.2% | −26.9426 to −3.4614 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.975 | 10.48 | +16.8% | +0.9070 to +2.1053 | yes: power given |
| pods started | 4.5 | 8.3 | +84.4% | +1.7544 to +5.8456 | yes: power given |
| pod start wait, total (s) | 7.2 | 11.5 | +59.7% | +1.0125 to +7.5875 | yes: LOSS |
| pod start wait, mean (s) | 1.6 | 1.357 | −15.2% | −0.5475 to +0.0614 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 29.58 | +6.7% | +1.3872 to +2.3309 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.507 | −0.5% | −0.0155 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 158.5 | −1.0% | −2.5172 to −0.7501 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 158.5 | −1.0% | −2.5172 to −0.7501 | yes: GAIN |
| response time (ms), mean | 157.7 | 150.6 | −4.5% | −10.9446 to −3.2815 | yes: GAIN |
| response time (ms), 95th percentile | 312.6 | 298.2 | −4.6% | −25.0832 to −3.8158 | yes: GAIN |
| response time (ms), 99th percentile | 425.9 | 411.4 | −3.4% | −32.3852 to +3.4668 | no |
| time over the response line (% of samples) | 0.5569 | 0.2439 | −56.2% | −0.5162 to −0.1097 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.6 | +6.600 (native is 0) | +5.1615 to +8.0385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.4283 | +435.4% | +0.1119 to +0.5847 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04307 | 0.03904 | −9.4% | −0.0045 to −0.0036 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.034 | 0.9369 | −9.4% | −0.1072 to −0.0863 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03355 | +0.034 (native is 0) | +0.0310 to +0.0361 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.034 | 0.9705 | −6.1% | −0.0743 to −0.0521 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 614.5 | 674.5 | +9.8% | +52.1516 to +67.7293 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.981 | 10.48 | +16.7% | +0.9068 to +2.0929 | yes: power given |
| pods started | 4.6 | 8.3 | +80.4% | +1.6754 to +5.7246 | yes: power given |
| pod start wait, total (s) | 6.6 | 11.5 | +74.2% | +1.3084 to +8.4916 | yes: LOSS |
| pod start wait, mean (s) | 1.415 | 1.357 | −4.1% | −0.3254 to +0.2092 | no |
| host CPU busy, the real machine under kind (%) | 32.05 | 29.58 | −7.7% | −2.7467 to −2.1935 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.509 | −0.3% | −0.0144 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.9 | +0.6% | −0.0691 to +1.8929 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.9 | +0.6% | −0.0691 to +1.8929 | no |
| response time (ms), mean | 150 | 156.9 | +4.7% | +3.2658 to +10.7003 | yes: LOSS |
| response time (ms), 95th percentile | 298.7 | 303.9 | +1.8% | −10.2476 to +20.7876 | no |
| response time (ms), 99th percentile | 412.6 | 419.2 | +1.6% | −23.8309 to +36.8819 | no |
| time over the response line (% of samples) | 0.3847 | 0.4135 | +7.5% | −0.2232 to +0.2808 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.5 | +8.500 (native is 0) | +5.7971 to +11.2029 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6667 | 0.5733 | −14.0% | −0.6685 to +0.4819 | no |
| utilisation (used / allocatable) | 0.0381 | 0.04469 | +17.3% | +0.0054 to +0.0078 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9145 | 1.073 | +17.3% | +0.1294 to +0.1868 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05416 | +0.054 (native is 0) | +0.0491 to +0.0592 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9145 | 1.127 | +23.2% | +0.1788 to +0.2457 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.7 | 594.6 | −13.8% | −109.4781 to −80.7634 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.975 | 11.07 | +23.3% | +1.1960 to +2.9941 | yes: power given |
| pods started | 4.5 | 8.7 | +93.3% | +2.4221 to +5.9779 | yes: power given |
| pod start wait, total (s) | 7.2 | 13.9 | +93.1% | +3.1949 to +10.2051 | yes: LOSS |
| pod start wait, mean (s) | 1.6 | 1.595 | −0.3% | −0.3361 to +0.3268 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 34.92 | +25.9% | +6.1414 to +8.2446 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*