# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 965 messages a second; base rate 144.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 364 | 424 | +16.7% | 50.1 to 71.2 | GAIN |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.00677 to 0.00473 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,158 | 9.79 | -99.5% | -3,000 to -1,296 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,376 | 23.9 | -99.3% | -4,247 to -2,458 | GAIN |
| end-to-end latency, median (ms) | 8.23 | 7.2 | -12.6% | -1.27 to -0.797 | GAIN |
| end-to-end latency, mean (ms) | 284 | 8.08 | -97.2% | -394 to -158 | GAIN |
| consumer lag, most messages waiting at once | 1,565 | 112 | -92.9% | -1,999 to -907 | GAIN |
| consumer lag, mean messages waiting | 124 | 3.56 | -97.1% | -170 to -71.7 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.95 | +147.5% | 1.44 to 4.46 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.297 | 0.311 | +4.7% | 0.0127 to 0.0151 | power given |
| host CPU-seconds | 528 | 552 | +4.6% | 22.6 to 25.5 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 2.89 | -10.4% | -0.434 to -0.238 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
