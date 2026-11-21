# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.0/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 715 | -1.5% | -38.2 to 16.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0231 to 0.0223 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,187 | 2,270 | +3.8% | -232 to 400 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,462 | 3,603 | +4.1% | -284 to 566 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.24 | -2.9% | -1.62 to 1.13 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 297 | 322 | +8.4% | -58 to 108 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,170 | 3,144 | -0.8% | -244 to 191 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 258 | 279 | +8.3% | -51 to 93.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.13 | +6.3% | -0.417 to 0.669 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.325 | 0.325 | -0.0% | -0.0103 to 0.00997 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 559 | +0.1% | -14.5 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.74 | +1.6% | -0.0172 to 0.0715 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
