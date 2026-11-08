# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.424 | 6 |
| node-hours | 2.511 | 2.518 | 2.28 | 2.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 | 274.4 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.2 | 256.3 | 272.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 403.9 | 135.4 | 397.3 | 121.6 |
| response time (ms), 95th percentile | 1498 | 218.9 | 1720 | 271.3 |
| response time (ms), 99th percentile | 2136 | 317.7 | 2413 | 388 |
| time over the response line (% of samples) | 16.85 | 0.2264 | 17.21 | 0.2773 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 0 | 11.75 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 120.2 | 114.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 931.6 | 11.9 | 1267 |
| utilisation (used / allocatable) | 0.06255 | 0.05965 | 0.06953 | 0.05849 |
| CPU used (cores), mean | 1.501 | 1.431 | 1.507 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07537 | 0.07027 |
| CPU used with Omni's own (cores), mean | 1.501 | 1.431 | 1.582 | 1.474 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.4 | 453.1 | 408 | 461.9 |
| HPA replicas, mean | 2.103 | 2.132 | 2.591 | 2.39 |
| pods started | 0.125 | 0 | 3 | 1.333 |
| pod start wait, total (s) | 0.25 | 0 | 8.25 | 5 |
| pod start wait, mean (s) | 0.25 | 0 | 2.312 | 1.25 |
| host CPU busy, the real machine under kind (%) | 42.95 | 45.18 | 46.12 | 47.19 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 791.5 | 1512 | 802.8 | 1513 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 4.91 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06771 | 174 | 0.1094 | 181.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.625 | 587 | 0.5 | 783.7 |
| queue: job turnaround, submitted to done, mean (s) | 97.04 | 783.7 | 109.2 | 877.2 |
| queue: jobs unfinished at the window's end | 0 | 6 | 0 | 12 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| node-hours | 2.518 | 2.528 | +0.4% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 273.3 | +0.4% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 273.3 | +0.4% | ±nan to ±nan | no |
| response time (ms), mean | 135.4 | 110.4 | −18.5% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 218.9 | 223.8 | +2.3% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 317.7 | 332.3 | +4.6% | ±nan to ±nan | no |
| time over the response line (% of samples) | 0.2264 | 0.0738 | −67.4% | ±nan to ±nan | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104 | +104.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 931.6 | 1097 | +17.7% | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.05965 | 0.05966 | +0.0% | ±nan to ±nan | no |
| CPU used (cores), mean | 1.431 | 1.432 | +0.0% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0631 | +0.063 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 1.431 | 1.495 | +4.4% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.1 | 453.1 | −0.0% | ±nan to ±nan | no |
| HPA replicas, mean | 2.132 | 2.139 | +0.3% | ±nan to ±nan | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| host CPU busy, the real machine under kind (%) | 45.18 | 46.74 | +3.5% | ±nan to ±nan | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±nan to ±nan | no |
| batch: queue finished (s) | 1512 | 1518 | +0.4% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 174 | 132.7 | −23.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 587 | 588 | +0.2% | ±nan to ±nan | no |
| queue: job turnaround, submitted to done, mean (s) | 783.7 | 877 | +11.9% | ±nan to ±nan | no |
| queue: jobs unfinished at the window's end | 6 | 9 | +50.0% | ±nan to ±nan | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 1 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw ±nan to ±nan | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.518 | +0.3% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 272.2 | +0.9% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 272.2 | +0.9% | ±nan to ±nan | no |
| response time (ms), mean | 176.1 | 135.4 | −23.1% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 432.6 | 218.9 | −49.4% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 594 | 317.7 | −46.5% | ±nan to ±nan | no |
| time over the response line (% of samples) | 2.344 | 0.2264 | −90.3% | ±nan to ±nan | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 0 | −100.0% | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.183 | 931.6 | +12868.2% | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.05424 | 0.05965 | +10.0% | ±nan to ±nan | no |
| CPU used (cores), mean | 1.302 | 1.431 | +10.0% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 1.302 | 1.431 | +10.0% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.2 | 453.1 | −8.5% | ±nan to ±nan | no |
| HPA replicas, mean | 1.941 | 2.132 | +9.9% | ±nan to ±nan | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| host CPU busy, the real machine under kind (%) | 37.44 | 45.18 | +20.7% | ±nan to ±nan | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±nan to ±nan | no |
| batch: queue finished (s) | 724 | 1512 | +108.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 174 | +208650.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 587 | +58600.0% | ±nan to ±nan | no |
| queue: job turnaround, submitted to done, mean (s) | 30.75 | 783.7 | +2448.5% | ±nan to ±nan | no |
| queue: jobs unfinished at the window's end | 0 | 6 | +6.000 (native is 0) | ±nan to ±nan | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 8 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.424 | −9.6% | −1.1600 to +0.0080 | no |
| node-hours | 2.511 | 2.28 | −9.2% | −0.4798 to +0.0181 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 274.4 | +0.6% | +0.5313 to +2.5296 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 256.3 | −6.1% | −35.5311 to +2.2483 | no |
| response time (ms), mean | 403.9 | 397.3 | −1.6% | −36.0887 to +22.8155 | no |
| response time (ms), 95th percentile | 1498 | 1720 | +14.8% | −6.3152 to +449.5964 | no |
| response time (ms), 99th percentile | 2136 | 2413 | +13.0% | −20.1668 to +575.4808 | no |
| time over the response line (% of samples) | 16.85 | 17.21 | +2.1% | −0.7027 to +1.4098 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11.75 | +17.5% | +0.2180 to +3.2820 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 120.2 | +120.250 (native is 0) | +32.7453 to +207.7547 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 11.9 | +14.9% | −1.3415 to +4.4249 | no |
| utilisation (used / allocatable) | 0.06255 | 0.06953 | +11.2% | +0.0006 to +0.0134 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.501 | 1.507 | +0.4% | −0.0096 to +0.0216 | no |
| Omni's own CPU (cores), mean | 0 | 0.07537 | +0.075 (native is 0) | +0.0698 to +0.0810 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.501 | 1.582 | +5.4% | +0.0624 to +0.1004 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.4 | 408 | −7.6% | −63.5076 to −3.3057 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.103 | 2.591 | +23.2% | +0.3044 to +0.6705 | yes: power given |
| pods started | 0.125 | 3 | +2300.0% | +1.2366 to +4.5134 | yes: power given |
| pod start wait, total (s) | 0.25 | 8.25 | +3200.0% | +2.8456 to +13.1544 | yes: LOSS |
| pod start wait, mean (s) | 0.25 | 2.312 | +825.0% | +1.0936 to +3.0314 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.95 | 46.12 | +7.4% | +2.8339 to +3.5089 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 791.5 | 802.8 | +1.4% | +1.7400 to +20.7600 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.91 | −18.2% | −2.1762 to −0.0038 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06771 | 0.1094 | +61.5% | −0.0351 to +0.1184 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.625 | 0.5 | −20.0% | −0.4206 to +0.1706 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.04 | 109.2 | +12.6% | +1.1074 to +23.2572 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 1 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.558 | −24.0% | ±nan to ±nan | no |
| node-hours | 2.518 | 1.916 | −23.9% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 270.8 | −0.5% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 225.4 | −17.2% | ±nan to ±nan | no |
| response time (ms), mean | 135.4 | 149 | +10.0% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 218.9 | 469.6 | +114.5% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 317.7 | 651.2 | +105.0% | ±nan to ±nan | no |
| time over the response line (% of samples) | 0.2264 | 4.046 | +1686.9% | ±nan to ±nan | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7 | +7.000 (native is 0) | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 197 | +197.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 931.6 | 5.533 | −99.4% | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.05965 | 0.06985 | +17.1% | ±nan to ±nan | no |
| CPU used (cores), mean | 1.431 | 1.274 | −11.0% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0728 | +0.073 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 1.431 | 1.346 | −5.9% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.1 | 421 | −7.1% | ±nan to ±nan | no |
| HPA replicas, mean | 2.132 | 2.172 | +1.9% | ±nan to ±nan | no |
| pods started | 0 | 1 | +1.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, total (s) | 0 | 2 | +2.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, mean (s) | 0 | 2 | +2.000 (native is 0) | ±nan to ±nan | no |
| host CPU busy, the real machine under kind (%) | 45.18 | 40.36 | −10.7% | ±nan to ±nan | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±nan to ±nan | no |
| batch: queue finished (s) | 1512 | 728 | −51.9% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 174 | 0.04167 | −100.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 587 | 0 | −100.0% | ±nan to ±nan | no |
| queue: job turnaround, submitted to done, mean (s) | 783.7 | 31.62 | −96.0% | ±nan to ±nan | no |
| queue: jobs unfinished at the window's end | 6 | 0 | −100.0% | ±nan to ±nan | no |

