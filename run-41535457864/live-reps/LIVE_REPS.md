# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.991 | 5.267 |
| node-hours | 2.51 | 2.517 | 2.088 | 2.213 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.2 | 274.7 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 275.2 | 243 | 252.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 526.1 | 529.8 | 563.5 | 541.3 |
| response time (ms), 95th percentile | 2033 | 2189 | 2236 | 2269 |
| response time (ms), 99th percentile | 2830 | 3041 | 3072 | 3183 |
| time over the response line (% of samples) | 23.54 | 21.71 | 24.22 | 22.56 |
| failed requests (%) | 0 | 0 | 0 | 0.01198 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 11.6 | 12.4 | 12 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 33.2 | 26.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.07 | 25.67 | 26.08 | 30.24 |
| utilisation (used / allocatable) | 0.06783 | 0.0676 | 0.0821 | 0.07556 |
| CPU used (cores), mean | 1.628 | 1.622 | 1.624 | 1.601 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06598 | 0.07057 |
| CPU used with Omni's own (cores), mean | 1.628 | 1.622 | 1.69 | 1.672 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.3 | 415.5 | 359.7 | 381.5 |
| HPA replicas, mean | 2.082 | 2.06 | 2.467 | 2.31 |
| pods started | 0 | 0.2 | 1.1 | 0.9 |
| pod start wait, total (s) | 0 | 0.5 | 1.8 | 1.6 |
| pod start wait, mean (s) | 0 | 0.5 | 0.75 | 1.15 |
| host CPU busy, the real machine under kind (%) | 46.54 | 47.4 | 49.14 | 49.7 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 848.7 | 859.4 | 860.1 | 866.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.034 | 4.561 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 1.613 | 0.4292 | 0.6083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2 | 2.7 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 168.6 | 166.5 | 172.5 |
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
| worker nodes in service, mean | 6 | 5.267 | −12.2% | −1.3315 to −0.1354 | yes: GAIN |
| node-hours | 2.517 | 2.213 | −12.1% | −0.5568 to −0.0520 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.5 | +0.1% | −0.5692 to +1.0502 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 252.4 | −8.3% | −42.1755 to −3.5768 | yes: GAIN |
| response time (ms), mean | 529.8 | 541.3 | +2.2% | +1.2139 to +21.7753 | yes: LOSS |
| response time (ms), 95th percentile | 2189 | 2269 | +3.6% | −32.4168 to +191.6118 | no |
| response time (ms), 99th percentile | 3041 | 3183 | +4.6% | −91.9202 to +374.2788 | no |
| time over the response line (% of samples) | 21.71 | 22.56 | +3.9% | +0.1449 to +1.5606 | yes: LOSS |
| failed requests (%) | 0 | 0.01198 | +0.012 (native is 0) | −0.0151 to +0.0391 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12 | +3.4% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.7 | +26.700 (native is 0) | +19.5465 to +33.8535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.67 | 30.24 | +17.8% | +2.3499 to +6.7868 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0676 | 0.07556 | +11.8% | +0.0021 to +0.0138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.622 | 1.601 | −1.3% | −0.0583 to +0.0159 | no |
| Omni's own CPU (cores), mean | 0 | 0.07057 | +0.071 (native is 0) | +0.0626 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.622 | 1.672 | +3.0% | +0.0062 to +0.0925 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.5 | 381.5 | −8.2% | −61.3910 to −6.6139 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 2.31 | +12.1% | −0.0164 to +0.5167 | no |
| pods started | 0.2 | 0.9 | +350.0% | −0.2567 to +1.6567 | no |
| pod start wait, total (s) | 0.5 | 1.6 | +220.0% | −0.3871 to +2.5871 | no |
| pod start wait, mean (s) | 0.5 | 1.15 | +130.0% | −0.2105 to +1.5105 | no |
| host CPU busy, the real machine under kind (%) | 47.4 | 49.7 | +4.9% | +1.8123 to +2.7981 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 859.4 | 866.5 | +0.8% | −0.1042 to +14.3042 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 | −24.0% | −2.4873 to −0.3899 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.613 | 0.6083 | −62.3% | −2.1682 to +0.1599 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 1.7 | −15.0% | −3.0196 to +2.4196 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.6 | 172.5 | +2.3% | −2.0274 to +9.9108 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.517 | +0.3% | +0.0011 to +0.0129 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.2 | +0.2% | +0.0530 to +1.2298 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 275.2 | +0.2% | +0.0530 to +1.2298 | yes: power given |
| response time (ms), mean | 526.1 | 529.8 | +0.7% | −10.8234 to +18.2344 | no |
| response time (ms), 95th percentile | 2033 | 2189 | +7.7% | +18.9857 to +293.3033 | yes: LOSS |
| response time (ms), 99th percentile | 2830 | 3041 | +7.5% | −18.1380 to +440.9826 | no |
| time over the response line (% of samples) | 23.54 | 21.71 | −7.8% | −2.8329 to −0.8225 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 11.6 | −5.7% | −2.1326 to +0.7326 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.07 | 25.67 | +34.6% | +1.1741 to +12.0359 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06783 | 0.0676 | −0.3% | −0.0012 to +0.0008 | no |
| CPU used (cores), mean | 1.628 | 1.622 | −0.3% | −0.0300 to +0.0190 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.628 | 1.622 | −0.3% | −0.0300 to +0.0190 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.3 | 415.5 | +0.8% | −6.0301 to +12.4729 | no |
| HPA replicas, mean | 2.082 | 2.06 | −1.1% | −0.1868 to +0.1422 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 46.54 | 47.4 | +1.8% | +0.5204 to +1.1999 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.7 | 859.4 | +1.3% | +3.7891 to +17.6109 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 1.612 | +360.7% | −0.1960 to +2.7210 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2 | +53.8% | −1.7093 to +3.1093 | no |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 168.6 | +7.9% | +4.3453 to +20.4713 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.991 | −16.8% | −1.7050 to −0.3128 | yes: GAIN |
| node-hours | 2.51 | 2.088 | −16.8% | −0.7123 to −0.1323 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.7 | +0.0% | −0.9852 to +1.2584 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 243 | −11.5% | −53.2355 to −9.8412 | yes: GAIN |
| response time (ms), mean | 526.1 | 563.5 | +7.1% | +19.1685 to +55.6770 | yes: LOSS |
| response time (ms), 95th percentile | 2033 | 2236 | +10.0% | +84.3957 to +321.6033 | yes: LOSS |
| response time (ms), 99th percentile | 2830 | 3072 | +8.5% | +48.7796 to +434.9712 | yes: LOSS |
| time over the response line (% of samples) | 23.54 | 24.22 | +2.9% | −0.1565 to +1.5184 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 12.4 | +0.8% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.200 (native is 0) | +19.3469 to +47.0531 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.07 | 26.08 | +36.8% | +2.9905 to +11.0329 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06783 | 0.0821 | +21.0% | +0.0041 to +0.0244 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.628 | 1.624 | −0.2% | −0.0203 to +0.0125 | no |
| Omni's own CPU (cores), mean | 0 | 0.06598 | +0.066 (native is 0) | +0.0593 to +0.0726 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.628 | 1.69 | +3.8% | +0.0420 to +0.0822 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.3 | 359.7 | −12.7% | −91.5429 to −13.5265 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.082 | 2.467 | +18.5% | +0.1206 to +0.6485 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0 | 1.8 | +1.800 (native is 0) | +0.0544 to +3.5456 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.75 | +0.750 (native is 0) | +0.1363 to +1.3637 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.54 | 49.14 | +5.6% | +2.2726 to +2.9236 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.7 | 860.1 | +1.3% | +4.5789 to +18.2211 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.034 | −32.8% | −3.0880 to −0.8437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.4292 | +22.6% | −0.1720 to +0.3303 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2.7 | +107.7% | +0.0428 to +2.7572 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 166.5 | +6.6% | +4.5468 to +16.1282 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.991 | −16.8% | −1.7050 to −0.3128 | yes: GAIN |
| node-hours | 2.517 | 2.088 | −17.1% | −0.7207 to −0.1380 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 274.7 | −0.2% | −1.4365 to +0.4269 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 243 | −11.7% | −53.7613 to −10.5983 | yes: GAIN |
| response time (ms), mean | 529.8 | 563.5 | +6.4% | +16.1754 to +51.2592 | yes: LOSS |
| response time (ms), 95th percentile | 2189 | 2236 | +2.1% | −89.7449 to +183.4549 | no |
| response time (ms), 99th percentile | 3041 | 3072 | +1.0% | −169.2694 to +230.1756 | no |
| time over the response line (% of samples) | 21.71 | 24.22 | +11.6% | +1.1496 to +3.8677 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.4 | +6.9% | −1.0407 to +2.6407 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.200 (native is 0) | +19.3469 to +47.0531 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.67 | 26.08 | +1.6% | −2.2465 to +3.0598 | no |
| utilisation (used / allocatable) | 0.0676 | 0.0821 | +21.4% | +0.0035 to +0.0255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.622 | 1.624 | +0.1% | −0.0195 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.06598 | +0.066 (native is 0) | +0.0593 to +0.0726 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.622 | 1.69 | +4.2% | +0.0487 to +0.0865 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.5 | 359.7 | −13.4% | −102.4319 to −9.0803 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 2.467 | +19.8% | +0.1572 to +0.6564 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0.5 | 1.8 | +260.0% | −0.8072 to +3.4072 | no |
| pod start wait, mean (s) | 0.5 | 0.75 | +50.0% | −0.8329 to +1.3329 | no |
| host CPU busy, the real machine under kind (%) | 47.4 | 49.14 | +3.7% | +1.4636 to +2.0123 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 859.4 | 860.1 | +0.1% | −2.1820 to +3.5820 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.034 | −32.8% | −3.0880 to −0.8437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.613 | 0.4292 | −73.4% | −2.4593 to +0.0927 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2.7 | +35.0% | −1.7327 to +3.1327 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.6 | 166.5 | −1.2% | −7.4369 to +3.2952 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.267 | −12.2% | −1.3315 to −0.1354 | yes: GAIN |
| node-hours | 2.51 | 2.213 | −11.8% | −0.5491 to −0.0457 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.5 | +0.3% | −0.0545 to +1.8183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 252.4 | −8.1% | −41.6906 to −2.7789 | yes: GAIN |
| response time (ms), mean | 526.1 | 541.3 | +2.9% | +2.2446 to +28.1555 | yes: LOSS |
| response time (ms), 95th percentile | 2033 | 2269 | +11.6% | +102.4495 to +369.0345 | yes: LOSS |
| response time (ms), 99th percentile | 2830 | 3183 | +12.5% | +113.1824 to +592.0208 | yes: LOSS |
| time over the response line (% of samples) | 23.54 | 22.56 | −4.1% | −1.9571 to +0.0071 | no |
| failed requests (%) | 0 | 0.01198 | +0.012 (native is 0) | −0.0151 to +0.0391 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 12 | −2.4% | −1.0578 to +0.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.7 | +26.700 (native is 0) | +19.5465 to +33.8535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.07 | 30.24 | +58.6% | +4.5364 to +17.8103 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06783 | 0.07556 | +11.4% | +0.0026 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.628 | 1.601 | −1.6% | −0.0814 to +0.0280 | no |
| Omni's own CPU (cores), mean | 0 | 0.07057 | +0.071 (native is 0) | +0.0626 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.628 | 1.672 | +2.7% | −0.0173 to +0.1051 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.3 | 381.5 | −7.5% | −52.2805 to −9.2818 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.082 | 2.31 | +10.9% | +0.0174 to +0.4384 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | +0.1615 to +3.0385 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.15 | +1.150 (native is 0) | +0.2258 to +2.0742 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.54 | 49.7 | +6.8% | +2.6326 to +3.6980 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.7 | 866.5 | +2.1% | +8.9759 to +26.6241 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 | −24.0% | −2.4873 to −0.3899 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.6083 | +73.8% | −0.1749 to +0.6916 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.7 | +30.8% | −1.9891 to +2.7891 | no |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 172.5 | +10.5% | +6.3308 to +26.3692 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*