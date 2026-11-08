# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.509 | 1.511 | 1.511 | 1.512 | 1.509 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | 158 | 158 | 158.1 | 157.7 | 157.9 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | 158 | 158 | 158.1 | 157.7 | 157.9 | 158 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 140.9 | 74.6 | 73.91 | 73.57 | 73.87 | 73.72 | 74.07 | 75.22 |
| response time (ms), 95th percentile | 309.6 | 107 | 105.5 | 104.1 | 105.5 | 105.4 | 105 | 106.2 |
| response time (ms), 99th percentile | 503.2 | 141.2 | 140.4 | 137.3 | 144.9 | 139.5 | 140.1 | 142.9 |
| time over the response line (% of samples) | 1.545 | 0 | 0 | 0 | 0 | 0 | 0.0119 | 0.03593 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | 14.7 | 18.2 | 17.3 | 17 | 19.5 | 20.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | 100 | 90 | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.2383 | 0.1067 | 0.08167 | 0.02667 | 0.025 | 0.1083 | 0.1067 |
| utilisation (used / allocatable) | 0.03657 | 0.03527 | 0.03514 | 0.03497 | 0.03505 | 0.03489 | 0.03498 | 0.0356 |
| CPU used (cores), mean | 0.8776 | 0.8465 | 0.8433 | 0.8393 | 0.8412 | 0.8373 | 0.8396 | 0.8544 |
| Omni's own CPU (cores), mean | 0 | 0.03412 | 0.00559 | 0.00659 | 0.00729 | 0.01331 | 0.02377 | 0.06506 |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8806 | 0.8489 | 0.8459 | 0.8485 | 0.8506 | 0.8634 | 0.9195 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 776.6 | 777.7 | 778 | 777.4 | 785.8 | 784 | 771.1 |
| HPA replicas, mean | 8.367 | 8.663 | 7.662 | 7.791 | 7.411 | 7.406 | 8.452 | 8.61 |
| pods started | 5.4 | 4.7 | 3.9 | 4.3 | 4.3 | 4.2 | 4.8 | 4.9 |
| pod start wait, total (s) | 7.7 | 5.7 | 5 | 5.8 | 5.7 | 6 | 6.3 | 6.7 |
| pod start wait, mean (s) | 1.45 | 1.198 | 1.337 | 1.402 | 1.273 | 1.465 | 1.333 | 1.42 |
| host CPU busy, the real machine under kind (%) | 26.78 | 27.12 | 25.93 | 26.11 | 26.26 | 26.28 | 26.63 | 28.34 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.509 | −0.1% | −0.0076 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | −0.3% | −1.0424 to +0.0054 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | −0.3% | −1.0424 to +0.0054 | no |
| response time (ms), mean | 140.9 | 74.6 | −47.1% | −87.8553 to −44.7529 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 107 | −65.4% | −263.8229 to −141.3211 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 141.2 | −71.9% | −465.4849 to −258.3829 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0 | −100.0% | −2.8055 to −0.2843 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +18.1997 to +20.2003 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.2383 | +32.4% | −0.1342 to +0.2508 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03527 | −3.5% | −0.0020 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8465 | −3.5% | −0.0469 to −0.0153 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03412 | +0.034 (native is 0) | +0.0298 to +0.0384 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8806 | +0.3% | −0.0093 to +0.0154 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 776.6 | +2.9% | +15.0950 to +28.4647 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 8.663 | +3.5% | −0.1116 to +0.7029 | no |
| pods started | 5.4 | 4.7 | −13.0% | −1.7690 to +0.3690 | no |
| pod start wait, total (s) | 7.7 | 5.7 | −26.0% | −4.6119 to +0.6119 | no |
| pod start wait, mean (s) | 1.45 | 1.198 | −17.4% | −0.5914 to +0.0881 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 27.12 | +1.2% | −0.0387 to +0.7041 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.511 | 0.0% | raw −0.0019 to +0.0019 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.5666 to −0.0682 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.5666 to −0.0682 | yes: GAIN |
| response time (ms), mean | 140.9 | 73.91 | −47.5% | −88.8884 to −45.1032 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 105.5 | −65.9% | −267.2270 to −140.8660 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 140.4 | −72.1% | −473.5490 to −251.8948 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0 | −100.0% | −2.8055 to −0.2843 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.7 | +14.700 (native is 0) | +12.5928 to +16.8072 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.1067 | −40.7% | −0.3218 to +0.1752 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03514 | −3.9% | −0.0024 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8433 | −3.9% | −0.0572 to −0.0114 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00559 | +0.006 (native is 0) | +0.0049 to +0.0063 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8489 | −3.3% | −0.0510 to −0.0064 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 777.7 | +3.0% | +11.2563 to +34.6245 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 7.662 | −8.4% | −1.6202 to +0.2104 | no |
| pods started | 5.4 | 3.9 | −27.8% | −2.8168 to −0.1832 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5 | −35.1% | −5.2019 to −0.1981 | yes: GAIN |
| pod start wait, mean (s) | 1.45 | 1.337 | −7.8% | −0.5084 to +0.2817 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 25.93 | −3.2% | −1.4287 to −0.2789 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.511 | +0.0% | −0.0009 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.6697 to −0.0026 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.6697 to −0.0026 | yes: GAIN |
| response time (ms), mean | 140.9 | 73.57 | −47.8% | −89.4168 to −45.2505 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 104.1 | −66.4% | −268.8994 to −141.9766 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 137.3 | −72.7% | −474.6747 to −257.0951 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0 | −100.0% | −2.8055 to −0.2843 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.2 | +18.200 (native is 0) | +15.8687 to +20.5313 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.08167 | −54.6% | −0.3335 to +0.1368 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03497 | −4.4% | −0.0027 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8393 | −4.4% | −0.0653 to −0.0112 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00659 | +0.007 (native is 0) | +0.0057 to +0.0075 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8459 | −3.6% | −0.0579 to −0.0054 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 778 | +3.1% | +8.6886 to +37.7291 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 7.791 | −6.9% | −1.1089 to −0.0429 | yes: GAIN |
| pods started | 5.4 | 4.3 | −20.4% | −1.8872 to −0.3128 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5.8 | −24.7% | −4.5860 to +0.7860 | no |
| pod start wait, mean (s) | 1.45 | 1.402 | −3.3% | −0.4502 to +0.3536 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 26.11 | −2.5% | −1.3029 to −0.0502 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0014 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.4987 to +0.0655 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.4987 to +0.0655 | no |
| response time (ms), mean | 140.9 | 73.87 | −47.6% | −88.8674 to −45.2072 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 105.5 | −65.9% | −266.7611 to −141.3089 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 144.9 | −71.2% | −470.7301 to −245.7383 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0 | −100.0% | −2.8055 to −0.2843 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 | +17.300 (native is 0) | +14.5184 to +20.0816 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.02667 | −85.2% | −0.3301 to +0.0234 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03505 | −4.2% | −0.0025 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8412 | −4.2% | −0.0601 to −0.0128 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00729 | +0.007 (native is 0) | +0.0062 to +0.0084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8485 | −3.3% | −0.0519 to −0.0065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 777.4 | +3.0% | +9.8081 to +35.4203 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 7.411 | −11.4% | −1.3572 to −0.5559 | yes: GAIN |
| pods started | 5.4 | 4.3 | −20.4% | −1.9564 to −0.2436 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5.7 | −26.0% | −5.0348 to +1.0348 | no |
| pod start wait, mean (s) | 1.45 | 1.273 | −12.2% | −0.6465 to +0.2932 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 26.26 | −2.0% | −1.0620 to +0.0156 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.509 | −0.1% | −0.0072 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.7 | −0.4% | −1.0393 to −0.0841 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.7 | −0.4% | −1.0393 to −0.0841 | yes: GAIN |
| response time (ms), mean | 140.9 | 73.72 | −47.7% | −89.1240 to −45.2450 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 105.4 | −65.9% | −266.8072 to −141.4888 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 139.5 | −72.3% | −472.6911 to −254.6233 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0 | −100.0% | −2.8055 to −0.2843 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17.000 (native is 0) | +13.8729 to +20.1271 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.025 | −86.1% | −0.3110 to +0.0010 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03489 | −4.6% | −0.0026 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8373 | −4.6% | −0.0622 to −0.0184 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01331 | +0.013 (native is 0) | +0.0116 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8506 | −3.1% | −0.0475 to −0.0065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 785.8 | +4.1% | +14.5657 to +47.4536 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 7.406 | −11.5% | −1.4107 to −0.5107 | yes: GAIN |
| pods started | 5.4 | 4.2 | −22.2% | −2.1417 to −0.2583 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6 | −22.1% | −3.8604 to +0.4604 | no |
| pod start wait, mean (s) | 1.45 | 1.465 | +1.0% | −0.3859 to +0.4159 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 26.28 | −1.9% | −1.1130 to +0.1120 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0052 to +0.0039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.3% | −0.8597 to +0.0231 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.3% | −0.8597 to +0.0231 | no |
| response time (ms), mean | 140.9 | 74.07 | −47.4% | −88.6568 to −45.0101 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 105 | −66.1% | −267.1118 to −141.9372 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 140.1 | −72.2% | −475.3427 to −250.8591 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0.0119 | −99.2% | −2.7975 to −0.2685 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +18.7274 to +20.2726 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.1083 | −39.8% | −0.2879 to +0.1445 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03498 | −4.3% | −0.0024 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8396 | −4.3% | −0.0571 to −0.0188 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02377 | +0.024 (native is 0) | +0.0209 to +0.0266 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.8634 | −1.6% | −0.0310 to +0.0026 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 784 | +3.9% | +13.2132 to +45.1854 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 8.452 | +1.0% | −0.1384 to +0.3087 | no |
| pods started | 5.4 | 4.8 | −11.1% | −1.7285 to +0.5285 | no |
| pod start wait, total (s) | 7.7 | 6.3 | −18.2% | −3.8825 to +1.0825 | no |
| pod start wait, mean (s) | 1.45 | 1.333 | −8.0% | −0.5056 to +0.2723 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 26.63 | −0.6% | −0.6531 to +0.3426 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.51 | −0.1% | −0.0065 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.8705 to +0.2506 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.8705 to +0.2506 | no |
| response time (ms), mean | 140.9 | 75.22 | −46.6% | −87.0677 to −44.3020 | yes: GAIN |
| response time (ms), 95th percentile | 309.6 | 106.2 | −65.7% | −266.1378 to −140.6242 | yes: GAIN |
| response time (ms), 99th percentile | 503.2 | 142.9 | −71.6% | −464.2527 to −256.2697 | yes: GAIN |
| time over the response line (% of samples) | 1.545 | 0.03593 | −97.7% | −2.7589 to −0.2590 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −3.0906 to +0.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +18.8674 to +21.7326 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.18 | 0.1067 | −40.7% | −0.2448 to +0.0982 | no |
| utilisation (used / allocatable) | 0.03657 | 0.0356 | −2.6% | −0.0017 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8776 | 0.8544 | −2.6% | −0.0417 to −0.0048 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06506 | +0.065 (native is 0) | +0.0575 to +0.0726 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8776 | 0.9195 | +4.8% | +0.0282 to +0.0555 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.8 | 771.1 | +2.2% | +6.9149 to +25.6107 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.367 | 8.61 | +2.9% | −0.0930 to +0.5787 | no |
| pods started | 5.4 | 4.9 | −9.3% | −1.3430 to +0.3430 | no |
| pod start wait, total (s) | 7.7 | 6.7 | −13.0% | −3.1853 to +1.1853 | no |
| pod start wait, mean (s) | 1.45 | 1.42 | −2.1% | −0.3798 to +0.3198 | no |
| host CPU busy, the real machine under kind (%) | 26.78 | 28.34 | +5.8% | +1.2467 to +1.8650 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.511 | +0.1% | −0.0037 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158 | +0.1% | −0.3642 to +0.7663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158 | +0.1% | −0.3642 to +0.7663 | no |
| response time (ms), mean | 74.6 | 73.91 | −0.9% | −1.7604 to +0.3770 | no |
| response time (ms), 95th percentile | 107 | 105.5 | −1.4% | −4.1937 to +1.2447 | no |
| response time (ms), 99th percentile | 141.2 | 140.4 | −0.6% | −12.7568 to +11.1808 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 14.7 | −23.4% | −6.5020 to −2.4980 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.1067 | −55.2% | −0.3713 to +0.1080 | no |
| utilisation (used / allocatable) | 0.03527 | 0.03514 | −0.4% | −0.0006 to +0.0004 | no |
| CPU used (cores), mean | 0.8465 | 0.8433 | −0.4% | −0.0148 to +0.0085 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.00559 | −83.6% | −0.0321 to −0.0249 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8489 | −3.6% | −0.0460 to −0.0174 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 777.7 | +0.1% | −9.5138 to +11.8348 | no |
| HPA replicas, mean | 8.663 | 7.662 | −11.5% | −1.6797 to −0.3213 | yes: GAIN |
| pods started | 4.7 | 3.9 | −17.0% | −2.0526 to +0.4526 | no |
| pod start wait, total (s) | 5.7 | 5 | −12.3% | −3.5423 to +2.1423 | no |
| pod start wait, mean (s) | 1.198 | 1.337 | +11.5% | −0.4125 to +0.6892 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 25.93 | −4.4% | −1.5990 to −0.7741 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.511 | +0.2% | −0.0038 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158 | +0.1% | −0.5009 to +0.8656 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158 | +0.1% | −0.5009 to +0.8656 | no |
| response time (ms), mean | 74.6 | 73.57 | −1.4% | −2.1861 to +0.1269 | no |
| response time (ms), 95th percentile | 107 | 104.1 | −2.7% | −6.0026 to +0.2706 | no |
| response time (ms), 99th percentile | 141.2 | 137.3 | −2.8% | −13.8033 to +5.9013 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 18.2 | −5.2% | −3.3117 to +1.3117 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.08167 | −65.7% | −0.3951 to +0.0818 | no |
| utilisation (used / allocatable) | 0.03527 | 0.03497 | −0.8% | −0.0009 to +0.0003 | no |
| CPU used (cores), mean | 0.8465 | 0.8393 | −0.8% | −0.0219 to +0.0076 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.00659 | −80.7% | −0.0310 to −0.0241 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8459 | −3.9% | −0.0521 to −0.0172 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 778 | +0.2% | −10.0737 to +12.9316 | no |
| HPA replicas, mean | 8.663 | 7.791 | −10.1% | −1.4080 to −0.3351 | yes: GAIN |
| pods started | 4.7 | 4.3 | −8.5% | −1.4228 to +0.6228 | no |
| pod start wait, total (s) | 5.7 | 5.8 | +1.8% | −2.8095 to +3.0095 | no |
| pod start wait, mean (s) | 1.198 | 1.402 | +17.0% | −0.3284 to +0.7350 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 26.11 | −3.7% | −1.4447 to −0.5738 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.512 | +0.2% | −0.0029 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158.1 | +0.2% | −0.3237 to +0.9275 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158.1 | +0.2% | −0.3237 to +0.9275 | no |
| response time (ms), mean | 74.6 | 73.87 | −1.0% | −1.8479 to +0.3815 | no |
| response time (ms), 95th percentile | 107 | 105.5 | −1.4% | −4.4944 to +1.5684 | no |
| response time (ms), 99th percentile | 141.2 | 144.9 | +2.6% | −16.8484 to +24.2478 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 17.3 | −9.9% | −4.7101 to +0.9101 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.02667 | −88.8% | −0.3840 to −0.0394 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03527 | 0.03505 | −0.6% | −0.0007 to +0.0002 | no |
| CPU used (cores), mean | 0.8465 | 0.8412 | −0.6% | −0.0165 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.00729 | −78.6% | −0.0301 to −0.0235 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8485 | −3.7% | −0.0460 to −0.0183 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 777.4 | +0.1% | −8.9056 to +10.5743 | no |
| HPA replicas, mean | 8.663 | 7.411 | −14.5% | −1.6303 to −0.8741 | yes: GAIN |
| pods started | 4.7 | 4.3 | −8.5% | −1.2396 to +0.4396 | no |
| pod start wait, total (s) | 5.7 | 5.7 | ±0.0% | −2.3117 to +2.3117 | no |
| pod start wait, mean (s) | 1.198 | 1.273 | +6.3% | −0.2646 to +0.4146 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 26.26 | −3.2% | −1.2417 to −0.4701 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.509 | −0.0% | −0.0016 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.7 | −0.0% | −0.2682 to +0.1817 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.7 | −0.0% | −0.2682 to +0.1817 | no |
| response time (ms), mean | 74.6 | 73.72 | −1.2% | −2.1737 to +0.4128 | no |
| response time (ms), 95th percentile | 107 | 105.4 | −1.5% | −4.1210 to +0.9690 | no |
| response time (ms), 99th percentile | 141.2 | 139.5 | −1.2% | −16.1906 to +12.7440 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 17 | −11.5% | −5.3052 to +0.9052 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.025 | −89.5% | −0.4266 to −0.0001 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03527 | 0.03489 | −1.1% | −0.0008 to +0.0000 | no |
| CPU used (cores), mean | 0.8465 | 0.8373 | −1.1% | −0.0194 to +0.0010 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.01331 | −61.0% | −0.0234 to −0.0182 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8506 | −3.4% | −0.0419 to −0.0181 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 785.8 | +1.2% | −4.8387 to +23.2983 | no |
| HPA replicas, mean | 8.663 | 7.406 | −14.5% | −1.7142 to −0.7985 | yes: GAIN |
| pods started | 4.7 | 4.2 | −10.6% | −1.7729 to +0.7729 | no |
| pod start wait, total (s) | 5.7 | 6 | +5.3% | −2.2691 to +2.8691 | no |
| pod start wait, mean (s) | 1.198 | 1.465 | +22.3% | −0.0888 to +0.6222 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 26.28 | −3.1% | −1.1469 to −0.5196 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0009 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.9 | +0.1% | −0.1776 to +0.3779 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.9 | +0.1% | −0.1776 to +0.3779 | no |
| response time (ms), mean | 74.6 | 74.07 | −0.7% | −1.4924 to +0.4337 | no |
| response time (ms), 95th percentile | 107 | 105 | −1.8% | −4.9181 to +1.0131 | no |
| response time (ms), 99th percentile | 141.2 | 140.1 | −0.8% | −15.5212 to +13.1872 | no |
| time over the response line (% of samples) | 0 | 0.0119 | +0.012 (native is 0) | −0.0150 to +0.0388 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 19.5 | +1.6% | −1.0081 to +1.6081 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 90 | −10.0% | −32.6200 to +12.6200 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.1083 | −54.5% | −0.3114 to +0.0514 | no |
| utilisation (used / allocatable) | 0.03527 | 0.03498 | −0.8% | −0.0008 to +0.0002 | no |
| CPU used (cores), mean | 0.8465 | 0.8396 | −0.8% | −0.0184 to +0.0047 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.02377 | −30.3% | −0.0119 to −0.0088 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8634 | −2.0% | −0.0295 to −0.0050 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 784 | +1.0% | −7.4169 to +22.2558 | no |
| HPA replicas, mean | 8.663 | 8.452 | −2.4% | −0.4458 to +0.0248 | no |
| pods started | 4.7 | 4.8 | +2.1% | −0.8204 to +1.0204 | no |
| pod start wait, total (s) | 5.7 | 6.3 | +10.5% | −0.8775 to +2.0775 | no |
| pod start wait, mean (s) | 1.198 | 1.333 | +11.3% | −0.1775 to +0.4475 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 26.63 | −1.8% | −0.7245 to −0.2514 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0008 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158 | +0.1% | −0.0484 to +0.4655 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158 | +0.1% | −0.0484 to +0.4655 | no |
| response time (ms), mean | 74.6 | 75.22 | +0.8% | +0.0492 to +1.1892 | yes: LOSS |
| response time (ms), 95th percentile | 107 | 106.2 | −0.8% | −3.1112 to +1.4932 | no |
| response time (ms), 99th percentile | 141.2 | 142.9 | +1.2% | −7.9901 to +11.3355 | no |
| time over the response line (% of samples) | 0 | 0.03593 | +0.036 (native is 0) | −0.0055 to +0.0773 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 20.3 | +5.7% | −0.8502 to +3.0502 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 80 | −20.0% | −50.1600 to +10.1600 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.1067 | −55.2% | −0.3138 to +0.0505 | no |
| utilisation (used / allocatable) | 0.03527 | 0.0356 | +0.9% | −0.0001 to +0.0008 | no |
| CPU used (cores), mean | 0.8465 | 0.8544 | +0.9% | −0.0030 to +0.0188 | no |
| Omni's own CPU (cores), mean | 0.03412 | 0.06506 | +90.7% | +0.0276 to +0.0343 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.9195 | +4.4% | +0.0277 to +0.0500 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.6 | 771.1 | −0.7% | −13.1307 to +2.0966 | no |
| HPA replicas, mean | 8.663 | 8.61 | −0.6% | −0.3683 to +0.2627 | no |
| pods started | 4.7 | 4.9 | +4.3% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 5.7 | 6.7 | +17.5% | −1.0511 to +3.0511 | no |
| pod start wait, mean (s) | 1.198 | 1.42 | +18.5% | −0.2584 to +0.7017 | no |
| host CPU busy, the real machine under kind (%) | 27.12 | 28.34 | +4.5% | +0.9843 to +1.4618 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*