# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.332 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 475.3 | 474.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.3 | 474.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 218.2 | 108.7 |
| response time (ms), 95th percentile | 555.1 | 196.2 |
| response time (ms), 99th percentile | 1015 | 449.3 |
| time over the response line (% of samples) | 8.988 | 1.652 |
| failed requests (%) | 0.7914 | 0.6379 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 4.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 10 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5433 | 0.9067 |
| utilisation (used / allocatable) | 0.06969 | 0.06725 |
| CPU used (cores), mean | 1.672 | 1.614 |
| Omni's own CPU (cores), mean | 0 | 0.00771 |
| CPU used with Omni's own (cores), mean | 1.672 | 1.622 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.6 | 457.6 |
| HPA replicas, mean | 9.517 | 9.675 |
| pods started | 6.6 | 11.6 |
| pod start wait, total (s) | 20.9 | 33 |
| pod start wait, mean (s) | 2.951 | 2.927 |
| host CPU busy, the real machine under kind (%) | 48.06 | 46.81 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.332 | 4.337 | +0.1% | +0.0001276 to +0.01054 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 475.3 | 474.3 | -0.2% | -1.919 to -0.08721 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 475.3 | 474.3 | -0.2% | -1.919 to -0.08721 | yes: GAIN |
| response time (ms), mean | 218.2 | 108.7 | -50.2% | -155.5 to -63.41 | yes: GAIN |
| response time (ms), 95th percentile | 555.1 | 196.2 | -64.7% | -496 to -221.7 | yes: GAIN |
| response time (ms), 99th percentile | 1015 | 449.3 | -55.7% | -777.7 to -354 | yes: GAIN |
| time over the response line (% of samples) | 8.988 | 1.652 | -81.6% | -12.01 to -2.664 | yes: GAIN |
| failed requests (%) | 0.7914 | 0.6379 | -19.4% | -0.2958 to -0.01107 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 4.4 | -72.7% | -18.39 to -5.015 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.9 | +44.9 (native is 0) | +29.65 to +60.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5433 | 0.9067 | +66.9% | +0.1006 to +0.626 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06969 | 0.06725 | -3.5% | -0.003658 to -0.001218 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.672 | 1.614 | -3.5% | -0.08779 to -0.02923 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00771 | +0.00771 (native is 0) | +0.005933 to +0.009487 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.672 | 1.622 | -3.0% | -0.07894 to -0.02266 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.6 | 457.6 | +2.5% | +6.494 to +15.54 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.517 | 9.675 | +1.7% | -0.9936 to +1.31 | no |
| pods started | 6.6 | 11.6 | +75.8% | +0.7884 to +9.212 | yes: power given |
| pod start wait, total (s) | 20.9 | 33 | +57.9% | +5.897 to +18.3 | yes: LOSS |
| pod start wait, mean (s) | 2.951 | 2.927 | -0.8% | -0.8614 to +0.8145 | no |
| host CPU busy, the real machine under kind (%) | 48.06 | 46.81 | -2.6% | -2.097 to -0.3884 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*