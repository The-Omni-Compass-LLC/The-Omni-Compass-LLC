# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.694 to 0.45 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.0017 to 0.000991 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,297 | -0.3% | -103 to 89.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,566 | 3,577 | +0.3% | -199 to 223 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.4% | -0.181 to 0.0823 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 309 | +0.6% | -17.2 to 20.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 667 | 671 | +0.6% | -40.2 to 48.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.3 | 56.6 | +0.6% | -2.32 to 2.99 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.278 | -1.5% | -0.0186 to 0.00997 | EVEN, no difference beyond the noise |
| host CPU-seconds | 498 | 490 | -1.5% | -32.8 to 17.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.41 | -1.4% | -0.481 to 0.267 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
