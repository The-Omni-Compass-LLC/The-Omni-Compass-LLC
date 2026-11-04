# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 520.8 | 521.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.8 | 521.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 312.8 | 210.4 |
| response time (ms), 95th percentile | 810.9 | 456.9 |
| response time (ms), 99th percentile | 2801 | 3089 |
| time over the response line (% of samples) | 21.71 | 16.47 |
| failed requests (%) | 12.16 | 12.69 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.5 | 26.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 55 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.6067 |
| utilisation (used / allocatable) | 0.1077 | 0.1084 |
| CPU used (cores), mean | 2.585 | 2.602 |
| Omni's own CPU (cores), mean | 0 | 0.04846 |
| CPU used with Omni's own (cores), mean | 2.585 | 2.65 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284 | 285 |
| HPA replicas, mean | 9.627 | 12.94 |
| pods started | 5.2 | 9.8 |
| pod start wait, total (s) | 7.3 | 16.8 |
| pod start wait, mean (s) | 1.401 | 1.735 |
| host CPU busy, the real machine under kind (%) | 72.63 | 74.62 |
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
| node-hours | 4.513 | 4.513 | 0.0% | raw −0.0076 to +0.0076 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 520.8 | 521.4 | +0.1% | −0.8713 to +2.0970 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.8 | 521.4 | +0.1% | −0.8713 to +2.0970 | no |
| response time (ms), mean | 312.8 | 210.4 | −32.7% | −129.0781 to −75.6212 | yes: GAIN |
| response time (ms), 95th percentile | 810.9 | 456.9 | −43.6% | −424.3083 to −283.5647 | yes: GAIN |
| response time (ms), 99th percentile | 2801 | 3089 | +10.3% | −796.8902 to +1371.8322 | no |
| time over the response line (% of samples) | 21.71 | 16.47 | −24.2% | −6.6852 to −3.8083 | yes: GAIN |
| failed requests (%) | 12.16 | 12.69 | +4.4% | −0.2201 to +1.2934 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.5 | 26.1 | −17.1% | −7.3429 to −3.4571 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.9 | +56.900 (native is 0) | +48.3399 to +65.4601 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.6067 | +182.2% | −0.0455 to +0.8288 | no |
| utilisation (used / allocatable) | 0.1077 | 0.1084 | +0.7% | −0.0006 to +0.0020 | no |
| CPU used (cores), mean | 2.585 | 2.602 | +0.7% | −0.0146 to +0.0485 | no |
| Omni's own CPU (cores), mean | 0 | 0.04846 | +0.048 (native is 0) | +0.0420 to +0.0549 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.585 | 2.65 | +2.5% | +0.0280 to +0.1028 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284 | 285 | +0.3% | −5.2443 to +7.1692 | no |
| HPA replicas, mean | 9.627 | 12.94 | +34.4% | +1.8116 to +4.8170 | yes: power given |
| pods started | 5.2 | 9.8 | +88.5% | +2.9758 to +6.2242 | yes: power given |
| pod start wait, total (s) | 7.3 | 16.8 | +130.1% | +5.8800 to +13.1200 | yes: LOSS |
| pod start wait, mean (s) | 1.401 | 1.735 | +23.8% | +0.0392 to +0.6278 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.63 | 74.62 | +2.7% | +0.9025 to +3.0782 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*