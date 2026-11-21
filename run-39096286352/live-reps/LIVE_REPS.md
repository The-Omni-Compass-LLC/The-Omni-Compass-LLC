# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 143.1 | 75.33 |
| response time (ms), 95th percentile | 309.9 | 111.2 |
| response time (ms), 99th percentile | 523 | 161.8 |
| time over the response line (% of samples) | 1.711 | 0.02424 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3367 | 0.2883 |
| utilisation (used / allocatable) | 0.03685 | 0.03526 |
| CPU used (cores), mean | 0.8845 | 0.8462 |
| Omni's own CPU (cores), mean | 0 | 0.00765 |
| CPU used with Omni's own (cores), mean | 0.8845 | 0.8539 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 756.8 | 780.8 |
| HPA replicas, mean | 8.456 | 8.232 |
| pods started | 4.6 | 4.2 |
| pod start wait, total (s) | 18.9 | 15.5 |
| pod start wait, mean (s) | 3.697 | 3.208 |
| host CPU busy, the real machine under kind (%) | 26.63 | 25.83 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.517 | -0.0% | -0.0018 to +0.001467 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | -0.2% | -0.6257 to -0.1032 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | -0.2% | -0.6257 to -0.1032 | yes: GAIN |
| response time (ms), mean | 143.1 | 75.33 | -47.4% | -90.01 to -45.57 | yes: GAIN |
| response time (ms), 95th percentile | 309.9 | 111.2 | -64.1% | -259.7 to -137.6 | yes: GAIN |
| response time (ms), 99th percentile | 523 | 161.8 | -69.1% | -470.9 to -251.5 | yes: GAIN |
| time over the response line (% of samples) | 1.711 | 0.02424 | -98.6% | -2.77 to -0.6029 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.825 to -0.3749 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.5 (native is 0) | +16.1 to +18.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3367 | 0.2883 | -14.4% | -0.244 to +0.1474 | no |
| utilisation (used / allocatable) | 0.03685 | 0.03526 | -4.3% | -0.002585 to -0.0006034 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8845 | 0.8462 | -4.3% | -0.06203 to -0.01448 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00765 | +0.00765 (native is 0) | +0.006539 to +0.008761 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8845 | 0.8539 | -3.5% | -0.05347 to -0.00774 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 756.8 | 780.8 | +3.2% | +12.15 to +35.91 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.456 | 8.232 | -2.7% | -0.3709 to -0.07756 | yes: GAIN |
| pods started | 4.6 | 4.2 | -8.7% | -1.091 to +0.2911 | no |
| pod start wait, total (s) | 18.9 | 15.5 | -18.0% | -8.324 to +1.524 | no |
| pod start wait, mean (s) | 3.697 | 3.208 | -13.2% | -1.201 to +0.2242 | no |
| host CPU busy, the real machine under kind (%) | 26.63 | 25.83 | -3.0% | -1.324 to -0.2745 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*