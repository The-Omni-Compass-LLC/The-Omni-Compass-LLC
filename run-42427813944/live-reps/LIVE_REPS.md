# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.33 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.2 | 479.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.2 | 479.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 264.6 | 135.2 |
| response time (ms), 95th percentile | 691.4 | 277.2 |
| response time (ms), 99th percentile | 1296 | 644.3 |
| time over the response line (% of samples) | 12.83 | 2.98 |
| failed requests (%) | 1.257 | 1.066 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.9 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 62.04 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.73 |
| utilisation (used / allocatable) | 0.07745 | 0.07547 |
| CPU used (cores), mean | 1.859 | 1.811 |
| Omni's own CPU (cores), mean | 0 | 0.04467 |
| CPU used with Omni's own (cores), mean | 1.859 | 1.856 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.4 | 400.2 |
| HPA replicas, mean | 9.683 | 12.1 |
| pods started | 6.4 | 15.1 |
| pod start wait, total (s) | 9.1 | 23.9 |
| pod start wait, mean (s) | 1.486 | 1.544 |
| host CPU busy, the real machine under kind (%) | 54.09 | 54.35 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 4.33 | 4.337 | +0.2% | −0.0013 to +0.0156 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.2 | 479.7 | −0.1% | −1.7111 to +0.7033 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.2 | 479.7 | −0.1% | −1.7111 to +0.7033 | no |
| response time (ms), mean | 264.6 | 135.2 | −48.9% | −175.3100 to −83.3844 | yes: GAIN |
| response time (ms), 95th percentile | 691.4 | 277.2 | −59.9% | −545.8938 to −282.4102 | yes: GAIN |
| response time (ms), 99th percentile | 1296 | 644.3 | −50.3% | −867.2229 to −436.9303 | yes: GAIN |
| time over the response line (% of samples) | 12.83 | 2.98 | −76.8% | −14.9833 to −4.7109 | yes: GAIN |
| failed requests (%) | 1.257 | 1.066 | −15.2% | −0.3317 to −0.0500 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.9 | 8.7 | −60.3% | −19.5605 to −6.8395 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70 | +70.000 (native is 0) | +53.3470 to +86.6530 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.73 | +71.1% | −0.1334 to +0.7401 | no |
| utilisation (used / allocatable) | 0.07745 | 0.07547 | −2.6% | −0.0028 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.859 | 1.811 | −2.6% | −0.0678 to −0.0273 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04467 | +0.045 (native is 0) | +0.0376 to +0.0517 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.859 | 1.856 | −0.2% | −0.0190 to +0.0133 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.4 | 400.2 | +2.0% | +4.9795 to +10.5456 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.683 | 12.1 | +25.0% | +0.6271 to +4.2105 | yes: power given |
| pods started | 6.4 | 15.1 | +135.9% | +5.0363 to +12.3637 | yes: power given |
| pod start wait, total (s) | 9.1 | 23.9 | +162.6% | +7.3985 to +22.2015 | yes: LOSS |
| pod start wait, mean (s) | 1.486 | 1.544 | +3.9% | −0.1733 to +0.2898 | no |
| host CPU busy, the real machine under kind (%) | 54.09 | 54.35 | +0.5% | −0.1056 to +0.6286 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*