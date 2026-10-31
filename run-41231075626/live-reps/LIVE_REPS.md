# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.855 | 5.807 |
| node-hours | 2.513 | 2.513 | 2.455 | 2.429 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.6 | 276.1 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.6 | 271.5 | 269.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 553.6 | 581.6 | 523.7 | 550.3 |
| response time (ms), 95th percentile | 2142 | 2253 | 2239 | 2339 |
| response time (ms), 99th percentile | 2962 | 3171 | 3225 | 3344 |
| time over the response line (% of samples) | 27.27 | 27.63 | 26.37 | 27 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.1 | 13.2 | 13.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 31.5 | 29.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 14.14 | 14.57 | 14.74 |
| utilisation (used / allocatable) | 0.06888 | 0.06924 | 0.07128 | 0.07198 |
| CPU used (cores), mean | 1.653 | 1.662 | 1.67 | 1.673 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01691 | 0.01721 |
| CPU used with Omni's own (cores), mean | 1.653 | 1.662 | 1.687 | 1.691 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 400.2 | 391.1 | 388.1 |
| HPA replicas, mean | 1.98 | 1.998 | 2.205 | 2.139 |
| pods started | 0 | 0.1 | 0.4 | 0.4 |
| pod start wait, total (s) | 0 | 0.2 | 0.9 | 0.7 |
| pod start wait, mean (s) | 0 | 0.2 | 0.9 | 0.7 |
| host CPU busy, the real machine under kind (%) | 47.08 | 47.98 | 48.19 | 49.21 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 851.3 | 863.2 | 858.8 | 873.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.699 | 5.622 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.6083 | 0.1208 | 0.6292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 3.3 | 0.9 | 4.3 |
| queue: job turnaround, submitted to done, mean (s) | 155.1 | 165.8 | 163.1 | 175.5 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.807 | −3.2% | −0.5380 to +0.1526 | no |
| node-hours | 2.513 | 2.429 | −3.3% | −0.2260 to +0.0594 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 275.5 | −0.0% | −0.6797 to +0.4841 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 269.5 | −2.2% | −17.0330 to +4.6957 | no |
| response time (ms), mean | 581.6 | 550.3 | −5.4% | −43.7151 to −18.8788 | yes: GAIN |
| response time (ms), 95th percentile | 2253 | 2339 | +3.8% | +25.8152 to +147.0378 | yes: LOSS |
| response time (ms), 99th percentile | 3171 | 3344 | +5.5% | −7.2678 to +353.0070 | no |
| time over the response line (% of samples) | 27.63 | 27 | −2.3% | −1.3472 to +0.1039 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.1 | 13.2 | +0.8% | −1.4617 to +1.6617 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.2 | +29.200 (native is 0) | +11.0826 to +47.3174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.14 | 14.74 | +4.2% | −1.8702 to +3.0636 | no |
| utilisation (used / allocatable) | 0.06924 | 0.07198 | +4.0% | −0.0005 to +0.0060 | no |
| CPU used (cores), mean | 1.662 | 1.673 | +0.7% | −0.0178 to +0.0411 | no |
| Omni's own CPU (cores), mean | 0 | 0.01721 | +0.017 (native is 0) | +0.0163 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.662 | 1.691 | +1.7% | −0.0002 to +0.0579 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.2 | 388.1 | −3.0% | −25.5275 to +1.3602 | no |
| HPA replicas, mean | 1.998 | 2.139 | +7.1% | −0.0531 to +0.3349 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −0.0058 to +1.0058 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 47.98 | 49.21 | +2.6% | +0.7149 to +1.7389 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 863.2 | 873.7 | +1.2% | −0.1378 to +21.1378 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.622 | −6.3% | −1.0298 to +0.2742 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6083 | 0.6292 | +3.4% | −0.1058 to +0.1475 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 4.3 | +30.3% | −1.5234 to +3.5234 | no |
| queue: job turnaround, submitted to done, mean (s) | 165.8 | 175.5 | +5.9% | +2.5850 to +16.8900 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.513 | +0.0% | −0.0105 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.6 | +0.1% | −0.9709 to +1.2692 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.6 | +0.1% | −0.9709 to +1.2692 | no |
| response time (ms), mean | 553.6 | 581.6 | +5.1% | +8.6631 to +47.2561 | yes: LOSS |
| response time (ms), 95th percentile | 2142 | 2253 | +5.2% | −22.9443 to +244.8843 | no |
| response time (ms), 99th percentile | 2962 | 3171 | +7.1% | −15.7114 to +434.1860 | no |
| time over the response line (% of samples) | 27.27 | 27.63 | +1.3% | −0.2950 to +1.0026 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.1 | +0.8% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 14.14 | +7.4% | −1.1921 to +3.1355 | no |
| utilisation (used / allocatable) | 0.06888 | 0.06924 | +0.5% | −0.0002 to +0.0009 | no |
| CPU used (cores), mean | 1.653 | 1.662 | +0.5% | −0.0057 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.653 | 1.662 | +0.5% | −0.0057 to +0.0227 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 400.2 | −0.6% | −6.4745 to +1.6932 | no |
| HPA replicas, mean | 1.98 | 1.998 | +0.9% | −0.1047 to +0.1407 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 47.08 | 47.98 | +1.9% | +0.6521 to +1.1574 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.3 | 863.2 | +1.4% | +6.8370 to +16.9630 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.6083 | +186.3% | +0.0280 to +0.7636 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 3.3 | +312.5% | −1.1357 to +6.1357 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.1 | 165.8 | +6.9% | +5.2457 to +16.2210 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.855 | −2.4% | −0.3857 to +0.0953 | no |
| node-hours | 2.513 | 2.455 | −2.3% | −0.1581 to +0.0429 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 276.1 | +0.2% | −0.0934 to +1.3211 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 271.5 | −1.4% | −11.4023 to +3.4841 | no |
| response time (ms), mean | 553.6 | 523.7 | −5.4% | −49.8004 to −10.1063 | yes: GAIN |
| response time (ms), 95th percentile | 2142 | 2239 | +4.5% | −37.2008 to +231.1328 | no |
| response time (ms), 99th percentile | 2962 | 3225 | +8.9% | +10.8735 to +515.6611 | yes: LOSS |
| time over the response line (% of samples) | 27.27 | 26.37 | −3.3% | −1.6124 to −0.2010 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.2 | +1.5% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +9.0813 to +53.9187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 14.57 | +10.6% | −0.7689 to +3.5556 | no |
| utilisation (used / allocatable) | 0.06888 | 0.07128 | +3.5% | −0.0006 to +0.0054 | no |
| CPU used (cores), mean | 1.653 | 1.67 | +1.0% | +0.0041 to +0.0299 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.017 (native is 0) | +0.0163 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.653 | 1.687 | +2.1% | +0.0207 to +0.0472 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 391.1 | −2.8% | −27.3401 to +4.4318 | no |
| HPA replicas, mean | 1.98 | 2.205 | +11.3% | +0.0235 to +0.4254 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0802 to +1.8802 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0802 to +1.8802 | no |
| host CPU busy, the real machine under kind (%) | 47.08 | 48.19 | +2.4% | +0.8411 to +1.3811 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.3 | 858.8 | +0.9% | +2.8858 to +12.1142 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.699 | −5.0% | −0.7707 to +0.1681 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.1208 | −43.1% | −0.4184 to +0.2351 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.1 | 163.1 | +5.2% | +0.5558 to +15.4859 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.855 | −2.4% | −0.3857 to +0.0953 | no |
| node-hours | 2.513 | 2.455 | −2.3% | −0.1597 to +0.0441 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 276.1 | +0.2% | −0.5414 to +1.4707 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 271.5 | −1.5% | −11.7682 to +3.5517 | no |
| response time (ms), mean | 581.6 | 523.7 | −10.0% | −74.8898 to −40.9361 | yes: GAIN |
| response time (ms), 95th percentile | 2253 | 2239 | −0.6% | −148.4035 to +120.3955 | no |
| response time (ms), 99th percentile | 3171 | 3225 | +1.7% | −95.2221 to +203.2821 | no |
| time over the response line (% of samples) | 27.63 | 26.37 | −4.6% | −2.2620 to −0.2589 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.1 | 13.2 | +0.8% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +9.0813 to +53.9187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.14 | 14.57 | +3.0% | −0.7249 to +1.5683 | no |
| utilisation (used / allocatable) | 0.06924 | 0.07128 | +2.9% | −0.0007 to +0.0048 | no |
| CPU used (cores), mean | 1.662 | 1.67 | +0.5% | −0.0102 to +0.0272 | no |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.017 (native is 0) | +0.0163 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.662 | 1.687 | +1.5% | +0.0066 to +0.0442 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.2 | 391.1 | −2.3% | −22.0629 to +3.9360 | no |
| HPA replicas, mean | 1.998 | 2.205 | +10.3% | −0.0703 to +0.4832 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.2567 to +1.6567 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.2567 to +1.6567 | no |
| host CPU busy, the real machine under kind (%) | 47.98 | 48.19 | +0.4% | −0.1801 to +0.5928 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 863.2 | 858.8 | −0.5% | −11.1288 to +2.3288 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.699 | −5.0% | −0.7707 to +0.1681 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6083 | 0.1208 | −80.1% | −1.0525 to +0.0775 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 0.9 | −72.7% | −6.3208 to +1.5208 | no |
| queue: job turnaround, submitted to done, mean (s) | 165.8 | 163.1 | −1.6% | −9.8023 to +4.3773 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.807 | −3.2% | −0.5380 to +0.1526 | no |
| node-hours | 2.513 | 2.429 | −3.3% | −0.2253 to +0.0590 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.5 | +0.0% | −0.8785 to +0.9812 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 269.5 | −2.2% | −16.7489 to +4.7100 | no |
| response time (ms), mean | 553.6 | 550.3 | −0.6% | −25.3799 to +18.7053 | no |
| response time (ms), 95th percentile | 2142 | 2339 | +9.2% | +26.4274 to +368.3656 | yes: LOSS |
| response time (ms), 99th percentile | 2962 | 3344 | +12.9% | +86.5806 to +677.6332 | yes: LOSS |
| time over the response line (% of samples) | 27.27 | 27 | −1.0% | −0.6083 to +0.0725 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.2 | +1.5% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.2 | +29.200 (native is 0) | +11.0826 to +47.3174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 14.74 | +11.9% | −1.3017 to +4.4383 | no |
| utilisation (used / allocatable) | 0.06888 | 0.07198 | +4.5% | −0.0005 to +0.0067 | no |
| CPU used (cores), mean | 1.653 | 1.673 | +1.2% | +0.0018 to +0.0385 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01721 | +0.017 (native is 0) | +0.0163 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.653 | 1.691 | +2.3% | +0.0193 to +0.0555 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 388.1 | −3.6% | −31.1198 to +2.1712 | no |
| HPA replicas, mean | 1.98 | 2.139 | +8.0% | +0.0299 to +0.2879 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| host CPU busy, the real machine under kind (%) | 47.08 | 49.21 | +4.5% | +1.6865 to +2.5769 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.3 | 873.7 | +2.6% | +12.4758 to +32.3242 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.622 | −6.3% | −1.0298 to +0.2742 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.6292 | +196.1% | −0.0062 to +0.8396 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4.3 | +437.5% | −1.2358 to +8.2358 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.1 | 175.5 | +13.2% | +11.6586 to +29.2830 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*