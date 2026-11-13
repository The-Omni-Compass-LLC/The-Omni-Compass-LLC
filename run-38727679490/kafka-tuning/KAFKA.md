# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.41 to 0.968 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00962 to 0.00783 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,323 | 2,330 | +0.3% | -145 to 158 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,736 | 3,645 | -2.4% | -215 to 34.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.65 | 8.59 | -0.8% | -0.169 to 0.0354 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 312 | +0.4% | -17.9 to 20.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,660 | 1,658 | -0.1% | -84.4 to 80.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 138 | +0.5% | -7.54 to 8.92 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.314 | -1.4% | -0.0245 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 552 | 545 | -1.3% | -44.3 to 30.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.31 | -1.2% | -0.259 to 0.178 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
