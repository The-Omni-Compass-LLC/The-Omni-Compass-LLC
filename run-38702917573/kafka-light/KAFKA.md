# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.4/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 723 | -0.4% | -17.5 to 11.9 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.015 to 0.00839 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,244 | 2,258 | +0.6% | -311 to 340 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,655 | 3,563 | -2.5% | -437 to 254 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.27 | -3.3% | -0.741 to 0.18 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 309 | 308 | -0.3% | -34.1 to 32.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,229 | 3,164 | -2.0% | -122 to -7.7 | GAIN |
| consumer lag, mean messages waiting | 268 | 268 | -0.0% | -28.3 to 28.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.1% | -0.419 to 0.664 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.326 | 0.326 | -0.2% | -0.0248 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 559 | -0.2% | -47.7 to 45.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.72 | +0.2% | -0.161 to 0.169 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
