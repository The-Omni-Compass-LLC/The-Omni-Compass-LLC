# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 120.8 | 87.86 |
| response time (ms), 95th percentile | 251.5 | 155.8 |
| response time (ms), 99th percentile | 375.9 | 254 |
| time over the response line (% of samples) | 0.4343 | 0.1116 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 418.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2183 |
| utilisation (used / allocatable) | 0.03576 | 0.04493 |
| CPU used (cores), mean | 0.8582 | 1.078 |
| Omni's own CPU (cores), mean | 0 | 0.1168 |
| CPU used with Omni's own (cores), mean | 0.8582 | 1.195 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.1 | 595.2 |
| HPA replicas, mean | 8.736 | 10.8 |
| pods started | 5.2 | 7.9 |
| pod start wait, total (s) | 7.4 | 12.4 |
| pod start wait, mean (s) | 1.392 | 1.581 |
| host CPU busy, the real machine under kind (%) | 27.64 | 37.75 |
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
| node-hours | 1.512 | 1.516 | +0.2% | −0.0018 to +0.0088 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 160.7 | +1.5% | +2.0582 to +2.8344 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 160.7 | +1.5% | +2.0582 to +2.8344 | yes: power given |
| response time (ms), mean | 120.8 | 87.86 | −27.3% | −41.8277 to −24.0404 | yes: GAIN |
| response time (ms), 95th percentile | 251.5 | 155.8 | −38.0% | −111.6217 to −79.6953 | yes: GAIN |
| response time (ms), 99th percentile | 375.9 | 254 | −32.4% | −157.6933 to −86.2659 | yes: GAIN |
| time over the response line (% of samples) | 0.4343 | 0.1116 | −74.3% | −0.6073 to −0.0381 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 418.3 | +418.300 (native is 0) | +269.4798 to +567.1202 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2183 | +2.3% | −0.3484 to +0.3584 | no |
| utilisation (used / allocatable) | 0.03576 | 0.04493 | +25.6% | +0.0069 to +0.0114 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8582 | 1.078 | +25.6% | +0.1654 to +0.2748 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.1168 | +0.117 (native is 0) | +0.0815 to +0.1522 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8582 | 1.195 | +39.3% | +0.2561 to +0.4178 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.1 | 595.2 | −18.8% | −164.2716 to −111.5583 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.736 | 10.8 | +23.6% | +0.9552 to +3.1685 | yes: power given |
| pods started | 5.2 | 7.9 | +51.9% | +1.0811 to +4.3189 | yes: power given |
| pod start wait, total (s) | 7.4 | 12.4 | +67.6% | +1.9840 to +8.0160 | yes: LOSS |
| pod start wait, mean (s) | 1.392 | 1.581 | +13.6% | −0.1497 to +0.5284 | no |
| host CPU busy, the real machine under kind (%) | 27.64 | 37.75 | +36.6% | +7.3709 to +12.8439 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*