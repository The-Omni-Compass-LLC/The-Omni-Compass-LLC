# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 340 | -0.5% | -5.91 to 2.35 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | +0.0% | -0.00111 to 0.00788 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,771 | +8.0% | 41.8 to 370 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,747 | 4,009 | +7.0% | 0.367 to 523 | LOSS |
| end-to-end latency, median (ms) | 8.66 | 8.57 | -1.0% | -0.582 to 0.41 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 411 | +6.5% | -28 to 78.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,685 | 1,779 | +5.6% | -2.83 to 191 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 177 | +6.1% | -7.94 to 28.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.284 | -1.1% | -0.0223 to 0.0161 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.0% | -15.7 to 11.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.5% | -0.23 to 0.199 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
