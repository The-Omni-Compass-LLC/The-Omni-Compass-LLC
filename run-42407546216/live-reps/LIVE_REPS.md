# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.124 |
| node-hours | 2.513 | 2.148 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 247.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 574.4 | 517.4 |
| response time (ms), 95th percentile | 3206 | 3138 |
| response time (ms), 99th percentile | 4292 | 4189 |
| time over the response line (% of samples) | 17.9 | 17.84 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 201.4 | 210.3 |
| utilisation (used / allocatable) | 0.06737 | 0.07738 |
| CPU used (cores), mean | 1.617 | 1.573 |
| Omni's own CPU (cores), mean | 0 | 0.08322 |
| CPU used with Omni's own (cores), mean | 1.617 | 1.657 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412 | 375.5 |
| HPA replicas, mean | 2.013 | 2.513 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 46.34 | 48.87 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 633.6 | 649.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.585 |
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
| worker nodes in service, mean | 6 | 5.124 | −14.6% | −1.5215 to −0.2297 | yes: GAIN |
| node-hours | 2.513 | 2.148 | −14.5% | −0.6305 to −0.0993 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275 | +0.0% | −1.1189 to +1.2166 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 247.4 | −10.0% | −47.1622 to −7.9026 | yes: GAIN |
| response time (ms), mean | 574.4 | 517.4 | −9.9% | −72.9848 to −41.0202 | yes: GAIN |
| response time (ms), 95th percentile | 3206 | 3138 | −2.1% | −191.8913 to +54.1763 | no |
| response time (ms), 99th percentile | 4292 | 4189 | −2.4% | −265.7071 to +59.6857 | no |
| time over the response line (% of samples) | 17.9 | 17.84 | −0.3% | −0.5218 to +0.3989 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11 | +2.8% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.9 | +8.900 (native is 0) | +7.0393 to +10.7607 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 201.4 | 210.3 | +4.4% | +4.8965 to +12.8835 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06737 | 0.07738 | +14.9% | +0.0010 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.617 | 1.573 | −2.7% | −0.0714 to −0.0155 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.08322 | +0.083 (native is 0) | +0.0754 to +0.0910 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.617 | 1.657 | +2.5% | +0.0124 to +0.0671 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412 | 375.5 | −8.9% | −71.8744 to −1.0855 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.013 | 2.513 | +24.8% | +0.0181 to +0.9817 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.34 | 48.87 | +5.5% | +2.1577 to +2.8973 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 633.6 | 649.1 | +2.4% | +9.9260 to +21.0740 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.585 | −23.6% | −2.4433 to −0.3874 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*