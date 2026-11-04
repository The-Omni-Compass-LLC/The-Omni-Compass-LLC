# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.207 | 6 |
| node-hours | 2.51 | 2.519 | 2.184 | 2.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.5 | 273.8 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 272.5 | 248.9 | 271.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 419.6 | 143 | 415.7 | 119.4 |
| response time (ms), 95th percentile | 1539 | 253.4 | 1814 | 263.1 |
| response time (ms), 99th percentile | 2205 | 370.7 | 2622 | 391.6 |
| time over the response line (% of samples) | 19.48 | 0.3175 | 19.41 | 0.4232 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0.2 | 11 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 114.9 | 106.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 1260 | 11.61 | 1338 |
| utilisation (used / allocatable) | 0.06365 | 0.05914 | 0.07435 | 0.05829 |
| CPU used (cores), mean | 1.528 | 1.419 | 1.512 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07299 | 0.07163 |
| CPU used with Omni's own (cores), mean | 1.528 | 1.419 | 1.585 | 1.471 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 457.5 | 394.4 | 463.2 |
| HPA replicas, mean | 1.97 | 2.109 | 2.647 | 2.229 |
| pods started | 0 | 0.1 | 2.5 | 0.9 |
| pod start wait, total (s) | 0 | 0.2 | 5.4 | 1.8 |
| pod start wait, mean (s) | 0 | 0.2 | 1.55 | 0.625 |
| host CPU busy, the real machine under kind (%) | 43.22 | 45.65 | 46.17 | 46.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 801.4 | 1485 | 812.9 | 1486 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.765 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 169.6 | 0.05 | 187.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 808.1 | 0.3 | 818.5 |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 916.8 | 119.8 | 927 |
| queue: jobs unfinished at the window's end | 0 | 13.4 | 0 | 14.3 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.519 | 2.512 | −0.3% | −0.0144 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 271.2 | −0.5% | −2.0529 to −0.5420 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 271.2 | −0.5% | −2.0529 to −0.5420 | yes: GAIN |
| response time (ms), mean | 143 | 119.4 | −16.5% | −29.9468 to −17.1941 | yes: GAIN |
| response time (ms), 95th percentile | 253.4 | 263.1 | +3.8% | −5.2485 to +24.6475 | no |
| response time (ms), 99th percentile | 370.7 | 391.6 | +5.6% | −8.7063 to +50.4993 | no |
| time over the response line (% of samples) | 0.3175 | 0.4232 | +33.3% | −0.1052 to +0.3164 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.3 | +106.300 (native is 0) | +92.9389 to +119.6611 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1260 | 1338 | +6.2% | +24.4873 to +131.0627 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05914 | 0.05829 | −1.4% | −0.0025 to +0.0008 | no |
| CPU used (cores), mean | 1.419 | 1.399 | −1.4% | −0.0599 to +0.0192 | no |
| Omni's own CPU (cores), mean | 0 | 0.07163 | +0.072 (native is 0) | +0.0629 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.471 | +3.6% | +0.0112 to +0.0913 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 463.2 | +1.3% | −6.3347 to +17.8858 | no |
| HPA replicas, mean | 2.109 | 2.229 | +5.7% | −0.2062 to +0.4455 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.3583 to +1.9583 | no |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | −0.6418 to +3.8418 | no |
| pod start wait, mean (s) | 0.2 | 0.625 | +212.5% | −0.5139 to +1.3639 | no |
| host CPU busy, the real machine under kind (%) | 45.65 | 46.9 | +2.7% | +0.3868 to +2.1136 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1485 | 1486 | +0.1% | −11.4519 to +13.8519 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 169.6 | 187.3 | +10.5% | −21.2876 to +56.8126 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 808.1 | 818.5 | +1.3% | −192.1882 to +212.9882 | no |
| queue: job turnaround, submitted to done, mean (s) | 916.8 | 927 | +1.1% | −33.0927 to +53.3427 | no |
| queue: jobs unfinished at the window's end | 13.4 | 14.3 | +6.7% | −1.0502 to +2.8502 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.519 | +0.4% | +0.0019 to +0.0168 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.5 | −0.3% | −3.3072 to +1.8078 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 272.5 | −0.3% | −3.3072 to +1.8078 | no |
| response time (ms), mean | 419.6 | 143 | −65.9% | −432.4235 to −120.7188 | yes: GAIN |
| response time (ms), 95th percentile | 1539 | 253.4 | −83.5% | −2023.7390 to −547.7780 | yes: GAIN |
| response time (ms), 99th percentile | 2205 | 370.7 | −83.2% | −2888.4581 to −779.3563 | yes: GAIN |
| time over the response line (% of samples) | 19.48 | 0.3175 | −98.4% | −30.2499 to −8.0777 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0.2 | −98.0% | −14.1024 to −5.4976 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 1260 | +11432.5% | +1021.5856 to +1477.1677 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06365 | 0.05914 | −7.1% | −0.0109 to +0.0019 | no |
| CPU used (cores), mean | 1.528 | 1.419 | −7.1% | −0.2616 to +0.0455 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.528 | 1.419 | −7.1% | −0.2616 to +0.0455 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 457.5 | +5.1% | −20.0849 to +64.3241 | no |
| HPA replicas, mean | 1.97 | 2.109 | +7.0% | −0.0137 to +0.2913 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.22 | 45.65 | +5.6% | −1.1107 to +5.9766 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.4 | 1485 | +85.3% | +621.0096 to +746.1904 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 169.6 | +150644.4% | +139.9735 to +198.9765 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 808.1 | +100912.5% | +643.7268 to +970.8732 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 916.8 | +757.3% | +713.4747 to +906.3337 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.4 | +13.400 (native is 0) | +8.2396 to +18.5604 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.207 | −13.2% | −1.6320 to +0.0458 | no |
| node-hours | 2.51 | 2.184 | −13.0% | −0.6795 to +0.0266 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.8 | +0.2% | −0.7510 to +1.8127 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 248.9 | −8.9% | −51.3279 to +2.5979 | no |
| response time (ms), mean | 419.6 | 415.7 | −0.9% | −30.3406 to +22.5428 | no |
| response time (ms), 95th percentile | 1539 | 1814 | +17.9% | +69.7181 to +480.0509 | yes: LOSS |
| response time (ms), 99th percentile | 2205 | 2622 | +18.9% | +57.6659 to +777.4637 | yes: LOSS |
| time over the response line (% of samples) | 19.48 | 19.41 | −0.4% | −0.9199 to +0.7767 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11 | +10.0% | −0.0116 to +2.0116 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.9 | +114.900 (native is 0) | +44.7282 to +185.0718 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 11.6 | +6.2% | −1.0187 to +2.3721 | no |
| utilisation (used / allocatable) | 0.06365 | 0.07435 | +16.8% | −0.0006 to +0.0220 | no |
| CPU used (cores), mean | 1.528 | 1.512 | −1.0% | −0.0569 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.07299 | +0.073 (native is 0) | +0.0662 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.528 | 1.585 | +3.8% | +0.0104 to +0.1050 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 394.4 | −9.4% | −82.1837 to +0.3550 | no |
| HPA replicas, mean | 1.97 | 2.647 | +34.4% | +0.3924 to +0.9616 | yes: power given |
| pods started | 0 | 2.5 | +2.500 (native is 0) | +1.3690 to +3.6310 | yes: power given |
| pod start wait, total (s) | 0 | 5.4 | +5.400 (native is 0) | +2.3058 to +8.4942 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.55 | +1.550 (native is 0) | +0.7302 to +2.3698 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.22 | 46.17 | +6.8% | +2.1619 to +3.7443 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.4 | 812.9 | +1.4% | +0.4635 to +22.5365 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.765 | −20.6% | −2.4139 to −0.0553 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.05 | −55.6% | −0.1483 to +0.0233 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | −62.5% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 119.8 | +12.0% | +3.2141 to +22.4859 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.207 | −13.2% | −1.6320 to +0.0458 | no |
| node-hours | 2.519 | 2.184 | −13.3% | −0.6893 to +0.0177 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 273.8 | +0.5% | −1.8393 to +4.4003 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 248.9 | −8.7% | −52.3897 to +5.1590 | no |
| response time (ms), mean | 143 | 415.7 | +190.7% | +110.8378 to +434.5067 | yes: LOSS |
| response time (ms), 95th percentile | 253.4 | 1814 | +615.8% | +698.0713 to +2423.2147 | yes: LOSS |
| response time (ms), 99th percentile | 370.7 | 2622 | +607.3% | +1010.7522 to +3492.1918 | yes: LOSS |
| time over the response line (% of samples) | 0.3175 | 19.41 | +6012.6% | +8.6040 to +29.5805 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 11 | +5400.0% | +6.7145 to +14.8855 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.9 | +114.900 (native is 0) | +44.7282 to +185.0718 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1260 | 11.61 | −99.1% | −1475.9858 to −1021.4142 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05914 | 0.07435 | +25.7% | +0.0072 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.512 | +6.5% | −0.0905 to +0.2761 | no |
| Omni's own CPU (cores), mean | 0 | 0.07299 | +0.073 (native is 0) | +0.0662 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.585 | +11.7% | −0.0238 to +0.3554 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 394.4 | −13.8% | −91.0454 to −35.0225 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.109 | 2.647 | +25.5% | +0.2016 to +0.8748 | yes: power given |
| pods started | 0.1 | 2.5 | +2400.0% | +1.1293 to +3.6707 | yes: power given |
| pod start wait, total (s) | 0.2 | 5.4 | +2600.0% | +1.8824 to +8.5176 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.55 | +675.0% | +0.2413 to +2.4587 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.65 | 46.17 | +1.1% | −3.5256 to +4.5659 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1485 | 812.9 | −45.3% | −735.9032 to −608.2968 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 169.6 | 0.05 | −100.0% | −199.0438 to −140.0312 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 808.1 | 0.3 | −100.0% | −971.4516 to −644.1484 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 916.8 | 119.8 | −86.9% | −889.2455 to −704.8628 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.4 | 0 | −100.0% | −18.5604 to −8.2396 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.512 | +0.1% | −0.0042 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 271.2 | −0.7% | −4.8087 to +0.7145 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 271.2 | −0.7% | −4.8087 to +0.7145 | no |
| response time (ms), mean | 419.6 | 119.4 | −71.5% | −458.9229 to −141.3603 | yes: GAIN |
| response time (ms), 95th percentile | 1539 | 263.1 | −82.9% | −2009.0351 to −543.0829 | yes: GAIN |
| response time (ms), 99th percentile | 2205 | 391.6 | −82.2% | −2856.1057 to −769.9157 | yes: GAIN |
| time over the response line (% of samples) | 19.48 | 0.4232 | −97.8% | −30.0970 to −8.0193 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0.3 | −97.0% | −13.9659 to −5.4341 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.3 | +106.300 (native is 0) | +92.9389 to +119.6611 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 1338 | +12144.1% | +1091.6356 to +1562.6678 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06365 | 0.05829 | −8.4% | −0.0121 to +0.0014 | no |
| CPU used (cores), mean | 1.528 | 1.399 | −8.4% | −0.2903 to +0.0334 | no |
| Omni's own CPU (cores), mean | 0 | 0.07163 | +0.072 (native is 0) | +0.0629 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.528 | 1.471 | −3.7% | −0.2107 to +0.0970 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 463.2 | +6.4% | −16.6670 to +72.4573 | no |
| HPA replicas, mean | 1.97 | 2.229 | +13.1% | +0.0162 to +0.5007 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0 | 1.8 | +1.800 (native is 0) | −0.3004 to +3.9004 | no |
| pod start wait, mean (s) | 0 | 0.625 | +0.625 (native is 0) | −0.1063 to +1.3563 | no |
| host CPU busy, the real machine under kind (%) | 43.22 | 46.9 | +8.5% | +0.1534 to +7.2129 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.4 | 1486 | +85.5% | +627.6830 to +741.9170 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 187.4 | +166433.3% | +143.5607 to +230.9143 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 818.5 | +102212.5% | +662.7802 to +972.6198 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 927 | +766.8% | +742.7819 to +897.2765 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.3 | +14.300 (native is 0) | +9.2302 to +19.3698 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*