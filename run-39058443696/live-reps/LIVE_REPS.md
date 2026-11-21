# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 511.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 511.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 260.3 | 140.3 |
| response time (ms), 95th percentile | 691.6 | 269.6 |
| response time (ms), 99th percentile | 2504 | 1498 |
| time over the response line (% of samples) | 15.86 | 9.514 |
| failed requests (%) | 8.644 | 7.512 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 18.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.5567 |
| utilisation (used / allocatable) | 0.09557 | 0.09252 |
| CPU used (cores), mean | 2.294 | 2.221 |
| Omni's own CPU (cores), mean | 0 | 0.0083 |
| CPU used with Omni's own (cores), mean | 2.294 | 2.229 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 325.8 | 339.5 |
| HPA replicas, mean | 9.573 | 9.739 |
| pods started | 4.8 | 6.6 |
| pod start wait, total (s) | 18 | 20.3 |
| pod start wait, mean (s) | 3.189 | 2.897 |
| host CPU busy, the real machine under kind (%) | 64.48 | 62.95 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.471e-16 to +9.471e-16 | no |
| node-hours | 4.515 | 4.519 | +0.1% | -0.002189 to +0.01152 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 511.4 | -0.3% | -2.76 to -0.1964 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 511.4 | -0.3% | -2.76 to -0.1964 | yes: GAIN |
| response time (ms), mean | 260.3 | 140.3 | -46.1% | -154.9 to -85.04 | yes: GAIN |
| response time (ms), 95th percentile | 691.6 | 269.6 | -61.0% | -524.7 to -319.3 | yes: GAIN |
| response time (ms), 99th percentile | 2504 | 1498 | -40.2% | -1632 to -381.3 | yes: GAIN |
| time over the response line (% of samples) | 15.86 | 9.514 | -40.0% | -8.876 to -3.822 | yes: GAIN |
| failed requests (%) | 8.644 | 7.512 | -13.1% | -1.819 to -0.4453 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 18.1 | -27.0% | -9.202 to -4.198 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 | +42.3 (native is 0) | +29.03 to +55.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.5567 | +10.2% | -0.3334 to +0.4367 | no |
| utilisation (used / allocatable) | 0.09557 | 0.09252 | -3.2% | -0.004242 to -0.001862 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.294 | 2.221 | -3.2% | -0.1018 to -0.0447 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0083 | +0.0083 (native is 0) | +0.006904 to +0.009696 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.294 | 2.229 | -2.8% | -0.09416 to -0.03575 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 325.8 | 339.5 | +4.2% | +1.08 to +26.43 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.573 | 9.739 | +1.7% | -0.6617 to +0.9936 | no |
| pods started | 4.8 | 6.6 | +37.5% | -0.5796 to +4.18 | no |
| pod start wait, total (s) | 18 | 20.3 | +12.8% | -4.838 to +9.438 | no |
| pod start wait, mean (s) | 3.189 | 2.897 | -9.1% | -1.496 to +0.9125 | no |
| host CPU busy, the real machine under kind (%) | 64.48 | 62.95 | -2.4% | -2.341 to -0.7104 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*