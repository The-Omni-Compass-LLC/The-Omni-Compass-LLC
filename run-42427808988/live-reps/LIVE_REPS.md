# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.223 |
| node-hours | 2.515 | 2.186 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 251.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 622 | 588.5 |
| response time (ms), 95th percentile | 3502 | 3490 |
| response time (ms), 99th percentile | 4536 | 4633 |
| time over the response line (% of samples) | 18.72 | 18.59 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 213 | 218.5 |
| utilisation (used / allocatable) | 0.06966 | 0.08004 |
| CPU used (cores), mean | 1.672 | 1.664 |
| Omni's own CPU (cores), mean | 0 | 0.08965 |
| CPU used with Omni's own (cores), mean | 1.672 | 1.754 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.4 | 363.5 |
| HPA replicas, mean | 2.218 | 2.25 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.1 | 1.8 |
| pod start wait, mean (s) | 0.1 | 0.9 |
| host CPU busy, the real machine under kind (%) | 48.27 | 51.15 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 662.2 | 682.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.682 |
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
| worker nodes in service, mean | 6 | 5.223 | −12.9% | −1.3866 to −0.1669 | yes: GAIN |
| node-hours | 2.515 | 2.186 | −13.1% | −0.5909 to −0.0681 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276 | −0.1% | −1.1942 to +0.7870 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 251.6 | −8.9% | −44.2683 to −4.7639 | yes: GAIN |
| response time (ms), mean | 622 | 588.5 | −5.4% | −44.0293 to −22.8185 | yes: GAIN |
| response time (ms), 95th percentile | 3502 | 3490 | −0.3% | −150.4754 to +127.4164 | no |
| response time (ms), 99th percentile | 4536 | 4633 | +2.1% | −66.4445 to +261.0287 | no |
| time over the response line (% of samples) | 18.72 | 18.59 | −0.7% | −0.5960 to +0.3431 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.6 | +3.6% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.6 | +8.600 (native is 0) | +7.0474 to +10.1526 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 213 | 218.5 | +2.6% | +3.5030 to +7.4603 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06966 | 0.08004 | +14.9% | +0.0021 to +0.0187 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.672 | 1.664 | −0.5% | −0.0351 to +0.0199 | no |
| Omni's own CPU (cores), mean | 0 | 0.08965 | +0.090 (native is 0) | +0.0793 to +0.1000 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.672 | 1.754 | +4.9% | +0.0542 to +0.1099 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.4 | 363.5 | −9.9% | −79.9092 to +0.0664 | no |
| HPA replicas, mean | 2.218 | 2.25 | +1.4% | −0.3179 to +0.3816 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.1 | 1.8 | +1700.0% | −2.4029 to +5.8029 | no |
| pod start wait, mean (s) | 0.1 | 0.9 | +800.0% | −1.2732 to +2.8732 | no |
| host CPU busy, the real machine under kind (%) | 48.27 | 51.15 | +6.0% | +2.3905 to +3.3745 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 662.2 | 682.9 | +3.1% | +14.6019 to +26.7981 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.682 | −22.0% | −2.2505 to −0.3846 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*