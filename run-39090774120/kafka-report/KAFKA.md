# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.1% | -1.96 to 1.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.1% | -2.04 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,583 | -0.0% | -278 to 277 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,791 | 3,631 | -4.2% | -430 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.52 | -1.4% | -0.397 to 0.16 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 381 | -1.0% | -17 to 8.92 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,654 | -2.0% | -176 to 108 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 164 | -1.4% | -8.77 to 4.25 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.288 | 0.289 | +0.2% | -0.0186 to 0.02 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 207 | +0.3% | -13.6 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.36 | +0.4% | -0.22 to 0.245 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.18 to 0.997 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00178 to 0.00192 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,415 | 2,399 | -0.7% | -355 to 323 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,746 | 3,683 | -1.7% | -643 to 516 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | +0.0% | -0.183 to 0.184 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 319 | -1.3% | -49.8 to 41.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 708 | 691 | -2.4% | -71.7 to 37.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.4 | 58.6 | -1.4% | -6.22 to 4.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.274 | 0.273 | -0.3% | -0.00846 to 0.00706 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 489 | -0.3% | -15.2 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.4 | -0.2% | -0.207 to 0.178 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1939 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 724 | -1.3% | -43.2 to 24.7 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0432 to 0.0349 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,064 | 2,198 | +6.5% | -415 to 685 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,303 | 3,462 | +4.8% | -390 to 707 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.8 | 8.21 | -16.2% | -5.22 to 2.06 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 283 | 308 | +8.7% | -83.7 to 133 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,076 | 3,084 | +0.3% | -76.8 to 93.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 249 | 269 | +8.3% | -74.4 to 115 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.7% | -0.293 to 0.802 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.283 | 0.289 | +1.9% | -0.00832 to 0.0192 | EVEN, no difference beyond the noise |
| host CPU-seconds | 506 | 516 | +1.9% | -14.9 to 34.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.53 | 1.58 | +3.2% | -0.0564 to 0.156 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.2% | -3.22 to 2.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | +0.0% | -0.00267 to 0.00397 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,214 | 2,241 | +1.2% | -222 to 274 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,567 | 3,531 | -1.0% | -181 to 111 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.6 | -0.5% | -0.143 to 0.062 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 296 | 300 | +1.3% | -24 to 31.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,600 | 1,629 | +1.8% | -58 to 117 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 131 | 132 | +1.1% | -10.5 to 13.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.314 | -0.6% | -0.0172 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 546 | -0.4% | -28.7 to 24.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.33 | -0.3% | -0.18 to 0.163 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
