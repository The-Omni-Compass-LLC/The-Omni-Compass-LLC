# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.29 to -0.689 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.000885 to 0.00633 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,471 | -1.1% | -103 to 47.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,800 | +1.7% | -485 to 609 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.69 | 8.73 | +0.5% | -0.346 to 0.433 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 372 | 379 | +1.8% | -6.79 to 20.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,624 | 1,677 | +3.3% | -119 to 225 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 160 | 163 | +2.0% | -3.23 to 9.63 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.299 | -0.6% | -0.0122 to 0.00849 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 214 | -0.6% | -8.58 to 6.13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.5 | 3.49 | -0.3% | -0.132 to 0.112 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
