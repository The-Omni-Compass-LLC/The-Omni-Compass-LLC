# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.1% | -3.94 to 4.42 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | 0.000409 to 0.0225 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,555 | 2,577 | +0.8% | -435 to 477 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,737 | 3,588 | -4.0% | -589 to 291 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.75 | +1.9% | -1.63 to 2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 388 | 384 | -1.1% | -31.6 to 23.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,659 | 1,648 | -0.7% | -90.6 to 68.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 165 | -2.1% | -14.2 to 7.25 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -0.9% | -0.0169 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.9% | -11.4 to 7.85 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.33 | -0.9% | -0.163 to 0.0996 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.65 to 1.45 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00268 to 0.00183 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,357 | 2,346 | -0.4% | -323 to 302 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,646 | 3,606 | -1.1% | -137 to 58.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | -0.1% | -0.136 to 0.111 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 314 | -0.5% | -39.6 to 36.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 681 | 675 | -0.9% | -48.2 to 35.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57.8 | 57.2 | -1.0% | -7.3 to 6.17 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.286 | -0.3% | -0.00483 to 0.0033 | EVEN, no difference beyond the noise |
| host CPU-seconds | 505 | 504 | -0.2% | -7.46 to 4.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.64 | 7.63 | -0.2% | -0.157 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1926 messages a second; base rate 288.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 721 | -0.5% | -20.4 to 12.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0158 to 0.00724 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,228 | 2,819 | +26.5% | -2,352 to 3,534 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,502 | 4,489 | +28.2% | -3,021 to 4,994 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.39 | 8.24 | -1.8% | -0.663 to 0.363 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 298 | 381 | +27.9% | -290 to 457 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,158 | 3,777 | +19.6% | -2,267 to 3,505 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 329 | +26.7% | -243 to 381 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.326 | +0.0% | -0.00111 to 0.00135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 560 | +0.1% | -3.45 to 4.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.73 | +0.6% | -0.0394 to 0.0606 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.2% | -3.04 to 1.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | -0.0% | -0.0166 to 0.00955 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,281 | 2,282 | +0.0% | -112 to 113 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,655 | 3,647 | -0.2% | -476 to 458 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.74 | 8.6 | -1.6% | -0.362 to 0.0803 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 308 | +0.5% | -20.4 to 23.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,640 | 1,632 | -0.5% | -90.4 to 74.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 136 | +0.6% | -9.37 to 11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0773 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.327 | 0.316 | -3.4% | -0.0295 to 0.00694 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 549 | -3.5% | -53.6 to 14.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.46 | 3.35 | -3.2% | -0.337 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
