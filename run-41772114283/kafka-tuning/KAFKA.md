# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 967 messages a second; base rate 145.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 425 | +16.0% | 56.2 to 60.8 | GAIN |
| throughput (messages a second consumed) | 426 | 425 | -0.0% | -0.0185 to 0.0109 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,991 | 9.92 | -99.5% | -2,081 to -1,881 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,255 | 23.3 | -99.3% | -3,333 to -3,132 | GAIN |
| end-to-end latency, median (ms) | 8.19 | 7.19 | -12.2% | -1.17 to -0.83 | GAIN |
| end-to-end latency, mean (ms) | 261 | 8.61 | -96.7% | -270 to -233 | GAIN |
| consumer lag, most messages waiting at once | 1,489 | 134 | -91.0% | -1,425 to -1,285 | GAIN |
| consumer lag, mean messages waiting | 115 | 4.09 | -96.4% | -118 to -103 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.86 | +142.8% | 2.19 to 3.52 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.294 | 0.305 | +3.6% | 0.00432 to 0.017 | power given |
| host CPU-seconds | 524 | 542 | +3.4% | 5.04 to 31 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.18 | 2.83 | -10.8% | -0.44 to -0.246 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
