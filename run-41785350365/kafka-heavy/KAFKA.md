# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +16.8% | 23.8 to 25.6 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00188 to 0.00137 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,348 | 12.8 | -99.5% | -2,471 to -2,198 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,574 | 69.4 | -98.1% | -3,641 to -3,368 | GAIN |
| end-to-end latency, median (ms) | 11.3 | 11.1 | -1.3% | -0.239 to -0.0479 | GAIN |
| end-to-end latency, mean (ms) | 309 | 16.1 | -94.8% | -309 to -277 | GAIN |
| consumer lag, most messages waiting at once | 668 | 174 | -73.9% | -607 to -380 | GAIN |
| consumer lag, mean messages waiting | 56.6 | 3.09 | -94.5% | -57.3 to -49.8 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.77 | +88.6% | 0.947 to 2.6 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.276 | 0.282 | +2.2% | 0.00232 to 0.00964 | power given |
| host CPU-seconds | 493 | 503 | +2.1% | 3.8 to 16.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.44 | 6.5 | -12.6% | -1.01 to -0.865 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
