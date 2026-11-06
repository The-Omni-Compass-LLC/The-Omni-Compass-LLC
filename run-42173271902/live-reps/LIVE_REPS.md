# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.712 | 6 |
| node-hours | 2.516 | 2.517 | 1.976 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | 272.9 | 270.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.1 | 232.4 | 270.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 365.5 | 130.4 | 363.2 | 108.3 |
| response time (ms), 95th percentile | 1351 | 226 | 1536 | 244.7 |
| response time (ms), 99th percentile | 1959 | 332.3 | 2255 | 367.5 |
| time over the response line (% of samples) | 16.52 | 0.23 | 16.51 | 0.375 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | 9.5 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 133.7 | 104.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 1132 | 10.76 | 1261 |
| utilisation (used / allocatable) | 0.06033 | 0.05911 | 0.07923 | 0.05782 |
| CPU used (cores), mean | 1.448 | 1.419 | 1.452 | 1.388 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07108 | 0.06954 |
| CPU used with Omni's own (cores), mean | 1.448 | 1.419 | 1.523 | 1.457 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.9 | 457.9 | 381.3 | 466.9 |
| HPA replicas, mean | 1.942 | 2.059 | 2.328 | 2.196 |
| pods started | 0 | 0 | 0.7 | 1.3 |
| pod start wait, total (s) | 0 | 0 | 1.5 | 3.5 |
| pod start wait, mean (s) | 0 | 0 | 0.8 | 1.625 |
| host CPU busy, the real machine under kind (%) | 41.28 | 44.2 | 44.38 | 46.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 785.1 | 1426 | 796.3 | 1485 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.957 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 173.6 | 0.0625 | 195.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 776.3 | 0.4 | 828.6 |
| queue: job turnaround, submitted to done, mean (s) | 90.32 | 816.3 | 102.1 | 912.8 |
| queue: jobs unfinished at the window's end | 0 | 10.6 | 0 | 12.9 |
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
| node-hours | 2.517 | 2.508 | −0.4% | −0.0173 to −0.0004 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 270.7 | −0.5% | −2.3406 to −0.3401 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 270.7 | −0.5% | −2.3406 to −0.3401 | yes: GAIN |
| response time (ms), mean | 130.4 | 108.3 | −16.9% | −29.1305 to −15.0579 | yes: GAIN |
| response time (ms), 95th percentile | 226 | 244.7 | +8.3% | +9.1578 to +28.1682 | yes: LOSS |
| response time (ms), 99th percentile | 332.3 | 367.5 | +10.6% | +9.4822 to +60.8998 | yes: LOSS |
| time over the response line (% of samples) | 0.23 | 0.375 | +63.1% | −0.0799 to +0.3699 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.5 | +104.500 (native is 0) | +90.6410 to +118.3590 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1132 | 1261 | +11.4% | +12.3224 to +245.0843 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05911 | 0.05782 | −2.2% | −0.0033 to +0.0007 | no |
| CPU used (cores), mean | 1.419 | 1.388 | −2.2% | −0.0793 to +0.0174 | no |
| Omni's own CPU (cores), mean | 0 | 0.06954 | +0.070 (native is 0) | +0.0612 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.457 | +2.7% | −0.0063 to +0.0835 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.9 | 466.9 | +2.0% | −5.1207 to +23.1055 | no |
| HPA replicas, mean | 2.059 | 2.196 | +6.7% | −0.0356 to +0.3102 | no |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2310 to +2.3690 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +0.6338 to +6.3662 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.625 | +1.625 (native is 0) | +0.5890 to +2.6610 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.2 | 46.59 | +5.4% | +1.2007 to +3.5928 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1426 | 1485 | +4.1% | −32.9388 to +149.7388 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 173.6 | 195.5 | +12.6% | −11.3519 to +55.0019 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 776.3 | 828.6 | +6.7% | −48.4949 to +153.0949 | no |
| queue: job turnaround, submitted to done, mean (s) | 816.3 | 912.8 | +11.8% | +23.5731 to +169.4519 | yes: LOSS |
| queue: jobs unfinished at the window's end | 10.6 | 12.9 | +21.7% | +0.3037 to +4.2963 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.0% | −0.0071 to +0.0081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | −0.2% | −2.8443 to +1.6262 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.1 | −0.2% | −2.8443 to +1.6262 | no |
| response time (ms), mean | 365.5 | 130.4 | −64.3% | −388.1789 to −81.9982 | yes: GAIN |
| response time (ms), 95th percentile | 1351 | 226 | −83.3% | −1859.9844 to −389.9816 | yes: GAIN |
| response time (ms), 99th percentile | 1959 | 332.3 | −83.0% | −2692.1731 to −560.6325 | yes: GAIN |
| time over the response line (% of samples) | 16.52 | 0.23 | −98.6% | −27.6367 to −4.9505 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | −98.9% | −13.1013 to −4.0987 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 1132 | +10729.3% | +854.5568 to +1389.3065 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06033 | 0.05911 | −2.0% | −0.0072 to +0.0047 | no |
| CPU used (cores), mean | 1.448 | 1.419 | −2.0% | −0.1725 to +0.1140 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.448 | 1.419 | −2.0% | −0.1725 to +0.1140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.9 | 457.9 | −0.4% | −45.2794 to +41.2183 | no |
| HPA replicas, mean | 1.942 | 2.059 | +6.0% | −0.0594 to +0.2932 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.28 | 44.2 | +7.1% | −0.3095 to +6.1384 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 785.1 | 1426 | +81.7% | +564.6626 to +717.7374 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 173.6 | +297550.0% | +117.5725 to +229.5692 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 776.3 | +258666.7% | +612.8880 to +939.1120 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 90.32 | 816.3 | +803.8% | +612.1645 to +839.7772 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.6 | +10.600 (native is 0) | +4.5661 to +16.6339 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.712 | −21.5% | −2.1976 to −0.3791 | yes: GAIN |
| node-hours | 2.516 | 1.976 | −21.5% | −0.9222 to −0.1585 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.6972 to +1.2188 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.4 | −14.8% | −69.1124 to −11.4701 | yes: GAIN |
| response time (ms), mean | 365.5 | 363.2 | −0.6% | −17.1547 to +12.6013 | no |
| response time (ms), 95th percentile | 1351 | 1536 | +13.7% | +34.9500 to +335.0680 | yes: LOSS |
| response time (ms), 99th percentile | 1959 | 2255 | +15.1% | +44.7353 to +547.2843 | yes: LOSS |
| time over the response line (% of samples) | 16.52 | 16.51 | −0.1% | −0.5868 to +0.5610 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.5 | +9.2% | −0.0121 to +1.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.7 | +133.700 (native is 0) | +69.9925 to +197.4075 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 10.76 | +2.9% | −1.0525 to +1.6625 | no |
| utilisation (used / allocatable) | 0.06033 | 0.07923 | +31.3% | +0.0054 to +0.0324 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.452 | +0.3% | −0.0242 to +0.0332 | no |
| Omni's own CPU (cores), mean | 0 | 0.07108 | +0.071 (native is 0) | +0.0623 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.523 | +5.2% | +0.0404 to +0.1108 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.9 | 381.3 | −17.1% | −133.3291 to −23.9252 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.328 | +19.9% | +0.1366 to +0.6359 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.2602 to +3.2602 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| host CPU busy, the real machine under kind (%) | 41.28 | 44.38 | +7.5% | +2.3146 to +3.8781 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 785.1 | 796.3 | +1.4% | +3.0387 to +19.3613 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.957 | −34.0% | −3.3007 to −0.7844 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0594 to +0.0677 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.5263 to +0.7263 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.32 | 102.1 | +13.0% | +2.7981 to +20.7019 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.712 | −21.5% | −2.1976 to −0.3791 | yes: GAIN |
| node-hours | 2.517 | 1.976 | −21.5% | −0.9247 to −0.1570 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.9 | +0.3% | −1.6394 to +3.3793 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 232.4 | −14.6% | −70.5733 to −8.7911 | yes: GAIN |
| response time (ms), mean | 130.4 | 363.2 | +178.6% | +69.1512 to +396.4725 | yes: LOSS |
| response time (ms), 95th percentile | 226 | 1536 | +579.6% | +468.4863 to +2151.4977 | yes: LOSS |
| response time (ms), 99th percentile | 332.3 | 2255 | +578.6% | +657.0177 to +3187.8075 | yes: LOSS |
| time over the response line (% of samples) | 0.23 | 16.51 | +7079.4% | +5.3304 to +27.2310 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9.5 | +9400.0% | +4.5579 to +14.2421 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.7 | +133.700 (native is 0) | +69.9925 to +197.4075 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1132 | 10.76 | −99.0% | −1389.8608 to −853.3925 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05911 | 0.07923 | +34.0% | +0.0117 to +0.0285 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.452 | +2.4% | −0.1276 to +0.1951 | no |
| Omni's own CPU (cores), mean | 0 | 0.07108 | +0.071 (native is 0) | +0.0623 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.523 | +7.4% | −0.0648 to +0.2745 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.9 | 381.3 | −16.7% | −95.2673 to −57.9260 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.059 | 2.328 | +13.1% | +0.0550 to +0.4837 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.2602 to +3.2602 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| host CPU busy, the real machine under kind (%) | 44.2 | 44.38 | +0.4% | −3.5317 to +3.8955 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1426 | 796.3 | −44.2% | −704.9781 to −555.0219 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 173.6 | 0.0625 | −100.0% | −229.5488 to −117.5845 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 776.3 | 0.4 | −99.9% | −938.6905 to −613.1095 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 816.3 | 102.1 | −87.5% | −821.5387 to −606.9030 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.6 | 0 | −100.0% | −16.6339 to −4.5661 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.508 | −0.3% | −0.0136 to −0.0030 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 270.7 | −0.7% | −4.4267 to +0.5278 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 270.7 | −0.7% | −4.4267 to +0.5278 | no |
| response time (ms), mean | 365.5 | 108.3 | −70.4% | −415.1852 to −99.1803 | yes: GAIN |
| response time (ms), 95th percentile | 1351 | 244.7 | −81.9% | −1846.1969 to −366.4431 | yes: GAIN |
| response time (ms), 99th percentile | 1959 | 367.5 | −81.2% | −2653.4574 to −528.9662 | yes: GAIN |
| time over the response line (% of samples) | 16.52 | 0.375 | −97.7% | −27.3504 to −4.9468 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.3 | −96.6% | −12.7732 to −4.0268 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.5 | +104.500 (native is 0) | +90.6410 to +118.3590 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.46 | 1261 | +11960.2% | +1041.6601 to +1459.6099 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06033 | 0.05782 | −4.2% | −0.0095 to +0.0045 | no |
| CPU used (cores), mean | 1.448 | 1.388 | −4.2% | −0.2280 to +0.1076 | no |
| Omni's own CPU (cores), mean | 0 | 0.06954 | +0.070 (native is 0) | +0.0612 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.457 | +0.6% | −0.1506 to +0.1693 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.9 | 466.9 | +1.5% | −43.4869 to +57.4107 | no |
| HPA replicas, mean | 1.942 | 2.196 | +13.1% | −0.0082 to +0.5166 | no |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2310 to +2.3690 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +0.6338 to +6.3662 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.625 | +1.625 (native is 0) | +0.5890 to +2.6610 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.28 | 46.59 | +12.9% | +1.4398 to +9.1827 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 785.1 | 1485 | +89.1% | +645.6406 to +753.5594 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 195.5 | +334964.3% | +146.1645 to +244.6272 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 828.6 | +276100.0% | +706.6856 to +949.9144 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 90.32 | 912.8 | +910.6% | +753.3702 to +891.5964 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.9 | +12.900 (native is 0) | +7.0357 to +18.7643 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*