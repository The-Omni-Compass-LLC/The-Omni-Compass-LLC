# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.1 | 159.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.1 | 159.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 185.1 | 89.5 | 94.47 |
| response time (ms), 95th percentile | 424.7 | 139.6 | 138.4 |
| response time (ms), 99th percentile | 736.1 | 204.1 | 190.5 |
| time over the response line (% of samples) | 3.737 | 0.0609 | 0.271 |
| failed requests (%) | 0 | 0 | 0.1363 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 0.1 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.9 | 16.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6067 | 0.435 | 0.3767 |
| utilisation (used / allocatable) | 0.04367 | 0.041 | 0.04195 |
| CPU used (cores), mean | 1.048 | 0.9839 | 1.007 |
| Omni's own CPU (cores), mean | 0 | 0.01038 | 0.00973 |
| CPU used with Omni's own (cores), mean | 1.048 | 0.9943 | 1.016 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.9 | 665.1 | 653 |
| HPA replicas, mean | 8.688 | 8.948 | 9.784 |
| pods started | 4.9 | 3.6 | 9.1 |
| pod start wait, total (s) | 8.5 | 6.1 | 17.9 |
| pod start wait, mean (s) | 1.75 | 1.61 | 1.972 |
| host CPU busy, the real machine under kind (%) | 31.57 | 30.4 | 31.11 |
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
| node-hours | 1.51 | 1.51 | −0.0% | −0.0021 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.1 | −0.4% | −1.0827 to −0.2945 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.1 | −0.4% | −1.0827 to −0.2945 | yes: GAIN |
| response time (ms), mean | 185.1 | 89.5 | −51.6% | −115.7624 to −75.4002 | yes: GAIN |
| response time (ms), 95th percentile | 424.7 | 139.6 | −67.1% | −343.7687 to −226.4103 | yes: GAIN |
| response time (ms), 99th percentile | 736.1 | 204.1 | −72.3% | −635.7486 to −428.1372 | yes: GAIN |
| time over the response line (% of samples) | 3.737 | 0.0609 | −98.4% | −4.7406 to −2.6123 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 0.1 | −97.5% | −5.0410 to −2.7590 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.9 | +20.900 (native is 0) | +13.7672 to +28.0328 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6067 | 0.435 | −28.3% | −0.7275 to +0.3841 | no |
| utilisation (used / allocatable) | 0.04367 | 0.041 | −6.1% | −0.0038 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.048 | 0.9839 | −6.1% | −0.0910 to −0.0375 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01038 | +0.010 (native is 0) | +0.0089 to +0.0118 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.048 | 0.9943 | −5.1% | −0.0798 to −0.0279 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.9 | 665.1 | +4.4% | +3.3894 to +52.9681 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.688 | 8.948 | +3.0% | −0.5074 to +1.0278 | no |
| pods started | 4.9 | 3.6 | −26.5% | −3.0859 to +0.4859 | no |
| pod start wait, total (s) | 8.5 | 6.1 | −28.2% | −6.5463 to +1.7463 | no |
| pod start wait, mean (s) | 1.75 | 1.61 | −8.0% | −0.6207 to +0.3407 | no |
| host CPU busy, the real machine under kind (%) | 31.57 | 30.4 | −3.7% | −1.9945 to −0.3319 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.513 | +0.2% | −0.0028 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.7 | −0.1% | −0.5977 to +0.3133 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.7 | −0.1% | −0.5977 to +0.3133 | no |
| response time (ms), mean | 185.1 | 94.47 | −49.0% | −110.1054 to −71.1232 | yes: GAIN |
| response time (ms), 95th percentile | 424.7 | 138.4 | −67.4% | −344.1020 to −228.5420 | yes: GAIN |
| response time (ms), 99th percentile | 736.1 | 190.5 | −74.1% | −648.3251 to −442.8051 | yes: GAIN |
| time over the response line (% of samples) | 3.737 | 0.271 | −92.7% | −4.4996 to −2.4331 | yes: GAIN |
| failed requests (%) | 0 | 0.1363 | +0.136 (native is 0) | +0.0707 to +0.2019 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 0.2 | −95.0% | −5.0064 to −2.5936 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.2 | +16.200 (native is 0) | +13.7267 to +18.6733 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6067 | 0.3767 | −37.9% | −0.7844 to +0.3244 | no |
| utilisation (used / allocatable) | 0.04367 | 0.04195 | −4.0% | −0.0027 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.048 | 1.007 | −4.0% | −0.0656 to −0.0173 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00973 | +0.010 (native is 0) | +0.0091 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.048 | 1.016 | −3.0% | −0.0554 to −0.0080 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.9 | 653 | +2.5% | −5.9048 to +38.1746 | no |
| HPA replicas, mean | 8.688 | 9.784 | +12.6% | +0.6087 to +1.5840 | yes: power given |
| pods started | 4.9 | 9.1 | +85.7% | +3.8984 to +4.5016 | yes: power given |
| pod start wait, total (s) | 8.5 | 17.9 | +110.6% | +7.7073 to +11.0927 | yes: LOSS |
| pod start wait, mean (s) | 1.75 | 1.972 | +12.7% | −0.0334 to +0.4778 | no |
| host CPU busy, the real machine under kind (%) | 31.57 | 31.11 | −1.4% | −1.1349 to +0.2251 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.513 | +0.2% | −0.0039 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.7 | +0.3% | −0.2290 to +1.3219 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.7 | +0.3% | −0.2290 to +1.3219 | no |
| response time (ms), mean | 89.5 | 94.47 | +5.5% | +0.8023 to +9.1316 | yes: LOSS |
| response time (ms), 95th percentile | 139.6 | 138.4 | −0.9% | −4.5974 to +2.1324 | no |
| response time (ms), 99th percentile | 204.1 | 190.5 | −6.7% | −36.0929 to +8.8485 | no |
| time over the response line (% of samples) | 0.0609 | 0.271 | +345.0% | +0.0794 to +0.3407 | yes: LOSS |
| failed requests (%) | 0 | 0.1363 | +0.136 (native is 0) | +0.0707 to +0.2019 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.9 | 16.2 | −22.5% | −13.1505 to +3.7505 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.435 | 0.3767 | −13.4% | −0.6420 to +0.5253 | no |
| utilisation (used / allocatable) | 0.041 | 0.04195 | +2.3% | +0.0002 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9839 | 1.007 | +2.3% | +0.0041 to +0.0415 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.01038 | 0.00973 | −6.3% | −0.0017 to +0.0004 | no |
| CPU used with Omni's own (cores), mean | 0.9943 | 1.016 | +2.2% | +0.0033 to +0.0410 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.1 | 653 | −1.8% | −22.4737 to −1.6139 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.948 | 9.784 | +9.3% | −0.2318 to +1.9041 | no |
| pods started | 3.6 | 9.1 | +152.8% | +3.6763 to +7.3237 | yes: power given |
| pod start wait, total (s) | 6.1 | 17.9 | +193.4% | +7.7564 to +15.8436 | yes: LOSS |
| pod start wait, mean (s) | 1.61 | 1.972 | +22.5% | −0.0141 to +0.7386 | no |
| host CPU busy, the real machine under kind (%) | 30.4 | 31.11 | +2.3% | +0.3252 to +1.0914 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*