# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.3/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.2% | -1.94 to 0.724 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.0148 to 0.0129 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,445 | 2,419 | -1.0% | -207 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,712 | 3,768 | +1.5% | -352 to 466 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.02 | 8.03 | +0.1% | -0.183 to 0.201 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 331 | +1.3% | -17.1 to 25.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,735 | +1.8% | -16.9 to 79.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 148 | +2.2% | -6.07 to 12.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.271 | 0.269 | -0.8% | -0.00464 to 0.000172 | EVEN, no difference beyond the noise |
| host CPU-seconds | 485 | 481 | -0.7% | -8.35 to 1.35 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.93 | 2.91 | -0.6% | -0.0556 to 0.0229 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
