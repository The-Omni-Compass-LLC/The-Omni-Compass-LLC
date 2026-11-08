# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +16.8% | 23.4 to 25.9 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.000972 to 0.000374 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,261 | 12.1 | -99.5% | -2,441 to -2,057 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,453 | 16.8 | -99.5% | -3,474 to -3,397 | GAIN |
| end-to-end latency, median (ms) | 11.2 | 11 | -1.5% | -0.209 to -0.128 | GAIN |
| end-to-end latency, mean (ms) | 299 | 15 | -95.0% | -306 to -263 | GAIN |
| consumer lag, most messages waiting at once | 670 | 161 | -75.9% | -625 to -393 | GAIN |
| consumer lag, mean messages waiting | 54.9 | 2.71 | -95.1% | -55.6 to -48.7 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.55 | +77.5% | 1.01 to 2.09 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.28 | 0.284 | +1.3% | -0.00272 to 0.0103 | STEADY, no difference beyond the noise |
| host CPU-seconds | 505 | 511 | +1.2% | -5.46 to 17.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.63 | 6.61 | -13.3% | -1.15 to -0.888 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
