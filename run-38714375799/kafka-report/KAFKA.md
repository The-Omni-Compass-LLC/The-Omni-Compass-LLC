# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.2% | -2.24 to 0.892 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00351 to 0.00719 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,472 | 2,602 | +5.2% | -1.7 to 261 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,858 | 3,902 | +1.1% | -595 to 683 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.59 | 9.6 | +0.0% | -0.721 to 0.724 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 392 | +2.3% | -15.7 to 33.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,668 | 1,705 | +2.2% | -154 to 229 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 169 | +1.6% | -8.83 to 14.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.299 | -1.8% | -0.0344 to 0.0235 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 210 | -1.7% | -23.8 to 16.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.42 | -1.6% | -0.397 to 0.289 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.01 to 0.522 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00418 to 0.00382 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,508 | 2,553 | +1.8% | -118 to 209 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,824 | 3,847 | +0.6% | -209 to 255 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.6 | +0.1% | -0.0507 to 0.0767 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 336 | 341 | +1.6% | -14.1 to 25.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 727 | +3.2% | 16.6 to 28.1 | LOSS |
| consumer lag, mean messages waiting | 61.1 | 62.7 | +2.5% | -1.45 to 4.51 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.6% | -0.00472 to 0.00111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 493 | 490 | -0.6% | -8.87 to 2.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.41 | -0.5% | -0.0826 to 0.012 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1956 messages a second; base rate 293.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 729 | -0.5% | -17 to 9.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 860 | 860 | -0.0% | -0.0178 to 0.00279 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,459 | 2,486 | +1.1% | -211 to 264 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,895 | 3,896 | +0.0% | -913 to 914 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 6.94 | 6.93 | -0.3% | -0.2 to 0.162 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 337 | +3.1% | -18.3 to 38.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,414 | 3,431 | +0.5% | -92.1 to 126 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 285 | 294 | +3.0% | -17.4 to 34.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.308 | 0.308 | -0.1% | -0.016 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 551 | 551 | +0.1% | -27 to 28.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.67 | 1.68 | +0.6% | -0.0513 to 0.0725 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.04 to -0.0368 | LOSS |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00584 to 0.00437 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,462 | 2,424 | -1.5% | -113 to 37.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,801 | 3,875 | +1.9% | -243 to 389 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.56 | -0.1% | -0.133 to 0.117 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 329 | 329 | +0.1% | -4.25 to 5.14 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,707 | 1,704 | -0.2% | -46.2 to 39.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 146 | 146 | +0.2% | -2.19 to 2.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.31 | 0.311 | +0.4% | -0.00841 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 541 | +0.7% | -12.8 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.29 | +0.9% | -0.0743 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
