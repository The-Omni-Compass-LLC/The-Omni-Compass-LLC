# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 740 | 739 | -0.2% | -5.06 to 2.08 | no difference beyond the noise |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0399 to 0.00715 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,553 | 1,565 | +0.8% | -149 to 174 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,460 | 2,464 | +0.1% | -51.2 to 57.8 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.24 | 7.92 | -14.3% | -1.89 to -0.763 | better |
| end-to-end latency, mean (ms) | 222 | 222 | +0.1% | -14.7 to 15.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,246 | 2,215 | -1.4% | -130 to 68.4 | no difference beyond the noise |
| consumer lag, mean messages waiting | 198 | 195 | -1.2% | -17.3 to 12.6 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.37 | +18.3% | 0.362 to 0.371 | **WORSE** |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | **WORSE** |
| host CPU busy (share of the run) | 0.292 | 0.293 | +0.2% | -0.0161 to 0.0171 | no difference beyond the noise |
| host CPU-seconds | 348 | 349 | +0.2% | -19.7 to 21.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.57 | 1.57 | +0.4% | -0.0905 to 0.104 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
