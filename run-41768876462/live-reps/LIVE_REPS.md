# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.993 |
| node-hours | 2.514 | 2.089 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 243.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 597.5 | 548.3 |
| response time (ms), 95th percentile | 3396 | 3331 |
| response time (ms), 99th percentile | 4407 | 4335 |
| time over the response line (% of samples) | 18.24 | 18.65 |
| failed requests (%) | 0 | 0.01093 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 207.9 | 213.3 |
| utilisation (used / allocatable) | 0.06896 | 0.08195 |
| CPU used (cores), mean | 1.655 | 1.627 |
| Omni's own CPU (cores), mean | 0 | 0.0853 |
| CPU used with Omni's own (cores), mean | 1.655 | 1.712 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.4 | 359.7 |
| HPA replicas, mean | 2.314 | 2.427 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 47.32 | 50.13 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 651.3 | 669.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.237 |
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
| worker nodes in service, mean | 6 | 4.993 | −16.8% | −1.5188 to −0.4957 | yes: GAIN |
| node-hours | 2.514 | 2.089 | −16.9% | −0.6395 to −0.2105 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.2 | −0.2% | −1.2744 to +0.3063 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 243.7 | −11.6% | −48.3221 to −15.8001 | yes: GAIN |
| response time (ms), mean | 597.5 | 548.3 | −8.2% | −59.9651 to −38.4242 | yes: GAIN |
| response time (ms), 95th percentile | 3396 | 3331 | −1.9% | −125.8339 to −4.6901 | yes: GAIN |
| response time (ms), 99th percentile | 4407 | 4335 | −1.7% | −194.4160 to +48.9120 | no |
| time over the response line (% of samples) | 18.24 | 18.65 | +2.3% | −0.1083 to +0.9347 | no |
| failed requests (%) | 0 | 0.01093 | +0.011 (native is 0) | −0.0138 to +0.0357 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 11.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.7 | +10.700 (native is 0) | +8.2673 to +13.1327 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 207.9 | 213.3 | +2.6% | −0.8528 to +11.6062 | no |
| utilisation (used / allocatable) | 0.06896 | 0.08195 | +18.8% | +0.0062 to +0.0198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.655 | 1.627 | −1.7% | −0.0534 to −0.0027 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0853 | +0.085 (native is 0) | +0.0762 to +0.0944 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.655 | 1.712 | +3.5% | +0.0287 to +0.0857 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.4 | 359.7 | −10.6% | −67.8690 to −17.6725 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.314 | 2.427 | +4.9% | −0.3499 to +0.5753 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 47.32 | 50.13 | +5.9% | +2.5065 to +3.1026 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 651.3 | 669.1 | +2.7% | +13.5374 to +22.0626 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.237 | −29.4% | −2.5981 to −0.9277 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*