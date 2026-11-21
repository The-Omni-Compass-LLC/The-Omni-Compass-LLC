# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 521 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 521 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 303.7 | 172.8 |
| response time (ms), 95th percentile | 779.6 | 324.4 |
| response time (ms), 99th percentile | 2862 | 1994 |
| time over the response line (% of samples) | 22.36 | 14.18 |
| failed requests (%) | 13.52 | 11.63 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.4 | 25.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4317 | 0.6333 |
| utilisation (used / allocatable) | 0.1101 | 0.1075 |
| CPU used (cores), mean | 2.642 | 2.579 |
| Omni's own CPU (cores), mean | 0 | 0.00976 |
| CPU used with Omni's own (cores), mean | 2.642 | 2.589 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.5 | 285.2 |
| HPA replicas, mean | 9.717 | 9.967 |
| pods started | 4 | 5 |
| pod start wait, total (s) | 12.5 | 13.1 |
| pod start wait, mean (s) | 2.67 | 2.079 |
| host CPU busy, the real machine under kind (%) | 74.12 | 72.93 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.586e-16 to +6.033e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.515 | +0.0% | -0.004065 to +0.007398 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 521 | -0.3% | -2.217 to -0.6449 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 521 | -0.3% | -2.217 to -0.6449 | yes: GAIN |
| response time (ms), mean | 303.7 | 172.8 | -43.1% | -158.5 to -103.3 | yes: GAIN |
| response time (ms), 95th percentile | 779.6 | 324.4 | -58.4% | -540.3 to -370 | yes: GAIN |
| response time (ms), 99th percentile | 2862 | 1994 | -30.3% | -1601 to -135.6 | yes: GAIN |
| time over the response line (% of samples) | 22.36 | 14.18 | -36.6% | -10.4 to -5.971 | yes: GAIN |
| failed requests (%) | 13.52 | 11.63 | -13.9% | -2.726 to -1.042 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.4 | 25.1 | -22.5% | -9.38 to -5.22 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 | +44.3 (native is 0) | +37.76 to +50.84 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4317 | 0.6333 | +46.7% | -0.2676 to +0.671 | no |
| utilisation (used / allocatable) | 0.1101 | 0.1075 | -2.4% | -0.00361 to -0.001582 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.642 | 2.579 | -2.4% | -0.08664 to -0.03796 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00976 | +0.00976 (native is 0) | +0.008631 to +0.01089 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.642 | 2.589 | -2.0% | -0.07616 to -0.02891 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.5 | 285.2 | +2.0% | +3.9 to +7.435 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.717 | 9.967 | +2.6% | -0.1119 to +0.6123 | no |
| pods started | 4 | 5 | +25.0% | -1.023 to +3.023 | no |
| pod start wait, total (s) | 12.5 | 13.1 | +4.8% | -4.691 to +5.891 | no |
| pod start wait, mean (s) | 2.67 | 2.079 | -22.1% | -1.213 to +0.03105 | no |
| host CPU busy, the real machine under kind (%) | 74.12 | 72.93 | -1.6% | -1.703 to -0.6586 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*