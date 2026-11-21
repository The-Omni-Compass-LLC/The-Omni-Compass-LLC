# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 507.8 | 506.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.8 | 506.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 234.4 | 136.7 |
| response time (ms), 95th percentile | 619.6 | 291.1 |
| response time (ms), 99th percentile | 2248 | 1538 |
| time over the response line (% of samples) | 14.52 | 8.97 |
| failed requests (%) | 8.125 | 7.022 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.8 | 15.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.52 | 0.7167 |
| utilisation (used / allocatable) | 0.08845 | 0.08613 |
| CPU used (cores), mean | 2.123 | 2.067 |
| Omni's own CPU (cores), mean | 0 | 0.00802 |
| CPU used with Omni's own (cores), mean | 2.123 | 2.075 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 361.6 | 374 |
| HPA replicas, mean | 9.473 | 9.323 |
| pods started | 5 | 5.7 |
| pod start wait, total (s) | 24.1 | 23.6 |
| pod start wait, mean (s) | 3.928 | 3.572 |
| host CPU busy, the real machine under kind (%) | 60.17 | 58.88 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.146e-15 to +9.679e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.512 | -0.0% | -0.00527 to +0.004936 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 507.8 | 506.3 | -0.3% | -2.491 to -0.51 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.8 | 506.3 | -0.3% | -2.491 to -0.51 | yes: GAIN |
| response time (ms), mean | 234.4 | 136.7 | -41.7% | -135.3 to -60.16 | yes: GAIN |
| response time (ms), 95th percentile | 619.6 | 291.1 | -53.0% | -433.8 to -223.2 | yes: GAIN |
| response time (ms), 99th percentile | 2248 | 1538 | -31.6% | -1124 to -294.8 | yes: GAIN |
| time over the response line (% of samples) | 14.52 | 8.97 | -38.2% | -8.872 to -2.221 | yes: GAIN |
| failed requests (%) | 8.125 | 7.022 | -13.6% | -1.972 to -0.2344 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.8 | 15.3 | -26.4% | -6.859 to -4.141 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +24.74 to +43.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.52 | 0.7167 | +37.8% | -0.1676 to +0.5609 | no |
| utilisation (used / allocatable) | 0.08845 | 0.08613 | -2.6% | -0.003296 to -0.001346 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.123 | 2.067 | -2.6% | -0.07911 to -0.03231 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00802 | +0.00802 (native is 0) | +0.006251 to +0.009789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.123 | 2.075 | -2.2% | -0.07141 to -0.02397 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 361.6 | 374 | +3.4% | +2.541 to +22.16 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.473 | 9.323 | -1.6% | -0.5508 to +0.2497 | no |
| pods started | 5 | 5.7 | +14.0% | -0.5639 to +1.964 | no |
| pod start wait, total (s) | 24.1 | 23.6 | -2.1% | -5.705 to +4.705 | no |
| pod start wait, mean (s) | 3.928 | 3.572 | -9.1% | -1.13 to +0.418 | no |
| host CPU busy, the real machine under kind (%) | 60.17 | 58.88 | -2.1% | -2 to -0.5849 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*