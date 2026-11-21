# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 514.9 | 512.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.9 | 512.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 275.4 | 145 |
| response time (ms), 95th percentile | 712.8 | 277.3 |
| response time (ms), 99th percentile | 2153 | 1366 |
| time over the response line (% of samples) | 17.78 | 10.08 |
| failed requests (%) | 9.248 | 7.968 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 19 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.3383 |
| utilisation (used / allocatable) | 0.09838 | 0.09532 |
| CPU used (cores), mean | 2.361 | 2.288 |
| Omni's own CPU (cores), mean | 0 | 0.00873 |
| CPU used with Omni's own (cores), mean | 2.361 | 2.296 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.1 | 326.7 |
| HPA replicas, mean | 9.567 | 10.33 |
| pods started | 5.2 | 5.9 |
| pod start wait, total (s) | 19 | 16.3 |
| pod start wait, mean (s) | 3.393 | 2.236 |
| host CPU busy, the real machine under kind (%) | 66.35 | 64.7 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | no |
| node-hours | 4.516 | 4.516 | -0.0% | -0.004606 to +0.003939 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 514.9 | 512.9 | -0.4% | -2.848 to -1.167 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.9 | 512.9 | -0.4% | -2.848 to -1.167 | yes: GAIN |
| response time (ms), mean | 275.4 | 145 | -47.4% | -170 to -90.97 | yes: GAIN |
| response time (ms), 95th percentile | 712.8 | 277.3 | -61.1% | -550.5 to -320.5 | yes: GAIN |
| response time (ms), 99th percentile | 2153 | 1366 | -36.6% | -1614 to +39.87 | no |
| time over the response line (% of samples) | 17.78 | 10.08 | -43.3% | -10.59 to -4.814 | yes: GAIN |
| failed requests (%) | 9.248 | 7.968 | -13.8% | -2.152 to -0.4071 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 19 | -32.4% | -11.02 to -7.179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 | +47.5 (native is 0) | +34.38 to +60.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.3383 | -30.5% | -0.537 to +0.2404 | no |
| utilisation (used / allocatable) | 0.09838 | 0.09532 | -3.1% | -0.003776 to -0.002353 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.361 | 2.288 | -3.1% | -0.09062 to -0.05648 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00873 | +0.00873 (native is 0) | +0.007364 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.361 | 2.296 | -2.7% | -0.08254 to -0.04711 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.1 | 326.7 | +4.0% | +2.541 to +22.5 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.567 | 10.33 | +8.0% | -0.2085 to +1.739 | no |
| pods started | 5.2 | 5.9 | +13.5% | -2.082 to +3.482 | no |
| pod start wait, total (s) | 19 | 16.3 | -14.2% | -9.814 to +4.414 | no |
| pod start wait, mean (s) | 3.393 | 2.236 | -34.1% | -2.031 to -0.2831 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 66.35 | 64.7 | -2.5% | -2.165 to -1.137 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*