# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.069 | 6 |
| node-hours | 2.514 | 2.516 | 2.127 | 2.506 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272 | 272 | 270.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 272 | 242.8 | 270.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.6 | 120.1 | 300.1 | 119.9 |
| response time (ms), 95th percentile | 1087 | 199 | 1229 | 262.3 |
| response time (ms), 99th percentile | 1576 | 289.9 | 1713 | 387.2 |
| time over the response line (% of samples) | 13.39 | 0.07547 | 13.52 | 0.5127 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 0 | 8.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 133.3 | 122 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.39 | 847.4 | 9.865 | 1335 |
| utilisation (used / allocatable) | 0.05793 | 0.05967 | 0.07049 | 0.05858 |
| CPU used (cores), mean | 1.39 | 1.432 | 1.391 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06827 | 0.07393 |
| CPU used with Omni's own (cores), mean | 1.39 | 1.432 | 1.459 | 1.48 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 453.9 | 418.9 | 461.2 |
| HPA replicas, mean | 1.938 | 1.902 | 2.249 | 2.483 |
| pods started | 0 | 0.25 | 1.4 | 2 |
| pod start wait, total (s) | 0 | 0.5 | 3.7 | 4.75 |
| pod start wait, mean (s) | 0 | 0.5 | 1.775 | 1.25 |
| host CPU busy, the real machine under kind (%) | 39.81 | 43.77 | 42.63 | 46.96 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 768.9 | 1428 | 778.8 | 1454 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.547 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 110.5 | 0.0625 | 192.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 575 | 0.4 | 844.2 |
| queue: job turnaround, submitted to done, mean (s) | 75.8 | 658.8 | 83.31 | 901.4 |
| queue: jobs unfinished at the window's end | 0 | 2.5 | 0 | 13.75 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 0 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 4 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.516 | +0.2% | −0.0007 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 268.6 | 272 | +1.3% | +1.9342 to +4.8015 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 268.6 | 272 | +1.3% | +1.9342 to +4.8015 | yes: power given |
| response time (ms), mean | 155.6 | 120.1 | −22.8% | −52.0170 to −19.0081 | yes: GAIN |
| response time (ms), 95th percentile | 360 | 199 | −44.7% | −217.9253 to −104.1422 | yes: GAIN |
| response time (ms), 99th percentile | 532.3 | 289.9 | −45.5% | −352.3449 to −132.5226 | yes: GAIN |
| time over the response line (% of samples) | 1.796 | 0.07547 | −95.8% | −3.5506 to +0.1090 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.75 | 0 | −100.0% | −7.9343 to +0.4343 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.004 | 847.4 | +14012.9% | +483.3994 to +1199.3172 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05101 | 0.05967 | +17.0% | +0.0036 to +0.0137 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.224 | 1.432 | +17.0% | +0.0871 to +0.3282 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.224 | 1.432 | +17.0% | +0.0871 to +0.3282 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 530.4 | 453.9 | −14.4% | −148.4875 to −4.4967 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 1.902 | −2.3% | −0.6818 to +0.5932 | no |
| pods started | 0 | 0.25 | +0.250 (native is 0) | −0.5455 to +1.0455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −1.0910 to +2.0910 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −1.0910 to +2.0910 | no |
| host CPU busy, the real machine under kind (%) | 35.69 | 43.77 | +22.6% | +7.4695 to +8.6909 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 723.2 | 1428 | +97.5% | +445.0599 to +965.4401 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 110.5 | +530100.0% | +74.9593 to +145.9157 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 575 | +575.000 (native is 0) | +453.2426 to +696.7574 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 29.31 | 658.8 | +2147.5% | +378.4293 to +880.5707 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 2.5 | +2.500 (native is 0) | −0.2557 to +5.2557 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.069 | −15.5% | −1.8035 to −0.0579 | yes: GAIN |
| node-hours | 2.514 | 2.127 | −15.4% | −0.7554 to −0.0187 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272 | +0.2% | −0.5241 to +1.5136 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 242.8 | −10.6% | −56.4446 to −1.0951 | yes: GAIN |
| response time (ms), mean | 313.6 | 300.1 | −4.3% | −26.3324 to −0.6529 | yes: GAIN |
| response time (ms), 95th percentile | 1087 | 1229 | +13.1% | +45.4039 to +238.8251 | yes: LOSS |
| response time (ms), 99th percentile | 1576 | 1713 | +8.7% | +40.5055 to +234.5937 | yes: LOSS |
| time over the response line (% of samples) | 13.39 | 13.52 | +1.0% | −0.6967 to +0.9619 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 8.4 | +16.7% | −0.0064 to +2.4064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.3 | +133.300 (native is 0) | +61.1646 to +205.4354 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.39 | 9.865 | +17.6% | −0.8243 to +3.7743 | no |
| utilisation (used / allocatable) | 0.05793 | 0.07049 | +21.7% | −0.0001 to +0.0252 | no |
| CPU used (cores), mean | 1.39 | 1.391 | +0.1% | −0.0253 to +0.0273 | no |
| Omni's own CPU (cores), mean | 0 | 0.06827 | +0.068 (native is 0) | +0.0605 to +0.0760 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.459 | +5.0% | +0.0413 to +0.0972 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 418.9 | −12.8% | −125.2984 to +2.6187 | no |
| HPA replicas, mean | 1.938 | 2.249 | +16.1% | +0.0150 to +0.6088 | yes: power given |
| pods started | 0 | 1.4 | +1.400 (native is 0) | +0.4344 to +2.3656 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.700 (native is 0) | +0.9389 to +6.4611 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.775 | +1.775 (native is 0) | +0.7341 to +2.8159 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.81 | 42.63 | +7.1% | +2.1896 to +3.4660 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 768.9 | 778.8 | +1.3% | +1.7830 to +18.0170 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.547 | −24.2% | −2.7237 to −0.1817 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0625 | +25.0% | −0.0221 to +0.0471 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.8 | 83.31 | +9.9% | −0.6518 to +15.6601 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 4 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.966 | −17.2% | −3.1982 to +1.1311 | no |
| node-hours | 2.516 | 2.084 | −17.2% | −1.3455 to +0.4819 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 269.8 | −0.8% | −2.9207 to −1.4722 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 237.3 | −12.8% | −103.2438 to +33.8926 | no |
| response time (ms), mean | 120.1 | 132.6 | +10.5% | +2.2026 to +22.8978 | yes: LOSS |
| response time (ms), 95th percentile | 199 | 412.7 | +107.4% | +150.5309 to +276.8291 | yes: LOSS |
| response time (ms), 99th percentile | 289.9 | 591.2 | +103.9% | +216.4616 to +386.1869 | yes: LOSS |
| time over the response line (% of samples) | 0.07547 | 2.666 | +3433.1% | +0.1533 to +5.0287 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 6.25 | +6.250 (native is 0) | −0.5468 to +13.0468 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 195.2 | +195.250 (native is 0) | +165.9314 to +224.5686 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 847.4 | 6.175 | −99.3% | −1198.0980 to −484.2770 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05967 | 0.06522 | +9.3% | −0.0248 to +0.0359 | no |
| CPU used (cores), mean | 1.432 | 1.23 | −14.1% | −0.2526 to −0.1517 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0628 | +0.063 (native is 0) | +0.0489 to +0.0767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.293 | −9.7% | −0.2014 to −0.0773 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.9 | 457.1 | +0.7% | −116.4822 to +122.7962 | no |
| HPA replicas, mean | 1.902 | 2.272 | +19.4% | −0.0866 to +0.8259 | no |
| pods started | 0.25 | 1.25 | +400.0% | −1.2500 to +3.2500 | no |
| pod start wait, total (s) | 0.5 | 2.25 | +350.0% | −2.8198 to +6.3198 | no |
| pod start wait, mean (s) | 0.5 | 1.25 | +150.0% | −0.7733 to +2.2733 | no |
| host CPU busy, the real machine under kind (%) | 43.77 | 38.2 | −12.7% | −6.1799 to −4.9488 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1428 | 726.8 | −49.1% | −959.2476 to −444.2524 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 110.5 | 0.02083 | −100.0% | −145.8915 to −74.9835 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 575 | 0 | −100.0% | −696.7574 to −453.2426 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 658.8 | 29.96 | −95.5% | −879.6618 to −378.0465 | yes: GAIN |
| queue: jobs unfinished at the window's end | 2.5 | 0 | −100.0% | −5.2557 to +0.2557 | no |

