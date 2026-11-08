# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.567 | 6 |
| node-hours | 2.515 | 2.515 | 2.333 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.3 | 273.4 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.3 | 259.7 | 271.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 384.1 | 146.9 | 373.7 | 122.2 |
| response time (ms), 95th percentile | 1357 | 252.6 | 1563 | 266.3 |
| response time (ms), 99th percentile | 1953 | 365.2 | 2254 | 394.4 |
| time over the response line (% of samples) | 17.32 | 0.2472 | 17.44 | 0.3612 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 0.1 | 11.3 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 127.2 | 114.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.85 | 1193 | 11.03 | 1345 |
| utilisation (used / allocatable) | 0.06155 | 0.06037 | 0.06731 | 0.05799 |
| CPU used (cores), mean | 1.477 | 1.449 | 1.497 | 1.392 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07777 | 0.07333 |
| CPU used with Omni's own (cores), mean | 1.477 | 1.449 | 1.575 | 1.465 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 448.5 | 418.7 | 465.6 |
| HPA replicas, mean | 2.005 | 2.003 | 2.359 | 2.323 |
| pods started | 0.1 | 0 | 1 | 1 |
| pod start wait, total (s) | 0.2 | 0 | 2.8 | 2.9 |
| pod start wait, mean (s) | 0.2 | 0 | 1.083 | 0.58 |
| host CPU busy, the real machine under kind (%) | 42.26 | 45.81 | 45.93 | 46.99 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 783.6 | 1510 | 799 | 1507 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.23 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 183.2 | 0.03333 | 200.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 773.8 | 0.1 | 904.3 |
| queue: job turnaround, submitted to done, mean (s) | 91.48 | 877.3 | 103 | 935.8 |
| queue: jobs unfinished at the window's end | 0 | 12 | 0 | 15.1 |
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
| node-hours | 2.515 | 2.511 | −0.1% | −0.0109 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.2 | −0.4% | −1.8263 to −0.5075 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.2 | −0.4% | −1.8263 to −0.5075 | yes: GAIN |
| response time (ms), mean | 146.9 | 122.2 | −16.8% | −31.3716 to −18.0460 | yes: GAIN |
| response time (ms), 95th percentile | 252.6 | 266.3 | +5.4% | −1.3673 to +28.7583 | no |
| response time (ms), 99th percentile | 365.2 | 394.4 | +8.0% | +5.4639 to +52.9935 | yes: LOSS |
| time over the response line (% of samples) | 0.2472 | 0.3612 | +46.1% | −0.0003 to +0.2284 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.4 | +114.400 (native is 0) | +98.9138 to +129.8862 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1193 | 1345 | +12.8% | +87.0009 to +217.2424 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06037 | 0.05799 | −3.9% | −0.0031 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.449 | 1.392 | −3.9% | −0.0750 to −0.0393 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07333 | +0.073 (native is 0) | +0.0660 to +0.0807 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.465 | +1.1% | −0.0069 to +0.0393 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 465.6 | +3.8% | +11.6140 to +22.4307 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.323 | +16.0% | −0.0071 to +0.6470 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.5080 to +2.5080 | no |
| pod start wait, total (s) | 0 | 2.9 | +2.900 (native is 0) | −1.4764 to +7.2764 | no |
| pod start wait, mean (s) | 0 | 0.58 | +0.580 (native is 0) | −0.2953 to +1.4553 | no |
| host CPU busy, the real machine under kind (%) | 45.81 | 46.99 | +2.6% | +0.5589 to +1.8018 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 1507 | −0.2% | −6.6186 to +1.2186 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 183.2 | 200.8 | +9.6% | −22.1260 to +57.4093 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 773.8 | 904.3 | +16.9% | −0.9900 to +261.9900 | no |
| queue: job turnaround, submitted to done, mean (s) | 877.3 | 935.8 | +6.7% | +11.3290 to +105.6877 | yes: LOSS |
| queue: jobs unfinished at the window's end | 12 | 15.1 | +25.8% | −0.1069 to +6.3069 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | 0.0% | raw −0.0059 to +0.0059 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.3 | −0.2% | −2.9839 to +1.6818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.3 | −0.2% | −2.9839 to +1.6818 | no |
| response time (ms), mean | 384.1 | 146.9 | −61.7% | −385.9732 to −88.3742 | yes: GAIN |
| response time (ms), 95th percentile | 1357 | 252.6 | −81.4% | −1801.0167 to −406.8563 | yes: GAIN |
| response time (ms), 99th percentile | 1953 | 365.2 | −81.3% | −2594.7738 to −581.0778 | yes: GAIN |
| time over the response line (% of samples) | 17.32 | 0.2472 | −98.6% | −28.0536 to −6.0938 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 0.1 | −99.0% | −13.4553 to −6.5447 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.85 | 1193 | +10896.6% | +969.4126 to +1394.4274 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06155 | 0.06037 | −1.9% | −0.0079 to +0.0055 | no |
| CPU used (cores), mean | 1.477 | 1.449 | −1.9% | −0.1888 to +0.1322 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.477 | 1.449 | −1.9% | −0.1888 to +0.1322 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 448.5 | −0.0% | −44.9593 to +44.9393 | no |
| HPA replicas, mean | 2.005 | 2.003 | −0.1% | −0.1364 to +0.1325 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 42.26 | 45.81 | +8.4% | −0.0288 to +7.1330 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.6 | 1510 | +92.7% | +681.5077 to +770.8923 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 183.1 | +488300.0% | +137.8676 to +228.3574 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 773.8 | +386800.0% | +660.1130 to +887.0870 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.48 | 877.3 | +858.9% | +716.3651 to +855.2099 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12 | +12.000 (native is 0) | +7.1957 to +16.8043 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.567 | −7.2% | −0.8626 to −0.0037 | yes: GAIN |
| node-hours | 2.515 | 2.333 | −7.2% | −0.3591 to −0.0047 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | +0.1% | −0.4774 to +1.2055 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 259.7 | −4.9% | −26.6983 to +0.1890 | no |
| response time (ms), mean | 384.1 | 373.7 | −2.7% | −31.3094 to +10.4828 | no |
| response time (ms), 95th percentile | 1357 | 1563 | +15.2% | +38.5865 to +374.2635 | yes: LOSS |
| response time (ms), 99th percentile | 1953 | 2254 | +15.4% | +85.9218 to +515.7704 | yes: LOSS |
| time over the response line (% of samples) | 17.32 | 17.44 | +0.7% | −0.7568 to +1.0006 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 11.3 | +11.9% | −0.0972 to +2.4972 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.2 | +127.200 (native is 0) | +51.2293 to +203.1707 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.85 | 11.03 | +1.6% | −1.7073 to +2.0639 | no |
| utilisation (used / allocatable) | 0.06155 | 0.06731 | +9.4% | +0.0013 to +0.0102 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.477 | 1.497 | +1.4% | −0.0059 to +0.0462 | no |
| Omni's own CPU (cores), mean | 0 | 0.07777 | +0.078 (native is 0) | +0.0734 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.575 | +6.6% | +0.0698 to +0.1260 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 418.7 | −6.6% | −50.0272 to −9.5733 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.359 | +17.7% | +0.1343 to +0.5740 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | −0.2410 to +2.0410 | no |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | −0.8255 to +6.0255 | no |
| pod start wait, mean (s) | 0.2 | 1.083 | +441.7% | −0.3531 to +2.1198 | no |
| host CPU busy, the real machine under kind (%) | 42.26 | 45.93 | +8.7% | +3.1872 to +4.1598 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.6 | 799 | +2.0% | +4.1394 to +26.6606 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.23 | −12.8% | −1.5507 to +0.0111 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.03333 | −11.1% | −0.0338 to +0.0255 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.48 | 103.1 | +12.6% | +0.9880 to +22.1453 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.567 | −7.2% | −0.8626 to −0.0037 | yes: GAIN |
| node-hours | 2.515 | 2.333 | −7.2% | −0.3582 to −0.0056 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.4 | +0.4% | −1.0267 to +3.0570 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 259.7 | −4.6% | −27.4857 to +2.2785 | no |
| response time (ms), mean | 146.9 | 373.7 | +154.3% | +66.7343 to +386.7865 | yes: LOSS |
| response time (ms), 95th percentile | 252.6 | 1563 | +518.7% | +493.2595 to +2127.4635 | yes: LOSS |
| response time (ms), 99th percentile | 365.2 | 2254 | +517.2% | +714.9146 to +3062.6292 | yes: LOSS |
| time over the response line (% of samples) | 0.2472 | 17.44 | +6957.2% | +6.8284 to +27.5629 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 11.3 | +11200.0% | +8.5066 to +13.8934 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.2 | +127.200 (native is 0) | +51.2293 to +203.1707 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1193 | 11.03 | −99.1% | −1394.6491 to −968.8343 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06037 | 0.06731 | +11.5% | +0.0016 to +0.0123 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.449 | 1.497 | +3.3% | −0.1208 to +0.2177 | no |
| Omni's own CPU (cores), mean | 0 | 0.07777 | +0.078 (native is 0) | +0.0734 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.575 | +8.7% | −0.0457 to +0.2982 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 418.7 | −6.6% | −62.8388 to +3.2582 | no |
| HPA replicas, mean | 2.003 | 2.359 | +17.8% | +0.1410 to +0.5711 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.0663 to +2.0663 | no |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | −0.5004 to +6.1004 | no |
| pod start wait, mean (s) | 0 | 1.083 | +1.083 (native is 0) | +0.0452 to +2.1215 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.81 | 45.93 | +0.3% | −3.6698 to +3.9126 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 799 | −47.1% | −764.4028 to −657.1972 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 183.2 | 0.03333 | −100.0% | −228.3699 to −137.8634 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 773.8 | 0.1 | −100.0% | −887.1964 to −660.2036 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 877.3 | 103 | −88.3% | −837.3136 to −711.1281 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12 | 0 | −100.0% | −16.8043 to −7.1957 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.512 | −0.1% | −0.0113 to +0.0047 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 271.2 | −0.7% | −4.2552 to +0.6193 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 271.2 | −0.7% | −4.2552 to +0.6193 | no |
| response time (ms), mean | 384.1 | 122.2 | −68.2% | −414.1064 to −109.6587 | yes: GAIN |
| response time (ms), 95th percentile | 1357 | 266.3 | −80.4% | −1786.9053 to −393.5767 | yes: GAIN |
| response time (ms), 99th percentile | 1953 | 394.4 | −79.8% | −2567.1854 to −550.2088 | yes: GAIN |
| time over the response line (% of samples) | 17.32 | 0.3612 | −97.9% | −27.9087 to −6.0106 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 0.2 | −98.0% | −13.2796 to −6.5204 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.4 | +114.400 (native is 0) | +98.9138 to +129.8862 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.85 | 1345 | +12299.1% | +1168.8726 to +1499.2107 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06155 | 0.05799 | −5.8% | −0.0098 to +0.0027 | no |
| CPU used (cores), mean | 1.477 | 1.392 | −5.8% | −0.2354 to +0.0645 | no |
| Omni's own CPU (cores), mean | 0 | 0.07333 | +0.073 (native is 0) | +0.0660 to +0.0807 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.465 | −0.8% | −0.1555 to +0.1313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 465.6 | +3.8% | −24.8288 to +58.8535 | no |
| HPA replicas, mean | 2.005 | 2.323 | +15.9% | +0.0507 to +0.5853 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | −0.4676 to +2.2676 | no |
| pod start wait, total (s) | 0.2 | 2.9 | +1350.0% | −1.3751 to +6.7751 | no |
| pod start wait, mean (s) | 0.2 | 0.58 | +190.0% | −0.2684 to +1.0284 | no |
| host CPU busy, the real machine under kind (%) | 42.26 | 46.99 | +11.2% | +1.3735 to +8.0914 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.6 | 1507 | +92.3% | +677.4970 to +769.5030 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 200.8 | +535344.4% | +170.1972 to +231.3111 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 904.3 | +452050.0% | +765.1345 to +1043.0655 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.48 | 935.8 | +922.9% | +803.1143 to +885.4774 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.1 | +15.100 (native is 0) | +11.5084 to +18.6916 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*