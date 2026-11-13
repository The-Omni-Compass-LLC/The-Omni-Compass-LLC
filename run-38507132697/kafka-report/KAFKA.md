# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 970 messages a second; base rate 109.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 338 | 364 | +7.5% | -83.5 to 134 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.0511 to 0.0626 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,687 | 1,744 | -35.1% | -3,860 to 1,974 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,933 | 2,666 | -32.2% | -5,582 to 3,050 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.81 | 8.51 | -3.4% | -1.04 to 0.437 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 268 | -32.8% | -580 to 318 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,155 | -32.6% | -2,365 to 1,245 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 171 | 114 | -33.7% | -246 to 131 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +15.8% | -0.655 to 1.29 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.286 | 0.294 | +2.6% | -0.00135 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 210 | +2.6% | -1.15 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.23 | -3.7% | -1.01 to 0.766 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.181 to -0.0316 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00377 to 0.00408 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,465 | 2,386 | -3.2% | -204 to 47 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,710 | 3,790 | +2.2% | -309 to 468 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.7% | -0.25 to 0.0936 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 323 | -0.9% | -10.5 to 4.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 701 | 679 | -3.1% | -59.7 to 16.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.8 | 59.1 | -1.3% | -1.7 to 0.195 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.276 | -1.4% | -0.0127 to 0.00502 | EVEN, no difference beyond the noise |
| host CPU-seconds | 501 | 494 | -1.4% | -22.3 to 8.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.47 | -1.3% | -0.334 to 0.137 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 760 | +4.2% | -112 to 174 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.014 to 0.00343 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,111 | 1,529 | -27.5% | -3,528 to 2,365 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,390 | 2,702 | -20.3% | -4,363 to 2,987 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.41 | 7.11 | -4.0% | -1.48 to 0.893 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 281 | 211 | -24.8% | -427 to 288 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,114 | 2,786 | -10.5% | -2,183 to 1,527 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 244 | 183 | -25.0% | -369 to 246 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +16.1% | -0.435 to 1.08 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.316 | +1.2% | -0.0151 to 0.0225 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 564 | +1.2% | -29 to 41.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.65 | -2.7% | -0.25 to 0.159 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -2.75 to 2.14 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | +0.0% | -0.0128 to 0.0171 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,349 | 2,318 | -1.4% | -198 to 134 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,596 | 3,664 | +1.9% | -184 to 322 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.55 | -1.1% | -0.279 to 0.0921 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 309 | 310 | +0.5% | -19.6 to 22.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,666 | 1,647 | -1.2% | -57 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 137 | -0.0% | -8.63 to 8.61 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.319 | 0.31 | -2.8% | -0.0334 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 553 | 538 | -2.7% | -59.8 to 30 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.27 | -2.6% | -0.378 to 0.202 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
