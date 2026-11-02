# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.336 |
| energy, parked workers still on at idle power (Wh, declared model) | 487.7 | 486 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 487.7 | 486 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 329.1 | 162.6 |
| response time (ms), 95th percentile | 856.2 | 344 |
| response time (ms), 99th percentile | 1692 | 831.9 |
| time over the response line (% of samples) | 17.62 | 4.059 |
| failed requests (%) | 1.649 | 1.404 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.1 | 11.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 6.25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.805 |
| utilisation (used / allocatable) | 0.0879 | 0.08527 |
| CPU used (cores), mean | 2.11 | 2.046 |
| Omni's own CPU (cores), mean | 0 | 0.04885 |
| CPU used with Omni's own (cores), mean | 2.11 | 2.095 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 342.8 | 351 |
| HPA replicas, mean | 9.778 | 12.98 |
| pods started | 5.2 | 15.5 |
| pod start wait, total (s) | 9 | 28.4 |
| pod start wait, mean (s) | 1.753 | 1.801 |
| host CPU busy, the real machine under kind (%) | 60.93 | 61.06 |
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
| node-hours | 4.336 | 4.336 | 0.0% | raw −0.0099 to +0.0099 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 487.7 | 486 | −0.4% | −3.4170 to −0.0465 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 487.7 | 486 | −0.4% | −3.4170 to −0.0465 | yes: GAIN |
| response time (ms), mean | 329.1 | 162.6 | −50.6% | −207.7495 to −125.3163 | yes: GAIN |
| response time (ms), 95th percentile | 856.2 | 344 | −59.8% | −634.8794 to −389.5486 | yes: GAIN |
| response time (ms), 99th percentile | 1692 | 831.9 | −50.8% | −1233.1694 to −486.2798 | yes: GAIN |
| time over the response line (% of samples) | 17.62 | 4.059 | −77.0% | −17.8484 to −9.2694 | yes: GAIN |
| failed requests (%) | 1.649 | 1.404 | −14.9% | −0.4323 to −0.0584 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.1 | 11.3 | −61.2% | −22.8332 to −12.7668 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.9 | +78.900 (native is 0) | +65.6525 to +92.1475 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.805 | +113.7% | −0.0275 to +0.8842 | no |
| utilisation (used / allocatable) | 0.0879 | 0.08527 | −3.0% | −0.0040 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.11 | 2.046 | −3.0% | −0.0949 to −0.0317 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04885 | +0.049 (native is 0) | +0.0424 to +0.0553 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.11 | 2.095 | −0.7% | −0.0437 to +0.0148 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 342.8 | 351 | +2.4% | +4.7108 to +11.7314 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.778 | 12.98 | +32.8% | +1.7611 to +4.6464 | yes: power given |
| pods started | 5.2 | 15.5 | +198.1% | +7.0648 to +13.5352 | yes: power given |
| pod start wait, total (s) | 9 | 28.4 | +215.6% | +11.6797 to +27.1203 | yes: LOSS |
| pod start wait, mean (s) | 1.753 | 1.801 | +2.7% | −0.1715 to +0.2675 | no |
| host CPU busy, the real machine under kind (%) | 60.93 | 61.06 | +0.2% | −0.7382 to +0.9953 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*