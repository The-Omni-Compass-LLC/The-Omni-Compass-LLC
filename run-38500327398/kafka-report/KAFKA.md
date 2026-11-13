# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.29 to -0.689 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.000885 to 0.00633 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,471 | -1.1% | -103 to 47.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,800 | +1.7% | -485 to 609 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.69 | 8.73 | +0.5% | -0.346 to 0.433 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 372 | 379 | +1.8% | -6.79 to 20.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,624 | 1,677 | +3.3% | -119 to 225 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 160 | 163 | +2.0% | -3.23 to 9.63 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.299 | -0.6% | -0.0122 to 0.00849 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 214 | -0.6% | -8.58 to 6.13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.5 | 3.49 | -0.3% | -0.132 to 0.112 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.606 to 0.794 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00507 to 0.00452 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,496 | 2,420 | -3.0% | -132 to -19.8 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,886 | 3,733 | -3.9% | -811 to 506 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.6% | -0.329 to 0.183 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 338 | 326 | -3.5% | -37.8 to 14 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 715 | 700 | -2.1% | -74.2 to 44.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.6 | 59.8 | -3.0% | -5.96 to 2.31 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.284 | 0.278 | -2.1% | -0.0265 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 489 | -2.1% | -47.2 to 26.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.55 | 7.38 | -2.2% | -0.704 to 0.376 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.2% | -3.27 to 0.881 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0255 to 0.0105 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,313 | 2,419 | +4.6% | -45.8 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,779 | 3,594 | -4.9% | -674 to 303 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.17 | 7.13 | -0.6% | -0.422 to 0.331 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 312 | +0.2% | -3.43 to 4.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,307 | 3,308 | +0.1% | -48.3 to 51.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 271 | 271 | +0.0% | -4.41 to 4.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.32 | 0.318 | -0.5% | -0.0129 to 0.00943 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 569 | -0.4% | -23.5 to 18.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.73 | -0.2% | -0.0674 to 0.0589 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.71 to 0.826 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -1.19 to 1.18 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,200 | 2,195 | -0.2% | -217 to 208 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,548 | 3,572 | +0.7% | -75.3 to 123 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.27 | -0.5% | -0.199 to 0.121 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 291 | 292 | +0.3% | -22.7 to 24.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,603 | 1,606 | +0.1% | -108 to 112 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 128 | 128 | +0.0% | -10.9 to 10.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.306 | -0.8% | -0.0107 to 0.00581 | EVEN, no difference beyond the noise |
| host CPU-seconds | 551 | 546 | -0.8% | -18.2 to 8.96 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.7% | -0.12 to 0.0722 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
