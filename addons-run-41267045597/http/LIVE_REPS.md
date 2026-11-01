# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 214.9 | 87.56 |
| response time (ms), 95th percentile | 500.2 | 133.8 |
| response time (ms), 99th percentile | 674.5 | 237.3 |
| time over the response line (% of samples) | 5.644 | 0.1217 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.055 |
| utilisation (used / allocatable) | 0.03055 | 0.04817 |
| CPU used (cores), mean | 0.7332 | 1.156 |
| Omni's own CPU (cores), mean | 0 | 0.01094 |
| CPU used with Omni's own (cores), mean | 0.7332 | 1.167 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 561.8 |
| HPA replicas, mean | 2.92 | 2.375 |
| pods started | 2.9 | 2.1 |
| pod start wait, total (s) | 4.2 | 3.1 |
| pod start wait, mean (s) | 1.433 | 1.5 |
| host CPU busy, the real machine under kind (%) | 24 | 36 |
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
| node-hours | 1.52 | 1.518 | −0.1% | −0.0097 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.9 | +2.4% | +2.8394 to +4.8732 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.9 | +2.4% | +2.8394 to +4.8732 | yes: power given |
| response time (ms), mean | 214.9 | 87.56 | −59.3% | −149.5666 to −105.1117 | yes: GAIN |
| response time (ms), 95th percentile | 500.2 | 133.8 | −73.3% | −423.8415 to −308.9715 | yes: GAIN |
| response time (ms), 99th percentile | 674.5 | 237.3 | −64.8% | −517.1810 to −357.2136 | yes: GAIN |
| time over the response line (% of samples) | 5.644 | 0.1217 | −97.8% | −7.7540 to −3.2906 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 0 | −100.0% | −8.1068 to −3.4932 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.3 | +5.300 (native is 0) | +3.4826 to +7.1174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.055 | −65.6% | −0.2373 to +0.0273 | no |
| utilisation (used / allocatable) | 0.03055 | 0.04817 | +57.7% | +0.0148 to +0.0204 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7332 | 1.156 | +57.7% | +0.3557 to +0.4901 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01094 | +0.011 (native is 0) | +0.0095 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7332 | 1.167 | +59.2% | +0.3653 to +0.5023 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 561.8 | −34.2% | −311.1843 to −274.0616 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.92 | 2.375 | −18.7% | −0.7245 to −0.3645 | yes: GAIN |
| pods started | 2.9 | 2.1 | −27.6% | −1.2524 to −0.3476 | yes: GAIN |
| pod start wait, total (s) | 4.2 | 3.1 | −26.2% | −2.1900 to −0.0100 | yes: GAIN |
| pod start wait, mean (s) | 1.433 | 1.5 | +4.7% | −0.2715 to +0.4048 | no |
| host CPU busy, the real machine under kind (%) | 24 | 36 | +50.0% | +10.0211 to +13.9789 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*