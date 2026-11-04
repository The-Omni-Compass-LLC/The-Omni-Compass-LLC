# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.86 |
| node-hours | 2.518 | 2.036 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 238.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 550.3 | 512 |
| response time (ms), 95th percentile | 3073 | 3113 |
| response time (ms), 99th percentile | 4061 | 4066 |
| time over the response line (% of samples) | 18.29 | 18.21 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 206.6 | 210.7 |
| utilisation (used / allocatable) | 0.06641 | 0.08182 |
| CPU used (cores), mean | 1.594 | 1.574 |
| Omni's own CPU (cores), mean | 0 | 0.08216 |
| CPU used with Omni's own (cores), mean | 1.594 | 1.656 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.1 | 362.6 |
| HPA replicas, mean | 2.377 | 2.238 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 46.02 | 48.73 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 631.9 | 650.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.108 |
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
| worker nodes in service, mean | 6 | 4.86 | −19.0% | −1.7974 to −0.4829 | yes: GAIN |
| node-hours | 2.518 | 2.036 | −19.1% | −0.7542 to −0.2090 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 274.7 | −0.2% | −1.5312 to +0.3336 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 238.9 | −13.2% | −56.5249 to −16.3644 | yes: GAIN |
| response time (ms), mean | 550.3 | 512 | −7.0% | −55.5032 to −21.1111 | yes: GAIN |
| response time (ms), 95th percentile | 3073 | 3113 | +1.3% | −34.8700 to +114.6760 | no |
| response time (ms), 99th percentile | 4061 | 4066 | +0.1% | −162.2271 to +171.6651 | no |
| time over the response line (% of samples) | 18.29 | 18.21 | −0.4% | −0.5198 to +0.3708 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.1 | +3.7% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.4 | +9.400 (native is 0) | +8.2222 to +10.5778 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 206.6 | 210.7 | +2.0% | +0.4484 to +7.7083 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06641 | 0.08182 | +23.2% | +0.0056 to +0.0252 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.594 | 1.574 | −1.2% | −0.0431 to +0.0036 | no |
| Omni's own CPU (cores), mean | 0 | 0.08216 | +0.082 (native is 0) | +0.0726 to +0.0918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.594 | 1.656 | +3.9% | +0.0389 to +0.0859 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.1 | 362.6 | −13.3% | −93.1417 to −17.8873 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.377 | 2.238 | −5.8% | −0.4695 to +0.1916 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.02 | 48.73 | +5.9% | +2.3254 to +3.0933 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 631.9 | 650.2 | +2.9% | +11.5979 to +25.0021 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.108 | −31.5% | −2.9456 to −0.8385 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*