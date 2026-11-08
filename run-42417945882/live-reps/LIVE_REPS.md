# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.2 | 170.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.2 | 170.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 464.8 | 463.2 |
| response time (ms), 95th percentile | 1918 | 2132 |
| response time (ms), 99th percentile | 4304 | 5202 |
| time over the response line (% of samples) | 20.85 | 20.09 |
| failed requests (%) | 2.175 | 1.507 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.242 | 2.17 |
| utilisation (used / allocatable) | 0.09119 | 0.0903 |
| CPU used (cores), mean | 2.189 | 2.167 |
| Omni's own CPU (cores), mean | 0 | 0.05072 |
| CPU used with Omni's own (cores), mean | 2.189 | 2.218 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.3 | 325 |
| HPA replicas, mean | 14.84 | 15.43 |
| pods started | 5.7 | 6.1 |
| pod start wait, total (s) | 8.8 | 10.5 |
| pod start wait, mean (s) | 1.575 | 1.77 |
| host CPU busy, the real machine under kind (%) | 63.04 | 64.35 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 272.6 | 296.7 |
| second app: response time (ms), 99th percentile | 2582 | 2590 |
| second app: time over the response line (% of samples) | 12.62 | 12.56 |
| second app: failed requests (%) | 10.23 | 10.43 |

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
| node-hours | 1.515 | 1.515 | 0.0% | raw −0.0098 to +0.0098 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 171.2 | 170.9 | −0.2% | −1.3567 to +0.8082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.2 | 170.9 | −0.2% | −1.3567 to +0.8082 | no |
| response time (ms), mean | 464.8 | 463.2 | −0.4% | −31.4692 to +28.1420 | no |
| response time (ms), 95th percentile | 1918 | 2132 | +11.2% | −198.3291 to +627.0091 | no |
| response time (ms), 99th percentile | 4304 | 5202 | +20.9% | +316.7288 to +1478.8612 | yes: LOSS |
| time over the response line (% of samples) | 20.85 | 20.09 | −3.7% | −2.1483 to +0.6157 | no |
| failed requests (%) | 2.175 | 1.507 | −30.7% | −1.3148 to −0.0213 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.2 | −1.4% | −0.8872 to +0.6872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.2 | +121.200 (native is 0) | +100.0025 to +142.3975 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.242 | 2.17 | +74.8% | +0.0400 to +1.8167 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09119 | 0.0903 | −1.0% | −0.0025 to +0.0007 | no |
| CPU used (cores), mean | 2.189 | 2.167 | −1.0% | −0.0590 to +0.0162 | no |
| Omni's own CPU (cores), mean | 0 | 0.05072 | +0.051 (native is 0) | +0.0420 to +0.0594 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.189 | 2.218 | +1.3% | −0.0064 to +0.0651 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.3 | 325 | +0.8% | −2.7044 to +8.1232 | no |
| HPA replicas, mean | 14.84 | 15.43 | +4.0% | −0.0388 to +1.2125 | no |
| pods started | 5.7 | 6.1 | +7.0% | −0.4396 to +1.2396 | no |
| pod start wait, total (s) | 8.8 | 10.5 | +19.3% | −0.3800 to +3.7800 | no |
| pod start wait, mean (s) | 1.575 | 1.77 | +12.4% | −0.0967 to +0.4870 | no |
| host CPU busy, the real machine under kind (%) | 63.04 | 64.35 | +2.1% | +0.4727 to +2.1443 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 272.6 | 296.7 | +8.8% | −8.8757 to +57.0727 | no |
| second app: response time (ms), 99th percentile | 2582 | 2590 | +0.3% | −1834.7770 to +1849.7682 | no |
| second app: time over the response line (% of samples) | 12.62 | 12.56 | −0.4% | −0.6362 to +0.5269 | no |
| second app: failed requests (%) | 10.23 | 10.43 | +2.0% | −0.1720 to +0.5849 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*