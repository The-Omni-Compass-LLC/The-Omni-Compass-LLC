# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.989 | 5.673 |
| node-hours | 1.509 | 1.432 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.9 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 154.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 75.67 | 76.07 |
| response time (ms), 95th percentile | 114.1 | 117.6 |
| response time (ms), 99th percentile | 128.8 | 140.2 |
| time over the response line (% of samples) | 0.01227 | 0.01227 |
| failed requests (%) | 0 | 0.01227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.295 |
| utilisation (used / allocatable) | 0.04656 | 0.04976 |
| CPU used (cores), mean | 1.115 | 1.097 |
| Omni's own CPU (cores), mean | 0 | 0.05316 |
| CPU used with Omni's own (cores), mean | 1.115 | 1.15 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 587.6 | 571.7 |
| HPA replicas, mean | 2.851 | 2.802 |
| pods started | 1.5 | 1.8 |
| pod start wait, total (s) | 2.1 | 2.4 |
| pod start wait, mean (s) | 1.5 | 1.3 |
| host CPU busy, the real machine under kind (%) | 34.94 | 36.66 |
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
| worker nodes in service, mean | 5.989 | 5.673 | −5.3% | −0.8604 to +0.2281 | no |
| node-hours | 1.509 | 1.432 | −5.1% | −0.2163 to +0.0630 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.9 | 161.1 | +0.1% | −1.1327 to +1.4082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 154.9 | −3.6% | −16.2917 to +4.5922 | no |
| response time (ms), mean | 75.67 | 76.07 | +0.5% | −2.1763 to +2.9753 | no |
| response time (ms), 95th percentile | 114.1 | 117.6 | +3.1% | +1.0504 to +6.0596 | yes: LOSS |
| response time (ms), 99th percentile | 128.8 | 140.2 | +8.9% | +6.0640 to +16.7618 | yes: LOSS |
| time over the response line (% of samples) | 0.01227 | 0.01227 | ±0.0% | −0.0414 to +0.0414 | no |
| failed requests (%) | 0 | 0.01227 | +0.012 (native is 0) | −0.0155 to +0.0400 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.9 | +5.900 (native is 0) | +2.8013 to +8.9987 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.295 | +1006.2% | −0.3453 to +0.8819 | no |
| utilisation (used / allocatable) | 0.04656 | 0.04976 | +6.9% | −0.0034 to +0.0098 | no |
| CPU used (cores), mean | 1.115 | 1.097 | −1.7% | −0.0636 to +0.0267 | no |
| Omni's own CPU (cores), mean | 0 | 0.05316 | +0.053 (native is 0) | +0.0394 to +0.0669 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.115 | 1.15 | +3.1% | −0.0021 to +0.0715 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 587.6 | 571.7 | −2.7% | −44.1577 to +12.2032 | no |
| HPA replicas, mean | 2.851 | 2.802 | −1.7% | −0.1535 to +0.0558 | no |
| pods started | 1.5 | 1.8 | +20.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 2.1 | 2.4 | +14.3% | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 1.5 | 1.3 | −13.3% | −0.5455 to +0.1455 | no |
| host CPU busy, the real machine under kind (%) | 34.94 | 36.66 | +4.9% | +0.8051 to +2.6251 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*