# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -1.76 to -0.706 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00803 to 0.00871 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,451 | -3.7% | -300 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,674 | 3,800 | +3.5% | -126 to 380 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.29 | 9.29 | +0.0% | -0.61 to 0.616 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 384 | +0.6% | -5.28 to 9.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,642 | 1,663 | +1.2% | -50.7 to 91.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 166 | +0.7% | -0.492 to 2.85 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.291 | -0.7% | -0.0178 to 0.0138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 204 | -0.6% | -11.8 to 9.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.31 | -0.2% | -0.174 to 0.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
