# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.374 |
| node-hours | 2.517 | 2.254 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 255 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 537.2 | 483.4 |
| response time (ms), 95th percentile | 3049 | 3016 |
| response time (ms), 99th percentile | 4005 | 4029 |
| time over the response line (% of samples) | 17.64 | 17.23 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.9 | 195.8 |
| utilisation (used / allocatable) | 0.06468 | 0.07304 |
| CPU used (cores), mean | 1.552 | 1.566 |
| Omni's own CPU (cores), mean | 0 | 0.0175 |
| CPU used with Omni's own (cores), mean | 1.552 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.6 | 391 |
| HPA replicas, mean | 2.145 | 2.447 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 1.6 |
| pod start wait, mean (s) | 0 | 1.6 |
| host CPU busy, the real machine under kind (%) | 45.16 | 45.96 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 617 | 622.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.028 |
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
| worker nodes in service, mean | 6 | 5.374 | −10.4% | −1.1612 to −0.0912 | yes: GAIN |
| node-hours | 2.517 | 2.254 | −10.5% | −0.4873 to −0.0393 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.7 | +0.0% | −0.7500 to +0.7842 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 255 | −7.2% | −36.3206 to −3.0160 | yes: GAIN |
| response time (ms), mean | 537.2 | 483.4 | −10.0% | −78.3799 to −29.0759 | yes: GAIN |
| response time (ms), 95th percentile | 3049 | 3016 | −1.1% | −173.4374 to +107.4224 | no |
| response time (ms), 99th percentile | 4005 | 4029 | +0.6% | −129.8956 to +176.9246 | no |
| time over the response line (% of samples) | 17.64 | 17.23 | −2.3% | −0.9160 to +0.1071 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.600 (native is 0) | +11.1615 to +14.0385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.9 | 195.8 | +2.6% | +0.3616 to +9.4184 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06468 | 0.07304 | +12.9% | +0.0007 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.552 | 1.566 | +0.9% | −0.0244 to +0.0525 | no |
| Omni's own CPU (cores), mean | 0 | 0.0175 | +0.018 (native is 0) | +0.0159 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.552 | 1.584 | +2.0% | −0.0060 to +0.0691 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.6 | 391 | −9.2% | −74.7750 to −4.2964 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.145 | 2.447 | +14.1% | −0.1881 to +0.7911 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | −0.3429 to +3.5429 | no |
| pod start wait, mean (s) | 0 | 1.6 | +1.600 (native is 0) | −0.3429 to +3.5429 | no |
| host CPU busy, the real machine under kind (%) | 45.16 | 45.96 | +1.8% | +0.4503 to +1.1520 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 617 | 622.4 | +0.9% | −1.4294 to +12.2294 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.028 | −16.2% | −1.7974 to −0.1459 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*