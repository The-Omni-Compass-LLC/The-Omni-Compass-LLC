# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 340 | -0.5% | -5.91 to 2.35 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | +0.0% | -0.00111 to 0.00788 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,771 | +8.0% | 41.8 to 370 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,747 | 4,009 | +7.0% | 0.367 to 523 | LOSS |
| end-to-end latency, median (ms) | 8.66 | 8.57 | -1.0% | -0.582 to 0.41 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 411 | +6.5% | -28 to 78.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,685 | 1,779 | +5.6% | -2.83 to 191 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 177 | +6.1% | -7.94 to 28.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.284 | -1.1% | -0.0223 to 0.0161 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.0% | -15.7 to 11.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.5% | -0.23 to 0.199 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1 to 0.785 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00423 to 0.0054 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,351 | 2,311 | -1.7% | -229 to 150 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,745 | +2.3% | -0.0122 to 166 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.7 | -0.5% | -0.219 to 0.101 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 318 | +0.8% | -19.2 to 24.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 683 | 691 | +1.2% | -48.8 to 64.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57.5 | 58.8 | +2.2% | -3.36 to 5.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.3 | 0.296 | -1.5% | -0.0136 to 0.00463 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 529 | -1.5% | -23.7 to 7.93 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 8.11 | 8 | -1.4% | -0.308 to 0.0817 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 729 | -0.0% | -2.97 to 2.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -1.05 to 1.69 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,155 | 2,144 | -0.5% | -37 to 16.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,468 | 3,477 | +0.3% | -452 to 470 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.05 | 6.98 | -1.0% | -0.529 to 0.387 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 280 | 281 | +0.5% | -16.7 to 19.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,127 | 3,109 | -0.6% | -129 to 93.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 242 | 243 | +0.5% | -12.7 to 15.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.5% | -0.302 to 0.802 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.312 | 0.313 | +0.3% | -0.019 to 0.0208 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 560 | +0.2% | -35.2 to 37.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | +0.3% | -0.112 to 0.122 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -2.65 to 1.03 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0177 to 0.00984 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,337 | 2,429 | +4.0% | 50.2 to 135 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,787 | 3,629 | -4.2% | -451 to 135 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.56 | 8.53 | -0.3% | -0.0849 to 0.0262 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 321 | +1.5% | -14.1 to 23.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,682 | 1,676 | -0.4% | -95.1 to 82.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 141 | +1.1% | -7.97 to 11.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | +0.4% | -0.0017 to 0.00431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 535 | 539 | +0.8% | -1.85 to 10.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.28 | +1.0% | -0.00542 to 0.0734 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
