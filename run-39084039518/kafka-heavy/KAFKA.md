# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.11 to 0.726 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.1% | -0.147 to 0.402 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,457 | 2,455 | -0.1% | -72.6 to 70.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,797 | 3,802 | +0.1% | -160 to 170 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | +0.2% | -0.116 to 0.165 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 334 | +1.3% | -7.65 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 690 | 704 | +2.0% | -13.7 to 41.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.3 | 61.5 | +2.0% | -3.42 to 5.88 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.286 | +0.0% | -0.0161 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 505 | 504 | -0.0% | -30.7 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.62 | 7.64 | +0.2% | -0.483 to 0.512 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
