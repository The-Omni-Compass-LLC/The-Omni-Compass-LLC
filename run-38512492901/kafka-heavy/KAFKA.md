# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 388 messages a second; base rate 58.3/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 154 | +5.7% | -27.7 to 44.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00207 to 0.00443 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,150 | 1,383 | -35.7% | -3,813 to 2,278 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,459 | 2,143 | -38.0% | -5,984 to 3,351 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -1.6% | -0.472 to 0.117 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 290 | 186 | -35.7% | -507 to 299 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 640 | 433 | -32.4% | -1,036 to 622 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52.9 | 34 | -35.7% | -93.8 to 56.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.36 | +18.0% | -0.506 to 1.23 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.28 | 0.274 | -1.9% | -0.00803 to -0.00253 | GAIN |
| host CPU-seconds | 501 | 491 | -1.9% | -14.5 to -4.51 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 7.62 | 7.1 | -6.8% | -2.2 to 1.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
