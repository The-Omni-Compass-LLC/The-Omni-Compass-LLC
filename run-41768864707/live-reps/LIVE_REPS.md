# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 524.4 | 519.9 |
| response time (ms), 95th percentile | 2123 | 2474 |
| response time (ms), 99th percentile | 5604 | 5314 |
| time over the response line (% of samples) | 23.49 | 23.92 |
| failed requests (%) | 3.256 | 2.432 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.58 | 1.71 |
| utilisation (used / allocatable) | 0.09722 | 0.09583 |
| CPU used (cores), mean | 2.333 | 2.3 |
| Omni's own CPU (cores), mean | 0 | 0.05539 |
| CPU used with Omni's own (cores), mean | 2.333 | 2.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 306.6 |
| HPA replicas, mean | 15.02 | 15.79 |
| pods started | 5.4 | 5.6 |
| pod start wait, total (s) | 8.2 | 10.2 |
| pod start wait, mean (s) | 1.519 | 1.833 |
| host CPU busy, the real machine under kind (%) | 67.6 | 68.59 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 263 | 284.1 |
| second app: response time (ms), 99th percentile | 1902 | 1583 |
| second app: time over the response line (% of samples) | 14.32 | 14.34 |
| second app: failed requests (%) | 12.5 | 12.78 |

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
| node-hours | 1.518 | 1.516 | −0.1% | −0.0102 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.3 | −0.3% | −1.5735 to +0.6137 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.3 | −0.3% | −1.5735 to +0.6137 | no |
| response time (ms), mean | 524.4 | 519.9 | −0.9% | −44.1718 to +35.0550 | no |
| response time (ms), 95th percentile | 2123 | 2474 | +16.5% | −70.4423 to +772.5343 | no |
| response time (ms), 99th percentile | 5604 | 5314 | −5.2% | −1089.8663 to +510.0109 | no |
| time over the response line (% of samples) | 23.49 | 23.92 | +1.8% | −0.8394 to +1.6984 | no |
| failed requests (%) | 3.256 | 2.432 | −25.3% | −1.7597 to +0.1119 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.3 | −2.4% | −0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.9 | +130.900 (native is 0) | +97.6462 to +164.1538 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.58 | 1.71 | +8.2% | −0.9080 to +1.1680 | no |
| utilisation (used / allocatable) | 0.09722 | 0.09583 | −1.4% | −0.0024 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.333 | 2.3 | −1.4% | −0.0579 to −0.0086 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05539 | +0.055 (native is 0) | +0.0464 to +0.0644 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.333 | 2.355 | +0.9% | +0.0025 to +0.0418 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 306.6 | +0.9% | +0.2492 to +5.2168 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.02 | 15.79 | +5.1% | +0.0020 to +1.5422 | yes: power given |
| pods started | 5.4 | 5.6 | +3.7% | −0.6121 to +1.0121 | no |
| pod start wait, total (s) | 8.2 | 10.2 | +24.4% | −0.4548 to +4.4548 | no |
| pod start wait, mean (s) | 1.519 | 1.833 | +20.7% | −0.0128 to +0.6418 | no |
| host CPU busy, the real machine under kind (%) | 67.6 | 68.59 | +1.5% | +0.4598 to +1.5213 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 263 | 284.1 | +8.0% | −26.3212 to +68.6072 | no |
| second app: response time (ms), 99th percentile | 1902 | 1583 | −16.7% | −1188.4341 to +551.8837 | no |
| second app: time over the response line (% of samples) | 14.32 | 14.34 | +0.1% | −0.5872 to +0.6299 | no |
| second app: failed requests (%) | 12.5 | 12.78 | +2.2% | −0.1798 to +0.7367 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*