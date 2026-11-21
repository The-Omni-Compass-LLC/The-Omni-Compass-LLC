# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.915 |
| node-hours | 1.495 | 1.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.7 | 164.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.1 | 162.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 216.3 | 136.2 |
| response time (ms), 95th percentile | 416.1 | 188 |
| response time (ms), 99th percentile | 1957 | 968.4 |
| time over the response line (% of samples) | 8.438 | 5.403 |
| failed requests (%) | 4.91 | 4.051 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.8483 |
| utilisation (used / allocatable) | 0.0697 | 0.06799 |
| CPU used (cores), mean | 1.649 | 1.608 |
| Omni's own CPU (cores), mean | 0 | 0.0102 |
| CPU used with Omni's own (cores), mean | 1.649 | 1.619 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412 | 417.3 |
| HPA replicas, mean | 8.635 | 10.53 |
| pods started | 4.6 | 7.2 |
| pod start wait, total (s) | 16.7 | 27 |
| pod start wait, mean (s) | 3.17 | 3.237 |
| host CPU busy, the real machine under kind (%) | 47.22 | 46.52 |
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
| worker nodes in service, mean | 5.915 | 5.915 | -0.0% | -0.001089 to +3.128e-05 | no |
| node-hours | 1.495 | 1.486 | -0.6% | -0.01892 to +0.0005877 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.7 | 164.3 | -0.9% | -2.727 to -0.09111 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.1 | 162.7 | -0.9% | -2.727 to -0.09111 | yes: GAIN |
| response time (ms), mean | 216.3 | 136.2 | -37.0% | -133.8 to -26.4 | yes: GAIN |
| response time (ms), 95th percentile | 416.1 | 188 | -54.8% | -280.1 to -176.1 | yes: GAIN |
| response time (ms), 99th percentile | 1957 | 968.4 | -50.5% | -1652 to -325.2 | yes: GAIN |
| time over the response line (% of samples) | 8.438 | 5.403 | -36.0% | -3.995 to -2.075 | yes: GAIN |
| failed requests (%) | 4.91 | 4.051 | -17.5% | -1.208 to -0.5097 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.4 | -22.9% | -2.203 to -0.9968 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.3 (native is 0) | +30.44 to +38.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.8483 | +83.8% | -0.09727 to +0.8706 | no |
| utilisation (used / allocatable) | 0.0697 | 0.06799 | -2.5% | -0.003675 to +0.000259 | no |
| CPU used (cores), mean | 1.649 | 1.608 | -2.5% | -0.08714 to +0.006014 | no |
| Omni's own CPU (cores), mean | 0 | 0.0102 | +0.0102 (native is 0) | +0.008698 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.649 | 1.619 | -1.8% | -0.07594 to +0.01521 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412 | 417.3 | +1.3% | -5.926 to +16.46 | no |
| HPA replicas, mean | 8.635 | 10.53 | +21.9% | +1.162 to +2.622 | yes: power given |
| pods started | 4.6 | 7.2 | +56.5% | +1.243 to +3.957 | yes: power given |
| pod start wait, total (s) | 16.7 | 27 | +61.7% | -4.818 to +25.42 | no |
| pod start wait, mean (s) | 3.17 | 3.237 | +2.1% | -1.036 to +1.17 | no |
| host CPU busy, the real machine under kind (%) | 47.22 | 46.52 | -1.5% | -1.548 to +0.16 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 59 | 16.0 |  |
| machine down | omni | 41 | 9.1 | -18 s (-31%) |
| spike | native | 255 | 66.1 |  |
| spike | omni | 240 | 58.1 | -16 s (-6%) |
| runaway pod started | native | 106 | 11.2 |  |
| runaway pod started | omni | 90 | 7.1 | -16 s (-15%) |
| probe blind | native | 64 | 0.3 |  |
| probe blind | omni | 60 | 0.1 | -4 s (-6%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*