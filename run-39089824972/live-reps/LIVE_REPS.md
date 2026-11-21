# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.914 |
| node-hours | 1.493 | 1.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 214.6 | 121.6 |
| response time (ms), 95th percentile | 396.2 | 167.4 |
| response time (ms), 99th percentile | 1024 | 479.8 |
| time over the response line (% of samples) | 8.524 | 5.731 |
| failed requests (%) | 5.326 | 4.795 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.41 | 0.6117 |
| utilisation (used / allocatable) | 0.07295 | 0.07111 |
| CPU used (cores), mean | 1.726 | 1.682 |
| Omni's own CPU (cores), mean | 0 | 0.00995 |
| CPU used with Omni's own (cores), mean | 1.726 | 1.692 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.4 | 394.8 |
| HPA replicas, mean | 8.902 | 10.87 |
| pods started | 4.3 | 6 |
| pod start wait, total (s) | 14 | 14 |
| pod start wait, mean (s) | 2.775 | 2.131 |
| host CPU busy, the real machine under kind (%) | 49.18 | 48.28 |
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
| worker nodes in service, mean | 5.915 | 5.914 | -0.0% | -0.006179 to +0.005032 | no |
| node-hours | 1.493 | 1.487 | -0.4% | -0.01318 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.1 | -0.7% | -1.802 to -0.4358 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.5 | -0.7% | -1.793 to -0.4526 | yes: GAIN |
| response time (ms), mean | 214.6 | 121.6 | -43.3% | -147.3 to -38.64 | yes: GAIN |
| response time (ms), 95th percentile | 396.2 | 167.4 | -57.7% | -263.1 to -194.4 | yes: GAIN |
| response time (ms), 99th percentile | 1024 | 479.8 | -53.2% | -839.7 to -249.1 | yes: GAIN |
| time over the response line (% of samples) | 8.524 | 5.731 | -32.8% | -3.94 to -1.645 | yes: GAIN |
| failed requests (%) | 5.326 | 4.795 | -10.0% | -1.083 to +0.02139 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 5.9 | -23.4% | -2.958 to -0.6417 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.7 | +30.7 (native is 0) | +27.57 to +33.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.41 | 0.6117 | +49.2% | -0.1859 to +0.5893 | no |
| utilisation (used / allocatable) | 0.07295 | 0.07111 | -2.5% | -0.003654 to -1.429e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.726 | 1.682 | -2.5% | -0.08582 to -0.001087 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00995 | +0.00995 (native is 0) | +0.008783 to +0.01112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.726 | 1.692 | -1.9% | -0.07527 to +0.008263 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.4 | 394.8 | +1.9% | -2.124 to +16.87 | no |
| HPA replicas, mean | 8.902 | 10.87 | +22.1% | +1.174 to +2.768 | yes: power given |
| pods started | 4.3 | 6 | +39.5% | +0.7433 to +2.657 | yes: power given |
| pod start wait, total (s) | 14 | 14 | +0.0% | -7.129 to +7.129 | no |
| pod start wait, mean (s) | 2.775 | 2.131 | -23.2% | -1.716 to +0.4285 | no |
| host CPU busy, the real machine under kind (%) | 49.18 | 48.28 | -1.8% | -1.766 to -0.02769 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 70 | 15.2 |  |
| machine down | omni | 45 | 9.3 | -26 s (-37%) |
| spike | native | 267 | 70.3 |  |
| spike | omni | 263 | 62.4 | -5 s (-2%) |
| runaway pod started | native | 133 | 13.0 |  |
| runaway pod started | omni | 95 | 8.4 | -38 s (-29%) |
| probe blind | native | 76 | 1.0 |  |
| probe blind | omni | 60 | 0.1 | -15 s (-20%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*