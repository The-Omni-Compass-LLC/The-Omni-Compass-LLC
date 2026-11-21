# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.2 | 170.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.2 | 170.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 470.3 | 377.7 |
| response time (ms), 95th percentile | 1901 | 1753 |
| response time (ms), 99th percentile | 5237 | 4305 |
| time over the response line (% of samples) | 20.07 | 17.88 |
| failed requests (%) | 3.546 | 3.397 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.253 | 1.063 |
| utilisation (used / allocatable) | 0.09149 | 0.09036 |
| CPU used (cores), mean | 2.196 | 2.169 |
| Omni's own CPU (cores), mean | 0 | 0.0102 |
| CPU used with Omni's own (cores), mean | 2.196 | 2.179 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.9 | 329.4 |
| HPA replicas, mean | 14.75 | 14.82 |
| pods started | 5.3 | 4.5 |
| pod start wait, total (s) | 13.7 | 11.9 |
| pod start wait, mean (s) | 2.319 | 2.24 |
| host CPU busy, the real machine under kind (%) | 63.54 | 63.09 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 326.1 | 331.2 |
| second app: response time (ms), 99th percentile | 1311 | 1242 |
| second app: time over the response line (% of samples) | 12.94 | 12.82 |
| second app: failed requests (%) | 10.94 | 10.86 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.514 | -0.1% | -0.007022 to +0.005355 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.2 | 170.9 | -0.2% | -1.07 to +0.5505 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.2 | 170.9 | -0.2% | -1.07 to +0.5505 | no |
| response time (ms), mean | 470.3 | 377.7 | -19.7% | -154.2 to -31 | yes: GAIN |
| response time (ms), 95th percentile | 1901 | 1753 | -7.8% | -453.7 to +158.2 | no |
| response time (ms), 99th percentile | 5237 | 4305 | -17.8% | -1601 to -262.7 | yes: GAIN |
| time over the response line (% of samples) | 20.07 | 17.88 | -10.9% | -4.352 to -0.03286 | yes: GAIN |
| failed requests (%) | 3.546 | 3.397 | -4.2% | -0.8046 to +0.506 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.8 | -2.9% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 | +33.4 (native is 0) | +31.96 to +34.84 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.253 | 1.063 | -15.2% | -1.037 to +0.6573 | no |
| utilisation (used / allocatable) | 0.09149 | 0.09036 | -1.2% | -0.00211 to -0.0001439 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.196 | 2.169 | -1.2% | -0.05065 to -0.003455 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0102 | +0.0102 (native is 0) | +0.008477 to +0.01192 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.196 | 2.179 | -0.8% | -0.04077 to +0.007066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.9 | 329.4 | +1.4% | -0.5804 to +9.474 | no |
| HPA replicas, mean | 14.75 | 14.82 | +0.5% | -0.2151 to +0.3654 | no |
| pods started | 5.3 | 4.5 | -15.1% | -2.3 to +0.7004 | no |
| pod start wait, total (s) | 13.7 | 11.9 | -13.1% | -5.252 to +1.652 | no |
| pod start wait, mean (s) | 2.319 | 2.24 | -3.4% | -0.4841 to +0.3279 | no |
| host CPU busy, the real machine under kind (%) | 63.54 | 63.09 | -0.7% | -1.143 to +0.2439 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 326.1 | 331.2 | +1.6% | -45.27 to +55.65 | no |
| second app: response time (ms), 99th percentile | 1311 | 1242 | -5.3% | -995.3 to +856.7 | no |
| second app: time over the response line (% of samples) | 12.94 | 12.82 | -1.0% | -0.7444 to +0.4959 | no |
| second app: failed requests (%) | 10.94 | 10.86 | -0.7% | -0.4037 to +0.2411 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*