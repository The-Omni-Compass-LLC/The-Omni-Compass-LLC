# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -0.857 to -0.076 | LOSS |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.00805 to 0.0137 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,512 | 2,452 | -2.4% | -150 to 31 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,673 | 3,827 | +4.2% | -148 to 455 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.66 | 10 | +3.7% | -0.626 to 1.34 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 383 | +0.3% | -5.97 to 8.59 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,646 | 1,654 | +0.5% | -110 to 128 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 167 | +0.7% | -2.77 to 5.07 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.292 | -1.9% | -0.0225 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 204 | -1.9% | -15.6 to 7.87 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.32 | -1.7% | -0.247 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.49 to 1.29 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00127 to 0.000576 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,408 | +1.2% | -241 to 296 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,760 | 3,770 | +0.3% | -94.7 to 116 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.2% | -0.00617 to 0.0462 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 326 | +0.2% | -35.2 to 36.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 708 | 694 | -2.1% | -85.6 to 56.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.5 | 59.9 | +0.7% | -4.41 to 5.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.278 | 0.277 | -0.5% | -0.00897 to 0.00644 | EVEN, no difference beyond the noise |
| host CPU-seconds | 489 | 487 | -0.4% | -16.2 to 12 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.39 | 7.36 | -0.4% | -0.299 to 0.246 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 723 | -0.4% | -17.5 to 11.9 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.015 to 0.00839 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,244 | 2,258 | +0.6% | -311 to 340 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,655 | 3,563 | -2.5% | -437 to 254 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.27 | -3.3% | -0.741 to 0.18 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 309 | 308 | -0.3% | -34.1 to 32.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,229 | 3,164 | -2.0% | -122 to -7.7 | GAIN |
| consumer lag, mean messages waiting | 268 | 268 | -0.0% | -28.3 to 28.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.1% | -0.419 to 0.664 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.326 | 0.326 | -0.2% | -0.0248 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 559 | -0.2% | -47.7 to 45.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.72 | +0.2% | -0.161 to 0.169 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.96 to 1.39 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00881 to 0.00278 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,403 | 2,372 | -1.3% | -241 to 180 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,659 | 3,752 | +2.6% | -251 to 439 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.43 | 8.4 | -0.3% | -0.0849 to 0.0309 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 315 | -0.0% | -19.5 to 19.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,678 | 1,665 | -0.7% | -46.1 to 21.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 139 | -0.4% | -8.76 to 7.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.314 | -0.7% | -0.0143 to 0.00983 | EVEN, no difference beyond the noise |
| host CPU-seconds | 564 | 560 | -0.6% | -24.8 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.4 | -0.5% | -0.133 to 0.0983 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