## omni on top of the orchestrator vs the organism alone, 4 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.506 | −0.4% | −0.0318 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 270.8 | −1.1% | −8.0749 to +1.8514 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 270.8 | −1.1% | −8.0749 to +1.8514 | no |
| response time (ms), mean | 448.2 | 119.9 | −73.3% | −633.4456 to −23.1935 | yes: GAIN |
| response time (ms), 95th percentile | 1691 | 262.3 | −84.5% | −2826.7747 to −29.6353 | yes: GAIN |
| response time (ms), 99th percentile | 2455 | 387.2 | −84.2% | −4076.0688 to −59.3882 | yes: GAIN |
| time over the response line (% of samples) | 23.78 | 0.5127 | −97.8% | −47.6501 to +1.1059 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.75 | 0 | −100.0% | −22.1768 to +0.6768 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 122 | +122.000 (native is 0) | +80.3697 to +163.6303 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.13 | 1335 | +11887.1% | +692.0122 to +1954.8461 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06358 | 0.05858 | −7.9% | −0.0226 to +0.0126 | no |
| CPU used (cores), mean | 1.526 | 1.406 | −7.9% | −0.5433 to +0.3031 | no |
| Omni's own CPU (cores), mean | 0 | 0.07393 | +0.074 (native is 0) | +0.0503 to +0.0975 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.526 | 1.48 | −3.0% | −0.4458 to +0.3535 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.8 | 461.2 | +4.6% | −118.7199 to +159.5815 | no |
| HPA replicas, mean | 1.939 | 2.483 | +28.1% | −0.0456 to +1.1344 | no |
| pods started | 0 | 2 | +2.000 (native is 0) | −1.8971 to +5.8971 | no |
| pod start wait, total (s) | 0 | 4.75 | +4.750 (native is 0) | −4.0005 to +13.5005 | no |
| pod start wait, mean (s) | 0 | 1.25 | +1.250 (native is 0) | −1.1365 to +3.6365 | no |
| host CPU busy, the real machine under kind (%) | 43.31 | 46.96 | +8.4% | −3.6517 to +10.9523 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807 | 1454 | +80.2% | +570.1803 to +723.8197 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09375 | 192.3 | +205011.1% | +89.7859 to +294.6099 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 844.2 | +84325.0% | +513.9031 to +1172.5969 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 115.2 | 901.4 | +682.5% | +549.6181 to +1022.7777 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.75 | +13.750 (native is 0) | −0.8534 to +28.3534 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*