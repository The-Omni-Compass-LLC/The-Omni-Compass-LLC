# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.85 | 5.144 |
| node-hours | 2.514 | 2.516 | 2.032 | 2.155 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.2 | 272.5 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 273.2 | 236.4 | 246 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 337.6 | 380 | 305.2 | 355.8 |
| response time (ms), 95th percentile | 1174 | 1615 | 1260 | 1688 |
| response time (ms), 99th percentile | 1668 | 2194 | 1803 | 2294 |
| time over the response line (% of samples) | 14.77 | 12.75 | 13.81 | 13.54 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9 | 7.6 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.6 | 34.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.598 | 21.17 | 10 | 22.86 |
| utilisation (used / allocatable) | 0.06079 | 0.06102 | 0.07554 | 0.07249 |
| CPU used (cores), mean | 1.459 | 1.465 | 1.441 | 1.465 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01702 | 0.01689 |
| CPU used with Omni's own (cores), mean | 1.459 | 1.465 | 1.458 | 1.482 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 454.6 | 393.5 | 403.5 |
| HPA replicas, mean | 1.964 | 1.999 | 2.066 | 2.037 |
| pods started | 0.1 | 0.1 | 0.3 | 0.4 |
| pod start wait, total (s) | 0.3 | 0.1 | 0.5 | 0.6 |
| pod start wait, mean (s) | 0.3 | 0.1 | 0.5 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.46 | 44.06 | 42.46 | 45.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 784.9 | 817.1 | 787 | 824.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.154 | 4.606 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1.075 | 0.07083 | 0.9583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | 0.5 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 89.96 | 121.6 | 92.04 | 128.4 |
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
| worker nodes in service, mean | 6 | 5.144 | −14.3% | −1.6965 to −0.0156 | yes: GAIN |
| node-hours | 2.516 | 2.155 | −14.4% | −0.7150 to −0.0073 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.9 | −0.1% | −1.1732 to +0.7402 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 246 | −9.9% | −54.1299 to −0.0990 | yes: GAIN |
| response time (ms), mean | 380 | 355.8 | −6.4% | −39.9397 to −8.4602 | yes: GAIN |
| response time (ms), 95th percentile | 1615 | 1688 | +4.5% | +12.1805 to +133.6015 | yes: LOSS |
| response time (ms), 99th percentile | 2194 | 2294 | +4.6% | −31.8306 to +232.1330 | no |
| time over the response line (% of samples) | 12.75 | 13.54 | +6.2% | −0.7737 to +2.3534 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.8 | +8.9% | −0.3583 to +1.9583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.100 (native is 0) | +21.2313 to +46.9687 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.17 | 22.86 | +8.0% | −1.5305 to +4.9038 | no |
| utilisation (used / allocatable) | 0.06102 | 0.07249 | +18.8% | +0.0012 to +0.0217 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.465 | +0.0% | −0.0396 to +0.0405 | no |
| Omni's own CPU (cores), mean | 0 | 0.01689 | +0.017 (native is 0) | +0.0158 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.482 | +1.2% | −0.0237 to +0.0584 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 403.5 | −11.2% | −94.1089 to −8.0376 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.037 | +1.9% | −0.0965 to +0.1729 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.1 | 0.6 | +500.0% | −0.1952 to +1.1952 | no |
| pod start wait, mean (s) | 0.1 | 0.6 | +500.0% | −0.1952 to +1.1952 | no |
| host CPU busy, the real machine under kind (%) | 44.06 | 45.27 | +2.7% | +0.8501 to +1.5707 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.1 | 824.9 | +1.0% | +2.0696 to +13.5304 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.7047 to −0.0829 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.075 | 0.9583 | −10.9% | −0.3948 to +0.1614 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 2.1 | −34.4% | −2.9910 to +0.7910 | no |
| queue: job turnaround, submitted to done, mean (s) | 121.6 | 128.5 | +5.6% | +1.2546 to +12.4620 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.516 | +0.1% | −0.0051 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.2 | +0.2% | −0.3129 to +1.2754 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 273.2 | +0.2% | −0.3129 to +1.2754 | no |
| response time (ms), mean | 337.6 | 380 | +12.6% | +6.7160 to +78.1942 | yes: LOSS |
| response time (ms), 95th percentile | 1174 | 1615 | +37.5% | +67.9880 to +812.9880 | yes: LOSS |
| response time (ms), 99th percentile | 1668 | 2194 | +31.6% | +90.5569 to +962.3869 | yes: LOSS |
| time over the response line (% of samples) | 14.77 | 12.75 | −13.7% | −5.1064 to +1.0643 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9 | +15.4% | −0.0972 to +2.4972 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.598 | 21.17 | +120.6% | +3.6892 to +19.4541 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06079 | 0.06102 | +0.4% | −0.0006 to +0.0010 | no |
| CPU used (cores), mean | 1.459 | 1.465 | +0.4% | −0.0132 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.459 | 1.465 | +0.4% | −0.0132 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 454.6 | −0.2% | −7.9009 to +5.6837 | no |
| HPA replicas, mean | 1.964 | 1.999 | +1.8% | −0.1164 to +0.1867 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 41.46 | 44.06 | +6.3% | +1.8282 to +3.3615 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 817.1 | +4.1% | +7.7704 to +56.6296 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1.075 | +1333.3% | +0.6034 to +1.3966 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | +540.0% | +0.2673 to +5.1327 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.96 | 121.6 | +35.2% | +9.3798 to +53.8869 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.85 | −19.2% | −1.9484 to −0.3511 | yes: GAIN |
| node-hours | 2.514 | 2.032 | −19.2% | −0.8173 to −0.1474 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 | −0.1% | −1.0252 to +0.6583 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 236.4 | −13.3% | −61.6345 to −10.9325 | yes: GAIN |
| response time (ms), mean | 337.6 | 305.2 | −9.6% | −47.1756 to −17.6222 | yes: GAIN |
| response time (ms), 95th percentile | 1174 | 1260 | +7.3% | −6.3589 to +177.6939 | no |
| response time (ms), 99th percentile | 1668 | 1803 | +8.1% | −51.4523 to +320.9793 | no |
| time over the response line (% of samples) | 14.77 | 13.81 | −6.5% | −1.8511 to −0.0596 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.6 | −2.6% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 | +46.600 (native is 0) | +26.9115 to +66.2885 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.598 | 10 | +4.2% | −0.9830 to +1.7930 | no |
| utilisation (used / allocatable) | 0.06079 | 0.07554 | +24.3% | +0.0040 to +0.0255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.459 | 1.441 | −1.2% | −0.0459 to +0.0104 | no |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.0154 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.458 | −0.1% | −0.0296 to +0.0281 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 393.5 | −13.7% | −106.8817 to −17.5756 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.066 | +5.2% | −0.0836 to +0.2887 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.8003 to +1.2003 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | −0.8003 to +1.2003 | no |
| host CPU busy, the real machine under kind (%) | 41.46 | 42.46 | +2.4% | +0.6673 to +1.3355 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 787 | +0.3% | −1.5231 to +5.7231 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.154 | −30.8% | −3.0418 to −0.6502 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.07083 | −5.6% | −0.0303 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.96 | 92.04 | +2.3% | −0.4962 to +4.6545 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.85 | −19.2% | −1.9484 to −0.3511 | yes: GAIN |
| node-hours | 2.516 | 2.032 | −19.2% | −0.8211 to −0.1475 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.5 | −0.2% | −1.4241 to +0.0947 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 236.4 | −13.5% | −62.2654 to −11.2640 | yes: GAIN |
| response time (ms), mean | 380 | 305.2 | −19.7% | −120.1197 to −29.5884 | yes: GAIN |
| response time (ms), 95th percentile | 1615 | 1260 | −22.0% | −660.9138 to −48.7272 | yes: GAIN |
| response time (ms), 99th percentile | 2194 | 1803 | −17.9% | −735.1729 to −48.2439 | yes: GAIN |
| time over the response line (% of samples) | 12.75 | 13.81 | +8.4% | −1.7866 to +3.9181 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 7.6 | −15.6% | −3.1260 to +0.3260 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 | +46.600 (native is 0) | +26.9115 to +66.2885 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.17 | 10 | −52.7% | −18.3174 to −4.0159 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06102 | 0.07554 | +23.8% | +0.0036 to +0.0254 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.441 | −1.6% | −0.0451 to −0.0019 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.0154 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.458 | −0.4% | −0.0293 to +0.0163 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 393.5 | −13.4% | −106.0753 to −16.1649 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.066 | +3.4% | −0.1240 to +0.2588 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 44.06 | 42.46 | −3.6% | −2.3644 to −0.8225 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 817.1 | 787 | −3.7% | −51.9307 to −8.2693 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.154 | −30.8% | −3.0418 to −0.6502 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.075 | 0.07083 | −93.4% | −1.3921 to −0.6162 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 0.5 | −84.4% | −5.1327 to −0.2673 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 121.6 | 92.04 | −24.3% | −49.9906 to −9.1177 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.144 | −14.3% | −1.6965 to −0.0156 | yes: GAIN |
| node-hours | 2.514 | 2.155 | −14.3% | −0.7113 to −0.0070 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.7019 to +1.2313 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 246 | −9.8% | −53.4981 to +0.2317 | no |
| response time (ms), mean | 337.6 | 355.8 | +5.4% | −15.7714 to +52.2817 | no |
| response time (ms), 95th percentile | 1174 | 1688 | +43.7% | +116.6768 to +910.0812 | yes: LOSS |
| response time (ms), 99th percentile | 1668 | 2294 | +37.6% | +162.7878 to +1090.4584 | yes: LOSS |
| time over the response line (% of samples) | 14.77 | 13.54 | −8.3% | −5.1808 to +2.7183 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9.8 | +25.6% | +0.0629 to +3.9371 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.100 (native is 0) | +21.2313 to +46.9687 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.598 | 22.86 | +138.1% | +4.0784 to +22.4382 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06079 | 0.07249 | +19.2% | +0.0015 to +0.0219 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.459 | 1.465 | +0.4% | −0.0386 to +0.0509 | no |
| Omni's own CPU (cores), mean | 0 | 0.01689 | +0.017 (native is 0) | +0.0158 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.482 | +1.6% | −0.0226 to +0.0687 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 403.5 | −11.5% | −95.7547 to −8.6090 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.037 | +3.7% | −0.0999 to +0.2466 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| host CPU busy, the real machine under kind (%) | 41.46 | 45.27 | +9.2% | +2.9055 to +4.7050 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784.9 | 824.9 | +5.1% | +10.6230 to +69.3770 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.7047 to −0.0829 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.9583 | +1177.8% | +0.6446 to +1.1221 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.1 | +320.0% | +0.9089 to +2.2911 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.96 | 128.4 | +42.8% | +13.5505 to +63.4329 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*