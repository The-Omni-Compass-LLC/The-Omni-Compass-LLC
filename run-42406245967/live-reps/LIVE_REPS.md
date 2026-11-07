# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.509 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 158.9 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 158.9 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 175.2 | 87.35 | 90.47 |
| response time (ms), 95th percentile | 400.4 | 135.5 | 134.7 |
| response time (ms), 99th percentile | 633 | 198.5 | 177.6 |
| time over the response line (% of samples) | 2.976 | 0.0241 | 0.2919 |
| failed requests (%) | 0 | 0 | 0.136 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | 23.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2467 | 0.1633 | 0 |
| utilisation (used / allocatable) | 0.04226 | 0.04001 | 0.04108 |
| CPU used (cores), mean | 1.014 | 0.9602 | 0.986 |
| Omni's own CPU (cores), mean | 0 | 0.0395 | 0.04007 |
| CPU used with Omni's own (cores), mean | 1.014 | 0.9997 | 1.026 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 645.9 | 674.7 | 659.3 |
| HPA replicas, mean | 8.758 | 9.323 | 9.627 |
| pods started | 5.4 | 3.2 | 9.5 |
| pod start wait, total (s) | 8.6 | 4.8 | 18.6 |
| pod start wait, mean (s) | 1.579 | 1.493 | 1.97 |
| host CPU busy, the real machine under kind (%) | 30.62 | 30.55 | 31.55 |
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
| node-hours | 1.51 | 1.509 | −0.1% | −0.0061 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 158.9 | −0.4% | −1.0787 to −0.2133 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 158.9 | −0.4% | −1.0787 to −0.2133 | yes: GAIN |
| response time (ms), mean | 175.2 | 87.35 | −50.1% | −107.1557 to −68.5684 | yes: GAIN |
| response time (ms), 95th percentile | 400.4 | 135.5 | −66.2% | −319.4608 to −210.4412 | yes: GAIN |
| response time (ms), 99th percentile | 633 | 198.5 | −68.6% | −520.8549 to −348.2009 | yes: GAIN |
| time over the response line (% of samples) | 2.976 | 0.0241 | −99.2% | −4.2415 to −1.6626 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.8775 to −1.9225 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.100 (native is 0) | +16.8773 to +21.3227 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2467 | 0.1633 | −33.8% | −0.3479 to +0.1812 | no |
| utilisation (used / allocatable) | 0.04226 | 0.04001 | −5.3% | −0.0032 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.014 | 0.9602 | −5.3% | −0.0763 to −0.0319 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0395 | +0.039 (native is 0) | +0.0363 to +0.0427 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.014 | 0.9997 | −1.4% | −0.0340 to +0.0048 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 645.9 | 674.7 | +4.5% | +16.7154 to +41.0035 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.758 | 9.323 | +6.5% | +0.2857 to +0.8446 | yes: power given |
| pods started | 5.4 | 3.2 | −40.7% | −3.1417 to −1.2583 | yes: GAIN |
| pod start wait, total (s) | 8.6 | 4.8 | −44.2% | −5.4792 to −2.1208 | yes: GAIN |
| pod start wait, mean (s) | 1.579 | 1.493 | −5.5% | −0.5274 to +0.3550 | no |
| host CPU busy, the real machine under kind (%) | 30.62 | 30.55 | −0.2% | −0.5375 to +0.4083 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.513 | +0.2% | −0.0052 to +0.0112 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.6 | +0.0% | −0.7565 to +0.8736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.6 | +0.0% | −0.7565 to +0.8736 | no |
| response time (ms), mean | 175.2 | 90.47 | −48.4% | −103.6224 to −65.8525 | yes: GAIN |
| response time (ms), 95th percentile | 400.4 | 134.7 | −66.4% | −320.7104 to −210.8816 | yes: GAIN |
| response time (ms), 99th percentile | 633 | 177.6 | −71.9% | −548.0209 to −362.7785 | yes: GAIN |
| time over the response line (% of samples) | 2.976 | 0.2919 | −90.2% | −4.0178 to −1.3507 | yes: GAIN |
| failed requests (%) | 0 | 0.136 | +0.136 (native is 0) | +0.0585 to +0.2136 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0.2 | −94.1% | −4.8450 to −1.5550 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.4 | +23.400 (native is 0) | +18.2617 to +28.5383 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2467 | 0 | −100.0% | −0.5008 to +0.0075 | no |
| utilisation (used / allocatable) | 0.04226 | 0.04108 | −2.8% | −0.0017 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.014 | 0.986 | −2.8% | −0.0416 to −0.0151 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04007 | +0.040 (native is 0) | +0.0369 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.014 | 1.026 | +1.2% | +0.0010 to +0.0225 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 645.9 | 659.3 | +2.1% | +2.3414 to +24.5452 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.758 | 9.627 | +9.9% | +0.8213 to +0.9180 | yes: power given |
| pods started | 5.4 | 9.5 | +75.9% | +3.5722 to +4.6278 | yes: power given |
| pod start wait, total (s) | 8.6 | 18.6 | +116.3% | +7.4099 to +12.5901 | yes: LOSS |
| pod start wait, mean (s) | 1.579 | 1.97 | +24.8% | −0.0371 to +0.8197 | no |
| host CPU busy, the real machine under kind (%) | 30.62 | 31.55 | +3.0% | +0.5570 to +1.3006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.513 | +0.3% | −0.0017 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.6 | +0.4% | +0.0208 to +1.3883 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.6 | +0.4% | +0.0208 to +1.3883 | yes: power given |
| response time (ms), mean | 87.35 | 90.47 | +3.6% | +0.3272 to +5.9220 | yes: LOSS |
| response time (ms), 95th percentile | 135.5 | 134.7 | −0.6% | −2.4064 to +0.7164 | no |
| response time (ms), 99th percentile | 198.5 | 177.6 | −10.5% | −40.8317 to −0.9119 | yes: GAIN |
| time over the response line (% of samples) | 0.0241 | 0.2919 | +1111.4% | +0.1910 to +0.3446 | yes: LOSS |
| failed requests (%) | 0 | 0.136 | +0.136 (native is 0) | +0.0585 to +0.2136 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 23.4 | +22.5% | −0.5987 to +9.1987 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 40 | −50.0% | −107.9978 to +27.9978 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0 | −100.0% | −0.2983 to −0.0284 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04001 | 0.04108 | +2.7% | +0.0005 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9602 | 0.986 | +2.7% | +0.0115 to +0.0400 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.0395 | 0.04007 | +1.4% | +0.0000 to +0.0011 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9997 | 1.026 | +2.6% | +0.0121 to +0.0406 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 674.7 | 659.3 | −2.3% | −23.3404 to −7.4919 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.323 | 9.627 | +3.3% | +0.0343 to +0.5747 | yes: power given |
| pods started | 3.2 | 9.5 | +196.9% | +5.4706 to +7.1294 | yes: power given |
| pod start wait, total (s) | 4.8 | 18.6 | +287.5% | +11.2587 to +16.3413 | yes: LOSS |
| pod start wait, mean (s) | 1.493 | 1.97 | +32.0% | +0.2236 to +0.7313 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.55 | 31.55 | +3.3% | +0.6436 to +1.3431 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*