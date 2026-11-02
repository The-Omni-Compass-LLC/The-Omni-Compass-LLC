# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 517.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 517.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 269.1 | 184.1 |
| response time (ms), 95th percentile | 729.8 | 436.7 |
| response time (ms), 99th percentile | 2265 | 2290 |
| time over the response line (% of samples) | 18.5 | 13.58 |
| failed requests (%) | 10.31 | 10.27 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 22.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2883 | 0.8617 |
| utilisation (used / allocatable) | 0.1019 | 0.1016 |
| CPU used (cores), mean | 2.446 | 2.437 |
| Omni's own CPU (cores), mean | 0 | 0.04456 |
| CPU used with Omni's own (cores), mean | 2.446 | 2.482 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.2 | 309 |
| HPA replicas, mean | 9.565 | 12.45 |
| pods started | 5.4 | 10.4 |
| pod start wait, total (s) | 7.5 | 18.8 |
| pod start wait, mean (s) | 1.379 | 1.8 |
| host CPU busy, the real machine under kind (%) | 68.54 | 69.74 |
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
| node-hours | 4.513 | 4.516 | +0.1% | −0.0063 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 517.1 | +0.0% | −0.6458 to +1.0593 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 517.1 | +0.0% | −0.6458 to +1.0593 | no |
| response time (ms), mean | 269.1 | 184.1 | −31.6% | −107.8949 to −62.0955 | yes: GAIN |
| response time (ms), 95th percentile | 729.8 | 436.7 | −40.2% | −394.2633 to −191.8127 | yes: GAIN |
| response time (ms), 99th percentile | 2265 | 2290 | +1.1% | −734.5552 to +784.3148 | no |
| time over the response line (% of samples) | 18.5 | 13.58 | −26.6% | −6.6195 to −3.2140 | yes: GAIN |
| failed requests (%) | 10.31 | 10.27 | −0.4% | −0.3769 to +0.2935 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 22.5 | −19.6% | −7.5580 to −3.4420 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.6 | +51.600 (native is 0) | +41.0969 to +62.1031 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2883 | 0.8617 | +198.8% | −0.0177 to +1.1643 | no |
| utilisation (used / allocatable) | 0.1019 | 0.1016 | −0.3% | −0.0016 to +0.0009 | no |
| CPU used (cores), mean | 2.446 | 2.437 | −0.3% | −0.0394 to +0.0226 | no |
| Omni's own CPU (cores), mean | 0 | 0.04456 | +0.045 (native is 0) | +0.0376 to +0.0516 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.446 | 2.482 | +1.5% | −0.0011 to +0.0735 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.2 | 309 | +1.6% | −2.7445 to +12.4251 | no |
| HPA replicas, mean | 9.565 | 12.45 | +30.1% | +1.1655 to +4.5950 | yes: power given |
| pods started | 5.4 | 10.4 | +92.6% | +3.2479 to +6.7521 | yes: power given |
| pod start wait, total (s) | 7.5 | 18.8 | +150.7% | +6.7503 to +15.8497 | yes: LOSS |
| pod start wait, mean (s) | 1.379 | 1.8 | +30.5% | +0.0226 to +0.8196 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 68.54 | 69.74 | +1.8% | +0.1988 to +2.2072 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*