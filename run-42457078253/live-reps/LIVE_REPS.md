# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.349 | 6 |
| node-hours | 2.516 | 2.517 | 2.241 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273 | 274.7 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 273 | 254.2 | 271.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 451.1 | 147 | 506.7 | 122.5 |
| response time (ms), 95th percentile | 1679 | 251.4 | 2147 | 263 |
| response time (ms), 99th percentile | 2416 | 366.3 | 2897 | 381.3 |
| time over the response line (% of samples) | 22.71 | 0.2664 | 23.38 | 0.3344 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 0.1111 | 12.3 | 0.2857 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 84.7 | 118 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 1217 | 22.5 | 1370 |
| utilisation (used / allocatable) | 0.06408 | 0.0611 | 0.07451 | 0.05847 |
| CPU used (cores), mean | 1.538 | 1.466 | 1.591 | 1.403 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07811 | 0.07397 |
| CPU used with Omni's own (cores), mean | 1.538 | 1.466 | 1.669 | 1.477 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431 | 443.9 | 384.3 | 462.3 |
| HPA replicas, mean | 1.966 | 2.09 | 2.281 | 2.326 |
| pods started | 0.1 | 0.1111 | 1.2 | 1.714 |
| pod start wait, total (s) | 0.2 | 0.1111 | 2.9 | 3.714 |
| pod start wait, mean (s) | 0.2 | 0.1111 | 1.45 | 1.329 |
| host CPU busy, the real machine under kind (%) | 43.95 | 46 | 48.71 | 47.07 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 805 | 1478 | 841.9 | 1480 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.796 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 155.4 | 0.3875 | 207 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 709.2 | 2 | 860.7 |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 890.9 | 145.1 | 963 |
| queue: jobs unfinished at the window's end | 0 | 12.78 | 0 | 14.71 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 6 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.518 | +0.0% | −0.0179 to +0.0191 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.2 | −0.2% | −2.2858 to +0.9970 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 272.2 | −0.2% | −2.2858 to +0.9970 | no |
| response time (ms), mean | 143.4 | 116.5 | −18.7% | −34.1032 to −19.6463 | yes: GAIN |
| response time (ms), 95th percentile | 248.7 | 258 | +3.8% | −7.7377 to +26.4761 | no |
| response time (ms), 99th percentile | 351.6 | 377.8 | +7.5% | −8.0863 to +60.5163 | no |
| time over the response line (% of samples) | 0.2318 | 0.3644 | +57.2% | −0.0972 to +0.3623 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3333 | +0.333 (native is 0) | −0.2087 to +0.8753 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.8 | +115.833 (native is 0) | +97.0525 to +134.6142 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1197 | 1333 | +11.4% | +93.6728 to +178.5328 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06065 | 0.05899 | −2.7% | −0.0033 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.456 | 1.416 | −2.7% | −0.0796 to −0.0002 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07297 | +0.073 (native is 0) | +0.0603 to +0.0856 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.456 | 1.489 | +2.3% | +0.0011 to +0.0650 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.9 | 458.3 | +2.6% | −0.3330 to +23.1356 | no |
| HPA replicas, mean | 2.043 | 2.239 | +9.6% | −0.0547 to +0.4479 | no |
| pods started | 0.1667 | 1.167 | +600.0% | −0.1498 to +2.1498 | no |
| pod start wait, total (s) | 0.1667 | 2 | +1100.0% | −0.5058 to +4.1725 | no |
| pod start wait, mean (s) | 0.1667 | 1.083 | +550.0% | −0.0463 to +1.8796 | no |
| host CPU busy, the real machine under kind (%) | 45.7 | 46.95 | +2.8% | +0.2095 to +2.3044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1462 | 1476 | +1.0% | −18.7295 to +47.3962 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 163.1 | 210.1 | +28.8% | −31.4921 to +125.4366 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 769.3 | 847 | +10.1% | −348.6966 to +504.0300 | no |
| queue: job turnaround, submitted to done, mean (s) | 871.4 | 941.7 | +8.1% | +32.1390 to +108.4582 | yes: LOSS |
| queue: jobs unfinished at the window's end | 13 | 14 | +7.7% | −1.0992 to +3.0992 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.0% | −0.0064 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273 | −0.4% | −2.8210 to +0.7546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 273 | −0.4% | −2.8210 to +0.7546 | no |
| response time (ms), mean | 441.2 | 147 | −66.7% | −443.9788 to −144.3582 | yes: GAIN |
| response time (ms), 95th percentile | 1638 | 251.4 | −84.7% | −2096.2575 to −676.6203 | yes: GAIN |
| response time (ms), 99th percentile | 2339 | 366.3 | −84.3% | −2960.9583 to −984.5335 | yes: GAIN |
| time over the response line (% of samples) | 21.85 | 0.2664 | −98.8% | −32.7716 to −10.3937 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.22 | 0.1111 | −99.0% | −15.0201 to −7.2021 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.61 | 1217 | +10387.8% | +964.6608 to +1446.8540 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06381 | 0.0611 | −4.2% | −0.0084 to +0.0030 | no |
| CPU used (cores), mean | 1.531 | 1.466 | −4.2% | −0.2020 to +0.0719 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.531 | 1.466 | −4.2% | −0.2020 to +0.0719 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.2 | 443.9 | +2.5% | −28.5789 to +50.0419 | no |
| HPA replicas, mean | 1.946 | 2.09 | +7.4% | −0.0053 to +0.2938 | no |
| pods started | 0.1111 | 0.1111 | ±0.0% | −0.3843 to +0.3843 | no |
| pod start wait, total (s) | 0.2222 | 0.1111 | −50.0% | −0.7120 to +0.4898 | no |
| pod start wait, mean (s) | 0.2222 | 0.1111 | −50.0% | −0.7120 to +0.4898 | no |
| host CPU busy, the real machine under kind (%) | 43.66 | 46 | +5.4% | −0.6677 to +5.3506 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.6 | 1478 | +84.2% | +608.7066 to +742.8489 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05093 | 155.4 | +305036.4% | +115.3508 to +195.3343 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4444 | 709.2 | +159475.0% | +506.8656 to +910.6899 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 109.7 | 890.9 | +712.0% | +697.1267 to +865.1696 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.78 | +12.778 (native is 0) | +6.5713 to +18.9842 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.349 | −10.9% | −1.2703 to −0.0322 | yes: GAIN |
| node-hours | 2.516 | 2.241 | −10.9% | −0.5375 to −0.0130 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.7 | +0.2% | −1.2177 to +2.3144 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 254.2 | −7.3% | −40.4143 to +0.5236 | no |
| response time (ms), mean | 451.1 | 506.7 | +12.3% | −99.2907 to +210.5973 | no |
| response time (ms), 95th percentile | 1679 | 2147 | +27.9% | −145.4892 to +1082.8302 | no |
| response time (ms), 99th percentile | 2416 | 2897 | +19.9% | −138.8961 to +1101.1973 | no |
| time over the response line (% of samples) | 22.71 | 23.38 | +2.9% | −1.3659 to +2.7008 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 12.3 | +7.0% | −0.2003 to +1.8003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.7 | +84.700 (native is 0) | +11.2339 to +158.1661 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.6 | 22.5 | +94.0% | −13.8230 to +35.6296 | no |
| utilisation (used / allocatable) | 0.06408 | 0.07451 | +16.3% | +0.0037 to +0.0172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.538 | 1.591 | +3.5% | −0.0313 to +0.1382 | no |
| Omni's own CPU (cores), mean | 0 | 0.07811 | +0.078 (native is 0) | +0.0700 to +0.0862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.538 | 1.669 | +8.6% | +0.0396 to +0.2235 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431 | 384.3 | −10.8% | −77.8268 to −15.6930 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.281 | +16.0% | +0.1278 to +0.5030 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.9 | +1350.0% | +0.3384 to +5.0616 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.45 | +625.0% | +0.0430 to +2.4570 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.95 | 48.71 | +10.8% | +1.7910 to +7.7261 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805 | 841.9 | +4.6% | −16.5388 to +90.3388 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.796 | −20.1% | −2.2952 to −0.1128 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.3875 | +564.3% | −0.3648 to +1.0231 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2 | +300.0% | −2.1668 to +5.1668 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 145.1 | +29.7% | −13.5087 to +80.0170 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.276 | −12.1% | −1.4040 to −0.0432 | yes: GAIN |
| node-hours | 2.517 | 2.212 | −12.1% | −0.5903 to −0.0203 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 274.7 | +0.6% | −1.3726 to +4.7941 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 251.9 | −7.7% | −45.0797 to +2.9595 | no |
| response time (ms), mean | 147 | 503.8 | +242.7% | +83.8224 to +629.8416 | yes: LOSS |
| response time (ms), 95th percentile | 251.4 | 2123 | +744.4% | +644.2826 to +3098.0196 | yes: LOSS |
| response time (ms), 99th percentile | 366.3 | 2841 | +675.6% | +1037.0381 to +3911.8177 | yes: LOSS |
| time over the response line (% of samples) | 0.2664 | 22.59 | +8378.1% | +10.5062 to +34.1316 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 12.11 | +10800.0% | +8.0430 to +15.9570 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.11 | +91.111 (native is 0) | +9.0234 to +173.1988 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1217 | 23.68 | −98.1% | −1427.9816 to −959.3850 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0611 | 0.07503 | +22.8% | +0.0097 to +0.0181 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.466 | 1.582 | +7.9% | −0.0894 to +0.3201 | no |
| Omni's own CPU (cores), mean | 0 | 0.07811 | +0.078 (native is 0) | +0.0689 to +0.0873 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.466 | 1.66 | +13.2% | −0.0196 to +0.4066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.9 | 383.3 | −13.7% | −79.2413 to −41.9624 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.09 | 2.268 | +8.5% | −0.0219 to +0.3767 | no |
| pods started | 0.1111 | 1.111 | +900.0% | +0.1406 to +1.8594 | yes: power given |
| pod start wait, total (s) | 0.1111 | 2.778 | +2400.0% | +0.2057 to +5.1276 | yes: LOSS |
| pod start wait, mean (s) | 0.1111 | 1.389 | +1150.0% | +0.1720 to +2.3835 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46 | 48.54 | +5.5% | −2.9618 to +8.0390 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1478 | 841.9 | −43.1% | −733.6208 to −539.2680 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.875 | −52.1% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 155.4 | 0.4259 | −99.7% | −195.2327 to −114.7024 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 709.2 | 2.222 | −99.7% | −910.5937 to −503.4063 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 890.9 | 144.6 | −83.8% | −832.7567 to −659.8174 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.78 | 0 | −100.0% | −18.9842 to −6.5713 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 7 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.516 | −0.1% | −0.0196 to +0.0153 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 271.8 | −0.9% | −5.0716 to +0.2114 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 271.8 | −0.9% | −5.0716 to +0.2114 | no |
| response time (ms), mean | 443 | 122.5 | −72.3% | −488.5517 to −152.4266 | yes: GAIN |
| response time (ms), 95th percentile | 1638 | 263 | −83.9% | −2150.1156 to −599.0958 | yes: GAIN |
| response time (ms), 99th percentile | 2430 | 381.3 | −84.3% | −3188.3078 to −909.7248 | yes: GAIN |
| time over the response line (% of samples) | 22.79 | 0.3344 | −98.5% | −35.6765 to −9.2272 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.14 | 0.2857 | −97.4% | −15.8785 to −5.8358 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118 | +118.000 (native is 0) | +101.9895 to +134.0105 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 1370 | +12547.6% | +1075.6663 to +1642.3861 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0637 | 0.05847 | −8.2% | −0.0131 to +0.0027 | no |
| CPU used (cores), mean | 1.529 | 1.403 | −8.2% | −0.3152 to +0.0640 | no |
| Omni's own CPU (cores), mean | 0 | 0.07397 | +0.074 (native is 0) | +0.0635 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.529 | 1.477 | −3.4% | −0.2310 to +0.1278 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.8 | 462.3 | +6.6% | −28.0624 to +85.1270 | no |
| HPA replicas, mean | 1.973 | 2.326 | +17.9% | +0.0607 to +0.6445 | yes: power given |
| pods started | 0.1429 | 1.714 | +1100.0% | −0.2673 to +3.4101 | no |
| pod start wait, total (s) | 0.2857 | 3.714 | +1200.0% | −1.4613 to +8.3184 | no |
| pod start wait, mean (s) | 0.2857 | 1.329 | +365.0% | −0.4426 to +2.5283 | no |
| host CPU busy, the real machine under kind (%) | 43.68 | 47.07 | +7.7% | −0.2384 to +7.0084 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 803 | 1480 | +84.3% | +618.9748 to +735.3109 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05357 | 207 | +386300.0% | +143.3065 to +270.5864 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5714 | 860.7 | +150525.0% | +609.8841 to +1110.4017 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 109.2 | 963 | +781.6% | +735.1803 to +972.3435 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.71 | +14.714 (native is 0) | +7.9238 to +21.5047 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*