# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.9 | 514.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.9 | 514.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 271.5 | 151.3 |
| response time (ms), 95th percentile | 731.3 | 290.3 |
| response time (ms), 99th percentile | 2280 | 1475 |
| time over the response line (% of samples) | 18.19 | 10.78 |
| failed requests (%) | 9.886 | 8.626 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.5 | 19.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 20 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4817 | 0.3733 |
| utilisation (used / allocatable) | 0.1001 | 0.09751 |
| CPU used (cores), mean | 2.403 | 2.34 |
| Omni's own CPU (cores), mean | 0 | 0.0084 |
| CPU used with Omni's own (cores), mean | 2.403 | 2.349 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.2 | 315.2 |
| HPA replicas, mean | 9.465 | 9.312 |
| pods started | 4.8 | 5.6 |
| pod start wait, total (s) | 14.2 | 16.1 |
| pod start wait, mean (s) | 2.702 | 2.587 |
| host CPU busy, the real machine under kind (%) | 67.52 | 66.22 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.83e-16 to +1.216e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.515 | +0.0% | -0.009558 to +0.01023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.9 | 514.3 | -0.3% | -2.798 to -0.4213 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.9 | 514.3 | -0.3% | -2.798 to -0.4213 | yes: GAIN |
| response time (ms), mean | 271.5 | 151.3 | -44.3% | -145.6 to -94.81 | yes: GAIN |
| response time (ms), 95th percentile | 731.3 | 290.3 | -60.3% | -527.1 to -354.8 | yes: GAIN |
| response time (ms), 99th percentile | 2280 | 1475 | -35.3% | -1379 to -230.7 | yes: GAIN |
| time over the response line (% of samples) | 18.19 | 10.78 | -40.7% | -9.954 to -4.854 | yes: GAIN |
| failed requests (%) | 9.886 | 8.626 | -12.7% | -2.188 to -0.3308 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.5 | 19.9 | -24.9% | -7.915 to -5.285 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.3 (native is 0) | +24.98 to +39.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4817 | 0.3733 | -22.5% | -0.4652 to +0.2485 | no |
| utilisation (used / allocatable) | 0.1001 | 0.09751 | -2.6% | -0.003539 to -0.001696 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.403 | 2.34 | -2.6% | -0.08494 to -0.0407 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.0084 (native is 0) | +0.007202 to +0.009598 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.403 | 2.349 | -2.3% | -0.0772 to -0.03164 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.2 | 315.2 | +3.3% | +1.348 to +18.66 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.465 | 9.312 | -1.6% | -0.5447 to +0.2388 | no |
| pods started | 4.8 | 5.6 | +16.7% | -1.273 to +2.873 | no |
| pod start wait, total (s) | 14.2 | 16.1 | +13.4% | -6.175 to +9.975 | no |
| pod start wait, mean (s) | 2.702 | 2.587 | -4.3% | -0.855 to +0.6241 | no |
| host CPU busy, the real machine under kind (%) | 67.52 | 66.22 | -1.9% | -1.941 to -0.677 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 20.4 |  |  | 10 |
| compass | 30.0 | +47.1% | +7.4 to +11.8 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*