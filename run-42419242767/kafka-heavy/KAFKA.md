# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.6% | 24.9 to 26.8 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00328 to 0.0021 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,569 | 12.6 | -99.5% | -2,678 to -2,434 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,893 | 43.2 | -98.9% | -4,009 to -3,690 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.4% | -0.301 to -0.265 | GAIN |
| end-to-end latency, mean (ms) | 345 | 13.4 | -96.1% | -353 to -311 | GAIN |
| consumer lag, most messages waiting at once | 715 | 99 | -86.2% | -739 to -493 | GAIN |
| consumer lag, mean messages waiting | 62.6 | 2.46 | -96.1% | -63.7 to -56.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.26 | +113.2% | 1.71 to 2.82 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.287 | 0.294 | +2.4% | -0.00128 to 0.0151 | STEADY, no difference beyond the noise |
| host CPU-seconds | 508 | 519 | +2.3% | -2.66 to 25.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.66 | 6.67 | -13.0% | -1.22 to -0.774 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
