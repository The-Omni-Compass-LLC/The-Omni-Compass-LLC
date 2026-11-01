# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.8 | 4.647 |
| node-hours | 2.513 | 2.515 | 2.014 | 1.944 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | 272.7 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.9 | 234.9 | 229.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 364.8 | 300.8 | 317.6 | 259.7 |
| response time (ms), 95th percentile | 1365 | 1126 | 1288 | 1094 |
| response time (ms), 99th percentile | 2021 | 1704 | 1789 | 1738 |
| time over the response line (% of samples) | 13.72 | 10.71 | 13.7 | 10.44 |
| failed requests (%) | 0.02597 | 0.02114 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6 | 7.6 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 47.5 | 41.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.01 | 17.8 | 11.43 | 16.56 |
| utilisation (used / allocatable) | 0.06119 | 0.06133 | 0.07524 | 0.07757 |
| CPU used (cores), mean | 1.468 | 1.472 | 1.429 | 1.427 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01661 | 0.01644 |
| CPU used with Omni's own (cores), mean | 1.468 | 1.472 | 1.445 | 1.443 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 455.3 | 395.2 | 387.5 |
| HPA replicas, mean | 2.027 | 2.002 | 1.988 | 2.043 |
| pods started | 0.3 | 0 | 0.3 | 0.3 |
| pod start wait, total (s) | 0.7 | 0 | 0.7 | 0.8 |
| pod start wait, mean (s) | 0.7 | 0 | 0.7 | 0.5 |
| host CPU busy, the real machine under kind (%) | 41.36 | 42.33 | 42.16 | 43.13 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 790.8 | 802.8 | 794.4 | 804.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.962 | 3.787 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.8042 | 0.2083 | 0.7625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.5 | 1.9 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 95.99 | 112.9 | 98.93 | 113.2 |
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
| worker nodes in service, mean | 6 | 4.647 | −22.6% | −2.2233 to −0.4828 | yes: GAIN |
| node-hours | 2.515 | 1.944 | −22.7% | −0.9322 to −0.2083 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.1 | −0.3% | −1.5700 to −0.1381 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 229.6 | −15.9% | −70.7102 to −15.9604 | yes: GAIN |
| response time (ms), mean | 300.8 | 259.7 | −13.7% | −65.5103 to −16.8379 | yes: GAIN |
| response time (ms), 95th percentile | 1126 | 1094 | −2.8% | −203.3708 to +139.6838 | no |
| response time (ms), 99th percentile | 1704 | 1738 | +2.0% | −98.1645 to +165.7651 | no |
| time over the response line (% of samples) | 10.71 | 10.44 | −2.5% | −1.3057 to +0.7639 | no |
| failed requests (%) | 0.02114 | 0 | −100.0% | −0.0531 to +0.0108 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.3 | +5.0% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 | +41.100 (native is 0) | +25.7901 to +56.4099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.8 | 16.56 | −7.0% | −2.8176 to +0.3376 | no |
| utilisation (used / allocatable) | 0.06133 | 0.07757 | +26.5% | +0.0056 to +0.0269 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.472 | 1.427 | −3.1% | −0.0956 to +0.0050 | no |
| Omni's own CPU (cores), mean | 0 | 0.01644 | +0.016 (native is 0) | +0.0145 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.472 | 1.443 | −2.0% | −0.0808 to +0.0231 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 387.5 | −14.9% | −111.0493 to −24.3909 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.043 | +2.1% | −0.1103 to +0.1936 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.5821 to +2.1821 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 42.33 | 43.13 | +1.9% | +0.3276 to +1.2676 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.8 | 804.2 | +0.2% | −1.5435 to +4.3435 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.787 | −36.9% | −3.5932 to −0.8324 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8042 | 0.7625 | −5.2% | −0.2611 to +0.1778 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.7 | +13.3% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.9 | 113.2 | +0.2% | −4.7576 to +5.1909 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.515 | +0.1% | −0.0049 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.4023 to +0.8204 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.9 | +0.1% | −0.4023 to +0.8204 | no |
| response time (ms), mean | 364.8 | 300.8 | −17.5% | −120.6598 to −7.2040 | yes: GAIN |
| response time (ms), 95th percentile | 1365 | 1126 | −17.5% | −493.1632 to +16.3442 | no |
| response time (ms), 99th percentile | 2021 | 1704 | −15.7% | −1004.1803 to +371.0095 | no |
| time over the response line (% of samples) | 13.72 | 10.71 | −21.9% | −5.5620 to −0.4533 | yes: GAIN |
| failed requests (%) | 0.02597 | 0.02114 | −18.6% | −0.0470 to +0.0373 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6 | −21.1% | −3.7905 to +0.5905 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.01 | 17.8 | +61.7% | +2.2099 to +11.3701 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06119 | 0.06133 | +0.2% | −0.0010 to +0.0012 | no |
| CPU used (cores), mean | 1.468 | 1.472 | +0.2% | −0.0230 to +0.0300 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.468 | 1.472 | +0.2% | −0.0230 to +0.0300 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 455.3 | +0.1% | −8.7656 to +9.6815 | no |
| HPA replicas, mean | 2.027 | 2.002 | −1.2% | −0.1671 to +0.1169 | no |
| pods started | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| pod start wait, total (s) | 0.7 | 0 | −100.0% | −1.5294 to +0.1294 | no |
| pod start wait, mean (s) | 0.7 | 0 | −100.0% | −1.5294 to +0.1294 | no |
| host CPU busy, the real machine under kind (%) | 41.36 | 42.33 | +2.4% | +0.5711 to +1.3765 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 790.8 | 802.8 | +1.5% | +1.8784 to +22.1216 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.8042 | +484.8% | +0.4016 to +0.9318 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.5 | +114.3% | −0.0793 to +1.6793 | no |
| queue: job turnaround, submitted to done, mean (s) | 95.99 | 112.9 | +17.7% | +2.7013 to +31.2070 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.8 | −20.0% | −2.0195 to −0.3806 | yes: GAIN |
| node-hours | 2.513 | 2.014 | −19.9% | −0.8410 to −0.1573 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.7 | −0.0% | −0.7631 to +0.6814 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 234.9 | −13.9% | −63.6199 to −12.0577 | yes: GAIN |
| response time (ms), mean | 364.8 | 317.6 | −12.9% | −94.7469 to +0.3123 | no |
| response time (ms), 95th percentile | 1365 | 1288 | −5.6% | −328.6449 to +175.3939 | no |
| response time (ms), 99th percentile | 2021 | 1789 | −11.5% | −843.7883 to +378.8743 | no |
| time over the response line (% of samples) | 13.72 | 13.7 | −0.1% | −0.6524 to +0.6163 | no |
| failed requests (%) | 0.02597 | 0 | −100.0% | −0.0847 to +0.0328 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.6 | ±0.0% | −0.7540 to +0.7540 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 | +47.500 (native is 0) | +25.5892 to +69.4108 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.01 | 11.43 | +3.8% | −1.1530 to +1.9964 | no |
| utilisation (used / allocatable) | 0.06119 | 0.07524 | +23.0% | +0.0041 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.468 | 1.429 | −2.7% | −0.0732 to −0.0064 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01661 | +0.017 (native is 0) | +0.0147 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.468 | 1.445 | −1.6% | −0.0570 to +0.0106 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 395.2 | −13.1% | −101.0704 to −18.1663 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 1.988 | −1.9% | −0.1879 to +0.1105 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.7 | 0.7 | ±0.0% | −1.3903 to +1.3903 | no |
| pod start wait, mean (s) | 0.7 | 0.7 | ±0.0% | −1.3903 to +1.3903 | no |
| host CPU busy, the real machine under kind (%) | 41.36 | 42.16 | +1.9% | +0.6030 to +1.0053 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 790.8 | 794.4 | +0.5% | +0.1250 to +7.0750 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.962 | −34.0% | −3.3810 to −0.6948 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.2083 | +51.5% | −0.0704 to +0.2121 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.9 | +171.4% | −1.2733 to +3.6733 | no |
| queue: job turnaround, submitted to done, mean (s) | 95.99 | 98.93 | +3.1% | −1.1361 to +7.0111 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.8 | −20.0% | −2.0195 to −0.3806 | yes: GAIN |
| node-hours | 2.515 | 2.014 | −19.9% | −0.8412 to −0.1610 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.7 | −0.1% | −1.0773 to +0.5774 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 234.9 | −13.9% | −63.4834 to −12.6124 | yes: GAIN |
| response time (ms), mean | 300.8 | 317.6 | +5.6% | −13.9659 to +47.3951 | no |
| response time (ms), 95th percentile | 1126 | 1288 | +14.4% | −7.8589 to +331.4269 | no |
| response time (ms), 99th percentile | 1704 | 1789 | +4.9% | −114.0195 to +282.2763 | no |
| time over the response line (% of samples) | 10.71 | 13.7 | +27.9% | +0.6965 to +5.2827 | yes: LOSS |
| failed requests (%) | 0.02114 | 0 | −100.0% | −0.0531 to +0.0108 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 7.6 | +26.7% | −0.4841 to +3.6841 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 | +47.500 (native is 0) | +25.5892 to +69.4108 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.8 | 11.43 | −35.8% | −9.9036 to −2.8331 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06133 | 0.07524 | +22.7% | +0.0033 to +0.0245 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.472 | 1.429 | −2.9% | −0.0728 to −0.0138 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01661 | +0.017 (native is 0) | +0.0147 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.472 | 1.445 | −1.8% | −0.0574 to +0.0040 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 395.2 | −13.2% | −105.3889 to −14.7638 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 1.988 | −0.7% | −0.1732 to +0.1460 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| host CPU busy, the real machine under kind (%) | 42.33 | 42.16 | −0.4% | −0.5324 to +0.1932 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.8 | 794.4 | −1.0% | −16.4731 to −0.3269 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.962 | −34.0% | −3.3810 to −0.6948 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8042 | 0.2083 | −74.1% | −0.9518 to −0.2398 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.9 | +26.7% | −2.8202 to +3.6202 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.9 | 98.93 | −12.4% | −26.2903 to −1.7430 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.647 | −22.6% | −2.2233 to −0.4828 | yes: GAIN |
| node-hours | 2.513 | 1.944 | −22.6% | −0.9318 to −0.2047 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | −0.2% | −1.5002 to +0.2103 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 229.6 | −15.8% | −70.8262 to −15.4262 | yes: GAIN |
| response time (ms), mean | 364.8 | 259.7 | −28.8% | −171.5200 to −38.6921 | yes: GAIN |
| response time (ms), 95th percentile | 1365 | 1094 | −19.8% | −538.7571 to −1.7489 | yes: GAIN |
| response time (ms), 99th percentile | 2021 | 1738 | −14.0% | −949.0525 to +383.4823 | no |
| time over the response line (% of samples) | 13.72 | 10.44 | −23.9% | −5.7316 to −0.8255 | yes: GAIN |
| failed requests (%) | 0.02597 | 0 | −100.0% | −0.0847 to +0.0328 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.3 | −17.1% | −3.2385 to +0.6385 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 | +41.100 (native is 0) | +25.7901 to +56.4099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.01 | 16.56 | +50.4% | +1.6040 to +9.4960 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06119 | 0.07757 | +26.8% | +0.0062 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.468 | 1.427 | −2.8% | −0.0934 to +0.0099 | no |
| Omni's own CPU (cores), mean | 0 | 0.01644 | +0.016 (native is 0) | +0.0145 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.468 | 1.443 | −1.7% | −0.0783 to +0.0276 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 387.5 | −14.8% | −107.8206 to −26.7036 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.043 | +0.8% | −0.1642 to +0.1973 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.7 | 0.8 | +14.3% | −1.6986 to +1.8986 | no |
| pod start wait, mean (s) | 0.7 | 0.5 | −28.6% | −1.4972 to +1.0972 | no |
| host CPU busy, the real machine under kind (%) | 41.36 | 43.13 | +4.3% | +1.3187 to +2.2242 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 790.8 | 804.2 | +1.7% | +3.2325 to +23.5675 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.787 | −36.9% | −3.5932 to −0.8324 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.7625 | +454.5% | +0.5050 to +0.7450 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.7 | +142.9% | +0.2460 to +1.7540 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 95.99 | 113.2 | +17.9% | +2.5632 to +31.7785 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*