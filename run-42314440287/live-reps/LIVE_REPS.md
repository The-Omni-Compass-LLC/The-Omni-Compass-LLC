# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.779 | 5.923 |
| node-hours | 2.516 | 2.516 | 2.005 | 2.485 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.6 | 270.7 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.6 | 232.3 | 268.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 245.3 | 126.6 | 231.5 | 101 |
| response time (ms), 95th percentile | 782.5 | 213.5 | 907.3 | 213.9 |
| response time (ms), 99th percentile | 1108 | 297.7 | 1305 | 323.6 |
| time over the response line (% of samples) | 8.069 | 0.1101 | 8.191 | 0.2282 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 0 | 7.2 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 192 | 100.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.775 | 893.7 | 8.827 | 1012 |
| utilisation (used / allocatable) | 0.0551 | 0.05879 | 0.06998 | 0.05757 |
| CPU used (cores), mean | 1.322 | 1.411 | 1.296 | 1.366 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06576 | 0.06219 |
| CPU used with Omni's own (cores), mean | 1.322 | 1.411 | 1.362 | 1.428 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.3 | 461.8 | 432.9 | 471.6 |
| HPA replicas, mean | 1.941 | 1.992 | 2.456 | 2.121 |
| pods started | 0.1 | 0 | 1.2 | 0.5 |
| pod start wait, total (s) | 0.3 | 0 | 2.7 | 1.2 |
| pod start wait, mean (s) | 0.3 | 0 | 1.083 | 0.45 |
| host CPU busy, the real machine under kind (%) | 37.46 | 43.6 | 40.4 | 44.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 751.5 | 1410 | 757.6 | 1416 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.119 | 5.008 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 129.9 | 0.05 | 143.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 680.8 | 0.2 | 608.3 |
| queue: job turnaround, submitted to done, mean (s) | 57.42 | 719.6 | 62.85 | 747.4 |
| queue: jobs unfinished at the window's end | 0 | 4.3 | 0 | 8 |
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
| worker nodes in service, mean | 6 | 5.923 | −1.3% | −0.2078 to +0.0540 | no |
| node-hours | 2.516 | 2.485 | −1.2% | −0.0873 to +0.0250 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 | −0.1% | −1.0126 to +0.3268 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 268.8 | −1.0% | −7.0932 to +1.5616 | no |
| response time (ms), mean | 126.6 | 101 | −20.2% | −30.5727 to −20.4806 | yes: GAIN |
| response time (ms), 95th percentile | 213.5 | 213.9 | +0.2% | −11.7304 to +12.3864 | no |
| response time (ms), 99th percentile | 297.7 | 323.6 | +8.7% | −4.3201 to +56.1617 | no |
| time over the response line (% of samples) | 0.1101 | 0.2282 | +107.3% | −0.0632 to +0.2995 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.4 | +100.400 (native is 0) | +90.0057 to +110.7943 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 893.7 | 1012 | +13.3% | +18.3013 to +218.7054 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05879 | 0.05757 | −2.1% | −0.0023 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.366 | −3.2% | −0.0668 to −0.0229 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06219 | +0.062 (native is 0) | +0.0551 to +0.0692 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.428 | +1.2% | −0.0049 to +0.0396 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 471.6 | +2.1% | +2.9373 to +16.6513 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.992 | 2.121 | +6.5% | −0.0839 to +0.3421 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.8732 to +3.2732 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.2742 to +1.1742 | no |
| host CPU busy, the real machine under kind (%) | 43.6 | 44.5 | +2.1% | −0.1572 to +1.9644 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1410 | 1416 | +0.4% | −24.3473 to +36.7473 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.008 | −16.5% | −3.3144 to +1.3312 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.9 | 143.5 | +10.4% | −10.5044 to +37.5794 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 680.8 | 608.3 | −10.6% | −231.4164 to +86.4164 | no |
| queue: job turnaround, submitted to done, mean (s) | 719.6 | 747.4 | +3.9% | −29.4106 to +85.0189 | no |
| queue: jobs unfinished at the window's end | 4.3 | 8 | +86.0% | +0.5359 to +6.8641 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.516 | 0.0% | raw −0.0066 to +0.0066 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.6 | +0.3% | −1.6902 to +3.3012 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.6 | +0.3% | −1.6902 to +3.3012 | no |
| response time (ms), mean | 245.3 | 126.6 | −48.4% | −240.1330 to +2.6088 | no |
| response time (ms), 95th percentile | 782.5 | 213.5 | −72.7% | −1158.5403 to +20.5893 | no |
| response time (ms), 99th percentile | 1108 | 297.7 | −73.1% | −1645.1823 to +25.1927 | no |
| time over the response line (% of samples) | 8.069 | 0.1101 | −98.6% | −17.1318 to +1.2142 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 0 | −100.0% | −10.1306 to −2.4694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.775 | 893.7 | +11394.2% | +623.3206 to +1148.4794 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0551 | 0.05879 | +6.7% | −0.0016 to +0.0090 | no |
| CPU used (cores), mean | 1.322 | 1.411 | +6.7% | −0.0386 to +0.2156 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.322 | 1.411 | +6.7% | −0.0386 to +0.2156 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.3 | 461.8 | −7.5% | −75.5044 to +0.6616 | no |
| HPA replicas, mean | 1.941 | 1.992 | +2.6% | −0.1182 to +0.2206 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 37.46 | 43.6 | +16.4% | +3.1787 to +9.1052 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.5 | 1410 | +87.7% | +549.9825 to +767.6175 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 129.9 | +311750.0% | +93.0939 to +166.6978 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 680.8 | +340300.0% | +515.1561 to +846.0439 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.42 | 719.6 | +1153.2% | +529.5379 to +794.8621 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 4.3 | +4.300 (native is 0) | −1.3126 to +9.9126 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.779 | −20.4% | −2.1510 to −0.2916 | yes: GAIN |
| node-hours | 2.516 | 2.005 | −20.3% | −0.9025 to −0.1192 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.7 | −0.0% | −1.1951 to +1.0065 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 232.3 | −14.2% | −68.4154 to −8.6274 | yes: GAIN |
| response time (ms), mean | 245.3 | 231.5 | −5.6% | −33.3068 to +5.6990 | no |
| response time (ms), 95th percentile | 782.5 | 907.3 | +15.9% | −21.6619 to +271.2649 | no |
| response time (ms), 99th percentile | 1108 | 1305 | +17.8% | −22.6365 to +416.8281 | no |
| time over the response line (% of samples) | 8.069 | 8.191 | +1.5% | −0.5834 to +0.8277 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 7.2 | +14.3% | −0.0802 to +1.8802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 192 | +192.000 (native is 0) | +129.9700 to +254.0300 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.775 | 8.827 | +13.5% | −0.7164 to +2.8197 | no |
| utilisation (used / allocatable) | 0.0551 | 0.06998 | +27.0% | +0.0028 to +0.0269 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.322 | 1.296 | −2.0% | −0.0936 to +0.0409 | no |
| Omni's own CPU (cores), mean | 0 | 0.06576 | +0.066 (native is 0) | +0.0590 to +0.0725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.322 | 1.362 | +3.0% | −0.0315 to +0.1103 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.3 | 432.9 | −13.3% | −120.0059 to −12.6341 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.456 | +26.5% | +0.1522 to +0.8780 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.7 | +800.0% | +0.1837 to +4.6163 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.083 | +261.1% | −0.0427 to +1.6094 | no |
| host CPU busy, the real machine under kind (%) | 37.46 | 40.4 | +7.9% | +2.2046 to +3.6885 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.5 | 757.6 | +0.8% | −3.0880 to +15.2880 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.119 | −31.4% | −3.2298 to −0.5327 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05 | +20.0% | −0.0224 to +0.0391 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.42 | 62.85 | +9.4% | −2.4346 to +13.2762 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.779 | −20.4% | −2.1510 to −0.2916 | yes: GAIN |
| node-hours | 2.516 | 2.005 | −20.3% | −0.9022 to −0.1195 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.7 | −0.3% | −3.4850 to +1.6854 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 232.3 | −14.5% | −69.9980 to −8.6557 | yes: GAIN |
| response time (ms), mean | 126.6 | 231.5 | +82.9% | −31.8653 to +241.7816 | no |
| response time (ms), 95th percentile | 213.5 | 907.3 | +324.9% | −34.9546 to +1422.5086 | no |
| response time (ms), 99th percentile | 297.7 | 1305 | +338.3% | −44.0861 to +2058.2673 | no |
| time over the response line (% of samples) | 0.1101 | 8.191 | +7341.7% | −0.6582 to +16.8200 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7.2 | +7.200 (native is 0) | +3.2131 to +11.1869 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 192 | +192.000 (native is 0) | +129.9700 to +254.0300 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 893.7 | 8.827 | −99.0% | −1145.9664 to −623.7303 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05879 | 0.06998 | +19.0% | +0.0005 to +0.0219 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.296 | −8.1% | −0.2665 to +0.0367 | no |
| Omni's own CPU (cores), mean | 0 | 0.06576 | +0.066 (native is 0) | +0.0590 to +0.0725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.362 | −3.5% | −0.2066 to +0.1083 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 432.9 | −6.3% | −71.5956 to +13.7984 | no |
| HPA replicas, mean | 1.992 | 2.456 | +23.3% | +0.1499 to +0.7779 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.1997 to +2.2003 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.1981 to +5.2019 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.083 | +1.083 (native is 0) | +0.2104 to +1.9562 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.6 | 40.4 | −7.3% | −6.4502 to +0.0595 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1410 | 757.6 | −46.3% | −761.8593 to −543.5407 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 129.9 | 0.05 | −100.0% | −166.6827 to −93.0923 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 680.8 | 0.2 | −100.0% | −846.1610 to −515.0390 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 719.6 | 62.85 | −91.3% | −785.1936 to −528.3647 | yes: GAIN |
| queue: jobs unfinished at the window's end | 4.3 | 0 | −100.0% | −9.9126 to +1.3126 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.923 | −1.3% | −0.2078 to +0.0540 | no |
| node-hours | 2.516 | 2.485 | −1.2% | −0.0876 to +0.0253 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | −1.7555 to +2.6807 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 268.8 | −0.7% | −6.5329 to +2.6122 | no |
| response time (ms), mean | 245.3 | 101 | −58.8% | −266.2549 to −22.3226 | yes: GAIN |
| response time (ms), 95th percentile | 782.5 | 213.9 | −72.7% | −1161.6600 to +24.3650 | no |
| response time (ms), 99th percentile | 1108 | 323.6 | −70.8% | −1616.1653 to +48.0173 | no |
| time over the response line (% of samples) | 8.069 | 0.2282 | −97.2% | −16.9121 to +1.2308 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 0.2 | −96.8% | −9.7231 to −2.4769 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.4 | +100.400 (native is 0) | +90.0057 to +110.7943 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.775 | 1012 | +12918.4% | +723.4645 to +1285.3422 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0551 | 0.05757 | +4.5% | −0.0030 to +0.0080 | no |
| CPU used (cores), mean | 1.322 | 1.366 | +3.3% | −0.0818 to +0.1691 | no |
| Omni's own CPU (cores), mean | 0 | 0.06219 | +0.062 (native is 0) | +0.0551 to +0.0692 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.322 | 1.428 | +8.0% | −0.0134 to +0.2251 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.3 | 471.6 | −5.5% | −67.1410 to +11.8868 | no |
| HPA replicas, mean | 1.941 | 2.121 | +9.3% | −0.0663 to +0.4269 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.4396 to +1.2396 | no |
| pod start wait, total (s) | 0.3 | 1.2 | +300.0% | −1.3733 to +3.1733 | no |
| pod start wait, mean (s) | 0.3 | 0.45 | +50.0% | −0.9170 to +1.2170 | no |
| host CPU busy, the real machine under kind (%) | 37.46 | 44.5 | +18.8% | +4.3822 to +9.7089 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.5 | 1416 | +88.5% | +552.9372 to +777.0628 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.008 | −16.5% | −3.3144 to +1.3312 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 143.5 | +344240.0% | +97.3751 to +189.4916 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 608.3 | +304050.0% | +422.8109 to +793.3891 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.42 | 747.4 | +1201.6% | +544.3460 to +835.6623 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8 | +8.000 (native is 0) | +3.0442 to +12.9558 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*