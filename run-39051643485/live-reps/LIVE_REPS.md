# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 514.9 | 514 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.9 | 514 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 258.9 | 138.3 |
| response time (ms), 95th percentile | 677.3 | 269.4 |
| response time (ms), 99th percentile | 2027 | 1005 |
| time over the response line (% of samples) | 17.92 | 11.11 |
| failed requests (%) | 10.44 | 9.184 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.8 | 20.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5617 | 0.6367 |
| utilisation (used / allocatable) | 0.0991 | 0.09708 |
| CPU used (cores), mean | 2.378 | 2.33 |
| Omni's own CPU (cores), mean | 0 | 0.00875 |
| CPU used with Omni's own (cores), mean | 2.378 | 2.339 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.6 | 324.4 |
| HPA replicas, mean | 9.602 | 9.856 |
| pods started | 4.5 | 7.2 |
| pod start wait, total (s) | 15.5 | 22.4 |
| pod start wait, mean (s) | 2.843 | 2.862 |
| host CPU busy, the real machine under kind (%) | 66.91 | 66.02 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.25e-15 to +3.623e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.515 | +0.1% | -0.00578 to +0.01211 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 514.9 | 514 | -0.2% | -1.925 to +0.09445 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.9 | 514 | -0.2% | -1.925 to +0.09445 | no |
| response time (ms), mean | 258.9 | 138.3 | -46.6% | -156.1 to -85.03 | yes: GAIN |
| response time (ms), 95th percentile | 677.3 | 269.4 | -60.2% | -507.8 to -308 | yes: GAIN |
| response time (ms), 99th percentile | 2027 | 1005 | -50.4% | -1513 to -530.4 | yes: GAIN |
| time over the response line (% of samples) | 17.92 | 11.11 | -38.0% | -9.348 to -4.282 | yes: GAIN |
| failed requests (%) | 10.44 | 9.184 | -12.0% | -1.978 to -0.527 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.8 | 20.4 | -23.9% | -8.253 to -4.547 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 | +39.2 (native is 0) | +30.85 to +47.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5617 | 0.6367 | +13.4% | -0.2747 to +0.4247 | no |
| utilisation (used / allocatable) | 0.0991 | 0.09708 | -2.0% | -0.002841 to -0.001213 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.378 | 2.33 | -2.0% | -0.06818 to -0.02911 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00875 | +0.00875 (native is 0) | +0.007334 to +0.01017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.378 | 2.339 | -1.7% | -0.05882 to -0.02097 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.6 | 324.4 | +1.8% | +2.611 to +9.059 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.602 | 9.856 | +2.6% | -0.5387 to +1.046 | no |
| pods started | 4.5 | 7.2 | +60.0% | +0.221 to +5.179 | yes: power given |
| pod start wait, total (s) | 15.5 | 22.4 | +44.5% | -1.356 to +15.16 | no |
| pod start wait, mean (s) | 2.843 | 2.862 | +0.7% | -0.9913 to +1.03 | no |
| host CPU busy, the real machine under kind (%) | 66.91 | 66.02 | -1.3% | -1.321 to -0.4665 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*