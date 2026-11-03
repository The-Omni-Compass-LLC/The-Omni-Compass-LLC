# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.67 | 5.013 |
| node-hours | 2.511 | 2.513 | 1.956 | 2.101 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.7 | 272.9 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.7 | 231.1 | 242 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 399 | 386.3 | 410.1 | 400.8 |
| response time (ms), 95th percentile | 1459 | 1484 | 1575 | 1573 |
| response time (ms), 99th percentile | 2128 | 2153 | 2201 | 2291 |
| time over the response line (% of samples) | 15.47 | 14.51 | 15.72 | 15.53 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 9.2 | 10.2 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 29.7 | 29.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 19.69 | 17.16 | 21.6 |
| utilisation (used / allocatable) | 0.06263 | 0.06219 | 0.0801 | 0.07312 |
| CPU used (cores), mean | 1.503 | 1.493 | 1.484 | 1.474 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0601 | 0.06541 |
| CPU used with Omni's own (cores), mean | 1.503 | 1.493 | 1.544 | 1.539 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 452 | 375.6 | 404.5 |
| HPA replicas, mean | 2.023 | 2.067 | 2.387 | 2.313 |
| pods started | 0 | 0.1 | 1 | 0.4 |
| pod start wait, total (s) | 0 | 0.2 | 1.9 | 0.8 |
| pod start wait, mean (s) | 0 | 0.2 | 1.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.02 | 43.76 | 45.23 | 46.31 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806.9 | 809.9 | 812.8 | 816.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.654 | 4.091 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.8542 | 0.3458 | 0.85 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.8 | 1.7 | 3 |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 117.3 | 117.3 | 125.9 |
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
| worker nodes in service, mean | 6 | 5.013 | −16.4% | −1.6263 to −0.3468 | yes: GAIN |
| node-hours | 2.513 | 2.101 | −16.4% | −0.6759 to −0.1479 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273 | +0.1% | −0.9722 to +1.4523 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 242 | −11.3% | −50.5092 to −10.9940 | yes: GAIN |
| response time (ms), mean | 386.3 | 400.8 | +3.8% | −9.0190 to +37.9914 | no |
| response time (ms), 95th percentile | 1484 | 1573 | +6.0% | −81.5574 to +259.5534 | no |
| response time (ms), 99th percentile | 2153 | 2291 | +6.4% | −7.3011 to +283.3477 | no |
| time over the response line (% of samples) | 14.51 | 15.53 | +7.0% | −0.3991 to +2.4439 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.6 | +15.2% | +0.0428 to +2.7572 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +20.2161 to +39.1839 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.69 | 21.6 | +9.7% | −1.8645 to +5.6778 | no |
| utilisation (used / allocatable) | 0.06219 | 0.07312 | +17.6% | +0.0043 to +0.0176 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.493 | 1.474 | −1.2% | −0.0718 to +0.0347 | no |
| Omni's own CPU (cores), mean | 0 | 0.06541 | +0.065 (native is 0) | +0.0565 to +0.0743 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.493 | 1.539 | +3.1% | −0.0112 to +0.1049 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452 | 404.5 | −10.5% | −80.1445 to −14.9591 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.313 | +11.9% | −0.0708 to +0.5622 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.76 | 46.31 | +5.8% | +2.1277 to +2.9739 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.9 | 816.9 | +0.9% | +1.3576 to +12.6424 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.091 | −31.8% | −2.9915 to −0.8265 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.85 | −0.5% | −0.9856 to +0.9773 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 3 | +66.7% | −2.4286 to +4.8286 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.3 | 125.9 | +7.3% | +1.4453 to +15.7464 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.513 | +0.1% | −0.0072 to +0.0105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.7 | +0.0% | −0.9722 to +1.0051 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.7 | +0.0% | −0.9722 to +1.0051 | no |
| response time (ms), mean | 399 | 386.3 | −3.2% | −31.9751 to +6.5485 | no |
| response time (ms), 95th percentile | 1459 | 1484 | +1.7% | −86.3901 to +135.2221 | no |
| response time (ms), 99th percentile | 2128 | 2153 | +1.2% | −155.7642 to +206.4880 | no |
| time over the response line (% of samples) | 15.47 | 14.51 | −6.2% | −1.7012 to −0.2194 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 9.2 | −9.8% | −2.2158 to +0.2158 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 19.69 | +29.2% | −0.1857 to +9.0991 | no |
| utilisation (used / allocatable) | 0.06263 | 0.06219 | −0.7% | −0.0012 to +0.0003 | no |
| CPU used (cores), mean | 1.503 | 1.493 | −0.7% | −0.0285 to +0.0072 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.503 | 1.493 | −0.7% | −0.0285 to +0.0072 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 452 | +1.0% | −2.2817 to +10.8322 | no |
| HPA replicas, mean | 2.023 | 2.067 | +2.2% | −0.1367 to +0.2253 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.02 | 43.76 | +1.7% | +0.1563 to +1.3310 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.9 | 809.9 | +0.4% | −3.5124 to +9.5124 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.8542 | +184.7% | −1.0082 to +2.1166 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.8 | +28.6% | −2.5046 to +3.3046 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 117.3 | +3.6% | −1.8548 to +10.0048 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.67 | −22.2% | −2.1109 to −0.5498 | yes: GAIN |
| node-hours | 2.511 | 1.956 | −22.1% | −0.8813 to −0.2296 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.6026 to +1.0952 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.1 | −15.2% | −65.9548 to −17.1984 | yes: GAIN |
| response time (ms), mean | 399 | 410.1 | +2.8% | −13.2726 to +35.4925 | no |
| response time (ms), 95th percentile | 1459 | 1575 | +7.9% | −32.3167 to +262.9187 | no |
| response time (ms), 99th percentile | 2128 | 2201 | +3.5% | −62.2624 to +209.5834 | no |
| time over the response line (% of samples) | 15.47 | 15.72 | +1.6% | −0.5319 to +1.0221 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.2 | ±0.0% | −0.7540 to +0.7540 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +19.4331 to +39.9669 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 17.16 | +12.6% | −0.4846 to +4.3313 | no |
| utilisation (used / allocatable) | 0.06263 | 0.0801 | +27.9% | +0.0069 to +0.0280 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.503 | 1.484 | −1.3% | −0.0399 to +0.0013 | no |
| Omni's own CPU (cores), mean | 0 | 0.0601 | +0.060 (native is 0) | +0.0519 to +0.0683 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.503 | 1.544 | +2.7% | +0.0126 to +0.0691 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 375.6 | −16.1% | −119.3755 to −25.0301 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.387 | +18.0% | +0.1139 to +0.6141 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.2460 to +1.7540 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | +0.3751 to +3.4249 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | +0.3887 to +1.8113 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.02 | 45.23 | +5.1% | +1.7715 to +2.6497 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.9 | 812.8 | +0.7% | +0.0261 to +11.7739 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.654 | −39.1% | −3.5257 to −1.1664 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.3458 | +15.3% | −0.0840 to +0.1757 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.7 | +21.4% | −1.0924 to +1.6924 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 117.3 | +3.6% | −1.3441 to +9.4274 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.67 | −22.2% | −2.1109 to −0.5498 | yes: GAIN |
| node-hours | 2.513 | 1.956 | −22.2% | −0.8807 to −0.2336 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.8637 to +1.3234 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.1 | −15.3% | −65.6100 to −17.5760 | yes: GAIN |
| response time (ms), mean | 386.3 | 410.1 | +6.2% | −8.1633 to +55.8098 | no |
| response time (ms), 95th percentile | 1484 | 1575 | +6.1% | −88.6053 to +270.3753 | no |
| response time (ms), 99th percentile | 2153 | 2201 | +2.2% | −142.4077 to +239.0049 | no |
| time over the response line (% of samples) | 14.51 | 15.72 | +8.3% | +0.6172 to +1.7936 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.2 | +10.9% | −0.0663 to +2.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +19.4331 to +39.9669 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.69 | 17.16 | −12.9% | −6.5665 to +1.4998 | no |
| utilisation (used / allocatable) | 0.06219 | 0.0801 | +28.8% | +0.0070 to +0.0288 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.493 | 1.484 | −0.6% | −0.0271 to +0.0099 | no |
| Omni's own CPU (cores), mean | 0 | 0.0601 | +0.060 (native is 0) | +0.0519 to +0.0683 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.493 | 1.544 | +3.5% | +0.0268 to +0.0763 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452 | 375.6 | −16.9% | −128.1066 to −24.8495 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.387 | +15.5% | +0.0353 to +0.6042 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | +0.2737 to +1.5263 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.9 | +850.0% | +0.4361 to +2.9639 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.1 | +450.0% | +0.1887 to +1.6113 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.76 | 45.23 | +3.4% | +0.7505 to +2.1833 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.9 | 812.8 | +0.4% | −4.2168 to +10.0168 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.654 | −39.1% | −3.5257 to −1.1664 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.3458 | −59.5% | −2.0366 to +1.0199 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 1.7 | −5.6% | −1.9910 to +1.7910 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.3 | 117.3 | −0.0% | −8.3879 to +8.3213 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.013 | −16.4% | −1.6263 to −0.3468 | yes: GAIN |
| node-hours | 2.511 | 2.101 | −16.3% | −0.6786 to −0.1419 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273 | +0.1% | −0.2864 to +0.7994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 242 | −11.3% | −51.0023 to −10.4681 | yes: GAIN |
| response time (ms), mean | 399 | 400.8 | +0.4% | −24.2148 to +27.7606 | no |
| response time (ms), 95th percentile | 1459 | 1573 | +7.8% | −111.7960 to +338.6240 | no |
| response time (ms), 99th percentile | 2128 | 2291 | +7.7% | −29.0927 to +355.8631 | no |
| time over the response line (% of samples) | 15.47 | 15.53 | +0.4% | −1.4326 to +1.5569 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.6 | +3.9% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +20.2161 to +39.1839 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 21.6 | +41.8% | +0.8323 to +11.8944 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06263 | 0.07312 | +16.7% | +0.0038 to +0.0172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.503 | 1.474 | −1.9% | −0.0870 to +0.0285 | no |
| Omni's own CPU (cores), mean | 0 | 0.06541 | +0.065 (native is 0) | +0.0565 to +0.0743 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.503 | 1.539 | +2.4% | −0.0273 to +0.0996 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 404.5 | −9.7% | −74.5957 to −11.9574 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.313 | +14.3% | +0.0172 to +0.5628 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −1.0096 to +2.6096 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.02 | 46.31 | +7.7% | +3.0315 to +3.5573 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.9 | 816.9 | +1.2% | +3.0403 to +16.9597 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.091 | −31.8% | −2.9915 to −0.8265 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.85 | +183.3% | −0.1932 to +1.2932 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 3 | +114.3% | −0.4288 to +3.6288 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 125.9 | +11.2% | +5.1525 to +20.1892 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*