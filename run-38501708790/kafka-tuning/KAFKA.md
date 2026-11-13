# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -1.34 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | +0.0% | -0.005 to 0.00691 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,364 | -1.2% | -105 to 48.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,792 | +1.7% | -206 to 332 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.31 | -0.1% | -0.15 to 0.134 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 316 | -0.9% | -22 to 16 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,693 | 1,684 | -0.6% | -151 to 132 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 139 | -1.1% | -10.3 to 7.15 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.31 | -0.5% | -0.00847 to 0.0055 | EVEN, no difference beyond the noise |
| host CPU-seconds | 556 | 553 | -0.4% | -14.9 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.36 | -0.5% | -0.0839 to 0.0521 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
