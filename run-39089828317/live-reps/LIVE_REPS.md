# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.008 |
| node-hours | 2.514 | 2.099 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 242.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 538.4 | 481.2 |
| response time (ms), 95th percentile | 3224 | 3199 |
| response time (ms), 99th percentile | 4867 | 4841 |
| time over the response line (% of samples) | 15.7 | 14.97 |
| failed requests (%) | 0.02157 | 0.01042 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.8 | 192.3 |
| utilisation (used / allocatable) | 0.06218 | 0.073 |
| CPU used (cores), mean | 1.492 | 1.464 |
| Omni's own CPU (cores), mean | 0 | 0.02419 |
| CPU used with Omni's own (cores), mean | 1.492 | 1.488 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 399 |
| HPA replicas, mean | 2.141 | 2.216 |
| pods started | 0.2 | 0.1 |
| pod start wait, total (s) | 9 | 3.4 |
| pod start wait, mean (s) | 9 | 3.4 |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.57 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 584.4 | 586.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.414 |

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
| worker nodes in service, mean | 6 | 5.008 | -16.5% | -1.43 to -0.5534 | yes: GAIN |
| node-hours | 2.514 | 2.099 | -16.5% | -0.5998 to -0.2306 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 | -0.0% | -1.235 to +0.9828 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 242.1 | -11.5% | -45.07 to -17.59 | yes: GAIN |
| response time (ms), mean | 538.4 | 481.2 | -10.6% | -70.4 to -43.86 | yes: GAIN |
| response time (ms), 95th percentile | 3224 | 3199 | -0.8% | -172.8 to +123.9 | no |
| response time (ms), 99th percentile | 4867 | 4841 | -0.5% | -193 to +142.1 | no |
| time over the response line (% of samples) | 15.7 | 14.97 | -4.6% | -1.295 to -0.1477 | yes: GAIN |
| failed requests (%) | 0.02157 | 0.01042 | -51.7% | -0.05438 to +0.03208 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.2 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.9 (native is 0) | +10.92 to +12.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.8 | 192.3 | +1.3% | -2.036 to +6.962 | no |
| utilisation (used / allocatable) | 0.06218 | 0.073 | +17.4% | +0.005541 to +0.01611 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.492 | 1.464 | -1.9% | -0.0561 to -0.001205 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02419 | +0.0242 (native is 0) | +0.02092 to +0.02746 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.492 | 1.488 | -0.3% | -0.03337 to +0.02444 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 399 | -10.5% | -76.6 to -16.67 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.141 | 2.216 | +3.5% | -0.1491 to +0.2984 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.506 to +0.306 | no |
| pod start wait, total (s) | 9 | 3.4 | -62.2% | -22.28 to +11.08 | no |
| pod start wait, mean (s) | 9 | 3.4 | -62.2% | -22.28 to +11.08 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.57 | +1.8% | +0.5612 to +0.9424 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 584.4 | 586.7 | +0.4% | -1.106 to +5.706 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.414 | -26.4% | -2.201 to -0.9708 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*