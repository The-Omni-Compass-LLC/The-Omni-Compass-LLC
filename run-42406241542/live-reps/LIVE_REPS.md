# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154.3 | 80.02 |
| response time (ms), 95th percentile | 352.8 | 121.4 |
| response time (ms), 99th percentile | 563.8 | 164.4 |
| time over the response line (% of samples) | 2.364 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.1917 |
| utilisation (used / allocatable) | 0.03883 | 0.03687 |
| CPU used (cores), mean | 0.932 | 0.8848 |
| Omni's own CPU (cores), mean | 0 | 0.03656 |
| CPU used with Omni's own (cores), mean | 0.932 | 0.9214 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.4 | 747.7 |
| HPA replicas, mean | 8.526 | 8.802 |
| pods started | 5.2 | 3.7 |
| pod start wait, total (s) | 8 | 5.2 |
| pod start wait, mean (s) | 1.566 | 1.41 |
| host CPU busy, the real machine under kind (%) | 28.34 | 28.57 |
| host cores (the real machine under kind) | 4 | 4 |
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
| node-hours | 1.513 | 1.513 | 0.0% | raw −0.0016 to +0.0016 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.3% | −0.6888 to −0.1888 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.3% | −0.6888 to −0.1888 | yes: GAIN |
| response time (ms), mean | 154.3 | 80.02 | −48.1% | −98.3249 to −50.1812 | yes: GAIN |
| response time (ms), 95th percentile | 352.8 | 121.4 | −65.6% | −305.6984 to −157.0366 | yes: GAIN |
| response time (ms), 99th percentile | 563.8 | 164.4 | −70.9% | −531.7254 to −267.2418 | yes: GAIN |
| time over the response line (% of samples) | 2.364 | 0 | −100.0% | −3.8836 to −0.8452 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.5790 to −0.8210 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.2 | +18.200 (native is 0) | +17.1444 to +19.2556 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.1917 | −36.5% | −0.4889 to +0.2689 | no |
| utilisation (used / allocatable) | 0.03883 | 0.03687 | −5.1% | −0.0031 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.932 | 0.8848 | −5.1% | −0.0745 to −0.0199 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03656 | +0.037 (native is 0) | +0.0320 to +0.0411 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.932 | 0.9214 | −1.1% | −0.0337 to +0.0125 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.4 | 747.7 | +3.5% | +9.2461 to +41.2857 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.526 | 8.802 | +3.2% | −0.0206 to +0.5736 | no |
| pods started | 5.2 | 3.7 | −28.8% | −2.7274 to −0.2726 | yes: GAIN |
| pod start wait, total (s) | 8 | 5.2 | −35.0% | −5.4076 to −0.1924 | yes: GAIN |
| pod start wait, mean (s) | 1.566 | 1.41 | −10.0% | −0.6066 to +0.2942 | no |
| host CPU busy, the real machine under kind (%) | 28.34 | 28.57 | +0.8% | −0.2030 to +0.6565 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*