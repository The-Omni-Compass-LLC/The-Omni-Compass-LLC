# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 539.5 | 505.6 |
| response time (ms), 95th percentile | 2351 | 2299 |
| response time (ms), 99th percentile | 5458 | 5410 |
| time over the response line (% of samples) | 24.47 | 24.4 |
| failed requests (%) | 3.09 | 2.542 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.433 | 1.102 |
| utilisation (used / allocatable) | 0.09829 | 0.0969 |
| CPU used (cores), mean | 2.359 | 2.326 |
| Omni's own CPU (cores), mean | 0 | 0.05648 |
| CPU used with Omni's own (cores), mean | 2.359 | 2.382 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.6 | 302 |
| HPA replicas, mean | 15.11 | 15.95 |
| pods started | 5.1 | 5.8 |
| pod start wait, total (s) | 7.7 | 9.5 |
| pod start wait, mean (s) | 1.456 | 1.655 |
| host CPU busy, the real machine under kind (%) | 68.29 | 69.62 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 285.4 | 292.1 |
| second app: response time (ms), 99th percentile | 1526 | 1462 |
| second app: time over the response line (% of samples) | 14.52 | 14.82 |
| second app: failed requests (%) | 12.75 | 13.12 |

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
| node-hours | 1.516 | 1.514 | −0.1% | −0.0088 to +0.0058 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.4 | −0.3% | −1.3089 to +0.4424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.4 | −0.3% | −1.3089 to +0.4424 | no |
| response time (ms), mean | 539.5 | 505.6 | −6.3% | −104.3633 to +36.5409 | no |
| response time (ms), 95th percentile | 2351 | 2299 | −2.2% | −543.4520 to +438.7780 | no |
| response time (ms), 99th percentile | 5458 | 5410 | −0.9% | −1361.0469 to +1265.1453 | no |
| time over the response line (% of samples) | 24.47 | 24.4 | −0.3% | −2.4453 to +2.3081 | no |
| failed requests (%) | 3.09 | 2.542 | −17.7% | −2.0537 to +0.9574 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 | −5.7% | −0.8770 to −0.1230 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127 | +127.000 (native is 0) | +111.8786 to +142.1214 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.433 | 1.102 | −23.1% | −1.0932 to +0.4299 | no |
| utilisation (used / allocatable) | 0.09829 | 0.0969 | −1.4% | −0.0024 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.359 | 2.326 | −1.4% | −0.0587 to −0.0078 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05648 | +0.056 (native is 0) | +0.0480 to +0.0649 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.359 | 2.382 | +1.0% | −0.0037 to +0.0502 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.6 | 302 | +1.5% | −0.8098 to +9.6110 | no |
| HPA replicas, mean | 15.11 | 15.95 | +5.6% | +0.0478 to +1.6369 | yes: power given |
| pods started | 5.1 | 5.8 | +13.7% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 7.7 | 9.5 | +23.4% | −1.0771 to +4.6771 | no |
| pod start wait, mean (s) | 1.456 | 1.655 | +13.7% | −0.2049 to +0.6030 | no |
| host CPU busy, the real machine under kind (%) | 68.29 | 69.62 | +1.9% | +0.5998 to +2.0629 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 285.4 | 292.1 | +2.3% | −16.5742 to +29.8432 | no |
| second app: response time (ms), 99th percentile | 1526 | 1462 | −4.2% | −1023.0379 to +895.9159 | no |
| second app: time over the response line (% of samples) | 14.52 | 14.82 | +2.0% | −0.2982 to +0.8893 | no |
| second app: failed requests (%) | 12.75 | 13.12 | +2.9% | +0.0674 to +0.6827 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*