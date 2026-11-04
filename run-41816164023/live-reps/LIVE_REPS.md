# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.66 | 4.921 |
| node-hours | 2.513 | 2.513 | 1.951 | 2.061 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.3 | 273 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.3 | 231 | 238.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 412.5 | 414.7 | 426.6 | 426.1 |
| response time (ms), 95th percentile | 1511 | 1641 | 1574 | 1686 |
| response time (ms), 99th percentile | 2216 | 2284 | 2356 | 2368 |
| time over the response line (% of samples) | 17.68 | 16.05 | 18.28 | 16.88 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.7 | 9.1 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 26.5 | 29.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 13.33 | 45.14 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.68 | 21.28 | 20.4 | 25.64 |
| utilisation (used / allocatable) | 0.06293 | 0.06386 | 0.08061 | 0.07377 |
| CPU used (cores), mean | 1.51 | 1.533 | 1.485 | 1.464 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06128 | 0.06651 |
| CPU used with Omni's own (cores), mean | 1.51 | 1.533 | 1.547 | 1.53 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 438.2 | 375.3 | 400.3 |
| HPA replicas, mean | 2.121 | 2.109 | 2.386 | 2.438 |
| pods started | 0.2 | 0.2 | 1.4 | 1.1 |
| pod start wait, total (s) | 0.4 | 0.4 | 2.8 | 2.5 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.25 | 1.02 |
| host CPU busy, the real machine under kind (%) | 43.43 | 44.36 | 45.69 | 46.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 817.3 | 822.3 | 821.7 | 828.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.813 | 4.038 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2667 | 0.7542 | 0.4542 | 0.2333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 3 | 2.9 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 123.3 | 129.4 | 125.6 | 136.5 |
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
| worker nodes in service, mean | 6 | 4.921 | −18.0% | −1.7622 to −0.3950 | yes: GAIN |
| node-hours | 2.513 | 2.061 | −18.0% | −0.7413 to −0.1629 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.7 | −0.2% | −1.7815 to +0.4601 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 238.8 | −12.6% | −56.8003 to −12.3419 | yes: GAIN |
| response time (ms), mean | 414.7 | 426.1 | +2.7% | −7.7180 to +30.4706 | no |
| response time (ms), 95th percentile | 1641 | 1686 | +2.7% | −11.3832 to +101.0702 | no |
| response time (ms), 99th percentile | 2284 | 2368 | +3.7% | −48.9713 to +215.7877 | no |
| time over the response line (% of samples) | 16.05 | 16.88 | +5.1% | +0.0233 to +1.6251 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.7 | ±0.0% | −0.5840 to +0.5840 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.400 (native is 0) | +23.0628 to +35.7372 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.28 | 25.64 | +20.5% | +0.0786 to +8.6414 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06386 | 0.07377 | +15.5% | +0.0031 to +0.0168 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.533 | 1.464 | −4.5% | −0.1363 to −0.0010 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06651 | +0.067 (native is 0) | +0.0591 to +0.0740 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.53 | −0.1% | −0.0751 to +0.0708 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.2 | 400.3 | −8.6% | −67.8133 to −7.9527 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.109 | 2.438 | +15.6% | +0.0192 to +0.6390 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | −0.4254 to +2.2254 | no |
| pod start wait, total (s) | 0.4 | 2.5 | +525.0% | −1.0533 to +5.2533 | no |
| pod start wait, mean (s) | 0.2 | 1.02 | +410.0% | −0.3509 to +1.9909 | no |
| host CPU busy, the real machine under kind (%) | 44.36 | 46.58 | +5.0% | +1.6684 to +2.7712 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.3 | 828.9 | +0.8% | +0.5473 to +12.6527 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.038 | −32.7% | −3.1616 to −0.7625 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.2333 | −69.1% | −1.2447 to +0.2030 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 0.9 | −70.0% | −5.1245 to +0.9245 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.4 | 136.5 | +5.5% | +1.2899 to +13.0018 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.513 | 0.0% | raw −0.0099 to +0.0099 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.3 | +0.1% | −0.7196 to +1.2300 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.3 | +0.1% | −0.7196 to +1.2300 | no |
| response time (ms), mean | 412.5 | 414.7 | +0.5% | −15.9561 to +20.4348 | no |
| response time (ms), 95th percentile | 1511 | 1641 | +8.6% | +8.4949 to +252.2681 | yes: LOSS |
| response time (ms), 99th percentile | 2216 | 2284 | +3.1% | +10.3539 to +127.2785 | yes: LOSS |
| time over the response line (% of samples) | 17.68 | 16.05 | −9.2% | −3.0138 to −0.2474 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.7 | ±0.0% | −0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.68 | 21.28 | +13.9% | −1.1575 to +6.3542 | no |
| utilisation (used / allocatable) | 0.06293 | 0.06386 | +1.5% | −0.0003 to +0.0021 | no |
| CPU used (cores), mean | 1.51 | 1.533 | +1.5% | −0.0064 to +0.0507 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.51 | 1.533 | +1.5% | −0.0064 to +0.0507 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 438.2 | −1.6% | −17.4685 to +3.0333 | no |
| HPA replicas, mean | 2.121 | 2.109 | −0.6% | −0.2111 to +0.1864 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −1.3488 to +1.3488 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43.43 | 44.36 | +2.1% | +0.5799 to +1.2808 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.3 | 822.3 | +0.6% | −1.6163 to +11.6163 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2667 | 0.7542 | +182.8% | −0.0278 to +1.0028 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 3 | +87.5% | −0.6566 to +3.4566 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.3 | 129.4 | +4.9% | −1.4266 to +13.5100 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.66 | −22.3% | −2.1631 to −0.5170 | yes: GAIN |
| node-hours | 2.513 | 1.951 | −22.3% | −0.9090 to −0.2143 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | −0.0% | −0.9623 to +0.8394 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 231 | −15.4% | −68.3902 to −15.8035 | yes: GAIN |
| response time (ms), mean | 412.5 | 426.6 | +3.4% | −2.7049 to +30.9820 | no |
| response time (ms), 95th percentile | 1511 | 1574 | +4.2% | −74.3134 to +200.7124 | no |
| response time (ms), 99th percentile | 2216 | 2356 | +6.3% | +5.8621 to +275.4057 | yes: LOSS |
| time over the response line (% of samples) | 17.68 | 18.28 | +3.4% | −0.1349 to +1.3313 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.1 | +4.6% | −0.6228 to +1.4228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +19.4732 to +33.5268 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.68 | 20.4 | +9.2% | −2.2222 to +5.6655 | no |
| utilisation (used / allocatable) | 0.06293 | 0.08061 | +28.1% | +0.0066 to +0.0287 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.51 | 1.485 | −1.7% | −0.0538 to +0.0039 | no |
| Omni's own CPU (cores), mean | 0 | 0.06128 | +0.061 (native is 0) | +0.0539 to +0.0686 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.51 | 1.547 | +2.4% | +0.0010 to +0.0716 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 375.3 | −15.7% | −115.4836 to −24.6796 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.121 | 2.386 | +12.5% | +0.0907 to +0.4393 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | −0.0064 to +2.4064 | no |
| pod start wait, total (s) | 0.4 | 2.8 | +600.0% | −0.0128 to +4.8128 | no |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | −0.0282 to +2.1282 | no |
| host CPU busy, the real machine under kind (%) | 43.43 | 45.69 | +5.2% | +1.7786 to +2.7331 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.3 | 821.7 | +0.5% | −2.3119 to +11.1119 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.813 | −36.4% | −3.3075 to −1.0664 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2667 | 0.4542 | +70.3% | −0.0843 to +0.4593 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.9 | +81.3% | −0.5174 to +3.1174 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.3 | 125.6 | +1.8% | −4.9558 to +9.4392 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.66 | −22.3% | −2.1631 to −0.5170 | yes: GAIN |
| node-hours | 2.513 | 1.951 | −22.3% | −0.9121 to −0.2112 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | −0.1% | −1.3587 to +0.7253 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 231 | −15.5% | −69.0665 to −15.6377 | yes: GAIN |
| response time (ms), mean | 414.7 | 426.6 | +2.9% | −1.6575 to +25.4559 | no |
| response time (ms), 95th percentile | 1641 | 1574 | −4.1% | −222.1457 to +87.7817 | no |
| response time (ms), 99th percentile | 2284 | 2356 | +3.1% | −43.1369 to +186.7723 | no |
| time over the response line (% of samples) | 16.05 | 18.28 | +13.9% | +0.7339 to +3.7237 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.1 | +4.6% | −0.4396 to +1.2396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +19.4732 to +33.5268 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.28 | 20.4 | −4.1% | −4.5939 to +2.8406 | no |
| utilisation (used / allocatable) | 0.06386 | 0.08061 | +26.2% | +0.0060 to +0.0275 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.533 | 1.485 | −3.1% | −0.0887 to −0.0055 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06128 | +0.061 (native is 0) | +0.0539 to +0.0686 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.547 | +0.9% | −0.0335 to +0.0618 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.2 | 375.3 | −14.3% | −103.5911 to −22.1368 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.109 | 2.386 | +13.2% | +0.0359 to +0.5187 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.8 | +600.0% | +0.5165 to +4.2835 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | +0.1649 to +1.9351 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.36 | 45.69 | +3.0% | +0.7276 to +1.9233 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.3 | 821.7 | −0.1% | −4.0421 to +2.8421 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.813 | −36.4% | −3.3075 to −1.0664 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.4542 | −39.8% | −0.8427 to +0.2427 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 2.9 | −3.3% | −3.3422 to +3.1422 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.4 | 125.6 | −2.9% | −10.9813 to +3.3813 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.921 | −18.0% | −1.7622 to −0.3950 | yes: GAIN |
| node-hours | 2.513 | 2.061 | −18.0% | −0.7373 to −0.1670 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.7 | −0.1% | −1.1792 to +0.3683 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 238.8 | −12.6% | −56.0780 to −12.5538 | yes: GAIN |
| response time (ms), mean | 412.5 | 426.1 | +3.3% | +3.4047 to +23.8267 | yes: LOSS |
| response time (ms), 95th percentile | 1511 | 1686 | +11.6% | +28.3777 to +322.0723 | yes: LOSS |
| response time (ms), 99th percentile | 2216 | 2368 | +6.9% | +2.0489 to +302.3999 | yes: LOSS |
| time over the response line (% of samples) | 17.68 | 16.88 | −4.6% | −1.7594 to +0.1466 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.7 | ±0.0% | −0.7540 to +0.7540 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.400 (native is 0) | +23.0628 to +35.7372 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.68 | 25.64 | +37.3% | +0.5628 to +13.3539 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06293 | 0.07377 | +17.2% | +0.0039 to +0.0177 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.51 | 1.464 | −3.1% | −0.1094 to +0.0164 | no |
| Omni's own CPU (cores), mean | 0 | 0.06651 | +0.067 (native is 0) | +0.0591 to +0.0740 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.51 | 1.53 | +1.3% | −0.0481 to +0.0881 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 400.3 | −10.1% | −76.0923 to −14.1089 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.121 | 2.438 | +14.9% | +0.0713 to +0.5622 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | −0.2410 to +2.0410 | no |
| pod start wait, total (s) | 0.4 | 2.5 | +525.0% | −0.4109 to +4.6109 | no |
| pod start wait, mean (s) | 0.2 | 1.02 | +410.0% | +0.1407 to +1.4993 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.43 | 46.58 | +7.3% | +2.6528 to +3.6475 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.3 | 828.9 | +1.4% | +2.6264 to +20.5736 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.038 | −32.7% | −3.1616 to −0.7625 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2667 | 0.2333 | −12.5% | −0.2509 to +0.1842 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.9 | −43.7% | −2.9633 to +1.5633 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.3 | 136.5 | +10.7% | +2.6071 to +23.7679 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*