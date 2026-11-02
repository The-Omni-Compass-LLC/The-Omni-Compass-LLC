# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.524 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 172 | 111 |
| response time (ms), 95th percentile | 360.8 | 220.1 |
| response time (ms), 99th percentile | 525.9 | 349.2 |
| time over the response line (% of samples) | 1.542 | 0.2735 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 544.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1633 |
| utilisation (used / allocatable) | 0.03438 | 0.04849 |
| CPU used (cores), mean | 0.8252 | 1.164 |
| Omni's own CPU (cores), mean | 0 | 0.09586 |
| CPU used with Omni's own (cores), mean | 0.8252 | 1.26 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.3 | 552.4 |
| HPA replicas, mean | 9.705 | 13.82 |
| pods started | 3.2 | 7.8 |
| pod start wait, total (s) | 4.9 | 13.7 |
| pod start wait, mean (s) | 1.5 | 1.74 |
| host CPU busy, the real machine under kind (%) | 25.73 | 39.41 |
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
| node-hours | 1.524 | 1.515 | −0.6% | −0.0133 to −0.0037 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.5 | +1.5% | +1.5715 to +3.0593 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.5 | +1.5% | +1.5715 to +3.0593 | yes: power given |
| response time (ms), mean | 172 | 111 | −35.5% | −74.0700 to −48.0803 | yes: GAIN |
| response time (ms), 95th percentile | 360.8 | 220.1 | −39.0% | −173.3043 to −108.2157 | yes: GAIN |
| response time (ms), 99th percentile | 525.9 | 349.2 | −33.6% | −250.3123 to −103.0847 | yes: GAIN |
| time over the response line (% of samples) | 1.542 | 0.2735 | −82.3% | −2.0809 to −0.4561 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −2.5796 to −0.4204 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 544.6 | +544.600 (native is 0) | +413.7423 to +675.4577 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1633 | −12.5% | −0.2542 to +0.2075 | no |
| utilisation (used / allocatable) | 0.03438 | 0.04849 | +41.0% | +0.0121 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8252 | 1.164 | +41.0% | +0.2913 to +0.3858 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.09586 | +0.096 (native is 0) | +0.0774 to +0.1144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8252 | 1.26 | +52.6% | +0.3747 to +0.4941 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.3 | 552.4 | −27.4% | −232.4434 to −185.3100 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.705 | 13.82 | +42.4% | +2.8699 to +5.3677 | yes: power given |
| pods started | 3.2 | 7.8 | +143.7% | +3.2015 to +5.9985 | yes: power given |
| pod start wait, total (s) | 4.9 | 13.7 | +179.6% | +4.9583 to +12.6417 | yes: LOSS |
| pod start wait, mean (s) | 1.5 | 1.74 | +16.0% | −0.2385 to +0.7190 | no |
| host CPU busy, the real machine under kind (%) | 25.73 | 39.41 | +53.1% | +11.6992 to +15.6505 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*