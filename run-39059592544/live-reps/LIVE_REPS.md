# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.3 | 158.6 |
| response time (ms), 95th percentile | 792.4 | 339.1 |
| response time (ms), 99th percentile | 1464 | 820 |
| time over the response line (% of samples) | 16.11 | 4.009 |
| failed requests (%) | 1.722 | 1.433 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.3 | 11.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7783 | 1.17 |
| utilisation (used / allocatable) | 0.08544 | 0.08251 |
| CPU used (cores), mean | 2.051 | 1.98 |
| Omni's own CPU (cores), mean | 0 | 0.01031 |
| CPU used with Omni's own (cores), mean | 2.051 | 1.991 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 353.2 | 363.8 |
| HPA replicas, mean | 9.793 | 11.66 |
| pods started | 5 | 16 |
| pod start wait, total (s) | 16.2 | 31.8 |
| pod start wait, mean (s) | 2.945 | 2.048 |
| host CPU busy, the real machine under kind (%) | 59.08 | 57.69 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.985e-16 to +8.985e-16 | no |
| node-hours | 4.334 | 4.337 | +0.1% | -0.006736 to +0.01307 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.2 | -0.3% | -2.914 to -0.2367 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.2 | -0.3% | -2.914 to -0.2367 | yes: GAIN |
| response time (ms), mean | 306.3 | 158.6 | -48.2% | -186 to -109.3 | yes: GAIN |
| response time (ms), 95th percentile | 792.4 | 339.1 | -57.2% | -558.3 to -348.5 | yes: GAIN |
| response time (ms), 99th percentile | 1464 | 820 | -44.0% | -858.4 to -430.5 | yes: GAIN |
| time over the response line (% of samples) | 16.11 | 4.009 | -75.1% | -16.18 to -8.017 | yes: GAIN |
| failed requests (%) | 1.722 | 1.433 | -16.7% | -0.4622 to -0.1142 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.3 | 11.3 | -58.6% | -20.87 to -11.13 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.7 | +66.7 (native is 0) | +51.1 to +82.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7783 | 1.17 | +50.3% | -0.2008 to +0.9841 | no |
| utilisation (used / allocatable) | 0.08544 | 0.08251 | -3.4% | -0.003647 to -0.00221 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.051 | 1.98 | -3.4% | -0.08752 to -0.05303 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01031 | +0.0103 (native is 0) | +0.008723 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.051 | 1.991 | -2.9% | -0.07589 to -0.04404 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 353.2 | 363.8 | +3.0% | +8.336 to +12.92 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.793 | 11.66 | +19.1% | +0.6118 to +3.125 | yes: power given |
| pods started | 5 | 16 | +220.0% | +6.578 to +15.42 | yes: power given |
| pod start wait, total (s) | 16.2 | 31.8 | +96.3% | +6.291 to +24.91 | yes: LOSS |
| pod start wait, mean (s) | 2.945 | 2.048 | -30.5% | -1.541 to -0.2532 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 59.08 | 57.69 | -2.3% | -1.603 to -1.171 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*