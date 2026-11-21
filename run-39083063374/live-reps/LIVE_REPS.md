# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.8 | 521.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.8 | 521.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 298.5 | 184.8 |
| response time (ms), 95th percentile | 850.7 | 396.7 |
| response time (ms), 99th percentile | 2411 | 2216 |
| time over the response line (% of samples) | 22.65 | 14.42 |
| failed requests (%) | 13.15 | 11.42 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.2 | 25.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.3217 |
| utilisation (used / allocatable) | 0.1105 | 0.1092 |
| CPU used (cores), mean | 2.652 | 2.62 |
| Omni's own CPU (cores), mean | 0 | 0.009 |
| CPU used with Omni's own (cores), mean | 2.652 | 2.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.9 | 276.4 |
| HPA replicas, mean | 9.534 | 9.939 |
| pods started | 5 | 6.1 |
| pod start wait, total (s) | 15.2 | 14.2 |
| pod start wait, mean (s) | 2.795 | 2.238 |
| host CPU busy, the real machine under kind (%) | 74.18 | 73.7 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.718e-16 to +8.494e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.507 | -0.2% | -0.0161 to +0.001102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.8 | 521.2 | -0.3% | -2.58 to -0.6736 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.8 | 521.2 | -0.3% | -2.58 to -0.6736 | yes: GAIN |
| response time (ms), mean | 298.5 | 184.8 | -38.1% | -143.8 to -83.65 | yes: GAIN |
| response time (ms), 95th percentile | 850.7 | 396.7 | -53.4% | -592.3 to -315.7 | yes: GAIN |
| response time (ms), 99th percentile | 2411 | 2216 | -8.1% | -936.9 to +547.9 | no |
| time over the response line (% of samples) | 22.65 | 14.42 | -36.3% | -10.55 to -5.902 | yes: GAIN |
| failed requests (%) | 13.15 | 11.42 | -13.1% | -2.567 to -0.8871 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.2 | 25.5 | -20.8% | -8.354 to -5.046 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.1 (native is 0) | +27.54 to +46.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.3217 | +2.7% | -0.143 to +0.1597 | no |
| utilisation (used / allocatable) | 0.1105 | 0.1092 | -1.2% | -0.002325 to -0.0003326 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.652 | 2.62 | -1.2% | -0.05579 to -0.007981 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.009 | +0.009 (native is 0) | +0.007918 to +0.01008 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.652 | 2.629 | -0.9% | -0.04661 to +0.0008369 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.9 | 276.4 | +0.9% | +0.6082 to +4.493 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.534 | 9.939 | +4.2% | -0.1404 to +0.9505 | no |
| pods started | 5 | 6.1 | +22.0% | -1.223 to +3.423 | no |
| pod start wait, total (s) | 15.2 | 14.2 | -6.6% | -4.724 to +2.724 | no |
| pod start wait, mean (s) | 2.795 | 2.238 | -20.0% | -1.206 to +0.09009 | no |
| host CPU busy, the real machine under kind (%) | 74.18 | 73.7 | -0.6% | -1.236 to +0.2779 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.8 |  |  | 10 |
| compass | 26.4 | +57.1% | +6.6 to +12.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*