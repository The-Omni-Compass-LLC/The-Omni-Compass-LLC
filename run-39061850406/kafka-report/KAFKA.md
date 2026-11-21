# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 339 | -0.8% | -10.3 to 4.57 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00747 to 0.0123 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,491 | 2,563 | +2.9% | -449 to 592 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,582 | 3,843 | +7.3% | -109 to 632 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.87 | 8.7 | -2.0% | -1.52 to 1.17 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 373 | 392 | +5.3% | -28.2 to 67.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,607 | 1,688 | +5.1% | -187 to 350 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 161 | 170 | +5.5% | -9.86 to 27.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.4% | -0.0957 to 0.11 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.284 | -0.3% | -0.0135 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | -0.3% | -9.45 to 8.41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.33 | +0.6% | -0.0579 to 0.0974 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.265 to 0.149 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00326 to 0.00271 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,351 | -1.2% | -103 to 46.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,705 | 3,650 | -1.5% | -405 to 295 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.9 | 11.8 | -0.6% | -0.354 to 0.207 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 314 | -1.4% | -7.53 to -1.1 | GAIN |
| consumer lag, most messages waiting at once | 700 | 683 | -2.4% | -63.7 to 30.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.5 | 57.7 | -1.4% | -1.42 to -0.157 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.293 | -1.5% | -0.0213 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 524 | 517 | -1.5% | -37.1 to 21.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.93 | 7.82 | -1.4% | -0.557 to 0.33 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.1/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -3.79 to 0.856 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.015 to 0.00416 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,382 | 2,362 | -0.8% | -110 to 69.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,653 | 3,652 | -0.0% | -369 to 368 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.46 | 8.07 | -4.6% | -1.53 to 0.759 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 318 | -0.6% | -25.7 to 21.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,282 | 3,291 | +0.3% | -111 to 129 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 276 | -0.9% | -24.2 to 19.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.334 | 0.334 | -0.0% | -0.013 to 0.0129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 573 | 575 | +0.5% | -21.1 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.76 | +0.7% | -0.0574 to 0.0804 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -2.51 to 2.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0202 to 0.0149 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,498 | 2,434 | -2.6% | -140 to 12.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,727 | 3,833 | +2.8% | -18.1 to 229 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.6 | +0.5% | -0.0351 to 0.121 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 326 | -0.7% | -20.6 to 16.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,701 | -0.2% | -49 to 43 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 144 | -1.0% | -7.98 to 5.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.314 | 0.32 | +1.8% | 0.000703 to 0.0105 | power given |
| host CPU-seconds | 545 | 556 | +1.9% | 2.71 to 17.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.37 | +1.9% | -0.00153 to 0.127 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
