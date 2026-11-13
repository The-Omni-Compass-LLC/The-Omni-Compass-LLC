# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -2.89 to 2.29 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0191 to 0.0241 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,575 | 2,573 | -0.1% | -328 to 324 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,901 | 3,782 | -3.1% | -476 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.59 | 9.59 | -0.0% | -0.49 to 0.486 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 394 | 389 | -1.3% | -32.8 to 22.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 1,689 | -0.6% | -26.9 to 6.21 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 171 | 169 | -1.3% | -16.6 to 12.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.296 | -1.7% | -0.0204 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 207 | -1.6% | -14.3 to 7.33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.37 | -1.6% | -0.215 to 0.109 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.135 to 0.0194 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.0104 to 0.00847 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,508 | 2,476 | -1.3% | -106 to 42.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,775 | 3,739 | -0.9% | -143 to 71.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.2% | -0.139 to 0.0868 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 334 | 331 | -0.8% | -8.6 to 2.97 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 695 | -1.2% | -28.3 to 11.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.6 | 60.7 | -1.4% | -3.09 to 1.39 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.284 | -0.8% | -0.0108 to 0.00632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 513 | 509 | -0.8% | -19.2 to 11.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.74 | 7.69 | -0.7% | -0.286 to 0.174 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.0/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 724 | -0.1% | -2.88 to 0.785 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.0162 to 0.00809 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,183 | 2,269 | +4.0% | -43.6 to 217 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,633 | 3,598 | -0.9% | -246 to 177 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.29 | 8.04 | -2.9% | -0.546 to 0.0598 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 299 | 302 | +0.8% | -5.31 to 10.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,172 | 3,208 | +1.1% | -53.4 to 124 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 261 | +0.6% | -5.34 to 8.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.344 | 0.348 | +1.0% | -0.00144 to 0.00825 | EVEN, no difference beyond the noise |
| host CPU-seconds | 592 | 599 | +1.2% | -3.88 to 18.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.81 | 1.84 | +1.4% | -0.00935 to 0.0599 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -0.467 to 0.231 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.1% | -1.01 to 0.365 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,388 | 2,299 | -3.7% | -141 to -35.6 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,738 | +2.4% | -16.9 to 194 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.28 | -0.3% | -0.105 to 0.0526 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 310 | -0.8% | -15.2 to 10.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,665 | 1,669 | +0.3% | -1.59 to 10.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 137 | -1.1% | -6.62 to 3.56 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.306 | -0.6% | -0.00681 to 0.00302 | EVEN, no difference beyond the noise |
| host CPU-seconds | 550 | 548 | -0.5% | -9.51 to 3.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.6% | -0.0624 to 0.0246 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
