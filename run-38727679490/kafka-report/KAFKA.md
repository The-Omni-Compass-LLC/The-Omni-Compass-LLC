# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -1.28 to 0.446 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0393 to 0.0406 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,511 | -0.2% | -86.3 to 76.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,795 | 3,699 | -2.5% | -789 to 598 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.78 | 9.67 | -1.1% | -1.91 to 1.7 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 384 | -0.1% | -20.1 to 19.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,654 | 1,656 | +0.1% | -17.6 to 22.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 166 | +0.3% | -7.5 to 8.45 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.31 | 0.302 | -2.6% | -0.043 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 212 | -2.6% | -30.2 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.45 | -2.5% | -0.493 to 0.316 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.24 to 0.231 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.000708 to 8.02e-05 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,462 | 2,562 | +4.1% | -75.7 to 276 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,870 | 3,808 | -1.6% | -364 to 241 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.0437 to 0.023 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 332 | 342 | +3.1% | -11.1 to 31.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 698 | 725 | +3.9% | -15 to 69.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.1 | 62.7 | +2.6% | -1.71 to 4.89 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.284 | +0.2% | -0.00897 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 501 | +0.3% | -16.2 to 19.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.57 | +0.7% | -0.204 to 0.303 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1928 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 722 | 767 | +6.2% | -129 to 219 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | +0.0% | -0.0142 to 0.0178 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,454 | 1,456 | -40.7% | -3,929 to 1,932 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,900 | 2,288 | -41.3% | -6,443 to 3,219 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.56 | 7.23 | -4.3% | -1.21 to 0.558 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 194 | -41.3% | -521 to 248 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,362 | 2,163 | -35.7% | -4,976 to 2,579 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 168 | -41.3% | -448 to 212 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.31 | +15.6% | -0.41 to 1.03 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.325 | -0.9% | -0.0274 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 584 | 579 | -0.8% | -43.2 to 33.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.68 | -6.2% | -0.375 to 0.15 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.41 to 0.968 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00962 to 0.00783 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,323 | 2,330 | +0.3% | -145 to 158 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,736 | 3,645 | -2.4% | -215 to 34.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.65 | 8.59 | -0.8% | -0.169 to 0.0354 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 312 | +0.4% | -17.9 to 20.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,660 | 1,658 | -0.1% | -84.4 to 80.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 138 | +0.5% | -7.54 to 8.92 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.314 | -1.4% | -0.0245 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 552 | 545 | -1.3% | -44.3 to 30.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.31 | -1.2% | -0.259 to 0.178 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
