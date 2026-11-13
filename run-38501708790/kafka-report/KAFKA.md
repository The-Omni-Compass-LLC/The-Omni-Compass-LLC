# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 969 messages a second; base rate 109.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -0.959 to 0.613 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 416 | 417 | +0.2% | -0.879 to 2.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | -0.8% | -213 to 175 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,487 | 3,553 | +1.9% | -422 to 554 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.47 | 9.44 | -0.3% | -0.385 to 0.324 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 362 | 364 | +0.6% | -4.19 to 8.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,550 | 1,545 | -0.4% | -48.5 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 156 | 156 | -0.3% | -7.15 to 6.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.3 | +0.1% | -0.00493 to 0.00558 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 210 | +0.0% | -3.17 to 3.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.42 | +0.2% | -0.0468 to 0.0636 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.32 to 0.945 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00164 to 0.00241 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,360 | 2,341 | -0.8% | -352 to 314 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,645 | 3,698 | +1.4% | -127 to 232 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.4 | -0.1% | -0.108 to 0.0823 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 318 | +0.9% | -30.1 to 35.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 687 | 692 | +0.6% | -71.5 to 80.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57.8 | 58.4 | +1.2% | -4.32 to 5.66 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.28 | -0.5% | -0.00996 to 0.00705 | EVEN, no difference beyond the noise |
| host CPU-seconds | 505 | 502 | -0.5% | -17.6 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.63 | 7.6 | -0.4% | -0.271 to 0.209 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1944 messages a second; base rate 291.5/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 721 | -0.6% | -21.1 to 12.3 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.015 to 0.00409 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,501 | 2,986 | +19.4% | -1,299 to 2,268 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,807 | 4,559 | +19.8% | -1,401 to 2,905 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.4 | 7.38 | -0.3% | -0.267 to 0.218 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 340 | 412 | +21.3% | -168 to 313 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,456 | 3,928 | +13.6% | -1,201 to 2,144 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 296 | 357 | +20.8% | -142 to 265 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.4% | -0.0106 to -0.00421 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.5% | -0.00494 to 0.00788 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 566 | +0.7% | -7.62 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.74 | +1.3% | -0.0509 to 0.0953 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -1.34 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | +0.0% | -0.005 to 0.00691 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,364 | -1.2% | -105 to 48.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,792 | +1.7% | -206 to 332 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.31 | -0.1% | -0.15 to 0.134 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 316 | -0.9% | -22 to 16 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,693 | 1,684 | -0.6% | -151 to 132 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 139 | -1.1% | -10.3 to 7.15 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.31 | -0.5% | -0.00847 to 0.0055 | EVEN, no difference beyond the noise |
| host CPU-seconds | 556 | 553 | -0.4% | -14.9 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.36 | -0.5% | -0.0839 to 0.0521 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
