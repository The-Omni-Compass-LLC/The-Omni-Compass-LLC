# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.855 | 5.982 |
| node-hours | 2.514 | 2.519 | 2.035 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | 272.7 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | 236.8 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 378.4 | 138 | 357.7 | 114.5 |
| response time (ms), 95th percentile | 1353 | 240.6 | 1464 | 252.5 |
| response time (ms), 99th percentile | 1934 | 345 | 2081 | 371.3 |
| time over the response line (% of samples) | 17.11 | 0.2247 | 17.09 | 0.3468 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0 | 10 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 111.3 | 119.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 1168 | 10.97 | 1267 |
| utilisation (used / allocatable) | 0.06088 | 0.05926 | 0.07579 | 0.0585 |
| CPU used (cores), mean | 1.461 | 1.422 | 1.446 | 1.4 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07442 | 0.07302 |
| CPU used with Omni's own (cores), mean | 1.461 | 1.422 | 1.52 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 457.2 | 392.9 | 462.4 |
| HPA replicas, mean | 2.014 | 2.05 | 2.188 | 2.373 |
| pods started | 0 | 0.1 | 1 | 1.8 |
| pod start wait, total (s) | 0 | 0.1 | 2.3 | 4.2 |
| pod start wait, mean (s) | 0 | 0.1 | 0.9 | 1.408 |
| host CPU busy, the real machine under kind (%) | 41.73 | 44.9 | 44.83 | 46.84 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 788.7 | 1448 | 795.7 | 1482 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.214 | 5 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.8 | 0.07917 | 187.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 642.9 | 0.4 | 806.7 |
| queue: job turnaround, submitted to done, mean (s) | 95.15 | 874.9 | 100.9 | 885.4 |
| queue: jobs unfinished at the window's end | 0 | 11.1 | 0 | 12.2 |
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
| worker nodes in service, mean | 6 | 5.982 | −0.3% | −0.0595 to +0.0230 | no |
| node-hours | 2.519 | 2.51 | −0.4% | −0.0281 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | −0.2% | −1.6506 to +0.6279 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.3 | −0.4% | −2.5581 to +0.3854 | no |
| response time (ms), mean | 138 | 114.5 | −17.0% | −30.7088 to −16.0950 | yes: GAIN |
| response time (ms), 95th percentile | 240.6 | 252.5 | +4.9% | −0.8454 to +24.6014 | no |
| response time (ms), 99th percentile | 345 | 371.3 | +7.6% | −9.6901 to +62.2735 | no |
| time over the response line (% of samples) | 0.2247 | 0.3468 | +54.4% | −0.1142 to +0.3585 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.2 | +119.200 (native is 0) | +97.1765 to +141.2235 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1168 | 1267 | +8.5% | +42.5632 to +155.4201 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05926 | 0.0585 | −1.3% | −0.0021 to +0.0006 | no |
| CPU used (cores), mean | 1.422 | 1.4 | −1.6% | −0.0487 to +0.0043 | no |
| Omni's own CPU (cores), mean | 0 | 0.07302 | +0.073 (native is 0) | +0.0663 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.422 | 1.473 | +3.6% | +0.0261 to +0.0755 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.2 | 462.4 | +1.1% | −4.2523 to +14.6139 | no |
| HPA replicas, mean | 2.05 | 2.373 | +15.8% | +0.0022 to +0.6446 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.4819 to +2.9181 | yes: power given |
| pod start wait, total (s) | 0.1 | 4.2 | +4100.0% | +1.1134 to +7.0866 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.408 | +1308.3% | +0.3496 to +2.2671 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.9 | 46.84 | +4.3% | +1.1950 to +2.7003 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1448 | 1482 | +2.3% | −28.8862 to +95.6862 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 151.8 | 187.1 | +23.3% | −7.7673 to +78.4089 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 642.9 | 806.7 | +25.5% | −33.1427 to +360.7427 | no |
| queue: job turnaround, submitted to done, mean (s) | 874.9 | 885.4 | +1.2% | −35.9710 to +56.9460 | no |
| queue: jobs unfinished at the window's end | 11.1 | 12.2 | +9.9% | −0.0898 to +2.2898 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.519 | +0.2% | −0.0023 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | −0.1% | −2.1203 to +1.6191 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | −0.1% | −2.1203 to +1.6191 | no |
| response time (ms), mean | 378.4 | 138 | −63.5% | −391.3235 to −89.6266 | yes: GAIN |
| response time (ms), 95th percentile | 1353 | 240.6 | −82.2% | −1821.6571 to −403.8049 | yes: GAIN |
| response time (ms), 99th percentile | 1934 | 345 | −82.2% | −2617.9868 to −560.4552 | yes: GAIN |
| time over the response line (% of samples) | 17.11 | 0.2247 | −98.7% | −28.0333 to −5.7349 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0 | −100.0% | −13.5024 to −4.8976 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 1168 | +11191.0% | +887.1902 to +1427.4898 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06088 | 0.05926 | −2.7% | −0.0080 to +0.0047 | no |
| CPU used (cores), mean | 1.461 | 1.422 | −2.7% | −0.1919 to +0.1140 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.461 | 1.422 | −2.7% | −0.1919 to +0.1140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 457.2 | −0.1% | −45.0664 to +44.3151 | no |
| HPA replicas, mean | 2.014 | 2.05 | +1.8% | −0.1035 to +0.1750 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 41.73 | 44.9 | +7.6% | −0.2199 to +6.5496 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.7 | 1448 | +83.6% | +577.2197 to +741.9803 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.8 | +331000.0% | +105.1472 to +198.2695 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 642.9 | +214200.0% | +445.7649 to +839.4351 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 95.15 | 874.9 | +819.5% | +645.2004 to +914.3246 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.1 | +11.100 (native is 0) | +5.3731 to +16.8269 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.855 | −19.1% | −2.0378 to −0.2516 | yes: GAIN |
| node-hours | 2.514 | 2.035 | −19.0% | −0.8580 to −0.0989 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 | +0.0% | −1.0992 to +1.2769 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 236.8 | −13.2% | −64.7639 to −6.9543 | yes: GAIN |
| response time (ms), mean | 378.4 | 357.7 | −5.5% | −30.9674 to −10.5062 | yes: GAIN |
| response time (ms), 95th percentile | 1353 | 1464 | +8.1% | +36.6568 to +183.7742 | yes: LOSS |
| response time (ms), 99th percentile | 1934 | 2081 | +7.6% | −61.7178 to +354.8916 | no |
| time over the response line (% of samples) | 17.11 | 17.09 | −0.1% | −0.8864 to +0.8541 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10 | +8.7% | +0.3476 to +1.2524 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.3 | +111.300 (native is 0) | +38.4088 to +184.1912 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 10.97 | +6.1% | −0.9836 to +2.2436 | no |
| utilisation (used / allocatable) | 0.06088 | 0.07579 | +24.5% | +0.0033 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.461 | 1.446 | −1.1% | −0.0536 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.07442 | +0.074 (native is 0) | +0.0690 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.52 | +4.0% | +0.0187 to +0.0992 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 392.9 | −14.1% | −114.0367 to −15.3856 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.188 | +8.6% | −0.0241 to +0.3715 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.0116 to +2.0116 | no |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | −0.0855 to +4.6855 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.0585 to +1.7415 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.73 | 44.83 | +7.4% | +2.7735 to +3.4293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.7 | 795.7 | +0.9% | −0.7482 to +14.7482 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.214 | −29.8% | −3.0606 to −0.5121 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.07917 | +72.7% | −0.0394 to +0.1061 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 95.15 | 100.9 | +6.1% | +0.2177 to +11.3490 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.855 | −19.1% | −2.0378 to −0.2516 | yes: GAIN |
| node-hours | 2.519 | 2.035 | −19.2% | −0.8593 to −0.1086 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.7 | +0.1% | −2.1423 to +2.8211 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 236.8 | −13.1% | −65.9778 to −5.2392 | yes: GAIN |
| response time (ms), mean | 138 | 357.7 | +159.3% | +67.0080 to +372.4685 | yes: LOSS |
| response time (ms), 95th percentile | 240.6 | 1464 | +508.3% | +455.7602 to +1990.1328 | yes: LOSS |
| response time (ms), 99th percentile | 345 | 2081 | +503.2% | +647.1915 to +2824.4243 | yes: LOSS |
| time over the response line (% of samples) | 0.2247 | 17.09 | +7507.4% | +6.1868 to +27.5490 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10 | +10.000 (native is 0) | +5.8978 to +14.1022 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.3 | +111.300 (native is 0) | +38.4088 to +184.1912 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1168 | 10.97 | −99.1% | −1426.8004 to −886.6196 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05926 | 0.07579 | +27.9% | +0.0097 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.422 | 1.446 | +1.6% | −0.1542 to +0.2011 | no |
| Omni's own CPU (cores), mean | 0 | 0.07442 | +0.074 (native is 0) | +0.0690 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.422 | 1.52 | +6.9% | −0.0827 to +0.2784 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.2 | 392.9 | −14.1% | −82.4420 to −46.2290 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.05 | 2.188 | +6.7% | −0.0226 to +0.2985 | no |
| pods started | 0.1 | 1 | +900.0% | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0.1 | 2.3 | +2200.0% | −0.2502 to +4.6502 | no |
| pod start wait, mean (s) | 0.1 | 0.9 | +800.0% | −0.1282 to +1.7282 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 44.83 | −0.1% | −3.5782 to +3.4514 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1448 | 795.7 | −45.1% | −736.6581 to −568.5419 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.083 | −65.3% | −4.9755 to −2.8578 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 151.8 | 0.07917 | −99.9% | −198.2089 to −105.1411 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 642.9 | 0.4 | −99.9% | −839.1741 to −445.8259 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 874.9 | 100.9 | −88.5% | −906.2740 to −641.6844 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.1 | 0 | −100.0% | −16.8269 to −5.3731 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.982 | −0.3% | −0.0595 to +0.0230 | no |
| node-hours | 2.514 | 2.51 | −0.1% | −0.0242 to +0.0168 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.9 | −0.3% | −3.2250 to +1.7011 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.3 | −0.5% | −3.7033 to +1.0293 | no |
| response time (ms), mean | 378.4 | 114.5 | −69.7% | −417.7509 to −110.0030 | yes: GAIN |
| response time (ms), 95th percentile | 1353 | 252.5 | −81.3% | −1807.9931 to −393.7129 | yes: GAIN |
| response time (ms), 99th percentile | 1934 | 371.3 | −80.8% | −2598.6081 to −527.2505 | yes: GAIN |
| time over the response line (% of samples) | 17.11 | 0.3468 | −98.0% | −27.9436 to −5.5803 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0.2 | −97.8% | −13.1845 to −4.8155 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.2 | +119.200 (native is 0) | +97.1765 to +141.2235 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 1267 | +12148.3% | +1006.1945 to +1506.4688 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06088 | 0.0585 | −3.9% | −0.0095 to +0.0047 | no |
| CPU used (cores), mean | 1.461 | 1.4 | −4.2% | −0.2279 to +0.1056 | no |
| Omni's own CPU (cores), mean | 0 | 0.07302 | +0.073 (native is 0) | +0.0663 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.473 | +0.8% | −0.1492 to +0.1730 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 462.4 | +1.1% | −45.1420 to +54.7523 | no |
| HPA replicas, mean | 2.014 | 2.373 | +17.8% | +0.1021 to +0.6162 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.5936 to +3.0064 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.200 (native is 0) | +1.2449 to +7.1551 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.408 | +1.408 (native is 0) | +0.4711 to +2.3456 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.73 | 46.84 | +12.3% | +1.3495 to +8.8754 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.7 | 1482 | +87.9% | +626.0917 to +759.9083 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 187.1 | +408063.6% | +138.9615 to +235.0969 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 806.7 | +268800.0% | +608.0865 to +1004.7135 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 95.15 | 885.4 | +830.5% | +690.1010 to +890.3990 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.2 | +12.200 (native is 0) | +6.4795 to +17.9205 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*