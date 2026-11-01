# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 122.9 | 78.81 |
| response time (ms), 95th percentile | 259.8 | 118.7 |
| response time (ms), 99th percentile | 369.3 | 154.4 |
| time over the response line (% of samples) | 0.3476 | 0.01227 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1867 |
| utilisation (used / allocatable) | 0.03601 | 0.04649 |
| CPU used (cores), mean | 0.8643 | 1.116 |
| Omni's own CPU (cores), mean | 0 | 0.01584 |
| CPU used with Omni's own (cores), mean | 0.8643 | 1.131 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.1 | 581 |
| HPA replicas, mean | 8.888 | 8.938 |
| pods started | 4.7 | 5.5 |
| pod start wait, total (s) | 6.2 | 8.4 |
| pod start wait, mean (s) | 1.287 | 1.477 |
| host CPU busy, the real machine under kind (%) | 27.26 | 35.02 |
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
| node-hours | 1.511 | 1.509 | −0.1% | −0.0123 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.3 | +1.3% | +1.0387 to +3.1849 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.3 | +1.3% | +1.0387 to +3.1849 | yes: power given |
| response time (ms), mean | 122.9 | 78.81 | −35.9% | −58.8826 to −29.3855 | yes: GAIN |
| response time (ms), 95th percentile | 259.8 | 118.7 | −54.3% | −176.4889 to −105.6841 | yes: GAIN |
| response time (ms), 99th percentile | 369.3 | 154.4 | −58.2% | −262.3039 to −167.5871 | yes: GAIN |
| time over the response line (% of samples) | 0.3476 | 0.01227 | −96.5% | −0.6560 to −0.0146 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +16.2960 to +43.3040 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1867 | +40.0% | −0.2134 to +0.3201 | no |
| utilisation (used / allocatable) | 0.03601 | 0.04649 | +29.1% | +0.0075 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8643 | 1.116 | +29.1% | +0.1798 to +0.3228 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01584 | +0.016 (native is 0) | +0.0117 to +0.0200 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8643 | 1.131 | +30.9% | +0.1929 to +0.3415 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.1 | 581 | −20.3% | −176.8468 to −119.2519 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.888 | 8.938 | +0.6% | −1.0949 to +1.1946 | no |
| pods started | 4.7 | 5.5 | +17.0% | −1.2176 to +2.8176 | no |
| pod start wait, total (s) | 6.2 | 8.4 | +35.5% | −1.7150 to +6.1150 | no |
| pod start wait, mean (s) | 1.287 | 1.477 | +14.8% | −0.1522 to +0.5327 | no |
| host CPU busy, the real machine under kind (%) | 27.26 | 35.02 | +28.5% | +5.9716 to +9.5463 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*