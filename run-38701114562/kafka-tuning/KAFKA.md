# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -0.467 to 0.231 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.1% | -1.01 to 0.365 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,388 | 2,299 | -3.7% | -141 to -35.6 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,738 | +2.4% | -16.9 to 194 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.28 | -0.3% | -0.105 to 0.0526 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 310 | -0.8% | -15.2 to 10.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,665 | 1,669 | +0.3% | -1.59 to 10.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 137 | -1.1% | -6.62 to 3.56 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.306 | -0.6% | -0.00681 to 0.00302 | EVEN, no difference beyond the noise |
| host CPU-seconds | 550 | 548 | -0.5% | -9.51 to 3.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.6% | -0.0624 to 0.0246 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
