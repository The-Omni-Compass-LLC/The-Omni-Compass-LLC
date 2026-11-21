# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -2 to -0.209 | LOSS |
| throughput (messages a second consumed) | 419 | 418 | -0.1% | -2.04 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,521 | 2,478 | -1.7% | -108 to 21.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,594 | 3,738 | +4.0% | 111 to 176 | LOSS |
| end-to-end latency, median (ms) | 9.41 | 9.63 | +2.4% | -0.582 to 1.04 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 378 | 380 | +0.6% | -1.45 to 5.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,619 | 1,630 | +0.7% | -94.2 to 116 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.4% | -0.464 to 1.62 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.298 | 0.292 | -1.9% | -0.0238 to 0.0126 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 204 | -1.8% | -16.4 to 8.99 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.33 | -1.6% | -0.246 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.34 to 0.924 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.0035 to 0.00242 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,539 | 2,575 | +1.4% | -102 to 175 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,923 | 3,818 | -2.7% | -582 to 373 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.6 | +0.4% | -0.116 to 0.201 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 346 | 347 | +0.2% | -32.6 to 34.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 725 | 737 | +1.7% | -14.3 to 38.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 63.6 | 64.1 | +0.8% | -5.17 to 6.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.281 | +0.1% | -0.0115 to 0.0118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 494 | +0.1% | -20.3 to 20.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.46 | +0.2% | -0.239 to 0.268 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.1/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 726 | +0.1% | -1.4 to 3 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.0239 to 0.0438 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,377 | 2,309 | -2.9% | -275 to 139 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,667 | +0.1% | -350 to 360 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.48 | 8.5 | +0.3% | -0.343 to 0.391 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 316 | -2.0% | -15.4 to 2.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,308 | 3,279 | -0.9% | -83.1 to 23.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 281 | 275 | -2.0% | -12.5 to 1.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.332 | 0.326 | -1.7% | -0.0259 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 559 | -1.7% | -43.1 to 24.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.71 | -1.8% | -0.136 to 0.074 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -0.704 to 0.908 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0123 to 0.00796 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,386 | 2,383 | -0.1% | -90.5 to 84.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,771 | 3,696 | -2.0% | -400 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.54 | +0.3% | -0.134 to 0.178 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 319 | -0.9% | -17.4 to 11.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,689 | 1,675 | -0.9% | -42.6 to 13.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 141 | -0.7% | -9.02 to 7.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.309 | 0.308 | -0.4% | -0.0153 to 0.0131 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 534 | -0.6% | -29.4 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.24 | -0.6% | -0.185 to 0.147 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
