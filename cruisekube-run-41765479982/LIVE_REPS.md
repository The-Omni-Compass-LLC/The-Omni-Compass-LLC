# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.944 | 6 |
| node-hours | 1.503 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.1 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 87.47 | 90.32 |
| response time (ms), 95th percentile | 135.8 | 138.8 |
| response time (ms), 99th percentile | 155.1 | 166.5 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.055 | 0.08 |
| utilisation (used / allocatable) | 0.05053 | 0.05071 |
| CPU used (cores), mean | 1.2 | 1.217 |
| Omni's own CPU (cores), mean | 0 | 0.05605 |
| CPU used with Omni's own (cores), mean | 1.2 | 1.273 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.2 | 532.1 |
| HPA replicas, mean | 2.764 | 2.902 |
| pods started | 1.4 | 1.3 |
| pod start wait, total (s) | 2.5 | 1.8 |
| pod start wait, mean (s) | 1.7 | 1.4 |
| host CPU busy, the real machine under kind (%) | 38.13 | 40.51 |
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
| worker nodes in service, mean | 5.944 | 6 | +0.9% | −0.0704 to +0.1819 | no |
| node-hours | 1.503 | 1.513 | +0.6% | −0.0217 to +0.0409 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 161.8 | −0.9% | −4.2286 to +1.3510 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.1 | 161.8 | −0.2% | −1.3105 to +0.5537 | no |
| response time (ms), mean | 87.47 | 90.32 | +3.2% | +1.4912 to +4.1939 | yes: LOSS |
| response time (ms), 95th percentile | 135.8 | 138.8 | +2.2% | +0.8587 to +5.0153 | yes: LOSS |
| response time (ms), 99th percentile | 155.1 | 166.5 | +7.3% | −1.4680 to +24.1900 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4.000 (native is 0) | +4.0000 to +4.0000 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.055 | 0.08 | +45.5% | −0.1178 to +0.1678 | no |
| utilisation (used / allocatable) | 0.05053 | 0.05071 | +0.4% | −0.0014 to +0.0017 | no |
| CPU used (cores), mean | 1.2 | 1.217 | +1.4% | −0.0020 to +0.0365 | no |
| Omni's own CPU (cores), mean | 0 | 0.05605 | +0.056 (native is 0) | +0.0511 to +0.0610 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.2 | 1.273 | +6.1% | +0.0527 to +0.0938 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.2 | 532.1 | −1.3% | −14.8703 to +0.8103 | no |
| HPA replicas, mean | 2.764 | 2.902 | +5.0% | −0.0966 to +0.3725 | no |
| pods started | 1.4 | 1.3 | −7.1% | −0.7263 to +0.5263 | no |
| pod start wait, total (s) | 2.5 | 1.8 | −28.0% | −1.8209 to +0.4209 | no |
| pod start wait, mean (s) | 1.7 | 1.4 | −17.6% | −0.6455 to +0.0455 | no |
| host CPU busy, the real machine under kind (%) | 38.13 | 40.51 | +6.2% | +1.8171 to +2.9306 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*