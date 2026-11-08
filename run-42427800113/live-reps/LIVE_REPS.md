# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 454.2 | 418 |
| response time (ms), 95th percentile | 1822 | 1908 |
| response time (ms), 99th percentile | 4975 | 4525 |
| time over the response line (% of samples) | 20.09 | 20.07 |
| failed requests (%) | 2.217 | 2.323 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.785 | 1.232 |
| utilisation (used / allocatable) | 0.09192 | 0.0915 |
| CPU used (cores), mean | 2.206 | 2.196 |
| Omni's own CPU (cores), mean | 0 | 0.05093 |
| CPU used with Omni's own (cores), mean | 2.206 | 2.247 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.5 | 317.8 |
| HPA replicas, mean | 14.8 | 15.09 |
| pods started | 6 | 6.6 |
| pod start wait, total (s) | 9.3 | 10.2 |
| pod start wait, mean (s) | 1.565 | 1.545 |
| host CPU busy, the real machine under kind (%) | 63.25 | 65.04 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 372.8 | 417 |
| second app: response time (ms), 99th percentile | 2505 | 2842 |
| second app: time over the response line (% of samples) | 13.28 | 13.22 |
| second app: failed requests (%) | 10.22 | 10.46 |

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
| node-hours | 1.514 | 1.514 | +0.0% | −0.0091 to +0.0097 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 | −0.0% | −1.1661 to +1.1496 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 | −0.0% | −1.1661 to +1.1496 | no |
| response time (ms), mean | 454.2 | 418 | −8.0% | −109.0027 to +36.6207 | no |
| response time (ms), 95th percentile | 1822 | 1908 | +4.7% | −273.6652 to +445.3912 | no |
| response time (ms), 99th percentile | 4975 | 4525 | −9.0% | −1248.6975 to +348.5779 | no |
| time over the response line (% of samples) | 20.09 | 20.07 | −0.1% | −2.2391 to +2.1977 | no |
| failed requests (%) | 2.217 | 2.323 | +4.8% | −1.2882 to +1.5019 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.9 | +3.9% | −0.5953 to +1.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.3 | +107.300 (native is 0) | +87.9821 to +126.6179 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.785 | 1.232 | +56.9% | −0.3555 to +1.2488 | no |
| utilisation (used / allocatable) | 0.09192 | 0.0915 | −0.5% | −0.0022 to +0.0013 | no |
| CPU used (cores), mean | 2.206 | 2.196 | −0.5% | −0.0524 to +0.0321 | no |
| Omni's own CPU (cores), mean | 0 | 0.05093 | +0.051 (native is 0) | +0.0445 to +0.0573 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.206 | 2.247 | +1.8% | +0.0019 to +0.0797 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.5 | 317.8 | +0.1% | −7.0550 to +7.6506 | no |
| HPA replicas, mean | 14.8 | 15.09 | +2.0% | −0.1516 to +0.7437 | no |
| pods started | 6 | 6.6 | +10.0% | −0.2396 to +1.4396 | no |
| pod start wait, total (s) | 9.3 | 10.2 | +9.7% | −1.1358 to +2.9358 | no |
| pod start wait, mean (s) | 1.565 | 1.545 | −1.3% | −0.3362 to +0.2966 | no |
| host CPU busy, the real machine under kind (%) | 63.25 | 65.04 | +2.8% | +0.9630 to +2.6186 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 372.8 | 417 | +11.9% | −42.4640 to +130.9310 | no |
| second app: response time (ms), 99th percentile | 2505 | 2842 | +13.4% | −816.9991 to +1490.4105 | no |
| second app: time over the response line (% of samples) | 13.28 | 13.22 | −0.4% | −1.0349 to +0.9192 | no |
| second app: failed requests (%) | 10.22 | 10.46 | +2.3% | −0.4083 to +0.8707 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*