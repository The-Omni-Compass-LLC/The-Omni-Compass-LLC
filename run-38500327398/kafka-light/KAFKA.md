# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.2% | -3.27 to 0.881 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0255 to 0.0105 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,313 | 2,419 | +4.6% | -45.8 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,779 | 3,594 | -4.9% | -674 to 303 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.17 | 7.13 | -0.6% | -0.422 to 0.331 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 312 | +0.2% | -3.43 to 4.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,307 | 3,308 | +0.1% | -48.3 to 51.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 271 | 271 | +0.0% | -4.41 to 4.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.32 | 0.318 | -0.5% | -0.0129 to 0.00943 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 569 | -0.4% | -23.5 to 18.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.73 | -0.2% | -0.0674 to 0.0589 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
