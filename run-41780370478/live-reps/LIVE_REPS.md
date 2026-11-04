# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 519.3 | 519.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.3 | 519.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 280.9 | 179.5 |
| response time (ms), 95th percentile | 740.1 | 369 |
| response time (ms), 99th percentile | 2351 | 2272 |
| time over the response line (% of samples) | 20.29 | 15.22 |
| failed requests (%) | 11.76 | 12.21 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.7 | 24.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 71.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.325 | 0.505 |
| utilisation (used / allocatable) | 0.105 | 0.1051 |
| CPU used (cores), mean | 2.521 | 2.523 |
| Omni's own CPU (cores), mean | 0 | 0.04644 |
| CPU used with Omni's own (cores), mean | 2.521 | 2.57 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.9 | 297.8 |
| HPA replicas, mean | 9.577 | 11.79 |
| pods started | 5.4 | 9.3 |
| pod start wait, total (s) | 9.2 | 16 |
| pod start wait, mean (s) | 1.72 | 1.692 |
| host CPU busy, the real machine under kind (%) | 70.78 | 72.35 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.515 | 4.515 | +0.0% | −0.0067 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 519.3 | 519.5 | +0.0% | −0.7782 to +1.2208 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.3 | 519.5 | +0.0% | −0.7782 to +1.2208 | no |
| response time (ms), mean | 280.9 | 179.5 | −36.1% | −127.1475 to −75.4834 | yes: GAIN |
| response time (ms), 95th percentile | 740.1 | 369 | −50.1% | −502.3358 to −239.8952 | yes: GAIN |
| response time (ms), 99th percentile | 2351 | 2272 | −3.4% | −617.6579 to +459.7457 | no |
| time over the response line (% of samples) | 20.29 | 15.22 | −25.0% | −6.9479 to −3.1875 | yes: GAIN |
| failed requests (%) | 11.76 | 12.21 | +3.8% | −0.1266 to +1.0144 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.7 | 24.8 | −16.5% | −6.3484 to −3.4516 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.3 | +48.300 (native is 0) | +38.5035 to +58.0965 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.325 | 0.505 | +55.4% | −0.1297 to +0.4897 | no |
| utilisation (used / allocatable) | 0.105 | 0.1051 | +0.1% | −0.0011 to +0.0014 | no |
| CPU used (cores), mean | 2.521 | 2.523 | +0.1% | −0.0273 to +0.0325 | no |
| Omni's own CPU (cores), mean | 0 | 0.04644 | +0.046 (native is 0) | +0.0388 to +0.0541 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.521 | 2.57 | +1.9% | +0.0132 to +0.0850 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.9 | 297.8 | +0.6% | −2.2894 to +6.0665 | no |
| HPA replicas, mean | 9.577 | 11.79 | +23.1% | +0.4884 to +3.9351 | yes: power given |
| pods started | 5.4 | 9.3 | +72.2% | +2.0090 to +5.7910 | yes: power given |
| pod start wait, total (s) | 9.2 | 16 | +73.9% | +3.1247 to +10.4753 | yes: LOSS |
| pod start wait, mean (s) | 1.72 | 1.692 | −1.7% | −0.2526 to +0.1956 | no |
| host CPU busy, the real machine under kind (%) | 70.78 | 72.35 | +2.2% | +0.4756 to +2.6518 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*