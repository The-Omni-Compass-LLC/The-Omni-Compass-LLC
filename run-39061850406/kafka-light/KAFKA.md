# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.1/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -3.79 to 0.856 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.015 to 0.00416 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,382 | 2,362 | -0.8% | -110 to 69.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,653 | 3,652 | -0.0% | -369 to 368 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.46 | 8.07 | -4.6% | -1.53 to 0.759 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 318 | -0.6% | -25.7 to 21.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,282 | 3,291 | +0.3% | -111 to 129 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 276 | -0.9% | -24.2 to 19.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.334 | 0.334 | -0.0% | -0.013 to 0.0129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 573 | 575 | +0.5% | -21.1 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.76 | +0.7% | -0.0574 to 0.0804 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
