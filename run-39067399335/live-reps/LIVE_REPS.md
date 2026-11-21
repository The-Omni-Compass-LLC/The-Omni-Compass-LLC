# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 170 | 170.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170 | 170.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 364.2 | 318.3 |
| response time (ms), 95th percentile | 1480 | 1506 |
| response time (ms), 99th percentile | 3544 | 3627 |
| time over the response line (% of samples) | 16.46 | 15.29 |
| failed requests (%) | 1.449 | 1.608 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8717 | 0.2983 |
| utilisation (used / allocatable) | 0.08541 | 0.08502 |
| CPU used (cores), mean | 2.05 | 2.04 |
| Omni's own CPU (cores), mean | 0 | 0.00931 |
| CPU used with Omni's own (cores), mean | 2.05 | 2.05 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 338.8 | 341.7 |
| HPA replicas, mean | 14.64 | 14.56 |
| pods started | 5.4 | 5.2 |
| pod start wait, total (s) | 14.5 | 17 |
| pod start wait, mean (s) | 2.419 | 2.827 |
| host CPU busy, the real machine under kind (%) | 58.67 | 58.72 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 290.3 | 302.2 |
| second app: response time (ms), 99th percentile | 3589 | 2420 |
| second app: time over the response line (% of samples) | 11.01 | 10.98 |
| second app: failed requests (%) | 8.082 | 8.531 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.1% | -0.0004361 to +0.003769 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170 | 170.1 | +0.1% | -0.3297 to +0.5671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170 | 170.1 | +0.1% | -0.3297 to +0.5671 | no |
| response time (ms), mean | 364.2 | 318.3 | -12.6% | -77.02 to -14.8 | yes: GAIN |
| response time (ms), 95th percentile | 1480 | 1506 | +1.7% | -67.49 to +118.4 | no |
| response time (ms), 99th percentile | 3544 | 3627 | +2.3% | -308.5 to +473.7 | no |
| time over the response line (% of samples) | 16.46 | 15.29 | -7.1% | -2.674 to +0.3426 | no |
| failed requests (%) | 1.449 | 1.608 | +11.0% | -0.294 to +0.6122 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.4 | +0.0% | -0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.3 (native is 0) | +30.71 to +35.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8717 | 0.2983 | -65.8% | -1.446 to +0.2995 | no |
| utilisation (used / allocatable) | 0.08541 | 0.08502 | -0.5% | -0.002032 to +0.001246 | no |
| CPU used (cores), mean | 2.05 | 2.04 | -0.5% | -0.04876 to +0.02989 | no |
| Omni's own CPU (cores), mean | 0 | 0.00931 | +0.00931 (native is 0) | +0.008036 to +0.01058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.05 | 2.05 | -0.0% | -0.03991 to +0.03966 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 338.8 | 341.7 | +0.9% | -4.07 to +9.884 | no |
| HPA replicas, mean | 14.64 | 14.56 | -0.6% | -0.4275 to +0.2521 | no |
| pods started | 5.4 | 5.2 | -3.7% | -1.358 to +0.9583 | no |
| pod start wait, total (s) | 14.5 | 17 | +17.2% | -4.153 to +9.153 | no |
| pod start wait, mean (s) | 2.419 | 2.827 | +16.9% | -0.4394 to +1.257 | no |
| host CPU busy, the real machine under kind (%) | 58.67 | 58.72 | +0.1% | -0.8057 to +0.8975 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 290.3 | 302.2 | +4.1% | -35.47 to +59.28 | no |
| second app: response time (ms), 99th percentile | 3589 | 2420 | -32.6% | -2807 to +468.3 | no |
| second app: time over the response line (% of samples) | 11.01 | 10.98 | -0.2% | -0.9062 to +0.8519 | no |
| second app: failed requests (%) | 8.082 | 8.531 | +5.6% | -0.1539 to +1.051 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*