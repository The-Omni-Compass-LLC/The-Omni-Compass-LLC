# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 418 | +22.6% | 67.5 to 86.4 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.903 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,602 | 11.6 | -99.6% | -2,623 to -2,558 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,795 | 352 | -90.7% | -4,478 to -2,407 | GAIN |
| end-to-end latency, median (ms) | 9.21 | 8.1 | -12.0% | -1.9 to -0.309 | GAIN |
| end-to-end latency, mean (ms) | 385 | 16.9 | -95.6% | -400 to -336 | GAIN |
| consumer lag, most messages waiting at once | 1,684 | 328 | -80.5% | -2,164 to -548 | GAIN |
| consumer lag, mean messages waiting | 166 | 7.43 | -95.5% | -173 to -144 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.3% | 2.15 to 3.9 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.313 | 0.333 | +6.4% | 0.00394 to 0.0365 | power given |
| host CPU-seconds | 221 | 234 | +6.1% | 1.31 to 25.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.11 | -13.2% | -0.695 to -0.252 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.3 to 25.9 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00122 to 0.000835 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,537 | 12.6 | -99.5% | -2,607 to -2,443 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,933 | 28.3 | -99.3% | -4,039 to -3,770 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.3% | -0.349 to -0.194 | GAIN |
| end-to-end latency, mean (ms) | 342 | 14.6 | -95.7% | -329 to -325 | GAIN |
| consumer lag, most messages waiting at once | 726 | 139 | -80.8% | -721 to -452 | GAIN |
| consumer lag, mean messages waiting | 62.7 | 2.73 | -95.6% | -60.5 to -59.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.02 | +150.9% | -0.238 to 6.27 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.289 | 0.296 | +2.6% | -0.00355 to 0.0188 | STEADY, no difference beyond the noise |
| host CPU-seconds | 510 | 523 | +2.5% | -6.26 to 31.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 6.72 | -12.7% | -1.25 to -0.698 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 850 | +17.5% | 126 to 127 | GAIN |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0183 to -0.00618 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,552 | 10.9 | -99.6% | -2,645 to -2,439 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,971 | 14.3 | -99.6% | -4,090 to -3,824 | GAIN |
| end-to-end latency, median (ms) | 8.52 | 7.01 | -17.7% | -2.13 to -0.886 | GAIN |
| end-to-end latency, mean (ms) | 339 | 7.56 | -97.8% | -349 to -313 | GAIN |
| consumer lag, most messages waiting at once | 3,433 | 82.3 | -97.6% | -3,455 to -3,245 | GAIN |
| consumer lag, mean messages waiting | 292 | 6.69 | -97.7% | -301 to -269 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.7% | 2.72 to 3.34 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.43 | 0.48 | +11.6% | 0.0181 to 0.0816 | power given |
| host CPU-seconds | 751 | 835 | +11.3% | 21 to 149 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.31 | 2.18 | -5.3% | -0.301 to 0.0562 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 967 messages a second; base rate 145.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 425 | +16.0% | 56.2 to 60.8 | GAIN |
| throughput (messages a second consumed) | 426 | 425 | -0.0% | -0.0185 to 0.0109 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,991 | 9.92 | -99.5% | -2,081 to -1,881 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,255 | 23.3 | -99.3% | -3,333 to -3,132 | GAIN |
| end-to-end latency, median (ms) | 8.19 | 7.19 | -12.2% | -1.17 to -0.83 | GAIN |
| end-to-end latency, mean (ms) | 261 | 8.61 | -96.7% | -270 to -233 | GAIN |
| consumer lag, most messages waiting at once | 1,489 | 134 | -91.0% | -1,425 to -1,285 | GAIN |
| consumer lag, mean messages waiting | 115 | 4.09 | -96.4% | -118 to -103 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.86 | +142.8% | 2.19 to 3.52 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.294 | 0.305 | +3.6% | 0.00432 to 0.017 | power given |
| host CPU-seconds | 524 | 542 | +3.4% | 5.04 to 31 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.18 | 2.83 | -10.8% | -0.44 to -0.246 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
