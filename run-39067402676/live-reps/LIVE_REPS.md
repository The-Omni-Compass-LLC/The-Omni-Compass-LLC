# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.913 |
| node-hours | 1.501 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 167 | 165.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 163.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 211 | 121.9 |
| response time (ms), 95th percentile | 381.6 | 163.5 |
| response time (ms), 99th percentile | 1169 | 721.9 |
| time over the response line (% of samples) | 8.219 | 5.692 |
| failed requests (%) | 5.515 | 4.594 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.9133 |
| utilisation (used / allocatable) | 0.07266 | 0.0709 |
| CPU used (cores), mean | 1.719 | 1.677 |
| Omni's own CPU (cores), mean | 0 | 0.01025 |
| CPU used with Omni's own (cores), mean | 1.719 | 1.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 391.9 | 398.9 |
| HPA replicas, mean | 8.815 | 10.54 |
| pods started | 4.3 | 6.2 |
| pod start wait, total (s) | 14.2 | 22.6 |
| pod start wait, mean (s) | 2.827 | 3.362 |
| host CPU busy, the real machine under kind (%) | 48.93 | 48.24 |
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
| worker nodes in service, mean | 5.914 | 5.913 | -0.0% | -0.001527 to -0.0001468 | yes: GAIN |
| node-hours | 1.501 | 1.489 | -0.8% | -0.02074 to -0.004645 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 167 | 165.3 | -1.1% | -2.868 to -0.6969 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 163.6 | -1.1% | -2.87 to -0.6984 | yes: GAIN |
| response time (ms), mean | 211 | 121.9 | -42.2% | -125.3 to -52.96 | yes: GAIN |
| response time (ms), 95th percentile | 381.6 | 163.5 | -57.2% | -244 to -192.2 | yes: GAIN |
| response time (ms), 99th percentile | 1169 | 721.9 | -38.3% | -804.4 to -90.55 | yes: GAIN |
| time over the response line (% of samples) | 8.219 | 5.692 | -30.7% | -3.272 to -1.781 | yes: GAIN |
| failed requests (%) | 5.515 | 4.594 | -16.7% | -1.363 to -0.4786 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.9 | -20.3% | -2.006 to -0.9942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31 | +31 (native is 0) | +26.28 to +35.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.9133 | +176.8% | +0.1616 to +1.005 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07266 | 0.0709 | -2.4% | -0.002903 to -0.000627 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.719 | 1.677 | -2.4% | -0.06901 to -0.01501 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01025 | +0.0102 (native is 0) | +0.009286 to +0.01121 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 1.687 | -1.8% | -0.05833 to -0.005189 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 391.9 | 398.9 | +1.8% | +1.499 to +12.53 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.815 | 10.54 | +19.6% | +0.9987 to +2.457 | yes: power given |
| pods started | 4.3 | 6.2 | +44.2% | -0.02085 to +3.821 | no |
| pod start wait, total (s) | 14.2 | 22.6 | +59.2% | -8.828 to +25.63 | no |
| pod start wait, mean (s) | 2.827 | 3.362 | +18.9% | -2.093 to +3.162 | no |
| host CPU busy, the real machine under kind (%) | 48.93 | 48.24 | -1.4% | -1.501 to +0.1222 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 13.9 |  |
| machine down | omni | 37 | 9.0 | -27 s (-42%) |
| spike | native | 273 | 76.2 |  |
| spike | omni | 268 | 62.8 | -4 s (-2%) |
| runaway pod started | native | 144 | 12.9 |  |
| runaway pod started | omni | 100 | 8.1 | -44 s (-30%) |
| probe blind | native | 67 | 0.4 |  |
| probe blind | omni | 36 | 0.0 | -31 s (-46%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*