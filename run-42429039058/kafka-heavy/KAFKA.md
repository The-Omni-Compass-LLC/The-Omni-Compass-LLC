# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +16.4% | 23.8 to 24.6 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00174 to 0.00101 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,115 | 11.7 | -99.4% | -2,206 to -2,000 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,285 | 15.4 | -99.5% | -3,479 to -3,061 | GAIN |
| end-to-end latency, median (ms) | 10.7 | 10.6 | -0.3% | -0.127 to 0.0547 | STEADY, no difference beyond the noise |
| end-to-end latency, mean (ms) | 277 | 11.5 | -95.8% | -270 to -261 | GAIN |
| consumer lag, most messages waiting at once | 646 | 62 | -90.4% | -721 to -448 | GAIN |
| consumer lag, mean messages waiting | 51.2 | 2.09 | -95.9% | -49.6 to -48.7 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.1 | +105.0% | -0.809 to 5.01 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.253 | 0.258 | +2.0% | 7.67e-05 to 0.00986 | power given |
| host CPU-seconds | 454 | 462 | +1.9% | -0.277 to 17.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.83 | 5.98 | -12.5% | -0.956 to -0.752 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
