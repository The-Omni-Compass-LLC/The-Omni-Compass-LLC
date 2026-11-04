# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 429 | +17.3% | 61.7 to 64.9 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0115 to 0.00554 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 10.5 | -99.6% | -2,532 to -2,348 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,773 | 16.6 | -99.6% | -3,976 to -3,537 | GAIN |
| end-to-end latency, median (ms) | 8.52 | 7.44 | -12.6% | -1.27 to -0.884 | GAIN |
| end-to-end latency, mean (ms) | 325 | 8.83 | -97.3% | -322 to -311 | GAIN |
| consumer lag, most messages waiting at once | 1,714 | 120 | -93.0% | -2,014 to -1,174 | GAIN |
| consumer lag, mean messages waiting | 144 | 3.87 | -97.3% | -142 to -137 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.36 | +167.8% | 2.44 to 4.27 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.326 | 0.347 | +6.4% | 0.0098 to 0.0319 | power given |
| host CPU-seconds | 571 | 607 | +6.4% | 17.6 to 55.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.14 | -9.3% | -0.424 to -0.22 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
