# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1925 messages a second; base rate 288.8/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9888ce5c575a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 724 | +0.1% | -4.49 to 6.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.00782 to 0.00651 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,340 | 2,276 | -2.7% | -719 to 592 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,624 | -3.1% | -1,236 to 1,006 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.56 | 7.49 | -0.9% | -0.175 to 0.036 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 304 | -3.2% | -96.1 to 75.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,259 | 3,238 | -0.6% | -697 to 656 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 262 | -3.5% | -77.2 to 58.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.21 | +10.4% | -0.278 to 0.692 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.323 | 0.325 | +0.6% | -0.0241 to 0.028 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 578 | +0.7% | -41.7 to 49.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.77 | +0.6% | -0.119 to 0.139 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
