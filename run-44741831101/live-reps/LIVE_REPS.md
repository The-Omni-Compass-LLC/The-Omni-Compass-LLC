# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.513 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.2 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.2 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 144.2 | 76.71 | 81.63 |
| response time (ms), 95th percentile | 327.6 | 114.4 | 114.9 |
| response time (ms), 99th percentile | 526.4 | 155.5 | 154.3 |
| time over the response line (% of samples) | 2.154 | 0 | 0.2192 |
| failed requests (%) | 0 | 0 | 0.07454 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | 29.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 57.14 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.16 | 0.07833 |
| utilisation (used / allocatable) | 0.03736 | 0.03577 | 0.03664 |
| CPU used (cores), mean | 0.8966 | 0.8586 | 0.8792 |
| Omni's own CPU (cores), mean | 0 | 0.03642 | 0.03743 |
| CPU used with Omni's own (cores), mean | 0.8966 | 0.895 | 0.9167 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.3 | 787.1 | 774.6 |
| HPA replicas, mean | 8.243 | 8.391 | 9.189 |
| pods started | 5.4 | 4.1 | 10.7 |
| pod start wait, total (s) | 8.2 | 6.4 | 18.3 |
| pod start wait, mean (s) | 1.537 | 1.587 | 1.76 |
| host CPU busy, the real machine under kind (%) | 27.68 | 28.04 | 28.8 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.1% | −0.0067 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.2 | −0.3% | −0.9883 to +0.0349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.2 | −0.3% | −0.9883 to +0.0349 | no |
| response time (ms), mean | 144.2 | 76.71 | −46.8% | −93.3875 to −41.6112 | yes: GAIN |
| response time (ms), 95th percentile | 327.6 | 114.4 | −65.1% | −289.4295 to −136.9405 | yes: GAIN |
| response time (ms), 99th percentile | 526.4 | 155.5 | −70.5% | −504.0595 to −237.9009 | yes: GAIN |
| time over the response line (% of samples) | 2.154 | 0 | −100.0% | −3.6686 to −0.6402 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.9128 to −0.4872 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.700 (native is 0) | +16.7615 to +20.6385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.16 | −50.5% | −0.4037 to +0.0770 | no |
| utilisation (used / allocatable) | 0.03736 | 0.03577 | −4.2% | −0.0029 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8966 | 0.8586 | −4.2% | −0.0707 to −0.0054 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03642 | +0.036 (native is 0) | +0.0306 to +0.0423 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8966 | 0.895 | −0.2% | −0.0290 to +0.0258 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.3 | 787.1 | +2.0% | −5.1592 to +36.7344 | no |
| HPA replicas, mean | 8.243 | 8.391 | +1.8% | −0.4083 to +0.7030 | no |
| pods started | 5.4 | 4.1 | −24.1% | −2.3144 to −0.2856 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 6.4 | −22.0% | −3.8732 to +0.2732 | no |
| pod start wait, mean (s) | 1.537 | 1.587 | +3.3% | −0.2706 to +0.3706 | no |
| host CPU busy, the real machine under kind (%) | 27.68 | 28.04 | +1.3% | −0.1363 to +0.8550 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0053 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.8 | +0.1% | −0.5720 to +0.8032 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.8 | +0.1% | −0.5720 to +0.8032 | no |
| response time (ms), mean | 144.2 | 81.63 | −43.4% | −86.6076 to −38.5345 | yes: GAIN |
| response time (ms), 95th percentile | 327.6 | 114.9 | −64.9% | −290.4170 to −134.9140 | yes: GAIN |
| response time (ms), 99th percentile | 526.4 | 154.3 | −70.7% | −511.6148 to −232.6168 | yes: GAIN |
| time over the response line (% of samples) | 2.154 | 0.2192 | −89.8% | −3.4181 to −0.4523 | yes: GAIN |
| failed requests (%) | 0 | 0.07454 | +0.075 (native is 0) | +0.0122 to +0.1368 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0.3 | −86.4% | −3.7299 to −0.0701 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +22.8802 to +36.5198 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.07833 | −75.8% | −0.5698 to +0.0798 | no |
| utilisation (used / allocatable) | 0.03736 | 0.03664 | −1.9% | −0.0016 to +0.0002 | no |
| CPU used (cores), mean | 0.8966 | 0.8792 | −1.9% | −0.0385 to +0.0038 | no |
| Omni's own CPU (cores), mean | 0 | 0.03743 | +0.037 (native is 0) | +0.0324 to +0.0424 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8966 | 0.9167 | +2.2% | +0.0030 to +0.0372 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.3 | 774.6 | +0.4% | −15.6603 to +22.2499 | no |
| HPA replicas, mean | 8.243 | 9.189 | +11.5% | +0.8008 to +1.0910 | yes: power given |
| pods started | 5.4 | 10.7 | +98.1% | +3.9076 to +6.6924 | yes: power given |
| pod start wait, total (s) | 8.2 | 18.3 | +123.2% | +7.8018 to +12.3982 | yes: LOSS |
| pod start wait, mean (s) | 1.537 | 1.76 | +14.5% | −0.0273 to +0.4740 | no |
| host CPU busy, the real machine under kind (%) | 27.68 | 28.8 | +4.1% | +0.7114 to +1.5410 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0021 to +0.0088 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.8 | +0.4% | −0.0584 to +1.2429 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.8 | +0.4% | −0.0584 to +1.2429 | no |
| response time (ms), mean | 76.71 | 81.63 | +6.4% | +2.4204 to +7.4361 | yes: LOSS |
| response time (ms), 95th percentile | 114.4 | 114.9 | +0.5% | −2.4080 to +3.4470 | no |
| response time (ms), 99th percentile | 155.5 | 154.3 | −0.7% | −13.1716 to +10.9004 | no |
| time over the response line (% of samples) | 0 | 0.2192 | +0.219 (native is 0) | +0.1287 to +0.3097 | yes: LOSS |
| failed requests (%) | 0 | 0.07454 | +0.075 (native is 0) | +0.0122 to +0.1368 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 29.7 | +58.8% | +3.1064 to +18.8936 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 57.14 | −42.9% | −92.2940 to +6.5797 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.07833 | −51.0% | −0.2993 to +0.1360 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03664 | +2.4% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8586 | 0.8792 | +2.4% | +0.0025 to +0.0389 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03642 | 0.03743 | +2.8% | −0.0002 to +0.0022 | no |
| CPU used with Omni's own (cores), mean | 0.895 | 0.9167 | +2.4% | +0.0036 to +0.0398 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.1 | 774.6 | −1.6% | −21.9129 to −3.0727 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.391 | 9.189 | +9.5% | +0.1299 to +1.4673 | yes: power given |
| pods started | 4.1 | 10.7 | +161.0% | +5.0845 to +8.1155 | yes: power given |
| pod start wait, total (s) | 6.4 | 18.3 | +185.9% | +9.3001 to +14.4999 | yes: LOSS |
| pod start wait, mean (s) | 1.587 | 1.76 | +10.9% | −0.2479 to +0.5946 | no |
| host CPU busy, the real machine under kind (%) | 28.04 | 28.8 | +2.7% | +0.3100 to +1.2237 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*