## omni on top of the orchestrator vs the organism alone, 3 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.509 | 2.521 | +0.5% | −0.0412 to +0.0645 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.4 | +0.2% | −6.5349 to +7.4957 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.4 | +0.2% | −6.5349 to +7.4957 | no |
| response time (ms), mean | 356.4 | 121.6 | −65.9% | −956.5282 to +486.9094 | no |
| response time (ms), 95th percentile | 1278 | 271.3 | −78.8% | −4515.8585 to +2503.0485 | no |
| response time (ms), 99th percentile | 1831 | 388 | −78.8% | −6621.8960 to +3736.8600 | no |
| time over the response line (% of samples) | 12.58 | 0.2773 | −97.8% | −55.4276 to +30.8321 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.333 | 0 | −100.0% | −22.6767 to +6.0100 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.3 | +114.333 (native is 0) | +69.8690 to +158.7977 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.4 | 1267 | +13379.5% | +447.1732 to +2068.1712 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06051 | 0.05849 | −3.3% | −0.0305 to +0.0264 | no |
| CPU used (cores), mean | 1.452 | 1.404 | −3.3% | −0.7309 to +0.6340 | no |
| Omni's own CPU (cores), mean | 0 | 0.07027 | +0.070 (native is 0) | +0.0368 to +0.1037 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.452 | 1.474 | +1.5% | −0.6274 to +0.6710 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.2 | 461.9 | +1.5% | −175.9087 to +189.2472 | no |
| HPA replicas, mean | 2.077 | 2.39 | +15.1% | −0.0085 to +0.6348 | no |
| pods started | 0 | 1.333 | +1.333 (native is 0) | −4.4040 to +7.0707 | no |
| pod start wait, total (s) | 0 | 5 | +5.000 (native is 0) | −16.5150 to +26.5150 | no |
| pod start wait, mean (s) | 0 | 1.25 | +1.250 (native is 0) | −4.1288 to +6.6288 | no |
| host CPU busy, the real machine under kind (%) | 41.67 | 47.19 | +13.2% | −9.2528 to +20.2776 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.7 | 1513 | +94.6% | +512.0440 to +959.2893 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 181.4 | +186500.0% | +43.1322 to +319.5067 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 783.7 | +78266.7% | +318.7114 to +1246.6220 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 83.47 | 877.2 | +950.9% | +556.4429 to +1031.0848 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12 | +12.000 (native is 0) | −5.3904 to +29.3904 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*