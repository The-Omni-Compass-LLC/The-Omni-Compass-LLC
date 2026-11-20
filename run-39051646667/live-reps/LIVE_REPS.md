# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 508.4 | 507.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.4 | 507.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 227 | 135.9 |
| response time (ms), 95th percentile | 616.2 | 264.6 |
| response time (ms), 99th percentile | 1697 | 1561 |
| time over the response line (% of samples) | 14.67 | 8.378 |
| failed requests (%) | 7.74 | 6.576 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.5 | 14.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6 | 0.5017 |
| utilisation (used / allocatable) | 0.08969 | 0.08781 |
| CPU used (cores), mean | 2.153 | 2.107 |
| Omni's own CPU (cores), mean | 0 | 0.00764 |
| CPU used with Omni's own (cores), mean | 2.153 | 2.115 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 346.4 | 353.9 |
| HPA replicas, mean | 9.307 | 9.152 |
| pods started | 5.4 | 5.5 |
| pod start wait, total (s) | 19.5 | 18.9 |
| pod start wait, mean (s) | 3.249 | 2.964 |
| host CPU busy, the real machine under kind (%) | 60.84 | 59.87 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.003e-15 to +4.702e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.511 | 4.513 | +0.0% | -0.003217 to +0.006217 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508.4 | 507.4 | -0.2% | -1.815 to -0.1799 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.4 | 507.4 | -0.2% | -1.815 to -0.1799 | yes: GAIN |
| response time (ms), mean | 227 | 135.9 | -40.1% | -116.1 to -66.1 | yes: GAIN |
| response time (ms), 95th percentile | 616.2 | 264.6 | -57.1% | -442.8 to -260.4 | yes: GAIN |
| response time (ms), 99th percentile | 1697 | 1561 | -8.0% | -565.6 to +293.6 | no |
| time over the response line (% of samples) | 14.67 | 8.378 | -42.9% | -9.623 to -2.968 | yes: GAIN |
| failed requests (%) | 7.74 | 6.576 | -15.0% | -2.169 to -0.1582 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.5 | 14.7 | -28.3% | -7.789 to -3.811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.6 | +27.6 (native is 0) | +18.68 to +36.52 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6 | 0.5017 | -16.4% | -0.2579 to +0.06126 | no |
| utilisation (used / allocatable) | 0.08969 | 0.08781 | -2.1% | -0.002623 to -0.001143 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.153 | 2.107 | -2.1% | -0.06295 to -0.02743 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00764 | +0.00764 (native is 0) | +0.006279 to +0.009001 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.153 | 2.115 | -1.7% | -0.05503 to -0.02007 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 346.4 | 353.9 | +2.2% | +2.108 to +12.82 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.307 | 9.152 | -1.7% | -0.5492 to +0.2386 | no |
| pods started | 5.4 | 5.5 | +1.9% | -1.567 to +1.767 | no |
| pod start wait, total (s) | 19.5 | 18.9 | -3.1% | -5.152 to +3.952 | no |
| pod start wait, mean (s) | 3.249 | 2.964 | -8.8% | -0.6664 to +0.0956 | no |
| host CPU busy, the real machine under kind (%) | 60.84 | 59.87 | -1.6% | -1.539 to -0.3877 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 25.8 |  |  | 10 |
| compass | 35.4 | +37.2% | +6.6 to +12.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*