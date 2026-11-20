# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.805 |
| node-hours | 2.508 | 2.015 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 236.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 527.9 | 492.3 |
| response time (ms), 95th percentile | 3000 | 3016 |
| response time (ms), 99th percentile | 3942 | 3955 |
| time over the response line (% of samples) | 17.64 | 17.52 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.2 | 203.1 |
| utilisation (used / allocatable) | 0.0655 | 0.0798 |
| CPU used (cores), mean | 1.572 | 1.527 |
| Omni's own CPU (cores), mean | 0 | 0.0797 |
| CPU used with Omni's own (cores), mean | 1.572 | 1.607 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.4 | 371.3 |
| HPA replicas, mean | 2.139 | 2.274 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.6 | 0 |
| pod start wait, mean (s) | 0.6 | 0 |
| host CPU busy, the real machine under kind (%) | 45.05 | 47.53 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 613.3 | 630.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.054 |
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
| worker nodes in service, mean | 6 | 4.805 | −19.9% | −1.7989 to −0.5906 | yes: GAIN |
| node-hours | 2.508 | 2.015 | −19.6% | −0.7447 to −0.2402 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.3 | +0.1% | −0.4826 to +1.1378 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 236.7 | −13.6% | −56.4967 to −18.0148 | yes: GAIN |
| response time (ms), mean | 527.9 | 492.3 | −6.7% | −51.1384 to −19.9633 | yes: GAIN |
| response time (ms), 95th percentile | 3000 | 3016 | +0.6% | −68.7777 to +102.1117 | no |
| response time (ms), 99th percentile | 3942 | 3955 | +0.3% | −149.6618 to +174.3978 | no |
| time over the response line (% of samples) | 17.64 | 17.52 | −0.7% | −0.7111 to +0.4752 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.9 | +3.8% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 | +9.400 (native is 0) | +7.9225 to +10.8775 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.2 | 203.1 | +1.4% | −2.5527 to +8.1560 | no |
| utilisation (used / allocatable) | 0.0655 | 0.0798 | +21.8% | +0.0068 to +0.0218 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.572 | 1.527 | −2.9% | −0.1017 to +0.0117 | no |
| Omni's own CPU (cores), mean | 0 | 0.0797 | +0.080 (native is 0) | +0.0704 to +0.0890 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.572 | 1.607 | +2.2% | −0.0257 to +0.0952 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.4 | 371.3 | −12.1% | −80.6857 to −21.4599 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.139 | 2.274 | +6.3% | −0.3570 to +0.6265 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.6 | 0 | −100.0% | −1.9572 to +0.7572 | no |
| pod start wait, mean (s) | 0.6 | 0 | −100.0% | −1.9572 to +0.7572 | no |
| host CPU busy, the real machine under kind (%) | 45.05 | 47.53 | +5.5% | +1.9291 to +3.0314 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 613.3 | 630.3 | +2.8% | +8.9565 to +25.0435 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.054 | −32.4% | −2.8915 to −1.0006 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*