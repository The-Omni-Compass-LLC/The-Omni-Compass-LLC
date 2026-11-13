# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 971 messages a second; base rate 109.2/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -1.57 to 0.776 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.00238 to 0.00859 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,481 | 2,448 | -1.4% | -252 to 185 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,568 | +1.3% | -381 to 471 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.56 | 9.36 | -2.1% | -0.505 to 0.105 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 370 | 369 | -0.2% | -5.79 to 4.12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,619 | 1,580 | -2.4% | -118 to 39.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 159 | 158 | -0.6% | -2.32 to 0.305 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.3 | 0.294 | -2.2% | -0.0289 to 0.016 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 205 | -2.2% | -20.5 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.42 | 3.35 | -2.1% | -0.341 to 0.199 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
