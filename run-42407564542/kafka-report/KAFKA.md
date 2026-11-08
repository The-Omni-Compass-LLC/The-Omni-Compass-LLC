# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 417 | +22.5% | 70 to 83.4 | GAIN |
| throughput (messages a second consumed) | 418 | 419 | +0.2% | -0.9 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,516 | 11.7 | -99.5% | -2,685 to -2,323 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,690 | 299 | -91.9% | -4,643 to -2,140 | GAIN |
| end-to-end latency, median (ms) | 9.16 | 8.14 | -11.1% | -1.28 to -0.763 | GAIN |
| end-to-end latency, mean (ms) | 378 | 16.2 | -95.7% | -393 to -331 | GAIN |
| consumer lag, most messages waiting at once | 1,651 | 291 | -82.4% | -2,174 to -545 | GAIN |
| consumer lag, mean messages waiting | 163 | 7.08 | -95.7% | -169 to -143 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.17 | +158.6% | 1.76 to 4.58 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.316 | 0.337 | +6.9% | 0.00479 to 0.0386 | power given |
| host CPU-seconds | 222 | 237 | +6.5% | 2.08 to 27 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.61 | 3.15 | -12.9% | -0.605 to -0.326 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.6 to 25.8 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00108 to 0.00164 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,500 | 12.5 | -99.5% | -2,555 to -2,419 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,830 | 36.5 | -99.0% | -4,011 to -3,576 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.5% | -0.291 to -0.28 | GAIN |
| end-to-end latency, mean (ms) | 335 | 11.9 | -96.5% | -325 to -322 | GAIN |
| consumer lag, most messages waiting at once | 715 | 45 | -93.7% | -767 to -573 | GAIN |
| consumer lag, mean messages waiting | 61.2 | 2.08 | -96.6% | -60.9 to -57.3 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.75 | +137.5% | 2.51 to 2.99 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.288 | 0.296 | +2.8% | 0.00308 to 0.0132 | power given |
| host CPU-seconds | 509 | 523 | +2.7% | 4.83 to 22.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 6.71 | -12.5% | -1.13 to -0.797 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1923 messages a second; base rate 288.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 845 | +16.6% | 116 to 125 | GAIN |
| throughput (messages a second consumed) | 846 | 846 | -0.0% | -0.0326 to 0.0134 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,185 | 9.25 | -99.6% | -2,216 to -2,137 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,510 | 11.3 | -99.7% | -3,809 to -3,189 | GAIN |
| end-to-end latency, median (ms) | 7.83 | 6.08 | -22.3% | -2.03 to -1.47 | GAIN |
| end-to-end latency, mean (ms) | 290 | 7.9 | -97.3% | -295 to -268 | GAIN |
| consumer lag, most messages waiting at once | 3,131 | 194 | -93.8% | -3,491 to -2,382 | GAIN |
| consumer lag, mean messages waiting | 250 | 6.95 | -97.2% | -256 to -231 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.72 | +185.9% | 2.46 to 4.97 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.343 | 0.391 | +14.2% | 0.0401 to 0.0569 | power given |
| host CPU-seconds | 594 | 681 | +14.6% | 72.5 to 100 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.79 | -1.8% | -0.0798 to 0.0155 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 428 | +16.9% | 59.7 to 64 | GAIN |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00374 to 0.00373 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,305 | 9.85 | -99.6% | -2,334 to -2,257 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,562 | 18.1 | -99.5% | -3,763 to -3,326 | GAIN |
| end-to-end latency, median (ms) | 8.3 | 7.1 | -14.5% | -1.92 to -0.491 | GAIN |
| end-to-end latency, mean (ms) | 301 | 8.94 | -97.0% | -302 to -283 | GAIN |
| consumer lag, most messages waiting at once | 1,645 | 128 | -92.2% | -2,002 to -1,033 | GAIN |
| consumer lag, mean messages waiting | 133 | 3.98 | -97.0% | -133 to -125 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.97 | +148.6% | 0.789 to 5.15 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.308 | 0.322 | +4.3% | -0.0124 to 0.0391 | STEADY, no difference beyond the noise |
| host CPU-seconds | 549 | 571 | +4.1% | -23.2 to 68.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 2.96 | -10.9% | -0.616 to -0.109 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
