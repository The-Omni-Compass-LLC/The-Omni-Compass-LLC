# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.057 | 9.947 |
| node-hours | 5.031 | 5.021 | 3.802 | 4.171 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.1 | 522.8 | 523.6 | 526 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.1 | 522.8 | 431 | 461.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 277.7 | 413.9 | 297.7 | 612.3 |
| response time (ms), 95th percentile | 908.5 | 1445 | 1109 | 2494 |
| response time (ms), 99th percentile | 1262 | 2043 | 1572 | 3361 |
| time over the response line (% of samples) | 11.06 | 19.13 | 15.31 | 27.52 |
| failed requests (%) | 0.006849 | 0.008547 | 0 | 0.1 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 11.5 | 9 | 13.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 252.6 | 152 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 36.74 | 38.75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.102 | 11.95 | 18.52 | 19.34 |
| utilisation (used / allocatable) | 0.03053 | 0.03177 | 0.04034 | 0.0412 |
| CPU used (cores), mean | 1.465 | 1.525 | 1.429 | 1.633 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05162 | 0.0503 |
| CPU used with Omni's own (cores), mean | 1.465 | 1.525 | 1.48 | 1.683 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.4 | 828.9 | 716.7 | 678.5 |
| HPA replicas, mean | 3.91 | 4.128 | 4.364 | 4.316 |
| pods started | 0.3 | 0.2 | 1.1 | 1.7 |
| pod start wait, total (s) | 0.6 | 0.3 | 2.5 | 4.1 |
| pod start wait, mean (s) | 0.4 | 0.3 | 0.89 | 1.8 |
| host CPU busy, the real machine under kind (%) | 44.71 | 50.28 | 49.57 | 57.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.3 | 833.1 | 791.7 | 920.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 6.997 | 7.849 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 2.367 | 0.05833 | 4.112 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | 0.2 | 41.1 |
| queue: job turnaround, submitted to done, mean (s) | 80.17 | 127.9 | 102.9 | 216.4 |
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
| worker nodes in service, mean | 12 | 9.947 | −17.1% | −3.3342 to −0.7722 | yes: GAIN |
| node-hours | 5.021 | 4.171 | −16.9% | −1.3828 to −0.3169 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.8 | 526 | +0.6% | +1.5066 to +4.8868 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.8 | 461.4 | −11.7% | −102.2210 to −20.5606 | yes: GAIN |
| response time (ms), mean | 413.9 | 612.3 | +47.9% | +91.6716 to +305.2239 | yes: LOSS |
| response time (ms), 95th percentile | 1445 | 2494 | +72.6% | +544.6278 to +1554.1942 | yes: LOSS |
| response time (ms), 99th percentile | 2043 | 3361 | +64.5% | +654.4047 to +1980.3927 | yes: LOSS |
| time over the response line (% of samples) | 19.13 | 27.52 | +43.8% | +0.9116 to +15.8615 | yes: LOSS |
| failed requests (%) | 0.008547 | 0.1 | +1070.0% | −0.1154 to +0.2983 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 13.2 | +14.8% | −1.3914 to +4.7914 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 152 | +152.000 (native is 0) | +49.4710 to +254.5290 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.95 | 19.34 | +61.8% | +3.0520 to +11.7214 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03177 | 0.0412 | +29.7% | +0.0063 to +0.0126 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.525 | 1.633 | +7.1% | +0.0055 to +0.2096 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0503 | +0.050 (native is 0) | +0.0463 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.525 | 1.683 | +10.3% | +0.0550 to +0.2606 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.9 | 678.5 | −18.1% | −199.6149 to −101.2350 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.128 | 4.316 | +4.5% | −0.2515 to +0.6269 | no |
| pods started | 0.2 | 1.7 | +750.0% | +0.6570 to +2.3430 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.1 | +1266.7% | +0.9828 to +6.6172 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.8 | +500.0% | +0.6740 to +2.3260 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.28 | 57.22 | +13.8% | +4.6186 to +9.2530 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.1 | 920.2 | +10.5% | +46.5162 to +127.6838 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.849 | −34.6% | −6.0685 to −2.2341 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 2.367 | 4.112 | +73.8% | −1.5887 to +5.0803 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 41.1 | +3636.4% | −49.2253 to +129.2253 | no |
| queue: job turnaround, submitted to done, mean (s) | 127.9 | 216.4 | +69.2% | +45.9363 to +130.9970 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.021 | −0.2% | −0.0233 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.1 | 522.8 | −0.1% | −1.6828 to +1.0967 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.1 | 522.8 | −0.1% | −1.6828 to +1.0967 | no |
| response time (ms), mean | 277.7 | 413.9 | +49.0% | +37.0252 to +235.3813 | yes: LOSS |
| response time (ms), 95th percentile | 908.5 | 1445 | +59.0% | +229.7095 to +842.3565 | yes: LOSS |
| response time (ms), 99th percentile | 1262 | 2043 | +61.8% | +350.8866 to +1210.6784 | yes: LOSS |
| time over the response line (% of samples) | 11.06 | 19.13 | +73.0% | +4.3664 to +11.7841 | yes: LOSS |
| failed requests (%) | 0.006849 | 0.008547 | +24.8% | −0.0021 to +0.0055 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 11.5 | +66.7% | +1.3798 to +7.8202 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.102 | 11.95 | +47.5% | −1.9765 to +9.6765 | no |
| utilisation (used / allocatable) | 0.03053 | 0.03177 | +4.1% | +0.0004 to +0.0021 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.525 | +4.1% | +0.0171 to +0.1021 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.465 | 1.525 | +4.1% | +0.0171 to +0.1021 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.4 | 828.9 | −4.2% | −58.0839 to −14.7822 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.91 | 4.128 | +5.6% | −0.3541 to +0.7908 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.7263 to +0.5263 | no |
| pod start wait, total (s) | 0.6 | 0.3 | −50.0% | −1.4705 to +0.8705 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 44.71 | 50.28 | +12.5% | +4.1918 to +6.9598 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.3 | 833.1 | +7.7% | +12.7975 to +106.8025 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 2.367 | +4269.2% | −2.6256 to +7.2506 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.0214 to +1.3786 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.17 | 127.9 | +59.5% | +21.1372 to +74.3044 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.057 | −24.5% | −4.4552 to −1.4300 | yes: GAIN |
| node-hours | 5.031 | 3.802 | −24.4% | −1.8614 to −0.5962 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.1 | 523.6 | +0.1% | −1.0798 to +1.9838 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.1 | 431 | −17.6% | −139.6580 to −44.6548 | yes: GAIN |
| response time (ms), mean | 277.7 | 297.7 | +7.2% | −12.7329 to +52.7331 | no |
| response time (ms), 95th percentile | 908.5 | 1109 | +22.1% | +64.1717 to +336.5433 | yes: LOSS |
| response time (ms), 99th percentile | 1262 | 1572 | +24.5% | +104.5946 to +514.9694 | yes: LOSS |
| time over the response line (% of samples) | 11.06 | 15.31 | +38.4% | +1.1169 to +7.3831 | yes: LOSS |
| failed requests (%) | 0.006849 | 0 | −100.0% | −0.0223 to +0.0086 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 9 | +30.4% | −0.2951 to +4.4951 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 252.6 | +252.600 (native is 0) | +154.2805 to +350.9195 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.102 | 18.53 | +128.7% | −9.8176 to +30.6642 | no |
| utilisation (used / allocatable) | 0.03053 | 0.04034 | +32.1% | +0.0040 to +0.0156 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.429 | −2.5% | −0.1100 to +0.0368 | no |
| Omni's own CPU (cores), mean | 0 | 0.05162 | +0.052 (native is 0) | +0.0476 to +0.0557 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.48 | +1.0% | −0.0563 to +0.0863 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.4 | 716.7 | −17.2% | −235.7829 to −61.6028 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.91 | 4.364 | +11.6% | +0.1612 to +0.7480 | yes: power given |
| pods started | 0.3 | 1.1 | +266.7% | −0.3583 to +1.9583 | no |
| pod start wait, total (s) | 0.6 | 2.5 | +316.7% | −0.8898 to +4.6898 | no |
| pod start wait, mean (s) | 0.4 | 0.89 | +122.5% | −0.2491 to +1.2291 | no |
| host CPU busy, the real machine under kind (%) | 44.71 | 49.57 | +10.9% | +3.7844 to +5.9491 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.3 | 791.7 | +2.4% | −1.5809 to +38.3809 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 6.997 | −41.7% | −7.1936 to −2.8122 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.05833 | +7.7% | −0.0528 to +0.0612 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | −50.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.17 | 102.9 | +28.3% | +2.1066 to +43.2851 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.057 | −24.5% | −4.4552 to −1.4300 | yes: GAIN |
| node-hours | 5.021 | 3.802 | −24.3% | −1.8487 to −0.5889 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.8 | 523.6 | +0.1% | −0.6034 to +2.0934 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.8 | 431 | −17.6% | −139.2232 to −44.5034 | yes: GAIN |
| response time (ms), mean | 413.9 | 297.7 | −28.1% | −199.7228 to −32.6834 | yes: GAIN |
| response time (ms), 95th percentile | 1445 | 1109 | −23.2% | −631.6072 to −39.7438 | yes: GAIN |
| response time (ms), 99th percentile | 2043 | 1572 | −23.1% | −836.6212 to −105.3798 | yes: GAIN |
| time over the response line (% of samples) | 19.13 | 15.31 | −20.0% | −6.3170 to −1.3336 | yes: GAIN |
| failed requests (%) | 0.008547 | 0 | −100.0% | −0.0279 to +0.0108 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 9 | −21.7% | −4.6125 to −0.3875 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 252.6 | +252.600 (native is 0) | +154.2805 to +350.9195 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.95 | 18.53 | +55.0% | −7.9653 to +21.1119 | no |
| utilisation (used / allocatable) | 0.03177 | 0.04034 | +27.0% | +0.0033 to +0.0139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.525 | 1.429 | −6.3% | −0.1478 to −0.0446 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05162 | +0.052 (native is 0) | +0.0476 to +0.0557 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.525 | 1.48 | −2.9% | −0.0953 to +0.0061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.9 | 716.7 | −13.5% | −186.4801 to −38.0396 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.128 | 4.364 | +5.7% | −0.2229 to +0.6954 | no |
| pods started | 0.2 | 1.1 | +450.0% | −0.3367 to +2.1367 | no |
| pod start wait, total (s) | 0.3 | 2.5 | +733.3% | −0.5969 to +4.9969 | no |
| pod start wait, mean (s) | 0.3 | 0.89 | +196.7% | −0.2196 to +1.3996 | no |
| host CPU busy, the real machine under kind (%) | 50.28 | 49.57 | −1.4% | −1.6588 to +0.2407 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.1 | 791.7 | −5.0% | −72.4318 to −10.3682 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 6.997 | −41.7% | −7.1936 to −2.8122 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 2.367 | 0.05833 | −97.5% | −7.2160 to +2.5993 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.2 | −81.8% | −1.5263 to −0.2737 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 127.9 | 102.9 | −19.6% | −36.4858 to −13.5642 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.947 | −17.1% | −3.3342 to −0.7722 | yes: GAIN |
| node-hours | 5.031 | 4.171 | −17.1% | −1.3959 to −0.3237 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.1 | 526 | +0.6% | +1.1346 to +4.6728 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.1 | 461.4 | −11.8% | −102.7723 to −20.5953 | yes: GAIN |
| response time (ms), mean | 277.7 | 612.3 | +120.5% | +156.5274 to +512.7746 | yes: LOSS |
| response time (ms), 95th percentile | 908.5 | 2494 | +174.5% | +936.9422 to +2233.9458 | yes: LOSS |
| response time (ms), 99th percentile | 1262 | 3361 | +166.2% | +1269.1227 to +2927.2397 | yes: LOSS |
| time over the response line (% of samples) | 11.06 | 27.52 | +148.9% | +8.5362 to +24.3874 | yes: LOSS |
| failed requests (%) | 0.006849 | 0.1 | +1360.0% | −0.1176 to +0.3039 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 13.2 | +91.3% | +1.9028 to +10.6972 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 152 | +152.000 (native is 0) | +49.4710 to +254.5290 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.102 | 19.34 | +138.7% | +5.4685 to +17.0048 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03053 | 0.0412 | +35.0% | +0.0071 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.633 | +11.4% | +0.0605 to +0.2737 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0503 | +0.050 (native is 0) | +0.0463 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.683 | +14.8% | +0.1115 to +0.3233 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.4 | 678.5 | −21.6% | −248.0415 to −125.6744 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.91 | 4.316 | +10.4% | +0.1165 to +0.6957 | yes: power given |
| pods started | 0.3 | 1.7 | +466.7% | +0.4952 to +2.3048 | yes: power given |
| pod start wait, total (s) | 0.6 | 4.1 | +583.3% | +0.5363 to +6.4637 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.8 | +350.0% | +0.4796 to +2.3204 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.71 | 57.22 | +28.0% | +9.9042 to +15.1190 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.3 | 920.2 | +19.0% | +86.1906 to +207.6094 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.849 | −34.6% | −6.0685 to −2.2341 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 4.112 | +7492.3% | −4.2120 to +12.3287 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 41.1 | +10175.0% | −49.1027 to +130.5027 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.17 | 216.4 | +169.9% | +82.6316 to +189.7434 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*