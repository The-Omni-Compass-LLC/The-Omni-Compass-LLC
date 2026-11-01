# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.59 | 10.83 |
| node-hours | 5.025 | 5.028 | 4.439 | 4.541 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.7 | 527.9 | 526.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.7 | 483.4 | 489.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 760.6 | 988.3 | 752.8 | 901 |
| response time (ms), 95th percentile | 3079 | 4122 | 3191 | 3801 |
| response time (ms), 99th percentile | 4102 | 5452 | 4355 | 5132 |
| time over the response line (% of samples) | 25.11 | 28.61 | 25.16 | 31.27 |
| failed requests (%) | 0 | 0.08697 | 0.007491 | 0.1501 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 16.1 | 12.4 | 16.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 61.7 | 30.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.7 | 32.82 | 21.7 | 82.25 |
| utilisation (used / allocatable) | 0.03703 | 0.03741 | 0.04167 | 0.03841 |
| CPU used (cores), mean | 1.777 | 1.796 | 1.753 | 1.651 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01345 | 0.01034 |
| CPU used with Omni's own (cores), mean | 1.777 | 1.796 | 1.766 | 1.661 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 726 | 666.4 | 715.9 |
| HPA replicas, mean | 4.043 | 4.056 | 4.194 | 4.452 |
| pods started | 0.2 | 0.2 | 0.4 | 0.6 |
| pod start wait, total (s) | 0.2 | 0.2 | 0.5 | 1.4 |
| pod start wait, mean (s) | 0.1 | 0.1 | 0.5 | 1.4 |
| host CPU busy, the real machine under kind (%) | 54.16 | 60.68 | 55.66 | 62.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 928.7 | 1046 | 944.5 | 1061 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.658 | 10.04 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 6.05 | 0.1417 | 14.01 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 34.6 | 0.6 | 128.6 |
| queue: job turnaround, submitted to done, mean (s) | 234.8 | 348 | 243.3 | 364.7 |
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
| worker nodes in service, mean | 12 | 10.83 | −9.7% | −2.5372 to +0.2015 | no |
| node-hours | 5.028 | 4.541 | −9.7% | −1.0621 to +0.0888 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 526.1 | −0.3% | −4.3885 to +1.1181 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 489.5 | −7.3% | −80.9941 to +4.4279 | no |
| response time (ms), mean | 988.3 | 901 | −8.8% | −212.3159 to +37.6611 | no |
| response time (ms), 95th percentile | 4122 | 3801 | −7.8% | −947.7831 to +304.3821 | no |
| response time (ms), 99th percentile | 5452 | 5132 | −5.9% | −904.3627 to +263.9763 | no |
| time over the response line (% of samples) | 28.61 | 31.27 | +9.3% | −0.5621 to +5.9008 | no |
| failed requests (%) | 0.08697 | 0.1501 | +72.5% | −0.0739 to +0.2001 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 16.3 | +1.2% | −0.6121 to +1.0121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.500 (native is 0) | +25.9478 to +35.0522 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.82 | 82.25 | +150.6% | +2.0265 to +96.8368 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03741 | 0.03841 | +2.7% | −0.0055 to +0.0075 | no |
| CPU used (cores), mean | 1.796 | 1.651 | −8.1% | −0.3099 to +0.0195 | no |
| Omni's own CPU (cores), mean | 0 | 0.01034 | +0.010 (native is 0) | +0.0090 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.796 | 1.661 | −7.5% | −0.2993 to +0.0296 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726 | 715.9 | −1.4% | −110.2139 to +90.0646 | no |
| HPA replicas, mean | 4.056 | 4.452 | +9.8% | +0.1491 to +0.6443 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | −0.0064 to +2.4064 | no |
| pod start wait, mean (s) | 0.1 | 1.4 | +1300.0% | +0.2310 to +2.3690 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.68 | 62.28 | +2.6% | +0.7419 to +2.4620 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1046 | 1061 | +1.5% | −0.9156 to +32.3156 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.04 | −16.3% | −4.1576 to +0.2373 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 6.05 | 14.01 | +131.5% | −1.1545 to +17.0711 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.6 | 128.6 | +271.7% | −13.9522 to +201.9522 | no |
| queue: job turnaround, submitted to done, mean (s) | 348 | 364.7 | +4.8% | −0.1888 to +33.4221 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.025 | 5.028 | +0.1% | −0.0202 to +0.0255 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.7 | +0.1% | −2.4253 to +3.6072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.7 | +0.1% | −2.4253 to +3.6072 | no |
| response time (ms), mean | 760.6 | 988.3 | +29.9% | +77.9278 to +377.6428 | yes: LOSS |
| response time (ms), 95th percentile | 3079 | 4122 | +33.9% | +374.0447 to +1713.2753 | yes: LOSS |
| response time (ms), 99th percentile | 4102 | 5452 | +32.9% | +679.4876 to +2020.0620 | yes: LOSS |
| time over the response line (% of samples) | 25.11 | 28.61 | +13.9% | +1.5422 to +5.4399 | yes: LOSS |
| failed requests (%) | 0 | 0.08697 | +0.087 (native is 0) | −0.0054 to +0.1793 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 16.1 | +34.2% | +1.8018 to +6.3982 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.7 | 32.82 | +96.5% | −2.7131 to +34.9598 | no |
| utilisation (used / allocatable) | 0.03703 | 0.03741 | +1.0% | −0.0020 to +0.0028 | no |
| CPU used (cores), mean | 1.777 | 1.796 | +1.0% | −0.0955 to +0.1322 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.777 | 1.796 | +1.0% | −0.0955 to +0.1322 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 726 | −0.7% | −42.3179 to +32.0987 | no |
| HPA replicas, mean | 4.043 | 4.056 | +0.3% | −0.2183 to +0.2433 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| host CPU busy, the real machine under kind (%) | 54.16 | 60.68 | +12.0% | +4.7578 to +8.2883 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 928.7 | 1046 | +12.6% | +60.3124 to +173.6876 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 6.05 | +5484.6% | −0.9314 to +12.8148 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 34.6 | +4225.0% | −39.6450 to +107.2450 | no |
| queue: job turnaround, submitted to done, mean (s) | 234.8 | 348 | +48.2% | +60.3292 to +166.1958 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.8% | −3.0075 to +0.1784 | no |
| node-hours | 5.025 | 4.439 | −11.7% | −1.2523 to +0.0802 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.9 | +0.1% | −1.0511 to +2.6196 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 483.4 | −8.3% | −93.8118 to +6.2720 | no |
| response time (ms), mean | 760.6 | 752.8 | −1.0% | −54.2987 to +38.8166 | no |
| response time (ms), 95th percentile | 3079 | 3191 | +3.6% | −141.4444 to +365.5744 | no |
| response time (ms), 99th percentile | 4102 | 4355 | +6.2% | −122.0810 to +627.9684 | no |
| time over the response line (% of samples) | 25.11 | 25.16 | +0.2% | −0.6103 to +0.7026 | no |
| failed requests (%) | 0 | 0.007491 | +0.007 (native is 0) | −0.0095 to +0.0244 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.4 | +3.3% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.7 | +61.700 (native is 0) | +25.3653 to +98.0347 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.7 | 21.69 | +29.9% | −2.7258 to +12.7158 | no |
| utilisation (used / allocatable) | 0.03703 | 0.04167 | +12.5% | −0.0008 to +0.0101 | no |
| CPU used (cores), mean | 1.777 | 1.753 | −1.4% | −0.0748 to +0.0258 | no |
| Omni's own CPU (cores), mean | 0 | 0.01345 | +0.013 (native is 0) | +0.0120 to +0.0149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.777 | 1.766 | −0.6% | −0.0609 to +0.0388 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 666.4 | −8.9% | −140.2886 to +10.8403 | no |
| HPA replicas, mean | 4.043 | 4.194 | +3.7% | −0.0073 to +0.3096 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | −0.4578 to +1.0578 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 54.16 | 55.66 | +2.8% | +0.6655 to +2.3466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 928.7 | 944.5 | +1.7% | +1.5824 to +30.0176 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.658 | −19.5% | −4.8355 to +0.1524 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.1417 | +30.8% | −0.0352 to +0.1019 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.6 | −25.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 234.8 | 243.3 | +3.6% | −2.5742 to +19.5326 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.8% | −3.0075 to +0.1784 | no |
| node-hours | 5.028 | 4.439 | −11.7% | −1.2546 to +0.0771 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 527.9 | +0.0% | −1.5305 to +1.9171 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 483.4 | −8.4% | −94.4937 to +5.7721 | no |
| response time (ms), mean | 988.3 | 752.8 | −23.8% | −363.7730 to −107.2796 | yes: GAIN |
| response time (ms), 95th percentile | 4122 | 3191 | −22.6% | −1466.5646 to −396.6254 | yes: GAIN |
| response time (ms), 99th percentile | 5452 | 4355 | −20.1% | −1596.5814 to −597.0808 | yes: GAIN |
| time over the response line (% of samples) | 28.61 | 25.16 | −12.0% | −5.0258 to −1.8640 | yes: GAIN |
| failed requests (%) | 0.08697 | 0.007491 | −91.4% | −0.1732 to +0.0143 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 12.4 | −23.0% | −6.1327 to −1.2673 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.7 | +61.700 (native is 0) | +25.3653 to +98.0347 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.82 | 21.7 | −33.9% | −27.1232 to +4.8666 | no |
| utilisation (used / allocatable) | 0.03741 | 0.04167 | +11.4% | −0.0014 to +0.0099 | no |
| CPU used (cores), mean | 1.796 | 1.753 | −2.4% | −0.1428 to +0.0572 | no |
| Omni's own CPU (cores), mean | 0 | 0.01345 | +0.013 (native is 0) | +0.0120 to +0.0149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.796 | 1.766 | −1.6% | −0.1294 to +0.0707 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726 | 666.4 | −8.2% | −134.8583 to +15.6293 | no |
| HPA replicas, mean | 4.056 | 4.194 | +3.4% | −0.0542 to +0.3315 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | −0.4578 to +1.0578 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 60.68 | 55.66 | −8.3% | −6.2537 to −3.7802 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1046 | 944.5 | −9.7% | −146.7379 to −55.6621 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.658 | −19.5% | −4.8355 to +0.1524 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 6.05 | 0.1417 | −97.7% | −12.7348 to +0.9182 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.6 | 0.6 | −98.3% | −107.3933 to +39.3933 | no |
| queue: job turnaround, submitted to done, mean (s) | 348 | 243.3 | −30.1% | −151.3939 to −58.1728 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.83 | −9.7% | −2.5372 to +0.2015 | no |
| node-hours | 5.025 | 4.541 | −9.6% | −1.0626 to +0.0947 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.1 | −0.2% | −4.1917 to +2.1032 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 489.5 | −7.2% | −80.5650 to +5.1807 | no |
| response time (ms), mean | 760.6 | 901 | +18.5% | +37.3446 to +243.5711 | yes: LOSS |
| response time (ms), 95th percentile | 3079 | 3801 | +23.5% | +80.6163 to +1363.3027 | yes: LOSS |
| response time (ms), 99th percentile | 4102 | 5132 | +25.1% | +323.6130 to +1735.5502 | yes: LOSS |
| time over the response line (% of samples) | 25.11 | 31.27 | +24.5% | +2.4389 to +9.8819 | yes: LOSS |
| failed requests (%) | 0 | 0.1501 | +0.150 (native is 0) | −0.0507 to +0.3509 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 16.3 | +35.8% | +1.9871 to +6.6129 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.500 (native is 0) | +25.9478 to +35.0522 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.7 | 82.25 | +392.5% | +8.5318 to +122.5782 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03703 | 0.03841 | +3.7% | −0.0052 to +0.0080 | no |
| CPU used (cores), mean | 1.777 | 1.651 | −7.1% | −0.2898 to +0.0360 | no |
| Omni's own CPU (cores), mean | 0 | 0.01034 | +0.010 (native is 0) | +0.0090 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.777 | 1.661 | −6.6% | −0.2790 to +0.0460 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 715.9 | −2.1% | −122.6342 to +92.2656 | no |
| HPA replicas, mean | 4.043 | 4.452 | +10.1% | +0.2083 to +0.6102 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | +0.3207 to +2.0793 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.4 | +1300.0% | +0.4047 to +2.1953 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.16 | 62.28 | +15.0% | +6.0222 to +10.2278 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 928.7 | 1061 | +14.3% | +67.6782 to +197.7218 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.04 | −16.3% | −4.1576 to +0.2373 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 14.01 | +12830.8% | +2.8031 to +24.9969 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 128.6 | +15975.0% | +11.1380 to +244.4620 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 234.8 | 364.7 | +55.3% | +68.8149 to +190.9435 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*