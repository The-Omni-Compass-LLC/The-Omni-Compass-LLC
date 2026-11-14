# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.469 | 6.148 |
| node-hours | 5.025 | 5.029 | 3.965 | 2.582 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 504.5 | 523.3 | 505.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 504.5 | 444 | 321.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 325.2 | 108.6 | 344.5 | 63.92 |
| response time (ms), 95th percentile | 1095 | 151.3 | 1357 | 81.78 |
| response time (ms), 99th percentile | 1508 | 167.6 | 1837 | 104.7 |
| time over the response line (% of samples) | 15.03 | 0.00381 | 18.11 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0 | 10.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 123.8 | 31.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 37.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.512 | 0 | 9.942 | 0.05 |
| utilisation (used / allocatable) | 0.03185 | 0.005505 | 0.04097 | 0.008828 |
| CPU used (cores), mean | 1.529 | 0.2642 | 1.51 | 0.2174 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04905 | 0.0277 |
| CPU used with Omni's own (cores), mean | 1.529 | 0.2642 | 1.559 | 0.2451 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 4624 | 702.8 | 3598 |
| HPA replicas, mean | 3.966 | 4.174 | 4.255 | 4.334 |
| pods started | 0.2 | 0.5 | 1.3 | 1.8 |
| pod start wait, total (s) | 0.4 | 0.7 | 3.2 | 2.9 |
| pod start wait, mean (s) | 0.4 | 0.6 | 1.25 | 1.358 |
| host CPU busy, the real machine under kind (%) | 46.32 | 13.88 | 50.69 | 16.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 779.7 | 1506 | 798.7 | 1509 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 7.836 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1160 | 0.05833 | 1163 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | 0.4 | 1479 |
| queue: job turnaround, submitted to done, mean (s) | 90.61 | 1160 | 107.4 | 1163 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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
| worker nodes in service, mean | 12 | 6.148 | −48.8% | −5.9108 to −5.7938 | yes: GAIN |
| node-hours | 5.029 | 2.582 | −48.7% | −2.4737 to −2.4203 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 505.7 | +0.2% | +0.0619 to +2.3545 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 321.4 | −36.3% | −185.2665 to −181.0129 | yes: GAIN |
| response time (ms), mean | 108.6 | 63.92 | −41.1% | −53.5619 to −35.7727 | yes: GAIN |
| response time (ms), 95th percentile | 151.3 | 81.78 | −46.0% | −85.1532 to −53.9658 | yes: GAIN |
| response time (ms), 99th percentile | 167.6 | 104.7 | −37.5% | −77.2434 to −48.5480 | yes: GAIN |
| time over the response line (% of samples) | 0.00381 | 0 | −100.0% | −0.0124 to +0.0048 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.4 | +31.400 (native is 0) | +29.6414 to +33.1586 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05 | +0.050 (native is 0) | −0.0631 to +0.1631 | no |
| utilisation (used / allocatable) | 0.005505 | 0.008828 | +60.4% | +0.0029 to +0.0038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2642 | 0.2174 | −17.7% | −0.0515 to −0.0423 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0277 | +0.028 (native is 0) | +0.0251 to +0.0303 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2642 | 0.2451 | −7.3% | −0.0249 to −0.0135 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4624 | 3598 | −22.2% | −1116.2043 to −935.2476 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.174 | 4.334 | +3.8% | −0.0440 to +0.3650 | no |
| pods started | 0.5 | 1.8 | +260.0% | +0.0819 to +2.5181 | yes: power given |
| pod start wait, total (s) | 0.7 | 2.9 | +314.3% | +0.2985 to +4.1015 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.358 | +126.4% | −0.3791 to +1.8958 | no |
| host CPU busy, the real machine under kind (%) | 13.88 | 16.27 | +17.3% | +1.9517 to +2.8447 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1509 | +0.2% | −0.2167 to +6.2167 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1163 | +0.3% | −0.3574 to +6.3241 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1479 | +0.2% | −0.3069 to +6.1069 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1163 | +0.3% | −0.3574 to +6.3241 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.025 | 5.029 | +0.1% | −0.0101 to +0.0188 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 504.5 | −3.6% | −20.7279 to −16.9024 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 504.5 | −3.6% | −20.7279 to −16.9024 | yes: GAIN |
| response time (ms), mean | 325.2 | 108.6 | −66.6% | −406.4569 to −26.8746 | yes: GAIN |
| response time (ms), 95th percentile | 1095 | 151.3 | −86.2% | −1817.1545 to −70.5275 | yes: GAIN |
| response time (ms), 99th percentile | 1508 | 167.6 | −88.9% | −2564.3951 to −116.9777 | yes: GAIN |
| time over the response line (% of samples) | 15.03 | 0.00381 | −100.0% | −23.6813 to −6.3740 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0 | −100.0% | −13.9258 to −5.4742 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.512 | 0 | −100.0% | −14.0139 to −5.0094 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03185 | 0.005505 | −82.7% | −0.0288 to −0.0239 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.529 | 0.2642 | −82.7% | −1.3816 to −1.1474 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.529 | 0.2642 | −82.7% | −1.3816 to −1.1474 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 4624 | +459.2% | +3411.5742 to +4182.0887 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.966 | 4.174 | +5.2% | +0.0723 to +0.3433 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.4 | 0.7 | +75.0% | −0.4578 to +1.0578 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | −0.4573 to +0.8573 | no |
| host CPU busy, the real machine under kind (%) | 46.32 | 13.88 | −70.0% | −35.8275 to −29.0521 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.7 | 1506 | +93.2% | +660.4100 to +792.7900 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1160 | +1855673.3% | +1156.5086 to +1163.0830 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | +368900.0% | +1472.2415 to +1478.9585 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 90.61 | 1160 | +1180.0% | +1005.5888 to +1132.9029 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.469 | −21.1% | −4.1810 to −0.8810 | yes: GAIN |
| node-hours | 5.025 | 3.965 | −21.1% | −1.7597 to −0.3593 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 523.3 | −0.0% | −2.5408 to +2.5395 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 444 | −15.2% | −132.8603 to −25.8118 | yes: GAIN |
| response time (ms), mean | 325.2 | 344.5 | +5.9% | −23.0274 to +61.5809 | no |
| response time (ms), 95th percentile | 1095 | 1357 | +23.9% | +9.2420 to +514.2420 | yes: LOSS |
| response time (ms), 99th percentile | 1508 | 1837 | +21.8% | +40.0655 to +617.4667 | yes: LOSS |
| time over the response line (% of samples) | 15.03 | 18.11 | +20.5% | +0.3476 to +5.8029 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.1 | +4.1% | −1.0775 to +1.8775 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123.8 | +123.800 (native is 0) | +67.2723 to +180.3277 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.512 | 9.942 | +4.5% | −1.0134 to +1.8734 | no |
| utilisation (used / allocatable) | 0.03185 | 0.04097 | +28.6% | +0.0035 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.529 | 1.51 | −1.2% | −0.0864 to +0.0496 | no |
| Omni's own CPU (cores), mean | 0 | 0.04905 | +0.049 (native is 0) | +0.0450 to +0.0531 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.529 | 1.559 | +2.0% | −0.0399 to +0.1011 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 702.8 | −15.0% | −190.4267 to −57.6655 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.966 | 4.255 | +7.3% | −0.0388 to +0.6177 | no |
| pods started | 0.2 | 1.3 | +550.0% | −0.0898 to +2.2898 | no |
| pod start wait, total (s) | 0.4 | 3.2 | +700.0% | −0.0771 to +5.6771 | no |
| pod start wait, mean (s) | 0.4 | 1.25 | +212.5% | −0.5723 to +2.2723 | no |
| host CPU busy, the real machine under kind (%) | 46.32 | 50.69 | +9.4% | +3.3644 to +5.3806 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.7 | 798.7 | +2.4% | +1.6318 to +36.3682 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.836 | −34.7% | −6.4795 to −1.8478 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05833 | −6.7% | −0.0517 to +0.0434 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.61 | 107.4 | +18.5% | +1.1548 to +32.3368 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.469 | −21.1% | −4.1810 to −0.8810 | yes: GAIN |
| node-hours | 5.029 | 3.965 | −21.2% | −1.7603 to −0.3673 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 523.3 | +3.7% | +15.0049 to +22.6240 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 444 | −12.0% | −114.9779 to −6.0640 | yes: GAIN |
| response time (ms), mean | 108.6 | 344.5 | +217.3% | +11.3948 to +460.4902 | yes: LOSS |
| response time (ms), 95th percentile | 151.3 | 1357 | +796.6% | +103.0954 to +2308.0706 | yes: LOSS |
| response time (ms), 99th percentile | 167.6 | 1837 | +996.4% | +234.8466 to +3104.0584 | yes: LOSS |
| time over the response line (% of samples) | 0.00381 | 18.11 | +475201.8% | +8.4449 to +27.7610 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.1 | +10.100 (native is 0) | +5.2550 to +14.9450 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123.8 | +123.800 (native is 0) | +67.2723 to +180.3277 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 9.942 | +9.942 (native is 0) | +5.8913 to +13.9920 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005505 | 0.04097 | +644.1% | +0.0309 to +0.0400 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2642 | 1.51 | +471.6% | +1.0852 to +1.4069 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04905 | +0.049 (native is 0) | +0.0450 to +0.0531 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2642 | 1.559 | +490.1% | +1.1306 to +1.4596 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4624 | 702.8 | −84.8% | −4364.2535 to −3477.5016 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.174 | 4.255 | +2.0% | −0.2372 to +0.4004 | no |
| pods started | 0.5 | 1.3 | +160.0% | −0.4526 to +2.0526 | no |
| pod start wait, total (s) | 0.7 | 3.2 | +357.1% | −0.4056 to +5.4056 | no |
| pod start wait, mean (s) | 0.6 | 1.25 | +108.3% | −0.7521 to +2.0521 | no |
| host CPU busy, the real machine under kind (%) | 13.88 | 50.69 | +265.3% | +32.7909 to +40.8337 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 798.7 | −47.0% | −788.2485 to −626.9515 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.05833 | −100.0% | −1163.0625 to −1156.5375 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.4 | −100.0% | −1478.7488 to −1472.4512 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 107.4 | −90.7% | −1128.0890 to −976.9110 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.148 | −48.8% | −5.9108 to −5.7938 | yes: GAIN |
| node-hours | 5.025 | 2.582 | −48.6% | −2.4734 to −2.4119 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 505.7 | −3.4% | −19.1317 to −16.0821 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 321.4 | −38.6% | −203.3369 to −200.5728 | yes: GAIN |
| response time (ms), mean | 325.2 | 63.92 | −80.3% | −456.4953 to −66.1708 | yes: GAIN |
| response time (ms), 95th percentile | 1095 | 81.78 | −92.5% | −1889.3113 to −137.4897 | yes: GAIN |
| response time (ms), 99th percentile | 1508 | 104.7 | −93.1% | −2624.4809 to −182.6833 | yes: GAIN |
| time over the response line (% of samples) | 15.03 | 0 | −100.0% | −23.6905 to −6.3724 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0 | −100.0% | −13.9258 to −5.4742 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.4 | +31.400 (native is 0) | +29.6414 to +33.1586 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.512 | 0.05 | −99.5% | −13.9933 to −4.9300 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03185 | 0.008828 | −72.3% | −0.0251 to −0.0209 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.529 | 0.2174 | −85.8% | −1.4275 to −1.1953 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0277 | +0.028 (native is 0) | +0.0251 to +0.0303 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.529 | 0.2451 | −84.0% | −1.3974 to −1.1700 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 826.9 | 3598 | +335.1% | +2417.3192 to +3124.8918 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.966 | 4.334 | +9.3% | +0.1923 to +0.5442 | yes: power given |
| pods started | 0.2 | 1.8 | +800.0% | +0.5772 to +2.6228 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.9 | +625.0% | +0.6454 to +4.3546 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.358 | +239.6% | −0.2014 to +2.1180 | no |
| host CPU busy, the real machine under kind (%) | 46.32 | 16.27 | −64.9% | −33.0620 to −27.0213 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.7 | 1509 | +93.6% | +662.9990 to +796.2010 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1163 | +1860446.7% | +1159.6891 to +1165.8692 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1479 | +369625.0% | +1475.1407 to +1481.8593 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 90.61 | 1163 | +1183.3% | +1007.9226 to +1136.5357 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*