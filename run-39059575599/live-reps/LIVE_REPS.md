# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 514 | 512.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514 | 512.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 290.5 | 151.2 |
| response time (ms), 95th percentile | 816.6 | 328.4 |
| response time (ms), 99th percentile | 2846 | 1481 |
| time over the response line (% of samples) | 15.93 | 8.624 |
| failed requests (%) | 6.716 | 5.99 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.8 | 17.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5417 | 0.5767 |
| utilisation (used / allocatable) | 0.0974 | 0.09557 |
| CPU used (cores), mean | 2.338 | 2.294 |
| Omni's own CPU (cores), mean | 0 | 0.00848 |
| CPU used with Omni's own (cores), mean | 2.338 | 2.302 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 308.6 |
| HPA replicas, mean | 9.462 | 9.588 |
| pods started | 5.5 | 6.9 |
| pod start wait, total (s) | 21.6 | 22.6 |
| pod start wait, mean (s) | 3.807 | 3.164 |
| host CPU busy, the real machine under kind (%) | 65.76 | 64.97 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.066e-15 to +7.108e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.51 | -0.1% | -0.009635 to +0.003301 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 514 | 512.4 | -0.3% | -2.482 to -0.6192 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514 | 512.4 | -0.3% | -2.482 to -0.6192 | yes: GAIN |
| response time (ms), mean | 290.5 | 151.2 | -47.9% | -170 to -108.5 | yes: GAIN |
| response time (ms), 95th percentile | 816.6 | 328.4 | -59.8% | -611.5 to -365.1 | yes: GAIN |
| response time (ms), 99th percentile | 2846 | 1481 | -48.0% | -2062 to -669.3 | yes: GAIN |
| time over the response line (% of samples) | 15.93 | 8.624 | -45.9% | -9.439 to -5.182 | yes: GAIN |
| failed requests (%) | 6.716 | 5.99 | -10.8% | -1.208 to -0.2451 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.8 | 17.9 | -30.6% | -9.425 to -6.375 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 | +40.7 (native is 0) | +31.69 to +49.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5417 | 0.5767 | +6.5% | -0.4574 to +0.5274 | no |
| utilisation (used / allocatable) | 0.0974 | 0.09557 | -1.9% | -0.002593 to -0.001065 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.338 | 2.294 | -1.9% | -0.06224 to -0.02557 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00848 | +0.00848 (native is 0) | +0.007598 to +0.009362 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.338 | 2.302 | -1.5% | -0.05337 to -0.01748 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 308.6 | +1.6% | +1.709 to +7.72 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.462 | 9.588 | +1.3% | -0.2114 to +0.4643 | no |
| pods started | 5.5 | 6.9 | +25.5% | -0.6006 to +3.401 | no |
| pod start wait, total (s) | 21.6 | 22.6 | +4.6% | -7.504 to +9.504 | no |
| pod start wait, mean (s) | 3.807 | 3.164 | -16.9% | -1.582 to +0.296 | no |
| host CPU busy, the real machine under kind (%) | 65.76 | 64.97 | -1.2% | -1.427 to -0.1574 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 20.4 |  |  | 10 |
| compass | 31.8 | +55.9% | +9.0 to +13.8 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*