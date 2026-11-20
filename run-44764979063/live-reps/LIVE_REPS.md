# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.926 | 4.965 |
| node-hours | 2.518 | 2.513 | 2.064 | 2.082 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 273.9 | 273.8 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 273.9 | 240 | 241.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 435.6 | 362.4 | 423.5 | 365.9 |
| response time (ms), 95th percentile | 1647 | 1532 | 1778 | 1795 |
| response time (ms), 99th percentile | 2332 | 2481 | 2542 | 2712 |
| time over the response line (% of samples) | 20.55 | 14.83 | 19.8 | 15.27 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 8.7 | 9.8 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 118.2 | 79.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 17.29 | 12.16 | 22.97 |
| utilisation (used / allocatable) | 0.06447 | 0.06446 | 0.07955 | 0.07829 |
| CPU used (cores), mean | 1.547 | 1.547 | 1.527 | 1.531 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07307 | 0.07633 |
| CPU used with Omni's own (cores), mean | 1.547 | 1.547 | 1.6 | 1.607 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.7 | 436.1 | 376 | 378 |
| HPA replicas, mean | 2.003 | 2.074 | 2.127 | 2.065 |
| pods started | 0.1 | 0.4 | 0.6 | 0.3 |
| pod start wait, total (s) | 0.2 | 0.6 | 1.3 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0.45 | 0.7 | 0.2667 |
| host CPU busy, the real machine under kind (%) | 43.91 | 45.02 | 46.94 | 48.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 816.7 | 835.8 | 829.4 | 845.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.374 | 4.319 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.6958 | 0.09167 | 0.9542 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | 0.5 | 2.8 |
| queue: job turnaround, submitted to done, mean (s) | 122 | 145.9 | 132.6 | 154.6 |
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
| worker nodes in service, mean | 6 | 4.965 | −17.3% | −1.8910 to −0.1792 | yes: GAIN |
| node-hours | 2.513 | 2.082 | −17.2% | −0.7924 to −0.0700 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274 | +0.0% | −0.8729 to +1.0545 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 241.5 | −11.8% | −59.7881 to −5.0385 | yes: GAIN |
| response time (ms), mean | 362.4 | 365.9 | +1.0% | −24.3070 to +31.2883 | no |
| response time (ms), 95th percentile | 1532 | 1795 | +17.1% | +36.9715 to +488.4725 | yes: LOSS |
| response time (ms), 99th percentile | 2481 | 2712 | +9.3% | −3.2063 to +465.5241 | no |
| time over the response line (% of samples) | 14.83 | 15.27 | +3.0% | −0.0409 to +0.9186 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.1 | +4.6% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.7 | +79.700 (native is 0) | +21.1952 to +138.2048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.29 | 22.97 | +32.9% | +0.7083 to +10.6550 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06446 | 0.07829 | +21.5% | +0.0017 to +0.0260 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.531 | −1.1% | −0.0544 to +0.0217 | no |
| Omni's own CPU (cores), mean | 0 | 0.07633 | +0.076 (native is 0) | +0.0690 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.607 | +3.9% | +0.0191 to +0.1009 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.1 | 378 | −13.3% | −110.7752 to −5.4542 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.074 | 2.065 | −0.4% | −0.1488 to +0.1310 | no |
| pods started | 0.4 | 0.3 | −25.0% | −1.0204 to +0.8204 | no |
| pod start wait, total (s) | 0.6 | 0.8 | +33.3% | −1.9004 to +2.3004 | no |
| pod start wait, mean (s) | 0.45 | 0.2667 | −40.7% | −1.0763 to +0.7096 | no |
| host CPU busy, the real machine under kind (%) | 45.02 | 48.11 | +6.9% | +2.5033 to +3.6799 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.8 | 845.4 | +1.1% | +0.2723 to +18.9277 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.319 | −28.0% | −2.8806 to −0.4820 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.9542 | +37.1% | +0.0138 to +0.5028 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2.8 | +115.4% | −0.2276 to +3.2276 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.9 | 154.6 | +5.9% | −0.4867 to +17.8034 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.513 | −0.2% | −0.0131 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 273.9 | −0.2% | −1.6959 to +0.5393 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 273.9 | −0.2% | −1.6959 to +0.5393 | no |
| response time (ms), mean | 435.6 | 362.4 | −16.8% | −109.2887 to −37.1111 | yes: GAIN |
| response time (ms), 95th percentile | 1647 | 1532 | −7.0% | −273.1255 to +44.0465 | no |
| response time (ms), 99th percentile | 2332 | 2481 | +6.4% | −124.8546 to +422.4624 | no |
| time over the response line (% of samples) | 20.55 | 14.83 | −27.8% | −8.7812 to −2.6590 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 8.7 | −11.2% | −2.8667 to +0.6667 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 17.29 | +48.6% | +2.5209 to +8.7891 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06447 | 0.06446 | −0.0% | −0.0015 to +0.0015 | no |
| CPU used (cores), mean | 1.547 | 1.547 | −0.0% | −0.0361 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.547 | 1.547 | −0.0% | −0.0361 to +0.0356 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.7 | 436.1 | +0.8% | −9.9069 to +16.7914 | no |
| HPA replicas, mean | 2.003 | 2.074 | +3.5% | −0.0758 to +0.2175 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.5656 to +1.3656 | no |
| pod start wait, mean (s) | 0.2 | 0.45 | +125.0% | −0.5272 to +1.0272 | no |
| host CPU busy, the real machine under kind (%) | 43.91 | 45.02 | +2.5% | +0.4443 to +1.7645 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.7 | 835.8 | +2.3% | +7.8938 to +30.3062 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.6958 | +1184.6% | +0.5571 to +0.7262 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | +160.0% | +0.3476 to +1.2524 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 122 | 145.9 | +19.6% | +8.9300 to +38.8617 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.926 | −17.9% | −2.0314 to −0.1175 | yes: GAIN |
| node-hours | 2.518 | 2.064 | −18.0% | −0.8546 to −0.0529 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 273.8 | −0.2% | −1.3882 to +0.1319 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 240 | −12.6% | −65.1493 to −3.7444 | yes: GAIN |
| response time (ms), mean | 435.6 | 423.5 | −2.8% | −27.6743 to +3.4644 | no |
| response time (ms), 95th percentile | 1647 | 1778 | +8.0% | +40.4109 to +221.8331 | yes: LOSS |
| response time (ms), 99th percentile | 2332 | 2542 | +9.0% | +64.1240 to +355.4640 | yes: LOSS |
| time over the response line (% of samples) | 20.55 | 19.8 | −3.6% | −1.4683 to −0.0251 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.8 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.2 | +118.200 (native is 0) | +21.7158 to +214.6842 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 12.16 | +4.5% | −1.6269 to +2.6736 | no |
| utilisation (used / allocatable) | 0.06447 | 0.07955 | +23.4% | +0.0020 to +0.0282 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.527 | −1.3% | −0.0640 to +0.0233 | no |
| Omni's own CPU (cores), mean | 0 | 0.07307 | +0.073 (native is 0) | +0.0661 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.6 | +3.4% | +0.0028 to +0.1027 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.7 | 376 | −13.1% | −104.5172 to −8.8339 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.127 | +6.2% | −0.0712 to +0.3182 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | −0.6342 to +2.8342 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.5256 to +1.5256 | no |
| host CPU busy, the real machine under kind (%) | 43.91 | 46.94 | +6.9% | +2.3167 to +3.7354 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.7 | 829.4 | +1.6% | +3.9520 to +21.4480 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.374 | −27.1% | −2.9465 to −0.3061 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.09167 | +69.2% | −0.0100 to +0.0850 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 122 | 132.6 | +8.6% | +3.4437 to +17.6563 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.926 | −17.9% | −2.0314 to −0.1175 | yes: GAIN |
| node-hours | 2.513 | 2.064 | −17.9% | −0.8503 to −0.0486 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.8 | −0.0% | −1.2939 to +1.1942 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 240 | −12.4% | −64.1748 to −3.5624 | yes: GAIN |
| response time (ms), mean | 362.4 | 423.5 | +16.9% | +20.5456 to +101.6443 | yes: LOSS |
| response time (ms), 95th percentile | 1532 | 1778 | +16.0% | +99.6358 to +391.6872 | yes: LOSS |
| response time (ms), 99th percentile | 2481 | 2542 | +2.5% | −96.3539 to +218.3341 | no |
| time over the response line (% of samples) | 14.83 | 19.8 | +33.5% | +2.3863 to +7.5606 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.8 | +12.6% | −0.4249 to +2.6249 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.2 | +118.200 (native is 0) | +21.7158 to +214.6842 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.29 | 12.16 | −29.7% | −7.5003 to −2.7630 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06446 | 0.07955 | +23.4% | +0.0010 to +0.0292 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.527 | −1.3% | −0.0527 to +0.0125 | no |
| Omni's own CPU (cores), mean | 0 | 0.07307 | +0.073 (native is 0) | +0.0661 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.6 | +3.4% | +0.0172 to +0.0888 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.1 | 376 | −13.8% | −117.2069 to −3.0286 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.074 | 2.127 | +2.5% | −0.0809 to +0.1863 | no |
| pods started | 0.4 | 0.6 | +50.0% | −0.6793 to +1.0793 | no |
| pod start wait, total (s) | 0.6 | 1.3 | +116.7% | −1.1174 to +2.5174 | no |
| pod start wait, mean (s) | 0.45 | 0.7 | +55.6% | −0.8063 to +1.3063 | no |
| host CPU busy, the real machine under kind (%) | 45.02 | 46.94 | +4.3% | +1.6178 to +2.2256 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.8 | 829.4 | −0.8% | −12.7282 to −0.0718 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.374 | −27.1% | −2.9465 to −0.3061 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.09167 | −86.8% | −0.6704 to −0.5379 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.5 | −61.5% | −1.1016 to −0.4984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 145.9 | 132.6 | −9.1% | −22.8844 to −3.8072 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.965 | −17.3% | −1.8910 to −0.1792 | yes: GAIN |
| node-hours | 2.518 | 2.082 | −17.3% | −0.7961 to −0.0750 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274 | −0.2% | −1.5694 to +0.5945 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 241.5 | −12.0% | −60.6816 to −5.3017 | yes: GAIN |
| response time (ms), mean | 435.6 | 365.9 | −16.0% | −86.8990 to −52.5194 | yes: GAIN |
| response time (ms), 95th percentile | 1647 | 1795 | +9.0% | −45.6374 to +342.0024 | no |
| response time (ms), 99th percentile | 2332 | 2712 | +16.3% | +27.6638 to +732.2618 | yes: LOSS |
| time over the response line (% of samples) | 20.55 | 15.27 | −25.7% | −8.1383 to −2.4242 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.1 | −7.1% | −2.5485 to +1.1485 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.7 | +79.700 (native is 0) | +21.1952 to +138.2048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 22.97 | +97.4% | +6.4181 to +16.2552 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06447 | 0.07829 | +21.4% | +0.0026 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.531 | −1.1% | −0.0575 to +0.0243 | no |
| Omni's own CPU (cores), mean | 0 | 0.07633 | +0.076 (native is 0) | +0.0690 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.607 | +3.9% | +0.0123 to +0.1071 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.7 | 378 | −12.6% | −97.9917 to −11.3533 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.065 | +3.1% | −0.1168 to +0.2407 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0.2 | 0.2667 | +33.3% | −0.0841 to +0.2175 | no |
| host CPU busy, the real machine under kind (%) | 43.91 | 48.11 | +9.6% | +3.1874 to +5.2047 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.7 | 845.4 | +3.5% | +12.2391 to +45.1609 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.319 | −28.0% | −2.8806 to −0.4820 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.9542 | +1661.5% | +0.6113 to +1.1887 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.8 | +460.0% | +0.4210 to +4.1790 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 122 | 154.6 | +26.7% | +13.3417 to +51.7667 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*