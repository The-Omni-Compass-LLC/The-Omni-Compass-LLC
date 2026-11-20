# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.51 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158 | 159 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158 | 159 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 147.8 | 75.54 | 80.85 |
| response time (ms), 95th percentile | 326.2 | 107.8 | 109.5 |
| response time (ms), 99th percentile | 534.5 | 135.3 | 141.3 |
| time over the response line (% of samples) | 1.917 | 0 | 0.3124 |
| failed requests (%) | 0 | 0 | 0.04961 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | 0.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | 28.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1067 | 0.05333 |
| utilisation (used / allocatable) | 0.03746 | 0.03589 | 0.03692 |
| CPU used (cores), mean | 0.8991 | 0.8614 | 0.8861 |
| Omni's own CPU (cores), mean | 0 | 0.03447 | 0.03556 |
| CPU used with Omni's own (cores), mean | 0.8991 | 0.8959 | 0.9216 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.3 | 759.2 | 736.9 |
| HPA replicas, mean | 8.616 | 8.622 | 9.3 |
| pods started | 4.8 | 4.3 | 10.4 |
| pod start wait, total (s) | 7.7 | 5.6 | 18.3 |
| pod start wait, mean (s) | 1.443 | 1.308 | 1.783 |
| host CPU busy, the real machine under kind (%) | 27.56 | 27.49 | 28.43 |
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
| node-hours | 1.512 | 1.51 | −0.1% | −0.0032 to −0.0008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158 | −0.4% | −0.8998 to −0.2721 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158 | −0.4% | −0.8998 to −0.2721 | yes: GAIN |
| response time (ms), mean | 147.8 | 75.54 | −48.9% | −93.7343 to −50.7886 | yes: GAIN |
| response time (ms), 95th percentile | 326.2 | 107.8 | −66.9% | −282.3386 to −154.3874 | yes: GAIN |
| response time (ms), 99th percentile | 534.5 | 135.3 | −74.7% | −524.0736 to −274.2686 | yes: GAIN |
| time over the response line (% of samples) | 1.917 | 0 | −100.0% | −3.2682 to −0.5661 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −2.9005 to −0.0995 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +16.9615 to +19.8385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1067 | 0.0% | raw −0.2379 to +0.2379 | STEADY, the same (to nine decimal places) |
| utilisation (used / allocatable) | 0.03746 | 0.03589 | −4.2% | −0.0026 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8991 | 0.8614 | −4.2% | −0.0615 to −0.0138 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03447 | +0.034 (native is 0) | +0.0305 to +0.0384 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8991 | 0.8959 | −0.3% | −0.0254 to +0.0191 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.3 | 759.2 | +3.8% | +9.9510 to +45.8196 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.616 | 8.622 | +0.1% | −0.3186 to +0.3321 | no |
| pods started | 4.8 | 4.3 | −10.4% | −2.0906 to +1.0906 | no |
| pod start wait, total (s) | 7.7 | 5.6 | −27.3% | −4.9702 to +0.7702 | no |
| pod start wait, mean (s) | 1.443 | 1.308 | −9.4% | −0.6948 to +0.4248 | no |
| host CPU busy, the real machine under kind (%) | 27.56 | 27.49 | −0.3% | −0.6962 to +0.5573 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.517 | +0.3% | +0.0036 to +0.0060 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 159 | +0.2% | +0.0371 to +0.6340 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 159 | +0.2% | +0.0371 to +0.6340 | yes: power given |
| response time (ms), mean | 147.8 | 80.85 | −45.3% | −87.5918 to −46.3073 | yes: GAIN |
| response time (ms), 95th percentile | 326.2 | 109.5 | −66.4% | −280.3006 to −153.0224 | yes: GAIN |
| response time (ms), 99th percentile | 534.5 | 141.3 | −73.6% | −517.9085 to −268.4377 | yes: GAIN |
| time over the response line (% of samples) | 1.917 | 0.3124 | −83.7% | −3.0021 to −0.2075 | yes: GAIN |
| failed requests (%) | 0 | 0.04961 | +0.050 (native is 0) | −0.0125 to +0.1117 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0.6 | −60.0% | −2.5673 to +0.7673 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.3 | +28.300 (native is 0) | +22.6975 to +33.9025 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.05333 | −50.0% | −0.2699 to +0.1632 | no |
| utilisation (used / allocatable) | 0.03746 | 0.03692 | −1.4% | −0.0015 to +0.0004 | no |
| CPU used (cores), mean | 0.8991 | 0.8861 | −1.4% | −0.0358 to +0.0099 | no |
| Omni's own CPU (cores), mean | 0 | 0.03556 | +0.036 (native is 0) | +0.0316 to +0.0395 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8991 | 0.9216 | +2.5% | +0.0000 to +0.0451 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.3 | 736.9 | +0.8% | −11.5020 to +22.6086 | no |
| HPA replicas, mean | 8.616 | 9.3 | +7.9% | +0.4317 to +0.9361 | yes: power given |
| pods started | 4.8 | 10.4 | +116.7% | +4.2015 to +6.9985 | yes: power given |
| pod start wait, total (s) | 7.7 | 18.3 | +137.7% | +6.7524 to +14.4476 | yes: LOSS |
| pod start wait, mean (s) | 1.443 | 1.783 | +23.5% | −0.2328 to +0.9123 | no |
| host CPU busy, the real machine under kind (%) | 27.56 | 28.43 | +3.1% | +0.2761 to +1.4518 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.517 | +0.5% | +0.0051 to +0.0086 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 159 | +0.6% | +0.5706 to +1.2724 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 159 | +0.6% | +0.5706 to +1.2724 | yes: power given |
| response time (ms), mean | 75.54 | 80.85 | +7.0% | +1.1221 to +9.5018 | yes: LOSS |
| response time (ms), 95th percentile | 107.8 | 109.5 | +1.6% | −1.2358 to +4.6388 | no |
| response time (ms), 99th percentile | 135.3 | 141.3 | +4.4% | −4.0347 to +16.0307 | no |
| time over the response line (% of samples) | 0 | 0.3124 | +0.312 (native is 0) | +0.2218 to +0.4029 | yes: LOSS |
| failed requests (%) | 0 | 0.04961 | +0.050 (native is 0) | −0.0125 to +0.1117 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 28.3 | +53.8% | +3.7703 to +16.0297 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 0 | −100.0% | −100.0000 to −100.0000 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.05333 | −50.0% | −0.2878 to +0.1811 | no |
| utilisation (used / allocatable) | 0.03589 | 0.03692 | +2.9% | +0.0001 to +0.0020 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8614 | 0.8861 | +2.9% | +0.0015 to +0.0478 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03447 | 0.03556 | +3.2% | +0.0004 to +0.0017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8959 | 0.9216 | +2.9% | +0.0021 to +0.0494 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 759.2 | 736.9 | −2.9% | −44.8359 to +0.1718 | no |
| HPA replicas, mean | 8.622 | 9.3 | +7.9% | +0.4093 to +0.9451 | yes: power given |
| pods started | 4.3 | 10.4 | +141.9% | +4.8182 to +7.3818 | yes: power given |
| pod start wait, total (s) | 5.6 | 18.3 | +226.8% | +10.2440 to +15.1560 | yes: LOSS |
| pod start wait, mean (s) | 1.308 | 1.783 | +36.3% | +0.1915 to +0.7580 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 27.49 | 28.43 | +3.4% | +0.1801 to +1.6867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*