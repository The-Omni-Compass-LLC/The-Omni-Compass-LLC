# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.851 | 10.75 |
| node-hours | 5.034 | 5.026 | 4.131 | 4.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 523.6 | 525.3 | 526.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 523.6 | 457.8 | 487.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 487.8 | 661.1 | 566.2 | 846.4 |
| response time (ms), 95th percentile | 1846 | 2275 | 2270 | 2990 |
| response time (ms), 99th percentile | 2388 | 2995 | 2917 | 4117 |
| time over the response line (% of samples) | 17.31 | 26.83 | 21.38 | 34.38 |
| failed requests (%) | 0 | 0.09865 | 0.008368 | 0.04751 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 12.1 | 11.2 | 15.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 144.4 | 115.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 47.67 | 27.94 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 52.06 | 23.04 | 53.25 |
| utilisation (used / allocatable) | 0.03244 | 0.03193 | 0.04085 | 0.03883 |
| CPU used (cores), mean | 1.557 | 1.532 | 1.588 | 1.669 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05166 | 0.05348 |
| CPU used with Omni's own (cores), mean | 1.557 | 1.532 | 1.639 | 1.722 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 823.6 | 827.3 | 697.4 | 703 |
| HPA replicas, mean | 3.982 | 4.004 | 4.764 | 4.67 |
| pods started | 0.1 | 0.3 | 3.1 | 2.9 |
| pod start wait, total (s) | 0.2 | 0.7 | 8.6 | 8.3 |
| pod start wait, mean (s) | 0.2 | 0.7 | 1.848 | 2.268 |
| host CPU busy, the real machine under kind (%) | 48.49 | 54.39 | 54.09 | 61.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 836.4 | 921.3 | 875.8 | 1004 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.29 | 9.377 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 3.425 | 0.0875 | 15.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 14.4 | 0.4 | 75.8 |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 220.3 | 182.1 | 286.2 |
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
| worker nodes in service, mean | 12 | 10.75 | −10.4% | −2.1997 to −0.3037 | yes: GAIN |
| node-hours | 5.026 | 4.51 | −10.3% | −0.9162 to −0.1161 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 526.5 | +0.6% | +0.3870 to +5.4231 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 487.2 | −7.0% | −67.1203 to −5.6904 | yes: GAIN |
| response time (ms), mean | 661.1 | 846.4 | +28.0% | +105.8613 to +264.8317 | yes: LOSS |
| response time (ms), 95th percentile | 2275 | 2990 | +31.4% | +264.2098 to +1164.9102 | yes: LOSS |
| response time (ms), 99th percentile | 2995 | 4117 | +37.5% | +495.5753 to +1747.8001 | yes: LOSS |
| time over the response line (% of samples) | 26.83 | 34.38 | +28.1% | +2.3307 to +12.7732 | yes: LOSS |
| failed requests (%) | 0.09865 | 0.04751 | −51.8% | −0.2174 to +0.1151 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 15.2 | +25.6% | +0.4567 to +5.7433 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.2 | +115.200 (native is 0) | +64.1995 to +166.2005 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 52.06 | 53.25 | +2.3% | −21.4261 to +23.8061 | no |
| utilisation (used / allocatable) | 0.03193 | 0.03883 | +21.6% | +0.0039 to +0.0099 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.669 | +8.9% | +0.0441 to +0.2284 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05348 | +0.053 (native is 0) | +0.0472 to +0.0598 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.722 | +12.4% | +0.0975 to +0.2820 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827.3 | 703 | −15.0% | −181.5984 to −67.1045 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.004 | 4.67 | +16.6% | +0.2440 to +1.0865 | yes: power given |
| pods started | 0.3 | 2.9 | +866.7% | +0.7779 to +4.4221 | yes: power given |
| pod start wait, total (s) | 0.7 | 8.3 | +1085.7% | +2.2984 to +12.9016 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.268 | +224.0% | +0.4069 to +2.7288 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 61.8 | +13.6% | +6.3001 to +8.5167 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 921.3 | 1004 | +9.0% | +49.5834 to +115.6166 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.377 | −21.9% | −4.2725 to −0.9728 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.425 | 15.7 | +358.5% | −6.4588 to +31.0171 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 14.4 | 75.8 | +426.4% | −27.3033 to +150.1033 | no |
| queue: job turnaround, submitted to done, mean (s) | 220.3 | 286.2 | +29.9% | +26.8661 to +105.0339 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.034 | 5.026 | −0.2% | −0.0179 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 523.6 | −0.2% | −2.9798 to +0.6485 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 523.6 | −0.2% | −2.9798 to +0.6485 | no |
| response time (ms), mean | 487.8 | 661.1 | +35.5% | +35.7817 to +310.7778 | yes: LOSS |
| response time (ms), 95th percentile | 1846 | 2275 | +23.3% | +66.2188 to +793.5022 | yes: LOSS |
| response time (ms), 99th percentile | 2388 | 2995 | +25.4% | +115.0669 to +1098.6319 | yes: LOSS |
| time over the response line (% of samples) | 17.31 | 26.83 | +55.0% | +4.1240 to +14.9149 | yes: LOSS |
| failed requests (%) | 0 | 0.09865 | +0.099 (native is 0) | −0.1245 to +0.3218 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 12.1 | +28.7% | +0.4367 to +4.9633 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 52.06 | +192.0% | −11.2958 to +79.7624 | no |
| utilisation (used / allocatable) | 0.03244 | 0.03193 | −1.6% | −0.0030 to +0.0019 | no |
| CPU used (cores), mean | 1.557 | 1.532 | −1.6% | −0.1426 to +0.0929 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.557 | 1.532 | −1.6% | −0.1426 to +0.0929 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 823.6 | 827.3 | +0.4% | −46.6760 to +54.0865 | no |
| HPA replicas, mean | 3.982 | 4.004 | +0.6% | −0.1996 to +0.2435 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −0.5256 to +1.5256 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.5256 to +1.5256 | no |
| host CPU busy, the real machine under kind (%) | 48.49 | 54.39 | +12.2% | +3.9884 to +7.8096 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.4 | 921.3 | +10.2% | +26.5028 to +143.2972 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 3.425 | +2734.5% | −1.5783 to +8.1867 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 14.4 | +2780.0% | −15.2876 to +43.0876 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 220.3 | +51.2% | +18.4511 to +130.7905 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.851 | −17.9% | −3.7888 to −0.5100 | yes: GAIN |
| node-hours | 5.034 | 4.131 | −17.9% | −1.5947 to −0.2114 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 525.3 | +0.1% | −1.7551 to +2.7002 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 457.8 | −12.8% | −119.6273 to −14.2860 | yes: GAIN |
| response time (ms), mean | 487.8 | 566.2 | +16.1% | −4.0289 to +160.8529 | no |
| response time (ms), 95th percentile | 1846 | 2270 | +23.0% | +68.2849 to +780.8711 | yes: LOSS |
| response time (ms), 99th percentile | 2388 | 2917 | +22.2% | +104.6030 to +953.5106 | yes: LOSS |
| time over the response line (% of samples) | 17.31 | 21.38 | +23.5% | +1.2899 to +6.8471 | yes: LOSS |
| failed requests (%) | 0 | 0.008368 | +0.008 (native is 0) | −0.0106 to +0.0273 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 11.2 | +19.1% | −0.3539 to +3.9539 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.4 | +144.400 (native is 0) | +75.5881 to +213.2119 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 23.04 | +29.3% | +0.6630 to +9.7670 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03244 | 0.04085 | +25.9% | +0.0032 to +0.0137 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.557 | 1.588 | +1.9% | −0.0398 to +0.1005 | no |
| Omni's own CPU (cores), mean | 0 | 0.05166 | +0.052 (native is 0) | +0.0449 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.557 | 1.639 | +5.3% | +0.0062 to +0.1578 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 823.6 | 697.4 | −15.3% | −200.0878 to −52.4232 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.982 | 4.764 | +19.6% | +0.3143 to +1.2485 | yes: power given |
| pods started | 0.1 | 3.1 | +3000.0% | +0.9768 to +5.0232 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.6 | +4200.0% | +1.9649 to +14.8351 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.848 | +824.0% | +0.6337 to +2.6623 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.49 | 54.09 | +11.6% | +4.1593 to +7.0454 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.4 | 875.8 | +4.7% | +5.9200 to +72.8800 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.29 | −30.9% | −6.1435 to −1.2768 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.0875 | −27.6% | −0.0700 to +0.0033 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 182.1 | +25.0% | +6.9216 to +65.8617 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.851 | −17.9% | −3.7888 to −0.5100 | yes: GAIN |
| node-hours | 5.026 | 4.131 | −17.8% | −1.5847 to −0.2054 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 525.3 | +0.3% | −0.7468 to +4.0232 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 457.8 | −12.6% | −118.8423 to −12.7396 | yes: GAIN |
| response time (ms), mean | 661.1 | 566.2 | −14.4% | −161.8526 to −27.8829 | yes: GAIN |
| response time (ms), 95th percentile | 2275 | 2270 | −0.2% | −232.3336 to +221.7686 | no |
| response time (ms), 99th percentile | 2995 | 2917 | −2.6% | −363.6504 to +208.0652 | no |
| time over the response line (% of samples) | 26.83 | 21.38 | −20.3% | −9.1354 to −1.7666 | yes: GAIN |
| failed requests (%) | 0.09865 | 0.008368 | −91.5% | −0.2945 to +0.1139 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 11.2 | −7.4% | −1.6113 to −0.1887 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.4 | +144.400 (native is 0) | +75.5881 to +213.2119 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 52.06 | 23.04 | −55.7% | −71.0258 to +12.9892 | no |
| utilisation (used / allocatable) | 0.03193 | 0.04085 | +28.0% | +0.0040 to +0.0138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.588 | +3.6% | −0.1075 to +0.2179 | no |
| Omni's own CPU (cores), mean | 0 | 0.05166 | +0.052 (native is 0) | +0.0449 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.639 | +7.0% | −0.0616 to +0.2753 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827.3 | 697.4 | −15.7% | −196.4322 to −63.4893 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.004 | 4.764 | +19.0% | +0.2631 to +1.2557 | yes: power given |
| pods started | 0.3 | 3.1 | +933.3% | +0.8688 to +4.7312 | yes: power given |
| pod start wait, total (s) | 0.7 | 8.6 | +1128.6% | +1.6509 to +14.1491 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 1.848 | +164.0% | +0.1352 to +2.1608 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 54.09 | −0.5% | −1.0152 to +0.4219 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 921.3 | 875.8 | −4.9% | −71.8841 to −19.1159 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.29 | −30.9% | −6.1435 to −1.2768 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.425 | 0.0875 | −97.4% | −8.2380 to +1.5630 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 14.4 | 0.4 | −97.2% | −43.1614 to +15.1614 | no |
| queue: job turnaround, submitted to done, mean (s) | 220.3 | 182.1 | −17.4% | −66.0967 to −10.3616 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.75 | −10.4% | −2.1997 to −0.3037 | yes: GAIN |
| node-hours | 5.034 | 4.51 | −10.4% | −0.9253 to −0.1230 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 526.5 | +0.3% | −0.8043 to +4.2830 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 487.2 | −7.2% | −67.8496 to −7.2924 | yes: GAIN |
| response time (ms), mean | 487.8 | 846.4 | +73.5% | +182.4896 to +534.7629 | yes: LOSS |
| response time (ms), 95th percentile | 1846 | 2990 | +62.0% | +577.5717 to +1711.2693 | yes: LOSS |
| response time (ms), 99th percentile | 2388 | 4117 | +72.4% | +921.1699 to +2535.9043 | yes: LOSS |
| time over the response line (% of samples) | 17.31 | 34.38 | +98.6% | +9.6187 to +24.5242 | yes: LOSS |
| failed requests (%) | 0 | 0.04751 | +0.048 (native is 0) | −0.0266 to +0.1217 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 15.2 | +61.7% | +2.7132 to +8.8868 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.2 | +115.200 (native is 0) | +64.1995 to +166.2005 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 53.25 | +198.7% | −10.3102 to +81.1569 | no |
| utilisation (used / allocatable) | 0.03244 | 0.03883 | +19.7% | +0.0021 to +0.0107 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.557 | 1.669 | +7.2% | −0.0064 to +0.2292 | no |
| Omni's own CPU (cores), mean | 0 | 0.05348 | +0.053 (native is 0) | +0.0472 to +0.0598 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.557 | 1.722 | +10.6% | +0.0518 to +0.2780 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 823.6 | 703 | −14.6% | −207.2269 to −34.0655 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.982 | 4.67 | +17.3% | +0.2254 to +1.1491 | yes: power given |
| pods started | 0.1 | 2.9 | +2800.0% | +1.2256 to +4.3744 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.3 | +4050.0% | +3.1967 to +13.0033 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.268 | +1033.9% | +1.1196 to +3.0161 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.49 | 61.8 | +27.4% | +11.2090 to +15.4058 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.4 | 1004 | +20.0% | +96.3013 to +238.6987 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.377 | −21.9% | −4.2725 to −0.9728 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 15.7 | +12896.6% | −6.3252 to +37.4919 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 75.8 | +15060.0% | −22.4895 to +173.0895 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 286.2 | +96.5% | +81.2645 to +199.8771 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*