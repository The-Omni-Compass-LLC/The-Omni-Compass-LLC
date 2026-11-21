# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 964 messages a second; base rate 108.4/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 337 | -0.6% | -8.77 to 4.74 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 414 | 414 | -0.0% | -0.00746 to 0.0011 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,167 | 2,241 | +3.4% | -154 to 302 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,215 | 3,374 | +4.9% | -101 to 418 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.49 | -1.2% | -0.589 to 0.376 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 337 | +2.7% | -18.8 to 36.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,442 | 1,445 | +0.2% | -16 to 21.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 144 | +2.6% | -8.74 to 16.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.7% | -0.0226 to -0.00684 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.285 | -0.0% | -0.0186 to 0.0186 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | +0.1% | -13.1 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.35 | +0.7% | -0.172 to 0.215 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.11 to 0.726 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.1% | -0.147 to 0.402 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,457 | 2,455 | -0.1% | -72.6 to 70.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,797 | 3,802 | +0.1% | -160 to 170 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | +0.2% | -0.116 to 0.165 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 334 | +1.3% | -7.65 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 690 | 704 | +2.0% | -13.7 to 41.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.3 | 61.5 | +2.0% | -3.42 to 5.88 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.286 | +0.0% | -0.0161 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 505 | 504 | -0.0% | -30.7 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.62 | 7.64 | +0.2% | -0.483 to 0.512 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724 | 725 | +0.1% | -11.5 to 13.1 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0129 to 0.0101 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,507 | 2,497 | -0.4% | -1,011 to 990 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,815 | 3,922 | +2.8% | -1,256 to 1,470 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.44 | 7.35 | -1.2% | -0.155 to -0.0168 | GAIN |
| end-to-end latency, mean (ms) | 336 | 338 | +0.6% | -138 to 142 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,396 | 3,432 | +1.1% | -1,261 to 1,332 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 293 | 294 | +0.4% | -126 to 128 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.03 | +1.6% | -0.136 to 0.201 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.314 | 0.311 | -1.1% | -0.00873 to 0.00156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 561 | 555 | -1.0% | -13.9 to 2.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.7 | -1.1% | -0.0718 to 0.0334 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 964 messages a second; base rate 144.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -2.37 to 2.08 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.835 to 0.519 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,989 | 1,925 | -3.2% | -252 to 124 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,213 | 3,224 | +0.3% | -241 to 264 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.53 | -0.5% | -0.109 to 0.0194 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 260 | 258 | -0.6% | -19.7 to 16.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,501 | 1,486 | -1.0% | -53 to 22.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 114 | 113 | -0.5% | -8.99 to 7.95 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.6% | -0.306 to 0.811 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.306 | 0.303 | -1.2% | -0.017 to 0.00991 | EVEN, no difference beyond the noise |
| host CPU-seconds | 532 | 526 | -1.1% | -30.6 to 18.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.2 | -1.1% | -0.175 to 0.102 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
