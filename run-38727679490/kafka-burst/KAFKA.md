# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.1% | -1.28 to 0.446 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0393 to 0.0406 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,511 | -0.2% | -86.3 to 76.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,795 | 3,699 | -2.5% | -789 to 598 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.78 | 9.67 | -1.1% | -1.91 to 1.7 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 384 | -0.1% | -20.1 to 19.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,654 | 1,656 | +0.1% | -17.6 to 22.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 166 | +0.3% | -7.5 to 8.45 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.31 | 0.302 | -2.6% | -0.043 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 212 | -2.6% | -30.2 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.45 | -2.5% | -0.493 to 0.316 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
