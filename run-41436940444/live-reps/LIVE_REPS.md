# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.518 | 4.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 519.1 | 518.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.1 | 518.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 293.2 | 200.9 |
| response time (ms), 95th percentile | 785.6 | 480.5 |
| response time (ms), 99th percentile | 3041 | 2905 |
| time over the response line (% of samples) | 21.32 | 16.73 |
| failed requests (%) | 12.62 | 12.92 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.9 | 24.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 56.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.515 | 0.325 |
| utilisation (used / allocatable) | 0.1044 | 0.1044 |
| CPU used (cores), mean | 2.504 | 2.507 |
| Omni's own CPU (cores), mean | 0 | 0.0462 |
| CPU used with Omni's own (cores), mean | 2.504 | 2.553 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.1 | 304.5 |
| HPA replicas, mean | 9.439 | 10.66 |
| pods started | 5.1 | 10.1 |
| pod start wait, total (s) | 7.8 | 16.8 |
| pod start wait, mean (s) | 1.54 | 1.597 |
| host CPU busy, the real machine under kind (%) | 70.44 | 72.23 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.518 | 4.51 | −0.2% | −0.0149 to −0.0021 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 519.1 | 518.4 | −0.1% | −1.6912 to +0.1441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.1 | 518.4 | −0.1% | −1.6912 to +0.1441 | no |
| response time (ms), mean | 293.2 | 200.9 | −31.5% | −129.2930 to −55.2850 | yes: GAIN |
| response time (ms), 95th percentile | 785.6 | 480.5 | −38.8% | −396.3210 to −213.9640 | yes: GAIN |
| response time (ms), 99th percentile | 3041 | 2905 | −4.5% | −1158.3447 to +885.6201 | no |
| time over the response line (% of samples) | 21.32 | 16.73 | −21.5% | −6.2818 to −2.8993 | yes: GAIN |
| failed requests (%) | 12.62 | 12.92 | +2.4% | −0.1628 to +0.7626 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.9 | 24.6 | −11.8% | −4.1953 to −2.4047 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 | +50.900 (native is 0) | +38.6840 to +63.1160 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.515 | 0.325 | −36.9% | −0.6181 to +0.2381 | no |
| utilisation (used / allocatable) | 0.1044 | 0.1044 | +0.1% | −0.0011 to +0.0013 | no |
| CPU used (cores), mean | 2.504 | 2.507 | +0.1% | −0.0268 to +0.0311 | no |
| Omni's own CPU (cores), mean | 0 | 0.0462 | +0.046 (native is 0) | +0.0378 to +0.0546 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.504 | 2.553 | +1.9% | +0.0132 to +0.0836 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.1 | 304.5 | +0.8% | −4.6512 to +9.6213 | no |
| HPA replicas, mean | 9.439 | 10.66 | +12.9% | −0.1393 to +2.5747 | no |
| pods started | 5.1 | 10.1 | +98.0% | +2.4766 to +7.5234 | yes: power given |
| pod start wait, total (s) | 7.8 | 16.8 | +115.4% | +2.8282 to +15.1718 | yes: LOSS |
| pod start wait, mean (s) | 1.54 | 1.597 | +3.7% | −0.2538 to +0.3670 | no |
| host CPU busy, the real machine under kind (%) | 70.44 | 72.23 | +2.5% | +0.7123 to +2.8629 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 20.4 |  |  | 10 |
| compass | 27.0 | +32.4% | +5.2 to +8.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*