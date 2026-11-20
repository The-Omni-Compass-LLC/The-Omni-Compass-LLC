# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.906 | 10.8 |
| node-hours | 5.021 | 5.034 | 4.156 | 4.531 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.3 | 525.1 | 527.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 524.3 | 459.3 | 490 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 434.4 | 567.9 | 469.5 | 813.2 |
| response time (ms), 95th percentile | 1533 | 1850 | 1816 | 3286 |
| response time (ms), 99th percentile | 2068 | 2539 | 2467 | 4503 |
| time over the response line (% of samples) | 19.26 | 26.33 | 21.49 | 34.34 |
| failed requests (%) | 0 | 0.01754 | 0.01653 | 0.2037 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12.6 | 12.2 | 15.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 178.7 | 103.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 20.09 | 30.76 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 43.54 | 22.41 | 26.5 |
| utilisation (used / allocatable) | 0.03322 | 0.03193 | 0.03987 | 0.04068 |
| CPU used (cores), mean | 1.594 | 1.532 | 1.568 | 1.75 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05382 | 0.05352 |
| CPU used with Omni's own (cores), mean | 1.594 | 1.532 | 1.621 | 1.803 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 822.1 | 703.9 | 671.4 |
| HPA replicas, mean | 4.121 | 4.001 | 4.429 | 4.402 |
| pods started | 0.2 | 0.2 | 1.7 | 1.9 |
| pod start wait, total (s) | 0.4 | 0.4 | 3.4 | 5.6 |
| pod start wait, mean (s) | 0.4 | 0.4 | 1.17 | 1.633 |
| host CPU busy, the real machine under kind (%) | 48.61 | 53.12 | 53.2 | 61.62 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 820.2 | 884.6 | 844.9 | 993.6 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.149 | 9.304 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 2.804 | 0.08333 | 10.47 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 18.1 | 0.5 | 53.1 |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 180.6 | 154.4 | 280.1 |
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
| worker nodes in service, mean | 12 | 10.8 | −10.0% | −2.2577 to −0.1365 | yes: GAIN |
| node-hours | 5.034 | 4.531 | −10.0% | −0.9448 to −0.0612 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 527.7 | +0.7% | +1.6416 to +5.1813 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 490 | −6.5% | −67.8478 to −0.7834 | yes: GAIN |
| response time (ms), mean | 567.9 | 813.2 | +43.2% | +133.3412 to +357.3269 | yes: LOSS |
| response time (ms), 95th percentile | 1850 | 3286 | +77.6% | +1043.8431 to +1826.7509 | yes: LOSS |
| response time (ms), 99th percentile | 2539 | 4503 | +77.4% | +1329.8856 to +2598.1100 | yes: LOSS |
| time over the response line (% of samples) | 26.33 | 34.34 | +30.4% | +0.7309 to +15.2965 | yes: LOSS |
| failed requests (%) | 0.01754 | 0.2037 | +1061.0% | −0.2440 to +0.6163 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 15.6 | +23.8% | +0.3881 to +5.6119 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.6 | +103.600 (native is 0) | +24.3294 to +182.8706 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.54 | 26.5 | −39.1% | −53.6941 to +19.6007 | no |
| utilisation (used / allocatable) | 0.03193 | 0.04068 | +27.4% | +0.0052 to +0.0123 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.75 | +14.2% | +0.1292 to +0.3055 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05352 | +0.054 (native is 0) | +0.0490 to +0.0581 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.803 | +17.7% | +0.1813 to +0.3604 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.1 | 671.4 | −18.3% | −207.2821 to −94.2228 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.001 | 4.402 | +10.0% | +0.0597 to +0.7434 | yes: power given |
| pods started | 0.2 | 1.9 | +850.0% | +0.1901 to +3.2099 | yes: power given |
| pod start wait, total (s) | 0.4 | 5.6 | +1300.0% | −0.2560 to +10.6560 | no |
| pod start wait, mean (s) | 0.4 | 1.633 | +308.3% | −0.2118 to +2.6784 | no |
| host CPU busy, the real machine under kind (%) | 53.12 | 61.62 | +16.0% | +6.5825 to +10.4067 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.6 | 993.6 | +12.3% | +64.7382 to +153.2618 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.304 | −22.5% | −4.7570 to −0.6354 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 2.804 | 10.47 | +273.4% | −4.4703 to +19.8037 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 18.1 | 53.1 | +193.4% | −20.8184 to +90.8184 | no |
| queue: job turnaround, submitted to done, mean (s) | 180.6 | 280.1 | +55.1% | +54.1378 to +144.7872 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.021 | 5.034 | +0.3% | +0.0028 to +0.0239 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.3 | +0.1% | −2.0369 to +2.7467 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 524.3 | +0.1% | −2.0369 to +2.7467 | no |
| response time (ms), mean | 434.4 | 567.9 | +30.7% | +11.0796 to +255.9697 | yes: LOSS |
| response time (ms), 95th percentile | 1533 | 1850 | +20.7% | +87.4027 to +546.6283 | yes: LOSS |
| response time (ms), 99th percentile | 2068 | 2539 | +22.8% | −72.6296 to +1015.0020 | no |
| time over the response line (% of samples) | 19.26 | 26.33 | +36.7% | +1.5667 to +12.5757 | yes: LOSS |
| failed requests (%) | 0 | 0.01754 | +0.018 (native is 0) | −0.0221 to +0.0572 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12.6 | +12.5% | +0.4344 to +2.3656 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 43.54 | +257.8% | −17.5983 to +80.3483 | no |
| utilisation (used / allocatable) | 0.03322 | 0.03193 | −3.9% | −0.0044 to +0.0019 | no |
| CPU used (cores), mean | 1.594 | 1.532 | −3.9% | −0.2127 to +0.0889 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.594 | 1.532 | −3.9% | −0.2127 to +0.0889 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 822.1 | +2.6% | −38.2025 to +80.1558 | no |
| HPA replicas, mean | 4.121 | 4.001 | −2.9% | −0.3401 to +0.0994 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | ±0.0% | −0.5840 to +0.5840 | no |
| host CPU busy, the real machine under kind (%) | 48.61 | 53.12 | +9.3% | +2.6260 to +6.4127 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.2 | 884.6 | +7.9% | +14.6027 to +114.1973 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 2.804 | +2592.0% | −3.0730 to +8.4730 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 18.1 | +2485.7% | −20.9551 to +55.7551 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 180.6 | +38.2% | +7.9500 to +91.8250 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.906 | −17.4% | −3.2997 to −0.8878 | yes: GAIN |
| node-hours | 5.021 | 4.156 | −17.2% | −1.3750 to −0.3548 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 525.1 | +0.2% | −0.6273 to +3.0697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 459.3 | −12.3% | −102.8701 to −26.3292 | yes: GAIN |
| response time (ms), mean | 434.4 | 469.5 | +8.1% | −30.0698 to +100.4468 | no |
| response time (ms), 95th percentile | 1533 | 1816 | +18.5% | −12.5604 to +579.0804 | no |
| response time (ms), 99th percentile | 2068 | 2467 | +19.3% | +4.4613 to +794.0837 | yes: LOSS |
| time over the response line (% of samples) | 19.26 | 21.49 | +11.6% | −2.3843 to +6.8355 | no |
| failed requests (%) | 0 | 0.01653 | +0.017 (native is 0) | −0.0209 to +0.0539 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12.2 | +8.9% | −0.5816 to +2.5816 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 178.7 | +178.700 (native is 0) | +69.0449 to +288.3551 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 22.41 | +84.2% | −9.1643 to +29.6576 | no |
| utilisation (used / allocatable) | 0.03322 | 0.03987 | +20.0% | +0.0017 to +0.0116 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.594 | 1.568 | −1.7% | −0.1187 to +0.0651 | no |
| Omni's own CPU (cores), mean | 0 | 0.05382 | +0.054 (native is 0) | +0.0497 to +0.0580 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.594 | 1.621 | +1.7% | −0.0632 to +0.1173 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 703.9 | −12.1% | −172.8392 to −21.7145 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.121 | 4.429 | +7.5% | −0.0662 to +0.6826 | no |
| pods started | 0.2 | 1.7 | +750.0% | +0.1832 to +2.8168 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.4 | +750.0% | +0.1388 to +5.8612 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.17 | +192.5% | −0.2107 to +1.7507 | no |
| host CPU busy, the real machine under kind (%) | 48.61 | 53.2 | +9.5% | +3.2346 to +5.9609 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.2 | 844.9 | +3.0% | −5.0425 to +54.4425 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 8.149 | −32.1% | −5.7536 to −1.9478 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.08333 | −20.0% | −0.0856 to +0.0439 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | −28.6% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 154.4 | +18.1% | −5.3607 to +52.7440 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.906 | −17.4% | −3.2997 to −0.8878 | yes: GAIN |
| node-hours | 5.034 | 4.156 | −17.4% | −1.3906 to −0.3660 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 525.1 | +0.2% | −1.8995 to +3.6320 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 459.3 | −12.4% | −104.3813 to −25.5279 | yes: GAIN |
| response time (ms), mean | 567.9 | 469.5 | −17.3% | −166.0904 to −30.5819 | yes: GAIN |
| response time (ms), 95th percentile | 1850 | 1816 | −1.8% | −308.6464 to +241.1354 | no |
| response time (ms), 99th percentile | 2539 | 2467 | −2.8% | −468.7520 to +324.9246 | no |
| time over the response line (% of samples) | 26.33 | 21.49 | −18.4% | −7.9811 to −1.7101 | yes: GAIN |
| failed requests (%) | 0.01754 | 0.01653 | −5.8% | −0.0585 to +0.0565 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 12.2 | −3.2% | −1.6251 to +0.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 178.7 | +178.700 (native is 0) | +69.0449 to +288.3551 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.54 | 22.41 | −48.5% | −66.0373 to +23.7807 | no |
| utilisation (used / allocatable) | 0.03193 | 0.03987 | +24.9% | +0.0034 to +0.0124 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.568 | +2.3% | −0.1228 to +0.1929 | no |
| Omni's own CPU (cores), mean | 0 | 0.05382 | +0.054 (native is 0) | +0.0497 to +0.0580 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.621 | +5.8% | −0.0708 to +0.2486 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.1 | 703.9 | −14.4% | −189.8085 to −46.6986 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.001 | 4.429 | +10.7% | +0.1820 to +0.6750 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | +0.1407 to +2.8593 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.4 | +750.0% | −0.1088 to +6.1088 | no |
| pod start wait, mean (s) | 0.4 | 1.17 | +192.5% | −0.3664 to +1.9064 | no |
| host CPU busy, the real machine under kind (%) | 53.12 | 53.2 | +0.1% | −0.6209 to +0.7776 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.6 | 844.9 | −4.5% | −61.6776 to −17.7224 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.149 | −32.1% | −5.7536 to −1.9478 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 2.804 | 0.08333 | −97.0% | −8.4471 to +3.0054 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 18.1 | 0.5 | −97.2% | −55.9047 to +20.7047 | no |
| queue: job turnaround, submitted to done, mean (s) | 180.6 | 154.4 | −14.5% | −43.2787 to −9.1130 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.8 | −10.0% | −2.2577 to −0.1365 | yes: GAIN |
| node-hours | 5.021 | 4.531 | −9.8% | −0.9278 to −0.0516 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 527.7 | +0.7% | +1.2556 to +6.2772 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 490 | −6.5% | −66.9417 to −0.9797 | yes: GAIN |
| response time (ms), mean | 434.4 | 813.2 | +87.2% | +248.7201 to +508.9974 | yes: LOSS |
| response time (ms), 95th percentile | 1533 | 3286 | +114.3% | +1290.7215 to +2213.9035 | yes: LOSS |
| response time (ms), 99th percentile | 2068 | 4503 | +117.8% | +1769.9024 to +3100.4656 | yes: LOSS |
| time over the response line (% of samples) | 19.26 | 34.34 | +78.3% | +9.3421 to +20.8277 | yes: LOSS |
| failed requests (%) | 0 | 0.2037 | +0.204 (native is 0) | −0.2219 to +0.6293 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 15.6 | +39.3% | +1.6564 to +7.1436 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.6 | +103.600 (native is 0) | +24.3294 to +182.8706 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 26.5 | +117.8% | −2.3824 to +31.0391 | no |
| utilisation (used / allocatable) | 0.03322 | 0.04068 | +22.5% | +0.0031 to +0.0118 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.594 | 1.75 | +9.8% | +0.0263 to +0.2846 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05352 | +0.054 (native is 0) | +0.0490 to +0.0581 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.594 | 1.803 | +13.1% | +0.0831 to +0.3348 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 671.4 | −16.2% | −199.4011 to −60.1505 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.121 | 4.402 | +6.8% | −0.1841 to +0.7465 | no |
| pods started | 0.2 | 1.9 | +850.0% | +0.0463 to +3.3537 | yes: power given |
| pod start wait, total (s) | 0.4 | 5.6 | +1300.0% | −0.3694 to +10.7694 | no |
| pod start wait, mean (s) | 0.4 | 1.633 | +308.3% | −0.2884 to +2.7551 | no |
| host CPU busy, the real machine under kind (%) | 48.61 | 61.62 | +26.8% | +11.7140 to +14.3138 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.2 | 993.6 | +21.1% | +126.6591 to +220.1409 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.304 | −22.5% | −4.7570 to −0.6354 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 10.47 | +9952.0% | −7.4224 to +28.1558 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 53.1 | +7485.7% | −39.2066 to +144.0066 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 280.1 | +114.2% | +110.0134 to +188.6866 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*