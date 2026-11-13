# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.04 to -0.0368 | LOSS |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00584 to 0.00437 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,462 | 2,424 | -1.5% | -113 to 37.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,801 | 3,875 | +1.9% | -243 to 389 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.56 | -0.1% | -0.133 to 0.117 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 329 | 329 | +0.1% | -4.25 to 5.14 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,707 | 1,704 | -0.2% | -46.2 to 39.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 146 | 146 | +0.2% | -2.19 to 2.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.31 | 0.311 | +0.4% | -0.00841 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 541 | +0.7% | -12.8 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.29 | +0.9% | -0.0743 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
