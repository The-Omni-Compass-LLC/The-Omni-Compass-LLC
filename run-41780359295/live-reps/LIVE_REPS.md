# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.511 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 171.5 | 86.56 | 89.33 |
| response time (ms), 95th percentile | 381.7 | 132.2 | 130.1 |
| response time (ms), 99th percentile | 656.4 | 189 | 165.3 |
| time over the response line (% of samples) | 2.751 | 0 | 0.2206 |
| failed requests (%) | 0 | 0 | 0.1239 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | 24 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.2417 | 0 |
| utilisation (used / allocatable) | 0.04183 | 0.03971 | 0.04048 |
| CPU used (cores), mean | 1.004 | 0.9531 | 0.9716 |
| Omni's own CPU (cores), mean | 0 | 0.03902 | 0.03936 |
| CPU used with Omni's own (cores), mean | 1.004 | 0.9921 | 1.011 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658.6 | 687.1 | 673.3 |
| HPA replicas, mean | 8.743 | 9.215 | 9.583 |
| pods started | 5.2 | 3.7 | 9.6 |
| pod start wait, total (s) | 8.3 | 5.8 | 18.6 |
| pod start wait, mean (s) | 1.601 | 1.49 | 1.97 |
| host CPU busy, the real machine under kind (%) | 30.41 | 30.38 | 31.25 |
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
| node-hours | 1.51 | 1.511 | +0.1% | −0.0003 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | −0.2% | −0.6485 to −0.0713 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | −0.2% | −0.6485 to −0.0713 | yes: GAIN |
| response time (ms), mean | 171.5 | 86.56 | −49.5% | −104.8035 to −65.0045 | yes: GAIN |
| response time (ms), 95th percentile | 381.7 | 132.2 | −65.4% | −305.4285 to −193.6605 | yes: GAIN |
| response time (ms), 99th percentile | 656.4 | 189 | −71.2% | −584.2720 to −350.4946 | yes: GAIN |
| time over the response line (% of samples) | 2.751 | 0 | −100.0% | −3.9883 to −1.5136 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | −100.0% | −4.5871 to −1.6129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | +19.400 (native is 0) | +17.8112 to +20.9888 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.2417 | −24.5% | −0.3491 to +0.1925 | no |
| utilisation (used / allocatable) | 0.04183 | 0.03971 | −5.1% | −0.0030 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.004 | 0.9531 | −5.1% | −0.0724 to −0.0295 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03902 | +0.039 (native is 0) | +0.0344 to +0.0436 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.004 | 0.9921 | −1.2% | −0.0300 to +0.0062 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658.6 | 687.1 | +4.3% | +19.1914 to +37.7573 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.743 | 9.215 | +5.4% | +0.1166 to +0.8263 | yes: power given |
| pods started | 5.2 | 3.7 | −28.8% | −2.1952 to −0.8048 | yes: GAIN |
| pod start wait, total (s) | 8.3 | 5.8 | −30.1% | −5.1605 to +0.1605 | no |
| pod start wait, mean (s) | 1.601 | 1.49 | −6.9% | −0.5577 to +0.3358 | no |
| host CPU busy, the real machine under kind (%) | 30.41 | 30.38 | −0.1% | −0.3852 to +0.3246 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.515 | +0.3% | −0.0006 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.6 | +0.2% | −0.2610 to +0.7598 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.6 | +0.2% | −0.2610 to +0.7598 | no |
| response time (ms), mean | 171.5 | 89.33 | −47.9% | −102.2662 to −61.9917 | yes: GAIN |
| response time (ms), 95th percentile | 381.7 | 130.1 | −65.9% | −309.2308 to −194.0212 | yes: GAIN |
| response time (ms), 99th percentile | 656.4 | 165.3 | −74.8% | −614.3023 to −367.8211 | yes: GAIN |
| time over the response line (% of samples) | 2.751 | 0.2206 | −92.0% | −3.7519 to −1.3089 | yes: GAIN |
| failed requests (%) | 0 | 0.1239 | +0.124 (native is 0) | +0.0514 to +0.1965 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0.1 | −96.8% | −4.5816 to −1.4184 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24 | +24.000 (native is 0) | +19.4760 to +28.5240 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0 | −100.0% | −0.5170 to −0.1230 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04183 | 0.04048 | −3.2% | −0.0022 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.004 | 0.9716 | −3.2% | −0.0538 to −0.0111 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03936 | +0.039 (native is 0) | +0.0353 to +0.0434 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.004 | 1.011 | +0.7% | −0.0121 to +0.0260 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658.6 | 673.3 | +2.2% | −0.3177 to +29.6433 | no |
| HPA replicas, mean | 8.743 | 9.583 | +9.6% | +0.7459 to +0.9344 | yes: power given |
| pods started | 5.2 | 9.6 | +84.6% | +3.7968 to +5.0032 | yes: power given |
| pod start wait, total (s) | 8.3 | 18.6 | +124.1% | +6.6363 to +13.9637 | yes: LOSS |
| pod start wait, mean (s) | 1.601 | 1.97 | +23.0% | −0.1418 to +0.8794 | no |
| host CPU busy, the real machine under kind (%) | 30.41 | 31.25 | +2.8% | +0.4535 to +1.2391 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.515 | +0.3% | −0.0019 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.6 | +0.4% | −0.0313 to +1.2499 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.6 | +0.4% | −0.0313 to +1.2499 | no |
| response time (ms), mean | 86.56 | 89.33 | +3.2% | −0.4087 to +5.9588 | no |
| response time (ms), 95th percentile | 132.2 | 130.1 | −1.6% | −5.2006 to +1.0376 | no |
| response time (ms), 99th percentile | 189 | 165.3 | −12.5% | −41.1418 to −6.2150 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.2206 | +0.221 (native is 0) | +0.1524 to +0.2887 | yes: LOSS |
| failed requests (%) | 0 | 0.1239 | +0.124 (native is 0) | +0.0514 to +0.1965 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.4 | 24 | +23.7% | +0.0111 to +9.1889 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 60 | −40.0% | −107.9978 to +27.9978 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2417 | 0 | −100.0% | −0.4315 to −0.0518 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03971 | 0.04048 | +1.9% | +0.0002 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9531 | 0.9716 | +1.9% | +0.0044 to +0.0326 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03902 | 0.03936 | +0.9% | −0.0007 to +0.0014 | no |
| CPU used with Omni's own (cores), mean | 0.9921 | 1.011 | +1.9% | +0.0041 to +0.0336 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 687.1 | 673.3 | −2.0% | −26.2055 to −1.4177 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.215 | 9.583 | +4.0% | +0.0230 to +0.7144 | yes: power given |
| pods started | 3.7 | 9.6 | +159.5% | +4.9796 to +6.8204 | yes: power given |
| pod start wait, total (s) | 5.8 | 18.6 | +220.7% | +8.6867 to +16.9133 | yes: LOSS |
| pod start wait, mean (s) | 1.49 | 1.97 | +32.2% | −0.0146 to +0.9741 | no |
| host CPU busy, the real machine under kind (%) | 30.38 | 31.25 | +2.9% | +0.4673 to +1.2859 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*