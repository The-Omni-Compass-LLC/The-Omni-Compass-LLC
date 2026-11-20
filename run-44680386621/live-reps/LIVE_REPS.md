# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.022 |
| node-hours | 2.516 | 2.101 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 274.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 244.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 576.4 | 542.2 |
| response time (ms), 95th percentile | 3205 | 3233 |
| response time (ms), 99th percentile | 4235 | 4282 |
| time over the response line (% of samples) | 18.55 | 18.71 |
| failed requests (%) | 0 | 0.01105 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 209.7 | 216.5 |
| utilisation (used / allocatable) | 0.06753 | 0.08042 |
| CPU used (cores), mean | 1.621 | 1.601 |
| Omni's own CPU (cores), mean | 0 | 0.08609 |
| CPU used with Omni's own (cores), mean | 1.621 | 1.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.7 | 366 |
| HPA replicas, mean | 2.183 | 2.317 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 46.98 | 49.96 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 644.2 | 665.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.338 |
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
| worker nodes in service, mean | 6 | 5.022 | −16.3% | −1.6032 to −0.3535 | yes: GAIN |
| node-hours | 2.516 | 2.101 | −16.5% | −0.6710 to −0.1578 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 274.8 | −0.2% | −1.8344 to +0.4820 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 244.1 | −11.4% | −50.4937 to −12.3421 | yes: GAIN |
| response time (ms), mean | 576.4 | 542.2 | −5.9% | −52.3772 to −16.1811 | yes: GAIN |
| response time (ms), 95th percentile | 3205 | 3233 | +0.9% | −33.9547 to +89.8917 | no |
| response time (ms), 99th percentile | 4235 | 4282 | +1.1% | −197.6310 to +292.2508 | no |
| time over the response line (% of samples) | 18.55 | 18.71 | +0.8% | −0.3578 to +0.6695 | no |
| failed requests (%) | 0 | 0.01105 | +0.011 (native is 0) | −0.0139 to +0.0360 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.2 | +2.8% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 | +9.800 (native is 0) | +7.8108 to +11.7892 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 209.7 | 216.5 | +3.3% | −0.8116 to +14.4616 | no |
| utilisation (used / allocatable) | 0.06753 | 0.08042 | +19.1% | +0.0046 to +0.0212 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.621 | 1.601 | −1.2% | −0.0658 to +0.0271 | no |
| Omni's own CPU (cores), mean | 0 | 0.08609 | +0.086 (native is 0) | +0.0764 to +0.0958 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.621 | 1.687 | +4.1% | +0.0179 to +0.1155 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.7 | 366 | −11.1% | −77.0678 to −14.4486 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.183 | 2.317 | +6.1% | −0.3362 to +0.6044 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.98 | 49.96 | +6.3% | +2.5924 to +3.3640 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 644.2 | 665.4 | +3.3% | +15.9566 to +26.4434 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.338 | −27.7% | −2.6915 to −0.6321 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*