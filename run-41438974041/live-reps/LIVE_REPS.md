# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.494 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.5 | 164.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 251.8 | 132.8 |
| response time (ms), 95th percentile | 398.7 | 152.8 |
| response time (ms), 99th percentile | 1092 | 526.6 |
| time over the response line (% of samples) | 8.501 | 6.505 |
| failed requests (%) | 5.735 | 5.623 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.042 | 0.6367 |
| utilisation (used / allocatable) | 0.07658 | 0.07521 |
| CPU used (cores), mean | 1.811 | 1.779 |
| Omni's own CPU (cores), mean | 0 | 0.04779 |
| CPU used with Omni's own (cores), mean | 1.811 | 1.827 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.7 | 370.2 |
| HPA replicas, mean | 8.835 | 12.01 |
| pods started | 5.3 | 10.1 |
| pod start wait, total (s) | 24.3 | 21.6 |
| pod start wait, mean (s) | 4.773 | 2.16 |
| host CPU busy, the real machine under kind (%) | 51.71 | 52.77 |
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
| worker nodes in service, mean | 5.913 | 5.913 | −0.0% | −0.0006 to +0.0006 | no |
| node-hours | 1.494 | 1.492 | −0.1% | −0.0074 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.5 | −0.3% | −1.1342 to +0.0022 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.5 | 164.9 | −0.3% | −1.1355 to +0.0077 | no |
| response time (ms), mean | 251.8 | 132.8 | −47.3% | −180.9761 to −57.0459 | yes: GAIN |
| response time (ms), 95th percentile | 398.7 | 152.8 | −61.7% | −277.6307 to −214.1163 | yes: GAIN |
| response time (ms), 99th percentile | 1092 | 526.6 | −51.8% | −949.8556 to −181.1586 | yes: GAIN |
| time over the response line (% of samples) | 8.501 | 6.505 | −23.5% | −3.0892 to −0.9032 | yes: GAIN |
| failed requests (%) | 5.735 | 5.623 | −2.0% | −0.8911 to +0.6668 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.5 | −14.5% | −2.1366 to −0.0634 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.400 (native is 0) | +41.0898 to +53.7102 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.042 | 0.6367 | −38.9% | −0.9704 to +0.1604 | no |
| utilisation (used / allocatable) | 0.07658 | 0.07521 | −1.8% | −0.0042 to +0.0014 | no |
| CPU used (cores), mean | 1.811 | 1.779 | −1.8% | −0.0984 to +0.0335 | no |
| Omni's own CPU (cores), mean | 0 | 0.04779 | +0.048 (native is 0) | +0.0440 to +0.0515 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.811 | 1.827 | +0.8% | −0.0511 to +0.0817 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.7 | 370.2 | +1.8% | −5.6504 to +18.6954 | no |
| HPA replicas, mean | 8.835 | 12.01 | +35.9% | +2.0848 to +4.2579 | yes: power given |
| pods started | 5.3 | 10.1 | +90.6% | +3.1899 to +6.4101 | yes: power given |
| pod start wait, total (s) | 24.3 | 21.6 | −11.1% | −27.0859 to +21.6859 | no |
| pod start wait, mean (s) | 4.773 | 2.16 | −54.8% | −7.6104 to +2.3835 | no |
| host CPU busy, the real machine under kind (%) | 51.71 | 52.77 | +2.0% | −0.4519 to +2.5590 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 81 | 14.1 |  |
| machine down | omni | 41 | 9.4 | -41 s (-50%) |
| spike | native | 286 | 73.4 |  |
| spike | omni | 281 | 74.8 | -5 s (-2%) |
| runaway pod started | native | 151 | 13.3 |  |
| runaway pod started | omni | 117 | 11.7 | -34 s (-22%) |
| probe blind | native | 66 | 0.8 |  |
| probe blind | omni | 60 | 0.1 | -6 s (-9%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*