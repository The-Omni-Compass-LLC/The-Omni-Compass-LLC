# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 347 | 347 | -0.2% | -3.12 to 1.41 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0262 to 0.0505 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,695 | 1,685 | -0.6% | -107 to 87.6 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,534 | 2,539 | +0.2% | -321 to 331 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.82 | 8.77 | -0.6% | -0.167 to 0.0604 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 260 | 264 | +1.4% | -1.44 to 8.65 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,123 | 1,119 | -0.4% | -59.5 to 50.8 | no difference beyond the noise |
| consumer lag, mean messages waiting | 114 | 115 | +0.8% | -5.75 to 7.6 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -1.2% | -0.0248 to -0.0248 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.312 | 0.306 | -2.0% | -0.0305 to 0.0182 | no difference beyond the noise |
| host CPU-seconds | 149 | 146 | -2.0% | -14.6 to 8.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.5 | -1.7% | -0.363 to 0.238 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 149 | 149 | -0.1% | -0.992 to 0.681 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.0118 to 0.0139 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,639 | 1,623 | -1.0% | -37.9 to 6.14 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,444 | 2,444 | -0.0% | -174 to 173 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.0563 to 0.019 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 221 | 222 | +0.4% | -3.11 to 4.93 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 483 | 467 | -3.2% | -117 to 86 | no difference beyond the noise |
| consumer lag, mean messages waiting | 41.9 | 41.7 | -0.6% | -1.44 to 0.954 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2 | +0.2% | -0.0575 to 0.0664 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.282 | -0.2% | -0.0102 to 0.00919 | no difference beyond the noise |
| host CPU-seconds | 331 | 331 | -0.1% | -11.6 to 10.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.42 | -0.0% | -0.293 to 0.293 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 733 | +0.1% | -3.51 to 4.57 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | +0.0% | -0.0405 to 0.0673 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,565 | 1,557 | -0.5% | -81.4 to 65.9 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,418 | 2,429 | +0.5% | -162 to 185 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.37 | 7.76 | -7.2% | -0.833 to -0.373 | better |
| end-to-end latency, mean (ms) | 218 | 215 | -1.5% | -21.7 to 15.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,225 | 2,218 | -0.3% | -54.6 to 40.6 | no difference beyond the noise |
| consumer lag, mean messages waiting | 192 | 188 | -2.5% | -20.5 to 10.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.37 | +18.5% | 0.357 to 0.382 | **WORSE** |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | **WORSE** |
| host CPU busy (share of the run) | 0.333 | 0.335 | +0.7% | -0.0187 to 0.0234 | no difference beyond the noise |
| host CPU-seconds | 381 | 384 | +0.8% | -22.8 to 29.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.8% | -0.104 to 0.13 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 370 | 369 | -0.1% | -2.86 to 2.12 | no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00943 to 0.00846 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,663 | 1,658 | -0.3% | -85.3 to 75 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,600 | 2,534 | -2.5% | -127 to -4.6 | better |
| end-to-end latency, median (ms) | 8.51 | 8.47 | -0.4% | -0.118 to 0.0435 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 226 | 227 | +0.4% | -2.3 to 3.95 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,168 | 1,143 | -2.2% | -72.4 to 21.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 101 | 101 | +0.1% | -1.44 to 1.63 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.24 | +11.8% | -0.293 to 0.766 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.31 | 0.308 | -0.6% | -0.0129 to 0.00911 | no difference beyond the noise |
| host CPU-seconds | 359 | 358 | -0.4% | -15.8 to 12.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.23 | -0.3% | -0.147 to 0.127 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
