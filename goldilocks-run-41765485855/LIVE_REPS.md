# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 158.2 | 98.55 |
| response time (ms), 95th percentile | 341 | 189.5 |
| response time (ms), 99th percentile | 504.6 | 310.5 |
| time over the response line (% of samples) | 1.561 | 0.1972 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 460.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.2717 |
| utilisation (used / allocatable) | 0.033 | 0.04629 |
| CPU used (cores), mean | 0.7921 | 1.111 |
| Omni's own CPU (cores), mean | 0 | 0.07998 |
| CPU used with Omni's own (cores), mean | 0.7921 | 1.191 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 578.4 |
| HPA replicas, mean | 9.686 | 13.35 |
| pods started | 2.7 | 6.6 |
| pod start wait, total (s) | 3.5 | 10.9 |
| pod start wait, mean (s) | 1.225 | 1.636 |
| host CPU busy, the real machine under kind (%) | 24.6 | 36.97 |
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
| node-hours | 1.517 | 1.509 | −0.6% | −0.0154 to −0.0016 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.3 | +1.3% | +1.2725 to +2.9861 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.3 | +1.3% | +1.2725 to +2.9861 | yes: power given |
| response time (ms), mean | 158.2 | 98.55 | −37.7% | −73.6660 to −45.7162 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 189.5 | −44.4% | −174.7433 to −128.2537 | yes: GAIN |
| response time (ms), 99th percentile | 504.6 | 310.5 | −38.5% | −225.8596 to −162.1820 | yes: GAIN |
| time over the response line (% of samples) | 1.561 | 0.1972 | −87.4% | −2.0705 to −0.6561 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −2.6310 to −0.3690 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 460.5 | +460.500 (native is 0) | +332.1089 to +588.8911 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.2717 | +162.9% | −0.1276 to +0.4643 | no |
| utilisation (used / allocatable) | 0.033 | 0.04629 | +40.3% | +0.0108 to +0.0158 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7921 | 1.111 | +40.3% | +0.2581 to +0.3797 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07998 | +0.080 (native is 0) | +0.0620 to +0.0980 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7921 | 1.191 | +50.4% | +0.3225 to +0.4753 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.6 | 578.4 | −26.8% | −241.3380 to −183.1937 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.686 | 13.35 | +37.8% | +2.1749 to +5.1538 | yes: power given |
| pods started | 2.7 | 6.6 | +144.4% | +2.4129 to +5.3871 | yes: power given |
| pod start wait, total (s) | 3.5 | 10.9 | +211.4% | +4.7837 to +10.0163 | yes: LOSS |
| pod start wait, mean (s) | 1.225 | 1.636 | +33.5% | −0.1111 to +0.9328 | no |
| host CPU busy, the real machine under kind (%) | 24.6 | 36.97 | +50.3% | +9.9154 to +14.8271 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*