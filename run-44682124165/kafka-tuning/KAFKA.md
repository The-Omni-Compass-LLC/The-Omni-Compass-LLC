# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.1/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.1% | 62.7 to 63.3 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.000915 to -0.000267 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,435 | 10.1 | -99.6% | -2,582 to -2,268 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,748 | 12.4 | -99.7% | -3,953 to -3,518 | GAIN |
| end-to-end latency, median (ms) | 8.01 | 7.02 | -12.4% | -1.24 to -0.751 | GAIN |
| end-to-end latency, mean (ms) | 322 | 9.32 | -97.1% | -322 to -305 | GAIN |
| consumer lag, most messages waiting at once | 1,706 | 266 | -84.4% | -1,478 to -1,402 | GAIN |
| consumer lag, mean messages waiting | 143 | 4.29 | -97.0% | -143 to -134 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.4 | +69.8% | 1.07 to 1.73 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.314 | 0.317 | +0.8% | -0.0122 to 0.0172 | STEADY, no difference beyond the noise |
| host CPU-seconds | 578 | 577 | -0.1% | -26.2 to 25.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 2.98 | -14.7% | -0.656 to -0.37 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
