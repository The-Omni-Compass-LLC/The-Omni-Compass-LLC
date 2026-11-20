# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.509 | 1.51 | 1.511 | 1.51 | 1.511 | 1.511 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.5 | 157.6 | 157.6 | 157.6 | 157.7 | 157.9 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.5 | 157.6 | 157.6 | 157.6 | 157.7 | 157.9 | 158 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 128.6 | 70.4 | 70.42 | 70.04 | 70.32 | 70.55 | 70.43 | 71.52 |
| response time (ms), 95th percentile | 283.1 | 104.9 | 104.5 | 102.9 | 102.8 | 104 | 102.8 | 106.3 |
| response time (ms), 99th percentile | 452.2 | 143.8 | 140.4 | 137.1 | 141.4 | 140.8 | 140.7 | 145.1 |
| time over the response line (% of samples) | 1.36 | 0 | 0 | 0 | 0.01212 | 0 | 0.02424 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | 16.7 | 17.6 | 14.1 | 15.3 | 17.8 | 20.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | nan | 80 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.2183 | 0.2133 | 0.2633 | 0.185 | 0.185 | 0.135 | 0.11 |
| utilisation (used / allocatable) | 0.03458 | 0.03329 | 0.03342 | 0.03359 | 0.03348 | 0.03367 | 0.03334 | 0.03382 |
| CPU used (cores), mean | 0.8298 | 0.7989 | 0.802 | 0.8062 | 0.8034 | 0.8081 | 0.8002 | 0.8117 |
| Omni's own CPU (cores), mean | 0 | 0.03459 | 0.00605 | 0.00667 | 0.00706 | 0.01364 | 0.02447 | 0.06702 |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8335 | 0.8081 | 0.8128 | 0.8105 | 0.8218 | 0.8246 | 0.8787 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 849.3 | 837.4 | 834.6 | 840.3 | 834 | 845.9 | 833 |
| HPA replicas, mean | 8.005 | 8.177 | 8.047 | 7.739 | 6.768 | 7.213 | 8.16 | 8.417 |
| pods started | 5.1 | 4.4 | 4.7 | 4.4 | 3.2 | 3.3 | 4 | 5.1 |
| pod start wait, total (s) | 6.9 | 6.4 | 6.9 | 6.6 | 4.3 | 4.7 | 5.6 | 7.3 |
| pod start wait, mean (s) | 1.387 | 1.49 | 1.373 | 1.56 | 1.308 | 1.51 | 1.546 | 1.367 |
| host CPU busy, the real machine under kind (%) | 25.71 | 26.15 | 25.21 | 25.27 | 25.22 | 25.52 | 25.94 | 27.55 |
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
| node-hours | 1.509 | 1.51 | +0.0% | −0.0013 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.5 | −0.1% | −0.4880 to +0.0462 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.5 | −0.1% | −0.4880 to +0.0462 | no |
| response time (ms), mean | 128.6 | 70.4 | −45.2% | −83.6613 to −32.6894 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 104.9 | −62.9% | −242.1200 to −114.1150 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 143.8 | −68.2% | −424.1659 to −192.5535 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0 | −100.0% | −2.6234 to −0.0968 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.600 (native is 0) | +17.4222 to +19.7778 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.2183 | +20.2% | −0.2244 to +0.2977 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03329 | −3.7% | −0.0022 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8298 | 0.7989 | −3.7% | −0.0523 to −0.0095 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03459 | +0.035 (native is 0) | +0.0289 to +0.0403 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8335 | +0.4% | −0.0136 to +0.0210 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 849.3 | +2.7% | +7.2480 to +37.4477 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.005 | 8.177 | +2.1% | −0.1425 to +0.4849 | no |
| pods started | 5.1 | 4.4 | −13.7% | −1.5294 to +0.1294 | no |
| pod start wait, total (s) | 6.9 | 6.4 | −7.2% | −2.0174 to +1.0174 | no |
| pod start wait, mean (s) | 1.387 | 1.49 | +7.5% | −0.1162 to +0.3229 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 26.15 | +1.7% | +0.0271 to +0.8648 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.511 | +0.1% | +0.0003 to +0.0030 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 | −0.1% | −0.4788 to +0.2207 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 | −0.1% | −0.4788 to +0.2207 | no |
| response time (ms), mean | 128.6 | 70.42 | −45.2% | −84.4029 to −31.9163 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 104.5 | −63.1% | −244.4526 to −112.7464 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 140.4 | −69.0% | −436.1209 to −187.5487 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0 | −100.0% | −2.6234 to −0.0968 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.7 | +16.700 (native is 0) | +14.9462 to +18.4538 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.2133 | +17.4% | −0.2148 to +0.2781 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03342 | −3.3% | −0.0025 to +0.0002 | no |
| CPU used (cores), mean | 0.8298 | 0.802 | −3.3% | −0.0592 to +0.0036 | no |
| Omni's own CPU (cores), mean | 0 | 0.00605 | +0.006 (native is 0) | +0.0052 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8081 | −2.6% | −0.0525 to +0.0090 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 837.4 | +1.3% | −11.6328 to +32.5809 | no |
| HPA replicas, mean | 8.005 | 8.047 | +0.5% | −0.2726 to +0.3550 | no |
| pods started | 5.1 | 4.7 | −7.8% | −1.9526 to +1.1526 | no |
| pod start wait, total (s) | 6.9 | 6.9 | ±0.0% | −3.4055 to +3.4055 | no |
| pod start wait, mean (s) | 1.387 | 1.373 | −1.0% | −0.3915 to +0.3634 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 25.21 | −1.9% | −1.2284 to +0.2349 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0008 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 | −0.1% | −0.5449 to +0.2581 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 | −0.1% | −0.5449 to +0.2581 | no |
| response time (ms), mean | 128.6 | 70.04 | −45.5% | −84.8389 to −32.2387 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 102.9 | −63.7% | −246.5906 to −113.7524 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 137.1 | −69.7% | −438.5577 to −191.7077 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0 | −100.0% | −2.6234 to −0.0968 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.6 | +17.600 (native is 0) | +15.8093 to +19.3907 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.2633 | +45.0% | −0.2006 to +0.3640 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03359 | −2.9% | −0.0022 to +0.0002 | no |
| CPU used (cores), mean | 0.8298 | 0.8062 | −2.9% | −0.0524 to +0.0051 | no |
| Omni's own CPU (cores), mean | 0 | 0.00667 | +0.007 (native is 0) | +0.0056 to +0.0077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8128 | −2.0% | −0.0449 to +0.0109 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 834.6 | +0.9% | −13.2461 to +28.6182 | no |
| HPA replicas, mean | 8.005 | 7.739 | −3.3% | −0.8137 to +0.2809 | no |
| pods started | 5.1 | 4.4 | −13.7% | −1.9181 to +0.5181 | no |
| pod start wait, total (s) | 6.9 | 6.6 | −4.3% | −2.9986 to +2.3986 | no |
| pod start wait, mean (s) | 1.387 | 1.56 | +12.5% | −0.2247 to +0.5713 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 25.27 | −1.7% | −1.2171 to +0.3441 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.511 | +0.1% | −0.0006 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 | −0.1% | −0.4639 to +0.1850 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 | −0.1% | −0.4639 to +0.1850 | no |
| response time (ms), mean | 128.6 | 70.32 | −45.3% | −84.4833 to −32.0352 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 102.8 | −63.7% | −246.4098 to −114.0222 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 141.4 | −68.7% | −432.3173 to −189.2367 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0.01212 | −99.1% | −2.6018 to −0.0942 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.100 (native is 0) | +10.7373 to +17.4627 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.185 | +1.8% | −0.2785 to +0.2852 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03348 | −3.2% | −0.0021 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8298 | 0.8034 | −3.2% | −0.0513 to −0.0015 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00706 | +0.007 (native is 0) | +0.0057 to +0.0084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8105 | −2.3% | −0.0432 to +0.0046 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 840.3 | +1.6% | −3.7689 to +30.3915 | no |
| HPA replicas, mean | 8.005 | 6.768 | −15.5% | −1.9410 to −0.5330 | yes: GAIN |
| pods started | 5.1 | 3.2 | −37.3% | −3.0410 to −0.7590 | yes: GAIN |
| pod start wait, total (s) | 6.9 | 4.3 | −37.7% | −4.8920 to −0.3080 | yes: GAIN |
| pod start wait, mean (s) | 1.387 | 1.308 | −5.6% | −0.4045 to +0.2478 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 25.22 | −1.9% | −1.1124 to +0.1314 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.511 | +0.1% | −0.0003 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.7 | −0.0% | −0.4716 to +0.4568 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.7 | −0.0% | −0.4716 to +0.4568 | no |
| response time (ms), mean | 128.6 | 70.55 | −45.1% | −84.2971 to −31.7496 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 104 | −63.3% | −245.3329 to −112.8711 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 140.8 | −68.9% | −434.6215 to −188.0977 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0 | −100.0% | −2.6234 to −0.0968 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.3 | +15.300 (native is 0) | +12.3594 to +18.2406 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.185 | +1.8% | −0.2326 to +0.2393 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03367 | −2.6% | −0.0022 to +0.0004 | no |
| CPU used (cores), mean | 0.8298 | 0.8081 | −2.6% | −0.0520 to +0.0087 | no |
| Omni's own CPU (cores), mean | 0 | 0.01364 | +0.014 (native is 0) | +0.0113 to +0.0160 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8218 | −1.0% | −0.0368 to +0.0207 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 834 | +0.9% | −16.9602 to +31.1807 | no |
| HPA replicas, mean | 8.005 | 7.213 | −9.9% | −1.5195 to −0.0662 | yes: GAIN |
| pods started | 5.1 | 3.3 | −35.3% | −2.7417 to −0.8583 | yes: GAIN |
| pod start wait, total (s) | 6.9 | 4.7 | −31.9% | −4.3004 to −0.0996 | yes: GAIN |
| pod start wait, mean (s) | 1.387 | 1.51 | +8.9% | −0.1964 to +0.4430 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 25.52 | −0.7% | −0.9563 to +0.5745 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.514 | +0.3% | +0.0000 to +0.0100 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.9 | +0.1% | −0.3583 to +0.7397 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.9 | +0.1% | −0.3583 to +0.7397 | no |
| response time (ms), mean | 128.6 | 70.43 | −45.2% | −83.9460 to −32.3429 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 102.8 | −63.7% | −245.7762 to −114.6688 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 140.7 | −68.9% | −431.1632 to −191.8084 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0.02424 | −98.2% | −2.5700 to −0.1018 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +15.8688 to +19.7312 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.135 | −25.7% | −0.3237 to +0.2304 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03334 | −3.6% | −0.0024 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8298 | 0.8002 | −3.6% | −0.0573 to −0.0020 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02447 | +0.024 (native is 0) | +0.0206 to +0.0284 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8246 | −0.6% | −0.0306 to +0.0202 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 845.9 | +2.3% | −13.7800 to +51.7420 | no |
| HPA replicas, mean | 8.005 | 8.16 | +1.9% | −0.2698 to +0.5794 | no |
| pods started | 5.1 | 4 | −21.6% | −2.5484 to +0.3484 | no |
| pod start wait, total (s) | 6.9 | 5.6 | −18.8% | −3.8912 to +1.2912 | no |
| pod start wait, mean (s) | 1.387 | 1.546 | +11.5% | −0.1735 to +0.4925 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 25.94 | +0.9% | −0.5812 to +1.0462 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.514 | +0.3% | −0.0012 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 158 | +0.2% | −0.3689 to +0.8861 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 158 | +0.2% | −0.3689 to +0.8861 | no |
| response time (ms), mean | 128.6 | 71.52 | −44.4% | −82.0806 to −32.0294 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 106.3 | −62.5% | −240.5011 to −113.0689 | yes: GAIN |
| response time (ms), 99th percentile | 452.2 | 145.1 | −67.9% | −418.6227 to −195.6297 | yes: GAIN |
| time over the response line (% of samples) | 1.36 | 0.01212 | −99.1% | −2.6018 to −0.0942 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1526 to −0.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 | +20.600 (native is 0) | +18.2109 to +22.9891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1817 | 0.11 | −39.4% | −0.3812 to +0.2379 | no |
| utilisation (used / allocatable) | 0.03458 | 0.03382 | −2.2% | −0.0017 to +0.0002 | no |
| CPU used (cores), mean | 0.8298 | 0.8117 | −2.2% | −0.0413 to +0.0050 | no |
| Omni's own CPU (cores), mean | 0 | 0.06702 | +0.067 (native is 0) | +0.0554 to +0.0787 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8298 | 0.8787 | +5.9% | +0.0317 to +0.0660 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 833 | +0.7% | −13.0531 to +25.2253 | no |
| HPA replicas, mean | 8.005 | 8.417 | +5.1% | +0.0610 to +0.7616 | yes: power given |
| pods started | 5.1 | 5.1 | ±0.0% | −1.3060 to +1.3060 | no |
| pod start wait, total (s) | 6.9 | 7.3 | +5.8% | −2.3642 to +3.1642 | no |
| pod start wait, mean (s) | 1.387 | 1.367 | −1.4% | −0.3951 to +0.3551 | no |
| host CPU busy, the real machine under kind (%) | 25.71 | 27.55 | +7.2% | +1.3655 to +2.3256 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.511 | +0.1% | −0.0008 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 157.6 | +0.1% | −0.2323 to +0.4160 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 157.6 | +0.1% | −0.2323 to +0.4160 | no |
| response time (ms), mean | 70.4 | 70.42 | +0.0% | −1.2183 to +1.2499 | no |
| response time (ms), 95th percentile | 104.9 | 104.5 | −0.5% | −3.2913 to +2.3273 | no |
| response time (ms), 99th percentile | 143.8 | 140.4 | −2.4% | −17.6296 to +10.6794 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 16.7 | −10.2% | −4.3187 to +0.5187 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.2133 | −2.3% | −0.2061 to +0.1961 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03342 | +0.4% | −0.0007 to +0.0010 | no |
| CPU used (cores), mean | 0.7989 | 0.802 | +0.4% | −0.0167 to +0.0230 | no |
| Omni's own CPU (cores), mean | 0.03459 | 0.00605 | −82.5% | −0.0334 to −0.0237 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8081 | −3.0% | −0.0481 to −0.0027 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 837.4 | −1.4% | −36.2478 to +12.5002 | no |
| HPA replicas, mean | 8.177 | 8.047 | −1.6% | −0.5530 to +0.2929 | no |
| pods started | 4.4 | 4.7 | +6.8% | −1.1717 to +1.7717 | no |
| pod start wait, total (s) | 6.4 | 6.9 | +7.8% | −2.8424 to +3.8424 | no |
| pod start wait, mean (s) | 1.49 | 1.373 | −7.9% | −0.4521 to +0.2173 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.21 | −3.6% | −1.4933 to −0.3922 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.51 | +0.0% | −0.0020 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 157.6 | +0.0% | −0.2437 to +0.3988 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 157.6 | +0.0% | −0.2437 to +0.3988 | no |
| response time (ms), mean | 70.4 | 70.04 | −0.5% | −1.8182 to +1.0912 | no |
| response time (ms), 95th percentile | 104.9 | 102.9 | −2.0% | −5.3206 to +1.2126 | no |
| response time (ms), 99th percentile | 143.8 | 137.1 | −4.7% | −20.0061 to +6.4601 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 17.6 | −5.4% | −2.7194 to +0.7194 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.2633 | +20.6% | −0.1706 to +0.2606 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03359 | +0.9% | −0.0001 to +0.0007 | no |
| CPU used (cores), mean | 0.7989 | 0.8062 | +0.9% | −0.0031 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0.03459 | 0.00667 | −80.7% | −0.0326 to −0.0233 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8128 | −2.5% | −0.0350 to −0.0064 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 834.6 | −1.7% | −29.4719 to +0.1484 | no |
| HPA replicas, mean | 8.177 | 7.739 | −5.4% | −1.0057 to +0.1305 | no |
| pods started | 4.4 | 4.4 | ±0.0% | −0.8921 to +0.8921 | no |
| pod start wait, total (s) | 6.4 | 6.6 | +3.1% | −2.2962 to +2.6962 | no |
| pod start wait, mean (s) | 1.49 | 1.56 | +4.7% | −0.2809 to +0.4209 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.27 | −3.4% | −1.4066 to −0.3583 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.0% | −0.0016 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 157.6 | +0.1% | −0.2242 to +0.3871 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 157.6 | +0.1% | −0.2242 to +0.3871 | no |
| response time (ms), mean | 70.4 | 70.32 | −0.1% | −1.5054 to +1.3377 | no |
| response time (ms), 95th percentile | 104.9 | 102.8 | −2.0% | −5.1048 to +0.9078 | no |
| response time (ms), 99th percentile | 143.8 | 141.4 | −1.7% | −11.9271 to +7.0925 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 14.1 | −24.2% | −8.1200 to −0.8800 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.185 | −15.3% | −0.2441 to +0.1774 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03348 | +0.6% | −0.0005 to +0.0009 | no |
| CPU used (cores), mean | 0.7989 | 0.8034 | +0.6% | −0.0115 to +0.0205 | no |
| Omni's own CPU (cores), mean | 0.03459 | 0.00706 | −79.6% | −0.0319 to −0.0231 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8105 | −2.8% | −0.0406 to −0.0055 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 840.3 | −1.1% | −28.1488 to +10.0756 | no |
| HPA replicas, mean | 8.177 | 6.768 | −17.2% | −1.9579 to −0.8586 | yes: GAIN |
| pods started | 4.4 | 3.2 | −27.3% | −2.8101 to +0.4101 | no |
| pod start wait, total (s) | 6.4 | 4.3 | −32.8% | −4.8071 to +0.6071 | no |
| pod start wait, mean (s) | 1.49 | 1.308 | −12.2% | −0.3788 to +0.0155 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.22 | −3.6% | −1.4702 to −0.4027 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.1% | −0.0015 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 157.7 | +0.1% | −0.2155 to +0.6426 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 157.7 | +0.1% | −0.2155 to +0.6426 | no |
| response time (ms), mean | 70.4 | 70.55 | +0.2% | −1.1004 to +1.4043 | no |
| response time (ms), 95th percentile | 104.9 | 104 | −0.9% | −4.4366 to +2.4676 | no |
| response time (ms), 99th percentile | 143.8 | 140.8 | −2.1% | −15.3804 to +9.3806 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 15.3 | −17.7% | −6.5176 to −0.0824 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.185 | −15.3% | −0.2657 to +0.1991 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03367 | +1.2% | −0.0004 to +0.0011 | no |
| CPU used (cores), mean | 0.7989 | 0.8081 | +1.2% | −0.0088 to +0.0273 | no |
| Omni's own CPU (cores), mean | 0.03459 | 0.01364 | −60.6% | −0.0243 to −0.0176 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8218 | −1.4% | −0.0314 to +0.0080 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 834 | −1.8% | −40.6480 to +10.1727 | no |
| HPA replicas, mean | 8.177 | 7.213 | −11.8% | −1.5492 to −0.3790 | yes: GAIN |
| pods started | 4.4 | 3.3 | −25.0% | −2.2410 to +0.0410 | no |
| pod start wait, total (s) | 6.4 | 4.7 | −26.6% | −3.6963 to +0.2963 | no |
| pod start wait, mean (s) | 1.49 | 1.51 | +1.3% | −0.1909 to +0.2309 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.52 | −2.4% | −1.2189 to −0.0548 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.514 | +0.3% | −0.0011 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 157.9 | +0.3% | −0.1487 to +0.9719 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 157.9 | +0.3% | −0.1487 to +0.9719 | no |
| response time (ms), mean | 70.4 | 70.43 | +0.0% | −1.2141 to +1.2758 | no |
| response time (ms), 95th percentile | 104.9 | 102.8 | −2.0% | −4.5095 to +0.2995 | no |
| response time (ms), 99th percentile | 143.8 | 140.7 | −2.2% | −15.6701 to +9.4179 | no |
| time over the response line (% of samples) | 0 | 0.02424 | +0.024 (native is 0) | −0.0123 to +0.0608 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 17.8 | −4.3% | −2.9801 to +1.3801 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 80 | −20.0% | −50.1600 to +10.1600 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.135 | −38.2% | −0.3085 to +0.1418 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03334 | +0.2% | −0.0006 to +0.0007 | no |
| CPU used (cores), mean | 0.7989 | 0.8002 | +0.2% | −0.0154 to +0.0179 | no |
| Omni's own CPU (cores), mean | 0.03459 | 0.02447 | −29.3% | −0.0122 to −0.0080 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8246 | −1.1% | −0.0268 to +0.0090 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 845.9 | −0.4% | −27.3629 to +20.6292 | no |
| HPA replicas, mean | 8.177 | 8.16 | −0.2% | −0.4186 to +0.3857 | no |
| pods started | 4.4 | 4 | −9.1% | −1.7146 to +0.9146 | no |
| pod start wait, total (s) | 6.4 | 5.6 | −12.5% | −3.1068 to +1.5068 | no |
| pod start wait, mean (s) | 1.49 | 1.546 | +3.8% | −0.2266 to +0.3390 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.94 | −0.8% | −0.9273 to +0.5004 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.514 | +0.2% | −0.0022 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.5 | 158 | +0.3% | −0.1506 to +1.1096 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.5 | 158 | +0.3% | −0.1506 to +1.1096 | no |
| response time (ms), mean | 70.4 | 71.52 | +1.6% | +0.3114 to +1.9294 | yes: LOSS |
| response time (ms), 95th percentile | 104.9 | 106.3 | +1.3% | −1.0418 to +3.7068 | no |
| response time (ms), 99th percentile | 143.8 | 145.1 | +0.9% | −10.5370 to +13.0040 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 20.6 | +10.8% | −0.8010 to +4.8010 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 90 | −10.0% | −32.6200 to +12.6200 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.11 | −49.6% | −0.2935 to +0.0768 | no |
| utilisation (used / allocatable) | 0.03329 | 0.03382 | +1.6% | +0.0000 to +0.0011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7989 | 0.8117 | +1.6% | +0.0003 to +0.0252 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03459 | 0.06702 | +93.8% | +0.0262 to +0.0386 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8335 | 0.8787 | +5.4% | +0.0320 to +0.0584 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 849.3 | 833 | −1.9% | −29.8007 to −2.7228 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.177 | 8.417 | +2.9% | −0.1519 to +0.6321 | no |
| pods started | 4.4 | 5.1 | +15.9% | −0.6509 to +2.0509 | no |
| pod start wait, total (s) | 6.4 | 7.3 | +14.1% | −1.8487 to +3.6487 | no |
| pod start wait, mean (s) | 1.49 | 1.367 | −8.3% | −0.5148 to +0.2681 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 27.55 | +5.4% | +0.9264 to +1.8727 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*