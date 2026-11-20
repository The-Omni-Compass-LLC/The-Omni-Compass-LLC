# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 171 | +17.1% | 23.6 to 26.4 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00431 to 0.00274 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,382 | 12.1 | -99.5% | -2,947 to -1,793 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,773 | 20.7 | -99.5% | -5,038 to -2,467 | GAIN |
| end-to-end latency, median (ms) | 11.2 | 11 | -1.3% | -0.156 to -0.124 | GAIN |
| end-to-end latency, mean (ms) | 318 | 11.9 | -96.3% | -405 to -207 | GAIN |
| consumer lag, most messages waiting at once | 713 | 64 | -91.0% | -933 to -365 | GAIN |
| consumer lag, mean messages waiting | 58.1 | 2 | -96.6% | -73.2 to -38.9 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.66 | +132.8% | 1.4 to 3.92 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.276 | 0.281 | +2.1% | 0.00101 to 0.0106 | power given |
| host CPU-seconds | 492 | 502 | +2.0% | 1.48 to 18.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 6.51 | -12.8% | -1.07 to -0.853 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
