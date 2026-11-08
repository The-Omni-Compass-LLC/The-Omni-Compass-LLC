# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.512 | 1.508 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.6 | 158.3 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.6 | 158.3 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 133.5 | 137.6 | 133.2 | 138 |
| response time (ms), 95th percentile | 269.6 | 283.1 | 269.1 | 273.5 |
| response time (ms), 99th percentile | 387.5 | 397.1 | 383.4 | 390.8 |
| time over the response line (% of samples) | 0.2935 | 0.4738 | 0.2943 | 0.358 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 6.6 | 6.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.08 | 0.3167 | 0.27 |
| utilisation (used / allocatable) | 0.0374 | 0.04174 | 0.03819 | 0.04305 |
| CPU used (cores), mean | 0.8976 | 1.002 | 0.9166 | 1.033 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03065 | 0.0487 |
| CPU used with Omni's own (cores), mean | 0.8976 | 1.002 | 0.9472 | 1.082 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.9 | 632.9 | 689 | 615.3 |
| HPA replicas, mean | 8.826 | 8.869 | 10.28 | 10.38 |
| pods started | 5.1 | 4.9 | 7.7 | 7.7 |
| pod start wait, total (s) | 8 | 7.9 | 10.7 | 12.6 |
| pod start wait, mean (s) | 1.573 | 1.635 | 1.401 | 1.602 |
| host CPU busy, the real machine under kind (%) | 26.98 | 30.69 | 28.65 | 33.32 |
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
| node-hours | 1.512 | 1.511 | −0.1% | −0.0079 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.8 | +0.1% | −0.5355 to +0.9484 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.8 | +0.1% | −0.5355 to +0.9484 | no |
| response time (ms), mean | 137.6 | 138 | +0.3% | −2.7395 to +3.5023 | no |
| response time (ms), 95th percentile | 283.1 | 273.5 | −3.4% | −23.5334 to +4.1354 | no |
| response time (ms), 99th percentile | 397.1 | 390.8 | −1.6% | −36.7496 to +24.1388 | no |
| time over the response line (% of samples) | 0.4738 | 0.358 | −24.4% | −0.2806 to +0.0490 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | −66.7% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 | +6.500 (native is 0) | +4.9456 to +8.0544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.27 | +237.5% | −0.0319 to +0.4119 | no |
| utilisation (used / allocatable) | 0.04174 | 0.04305 | +3.1% | +0.0005 to +0.0021 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.002 | 1.033 | +3.1% | +0.0120 to +0.0506 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0487 | +0.049 (native is 0) | +0.0429 to +0.0545 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.002 | 1.082 | +8.0% | +0.0569 to +0.1031 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 632.9 | 615.3 | −2.8% | −28.2183 to −6.9976 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.869 | 10.38 | +17.0% | +0.7214 to +2.2953 | yes: power given |
| pods started | 4.9 | 7.7 | +57.1% | +0.9593 to +4.6407 | yes: power given |
| pod start wait, total (s) | 7.9 | 12.6 | +59.5% | +1.4299 to +7.9701 | yes: LOSS |
| pod start wait, mean (s) | 1.635 | 1.602 | −2.0% | −0.3528 to +0.2868 | no |
| host CPU busy, the real machine under kind (%) | 30.69 | 33.32 | +8.6% | +1.8999 to +3.3769 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.1% | −0.0098 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.6 | +0.6% | −0.1348 to +1.9053 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.6 | +0.6% | −0.1348 to +1.9053 | no |
| response time (ms), mean | 133.5 | 137.6 | +3.1% | +1.1346 to +7.1912 | yes: LOSS |
| response time (ms), 95th percentile | 269.6 | 283.1 | +5.0% | +0.5075 to +26.6555 | yes: LOSS |
| response time (ms), 99th percentile | 387.5 | 397.1 | +2.5% | −20.6392 to +39.8214 | no |
| time over the response line (% of samples) | 0.2935 | 0.4738 | +61.4% | +0.0117 to +0.3490 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.08 | −75.3% | −0.5581 to +0.0714 | no |
| utilisation (used / allocatable) | 0.0374 | 0.04174 | +11.6% | +0.0035 to +0.0052 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8976 | 1.002 | +11.6% | +0.0847 to +0.1239 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8976 | 1.002 | +11.6% | +0.0847 to +0.1239 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.9 | 632.9 | −9.8% | −81.5817 to −56.4376 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.826 | 8.869 | +0.5% | −0.0336 to +0.1200 | no |
| pods started | 5.1 | 4.9 | −3.9% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 8 | 7.9 | −1.2% | −1.9607 to +1.7607 | no |
| pod start wait, mean (s) | 1.573 | 1.635 | +3.9% | −0.3967 to +0.5200 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 30.69 | +13.7% | +3.2399 to +4.1732 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.508 | −0.4% | −0.0127 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | −0.2% | −1.0722 to +0.4103 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | −0.2% | −1.0722 to +0.4103 | no |
| response time (ms), mean | 133.5 | 133.2 | −0.2% | −3.3813 to +2.8390 | no |
| response time (ms), 95th percentile | 269.6 | 269.1 | −0.2% | −13.4365 to +12.5565 | no |
| response time (ms), 99th percentile | 387.5 | 383.4 | −1.1% | −35.8618 to +27.5752 | no |
| time over the response line (% of samples) | 0.2935 | 0.2943 | +0.3% | −0.1837 to +0.1853 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.6 | +6.600 (native is 0) | +5.0474 to +8.1526 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.3167 | −2.1% | −0.3806 to +0.3673 | no |
| utilisation (used / allocatable) | 0.0374 | 0.03819 | +2.1% | +0.0002 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8976 | 0.9166 | +2.1% | +0.0050 to +0.0330 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03065 | +0.031 (native is 0) | +0.0273 to +0.0340 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8976 | 0.9472 | +5.5% | +0.0332 to +0.0661 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.9 | 689 | −1.8% | −22.6480 to −3.0880 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.826 | 10.28 | +16.4% | +0.7173 to +2.1809 | yes: power given |
| pods started | 5.1 | 7.7 | +51.0% | +1.0845 to +4.1155 | yes: power given |
| pod start wait, total (s) | 8 | 10.7 | +33.7% | −0.7396 to +6.1396 | no |
| pod start wait, mean (s) | 1.573 | 1.401 | −11.0% | −0.5975 to +0.2528 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 28.65 | +6.2% | +1.0768 to +2.2725 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.508 | −0.3% | −0.0118 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 158.3 | −0.8% | −2.0830 to −0.3494 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 158.3 | −0.8% | −2.0830 to −0.3494 | yes: GAIN |
| response time (ms), mean | 137.6 | 133.2 | −3.2% | −8.3076 to −0.5605 | yes: GAIN |
| response time (ms), 95th percentile | 283.1 | 269.1 | −5.0% | −24.7878 to −3.2552 | yes: GAIN |
| response time (ms), 99th percentile | 397.1 | 383.4 | −3.5% | −45.4228 to +17.9540 | no |
| time over the response line (% of samples) | 0.4738 | 0.2943 | −37.9% | −0.3422 to −0.0168 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | −66.7% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.6 | +6.600 (native is 0) | +5.0474 to +8.1526 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.3167 | +295.8% | +0.0293 to +0.4441 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04174 | 0.03819 | −8.5% | −0.0042 to −0.0029 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.002 | 0.9166 | −8.5% | −0.1008 to −0.0697 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03065 | +0.031 (native is 0) | +0.0273 to +0.0340 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.002 | 0.9472 | −5.5% | −0.0722 to −0.0370 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 632.9 | 689 | +8.9% | +44.4606 to +67.8227 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.869 | 10.28 | +15.9% | +0.6973 to +2.1146 | yes: power given |
| pods started | 4.9 | 7.7 | +57.1% | +1.0544 to +4.5456 | yes: power given |
| pod start wait, total (s) | 7.9 | 10.7 | +35.4% | +0.1924 to +5.4076 | yes: LOSS |
| pod start wait, mean (s) | 1.635 | 1.401 | −14.3% | −0.6118 to +0.1439 | no |
| host CPU busy, the real machine under kind (%) | 30.69 | 28.65 | −6.6% | −2.4364 to −1.6275 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.511 | −0.1% | −0.0099 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.8 | +0.7% | +0.2780 to +1.9055 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.8 | +0.7% | +0.2780 to +1.9055 | yes: power given |
| response time (ms), mean | 133.5 | 138 | +3.4% | +2.0509 to +7.0376 | yes: LOSS |
| response time (ms), 95th percentile | 269.6 | 273.5 | +1.4% | −4.7959 to +12.5609 | no |
| response time (ms), 99th percentile | 387.5 | 390.8 | +0.8% | −23.2600 to +29.8314 | no |
| time over the response line (% of samples) | 0.2935 | 0.358 | +22.0% | −0.0668 to +0.1958 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 | +6.500 (native is 0) | +4.9456 to +8.0544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.27 | −16.5% | −0.4474 to +0.3407 | no |
| utilisation (used / allocatable) | 0.0374 | 0.04305 | +15.1% | +0.0049 to +0.0064 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8976 | 1.033 | +15.1% | +0.1180 to +0.1532 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0487 | +0.049 (native is 0) | +0.0429 to +0.0545 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8976 | 1.082 | +20.5% | +0.1624 to +0.2061 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.9 | 615.3 | −12.3% | −94.5614 to −78.6739 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.826 | 10.38 | +17.6% | +0.7380 to +2.3651 | yes: power given |
| pods started | 5.1 | 7.7 | +51.0% | +1.0845 to +4.1155 | yes: power given |
| pod start wait, total (s) | 8 | 12.6 | +57.5% | +1.0442 to +8.1558 | yes: LOSS |
| pod start wait, mean (s) | 1.573 | 1.602 | +1.8% | −0.2238 to +0.2812 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 33.32 | +23.5% | +5.4078 to +7.2821 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*