# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.514 | 1.514 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.7 | 158.8 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.7 | 158.8 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 134.7 | 137.8 | 132.4 | 140.5 |
| response time (ms), 95th percentile | 274.1 | 282.8 | 270.1 | 279.9 |
| response time (ms), 99th percentile | 379.7 | 388.8 | 353.1 | 390.2 |
| time over the response line (% of samples) | 0.2186 | 0.3347 | 0.1924 | 0.3353 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.4 | 7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.16 | 0.2667 | 0.2217 |
| utilisation (used / allocatable) | 0.03747 | 0.04191 | 0.03781 | 0.0434 |
| CPU used (cores), mean | 0.8992 | 1.006 | 0.9076 | 1.042 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.02947 | 0.04835 |
| CPU used with Omni's own (cores), mean | 0.8992 | 1.006 | 0.937 | 1.09 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.7 | 631.8 | 695.9 | 612.4 |
| HPA replicas, mean | 8.895 | 8.868 | 9.917 | 10.32 |
| pods started | 4.8 | 5.1 | 6.1 | 7.9 |
| pod start wait, total (s) | 7.5 | 7.5 | 9.3 | 12.2 |
| pod start wait, mean (s) | 1.565 | 1.487 | 1.495 | 1.503 |
| host CPU busy, the real machine under kind (%) | 27.02 | 30.77 | 28.29 | 33.76 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.511 | −0.2% | −0.0109 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 159.8 | +0.1% | −0.7811 to +0.9425 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 159.8 | +0.1% | −0.7811 to +0.9425 | no |
| response time (ms), mean | 137.8 | 140.5 | +1.9% | −1.5102 to +6.8022 | no |
| response time (ms), 95th percentile | 282.8 | 279.9 | −1.0% | −16.2809 to +10.4569 | no |
| response time (ms), 99th percentile | 388.8 | 390.2 | +0.4% | −24.6383 to +27.4411 | no |
| time over the response line (% of samples) | 0.3347 | 0.3353 | +0.2% | −0.1889 to +0.1902 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7 | +7.000 (native is 0) | +5.1226 to +8.8774 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2217 | +38.5% | −0.2128 to +0.3361 | no |
| utilisation (used / allocatable) | 0.04191 | 0.0434 | +3.6% | +0.0007 to +0.0023 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.006 | 1.042 | +3.6% | +0.0160 to +0.0555 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04835 | +0.048 (native is 0) | +0.0409 to +0.0558 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 1.09 | +8.4% | +0.0585 to +0.1098 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.8 | 612.4 | −3.1% | −29.4537 to −9.1707 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.868 | 10.32 | +16.4% | +0.6421 to +2.2689 | yes: power given |
| pods started | 5.1 | 7.9 | +54.9% | +0.9904 to +4.6096 | yes: power given |
| pod start wait, total (s) | 7.5 | 12.2 | +62.7% | +1.1147 to +8.2853 | yes: LOSS |
| pod start wait, mean (s) | 1.487 | 1.503 | +1.1% | −0.3411 to +0.3746 | no |
| host CPU busy, the real machine under kind (%) | 30.77 | 33.76 | +9.7% | +2.2236 to +3.7550 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.513 | +0.1% | −0.0081 to +0.0124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.7 | +0.8% | +0.1331 to +2.3545 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.7 | +0.8% | +0.1331 to +2.3545 | yes: power given |
| response time (ms), mean | 134.7 | 137.8 | +2.3% | +0.5623 to +5.6908 | yes: LOSS |
| response time (ms), 95th percentile | 274.1 | 282.8 | +3.2% | −2.4304 to +19.9104 | no |
| response time (ms), 99th percentile | 379.7 | 388.8 | +2.4% | −3.9385 to +21.9839 | no |
| time over the response line (% of samples) | 0.2186 | 0.3347 | +53.1% | −0.0366 to +0.2687 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.16 | −62.6% | −0.6617 to +0.1250 | no |
| utilisation (used / allocatable) | 0.03747 | 0.04191 | +11.9% | +0.0039 to +0.0050 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8992 | 1.006 | +11.9% | +0.0932 to +0.1200 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8992 | 1.006 | +11.9% | +0.0932 to +0.1200 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.7 | 631.8 | −10.0% | −76.0805 to −63.7208 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.895 | 8.868 | −0.3% | −0.1196 to +0.0657 | no |
| pods started | 4.8 | 5.1 | +6.2% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 7.5 | 7.5 | ±0.0% | −1.7194 to +1.7194 | no |
| pod start wait, mean (s) | 1.565 | 1.487 | −5.0% | −0.4865 to +0.3298 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 30.77 | +13.9% | +3.4154 to +4.1030 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.514 | +0.2% | +0.0009 to +0.0037 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.8 | +0.2% | +0.1658 to +0.5282 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.8 | +0.2% | +0.1658 to +0.5282 | yes: power given |
| response time (ms), mean | 134.7 | 132.4 | −1.8% | −5.2589 to +0.5370 | no |
| response time (ms), 95th percentile | 274.1 | 270.1 | −1.5% | −14.1775 to +6.1675 | no |
| response time (ms), 99th percentile | 379.7 | 353.1 | −7.0% | −40.3153 to −12.8723 | yes: GAIN |
| time over the response line (% of samples) | 0.2186 | 0.1924 | −12.0% | −0.1980 to +0.1455 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.4 | +5.400 (native is 0) | +4.3231 to +6.4769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.2667 | −37.7% | −0.4369 to +0.1135 | no |
| utilisation (used / allocatable) | 0.03747 | 0.03781 | +0.9% | +0.0000 to +0.0006 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8992 | 0.9076 | +0.9% | +0.0011 to +0.0155 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02947 | +0.029 (native is 0) | +0.0253 to +0.0337 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8992 | 0.937 | +4.2% | +0.0283 to +0.0473 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.7 | 695.9 | −0.8% | −11.1221 to −0.4323 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.895 | 9.917 | +11.5% | +0.2966 to +1.7474 | yes: power given |
| pods started | 4.8 | 6.1 | +27.1% | −0.3537 to +2.9537 | no |
| pod start wait, total (s) | 7.5 | 9.3 | +24.0% | −1.8908 to +5.4908 | no |
| pod start wait, mean (s) | 1.565 | 1.495 | −4.5% | −0.5300 to +0.3900 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 28.29 | +4.7% | +1.0226 to +1.5226 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0098 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 158.8 | −0.6% | −1.9317 to +0.1381 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 158.8 | −0.6% | −1.9317 to +0.1381 | no |
| response time (ms), mean | 137.8 | 132.4 | −4.0% | −9.2522 to −1.7228 | yes: GAIN |
| response time (ms), 95th percentile | 282.8 | 270.1 | −4.5% | −27.0587 to +1.5687 | no |
| response time (ms), 99th percentile | 388.8 | 353.1 | −9.2% | −58.3175 to −12.9155 | yes: GAIN |
| time over the response line (% of samples) | 0.3347 | 0.1924 | −42.5% | −0.2690 to −0.0156 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.4 | +5.400 (native is 0) | +4.3231 to +6.4769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2667 | +66.7% | −0.1961 to +0.4095 | no |
| utilisation (used / allocatable) | 0.04191 | 0.03781 | −9.8% | −0.0046 to −0.0036 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.006 | 0.9076 | −9.8% | −0.1097 to −0.0869 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02947 | +0.029 (native is 0) | +0.0253 to +0.0337 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 0.937 | −6.8% | −0.0788 to −0.0588 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.8 | 695.9 | +10.1% | +58.6540 to +69.5928 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.868 | 9.917 | +11.8% | +0.3413 to +1.7567 | yes: power given |
| pods started | 5.1 | 6.1 | +19.6% | −0.8469 to +2.8469 | no |
| pod start wait, total (s) | 7.5 | 9.3 | +24.0% | −1.6355 to +5.2355 | no |
| pod start wait, mean (s) | 1.487 | 1.495 | +0.6% | −0.4410 to +0.4576 | no |
| host CPU busy, the real machine under kind (%) | 30.77 | 28.29 | −8.1% | −2.7518 to −2.2214 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.511 | −0.0% | −0.0066 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.8 | +0.8% | +0.6194 to +2.0296 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.8 | +0.8% | +0.6194 to +2.0296 | yes: power given |
| response time (ms), mean | 134.7 | 140.5 | +4.3% | +3.1890 to +8.3561 | yes: LOSS |
| response time (ms), 95th percentile | 274.1 | 279.9 | +2.1% | −3.1806 to +14.8366 | no |
| response time (ms), 99th percentile | 379.7 | 390.2 | +2.7% | −10.7561 to +31.6043 | no |
| time over the response line (% of samples) | 0.2186 | 0.3353 | +53.4% | −0.0750 to +0.3084 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7 | +7.000 (native is 0) | +5.1226 to +8.8774 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.2217 | −48.2% | −0.5192 to +0.1059 | no |
| utilisation (used / allocatable) | 0.03747 | 0.0434 | +15.8% | +0.0049 to +0.0070 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8992 | 1.042 | +15.8% | +0.1174 to +0.1673 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04835 | +0.048 (native is 0) | +0.0409 to +0.0558 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8992 | 1.09 | +21.2% | +0.1590 to +0.2224 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.7 | 612.4 | −12.7% | −98.9617 to −79.4639 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.895 | 10.32 | +16.1% | +0.5765 to +2.2806 | yes: power given |
| pods started | 4.8 | 7.9 | +64.6% | +1.4671 to +4.7329 | yes: power given |
| pod start wait, total (s) | 7.5 | 12.2 | +62.7% | +1.0208 to +8.3792 | yes: LOSS |
| pod start wait, mean (s) | 1.565 | 1.503 | −3.9% | −0.4834 to +0.3603 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 33.76 | +25.0% | +5.7623 to +7.7347 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*