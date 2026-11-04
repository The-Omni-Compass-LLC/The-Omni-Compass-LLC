# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.517 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.8 | 521.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.8 | 521.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 311.5 | 189.4 |
| response time (ms), 95th percentile | 823.8 | 441 |
| response time (ms), 99th percentile | 2994 | 2093 |
| time over the response line (% of samples) | 21.75 | 15.86 |
| failed requests (%) | 12.16 | 12.18 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.9 | 26 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.5317 |
| utilisation (used / allocatable) | 0.1085 | 0.1081 |
| CPU used (cores), mean | 2.605 | 2.594 |
| Omni's own CPU (cores), mean | 0 | 0.04697 |
| CPU used with Omni's own (cores), mean | 2.605 | 2.641 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.3 | 283.5 |
| HPA replicas, mean | 9.65 | 12.04 |
| pods started | 4.8 | 10 |
| pod start wait, total (s) | 7.1 | 19.6 |
| pod start wait, mean (s) | 1.481 | 1.977 |
| host CPU busy, the real machine under kind (%) | 72.92 | 74.23 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.517 | 4.518 | +0.0% | −0.0065 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.8 | 521.7 | −0.0% | −1.2267 to +1.1362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.8 | 521.7 | −0.0% | −1.2267 to +1.1362 | no |
| response time (ms), mean | 311.5 | 189.4 | −39.2% | −152.9712 to −91.2087 | yes: GAIN |
| response time (ms), 95th percentile | 823.8 | 441 | −46.5% | −562.8653 to −202.7567 | yes: GAIN |
| response time (ms), 99th percentile | 2994 | 2093 | −30.1% | −1708.1022 to −94.5400 | yes: GAIN |
| time over the response line (% of samples) | 21.75 | 15.86 | −27.1% | −7.9429 to −3.8386 | yes: GAIN |
| failed requests (%) | 12.16 | 12.18 | +0.2% | −0.6858 to +0.7280 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.9 | 26 | −18.5% | −7.8209 to −3.9791 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.3 | +50.300 (native is 0) | +42.7446 to +57.8554 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.5317 | +177.4% | +0.0121 to +0.6679 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1085 | 0.1081 | −0.4% | −0.0016 to +0.0007 | no |
| CPU used (cores), mean | 2.605 | 2.594 | −0.4% | −0.0387 to +0.0178 | no |
| Omni's own CPU (cores), mean | 0 | 0.04697 | +0.047 (native is 0) | +0.0407 to +0.0532 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.605 | 2.641 | +1.4% | +0.0044 to +0.0686 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.3 | 283.5 | +0.8% | −1.1338 to +5.5967 | no |
| HPA replicas, mean | 9.65 | 12.04 | +24.8% | +0.9138 to +3.8731 | yes: power given |
| pods started | 4.8 | 10 | +108.3% | +2.8204 to +7.5796 | yes: power given |
| pod start wait, total (s) | 7.1 | 19.6 | +176.1% | +7.1764 to +17.8236 | yes: LOSS |
| pod start wait, mean (s) | 1.481 | 1.977 | +33.5% | +0.0856 to +0.9063 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.92 | 74.23 | +1.8% | +0.4689 to +2.1593 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*