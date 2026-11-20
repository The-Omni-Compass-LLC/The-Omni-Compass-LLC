# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.35 | 6.193 |
| node-hours | 5.035 | 5.029 | 4.341 | 2.596 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 504.7 | 527.4 | 504.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 504.7 | 475.3 | 322.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 568.2 | 114.1 | 688.3 | 67.93 |
| response time (ms), 95th percentile | 2163 | 157.1 | 2841 | 88.61 |
| response time (ms), 99th percentile | 2986 | 179.7 | 3911 | 115 |
| time over the response line (% of samples) | 21.31 | 0.00381 | 26.88 | 0 |
| failed requests (%) | 0 | 0 | 0.03158 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0 | 13.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 149.9 | 33.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 12.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.04 | 0 | 20.21 | 0.16 |
| utilisation (used / allocatable) | 0.03505 | 0.005949 | 0.04162 | 0.009378 |
| CPU used (cores), mean | 1.682 | 0.2855 | 1.704 | 0.2328 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05556 | 0.03088 |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2855 | 1.76 | 0.2637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 4305 | 671.2 | 3407 |
| HPA replicas, mean | 3.976 | 4.212 | 4.794 | 4.398 |
| pods started | 0.2 | 0.4 | 3.4 | 1.9 |
| pod start wait, total (s) | 0.4 | 0.5 | 9.9 | 3.2 |
| pod start wait, mean (s) | 0.4 | 0.4 | 1.855 | 1.107 |
| host CPU busy, the real machine under kind (%) | 51.23 | 15.06 | 57.47 | 17.67 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 864.5 | 1506 | 918.3 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.869 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1160 | 0.1083 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | 0.6 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 171 | 1160 | 223.3 | 1160 |
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
| worker nodes in service, mean | 12 | 6.193 | −48.4% | −5.9046 to −5.7094 | yes: GAIN |
| node-hours | 5.029 | 2.596 | −48.4% | −2.4790 to −2.3874 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 504.9 | +0.0% | −1.2009 to +1.6052 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 322.4 | −36.1% | −186.0928 to −178.5821 | yes: GAIN |
| response time (ms), mean | 114.1 | 67.93 | −40.5% | −56.8431 to −35.5637 | yes: GAIN |
| response time (ms), 95th percentile | 157.1 | 88.61 | −43.6% | −84.3765 to −52.5015 | yes: GAIN |
| response time (ms), 99th percentile | 179.7 | 115 | −36.0% | −76.1455 to −53.2429 | yes: GAIN |
| time over the response line (% of samples) | 0.00381 | 0 | −100.0% | −0.0124 to +0.0048 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.200 (native is 0) | +30.3032 to +36.0968 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.16 | +0.160 (native is 0) | −0.0450 to +0.3650 | no |
| utilisation (used / allocatable) | 0.005949 | 0.009378 | +57.6% | +0.0029 to +0.0040 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2855 | 0.2328 | −18.5% | −0.0606 to −0.0447 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03088 | +0.031 (native is 0) | +0.0269 to +0.0348 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2855 | 0.2637 | −7.6% | −0.0312 to −0.0125 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4305 | 3407 | −20.9% | −1042.8647 to −754.7528 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.212 | 4.398 | +4.4% | −0.0852 to +0.4586 | no |
| pods started | 0.4 | 1.9 | +375.0% | +0.3690 to +2.6310 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.2 | +540.0% | +0.2673 to +5.1327 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.107 | +176.7% | −0.1676 to +1.5809 | no |
| host CPU busy, the real machine under kind (%) | 15.06 | 17.67 | +17.3% | +1.8005 to +3.4055 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1507 | +0.1% | −3.8087 to +5.4087 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1160 | +0.1% | −3.8077 to +5.2410 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1476 | +0.0% | −3.9391 to +5.1391 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1160 | +0.1% | −3.8077 to +5.2410 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.035 | 5.029 | −0.1% | −0.0172 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 504.7 | −4.2% | −25.3623 to −18.7296 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 504.7 | −4.2% | −25.3623 to −18.7296 | yes: GAIN |
| response time (ms), mean | 568.2 | 114.1 | −79.9% | −766.0946 to −142.0871 | yes: GAIN |
| response time (ms), 95th percentile | 2163 | 157.1 | −92.7% | −3421.6271 to −589.6009 | yes: GAIN |
| response time (ms), 99th percentile | 2986 | 179.7 | −94.0% | −4743.9220 to −869.1938 | yes: GAIN |
| time over the response line (% of samples) | 21.31 | 0.00381 | −100.0% | −32.5393 to −10.0645 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0 | −100.0% | −16.5663 to −7.0337 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.04 | 0 | −100.0% | −22.0176 to −8.0590 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.005949 | −83.0% | −0.0324 to −0.0258 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.682 | 0.2855 | −83.0% | −1.5550 to −1.2388 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2855 | −83.0% | −1.5550 to −1.2388 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 4305 | +465.4% | +3146.4898 to +3941.4910 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.212 | +5.9% | +0.0140 to +0.4564 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −0.7564 to +0.9564 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | ±0.0% | −0.7540 to +0.7540 | no |
| host CPU busy, the real machine under kind (%) | 51.23 | 15.06 | −70.6% | −41.1358 to −31.1998 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.5 | 1506 | +74.2% | +535.1758 to +748.0242 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1160 | +1070284.6% | +1156.6175 to +1162.3325 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245866.7% | +1472.2449 to +1478.1551 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 171 | 1160 | +578.1% | +884.6479 to +1092.5187 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.35 | −13.8% | −3.0668 to −0.2428 | yes: GAIN |
| node-hours | 5.035 | 4.341 | −13.8% | −1.2842 to −0.1040 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 527.4 | +0.1% | −1.3081 to +2.5353 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 475.3 | −9.8% | −96.2060 to −6.7293 | yes: GAIN |
| response time (ms), mean | 568.2 | 688.3 | +21.1% | +40.2741 to +199.8888 | yes: LOSS |
| response time (ms), 95th percentile | 2163 | 2841 | +31.4% | +287.6898 to +1069.5762 | yes: LOSS |
| response time (ms), 99th percentile | 2986 | 3911 | +31.0% | +414.1416 to +1435.4716 | yes: LOSS |
| time over the response line (% of samples) | 21.31 | 26.88 | +26.1% | +2.2655 to +8.8734 | yes: LOSS |
| failed requests (%) | 0 | 0.03158 | +0.032 (native is 0) | −0.0082 to +0.0714 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 13.8 | +16.9% | +0.4548 to +3.5452 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 149.9 | +149.900 (native is 0) | +54.5863 to +245.2137 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.04 | 20.21 | +34.4% | +1.2154 to +9.1313 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.04162 | +18.7% | +0.0016 to +0.0115 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.682 | 1.704 | +1.3% | −0.0275 to +0.0707 | no |
| Omni's own CPU (cores), mean | 0 | 0.05556 | +0.056 (native is 0) | +0.0495 to +0.0616 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.682 | 1.76 | +4.6% | +0.0245 to +0.1298 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 671.2 | −11.9% | −151.7881 to −28.8639 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.794 | +20.6% | +0.3384 to +1.2972 | yes: power given |
| pods started | 0.2 | 3.4 | +1600.0% | +0.8444 to +5.5556 | yes: power given |
| pod start wait, total (s) | 0.4 | 9.9 | +2375.0% | +1.5687 to +17.4313 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.855 | +363.8% | +0.0914 to +2.8186 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.23 | 57.47 | +12.2% | +4.9532 to +7.5194 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.5 | 918.3 | +6.2% | +26.2283 to +81.3717 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.869 | −26.1% | −5.4491 to −0.8130 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.1083 | 0.0% | raw −0.0596 to +0.0596 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 171 | 223.3 | +30.6% | +29.0015 to +75.6402 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.35 | −13.8% | −3.0668 to −0.2428 | yes: GAIN |
| node-hours | 5.029 | 4.341 | −13.7% | −1.2860 to −0.0908 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 527.4 | +4.5% | +19.1913 to +26.1277 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 475.3 | −5.8% | −76.7990 to +17.9556 | no |
| response time (ms), mean | 114.1 | 688.3 | +503.1% | +190.4680 to +957.8765 | yes: LOSS |
| response time (ms), 95th percentile | 157.1 | 2841 | +1709.1% | +929.1509 to +4439.3431 | yes: LOSS |
| response time (ms), 99th percentile | 179.7 | 3911 | +2076.0% | +1307.0314 to +6155.6976 | yes: LOSS |
| time over the response line (% of samples) | 0.00381 | 26.88 | +705373.2% | +16.4818 to +37.2609 | yes: LOSS |
| failed requests (%) | 0 | 0.03158 | +0.032 (native is 0) | −0.0082 to +0.0714 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 13.8 | +13.800 (native is 0) | +9.6182 to +17.9818 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 149.9 | +149.900 (native is 0) | +54.5863 to +245.2137 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 20.21 | +20.212 (native is 0) | +10.3171 to +30.1062 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005949 | 0.04162 | +599.7% | +0.0320 to +0.0393 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2855 | 1.704 | +496.8% | +1.2245 to +1.6125 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05556 | +0.056 (native is 0) | +0.0495 to +0.0616 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2855 | 1.76 | +516.2% | +1.2757 to +1.6724 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4305 | 671.2 | −84.4% | −4081.6168 to −3187.0160 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.212 | 4.794 | +13.8% | +0.1794 to +0.9859 | yes: power given |
| pods started | 0.4 | 3.4 | +750.0% | +1.0051 to +4.9949 | yes: power given |
| pod start wait, total (s) | 0.5 | 9.9 | +1880.0% | +2.1115 to +16.6885 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.855 | +363.8% | +0.4612 to +2.4488 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.06 | 57.47 | +281.5% | +36.2475 to +48.5607 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 918.3 | −39.0% | −719.9041 to −455.6959 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.1083 | −100.0% | −1162.3301 to −1156.6199 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.6 | −100.0% | −1478.2122 to −1472.1878 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 223.3 | −80.7% | −1061.6228 to −810.9022 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.193 | −48.4% | −5.9046 to −5.7094 | yes: GAIN |
| node-hours | 5.035 | 2.596 | −48.4% | −2.4781 to −2.3996 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 504.9 | −4.1% | −24.4179 to −19.2698 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 322.4 | −38.8% | −206.2012 to −202.5656 | yes: GAIN |
| response time (ms), mean | 568.2 | 67.93 | −88.0% | −821.4484 to −179.1402 | yes: GAIN |
| response time (ms), 95th percentile | 2163 | 88.61 | −95.9% | −3499.8611 to −648.2449 | yes: GAIN |
| response time (ms), 99th percentile | 2986 | 115 | −96.1% | −4813.6786 to −928.8256 | yes: GAIN |
| time over the response line (% of samples) | 21.31 | 0 | −100.0% | −32.5461 to −10.0652 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0 | −100.0% | −16.5663 to −7.0337 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.200 (native is 0) | +30.3032 to +36.0968 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.04 | 0.16 | −98.9% | −21.7389 to −8.0178 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.009378 | −73.2% | −0.0286 to −0.0227 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.682 | 0.2328 | −86.2% | −1.6090 to −1.2902 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03088 | +0.031 (native is 0) | +0.0269 to +0.0348 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2637 | −84.3% | −1.5747 to −1.2627 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 3407 | +347.4% | +2261.1786 to +3029.1846 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.398 | +10.6% | +0.0644 to +0.7794 | yes: power given |
| pods started | 0.2 | 1.9 | +850.0% | +0.3491 to +3.0509 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.2 | +700.0% | +0.2143 to +5.3857 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.107 | +176.7% | −0.1932 to +1.6066 | no |
| host CPU busy, the real machine under kind (%) | 51.23 | 17.67 | −65.5% | −38.0302 to −29.0994 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.5 | 1507 | +74.3% | +538.0909 to +746.7091 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1160 | +1070946.2% | +1156.8687 to +1163.5146 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245966.7% | +1472.4653 to +1479.1347 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 171 | 1160 | +578.5% | +887.5457 to +1091.0543 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*