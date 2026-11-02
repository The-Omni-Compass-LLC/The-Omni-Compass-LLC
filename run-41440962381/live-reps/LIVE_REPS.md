# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.329 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 475.1 | 474.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.1 | 474.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 224.2 | 118.5 |
| response time (ms), 95th percentile | 565.5 | 228.3 |
| response time (ms), 99th percentile | 1088 | 567.2 |
| time over the response line (% of samples) | 9.997 | 2.339 |
| failed requests (%) | 1.028 | 0.8609 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.4 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 52.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4717 | 0.86 |
| utilisation (used / allocatable) | 0.06986 | 0.0681 |
| CPU used (cores), mean | 1.677 | 1.634 |
| Omni's own CPU (cores), mean | 0 | 0.04051 |
| CPU used with Omni's own (cores), mean | 1.677 | 1.675 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 463.4 |
| HPA replicas, mean | 9.467 | 10.95 |
| pods started | 7.4 | 13.5 |
| pod start wait, total (s) | 11.4 | 22 |
| pod start wait, mean (s) | 1.584 | 1.599 |
| host CPU busy, the real machine under kind (%) | 49.08 | 49.17 |
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
| node-hours | 4.329 | 4.337 | +0.2% | +0.0001 to +0.0159 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 475.1 | 474.8 | −0.1% | −1.0694 to +0.4120 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.1 | 474.8 | −0.1% | −1.0694 to +0.4120 | no |
| response time (ms), mean | 224.2 | 118.5 | −47.2% | −157.1690 to −54.3148 | yes: GAIN |
| response time (ms), 95th percentile | 565.5 | 228.3 | −59.6% | −484.7964 to −189.5986 | yes: GAIN |
| response time (ms), 99th percentile | 1088 | 567.2 | −47.9% | −733.7902 to −307.9702 | yes: GAIN |
| time over the response line (% of samples) | 9.997 | 2.339 | −76.6% | −13.1303 to −2.1873 | yes: GAIN |
| failed requests (%) | 1.028 | 0.8609 | −16.3% | −0.3019 to −0.0327 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.4 | 6.9 | −60.3% | −18.1094 to −2.8906 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.4 | +59.400 (native is 0) | +40.4561 to +78.3439 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4717 | 0.86 | +82.3% | +0.1070 to +0.6697 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06986 | 0.0681 | −2.5% | −0.0024 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.677 | 1.634 | −2.5% | −0.0587 to −0.0256 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04051 | +0.041 (native is 0) | +0.0317 to +0.0493 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.675 | −0.1% | −0.0173 to +0.0140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 463.4 | +2.7% | +3.2707 to +21.4909 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.467 | 10.95 | +15.7% | −0.6082 to +3.5742 | no |
| pods started | 7.4 | 13.5 | +82.4% | +1.9503 to +10.2497 | yes: power given |
| pod start wait, total (s) | 11.4 | 22 | +93.0% | +1.9951 to +19.2049 | yes: LOSS |
| pod start wait, mean (s) | 1.584 | 1.599 | +0.9% | −0.3231 to +0.3520 | no |
| host CPU busy, the real machine under kind (%) | 49.08 | 49.17 | +0.2% | −0.4060 to +0.5959 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*