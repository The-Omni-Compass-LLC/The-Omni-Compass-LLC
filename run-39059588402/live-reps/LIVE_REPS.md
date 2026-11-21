# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.816 |
| node-hours | 2.519 | 2.018 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 234.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 447.3 | 401.3 |
| response time (ms), 95th percentile | 2728 | 2716 |
| response time (ms), 99th percentile | 4230 | 4148 |
| time over the response line (% of samples) | 14.6 | 14.38 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174.6 | 175.5 |
| utilisation (used / allocatable) | 0.05772 | 0.07166 |
| CPU used (cores), mean | 1.385 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0.01893 |
| CPU used with Omni's own (cores), mean | 1.385 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.2 | 408.8 |
| HPA replicas, mean | 2.102 | 2.253 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 5.4 | 4.4 |
| pod start wait, mean (s) | 5.4 | 4.4 |
| host CPU busy, the real machine under kind (%) | 39.56 | 40.36 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 537.7 | 542.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.233 |

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
| worker nodes in service, mean | 6 | 4.816 | -19.7% | -1.765 to -0.6025 | yes: GAIN |
| node-hours | 2.519 | 2.018 | -19.9% | -0.7415 to -0.2591 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | -0.0% | -1.055 to +0.7861 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 234.6 | -13.7% | -55.54 to -19.23 | yes: GAIN |
| response time (ms), mean | 447.3 | 401.3 | -10.3% | -61.22 to -30.72 | yes: GAIN |
| response time (ms), 95th percentile | 2728 | 2716 | -0.4% | -107.2 to +83.43 | no |
| response time (ms), 99th percentile | 4230 | 4148 | -2.0% | -272.8 to +107 | no |
| time over the response line (% of samples) | 14.6 | 14.38 | -1.5% | -0.5794 to +0.1361 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.9 (native is 0) | +10.62 to +13.18 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174.6 | 175.5 | +0.5% | -4.251 to +6.101 | no |
| utilisation (used / allocatable) | 0.05772 | 0.07166 | +24.2% | +0.007124 to +0.02076 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.378 | -0.5% | -0.04383 to +0.02927 | no |
| Omni's own CPU (cores), mean | 0 | 0.01893 | +0.0189 (native is 0) | +0.01566 to +0.0222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.397 | +0.8% | -0.02602 to +0.04933 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.2 | 408.8 | -14.2% | -103.7 to -31.14 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.102 | 2.253 | +7.2% | -0.08275 to +0.3853 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 5.4 | 4.4 | -18.5% | -17.3 to +15.3 | no |
| pod start wait, mean (s) | 5.4 | 4.4 | -18.5% | -17.3 to +15.3 | no |
| host CPU busy, the real machine under kind (%) | 39.56 | 40.36 | +2.0% | +0.1604 to +1.438 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 537.7 | 542.3 | +0.9% | -4.207 to +13.41 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.233 | -29.5% | -2.59 to -0.945 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*