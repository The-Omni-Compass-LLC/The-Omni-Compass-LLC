# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.513 | 1.514 | 1.515 | 1.513 | 1.514 | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | 158 | 158.1 | 157.9 | 158 | 157.9 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | 158 | 158.1 | 157.9 | 158 | 157.9 | 158.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 137.6 | 72.67 | 71.16 | 71.56 | 72.32 | 71.98 | 72.52 | 73.68 |
| response time (ms), 95th percentile | 313.7 | 105.4 | 100.8 | 101.6 | 103.1 | 102.3 | 103.9 | 107.1 |
| response time (ms), 99th percentile | 488.6 | 139.3 | 126.3 | 131.1 | 161.5 | 137.7 | 132.2 | 136.5 |
| time over the response line (% of samples) | 1.617 | 0 | 0.01198 | 0.01198 | 0.1213 | 0.0241 | 0.03622 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | 0 | 0 | 0.2 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19 | 15.5 | 18.9 | 21.1 | 16.4 | 18.6 | 20.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | 100 | 70 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.235 | 0.11 | 0.05333 | 0.08 | 0.02667 | 0.05333 | 0.1567 |
| utilisation (used / allocatable) | 0.03513 | 0.0342 | 0.0337 | 0.03393 | 0.03385 | 0.03403 | 0.03413 | 0.03474 |
| CPU used (cores), mean | 0.843 | 0.8207 | 0.8087 | 0.8144 | 0.8125 | 0.8168 | 0.819 | 0.8338 |
| Omni's own CPU (cores), mean | 0 | 0.03465 | 0.00578 | 0.00669 | 0.00779 | 0.01331 | 0.02403 | 0.06555 |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8554 | 0.8145 | 0.8211 | 0.8203 | 0.8301 | 0.8431 | 0.8993 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 796.3 | 808.9 | 800.3 | 805 | 802.5 | 795.9 | 780.3 |
| HPA replicas, mean | 8.213 | 8.439 | 8.112 | 7.866 | 7.608 | 7.236 | 8.404 | 8.458 |
| pods started | 5.5 | 5.1 | 4.4 | 4.7 | 5.2 | 4.1 | 4.7 | 4.9 |
| pod start wait, total (s) | 8.2 | 7.7 | 6.9 | 7.8 | 7.6 | 6.6 | 6.7 | 7 |
| pod start wait, mean (s) | 1.5 | 1.533 | 1.407 | 1.683 | 1.391 | 1.558 | 1.437 | 1.435 |
| host CPU busy, the real machine under kind (%) | 26.29 | 26.88 | 25.48 | 25.66 | 25.7 | 25.87 | 26.41 | 28.04 |
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
| node-hours | 1.514 | 1.513 | −0.1% | −0.0057 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.7402 to +0.1594 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.7402 to +0.1594 | no |
| response time (ms), mean | 137.6 | 72.67 | −47.2% | −87.5632 to −42.3793 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 105.4 | −66.4% | −278.4702 to −138.1108 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 139.3 | −71.5% | −481.1513 to −217.4331 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0 | −100.0% | −3.1130 to −0.1215 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19 | +19.000 (native is 0) | +18.1740 to +19.8260 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.235 | −31.9% | −0.5993 to +0.3793 | no |
| utilisation (used / allocatable) | 0.03513 | 0.0342 | −2.6% | −0.0021 to +0.0002 | no |
| CPU used (cores), mean | 0.843 | 0.8207 | −2.6% | −0.0504 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0 | 0.03465 | +0.035 (native is 0) | +0.0301 to +0.0392 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8554 | +1.5% | −0.0122 to +0.0369 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 796.3 | +1.4% | −13.3323 to +35.5639 | no |
| HPA replicas, mean | 8.213 | 8.439 | +2.8% | −0.0573 to +0.5101 | no |
| pods started | 5.5 | 5.1 | −7.3% | −1.1689 to +0.3689 | no |
| pod start wait, total (s) | 8.2 | 7.7 | −6.1% | −3.1817 to +2.1817 | no |
| pod start wait, mean (s) | 1.5 | 1.533 | +2.2% | −0.3854 to +0.4521 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 26.88 | +2.2% | −0.0672 to +1.2369 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0017 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.6469 to +0.0614 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.6469 to +0.0614 | no |
| response time (ms), mean | 137.6 | 71.16 | −48.3% | −89.3008 to −43.6558 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 100.8 | −67.9% | −283.3270 to −142.5390 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 126.3 | −74.2% | −497.7232 to −226.9452 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0.01198 | −99.3% | −3.0860 to −0.1246 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.5 | +15.500 (native is 0) | +14.1832 to +16.8168 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.11 | −68.1% | −0.6563 to +0.1863 | no |
| utilisation (used / allocatable) | 0.03513 | 0.0337 | −4.1% | −0.0025 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.843 | 0.8087 | −4.1% | −0.0588 to −0.0099 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00578 | +0.006 (native is 0) | +0.0050 to +0.0065 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8145 | −3.4% | −0.0524 to −0.0047 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 808.9 | +3.0% | +11.4328 to +35.9163 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.213 | 8.112 | −1.2% | −0.3744 to +0.1720 | no |
| pods started | 5.5 | 4.4 | −20.0% | −2.4254 to +0.2254 | no |
| pod start wait, total (s) | 8.2 | 6.9 | −15.9% | −4.5352 to +1.9352 | no |
| pod start wait, mean (s) | 1.5 | 1.407 | −6.2% | −0.6192 to +0.4325 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 25.48 | −3.1% | −1.4261 to −0.2026 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0014 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.5717 to +0.2415 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.5717 to +0.2415 | no |
| response time (ms), mean | 137.6 | 71.56 | −48.0% | −88.9507 to −43.2114 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 101.6 | −67.6% | −282.9343 to −141.2967 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 131.1 | −73.2% | −495.7135 to −219.3831 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0.01198 | −99.3% | −3.0860 to −0.1246 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +16.3442 to +21.4558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.05333 | −84.5% | −0.6688 to +0.0855 | no |
| utilisation (used / allocatable) | 0.03513 | 0.03393 | −3.4% | −0.0023 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.843 | 0.8144 | −3.4% | −0.0555 to −0.0018 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00669 | +0.007 (native is 0) | +0.0058 to +0.0076 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8211 | −2.6% | −0.0482 to +0.0043 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 800.3 | +1.9% | −4.9585 to +35.1292 | no |
| HPA replicas, mean | 8.213 | 7.866 | −4.2% | −0.9148 to +0.2217 | no |
| pods started | 5.5 | 4.7 | −14.5% | −2.1403 to +0.5403 | no |
| pod start wait, total (s) | 8.2 | 7.8 | −4.9% | −3.6553 to +2.8553 | no |
| pod start wait, mean (s) | 1.5 | 1.683 | +12.2% | −0.1332 to +0.4999 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 25.66 | −2.4% | −1.3660 to +0.1046 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.1% | −0.0062 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.2% | −0.7803 to +0.0807 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.2% | −0.7803 to +0.0807 | no |
| response time (ms), mean | 137.6 | 72.32 | −47.5% | −87.1469 to −43.4852 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 103.1 | −67.1% | −279.2856 to −141.8884 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 161.5 | −67.0% | −430.3865 to −223.9587 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0.1213 | −92.5% | −2.8497 to −0.1422 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0.2 | −85.7% | −2.4526 to +0.0526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.1 | +21.100 (native is 0) | +11.8258 to +30.3742 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.08 | −76.8% | −0.6023 to +0.0723 | no |
| utilisation (used / allocatable) | 0.03513 | 0.03385 | −3.6% | −0.0022 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.843 | 0.8125 | −3.6% | −0.0525 to −0.0086 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00779 | +0.008 (native is 0) | +0.0060 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8203 | −2.7% | −0.0434 to −0.0021 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 805 | +2.5% | −4.1370 to +43.7830 | no |
| HPA replicas, mean | 8.213 | 7.608 | −7.4% | −1.7159 to +0.5051 | no |
| pods started | 5.5 | 5.2 | −5.5% | −2.3246 to +1.7246 | no |
| pod start wait, total (s) | 8.2 | 7.6 | −7.3% | −4.6911 to +3.4911 | no |
| pod start wait, mean (s) | 1.5 | 1.391 | −7.3% | −0.5836 to +0.3660 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 25.7 | −2.3% | −1.1526 to −0.0392 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0023 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.5671 to +0.0621 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.5671 to +0.0621 | no |
| response time (ms), mean | 137.6 | 71.98 | −47.7% | −88.6048 to −42.7213 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 102.3 | −67.4% | −282.0868 to −140.7982 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 137.7 | −71.8% | −487.8992 to −213.9278 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0.0241 | −98.5% | −3.0596 to −0.1267 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 | +16.400 (native is 0) | +13.3243 to +19.4757 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.02667 | −92.3% | −0.6767 to +0.0400 | no |
| utilisation (used / allocatable) | 0.03513 | 0.03403 | −3.1% | −0.0019 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.843 | 0.8168 | −3.1% | −0.0461 to −0.0064 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01331 | +0.013 (native is 0) | +0.0115 to +0.0151 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8301 | −1.5% | −0.0312 to +0.0053 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 802.5 | +2.2% | +3.4363 to +31.1004 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.213 | 7.236 | −11.9% | −1.3644 to −0.5887 | yes: GAIN |
| pods started | 5.5 | 4.1 | −25.5% | −2.0032 to −0.7968 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 6.6 | −19.5% | −4.1945 to +0.9945 | no |
| pod start wait, mean (s) | 1.5 | 1.558 | +3.9% | −0.3430 to +0.4597 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 25.87 | −1.6% | −1.0462 to +0.2027 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0062 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.2% | −0.8682 to +0.1285 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.2% | −0.8682 to +0.1285 | no |
| response time (ms), mean | 137.6 | 72.52 | −47.3% | −87.8673 to −42.3748 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 103.9 | −66.9% | −279.6572 to −140.0368 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 132.2 | −73.0% | −488.5849 to −224.3351 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0.03622 | −97.8% | −3.0359 to −0.1261 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.600 (native is 0) | +17.3749 to +19.8251 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.05333 | −84.5% | −0.6099 to +0.0266 | no |
| utilisation (used / allocatable) | 0.03513 | 0.03413 | −2.8% | −0.0021 to +0.0001 | no |
| CPU used (cores), mean | 0.843 | 0.819 | −2.8% | −0.0510 to +0.0031 | no |
| Omni's own CPU (cores), mean | 0 | 0.02403 | +0.024 (native is 0) | +0.0210 to +0.0271 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8431 | +0.0% | −0.0245 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 795.9 | +1.4% | −11.7953 to +33.2365 | no |
| HPA replicas, mean | 8.213 | 8.404 | +2.3% | −0.0066 to +0.3897 | no |
| pods started | 5.5 | 4.7 | −14.5% | −2.0526 to +0.4526 | no |
| pod start wait, total (s) | 8.2 | 6.7 | −18.3% | −4.9758 to +1.9758 | no |
| pod start wait, mean (s) | 1.5 | 1.437 | −4.2% | −0.4893 to +0.3627 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 26.41 | +0.4% | −0.5207 to +0.7541 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0055 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.2 | −0.1% | −0.5253 to +0.2990 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.2 | −0.1% | −0.5253 to +0.2990 | no |
| response time (ms), mean | 137.6 | 73.68 | −46.5% | −86.8573 to −41.0696 | yes: GAIN |
| response time (ms), 95th percentile | 313.7 | 107.1 | −65.9% | −276.1868 to −137.0782 | yes: GAIN |
| response time (ms), 99th percentile | 488.6 | 136.5 | −72.1% | −483.6305 to −220.7329 | yes: GAIN |
| time over the response line (% of samples) | 1.617 | 0 | −100.0% | −3.1130 to −0.1215 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.9155 to +0.1155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.2 | +20.200 (native is 0) | +18.4872 to +21.9128 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.1567 | −54.6% | −0.6465 to +0.2698 | no |
| utilisation (used / allocatable) | 0.03513 | 0.03474 | −1.1% | −0.0016 to +0.0009 | no |
| CPU used (cores), mean | 0.843 | 0.8338 | −1.1% | −0.0395 to +0.0210 | no |
| Omni's own CPU (cores), mean | 0 | 0.06555 | +0.066 (native is 0) | +0.0575 to +0.0736 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.843 | 0.8993 | +6.7% | +0.0314 to +0.0812 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.2 | 780.3 | −0.6% | −40.3303 to +30.5288 | no |
| HPA replicas, mean | 8.213 | 8.458 | +3.0% | −0.0164 to +0.5058 | no |
| pods started | 5.5 | 4.9 | −10.9% | −1.7285 to +0.5285 | no |
| pod start wait, total (s) | 8.2 | 7 | −14.6% | −3.2732 to +0.8732 | no |
| pod start wait, mean (s) | 1.5 | 1.435 | −4.3% | −0.4093 to +0.2797 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 28.04 | +6.7% | +1.0918 to +2.4078 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0044 to +0.0067 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158 | −0.0% | −0.5482 to +0.5435 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158 | −0.0% | −0.5482 to +0.5435 | no |
| response time (ms), mean | 72.67 | 71.16 | −2.1% | −2.7461 to −0.2680 | yes: GAIN |
| response time (ms), 95th percentile | 105.4 | 100.8 | −4.4% | −10.0846 to +0.7996 | no |
| response time (ms), 99th percentile | 139.3 | 126.3 | −9.4% | −25.9961 to −0.0879 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.01198 | +0.012 (native is 0) | −0.0151 to +0.0391 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 15.5 | −18.4% | −4.5256 to −2.4744 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.11 | −53.2% | −0.3381 to +0.0881 | no |
| utilisation (used / allocatable) | 0.0342 | 0.0337 | −1.5% | −0.0011 to +0.0001 | no |
| CPU used (cores), mean | 0.8207 | 0.8087 | −1.5% | −0.0266 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0.03465 | 0.00578 | −83.3% | −0.0327 to −0.0250 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8145 | −4.8% | −0.0558 to −0.0260 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 808.9 | +1.6% | −5.3485 to +30.4660 | no |
| HPA replicas, mean | 8.439 | 8.112 | −3.9% | −0.6190 to −0.0362 | yes: GAIN |
| pods started | 5.1 | 4.4 | −13.7% | −1.5294 to +0.1294 | no |
| pod start wait, total (s) | 7.7 | 6.9 | −10.4% | −2.9273 to +1.3273 | no |
| pod start wait, mean (s) | 1.533 | 1.407 | −8.3% | −0.6375 to +0.3842 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 25.48 | −5.2% | −1.8943 to −0.9042 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0035 to +0.0072 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.1 | +0.1% | −0.4170 to +0.6676 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.1 | +0.1% | −0.4170 to +0.6676 | no |
| response time (ms), mean | 72.67 | 71.56 | −1.5% | −2.4797 to +0.2601 | no |
| response time (ms), 95th percentile | 105.4 | 101.6 | −3.6% | −8.4966 to +0.8466 | no |
| response time (ms), 99th percentile | 139.3 | 131.1 | −5.9% | −23.4288 to +6.9166 | no |
| time over the response line (% of samples) | 0 | 0.01198 | +0.012 (native is 0) | −0.0151 to +0.0391 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 18.9 | −0.5% | −2.8693 to +2.6693 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.05333 | −77.3% | −0.4133 to +0.0499 | no |
| utilisation (used / allocatable) | 0.0342 | 0.03393 | −0.8% | −0.0009 to +0.0003 | no |
| CPU used (cores), mean | 0.8207 | 0.8144 | −0.8% | −0.0206 to +0.0080 | no |
| Omni's own CPU (cores), mean | 0.03465 | 0.00669 | −80.7% | −0.0317 to −0.0243 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8211 | −4.0% | −0.0494 to −0.0192 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 800.3 | +0.5% | −14.3100 to +22.2490 | no |
| HPA replicas, mean | 8.439 | 7.866 | −6.8% | −1.0887 to −0.0571 | yes: GAIN |
| pods started | 5.1 | 4.7 | −7.8% | −1.5285 to +0.7285 | no |
| pod start wait, total (s) | 7.7 | 7.8 | +1.3% | −2.0179 to +2.2179 | no |
| pod start wait, mean (s) | 1.533 | 1.683 | +9.8% | −0.1479 to +0.4479 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 25.66 | −4.5% | −1.7126 to −0.7185 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0020 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | −0.0% | −0.2903 to +0.1715 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | −0.0% | −0.2903 to +0.1715 | no |
| response time (ms), mean | 72.67 | 72.32 | −0.5% | −1.9687 to +1.2792 | no |
| response time (ms), 95th percentile | 105.4 | 103.1 | −2.2% | −7.5860 to +2.9930 | no |
| response time (ms), 99th percentile | 139.3 | 161.5 | +15.9% | −25.3125 to +69.5517 | no |
| time over the response line (% of samples) | 0 | 0.1213 | +0.121 (native is 0) | −0.0425 to +0.2850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 21.1 | +11.1% | −6.7089 to +10.9089 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.08 | −66.0% | −0.4500 to +0.1400 | no |
| utilisation (used / allocatable) | 0.0342 | 0.03385 | −1.0% | −0.0010 to +0.0003 | no |
| CPU used (cores), mean | 0.8207 | 0.8125 | −1.0% | −0.0237 to +0.0072 | no |
| Omni's own CPU (cores), mean | 0.03465 | 0.00779 | −77.5% | −0.0299 to −0.0239 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8203 | −4.1% | −0.0499 to −0.0202 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 805 | +1.1% | −3.8387 to +21.2531 | no |
| HPA replicas, mean | 8.439 | 7.608 | −9.9% | −1.8223 to +0.1587 | no |
| pods started | 5.1 | 5.2 | +2.0% | −2.3187 to +2.5187 | no |
| pod start wait, total (s) | 7.7 | 7.6 | −1.3% | −4.2634 to +4.0634 | no |
| pod start wait, mean (s) | 1.533 | 1.391 | −9.3% | −0.5065 to +0.2222 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 25.7 | −4.4% | −1.5650 to −0.7965 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0051 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158 | +0.0% | −0.5321 to +0.6080 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158 | +0.0% | −0.5321 to +0.6080 | no |
| response time (ms), mean | 72.67 | 71.98 | −1.0% | −1.6419 to +0.2583 | no |
| response time (ms), 95th percentile | 105.4 | 102.3 | −3.0% | −7.7823 to +1.4783 | no |
| response time (ms), 99th percentile | 139.3 | 137.7 | −1.2% | −12.4211 to +9.1785 | no |
| time over the response line (% of samples) | 0 | 0.0241 | +0.024 (native is 0) | −0.0122 to +0.0604 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 16.4 | −13.7% | −5.2379 to +0.0379 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.02667 | −88.7% | −0.4841 to +0.0674 | no |
| utilisation (used / allocatable) | 0.0342 | 0.03403 | −0.5% | −0.0007 to +0.0003 | no |
| CPU used (cores), mean | 0.8207 | 0.8168 | −0.5% | −0.0160 to +0.0081 | no |
| Omni's own CPU (cores), mean | 0.03465 | 0.01331 | −61.6% | −0.0242 to −0.0185 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8301 | −3.0% | −0.0364 to −0.0141 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 802.5 | +0.8% | −6.6925 to +18.9976 | no |
| HPA replicas, mean | 8.439 | 7.236 | −14.3% | −1.6035 to −0.8024 | yes: GAIN |
| pods started | 5.1 | 4.1 | −19.6% | −1.8921 to −0.1079 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.6 | −14.3% | −3.9503 to +1.7503 | no |
| pod start wait, mean (s) | 1.533 | 1.558 | +1.6% | −0.3505 to +0.4005 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 25.87 | −3.7% | −1.3505 to −0.6628 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0023 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | −0.1% | −0.2800 to +0.1212 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | −0.1% | −0.2800 to +0.1212 | no |
| response time (ms), mean | 72.67 | 72.52 | −0.2% | −1.0691 to +0.7696 | no |
| response time (ms), 95th percentile | 105.4 | 103.9 | −1.5% | −6.9358 to +3.8228 | no |
| response time (ms), 99th percentile | 139.3 | 132.2 | −5.1% | −20.5989 to +6.2633 | no |
| time over the response line (% of samples) | 0 | 0.03622 | +0.036 (native is 0) | −0.0055 to +0.0779 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 18.6 | −2.1% | −1.7985 to +0.9985 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 70 | −30.0% | −64.5526 to +4.5526 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.05333 | −77.3% | −0.4608 to +0.0974 | no |
| utilisation (used / allocatable) | 0.0342 | 0.03413 | −0.2% | −0.0005 to +0.0004 | no |
| CPU used (cores), mean | 0.8207 | 0.819 | −0.2% | −0.0120 to +0.0087 | no |
| Omni's own CPU (cores), mean | 0.03465 | 0.02403 | −30.6% | −0.0122 to −0.0090 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8431 | −1.4% | −0.0230 to −0.0016 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 795.9 | −0.0% | −12.3287 to +11.5383 | no |
| HPA replicas, mean | 8.439 | 8.404 | −0.4% | −0.2359 to +0.1663 | no |
| pods started | 5.1 | 4.7 | −7.8% | −1.1689 to +0.3689 | no |
| pod start wait, total (s) | 7.7 | 6.7 | −13.0% | −3.1853 to +1.1853 | no |
| pod start wait, mean (s) | 1.533 | 1.437 | −6.3% | −0.5162 to +0.3229 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 26.41 | −1.7% | −0.7778 to −0.1585 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0016 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.2 | +0.1% | −0.0720 to +0.4265 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.2 | +0.1% | −0.0720 to +0.4265 | no |
| response time (ms), mean | 72.67 | 73.68 | +1.4% | +0.0775 to +1.9381 | yes: LOSS |
| response time (ms), 95th percentile | 105.4 | 107.1 | +1.6% | −1.5233 to +4.8393 | no |
| response time (ms), 99th percentile | 139.3 | 136.5 | −2.1% | −8.3224 to +2.5434 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 20.2 | +6.3% | −0.7604 to +3.1604 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.235 | 0.1567 | −33.3% | −0.3768 to +0.2201 | no |
| utilisation (used / allocatable) | 0.0342 | 0.03474 | +1.6% | +0.0001 to +0.0010 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8207 | 0.8338 | +1.6% | +0.0026 to +0.0235 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03465 | 0.06555 | +89.2% | +0.0274 to +0.0344 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8554 | 0.8993 | +5.1% | +0.0330 to +0.0549 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.3 | 780.3 | −2.0% | −32.6651 to +0.6319 | no |
| HPA replicas, mean | 8.439 | 8.458 | +0.2% | −0.2909 to +0.3276 | no |
| pods started | 5.1 | 4.9 | −3.9% | −0.9388 to +0.5388 | no |
| pod start wait, total (s) | 7.7 | 7 | −9.1% | −2.6676 to +1.2676 | no |
| pod start wait, mean (s) | 1.533 | 1.435 | −6.4% | −0.5547 to +0.3585 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 28.04 | +4.3% | +1.0245 to +1.3054 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*