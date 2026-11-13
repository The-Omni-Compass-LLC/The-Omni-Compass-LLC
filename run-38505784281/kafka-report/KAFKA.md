# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 971 messages a second; base rate 109.2/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -1.57 to 0.776 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.00238 to 0.00859 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,481 | 2,448 | -1.4% | -252 to 185 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,568 | +1.3% | -381 to 471 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.56 | 9.36 | -2.1% | -0.505 to 0.105 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 370 | 369 | -0.2% | -5.79 to 4.12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,619 | 1,580 | -2.4% | -118 to 39.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 159 | 158 | -0.6% | -2.32 to 0.305 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.3 | 0.294 | -2.2% | -0.0289 to 0.016 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 205 | -2.2% | -20.5 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.35 | -2.1% | -0.341 to 0.199 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.598 to 0.69 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00852 to 0.0138 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,245 | -2.5% | -111 to -6.15 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,540 | 3,486 | -1.5% | -76.3 to -31.6 | GAIN |
| end-to-end latency, median (ms) | 10.9 | 11 | +0.6% | -0.521 to 0.648 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 298 | -2.3% | -22.7 to 8.63 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 687 | 658 | -4.2% | -52.7 to -5.3 | GAIN |
| consumer lag, mean messages waiting | 55.8 | 54.6 | -2.2% | -3.7 to 1.29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.261 | 0.262 | +0.4% | -0.0174 to 0.0198 | EVEN, no difference beyond the noise |
| host CPU-seconds | 467 | 469 | +0.4% | -30.8 to 34.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.05 | 7.08 | +0.4% | -0.472 to 0.531 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1944 messages a second; base rate 291.6/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 728 | +0.1% | -4.02 to 5.06 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | +0.0% | -0.0906 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,475 | 2,437 | -1.5% | -324 to 248 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,889 | 3,770 | -3.1% | -224 to -14 | GAIN |
| end-to-end latency, median (ms) | 7.45 | 7.33 | -1.6% | -0.17 to -0.0627 | GAIN |
| end-to-end latency, mean (ms) | 337 | 328 | -2.8% | -43.4 to 24.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,408 | 3,376 | -0.9% | -145 to 82.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 294 | 285 | -2.9% | -37.6 to 20.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.7% | -0.308 to 0.815 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.315 | 0.315 | -0.1% | -0.00864 to 0.00816 | EVEN, no difference beyond the noise |
| host CPU-seconds | 561 | 561 | +0.0% | -13.2 to 13.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | -0.0% | -0.0375 to 0.0359 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.3/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.2% | -1.94 to 0.724 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.0148 to 0.0129 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,445 | 2,419 | -1.0% | -207 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,712 | 3,768 | +1.5% | -352 to 466 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.02 | 8.03 | +0.1% | -0.183 to 0.201 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 331 | +1.3% | -17.1 to 25.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,735 | +1.8% | -16.9 to 79.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 148 | +2.2% | -6.07 to 12.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.271 | 0.269 | -0.8% | -0.00464 to 0.000172 | EVEN, no difference beyond the noise |
| host CPU-seconds | 485 | 481 | -0.7% | -8.35 to 1.35 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.93 | 2.91 | -0.6% | -0.0556 to 0.0229 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
