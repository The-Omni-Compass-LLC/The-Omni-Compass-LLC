# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.988 | 5.986 |
| node-hours | 1.515 | 1.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.5 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 91.46 | 92.21 |
| response time (ms), 95th percentile | 143.5 | 144.2 |
| response time (ms), 99th percentile | 160.7 | 162.7 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02833 |
| utilisation (used / allocatable) | 0.051 | 0.05145 |
| CPU used (cores), mean | 1.221 | 1.232 |
| Omni's own CPU (cores), mean | 0 | 0.01087 |
| CPU used with Omni's own (cores), mean | 1.221 | 1.243 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 530.8 | 526.2 |
| HPA replicas, mean | 2.856 | 2.787 |
| pods started | 1.1 | 1.2 |
| pod start wait, total (s) | 1.7 | 1.6 |
| pod start wait, mean (s) | 1.35 | 1.25 |
| host CPU busy, the real machine under kind (%) | 38.36 | 39.21 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.988 | 5.986 | −0.0% | −0.0415 to +0.0376 | no |
| node-hours | 1.515 | 1.503 | −0.8% | −0.0226 to −0.0004 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 162.5 | 161.5 | −0.6% | −1.9391 to −0.0600 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.3 | −0.6% | −1.6568 to −0.4131 | yes: GAIN |
| response time (ms), mean | 91.46 | 92.21 | +0.8% | −0.7798 to +2.2843 | no |
| response time (ms), 95th percentile | 143.5 | 144.2 | +0.5% | −0.6635 to +1.9575 | no |
| response time (ms), 99th percentile | 160.7 | 162.7 | +1.2% | −1.8560 to +5.7926 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02833 | −46.9% | −0.1359 to +0.0859 | no |
| utilisation (used / allocatable) | 0.051 | 0.05145 | +0.9% | −0.0004 to +0.0013 | no |
| CPU used (cores), mean | 1.221 | 1.232 | +0.8% | −0.0079 to +0.0286 | no |
| Omni's own CPU (cores), mean | 0 | 0.01087 | +0.011 (native is 0) | +0.0098 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.221 | 1.243 | +1.7% | +0.0032 to +0.0392 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 530.8 | 526.2 | −0.9% | −12.1310 to +2.9194 | no |
| HPA replicas, mean | 2.856 | 2.787 | −2.4% | −0.2663 to +0.1289 | no |
| pods started | 1.1 | 1.2 | +9.1% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 1.7 | 1.6 | −5.9% | −1.3818 to +1.1818 | no |
| pod start wait, mean (s) | 1.35 | 1.25 | −7.4% | −0.9728 to +0.7728 | no |
| host CPU busy, the real machine under kind (%) | 38.36 | 39.21 | +2.2% | +0.5078 to +1.2015 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*