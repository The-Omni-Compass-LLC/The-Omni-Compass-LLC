# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 171.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 171.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 503.9 | 470 |
| response time (ms), 95th percentile | 2042 | 2033 |
| response time (ms), 99th percentile | 5367 | 5313 |
| time over the response line (% of samples) | 23 | 22.21 |
| failed requests (%) | 2.873 | 2.401 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.588 | 1.558 |
| utilisation (used / allocatable) | 0.09446 | 0.09279 |
| CPU used (cores), mean | 2.267 | 2.227 |
| Omni's own CPU (cores), mean | 0 | 0.05613 |
| CPU used with Omni's own (cores), mean | 2.267 | 2.283 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.2 | 316.2 |
| HPA replicas, mean | 14.8 | 15.53 |
| pods started | 5.9 | 6.5 |
| pod start wait, total (s) | 9.9 | 10.8 |
| pod start wait, mean (s) | 1.66 | 1.684 |
| host CPU busy, the real machine under kind (%) | 65.6 | 66.96 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 399.6 | 453.1 |
| second app: response time (ms), 99th percentile | 1509 | 1247 |
| second app: time over the response line (% of samples) | 13.69 | 14.1 |
| second app: failed requests (%) | 11.63 | 11.45 |

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
| node-hours | 1.515 | 1.513 | −0.1% | −0.0071 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 171.3 | −0.3% | −1.2995 to +0.2053 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 171.3 | −0.3% | −1.2995 to +0.2053 | no |
| response time (ms), mean | 503.9 | 470 | −6.7% | −96.9753 to +29.1514 | no |
| response time (ms), 95th percentile | 2042 | 2033 | −0.5% | −368.5599 to +350.0469 | no |
| response time (ms), 99th percentile | 5367 | 5313 | −1.0% | −805.3996 to +697.6078 | no |
| time over the response line (% of samples) | 23 | 22.21 | −3.4% | −2.6586 to +1.0863 | no |
| failed requests (%) | 2.873 | 2.401 | −16.4% | −1.8790 to +0.9351 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8 | −8.0% | −1.7690 to +0.3690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.3 | +121.300 (native is 0) | +103.7202 to +138.8798 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.588 | 1.558 | −1.9% | −1.0614 to +1.0014 | no |
| utilisation (used / allocatable) | 0.09446 | 0.09279 | −1.8% | −0.0028 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.267 | 2.227 | −1.8% | −0.0679 to −0.0126 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05613 | +0.056 (native is 0) | +0.0477 to +0.0646 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.267 | 2.283 | +0.7% | −0.0074 to +0.0391 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.2 | 316.2 | +1.3% | −0.1551 to +8.1593 | no |
| HPA replicas, mean | 14.8 | 15.53 | +4.9% | +0.2264 to +1.2316 | yes: power given |
| pods started | 5.9 | 6.5 | +10.2% | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 9.9 | 10.8 | +9.1% | −1.5187 to +3.3187 | no |
| pod start wait, mean (s) | 1.66 | 1.684 | +1.4% | −0.2886 to +0.3367 | no |
| host CPU busy, the real machine under kind (%) | 65.6 | 66.96 | +2.1% | +0.5208 to +2.1979 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 399.6 | 453.1 | +13.4% | +9.0338 to +97.9922 | yes: LOSS |
| second app: response time (ms), 99th percentile | 1509 | 1247 | −17.4% | −660.1954 to +135.6414 | no |
| second app: time over the response line (% of samples) | 13.69 | 14.1 | +3.0% | −0.6612 to +1.4771 | no |
| second app: failed requests (%) | 11.63 | 11.45 | −1.6% | −0.7127 to +0.3510 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*