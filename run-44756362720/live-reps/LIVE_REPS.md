# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.127 | 5.06 |
| node-hours | 2.516 | 2.514 | 2.149 | 2.122 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.7 | 273.8 | 274.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 273.7 | 246.3 | 244.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 417.3 | 366.3 | 402.2 | 347.2 |
| response time (ms), 95th percentile | 1543 | 1426 | 1682 | 1641 |
| response time (ms), 99th percentile | 2117 | 2263 | 2344 | 2356 |
| time over the response line (% of samples) | 17.71 | 13.71 | 17.53 | 13.32 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7.9 | 9.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 106.7 | 82.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 42.5 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 19.95 | 14.18 | 23.33 |
| utilisation (used / allocatable) | 0.06365 | 0.06394 | 0.07459 | 0.07597 |
| CPU used (cores), mean | 1.528 | 1.534 | 1.517 | 1.532 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07556 | 0.07875 |
| CPU used with Omni's own (cores), mean | 1.528 | 1.534 | 1.593 | 1.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 436.4 | 391.3 | 383.8 |
| HPA replicas, mean | 2.011 | 2.031 | 2.335 | 2.115 |
| pods started | 0.1 | 0.1 | 1.5 | 0.5 |
| pod start wait, total (s) | 0.3 | 0.4 | 2.7 | 1.3 |
| pod start wait, mean (s) | 0.3 | 0.4 | 1.067 | 0.55 |
| host CPU busy, the real machine under kind (%) | 43.69 | 44.74 | 46.88 | 48.08 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 810.1 | 824.1 | 819.7 | 836.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.619 | 4.321 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.083 | 0.4625 | 1.017 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4.1 | 1.4 | 3.3 |
| queue: job turnaround, submitted to done, mean (s) | 114.6 | 135.3 | 123.4 | 146.2 |
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
| worker nodes in service, mean | 6 | 5.06 | −15.7% | −1.6622 to −0.2180 | yes: GAIN |
| node-hours | 2.514 | 2.122 | −15.6% | −0.6969 to −0.0866 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.2 | +0.2% | −0.6125 to +1.5100 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 244.6 | −10.6% | −52.3072 to −5.9036 | yes: GAIN |
| response time (ms), mean | 366.3 | 347.2 | −5.2% | −38.2952 to +0.1552 | no |
| response time (ms), 95th percentile | 1426 | 1641 | +15.0% | +45.9641 to +383.3429 | yes: LOSS |
| response time (ms), 99th percentile | 2263 | 2356 | +4.1% | −0.2757 to +186.1007 | no |
| time over the response line (% of samples) | 13.71 | 13.32 | −2.8% | −1.3480 to +0.5733 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.3 | +5.1% | −0.3689 to +1.1689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.5 | +82.500 (native is 0) | +27.9391 to +137.0609 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.95 | 23.33 | +17.0% | −0.1979 to +6.9612 | no |
| utilisation (used / allocatable) | 0.06394 | 0.07597 | +18.8% | +0.0034 to +0.0207 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.534 | 1.532 | −0.2% | −0.0341 to +0.0288 | no |
| Omni's own CPU (cores), mean | 0 | 0.07875 | +0.079 (native is 0) | +0.0730 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.534 | 1.611 | +5.0% | +0.0417 to +0.1105 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.4 | 383.8 | −12.0% | −90.1105 to −14.9147 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.031 | 2.115 | +4.1% | −0.0771 to +0.2451 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.4396 to +1.2396 | no |
| pod start wait, total (s) | 0.4 | 1.3 | +225.0% | −1.3982 to +3.1982 | no |
| pod start wait, mean (s) | 0.4 | 0.55 | +37.5% | −1.1993 to +1.4993 | no |
| host CPU busy, the real machine under kind (%) | 44.74 | 48.08 | +7.5% | +2.9895 to +3.6829 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.1 | 836.2 | +1.5% | +3.7551 to +20.4449 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.321 | −28.0% | −2.9046 to −0.4532 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.083 | 1.017 | −6.2% | −0.2483 to +0.1150 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.1 | 3.3 | −19.5% | −3.4293 to +1.8293 | no |
| queue: job turnaround, submitted to done, mean (s) | 135.3 | 146.2 | +8.1% | +2.1772 to +19.6811 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0124 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.7 | −0.1% | −1.4016 to +1.0359 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 273.7 | −0.1% | −1.4016 to +1.0359 | no |
| response time (ms), mean | 417.3 | 366.3 | −12.2% | −86.6154 to −15.4383 | yes: GAIN |
| response time (ms), 95th percentile | 1543 | 1426 | −7.6% | −233.6630 to +0.4540 | no |
| response time (ms), 99th percentile | 2117 | 2263 | +6.9% | −97.9147 to +391.5333 | no |
| time over the response line (% of samples) | 17.71 | 13.71 | −22.6% | −6.2399 to −1.7496 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7.9 | −18.6% | −4.2034 to +0.6034 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 19.95 | +62.9% | +3.6770 to +11.7230 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06365 | 0.06394 | +0.4% | −0.0005 to +0.0011 | no |
| CPU used (cores), mean | 1.528 | 1.534 | +0.4% | −0.0126 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.528 | 1.534 | +0.4% | −0.0126 to +0.0261 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 436.4 | −0.3% | −8.8110 to +5.9293 | no |
| HPA replicas, mean | 2.011 | 2.031 | +1.0% | −0.0765 to +0.1156 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −1.0898 to +1.2898 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −1.0898 to +1.2898 | no |
| host CPU busy, the real machine under kind (%) | 43.69 | 44.74 | +2.4% | +0.6957 to +1.4170 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 824.1 | +1.7% | +4.3677 to +23.6323 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.083 | +983.3% | +0.5475 to +1.4192 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4.1 | +412.5% | −0.9392 to +7.5392 | no |
| queue: job turnaround, submitted to done, mean (s) | 114.6 | 135.3 | +18.1% | +6.1587 to +35.2330 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.127 | −14.5% | −1.5915 to −0.1545 | yes: GAIN |
| node-hours | 2.516 | 2.149 | −14.6% | −0.6690 to −0.0653 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.8 | −0.0% | −1.2756 to +1.0782 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 246.3 | −10.1% | −50.4863 to −4.6361 | yes: GAIN |
| response time (ms), mean | 417.3 | 402.2 | −3.6% | −24.7445 to −5.6361 | yes: GAIN |
| response time (ms), 95th percentile | 1543 | 1682 | +9.0% | +26.8015 to +250.8485 | yes: LOSS |
| response time (ms), 99th percentile | 2117 | 2344 | +10.8% | +58.9994 to +396.6358 | yes: LOSS |
| time over the response line (% of samples) | 17.71 | 17.53 | −1.0% | −0.7428 to +0.3895 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | −1.2254 to +1.4254 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.7 | +106.700 (native is 0) | +24.0979 to +189.3021 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 14.18 | +15.7% | −1.0216 to +4.8749 | no |
| utilisation (used / allocatable) | 0.06365 | 0.07459 | +17.2% | +0.0015 to +0.0204 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.528 | 1.517 | −0.7% | −0.0426 to +0.0215 | no |
| Omni's own CPU (cores), mean | 0 | 0.07556 | +0.076 (native is 0) | +0.0702 to +0.0810 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.528 | 1.593 | +4.3% | +0.0309 to +0.0991 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 391.3 | −10.6% | −83.5358 to −9.4510 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.335 | +16.1% | +0.0891 to +0.5581 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.3772 to +2.4228 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.7 | +800.0% | +0.1080 to +4.6920 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.067 | +255.6% | −0.2515 to +1.7848 | no |
| host CPU busy, the real machine under kind (%) | 43.69 | 46.88 | +7.3% | +2.7872 to +3.5914 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 819.7 | +1.2% | +2.2262 to +16.9738 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.619 | −23.0% | −2.4316 to −0.3306 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.4625 | +362.5% | −0.2949 to +1.0199 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.4 | +75.0% | −0.4228 to +1.6228 | no |
| queue: job turnaround, submitted to done, mean (s) | 114.6 | 123.4 | +7.7% | +2.4516 to +15.1568 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.127 | −14.5% | −1.5915 to −0.1545 | yes: GAIN |
| node-hours | 2.514 | 2.149 | −14.5% | −0.6659 to −0.0635 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.8 | +0.0% | −0.9486 to +1.1170 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 246.3 | −10.0% | −50.3005 to −4.4561 | yes: GAIN |
| response time (ms), mean | 366.3 | 402.2 | +9.8% | −3.4491 to +75.1222 | no |
| response time (ms), 95th percentile | 1426 | 1682 | +17.9% | +125.7384 to +385.1206 | yes: LOSS |
| response time (ms), 99th percentile | 2263 | 2344 | +3.6% | −34.8186 to +196.8352 | no |
| time over the response line (% of samples) | 13.71 | 17.53 | +27.8% | +1.9359 to +5.7002 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 9.8 | +24.1% | +0.1989 to +3.6011 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.7 | +106.700 (native is 0) | +24.0979 to +189.3021 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.95 | 14.18 | −28.9% | −7.7054 to −3.8412 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06394 | 0.07459 | +16.7% | +0.0013 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.534 | 1.517 | −1.1% | −0.0516 to +0.0170 | no |
| Omni's own CPU (cores), mean | 0 | 0.07556 | +0.076 (native is 0) | +0.0702 to +0.0810 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.534 | 1.593 | +3.8% | +0.0203 to +0.0962 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.4 | 391.3 | −10.3% | −81.8509 to −8.2542 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.031 | 2.335 | +15.0% | +0.0888 to +0.5193 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.4344 to +2.3656 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.7 | +575.0% | +0.0118 to +4.5882 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.067 | +166.7% | −0.5175 to +1.8509 | no |
| host CPU busy, the real machine under kind (%) | 44.74 | 46.88 | +4.8% | +1.8839 to +2.3820 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.1 | 819.7 | −0.5% | −7.1642 to −1.6358 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.619 | −23.0% | −2.4316 to −0.3306 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.083 | 0.4625 | −57.3% | −1.3241 to +0.0824 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.1 | 1.4 | −65.9% | −6.6186 to +1.2186 | no |
| queue: job turnaround, submitted to done, mean (s) | 135.3 | 123.4 | −8.8% | −20.3670 to −3.4163 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.06 | −15.7% | −1.6622 to −0.2180 | yes: GAIN |
| node-hours | 2.516 | 2.122 | −15.7% | −0.6995 to −0.0889 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.2 | +0.1% | −0.6269 to +1.1587 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 244.6 | −10.7% | −52.4759 to −6.1007 | yes: GAIN |
| response time (ms), mean | 417.3 | 347.2 | −16.8% | −95.7139 to −44.4799 | yes: GAIN |
| response time (ms), 95th percentile | 1543 | 1641 | +6.4% | −86.8543 to +282.9523 | no |
| response time (ms), 99th percentile | 2117 | 2356 | +11.3% | −43.9393 to +523.3829 | no |
| time over the response line (% of samples) | 17.71 | 13.32 | −24.7% | −7.0362 to −1.7280 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 8.3 | −14.4% | −3.5644 to +0.7644 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.5 | +82.500 (native is 0) | +27.9391 to +137.0609 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 23.33 | +90.5% | +4.1725 to +17.9908 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06365 | 0.07597 | +19.3% | +0.0037 to +0.0209 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.528 | 1.532 | +0.3% | −0.0314 to +0.0396 | no |
| Omni's own CPU (cores), mean | 0 | 0.07875 | +0.079 (native is 0) | +0.0730 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.528 | 1.611 | +5.4% | +0.0454 to +0.1203 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 383.8 | −12.3% | −91.1234 to −16.7834 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.115 | +5.1% | −0.0743 to +0.2814 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.4396 to +1.2396 | no |
| pod start wait, total (s) | 0.3 | 1.3 | +333.3% | −1.1853 to +3.1853 | no |
| pod start wait, mean (s) | 0.3 | 0.55 | +83.3% | −0.9332 to +1.4332 | no |
| host CPU busy, the real machine under kind (%) | 43.69 | 48.08 | +10.1% | +3.7218 to +5.0633 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 836.2 | +3.2% | +8.5027 to +43.6973 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.321 | −28.0% | −2.9046 to −0.4532 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.017 | +916.7% | +0.6170 to +1.2164 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 3.3 | +312.5% | +0.6454 to +4.3546 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 114.6 | 146.2 | +27.6% | +10.0085 to +53.2415 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*