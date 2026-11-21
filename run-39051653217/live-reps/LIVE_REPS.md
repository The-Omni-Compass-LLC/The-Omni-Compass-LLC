# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.919 |
| node-hours | 1.495 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.5 | 165.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.9 | 164 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 197.4 | 121.8 |
| response time (ms), 95th percentile | 381.7 | 179.3 |
| response time (ms), 99th percentile | 1098 | 839.1 |
| time over the response line (% of samples) | 8.385 | 5.76 |
| failed requests (%) | 5.619 | 4.534 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 1.18 |
| utilisation (used / allocatable) | 0.07359 | 0.07053 |
| CPU used (cores), mean | 1.741 | 1.669 |
| Omni's own CPU (cores), mean | 0 | 0.01038 |
| CPU used with Omni's own (cores), mean | 1.741 | 1.68 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 383.8 | 397.2 |
| HPA replicas, mean | 8.766 | 10.68 |
| pods started | 4.9 | 8.1 |
| pod start wait, total (s) | 17.1 | 29.7 |
| pod start wait, mean (s) | 3.166 | 3.463 |
| host CPU busy, the real machine under kind (%) | 49.62 | 48.36 |
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
| worker nodes in service, mean | 5.915 | 5.919 | +0.1% | -0.00459 to +0.01156 | no |
| node-hours | 1.495 | 1.493 | -0.1% | -0.01118 to +0.007343 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.5 | 165.5 | -0.6% | -1.862 to -0.02698 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.9 | 164 | -0.5% | -1.892 to +0.1408 | no |
| response time (ms), mean | 197.4 | 121.8 | -38.3% | -98.04 to -53.18 | yes: GAIN |
| response time (ms), 95th percentile | 381.7 | 179.3 | -53.0% | -266.8 to -138 | yes: GAIN |
| response time (ms), 99th percentile | 1098 | 839.1 | -23.6% | -1181 to +664.2 | no |
| time over the response line (% of samples) | 8.385 | 5.76 | -31.3% | -3.795 to -1.456 | yes: GAIN |
| failed requests (%) | 5.619 | 4.534 | -19.3% | -1.734 to -0.4357 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.6 | -20.0% | -2.24 to -0.5604 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.1 (native is 0) | +29.15 to +39.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 1.18 | +142.5% | +0.1323 to +1.254 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07359 | 0.07053 | -4.2% | -0.004739 to -0.001397 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.741 | 1.669 | -4.1% | -0.1125 to -0.03124 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01038 | +0.0104 (native is 0) | +0.009013 to +0.01175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.741 | 1.68 | -3.5% | -0.101 to -0.02204 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 383.8 | 397.2 | +3.5% | +6.895 to +19.92 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.766 | 10.68 | +21.9% | +1.076 to +2.759 | yes: power given |
| pods started | 4.9 | 8.1 | +65.3% | +1.39 to +5.01 | yes: power given |
| pod start wait, total (s) | 17.1 | 29.7 | +73.7% | -3.509 to +28.71 | no |
| pod start wait, mean (s) | 3.166 | 3.463 | +9.4% | -1.155 to +1.749 | no |
| host CPU busy, the real machine under kind (%) | 49.62 | 48.36 | -2.5% | -2.208 to -0.3124 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 61 | 13.9 |  |
| machine down | omni | 42 | 9.8 | -18 s (-30%) |
| spike | native | 267 | 72.2 |  |
| spike | omni | 267 | 56.6 | -1 s (-0%) |
| runaway pod started | native | 119 | 13.6 |  |
| runaway pod started | omni | 91 | 7.2 | -28 s (-23%) |
| probe blind | native | 67 | 0.6 |  |
| probe blind | omni | 60 | 0.0 | -7 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*