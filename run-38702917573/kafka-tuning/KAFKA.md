# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.96 to 1.39 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00881 to 0.00278 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,403 | 2,372 | -1.3% | -241 to 180 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,659 | 3,752 | +2.6% | -251 to 439 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.43 | 8.4 | -0.3% | -0.0849 to 0.0309 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 315 | -0.0% | -19.5 to 19.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,678 | 1,665 | -0.7% | -46.1 to 21.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 139 | -0.4% | -8.76 to 7.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.314 | -0.7% | -0.0143 to 0.00983 | EVEN, no difference beyond the noise |
| host CPU-seconds | 564 | 560 | -0.6% | -24.8 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.4 | -0.5% | -0.133 to 0.0983 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
