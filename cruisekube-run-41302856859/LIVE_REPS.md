# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.913 |
| node-hours | 1.515 | 1.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 162 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 87.95 | 88.62 |
| response time (ms), 95th percentile | 136.2 | 136.4 |
| response time (ms), 99th percentile | 152.9 | 158.2 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.055 | 0.055 |
| utilisation (used / allocatable) | 0.05022 | 0.05089 |
| CPU used (cores), mean | 1.205 | 1.2 |
| Omni's own CPU (cores), mean | 0 | 0.01143 |
| CPU used with Omni's own (cores), mean | 1.205 | 1.212 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.2 | 538.7 |
| HPA replicas, mean | 2.827 | 2.956 |
| pods started | 1.5 | 1.7 |
| pod start wait, total (s) | 2.5 | 2.4 |
| pod start wait, mean (s) | 1.7 | 1.4 |
| host CPU busy, the real machine under kind (%) | 37.87 | 38.45 |
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

Omni-Compass stayed native in 9 of 10 repetitions (repetitions 1, 2, 3, 4, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.913 | −1.5% | −0.2849 to +0.1102 | no |
| node-hours | 1.515 | 1.486 | −1.9% | −0.0805 to +0.0214 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162 | 161.1 | −0.5% | −1.5177 to −0.1862 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162 | 159.5 | −1.5% | −6.2210 to +1.2380 | no |
| response time (ms), mean | 87.95 | 88.62 | +0.8% | −1.4814 to +2.8227 | no |
| response time (ms), 95th percentile | 136.2 | 136.4 | +0.2% | −3.3494 to +3.7844 | no |
| response time (ms), 99th percentile | 152.9 | 158.2 | +3.4% | −3.2738 to +13.7604 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.055 | 0.055 | ±0.0% | −0.1312 to +0.1312 | no |
| utilisation (used / allocatable) | 0.05022 | 0.05089 | +1.3% | −0.0017 to +0.0030 | no |
| CPU used (cores), mean | 1.205 | 1.2 | −0.4% | −0.0263 to +0.0161 | no |
| Omni's own CPU (cores), mean | 0 | 0.01143 | +0.011 (native is 0) | +0.0091 to +0.0138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.205 | 1.212 | +0.5% | −0.0162 to +0.0289 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.2 | 538.7 | −0.1% | −18.3605 to +17.4896 | no |
| HPA replicas, mean | 2.827 | 2.956 | +4.5% | −0.1021 to +0.3593 | no |
| pods started | 1.5 | 1.7 | +13.3% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 2.5 | 2.4 | −4.0% | −1.1366 to +0.9366 | no |
| pod start wait, mean (s) | 1.7 | 1.4 | −17.6% | −0.6455 to +0.0455 | no |
| host CPU busy, the real machine under kind (%) | 37.87 | 38.45 | +1.5% | −0.0218 to +1.1940 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*