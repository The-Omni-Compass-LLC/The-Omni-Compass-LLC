# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.229 | 4.562 |
| node-hours | 2.512 | 2.518 | 2.194 | 1.915 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.9 | 273.9 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 273.9 | 249.7 | 229.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 416.1 | 394.3 | 401.2 | 378 |
| response time (ms), 95th percentile | 1528 | 1687 | 1658 | 1789 |
| response time (ms), 99th percentile | 2187 | 2302 | 2333 | 2446 |
| time over the response line (% of samples) | 17.77 | 13.22 | 17.55 | 13.13 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.7 | 9.8 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 154.7 | 121.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 8.333 | 58.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 14.16 | 14.81 | 17 |
| utilisation (used / allocatable) | 0.06279 | 0.06313 | 0.07411 | 0.08601 |
| CPU used (cores), mean | 1.507 | 1.515 | 1.516 | 1.518 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07586 | 0.07642 |
| CPU used with Omni's own (cores), mean | 1.507 | 1.515 | 1.591 | 1.594 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.9 | 442.7 | 397 | 358.6 |
| HPA replicas, mean | 1.917 | 2.042 | 2.387 | 2.199 |
| pods started | 0.2 | 0.1 | 1.5 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.2 | 2.8 | 0.6 |
| pod start wait, mean (s) | 0.4 | 0.2 | 1.467 | 0.35 |
| host CPU busy, the real machine under kind (%) | 43.44 | 43.58 | 46.62 | 46.88 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.6 | 816 | 821.4 | 827.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.785 | 3.915 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.3167 | 0.2583 | 0.5708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 | 1.6 | 2.4 |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 124.7 | 127.1 | 133.5 |
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
| worker nodes in service, mean | 6 | 4.562 | −24.0% | −2.4371 to −0.4394 | yes: GAIN |
| node-hours | 2.518 | 1.915 | −23.9% | −1.0193 to −0.1860 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.4 | +0.2% | −0.1328 to +1.0817 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 229.1 | −16.4% | −76.0351 to −13.6202 | yes: GAIN |
| response time (ms), mean | 394.3 | 378 | −4.1% | −29.3929 to −3.1584 | yes: GAIN |
| response time (ms), 95th percentile | 1687 | 1789 | +6.0% | +5.4896 to +198.4164 | yes: LOSS |
| response time (ms), 99th percentile | 2302 | 2446 | +6.3% | −50.7988 to +340.7250 | no |
| time over the response line (% of samples) | 13.22 | 13.13 | −0.6% | −0.4838 to +0.3131 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.1 | +5.2% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.2 | +121.200 (native is 0) | +60.8962 to +181.5038 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 17 | +20.0% | −0.7174 to +6.3874 | no |
| utilisation (used / allocatable) | 0.06313 | 0.08601 | +36.3% | +0.0075 to +0.0383 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.515 | 1.518 | +0.2% | −0.0235 to +0.0295 | no |
| Omni's own CPU (cores), mean | 0 | 0.07642 | +0.076 (native is 0) | +0.0702 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.515 | 1.594 | +5.2% | +0.0493 to +0.1096 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 358.6 | −19.0% | −140.3933 to −27.8582 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.042 | 2.199 | +7.7% | −0.0092 to +0.3235 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.8707 to +1.6707 | no |
| pod start wait, mean (s) | 0.2 | 0.35 | +75.0% | −0.6417 to +0.9417 | no |
| host CPU busy, the real machine under kind (%) | 43.58 | 46.88 | +7.6% | +2.7998 to +3.7933 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816 | 827.6 | +1.4% | +4.1266 to +19.0734 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.915 | −34.8% | −3.4283 to −0.7419 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3167 | 0.5708 | +80.3% | −0.2312 to +0.7395 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 2.4 | +60.0% | +0.1128 to +1.6872 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124.7 | 133.5 | +7.1% | +2.0996 to +15.5670 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.518 | +0.2% | −0.0008 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.9 | +0.3% | +0.1331 to +1.3940 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 273.9 | +0.3% | +0.1331 to +1.3940 | yes: power given |
| response time (ms), mean | 416.1 | 394.3 | −5.3% | −37.4906 to −6.2915 | yes: GAIN |
| response time (ms), 95th percentile | 1528 | 1687 | +10.4% | −15.5428 to +332.9258 | no |
| response time (ms), 99th percentile | 2187 | 2302 | +5.2% | −156.8713 to +386.1999 | no |
| time over the response line (% of samples) | 17.77 | 13.22 | −25.6% | −7.5284 to −1.5859 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.7 | −8.3% | −1.5294 to +0.1294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 14.16 | +9.9% | −0.5713 to +3.1313 | no |
| utilisation (used / allocatable) | 0.06279 | 0.06313 | +0.5% | −0.0007 to +0.0014 | no |
| CPU used (cores), mean | 1.507 | 1.515 | +0.5% | −0.0162 to +0.0324 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.507 | 1.515 | +0.5% | −0.0162 to +0.0324 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.9 | 442.7 | −0.7% | −11.9772 to +5.6348 | no |
| HPA replicas, mean | 1.917 | 2.042 | +6.5% | +0.0451 to +0.2057 | yes: power given |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.4 | 0.2 | −50.0% | −1.0121 to +0.6121 | no |
| pod start wait, mean (s) | 0.4 | 0.2 | −50.0% | −1.0121 to +0.6121 | no |
| host CPU busy, the real machine under kind (%) | 43.44 | 43.58 | +0.3% | −0.1803 to +0.4645 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 816 | +0.4% | −0.6911 to +7.4911 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.3167 | +72.7% | −0.0667 to +0.3334 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 | +7.1% | −1.3086 to +1.5086 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 124.7 | +6.4% | +1.0591 to +13.8575 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.229 | −12.8% | −1.5638 to +0.0226 | no |
| node-hours | 2.512 | 2.194 | −12.7% | −0.6500 to +0.0134 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.9 | +0.3% | +0.2530 to +1.2506 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 249.7 | −8.6% | −48.4777 to +1.5355 | no |
| response time (ms), mean | 416.1 | 401.2 | −3.6% | −34.5893 to +4.6625 | no |
| response time (ms), 95th percentile | 1528 | 1658 | +8.5% | −17.6184 to +277.6184 | no |
| response time (ms), 99th percentile | 2187 | 2333 | +6.7% | −3.9674 to +296.8296 | no |
| time over the response line (% of samples) | 17.77 | 17.55 | −1.3% | −0.8253 to +0.3735 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.8 | +16.7% | +0.1293 to +2.6707 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 | +154.700 (native is 0) | +62.6335 to +246.7665 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 14.81 | +15.0% | −0.9515 to +4.8082 | no |
| utilisation (used / allocatable) | 0.06279 | 0.07411 | +18.0% | −0.0006 to +0.0232 | no |
| CPU used (cores), mean | 1.507 | 1.516 | +0.6% | −0.0132 to +0.0305 | no |
| Omni's own CPU (cores), mean | 0 | 0.07586 | +0.076 (native is 0) | +0.0706 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.591 | +5.6% | +0.0628 to +0.1062 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.9 | 397 | −11.0% | −95.2034 to −2.5173 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.917 | 2.387 | +24.5% | +0.2538 to +0.6862 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.6214 to +1.9786 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.8 | +600.0% | +0.7412 to +4.0588 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.467 | +266.7% | +0.2675 to +1.8658 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.44 | 46.62 | +7.3% | +2.7991 to +3.5714 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 821.4 | +1.1% | −0.8841 to +18.4841 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 | −20.3% | −2.3188 to −0.1119 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.2583 | +40.9% | −0.0136 to +0.1636 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.6 | +14.3% | −0.5388 to +0.9388 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 127.1 | +8.4% | +0.2174 to +19.4492 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.229 | −12.8% | −1.5638 to +0.0226 | no |
| node-hours | 2.518 | 2.194 | −12.8% | −0.6557 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.9 | −0.0% | −0.6260 to +0.6025 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 249.7 | −8.8% | −49.2874 to +0.8180 | no |
| response time (ms), mean | 394.3 | 401.2 | +1.8% | −13.7961 to +27.6515 | no |
| response time (ms), 95th percentile | 1687 | 1658 | −1.7% | −172.2056 to +114.8226 | no |
| response time (ms), 99th percentile | 2302 | 2333 | +1.4% | −220.3125 to +283.8461 | no |
| time over the response line (% of samples) | 13.22 | 17.55 | +32.8% | +1.9012 to +6.7613 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 9.8 | +27.3% | +0.3658 to +3.8342 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 | +154.700 (native is 0) | +62.6335 to +246.7665 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 14.81 | +4.6% | −1.9901 to +3.2868 | no |
| utilisation (used / allocatable) | 0.06313 | 0.07411 | +17.4% | −0.0008 to +0.0228 | no |
| CPU used (cores), mean | 1.515 | 1.516 | +0.0% | −0.0268 to +0.0278 | no |
| Omni's own CPU (cores), mean | 0 | 0.07586 | +0.076 (native is 0) | +0.0706 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.515 | 1.591 | +5.0% | +0.0471 to +0.1057 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 397 | −10.3% | −91.3609 to −0.0175 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.042 | 2.387 | +16.9% | +0.1444 to +0.5448 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.7968 to +2.0032 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | +1.2854 to +3.9146 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.467 | +633.3% | +0.6875 to +1.8458 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.58 | 46.62 | +7.0% | +2.7172 to +3.3692 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816 | 821.4 | +0.7% | −1.2694 to +12.0694 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 | −20.3% | −2.3188 to −0.1119 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3167 | 0.2583 | −18.4% | −0.2253 to +0.1086 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.6 | +6.7% | −0.6113 to +0.8113 | no |
| queue: job turnaround, submitted to done, mean (s) | 124.7 | 127.1 | +1.9% | −3.2970 to +8.0470 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.562 | −24.0% | −2.4371 to −0.4394 | yes: GAIN |
| node-hours | 2.512 | 1.915 | −23.8% | −1.0140 to −0.1811 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 274.4 | +0.5% | +0.4854 to +1.9906 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 229.1 | −16.1% | −75.0807 to −13.0474 | yes: GAIN |
| response time (ms), mean | 416.1 | 378 | −9.2% | −50.7285 to −25.6049 | yes: GAIN |
| response time (ms), 95th percentile | 1528 | 1789 | +17.1% | +23.6052 to +497.6838 | yes: LOSS |
| response time (ms), 99th percentile | 2187 | 2446 | +11.9% | +8.9562 to +510.2986 | yes: LOSS |
| time over the response line (% of samples) | 17.77 | 13.13 | −26.1% | −7.7806 to −1.5043 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.1 | −3.6% | −1.1953 to +0.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.2 | +121.200 (native is 0) | +60.8962 to +181.5038 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 17 | +31.9% | +0.5456 to +7.6844 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06279 | 0.08601 | +37.0% | +0.0075 to +0.0390 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.507 | 1.518 | +0.7% | −0.0087 to +0.0309 | no |
| Omni's own CPU (cores), mean | 0 | 0.07642 | +0.076 (native is 0) | +0.0702 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.594 | +5.8% | +0.0673 to +0.1078 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.9 | 358.6 | −19.6% | −146.3930 to −28.2010 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.917 | 2.199 | +14.7% | +0.1494 to +0.4158 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −1.0972 to +1.4972 | no |
| pod start wait, mean (s) | 0.4 | 0.35 | −12.5% | −0.8488 to +0.7488 | no |
| host CPU busy, the real machine under kind (%) | 43.44 | 46.88 | +7.9% | +2.9292 to +3.9481 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 827.6 | +1.8% | +4.8728 to +25.1272 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.915 | −34.8% | −3.4283 to −0.7419 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.5708 | +211.4% | −0.2219 to +0.9969 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 2.4 | +71.4% | −0.8469 to +2.8469 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 133.5 | +13.9% | +4.0090 to +28.5744 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*