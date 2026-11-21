# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.7 | 170.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.7 | 170.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 404.6 | 380.3 |
| response time (ms), 95th percentile | 1666 | 1946 |
| response time (ms), 99th percentile | 3998 | 4257 |
| time over the response line (% of samples) | 19.51 | 17.38 |
| failed requests (%) | 3.631 | 3.037 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.95 | 0.8167 |
| utilisation (used / allocatable) | 0.09028 | 0.08877 |
| CPU used (cores), mean | 2.167 | 2.13 |
| Omni's own CPU (cores), mean | 0 | 0.00995 |
| CPU used with Omni's own (cores), mean | 2.167 | 2.14 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327.1 | 335.9 |
| HPA replicas, mean | 14.76 | 14.88 |
| pods started | 5.4 | 4.3 |
| pod start wait, total (s) | 14.8 | 13.4 |
| pod start wait, mean (s) | 2.518 | 2.426 |
| host CPU busy, the real machine under kind (%) | 62.31 | 62.07 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 293.7 | 284.3 |
| second app: response time (ms), 99th percentile | 1966 | 1588 |
| second app: time over the response line (% of samples) | 12.1 | 11.98 |
| second app: failed requests (%) | 10.42 | 10.24 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.514 | +0.1% | -0.003933 to +0.006599 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170.7 | 170.6 | -0.1% | -0.6709 to +0.4651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.7 | 170.6 | -0.1% | -0.6709 to +0.4651 | no |
| response time (ms), mean | 404.6 | 380.3 | -6.0% | -55.8 to +7.258 | no |
| response time (ms), 95th percentile | 1666 | 1946 | +16.8% | +42.66 to +517.4 | yes: LOSS |
| response time (ms), 99th percentile | 3998 | 4257 | +6.5% | -449.1 to +966.3 | no |
| time over the response line (% of samples) | 19.51 | 17.38 | -10.9% | -4.338 to +0.08707 | no |
| failed requests (%) | 3.631 | 3.037 | -16.4% | -1.391 to +0.2024 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.6 | -7.0% | -1.108 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.9 | +31.9 (native is 0) | +30.38 to +33.42 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.95 | 0.8167 | -14.0% | -0.5418 to +0.2751 | no |
| utilisation (used / allocatable) | 0.09028 | 0.08877 | -1.7% | -0.003017 to -1.814e-06 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.167 | 2.13 | -1.7% | -0.07241 to -4.355e-05 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00995 | +0.00995 (native is 0) | +0.008267 to +0.01163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.167 | 2.14 | -1.2% | -0.06369 to +0.01114 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327.1 | 335.9 | +2.7% | +0.3562 to +17.22 | yes, up (shown, not judged) |
| HPA replicas, mean | 14.76 | 14.88 | +0.8% | -0.2068 to +0.449 | no |
| pods started | 5.4 | 4.3 | -20.4% | -2.29 to +0.08979 | no |
| pod start wait, total (s) | 14.8 | 13.4 | -9.5% | -5.477 to +2.677 | no |
| pod start wait, mean (s) | 2.518 | 2.426 | -3.6% | -0.581 to +0.3972 | no |
| host CPU busy, the real machine under kind (%) | 62.31 | 62.07 | -0.4% | -0.7961 to +0.3052 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 293.7 | 284.3 | -3.2% | -27.84 to +9.112 | no |
| second app: response time (ms), 99th percentile | 1966 | 1588 | -19.2% | -1382 to +625.6 | no |
| second app: time over the response line (% of samples) | 12.1 | 11.98 | -1.0% | -0.5326 to +0.2967 | no |
| second app: failed requests (%) | 10.42 | 10.24 | -1.7% | -0.449 to +0.0959 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*