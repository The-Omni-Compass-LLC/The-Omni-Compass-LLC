# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.335 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 475.5 | 473.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.5 | 473.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 214.7 | 108.1 |
| response time (ms), 95th percentile | 556 | 210.6 |
| response time (ms), 99th percentile | 960.3 | 494.4 |
| time over the response line (% of samples) | 8.419 | 1.774 |
| failed requests (%) | 0.6721 | 0.5346 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.2 | 4.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7433 | 1.215 |
| utilisation (used / allocatable) | 0.06946 | 0.06678 |
| CPU used (cores), mean | 1.667 | 1.603 |
| Omni's own CPU (cores), mean | 0 | 0.00817 |
| CPU used with Omni's own (cores), mean | 1.667 | 1.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.7 | 441.3 |
| HPA replicas, mean | 9.617 | 9.689 |
| pods started | 6.3 | 12.3 |
| pod start wait, total (s) | 20.7 | 33.3 |
| pod start wait, mean (s) | 3.076 | 2.677 |
| host CPU busy, the real machine under kind (%) | 48.4 | 46.96 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.989e-16 to +5.436e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.335 | 4.335 | +0.0% | -0.005751 to +0.007417 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 475.5 | 473.8 | -0.3% | -2.561 to -0.7432 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.5 | 473.8 | -0.3% | -2.561 to -0.7432 | yes: GAIN |
| response time (ms), mean | 214.7 | 108.1 | -49.7% | -144.6 to -68.59 | yes: GAIN |
| response time (ms), 95th percentile | 556 | 210.6 | -62.1% | -446.8 to -244 | yes: GAIN |
| response time (ms), 99th percentile | 960.3 | 494.4 | -48.5% | -613.1 to -318.8 | yes: GAIN |
| time over the response line (% of samples) | 8.419 | 1.774 | -78.9% | -10.89 to -2.399 | yes: GAIN |
| failed requests (%) | 0.6721 | 0.5346 | -20.5% | -0.3201 to +0.04516 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.2 | 4.5 | -72.2% | -17.63 to -5.772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.3 (native is 0) | +31.4 to +63.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7433 | 1.215 | +63.5% | -0.3315 to +1.275 | no |
| utilisation (used / allocatable) | 0.06946 | 0.06678 | -3.9% | -0.003775 to -0.001591 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.667 | 1.603 | -3.9% | -0.0906 to -0.03818 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00817 | +0.00817 (native is 0) | +0.006521 to +0.009819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.667 | 1.611 | -3.4% | -0.08114 to -0.0313 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.7 | 441.3 | +2.9% | +8.896 to +16.21 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.617 | 9.689 | +0.7% | -0.8958 to +1.04 | no |
| pods started | 6.3 | 12.3 | +95.2% | +2.23 to +9.77 | yes: power given |
| pod start wait, total (s) | 20.7 | 33.3 | +60.9% | -0.1075 to +25.31 | no |
| pod start wait, mean (s) | 3.076 | 2.677 | -13.0% | -1.486 to +0.6884 | no |
| host CPU busy, the real machine under kind (%) | 48.4 | 46.96 | -3.0% | -2.017 to -0.875 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*