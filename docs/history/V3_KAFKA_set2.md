# Kafka, a consumer group's operator-set size: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any increase in any run is WORSE. The tuning workload is shown and not counted. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38021564790 | `0a74e9a66193` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38013304929 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38013309420 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 976, 976 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 364.8 | 364.7 | -0.0% (-0.8 to +0.7) | -0.0% (-0.4 to +0.3) | -0.1% (-0.6 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 427.8 | 427.8 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,355 | +2.2% (-9.5 to +13.9) | +0.3% (-5.6 to +6.1) | +1.5% (-5.3 to +8.4) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,641 | 3,589 | -1.4% (-12.2 to +9.3) | +1.2% (-9.1 to +11.5) | +4.3% (-9.5 to +18.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.73 | 8.71 | -0.2% (-3.4 to +3.0) | +0.0% (-0.5 to +0.5) | -0.2% (-1.9 to +1.5) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 312.7 | 310.9 | -0.6% (-9.4 to +8.2) | +0.7% (-4.2 to +5.5) | +3.9% (-6.7 to +14.5) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,656 | 1,657 | +0.1% (-3.5 to +3.6) | +1.5% (-0.7 to +3.6) | +3.5% (-4.1 to +11.1) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 137.8 | 137.2 | -0.4% (-9.4 to +8.5) | +0.3% (-3.8 to +4.5) | +3.5% (-7.1 to +14.1) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.323 | 0.325 | +0.5% (-2.0 to +3.0) | -0.4% (-4.7 to +4.0) | -1.0% (-4.0 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 560.7 | 565.2 | +0.8% (-2.1 to +3.7) | -0.5% (-5.2 to +4.2) | -0.9% (-3.8 to +1.9) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.44 | +0.8% (-2.7 to +4.3) | -0.4% (-4.9 to +4.0) | -0.9% (-3.7 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 982, 976 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.0 | 339.8 | -0.4% (-0.7 to -0.1) | -0.2% (-0.9 to +0.6) | -0.3% (-0.5 to -0.2) | no difference beyond the noise (1 of 3 runs) |
| throughput (messages a second consumed) | 418.4 | 418.4 | -0.0% (-0.0 to +0.0) | -0.1% (-0.5 to +0.3) | +0.1% (-0.3 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,471 | 2,474 | +0.1% (-4.5 to +4.6) | -2.5% (-8.2 to +3.1) | -0.2% (-5.8 to +5.4) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,768 | 3,732 | -1.0% (-9.8 to +7.9) | +1.5% (-11.6 to +14.6) | -0.1% (-7.3 to +7.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 9.47 | 9.28 | -2.0% (-8.7 to +4.7) | -17.0% (-97.9 to +63.9) | +1.1% (-7.0 to +9.1) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 378.6 | 380.4 | +0.5% (-1.0 to +2.0) | -1.3% (-4.3 to +1.6) | +2.4% (-4.0 to +8.9) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,641 | 1,633 | -0.4% (-1.3 to +0.4) | -1.9% (-8.3 to +4.5) | +0.7% (-2.9 to +4.3) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 163.2 | 164.0 | +0.5% (-3.2 to +4.2) | -2.2% (-8.1 to +3.7) | +1.1% (-5.9 to +8.1) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.295 | 0.293 | -0.7% (-4.9 to +3.4) | -7.1% (-29.0 to +14.8) | -0.5% (-6.9 to +5.9) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 206.4 | 205.0 | -0.7% (-4.8 to +3.4) | -6.9% (-28.0 to +14.3) | -0.6% (-6.8 to +5.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.34 | -0.3% (-4.3 to +3.7) | -6.8% (-28.2 to +14.6) | -0.2% (-6.8 to +6.4) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 395 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.5 | 147.6 | +0.1% (-0.5 to +0.6) | -0.2% (-0.8 to +0.3) | -0.3% (-0.4 to -0.1) | no difference beyond the noise (2 of 3 runs) |
| throughput (messages a second consumed) | 173.1 | 173.1 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,350 | 2,370 | +0.8% (-10.9 to +12.6) | +0.9% (-3.0 to +4.9) | +1.3% (-1.9 to +4.5) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,672 | -1.8% (-9.1 to +5.6) | +0.0% (-7.1 to +7.2) | +1.7% (-11.9 to +15.4) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% (-0.6 to +0.3) | -0.2% (-1.2 to +0.8) | -0.0% (-0.9 to +0.9) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 319.2 | 313.1 | -1.9% (-10.7 to +6.9) | +2.3% (-3.9 to +8.4) | +1.9% (-2.3 to +6.0) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 696.0 | 674.7 | -3.1% (-10.8 to +4.6) | -1.4% (-7.3 to +4.6) | -0.3% (-4.1 to +3.6) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 58.7 | 57.0 | -2.9% (-15.9 to +10.1) | +0.6% (-5.6 to +6.7) | +0.8% (-0.3 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **confirmed better** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.257 | 0.256 | -0.5% (-2.4 to +1.4) | -0.4% (-3.2 to +2.3) | -0.2% (-3.7 to +3.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 460.5 | 458.4 | -0.5% (-2.3 to +1.4) | -0.4% (-3.2 to +2.4) | -0.1% (-3.6 to +3.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 6.94 | 6.9 | -0.5% (-2.2 to +1.1) | -0.2% (-2.4 to +2.0) | +0.1% (-3.2 to +3.4) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,947, 1,937, 1,932 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729.8 | 728.1 | -0.2% (-0.7 to +0.2) | +0.0% (-1.7 to +1.8) | +0.0% (-0.6 to +0.7) | no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 856.6 | 856.6 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,474 | 2,503 | +1.2% (-3.1 to +5.5) | -7.6% (-44.2 to +29.0) | -0.1% (-13.0 to +12.9) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,743 | -2.1% (-18.6 to +14.3) | -10.5% (-39.9 to +18.9) | -2.3% (-12.3 to +7.7) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 7.39 | 7.45 | +0.8% (-2.1 to +3.7) | -0.5% (-4.5 to +3.6) | -1.0% (-5.1 to +3.1) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 328.3 | 333.2 | +1.5% (-5.2 to +8.3) | -6.9% (-40.4 to +26.6) | -0.9% (-9.7 to +7.9) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 3,394 | 3,433 | +1.2% (-0.4 to +2.7) | -7.6% (-32.5 to +17.3) | +0.5% (-4.4 to +5.5) | no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 286.0 | 290.5 | +1.6% (-4.7 to +7.8) | -6.9% (-40.4 to +26.6) | -0.8% (-9.3 to +7.8) | no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.6 to +0.1) | -0.3% (-0.3 to -0.3) | no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.32 | 0.319 | -0.2% (-2.1 to +1.6) | -0.3% (-2.0 to +1.4) | -1.4% (-5.0 to +2.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 569.6 | 568.0 | -0.3% (-1.6 to +1.1) | -0.3% (-2.7 to +2.2) | -1.3% (-5.0 to +2.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.73 | -0.0% (-1.0 to +0.9) | -0.3% (-3.4 to +2.8) | -1.3% (-5.0 to +2.4) | no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 2 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
