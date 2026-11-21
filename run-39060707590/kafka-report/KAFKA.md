# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -1.76 to -0.706 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00803 to 0.00871 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,451 | -3.7% | -300 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,674 | 3,800 | +3.5% | -126 to 380 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.29 | 9.29 | +0.0% | -0.61 to 0.616 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 384 | +0.6% | -5.28 to 9.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,642 | 1,663 | +1.2% | -50.7 to 91.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 166 | +0.7% | -0.492 to 2.85 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.291 | -0.7% | -0.0178 to 0.0138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 204 | -0.6% | -11.8 to 9.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.31 | -0.2% | -0.174 to 0.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.55 to 0.784 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00316 to 0.00586 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,320 | -3.1% | -239 to 90.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,726 | 3,659 | -1.8% | -597 to 464 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.1 | 11 | -0.8% | -0.175 to -0.00388 | GAIN |
| end-to-end latency, mean (ms) | 320 | 314 | -1.8% | -33.1 to 21.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 692 | 688 | -0.6% | -50.5 to 42.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.3 | 57.7 | -2.8% | -4.93 to 1.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.27 | 0.264 | -2.5% | -0.0119 to -0.00177 | GAIN |
| host CPU-seconds | 485 | 473 | -2.5% | -21.3 to -3.01 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 7.31 | 7.12 | -2.6% | -0.338 to -0.0392 | GAIN |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1959 messages a second; base rate 293.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.2% | -2.61 to -0.00155 | LOSS |
| throughput (messages a second consumed) | 862 | 862 | -0.0% | -0.0452 to 0.0326 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,496 | 2,540 | +1.8% | -145 to 234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,871 | 3,870 | -0.0% | -335 to 334 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9 | 11.5 | +28.2% | -13 to 18.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 343 | 347 | +1.2% | -7.22 to 15.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,468 | 3,476 | +0.2% | -244 to 262 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 302 | 306 | +1.5% | -6.88 to 15.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.292 | +0.2% | -0.0378 to 0.0391 | EVEN, no difference beyond the noise |
| host CPU-seconds | 520 | 522 | +0.4% | -63.3 to 67.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.58 | 1.58 | +0.5% | -0.19 to 0.208 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -2.27 to 1.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00556 to 0.00334 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,258 | 2,285 | +1.2% | -174 to 228 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,628 | 3,569 | -1.6% | -318 to 200 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.53 | 8.52 | -0.2% | -0.1 to 0.0737 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 304 | -0.5% | -30.3 to 27.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,653 | 1,638 | -0.9% | -75.9 to 45.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 135 | -0.5% | -12.8 to 11.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.304 | -0.4% | -0.0137 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 529 | -0.2% | -26 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.22 | -0.2% | -0.141 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
