# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.848 |
| node-hours | 2.516 | 2.035 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 238.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 553 | 510.5 |
| response time (ms), 95th percentile | 3060 | 3112 |
| response time (ms), 99th percentile | 4144 | 4081 |
| time over the response line (% of samples) | 17.7 | 17.53 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 198.5 | 203.6 |
| utilisation (used / allocatable) | 0.06476 | 0.07963 |
| CPU used (cores), mean | 1.554 | 1.542 |
| Omni's own CPU (cores), mean | 0 | 0.08008 |
| CPU used with Omni's own (cores), mean | 1.554 | 1.622 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.5 | 372.6 |
| HPA replicas, mean | 2.206 | 2.309 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.8 | 0.8 |
| pod start wait, mean (s) | 0.8 | 0.8 |
| host CPU busy, the real machine under kind (%) | 45.1 | 47.72 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 615.3 | 633.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.146 |
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
| worker nodes in service, mean | 6 | 4.848 | −19.2% | −1.7927 to −0.5111 | yes: GAIN |
| node-hours | 2.516 | 2.035 | −19.1% | −0.7529 to −0.2089 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 | +0.1% | −0.8691 to +1.1942 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 238.5 | −13.1% | −56.5690 to −15.6350 | yes: GAIN |
| response time (ms), mean | 553 | 510.5 | −7.7% | −53.8836 to −31.1404 | yes: GAIN |
| response time (ms), 95th percentile | 3060 | 3112 | +1.7% | −42.7432 to +146.1522 | no |
| response time (ms), 99th percentile | 4144 | 4081 | −1.5% | −216.0871 to +89.4315 | no |
| time over the response line (% of samples) | 17.7 | 17.53 | −1.0% | −0.3768 to +0.0373 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 11 | +3.8% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.9 | +8.900 (native is 0) | +7.5324 to +10.2676 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 198.5 | 203.6 | +2.5% | −1.2278 to +11.3378 | no |
| utilisation (used / allocatable) | 0.06476 | 0.07963 | +23.0% | +0.0066 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.554 | 1.542 | −0.8% | −0.0501 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0 | 0.08008 | +0.080 (native is 0) | +0.0703 to +0.0898 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.554 | 1.622 | +4.4% | +0.0274 to +0.1079 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.5 | 372.6 | −14.1% | −100.9894 to −20.8716 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.206 | 2.309 | +4.7% | −0.3144 to +0.5202 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.8 | 0.8 | ±0.0% | −2.6976 to +2.6976 | no |
| pod start wait, mean (s) | 0.8 | 0.8 | ±0.0% | −2.6976 to +2.6976 | no |
| host CPU busy, the real machine under kind (%) | 45.1 | 47.72 | +5.8% | +2.2779 to +2.9537 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 615.3 | 633.2 | +2.9% | +13.6554 to +22.1446 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.146 | −30.9% | −2.8010 to −0.9072 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*