# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.159 | 5.248 |
| node-hours | 2.514 | 2.517 | 2.159 | 2.202 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | 271.9 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | 245.5 | 249.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 310.3 | 330.6 | 280.3 | 321.6 |
| response time (ms), 95th percentile | 1071 | 1354 | 1102 | 1457 |
| response time (ms), 99th percentile | 1477 | 1954 | 1524 | 2080 |
| time over the response line (% of samples) | 12.34 | 11.08 | 12.2 | 11.8 |
| failed requests (%) | 0.01124 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9 | 7.7 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 44.6 | 35.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.855 | 20.94 | 9.435 | 19.9 |
| utilisation (used / allocatable) | 0.05983 | 0.05968 | 0.07115 | 0.06966 |
| CPU used (cores), mean | 1.436 | 1.432 | 1.434 | 1.441 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01614 | 0.01809 |
| CPU used with Omni's own (cores), mean | 1.436 | 1.432 | 1.45 | 1.459 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.7 | 465 | 412 | 415.9 |
| HPA replicas, mean | 1.939 | 2.115 | 2.172 | 2.008 |
| pods started | 0.1 | 0.3 | 0.7 | 0.2 |
| pod start wait, total (s) | 0.2 | 0.4 | 1.1 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.4 | 0.5 | 0.2 |
| host CPU busy, the real machine under kind (%) | 40.77 | 43.42 | 41.84 | 44.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.8 | 802.2 | 776.2 | 806 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.53 | 4.653 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.9125 | 0.05417 | 0.9833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.7 | 0.3 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 79.13 | 107.4 | 81.31 | 110.7 |
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
| worker nodes in service, mean | 6 | 5.248 | −12.5% | −1.4270 to −0.0761 | yes: GAIN |
| node-hours | 2.517 | 2.202 | −12.5% | −0.6007 to −0.0288 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.5903 to +1.0112 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 249.3 | −8.6% | −44.6208 to −2.1667 | yes: GAIN |
| response time (ms), mean | 330.6 | 321.6 | −2.7% | −43.5409 to +25.5974 | no |
| response time (ms), 95th percentile | 1354 | 1457 | +7.6% | −16.1619 to +221.7499 | no |
| response time (ms), 99th percentile | 1954 | 2080 | +6.4% | −76.0176 to +327.5082 | no |
| time over the response line (% of samples) | 11.08 | 11.8 | +6.5% | −1.1805 to +2.6191 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.5 | +5.6% | −0.8168 to +1.8168 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.2 | +35.200 (native is 0) | +22.0761 to +48.3239 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.94 | 19.9 | −5.0% | −3.4254 to +1.3454 | no |
| utilisation (used / allocatable) | 0.05968 | 0.06966 | +16.7% | −0.0001 to +0.0201 | no |
| CPU used (cores), mean | 1.432 | 1.441 | +0.6% | −0.0190 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0 | 0.01809 | +0.018 (native is 0) | +0.0165 to +0.0197 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.459 | +1.8% | +0.0001 to +0.0527 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 415.9 | −10.6% | −98.0340 to −0.1213 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.115 | 2.008 | −5.0% | −0.2502 to +0.0371 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.4 | 0.2 | −50.0% | −0.8573 to +0.4573 | no |
| pod start wait, mean (s) | 0.4 | 0.2 | −50.0% | −0.8573 to +0.4573 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 44.52 | +2.5% | +0.7431 to +1.4398 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.2 | 806 | +0.5% | +0.8449 to +6.7551 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.653 | −22.4% | −2.4445 to −0.2485 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 0.9833 | +7.8% | −0.0192 to +0.1609 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 2.3 | −14.8% | −1.0911 to +0.2911 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.4 | 110.7 | +3.0% | −0.2127 to +6.7127 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.517 | +0.1% | −0.0021 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | +0.1% | −0.2129 to +1.0064 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | +0.1% | −0.2129 to +1.0064 | no |
| response time (ms), mean | 310.3 | 330.6 | +6.5% | −7.4730 to +48.1005 | no |
| response time (ms), 95th percentile | 1071 | 1354 | +26.4% | −8.2760 to +573.8950 | no |
| response time (ms), 99th percentile | 1477 | 1954 | +32.3% | +120.8656 to +833.7714 | yes: LOSS |
| time over the response line (% of samples) | 12.34 | 11.08 | −10.2% | −4.0052 to +1.4910 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9 | +15.4% | −0.1403 to +2.5403 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.855 | 20.94 | +136.5% | +4.7003 to +19.4764 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05983 | 0.05968 | −0.3% | −0.0016 to +0.0013 | no |
| CPU used (cores), mean | 1.436 | 1.432 | −0.3% | −0.0384 to +0.0309 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.436 | 1.432 | −0.3% | −0.0384 to +0.0309 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.7 | 465 | +0.9% | −8.7804 to +17.3930 | no |
| HPA replicas, mean | 1.939 | 2.115 | +9.1% | +0.0581 to +0.2943 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 40.77 | 43.42 | +6.5% | +1.9294 to +3.3736 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.8 | 802.2 | +3.7% | +4.7691 to +52.0309 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.9125 | +1268.8% | +0.5504 to +1.1412 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.7 | +800.0% | +0.7412 to +4.0588 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.13 | 107.4 | +35.8% | +8.2526 to +48.3474 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.159 | −14.0% | −1.5977 to −0.0845 | yes: GAIN |
| node-hours | 2.514 | 2.159 | −14.1% | −0.6717 to −0.0390 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.9 | −0.2% | −1.0764 to +0.1648 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 245.5 | −9.9% | −50.8591 to −2.8025 | yes: GAIN |
| response time (ms), mean | 310.3 | 280.3 | −9.7% | −41.5108 to −18.5254 | yes: GAIN |
| response time (ms), 95th percentile | 1071 | 1102 | +2.9% | −21.2610 to +84.1550 | no |
| response time (ms), 99th percentile | 1477 | 1524 | +3.2% | −96.1978 to +190.7266 | no |
| time over the response line (% of samples) | 12.34 | 12.2 | −1.2% | −1.1866 to +0.8930 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.7 | −1.3% | −1.8342 to +1.6342 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 | +44.600 (native is 0) | +23.6334 to +65.5666 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.855 | 9.435 | +6.5% | −1.1932 to +2.3532 | no |
| utilisation (used / allocatable) | 0.05983 | 0.07115 | +18.9% | +0.0010 to +0.0216 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.434 | −0.2% | −0.0344 to +0.0297 | no |
| Omni's own CPU (cores), mean | 0 | 0.01614 | +0.016 (native is 0) | +0.0145 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.45 | +1.0% | −0.0186 to +0.0462 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.7 | 412 | −10.6% | −91.2269 to −6.0841 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.939 | 2.172 | +12.0% | −0.0634 to +0.5294 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.3048 to +1.5048 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.4676 to +2.2676 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | −0.1559 to +0.7559 | no |
| host CPU busy, the real machine under kind (%) | 40.77 | 41.84 | +2.6% | +0.6595 to +1.4751 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.8 | 776.2 | +0.3% | −0.3018 to +5.1018 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.53 | −24.5% | −2.6754 to −0.2648 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | −18.8% | −0.0370 to +0.0120 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.13 | 81.31 | +2.7% | −1.6803 to +6.0303 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.159 | −14.0% | −1.5977 to −0.0845 | yes: GAIN |
| node-hours | 2.517 | 2.158 | −14.2% | −0.6755 to −0.0409 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.9 | −0.3% | −1.3420 to −0.3631 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 245.5 | −10.0% | −51.0010 to −3.4541 | yes: GAIN |
| response time (ms), mean | 330.6 | 280.3 | −15.2% | −79.3648 to −21.2988 | yes: GAIN |
| response time (ms), 95th percentile | 1354 | 1102 | −18.6% | −513.2230 to +10.4980 | no |
| response time (ms), 99th percentile | 1954 | 1524 | −22.0% | −769.9926 to −90.1156 | yes: GAIN |
| time over the response line (% of samples) | 11.08 | 12.2 | +10.0% | −1.6694 to +3.8900 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 7.7 | −14.4% | −3.0859 to +0.4859 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 | +44.600 (native is 0) | +23.6334 to +65.5666 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.94 | 9.435 | −54.9% | −19.0598 to −3.9569 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05968 | 0.07115 | +19.2% | +0.0003 to +0.0227 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 1.434 | +0.1% | −0.0309 to +0.0338 | no |
| Omni's own CPU (cores), mean | 0 | 0.01614 | +0.016 (native is 0) | +0.0145 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.45 | +1.2% | −0.0138 to +0.0490 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 412 | −11.4% | −104.3822 to −1.5415 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.115 | 2.172 | +2.7% | −0.2720 to +0.3857 | no |
| pods started | 0.3 | 0.7 | +133.3% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | −0.3144 to +1.7144 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | −0.4396 to +0.6396 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 41.84 | −3.6% | −2.2972 to −0.8713 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.2 | 776.2 | −3.2% | −47.7748 to −4.2252 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.53 | −24.5% | −2.6754 to −0.2648 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 0.05417 | −94.1% | −1.1578 to −0.5589 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 0.3 | −88.9% | −4.1586 to −0.6414 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 107.4 | 81.31 | −24.3% | −43.4528 to −8.7972 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.248 | −12.5% | −1.4270 to −0.0761 | yes: GAIN |
| node-hours | 2.514 | 2.202 | −12.4% | −0.5976 to −0.0262 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.9 | +0.2% | −0.3726 to +1.5870 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 249.3 | −8.4% | −44.6104 to −1.3835 | yes: GAIN |
| response time (ms), mean | 310.3 | 321.6 | +3.7% | −18.6745 to +41.3585 | no |
| response time (ms), 95th percentile | 1071 | 1457 | +36.0% | +63.7507 to +707.4563 | yes: LOSS |
| response time (ms), 99th percentile | 1477 | 2080 | +40.8% | +150.4591 to +1055.6685 | yes: LOSS |
| time over the response line (% of samples) | 12.34 | 11.8 | −4.4% | −3.8102 to +2.7346 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9.5 | +21.8% | −0.1485 to +3.5485 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.2 | +35.200 (native is 0) | +22.0761 to +48.3239 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.855 | 19.9 | +124.8% | +3.3984 to +18.6983 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05983 | 0.06966 | +16.4% | +0.0009 to +0.0187 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.441 | +0.3% | −0.0240 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.01809 | +0.018 (native is 0) | +0.0165 to +0.0197 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.459 | +1.6% | −0.0063 to +0.0515 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.7 | 415.9 | −9.7% | −82.9431 to −6.5995 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.939 | 2.008 | +3.6% | −0.0282 to +0.1675 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| host CPU busy, the real machine under kind (%) | 40.77 | 44.52 | +9.2% | +3.0783 to +4.4076 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.8 | 806 | +4.2% | +6.8723 to +57.5277 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.653 | −22.4% | −2.4445 to −0.2485 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.9833 | +1375.0% | +0.6388 to +1.1945 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.3 | +666.7% | +0.9337 to +3.0663 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.13 | 110.7 | +39.9% | +11.1313 to +51.9687 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*