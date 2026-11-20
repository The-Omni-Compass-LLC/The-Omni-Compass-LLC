# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.27 | 6 |
| node-hours | 2.513 | 2.519 | 2.214 | 2.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273 | 273.4 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 273 | 250.5 | 271.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 367.9 | 143.1 | 351 | 150.3 |
| response time (ms), 95th percentile | 1308 | 247 | 1472 | 267.8 |
| response time (ms), 99th percentile | 1910 | 357.4 | 2077 | 386.2 |
| time over the response line (% of samples) | 16.48 | 0.2845 | 16.8 | 0.3491 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | 10.2 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 140.6 | 20 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 1209 | 9.862 | 1286 |
| utilisation (used / allocatable) | 0.06056 | 0.06078 | 0.069 | 0.0584 |
| CPU used (cores), mean | 1.453 | 1.459 | 1.453 | 1.402 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07761 | 0.06917 |
| CPU used with Omni's own (cores), mean | 1.453 | 1.459 | 1.531 | 1.471 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.5 | 446 | 415.1 | 462.5 |
| HPA replicas, mean | 1.955 | 2.025 | 2.386 | 2.226 |
| pods started | 0.2 | 0.1 | 1.8 | 1.5 |
| pod start wait, total (s) | 0.6 | 0.1 | 3.9 | 3.4 |
| pod start wait, mean (s) | 0.3 | 0.1 | 1.475 | 1.067 |
| host CPU busy, the real machine under kind (%) | 42.08 | 46.09 | 45.4 | 47.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 781.6 | 1508 | 791.7 | 1511 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.659 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 158.1 | 0.07917 | 177.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 696.1 | 0.5 | 763.8 |
| queue: job turnaround, submitted to done, mean (s) | 87.9 | 880.8 | 97.46 | 893 |
| queue: jobs unfinished at the window's end | 0 | 11.2 | 0 | 12.6 |
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
| node-hours | 2.519 | 2.517 | −0.1% | −0.0120 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 271.9 | −0.4% | −2.2962 to +0.0558 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 271.9 | −0.4% | −2.2962 to +0.0558 | no |
| response time (ms), mean | 143.1 | 150.3 | +5.1% | +2.7192 to +11.7512 | yes: LOSS |
| response time (ms), 95th percentile | 247 | 267.8 | +8.4% | +4.9417 to +36.5593 | yes: LOSS |
| response time (ms), 99th percentile | 357.4 | 386.2 | +8.1% | +9.5690 to +48.0142 | yes: LOSS |
| time over the response line (% of samples) | 0.2845 | 0.3491 | +22.7% | −0.0739 to +0.2031 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20.000 (native is 0) | +13.9586 to +26.0414 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1209 | 1286 | +6.4% | +39.5007 to +114.5526 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06078 | 0.0584 | −3.9% | −0.0035 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.459 | 1.402 | −3.9% | −0.0846 to −0.0293 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06917 | +0.069 (native is 0) | +0.0636 to +0.0748 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.471 | +0.8% | −0.0167 to +0.0412 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446 | 462.5 | +3.7% | +8.5704 to +24.5871 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.226 | +9.9% | −0.1499 to +0.5525 | no |
| pods started | 0.1 | 1.5 | +1400.0% | +0.0015 to +2.7985 | yes: power given |
| pod start wait, total (s) | 0.1 | 3.4 | +3300.0% | −0.2374 to +6.8374 | no |
| pod start wait, mean (s) | 0.1 | 1.067 | +966.7% | +0.0232 to +1.9101 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.09 | 47.47 | +3.0% | +0.9574 to +1.8012 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 1511 | +0.2% | −6.0307 to +11.8307 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158.1 | 177.5 | +12.3% | −31.0940 to +69.9440 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.1 | 763.8 | +9.7% | −159.0593 to +294.4593 | no |
| queue: job turnaround, submitted to done, mean (s) | 880.8 | 893 | +1.4% | −7.8203 to +32.2036 | no |
| queue: jobs unfinished at the window's end | 11.2 | 12.6 | +12.5% | −0.6841 to +3.4841 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.519 | +0.3% | −0.0019 to +0.0156 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273 | +0.2% | −1.8685 to +3.1939 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 273 | +0.2% | −1.8685 to +3.1939 | no |
| response time (ms), mean | 367.9 | 143.1 | −61.1% | −366.2510 to −83.5077 | yes: GAIN |
| response time (ms), 95th percentile | 1308 | 247 | −81.1% | −1738.1623 to −382.8307 | yes: GAIN |
| response time (ms), 99th percentile | 1910 | 357.4 | −81.3% | −2535.3483 to −569.9395 | yes: GAIN |
| time over the response line (% of samples) | 16.48 | 0.2845 | −98.3% | −27.1346 to −5.2579 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | −98.9% | −12.6565 to −4.9435 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 1209 | +11564.5% | +1024.8978 to +1371.6556 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06056 | 0.06078 | +0.4% | −0.0060 to +0.0065 | no |
| CPU used (cores), mean | 1.453 | 1.459 | +0.4% | −0.1449 to +0.1554 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.453 | 1.459 | +0.4% | −0.1449 to +0.1554 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.5 | 446 | −2.3% | −54.2533 to +33.2826 | no |
| HPA replicas, mean | 1.955 | 2.025 | +3.6% | −0.0964 to +0.2361 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.6 | 0.1 | −83.3% | −1.9005 to +0.9005 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 42.08 | 46.09 | +9.5% | +0.8701 to +7.1500 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.6 | 1508 | +92.9% | +684.9059 to +767.2941 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 158.1 | +223035.3% | +107.9852 to +207.9815 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 696.1 | +115916.7% | +469.8442 to +921.1558 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.9 | 880.8 | +902.1% | +742.6115 to +843.2885 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.2 | +11.200 (native is 0) | +6.3744 to +16.0256 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.27 | −12.2% | −1.2783 to −0.1816 | yes: GAIN |
| node-hours | 2.513 | 2.214 | −11.9% | −0.5284 to −0.0680 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273.4 | +0.4% | +0.3580 to +1.8107 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 250.5 | −8.0% | −39.3328 to −4.4818 | yes: GAIN |
| response time (ms), mean | 367.9 | 351 | −4.6% | −28.4360 to −5.5270 | yes: GAIN |
| response time (ms), 95th percentile | 1308 | 1472 | +12.6% | +64.8506 to +263.4504 | yes: LOSS |
| response time (ms), 99th percentile | 1910 | 2077 | +8.7% | +60.5767 to +273.4759 | yes: LOSS |
| time over the response line (% of samples) | 16.48 | 16.8 | +1.9% | −0.4949 to +1.1346 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 10.2 | +14.6% | +0.4706 to +2.1294 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 140.6 | +140.600 (native is 0) | +42.5561 to +238.6439 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 9.862 | −4.8% | −2.7623 to +1.7623 | no |
| utilisation (used / allocatable) | 0.06056 | 0.069 | +13.9% | +0.0029 to +0.0140 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.453 | −0.0% | −0.0262 to +0.0257 | no |
| Omni's own CPU (cores), mean | 0 | 0.07761 | +0.078 (native is 0) | +0.0728 to +0.0825 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.531 | +5.3% | +0.0532 to +0.1016 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.5 | 415.1 | −9.1% | −68.5188 to −14.2594 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.386 | +22.0% | +0.1237 to +0.7381 | yes: power given |
| pods started | 0.2 | 1.8 | +800.0% | +0.5772 to +2.6228 | yes: power given |
| pod start wait, total (s) | 0.6 | 3.9 | +550.0% | +0.6870 to +5.9130 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.475 | +391.7% | +0.2591 to +2.0909 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.08 | 45.4 | +7.9% | +3.0643 to +3.5801 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.6 | 791.7 | +1.3% | +3.2105 to +16.9895 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.659 | −22.4% | −2.3053 to −0.3770 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.07917 | +11.8% | −0.0399 to +0.0566 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.9 | 97.46 | +10.9% | +2.6675 to +16.4658 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.27 | −12.2% | −1.2783 to −0.1816 | yes: GAIN |
| node-hours | 2.519 | 2.214 | −12.1% | −0.5347 to −0.0755 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | +0.2% | −2.1023 to +2.9457 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 250.5 | −8.3% | −41.8107 to −3.3292 | yes: GAIN |
| response time (ms), mean | 143.1 | 351 | +145.3% | +60.1220 to +355.6737 | yes: LOSS |
| response time (ms), 95th percentile | 247 | 1472 | +495.7% | +469.2829 to +1980.0111 | yes: LOSS |
| response time (ms), 99th percentile | 357.4 | 2077 | +481.1% | +644.0068 to +2795.3336 | yes: LOSS |
| time over the response line (% of samples) | 0.2845 | 16.8 | +5805.2% | +6.2728 to +26.7593 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 10.2 | +10100.0% | +6.9287 to +13.2713 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 140.6 | +140.600 (native is 0) | +42.5561 to +238.6439 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1209 | 9.862 | −99.2% | −1372.2043 to −1025.3490 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06078 | 0.069 | +13.5% | +0.0035 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.459 | 1.453 | −0.4% | −0.1733 to +0.1623 | no |
| Omni's own CPU (cores), mean | 0 | 0.07761 | +0.078 (native is 0) | +0.0728 to +0.0825 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.531 | +4.9% | −0.0961 to +0.2404 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446 | 415.1 | −6.9% | −58.4220 to −3.3855 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.386 | +17.8% | +0.1270 to +0.5950 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.5295 to +2.8705 | yes: power given |
| pod start wait, total (s) | 0.1 | 3.9 | +3800.0% | +1.1707 to +6.4293 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.475 | +1375.0% | +0.4939 to +2.2561 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.09 | 45.4 | −1.5% | −3.8885 to +2.5128 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 791.7 | −47.5% | −762.8682 to −669.1318 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.25 | −29.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158.1 | 0.07917 | −99.9% | −207.9652 to −107.9848 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.1 | 0.5 | −99.9% | −921.3059 to −469.8941 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 880.8 | 97.46 | −88.9% | −832.1296 to −734.6371 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.2 | 0 | −100.0% | −16.0256 to −6.3744 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.517 | +0.2% | −0.0055 to +0.0142 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | −0.2% | −3.3471 to +2.4320 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | −0.2% | −3.3471 to +2.4320 | no |
| response time (ms), mean | 367.9 | 150.3 | −59.2% | −357.5354 to −77.7529 | yes: GAIN |
| response time (ms), 95th percentile | 1308 | 267.8 | −79.5% | −1711.5460 to −367.9460 | yes: GAIN |
| response time (ms), 99th percentile | 1910 | 386.2 | −79.8% | −2495.0313 to −552.6733 | yes: GAIN |
| time over the response line (% of samples) | 16.48 | 0.3491 | −97.9% | −26.9993 to −5.2639 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | −98.9% | −12.6565 to −4.9435 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20.000 (native is 0) | +13.9586 to +26.0414 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 1286 | +12307.9% | +1092.7899 to +1457.8168 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06056 | 0.0584 | −3.6% | −0.0085 to +0.0042 | no |
| CPU used (cores), mean | 1.453 | 1.402 | −3.6% | −0.2045 to +0.1011 | no |
| Omni's own CPU (cores), mean | 0 | 0.06917 | +0.069 (native is 0) | +0.0636 to +0.0748 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.471 | +1.2% | −0.1303 to +0.1652 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.5 | 462.5 | +1.3% | −38.2869 to +50.4737 | no |
| HPA replicas, mean | 1.955 | 2.226 | +13.9% | −0.0727 to +0.6150 | no |
| pods started | 0.2 | 1.5 | +650.0% | −0.2099 to +2.8099 | no |
| pod start wait, total (s) | 0.6 | 3.4 | +466.7% | −1.2295 to +6.8295 | no |
| pod start wait, mean (s) | 0.3 | 1.067 | +255.6% | −0.4751 to +2.0084 | no |
| host CPU busy, the real machine under kind (%) | 42.08 | 47.47 | +12.8% | +2.3662 to +8.4126 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.6 | 1511 | +93.3% | +684.6164 to +773.3836 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 177.5 | +250458.8% | +142.7222 to +212.0945 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 763.8 | +127200.0% | +641.9335 to +884.4665 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.9 | 893 | +916.0% | +753.2814 to +857.0019 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.6 | +12.600 (native is 0) | +8.5790 to +16.6210 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*