# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.51 | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159 | 159.1 | 159.2 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159 | 159.1 | 159.2 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 161.7 | 160.5 | 157.6 | 155.8 | 83.47 |
| response time (ms), 95th percentile | 361.2 | 356.2 | 354.5 | 343.4 | 122.1 |
| response time (ms), 99th percentile | 560.9 | 562.3 | 558.5 | 553.7 | 162.9 |
| time over the response line (% of samples) | 1.732 | 1.828 | 2.069 | 1.96 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 1.8 | 2 | 2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 20.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.2217 | 0.08 | 0.1067 | 0.2483 |
| utilisation (used / allocatable) | 0.04053 | 0.04045 | 0.0404 | 0.0403 | 0.03868 |
| CPU used (cores), mean | 0.9728 | 0.9708 | 0.9696 | 0.9673 | 0.9284 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03779 |
| CPU used with Omni's own (cores), mean | 0.9728 | 0.9708 | 0.9696 | 0.9673 | 0.9662 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 659 | 660.3 | 660.5 | 663.6 | 686.3 |
| HPA replicas, mean | 8.873 | 9.167 | 9.64 | 10 | 9.168 |
| pods started | 5.1 | 4.2 | 2.2 | 0 | 4.3 |
| pod start wait, total (s) | 7.7 | 6.6 | 3.4 | 0 | 6.4 |
| pod start wait, mean (s) | 1.553 | 1.605 | 1.383 | 0 | 1.477 |
| host CPU busy, the real machine under kind (%) | 29.73 | 29.52 | 29.65 | 29.5 | 29.88 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan |

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
| node-hours | 1.51 | 1.512 | +0.1% | −0.0004 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.8 | −0.2% | −0.5108 to −0.1004 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.8 | −0.2% | −0.5108 to −0.1004 | yes: GAIN |
| response time (ms), mean | 161.7 | 83.47 | −48.4% | −90.3530 to −66.1374 | yes: GAIN |
| response time (ms), 95th percentile | 361.2 | 122.1 | −66.2% | −270.5859 to −207.6081 | yes: GAIN |
| response time (ms), 99th percentile | 560.9 | 162.9 | −71.0% | −477.9423 to −318.0257 | yes: GAIN |
| time over the response line (% of samples) | 1.732 | 0.01212 | −99.3% | −2.8026 to −0.6363 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.1 | +20.100 (native is 0) | +18.8633 to +21.3367 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.2483 | +30.7% | −0.1637 to +0.2804 | no |
| utilisation (used / allocatable) | 0.04053 | 0.03868 | −4.6% | −0.0027 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9728 | 0.9284 | −4.6% | −0.0638 to −0.0249 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03779 | +0.038 (native is 0) | +0.0332 to +0.0423 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9728 | 0.9662 | −0.7% | −0.0227 to +0.0096 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 659 | 686.3 | +4.1% | +18.7892 to +35.7982 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.873 | 9.168 | +3.3% | −0.0896 to +0.6801 | no |
| pods started | 5.1 | 4.3 | −15.7% | −1.6793 to +0.0793 | no |
| pod start wait, total (s) | 7.7 | 6.4 | −16.9% | −3.6855 to +1.0855 | no |
| pod start wait, mean (s) | 1.553 | 1.477 | −4.9% | −0.5491 to +0.3957 | no |
| host CPU busy, the real machine under kind (%) | 29.73 | 29.88 | +0.5% | −0.1957 to +0.5078 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 361.2 | 560.9 | 8.873 | 0.9728 | 6 |
| Native tuned, HPA target 40 | 356.2 | 562.3 | 9.167 | 0.9708 | 6 |
| Native tuned, HPA target 30 | 354.5 | 558.5 | 9.64 | 0.9696 | 6 |
| Native tuned, HPA target 20 | 343.4 | 553.7 | 10 | 0.9673 | 6 |
| omni | 122.1 | 162.9 | 9.168 | 0.9662 | 6 |

- omni (p95 122.1 ms): no native setting tried reached it; the lowest native p95 is 343.4 ms (Native tuned, HPA target 20).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*