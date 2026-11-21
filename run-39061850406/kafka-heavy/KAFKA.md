# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.265 to 0.149 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00326 to 0.00271 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,351 | -1.2% | -103 to 46.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,705 | 3,650 | -1.5% | -405 to 295 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.9 | 11.8 | -0.6% | -0.354 to 0.207 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 314 | -1.4% | -7.53 to -1.1 | GAIN |
| consumer lag, most messages waiting at once | 700 | 683 | -2.4% | -63.7 to 30.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.5 | 57.7 | -1.4% | -1.42 to -0.157 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.293 | -1.5% | -0.0213 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 524 | 517 | -1.5% | -37.1 to 21.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.93 | 7.82 | -1.4% | -0.557 to 0.33 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
