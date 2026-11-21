# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.936 |
| node-hours | 2.516 | 2.067 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 238.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 487.9 | 436.4 |
| response time (ms), 95th percentile | 2984 | 3012 |
| response time (ms), 99th percentile | 4449 | 4539 |
| time over the response line (% of samples) | 15.2 | 14.39 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 182.6 | 180.7 |
| utilisation (used / allocatable) | 0.06 | 0.07311 |
| CPU used (cores), mean | 1.44 | 1.436 |
| Omni's own CPU (cores), mean | 0 | 0.02269 |
| CPU used with Omni's own (cores), mean | 1.44 | 1.459 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.8 | 401.8 |
| HPA replicas, mean | 1.986 | 2.185 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 3.4 | 3.2 |
| pod start wait, mean (s) | 3.4 | 3.2 |
| host CPU busy, the real machine under kind (%) | 41.4 | 41.94 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 561.1 | 561.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.336 |

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
| worker nodes in service, mean | 6 | 4.936 | -17.7% | -1.566 to -0.5626 | yes: GAIN |
| node-hours | 2.516 | 2.067 | -17.9% | -0.6608 to -0.2382 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.3 | -0.1% | -1.182 to +0.4685 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 238.9 | -12.4% | -49.36 to -18.13 | yes: GAIN |
| response time (ms), mean | 487.9 | 436.4 | -10.5% | -68.36 to -34.51 | yes: GAIN |
| response time (ms), 95th percentile | 2984 | 3012 | +0.9% | -142.3 to +198.6 | no |
| response time (ms), 99th percentile | 4449 | 4539 | +2.0% | -105.1 to +286.2 | no |
| time over the response line (% of samples) | 15.2 | 14.39 | -5.3% | -1.402 to -0.2189 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +10.8 to +12.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 182.6 | 180.7 | -1.0% | -8.975 to +5.221 | no |
| utilisation (used / allocatable) | 0.06 | 0.07311 | +21.9% | +0.006257 to +0.01998 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.44 | 1.436 | -0.2% | -0.0425 to +0.03554 | no |
| Omni's own CPU (cores), mean | 0 | 0.02269 | +0.0227 (native is 0) | +0.01875 to +0.02663 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.459 | +1.3% | -0.01985 to +0.05828 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.8 | 401.8 | -12.8% | -96.98 to -21.14 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.185 | +10.0% | -0.1356 to +0.5336 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 3.4 | 3.2 | -5.9% | -11.17 to +10.77 | no |
| pod start wait, mean (s) | 3.4 | 3.2 | -5.9% | -11.17 to +10.77 | no |
| host CPU busy, the real machine under kind (%) | 41.4 | 41.94 | +1.3% | +0.1213 to +0.9531 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 561.1 | 561.6 | +0.1% | -8.151 to +9.151 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.336 | -27.7% | -2.371 to -0.9569 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*