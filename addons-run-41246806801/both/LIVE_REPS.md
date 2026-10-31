# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.508 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 160.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 160.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 105.2 | 67.84 |
| response time (ms), 95th percentile | 225.4 | 99.08 |
| response time (ms), 99th percentile | 328.5 | 132.8 |
| time over the response line (% of samples) | 0.1928 | 0.02454 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.025 |
| utilisation (used / allocatable) | 0.03519 | 0.0436 |
| CPU used (cores), mean | 0.8446 | 1.046 |
| Omni's own CPU (cores), mean | 0 | 0.01394 |
| CPU used with Omni's own (cores), mean | 0.8446 | 1.06 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.3 | 615.7 |
| HPA replicas, mean | 8.799 | 9.34 |
| pods started | 5 | 6 |
| pod start wait, total (s) | 6.5 | 8.7 |
| pod start wait, mean (s) | 1.287 | 1.461 |
| host CPU busy, the real machine under kind (%) | 26.69 | 33.1 |
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
| node-hours | 1.508 | 1.515 | +0.5% | −0.0007 to +0.0147 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 160.4 | +1.7% | +1.7487 to +3.6348 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 160.4 | +1.7% | +1.7487 to +3.6348 | yes: power given |
| response time (ms), mean | 105.2 | 67.84 | −35.5% | −52.6991 to −21.9302 | yes: GAIN |
| response time (ms), 95th percentile | 225.4 | 99.08 | −56.0% | −157.9682 to −94.7018 | yes: GAIN |
| response time (ms), 99th percentile | 328.5 | 132.8 | −59.6% | −233.2745 to −157.9697 | yes: GAIN |
| time over the response line (% of samples) | 0.1928 | 0.02454 | −87.3% | −0.3799 to +0.0433 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 | +26.800 (native is 0) | +14.5406 to +39.0594 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.025 | −51.6% | −0.0829 to +0.0296 | no |
| utilisation (used / allocatable) | 0.03519 | 0.0436 | +23.9% | +0.0054 to +0.0114 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8446 | 1.046 | +23.9% | +0.1308 to +0.2731 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01394 | +0.014 (native is 0) | +0.0101 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8446 | 1.06 | +25.6% | +0.1413 to +0.2904 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.3 | 615.7 | −17.3% | −158.6794 to −98.6255 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.799 | 9.34 | +6.2% | −0.4036 to +1.4863 | no |
| pods started | 5 | 6 | +20.0% | −0.6860 to +2.6860 | no |
| pod start wait, total (s) | 6.5 | 8.7 | +33.8% | −0.5560 to +4.9560 | no |
| pod start wait, mean (s) | 1.287 | 1.461 | +13.6% | −0.0998 to +0.4493 | no |
| host CPU busy, the real machine under kind (%) | 26.69 | 33.1 | +24.0% | +4.2954 to +8.5256 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*