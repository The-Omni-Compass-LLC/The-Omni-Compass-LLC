# Kafka, a consumer group's operator-set size: the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any increase in any run is WORSE. The tuning workload is shown and not counted. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013371103 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38013376137 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38013380640 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 981, 977, 974 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367.1 | 366.1 | -0.3% (-0.9 to +0.4) | -0.2% (-1.0 to +0.7) | -0.1% (-0.3 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 431.5 | 431.5 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,510 | 2,592 | +3.2% (-3.6 to +10.1) | +0.2% (-18.4 to +18.8) | +0.0% (-6.7 to +6.8) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,834 | 3,913 | +2.1% (-1.6 to +5.7) | +0.9% (-3.3 to +5.1) | +3.5% (-3.6 to +10.5) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.19 | 8.17 | -0.2% (-1.5 to +1.0) | -0.2% (-1.0 to +0.6) | -0.2% (-1.4 to +0.9) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 335.2 | 344.0 | +2.6% (-7.1 to +12.3) | +0.6% (-11.3 to +12.4) | +1.3% (-3.1 to +5.7) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,742 | 1,758 | +0.9% (-2.8 to +4.7) | +0.3% (-11.3 to +11.9) | -0.2% (-2.9 to +2.4) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 148.6 | 151.8 | +2.2% (-6.2 to +10.5) | +0.4% (-11.0 to +11.8) | +1.0% (-3.5 to +5.5) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.298 | 0.296 | -0.5% (-1.9 to +0.8) | -0.4% (-2.1 to +1.3) | -0.5% (-2.7 to +1.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 531.8 | 528.8 | -0.6% (-1.9 to +0.8) | -0.3% (-2.2 to +1.6) | -0.5% (-2.6 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.21 | -0.3% (-1.9 to +1.4) | -0.1% (-2.6 to +2.4) | -0.4% (-2.3 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 973, 976, 959 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.5 | 339.8 | -0.2% (-0.5 to +0.1) | -0.0% (-0.3 to +0.2) | -0.4% (-0.6 to -0.1) | no difference beyond the noise (2 of 3 runs) |
| throughput (messages a second consumed) | 418.0 | 418.0 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,524 | +2.6% (-4.4 to +9.7) | +0.3% (-4.8 to +5.3) | +5.1% (-9.1 to +19.3) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,707 | 3,514 | -5.2% (-22.2 to +11.8) | +1.8% (-6.2 to +9.7) | +5.8% (+0.8 to +10.8) | no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, median (ms) | 9.57 | 9.5 | -0.7% (-6.6 to +5.2) | +0.7% (-3.6 to +5.0) | -1.0% (-3.3 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 377.3 | 379.6 | +0.6% (-0.4 to +1.6) | -0.5% (-4.1 to +3.1) | +5.2% (+0.1 to +10.3) | no difference beyond the noise (2 of 3 runs) |
| consumer lag, most messages waiting at once | 1,632 | 1,624 | -0.5% (-3.8 to +2.8) | -0.2% (-4.6 to +4.2) | +5.6% (-3.0 to +14.1) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 164.1 | 162.9 | -0.7% (-2.9 to +1.4) | -1.3% (-3.0 to +0.4) | +4.5% (+0.1 to +8.9) | no difference beyond the noise (2 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% (-6.1 to +4.1) | -0.7% (-4.5 to +3.1) | +0.3% (-2.6 to +3.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 209.5 | 207.4 | -1.0% (-6.1 to +4.1) | -0.7% (-4.5 to +3.2) | +0.3% (-2.6 to +3.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.38 | -0.8% (-5.8 to +4.1) | -0.6% (-4.4 to +3.2) | +0.6% (-2.5 to +3.8) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 146.9 | -0.2% (-0.6 to +0.2) | +0.0% (-0.5 to +0.5) | -0.1% (-0.5 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 172.7 | 172.7 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,437 | +1.5% (-5.0 to +7.9) | +0.7% (-3.3 to +4.6) | +0.5% (-7.4 to +8.4) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,795 | 3,718 | -2.0% (-6.7 to +2.7) | -1.0% (-2.8 to +0.8) | +1.4% (-6.3 to +9.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.3 | 11.3 | -0.0% (-1.0 to +0.9) | -0.2% (-2.8 to +2.4) | -0.1% (-0.8 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 322.4 | 324.0 | +0.5% (-1.4 to +2.4) | -1.3% (-6.5 to +3.9) | +0.9% (-3.5 to +5.3) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 702.0 | 700.7 | -0.2% (-6.8 to +6.4) | +1.1% (-2.5 to +4.8) | +1.1% (-6.7 to +8.9) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 59.0 | 59.0 | -0.1% (-1.8 to +1.6) | -0.1% (-7.8 to +7.5) | +1.7% (-0.8 to +4.2) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.277 | 0.277 | -0.3% (-3.3 to +2.8) | -0.0% (-5.7 to +5.6) | -0.3% (-4.5 to +3.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 496.7 | 495.6 | -0.2% (-3.4 to +2.9) | -0.0% (-5.6 to +5.5) | -0.2% (-4.4 to +3.9) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.49 | 7.49 | -0.0% (-3.3 to +3.2) | -0.0% (-5.8 to +5.8) | -0.1% (-4.1 to +3.8) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,932, 1,937, 1,931 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.5 | 726.9 | +0.1% (-1.0 to +1.1) | +0.0% (-0.3 to +0.3) | -0.0% (-0.4 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 849.9 | 849.9 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,258 | 2,142 | -5.2% (-48.9 to +38.6) | +0.5% (-2.1 to +3.1) | -1.7% (-6.5 to +3.1) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,555 | 3,346 | -5.9% (-53.8 to +42.0) | -6.0% (-12.4 to +0.3) | -2.1% (-6.7 to +2.6) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 7.56 | 7.45 | -1.4% (-4.7 to +1.9) | -0.3% (-6.6 to +6.0) | -2.6% (-7.4 to +2.3) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 303.9 | 290.4 | -4.4% (-48.0 to +39.2) | -1.1% (-3.7 to +1.5) | -1.0% (-6.6 to +4.5) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 3,174 | 3,072 | -3.2% (-43.9 to +37.5) | -1.0% (-5.2 to +3.3) | -0.5% (-5.1 to +4.1) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 263.6 | 252.2 | -4.3% (-46.0 to +37.3) | -1.0% (-3.7 to +1.6) | -1.1% (-6.1 to +3.8) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.317 | 0.315 | -0.4% (-3.6 to +2.7) | -1.3% (-13.8 to +11.3) | +0.2% (-2.0 to +2.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 564.5 | 562.1 | -0.4% (-3.6 to +2.8) | -1.2% (-14.0 to +11.6) | +0.3% (-1.5 to +2.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.72 | -0.5% (-4.6 to +3.7) | -1.2% (-14.1 to +11.6) | +0.3% (-1.8 to +2.5) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (7 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 3 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
