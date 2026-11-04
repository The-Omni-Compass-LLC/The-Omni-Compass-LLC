# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.796 | 2.791 |
| node-hours | 0.7064 | 0.7045 |
| energy, parked workers still on at idle power (Wh, declared model) | 87.91 | 88.66 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.81 | 84.05 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 541.6 | 530.6 |
| response time (ms), 95th percentile | 1358 | 1331 |
| response time (ms), 99th percentile | 5374 | 5068 |
| time over the response line (% of samples) | 30.82 | 31.33 |
| failed requests (%) | 6.054 | 6.677 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.18 | 14.29 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.47 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 10.92 |
| pods with no machine to take them (unschedulable) | 2.855 | 2.849 |
| time pods had no machine to take them, pod-minutes | 4.409 | 4.469 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.643 | 7.527 |
| utilisation (used / allocatable) | 0.3793 | 0.3822 |
| CPU used (cores), mean | 2.014 | 2.025 |
| Omni's own CPU (cores), mean | 0 | 0.005538 |
| CPU used with Omni's own (cores), mean | 2.014 | 2.03 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 164.8 | 164.6 |
| HPA replicas, mean | 9.372 | 9.366 |
| pods started | 5.47 | 5.244 |
| pod start wait, total (s) | 310.9 | 309.5 |
| pod start wait, mean (s) | 57.85 | 59.8 |
| machines billed, machine-hours | 0.5878 | 0.5944 |
| compute bill at list price ($) | 0.05643 | 0.05706 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 73 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.797 | 2.792 | −0.2% | −0.0294 to +0.0191 | no |
| node-hours | 0.7065 | 0.7048 | −0.2% | −0.0078 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 87.92 | 88.19 | +0.3% | −0.7135 to +1.2484 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.82 | 83.99 | +0.2% | −0.4313 to +0.7779 | no |
| response time (ms), mean | 540.8 | 525.2 | −2.9% | −32.5452 to +1.4845 | no |
| response time (ms), 95th percentile | 1345 | 1319 | −1.9% | −119.2190 to +67.3742 | no |
| response time (ms), 99th percentile | 5373 | 4995 | −7.0% | −864.6296 to +107.4342 | no |
| time over the response line (% of samples) | 30.68 | 31.07 | +1.3% | −0.6902 to +1.4786 | no |
| failed requests (%) | 6.018 | 6.616 | +9.9% | −0.3399 to +1.5347 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.15 | 14.27 | +0.9% | −0.1224 to +0.3690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.3 | +25.301 (native is 0) | +24.4367 to +26.1661 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.863 | 2.849 | −0.5% | −0.2248 to +0.1974 | no |
| time pods had no machine to take them, pod-minutes | 4.411 | 4.525 | +2.6% | −0.2995 to +0.5282 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.613 | 7.596 | −0.2% | −0.5815 to +0.5482 | no |
| utilisation (used / allocatable) | 0.3793 | 0.3817 | +0.6% | −0.0034 to +0.0080 | no |
| CPU used (cores), mean | 2.015 | 2.023 | +0.4% | −0.0119 to +0.0282 | no |
| Omni's own CPU (cores), mean | 0 | 0.005547 | +0.006 (native is 0) | +0.0053 to +0.0058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.015 | 2.028 | +0.7% | −0.0064 to +0.0338 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 164.8 | 164.6 | −0.1% | −1.8301 to +1.3656 | no |
| HPA replicas, mean | 9.372 | 9.383 | +0.1% | −0.0465 to +0.0678 | no |
| pods started | 5.466 | 5.219 | −4.5% | −0.5666 to +0.0735 | no |
| pod start wait, total (s) | 311.1 | 312.5 | +0.4% | −27.4012 to +30.1957 | no |
| pod start wait, mean (s) | 57.73 | 60.24 | +4.4% | −2.9481 to +7.9749 | no |
| machines billed, machine-hours | 0.5878 | 0.5897 | +0.3% | −0.0091 to +0.0129 | no |
| compute bill at list price ($) | 0.05643 | 0.05662 | +0.3% | −0.0009 to +0.0012 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*