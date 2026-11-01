# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.5 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.5 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 151.5 | 78.57 | 78.28 |
| response time (ms), 95th percentile | 343.5 | 116.6 | 114.2 |
| response time (ms), 99th percentile | 579.9 | 165.2 | 153.6 |
| time over the response line (% of samples) | 2.481 | 0.08522 | 0.1589 |
| failed requests (%) | 0 | 0 | 0.09877 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | 17.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.275 | 0.7 |
| utilisation (used / allocatable) | 0.03861 | 0.03654 | 0.03704 |
| CPU used (cores), mean | 0.9266 | 0.877 | 0.8888 |
| Omni's own CPU (cores), mean | 0 | 0.00922 | 0.00869 |
| CPU used with Omni's own (cores), mean | 0.9266 | 0.8862 | 0.8975 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.9 | 785 | 777.3 |
| HPA replicas, mean | 8.33 | 8.051 | 9.608 |
| pods started | 4.9 | 4.2 | 9 |
| pod start wait, total (s) | 7.4 | 6.2 | 15.4 |
| pod start wait, mean (s) | 1.525 | 1.423 | 1.711 |
| host CPU busy, the real machine under kind (%) | 28.05 | 27.31 | 27.69 |
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
| node-hours | 1.512 | 1.513 | +0.0% | −0.0019 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.5 | −0.2% | −0.7607 to +0.0697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.5 | −0.2% | −0.7607 to +0.0697 | no |
| response time (ms), mean | 151.5 | 78.57 | −48.1% | −101.4449 to −44.4644 | yes: GAIN |
| response time (ms), 95th percentile | 343.5 | 116.6 | −66.0% | −307.3553 to −146.4267 | yes: GAIN |
| response time (ms), 99th percentile | 579.9 | 165.2 | −71.5% | −567.5759 to −261.8443 | yes: GAIN |
| time over the response line (% of samples) | 2.481 | 0.08522 | −96.6% | −3.8414 to −0.9494 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0.1 | −96.3% | −4.2242 to −0.9758 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.600 (native is 0) | +10.9097 to +28.2903 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.275 | −45.2% | −0.7087 to +0.2554 | no |
| utilisation (used / allocatable) | 0.03861 | 0.03654 | −5.4% | −0.0032 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9266 | 0.877 | −5.4% | −0.0770 to −0.0223 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00922 | +0.009 (native is 0) | +0.0071 to +0.0113 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9266 | 0.8862 | −4.4% | −0.0664 to −0.0145 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.9 | 785 | +4.3% | +17.8470 to +46.2174 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.33 | 8.051 | −3.4% | −1.3462 to +0.7877 | no |
| pods started | 4.9 | 4.2 | −14.3% | −2.3537 to +0.9537 | no |
| pod start wait, total (s) | 7.4 | 6.2 | −16.2% | −5.0858 to +2.6858 | no |
| pod start wait, mean (s) | 1.525 | 1.423 | −6.7% | −0.6285 to +0.4252 | no |
| host CPU busy, the real machine under kind (%) | 28.05 | 27.31 | −2.6% | −1.3446 to −0.1395 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0033 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.0% | −0.7164 to +0.6302 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.0% | −0.7164 to +0.6302 | no |
| response time (ms), mean | 151.5 | 78.28 | −48.3% | −102.3877 to −44.0867 | yes: GAIN |
| response time (ms), 95th percentile | 343.5 | 114.2 | −66.7% | −310.8741 to −147.7169 | yes: GAIN |
| response time (ms), 99th percentile | 579.9 | 153.6 | −73.5% | −583.0144 to −269.7156 | yes: GAIN |
| time over the response line (% of samples) | 2.481 | 0.1589 | −93.6% | −3.7985 to −0.8447 | yes: GAIN |
| failed requests (%) | 0 | 0.09877 | +0.099 (native is 0) | +0.0288 to +0.1687 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0.1 | −96.3% | −4.3260 to −0.8740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.200 (native is 0) | +14.7267 to +19.6733 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.7 | +39.5% | −0.3849 to +0.7816 | no |
| utilisation (used / allocatable) | 0.03861 | 0.03704 | −4.1% | −0.0024 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9266 | 0.8888 | −4.1% | −0.0586 to −0.0169 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00869 | +0.009 (native is 0) | +0.0075 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9266 | 0.8975 | −3.1% | −0.0489 to −0.0092 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.9 | 777.3 | +3.2% | +4.5947 to +44.2320 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.33 | 9.608 | +15.3% | +0.6979 to +1.8572 | yes: power given |
| pods started | 4.9 | 9 | +83.7% | +3.2436 to +4.9564 | yes: power given |
| pod start wait, total (s) | 7.4 | 15.4 | +108.1% | +5.1990 to +10.8010 | yes: LOSS |
| pod start wait, mean (s) | 1.525 | 1.711 | +12.2% | −0.1788 to +0.5510 | no |
| host CPU busy, the real machine under kind (%) | 28.05 | 27.69 | −1.3% | −0.7020 to −0.0167 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.2% | −0.0043 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.8 | +0.2% | −0.4824 to +1.0871 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.8 | +0.2% | −0.4824 to +1.0871 | no |
| response time (ms), mean | 78.57 | 78.28 | −0.4% | −2.1906 to +1.6255 | no |
| response time (ms), 95th percentile | 116.6 | 114.2 | −2.1% | −5.4432 to +0.6342 | no |
| response time (ms), 99th percentile | 165.2 | 153.6 | −7.1% | −36.9250 to +13.6152 | no |
| time over the response line (% of samples) | 0.08522 | 0.1589 | +86.5% | −0.1056 to +0.2530 | no |
| failed requests (%) | 0 | 0.09877 | +0.099 (native is 0) | +0.0288 to +0.1687 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 17.2 | −12.2% | −12.7339 to +7.9339 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.7 | +154.5% | −0.2563 to +1.1063 | no |
| utilisation (used / allocatable) | 0.03654 | 0.03704 | +1.4% | −0.0001 to +0.0011 | no |
| CPU used (cores), mean | 0.877 | 0.8888 | +1.4% | −0.0022 to +0.0259 | no |
| Omni's own CPU (cores), mean | 0.00922 | 0.00869 | −5.7% | −0.0015 to +0.0005 | no |
| CPU used with Omni's own (cores), mean | 0.8862 | 0.8975 | +1.3% | −0.0026 to +0.0253 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785 | 777.3 | −1.0% | −18.9877 to +3.7499 | no |
| HPA replicas, mean | 8.051 | 9.608 | +19.3% | +0.0762 to +3.0374 | yes: power given |
| pods started | 4.2 | 9 | +114.3% | +3.1550 to +6.4450 | yes: power given |
| pod start wait, total (s) | 6.2 | 15.4 | +148.4% | +6.1132 to +12.2868 | yes: LOSS |
| pod start wait, mean (s) | 1.423 | 1.711 | +20.2% | −0.0975 to +0.6730 | no |
| host CPU busy, the real machine under kind (%) | 27.31 | 27.69 | +1.4% | −0.0969 to +0.8623 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*