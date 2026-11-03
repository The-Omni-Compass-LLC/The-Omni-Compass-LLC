# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.519 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 159.4 | 131.6 |
| response time (ms), 95th percentile | 282.4 | 292.9 |
| response time (ms), 99th percentile | 412.5 | 431 |
| time over the response line (% of samples) | 0.3104 | 0.4689 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1441 | 1503 |
| utilisation (used / allocatable) | 0.06038 | 0.05831 |
| CPU used (cores), mean | 1.449 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0.07696 |
| CPU used with Omni's own (cores), mean | 1.449 | 1.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 463.5 |
| HPA replicas, mean | 2.044 | 2.347 |
| pods started | 0 | 1.1 |
| pod start wait, total (s) | 0 | 2.5 |
| pod start wait, mean (s) | 0 | 0.8867 |
| host CPU busy, the real machine under kind (%) | 46.31 | 47.76 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1509 | 1506 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 185.8 | 220.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 836.1 | 991 |
| queue: job turnaround, submitted to done, mean (s) | 992.5 | 996.4 |
| queue: jobs unfinished at the window's end | 16.5 | 18.2 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| node-hours | 2.519 | 2.508 | −0.4% | −0.0180 to −0.0037 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 271.1 | −0.7% | −2.5753 to −1.2772 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 271.1 | −0.7% | −2.5753 to −1.2772 | yes: GAIN |
| response time (ms), mean | 159.4 | 131.6 | −17.4% | −35.2441 to −20.3791 | yes: GAIN |
| response time (ms), 95th percentile | 282.4 | 292.9 | +3.7% | −5.3705 to +26.3545 | no |
| response time (ms), 99th percentile | 412.5 | 431 | +4.5% | +4.6104 to +32.3178 | yes: LOSS |
| time over the response line (% of samples) | 0.3104 | 0.4689 | +51.1% | +0.0237 to +0.2934 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.9 | +115.900 (native is 0) | +96.3353 to +135.4647 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1441 | 1503 | +4.3% | −10.8367 to +134.0701 | no |
| utilisation (used / allocatable) | 0.06038 | 0.05831 | −3.4% | −0.0034 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.449 | 1.399 | −3.4% | −0.0810 to −0.0181 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07696 | +0.077 (native is 0) | +0.0706 to +0.0833 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.476 | +1.9% | −0.0067 to +0.0614 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 463.5 | +3.3% | +5.1805 to +24.0400 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.044 | 2.347 | +14.8% | +0.0307 to +0.5736 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.1367 to +2.3367 | no |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | −0.3463 to +5.3463 | no |
| pod start wait, mean (s) | 0 | 0.8867 | +0.887 (native is 0) | +0.0576 to +1.7157 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.31 | 47.76 | +3.1% | +0.5302 to +2.3769 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1509 | 1506 | −0.2% | −10.7184 to +4.5184 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 185.8 | 220.6 | +18.8% | −22.3919 to +92.0919 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 836.1 | 991 | +18.5% | −28.3339 to +338.1339 | no |
| queue: job turnaround, submitted to done, mean (s) | 992.5 | 996.4 | +0.4% | −34.7064 to +42.4730 | no |
| queue: jobs unfinished at the window's end | 16.5 | 18.2 | +10.3% | +0.3491 to +3.0509 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*