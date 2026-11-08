# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.873 | 3.646 |
| node-hours | 0.4846 | 0.6153 |
| energy, parked workers still on at idle power (Wh, declared model) | 66.93 | 104.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.32 | 87.81 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 565.2 | 663.5 |
| response time (ms), 95th percentile | 1257 | 2354 |
| response time (ms), 99th percentile | 4764 | 6624 |
| time over the response line (% of samples) | 44.94 | 41.16 |
| failed requests (%) | 30.86 | 21.06 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 11.11 |
| pods with no machine to take them (unschedulable) | 2.333 | 20.67 |
| time pods had no machine to take them, pod-minutes | 2.133 | 40.31 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.733 | 49.24 |
| utilisation (used / allocatable) | 0.5236 | 0.5132 |
| CPU used (cores), mean | 2.858 | 3.535 |
| Omni's own CPU (cores), mean | 0 | 0.01597 |
| CPU used with Omni's own (cores), mean | 2.858 | 3.551 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 135.5 | 147.2 |
| HPA replicas, mean | 9.636 | 20.69 |
| pods started | 2.333 | 24 |
| pod start wait, total (s) | 58.33 | 2501 |
| pod start wait, mean (s) | 19.27 | 103.5 |
| machines billed, machine-hours | 0.36 | 0.574 |
| compute bill at list price ($) | 0.03456 | 0.0551 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.873 | 3.646 | +26.9% | −0.3108 to +1.8574 | no |
| node-hours | 0.4846 | 0.6153 | +27.0% | −0.0776 to +0.3389 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 66.93 | 104.9 | +56.7% | +26.9373 to +48.9966 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.32 | 87.81 | +34.4% | −1.2341 to +46.2236 | no |
| response time (ms), mean | 565.2 | 663.5 | +17.4% | −304.5927 to +501.1029 | no |
| response time (ms), 95th percentile | 1257 | 2354 | +87.3% | −3465.7220 to +5659.8120 | no |
| response time (ms), 99th percentile | 4764 | 6624 | +39.0% | −3895.1500 to +7614.9687 | no |
| time over the response line (% of samples) | 44.94 | 41.16 | −8.4% | −16.7043 to +9.1434 | no |
| failed requests (%) | 30.86 | 21.06 | −31.8% | −43.3664 to +23.7506 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.33 | +21.333 (native is 0) | +19.8990 to +22.7677 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.333 | 20.67 | +785.7% | +10.7436 to +25.9231 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 2.133 | 40.31 | +1789.3% | +9.1727 to +67.1717 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.733 | 49.24 | +758.9% | +12.7560 to +74.2662 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5236 | 0.5132 | −2.0% | −0.1014 to +0.0805 | no |
| CPU used (cores), mean | 2.858 | 3.535 | +23.7% | +0.0857 to +1.2684 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01597 | +0.016 (native is 0) | +0.0106 to +0.0213 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.858 | 3.551 | +24.3% | +0.1064 to +1.2797 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 135.5 | 147.2 | +8.6% | −10.9382 to +34.3225 | no |
| HPA replicas, mean | 9.636 | 20.69 | +114.7% | +2.8549 to +19.2501 | yes: power given |
| pods started | 2.333 | 24 | +928.6% | +11.3235 to +32.0098 | yes: power given |
| pod start wait, total (s) | 58.33 | 2501 | +4186.9% | +938.8215 to +3945.8452 | yes: LOSS |
| pod start wait, mean (s) | 19.27 | 103.5 | +437.0% | +39.8624 to +128.5340 | yes: LOSS |
| machines billed, machine-hours | 0.36 | 0.574 | +59.4% | +0.2088 to +0.2192 | yes: power given |
| compute bill at list price ($) | 0.03456 | 0.0551 | +59.4% | +0.0200 to +0.0210 | yes: power given |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*