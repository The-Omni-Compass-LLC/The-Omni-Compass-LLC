# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 341 | +0.3% | -4.63 to 6.71 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00467 to 0.0017 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,584 | 2,552 | -1.2% | -436 to 373 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,044 | 3,819 | -5.6% | -1,137 to 687 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.74 | 8.73 | -0.2% | -0.365 to 0.333 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 404 | 388 | -4.0% | -98.7 to 66.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,737 | 1,697 | -2.3% | -280 to 200 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 176 | 168 | -4.3% | -42.9 to 27.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.281 | -0.8% | -0.0146 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 201 | -0.7% | -10.1 to 7.14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.26 | -1.0% | -0.144 to 0.0756 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.616 to 0.184 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00185 to 0.00298 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,553 | 2,508 | -1.8% | -247 to 157 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,769 | 3,817 | +1.3% | -180 to 276 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.6 | -0.1% | -0.171 to 0.144 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 339 | +1.1% | -7.8 to 15 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 707 | 711 | +0.6% | -18.2 to 26.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.5 | 62.1 | +0.9% | -1.49 to 2.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.296 | 0.295 | -0.5% | -0.0166 to 0.0138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 528 | -0.5% | -29.4 to 24.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 8 | 7.98 | -0.3% | -0.439 to 0.386 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1948 messages a second; base rate 292.3/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 813 | +11.4% | -100 to 266 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0134 to 0.0114 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,435 | 855 | -64.9% | -5,209 to 2,050 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,781 | 1,351 | -64.3% | -7,464 to 2,604 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.44 | 6.7 | -9.9% | -2.2 to 0.732 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 120 | -63.2% | -674 to 262 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,388 | 1,375 | -59.4% | -6,326 to 2,301 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 285 | 106 | -63.0% | -587 to 227 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | +19.3% | -0.466 to 1.24 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.323 | +2.3% | -0.0115 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 577 | +2.5% | -19.6 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.58 | -7.5% | -0.407 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -2.74 to 1.95 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0058 to 0.00413 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,386 | 2,384 | -0.1% | -240 to 236 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,746 | -0.5% | -347 to 306 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.49 | -0.6% | -0.0896 to -0.0091 | GAIN |
| end-to-end latency, mean (ms) | 323 | 321 | -0.4% | -28.8 to 26.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,685 | 1,683 | -0.1% | -69.7 to 66.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 142 | -0.3% | -13.4 to 12.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.305 | -0.7% | -0.0184 to 0.0141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 530 | -0.6% | -35.9 to 29.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.23 | -0.5% | -0.194 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
