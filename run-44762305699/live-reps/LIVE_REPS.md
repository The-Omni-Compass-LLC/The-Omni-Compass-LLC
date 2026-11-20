# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.3 | 6.184 |
| node-hours | 5.018 | 5.025 | 4.317 | 2.591 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 504.4 | 525.9 | 504.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 504.4 | 472.4 | 322 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 570.8 | 121.9 | 655.7 | 70.39 |
| response time (ms), 95th percentile | 2169 | 167.5 | 2675 | 90.09 |
| response time (ms), 99th percentile | 2998 | 198.1 | 3643 | 114.8 |
| time over the response line (% of samples) | 21.15 | 0.003846 | 24.34 | 0.00361 |
| failed requests (%) | 0 | 0 | 0.025 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 0 | 12.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 154.2 | 33.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 36.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.83 | 0.025 | 23.03 | 0.05167 |
| utilisation (used / allocatable) | 0.0342 | 0.006052 | 0.0398 | 0.009728 |
| CPU used (cores), mean | 1.641 | 0.2905 | 1.633 | 0.2409 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05604 | 0.03122 |
| CPU used with Omni's own (cores), mean | 1.641 | 0.2905 | 1.689 | 0.2721 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 4201 | 704.5 | 3254 |
| HPA replicas, mean | 4.077 | 4.184 | 4.687 | 4.584 |
| pods started | 0.1 | 0.5 | 2.6 | 2.2 |
| pod start wait, total (s) | 0.3 | 0.6 | 7.1 | 3.8 |
| pod start wait, mean (s) | 0.3 | 0.6 | 2.45 | 1.3 |
| host CPU busy, the real machine under kind (%) | 50.54 | 15.45 | 56.02 | 18.05 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 862.7 | 1507 | 900.8 | 1506 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.131 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1160 | 0.09167 | 1159 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | 0.4 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 170.4 | 1160 | 206.7 | 1159 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.184 | −48.5% | −5.8885 to −5.7437 | yes: GAIN |
| node-hours | 5.025 | 2.591 | −48.4% | −2.4674 to −2.4011 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 504.8 | +0.1% | −0.9154 to +1.7389 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 322 | −36.2% | −185.0706 to −179.6435 | yes: GAIN |
| response time (ms), mean | 121.9 | 70.39 | −42.2% | −62.4723 to −40.5274 | yes: GAIN |
| response time (ms), 95th percentile | 167.5 | 90.09 | −46.2% | −94.2225 to −60.5355 | yes: GAIN |
| response time (ms), 99th percentile | 198.1 | 114.8 | −42.1% | −100.8779 to −65.8477 | yes: GAIN |
| time over the response line (% of samples) | 0.003846 | 0.00361 | −6.1% | −0.0008 to +0.0003 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.6 | +33.600 (native is 0) | +29.6216 to +37.5784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.05167 | +106.7% | −0.0770 to +0.1303 | no |
| utilisation (used / allocatable) | 0.006052 | 0.009728 | +60.7% | +0.0032 to +0.0042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2905 | 0.2409 | −17.1% | −0.0555 to −0.0438 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03122 | +0.031 (native is 0) | +0.0280 to +0.0345 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2905 | 0.2721 | −6.3% | −0.0256 to −0.0113 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4201 | 3254 | −22.5% | −1038.4269 to −856.1531 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.184 | 4.584 | +9.5% | −0.0429 to +0.8413 | no |
| pods started | 0.5 | 2.2 | +340.0% | +0.3919 to +3.0081 | yes: power given |
| pod start wait, total (s) | 0.6 | 3.8 | +533.3% | +0.6143 to +5.7857 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.3 | +116.7% | −0.0215 to +1.4215 | no |
| host CPU busy, the real machine under kind (%) | 15.45 | 18.05 | +16.8% | +1.9498 to +3.2422 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1506 | −0.1% | −5.1177 to +3.3177 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1159 | −0.1% | −5.0052 to +3.1385 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1476 | −0.1% | −4.8436 to +3.2436 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1159 | −0.1% | −5.0052 to +3.1385 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.018 | 5.025 | +0.1% | −0.0036 to +0.0176 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 504.4 | −3.8% | −23.3088 to −16.5319 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 504.4 | −3.8% | −23.3088 to −16.5319 | yes: GAIN |
| response time (ms), mean | 570.8 | 121.9 | −78.6% | −760.1562 to −137.5805 | yes: GAIN |
| response time (ms), 95th percentile | 2169 | 167.5 | −92.3% | −3426.4154 to −576.3366 | yes: GAIN |
| response time (ms), 99th percentile | 2998 | 198.1 | −93.4% | −4764.6944 to −835.4444 | yes: GAIN |
| time over the response line (% of samples) | 21.15 | 0.003846 | −100.0% | −32.3172 to −9.9722 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 0 | −100.0% | −16.5810 to −6.6190 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.83 | 0.025 | −99.8% | −22.4514 to −9.1586 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0342 | 0.006052 | −82.3% | −0.0324 to −0.0238 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.641 | 0.2905 | −82.3% | −1.5573 to −1.1445 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.641 | 0.2905 | −82.3% | −1.5573 to −1.1445 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 4201 | +431.4% | +3142.4271 to +3679.0686 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.077 | 4.184 | +2.6% | −0.0546 to +0.2698 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.4578 to +1.0578 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.4578 to +1.0578 | no |
| host CPU busy, the real machine under kind (%) | 50.54 | 15.45 | −69.4% | −41.3673 to −28.8063 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 862.7 | 1507 | +74.7% | +537.8743 to +750.7257 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1160 | +1326090.5% | +1158.0752 to +1162.5831 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245983.3% | +1473.7291 to +1478.0709 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 170.4 | 1160 | +581.0% | +885.1936 to +1094.8398 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.3 | −14.2% | −3.3084 to −0.0943 | yes: GAIN |
| node-hours | 5.018 | 4.317 | −14.0% | −1.3707 to −0.0315 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 525.9 | +0.3% | −0.1394 to +3.3811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 472.4 | −9.9% | −102.3669 to −1.4580 | yes: GAIN |
| response time (ms), mean | 570.8 | 655.7 | +14.9% | −3.7656 to +173.6864 | no |
| response time (ms), 95th percentile | 2169 | 2675 | +23.3% | +113.4088 to +899.2482 | yes: LOSS |
| response time (ms), 99th percentile | 2998 | 3643 | +21.5% | +140.0063 to +1148.9357 | yes: LOSS |
| time over the response line (% of samples) | 21.15 | 24.34 | +15.1% | +1.5236 to +4.8610 | yes: LOSS |
| failed requests (%) | 0 | 0.025 | +0.025 (native is 0) | −0.0315 to +0.0815 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.6 | +8.6% | −0.0663 to +2.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.2 | +154.200 (native is 0) | +56.6062 to +251.7938 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.83 | 23.03 | +45.5% | −7.5672 to +21.9706 | no |
| utilisation (used / allocatable) | 0.0342 | 0.0398 | +16.4% | +0.0008 to +0.0104 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.641 | 1.633 | −0.5% | −0.0811 to +0.0636 | no |
| Omni's own CPU (cores), mean | 0 | 0.05604 | +0.056 (native is 0) | +0.0507 to +0.0614 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.641 | 1.689 | +2.9% | −0.0268 to +0.1214 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 704.5 | −10.9% | −161.1652 to −11.0852 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.077 | 4.687 | +15.0% | +0.3101 to +0.9106 | yes: power given |
| pods started | 0.1 | 2.6 | +2500.0% | +1.3198 to +3.6802 | yes: power given |
| pod start wait, total (s) | 0.3 | 7.1 | +2266.7% | +3.3978 to +10.2022 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.45 | +716.7% | +1.2624 to +3.0376 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.54 | 56.02 | +10.8% | +4.4052 to +6.5450 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 862.7 | 900.8 | +4.4% | +9.0236 to +67.1764 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.131 | −23.9% | −5.2306 to −0.5067 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.09167 | +4.8% | −0.0874 to +0.0957 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 170.4 | 206.7 | +21.3% | +10.7045 to +61.8621 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.3 | −14.2% | −3.3084 to −0.0943 | yes: GAIN |
| node-hours | 5.025 | 4.317 | −14.1% | −1.3776 to −0.0387 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 525.9 | +4.3% | +17.5734 to +25.5091 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 472.4 | −6.3% | −85.2745 to +21.2903 | no |
| response time (ms), mean | 121.9 | 655.7 | +437.9% | +139.3954 to +928.2622 | yes: LOSS |
| response time (ms), 95th percentile | 167.5 | 2675 | +1497.4% | +740.0252 to +4275.3838 | yes: LOSS |
| response time (ms), 99th percentile | 198.1 | 3643 | +1738.4% | +1062.7191 to +5826.3617 | yes: LOSS |
| time over the response line (% of samples) | 0.003846 | 24.34 | +632761.1% | +12.7477 to +35.9262 | yes: LOSS |
| failed requests (%) | 0 | 0.025 | +0.025 (native is 0) | −0.0315 to +0.0815 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.6 | +12.600 (native is 0) | +7.4839 to +17.7161 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.2 | +154.200 (native is 0) | +56.6062 to +251.7938 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 23.03 | +92026.7% | +5.1210 to +40.8924 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006052 | 0.0398 | +557.5% | +0.0306 to +0.0369 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2905 | 1.633 | +462.0% | +1.0860 to +1.5984 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05604 | +0.056 (native is 0) | +0.0507 to +0.0614 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2905 | 1.689 | +481.3% | +1.1388 to +1.6577 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4201 | 704.5 | −83.2% | −3831.5221 to −3162.2240 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.184 | 4.687 | +12.0% | +0.1827 to +0.8228 | yes: power given |
| pods started | 0.5 | 2.6 | +420.0% | +1.0100 to +3.1900 | yes: power given |
| pod start wait, total (s) | 0.6 | 7.1 | +1083.3% | +3.0903 to +9.9097 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.45 | +308.3% | +1.2729 to +2.4271 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.45 | 56.02 | +262.5% | +33.3849 to +47.7389 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 900.8 | −40.2% | −741.2905 to −471.1095 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.09167 | −100.0% | −1162.5871 to −1158.0629 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.4 | −100.0% | −1478.4712 to −1473.7288 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 206.7 | −82.2% | −1083.3153 to −824.1513 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.184 | −48.5% | −5.8885 to −5.7437 | yes: GAIN |
| node-hours | 5.018 | 2.591 | −48.4% | −2.4622 to −2.3923 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 504.8 | −3.7% | −22.3253 to −16.6920 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 322 | −38.6% | −205.2840 to −199.2708 | yes: GAIN |
| response time (ms), mean | 570.8 | 70.39 | −87.7% | −821.0509 to −179.6856 | yes: GAIN |
| response time (ms), 95th percentile | 2169 | 90.09 | −95.8% | −3515.6175 to −641.8925 | yes: GAIN |
| response time (ms), 99th percentile | 2998 | 114.8 | −96.2% | −4862.5971 to −904.2673 | yes: GAIN |
| time over the response line (% of samples) | 21.15 | 0.00361 | −100.0% | −32.3176 to −9.9723 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 0 | −100.0% | −16.5810 to −6.6190 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.6 | +33.600 (native is 0) | +29.6216 to +37.5784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.83 | 0.05167 | −99.7% | −22.4345 to −9.1221 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0342 | 0.009728 | −71.6% | −0.0283 to −0.0206 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.641 | 0.2409 | −85.3% | −1.6056 to −1.1956 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03122 | +0.031 (native is 0) | +0.0280 to +0.0345 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.641 | 0.2721 | −83.4% | −1.5713 to −1.1675 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 3254 | +311.6% | +2228.3271 to +2698.5886 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.077 | 4.584 | +12.4% | +0.0906 to +0.9230 | yes: power given |
| pods started | 0.1 | 2.2 | +2100.0% | +0.7746 to +3.4254 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.8 | +1166.7% | +0.6738 to +6.3262 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.3 | +333.3% | +0.0446 to +1.9554 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.54 | 18.05 | −64.3% | −38.2414 to −26.7402 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 862.7 | 1506 | +74.6% | +538.0113 to +748.7887 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1159 | +1325023.8% | +1156.5741 to +1162.2176 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245850.0% | +1472.2298 to +1477.9702 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 170.4 | 1159 | +580.4% | +885.3308 to +1092.8358 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*