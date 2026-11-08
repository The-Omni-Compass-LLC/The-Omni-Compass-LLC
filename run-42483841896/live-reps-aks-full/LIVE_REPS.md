# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.855 | 3.679 |
| node-hours | 0.489 | 0.6187 |
| energy, parked workers still on at idle power (Wh, declared model) | 68.6 | 107.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 66.73 | 90.66 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 464.7 | 619.3 |
| response time (ms), 95th percentile | 1074 | 1480 |
| response time (ms), 99th percentile | 2533 | 5842 |
| time over the response line (% of samples) | 46.34 | 45.1 |
| failed requests (%) | 33.74 | 28.83 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.667 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.67 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25.56 |
| pods with no machine to take them (unschedulable) | 2.333 | 21.67 |
| time pods had no machine to take them, pod-minutes | 2.933 | 39.82 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.889 | 47.18 |
| utilisation (used / allocatable) | 0.5294 | 0.5292 |
| CPU used (cores), mean | 2.871 | 3.7 |
| Omni's own CPU (cores), mean | 0 | 0.0145 |
| CPU used with Omni's own (cores), mean | 2.871 | 3.714 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 135.7 | 145.9 |
| HPA replicas, mean | 9.634 | 20.66 |
| pods started | 1.667 | 26.33 |
| pod start wait, total (s) | 38 | 2555 |
| pod start wait, mean (s) | 7.6 | 95.33 |
| machines billed, machine-hours | 0.3709 | 0.5641 |
| compute bill at list price ($) | 0.03561 | 0.05415 |
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
| worker nodes in service, mean | 2.855 | 3.679 | +28.9% | +0.7459 to +0.9039 | yes: power given |
| node-hours | 0.489 | 0.6187 | +26.5% | +0.1134 to +0.1460 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 68.6 | 107.3 | +56.4% | +36.3165 to +41.0998 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 66.73 | 90.66 | +35.8% | +21.2529 to +26.5940 | yes: power given |
| response time (ms), mean | 464.7 | 619.3 | +33.3% | +59.2625 to +249.9818 | yes: LOSS |
| response time (ms), 95th percentile | 1074 | 1480 | +37.9% | +158.4206 to +654.7994 | yes: LOSS |
| response time (ms), 99th percentile | 2533 | 5842 | +130.6% | +50.6328 to +6567.1926 | yes: LOSS |
| time over the response line (% of samples) | 46.34 | 45.1 | −2.7% | −14.3359 to +11.8374 | no |
| failed requests (%) | 33.74 | 28.83 | −14.6% | −15.8804 to +6.0515 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.667 | 10 | +3.4% | −1.1010 to +1.7677 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.67 | +19.667 (native is 0) | +18.2323 to +21.1010 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.333 | 21.67 | +828.6% | +9.2930 to +29.3737 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 2.933 | 39.82 | +1257.4% | +6.3073 to +67.4594 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.889 | 47.18 | +584.9% | +19.6770 to +60.9119 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5294 | 0.5292 | −0.0% | −0.0585 to +0.0581 | no |
| CPU used (cores), mean | 2.871 | 3.7 | +28.8% | +0.4615 to +1.1952 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0145 | +0.014 (native is 0) | +0.0076 to +0.0214 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.871 | 3.714 | +29.4% | +0.4699 to +1.2158 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 135.7 | 145.9 | +7.5% | −1.9268 to +22.3416 | no |
| HPA replicas, mean | 9.634 | 20.66 | +114.5% | +8.4232 to +13.6346 | yes: power given |
| pods started | 1.667 | 26.33 | +1480.0% | +13.4642 to +35.8692 | yes: power given |
| pod start wait, total (s) | 38 | 2555 | +6623.7% | +589.9669 to +4444.0331 | yes: LOSS |
| pod start wait, mean (s) | 7.6 | 95.33 | +1154.4% | +66.8438 to +108.6194 | yes: LOSS |
| machines billed, machine-hours | 0.3709 | 0.5641 | +52.1% | +0.0839 to +0.3024 | yes: power given |
| compute bill at list price ($) | 0.03561 | 0.05415 | +52.1% | +0.0081 to +0.0290 | yes: power given |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*