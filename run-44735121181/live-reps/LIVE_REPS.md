# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.516 | 1.514 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 159.8 | 158.7 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 159.8 | 158.7 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 125.6 | 127.4 | 125.9 | 128.6 |
| response time (ms), 95th percentile | 249.7 | 255.4 | 253.4 | 256.8 |
| response time (ms), 99th percentile | 348.2 | 361.2 | 354.6 | 353.1 |
| time over the response line (% of samples) | 0.1397 | 0.14 | 0.08878 | 0.06354 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 4.8 | 5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.27 | 0.3467 | 0.545 |
| utilisation (used / allocatable) | 0.03675 | 0.04093 | 0.037 | 0.04151 |
| CPU used (cores), mean | 0.882 | 0.9823 | 0.8879 | 0.9962 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.02813 | 0.04433 |
| CPU used with Omni's own (cores), mean | 0.882 | 0.9823 | 0.916 | 1.041 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.5 | 644.5 | 709.6 | 636.9 |
| HPA replicas, mean | 8.802 | 8.814 | 9.218 | 9.5 |
| pods started | 5.3 | 5 | 5.5 | 6.1 |
| pod start wait, total (s) | 6.8 | 8.5 | 7.8 | 9.5 |
| pod start wait, mean (s) | 1.29 | 1.693 | 1.428 | 1.533 |
| host CPU busy, the real machine under kind (%) | 26.75 | 30.21 | 27.89 | 32.25 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.51 | −0.4% | −0.0143 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.3 | −0.3% | −1.3589 to +0.3807 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.3 | −0.3% | −1.3589 to +0.3807 | no |
| response time (ms), mean | 127.4 | 128.6 | +1.0% | −2.0839 to +4.5877 | no |
| response time (ms), 95th percentile | 255.4 | 256.8 | +0.5% | −7.1518 to +9.8448 | no |
| response time (ms), 99th percentile | 361.2 | 353.1 | −2.2% | −30.4927 to +14.2639 | no |
| time over the response line (% of samples) | 0.14 | 0.06354 | −54.6% | −0.2375 to +0.0846 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5 | +5.000 (native is 0) | +4.0463 to +5.9537 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.545 | +101.9% | −0.0157 to +0.5657 | no |
| utilisation (used / allocatable) | 0.04093 | 0.04151 | +1.4% | −0.0002 to +0.0013 | no |
| CPU used (cores), mean | 0.9823 | 0.9962 | +1.4% | −0.0040 to +0.0319 | no |
| Omni's own CPU (cores), mean | 0 | 0.04433 | +0.044 (native is 0) | +0.0403 to +0.0483 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9823 | 1.041 | +5.9% | +0.0375 to +0.0790 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.5 | 636.9 | −1.2% | −17.1680 to +1.7694 | no |
| HPA replicas, mean | 8.814 | 9.5 | +7.8% | +0.0283 to +1.3447 | yes: power given |
| pods started | 5 | 6.1 | +22.0% | −0.5329 to +2.7329 | no |
| pod start wait, total (s) | 8.5 | 9.5 | +11.8% | −1.7806 to +3.7806 | no |
| pod start wait, mean (s) | 1.693 | 1.533 | −9.5% | −0.5013 to +0.1797 | no |
| host CPU busy, the real machine under kind (%) | 30.21 | 32.25 | +6.8% | +1.4106 to +2.6717 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.516 | +0.3% | −0.0043 to +0.0136 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 159.8 | +0.9% | +0.4017 to +2.4423 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 159.8 | +0.9% | +0.4017 to +2.4423 | yes: power given |
| response time (ms), mean | 125.6 | 127.4 | +1.4% | −2.4696 to +5.8839 | no |
| response time (ms), 95th percentile | 249.7 | 255.4 | +2.3% | −11.1744 to +22.6924 | no |
| response time (ms), 99th percentile | 348.2 | 361.2 | +3.7% | −19.4885 to +45.3593 | no |
| time over the response line (% of samples) | 0.1397 | 0.14 | +0.2% | −0.1338 to +0.1344 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.27 | +161.3% | −0.0886 to +0.4219 | no |
| utilisation (used / allocatable) | 0.03675 | 0.04093 | +11.4% | +0.0035 to +0.0048 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.882 | 0.9823 | +11.4% | +0.0847 to +0.1159 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.882 | 0.9823 | +11.4% | +0.0847 to +0.1159 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.5 | 644.5 | −9.7% | −79.2046 to −58.6607 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.802 | 8.814 | +0.1% | −0.0735 to +0.0981 | no |
| pods started | 5.3 | 5 | −5.7% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 6.8 | 8.5 | +25.0% | −0.4340 to +3.8340 | no |
| pod start wait, mean (s) | 1.29 | 1.693 | +31.3% | +0.0049 to +0.8018 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.75 | 30.21 | +12.9% | +3.0437 to +3.8784 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.514 | +0.2% | +0.0009 to +0.0045 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.7 | +0.2% | +0.0693 to +0.5855 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.7 | +0.2% | +0.0693 to +0.5855 | yes: power given |
| response time (ms), mean | 125.6 | 125.9 | +0.2% | −3.2284 to +3.6545 | no |
| response time (ms), 95th percentile | 249.7 | 253.4 | +1.5% | −13.9442 to +21.4702 | no |
| response time (ms), 99th percentile | 348.2 | 354.6 | +1.8% | −31.2940 to +44.1122 | no |
| time over the response line (% of samples) | 0.1397 | 0.08878 | −36.4% | −0.1570 to +0.0552 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.8 | +4.800 (native is 0) | +2.9904 to +6.6096 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.3467 | +235.5% | +0.0169 to +0.4698 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03675 | 0.037 | +0.7% | −0.0005 to +0.0010 | no |
| CPU used (cores), mean | 0.882 | 0.8879 | +0.7% | −0.0128 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.02813 | +0.028 (native is 0) | +0.0253 to +0.0309 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.882 | 0.916 | +3.9% | +0.0138 to +0.0543 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.5 | 709.6 | −0.5% | −17.2662 to +9.5956 | no |
| HPA replicas, mean | 8.802 | 9.218 | +4.7% | −0.2642 to +1.0976 | no |
| pods started | 5.3 | 5.5 | +3.8% | −1.3744 to +1.7744 | no |
| pod start wait, total (s) | 6.8 | 7.8 | +14.7% | −1.1326 to +3.1326 | no |
| pod start wait, mean (s) | 1.29 | 1.428 | +10.7% | −0.0880 to +0.3641 | no |
| host CPU busy, the real machine under kind (%) | 26.75 | 27.89 | +4.3% | +0.5609 to +1.7269 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0106 to +0.0066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 158.7 | −0.7% | −2.0526 to −0.1367 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 158.7 | −0.7% | −2.0526 to −0.1367 | yes: GAIN |
| response time (ms), mean | 127.4 | 125.9 | −1.2% | −4.6597 to +1.6715 | no |
| response time (ms), 95th percentile | 255.4 | 253.4 | −0.8% | −12.8141 to +8.8221 | no |
| response time (ms), 99th percentile | 361.2 | 354.6 | −1.8% | −32.5992 to +19.5466 | no |
| time over the response line (% of samples) | 0.14 | 0.08878 | −36.6% | −0.1146 to +0.0122 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.8 | +4.800 (native is 0) | +2.9904 to +6.6096 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.3467 | +28.4% | −0.1945 to +0.3478 | no |
| utilisation (used / allocatable) | 0.04093 | 0.037 | −9.6% | −0.0047 to −0.0032 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9823 | 0.8879 | −9.6% | −0.1125 to −0.0763 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02813 | +0.028 (native is 0) | +0.0253 to +0.0309 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9823 | 0.916 | −6.7% | −0.0861 to −0.0465 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.5 | 709.6 | +10.1% | +52.1185 to +78.0761 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.814 | 9.218 | +4.6% | −0.2507 to +1.0596 | no |
| pods started | 5 | 5.5 | +10.0% | −1.2922 to +2.2922 | no |
| pod start wait, total (s) | 8.5 | 7.8 | −8.2% | −3.5222 to +2.1222 | no |
| pod start wait, mean (s) | 1.693 | 1.428 | −15.7% | −0.6141 to +0.0835 | no |
| host CPU busy, the real machine under kind (%) | 30.21 | 27.89 | −7.7% | −2.7728 to −1.8615 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.51 | −0.1% | −0.0044 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 159.3 | +0.6% | +0.4086 to +1.4573 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 159.3 | +0.6% | +0.4086 to +1.4573 | yes: power given |
| response time (ms), mean | 125.6 | 128.6 | +2.4% | −0.6688 to +6.5869 | no |
| response time (ms), 95th percentile | 249.7 | 256.8 | +2.8% | −8.8077 to +23.0187 | no |
| response time (ms), 99th percentile | 348.2 | 353.1 | +1.4% | −24.0064 to +33.6484 | no |
| time over the response line (% of samples) | 0.1397 | 0.06354 | −54.5% | −0.2203 to +0.0680 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5 | +5.000 (native is 0) | +4.0463 to +5.9537 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.545 | +427.4% | +0.2355 to +0.6479 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03675 | 0.04151 | +13.0% | +0.0038 to +0.0057 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.882 | 0.9962 | +13.0% | +0.0910 to +0.1375 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04433 | +0.044 (native is 0) | +0.0403 to +0.0483 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.882 | 1.041 | +18.0% | +0.1328 to +0.1844 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.5 | 636.9 | −10.7% | −88.5375 to −64.7265 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.802 | 9.5 | +7.9% | +0.0424 to +1.3551 | yes: power given |
| pods started | 5.3 | 6.1 | +15.1% | −0.7744 to +2.3744 | no |
| pod start wait, total (s) | 6.8 | 9.5 | +39.7% | +0.2673 to +5.1327 | yes: LOSS |
| pod start wait, mean (s) | 1.29 | 1.533 | +18.8% | −0.0841 to +0.5693 | no |
| host CPU busy, the real machine under kind (%) | 26.75 | 32.25 | +20.6% | +4.6195 to +6.3848 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*