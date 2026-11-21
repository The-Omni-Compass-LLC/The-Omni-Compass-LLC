# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 479.3 | 478.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 479.3 | 478.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 248.4 | 123.5 |
| response time (ms), 95th percentile | 633.8 | 242.9 |
| response time (ms), 99th percentile | 1234 | 590.2 |
| time over the response line (% of samples) | 10.76 | 2.515 |
| failed requests (%) | 0.961 | 0.8431 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.7 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6317 | 1.057 |
| utilisation (used / allocatable) | 0.07549 | 0.07298 |
| CPU used (cores), mean | 1.812 | 1.752 |
| Omni's own CPU (cores), mean | 0 | 0.00863 |
| CPU used with Omni's own (cores), mean | 1.812 | 1.76 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.5 | 413 |
| HPA replicas, mean | 9.669 | 10.46 |
| pods started | 5.9 | 14 |
| pod start wait, total (s) | 21.6 | 34.3 |
| pod start wait, mean (s) | 3.318 | 2.502 |
| host CPU busy, the real machine under kind (%) | 52.03 | 50.97 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.679e-16 to +1.146e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.338 | +0.1% | -2.714e-05 to +0.008694 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 479.3 | 478.1 | -0.2% | -1.892 to -0.4444 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 479.3 | 478.1 | -0.2% | -1.892 to -0.4444 | yes: GAIN |
| response time (ms), mean | 248.4 | 123.5 | -50.3% | -167.4 to -82.37 | yes: GAIN |
| response time (ms), 95th percentile | 633.8 | 242.9 | -61.7% | -507.1 to -274.6 | yes: GAIN |
| response time (ms), 99th percentile | 1234 | 590.2 | -52.2% | -847.9 to -439.2 | yes: GAIN |
| time over the response line (% of samples) | 10.76 | 2.515 | -76.6% | -12.44 to -4.049 | yes: GAIN |
| failed requests (%) | 0.961 | 0.8431 | -12.3% | -0.2488 to +0.01297 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.7 | 7.1 | -65.7% | -19.44 to -7.758 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.9 | +53.9 (native is 0) | +38.23 to +69.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6317 | 1.057 | +67.3% | -0.2695 to +1.12 | no |
| utilisation (used / allocatable) | 0.07549 | 0.07298 | -3.3% | -0.003421 to -0.001607 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.812 | 1.752 | -3.3% | -0.08211 to -0.03856 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00863 | +0.00863 (native is 0) | +0.006906 to +0.01035 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.812 | 1.76 | -2.9% | -0.07231 to -0.03111 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.5 | 413 | +2.6% | +7.138 to +13.82 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.669 | 10.46 | +8.2% | -0.4625 to +2.049 | no |
| pods started | 5.9 | 14 | +137.3% | +4.338 to +11.86 | yes: power given |
| pod start wait, total (s) | 21.6 | 34.3 | +58.8% | +6.293 to +19.11 | yes: LOSS |
| pod start wait, mean (s) | 3.318 | 2.502 | -24.6% | -1.613 to -0.01785 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 52.03 | 50.97 | -2.0% | -1.573 to -0.5462 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*