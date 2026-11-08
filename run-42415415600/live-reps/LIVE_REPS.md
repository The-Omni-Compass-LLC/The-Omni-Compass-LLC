# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 317.2 | 203.1 |
| response time (ms), 95th percentile | 833.3 | 433.4 |
| response time (ms), 99th percentile | 2773 | 3024 |
| time over the response line (% of samples) | 21.1 | 14.06 |
| failed requests (%) | 10.66 | 10.4 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.2 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3567 | 0.6617 |
| utilisation (used / allocatable) | 0.1081 | 0.1079 |
| CPU used (cores), mean | 2.594 | 2.591 |
| Omni's own CPU (cores), mean | 0 | 0.04739 |
| CPU used with Omni's own (cores), mean | 2.594 | 2.638 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.2 | 273.5 |
| HPA replicas, mean | 9.735 | 12.72 |
| pods started | 4.2 | 9.7 |
| pod start wait, total (s) | 7.2 | 16.8 |
| pod start wait, mean (s) | 1.577 | 1.714 |
| host CPU busy, the real machine under kind (%) | 72.63 | 74.19 |
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
| node-hours | 4.514 | 4.514 | +0.0% | −0.0077 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.3 | +0.0% | −1.2611 to +1.3604 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.3 | +0.0% | −1.2611 to +1.3604 | no |
| response time (ms), mean | 317.2 | 203.1 | −36.0% | −138.3588 to −89.9114 | yes: GAIN |
| response time (ms), 95th percentile | 833.3 | 433.4 | −48.0% | −494.6820 to −304.9800 | yes: GAIN |
| response time (ms), 99th percentile | 2773 | 3024 | +9.0% | −1071.5209 to +1572.2119 | no |
| time over the response line (% of samples) | 21.1 | 14.06 | −33.4% | −8.6604 to −5.4143 | yes: GAIN |
| failed requests (%) | 10.66 | 10.4 | −2.5% | −1.0323 to +0.4985 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.2 | 25 | −22.4% | −9.2176 to −5.1824 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.4 | +54.400 (native is 0) | +51.3802 to +57.4198 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3567 | 0.6617 | +85.5% | −0.0154 to +0.6254 | no |
| utilisation (used / allocatable) | 0.1081 | 0.1079 | −0.2% | −0.0022 to +0.0018 | no |
| CPU used (cores), mean | 2.594 | 2.591 | −0.2% | −0.0518 to +0.0440 | no |
| Omni's own CPU (cores), mean | 0 | 0.04739 | +0.047 (native is 0) | +0.0434 to +0.0514 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.594 | 2.638 | +1.7% | −0.0041 to +0.0910 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.2 | 273.5 | +0.1% | −4.9732 to +5.6618 | no |
| HPA replicas, mean | 9.735 | 12.72 | +30.7% | +2.1818 to +3.7912 | yes: power given |
| pods started | 4.2 | 9.7 | +131.0% | +4.1407 to +6.8593 | yes: power given |
| pod start wait, total (s) | 7.2 | 16.8 | +133.3% | +6.3798 to +12.8202 | yes: LOSS |
| pod start wait, mean (s) | 1.577 | 1.714 | +8.7% | −0.3262 to +0.6004 | no |
| host CPU busy, the real machine under kind (%) | 72.63 | 74.19 | +2.1% | +0.3088 to +2.8071 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*