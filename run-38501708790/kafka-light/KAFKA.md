# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1944 messages a second; base rate 291.5/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 721 | -0.6% | -21.1 to 12.3 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.015 to 0.00409 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,501 | 2,986 | +19.4% | -1,299 to 2,268 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,807 | 4,559 | +19.8% | -1,401 to 2,905 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.4 | 7.38 | -0.3% | -0.267 to 0.218 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 340 | 412 | +21.3% | -168 to 313 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,456 | 3,928 | +13.6% | -1,201 to 2,144 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 296 | 357 | +20.8% | -142 to 265 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.4% | -0.0106 to -0.00421 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.5% | -0.00494 to 0.00788 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 566 | +0.7% | -7.62 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.74 | +1.3% | -0.0509 to 0.0953 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
