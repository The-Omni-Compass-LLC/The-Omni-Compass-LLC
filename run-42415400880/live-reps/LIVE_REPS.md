# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 171.6 | 85.43 |
| response time (ms), 95th percentile | 393.4 | 131.4 |
| response time (ms), 99th percentile | 664.1 | 182.2 |
| time over the response line (% of samples) | 3.112 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5067 | 0.2167 |
| utilisation (used / allocatable) | 0.04123 | 0.03903 |
| CPU used (cores), mean | 0.9896 | 0.9368 |
| Omni's own CPU (cores), mean | 0 | 0.03993 |
| CPU used with Omni's own (cores), mean | 0.9896 | 0.9767 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 675.7 | 705.5 |
| HPA replicas, mean | 8.713 | 9.123 |
| pods started | 5.3 | 3.8 |
| pod start wait, total (s) | 13 | 9.8 |
| pod start wait, mean (s) | 2.37 | 2.15 |
| host CPU busy, the real machine under kind (%) | 30.26 | 30.32 |
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
| node-hours | 1.513 | 1.513 | +0.0% | −0.0008 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.1 | −0.3% | −0.7762 to −0.1139 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.1 | −0.3% | −0.7762 to −0.1139 | yes: GAIN |
| response time (ms), mean | 171.6 | 85.43 | −50.2% | −108.0143 to −64.2823 | yes: GAIN |
| response time (ms), 95th percentile | 393.4 | 131.4 | −66.6% | −324.9094 to −199.2096 | yes: GAIN |
| response time (ms), 99th percentile | 664.1 | 182.2 | −72.6% | −599.9416 to −363.7136 | yes: GAIN |
| time over the response line (% of samples) | 3.112 | 0 | −100.0% | −4.4093 to −1.8143 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | −100.0% | −4.6924 to −1.9076 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +17.4914 to +20.3086 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5067 | 0.2167 | −57.2% | −0.6584 to +0.0784 | no |
| utilisation (used / allocatable) | 0.04123 | 0.03903 | −5.3% | −0.0033 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9896 | 0.9368 | −5.3% | −0.0791 to −0.0264 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03993 | +0.040 (native is 0) | +0.0356 to +0.0443 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9896 | 0.9767 | −1.3% | −0.0370 to +0.0113 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 675.7 | 705.5 | +4.4% | +16.6904 to +42.9741 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.713 | 9.123 | +4.7% | −0.0717 to +0.8906 | no |
| pods started | 5.3 | 3.8 | −28.3% | −2.5796 to −0.4204 | yes: GAIN |
| pod start wait, total (s) | 13 | 9.8 | −24.6% | −18.4703 to +12.0703 | no |
| pod start wait, mean (s) | 2.37 | 2.15 | −9.3% | −2.7694 to +2.3289 | no |
| host CPU busy, the real machine under kind (%) | 30.26 | 30.32 | +0.2% | −0.4581 to +0.5699 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*