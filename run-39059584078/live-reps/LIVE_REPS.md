# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.494 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.7 | 165.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165 | 164.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 226.4 | 116 |
| response time (ms), 95th percentile | 384.7 | 148.1 |
| response time (ms), 99th percentile | 1574 | 646.3 |
| time over the response line (% of samples) | 8.006 | 5.972 |
| failed requests (%) | 5.369 | 5.192 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.66 | 0.9367 |
| utilisation (used / allocatable) | 0.07482 | 0.07295 |
| CPU used (cores), mean | 1.77 | 1.726 |
| Omni's own CPU (cores), mean | 0 | 0.01001 |
| CPU used with Omni's own (cores), mean | 1.77 | 1.736 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 371.9 | 379.9 |
| HPA replicas, mean | 8.968 | 10.13 |
| pods started | 4.3 | 6.2 |
| pod start wait, total (s) | 20.2 | 24.7 |
| pod start wait, mean (s) | 5.17 | 3.855 |
| host CPU busy, the real machine under kind (%) | 50.51 | 49.76 |
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
| worker nodes in service, mean | 5.913 | 5.913 | -0.0% | -0.0008549 to +0.0002554 | no |
| node-hours | 1.494 | 1.49 | -0.2% | -0.009637 to +0.002915 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.7 | 165.9 | -0.5% | -1.342 to -0.2423 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165 | 164.2 | -0.5% | -1.342 to -0.2462 | yes: GAIN |
| response time (ms), mean | 226.4 | 116 | -48.7% | -154.8 to -65.86 | yes: GAIN |
| response time (ms), 95th percentile | 384.7 | 148.1 | -61.5% | -271.3 to -201.8 | yes: GAIN |
| response time (ms), 99th percentile | 1574 | 646.3 | -58.9% | -1652 to -203.1 | yes: GAIN |
| time over the response line (% of samples) | 8.006 | 5.972 | -25.4% | -2.948 to -1.119 | yes: GAIN |
| failed requests (%) | 5.369 | 5.192 | -3.3% | -0.4636 to +0.1087 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 6.2 | -13.9% | -1.954 to -0.04626 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.9 | +27.9 (native is 0) | +23.1 to +32.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.66 | 0.9367 | +41.9% | -0.2892 to +0.8425 | no |
| utilisation (used / allocatable) | 0.07482 | 0.07295 | -2.5% | -0.003667 to -7.017e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.77 | 1.726 | -2.5% | -0.08673 to -0.001832 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01001 | +0.01 (native is 0) | +0.008961 to +0.01106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.77 | 1.736 | -1.9% | -0.07633 to +0.007783 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 371.9 | 379.9 | +2.1% | +0.4161 to +15.46 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.968 | 10.13 | +13.0% | +0.4643 to +1.86 | yes: power given |
| pods started | 4.3 | 6.2 | +44.2% | -0.1358 to +3.936 | no |
| pod start wait, total (s) | 20.2 | 24.7 | +22.3% | -22.92 to +31.92 | no |
| pod start wait, mean (s) | 5.17 | 3.855 | -25.4% | -8.109 to +5.479 | no |
| host CPU busy, the real machine under kind (%) | 50.51 | 49.76 | -1.5% | -1.707 to +0.2102 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 72 | 13.7 |  |
| machine down | omni | 49 | 10.0 | -23 s (-31%) |
| spike | native | 274 | 72.7 |  |
| spike | omni | 273 | 62.5 | -2 s (-1%) |
| runaway pod started | native | 125 | 11.9 |  |
| runaway pod started | omni | 100 | 8.0 | -24 s (-20%) |
| probe blind | native | 60 | 0.1 |  |
| probe blind | omni | 60 | 0.0 | -0 s (-0%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*