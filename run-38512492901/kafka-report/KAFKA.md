# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -5.06 to 2.76 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0175 to 0.0205 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,525 | 2,573 | +1.9% | -260 to 355 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,755 | 3,843 | +2.4% | 15.5 to 162 | LOSS |
| end-to-end latency, median (ms) | 9.78 | 9.54 | -2.4% | -1.94 to 1.47 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 388 | 396 | +2.1% | -33.4 to 49.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,680 | 1,690 | +0.6% | -54.2 to 73.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 172 | +2.2% | -15.1 to 22.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.298 | 0.294 | -1.4% | -0.0345 to 0.026 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 206 | -1.4% | -24.6 to 18.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.35 | -1.1% | -0.41 to 0.336 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 388 messages a second; base rate 58.3/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 154 | +5.7% | -27.7 to 44.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00207 to 0.00443 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,150 | 1,383 | -35.7% | -3,813 to 2,278 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,459 | 2,143 | -38.0% | -5,984 to 3,351 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -1.6% | -0.472 to 0.117 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 290 | 186 | -35.7% | -507 to 299 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 640 | 433 | -32.4% | -1,036 to 622 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52.9 | 34 | -35.7% | -93.8 to 56.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.36 | +18.0% | -0.506 to 1.23 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.28 | 0.274 | -1.9% | -0.00803 to -0.00253 | GAIN |
| host CPU-seconds | 501 | 491 | -1.9% | -14.5 to -4.51 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 7.62 | 7.1 | -6.8% | -2.2 to 1.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1923 messages a second; base rate 288.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 720 | -0.6% | -18 to 8.82 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | +0.0% | -0.0191 to 0.0216 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,156 | 2,204 | +2.2% | -58.8 to 155 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,438 | 3,456 | +0.5% | -103 to 140 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 7.95 | -3.1% | -0.841 to 0.325 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 291 | 299 | +2.9% | -15.8 to 32.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,117 | 3,143 | +0.8% | -70.9 to 122 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 252 | 258 | +2.5% | -16.6 to 29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.5% | -0.293 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.33 | 0.329 | -0.3% | -0.0148 to 0.0128 | EVEN, no difference beyond the noise |
| host CPU-seconds | 567 | 566 | -0.2% | -27 to 24.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | +0.4% | -0.0432 to 0.0577 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -0.702 to 0.143 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00599 to 0.00239 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,344 | -0.1% | -153 to 150 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,634 | 3,640 | +0.2% | -75.5 to 87.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.71 | 8.67 | -0.5% | -0.28 to 0.193 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 309 | -0.2% | -13.4 to 12.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,678 | +0.5% | -92.2 to 109 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 136 | 136 | -0.2% | -6.31 to 5.87 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.321 | -2.0% | -0.0396 to 0.0264 | EVEN, no difference beyond the noise |
| host CPU-seconds | 568 | 558 | -1.8% | -70.6 to 50.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.45 | 3.39 | -1.7% | -0.429 to 0.312 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
