# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +17.0% | 24 to 25.9 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00286 to 0.00179 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,236 | 11.9 | -99.5% | -2,360 to -2,087 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,462 | 16.5 | -99.5% | -3,791 to -3,100 | GAIN |
| end-to-end latency, median (ms) | 11.1 | 11 | -0.8% | -0.104 to -0.0739 | GAIN |
| end-to-end latency, mean (ms) | 297 | 11.4 | -96.2% | -307 to -265 | GAIN |
| consumer lag, most messages waiting at once | 659 | 41 | -93.8% | -703 to -534 | GAIN |
| consumer lag, mean messages waiting | 54.5 | 1.99 | -96.4% | -57.2 to -47.8 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.05 | +102.3% | -0.149 to 4.24 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.287 | 0.288 | +0.5% | -0.00129 to 0.00394 | STEADY, no difference beyond the noise |
| host CPU-seconds | 523 | 524 | +0.1% | -4.27 to 5.51 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.9 | 6.77 | -14.4% | -1.27 to -1.01 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
