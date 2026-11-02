# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.3 | 516.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.3 | 516.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 284 | 200.7 |
| response time (ms), 95th percentile | 723.1 | 383.9 |
| response time (ms), 99th percentile | 2867 | 3368 |
| time over the response line (% of samples) | 19.36 | 14.44 |
| failed requests (%) | 11.34 | 11.41 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.8 | 23 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.8783 |
| utilisation (used / allocatable) | 0.1012 | 0.1014 |
| CPU used (cores), mean | 2.428 | 2.433 |
| Omni's own CPU (cores), mean | 0 | 0.04585 |
| CPU used with Omni's own (cores), mean | 2.428 | 2.479 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.2 | 316.2 |
| HPA replicas, mean | 9.576 | 11.4 |
| pods started | 4.9 | 7.8 |
| pod start wait, total (s) | 7.6 | 12.2 |
| pod start wait, mean (s) | 1.591 | 1.555 |
| host CPU busy, the real machine under kind (%) | 68.54 | 70.16 |
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
| node-hours | 4.512 | 4.513 | +0.0% | −0.0090 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.3 | 516.7 | +0.1% | −1.0491 to +1.7019 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.3 | 516.7 | +0.1% | −1.0491 to +1.7019 | no |
| response time (ms), mean | 284 | 200.7 | −29.3% | −121.5337 to −45.0200 | yes: GAIN |
| response time (ms), 95th percentile | 723.1 | 383.9 | −46.9% | −473.0360 to −205.3260 | yes: GAIN |
| response time (ms), 99th percentile | 2867 | 3368 | +17.4% | −671.1936 to +1671.7678 | no |
| time over the response line (% of samples) | 19.36 | 14.44 | −25.4% | −6.7321 to −3.1147 | yes: GAIN |
| failed requests (%) | 11.34 | 11.41 | +0.6% | −0.6177 to +0.7641 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.8 | 23 | −17.3% | −6.0526 to −3.5474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.800 (native is 0) | +35.3176 to +52.2824 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.8783 | +191.2% | +0.2382 to +0.9151 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1012 | 0.1014 | +0.2% | −0.0005 to +0.0008 | no |
| CPU used (cores), mean | 2.428 | 2.433 | +0.2% | −0.0115 to +0.0204 | no |
| Omni's own CPU (cores), mean | 0 | 0.04585 | +0.046 (native is 0) | +0.0374 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.479 | +2.1% | +0.0280 to +0.0726 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.2 | 316.2 | +0.3% | −2.0384 to +4.0591 | no |
| HPA replicas, mean | 9.576 | 11.4 | +19.0% | +0.2943 to +3.3505 | yes: power given |
| pods started | 4.9 | 7.8 | +59.2% | +1.2327 to +4.5673 | yes: power given |
| pod start wait, total (s) | 7.6 | 12.2 | +60.5% | +0.9651 to +8.2349 | yes: LOSS |
| pod start wait, mean (s) | 1.591 | 1.555 | −2.3% | −0.4058 to +0.3325 | no |
| host CPU busy, the real machine under kind (%) | 68.54 | 70.16 | +2.4% | +0.8327 to +2.3909 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*