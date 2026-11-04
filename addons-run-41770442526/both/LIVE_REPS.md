# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.509 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 140.1 | 100.9 |
| response time (ms), 95th percentile | 290.8 | 184 |
| response time (ms), 99th percentile | 431.3 | 312.3 |
| time over the response line (% of samples) | 0.6585 | 0.1856 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 445 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.2333 |
| utilisation (used / allocatable) | 0.03692 | 0.04638 |
| CPU used (cores), mean | 0.8861 | 1.113 |
| Omni's own CPU (cores), mean | 0 | 0.1258 |
| CPU used with Omni's own (cores), mean | 0.8861 | 1.239 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.3 | 579.6 |
| HPA replicas, mean | 8.848 | 11.26 |
| pods started | 4.8 | 8.3 |
| pod start wait, total (s) | 6.6 | 12.2 |
| pod start wait, mean (s) | 1.38 | 1.469 |
| host CPU busy, the real machine under kind (%) | 28.28 | 39.28 |
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
| node-hours | 1.509 | 1.511 | +0.1% | −0.0033 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.6 | +1.5% | +1.9824 to +2.7213 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.6 | +1.5% | +1.9824 to +2.7213 | yes: power given |
| response time (ms), mean | 140.1 | 100.9 | −28.0% | −48.5098 to −30.0500 | yes: GAIN |
| response time (ms), 95th percentile | 290.8 | 184 | −36.7% | −122.3010 to −91.2240 | yes: GAIN |
| response time (ms), 99th percentile | 431.3 | 312.3 | −27.6% | −146.3246 to −91.5354 | yes: GAIN |
| time over the response line (% of samples) | 0.6585 | 0.1856 | −71.8% | −0.7929 to −0.1529 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | −100.0% | −1.1001 to −0.0999 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 445 | +445.000 (native is 0) | +301.6527 to +588.3473 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.2333 | +77.2% | −0.2168 to +0.4201 | no |
| utilisation (used / allocatable) | 0.03692 | 0.04638 | +25.6% | +0.0069 to +0.0120 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8861 | 1.113 | +25.6% | +0.1661 to +0.2879 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.1258 | +0.126 (native is 0) | +0.0933 to +0.1582 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8861 | 1.239 | +39.8% | +0.2625 to +0.4430 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.3 | 579.6 | −18.5% | −161.0895 to −102.3314 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.848 | 11.26 | +27.2% | +1.3901 to +3.4296 | yes: power given |
| pods started | 4.8 | 8.3 | +72.9% | +2.0995 to +4.9005 | yes: power given |
| pod start wait, total (s) | 6.6 | 12.2 | +84.8% | +2.8153 to +8.3847 | yes: LOSS |
| pod start wait, mean (s) | 1.38 | 1.469 | +6.4% | −0.1674 to +0.3450 | no |
| host CPU busy, the real machine under kind (%) | 28.28 | 39.28 | +38.9% | +8.1734 to +13.8219 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*