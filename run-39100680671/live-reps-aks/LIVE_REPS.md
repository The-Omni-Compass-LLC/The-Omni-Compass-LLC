# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.844 | 1.809 |
| node-hours | 0.4662 | 0.4562 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.92 | 85.15 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.96 | 81.54 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 492.4 | 486.8 |
| response time (ms), 95th percentile | 1083 | 1025 |
| response time (ms), 99th percentile | 4604 | 4085 |
| time over the response line (% of samples) | 27.81 | 27.25 |
| failed requests (%) | 4.38 | 4.507 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 4.286 |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 |
| time pods had no machine to take them, pod-minutes | 10.61 | 10.49 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.843 | 5.01 |
| utilisation (used / allocatable) | 0.4776 | 0.4924 |
| CPU used (cores), mean | 1.668 | 1.692 |
| Omni's own CPU (cores), mean | 0 | 0.0044 |
| CPU used with Omni's own (cores), mean | 1.668 | 1.696 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 197 | 191.2 |
| HPA replicas, mean | 9.307 | 9.336 |
| pods started | 6 | 4.4 |
| pod start wait, total (s) | 671 | 659.6 |
| pod start wait, mean (s) | 128.6 | 141.6 |
| machines billed, machine-hours | 0.6096 | 0.5799 |
| compute bill at list price ($) | 0.05852 | 0.05567 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.844 | 1.809 | -1.9% | -0.1524 to +0.08339 | no |
| node-hours | 0.4662 | 0.4562 | -2.1% | -0.03821 to +0.01821 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.92 | 85.15 | -0.9% | -2.277 to +0.7295 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.96 | 81.54 | -1.7% | -3.773 to +0.9415 | no |
| response time (ms), mean | 492.4 | 486.8 | -1.1% | -95.71 to +84.51 | no |
| response time (ms), 95th percentile | 1083 | 1025 | -5.3% | -182.9 to +67.2 | no |
| response time (ms), 99th percentile | 4604 | 4085 | -11.3% | -5624 to +4585 | no |
| time over the response line (% of samples) | 27.81 | 27.25 | -2.0% | -5.731 to +4.62 | no |
| failed requests (%) | 4.38 | 4.507 | +2.9% | -3.272 to +3.526 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 | +7.5% | -0.7557 to +2.756 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.4 | +26.4 (native is 0) | +23.68 to +29.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 | +8.3% | -1.16 to +1.56 | no |
| time pods had no machine to take them, pod-minutes | 10.61 | 10.49 | -1.1% | -33.5 to +33.26 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.843 | 5.01 | +3.4% | -2.013 to +2.346 | no |
| utilisation (used / allocatable) | 0.4776 | 0.4924 | +3.1% | -0.03671 to +0.06629 | no |
| CPU used (cores), mean | 1.668 | 1.692 | +1.4% | -0.0735 to +0.1204 | no |
| Omni's own CPU (cores), mean | 0 | 0.0044 | +0.0044 (native is 0) | +0.003249 to +0.005551 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.668 | 1.696 | +1.7% | -0.06863 to +0.1243 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 197 | 191.2 | -3.0% | -23.07 to +11.38 | no |
| HPA replicas, mean | 9.307 | 9.336 | +0.3% | -0.3693 to +0.4292 | no |
| pods started | 6 | 4.4 | -26.7% | -4.32 to +1.12 | no |
| pod start wait, total (s) | 671 | 659.6 | -1.7% | -1980 to +1957 | no |
| pod start wait, mean (s) | 128.6 | 141.6 | +10.2% | -382.9 to +409 | no |
| machines billed, machine-hours | 0.6096 | 0.5799 | -4.9% | -0.1259 to +0.06643 | no |
| compute bill at list price ($) | 0.05852 | 0.05567 | -4.9% | -0.01208 to +0.006377 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*