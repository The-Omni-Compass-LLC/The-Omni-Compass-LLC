# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.0% | 61.7 to 63.4 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00674 to 0.0055 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,324 | 8.95 | -99.6% | -2,442 to -2,187 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,584 | 13.2 | -99.6% | -3,834 to -3,307 | GAIN |
| end-to-end latency, median (ms) | 8.08 | 6.56 | -18.8% | -1.63 to -1.41 | GAIN |
| end-to-end latency, mean (ms) | 309 | 7.19 | -97.7% | -306 to -297 | GAIN |
| consumer lag, most messages waiting at once | 1,658 | 84 | -94.9% | -1,790 to -1,358 | GAIN |
| consumer lag, mean messages waiting | 137 | 3.27 | -97.6% | -136 to -132 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.42 | +170.8% | 2.49 to 4.35 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.285 | 0.294 | +3.2% | -0.00445 to 0.023 | STEADY, no difference beyond the noise |
| host CPU-seconds | 508 | 524 | +3.1% | -8.94 to 40.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 2.7 | -11.9% | -0.515 to -0.215 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
