# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.517 | 1.51 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 160.3 | 158.6 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 160.3 | 158.6 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 142.4 | 147.3 | 141.8 | 148.3 |
| response time (ms), 95th percentile | 295.1 | 289.9 | 284.3 | 295.9 |
| response time (ms), 99th percentile | 430.5 | 401.6 | 394.9 | 408.2 |
| time over the response line (% of samples) | 0.4733 | 0.2188 | 0.216 | 0.3334 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.8 | 6.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.24 | 0.4 | 0.33 |
| utilisation (used / allocatable) | 0.03816 | 0.04252 | 0.03835 | 0.04339 |
| CPU used (cores), mean | 0.9158 | 1.021 | 0.9203 | 1.041 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03155 | 0.05053 |
| CPU used with Omni's own (cores), mean | 0.9158 | 1.021 | 0.9519 | 1.092 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 688.5 | 621.8 | 685.7 | 610.9 |
| HPA replicas, mean | 8.957 | 8.946 | 10.1 | 10.31 |
| pods started | 4.3 | 4.6 | 7.4 | 8 |
| pod start wait, total (s) | 6.3 | 7.3 | 11.4 | 12.6 |
| pod start wait, mean (s) | 1.477 | 1.588 | 1.527 | 1.524 |
| host CPU busy, the real machine under kind (%) | 27.54 | 31.48 | 28.84 | 33.89 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.511 | −0.4% | −0.0152 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 159.8 | −0.3% | −1.5141 to +0.5788 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 159.8 | −0.3% | −1.5141 to +0.5788 | no |
| response time (ms), mean | 147.3 | 148.3 | +0.7% | −1.7572 to +3.6743 | no |
| response time (ms), 95th percentile | 289.9 | 295.9 | +2.1% | −8.9137 to +20.9227 | no |
| response time (ms), 99th percentile | 401.6 | 408.2 | +1.6% | −12.1525 to +25.3453 | no |
| time over the response line (% of samples) | 0.2188 | 0.3334 | +52.4% | −0.0935 to +0.3226 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +4.8845 to +7.9155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.24 | 0.33 | +37.5% | −0.3016 to +0.4816 | no |
| utilisation (used / allocatable) | 0.04252 | 0.04339 | +2.1% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.021 | 1.041 | +2.1% | +0.0026 to +0.0392 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05053 | +0.051 (native is 0) | +0.0460 to +0.0551 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.021 | 1.092 | +7.0% | +0.0494 to +0.0936 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 621.8 | 610.9 | −1.8% | −21.3255 to −0.5068 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.946 | 10.31 | +15.2% | +0.6015 to +2.1175 | yes: power given |
| pods started | 4.6 | 8 | +73.9% | +1.9225 to +4.8775 | yes: power given |
| pod start wait, total (s) | 7.3 | 12.6 | +72.6% | +1.7949 to +8.8051 | yes: LOSS |
| pod start wait, mean (s) | 1.588 | 1.524 | −4.0% | −0.4641 to +0.3362 | no |
| host CPU busy, the real machine under kind (%) | 31.48 | 33.89 | +7.7% | +1.7881 to +3.0313 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.517 | +0.2% | −0.0062 to +0.0136 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 160.3 | +0.9% | +0.3074 to +2.4961 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 160.3 | +0.9% | +0.3074 to +2.4961 | yes: power given |
| response time (ms), mean | 142.4 | 147.3 | +3.5% | +1.7215 to +8.2060 | yes: LOSS |
| response time (ms), 95th percentile | 295.1 | 289.9 | −1.8% | −17.3269 to +6.9829 | no |
| response time (ms), 99th percentile | 430.5 | 401.6 | −6.7% | −54.4913 to −3.3711 | yes: GAIN |
| time over the response line (% of samples) | 0.4733 | 0.2188 | −53.8% | −0.4371 to −0.0720 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.24 | −45.0% | −0.5879 to +0.1946 | no |
| utilisation (used / allocatable) | 0.03816 | 0.04252 | +11.4% | +0.0035 to +0.0052 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9158 | 1.021 | +11.4% | +0.0840 to +0.1254 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9158 | 1.021 | +11.4% | +0.0840 to +0.1254 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 688.5 | 621.8 | −9.7% | −79.4283 to −53.9397 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.957 | 8.946 | −0.1% | −0.1400 to +0.1175 | no |
| pods started | 4.3 | 4.6 | +7.0% | −0.5294 to +1.1294 | no |
| pod start wait, total (s) | 6.3 | 7.3 | +15.9% | −1.1591 to +3.1591 | no |
| pod start wait, mean (s) | 1.477 | 1.588 | +7.6% | −0.2840 to +0.5073 | no |
| host CPU busy, the real machine under kind (%) | 27.54 | 31.48 | +14.3% | +3.4380 to +4.4370 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.51 | −0.2% | −0.0101 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | −0.2% | −0.9090 to +0.2895 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | −0.2% | −0.9090 to +0.2895 | no |
| response time (ms), mean | 142.4 | 141.8 | −0.4% | −3.5333 to +2.3217 | no |
| response time (ms), 95th percentile | 295.1 | 284.3 | −3.7% | −21.1447 to −0.4483 | yes: GAIN |
| response time (ms), 99th percentile | 430.5 | 394.9 | −8.3% | −64.3724 to −6.7640 | yes: GAIN |
| time over the response line (% of samples) | 0.4733 | 0.216 | −54.4% | −0.4943 to −0.0203 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.8 | +5.800 (native is 0) | +4.8583 to +6.7417 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.4 | −8.4% | −0.4094 to +0.3361 | no |
| utilisation (used / allocatable) | 0.03816 | 0.03835 | +0.5% | −0.0007 to +0.0011 | no |
| CPU used (cores), mean | 0.9158 | 0.9203 | +0.5% | −0.0162 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0 | 0.03155 | +0.032 (native is 0) | +0.0291 to +0.0340 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9158 | 0.9519 | +3.9% | +0.0141 to +0.0580 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 688.5 | 685.7 | −0.4% | −17.0596 to +11.5154 | no |
| HPA replicas, mean | 8.957 | 10.1 | +12.7% | +0.5365 to +1.7420 | yes: power given |
| pods started | 4.3 | 7.4 | +72.1% | +1.7324 to +4.4676 | yes: power given |
| pod start wait, total (s) | 6.3 | 11.4 | +81.0% | +2.3307 to +7.8693 | yes: LOSS |
| pod start wait, mean (s) | 1.477 | 1.527 | +3.4% | −0.1641 to +0.2641 | no |
| host CPU busy, the real machine under kind (%) | 27.54 | 28.84 | +4.7% | +0.8319 to +1.7629 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.517 | 1.51 | −0.5% | −0.0163 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 158.6 | −1.1% | −2.8183 to −0.6048 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 158.6 | −1.1% | −2.8183 to −0.6048 | yes: GAIN |
| response time (ms), mean | 147.3 | 141.8 | −3.8% | −9.3405 to −1.7985 | yes: GAIN |
| response time (ms), 95th percentile | 289.9 | 284.3 | −1.9% | −17.4360 to +6.1870 | no |
| response time (ms), 99th percentile | 401.6 | 394.9 | −1.7% | −29.5792 to +16.3052 | no |
| time over the response line (% of samples) | 0.2188 | 0.216 | −1.3% | −0.2046 to +0.1990 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.8 | +5.800 (native is 0) | +4.8583 to +6.7417 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.24 | 0.4 | +66.7% | −0.0639 to +0.3839 | no |
| utilisation (used / allocatable) | 0.04252 | 0.03835 | −9.8% | −0.0049 to −0.0035 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.021 | 0.9203 | −9.8% | −0.1167 to −0.0837 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03155 | +0.032 (native is 0) | +0.0291 to +0.0340 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.021 | 0.9519 | −6.7% | −0.0859 to −0.0514 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 621.8 | 685.7 | +10.3% | +52.3950 to +75.4287 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.946 | 10.1 | +12.9% | +0.5366 to +1.7644 | yes: power given |
| pods started | 4.6 | 7.4 | +60.9% | +1.6417 to +3.9583 | yes: power given |
| pod start wait, total (s) | 7.3 | 11.4 | +56.2% | +1.1517 to +7.0483 | yes: LOSS |
| pod start wait, mean (s) | 1.588 | 1.527 | −3.9% | −0.4831 to +0.3598 | no |
| host CPU busy, the real machine under kind (%) | 31.48 | 28.84 | −8.4% | −3.0094 to −2.2708 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.511 | −0.2% | −0.0095 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.8 | +0.6% | +0.2528 to +1.6155 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.8 | +0.6% | +0.2528 to +1.6155 | yes: power given |
| response time (ms), mean | 142.4 | 148.3 | +4.2% | +3.5713 to +8.2733 | yes: LOSS |
| response time (ms), 95th percentile | 295.1 | 295.9 | +0.3% | −10.1638 to +11.8288 | no |
| response time (ms), 99th percentile | 430.5 | 408.2 | −5.2% | −52.4176 to +7.7480 | no |
| time over the response line (% of samples) | 0.4733 | 0.3334 | −29.6% | −0.3629 to +0.0830 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | −66.7% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +4.8845 to +7.9155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.33 | −24.4% | −0.6253 to +0.4120 | no |
| utilisation (used / allocatable) | 0.03816 | 0.04339 | +13.7% | +0.0040 to +0.0064 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9158 | 1.041 | +13.7% | +0.0968 to +0.1544 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05053 | +0.051 (native is 0) | +0.0460 to +0.0551 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9158 | 1.092 | +19.2% | +0.1441 to +0.2082 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 688.5 | 610.9 | −11.3% | −93.1604 to −62.0399 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.957 | 10.31 | +15.1% | +0.6024 to +2.0941 | yes: power given |
| pods started | 4.3 | 8 | +86.0% | +1.9141 to +5.4859 | yes: power given |
| pod start wait, total (s) | 6.3 | 12.6 | +100.0% | +2.1695 to +10.4305 | yes: LOSS |
| pod start wait, mean (s) | 1.477 | 1.524 | +3.2% | −0.2908 to +0.3863 | no |
| host CPU busy, the real machine under kind (%) | 27.54 | 33.89 | +23.0% | +5.4185 to +7.2759 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*