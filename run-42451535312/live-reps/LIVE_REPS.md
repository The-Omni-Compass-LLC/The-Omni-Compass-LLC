# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.082 | 9.57 |
| node-hours | 5.024 | 5.032 | 3.804 | 4.015 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.2 | 525.4 | 523.9 | 525.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.2 | 525.4 | 432.2 | 449.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 409 | 532.2 | 415.4 | 572.9 |
| response time (ms), 95th percentile | 1416 | 2113 | 1634 | 2379 |
| response time (ms), 99th percentile | 1868 | 3075 | 2202 | 3614 |
| time over the response line (% of samples) | 15.27 | 18.55 | 17.94 | 19.92 |
| failed requests (%) | 0.02326 | 0.06944 | 0.007692 | 0.1319 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 13.44 | 10.9 | 12.44 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 152.1 | 58.78 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 32.61 | 67.59 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.09 | 22.74 | 15.77 | 21.18 |
| utilisation (used / allocatable) | 0.03175 | 0.03343 | 0.04257 | 0.04215 |
| CPU used (cores), mean | 1.524 | 1.604 | 1.522 | 1.575 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05122 | 0.03621 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.604 | 1.573 | 1.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 835 | 795.1 | 680.2 | 681.6 |
| HPA replicas, mean | 4.022 | 4.054 | 4.446 | 4.495 |
| pods started | 0.3 | 0 | 1.9 | 1.556 |
| pod start wait, total (s) | 0.6 | 0 | 4.2 | 4.778 |
| pod start wait, mean (s) | 0.4 | 0 | 1.95 | 1.87 |
| host CPU busy, the real machine under kind (%) | 47.62 | 53.33 | 51.6 | 57.14 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.5 | 892.4 | 823.7 | 921.8 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 6.933 | 7.986 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1.931 | 0.09167 | 7.782 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2 | 0.4 | 71.22 |
| queue: job turnaround, submitted to done, mean (s) | 123.8 | 201.7 | 133.4 | 224.1 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.976 | −16.9% | −3.9784 to −0.0693 | yes: GAIN |
| node-hours | 5.03 | 4.186 | −16.8% | −1.6624 to −0.0256 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.1 | +0.2% | −0.5077 to +2.3029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 462.5 | −11.9% | −124.5890 to −0.8450 | yes: GAIN |
| response time (ms), mean | 556.9 | 633.7 | +13.8% | +11.0153 to +142.6562 | yes: LOSS |
| response time (ms), 95th percentile | 2233 | 2646 | +18.5% | +138.4443 to +688.1307 | yes: LOSS |
| response time (ms), 99th percentile | 3183 | 4022 | +26.3% | +220.7362 to +1455.5288 | yes: LOSS |
| time over the response line (% of samples) | 18.77 | 22.37 | +19.2% | +0.7978 to +6.4169 | yes: LOSS |
| failed requests (%) | 0.07812 | 0.1484 | +90.0% | −0.0571 to +0.1977 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.38 | 14 | +4.7% | +0.1922 to +1.0578 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54 | +54.000 (native is 0) | +34.0922 to +73.9078 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.27 | 23.04 | −5.1% | −15.0665 to +12.6040 | no |
| utilisation (used / allocatable) | 0.03353 | 0.04141 | +23.5% | +0.0010 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.609 | 1.619 | +0.6% | −0.0519 to +0.0723 | no |
| Omni's own CPU (cores), mean | 0 | 0.03757 | +0.038 (native is 0) | +0.0276 to +0.0475 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.609 | 1.657 | +3.0% | −0.0174 to +0.1129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 794.6 | 682.9 | −14.1% | −197.9695 to −25.3445 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.056 | 4.572 | +12.7% | −0.1311 to +1.1629 | no |
| pods started | 0 | 1.75 | +1.750 (native is 0) | +0.2846 to +3.2154 | yes: power given |
| pod start wait, total (s) | 0 | 5.375 | +5.375 (native is 0) | +1.2802 to +9.4698 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.104 | +2.104 (native is 0) | +0.5378 to +3.6706 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.61 | 58.74 | +9.6% | +3.5357 to +6.7382 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 899.4 | 946.1 | +5.2% | +21.4878 to +72.0122 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.473 | −29.4% | −6.5249 to −0.5282 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 2.141 | 8.745 | +308.5% | −3.4742 to +16.6826 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.125 | 80 | +3664.7% | −42.4377 to +198.1877 | no |
| queue: job turnaround, submitted to done, mean (s) | 208.4 | 248.1 | +19.0% | +14.2381 to +65.1264 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.023 | 5.032 | +0.2% | −0.0080 to +0.0250 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.5 | 525.4 | +0.4% | −0.1502 to +3.8548 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.5 | 525.4 | +0.4% | −0.1502 to +3.8548 | no |
| response time (ms), mean | 443.5 | 532.2 | +20.0% | +10.9096 to +166.5388 | yes: LOSS |
| response time (ms), 95th percentile | 1552 | 2113 | +36.2% | −31.4453 to +1153.5842 | no |
| response time (ms), 99th percentile | 2040 | 3075 | +50.8% | +386.1924 to +1684.5196 | yes: LOSS |
| time over the response line (% of samples) | 16.97 | 18.55 | +9.3% | −1.6299 to +4.7883 | no |
| failed requests (%) | 0.02584 | 0.06944 | +168.8% | −0.0569 to +0.1442 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.67 | 13.44 | +26.0% | +0.6805 to +4.8750 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.22 | 22.74 | +18.3% | −21.9851 to +29.0110 | no |
| utilisation (used / allocatable) | 0.0323 | 0.03343 | +3.5% | −0.0011 to +0.0034 | no |
| CPU used (cores), mean | 1.55 | 1.604 | +3.5% | −0.0547 to +0.1633 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.55 | 1.604 | +3.5% | −0.0547 to +0.1633 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 820.7 | 795.1 | −3.1% | −60.8428 to +9.6595 | no |
| HPA replicas, mean | 4.042 | 4.054 | +0.3% | −0.3023 to +0.3264 | no |
| pods started | 0.3333 | 0 | −100.0% | −0.8769 to +0.2102 | no |
| pod start wait, total (s) | 0.6667 | 0 | −100.0% | −1.7537 to +0.4204 | no |
| pod start wait, mean (s) | 0.4444 | 0 | −100.0% | −1.1223 to +0.2335 | no |
| host CPU busy, the real machine under kind (%) | 48.62 | 53.33 | +9.7% | +3.8891 to +5.5398 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.4 | 892.4 | +8.5% | +34.6560 to +105.3440 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1343 | 1.931 | +1337.9% | −1.8421 to +5.4347 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2 | +100.0% | −0.8027 to +2.8027 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.2 | 201.7 | +50.3% | +35.4590 to +99.5318 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.082 | −24.3% | −4.3844 to −1.4524 | yes: GAIN |
| node-hours | 5.024 | 3.804 | −24.3% | −1.8366 to −0.6026 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.2 | 523.9 | +0.1% | −1.4977 to +2.9122 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.2 | 432.2 | −17.4% | −137.7111 to −44.3701 | yes: GAIN |
| response time (ms), mean | 409 | 415.4 | +1.6% | −6.2317 to +19.0241 | no |
| response time (ms), 95th percentile | 1416 | 1634 | +15.4% | +51.1596 to +385.8244 | yes: LOSS |
| response time (ms), 99th percentile | 1868 | 2202 | +17.9% | +33.9564 to +634.4798 | yes: LOSS |
| time over the response line (% of samples) | 15.27 | 17.94 | +17.5% | +0.2200 to +5.1244 | yes: LOSS |
| failed requests (%) | 0.02326 | 0.007692 | −66.9% | −0.0508 to +0.0196 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.9 | +13.5% | −0.0081 to +2.6081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 152.1 | +152.100 (native is 0) | +81.3497 to +222.8503 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.09 | 15.77 | −12.8% | −22.4843 to +17.8443 | no |
| utilisation (used / allocatable) | 0.03175 | 0.04257 | +34.1% | +0.0049 to +0.0168 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.522 | −0.1% | −0.0986 to +0.0944 | no |
| Omni's own CPU (cores), mean | 0 | 0.05122 | +0.051 (native is 0) | +0.0456 to +0.0568 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.573 | +3.2% | −0.0489 to +0.1471 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 835 | 680.2 | −18.5% | −237.8886 to −71.7193 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.022 | 4.446 | +10.5% | +0.1318 to +0.7153 | yes: power given |
| pods started | 0.3 | 1.9 | +533.3% | +0.9089 to +2.2911 | yes: power given |
| pod start wait, total (s) | 0.6 | 4.2 | +600.0% | +1.4356 to +5.7644 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.95 | +387.5% | +0.4645 to +2.6355 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.62 | 51.6 | +8.3% | +3.4500 to +4.4982 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 823.7 | +1.4% | +0.3215 to +22.0785 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 6.933 | −42.2% | −7.1610 to −2.9728 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.09167 | −24.1% | −0.2166 to +0.1583 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.4 | −55.6% | −1.5796 to +0.5796 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.8 | 133.4 | +7.8% | −4.7314 to +23.9314 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.388 | −21.8% | −4.0855 to −1.1395 | yes: GAIN |
| node-hours | 5.032 | 3.931 | −21.9% | −1.7134 to −0.4875 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 524.2 | −0.2% | −2.3126 to −0.0658 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 442.1 | −15.9% | −129.2460 to −37.3129 | yes: GAIN |
| response time (ms), mean | 532.2 | 450.6 | −15.3% | −158.2575 to −4.9656 | yes: GAIN |
| response time (ms), 95th percentile | 2113 | 1781 | −15.7% | −758.8321 to +95.4154 | no |
| response time (ms), 99th percentile | 3075 | 2388 | −22.3% | −1090.4818 to −283.9980 | yes: GAIN |
| time over the response line (% of samples) | 18.55 | 19.79 | +6.7% | −2.0032 to +4.4907 | no |
| failed requests (%) | 0.06944 | 0.008547 | −87.7% | −0.2013 to +0.0795 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.44 | 11.89 | −11.6% | −2.5057 to −0.6055 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137.2 | +137.222 (native is 0) | +66.2893 to +208.1552 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.74 | 17.29 | −24.0% | −11.4527 to +0.5527 | no |
| utilisation (used / allocatable) | 0.03343 | 0.04198 | +25.6% | +0.0027 to +0.0144 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.604 | 1.556 | −3.0% | −0.0716 to −0.0247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05124 | +0.051 (native is 0) | +0.0449 to +0.0576 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.604 | 1.608 | +0.2% | −0.0227 to +0.0288 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.1 | 681 | −14.3% | −191.0707 to −37.0734 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.054 | 4.492 | +10.8% | +0.1466 to +0.7295 | yes: power given |
| pods started | 0 | 2.111 | +2.111 (native is 0) | +1.6492 to +2.5730 | yes: power given |
| pod start wait, total (s) | 0 | 4.667 | +4.667 (native is 0) | +3.0361 to +6.2973 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.167 | +2.167 (native is 0) | +1.4738 to +2.8595 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.33 | 52.53 | −1.5% | −1.4349 to −0.1629 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 892.4 | 834.8 | −6.5% | −87.9779 to −27.3555 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 7.252 | −39.6% | −6.9881 to −2.5072 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.931 | 0.1019 | −94.7% | −5.3539 to +1.6965 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 0.4444 | −77.8% | −2.9993 to −0.1118 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 201.7 | 144.3 | −28.5% | −88.4949 to −26.3939 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.57 | −20.2% | −4.3540 to −0.5059 | yes: GAIN |
| node-hours | 5.025 | 4.015 | −20.1% | −1.8186 to −0.2008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.4 | 525.5 | +0.4% | +0.2377 to +4.0460 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.4 | 449.1 | −14.2% | −135.7072 to −12.8007 | yes: GAIN |
| response time (ms), mean | 422 | 572.9 | +35.8% | +18.8092 to +282.9892 | yes: LOSS |
| response time (ms), 95th percentile | 1469 | 2379 | +61.9% | +250.6017 to +1568.4705 | yes: LOSS |
| response time (ms), 99th percentile | 1944 | 3614 | +85.9% | +688.8050 to +2651.3799 | yes: LOSS |
| time over the response line (% of samples) | 14.92 | 19.92 | +33.5% | +1.7768 to +8.2162 | yes: LOSS |
| failed requests (%) | 0.02584 | 0.1319 | +410.6% | −0.0568 to +0.2690 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.222 | 12.44 | +34.9% | +1.0557 to +5.3888 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.78 | +58.778 (native is 0) | +38.4198 to +79.1358 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.46 | 21.18 | +8.9% | −14.4972 to +17.9454 | no |
| utilisation (used / allocatable) | 0.03172 | 0.04215 | +32.9% | +0.0036 to +0.0173 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.523 | 1.575 | +3.4% | −0.0606 to +0.1645 | no |
| Omni's own CPU (cores), mean | 0 | 0.03621 | +0.036 (native is 0) | +0.0271 to +0.0453 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.523 | 1.611 | +5.8% | −0.0276 to +0.2039 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 837.5 | 681.6 | −18.6% | −247.7275 to −64.0628 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.989 | 4.495 | +12.7% | −0.0589 to +1.0723 | no |
| pods started | 0.3333 | 1.556 | +366.7% | −0.0968 to +2.5412 | no |
| pod start wait, total (s) | 0.6667 | 4.778 | +616.7% | +0.7289 to +7.4933 | yes: LOSS |
| pod start wait, mean (s) | 0.4444 | 1.87 | +320.8% | +0.2617 to +2.5902 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.73 | 57.14 | +19.7% | +7.0883 to +11.7439 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.9 | 921.8 | +12.7% | +42.4467 to +165.3311 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.986 | −33.5% | −6.8274 to −1.2013 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 7.782 | +6125.9% | −3.8505 to +19.1653 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8889 | 71.22 | +7912.5% | −35.8665 to +176.5332 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.8 | 224.1 | +74.0% | +36.4230 to +154.1974 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*