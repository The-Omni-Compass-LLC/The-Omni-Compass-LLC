# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1928 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 722 | 767 | +6.2% | -129 to 219 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | +0.0% | -0.0142 to 0.0178 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,454 | 1,456 | -40.7% | -3,929 to 1,932 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,900 | 2,288 | -41.3% | -6,443 to 3,219 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.56 | 7.23 | -4.3% | -1.21 to 0.558 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 194 | -41.3% | -521 to 248 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,362 | 2,163 | -35.7% | -4,976 to 2,579 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 168 | -41.3% | -448 to 212 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.31 | +15.6% | -0.41 to 1.03 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.325 | -0.9% | -0.0274 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 584 | 579 | -0.8% | -43.2 to 33.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.68 | -6.2% | -0.375 to 0.15 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
