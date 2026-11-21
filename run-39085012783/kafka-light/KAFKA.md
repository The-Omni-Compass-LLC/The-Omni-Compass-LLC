# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1948 messages a second; base rate 292.3/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 813 | +11.4% | -100 to 266 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0134 to 0.0114 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,435 | 855 | -64.9% | -5,209 to 2,050 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,781 | 1,351 | -64.3% | -7,464 to 2,604 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.44 | 6.7 | -9.9% | -2.2 to 0.732 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 120 | -63.2% | -674 to 262 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,388 | 1,375 | -59.4% | -6,326 to 2,301 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 285 | 106 | -63.0% | -587 to 227 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | +19.3% | -0.466 to 1.24 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.323 | +2.3% | -0.0115 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 577 | +2.5% | -19.6 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.58 | -7.5% | -0.407 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
