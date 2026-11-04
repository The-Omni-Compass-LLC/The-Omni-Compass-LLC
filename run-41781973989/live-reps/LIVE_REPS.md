# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 483.4 | 481.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.4 | 481.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 290.4 | 144.7 |
| response time (ms), 95th percentile | 770.3 | 307.4 |
| response time (ms), 99th percentile | 1370 | 722.7 |
| time over the response line (% of samples) | 14.99 | 3.566 |
| failed requests (%) | 1.545 | 1.27 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.7 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 73.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.7367 |
| utilisation (used / allocatable) | 0.08141 | 0.07863 |
| CPU used (cores), mean | 1.954 | 1.887 |
| Omni's own CPU (cores), mean | 0 | 0.04582 |
| CPU used with Omni's own (cores), mean | 1.954 | 1.933 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 378.1 | 390.8 |
| HPA replicas, mean | 9.685 | 12.52 |
| pods started | 6 | 15.4 |
| pod start wait, total (s) | 8.8 | 27.4 |
| pod start wait, mean (s) | 1.428 | 1.783 |
| host CPU busy, the real machine under kind (%) | 56.74 | 56.46 |
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
| node-hours | 4.336 | 4.338 | +0.0% | −0.0073 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 483.4 | 481.8 | −0.3% | −2.6344 to −0.5973 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.4 | 481.8 | −0.3% | −2.6344 to −0.5973 | yes: GAIN |
| response time (ms), mean | 290.4 | 144.7 | −50.2% | −191.7972 to −99.5190 | yes: GAIN |
| response time (ms), 95th percentile | 770.3 | 307.4 | −60.1% | −597.5387 to −328.1703 | yes: GAIN |
| response time (ms), 99th percentile | 1370 | 722.7 | −47.3% | −852.3480 to −442.5774 | yes: GAIN |
| time over the response line (% of samples) | 14.99 | 3.566 | −76.2% | −16.3018 to −6.5429 | yes: GAIN |
| failed requests (%) | 1.545 | 1.27 | −17.8% | −0.4350 to −0.1156 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.7 | 10.5 | −59.1% | −21.2958 to −9.1042 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 73.9 | +73.900 (native is 0) | +57.7164 to +90.0836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.7367 | +61.9% | −0.2679 to +0.8312 | no |
| utilisation (used / allocatable) | 0.08141 | 0.07863 | −3.4% | −0.0035 to −0.0021 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.954 | 1.887 | −3.4% | −0.0829 to −0.0509 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04582 | +0.046 (native is 0) | +0.0380 to +0.0536 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.954 | 1.933 | −1.1% | −0.0332 to −0.0089 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 378.1 | 390.8 | +3.3% | +6.9921 to +18.3280 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.685 | 12.52 | +29.2% | +1.1556 to +4.5053 | yes: power given |
| pods started | 6 | 15.4 | +156.7% | +5.6877 to +13.1123 | yes: power given |
| pod start wait, total (s) | 8.8 | 27.4 | +211.4% | +9.9228 to +27.2772 | yes: LOSS |
| pod start wait, mean (s) | 1.428 | 1.783 | +24.9% | +0.0104 to +0.7000 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.74 | 56.46 | −0.5% | −0.6445 to +0.0900 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*