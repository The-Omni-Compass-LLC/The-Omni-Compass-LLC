# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.512 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.9 | 159.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.9 | 159.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 168.3 | 84.99 | 88.41 |
| response time (ms), 95th percentile | 365.6 | 128.5 | 127.7 |
| response time (ms), 99th percentile | 608.7 | 182.7 | 170.3 |
| time over the response line (% of samples) | 2.403 | 0.03644 | 0.3019 |
| failed requests (%) | 0 | 0 | 0.09892 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.8 | 24.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | 42.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.3983 | 0 |
| utilisation (used / allocatable) | 0.04126 | 0.03909 | 0.04021 |
| CPU used (cores), mean | 0.9902 | 0.9381 | 0.9651 |
| Omni's own CPU (cores), mean | 0 | 0.03989 | 0.04024 |
| CPU used with Omni's own (cores), mean | 0.9902 | 0.978 | 1.005 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.9 | 683.9 | 669.1 |
| HPA replicas, mean | 8.765 | 9.444 | 9.579 |
| pods started | 5.3 | 3.8 | 9.6 |
| pod start wait, total (s) | 8.1 | 5.2 | 17.2 |
| pod start wait, mean (s) | 1.527 | 1.35 | 1.802 |
| host CPU busy, the real machine under kind (%) | 30.12 | 30.39 | 31.18 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.512 | +0.1% | +0.0003 to +0.0040 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.9 | −0.2% | −0.5886 to +0.0122 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.9 | −0.2% | −0.5886 to +0.0122 | no |
| response time (ms), mean | 168.3 | 84.99 | −49.5% | −100.3999 to −66.1627 | yes: GAIN |
| response time (ms), 95th percentile | 365.6 | 128.5 | −64.8% | −286.4862 to −187.6358 | yes: GAIN |
| response time (ms), 99th percentile | 608.7 | 182.7 | −70.0% | −542.7148 to −309.2766 | yes: GAIN |
| time over the response line (% of samples) | 2.403 | 0.03644 | −98.5% | −3.5838 to −1.1501 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.6509 to −0.9491 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.8 | +20.800 (native is 0) | +18.2587 to +23.3413 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.3983 | +149.0% | −0.1285 to +0.6052 | no |
| utilisation (used / allocatable) | 0.04126 | 0.03909 | −5.3% | −0.0033 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9902 | 0.9381 | −5.3% | −0.0781 to −0.0261 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03989 | +0.040 (native is 0) | +0.0363 to +0.0434 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9902 | 0.978 | −1.2% | −0.0356 to +0.0112 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.9 | 683.9 | +4.4% | +16.3773 to +41.7024 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.765 | 9.444 | +7.7% | +0.0872 to +1.2706 | yes: power given |
| pods started | 5.3 | 3.8 | −28.3% | −2.5256 to −0.4744 | yes: GAIN |
| pod start wait, total (s) | 8.1 | 5.2 | −35.8% | −4.6011 to −1.1989 | yes: GAIN |
| pod start wait, mean (s) | 1.527 | 1.35 | −11.6% | −0.5030 to +0.1497 | no |
| host CPU busy, the real machine under kind (%) | 30.12 | 30.39 | +0.9% | −0.1269 to +0.6758 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.519 | +0.6% | +0.0077 to +0.0107 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.9 | +0.4% | +0.4404 to +0.8946 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.9 | +0.4% | +0.4404 to +0.8946 | yes: power given |
| response time (ms), mean | 168.3 | 88.41 | −47.5% | −98.1702 to −61.5509 | yes: GAIN |
| response time (ms), 95th percentile | 365.6 | 127.7 | −65.1% | −289.2267 to −186.5393 | yes: GAIN |
| response time (ms), 99th percentile | 608.7 | 170.3 | −72.0% | −561.3126 to −315.3824 | yes: GAIN |
| time over the response line (% of samples) | 2.403 | 0.3019 | −87.4% | −3.4291 to −0.7738 | yes: GAIN |
| failed requests (%) | 0 | 0.09892 | +0.099 (native is 0) | +0.0289 to +0.1689 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0.4 | −82.6% | −3.6011 to −0.1989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.5 | +24.500 (native is 0) | +20.3530 to +28.6470 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0 | −100.0% | −0.3443 to +0.0243 | no |
| utilisation (used / allocatable) | 0.04126 | 0.04021 | −2.5% | −0.0017 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9902 | 0.9651 | −2.5% | −0.0413 to −0.0089 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04024 | +0.040 (native is 0) | +0.0373 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9902 | 1.005 | +1.5% | −0.0004 to +0.0307 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.9 | 669.1 | +2.2% | +6.2123 to +22.2117 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.765 | 9.579 | +9.3% | +0.7417 to +0.8854 | yes: power given |
| pods started | 5.3 | 9.6 | +81.1% | +3.8172 to +4.7828 | yes: power given |
| pod start wait, total (s) | 8.1 | 17.2 | +112.3% | +6.0755 to +12.1245 | yes: LOSS |
| pod start wait, mean (s) | 1.527 | 1.802 | +18.0% | −0.0751 to +0.6260 | no |
| host CPU busy, the real machine under kind (%) | 30.12 | 31.18 | +3.5% | +0.6817 to +1.4432 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.519 | +0.5% | +0.0061 to +0.0079 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.9 | +0.6% | +0.7445 to +1.1669 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.9 | +0.6% | +0.7445 to +1.1669 | yes: power given |
| response time (ms), mean | 84.99 | 88.41 | +4.0% | +0.6883 to +6.1532 | yes: LOSS |
| response time (ms), 95th percentile | 128.5 | 127.7 | −0.6% | −3.5305 to +1.8865 | no |
| response time (ms), 99th percentile | 182.7 | 170.3 | −6.8% | −26.8984 to +2.1948 | no |
| time over the response line (% of samples) | 0.03644 | 0.3019 | +728.6% | +0.1349 to +0.3961 | yes: LOSS |
| failed requests (%) | 0 | 0.09892 | +0.099 (native is 0) | +0.0289 to +0.1689 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 20.8 | 24.5 | +17.8% | −0.9972 to +8.3972 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 51.43 | −35.7% | −116.5450 to +59.4021 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0 | −100.0% | −0.6640 to −0.1326 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03909 | 0.04021 | +2.9% | +0.0004 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9381 | 0.9651 | +2.9% | +0.0089 to +0.0451 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03989 | 0.04024 | +0.9% | −0.0005 to +0.0012 | no |
| CPU used with Omni's own (cores), mean | 0.978 | 1.005 | +2.8% | +0.0097 to +0.0450 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.9 | 669.1 | −2.2% | −24.6295 to −5.0261 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.444 | 9.579 | +1.4% | −0.4131 to +0.6824 | no |
| pods started | 3.8 | 9.6 | +152.6% | +5.0612 to +6.5388 | yes: power given |
| pod start wait, total (s) | 5.2 | 17.2 | +230.8% | +8.3526 to +15.6474 | yes: LOSS |
| pod start wait, mean (s) | 1.35 | 1.802 | +33.5% | +0.0200 to +0.8842 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.39 | 31.18 | +2.6% | +0.4286 to +1.1474 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*