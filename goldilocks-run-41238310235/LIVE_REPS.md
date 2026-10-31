# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 148.7 | 77.76 |
| response time (ms), 95th percentile | 315 | 114.7 |
| response time (ms), 99th percentile | 448.1 | 150.8 |
| time over the response line (% of samples) | 0.8073 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.3067 |
| utilisation (used / allocatable) | 0.0325 | 0.04726 |
| CPU used (cores), mean | 0.7801 | 1.134 |
| Omni's own CPU (cores), mean | 0 | 0.01082 |
| CPU used with Omni's own (cores), mean | 0.7801 | 1.145 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 568.6 |
| HPA replicas, mean | 9.669 | 11.65 |
| pods started | 2.9 | 5 |
| pod start wait, total (s) | 4.9 | 7 |
| pod start wait, mean (s) | 1.508 | 1.361 |
| host CPU busy, the real machine under kind (%) | 24.2 | 34.31 |
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
| node-hours | 1.516 | 1.516 | +0.0% | −0.0065 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.2 | +2.1% | +2.7241 to +4.0083 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.2 | +2.1% | +2.7241 to +4.0083 | yes: power given |
| response time (ms), mean | 148.7 | 77.76 | −47.7% | −83.4816 to −58.3789 | yes: GAIN |
| response time (ms), 95th percentile | 315 | 114.7 | −63.6% | −223.4484 to −177.0136 | yes: GAIN |
| response time (ms), 99th percentile | 448.1 | 150.8 | −66.3% | −326.4912 to −268.1092 | yes: GAIN |
| time over the response line (% of samples) | 0.8073 | 0.0122 | −98.5% | −1.3793 to −0.2109 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | −100.0% | −1.5048 to +0.3048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.900 (native is 0) | +25.5372 to +46.2628 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.3067 | +29.6% | −0.4833 to +0.6233 | no |
| utilisation (used / allocatable) | 0.0325 | 0.04726 | +45.4% | +0.0120 to +0.0175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7801 | 1.134 | +45.4% | +0.2887 to +0.4194 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01082 | +0.011 (native is 0) | +0.0089 to +0.0128 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7801 | 1.145 | +46.8% | +0.2981 to +0.4317 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.8 | 568.6 | −29.2% | −258.7578 to −209.6002 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.669 | 11.65 | +20.5% | +1.1417 to +2.8222 | yes: power given |
| pods started | 2.9 | 5 | +72.4% | +0.4327 to +3.7673 | yes: power given |
| pod start wait, total (s) | 4.9 | 7 | +42.9% | −1.0533 to +5.2533 | no |
| pod start wait, mean (s) | 1.508 | 1.361 | −9.8% | −0.7338 to +0.4388 | no |
| host CPU busy, the real machine under kind (%) | 24.2 | 34.31 | +41.8% | +8.3000 to +11.9266 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*