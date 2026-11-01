# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.534 | 5.279 |
| node-hours | 2.514 | 2.514 | 2.316 | 2.213 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | 274.6 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.9 | 260 | 251.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 529 | 522.8 | 517.7 | 531 |
| response time (ms), 95th percentile | 2127 | 2213 | 2088 | 2214 |
| response time (ms), 99th percentile | 3019 | 3028 | 2964 | 3094 |
| time over the response line (% of samples) | 23.64 | 21.97 | 23.24 | 22.61 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 10.9 | 11.5 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 11.5 | 9.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.44 | 23.17 | 18.01 | 26.73 |
| utilisation (used / allocatable) | 0.06743 | 0.06767 | 0.073 | 0.0753 |
| CPU used (cores), mean | 1.618 | 1.624 | 1.614 | 1.587 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01311 | 0.01373 |
| CPU used with Omni's own (cores), mean | 1.618 | 1.624 | 1.627 | 1.601 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.2 | 413.2 | 388.2 | 382.8 |
| HPA replicas, mean | 2.041 | 2.068 | 2.141 | 2.097 |
| pods started | 0 | 0 | 0.8 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 1.2 | 0.5 |
| pod start wait, mean (s) | 0 | 0 | 1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 46.35 | 47.23 | 46.97 | 47.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 851.9 | 858.6 | 848.2 | 862.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.125 | 4.68 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 0.8542 | 0.3458 | 0.4167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 1.2 | 1.4 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 167.3 | 154.5 | 170.2 |
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
| worker nodes in service, mean | 6 | 5.279 | −12.0% | −1.4756 to +0.0342 | no |
| node-hours | 2.514 | 2.213 | −12.0% | −0.6186 to +0.0153 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.4 | −0.2% | −1.6271 to +0.5756 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 251.7 | −8.4% | −47.6221 to +1.2998 | no |
| response time (ms), mean | 522.8 | 531 | +1.6% | −20.6536 to +36.9240 | no |
| response time (ms), 95th percentile | 2213 | 2214 | +0.0% | −132.1406 to +133.5536 | no |
| response time (ms), 99th percentile | 3028 | 3094 | +2.2% | −50.6935 to +183.2107 | no |
| time over the response line (% of samples) | 21.97 | 22.61 | +2.9% | −0.7449 to +2.0157 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11 | +0.9% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 | +9.400 (native is 0) | +7.7758 to +11.0242 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.17 | 26.73 | +15.4% | −0.2557 to +7.3757 | no |
| utilisation (used / allocatable) | 0.06767 | 0.0753 | +11.3% | +0.0000 to +0.0152 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.624 | 1.587 | −2.3% | −0.0869 to +0.0136 | no |
| Omni's own CPU (cores), mean | 0 | 0.01373 | +0.014 (native is 0) | +0.0125 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.624 | 1.601 | −1.4% | −0.0741 to +0.0282 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.2 | 382.8 | −7.4% | −61.5313 to +0.7265 | no |
| HPA replicas, mean | 2.068 | 2.097 | +1.4% | −0.1708 to +0.2287 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.4079 to +1.4079 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.4079 to +1.4079 | no |
| host CPU busy, the real machine under kind (%) | 47.23 | 47.76 | +1.1% | +0.1604 to +0.8965 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.6 | 862.9 | +0.5% | −2.3253 to +10.9253 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.68 | −22.0% | −2.6451 to +0.0046 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.4167 | −51.2% | −1.1657 to +0.2907 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.9 | −25.0% | −1.0578 to +0.4578 | no |
| queue: job turnaround, submitted to done, mean (s) | 167.3 | 170.2 | +1.7% | −0.7941 to +6.5441 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.514 | ±0.0% | −0.0106 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | +0.0% | −1.1421 to +1.2465 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.9 | +0.0% | −1.1421 to +1.2465 | no |
| response time (ms), mean | 529 | 522.8 | −1.2% | −23.6257 to +11.1890 | no |
| response time (ms), 95th percentile | 2127 | 2213 | +4.0% | −13.9717 to +185.9497 | no |
| response time (ms), 99th percentile | 3019 | 3028 | +0.3% | −143.6196 to +161.7296 | no |
| time over the response line (% of samples) | 23.64 | 21.97 | −7.0% | −2.8110 to −0.5192 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 10.9 | −0.9% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.44 | 23.17 | +19.2% | +0.4531 to +7.0103 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06743 | 0.06767 | +0.4% | −0.0002 to +0.0007 | no |
| CPU used (cores), mean | 1.618 | 1.624 | +0.4% | −0.0042 to +0.0160 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.618 | 1.624 | +0.4% | −0.0042 to +0.0160 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.2 | 413.2 | −0.5% | −5.5892 to +1.4920 | no |
| HPA replicas, mean | 2.041 | 2.068 | +1.3% | −0.1228 to +0.1761 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.35 | 47.23 | +1.9% | +0.4848 to +1.2792 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.9 | 858.6 | +0.8% | +0.1610 to +13.2390 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 0.8542 | +120.4% | −0.0736 to +1.0070 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 1.2 | −50.0% | −3.5068 to +1.1068 | no |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 167.3 | +6.3% | +3.4228 to +16.3439 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.534 | −7.8% | −1.0385 to +0.1063 | no |
| node-hours | 2.514 | 2.316 | −7.9% | −0.4397 to +0.0428 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.6 | −0.1% | −0.9201 to +0.4236 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 260 | −5.4% | −32.7116 to +2.9985 | no |
| response time (ms), mean | 529 | 517.7 | −2.1% | −29.0283 to +6.3022 | no |
| response time (ms), 95th percentile | 2127 | 2088 | −1.8% | −93.2851 to +14.9031 | no |
| response time (ms), 99th percentile | 3019 | 2964 | −1.8% | −216.4373 to +106.8051 | no |
| time over the response line (% of samples) | 23.64 | 23.24 | −1.7% | −1.0196 to +0.2226 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.5 | +4.5% | −0.2726 to +1.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 | +11.500 (native is 0) | +10.1407 to +12.8593 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.44 | 18.01 | −7.4% | −4.0707 to +1.2007 | no |
| utilisation (used / allocatable) | 0.06743 | 0.073 | +8.3% | −0.0020 to +0.0132 | no |
| CPU used (cores), mean | 1.618 | 1.614 | −0.3% | −0.0149 to +0.0060 | no |
| Omni's own CPU (cores), mean | 0 | 0.01311 | +0.013 (native is 0) | +0.0125 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.618 | 1.627 | +0.5% | −0.0019 to +0.0191 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.2 | 388.2 | −6.5% | −63.4499 to +9.3395 | no |
| HPA replicas, mean | 2.041 | 2.141 | +4.9% | −0.0667 to +0.2666 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.3476 to +1.2524 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3207 to +2.0793 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.4160 to +1.5840 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.35 | 46.97 | +1.3% | +0.0167 to +1.2279 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.9 | 848.2 | −0.4% | −7.3325 to −0.0675 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.125 | −14.6% | −1.9484 to +0.1984 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 0.3458 | −10.8% | −0.2878 to +0.2045 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 1.4 | −41.7% | −2.7843 to +0.7843 | no |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 154.5 | −1.9% | −7.5230 to +1.6313 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.534 | −7.8% | −1.0385 to +0.1063 | no |
| node-hours | 2.514 | 2.316 | −7.9% | −0.4382 to +0.0413 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.6 | −0.1% | −1.2717 to +0.6709 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 260 | −5.4% | −32.6556 to +2.8381 | no |
| response time (ms), mean | 522.8 | 517.7 | −1.0% | −23.1152 to +12.8258 | no |
| response time (ms), 95th percentile | 2213 | 2088 | −5.7% | −240.9292 to −9.4308 | yes: GAIN |
| response time (ms), 99th percentile | 3028 | 2964 | −2.1% | −189.3725 to +61.6303 | no |
| time over the response line (% of samples) | 21.97 | 23.24 | +5.8% | −0.1033 to +2.6364 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.5 | +5.5% | −0.4769 to +1.6769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 | +11.500 (native is 0) | +10.1407 to +12.8593 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.17 | 18.01 | −22.3% | −8.9519 to −1.3815 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06767 | 0.073 | +7.9% | −0.0021 to +0.0128 | no |
| CPU used (cores), mean | 1.624 | 1.614 | −0.6% | −0.0213 to +0.0006 | no |
| Omni's own CPU (cores), mean | 0 | 0.01311 | +0.013 (native is 0) | +0.0125 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.624 | 1.627 | +0.2% | −0.0086 to +0.0141 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.2 | 388.2 | −6.1% | −59.7248 to +9.7116 | no |
| HPA replicas, mean | 2.068 | 2.141 | +3.5% | −0.0453 to +0.1919 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.3476 to +1.2524 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3207 to +2.0793 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.4160 to +1.5840 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.23 | 46.97 | −0.5% | −0.7628 to +0.2433 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.6 | 848.2 | −1.2% | −16.3676 to −4.4324 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.125 | −14.6% | −1.9484 to +0.1984 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.3458 | −59.5% | −1.1160 to +0.0994 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 | +16.7% | −1.5779 to +1.9779 | no |
| queue: job turnaround, submitted to done, mean (s) | 167.3 | 154.5 | −7.7% | −20.7634 to −4.8949 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.279 | −12.0% | −1.4756 to +0.0342 | no |
| node-hours | 2.514 | 2.213 | −12.0% | −0.6184 to +0.0151 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.4 | −0.2% | −1.5644 to +0.6173 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 251.7 | −8.4% | −47.5018 to +1.2839 | no |
| response time (ms), mean | 529 | 531 | +0.4% | −20.2412 to +24.0749 | no |
| response time (ms), 95th percentile | 2127 | 2214 | +4.1% | −40.0817 to +213.4727 | no |
| response time (ms), 99th percentile | 3019 | 3094 | +2.5% | −101.3282 to +251.9554 | no |
| time over the response line (% of samples) | 23.64 | 22.61 | −4.4% | −1.8489 to −0.2106 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 | +9.400 (native is 0) | +7.7758 to +11.0242 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.44 | 26.73 | +37.5% | +3.3748 to +11.2086 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06743 | 0.0753 | +11.7% | +0.0001 to +0.0157 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.618 | 1.587 | −1.9% | −0.0780 to +0.0164 | no |
| Omni's own CPU (cores), mean | 0 | 0.01373 | +0.014 (native is 0) | +0.0125 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.618 | 1.601 | −1.1% | −0.0651 to +0.0310 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.2 | 382.8 | −7.8% | −65.5576 to +0.6557 | no |
| HPA replicas, mean | 2.041 | 2.097 | +2.7% | −0.1526 to +0.2638 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.4079 to +1.4079 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.4079 to +1.4079 | no |
| host CPU busy, the real machine under kind (%) | 46.35 | 47.76 | +3.0% | +1.0628 to +1.7581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.9 | 862.9 | +1.3% | +4.6736 to +17.3264 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.68 | −22.0% | −2.6451 to +0.0046 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 0.4167 | +7.5% | −0.2891 to +0.3474 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 0.9 | −62.5% | −3.6657 to +0.6657 | no |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 170.2 | +8.1% | +5.3713 to +20.1454 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*