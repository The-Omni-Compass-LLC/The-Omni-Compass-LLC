# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.2% | -1.74 to 0.239 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00706 to 0.00938 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,503 | 2,495 | -0.3% | -58.1 to 42.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,634 | -1.0% | -109 to 35 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.52 | 9.35 | -1.8% | -0.338 to 0.00219 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 384 | +0.5% | -7.01 to 10.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,661 | 1,635 | -1.6% | -125 to 73.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 165 | -0.1% | -6.2 to 5.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.291 | -1.3% | -0.0149 to 0.0073 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.3% | -10.5 to 4.93 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.31 | -1.1% | -0.172 to 0.0964 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.694 to 0.45 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.0017 to 0.000991 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,297 | -0.3% | -103 to 89.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,566 | 3,577 | +0.3% | -199 to 223 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.4% | -0.181 to 0.0823 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 309 | +0.6% | -17.2 to 20.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 667 | 671 | +0.6% | -40.2 to 48.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.3 | 56.6 | +0.6% | -2.32 to 2.99 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.278 | -1.5% | -0.0186 to 0.00997 | EVEN, no difference beyond the noise |
| host CPU-seconds | 498 | 490 | -1.5% | -32.8 to 17.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.41 | -1.4% | -0.481 to 0.267 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.0/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 715 | -1.5% | -38.2 to 16.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0231 to 0.0223 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,187 | 2,270 | +3.8% | -232 to 400 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,462 | 3,603 | +4.1% | -284 to 566 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.24 | -2.9% | -1.62 to 1.13 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 297 | 322 | +8.4% | -58 to 108 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,170 | 3,144 | -0.8% | -244 to 191 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 258 | 279 | +8.3% | -51 to 93.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.13 | +6.3% | -0.417 to 0.669 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.325 | 0.325 | -0.0% | -0.0103 to 0.00997 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 559 | +0.1% | -14.5 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.74 | +1.6% | -0.0172 to 0.0715 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.52 to 0.52 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0111 to 0.0117 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,444 | 2,432 | -0.5% | -38.9 to 13.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,785 | 3,780 | -0.1% | -556 to 547 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.53 | -0.2% | -0.106 to 0.0704 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 330 | +0.9% | -10.1 to 15.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,713 | +0.5% | -49.3 to 66.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 146 | +0.5% | -6.16 to 7.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.311 | +0.0% | -0.0264 to 0.0265 | EVEN, no difference beyond the noise |
| host CPU-seconds | 540 | 541 | +0.1% | -50.8 to 52.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.28 | 3.29 | +0.3% | -0.295 to 0.312 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
