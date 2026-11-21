# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 140.7 | 75.06 |
| response time (ms), 95th percentile | 307 | 114.7 |
| response time (ms), 99th percentile | 511.7 | 165.3 |
| time over the response line (% of samples) | 1.909 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 0.3433 |
| utilisation (used / allocatable) | 0.03694 | 0.03474 |
| CPU used (cores), mean | 0.8865 | 0.8338 |
| Omni's own CPU (cores), mean | 0 | 0.00797 |
| CPU used with Omni's own (cores), mean | 0.8865 | 0.8418 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 764.9 | 803.1 |
| HPA replicas, mean | 8.421 | 8.054 |
| pods started | 4.7 | 3.4 |
| pod start wait, total (s) | 17.6 | 12.4 |
| pod start wait, mean (s) | 3.438 | 2.807 |
| host CPU busy, the real machine under kind (%) | 26.92 | 25.79 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | -0.004143 to +0.008476 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | -0.2% | -0.8953 to +0.343 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | -0.2% | -0.8953 to +0.343 | no |
| response time (ms), mean | 140.7 | 75.06 | -46.6% | -90.25 to -41 | yes: GAIN |
| response time (ms), 95th percentile | 307 | 114.7 | -62.6% | -257.9 to -126.8 | yes: GAIN |
| response time (ms), 99th percentile | 511.7 | 165.3 | -67.7% | -466.7 to -226.1 | yes: GAIN |
| time over the response line (% of samples) | 1.909 | 0.01212 | -99.4% | -3.029 to -0.7643 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 | -100.0% | -3.468 to -0.7324 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.5 (native is 0) | +15.56 to +19.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 0.3433 | -13.1% | -0.2026 to +0.09929 | no |
| utilisation (used / allocatable) | 0.03694 | 0.03474 | -6.0% | -0.0031 to -0.001296 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8865 | 0.8338 | -6.0% | -0.07441 to -0.03111 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00797 | +0.00797 (native is 0) | +0.006743 to +0.009197 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8865 | 0.8418 | -5.1% | -0.06542 to -0.02416 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 764.9 | 803.1 | +5.0% | +27.57 to +48.76 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.421 | 8.054 | -4.4% | -0.7919 to +0.05781 | no |
| pods started | 4.7 | 3.4 | -27.7% | -2.564 to -0.03607 | yes: GAIN |
| pod start wait, total (s) | 17.6 | 12.4 | -29.5% | -11.68 to +1.284 | no |
| pod start wait, mean (s) | 3.438 | 2.807 | -18.4% | -1.475 to +0.2115 | no |
| host CPU busy, the real machine under kind (%) | 26.92 | 25.79 | -4.2% | -1.759 to -0.5007 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*