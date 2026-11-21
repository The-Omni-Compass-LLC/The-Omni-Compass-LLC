# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 160.2 | 82.56 |
| response time (ms), 95th percentile | 358.9 | 127.5 |
| response time (ms), 99th percentile | 617.3 | 189.1 |
| time over the response line (% of samples) | 2.319 | 0.04834 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2867 | 0.4067 |
| utilisation (used / allocatable) | 0.03974 | 0.03786 |
| CPU used (cores), mean | 0.9537 | 0.9088 |
| Omni's own CPU (cores), mean | 0 | 0.00864 |
| CPU used with Omni's own (cores), mean | 0.9537 | 0.9174 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.5 | 715.4 |
| HPA replicas, mean | 8.761 | 8.461 |
| pods started | 4.4 | 4.3 |
| pod start wait, total (s) | 14.3 | 13.8 |
| pod start wait, mean (s) | 2.953 | 2.948 |
| host CPU busy, the real machine under kind (%) | 28.52 | 27.84 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.624e-16 to +6.953e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.516 | -0.2% | -0.01167 to +0.004337 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.1 | -0.5% | -1.643 to +0.04696 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.1 | -0.5% | -1.643 to +0.04696 | no |
| response time (ms), mean | 160.2 | 82.56 | -48.5% | -97.74 to -57.5 | yes: GAIN |
| response time (ms), 95th percentile | 358.9 | 127.5 | -64.5% | -281.6 to -181.4 | yes: GAIN |
| response time (ms), 99th percentile | 617.3 | 189.1 | -69.4% | -512.7 to -343.7 | yes: GAIN |
| time over the response line (% of samples) | 2.319 | 0.04834 | -97.9% | -3.229 to -1.314 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | -100.0% | -3.817 to -1.183 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 | +20.6 (native is 0) | +18.16 to +23.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2867 | 0.4067 | +41.9% | -0.1076 to +0.3476 | no |
| utilisation (used / allocatable) | 0.03974 | 0.03786 | -4.7% | -0.002958 to -0.0007847 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9537 | 0.9088 | -4.7% | -0.07098 to -0.01883 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00864 | +0.00864 (native is 0) | +0.007725 to +0.009555 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9537 | 0.9174 | -3.8% | -0.0618 to -0.01073 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.5 | 715.4 | +3.8% | +11.02 to +40.83 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.761 | 8.461 | -3.4% | -0.5556 to -0.04381 | yes: GAIN |
| pods started | 4.4 | 4.3 | -2.3% | -1.29 to +1.09 | no |
| pod start wait, total (s) | 14.3 | 13.8 | -3.5% | -6.195 to +5.195 | no |
| pod start wait, mean (s) | 2.953 | 2.948 | -0.2% | -0.8644 to +0.8544 | no |
| host CPU busy, the real machine under kind (%) | 28.52 | 27.84 | -2.4% | -1.39 to +0.03665 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*