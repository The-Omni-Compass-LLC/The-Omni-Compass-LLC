# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.971 |
| node-hours | 2.515 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 270.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 128.2 | 107.2 |
| response time (ms), 95th percentile | 220.9 | 235.4 |
| response time (ms), 99th percentile | 322.7 | 353.7 |
| time over the response line (% of samples) | 0.224 | 0.3342 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1046 | 1133 |
| utilisation (used / allocatable) | 0.05922 | 0.05794 |
| CPU used (cores), mean | 1.421 | 1.384 |
| Omni's own CPU (cores), mean | 0 | 0.06929 |
| CPU used with Omni's own (cores), mean | 1.421 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 466.4 |
| HPA replicas, mean | 1.94 | 2.16 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.25 |
| host CPU busy, the real machine under kind (%) | 44.01 | 45.74 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1408 | 1449 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.477 |
| queue: job wait, submitted to its first pod running, mean (s) | 101 | 172.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 504.5 | 763.5 |
| queue: job turnaround, submitted to done, mean (s) | 779.6 | 822.8 |
| queue: jobs unfinished at the window's end | 8.8 | 10.9 |
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
| worker nodes in service, mean | 6 | 5.971 | −0.5% | −0.0746 to +0.0166 | no |
| node-hours | 2.515 | 2.504 | −0.4% | −0.0292 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.4 | −0.2% | −1.4201 to +0.5157 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 270.5 | −0.5% | −2.6420 to −0.0832 | yes: GAIN |
| response time (ms), mean | 128.2 | 107.2 | −16.4% | −28.5779 to −13.4496 | yes: GAIN |
| response time (ms), 95th percentile | 220.9 | 235.4 | +6.6% | −2.4107 to +31.3577 | no |
| response time (ms), 99th percentile | 322.7 | 353.7 | +9.6% | −1.8838 to +63.9376 | no |
| time over the response line (% of samples) | 0.224 | 0.3342 | +49.2% | −0.2104 to +0.4308 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 | +50.0% | −0.6872 to +0.8872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.4 | +110.400 (native is 0) | +95.9232 to +124.8768 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1046 | 1133 | +8.3% | +30.9312 to +142.5988 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05922 | 0.05794 | −2.2% | −0.0028 to +0.0003 | no |
| CPU used (cores), mean | 1.421 | 1.384 | −2.6% | −0.0684 to −0.0057 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06929 | +0.069 (native is 0) | +0.0611 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.454 | +2.3% | +0.0052 to +0.0593 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.6 | 466.4 | +1.9% | −2.0823 to +19.7398 | no |
| HPA replicas, mean | 1.94 | 2.16 | +11.4% | +0.0698 to +0.3718 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 44.01 | 45.74 | +3.9% | +1.1961 to +2.2611 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1408 | 1449 | +2.9% | −12.7104 to +94.3104 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.477 | −8.7% | −1.7166 to +0.6703 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 101 | 172.8 | +71.1% | +20.0510 to +123.5240 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 504.5 | 763.5 | +51.3% | +57.6831 to +460.3169 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 779.6 | 822.8 | +5.5% | +1.0309 to +85.2775 | yes: LOSS |
| queue: jobs unfinished at the window's end | 8.8 | 10.9 | +23.9% | −1.1771 to +5.3771 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*