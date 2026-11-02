# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.522 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.8 | 174.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.8 | 174.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 632.5 | 582 |
| response time (ms), 95th percentile | 2650 | 2594 |
| response time (ms), 99th percentile | 6448 | 6223 |
| time over the response line (% of samples) | 28.48 | 28.86 |
| failed requests (%) | 3.658 | 2.51 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 132.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.44 | 1.823 |
| utilisation (used / allocatable) | 0.1037 | 0.103 |
| CPU used (cores), mean | 2.489 | 2.471 |
| Omni's own CPU (cores), mean | 0 | 0.0607 |
| CPU used with Omni's own (cores), mean | 2.489 | 2.532 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279 | 280 |
| HPA replicas, mean | 15.2 | 16.46 |
| pods started | 5.1 | 5.8 |
| pod start wait, total (s) | 8.3 | 10.4 |
| pod start wait, mean (s) | 1.633 | 1.782 |
| host CPU busy, the real machine under kind (%) | 72.14 | 73.56 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 232.4 | 251.7 |
| second app: response time (ms), 99th percentile | 1891 | 1356 |
| second app: time over the response line (% of samples) | 16.09 | 16 |
| second app: failed requests (%) | 14.78 | 14.79 |

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
| node-hours | 1.514 | 1.522 | +0.5% | +0.0020 to +0.0143 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 173.8 | 174.6 | +0.5% | +0.1413 to +1.4468 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.8 | 174.6 | +0.5% | +0.1413 to +1.4468 | yes: power given |
| response time (ms), mean | 632.5 | 582 | −8.0% | −101.4606 to +0.5420 | no |
| response time (ms), 95th percentile | 2650 | 2594 | −2.1% | −458.6021 to +345.1741 | no |
| response time (ms), 99th percentile | 6448 | 6223 | −3.5% | −923.1089 to +472.0199 | no |
| time over the response line (% of samples) | 28.48 | 28.86 | +1.3% | −0.5021 to +1.2525 | no |
| failed requests (%) | 3.658 | 2.51 | −31.4% | −2.1734 to −0.1227 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.4 | −2.1% | −0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 132.4 | +132.400 (native is 0) | +107.8603 to +156.9397 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.44 | 1.823 | +26.6% | −0.4432 to +1.2099 | no |
| utilisation (used / allocatable) | 0.1037 | 0.103 | −0.7% | −0.0024 to +0.0009 | no |
| CPU used (cores), mean | 2.489 | 2.471 | −0.7% | −0.0564 to +0.0224 | no |
| Omni's own CPU (cores), mean | 0 | 0.0607 | +0.061 (native is 0) | +0.0559 to +0.0655 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.489 | 2.532 | +1.8% | +0.0079 to +0.0795 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279 | 280 | +0.4% | −3.1416 to +5.2771 | no |
| HPA replicas, mean | 15.2 | 16.46 | +8.3% | +0.5772 to +1.9389 | yes: power given |
| pods started | 5.1 | 5.8 | +13.7% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 8.3 | 10.4 | +25.3% | −0.7899 to +4.9899 | no |
| pod start wait, mean (s) | 1.633 | 1.782 | +9.1% | −0.2024 to +0.4989 | no |
| host CPU busy, the real machine under kind (%) | 72.14 | 73.56 | +2.0% | +0.9300 to +1.9059 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 232.4 | 251.7 | +8.3% | +2.4166 to +36.1674 | yes: LOSS |
| second app: response time (ms), 99th percentile | 1891 | 1356 | −28.3% | −2526.5618 to +1457.0828 | no |
| second app: time over the response line (% of samples) | 16.09 | 16 | −0.5% | −0.6497 to +0.4759 | no |
| second app: failed requests (%) | 14.78 | 14.79 | +0.1% | −0.6183 to +0.6444 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*