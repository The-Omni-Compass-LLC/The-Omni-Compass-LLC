# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.3 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.3 | 160.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 116 | 84.76 | 73.76 |
| response time (ms), 95th percentile | 247.4 | 149.5 | 109.3 |
| response time (ms), 99th percentile | 359 | 259.3 | 135.4 |
| time over the response line (% of samples) | 0.2941 | 0.1858 | 0.02439 |
| failed requests (%) | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 367 | 23.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2117 | 0.08 | 0.1867 |
| utilisation (used / allocatable) | 0.03589 | 0.04441 | 0.04517 |
| CPU used (cores), mean | 0.8615 | 1.066 | 1.084 |
| Omni's own CPU (cores), mean | 0 | 0.09959 | 0.01392 |
| CPU used with Omni's own (cores), mean | 0.8615 | 1.166 | 1.098 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 602.4 | 595.1 |
| HPA replicas, mean | 8.851 | 10.46 | 8.762 |
| pods started | 5 | 7.8 | 5.1 |
| pod start wait, total (s) | 8.2 | 12.2 | 7.6 |
| pod start wait, mean (s) | 1.643 | 1.56 | 1.429 |
| host CPU busy, the real machine under kind (%) | 27.49 | 36.49 | 34.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.513 | +0.2% | −0.0046 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.3 | +1.4% | +1.7320 to +2.6277 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.3 | +1.4% | +1.7320 to +2.6277 | yes: power given |
| response time (ms), mean | 116 | 84.76 | −26.9% | −40.8129 to −21.7069 | yes: GAIN |
| response time (ms), 95th percentile | 247.4 | 149.5 | −39.6% | −117.8844 to −78.0366 | yes: GAIN |
| response time (ms), 99th percentile | 359 | 259.3 | −27.8% | −138.0986 to −61.2646 | yes: GAIN |
| time over the response line (% of samples) | 0.2941 | 0.1858 | −36.8% | −0.3143 to +0.0978 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 367 | +367.000 (native is 0) | +228.2390 to +505.7610 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2117 | 0.08 | −62.2% | −0.3722 to +0.1089 | no |
| utilisation (used / allocatable) | 0.03589 | 0.04441 | +23.7% | +0.0061 to +0.0110 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8615 | 1.066 | +23.7% | +0.1455 to +0.2634 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.09959 | +0.100 (native is 0) | +0.0673 to +0.1319 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8615 | 1.166 | +35.3% | +0.2160 to +0.3922 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 602.4 | −17.5% | −155.2622 to −100.5599 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.851 | 10.46 | +18.2% | +0.5069 to +2.7114 | yes: power given |
| pods started | 5 | 7.8 | +56.0% | +1.2256 to +4.3744 | yes: power given |
| pod start wait, total (s) | 8.2 | 12.2 | +48.8% | +0.4634 to +7.5366 | yes: LOSS |
| pod start wait, mean (s) | 1.643 | 1.56 | −5.1% | −0.4650 to +0.2975 | no |
| host CPU busy, the real machine under kind (%) | 27.49 | 36.49 | +32.8% | +6.2980 to +11.7082 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.514 | +0.2% | −0.0053 to +0.0127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.5 | +1.6% | +1.4942 to +3.4278 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.5 | +1.6% | +1.4942 to +3.4278 | yes: power given |
| response time (ms), mean | 116 | 73.76 | −36.4% | −55.4671 to −29.0671 | yes: GAIN |
| response time (ms), 95th percentile | 247.4 | 109.3 | −55.8% | −163.8492 to −112.3608 | yes: GAIN |
| response time (ms), 99th percentile | 359 | 135.4 | −62.3% | −259.9637 to −187.2019 | yes: GAIN |
| time over the response line (% of samples) | 0.2941 | 0.02439 | −91.7% | −0.5360 to −0.0034 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.3 | +23.300 (native is 0) | +15.4784 to +31.1216 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2117 | 0.1867 | −11.8% | −0.3654 to +0.3154 | no |
| utilisation (used / allocatable) | 0.03589 | 0.04517 | +25.8% | +0.0062 to +0.0124 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8615 | 1.084 | +25.8% | +0.1478 to +0.2975 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01392 | +0.014 (native is 0) | +0.0106 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8615 | 1.098 | +27.5% | +0.1593 to +0.3138 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 595.1 | −18.5% | −169.6270 to −100.8081 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.851 | 8.762 | −1.0% | −1.1385 to +0.9604 | no |
| pods started | 5 | 5.1 | +2.0% | −1.4249 to +1.6249 | no |
| pod start wait, total (s) | 8.2 | 7.6 | −7.3% | −3.4850 to +2.2850 | no |
| pod start wait, mean (s) | 1.643 | 1.429 | −13.0% | −0.4911 to +0.0625 | no |
| host CPU busy, the real machine under kind (%) | 27.49 | 34.22 | +24.5% | +4.6187 to +8.8446 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0048 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 160.5 | +0.2% | −0.4469 to +1.0092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 160.5 | +0.2% | −0.4469 to +1.0092 | no |
| response time (ms), mean | 84.76 | 73.76 | −13.0% | −16.7782 to −5.2361 | yes: GAIN |
| response time (ms), 95th percentile | 149.5 | 109.3 | −26.9% | −63.7058 to −16.5832 | yes: GAIN |
| response time (ms), 99th percentile | 259.3 | 135.4 | −47.8% | −169.8505 to −77.9519 | yes: GAIN |
| time over the response line (% of samples) | 0.1858 | 0.02439 | −86.9% | −0.3670 to +0.0442 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 367 | 23.3 | −93.7% | −475.6324 to −211.7676 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1867 | +133.3% | −0.1661 to +0.3794 | no |
| utilisation (used / allocatable) | 0.04441 | 0.04517 | +1.7% | −0.0001 to +0.0016 | no |
| CPU used (cores), mean | 1.066 | 1.084 | +1.7% | −0.0025 to +0.0389 | no |
| Omni's own CPU (cores), mean | 0.09959 | 0.01392 | −86.0% | −0.1149 to −0.0564 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.166 | 1.098 | −5.8% | −0.0915 to −0.0434 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 602.4 | 595.1 | −1.2% | −16.9557 to +2.3425 | no |
| HPA replicas, mean | 10.46 | 8.762 | −16.2% | −2.5820 to −0.8144 | yes: GAIN |
| pods started | 7.8 | 5.1 | −34.6% | −4.1326 to −1.2674 | yes: GAIN |
| pod start wait, total (s) | 12.2 | 7.6 | −37.7% | −7.9244 to −1.2756 | yes: GAIN |
| pod start wait, mean (s) | 1.56 | 1.429 | −8.4% | −0.4784 to +0.2173 | no |
| host CPU busy, the real machine under kind (%) | 36.49 | 34.22 | −6.2% | −3.1736 to −1.3694 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*