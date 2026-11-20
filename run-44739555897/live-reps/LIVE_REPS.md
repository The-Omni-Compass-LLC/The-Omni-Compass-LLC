# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.03 | 6.514 |
| node-hours | 5.027 | 5.025 | 4.619 | 2.732 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 504.5 | 526.5 | 505.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 504.5 | 495.9 | 332.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 691.7 | 136.1 | 765.8 | 79.77 |
| response time (ms), 95th percentile | 2662 | 184.8 | 3154 | 102.6 |
| response time (ms), 99th percentile | 3561 | 207 | 4345 | 147.6 |
| time over the response line (% of samples) | 27.44 | 0.004282 | 31.97 | 0.004055 |
| failed requests (%) | 0 | 0 | 0.0239 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15 | 0 | 15.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 89.6 | 34.44 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 94.44 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.35 | 0.02963 | 29.46 | 0.05926 |
| utilisation (used / allocatable) | 0.03602 | 0.00637 | 0.03896 | 0.01011 |
| CPU used (cores), mean | 1.729 | 0.3058 | 1.722 | 0.2626 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05536 | 0.03231 |
| CPU used with Omni's own (cores), mean | 1.729 | 0.3058 | 1.778 | 0.2949 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.2 | 3981 | 691.5 | 3047 |
| HPA replicas, mean | 3.998 | 4.225 | 4.758 | 4.739 |
| pods started | 0.1 | 0.4444 | 3.4 | 3.111 |
| pod start wait, total (s) | 0.4 | 0.5556 | 8 | 4.556 |
| pod start wait, mean (s) | 0.4 | 0.5556 | 2.246 | 1.267 |
| host CPU busy, the real machine under kind (%) | 53.69 | 16.16 | 59.38 | 19.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 898.3 | 1505 | 946.2 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.823 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1158 | 0.1667 | 1161 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1474 | 0.8 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 210.9 | 1158 | 253.7 | 1161 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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
| worker nodes in service, mean | 12 | 6.514 | −45.7% | −6.1737 to −4.7990 | yes: GAIN |
| node-hours | 5.025 | 2.732 | −45.6% | −2.5829 to −2.0038 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 505.5 | +0.2% | +0.5224 to +1.5244 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 332.9 | −34.0% | −193.3595 to −149.7650 | yes: GAIN |
| response time (ms), mean | 136.1 | 79.77 | −41.4% | −62.1933 to −50.4863 | yes: GAIN |
| response time (ms), 95th percentile | 184.8 | 102.6 | −44.5% | −87.6714 to −76.8219 | yes: GAIN |
| response time (ms), 99th percentile | 207 | 147.6 | −28.7% | −80.2402 to −38.5536 | yes: GAIN |
| time over the response line (% of samples) | 0.004282 | 0.004055 | −5.3% | −0.0007 to +0.0003 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.44 | +34.444 (native is 0) | +31.6700 to +37.2189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02963 | 0.05926 | +100.0% | −0.1306 to +0.1899 | no |
| utilisation (used / allocatable) | 0.00637 | 0.01011 | +58.7% | +0.0033 to +0.0042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3058 | 0.2626 | −14.1% | −0.0565 to −0.0298 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03231 | +0.032 (native is 0) | +0.0289 to +0.0357 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3058 | 0.2949 | −3.5% | −0.0235 to +0.0019 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3981 | 3047 | −23.5% | −1088.9516 to −778.7048 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.225 | 4.739 | +12.2% | +0.1687 to +0.8590 | yes: power given |
| pods started | 0.4444 | 3.111 | +600.0% | +0.8235 to +4.5099 | yes: power given |
| pod start wait, total (s) | 0.5556 | 4.556 | +720.0% | +0.6057 to +7.3943 | yes: LOSS |
| pod start wait, mean (s) | 0.5556 | 1.267 | +128.0% | −0.2470 to +1.6692 | no |
| host CPU busy, the real machine under kind (%) | 16.16 | 19.06 | +18.0% | +2.3818 to +3.4289 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1507 | +0.2% | +1.3335 to +3.7777 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1161 | +0.2% | +1.4913 to +3.8420 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 1477 | +0.2% | +1.7846 to +4.2154 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1161 | +0.2% | +1.4913 to +3.8420 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.025 | 5.025 | 0.0% | raw −0.0115 to +0.0115 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 504.5 | −4.3% | −25.0013 to −19.8443 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 504.5 | −4.3% | −25.0013 to −19.8443 | yes: GAIN |
| response time (ms), mean | 739.1 | 136.1 | −81.6% | −940.0860 to −265.8616 | yes: GAIN |
| response time (ms), 95th percentile | 2866 | 184.8 | −93.6% | −4189.5719 to −1173.4459 | yes: GAIN |
| response time (ms), 99th percentile | 3838 | 207 | −94.6% | −5663.4973 to −1598.3511 | yes: GAIN |
| time over the response line (% of samples) | 28.85 | 0.004282 | −100.0% | −37.6086 to −20.0832 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.33 | 0 | −100.0% | −17.3670 to −13.2996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.61 | 0.02963 | −99.8% | −28.9347 to −10.2283 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03657 | 0.00637 | −82.6% | −0.0335 to −0.0269 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.755 | 0.3058 | −82.6% | −1.6088 to −1.2900 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.755 | 0.3058 | −82.6% | −1.6088 to −1.2900 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.3 | 3981 | +446.6% | +2992.2177 to +3513.3774 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.987 | 4.225 | +6.0% | +0.0796 to +0.3963 | yes: power given |
| pods started | 0.1111 | 0.4444 | +300.0% | −0.0510 to +0.7177 | no |
| pod start wait, total (s) | 0.4444 | 0.5556 | +25.0% | −0.9375 to +1.1597 | no |
| pod start wait, mean (s) | 0.4444 | 0.5556 | +25.0% | −0.9375 to +1.1597 | no |
| host CPU busy, the real machine under kind (%) | 54.54 | 16.16 | −70.4% | −43.3317 to −33.4292 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 915.1 | 1505 | +64.4% | +469.3888 to +709.9446 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1204 | 1158 | +961957.7% | +1156.9231 to +1158.9009 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7778 | 1474 | +189428.6% | +1472.3165 to +1474.3502 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 227.2 | 1158 | +409.6% | +813.9971 to +1047.6048 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −1.5747 to −0.3685 | yes: GAIN |
| node-hours | 5.027 | 4.619 | −8.1% | −0.6603 to −0.1563 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 526.5 | −0.0% | −1.4326 to +0.9627 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 495.9 | −5.8% | −49.1854 to −12.3304 | yes: GAIN |
| response time (ms), mean | 691.7 | 765.8 | +10.7% | +22.7449 to +125.5490 | yes: LOSS |
| response time (ms), 95th percentile | 2662 | 3154 | +18.5% | +242.6897 to +740.7373 | yes: LOSS |
| response time (ms), 99th percentile | 3561 | 4345 | +22.0% | +407.0870 to +1160.1406 | yes: LOSS |
| time over the response line (% of samples) | 27.44 | 31.97 | +16.5% | +2.1420 to +6.9167 | yes: LOSS |
| failed requests (%) | 0 | 0.0239 | +0.024 (native is 0) | −0.0302 to +0.0780 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15 | 15.9 | +6.0% | +0.3722 to +1.4278 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +53.3904 to +125.8096 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.35 | 29.46 | +60.6% | −2.3183 to +24.5416 | no |
| utilisation (used / allocatable) | 0.03602 | 0.03896 | +8.2% | +0.0003 to +0.0056 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.729 | 1.722 | −0.4% | −0.0472 to +0.0346 | no |
| Omni's own CPU (cores), mean | 0 | 0.05536 | +0.055 (native is 0) | +0.0503 to +0.0604 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.729 | 1.778 | +2.8% | +0.0110 to +0.0871 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.2 | 691.5 | −6.5% | −89.8495 to −5.5394 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.998 | 4.758 | +19.0% | +0.3388 to +1.1809 | yes: power given |
| pods started | 0.1 | 3.4 | +3300.0% | +1.7529 to +4.8471 | yes: power given |
| pod start wait, total (s) | 0.4 | 8 | +1900.0% | +3.2529 to +11.9471 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 2.246 | +461.5% | +0.6910 to +3.0007 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.69 | 59.38 | +10.6% | +4.5530 to +6.8221 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 898.3 | 946.2 | +5.3% | +26.7868 to +69.0132 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.823 | −18.1% | −3.4042 to −0.9503 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1667 | +37.9% | −0.0354 to +0.1271 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 210.9 | 253.7 | +20.3% | +21.9802 to +63.6531 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.11 | −7.4% | −1.5482 to −0.2360 | yes: GAIN |
| node-hours | 5.025 | 4.652 | −7.4% | −0.6464 to −0.1002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 526.7 | +4.4% | +20.2718 to +24.1268 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 498.7 | −1.2% | −28.1508 to +16.4984 | no |
| response time (ms), mean | 136.1 | 811.3 | +496.0% | +284.2999 to +1066.0388 | yes: LOSS |
| response time (ms), 95th percentile | 184.8 | 3350 | +1712.7% | +1404.8228 to +4926.2272 | yes: LOSS |
| response time (ms), 99th percentile | 207 | 4617 | +2130.2% | +1985.1183 to +6834.9586 | yes: LOSS |
| time over the response line (% of samples) | 0.004282 | 32.6 | +761172.8% | +23.9232 to +41.2596 | yes: LOSS |
| failed requests (%) | 0 | 0.02656 | +0.027 (native is 0) | −0.0347 to +0.0878 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 16.11 | +16.111 (native is 0) | +13.6973 to +18.5249 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89 | +89.000 (native is 0) | +47.7580 to +130.2420 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02963 | 31.67 | +106781.2% | +8.5838 to +54.6940 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.00637 | 0.0391 | +513.9% | +0.0317 to +0.0338 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3058 | 1.741 | +469.4% | +1.3081 to +1.5625 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05596 | +0.056 (native is 0) | +0.0504 to +0.0615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3058 | 1.797 | +487.7% | +1.3591 to +1.6234 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3981 | 687.9 | −82.7% | −3594.3444 to −2991.9703 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.225 | 4.805 | +13.7% | +0.1722 to +0.9875 | yes: power given |
| pods started | 0.4444 | 3.667 | +725.0% | +1.5130 to +4.9314 | yes: power given |
| pod start wait, total (s) | 0.5556 | 8.778 | +1480.0% | +3.9463 to +12.4981 | yes: LOSS |
| pod start wait, mean (s) | 0.5556 | 2.384 | +329.2% | +1.0714 to +2.5860 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 16.16 | 60.12 | +272.1% | +37.8883 to +50.0293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 962.1 | −36.1% | −685.6598 to −399.6735 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.1759 | −100.0% | −1158.8260 to −1156.8870 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 0.7778 | −99.9% | −1474.3502 to −1472.3165 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 269.6 | −76.7% | −1026.7248 to −750.2196 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.514 | −45.7% | −6.1737 to −4.7990 | yes: GAIN |
| node-hours | 5.025 | 2.732 | −45.6% | −2.5842 to −2.0025 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 505.5 | −4.1% | −23.9109 to −18.8880 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 332.9 | −36.8% | −214.6836 to −173.2866 | yes: GAIN |
| response time (ms), mean | 739.1 | 79.77 | −89.2% | −1001.4997 to −317.1275 | yes: GAIN |
| response time (ms), 95th percentile | 2866 | 102.6 | −96.4% | −4270.3722 to −1257.1389 | yes: GAIN |
| response time (ms), 99th percentile | 3838 | 147.6 | −96.2% | −5716.2501 to −1664.3921 | yes: GAIN |
| time over the response line (% of samples) | 28.85 | 0.004055 | −100.0% | −37.6090 to −20.0832 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.33 | 0 | −100.0% | −17.3670 to −13.2996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.44 | +34.444 (native is 0) | +31.6700 to +37.2189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.61 | 0.05926 | −99.7% | −28.9280 to −10.1757 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03657 | 0.01011 | −72.3% | −0.0299 to −0.0230 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.755 | 0.2626 | −85.0% | −1.6521 to −1.3330 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03231 | +0.032 (native is 0) | +0.0289 to +0.0357 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.755 | 0.2949 | −83.2% | −1.6166 to −1.3038 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.3 | 3047 | +318.4% | +2178.7634 to +2459.1753 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.987 | 4.739 | +18.9% | +0.3545 to +1.1490 | yes: power given |
| pods started | 0.1111 | 3.111 | +2700.0% | +1.2812 to +4.7188 | yes: power given |
| pod start wait, total (s) | 0.4444 | 4.556 | +925.0% | +0.6426 to +7.5796 | yes: LOSS |
| pod start wait, mean (s) | 0.4444 | 1.267 | +185.0% | −0.3716 to +2.0160 | no |
| host CPU busy, the real machine under kind (%) | 54.54 | 19.06 | −65.0% | −39.9784 to −30.9718 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 915.1 | 1507 | +64.7% | +471.9623 to +712.4822 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1204 | 1161 | +964173.1% | +1159.6359 to +1161.5215 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7778 | 1477 | +189814.3% | +1475.2463 to +1477.4204 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 227.2 | 1161 | +410.8% | +816.8097 to +1050.1255 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*