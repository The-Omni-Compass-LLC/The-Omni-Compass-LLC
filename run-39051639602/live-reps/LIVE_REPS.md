# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 158.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 158.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.7 | 80.93 |
| response time (ms), 95th percentile | 350.5 | 121.6 |
| response time (ms), 99th percentile | 587.3 | 183.8 |
| time over the response line (% of samples) | 2.064 | 0.03636 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.21 |
| utilisation (used / allocatable) | 0.04004 | 0.03716 |
| CPU used (cores), mean | 0.961 | 0.8919 |
| Omni's own CPU (cores), mean | 0 | 0.00824 |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9002 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.8 | 730.2 |
| HPA replicas, mean | 8.682 | 8.309 |
| pods started | 4.6 | 3.5 |
| pod start wait, total (s) | 15.3 | 11.8 |
| pod start wait, mean (s) | 3.043 | 2.777 |
| host CPU busy, the real machine under kind (%) | 28.81 | 27.33 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.395e-16 to +4.066e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.513 | -0.1% | -0.002963 to +0.000963 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 158.7 | -0.5% | -1.229 to -0.3125 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 158.7 | -0.5% | -1.229 to -0.3125 | yes: GAIN |
| response time (ms), mean | 157.7 | 80.93 | -48.7% | -97.44 to -56.14 | yes: GAIN |
| response time (ms), 95th percentile | 350.5 | 121.6 | -65.3% | -287.9 to -170 | yes: GAIN |
| response time (ms), 99th percentile | 587.3 | 183.8 | -68.7% | -516.7 to -290.4 | yes: GAIN |
| time over the response line (% of samples) | 2.064 | 0.03636 | -98.2% | -3.169 to -0.8868 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | -100.0% | -3.772 to -0.8283 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.4 (native is 0) | +16.55 to +20.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.21 | -43.0% | -0.2512 to -0.06543 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04004 | 0.03716 | -7.2% | -0.004265 to -0.001493 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.8919 | -7.2% | -0.1024 to -0.03584 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00824 | +0.00824 (native is 0) | +0.007162 to +0.009318 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9002 | -6.3% | -0.09317 to -0.02856 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.8 | 730.2 | +5.6% | +17.79 to +59.03 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.682 | 8.309 | -4.3% | -0.8489 to +0.1028 | no |
| pods started | 4.6 | 3.5 | -23.9% | -2.509 to +0.3086 | no |
| pod start wait, total (s) | 15.3 | 11.8 | -22.9% | -8.47 to +1.47 | no |
| pod start wait, mean (s) | 3.043 | 2.777 | -8.8% | -1.015 to +0.4814 | no |
| host CPU busy, the real machine under kind (%) | 28.81 | 27.33 | -5.1% | -2.361 to -0.6011 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*