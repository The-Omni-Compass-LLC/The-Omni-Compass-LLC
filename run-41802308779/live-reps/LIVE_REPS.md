# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.719 |
| node-hours | 2.515 | 2.398 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 267.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 488.1 | 458.6 |
| response time (ms), 95th percentile | 2164 | 2323 |
| response time (ms), 99th percentile | 3052 | 3213 |
| time over the response line (% of samples) | 18.41 | 17.74 |
| failed requests (%) | 0 | 0.01105 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 17.41 |
| utilisation (used / allocatable) | 0.06797 | 0.07213 |
| CPU used (cores), mean | 1.631 | 1.652 |
| Omni's own CPU (cores), mean | 0 | 0.07517 |
| CPU used with Omni's own (cores), mean | 1.631 | 1.727 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.9 | 389 |
| HPA replicas, mean | 2.133 | 2.528 |
| pods started | 0.2 | 1.7 |
| pod start wait, total (s) | 0.3 | 3.3 |
| pod start wait, mean (s) | 0.3 | 1.15 |
| host CPU busy, the real machine under kind (%) | 46.5 | 49.81 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 843 | 856 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.419 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.3458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 164.5 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 5.719 | −4.7% | −0.5880 to +0.0262 | no |
| node-hours | 2.515 | 2.398 | −4.7% | −0.2513 to +0.0164 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.9 | +0.1% | −0.5589 to +1.3429 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 267.1 | −3.1% | −18.5845 to +1.7559 | no |
| response time (ms), mean | 488.1 | 458.6 | −6.0% | −41.2999 to −17.7534 | yes: GAIN |
| response time (ms), 95th percentile | 2164 | 2323 | +7.3% | +9.3013 to +308.6007 | yes: LOSS |
| response time (ms), 99th percentile | 3052 | 3213 | +5.3% | −27.6530 to +348.5544 | no |
| time over the response line (% of samples) | 18.41 | 17.74 | −3.6% | −1.3871 to +0.0529 | no |
| failed requests (%) | 0 | 0.01105 | +0.011 (native is 0) | −0.0139 to +0.0360 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12 | +2.6% | −0.7144 to +1.3144 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.1 | +69.100 (native is 0) | +26.0381 to +112.1619 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 17.41 | +14.8% | −0.8693 to +5.3660 | no |
| utilisation (used / allocatable) | 0.06797 | 0.07213 | +6.1% | +0.0005 to +0.0079 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.631 | 1.652 | +1.3% | +0.0011 to +0.0405 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07517 | +0.075 (native is 0) | +0.0702 to +0.0801 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.631 | 1.727 | +5.9% | +0.0743 to +0.1176 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.9 | 389 | −4.6% | −35.9198 to −1.9672 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.133 | 2.528 | +18.5% | +0.0638 to +0.7255 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | +0.3198 to +2.6802 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.3 | +1000.0% | +0.6396 to +5.3604 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.15 | +283.3% | +0.1538 to +1.5462 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.5 | 49.81 | +7.1% | +2.9056 to +3.7227 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 843 | 856 | +1.5% | +4.8095 to +21.1905 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.419 | −9.7% | −1.1863 to +0.0242 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.3458 | +80.4% | −0.0480 to +0.3563 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.5 | +56.2% | +0.2737 to +1.5263 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 164.5 | +8.4% | +4.5880 to +20.9286 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*