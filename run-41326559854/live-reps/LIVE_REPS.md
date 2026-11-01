# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.793 | 5.558 |
| node-hours | 2.516 | 2.517 | 2.429 | 2.33 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.7 | 275.4 | 275.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.7 | 268.9 | 261.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 520.4 | 435.3 | 476.4 | 434.5 |
| response time (ms), 95th percentile | 1960 | 1793 | 2027 | 2098 |
| response time (ms), 99th percentile | 2844 | 2972 | 2874 | 3238 |
| time over the response line (% of samples) | 24.78 | 18.53 | 24.37 | 18.47 |
| failed requests (%) | 0 | 0 | 0 | 0.01087 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 11.6 | 12.9 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 30.6 | 42.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.62 | 19.88 | 12.89 | 23.32 |
| utilisation (used / allocatable) | 0.06769 | 0.06819 | 0.0699 | 0.07492 |
| CPU used (cores), mean | 1.624 | 1.637 | 1.621 | 1.649 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01759 | 0.01847 |
| CPU used with Omni's own (cores), mean | 1.624 | 1.637 | 1.639 | 1.668 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.3 | 407.3 | 400.2 | 380.3 |
| HPA replicas, mean | 1.981 | 2.056 | 2.187 | 2.192 |
| pods started | 0.1 | 0 | 0.6 | 0.4 |
| pod start wait, total (s) | 0.2 | 0 | 1 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0 | 1 | 0.8 |
| host CPU busy, the real machine under kind (%) | 46.27 | 47.55 | 47.03 | 48.81 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 838.6 | 857.6 | 840.8 | 866.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.59 | 5.215 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.9167 | 0.1 | 0.9917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.9 | 0.6 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 143.2 | 169.7 | 145.3 | 179.3 |
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
| worker nodes in service, mean | 6 | 5.558 | −7.4% | −1.0622 to +0.1777 | no |
| node-hours | 2.517 | 2.33 | −7.4% | −0.4477 to +0.0736 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.9 | +0.1% | −0.4346 to +0.8093 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 261.9 | −5.0% | −33.5217 to +6.0339 | no |
| response time (ms), mean | 435.3 | 434.5 | −0.2% | −42.7704 to +41.1693 | no |
| response time (ms), 95th percentile | 1793 | 2098 | +17.0% | −62.3344 to +671.7164 | no |
| response time (ms), 99th percentile | 2972 | 3238 | +9.0% | −102.0717 to +634.4941 | no |
| time over the response line (% of samples) | 18.53 | 18.47 | −0.3% | −1.1293 to +1.0099 | no |
| failed requests (%) | 0 | 0.01087 | +0.011 (native is 0) | −0.0137 to +0.0355 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.5 | −0.9% | −0.8113 to +0.6113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.4 | +42.400 (native is 0) | +23.4531 to +61.3469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.88 | 23.32 | +17.3% | +0.6095 to +6.2672 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06819 | 0.07492 | +9.9% | −0.0017 to +0.0152 | no |
| CPU used (cores), mean | 1.637 | 1.649 | +0.8% | −0.0149 to +0.0398 | no |
| Omni's own CPU (cores), mean | 0 | 0.01847 | +0.018 (native is 0) | +0.0177 to +0.0192 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.637 | 1.668 | +1.9% | +0.0042 to +0.0576 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.3 | 380.3 | −6.6% | −58.0658 to +4.1617 | no |
| HPA replicas, mean | 2.056 | 2.192 | +6.6% | −0.0559 to +0.3263 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| host CPU busy, the real machine under kind (%) | 47.55 | 48.81 | +2.6% | +0.9585 to +1.5557 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 857.6 | 866.7 | +1.1% | +2.7875 to +15.4125 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.215 | −13.1% | −1.7780 to +0.2089 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9167 | 0.9917 | +8.2% | −0.0489 to +0.1989 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.3 | +21.1% | −0.3689 to +1.1689 | no |
| queue: job turnaround, submitted to done, mean (s) | 169.7 | 179.3 | +5.7% | +3.2161 to +16.0256 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.0% | −0.0062 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.7 | +0.1% | −0.3641 to +0.8214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.7 | +0.1% | −0.3641 to +0.8214 | no |
| response time (ms), mean | 520.4 | 435.3 | −16.4% | −128.7486 to −41.5243 | yes: GAIN |
| response time (ms), 95th percentile | 1960 | 1793 | −8.5% | −407.3935 to +75.1035 | no |
| response time (ms), 99th percentile | 2844 | 2972 | +4.5% | −70.7076 to +326.1730 | no |
| time over the response line (% of samples) | 24.78 | 18.53 | −25.2% | −8.6411 to −3.8490 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 11.6 | −7.2% | −1.9900 to +0.1900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.62 | 19.88 | +57.5% | +5.6444 to +8.8756 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06769 | 0.06819 | +0.8% | −0.0005 to +0.0015 | no |
| CPU used (cores), mean | 1.624 | 1.637 | +0.8% | −0.0113 to +0.0357 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.624 | 1.637 | +0.8% | −0.0113 to +0.0357 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.3 | 407.3 | −0.5% | −6.9000 to +2.7766 | no |
| HPA replicas, mean | 1.981 | 2.056 | +3.8% | −0.0263 to +0.1772 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 46.27 | 47.55 | +2.8% | +0.9853 to +1.5716 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.6 | 857.6 | +2.3% | +10.1105 to +27.8895 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.9167 | +816.7% | +0.6428 to +0.9906 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.9 | +111.1% | +0.5231 to +1.4769 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.2 | 169.7 | +18.5% | +14.9898 to +38.0268 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.793 | −3.5% | −0.4257 to +0.0108 | no |
| node-hours | 2.516 | 2.429 | −3.5% | −0.1755 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.4 | −0.0% | −0.6309 to +0.6165 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 268.9 | −2.4% | −13.1529 to +0.0760 | no |
| response time (ms), mean | 520.4 | 476.4 | −8.5% | −60.5119 to −27.5779 | yes: GAIN |
| response time (ms), 95th percentile | 1960 | 2027 | +3.5% | −69.5810 to +205.0030 | no |
| response time (ms), 99th percentile | 2844 | 2874 | +1.1% | −160.0977 to +219.8923 | no |
| time over the response line (% of samples) | 24.78 | 24.37 | −1.7% | −1.1491 to +0.3302 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 12.9 | +3.2% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 | +30.600 (native is 0) | +8.8430 to +52.3570 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.62 | 12.89 | +2.1% | −2.2965 to +2.8365 | no |
| utilisation (used / allocatable) | 0.06769 | 0.0699 | +3.3% | +0.0002 to +0.0043 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.624 | 1.621 | −0.2% | −0.0183 to +0.0114 | no |
| Omni's own CPU (cores), mean | 0 | 0.01759 | +0.018 (native is 0) | +0.0163 to +0.0189 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.624 | 1.639 | +0.9% | −0.0005 to +0.0287 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.3 | 400.2 | −2.2% | −17.6677 to −0.6409 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.981 | 2.187 | +10.4% | +0.0290 to +0.3830 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.0121 to +1.6121 | no |
| pod start wait, mean (s) | 0.2 | 1 | +400.0% | −0.0121 to +1.6121 | no |
| host CPU busy, the real machine under kind (%) | 46.27 | 47.03 | +1.6% | +0.5515 to +0.9629 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.6 | 840.8 | +0.3% | −2.8106 to +7.2106 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.59 | −6.8% | −0.8395 to +0.0190 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.1 | 0.0% | raw −0.0855 to +0.0855 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.6 | −33.3% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 143.2 | 145.3 | +1.5% | −2.8072 to +7.0489 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.793 | −3.5% | −0.4257 to +0.0108 | no |
| node-hours | 2.517 | 2.429 | −3.5% | −0.1823 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.4 | −0.1% | −0.7856 to +0.3139 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 268.9 | −2.5% | −13.7891 to +0.2548 | no |
| response time (ms), mean | 435.3 | 476.4 | +9.4% | +3.8231 to +78.3600 | yes: LOSS |
| response time (ms), 95th percentile | 1793 | 2027 | +13.0% | −43.4695 to +511.1815 | no |
| response time (ms), 99th percentile | 2972 | 2874 | −3.3% | −286.5010 to +90.8302 | no |
| time over the response line (% of samples) | 18.53 | 24.37 | +31.5% | +3.7884 to +7.8828 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.9 | +11.2% | −0.1717 to +2.7717 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 | +30.600 (native is 0) | +8.8430 to +52.3570 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.88 | 12.89 | −35.2% | −9.7403 to −4.2397 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06819 | 0.0699 | +2.5% | −0.0009 to +0.0043 | no |
| CPU used (cores), mean | 1.637 | 1.621 | −1.0% | −0.0353 to +0.0040 | no |
| Omni's own CPU (cores), mean | 0 | 0.01759 | +0.018 (native is 0) | +0.0163 to +0.0189 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.637 | 1.639 | +0.1% | −0.0177 to +0.0216 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.3 | 400.2 | −1.7% | −18.4978 to +4.3125 | no |
| HPA replicas, mean | 2.056 | 2.187 | +6.3% | −0.0210 to +0.2822 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | +0.3256 to +1.6744 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.3256 to +1.6744 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.55 | 47.03 | −1.1% | −0.8162 to −0.2263 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 857.6 | 840.8 | −2.0% | −25.1405 to −8.4595 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.59 | −6.8% | −0.8395 to +0.0190 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9167 | 0.1 | −89.1% | −1.0218 to −0.6115 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.6 | −68.4% | −1.8889 to −0.7111 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 169.7 | 145.3 | −14.4% | −34.9042 to −13.8708 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.558 | −7.4% | −1.0622 to +0.1777 | no |
| node-hours | 2.516 | 2.33 | −7.4% | −0.4437 to +0.0718 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.9 | +0.2% | −0.1570 to +0.9890 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 261.9 | −4.9% | −33.1175 to +6.0870 | no |
| response time (ms), mean | 520.4 | 434.5 | −16.5% | −117.5299 to −54.3442 | yes: GAIN |
| response time (ms), 95th percentile | 1960 | 2098 | +7.1% | −89.1526 to +366.2446 | no |
| response time (ms), 99th percentile | 2844 | 3238 | +13.9% | +66.9896 to +720.8982 | yes: LOSS |
| time over the response line (% of samples) | 24.78 | 18.47 | −25.4% | −8.5566 to −4.0528 | yes: GAIN |
| failed requests (%) | 0 | 0.01087 | +0.011 (native is 0) | −0.0137 to +0.0355 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 11.5 | −8.0% | −2.2158 to +0.2158 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.4 | +42.400 (native is 0) | +23.4531 to +61.3469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.62 | 23.32 | +84.8% | +6.9199 to +14.4768 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06769 | 0.07492 | +10.7% | −0.0009 to +0.0153 | no |
| CPU used (cores), mean | 1.624 | 1.649 | +1.5% | −0.0046 to +0.0539 | no |
| Omni's own CPU (cores), mean | 0 | 0.01847 | +0.018 (native is 0) | +0.0177 to +0.0192 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.624 | 1.668 | +2.7% | +0.0143 to +0.0719 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.3 | 380.3 | −7.1% | −57.8032 to −0.2243 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.981 | 2.192 | +10.6% | +0.0826 to +0.3387 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.4228 to +1.6228 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | −0.4228 to +1.6228 | no |
| host CPU busy, the real machine under kind (%) | 46.27 | 48.81 | +5.5% | +2.1400 to +2.9311 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.6 | 866.7 | +3.4% | +15.9167 to +40.2833 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.215 | −13.1% | −1.7780 to +0.2089 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.9917 | +891.7% | +0.6808 to +1.1025 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.3 | +155.6% | +0.3772 to +2.4228 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.2 | 179.3 | +25.2% | +22.3040 to +49.9544 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*