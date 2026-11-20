# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 985 messages a second; base rate 110.8/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 421 | +22.8% | 65.1 to 91.2 | GAIN |
| throughput (messages a second consumed) | 423 | 424 | +0.2% | -0.908 to 2.45 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,708 | 10.6 | -99.6% | -2,802 to -2,594 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,057 | 601 | -85.2% | -5,883 to -1,028 | GAIN |
| end-to-end latency, median (ms) | 8.69 | 7.47 | -14.0% | -1.94 to -0.499 | GAIN |
| end-to-end latency, mean (ms) | 409 | 19.4 | -95.2% | -458 to -321 | GAIN |
| consumer lag, most messages waiting at once | 1,784 | 400 | -77.6% | -2,937 to 169 | STEADY, no difference beyond the noise |
| consumer lag, mean messages waiting | 178 | 8.57 | -95.2% | -197 to -142 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.25 | +162.5% | 1.82 to 4.68 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.278 | 0.29 | +4.3% | 0.00511 to 0.0188 | power given |
| host CPU-seconds | 199 | 207 | +3.8% | 2.66 to 12.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 2.72 | -15.3% | -0.512 to -0.469 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 171 | +17.1% | 23.6 to 26.4 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00431 to 0.00274 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,382 | 12.1 | -99.5% | -2,947 to -1,793 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,773 | 20.7 | -99.5% | -5,038 to -2,467 | GAIN |
| end-to-end latency, median (ms) | 11.2 | 11 | -1.3% | -0.156 to -0.124 | GAIN |
| end-to-end latency, mean (ms) | 318 | 11.9 | -96.3% | -405 to -207 | GAIN |
| consumer lag, most messages waiting at once | 713 | 64 | -91.0% | -933 to -365 | GAIN |
| consumer lag, mean messages waiting | 58.1 | 2 | -96.6% | -73.2 to -38.9 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.66 | +132.8% | 1.4 to 3.92 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.276 | 0.281 | +2.1% | 0.00101 to 0.0106 | power given |
| host CPU-seconds | 492 | 502 | +2.0% | 1.48 to 18.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 6.51 | -12.8% | -1.07 to -0.853 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1882 messages a second; base rate 282.3/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 743 | 827 | +11.3% | 82 to 86.2 | GAIN |
| throughput (messages a second consumed) | 828 | 828 | -0.0% | -0.0156 to 0.00373 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,314 | 8.53 | -99.4% | -1,366 to -1,246 | GAIN |
| end-to-end latency, 99th percentile (ms) | 2,294 | 9.89 | -99.6% | -2,347 to -2,221 | GAIN |
| end-to-end latency, median (ms) | 6.8 | 5.52 | -18.8% | -1.51 to -1.04 | GAIN |
| end-to-end latency, mean (ms) | 159 | 6.69 | -95.8% | -154 to -149 | GAIN |
| consumer lag, most messages waiting at once | 2,220 | 128 | -94.3% | -2,450 to -1,735 | GAIN |
| consumer lag, mean messages waiting | 135 | 5.54 | -95.9% | -132 to -127 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.46 | +173.2% | 1.36 to 5.56 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.326 | 0.346 | +6.1% | 0.0132 to 0.0265 | power given |
| host CPU-seconds | 597 | 622 | +4.3% | 13.8 to 38.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.78 | 1.67 | -6.3% | -0.142 to -0.0817 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.2% | 61.3 to 65.1 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00671 to -0.000368 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,365 | 9.54 | -99.6% | -2,424 to -2,287 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,704 | 11.1 | -99.7% | -3,986 to -3,401 | GAIN |
| end-to-end latency, median (ms) | 8.07 | 6.91 | -14.4% | -1.93 to -0.404 | GAIN |
| end-to-end latency, mean (ms) | 318 | 7.43 | -97.7% | -327 to -295 | GAIN |
| consumer lag, most messages waiting at once | 1,679 | 105 | -93.7% | -2,030 to -1,118 | GAIN |
| consumer lag, mean messages waiting | 141 | 3.32 | -97.7% | -146 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.3% | 1.48 to 4.57 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.279 | 0.309 | +10.8% | 0.000657 to 0.0598 | power given |
| host CPU-seconds | 497 | 550 | +10.6% | 0.37 to 105 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3 | 2.83 | -5.6% | -0.462 to 0.123 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
