# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -1.52 to 0.52 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0111 to 0.0117 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,444 | 2,432 | -0.5% | -38.9 to 13.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,785 | 3,780 | -0.1% | -556 to 547 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.53 | -0.2% | -0.106 to 0.0704 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 330 | +0.9% | -10.1 to 15.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,713 | +0.5% | -49.3 to 66.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 146 | +0.5% | -6.16 to 7.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.311 | +0.0% | -0.0264 to 0.0265 | EVEN, no difference beyond the noise |
| host CPU-seconds | 540 | 541 | +0.1% | -50.8 to 52.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.28 | 3.29 | +0.3% | -0.295 to 0.312 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
