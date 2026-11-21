# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.335 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.9 | 479.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.9 | 479.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 265.3 | 136.4 |
| response time (ms), 95th percentile | 686.4 | 259.5 |
| response time (ms), 99th percentile | 1311 | 664.5 |
| time over the response line (% of samples) | 12.35 | 2.774 |
| failed requests (%) | 1.277 | 0.9818 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.6 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9233 | 0.745 |
| utilisation (used / allocatable) | 0.0778 | 0.0746 |
| CPU used (cores), mean | 1.867 | 1.79 |
| Omni's own CPU (cores), mean | 0 | 0.00911 |
| CPU used with Omni's own (cores), mean | 1.867 | 1.8 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 394.1 | 409.8 |
| HPA replicas, mean | 9.651 | 10.45 |
| pods started | 5.9 | 13.8 |
| pod start wait, total (s) | 23.2 | 33 |
| pod start wait, mean (s) | 3.367 | 2.413 |
| host CPU busy, the real machine under kind (%) | 53.93 | 52.3 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.237e-15 to -7.272e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.335 | 4.337 | +0.1% | -0.007273 to +0.01194 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.9 | 479.1 | -0.4% | -3.292 to -0.3412 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.9 | 479.1 | -0.4% | -3.292 to -0.3412 | yes: GAIN |
| response time (ms), mean | 265.3 | 136.4 | -48.6% | -172.3 to -85.45 | yes: GAIN |
| response time (ms), 95th percentile | 686.4 | 259.5 | -62.2% | -570 to -283.9 | yes: GAIN |
| response time (ms), 99th percentile | 1311 | 664.5 | -49.3% | -870.3 to -422.7 | yes: GAIN |
| time over the response line (% of samples) | 12.35 | 2.774 | -77.5% | -14.52 to -4.635 | yes: GAIN |
| failed requests (%) | 1.277 | 0.9818 | -23.1% | -0.4958 to -0.09464 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.6 | 7.6 | -64.8% | -20.44 to -7.558 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 | +53.3 (native is 0) | +36.28 to +70.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9233 | 0.745 | -19.3% | -0.7017 to +0.345 | no |
| utilisation (used / allocatable) | 0.0778 | 0.0746 | -4.1% | -0.004071 to -0.002327 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.867 | 1.79 | -4.1% | -0.09771 to -0.05585 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00911 | +0.00911 (native is 0) | +0.007418 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.867 | 1.8 | -3.6% | -0.08775 to -0.04759 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 394.1 | 409.8 | +4.0% | +10.32 to +20.91 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.651 | 10.45 | +8.3% | -0.4767 to +2.077 | no |
| pods started | 5.9 | 13.8 | +133.9% | +3.21 to +12.59 | yes: power given |
| pod start wait, total (s) | 23.2 | 33 | +42.2% | -2.589 to +22.19 | no |
| pod start wait, mean (s) | 3.367 | 2.413 | -28.3% | -1.808 to -0.09955 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 53.93 | 52.3 | -3.0% | -2.174 to -1.087 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*