# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 970 messages a second; base rate 109.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 338 | 364 | +7.5% | -83.5 to 134 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.0511 to 0.0626 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,687 | 1,744 | -35.1% | -3,860 to 1,974 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,933 | 2,666 | -32.2% | -5,582 to 3,050 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.81 | 8.51 | -3.4% | -1.04 to 0.437 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 268 | -32.8% | -580 to 318 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,155 | -32.6% | -2,365 to 1,245 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 171 | 114 | -33.7% | -246 to 131 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +15.8% | -0.655 to 1.29 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.286 | 0.294 | +2.6% | -0.00135 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 210 | +2.6% | -1.15 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.23 | -3.7% | -1.01 to 0.766 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
