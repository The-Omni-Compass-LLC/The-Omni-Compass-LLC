# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.487 | 5.996 |
| node-hours | 2.514 | 2.518 | 2.297 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 272.8 | 274.2 | 272.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 272.8 | 258.1 | 272.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 497.7 | 149.9 | 461.4 | 112.6 |
| response time (ms), 95th percentile | 1901 | 261.8 | 1991 | 253 |
| response time (ms), 99th percentile | 2710 | 383.3 | 2760 | 384.9 |
| time over the response line (% of samples) | 25.82 | 0.2942 | 24.88 | 0.3238 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 0 | 12.4 | 0.3333 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 24.5 | 13.11 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.53 | 1344 | 11.56 | 1339 |
| utilisation (used / allocatable) | 0.06593 | 0.06027 | 0.07158 | 0.06052 |
| CPU used (cores), mean | 1.582 | 1.446 | 1.564 | 1.452 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.017 | 0.013 |
| CPU used with Omni's own (cores), mean | 1.582 | 1.446 | 1.581 | 1.465 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.1 | 450.3 | 396 | 447.8 |
| HPA replicas, mean | 2.021 | 2.011 | 2.086 | 2.064 |
| pods started | 0.2 | 0 | 0.4 | 0.1111 |
| pod start wait, total (s) | 0.6 | 0 | 0.5 | 0.2222 |
| pod start wait, mean (s) | 0.6 | 0 | 0.5 | 0.2222 |
| host CPU busy, the real machine under kind (%) | 45.06 | 45.85 | 45.91 | 46.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 818 | 1481 | 822.7 | 1480 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.095 | 5.812 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 163.2 | 0.0625 | 170.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 759.8 | 0.4 | 818.9 |
| queue: job turnaround, submitted to done, mean (s) | 125.3 | 931.7 | 128.7 | 929.9 |
| queue: jobs unfinished at the window's end | 0 | 15.5 | 0 | 14.78 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0117 to +0.0046 | no |
| node-hours | 2.517 | 2.513 | −0.2% | −0.0131 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.5 | −0.0% | −0.9194 to +0.6913 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | −0.1% | −1.0141 to +0.5639 | no |
| response time (ms), mean | 149.1 | 112.6 | −24.4% | −44.1126 to −28.7283 | yes: GAIN |
| response time (ms), 95th percentile | 260 | 253 | −2.7% | −22.9451 to +8.8007 | no |
| response time (ms), 99th percentile | 383.2 | 384.9 | +0.4% | −27.8174 to +31.2383 | no |
| time over the response line (% of samples) | 0.3097 | 0.3238 | +4.5% | −0.1360 to +0.1641 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3333 | +0.333 (native is 0) | −0.0510 to +0.7177 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.11 | +13.111 (native is 0) | +10.2753 to +15.9470 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1327 | 1339 | +0.9% | −33.1814 to +56.7592 | no |
| utilisation (used / allocatable) | 0.05996 | 0.06052 | +0.9% | −0.0011 to +0.0022 | no |
| CPU used (cores), mean | 1.439 | 1.452 | +0.9% | −0.0261 to +0.0513 | no |
| Omni's own CPU (cores), mean | 0 | 0.013 | +0.013 (native is 0) | +0.0117 to +0.0143 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.465 | +1.8% | −0.0124 to +0.0636 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.4 | 447.8 | −1.0% | −16.7949 to +7.6568 | no |
| HPA replicas, mean | 2.015 | 2.064 | +2.4% | −0.0811 to +0.1793 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.2222 | +0.222 (native is 0) | −0.2902 to +0.7347 | no |
| pod start wait, mean (s) | 0 | 0.2222 | +0.222 (native is 0) | −0.2902 to +0.7347 | no |
| host CPU busy, the real machine under kind (%) | 45.68 | 46.11 | +0.9% | −0.7114 to +1.5661 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1477 | 1480 | +0.2% | −5.7730 to +12.2174 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.812 | −3.1% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.1 | 170.4 | +5.1% | −28.4827 to +45.1124 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 749.7 | 818.9 | +9.2% | −101.5061 to +239.9505 | no |
| queue: job turnaround, submitted to done, mean (s) | 926.1 | 929.9 | +0.4% | −25.8525 to +33.4728 | no |
| queue: jobs unfinished at the window's end | 15.44 | 14.78 | −4.3% | −1.9414 to +0.6080 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.518 | +0.2% | −0.0089 to +0.0172 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 272.8 | −0.7% | −3.9403 to +0.3036 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 272.8 | −0.7% | −3.9403 to +0.3036 | no |
| response time (ms), mean | 497.7 | 149.9 | −69.9% | −466.7989 to −228.8351 | yes: GAIN |
| response time (ms), 95th percentile | 1901 | 261.8 | −86.2% | −2209.6477 to −1067.9433 | yes: GAIN |
| response time (ms), 99th percentile | 2710 | 383.3 | −85.9% | −3159.1016 to −1493.8958 | yes: GAIN |
| time over the response line (% of samples) | 25.82 | 0.2942 | −98.9% | −34.7800 to −16.2707 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 0 | −100.0% | −15.4252 to −7.9748 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.53 | 1344 | +10632.5% | +1116.1650 to +1547.2750 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06593 | 0.06027 | −8.6% | −0.0101 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.582 | 1.446 | −8.6% | −0.2425 to −0.0295 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.582 | 1.446 | −8.6% | −0.2425 to −0.0295 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.1 | 450.3 | +7.2% | −0.3635 to +60.6986 | no |
| HPA replicas, mean | 2.021 | 2.011 | −0.5% | −0.1071 to +0.0869 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.6 | 0 | −100.0% | −1.5048 to +0.3048 | no |
| pod start wait, mean (s) | 0.6 | 0 | −100.0% | −1.5048 to +0.3048 | no |
| host CPU busy, the real machine under kind (%) | 45.06 | 45.85 | +1.8% | −1.6510 to +3.2388 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818 | 1481 | +81.0% | +608.8115 to +716.3885 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 163.2 | +301253.8% | +127.0598 to +199.2985 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 759.8 | +189850.0% | +584.4762 to +934.3238 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 125.3 | 931.7 | +643.8% | +715.7735 to +897.0682 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.5 | +15.500 (native is 0) | +10.7402 to +20.2598 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.487 | −8.5% | −1.1249 to +0.0999 | no |
| node-hours | 2.514 | 2.297 | −8.6% | −0.4732 to +0.0399 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.2 | −0.2% | −1.2253 to +0.3875 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 258.1 | −6.0% | −36.1040 to +2.9953 | no |
| response time (ms), mean | 497.7 | 461.4 | −7.3% | −49.8475 to −22.7086 | yes: GAIN |
| response time (ms), 95th percentile | 1901 | 1991 | +4.7% | +10.6564 to +169.3046 | yes: LOSS |
| response time (ms), 99th percentile | 2710 | 2760 | +1.9% | −109.9867 to +211.3101 | no |
| time over the response line (% of samples) | 25.82 | 24.88 | −3.6% | −1.7977 to −0.0750 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.4 | +6.0% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.5 | +24.500 (native is 0) | +10.5144 to +38.4856 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.53 | 11.56 | −7.7% | −2.4671 to +0.5371 | no |
| utilisation (used / allocatable) | 0.06593 | 0.07158 | +8.6% | −0.0013 to +0.0126 | no |
| CPU used (cores), mean | 1.582 | 1.564 | −1.2% | −0.0480 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.0156 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.582 | 1.581 | −0.1% | −0.0318 to +0.0290 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.1 | 396 | −5.7% | −54.2891 to +6.1029 | no |
| HPA replicas, mean | 2.021 | 2.086 | +3.2% | −0.0706 to +0.1996 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.6 | 0.5 | −16.7% | −1.1366 to +0.9366 | no |
| pod start wait, mean (s) | 0.6 | 0.5 | −16.7% | −1.1366 to +0.9366 | no |
| host CPU busy, the real machine under kind (%) | 45.06 | 45.91 | +1.9% | +0.4258 to +1.2825 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818 | 822.7 | +0.6% | +1.4648 to +7.9352 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.095 | −15.1% | −1.8245 to +0.0153 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0625 | +15.4% | −0.0224 to +0.0391 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.3 | 128.7 | +2.8% | +0.3087 to +6.6163 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.487 | −8.5% | −1.1249 to +0.0999 | no |
| node-hours | 2.518 | 2.297 | −8.8% | −0.4759 to +0.0343 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 274.2 | +0.5% | −0.4263 to +3.2251 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 258.1 | −5.4% | −35.2379 to +5.7659 | no |
| response time (ms), mean | 149.9 | 461.4 | +207.8% | +196.7301 to +426.3477 | yes: LOSS |
| response time (ms), 95th percentile | 261.8 | 1991 | +660.3% | +1139.0291 to +2318.5229 | yes: LOSS |
| response time (ms), 99th percentile | 383.3 | 2760 | +620.2% | +1564.3352 to +3189.9856 | yes: LOSS |
| time over the response line (% of samples) | 0.2942 | 24.88 | +8359.1% | +16.0416 to +33.1364 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.4 | +12.400 (native is 0) | +9.1798 to +15.6202 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.5 | +24.500 (native is 0) | +10.5144 to +38.4856 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1344 | 11.56 | −99.1% | −1548.9983 to −1116.3717 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06027 | 0.07158 | +18.8% | +0.0067 to +0.0159 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.564 | +8.1% | −0.0098 to +0.2449 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.0156 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.581 | +9.3% | +0.0061 to +0.2629 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.3 | 396 | −12.1% | −72.1495 to −36.3718 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.086 | +3.7% | −0.0600 to +0.2091 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 45.85 | 45.91 | +0.1% | −2.5832 to +2.7036 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1481 | 822.7 | −44.4% | −711.7004 to −604.0996 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 163.2 | 0.0625 | −100.0% | −199.3085 to −127.0331 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 759.8 | 0.4 | −99.9% | −934.4424 to −584.3576 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 931.7 | 128.7 | −86.2% | −892.3940 to −713.5226 | yes: GAIN |
| queue: jobs unfinished at the window's end | 15.5 | 0 | −100.0% | −20.2598 to −10.7402 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0117 to +0.0046 | no |
| node-hours | 2.515 | 2.513 | −0.1% | −0.0173 to +0.0140 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 272.5 | −0.8% | −3.9523 to −0.2759 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 272.4 | −0.8% | −3.9918 to −0.4587 | yes: GAIN |
| response time (ms), mean | 491.7 | 112.6 | −77.1% | −518.4243 to −239.6359 | yes: GAIN |
| response time (ms), 95th percentile | 1872 | 253 | −86.5% | −2264.1462 to −974.5638 | yes: GAIN |
| response time (ms), 99th percentile | 2689 | 384.9 | −85.7% | −3245.9864 to −1361.1629 | yes: GAIN |
| time over the response line (% of samples) | 25.22 | 0.3238 | −98.7% | −35.3301 to −14.4572 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.44 | 0.3333 | −97.1% | −15.1866 to −7.0356 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.11 | +13.111 (native is 0) | +10.2753 to +15.9470 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.1 | 1339 | +10966.8% | +1095.9258 to +1557.2298 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06564 | 0.06052 | −7.8% | −0.0110 to +0.0008 | no |
| CPU used (cores), mean | 1.575 | 1.452 | −7.9% | −0.2644 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0 | 0.013 | +0.013 (native is 0) | +0.0117 to +0.0143 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.575 | 1.465 | −7.0% | −0.2503 to +0.0288 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.4 | 447.8 | +6.0% | −16.5626 to +67.5035 | no |
| HPA replicas, mean | 2.004 | 2.064 | +3.0% | −0.0819 to +0.2032 | no |
| pods started | 0.2222 | 0.1111 | −50.0% | −0.5730 to +0.3508 | no |
| pod start wait, total (s) | 0.6667 | 0.2222 | −66.7% | −1.6665 to +0.7777 | no |
| pod start wait, mean (s) | 0.6667 | 0.2222 | −66.7% | −1.6665 to +0.7777 | no |
| host CPU busy, the real machine under kind (%) | 44.84 | 46.11 | +2.8% | −1.6255 to +4.1556 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.4 | 1480 | +81.3% | +610.5077 to +716.8257 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.812 | −3.1% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 170.4 | +408855.6% | +121.8655 to +218.8475 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 818.9 | +245566.7% | +610.6461 to +1026.4650 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124 | 929.9 | +649.8% | +700.9409 to +910.7721 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.78 | +14.778 (native is 0) | +9.7700 to +19.7856 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*