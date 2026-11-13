# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -2.89 to 2.29 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0191 to 0.0241 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,575 | 2,573 | -0.1% | -328 to 324 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,901 | 3,782 | -3.1% | -476 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.59 | 9.59 | -0.0% | -0.49 to 0.486 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 394 | 389 | -1.3% | -32.8 to 22.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 1,689 | -0.6% | -26.9 to 6.21 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 171 | 169 | -1.3% | -16.6 to 12.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.296 | -1.7% | -0.0204 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 207 | -1.6% | -14.3 to 7.33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.37 | -1.6% | -0.215 to 0.109 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
