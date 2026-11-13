# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -2.75 to 2.14 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | +0.0% | -0.0128 to 0.0171 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,349 | 2,318 | -1.4% | -198 to 134 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,596 | 3,664 | +1.9% | -184 to 322 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.55 | -1.1% | -0.279 to 0.0921 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 309 | 310 | +0.5% | -19.6 to 22.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,666 | 1,647 | -1.2% | -57 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 137 | -0.0% | -8.63 to 8.61 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.319 | 0.31 | -2.8% | -0.0334 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 553 | 538 | -2.7% | -59.8 to 30 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.27 | -2.6% | -0.378 to 0.202 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
