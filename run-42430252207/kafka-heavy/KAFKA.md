# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.2% | 24.5 to 26.3 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.002 to 0.00211 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,440 | 11.9 | -99.5% | -2,577 to -2,279 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,711 | 15.8 | -99.6% | -3,933 to -3,459 | GAIN |
| end-to-end latency, median (ms) | 10.8 | 10.7 | -1.3% | -0.58 to 0.302 | STEADY, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 12.6 | -96.1% | -336 to -285 | GAIN |
| consumer lag, most messages waiting at once | 699 | 82.7 | -88.2% | -704 to -530 | GAIN |
| consumer lag, mean messages waiting | 59 | 2.21 | -96.2% | -61 to -52.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.11 | +105.6% | -0.359 to 4.58 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.262 | 0.268 | +2.4% | -0.0069 to 0.0195 | STEADY, no difference beyond the noise |
| host CPU-seconds | 468 | 479 | +2.3% | -12.5 to 34 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.05 | 6.15 | -12.7% | -1.31 to -0.482 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
