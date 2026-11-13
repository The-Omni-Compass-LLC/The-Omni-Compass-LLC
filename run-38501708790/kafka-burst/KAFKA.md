# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 969 messages a second; base rate 109.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -0.959 to 0.613 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 416 | 417 | +0.2% | -0.879 to 2.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | -0.8% | -213 to 175 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,487 | 3,553 | +1.9% | -422 to 554 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.47 | 9.44 | -0.3% | -0.385 to 0.324 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 362 | 364 | +0.6% | -4.19 to 8.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,550 | 1,545 | -0.4% | -48.5 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 156 | 156 | -0.3% | -7.15 to 6.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.3 | +0.1% | -0.00493 to 0.00558 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 210 | +0.0% | -3.17 to 3.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.42 | +0.2% | -0.0468 to 0.0636 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
