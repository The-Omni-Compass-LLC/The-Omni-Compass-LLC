# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.509 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 160.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 160.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 119.8 | 86.5 |
| response time (ms), 95th percentile | 252.9 | 153.5 |
| response time (ms), 99th percentile | 373.2 | 253.5 |
| time over the response line (% of samples) | 0.4387 | 0.07461 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 390.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.14 |
| utilisation (used / allocatable) | 0.03555 | 0.04434 |
| CPU used (cores), mean | 0.8531 | 1.064 |
| Omni's own CPU (cores), mean | 0 | 0.107 |
| CPU used with Omni's own (cores), mean | 0.8531 | 1.171 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.9 | 605.1 |
| HPA replicas, mean | 8.771 | 10.68 |
| pods started | 5 | 7.5 |
| pod start wait, total (s) | 6.6 | 10.3 |
| pod start wait, mean (s) | 1.313 | 1.358 |
| host CPU busy, the real machine under kind (%) | 27.42 | 36.96 |
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
| node-hours | 1.509 | 1.513 | +0.2% | −0.0046 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 160.3 | +1.5% | +1.7422 to +2.9828 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 160.3 | +1.5% | +1.7422 to +2.9828 | yes: power given |
| response time (ms), mean | 119.8 | 86.5 | −27.8% | −45.6170 to −20.9043 | yes: GAIN |
| response time (ms), 95th percentile | 252.9 | 153.5 | −39.3% | −124.5860 to −74.3220 | yes: GAIN |
| response time (ms), 99th percentile | 373.2 | 253.5 | −32.1% | −140.8372 to −98.6698 | yes: GAIN |
| time over the response line (% of samples) | 0.4387 | 0.07461 | −83.0% | −0.6821 to −0.0460 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 390.5 | +390.500 (native is 0) | +269.3215 to +511.6785 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.14 | −24.3% | −0.3671 to +0.2771 | no |
| utilisation (used / allocatable) | 0.03555 | 0.04434 | +24.7% | +0.0062 to +0.0114 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8531 | 1.064 | +24.7% | +0.1486 to +0.2735 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.107 | +0.107 (native is 0) | +0.0775 to +0.1366 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8531 | 1.171 | +37.3% | +0.2306 to +0.4056 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.9 | 605.1 | −18.0% | −158.8817 to −106.7589 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.771 | 10.68 | +21.8% | +0.8968 to +2.9261 | yes: power given |
| pods started | 5 | 7.5 | +50.0% | +0.6454 to +4.3546 | yes: power given |
| pod start wait, total (s) | 6.6 | 10.3 | +56.1% | +0.6831 to +6.7169 | yes: LOSS |
| pod start wait, mean (s) | 1.313 | 1.358 | +3.4% | −0.2147 to +0.3041 | no |
| host CPU busy, the real machine under kind (%) | 27.42 | 36.96 | +34.8% | +7.0584 to +12.0199 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*