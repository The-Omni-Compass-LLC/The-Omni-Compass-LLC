# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.738 |
| node-hours | 2.517 | 1.985 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 233.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 301.6 | 304.7 |
| response time (ms), 95th percentile | 1099 | 1331 |
| response time (ms), 99th percentile | 1740 | 1975 |
| time over the response line (% of samples) | 11.27 | 11.89 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.08 | 19.22 |
| utilisation (used / allocatable) | 0.06051 | 0.07908 |
| CPU used (cores), mean | 1.452 | 1.471 |
| Omni's own CPU (cores), mean | 0 | 0.07439 |
| CPU used with Omni's own (cores), mean | 1.452 | 1.545 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.3 | 380.3 |
| HPA replicas, mean | 2.004 | 2.182 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.4 | 0.9 |
| pod start wait, mean (s) | 0.4 | 0.7 |
| host CPU busy, the real machine under kind (%) | 42.52 | 46.02 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 805 | 814.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.057 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 114.1 | 125.1 |
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
| worker nodes in service, mean | 6 | 4.738 | −21.0% | −2.1830 to −0.3417 | yes: GAIN |
| node-hours | 2.517 | 1.985 | −21.2% | −0.9182 to −0.1474 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 | +0.0% | −0.4394 to +0.5256 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 233.2 | −14.5% | −68.5699 to −10.6855 | yes: GAIN |
| response time (ms), mean | 301.6 | 304.7 | +1.0% | −29.5718 to +35.8293 | no |
| response time (ms), 95th percentile | 1099 | 1331 | +21.0% | −36.8436 to +499.0546 | no |
| response time (ms), 99th percentile | 1740 | 1975 | +13.5% | −11.9484 to +480.4014 | no |
| time over the response line (% of samples) | 11.27 | 11.89 | +5.5% | −0.7246 to +1.9704 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.8 | +11.4% | −0.3081 to +1.9081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.6 | +127.600 (native is 0) | +40.2367 to +214.9633 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.08 | 19.22 | +12.5% | −1.9994 to +6.2761 | no |
| utilisation (used / allocatable) | 0.06051 | 0.07908 | +30.7% | +0.0055 to +0.0316 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.452 | 1.471 | +1.3% | −0.0069 to +0.0441 | no |
| Omni's own CPU (cores), mean | 0 | 0.07439 | +0.074 (native is 0) | +0.0671 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.452 | 1.545 | +6.4% | +0.0622 to +0.1238 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.3 | 380.3 | −18.1% | −142.8194 to −25.0309 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.182 | +8.9% | −0.0859 to +0.4414 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | −0.9405 to +1.9405 | no |
| pod start wait, mean (s) | 0.4 | 0.7 | +75.0% | −0.9181 to +1.5181 | no |
| host CPU busy, the real machine under kind (%) | 42.52 | 46.02 | +8.2% | +2.9650 to +4.0417 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805 | 814.1 | +1.1% | +0.8925 to +17.3075 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.057 | −32.4% | −3.2550 to −0.6314 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.875 | +11.7% | −0.1322 to +0.3155 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.7 | −10.5% | −1.2556 to +0.8556 | no |
| queue: job turnaround, submitted to done, mean (s) | 114.1 | 125.1 | +9.7% | +0.9876 to +21.0707 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*