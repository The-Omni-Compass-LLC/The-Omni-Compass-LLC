# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.7 | 4.548 |
| node-hours | 2.516 | 2.522 | 1.97 | 1.9 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.9 | 272.1 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.9 | 231.2 | 226.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 292.6 | 250.5 | 271.9 | 262.1 |
| response time (ms), 95th percentile | 980.5 | 958.9 | 1062 | 1164 |
| response time (ms), 99th percentile | 1349 | 1515 | 1462 | 1637 |
| time over the response line (% of samples) | 11.16 | 6.745 | 11.63 | 8.34 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6 | 8.4 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 133 | 106.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 10.19 | 36.11 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.843 | 10.62 | 10.17 | 12.09 |
| utilisation (used / allocatable) | 0.05904 | 0.05869 | 0.07685 | 0.08069 |
| CPU used (cores), mean | 1.417 | 1.409 | 1.412 | 1.441 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07103 | 0.06981 |
| CPU used with Omni's own (cores), mean | 1.417 | 1.409 | 1.483 | 1.511 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 469.6 | 391.5 | 376.7 |
| HPA replicas, mean | 1.928 | 2.058 | 2.354 | 2.127 |
| pods started | 0 | 0.4 | 1.7 | 0.5 |
| pod start wait, total (s) | 0 | 0.9 | 3.3 | 1.5 |
| pod start wait, mean (s) | 0 | 0.65 | 1.5 | 0.525 |
| host CPU busy, the real machine under kind (%) | 40.43 | 40.54 | 43.77 | 44.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 765.4 | 770.5 | 771.8 | 781.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.884 | 3.516 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 | 0.075 | 0.1542 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | 0.6 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 73.41 | 75.99 | 79.65 | 87.45 |
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
| worker nodes in service, mean | 6 | 4.548 | −24.2% | −2.2074 to −0.6965 | yes: GAIN |
| node-hours | 2.522 | 1.9 | −24.7% | −0.9394 to −0.3062 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.9 | −0.4% | −1.4904 to −0.5688 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 226.4 | −17.0% | −70.5141 to −22.5409 | yes: GAIN |
| response time (ms), mean | 250.5 | 262.1 | +4.6% | −36.0243 to +59.1867 | no |
| response time (ms), 95th percentile | 958.9 | 1164 | +21.4% | −47.1540 to +458.2460 | no |
| response time (ms), 99th percentile | 1515 | 1637 | +8.1% | −26.9420 to +270.8342 | no |
| time over the response line (% of samples) | 6.745 | 8.34 | +23.6% | −0.2814 to +3.4713 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.4 | +6.7% | −0.8707 to +1.6707 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +55.3290 to +158.4710 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.62 | 12.09 | +13.8% | −2.0446 to +4.9846 | no |
| utilisation (used / allocatable) | 0.05869 | 0.08069 | +37.5% | +0.0106 to +0.0334 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.441 | +2.3% | +0.0055 to +0.0589 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06981 | +0.070 (native is 0) | +0.0639 to +0.0757 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.511 | +7.2% | +0.0721 to +0.1319 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 376.7 | −19.8% | −138.5904 to −47.2296 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.127 | +3.4% | −0.2039 to +0.3430 | no |
| pods started | 0.4 | 0.5 | +25.0% | −1.0410 to +1.2410 | no |
| pod start wait, total (s) | 0.9 | 1.5 | +66.7% | −2.7922 to +3.9922 | no |
| pod start wait, mean (s) | 0.65 | 0.525 | −19.2% | −1.4014 to +1.1514 | no |
| host CPU busy, the real machine under kind (%) | 40.54 | 44.02 | +8.6% | +2.9187 to +4.0423 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.5 | 781.8 | +1.5% | −1.1355 to +23.7355 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.516 | −41.4% | −3.5930 to −1.3760 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1542 | +164.3% | −0.0440 to +0.2357 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.99 | 87.45 | +15.1% | −2.7906 to +25.7072 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.522 | +0.3% | +0.0011 to +0.0125 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.9 | +0.3% | +0.3516 to +1.2208 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.9 | +0.3% | +0.3516 to +1.2208 | yes: power given |
| response time (ms), mean | 292.6 | 250.5 | −14.4% | −73.6742 to −10.4848 | yes: GAIN |
| response time (ms), 95th percentile | 980.5 | 958.9 | −2.2% | −79.9241 to +36.6641 | no |
| response time (ms), 99th percentile | 1349 | 1515 | +12.3% | −95.6543 to +426.4105 | no |
| time over the response line (% of samples) | 11.16 | 6.745 | −39.6% | −8.4151 to −0.4163 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6 | −24.1% | −3.9077 to +0.1077 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.843 | 10.62 | +20.1% | +0.0997 to +3.4470 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05904 | 0.05869 | −0.6% | −0.0016 to +0.0009 | no |
| CPU used (cores), mean | 1.417 | 1.409 | −0.6% | −0.0374 to +0.0207 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.417 | 1.409 | −0.6% | −0.0374 to +0.0207 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 469.6 | +0.9% | −6.0678 to +14.6109 | no |
| HPA replicas, mean | 1.928 | 2.058 | +6.7% | −0.0782 to +0.3365 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.2898 to +2.0898 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.650 (native is 0) | −0.1049 to +1.4049 | no |
| host CPU busy, the real machine under kind (%) | 40.43 | 40.54 | +0.3% | −0.6430 to +0.8597 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.4 | 770.5 | +0.7% | −2.4509 to +12.6509 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 | +40.0% | −0.0236 to +0.0569 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.41 | 75.99 | +3.5% | −1.8379 to +6.9962 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.7 | −21.7% | −2.0591 to −0.5409 | yes: GAIN |
| node-hours | 2.516 | 1.97 | −21.7% | −0.8628 to −0.2284 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −0.6629 to +0.6326 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 231.2 | −15.0% | −64.7635 to −17.0376 | yes: GAIN |
| response time (ms), mean | 292.6 | 271.9 | −7.1% | −38.4446 to −2.9760 | yes: GAIN |
| response time (ms), 95th percentile | 980.5 | 1062 | +8.3% | +2.2399 to +160.9871 | yes: LOSS |
| response time (ms), 99th percentile | 1349 | 1462 | +8.4% | −5.8000 to +231.3206 | no |
| time over the response line (% of samples) | 11.16 | 11.63 | +4.2% | −0.8573 to +1.7955 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.4 | +6.3% | −1.1944 to +2.1944 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133 | +133.000 (native is 0) | +75.0518 to +190.9482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.843 | 10.17 | +15.0% | −0.8068 to +3.4668 | no |
| utilisation (used / allocatable) | 0.05904 | 0.07685 | +30.2% | +0.0062 to +0.0295 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.417 | 1.412 | −0.4% | −0.0411 to +0.0307 | no |
| Omni's own CPU (cores), mean | 0 | 0.07103 | +0.071 (native is 0) | +0.0651 to +0.0770 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.483 | +4.6% | +0.0289 to +0.1028 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 391.5 | −15.9% | −117.6950 to −30.0405 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.928 | 2.354 | +22.1% | +0.2311 to +0.6199 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.8706 to +2.5294 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +1.5141 to +5.0859 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | +0.8592 to +2.1408 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.43 | 43.77 | +8.3% | +2.7196 to +3.9767 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.4 | 771.8 | +0.8% | −0.6748 to +13.4748 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.884 | −35.3% | −3.1765 to −1.0552 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.075 | +80.0% | −0.0059 to +0.0726 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.41 | 79.65 | +8.5% | −0.7017 to +13.1767 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.7 | −21.7% | −2.0591 to −0.5409 | yes: GAIN |
| node-hours | 2.522 | 1.97 | −21.9% | −0.8711 to −0.2338 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.1 | −0.3% | −1.4056 to −0.1970 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 231.2 | −15.3% | −65.6430 to −17.7305 | yes: GAIN |
| response time (ms), mean | 250.5 | 271.9 | +8.5% | −15.7892 to +58.5277 | no |
| response time (ms), 95th percentile | 958.9 | 1062 | +10.8% | +38.3660 to +168.1210 | yes: LOSS |
| response time (ms), 99th percentile | 1515 | 1462 | −3.5% | −273.8911 to +168.6555 | no |
| time over the response line (% of samples) | 6.745 | 11.63 | +72.4% | +1.0642 to +8.7055 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 8.4 | +40.0% | +0.0834 to +4.7166 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133 | +133.000 (native is 0) | +75.0518 to +190.9482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.62 | 10.17 | −4.2% | −2.5966 to +1.7099 | no |
| utilisation (used / allocatable) | 0.05869 | 0.07685 | +30.9% | +0.0060 to +0.0303 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.412 | +0.2% | −0.0307 to +0.0370 | no |
| Omni's own CPU (cores), mean | 0 | 0.07103 | +0.071 (native is 0) | +0.0651 to +0.0770 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.483 | +5.3% | +0.0401 to +0.1083 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 391.5 | −16.6% | −126.8831 to −29.3955 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.354 | +14.4% | +0.1421 to +0.4506 | yes: power given |
| pods started | 0.4 | 1.7 | +325.0% | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0.9 | 3.3 | +266.7% | +0.4571 to +4.3429 | yes: LOSS |
| pod start wait, mean (s) | 0.65 | 1.5 | +130.8% | −0.2273 to +1.9273 | no |
| host CPU busy, the real machine under kind (%) | 40.54 | 43.77 | +8.0% | +2.2805 to +4.1992 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.5 | 771.8 | +0.2% | −7.5192 to +10.1192 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.884 | −35.3% | −3.1765 to −1.0552 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.075 | +28.6% | −0.0042 to +0.0375 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.99 | 79.65 | +4.8% | −0.8144 to +8.1311 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.548 | −24.2% | −2.2074 to −0.6965 | yes: GAIN |
| node-hours | 2.516 | 1.9 | −24.5% | −0.9311 to −0.3008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.9 | −0.1% | −0.8200 to +0.3332 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 226.4 | −16.8% | −69.6395 to −21.8431 | yes: GAIN |
| response time (ms), mean | 292.6 | 262.1 | −10.4% | −52.1133 to −8.8833 | yes: GAIN |
| response time (ms), 95th percentile | 980.5 | 1164 | +18.8% | −109.4935 to +477.3255 | no |
| response time (ms), 99th percentile | 1349 | 1637 | +21.3% | −98.7579 to +673.4063 | no |
| time over the response line (% of samples) | 11.16 | 8.34 | −25.3% | −5.0235 to −0.6182 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6.4 | −19.0% | −3.1605 to +0.1605 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +55.3290 to +158.4710 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.843 | 12.09 | +36.7% | +0.5895 to +5.8972 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05904 | 0.08069 | +36.7% | +0.0108 to +0.0325 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.417 | 1.441 | +1.7% | −0.0167 to +0.0644 | no |
| Omni's own CPU (cores), mean | 0 | 0.06981 | +0.070 (native is 0) | +0.0639 to +0.0757 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.511 | +6.6% | +0.0495 to +0.1378 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 376.7 | −19.0% | −129.4625 to −47.8144 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.928 | 2.127 | +10.3% | −0.0097 to +0.4072 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.4079 to +1.4079 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −1.4251 to +4.4251 | no |
| pod start wait, mean (s) | 0 | 0.525 | +0.525 (native is 0) | −0.2943 to +1.3443 | no |
| host CPU busy, the real machine under kind (%) | 40.43 | 44.02 | +8.9% | +2.6004 to +4.5773 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.4 | 781.8 | +2.1% | −2.9477 to +35.7477 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.516 | −41.4% | −3.5930 to −1.3760 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1542 | +270.0% | −0.0502 to +0.2752 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | −0.1001 to +0.9001 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.41 | 87.45 | +19.1% | +0.3149 to +27.7601 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*