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
| response time (ms), 95th percentile | 1633 | 1521 | 1872 | 1981 | 1360 | 1439 | 1987 | 1728 |
| response time (ms), 99th percentile | 5322 | 5264 | 5745 | 5527 | 4370 | 4611 | 5502 | 5013 |
| time over the response line (% of samples) | 28.62 | 19.39 | 20.79 | 15.27 | 15.24 | 11.32 | 29.58 | 20.58 |
| failed requests (%) | 12.53 | 9.908 | 7.025 | 6.165 | 4.967 | 4.325 | 9.499 | 8.61 |
| HPA replicas, mean | 9.679 | 12.92 | 9.631 | 13.54 | 9.57 | 12.71 | 9.627 | 13.81 |
| pods started | 4.951 | 10.05 | 5.024 | 9.951 | 5.439 | 9.488 | 4.976 | 9.902 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.7 | 181.4 | 180.3 | 179 | 178.4 | 182.7 | 182.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.7 | 181.4 | 180.3 | 179 | 178.4 | 182.7 | 182.2 |
| CPU used with Omni's own (cores), mean | 2.192 | 2.17 | 2.066 | 2.067 | 1.844 | 1.851 | 2.202 | 2.196 |
| host CPU busy, the real machine under kind (%) | 64.84 | 64.45 | 61.14 | 61.44 | 54.84 | 55.15 | 64.95 | 65.42 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1633 | 1521 | -6.9% | -315.7 to +91.01 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5322 | 5264 | -1.1% | -616.7 to +500.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.62 | 19.39 | -32.3% | -11.5 to -6.966 | GAIN |
| failed requests (%) | 12.53 | 9.908 | -20.9% | -3.774 to -1.46 | GAIN |
| HPA replicas, mean | 9.679 | 12.92 | +33.4% | +2.742 to +3.732 | power given |
| pods started | 4.951 | 10.05 | +103.0% | +4.51 to +5.686 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.286e-16 to +2.853e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.7 | -0.3% | -0.8645 to -0.07838 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.7 | -0.3% | -0.8645 to -0.07838 | GAIN |
| CPU used with Omni's own (cores), mean | 2.192 | 2.17 | -1.0% | -0.03147 to -0.01279 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.84 | 64.45 | -0.6% | -0.6733 to -0.1007 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.621e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.145e-05 to -8.142e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1872 | 1981 | +5.8% | -206.3 to +424.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5745 | 5527 | -3.8% | -617.5 to +180.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.79 | 15.27 | -26.5% | -6.553 to -4.486 | GAIN |
| failed requests (%) | 7.025 | 6.165 | -12.2% | -1.26 to -0.4592 | GAIN |
| HPA replicas, mean | 9.631 | 13.54 | +40.6% | +3.321 to +4.501 | power given |
| pods started | 5.024 | 9.951 | +98.1% | +4.176 to +5.678 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.461e-16 to -2.04e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.3 | -0.6% | -1.397 to -0.6398 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.3 | -0.6% | -1.397 to -0.6398 | GAIN |
| CPU used with Omni's own (cores), mean | 2.066 | 2.067 | +0.1% | -0.006427 to +0.009432 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.14 | 61.44 | +0.5% | +0.08527 to +0.517 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1360 | 1439 | +5.8% | -135.9 to +294.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4370 | 4611 | +5.5% | -123.5 to +604.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.24 | 11.32 | -25.7% | -5.009 to -2.82 | GAIN |
| failed requests (%) | 4.967 | 4.325 | -12.9% | -1.017 to -0.2671 | GAIN |
| HPA replicas, mean | 9.57 | 12.71 | +32.8% | +2.432 to +3.852 | power given |
| pods started | 5.439 | 9.488 | +74.4% | +3.18 to +4.917 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.367e-16 to +3.067e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 178.4 | -0.3% | -0.915 to -0.1531 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 178.4 | -0.3% | -0.915 to -0.1531 | GAIN |
| CPU used with Omni's own (cores), mean | 1.844 | 1.851 | +0.4% | -0.004043 to +0.01824 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.84 | 55.15 | +0.6% | +0.034 to +0.5881 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1987 | 1728 | -13.0% | -492.1 to -26.22 | GAIN |
| response time (ms), 99th percentile | 5502 | 5013 | -8.9% | -947.7 to -30.69 | GAIN |
| time over the response line (% of samples) | 29.58 | 20.58 | -30.4% | -10.79 to -7.212 | GAIN |
| failed requests (%) | 9.499 | 8.61 | -9.4% | -1.246 to -0.5316 | GAIN |
| HPA replicas, mean | 9.627 | 13.81 | +43.4% | +3.595 to +4.766 | power given |
| pods started | 4.976 | 9.902 | +99.0% | +4.248 to +5.606 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.066e-16 to -2.992e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.2 | -0.3% | -0.9307 to -0.03248 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.2 | -0.3% | -0.9307 to -0.03248 | GAIN |
| CPU used with Omni's own (cores), mean | 2.202 | 2.196 | -0.3% | -0.01506 to +0.001596 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.95 | 65.42 | +0.7% | +0.2831 to +0.6521 | shown, not judged |
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
