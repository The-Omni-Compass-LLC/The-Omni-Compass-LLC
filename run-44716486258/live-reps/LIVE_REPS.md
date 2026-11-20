# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.813 | 4.745 |
| node-hours | 2.519 | 2.516 | 2.015 | 1.99 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | 272.2 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.8 | 234.9 | 233.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 343.9 | 319.2 | 334.1 | 314.5 |
| response time (ms), 95th percentile | 1241 | 1328 | 1402 | 1468 |
| response time (ms), 99th percentile | 1684 | 1939 | 1927 | 2096 |
| time over the response line (% of samples) | 14.09 | 9.994 | 14.15 | 10.08 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 6.6 | 8.5 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 143.8 | 116.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 37.5 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 11.69 | 11.81 | 15.53 |
| utilisation (used / allocatable) | 0.06019 | 0.0602 | 0.07576 | 0.07831 |
| CPU used (cores), mean | 1.445 | 1.445 | 1.429 | 1.445 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07205 | 0.07125 |
| CPU used with Omni's own (cores), mean | 1.445 | 1.445 | 1.501 | 1.516 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 463 | 394.1 | 386.2 |
| HPA replicas, mean | 1.979 | 2.068 | 2.251 | 2.277 |
| pods started | 0.2 | 0.1 | 1.5 | 1.1 |
| pod start wait, total (s) | 0.5 | 0.2 | 3.2 | 1.8 |
| pod start wait, mean (s) | 0.5 | 0.2 | 1.8 | 0.7833 |
| host CPU busy, the real machine under kind (%) | 41.62 | 41.7 | 44.67 | 44.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 784.9 | 791.4 | 794.8 | 800.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.171 | 4.067 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1167 | 0.09583 | 0.2708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | 0.5 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 90.5 | 97.65 | 99.74 | 106.5 |
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
| worker nodes in service, mean | 6 | 4.745 | −20.9% | −2.1725 to −0.3372 | yes: GAIN |
| node-hours | 2.516 | 1.99 | −20.9% | −0.9133 to −0.1387 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 | +0.1% | −0.5902 to +0.8967 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 233.5 | −14.4% | −68.5553 to −10.0174 | yes: GAIN |
| response time (ms), mean | 319.2 | 314.5 | −1.5% | −31.8071 to +22.3724 | no |
| response time (ms), 95th percentile | 1328 | 1468 | +10.5% | +8.6108 to +270.5662 | yes: LOSS |
| response time (ms), 99th percentile | 1939 | 2096 | +8.1% | −1.3795 to +315.4259 | no |
| time over the response line (% of samples) | 9.994 | 10.08 | +0.9% | −0.4717 to +0.6486 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.8 | +3.0% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.8 | +116.800 (native is 0) | +42.3425 to +191.2575 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.69 | 15.53 | +32.9% | −2.3890 to +10.0790 | no |
| utilisation (used / allocatable) | 0.0602 | 0.07831 | +30.1% | +0.0043 to +0.0319 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.445 | +0.0% | −0.0308 to +0.0310 | no |
| Omni's own CPU (cores), mean | 0 | 0.07125 | +0.071 (native is 0) | +0.0636 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.516 | +4.9% | +0.0386 to +0.1040 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 386.2 | −16.6% | −132.7757 to −20.8279 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.068 | 2.277 | +10.1% | +0.0436 to +0.3732 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | +0.1740 to +1.8260 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | +0.0845 to +3.1155 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.7833 | +291.7% | −0.1032 to +1.2699 | no |
| host CPU busy, the real machine under kind (%) | 41.7 | 44.87 | +7.6% | +2.4852 to +3.8483 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 791.4 | 800.1 | +1.1% | −3.9665 to +21.3665 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.067 | −32.2% | −3.2042 to −0.6620 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.2708 | +132.1% | −0.1678 to +0.4761 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | +160.0% | −1.3273 to +2.9273 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.65 | 106.5 | +9.1% | −1.5911 to +19.3161 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.519 | 2.516 | −0.1% | −0.0100 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | −0.1% | −0.9687 to +0.4842 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.8 | −0.1% | −0.9687 to +0.4842 | no |
| response time (ms), mean | 343.9 | 319.2 | −7.2% | −43.7099 to −5.6908 | yes: GAIN |
| response time (ms), 95th percentile | 1241 | 1328 | +7.0% | −60.0332 to +234.6692 | no |
| response time (ms), 99th percentile | 1684 | 1939 | +15.2% | −53.3915 to +563.9131 | no |
| time over the response line (% of samples) | 14.09 | 9.994 | −29.1% | −7.0004 to −1.1862 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 6.6 | −18.5% | −3.1259 to +0.1259 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 11.69 | +19.8% | −0.0643 to +3.9343 | no |
| utilisation (used / allocatable) | 0.06019 | 0.0602 | +0.0% | −0.0008 to +0.0008 | no |
| CPU used (cores), mean | 1.445 | 1.445 | +0.0% | −0.0186 to +0.0191 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.445 | 1.445 | +0.0% | −0.0186 to +0.0191 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 463 | +0.3% | −6.1186 to +8.4981 | no |
| HPA replicas, mean | 1.979 | 2.068 | +4.5% | −0.0462 to +0.2243 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.5 | 0.2 | −60.0% | −1.2567 to +0.6567 | no |
| pod start wait, mean (s) | 0.5 | 0.2 | −60.0% | −1.2567 to +0.6567 | no |
| host CPU busy, the real machine under kind (%) | 41.62 | 41.7 | +0.2% | −0.4592 to +0.6166 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 791.4 | +0.8% | +0.6377 to +12.3623 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1167 | +75.0% | −0.0861 to +0.1861 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.5 | 97.65 | +7.9% | −0.3466 to +14.6633 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.813 | −19.8% | −2.0567 to −0.3176 | yes: GAIN |
| node-hours | 2.519 | 2.015 | −20.0% | −0.8674 to −0.1408 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.2 | −0.3% | −1.5943 to −0.0469 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 234.9 | −14.0% | −65.6235 to −10.6802 | yes: GAIN |
| response time (ms), mean | 343.9 | 334.1 | −2.8% | −32.4090 to +12.8659 | no |
| response time (ms), 95th percentile | 1241 | 1402 | +13.0% | +10.0046 to +312.7984 | yes: LOSS |
| response time (ms), 99th percentile | 1684 | 1927 | +14.4% | −40.8290 to +526.5230 | no |
| time over the response line (% of samples) | 14.09 | 14.15 | +0.5% | −0.2097 to +0.3366 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.5 | +4.9% | −0.5048 to +1.3048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.8 | +143.800 (native is 0) | +54.1965 to +233.4035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 11.81 | +21.1% | −0.4257 to +4.5357 | no |
| utilisation (used / allocatable) | 0.06019 | 0.07576 | +25.9% | +0.0036 to +0.0275 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.429 | −1.0% | −0.0407 to +0.0105 | no |
| Omni's own CPU (cores), mean | 0 | 0.07205 | +0.072 (native is 0) | +0.0652 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.501 | +3.9% | +0.0250 to +0.0888 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 394.1 | −14.7% | −116.4906 to −18.9422 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.251 | +13.7% | +0.0614 to +0.4822 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.1791 to +2.4209 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.2 | +540.0% | +0.3384 to +5.0616 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.8 | +260.0% | −0.1717 to +2.7717 | no |
| host CPU busy, the real machine under kind (%) | 41.62 | 44.67 | +7.3% | +2.3467 to +3.7566 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 794.8 | +1.3% | −0.5936 to +20.3936 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.171 | −30.5% | −3.0531 to −0.6041 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.09583 | +43.7% | −0.0926 to +0.1509 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.7263 to +0.5263 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.5 | 99.74 | +10.2% | −0.6397 to +19.1314 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.813 | −19.8% | −2.0567 to −0.3176 | yes: GAIN |
| node-hours | 2.516 | 2.015 | −19.9% | −0.8655 to −0.1357 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.2 | −0.2% | −1.5335 to +0.3768 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 234.9 | −13.9% | −65.4646 to −10.3547 | yes: GAIN |
| response time (ms), mean | 319.2 | 334.1 | +4.7% | −17.9666 to +47.8242 | no |
| response time (ms), 95th percentile | 1328 | 1402 | +5.6% | −31.7809 to +179.9479 | no |
| response time (ms), 99th percentile | 1939 | 1927 | −0.6% | −286.9275 to +262.0999 | no |
| time over the response line (% of samples) | 9.994 | 14.15 | +41.6% | +1.2834 to +7.0300 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 8.5 | +28.8% | −0.3481 to +4.1481 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.8 | +143.800 (native is 0) | +54.1965 to +233.4035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.69 | 11.81 | +1.0% | −3.1406 to +3.3806 | no |
| utilisation (used / allocatable) | 0.0602 | 0.07576 | +25.8% | +0.0031 to +0.0280 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.429 | −1.1% | −0.0337 to +0.0028 | no |
| Omni's own CPU (cores), mean | 0 | 0.07205 | +0.072 (native is 0) | +0.0652 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.501 | +3.9% | +0.0338 to +0.0795 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 394.1 | −14.9% | −121.4741 to −16.3381 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.068 | 2.251 | +8.8% | −0.0404 to +0.4058 | no |
| pods started | 0.1 | 1.5 | +1400.0% | +0.4344 to +2.3656 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.2 | +1500.0% | +1.1531 to +4.8469 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.8 | +800.0% | +0.9089 to +2.2911 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.7 | 44.67 | +7.1% | +2.5731 to +3.3729 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 791.4 | 794.8 | +0.4% | −4.2016 to +11.0016 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.171 | −30.5% | −3.0531 to −0.6041 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.09583 | −17.9% | −0.2211 to +0.1795 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.6744 to +0.6744 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.65 | 99.74 | +2.1% | −4.7406 to +8.9156 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.745 | −20.9% | −2.1725 to −0.3372 | yes: GAIN |
| node-hours | 2.519 | 1.99 | −21.0% | −0.9154 to −0.1437 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −1.0458 to +0.8679 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 233.5 | −14.5% | −68.7081 to −10.3490 | yes: GAIN |
| response time (ms), mean | 343.9 | 314.5 | −8.6% | −54.2307 to −4.6047 | yes: GAIN |
| response time (ms), 95th percentile | 1241 | 1468 | +18.3% | −41.8678 to +495.6808 | no |
| response time (ms), 99th percentile | 1684 | 2096 | +24.5% | −12.7097 to +837.2777 | no |
| time over the response line (% of samples) | 14.09 | 10.08 | −28.4% | −6.9677 to −1.0419 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 6.8 | −16.0% | −2.9189 to +0.3189 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.8 | +116.800 (native is 0) | +42.3425 to +191.2575 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 15.53 | +59.3% | −1.9127 to +13.4727 | no |
| utilisation (used / allocatable) | 0.06019 | 0.07831 | +30.1% | +0.0047 to +0.0315 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.445 | +0.0% | −0.0290 to +0.0297 | no |
| Omni's own CPU (cores), mean | 0 | 0.07125 | +0.071 (native is 0) | +0.0636 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.516 | +5.0% | +0.0379 to +0.1054 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 386.2 | −16.4% | −127.8103 to −23.4138 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.277 | +15.0% | +0.0882 to +0.5067 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.1128 to +1.6872 | yes: power given |
| pod start wait, total (s) | 0.5 | 1.8 | +260.0% | +0.0819 to +2.5181 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 0.7833 | +56.7% | −0.2617 to +0.8284 | no |
| host CPU busy, the real machine under kind (%) | 41.62 | 44.87 | +7.8% | +2.3650 to +4.1259 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 800.1 | +1.9% | −1.4216 to +31.8216 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.067 | −32.2% | −3.2042 to −0.6620 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.2708 | +306.2% | −0.2499 to +0.6582 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.3 | +116.7% | −1.4340 to +2.8340 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.5 | 106.5 | +17.7% | −1.0921 to +33.1338 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*