# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.757 | 5.008 |
| node-hours | 2.517 | 2.516 | 1.994 | 2.098 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.8 | 273.3 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 273.8 | 234.3 | 242.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 399 | 399.3 | 417.1 | 430 |
| response time (ms), 95th percentile | 1491 | 1526 | 1582 | 1671 |
| response time (ms), 99th percentile | 2119 | 2200 | 2270 | 2358 |
| time over the response line (% of samples) | 15.67 | 14.86 | 15.85 | 15.77 |
| failed requests (%) | 0 | 0.0117 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.3 | 11 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 17 | 16.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 42.86 | 32.14 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 19.43 | 18.22 | 21.78 |
| utilisation (used / allocatable) | 0.06378 | 0.06412 | 0.07905 | 0.0755 |
| CPU used (cores), mean | 1.531 | 1.539 | 1.496 | 1.513 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0619 | 0.06595 |
| CPU used with Omni's own (cores), mean | 1.531 | 1.539 | 1.558 | 1.579 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 432.2 | 377 | 385.9 |
| HPA replicas, mean | 2.093 | 2.086 | 2.362 | 2.152 |
| pods started | 0 | 0.1 | 1.2 | 0.2 |
| pod start wait, total (s) | 0 | 0.3 | 2 | 0.4 |
| pod start wait, mean (s) | 0 | 0.3 | 0.5867 | 0.4 |
| host CPU busy, the real machine under kind (%) | 43.81 | 44.82 | 46.01 | 47.18 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806.7 | 813.6 | 813.3 | 820.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.721 | 4.132 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2458 | 0.2167 | 0.2 | 0.9875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | 1.2 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 112 | 120.4 | 118.7 | 126.3 |
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
| worker nodes in service, mean | 6 | 5.008 | −16.5% | −1.6488 to −0.3344 | yes: GAIN |
| node-hours | 2.516 | 2.097 | −16.6% | −0.6926 to −0.1447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.3 | −0.2% | −1.6111 to +0.6803 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 242.2 | −11.5% | −52.5760 to −10.6548 | yes: GAIN |
| response time (ms), mean | 399.3 | 430 | +7.7% | −3.2818 to +64.4861 | no |
| response time (ms), 95th percentile | 1526 | 1671 | +9.5% | −27.9146 to +317.5946 | no |
| response time (ms), 99th percentile | 2200 | 2358 | +7.2% | −58.2700 to +374.4838 | no |
| time over the response line (% of samples) | 14.86 | 15.77 | +6.1% | −0.3089 to +2.1205 | no |
| failed requests (%) | 0.0117 | 0 | −100.0% | −0.0382 to +0.0148 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 11 | +6.8% | −0.1294 to +1.5294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.800 (native is 0) | +11.8350 to +21.7650 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.43 | 21.78 | +12.1% | −1.4140 to +6.1040 | no |
| utilisation (used / allocatable) | 0.06412 | 0.0755 | +17.7% | +0.0046 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.539 | 1.513 | −1.7% | −0.0814 to +0.0298 | no |
| Omni's own CPU (cores), mean | 0 | 0.06595 | +0.066 (native is 0) | +0.0595 to +0.0724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.539 | 1.579 | +2.6% | −0.0206 to +0.1008 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 385.9 | −10.7% | −74.4425 to −18.0845 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.086 | 2.152 | +3.2% | −0.1575 to +0.2904 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 44.82 | 47.18 | +5.3% | +1.8145 to +2.9176 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.6 | 820.6 | +0.9% | +0.0813 to +13.9187 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.132 | −31.1% | −3.0696 to −0.6666 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.9875 | +355.8% | −0.7403 to +2.2819 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | +25.0% | −0.6121 to +1.0121 | no |
| queue: job turnaround, submitted to done, mean (s) | 120.4 | 126.3 | +4.9% | +0.1058 to +11.6525 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.516 | −0.0% | −0.0076 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.8 | +0.0% | −0.7279 to +0.8243 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 273.8 | +0.0% | −0.7279 to +0.8243 | no |
| response time (ms), mean | 399 | 399.3 | +0.1% | −15.0628 to +15.7080 | no |
| response time (ms), 95th percentile | 1491 | 1526 | +2.4% | −65.9868 to +137.6248 | no |
| response time (ms), 99th percentile | 2119 | 2200 | +3.8% | −18.0293 to +178.9007 | no |
| time over the response line (% of samples) | 15.67 | 14.86 | −5.2% | −1.8761 to +0.2580 | no |
| failed requests (%) | 0 | 0.0117 | +0.012 (native is 0) | −0.0148 to +0.0382 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.3 | −4.6% | −1.9005 to +0.9005 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 19.44 | +37.2% | +1.0706 to +9.4760 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06378 | 0.06412 | +0.5% | −0.0003 to +0.0010 | no |
| CPU used (cores), mean | 1.531 | 1.539 | +0.5% | −0.0066 to +0.0232 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.531 | 1.539 | +0.5% | −0.0066 to +0.0232 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 432.2 | −0.5% | −6.0551 to +1.9203 | no |
| HPA replicas, mean | 2.093 | 2.086 | −0.4% | −0.1725 to +0.1572 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 43.81 | 44.82 | +2.3% | +0.7131 to +1.3103 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.7 | 813.6 | +0.9% | +1.9048 to +11.8952 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2458 | 0.2167 | −11.9% | −0.3716 to +0.3133 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | −11.1% | −1.1900 to +0.9900 | no |
| queue: job turnaround, submitted to done, mean (s) | 112 | 120.4 | +7.5% | +2.9290 to +13.8210 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.757 | −20.7% | −1.8822 to −0.6030 | yes: GAIN |
| node-hours | 2.517 | 1.994 | −20.8% | −0.7914 to −0.2536 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.3 | −0.2% | −1.3966 to +0.5743 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 234.3 | −14.4% | −60.0287 to −18.8727 | yes: GAIN |
| response time (ms), mean | 399 | 417.1 | +4.5% | −1.2325 to +37.3971 | no |
| response time (ms), 95th percentile | 1491 | 1582 | +6.2% | −3.0433 to +186.8123 | no |
| response time (ms), 99th percentile | 2119 | 2270 | +7.1% | −35.6031 to +336.5741 | no |
| time over the response line (% of samples) | 15.67 | 15.85 | +1.1% | −0.3818 to +0.7386 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11 | +1.9% | −0.9081 to +1.3081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17.000 (native is 0) | +12.6164 to +21.3836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 18.22 | +28.7% | +0.2002 to +7.9198 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06378 | 0.07905 | +23.9% | +0.0074 to +0.0231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.531 | 1.496 | −2.3% | −0.0748 to +0.0055 | no |
| Omni's own CPU (cores), mean | 0 | 0.0619 | +0.062 (native is 0) | +0.0540 to +0.0698 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.531 | 1.558 | +1.8% | −0.0181 to +0.0726 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 377 | −13.2% | −86.3195 to −28.2294 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.093 | 2.362 | +12.9% | −0.0459 to +0.5842 | no |
| pods started | 0 | 1.2 | +1.200 (native is 0) | −0.0972 to +2.4972 | no |
| pod start wait, total (s) | 0 | 2 | +2.000 (native is 0) | −0.5458 to +4.5458 | no |
| pod start wait, mean (s) | 0 | 0.5867 | +0.587 (native is 0) | +0.0049 to +1.1685 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.81 | 46.01 | +5.0% | +1.5620 to +2.8368 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.7 | 813.3 | +0.8% | +0.0859 to +13.1141 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 | −38.0% | −3.1259 to −1.4317 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2458 | 0.2 | −18.6% | −0.1757 to +0.0840 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.2 | +33.3% | −0.4578 to +1.0578 | no |
| queue: job turnaround, submitted to done, mean (s) | 112 | 118.7 | +5.9% | +0.7286 to +12.5964 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.757 | −20.7% | −1.8822 to −0.6030 | yes: GAIN |
| node-hours | 2.516 | 1.994 | −20.7% | −0.7905 to −0.2532 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.3 | −0.2% | −1.5188 to +0.6002 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 234.3 | −14.4% | −60.0293 to −18.9685 | yes: GAIN |
| response time (ms), mean | 399.3 | 417.1 | +4.4% | −3.6955 to +39.2148 | no |
| response time (ms), 95th percentile | 1526 | 1582 | +3.7% | −43.9756 to +156.1066 | no |
| response time (ms), 99th percentile | 2200 | 2270 | +3.2% | −133.2354 to +273.3350 | no |
| time over the response line (% of samples) | 14.86 | 15.85 | +6.6% | −0.0612 to +2.0360 | no |
| failed requests (%) | 0.0117 | 0 | −100.0% | −0.0382 to +0.0148 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 11 | +6.8% | −0.8099 to +2.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17.000 (native is 0) | +12.6164 to +21.3836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.43 | 18.22 | −6.2% | −3.3855 to +0.9589 | no |
| utilisation (used / allocatable) | 0.06412 | 0.07905 | +23.3% | +0.0068 to +0.0230 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.539 | 1.496 | −2.8% | −0.0822 to −0.0037 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0619 | +0.062 (native is 0) | +0.0540 to +0.0698 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.539 | 1.558 | +1.2% | −0.0253 to +0.0632 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 377 | −12.8% | −85.3503 to −25.0639 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.086 | 2.362 | +13.3% | −0.0103 to +0.5640 | no |
| pods started | 0.1 | 1.2 | +1100.0% | −0.2676 to +2.4676 | no |
| pod start wait, total (s) | 0.3 | 2 | +566.7% | −1.0611 to +4.4611 | no |
| pod start wait, mean (s) | 0.3 | 0.5867 | +95.6% | −0.7129 to +1.2862 | no |
| host CPU busy, the real machine under kind (%) | 44.82 | 46.01 | +2.7% | +0.5549 to +1.8205 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.6 | 813.3 | −0.0% | −3.4641 to +2.8641 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 | −38.0% | −3.1259 to −1.4317 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.2 | −7.7% | −0.2340 to +0.2006 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.2 | +50.0% | −1.0385 to +1.8385 | no |
| queue: job turnaround, submitted to done, mean (s) | 120.4 | 118.7 | −1.4% | −7.0014 to +3.5764 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.008 | −16.5% | −1.6488 to −0.3344 | yes: GAIN |
| node-hours | 2.517 | 2.098 | −16.7% | −0.6925 to −0.1462 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.3 | −0.2% | −1.6794 to +0.8449 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 242.2 | −11.5% | −52.4682 to −10.6663 | yes: GAIN |
| response time (ms), mean | 399 | 430 | +7.8% | +3.0925 to +58.7571 | yes: LOSS |
| response time (ms), 95th percentile | 1491 | 1671 | +12.1% | +21.8074 to +339.5106 | yes: LOSS |
| response time (ms), 99th percentile | 2119 | 2358 | +11.3% | −11.2746 to +488.3598 | no |
| time over the response line (% of samples) | 15.67 | 15.77 | +0.6% | −1.3730 to +1.5665 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11 | +1.9% | −1.1403 to +1.5403 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.800 (native is 0) | +11.8350 to +21.7650 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 21.78 | +53.8% | +0.7050 to +14.5317 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06378 | 0.0755 | +18.4% | +0.0050 to +0.0184 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.531 | 1.513 | −1.1% | −0.0772 to +0.0422 | no |
| Omni's own CPU (cores), mean | 0 | 0.06595 | +0.066 (native is 0) | +0.0595 to +0.0724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.531 | 1.579 | +3.2% | −0.0162 to +0.1130 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 385.9 | −11.1% | −76.3274 to −20.3344 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.093 | 2.152 | +2.8% | −0.1479 to +0.2656 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 43.81 | 47.18 | +7.7% | +2.8262 to +3.9292 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.7 | 820.6 | +1.7% | +3.1813 to +24.6187 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.132 | −31.1% | −3.0696 to −0.6666 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2458 | 0.9875 | +301.7% | −0.5301 to +2.0134 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1 | +11.1% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 112 | 126.3 | +12.7% | +5.7658 to +22.7426 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*