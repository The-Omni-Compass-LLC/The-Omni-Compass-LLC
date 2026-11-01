# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.173 |
| node-hours | 2.514 | 2.168 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 247.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 398.1 | 365.1 |
| response time (ms), 95th percentile | 1693 | 1787 |
| response time (ms), 99th percentile | 2431 | 2530 |
| time over the response line (% of samples) | 15.21 | 14.9 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12 | 12.67 |
| utilisation (used / allocatable) | 0.06382 | 0.07471 |
| CPU used (cores), mean | 1.532 | 1.527 |
| Omni's own CPU (cores), mean | 0 | 0.01704 |
| CPU used with Omni's own (cores), mean | 1.532 | 1.544 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 389.3 |
| HPA replicas, mean | 2.123 | 2.059 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.1 | 0.5 |
| pod start wait, mean (s) | 0.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 43.77 | 44.82 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 808.1 | 814.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.597 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.1875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 116.9 | 123.8 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 5.173 | −13.8% | −1.5793 to −0.0747 | yes: GAIN |
| node-hours | 2.514 | 2.168 | −13.8% | −0.6639 to −0.0286 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.8 | −0.0% | −1.0781 to +0.9918 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 247.9 | −9.5% | −50.2264 to −1.7682 | yes: GAIN |
| response time (ms), mean | 398.1 | 365.1 | −8.3% | −52.4432 to −13.5539 | yes: GAIN |
| response time (ms), 95th percentile | 1693 | 1787 | +5.6% | −16.4105 to +204.5225 | no |
| response time (ms), 99th percentile | 2431 | 2530 | +4.1% | −64.7084 to +263.0700 | no |
| time over the response line (% of samples) | 15.21 | 14.9 | −2.0% | −1.8924 to +1.2840 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.2 | +3.0% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +16.4010 to +37.5990 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12 | 12.66 | +5.5% | −1.0454 to +2.3754 | no |
| utilisation (used / allocatable) | 0.06382 | 0.07471 | +17.1% | +0.0011 to +0.0207 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.527 | −0.3% | −0.0348 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0.01704 | +0.017 (native is 0) | +0.0153 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.544 | +0.8% | −0.0182 to +0.0436 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 389.3 | −10.7% | −87.3367 to −5.7693 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.123 | 2.059 | −3.0% | −0.3329 to +0.2045 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 43.77 | 44.82 | +2.4% | +0.6249 to +1.4672 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 808.1 | 814.9 | +0.8% | −0.7611 to +14.3611 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.597 | −23.4% | −2.5522 to −0.2532 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.1875 | +32.4% | −0.0569 to +0.1486 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.3 | +85.7% | −0.3656 to +1.5656 | no |
| queue: job turnaround, submitted to done, mean (s) | 116.9 | 123.8 | +5.9% | −1.0564 to +14.8647 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*