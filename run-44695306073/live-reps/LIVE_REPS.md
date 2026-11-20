# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.335 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 482 | 480 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482 | 480 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 272.9 | 136.7 |
| response time (ms), 95th percentile | 708.3 | 292.1 |
| response time (ms), 99th percentile | 1277 | 663.7 |
| time over the response line (% of samples) | 12.76 | 3.161 |
| failed requests (%) | 1.061 | 0.9409 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.4 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50.95 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 1.083 |
| utilisation (used / allocatable) | 0.07943 | 0.07674 |
| CPU used (cores), mean | 1.906 | 1.842 |
| Omni's own CPU (cores), mean | 0 | 0.04614 |
| CPU used with Omni's own (cores), mean | 1.906 | 1.888 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.4 | 382.6 |
| HPA replicas, mean | 9.754 | 12 |
| pods started | 6.2 | 18.3 |
| pod start wait, total (s) | 9.3 | 33.3 |
| pod start wait, mean (s) | 1.48 | 1.832 |
| host CPU busy, the real machine under kind (%) | 55.22 | 55.44 |
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
| node-hours | 4.335 | 4.333 | −0.0% | −0.0054 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482 | 480 | −0.4% | −2.9918 to −1.1321 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482 | 480 | −0.4% | −2.9918 to −1.1321 | yes: GAIN |
| response time (ms), mean | 272.9 | 136.7 | −49.9% | −176.1372 to −96.2637 | yes: GAIN |
| response time (ms), 95th percentile | 708.3 | 292.1 | −58.8% | −522.6027 to −309.8103 | yes: GAIN |
| response time (ms), 99th percentile | 1277 | 663.7 | −48.0% | −795.9520 to −430.9146 | yes: GAIN |
| time over the response line (% of samples) | 12.76 | 3.161 | −75.2% | −14.2869 to −4.9113 | yes: GAIN |
| failed requests (%) | 1.061 | 0.9409 | −11.3% | −0.2230 to −0.0173 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.4 | 9.2 | −58.9% | −18.2219 to −8.1781 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.9 | +82.900 (native is 0) | +68.8285 to +96.9715 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 1.083 | +169.7% | +0.0417 to +1.3217 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07943 | 0.07674 | −3.4% | −0.0037 to −0.0017 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.906 | 1.842 | −3.4% | −0.0878 to −0.0413 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04614 | +0.046 (native is 0) | +0.0389 to +0.0533 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.906 | 1.888 | −1.0% | −0.0375 to +0.0006 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.4 | 382.6 | +2.7% | +7.6860 to +12.6564 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.754 | 12 | +23.0% | +0.5900 to +3.9031 | yes: power given |
| pods started | 6.2 | 18.3 | +195.2% | +8.0473 to +16.1527 | yes: power given |
| pod start wait, total (s) | 9.3 | 33.3 | +258.1% | +16.0561 to +31.9439 | yes: LOSS |
| pod start wait, mean (s) | 1.48 | 1.832 | +23.8% | −0.0372 to +0.7422 | no |
| host CPU busy, the real machine under kind (%) | 55.22 | 55.44 | +0.4% | −0.1155 to +0.5513 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*