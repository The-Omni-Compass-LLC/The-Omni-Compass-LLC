# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 208.9 | 112.9 |
| response time (ms), 95th percentile | 492.7 | 304.7 |
| response time (ms), 99th percentile | 656.9 | 567 |
| time over the response line (% of samples) | 5.854 | 1.632 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 2.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.055 |
| utilisation (used / allocatable) | 0.03055 | 0.04381 |
| CPU used (cores), mean | 0.7333 | 1.051 |
| Omni's own CPU (cores), mean | 0 | 0.06491 |
| CPU used with Omni's own (cores), mean | 0.7333 | 1.116 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 610.9 |
| HPA replicas, mean | 2.912 | 2.698 |
| pods started | 3 | 2.7 |
| pod start wait, total (s) | 4.1 | 3.9 |
| pod start wait, mean (s) | 1.375 | 1.433 |
| host CPU busy, the real machine under kind (%) | 24.07 | 35.34 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.519 | +0.4% | −0.0047 to +0.0171 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 161 | +2.4% | +2.2810 to +5.1133 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 161 | +2.4% | +2.2810 to +5.1133 | yes: power given |
| response time (ms), mean | 208.9 | 112.9 | −46.0% | −118.8287 to −73.1901 | yes: GAIN |
| response time (ms), 95th percentile | 492.7 | 304.7 | −38.2% | −240.1348 to −135.7902 | yes: GAIN |
| response time (ms), 99th percentile | 656.9 | 567 | −13.7% | −157.2671 to −22.5113 | yes: GAIN |
| time over the response line (% of samples) | 5.854 | 1.632 | −72.1% | −6.6815 to −1.7637 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 2.2 | −55.1% | −4.8340 to −0.5660 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.9 | +99.900 (native is 0) | +78.3920 to +121.4080 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.055 | −76.9% | −0.3835 to +0.0168 | no |
| utilisation (used / allocatable) | 0.03055 | 0.04381 | +43.4% | +0.0108 to +0.0157 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7333 | 1.051 | +43.4% | +0.2588 to +0.3775 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06491 | +0.065 (native is 0) | +0.0547 to +0.0751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7333 | 1.116 | +52.2% | +0.3184 to +0.4477 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 610.9 | −28.5% | −273.4693 to −213.4335 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.912 | 2.698 | −7.3% | −0.4793 to +0.0512 | no |
| pods started | 3 | 2.7 | −10.0% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 4.1 | 3.9 | −4.9% | −1.2003 to +0.8003 | no |
| pod start wait, mean (s) | 1.375 | 1.433 | +4.2% | −0.1835 to +0.3001 | no |
| host CPU busy, the real machine under kind (%) | 24.07 | 35.34 | +46.8% | +9.6159 to +12.9308 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*