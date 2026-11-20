# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.509 | 1.51 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 163.2 | 83.71 | 87.06 |
| response time (ms), 95th percentile | 363.2 | 123 | 122.3 |
| response time (ms), 99th percentile | 581.1 | 174.5 | 159.1 |
| time over the response line (% of samples) | 2.215 | 0.01212 | 0.302 |
| failed requests (%) | 0 | 0 | 0.07408 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.5 | 26.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 37.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.28 | 0.2183 | 0 |
| utilisation (used / allocatable) | 0.04055 | 0.03886 | 0.03955 |
| CPU used (cores), mean | 0.9732 | 0.9326 | 0.9492 |
| Omni's own CPU (cores), mean | 0 | 0.03786 | 0.03845 |
| CPU used with Omni's own (cores), mean | 0.9732 | 0.9704 | 0.9877 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.8 | 689.7 | 677.6 |
| HPA replicas, mean | 8.776 | 9.173 | 9.602 |
| pods started | 5.4 | 5 | 10 |
| pod start wait, total (s) | 8.2 | 7.7 | 17.5 |
| pod start wait, mean (s) | 1.518 | 1.52 | 1.747 |
| host CPU busy, the real machine under kind (%) | 29.67 | 29.88 | 30.54 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.0% | −0.0015 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | −0.2% | −0.6958 to −0.0257 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | −0.2% | −0.6958 to −0.0257 | yes: GAIN |
| response time (ms), mean | 163.2 | 83.71 | −48.7% | −97.1938 to −61.6871 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 123 | −66.1% | −291.2563 to −189.1997 | yes: GAIN |
| response time (ms), 99th percentile | 581.1 | 174.5 | −70.0% | −492.9540 to −320.2396 | yes: GAIN |
| time over the response line (% of samples) | 2.215 | 0.01212 | −99.5% | −3.5397 to −0.8651 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.4306 to −0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.5 | +20.500 (native is 0) | +18.9094 to +22.0906 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.28 | 0.2183 | −22.0% | −0.3946 to +0.2712 | no |
| utilisation (used / allocatable) | 0.04055 | 0.03886 | −4.2% | −0.0027 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9732 | 0.9326 | −4.2% | −0.0637 to −0.0175 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03786 | +0.038 (native is 0) | +0.0335 to +0.0422 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9732 | 0.9704 | −0.3% | −0.0228 to +0.0173 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.8 | 689.7 | +3.4% | +10.8784 to +34.9494 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.776 | 9.173 | +4.5% | +0.0095 to +0.7844 | yes: power given |
| pods started | 5.4 | 5 | −7.4% | −0.9001 to +0.1001 | no |
| pod start wait, total (s) | 8.2 | 7.7 | −6.1% | −2.2276 to +1.2276 | no |
| pod start wait, mean (s) | 1.518 | 1.52 | +0.1% | −0.2747 to +0.2785 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 29.88 | +0.7% | −0.2118 to +0.6221 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.516 | +0.4% | +0.0048 to +0.0082 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.5 | +0.3% | +0.2539 to +0.6749 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.5 | +0.3% | +0.2539 to +0.6749 | yes: power given |
| response time (ms), mean | 163.2 | 87.06 | −46.6% | −94.9505 to −57.2463 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 122.3 | −66.3% | −292.3608 to −189.4612 | yes: GAIN |
| response time (ms), 99th percentile | 581.1 | 159.1 | −72.6% | −521.9339 to −322.0185 | yes: GAIN |
| time over the response line (% of samples) | 2.215 | 0.302 | −86.4% | −3.3281 to −0.4970 | yes: GAIN |
| failed requests (%) | 0 | 0.07408 | +0.074 (native is 0) | +0.0122 to +0.1360 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0.5 | −75.0% | −3.2922 to +0.2922 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +20.4883 to +32.1117 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.28 | 0 | −100.0% | −0.6214 to +0.0614 | no |
| utilisation (used / allocatable) | 0.04055 | 0.03955 | −2.5% | −0.0018 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9732 | 0.9492 | −2.5% | −0.0443 to −0.0035 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03845 | +0.038 (native is 0) | +0.0346 to +0.0423 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9732 | 0.9877 | +1.5% | −0.0025 to +0.0316 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.8 | 677.6 | +1.6% | −1.4779 to +23.1135 | no |
| HPA replicas, mean | 8.776 | 9.602 | +9.4% | +0.6922 to +0.9606 | yes: power given |
| pods started | 5.4 | 10 | +85.2% | +3.7604 to +5.4396 | yes: power given |
| pod start wait, total (s) | 8.2 | 17.5 | +113.4% | +6.5804 to +12.0196 | yes: LOSS |
| pod start wait, mean (s) | 1.518 | 1.747 | +15.1% | −0.0737 to +0.5308 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 30.54 | +2.9% | +0.6013 to +1.1226 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.516 | +0.4% | +0.0048 to +0.0075 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.5 | +0.5% | +0.5758 to +1.0745 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.5 | +0.5% | +0.5758 to +1.0745 | yes: power given |
| response time (ms), mean | 83.71 | 87.06 | +4.0% | +0.6216 to +6.0625 | yes: LOSS |
| response time (ms), 95th percentile | 123 | 122.3 | −0.6% | −2.4336 to +1.0676 | no |
| response time (ms), 99th percentile | 174.5 | 159.1 | −8.8% | −33.7762 to +3.0174 | no |
| time over the response line (% of samples) | 0.01212 | 0.302 | +2391.2% | +0.1990 to +0.3807 | yes: LOSS |
| failed requests (%) | 0 | 0.07408 | +0.074 (native is 0) | +0.0122 to +0.1360 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 20.5 | 26.3 | +28.3% | −0.5246 to +12.1246 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 37.5 | −62.5% | −105.7751 to −19.2249 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0 | −100.0% | −0.4162 to −0.0205 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03886 | 0.03955 | +1.8% | +0.0001 to +0.0013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9326 | 0.9492 | +1.8% | +0.0018 to +0.0316 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03786 | 0.03845 | +1.6% | −0.0003 to +0.0015 | no |
| CPU used with Omni's own (cores), mean | 0.9704 | 0.9877 | +1.8% | +0.0023 to +0.0322 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.7 | 677.6 | −1.8% | −21.5288 to −2.6633 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.173 | 9.602 | +4.7% | +0.0294 to +0.8294 | yes: power given |
| pods started | 5 | 10 | +100.0% | +4.2460 to +5.7540 | yes: power given |
| pod start wait, total (s) | 7.7 | 17.5 | +127.3% | +7.0440 to +12.5560 | yes: LOSS |
| pod start wait, mean (s) | 1.52 | 1.747 | +14.9% | −0.1418 to +0.5951 | no |
| host CPU busy, the real machine under kind (%) | 29.88 | 30.54 | +2.2% | +0.3780 to +0.9357 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*