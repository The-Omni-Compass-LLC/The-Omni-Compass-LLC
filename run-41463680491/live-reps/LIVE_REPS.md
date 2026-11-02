# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 487.1 | 486.3 |
| response time (ms), 95th percentile | 2162 | 2178 |
| response time (ms), 99th percentile | 4885 | 5305 |
| time over the response line (% of samples) | 21.52 | 22.24 |
| failed requests (%) | 2.138 | 1.371 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 132.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.207 | 1.607 |
| utilisation (used / allocatable) | 0.09373 | 0.09269 |
| CPU used (cores), mean | 2.25 | 2.225 |
| Omni's own CPU (cores), mean | 0 | 0.05499 |
| CPU used with Omni's own (cores), mean | 2.25 | 2.28 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 310.4 | 313.9 |
| HPA replicas, mean | 14.98 | 15.55 |
| pods started | 5.6 | 5.5 |
| pod start wait, total (s) | 9 | 9.4 |
| pod start wait, mean (s) | 1.584 | 1.705 |
| host CPU busy, the real machine under kind (%) | 65.1 | 66.57 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 290.5 | 285.1 |
| second app: response time (ms), 99th percentile | 2576 | 2154 |
| second app: time over the response line (% of samples) | 13.5 | 13.53 |
| second app: failed requests (%) | 10.97 | 11.43 |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0025 to +0.0092 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.6 | +0.1% | −0.7383 to +0.9556 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.6 | +0.1% | −0.7383 to +0.9556 | no |
| response time (ms), mean | 487.1 | 486.3 | −0.2% | −22.8882 to +21.1994 | no |
| response time (ms), 95th percentile | 2162 | 2178 | +0.7% | −281.7511 to +313.4661 | no |
| response time (ms), 99th percentile | 4885 | 5305 | +8.6% | −480.5287 to +1319.7011 | no |
| time over the response line (% of samples) | 21.52 | 22.24 | +3.3% | −0.7122 to +2.1386 | no |
| failed requests (%) | 2.138 | 1.371 | −35.9% | −1.5494 to +0.0160 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 7.9 | −3.7% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 132.5 | +132.500 (native is 0) | +118.2846 to +146.7154 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.207 | 1.607 | +33.1% | −0.0547 to +0.8547 | no |
| utilisation (used / allocatable) | 0.09373 | 0.09269 | −1.1% | −0.0026 to +0.0005 | no |
| CPU used (cores), mean | 2.25 | 2.225 | −1.1% | −0.0616 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.05499 | +0.055 (native is 0) | +0.0485 to +0.0615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.25 | 2.28 | +1.3% | −0.0066 to +0.0668 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 310.4 | 313.9 | +1.2% | −2.1587 to +9.3206 | no |
| HPA replicas, mean | 14.98 | 15.55 | +3.8% | −0.1115 to +1.2466 | no |
| pods started | 5.6 | 5.5 | −1.8% | −1.3818 to +1.1818 | no |
| pod start wait, total (s) | 9 | 9.4 | +4.4% | −2.8378 to +3.6378 | no |
| pod start wait, mean (s) | 1.584 | 1.705 | +7.6% | −0.1271 to +0.3680 | no |
| host CPU busy, the real machine under kind (%) | 65.1 | 66.57 | +2.3% | +0.6223 to +2.3154 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 290.5 | 285.1 | −1.9% | −42.8931 to +32.1111 | no |
| second app: response time (ms), 99th percentile | 2576 | 2154 | −16.4% | −1373.8943 to +529.9735 | no |
| second app: time over the response line (% of samples) | 13.5 | 13.53 | +0.2% | −0.5755 to +0.6409 | no |
| second app: failed requests (%) | 10.97 | 11.43 | +4.2% | −0.0417 to +0.9596 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*