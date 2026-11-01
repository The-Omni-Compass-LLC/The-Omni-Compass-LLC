# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.51 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.4 | 172.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.4 | 172.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 574 | 473.7 |
| response time (ms), 95th percentile | 2409 | 2071 |
| response time (ms), 99th percentile | 5742 | 5407 |
| time over the response line (% of samples) | 26.18 | 23.5 |
| failed requests (%) | 3.324 | 3.402 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.3 | 1.925 |
| utilisation (used / allocatable) | 0.09942 | 0.09795 |
| CPU used (cores), mean | 2.386 | 2.351 |
| Omni's own CPU (cores), mean | 0 | 0.01328 |
| CPU used with Omni's own (cores), mean | 2.386 | 2.364 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.1 | 299.6 |
| HPA replicas, mean | 15 | 15.23 |
| pods started | 5.5 | 5 |
| pod start wait, total (s) | 8.1 | 9.1 |
| pod start wait, mean (s) | 1.46 | 1.826 |
| host CPU busy, the real machine under kind (%) | 69.34 | 68.88 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 265.4 | 278.8 |
| second app: response time (ms), 99th percentile | 982.8 | 1209 |
| second app: time over the response line (% of samples) | 14.97 | 14.96 |
| second app: failed requests (%) | 13.68 | 13.38 |

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
| node-hours | 1.51 | 1.514 | +0.3% | −0.0037 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.4 | 172.6 | +0.1% | −0.7062 to +1.1072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.4 | 172.6 | +0.1% | −0.7062 to +1.1072 | no |
| response time (ms), mean | 574 | 473.7 | −17.5% | −151.2954 to −49.3619 | yes: GAIN |
| response time (ms), 95th percentile | 2409 | 2071 | −14.0% | −662.5900 to −13.7660 | yes: GAIN |
| response time (ms), 99th percentile | 5742 | 5407 | −5.8% | −1131.0448 to +461.2398 | no |
| time over the response line (% of samples) | 26.18 | 23.5 | −10.2% | −4.0056 to −1.3431 | yes: GAIN |
| failed requests (%) | 3.324 | 3.402 | +2.4% | −0.5942 to +0.7513 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.6 | −4.4% | −1.0032 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 | +42.000 (native is 0) | +32.5765 to +51.4235 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.3 | 1.925 | +48.1% | −0.0121 to +1.2621 | no |
| utilisation (used / allocatable) | 0.09942 | 0.09795 | −1.5% | −0.0024 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.386 | 2.351 | −1.5% | −0.0588 to −0.0118 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01328 | +0.013 (native is 0) | +0.0123 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.386 | 2.364 | −0.9% | −0.0456 to +0.0016 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.1 | 299.6 | +1.5% | +0.1709 to +8.9112 | yes, up (shown, not judged) |
| HPA replicas, mean | 15 | 15.23 | +1.5% | −0.1808 to +0.6378 | no |
| pods started | 5.5 | 5 | −9.1% | −1.7274 to +0.7274 | no |
| pod start wait, total (s) | 8.1 | 9.1 | +12.3% | −1.9589 to +3.9589 | no |
| pod start wait, mean (s) | 1.46 | 1.826 | +25.1% | +0.0783 to +0.6541 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 69.34 | 68.88 | −0.7% | −0.9474 to +0.0298 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 265.4 | 278.8 | +5.0% | −6.6248 to +33.3178 | no |
| second app: response time (ms), 99th percentile | 982.8 | 1209 | +23.0% | −339.0470 to +790.9484 | no |
| second app: time over the response line (% of samples) | 14.97 | 14.96 | −0.0% | −0.5056 to +0.4939 | no |
| second app: failed requests (%) | 13.68 | 13.38 | −2.2% | −0.8255 to +0.2200 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*