# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.51 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.9 | 518.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.9 | 518.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 293.1 | 179.1 |
| response time (ms), 95th percentile | 793 | 390.7 |
| response time (ms), 99th percentile | 2587 | 2221 |
| time over the response line (% of samples) | 20.19 | 14.08 |
| failed requests (%) | 10.76 | 11.04 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.8 | 23.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.7583 |
| utilisation (used / allocatable) | 0.1038 | 0.1033 |
| CPU used (cores), mean | 2.49 | 2.479 |
| Omni's own CPU (cores), mean | 0 | 0.04762 |
| CPU used with Omni's own (cores), mean | 2.49 | 2.527 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.6 | 299 |
| HPA replicas, mean | 9.616 | 12.52 |
| pods started | 5.3 | 10.1 |
| pod start wait, total (s) | 8.3 | 18.8 |
| pod start wait, mean (s) | 1.544 | 1.871 |
| host CPU busy, the real machine under kind (%) | 70.2 | 71.56 |
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
| node-hours | 4.51 | 4.514 | +0.1% | −0.0046 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.9 | 518.1 | +0.0% | −1.2547 to +1.6630 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.9 | 518.1 | +0.0% | −1.2547 to +1.6630 | no |
| response time (ms), mean | 293.1 | 179.1 | −38.9% | −145.2882 to −82.8026 | yes: GAIN |
| response time (ms), 95th percentile | 793 | 390.7 | −50.7% | −503.5662 to −300.9938 | yes: GAIN |
| response time (ms), 99th percentile | 2587 | 2221 | −14.2% | −1713.4185 to +979.9465 | no |
| time over the response line (% of samples) | 20.19 | 14.08 | −30.2% | −7.6036 to −4.6062 | yes: GAIN |
| failed requests (%) | 10.76 | 11.04 | +2.6% | −0.2578 to +0.8156 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.8 | 23.3 | −21.8% | −8.6918 to −4.3082 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.5 | +55.500 (native is 0) | +47.1021 to +63.8979 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.7583 | +175.8% | +0.0895 to +0.8772 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1038 | 0.1033 | −0.4% | −0.0022 to +0.0013 | no |
| CPU used (cores), mean | 2.49 | 2.479 | −0.4% | −0.0535 to +0.0321 | no |
| Omni's own CPU (cores), mean | 0 | 0.04762 | +0.048 (native is 0) | +0.0409 to +0.0544 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.49 | 2.527 | +1.5% | −0.0119 to +0.0858 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.6 | 299 | +1.9% | −5.6974 to +16.5751 | no |
| HPA replicas, mean | 9.616 | 12.52 | +30.2% | +1.4149 to +4.3980 | yes: power given |
| pods started | 5.3 | 10.1 | +90.6% | +3.2256 to +6.3744 | yes: power given |
| pod start wait, total (s) | 8.3 | 18.8 | +126.5% | +7.1576 to +13.8424 | yes: LOSS |
| pod start wait, mean (s) | 1.544 | 1.871 | +21.1% | +0.0357 to +0.6168 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 70.2 | 71.56 | +1.9% | −0.0070 to +2.7161 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*