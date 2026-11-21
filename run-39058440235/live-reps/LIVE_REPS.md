# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 159.1 | 80.42 |
| response time (ms), 95th percentile | 369.3 | 121.9 |
| response time (ms), 99th percentile | 577.2 | 169.6 |
| time over the response line (% of samples) | 2.716 | 0.02424 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3433 | 0.375 |
| utilisation (used / allocatable) | 0.0393 | 0.03729 |
| CPU used (cores), mean | 0.9431 | 0.8949 |
| Omni's own CPU (cores), mean | 0 | 0.00819 |
| CPU used with Omni's own (cores), mean | 0.9431 | 0.9031 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 708 | 739.6 |
| HPA replicas, mean | 8.543 | 8.337 |
| pods started | 4.9 | 4 |
| pod start wait, total (s) | 19.4 | 14.3 |
| pod start wait, mean (s) | 3.622 | 2.97 |
| host CPU busy, the real machine under kind (%) | 28.41 | 27.51 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.718e-16 to +4.495e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.511 | -0.2% | -0.0109 to +0.003902 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.5 | -0.5% | -1.666 to +0.02476 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.5 | -0.5% | -1.666 to +0.02476 | no |
| response time (ms), mean | 159.1 | 80.42 | -49.5% | -103.9 to -53.49 | yes: GAIN |
| response time (ms), 95th percentile | 369.3 | 121.9 | -67.0% | -323 to -171.8 | yes: GAIN |
| response time (ms), 99th percentile | 577.2 | 169.6 | -70.6% | -542 to -273.2 | yes: GAIN |
| time over the response line (% of samples) | 2.716 | 0.02424 | -99.1% | -4.238 to -1.145 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | -100.0% | -4.259 to -0.9412 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | +18.1 (native is 0) | +16.18 to +20.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3433 | 0.375 | +9.2% | -0.3064 to +0.3698 | no |
| utilisation (used / allocatable) | 0.0393 | 0.03729 | -5.1% | -0.002978 to -0.001039 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9431 | 0.8949 | -5.1% | -0.07148 to -0.02492 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00819 | +0.00819 (native is 0) | +0.006937 to +0.009443 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9431 | 0.9031 | -4.2% | -0.06237 to -0.01766 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 708 | 739.6 | +4.5% | +21.17 to +42.14 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.543 | 8.337 | -2.4% | -0.5463 to +0.1351 | no |
| pods started | 4.9 | 4 | -18.4% | -2.182 to +0.3818 | no |
| pod start wait, total (s) | 19.4 | 14.3 | -26.3% | -11.81 to +1.606 | no |
| pod start wait, mean (s) | 3.622 | 2.97 | -18.0% | -1.578 to +0.2747 | no |
| host CPU busy, the real machine under kind (%) | 28.41 | 27.51 | -3.2% | -1.319 to -0.4741 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*