# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1416 | 1286 | 1782 | 1635 | 1866 | 1669 |
| response time (ms), 99th percentile | 4323 | 4617 | 5026 | 4987 | 5331 | 5120 |
| time over the response line (% of samples) | 22.54 | 16.25 | 18.2 | 13.46 | 28.49 | 20.64 |
| failed requests (%) | 9.594 | 8.19 | 6.158 | 5.63 | 9.217 | 8.389 |
| HPA replicas, mean | 9.628 | 12.64 | 9.593 | 13.15 | 9.633 | 13.83 |
| pods started | 5.289 | 10.25 | 5.193 | 9.458 | 4.964 | 10.14 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.8 | 180 | 179.1 | 182.3 | 182.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.8 | 180 | 179.1 | 182.3 | 182.4 |
| CPU used with Omni's own (cores), mean | 2.054 | 2.048 | 1.943 | 1.951 | 2.209 | 2.214 |
| host CPU busy, the real machine under kind (%) | 60.9 | 60.99 | 57.72 | 58.12 | 65.23 | 65.82 |
| organism work | 2.085e+10 | 2.085e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1416 | 1286 | -9.2% | -261.2 to +1.568 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4323 | 4617 | +6.8% | +44.23 to +544 | LOSS |
| time over the response line (% of samples) | 22.54 | 16.25 | -27.9% | -7.627 to -4.934 | GAIN |
| failed requests (%) | 9.594 | 8.19 | -14.6% | -1.922 to -0.8864 | GAIN |
| HPA replicas, mean | 9.628 | 12.64 | +31.3% | +2.592 to +3.435 | power given |
| pods started | 5.289 | 10.25 | +93.8% | +4.421 to +5.507 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.013e-16 to +5.889e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.8 | +0.0% | -0.2422 to +0.2916 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.8 | +0.0% | -0.2422 to +0.2916 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.054 | 2.048 | -0.3% | -0.01447 to +0.001238 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.9 | 60.99 | +0.1% | -0.1424 to +0.3232 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.145e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1782 | 1635 | -8.2% | -363 to +69.28 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5026 | 4987 | -0.8% | -240.2 to +163.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.2 | 13.46 | -26.0% | -5.49 to -3.98 | GAIN |
| failed requests (%) | 6.158 | 5.63 | -8.6% | -0.765 to -0.292 | GAIN |
| HPA replicas, mean | 9.593 | 13.15 | +37.1% | +3.078 to +4.036 | power given |
| pods started | 5.193 | 9.458 | +82.1% | +3.673 to +4.857 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.597e-16 to +1.243e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.1 | -0.5% | -1.177 to -0.6197 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.1 | -0.5% | -1.177 to -0.6197 | GAIN |
| CPU used with Omni's own (cores), mean | 1.943 | 1.951 | +0.4% | +0.002704 to +0.01412 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.72 | 58.12 | +0.7% | +0.2741 to +0.5309 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1866 | 1669 | -10.6% | -313.3 to -82.34 | GAIN |
| response time (ms), 99th percentile | 5331 | 5120 | -4.0% | -474.5 to +52.63 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.49 | 20.64 | -27.5% | -8.901 to -6.792 | GAIN |
| failed requests (%) | 9.217 | 8.389 | -9.0% | -1.092 to -0.5634 | GAIN |
| HPA replicas, mean | 9.633 | 13.83 | +43.6% | +3.821 to +4.572 | power given |
| pods started | 4.964 | 10.14 | +104.4% | +4.697 to +5.664 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.306e-16 to -1.827e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.4 | +0.1% | -0.173 to +0.419 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.4 | +0.1% | -0.173 to +0.419 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.209 | 2.214 | +0.2% | -0.003667 to +0.01388 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.23 | 65.82 | +0.9% | +0.3616 to +0.8211 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Physics / Robotics / Autonomous
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
