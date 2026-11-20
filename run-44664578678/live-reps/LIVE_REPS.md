# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 522.3 | 501 |
| response time (ms), 95th percentile | 2184 | 2230 |
| response time (ms), 99th percentile | 5443 | 4997 |
| time over the response line (% of samples) | 22.81 | 23.6 |
| failed requests (%) | 2.851 | 1.708 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 444.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.7 | 2.312 |
| utilisation (used / allocatable) | 0.09388 | 0.09411 |
| CPU used (cores), mean | 2.253 | 2.259 |
| Omni's own CPU (cores), mean | 0 | 0.08656 |
| CPU used with Omni's own (cores), mean | 2.253 | 2.345 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 316.2 | 314.4 |
| HPA replicas, mean | 14.95 | 16.33 |
| pods started | 5.2 | 5.4 |
| pod start wait, total (s) | 8.8 | 9.9 |
| pod start wait, mean (s) | 1.624 | 1.823 |
| host CPU busy, the real machine under kind (%) | 65.78 | 69 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 283.8 | 347.3 |
| second app: response time (ms), 99th percentile | 1890 | 1490 |
| second app: time over the response line (% of samples) | 13.35 | 14.04 |
| second app: failed requests (%) | 11.4 | 12.04 |

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
| node-hours | 1.513 | 1.514 | +0.1% | −0.0067 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.7 | +0.1% | −0.7796 to +1.1504 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.7 | +0.1% | −0.7796 to +1.1504 | no |
| response time (ms), mean | 522.3 | 501 | −4.1% | −67.9664 to +25.2884 | no |
| response time (ms), 95th percentile | 2184 | 2230 | +2.1% | −349.6999 to +441.9029 | no |
| response time (ms), 99th percentile | 5443 | 4997 | −8.2% | −1154.3952 to +262.6242 | no |
| time over the response line (% of samples) | 22.81 | 23.6 | +3.4% | −0.4736 to +2.0422 | no |
| failed requests (%) | 2.851 | 1.708 | −40.1% | −2.2941 to +0.0069 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 7.8 | −3.7% | −1.2567 to +0.6567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 444.5 | +444.500 (native is 0) | +392.9193 to +496.0807 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.7 | 2.312 | +36.0% | −0.3396 to +1.5630 | no |
| utilisation (used / allocatable) | 0.09388 | 0.09411 | +0.2% | −0.0010 to +0.0015 | no |
| CPU used (cores), mean | 2.253 | 2.259 | +0.2% | −0.0246 to +0.0352 | no |
| Omni's own CPU (cores), mean | 0 | 0.08656 | +0.087 (native is 0) | +0.0714 to +0.1017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.253 | 2.345 | +4.1% | +0.0633 to +0.1205 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 316.2 | 314.4 | −0.6% | −6.3398 to +2.7842 | no |
| HPA replicas, mean | 14.95 | 16.33 | +9.2% | +0.3697 to +2.3778 | yes: power given |
| pods started | 5.2 | 5.4 | +3.8% | −0.9583 to +1.3583 | no |
| pod start wait, total (s) | 8.8 | 9.9 | +12.5% | −1.9245 to +4.1245 | no |
| pod start wait, mean (s) | 1.624 | 1.823 | +12.3% | −0.2464 to +0.6445 | no |
| host CPU busy, the real machine under kind (%) | 65.78 | 69 | +4.9% | +2.6031 to +3.8343 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 283.8 | 347.3 | +22.4% | −28.6640 to +155.7970 | no |
| second app: response time (ms), 99th percentile | 1890 | 1490 | −21.2% | −1933.4848 to +1133.9588 | no |
| second app: time over the response line (% of samples) | 13.35 | 14.04 | +5.1% | −0.1093 to +1.4818 | no |
| second app: failed requests (%) | 11.4 | 12.04 | +5.5% | −0.0232 to +1.2888 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*