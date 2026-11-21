# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1656 | 1516 | 1966 | 1820 | 1903 | 1788 | 1925 | 1822 |
| response time (ms), 99th percentile | 4891 | 5071 | 5912 | 5635 | 5585 | 5636 | 5206 | 5441 |
| time over the response line (% of samples) | 29.08 | 20.29 | 20.73 | 15.23 | 19.54 | 14.6 | 28.55 | 21.29 |
| failed requests (%) | 13.15 | 10.72 | 7.012 | 6.301 | 6.434 | 5.869 | 9.16 | 8.486 |
| HPA replicas, mean | 9.68 | 12.88 | 9.635 | 13.7 | 9.615 | 13.46 | 9.638 | 13.96 |
| pods started | 4.935 | 10.11 | 4.919 | 9.629 | 5.258 | 9.806 | 4.919 | 10.08 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182 | 181.4 | 180.2 | 180.7 | 179.7 | 183 | 182.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182 | 181.4 | 180.2 | 180.7 | 179.7 | 183 | 182.6 |
| CPU used with Omni's own (cores), mean | 2.198 | 2.183 | 2.051 | 2.058 | 2.009 | 2.012 | 2.233 | 2.238 |
| host CPU busy, the real machine under kind (%) | 64.92 | 64.99 | 60.73 | 61 | 59.53 | 59.7 | 65.79 | 66.44 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1656 | 1516 | -8.4% | -321.9 to +42.47 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4891 | 5071 | +3.7% | -205.7 to +564.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.08 | 20.29 | -30.2% | -10.65 to -6.912 | GAIN |
| failed requests (%) | 13.15 | 10.72 | -18.5% | -3.463 to -1.396 | GAIN |
| HPA replicas, mean | 9.68 | 12.88 | +33.0% | +2.757 to +3.641 | power given |
| pods started | 4.935 | 10.11 | +104.9% | +4.592 to +5.763 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.831e-16 to -1.477e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182 | -0.2% | -0.7395 to -0.01968 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182 | -0.2% | -0.7395 to -0.01968 | GAIN |
| CPU used with Omni's own (cores), mean | 2.198 | 2.183 | -0.7% | -0.02611 to -0.003894 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.92 | 64.99 | +0.1% | -0.1986 to +0.3466 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.143e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1966 | 1820 | -7.4% | -382.1 to +91.95 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5912 | 5635 | -4.7% | -586.3 to +31.42 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.73 | 15.23 | -26.5% | -6.346 to -4.652 | GAIN |
| failed requests (%) | 7.012 | 6.301 | -10.1% | -1.049 to -0.3731 | GAIN |
| HPA replicas, mean | 9.635 | 13.7 | +42.2% | +3.588 to +4.538 | power given |
| pods started | 4.919 | 9.629 | +95.7% | +4.139 to +5.28 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.027e-16 to +7.292e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.2 | -0.6% | -1.449 to -0.8624 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.2 | -0.6% | -1.449 to -0.8624 | GAIN |
| CPU used with Omni's own (cores), mean | 2.051 | 2.058 | +0.3% | +0.0004498 to +0.01327 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.73 | 61 | +0.4% | +0.09929 to +0.4447 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1903 | 1788 | -6.0% | -301.1 to +71.14 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5585 | 5636 | +0.9% | -242.4 to +345.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.54 | 14.6 | -25.3% | -5.769 to -4.123 | GAIN |
| failed requests (%) | 6.434 | 5.869 | -8.8% | -0.8594 to -0.2711 | GAIN |
| HPA replicas, mean | 9.615 | 13.46 | +40.0% | +3.356 to +4.338 | power given |
| pods started | 5.258 | 9.806 | +86.5% | +3.944 to +5.153 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.992e-16 to +1.268e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.7 | -0.6% | -1.34 to -0.7272 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.7 | -0.6% | -1.34 to -0.7272 | GAIN |
| CPU used with Omni's own (cores), mean | 2.009 | 2.012 | +0.1% | -0.005572 to +0.0112 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.53 | 59.7 | +0.3% | -0.04086 to +0.3787 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1925 | 1822 | -5.4% | -224.7 to +17.43 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5206 | 5441 | +4.5% | -102.4 to +571.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.55 | 21.29 | -25.4% | -8.28 to -6.238 | GAIN |
| failed requests (%) | 9.16 | 8.486 | -7.4% | -0.8846 to -0.4634 | GAIN |
| HPA replicas, mean | 9.638 | 13.96 | +44.8% | +3.925 to +4.709 | power given |
| pods started | 4.919 | 10.08 | +104.9% | +4.669 to +5.653 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.69e-16 to +1.539e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 182.6 | -0.2% | -0.7772 to -0.05742 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 182.6 | -0.2% | -0.7772 to -0.05742 | GAIN |
| CPU used with Omni's own (cores), mean | 2.233 | 2.238 | +0.2% | -0.0007481 to +0.01166 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.79 | 66.44 | +1.0% | +0.4777 to +0.8193 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
