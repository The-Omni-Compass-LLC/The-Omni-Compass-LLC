# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.7 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.7 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 153.9 | 79.86 | 83.34 |
| response time (ms), 95th percentile | 344.7 | 118.4 | 117 |
| response time (ms), 99th percentile | 567.4 | 156.7 | 151.6 |
| time over the response line (% of samples) | 1.992 | 0.01198 | 0.3155 |
| failed requests (%) | 0 | 0 | 0.08673 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | 0.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | 28.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 28.57 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.195 | 0.1067 |
| utilisation (used / allocatable) | 0.03856 | 0.03708 | 0.03771 |
| CPU used (cores), mean | 0.9254 | 0.8899 | 0.905 |
| Omni's own CPU (cores), mean | 0 | 0.03619 | 0.03653 |
| CPU used with Omni's own (cores), mean | 0.9254 | 0.9261 | 0.9415 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.5 | 729.6 | 717.7 |
| HPA replicas, mean | 8.547 | 8.854 | 9.426 |
| pods started | 5.6 | 4.5 | 10.1 |
| pod start wait, total (s) | 8.2 | 6.6 | 16.2 |
| pod start wait, mean (s) | 1.47 | 1.349 | 1.629 |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.7 | 29.11 |
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
| node-hours | 1.514 | 1.514 | 0.0% | raw −0.0014 to +0.0014 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.7 | −0.2% | −0.5541 to −0.1677 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.7 | −0.2% | −0.5541 to −0.1677 | yes: GAIN |
| response time (ms), mean | 153.9 | 79.86 | −48.1% | −91.3505 to −56.6599 | yes: GAIN |
| response time (ms), 95th percentile | 344.7 | 118.4 | −65.7% | −273.8350 to −178.8070 | yes: GAIN |
| response time (ms), 99th percentile | 567.4 | 156.7 | −72.4% | −514.2069 to −307.0037 | yes: GAIN |
| time over the response line (% of samples) | 1.992 | 0.01198 | −99.4% | −2.9938 to −0.9657 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.1367 to −0.6633 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +16.5492 to +21.8508 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.195 | +265.6% | −0.1444 to +0.4277 | no |
| utilisation (used / allocatable) | 0.03856 | 0.03708 | −3.8% | −0.0025 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9254 | 0.8899 | −3.8% | −0.0594 to −0.0116 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03619 | +0.036 (native is 0) | +0.0316 to +0.0408 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9254 | 0.9261 | +0.1% | −0.0189 to +0.0203 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.5 | 729.6 | +2.5% | −1.2465 to +37.4349 | no |
| HPA replicas, mean | 8.547 | 8.854 | +3.6% | −0.1027 to +0.7169 | no |
| pods started | 5.6 | 4.5 | −19.6% | −2.2410 to +0.0410 | no |
| pod start wait, total (s) | 8.2 | 6.6 | −19.5% | −4.4652 to +1.2652 | no |
| pod start wait, mean (s) | 1.47 | 1.349 | −8.2% | −0.6648 to +0.4224 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.7 | +1.2% | +0.0331 to +0.6489 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0076 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | −0.1% | −0.9675 to +0.6057 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | −0.1% | −0.9675 to +0.6057 | no |
| response time (ms), mean | 153.9 | 83.34 | −45.8% | −88.0421 to −53.0168 | yes: GAIN |
| response time (ms), 95th percentile | 344.7 | 117 | −66.1% | −276.9064 to −178.4426 | yes: GAIN |
| response time (ms), 99th percentile | 567.4 | 151.6 | −73.3% | −523.5073 to −307.9031 | yes: GAIN |
| time over the response line (% of samples) | 1.992 | 0.3155 | −84.2% | −2.6892 to −0.6633 | yes: GAIN |
| failed requests (%) | 0 | 0.08673 | +0.087 (native is 0) | +0.0026 to +0.1709 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0.7 | −63.2% | −2.5403 to +0.1403 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.400 (native is 0) | +23.4649 to +33.3351 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.1067 | +100.0% | −0.1220 to +0.2286 | no |
| utilisation (used / allocatable) | 0.03856 | 0.03771 | −2.2% | −0.0018 to +0.0001 | no |
| CPU used (cores), mean | 0.9254 | 0.905 | −2.2% | −0.0438 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.03653 | +0.037 (native is 0) | +0.0323 to +0.0407 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9254 | 0.9415 | +1.7% | −0.0056 to +0.0378 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.5 | 717.7 | +0.9% | −22.0668 to +34.4932 | no |
| HPA replicas, mean | 8.547 | 9.426 | +10.3% | +0.6569 to +1.1004 | yes: power given |
| pods started | 5.6 | 10.1 | +80.4% | +3.5315 to +5.4685 | yes: power given |
| pod start wait, total (s) | 8.2 | 16.2 | +97.6% | +5.4099 to +10.5901 | yes: LOSS |
| pod start wait, mean (s) | 1.47 | 1.629 | +10.8% | −0.1964 to +0.5135 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 29.11 | +2.7% | +0.1378 to +1.3670 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0075 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.9 | +0.1% | −0.5762 to +0.9362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.9 | +0.1% | −0.5762 to +0.9362 | no |
| response time (ms), mean | 79.86 | 83.34 | +4.4% | +0.8994 to +6.0522 | yes: LOSS |
| response time (ms), 95th percentile | 118.4 | 117 | −1.1% | −4.9465 to +2.2395 | no |
| response time (ms), 99th percentile | 156.7 | 151.6 | −3.3% | −13.3240 to +3.1242 | no |
| time over the response line (% of samples) | 0.01198 | 0.3155 | +2534.1% | +0.2107 to +0.3963 | yes: LOSS |
| failed requests (%) | 0 | 0.08673 | +0.087 (native is 0) | +0.0026 to +0.1709 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.7 | +0.700 (native is 0) | +0.3545 to +1.0455 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 28.4 | +47.9% | +3.3908 to +15.0092 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 28.57 | −71.4% | −116.5580 to −26.2991 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.195 | 0.1067 | −45.3% | −0.4004 to +0.2238 | no |
| utilisation (used / allocatable) | 0.03708 | 0.03771 | +1.7% | −0.0003 to +0.0016 | no |
| CPU used (cores), mean | 0.8899 | 0.905 | +1.7% | −0.0072 to +0.0374 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.03653 | +0.9% | −0.0004 to +0.0011 | no |
| CPU used with Omni's own (cores), mean | 0.9261 | 0.9415 | +1.7% | −0.0069 to +0.0378 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.6 | 717.7 | −1.6% | −29.7064 to +5.9444 | no |
| HPA replicas, mean | 8.854 | 9.426 | +6.5% | +0.0232 to +1.1199 | yes: power given |
| pods started | 4.5 | 10.1 | +124.4% | +4.2015 to +6.9985 | yes: power given |
| pod start wait, total (s) | 6.6 | 16.2 | +145.5% | +5.8877 to +13.3123 | yes: LOSS |
| pod start wait, mean (s) | 1.349 | 1.629 | +20.7% | −0.2357 to +0.7952 | no |
| host CPU busy, the real machine under kind (%) | 28.7 | 29.11 | +1.4% | −0.1737 to +0.9965 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*