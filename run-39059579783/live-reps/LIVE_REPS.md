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
| energy, parked workers still on at idle power (Wh, declared model) | 171.4 | 171.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.4 | 171.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 455.9 | 412 |
| response time (ms), 95th percentile | 1800 | 1929 |
| response time (ms), 99th percentile | 4639 | 4709 |
| time over the response line (% of samples) | 21.03 | 19.44 |
| failed requests (%) | 2.599 | 2.602 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.56 | 1.237 |
| utilisation (used / allocatable) | 0.09254 | 0.09252 |
| CPU used (cores), mean | 2.221 | 2.22 |
| Omni's own CPU (cores), mean | 0 | 0.01075 |
| CPU used with Omni's own (cores), mean | 2.221 | 2.231 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.2 | 314.7 |
| HPA replicas, mean | 14.93 | 15.03 |
| pods started | 4.8 | 4.6 |
| pod start wait, total (s) | 10.8 | 10.6 |
| pod start wait, mean (s) | 1.977 | 2.04 |
| host CPU busy, the real machine under kind (%) | 64 | 64.57 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 278.1 | 271.5 |
| second app: response time (ms), 99th percentile | 2279 | 2283 |
| second app: time over the response line (% of samples) | 12.96 | 13.34 |
| second app: failed requests (%) | 10.82 | 11.03 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.235e-16 to +6.788e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.514 | -0.1% | -0.008415 to +0.005749 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.4 | 171.3 | -0.1% | -0.9161 to +0.6899 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.4 | 171.3 | -0.1% | -0.9161 to +0.6899 | no |
| response time (ms), mean | 455.9 | 412 | -9.6% | -81.03 to -6.797 | yes: GAIN |
| response time (ms), 95th percentile | 1800 | 1929 | +7.1% | -224.1 to +481.4 | no |
| response time (ms), 99th percentile | 4639 | 4709 | +1.5% | -606.2 to +747.2 | no |
| time over the response line (% of samples) | 21.03 | 19.44 | -7.6% | -2.818 to -0.3605 | yes: GAIN |
| failed requests (%) | 2.599 | 2.602 | +0.1% | -0.6288 to +0.6339 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.7 | +1.3% | -0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 | +33.7 (native is 0) | +31.2 to +36.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.56 | 1.237 | +120.8% | +0.1155 to +1.238 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09254 | 0.09252 | -0.0% | -0.001444 to +0.001407 | no |
| CPU used (cores), mean | 2.221 | 2.22 | -0.0% | -0.03466 to +0.03377 | no |
| Omni's own CPU (cores), mean | 0 | 0.01075 | +0.0107 (native is 0) | +0.009529 to +0.01197 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.221 | 2.231 | +0.5% | -0.02378 to +0.04439 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.2 | 314.7 | +0.2% | -4.04 to +5.032 | no |
| HPA replicas, mean | 14.93 | 15.03 | +0.7% | -0.1129 to +0.3149 | no |
| pods started | 4.8 | 4.6 | -4.2% | -0.8573 to +0.4573 | no |
| pod start wait, total (s) | 10.8 | 10.6 | -1.9% | -4.115 to +3.715 | no |
| pod start wait, mean (s) | 1.977 | 2.04 | +3.2% | -0.434 to +0.5616 | no |
| host CPU busy, the real machine under kind (%) | 64 | 64.57 | +0.9% | -0.0283 to +1.17 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 278.1 | 271.5 | -2.4% | -29 to +15.78 | no |
| second app: response time (ms), 99th percentile | 2279 | 2283 | +0.1% | -1368 to +1374 | no |
| second app: time over the response line (% of samples) | 12.96 | 13.34 | +3.0% | -0.2149 to +0.985 | no |
| second app: failed requests (%) | 10.82 | 11.03 | +2.0% | -0.2878 to +0.7143 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*