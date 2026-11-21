# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 552.6 | 478.9 |
| response time (ms), 95th percentile | 2341 | 2254 |
| response time (ms), 99th percentile | 5670 | 5707 |
| time over the response line (% of samples) | 24.83 | 23.26 |
| failed requests (%) | 3.982 | 3.683 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9267 | 2.163 |
| utilisation (used / allocatable) | 0.09791 | 0.09706 |
| CPU used (cores), mean | 2.35 | 2.33 |
| Omni's own CPU (cores), mean | 0 | 0.01145 |
| CPU used with Omni's own (cores), mean | 2.35 | 2.341 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.4 | 302.8 |
| HPA replicas, mean | 15.33 | 15.34 |
| pods started | 3.9 | 3.7 |
| pod start wait, total (s) | 9.8 | 10.9 |
| pod start wait, mean (s) | 2.15 | 2.27 |
| host CPU busy, the real machine under kind (%) | 69.18 | 68.82 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 283.7 | 299.2 |
| second app: response time (ms), 99th percentile | 1474 | 1121 |
| second app: time over the response line (% of samples) | 14.97 | 15.04 |
| second app: failed requests (%) | 13.32 | 13.32 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.0% | -0.00526 to +0.00626 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 172.7 | -0.1% | -0.8908 to +0.6661 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 172.7 | -0.1% | -0.8908 to +0.6661 | no |
| response time (ms), mean | 552.6 | 478.9 | -13.3% | -119.3 to -28.18 | yes: GAIN |
| response time (ms), 95th percentile | 2341 | 2254 | -3.7% | -434.7 to +260.4 | no |
| response time (ms), 99th percentile | 5670 | 5707 | +0.6% | -638.1 to +711.1 | no |
| time over the response line (% of samples) | 24.83 | 23.26 | -6.4% | -3.196 to +0.04027 | no |
| failed requests (%) | 3.982 | 3.683 | -7.5% | -1.099 to +0.5002 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.6 | -2.3% | -0.8573 to +0.4573 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.1 (native is 0) | +30.06 to +34.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9267 | 2.163 | +133.5% | +0.2534 to +2.22 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09791 | 0.09706 | -0.9% | -0.001849 to +0.0001581 | no |
| CPU used (cores), mean | 2.35 | 2.33 | -0.9% | -0.04437 to +0.003794 | no |
| Omni's own CPU (cores), mean | 0 | 0.01145 | +0.0114 (native is 0) | +0.01024 to +0.01266 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.35 | 2.341 | -0.4% | -0.03282 to +0.01514 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.4 | 302.8 | +0.8% | -1.338 to +6.046 | no |
| HPA replicas, mean | 15.33 | 15.34 | +0.0% | -0.4352 to +0.4445 | no |
| pods started | 3.9 | 3.7 | -5.1% | -1.256 to +0.8556 | no |
| pod start wait, total (s) | 9.8 | 10.9 | +11.2% | -3.884 to +6.084 | no |
| pod start wait, mean (s) | 2.15 | 2.27 | +5.6% | -0.5578 to +0.7983 | no |
| host CPU busy, the real machine under kind (%) | 69.18 | 68.82 | -0.5% | -0.7582 to +0.04302 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 283.7 | 299.2 | +5.4% | -15.44 to +46.36 | no |
| second app: response time (ms), 99th percentile | 1474 | 1121 | -23.9% | -815.2 to +109.9 | no |
| second app: time over the response line (% of samples) | 14.97 | 15.04 | +0.5% | -0.6804 to +0.8228 | no |
| second app: failed requests (%) | 13.32 | 13.32 | +0.0% | -0.3869 to +0.3888 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*