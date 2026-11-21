# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.518 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 510.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 254.3 | 129.5 |
| response time (ms), 95th percentile | 635.2 | 248 |
| response time (ms), 99th percentile | 2696 | 1117 |
| time over the response line (% of samples) | 16.66 | 10.62 |
| failed requests (%) | 9.941 | 8.977 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 18.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.4367 |
| utilisation (used / allocatable) | 0.09398 | 0.092 |
| CPU used (cores), mean | 2.255 | 2.208 |
| Omni's own CPU (cores), mean | 0 | 0.00859 |
| CPU used with Omni's own (cores), mean | 2.255 | 2.217 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.7 | 353.6 |
| HPA replicas, mean | 9.501 | 9.346 |
| pods started | 4.6 | 6.1 |
| pod start wait, total (s) | 18.5 | 19.1 |
| pod start wait, mean (s) | 3.185 | 2.915 |
| host CPU busy, the real machine under kind (%) | 63.77 | 62.89 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.518 | 4.515 | -0.1% | -0.01154 to +0.004536 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 510.5 | -0.3% | -2.293 to -0.9335 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.5 | -0.3% | -2.293 to -0.9335 | yes: GAIN |
| response time (ms), mean | 254.3 | 129.5 | -49.1% | -173.8 to -75.79 | yes: GAIN |
| response time (ms), 95th percentile | 635.2 | 248 | -61.0% | -508.2 to -266.2 | yes: GAIN |
| response time (ms), 99th percentile | 2696 | 1117 | -58.6% | -2434 to -724.9 | yes: GAIN |
| time over the response line (% of samples) | 16.66 | 10.62 | -36.2% | -9.116 to -2.952 | yes: GAIN |
| failed requests (%) | 9.941 | 8.977 | -9.7% | -1.569 to -0.3595 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 18.6 | -21.2% | -6.012 to -3.988 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 | +37.6 (native is 0) | +27 to +48.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.4367 | +63.7% | -0.2666 to +0.6066 | no |
| utilisation (used / allocatable) | 0.09398 | 0.092 | -2.1% | -0.002755 to -0.001194 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.255 | 2.208 | -2.1% | -0.06613 to -0.02865 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00859 | +0.00859 (native is 0) | +0.006754 to +0.01043 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.255 | 2.217 | -1.7% | -0.05758 to -0.02003 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.7 | 353.6 | +2.6% | +0.3528 to +17.36 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.501 | 9.346 | -1.6% | -0.6357 to +0.3268 | no |
| pods started | 4.6 | 6.1 | +32.6% | -0.1605 to +3.161 | no |
| pod start wait, total (s) | 18.5 | 19.1 | +3.2% | -5.377 to +6.577 | no |
| pod start wait, mean (s) | 3.185 | 2.915 | -8.5% | -1.02 to +0.4804 | no |
| host CPU busy, the real machine under kind (%) | 63.77 | 62.89 | -1.4% | -1.573 to -0.1989 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*