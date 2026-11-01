# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 532 | 486.4 |
| response time (ms), 95th percentile | 2251 | 2331 |
| response time (ms), 99th percentile | 5223 | 5567 |
| time over the response line (% of samples) | 24.68 | 22.8 |
| failed requests (%) | 3.214 | 2.632 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.427 | 2.072 |
| utilisation (used / allocatable) | 0.09646 | 0.09543 |
| CPU used (cores), mean | 2.315 | 2.29 |
| Omni's own CPU (cores), mean | 0 | 0.01316 |
| CPU used with Omni's own (cores), mean | 2.315 | 2.303 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.3 | 308.5 |
| HPA replicas, mean | 15 | 15.34 |
| pods started | 5.2 | 4 |
| pod start wait, total (s) | 8.5 | 7.2 |
| pod start wait, mean (s) | 1.631 | 1.505 |
| host CPU busy, the real machine under kind (%) | 67.25 | 67.06 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 300.5 | 269.5 |
| second app: response time (ms), 99th percentile | 2092 | 1554 |
| second app: time over the response line (% of samples) | 14.6 | 13.83 |
| second app: failed requests (%) | 12.49 | 12.43 |

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
| node-hours | 1.517 | 1.519 | +0.1% | −0.0049 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.5 | −0.0% | −1.0548 to +0.8858 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.5 | −0.0% | −1.0548 to +0.8858 | no |
| response time (ms), mean | 532 | 486.4 | −8.6% | −84.5312 to −6.7002 | yes: GAIN |
| response time (ms), 95th percentile | 2251 | 2331 | +3.6% | −158.3773 to +318.4543 | no |
| response time (ms), 99th percentile | 5223 | 5567 | +6.6% | −649.8739 to +1337.2947 | no |
| time over the response line (% of samples) | 24.68 | 22.8 | −7.6% | −4.1450 to +0.3810 | no |
| failed requests (%) | 3.214 | 2.632 | −18.1% | −1.4469 to +0.2832 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.2 | −8.9% | −1.5388 to −0.0612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 | +42.200 (native is 0) | +29.7885 to +54.6115 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.427 | 2.072 | +45.2% | +0.0836 to +1.2064 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09646 | 0.09543 | −1.1% | −0.0026 to +0.0005 | no |
| CPU used (cores), mean | 2.315 | 2.29 | −1.1% | −0.0627 to +0.0130 | no |
| Omni's own CPU (cores), mean | 0 | 0.01316 | +0.013 (native is 0) | +0.0121 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.315 | 2.303 | −0.5% | −0.0496 to +0.0263 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.3 | 308.5 | +0.7% | −3.4461 to +7.9696 | no |
| HPA replicas, mean | 15 | 15.34 | +2.3% | −0.0179 to +0.6940 | no |
| pods started | 5.2 | 4 | −23.1% | −2.4972 to +0.0972 | no |
| pod start wait, total (s) | 8.5 | 7.2 | −15.3% | −4.6559 to +2.0559 | no |
| pod start wait, mean (s) | 1.631 | 1.505 | −7.8% | −0.7095 to +0.4561 | no |
| host CPU busy, the real machine under kind (%) | 67.25 | 67.06 | −0.3% | −0.7957 to +0.4030 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 300.5 | 269.5 | −10.3% | −81.9418 to +19.9758 | no |
| second app: response time (ms), 99th percentile | 2092 | 1554 | −25.7% | −1478.1134 to +403.8254 | no |
| second app: time over the response line (% of samples) | 14.6 | 13.83 | −5.3% | −1.1683 to −0.3716 | yes: GAIN |
| second app: failed requests (%) | 12.49 | 12.43 | −0.4% | −0.6073 to +0.4960 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*